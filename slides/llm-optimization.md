---
layout: farshid_default
title: "New LLM Optimization Methods — Run Local & Fast"
tags:
  - presentation
  - llm
  - optimization
  - inference
  - quantization
  - speculative-decoding
  - qwen
hashtags: "#llm #optimization #quantization #speculative-decoding #mlx #qwen #research"
excerpt: "Every method to run big LLMs fast and small — quantization (Unsloth Dynamic 3.0), multi-token prediction, DFlash2, oMLX/MLX, FlashAttention-2 — with visualizations and a Qwen3.8-Flash synthesis."
---

<section data-background-color="#0b1220">
  <div style="background:radial-gradient(900px 400px at 30% 20%, rgba(56,189,248,.18), transparent), radial-gradient(700px 380px at 80% 70%, rgba(168,85,247,.16), transparent); padding:34px 40px; border-radius:18px;">
    <div style="font-size:.6em; letter-spacing:.18em; color:#67e8f9; text-transform:uppercase;">Inference Engineering · 2026</div>
    <h1 style="font-size:2.0em; margin:.18em 0 .1em; background:linear-gradient(90deg,#38bdf8,#a855f7,#22d3ee); -webkit-background-clip:text; background-clip:text; color:transparent;">New LLM Optimization Methods</h1>
    <p style="font-size:.82em; color:#cbd5e1; max-width:760px;">How to run frontier-scale models on a laptop, a single GPU, or Apple Silicon — fast and cheap. One method per page, with a visualization, then a synthesis for the <b>Qwen3.8-Flash</b> class.</p>
    <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:18px;">
      <div class="strip"><b>5</b><span>core methods</span></div>
      <div class="strip"><b>2×–10×</b><span>typical speedup</span></div>
      <div class="strip"><b>1-bit</b><span>to 4-bit viable</span></div>
      <div class="strip"><b>Qwen3.8</b><span>target model</span></div>
    </div>
  </div>
</section>

<section data-background-color="#0b1220">
  <h2>The Bottleneck: Where the Cost Lives</h2>
  <div class="m-3">
    <div>
      <h3 style="color:#38bdf8;">Memory (weights + KV cache)</h3>
      <p>Model size dominates. 27B @ BF16 ≈ 54 GB. Quantization shrinks weights; KV-cache grows with context length.</p>
      <div class="code-box" style="font-size:.56em;">
W = weights,  KV = past-key/value
RAM ≈ params×bits + seq×layers×2×d_model×2
27B×16b = 54 GB   →   27B×4b = 13.5 GB
      </div>
    </div>
    <div>
      <h3 style="color:#a855f7;">Compute (decode loop)</h3>
      <p>Autoregressive: 1 token per forward pass. Each pass is a big matmul over all weights — bandwidth-bound on most hardware.</p>
      <div class="code-box" style="font-size:.56em;">
for t in range(N):              # N sequential passes
    logits = model(x[:, -1:])   # full-weight matmul
    x = cat(x, sample(logits))
      </div>
    </div>
    <div>
      <h3 style="color:#22d3ee;">Attention IO</h3>
      <p>Naive attention materializes N×N scores → quadratic memory + HBM traffic. FlashAttention fixes this at the kernel level.</p>
      <div class="code-box" style="font-size:.56em;">
standard:  S = QKᵀ  (N×N, stored to HBM)
flash:     tile→SRAM, online softmax, never materialize S
      </div>
    </div>
  </div>
  <p style="text-align:center; color:#94a3b8; font-size:.6em;">Three levers → three families of optimization: <b>shrink weights</b>, <b>draft many tokens per pass</b>, <b>fuse the kernel</b>.</p>
</section>

<section data-background-color="#0b1220">
  <h2>1 · Unsloth Dynamic 3.0 — Smart Quantization <span class="tag p">PTQ</span></h2>
  <div class="m-2">
    <div>
      <h3 style="color:#a855f7;">What it does</h3>
      <p>Post-training quantization that assigns <b>different bit-widths per layer/tensor</b>. Important tensors stay at 8/16-bit; unimportant ones drop to 1–2-bit. Pure PTQ — no QAT/QAD, no training on the calibration set.</p>
      <ul style="font-size:.62em;">
        <li>Improved <b>imatrix calibration</b> tuned for agentic coding, chat, multilingual</li>
        <li>Per-model, per-layer quantization schemes</li>
        <li>Ships as GGUF (llama.cpp, Ollama) and safetensors</li>
        <li>New metric <b>Divergence-300@32</b>: 32-token trajectory vs BF16</li>
      </ul>
    </div>
    <div>
      <h3 style="color:#22d3ee;">Qwen3.8-27B results</h3>
      <div class="code-box" style="font-size:.58em;">
