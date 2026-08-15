---
layout: farshid_default
permalink: /crypto/
title: "Crypto Payments — Support"
description: "Support Dr. Farshid Pirahansiah's open-source computer vision and edge AI work with cryptocurrency. Bitcoin, Ethereum, Solana, Base and BNB Smart Chain wallet addresses."
tags: [crypto, bitcoin, ethereum, solana, base, bnb, donations, support]
hashtags: "#crypto #bitcoin #ethereum #solana #base #bnb #donate #web3"
---

> **Crypto Payments** — Support open-source computer vision and edge AI work with cryptocurrency. — https://www.pirahansiah.com/notes/docs/crypto/

<style>
.crypto-hero {
  text-align: center;
  padding: 48px 24px 28px;
}
.crypto-hero h1 {
  font-size: 2.5rem;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 12px;
  background: linear-gradient(135deg, #0a84ff 0%, #bf5af2 50%, #ff375f 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.crypto-hero p {
  color: var(--text-muted);
  font-size: 1.12rem;
  max-width: 680px;
  margin: 0 auto;
  line-height: 1.65;
}
.crypto-note {
  max-width: 720px;
  margin: 18px auto 0;
  padding: 14px 18px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--text-muted);
  font-size: 0.92rem;
  line-height: 1.6;
}
.crypto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  padding: 8px 16px 40px;
  max-width: 1200px;
  margin: 0 auto;
}
.wallet-card {
  border-radius: 18px;
  padding: 24px 20px;
  text-align: center;
  background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}
.wallet-card:hover {
  transform: translateY(-4px);
  border-color: rgba(90, 200, 250, 0.5);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35);
}
.wallet-card .coin {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-bottom: 16px;
}
.wallet-card .coin .ticker {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: 0.5px;
}
.wallet-card .coin .chain {
  font-size: 0.82rem;
  color: var(--text-muted);
  background: rgba(255, 255, 255, 0.08);
  padding: 3px 10px;
  border-radius: 999px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}
.wallet-card .qr {
  width: 140px;
  height: 140px;
  margin: 0 auto 16px;
  border-radius: 12px;
  background: #fff;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.wallet-card .qr img {
  width: 124px;
  height: 124px;
  display: block;
}
.wallet-card .addr {
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
  font-size: 0.78rem;
  line-height: 1.5;
  word-break: break-all;
  color: #c9d4e3;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 10px 12px;
  margin-bottom: 14px;
  min-height: 58px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.wallet-card .copy-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 9px 20px;
  background: linear-gradient(135deg, #0a84ff, #5ac8fa);
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 0.9rem;
  font-weight: 700;
  cursor: pointer;
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.wallet-card .copy-btn:hover { opacity: 0.9; transform: scale(1.03); }
.wallet-card .copy-btn.copied { background: linear-gradient(135deg, #34c759, #30d158); }
</style>

<div class="crypto-hero">
  <h1>Support via Crypto</h1>
  <p>If my open-source computer vision and edge AI work has helped you, you can support it directly with cryptocurrency. Every contribution funds research, tutorials, and open-source tooling.</p>
  <div class="crypto-note">
    <strong>Note:</strong> Ethereum, Base and BNB Smart Chain share the same EVM address
    (<code style="font-family:ui-monospace,monospace;color:#5ac8fa;">0xFcE7&hellip;53B0C</code>).
    Always send assets on the network you intend &mdash; verify the chain before confirming any transaction.
  </div>
</div>

<div class="crypto-grid">

  <div class="wallet-card">
    <div class="coin"><span class="ticker">&#9874; ETH</span><span class="chain">Ethereum</span></div>
    <div class="qr"><img src="{{ '/assets/qr/eth.svg' | relative_url }}" alt="Ethereum QR code" loading="lazy"></div>
    <div class="addr">0xFcE78486AE65e006Dc0d235FDD5d1E9169D53B0C</div>
    <button class="copy-btn" data-addr="0xFcE78486AE65e006Dc0d235FDD5d1E9169D53B0C">Copy address</button>
  </div>

  <div class="wallet-card">
    <div class="coin"><span class="ticker">&#8383; BTC</span><span class="chain">Bitcoin</span></div>
    <div class="qr"><img src="{{ '/assets/qr/btc.svg' | relative_url }}" alt="Bitcoin QR code" loading="lazy"></div>
    <div class="addr">bc1q922uu6uwu3x2grlkypeuyywet9msk2fzxypy6d</div>
    <button class="copy-btn" data-addr="bc1q922uu6uwu3x2grlkypeuyywet9msk2fzxypy6d">Copy address</button>
  </div>

  <div class="wallet-card">
    <div class="coin"><span class="ticker">&#9670; SOL</span><span class="chain">Solana</span></div>
    <div class="qr"><img src="{{ '/assets/qr/sol.svg' | relative_url }}" alt="Solana QR code" loading="lazy"></div>
    <div class="addr">DPfX2mNvCqQuosQLe4nDBQRf8ZdNfS5LA4tvSsGPyCH4</div>
    <button class="copy-btn" data-addr="DPfX2mNvCqQuosQLe4nDBQRf8ZdNfS5LA4tvSsGPyCH4">Copy address</button>
  </div>

  <div class="wallet-card">
    <div class="coin"><span class="ticker">&#9650; BASE</span><span class="chain">Base</span></div>
    <div class="qr"><img src="{{ '/assets/qr/base.svg' | relative_url }}" alt="Base QR code" loading="lazy"></div>
    <div class="addr">0xFcE78486AE65e006Dc0d235FDD5d1E9169D53B0C</div>
    <button class="copy-btn" data-addr="0xFcE78486AE65e006Dc0d235FDD5d1E9169D53B0C">Copy address</button>
  </div>

  <div class="wallet-card">
    <div class="coin"><span class="ticker">&#9679; BNB</span><span class="chain">BNB Smart Chain</span></div>
    <div class="qr"><img src="{{ '/assets/qr/bnb.svg' | relative_url }}" alt="BNB Smart Chain QR code" loading="lazy"></div>
    <div class="addr">0xFcE78486AE65e006Dc0d235FDD5d1E9169D53B0C</div>
    <button class="copy-btn" data-addr="0xFcE78486AE65e006Dc0d235FDD5d1E9169D53B0C">Copy address</button>
  </div>

</div>

<script>
(function () {
  var btns = document.querySelectorAll('.copy-btn');
  function fallbackCopy(text, done) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); done(); } catch (e) { done(); }
    document.body.removeChild(ta);
  }
  btns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var addr = btn.getAttribute('data-addr');
      var onDone = function () {
        var original = btn.textContent;
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        setTimeout(function () { btn.textContent = original; btn.classList.remove('copied'); }, 1800);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(addr).then(onDone, function () { fallbackCopy(addr, onDone); });
      } else {
        fallbackCopy(addr, onDone);
      }
    });
  });
})();
</script>