Quant          Size      Top-1      vs others
UD-IQ1_S       6.2 GB    ~72%       -89% size
UD-Q2_K_XL     9.83 GB   +8%        best agent tier
UD-Q4_0        ~13 GB    higher     MTP optional
>10% Top-1 better at same disk vs other providers
      </div>
      <div class="vis" style="font-size:.52em; margin-top:10px;">
        <div class="bar"><span style="width:18%; background:#a855f7;">IQ1_S</span></div>
        <div class="bar"><span style="width:28%; background:#7c3aed;">Q2_K_XL</span></div>
        <div class="bar"><span style="width:37%; background:#38bdf8;">Q4_0</span></div>
        <div class="bar"><span style="width:100%; background:#334155;">BF16 (54GB)</span></div>
      </div>
      <p style="font-size:.5em; color:#94a3b8;">Bar width ∝ disk size. Lower bars = runs on consumer HW.</p>
    </div>
  </div>
</section>

<section data-background-color="#0b1220">
  <h2>2 · Multi-Token Prediction (MTP) — Self-Speculative <span class="tag">decode</span></h2>
  <div class="m-2">
    <div>
      <h3 style="color:#38bdf8;">Mechanism</h3>
      <p>A tiny <b>draft head</b> baked into the model (e.g. Qwen3.5/3.6 ship <code>mtp.*</code>, 1 transformer layer) predicts t+2, t+3 … cheaply. The main model verifies them in <b>one</b> extra forward pass and accepts the longest matching prefix.</p>
      <div class="code-box" style="font-size:.56em;">
t2,t3 = mtp_head(hidden_t, emb(t1))   # draft
L     = model([t1,t2,t3], kv=shared)  # verify (1 pass)
accept longest prefix where argmax(L)==draft
      </div>
    </div>
    <div>
      <h3 style="color:#22d3ee;">Why it is "free tokens"</h3>
      <div class="vis" style="font-size:.54em;">
        <div class="flow">
          <div class="node">t₁<br><small>main</small></div>
          <div class="arrow">→ draft →</div>
          <div class="node ok">t₂ t₃<br><small>MTP head</small></div>
          <div class="arrow">→ 1 verify pass →</div>
          <div class="node ok">accept 2<br><small>2 tok / 1 pass</small></div>
        </div>
      </div>
      <ul style="font-size:.58em;">
        <li>Qwen3.5: <b>~70 → 131 tok/s</b> (GB10), <b>1.5–1.6×</b> on M4 Pro</li>
        <li>Acceptance ~80–88% (temp 0–1); lossless (greedy verify)</li>
        <li>Sweet spot: depth <b>1</b> on Apple Silicon, n_max <b>2–3</b> on CUDA</li>
        <li>No separate draft model; works only on MTP-shipped checkpoints</li>
      </ul>
    </div>
  </div>
</section>

<section data-background-color="#0b1220">
  <h2>3 · DFlash2 — Parallel Speculative Decoding <span class="tag p">z-lab / Inco AI</span></h2>
  <div class="m-2">
    <div>
      <h3 style="color:#a855f7;">Block-diffusion drafter</h3>
      <p>Unlike sequential drafters, DFlash2 proposes the <b>whole draft block in one parallel pass</b> via a small block-diffusion network. A <b>path selector</b> keeps top-16 candidates per slot; a <b>two-tap conv</b> keeps coherence. Adds ~2M+16.5M params, ~1.3% latency.</p>
      <ul style="font-size:.6em;">
        <li>+21% acceptance length over DFlash</li>
        <li>Runs on SGLang, vLLM, llama.cpp (PR #27342), oMLX</li>
        <li>MLX build for Apple Silicon (Qwen3.8-27B)</li>
      </ul>
    </div>
    <div>
      <h3 style="color:#22d3ee;">Measured speedup</h3>
      <div class="code-box" style="font-size:.56em;">
Setup                     Base    DFlash2   ×speed
A100 (Qwen3.8-27B)        28.9    59.1       ~2.0×
Apple M5 Pro Q4_K_M      10.42   19.31      1.85×
RTX 5050 (8GB, starved)   6.8     11.6       1.7×
      </div>
      <div class="vis" style="font-size:.5em; margin-top:8px;">
        <div class="bar"><span style="width:35%; background:#334155;">baseline</span></div>
        <div class="bar"><span style="width:100%; background:#a855f7;">DFlash2 ~2×</span></div>
      </div>
      <p style="font-size:.5em; color:#94a3b8;">Biggest gain when baseline is compute/VRAM-starved.</p>
    </div>
  </div>
</section>

<section data-background-color="#0b1220">
  <h2>4 · oMLX / MLX — Apple-Silicon Native Runtime <span class="tag">runtime</span></h2>
  <div class="m-2">
    <div>
      <h3 style="color:#38bdf8;">Unified memory advantage</h3>
      <p>MLX (Apple ML Research) keeps tensors in <b>shared memory</b> — no CPU↔GPU copy. On 128 GB M-series, a 27B model sits fully resident and bandwidth-efficient, so quantized + MTP/DFlash overhead is amortized.</p>
      <div class="code-box" style="font-size:.56em;">
pip install mlx-lm
mlx_lm.generate --model Qwen3.8-27B-4bit --mtp
mlx_lm.server   --model Qwen3.8-27B-4bit --mtp
      </div>
      <p style="font-size:.56em;">oMLX = optimized local MLX serving stack (e.g. Qwen3.5-4B-OptiQ on 127.0.0.1:8000).</p>
    </div>
    <div>
      <h3 style="color:#22d3ee;">Why it matters for these methods</h3>
      <ul style="font-size:.6em;">
        <li>Native <b>MTP</b> in mlx-lm (#990): 1.5× Qwen3.6-27B on M4 Pro</li>
        <li>DFlash2 ships an <b>oMLX build</b> for Apple Silicon</li>
        <li>Lazy eval + dynamic graphs → no recompile per shape</li>
        <li>Skip MTP below ~4B (overhead &gt; gain); use 4B+ for wins</li>
      </ul>
      <div class="vis" style="font-size:.5em; margin-top:6px;">
        <div class="flow">
          <div class="node">weights<br><small>unified</small></div>
          <div class="arrow">→ no copy →</div>
          <div class="node ok">GPU+CPU<br><small>same RAM</small></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section data-background-color="#0b1220">
  <h2>5 · FlashAttention-2 — IO-Aware Kernel <span class="tag p">foundation</span></h2>
  <div class="m-2">
    <div>
      <h3 style="color:#38bdf8;">The kernel everything rides on</h3>
      <p>Exact (no approximation) attention that tiles Q/K/V into SRAM, does online softmax, and <b>never writes the N×N score matrix to HBM</b>. Memory becomes <b>linear</b> in sequence length; the decode matmul stays bandwidth-bound, not memory-bound.</p>
      <div class="code-box" style="font-size:.56em;">
FlashAttention : 2–4× faster, 10–20× less memory (linear)
FlashAttention-2: +2× again → up to 73% A100 FLOPs
  · split Q across warps (not K/V) → less shared-mem traffic
  · parallelize over sequence length
  · supports head_dim≤256, MQA/GQA
      </div>
    </div>
    <div>
      <h3 style="color:#22d3ee;">Impact on the other 4 methods</h3>
      <div class="vis" style="font-size:.54em;">
        <div class="bar"><span style="width:100%; background:#334155;">naive attn (quadratic)</span></div>
        <div class="bar"><span style="width:42%; background:#38bdf8;">FlashAttn</span></div>
        <div class="bar"><span style="width:22%; background:#22d3ee;">FlashAttn-2</span></div>
      </div>
      <ul style="font-size:.56em;">
        <li>Speculative methods (MTP/DFlash2) verify a <b>batch</b> of draft tokens — FlashAttn-2 makes that batched verify nearly free</li>
        <li>Long-context KV cache stays small enough to keep on-chip</li>
        <li>Underpins vLLM, SGLang, llama.cpp, MLX backends</li>
      </ul>
    </div>
  </div>
</section>

<section data-background-color="#0b1220">
  <h2>Method Map — Where Each Lever Hits</h2>
  <div class="m-3">
    <div class="card"><h3 style="color:#a855f7;">Shrink weights</h3><p style="font-size:.6em;">Unsloth Dynamic 3.0 → fits 27B in 6–14 GB.</p></div>
    <div class="card"><h3 style="color:#38bdf8;">Draft tokens</h3><p style="font-size:.6em;">MTP (self) + DFlash2 (parallel) → 1.5–2× decode.</p></div>
    <div class="card"><h3 style="color:#22d3ee;">Fuse kernel</h3><p style="font-size:.6em;">FlashAttention-2 → linear memory, free batched verify.</p></div>
    <div class="card"><h3 style="color:#67e8f9;">Run natively</h3><p style="font-size:.6em;">oMLX/MLX → unified memory removes copy cost.</p></div>
  </div>
  <p style="text-align:center; color:#94a3b8; font-size:.58em;">Stack them: <b>quantize → load in MLX → enable MTP/DFlash2 → rely on FlashAttn-2 under the hood</b>.</p>
</section>

<section data-background-color="#0b1220">
  <h2>Synthesis — Qwen3.8-Flash: Stack the Stack</h2>
  <div style="background:linear-gradient(135deg, rgba(56,189,248,.12), rgba(168,85,247,.12)); border:1px solid #1e293b; border-radius:14px; padding:18px 22px;">
    <p style="font-size:.7em; color:#e2e8f0;">The <b>Qwen3.8-Flash</b> class (next-gen small/fast variant) is the ideal target for the full stack. Concrete recipe for a 27B-class model on a single Apple-Silicon or 24 GB GPU box:</p>
    <div class="m-2" style="margin-top:10px;">
      <div>
        <ol style="font-size:.6em; line-height:1.5;">
          <li><b>Quantize</b> with Unsloth Dynamic 3.0 → <code>UD-Q4_K_M</code> (~13 GB) or <code>UD-Q2_K_XL</code> (~9.8 GB, best agent tier).</li>
          <li><b>Load</b> via oMLX / mlx-lm (unified memory) — no CPU↔GPU copies.</li>
          <li><b>Enable MTP</b> (<code>--mtp</code>); depth 1 on Metal, n_max 2–3 on CUDA → +1.5× decode.</li>
          <li><b>Add DFlash2</b> drafter when VRAM allows → up to +2×; pairs with MTP on llama.cpp.</li>
          <li><b>FlashAttention-2</b> is automatic in the backend — keeps long context cheap.</li>
        </ol>
      </div>
      <div>
        <div class="code-box" style="font-size:.56em;">
# Apple Silicon, 27B, ~2× throughput
mlx_lm.server --model Qwen3.8-27B-4bit \
              --mtp

# CUDA / llama.cpp, chain drafters
llama-server -m Qwen3.8-27B-UD-Q4_K_M.gguf \
  --spec-type draft-mtp --spec-draft-n-max 3 \
  --spec-draft dflash2-q8  # optional
        </div>
        <p style="font-size:.52em; color:#94a3b8;">Expected: BF16-class quality at 4-bit, 1.5–2× faster, runs on a laptop or single GPU.</p>
      </div>
    </div>
  </div>
  <p style="font-size:.5em; color:#64748b; text-align:center;">Numbers are from vendor/repro benchmarks (Unsloth, z-lab, mlx-lm, Dao et al.); real throughput is hardware- and prompt-dependent.</p>
</section>

<section data-background-color="#0b1220">
  <h1>Thank You & Discussion</h1>
  <p style="text-align:center; color:#94a3b8; font-size:.7em;">Quantize smart · Draft in parallel · Fuse the kernel · Run native</p>
  <p style="text-align:center; font-size:.6em; margin-top:8px;"><a href="/notes/slides/" style="color:#38bdf8;">← All presentations</a> · <a href="/notes/slides/research-tools/" style="color:#a855f7;">New Era of Research Tools</a></p>
</section>
