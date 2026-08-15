---
layout: farshid_default
permalink: /metamask/
title: "MetaMask — Connect & Receive"
description: "Connect MetaMask to auto-fill your EVM address, or select a token to reveal its receive address. Private test page."
sitemap: false
noindex: true
---

> **MetaMask Connect** — Connect your wallet and get your receive address + QR code. — https://pirahansiah.com/metamask/

<style>
.mm-hero { text-align: center; padding: 32px 16px 4px; }
.mm-hero h1 { font-size: 2rem; margin: 0 0 8px; }
.mm-hero p { color: var(--text-muted); margin: 0 auto 4px; max-width: 640px; }

/* --- connect bar --- */
.mm-connect-bar { max-width: 520px; margin: 18px auto 0; padding: 0 16px; text-align: center; }
.mm-btn {
  display: inline-block; padding: 12px 26px; border: none; border-radius: 12px; cursor: pointer;
  font-size: 1rem; font-weight: 600; color: #fff;
  background: linear-gradient(135deg, var(--farshid-blue), var(--farshid-purple));
  box-shadow: 0 4px 18px rgba(10,132,255,0.35); transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.mm-btn:hover { transform: translateY(-1px); box-shadow: 0 6px 22px rgba(10,132,255,0.45); }
.mm-btn.ghost { background: var(--glass-bg-strong); box-shadow: none; }
.mm-connected {
  display: none; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap;
  padding: 12px 16px; border-radius: 14px; background: var(--glass-bg); border: 1px solid var(--glass-border);
  font-size: 0.9rem;
}
.mm-connected .acct { font-family: ui-monospace, monospace; color: #7ee0a3; }
.mm-connected .bal { color: var(--text-muted); }
.mm-err {
  margin-top: 12px; padding: 12px; border-radius: 10px;
  background: rgba(255,55,95,0.15); border: 1px solid rgba(255,55,95,0.4);
  color: #ff8a9b; font-size: 0.88rem; display: none;
}

/* --- disclaimers --- */
.crypto-warnings { max-width: 760px; margin: 22px auto 6px; padding: 0 16px; display: grid; gap: 12px; }
.warn-box {
  display: flex; gap: 12px; align-items: flex-start;
  border-radius: 14px; padding: 14px 16px; font-size: 0.92rem; line-height: 1.6;
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
}
.warn-box .warn-icon { font-size: 1.2rem; line-height: 1.4; flex-shrink: 0; }
.warn-box b { display: block; margin-bottom: 2px; }
.warn-box.warning { background: rgba(255,59,48,0.10); border: 1px solid rgba(255,59,48,0.38); color: #ffb3b8; }
.warn-box.warning b { color: #ff6961; }
.warn-box.caution { background: rgba(255,149,0,0.10); border: 1px solid rgba(255,159,10,0.38); color: #ffd9a0; }
.warn-box.caution b { color: #ffb340; }
.warn-box.note { background: rgba(10,132,255,0.10); border: 1px solid rgba(10,132,255,0.38); color: #bcd9ff; }
.warn-box.note b { color: #5ac8fa; }
.warn-box.when { background: rgba(48,209,88,0.09); border: 1px solid rgba(48,209,88,0.36); color: #b7e8c7; }
.warn-box.when b { color: #30d158; }
.warn-box code { font-family: ui-monospace, monospace; color: #5ac8fa; }

/* --- token selector --- */
.crypto-selector { max-width: 760px; margin: 26px auto 0; padding: 0 16px; display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
.token-pill {
  padding: 9px 18px; border-radius: 999px; cursor: pointer; font-size: 0.9rem; font-weight: 700;
  color: var(--text-muted); background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.14);
  transition: all 0.18s ease;
}
.token-pill:hover { border-color: rgba(90,200,250,0.5); color: var(--text); }
.token-pill.active { color: #fff; border-color: transparent; background: linear-gradient(135deg, #0a84ff, #bf5af2); box-shadow: 0 4px 16px rgba(10,132,255,0.35); }

/* --- wallet panel --- */
.crypto-panel {
  max-width: 440px; margin: 22px auto 40px; padding: 26px 22px; border-radius: 20px; text-align: center;
  background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.12);
  backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
}
.panel-head { display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 6px; }
.panel-head .ticker { font-size: 1.6rem; font-weight: 800; letter-spacing: 0.5px; }
.panel-head .chain { font-size: 0.8rem; color: var(--text-muted); background: rgba(255,255,255,0.08); padding: 3px 10px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.1); }
.panel-network { color: var(--text-muted); font-size: 0.82rem; margin-bottom: 14px; }
.panel-live { display: none; color: #30d158; font-size: 0.78rem; margin-bottom: 10px; }
.crypto-panel .qr { width: 168px; height: 168px; margin: 0 auto 16px; border-radius: 12px; background: #fff; padding: 10px; display: flex; align-items: center; justify-content: center; }
.crypto-panel .qr img { width: 148px; height: 148px; display: block; }
.crypto-panel .qr canvas { display: none; }
.crypto-panel .addr {
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
  font-size: 0.8rem; line-height: 1.5; word-break: break-all; color: #c9d4e3;
  background: rgba(0,0,0,0.28); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 12px; margin-bottom: 16px;
}
.copy-btn {
  display: inline-flex; align-items: center; gap: 8px; padding: 10px 22px;
  background: linear-gradient(135deg, #0a84ff, #5ac8fa); color: #fff; border: none; border-radius: 10px;
  font-size: 0.92rem; font-weight: 700; cursor: pointer; transition: opacity 0.2s ease, transform 0.2s ease;
}
.copy-btn:hover { opacity: 0.9; transform: scale(1.03); }
.copy-btn.copied { background: linear-gradient(135deg, #34c759, #30d158); }
.panel-warn { margin-top: 16px; font-size: 0.8rem; color: #ffb340; line-height: 1.5; }
.mm-note { color: var(--text-muted); font-size: 0.8rem; margin: 20px auto 0; text-align: center; max-width: 560px; padding-bottom: 40px; }
</style>

<div class="mm-hero">
  <h1>MetaMask — Connect &amp; Receive</h1>
  <p>Connect your wallet to auto-fill your EVM address, or select a token below to reveal its receive address.</p>
</div>

<div class="mm-connect-bar">
  <button class="mm-btn" id="mm-connect-btn" type="button">Connect MetaMask</button>
  <div class="mm-connected" id="mm-connected">
    <span class="acct" id="mm-acct"></span>
    <span class="bal" id="mm-bal"></span>
    <button class="mm-btn ghost" id="mm-disconnect" type="button">Disconnect</button>
  </div>
  <div class="mm-err" id="mm-err"></div>
</div>

<div class="crypto-warnings">
  <div class="warn-box warning">
    <span class="warn-icon">&#9888;&#65039;</span>
    <div><b>Warning — transfers are irreversible</b>
    Crypto transactions cannot be reversed, refunded, or recovered once confirmed. There is no chargeback and no support line that can undo a transfer. Double-check everything before you send.</div>
  </div>
  <div class="warn-box caution">
    <span class="warn-icon">&#9888;&#65039;</span>
    <div><b>Caution — send on the correct network</b>
    Ethereum, Base and BNB Smart Chain share the same address (<code>0xFcE7&hellip;53B0C</code>). Sending on the wrong network — for example Base instead of Ethereum — can permanently lose your funds. Always verify the network in your wallet before confirming.</div>
  </div>
  <div class="warn-box note">
    <span class="warn-icon">&#8505;&#65039;</span>
    <div><b>Note — voluntary, no invoice</b>
    This page is a voluntary support option, not a purchase or invoice. Crypto payments are final with no automatic receipt or confirmation. If you are unsure, send a small test amount first.</div>
  </div>
  <div class="warn-box when">
    <span class="warn-icon">&#128161;</span>
    <div><b>When to use it</b>
    Use crypto to support the work anonymously or internationally with low fees. For contracts, invoices, consulting, or anything that needs a receipt, email <code>info@pirahansiah.com</code> instead.</div>
  </div>
</div>

<div class="crypto-selector" id="crypto-selector">
  <button class="token-pill" data-token="btc" type="button">BTC</button>
  <button class="token-pill active" data-token="eth" type="button">ETH</button>
  <button class="token-pill" data-token="sol" type="button">SOL</button>
  <button class="token-pill" data-token="base" type="button">BASE</button>
  <button class="token-pill" data-token="bnb" type="button">BNB</button>
</div>

<div class="crypto-panel">
  <div class="panel-head">
    <span class="ticker" id="sel-ticker">&#9874; ETH</span>
    <span class="chain" id="sel-chain">Ethereum</span>
  </div>
  <div class="panel-network" id="sel-network">Ethereum mainnet &middot; native ETH &amp; ERC-20 tokens</div>
  <div class="panel-live" id="sel-live">&#10003; Live from your connected MetaMask wallet</div>
  <div class="qr">
    <img id="sel-qr-img" src="{{ '/assets/qr/eth.svg' | relative_url }}" alt="Ethereum QR code">
    <canvas id="sel-qr-canvas" width="148" height="148"></canvas>
  </div>
  <div class="addr" id="sel-addr">0xFcE78486AE65e006Dc0d235FDD5d1E9169D53B0C</div>
  <button class="copy-btn" id="sel-copy" type="button">Copy address</button>
  <div class="panel-warn" id="sel-warn">Send only on the Ethereum network (ERC-20).</div>
</div>

<p class="mm-note">Private test page — not linked from anywhere on the site. Requires the MetaMask browser extension.</p>

<script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.4/lib/browser.min.js"></script>
<script>
(function () {
  var TOKENS = {
    btc: { ticker: '&#8383; BTC', chain: 'Bitcoin', qr: '/assets/qr/btc.svg',
      addr: 'bc1q922uu6uwu3x2grlkypeuyywet9msk2fzxypy6d',
      network: 'Bitcoin network &middot; native BTC &middot; bech32 (SegWit) address',
      warn: 'Send only on the Bitcoin network.', evm: false },
    eth: { ticker: '&#9874; ETH', chain: 'Ethereum', qr: '/assets/qr/eth.svg',
      addr: '0xFcE78486AE65e006Dc0d235FDD5d1E9169D53B0C',
      network: 'Ethereum mainnet &middot; native ETH &amp; ERC-20 tokens',
      warn: 'Send only on the Ethereum network (ERC-20).', evm: true },
    sol: { ticker: '&#9670; SOL', chain: 'Solana', qr: '/assets/qr/sol.svg',
      addr: 'DPfX2mNvCqQuosQLe4nDBQRf8ZdNfS5LA4tvSsGPyCH4',
      network: 'Solana network &middot; native SOL &amp; SPL tokens',
      warn: 'Send only on the Solana network.', evm: false },
    base: { ticker: '&#9650; BASE', chain: 'Base', qr: '/assets/qr/base.svg',
      addr: '0xFcE78486AE65e006Dc0d235FDD5d1E9169D53B0C',
      network: 'Base L2 &middot; native ETH &amp; ERC-20 tokens',
      warn: 'Send only on the Base network &mdash; do NOT send on Ethereum mainnet.', evm: true },
    bnb: { ticker: '&#9679; BNB', chain: 'BNB Smart Chain', qr: '/assets/qr/bnb.svg',
      addr: '0xFcE78486AE65e006Dc0d235FDD5d1E9169D53B0C',
      network: 'BNB Smart Chain &middot; native BNB &amp; BEP-20 tokens',
      warn: 'Send only on BNB Smart Chain (BEP-20).', evm: true }
  };
  var CHAINS = {
    '0x1': { name: 'Ethereum Mainnet', sym: 'ETH' },
    '0xaa36a7': { name: 'Sepolia Testnet', sym: 'ETH' },
    '0x2105': { name: 'Base', sym: 'ETH' },
    '0x38': { name: 'BNB Smart Chain', sym: 'BNB' },
    '0x89': { name: 'Polygon', sym: 'POL' },
    '0xa4b1': { name: 'Arbitrum One', sym: 'ETH' },
    '0xa': { name: 'Optimism', sym: 'ETH' }
  };

  var tickerEl = document.getElementById('sel-ticker');
  var chainEl = document.getElementById('sel-chain');
  var networkEl = document.getElementById('sel-network');
  var liveEl = document.getElementById('sel-live');
  var qrImg = document.getElementById('sel-qr-img');
  var qrCanvas = document.getElementById('sel-qr-canvas');
  var addrEl = document.getElementById('sel-addr');
  var warnEl = document.getElementById('sel-warn');
  var copyBtn = document.getElementById('sel-copy');
  var pills = document.querySelectorAll('.token-pill');

  var connectBtn = document.getElementById('mm-connect-btn');
  var connectedBox = document.getElementById('mm-connected');
  var acctEl = document.getElementById('mm-acct');
  var balEl = document.getElementById('mm-bal');
  var disconnectBtn = document.getElementById('mm-disconnect');
  var errBox = document.getElementById('mm-err');

  var connectedAccount = null;
  var current = 'eth';

  function showErr(msg) { errBox.textContent = msg; errBox.style.display = 'block'; }
  function clearErr() { errBox.style.display = 'none'; errBox.textContent = ''; }
  function short(a) { return a.slice(0, 6) + '&hellip;' + a.slice(-4); }

  function display() {
    var t = TOKENS[current];
    tickerEl.innerHTML = t.ticker;
    chainEl.textContent = t.chain;
    networkEl.innerHTML = t.network;
    warnEl.innerHTML = t.warn;
    var useLive = t.evm && connectedAccount;
    var addr = useLive ? connectedAccount : t.addr;
    addrEl.textContent = addr;
    if (useLive) {
      liveEl.style.display = 'block';
      qrImg.style.display = 'none';
      qrCanvas.style.display = 'block';
      if (window.QRCode) {
        try { QRCode.toCanvas(qrCanvas, addr, { width: 148, margin: 1 }); } catch (e) {}
      }
    } else {
      liveEl.style.display = 'none';
      qrCanvas.style.display = 'none';
      qrImg.style.display = 'block';
      qrImg.src = t.qr;
      qrImg.alt = t.chain + ' QR code';
    }
    copyBtn.classList.remove('copied');
    copyBtn.textContent = 'Copy address';
    pills.forEach(function (p) { p.classList.toggle('active', p.getAttribute('data-token') === current); });
  }

  function select(token) { current = token; display(); }
  pills.forEach(function (p) {
    p.addEventListener('click', function () { select(p.getAttribute('data-token')); });
  });

  async function refreshLive() {
    if (!connectedAccount) return;
    try {
      var chainId = await window.ethereum.request({ method: 'eth_chainId' });
      var c = CHAINS[chainId] || { name: chainId, sym: '' };
      var bal = await window.ethereum.request({ method: 'eth_getBalance', params: [connectedAccount, 'latest'] });
      acctEl.textContent = short(connectedAccount);
      balEl.textContent = (parseInt(bal, 16) / 1e18).toFixed(4) + (c.sym ? ' ' + c.sym : '') + '  ·  ' + c.name;
    } catch (e) {
      balEl.textContent = '';
    }
  }

  async function connect() {
    if (typeof window.ethereum === 'undefined') {
      showErr('MetaMask not detected. Please install the MetaMask extension and reload.');
      return;
    }
    clearErr();
    try {
      var accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      connectedAccount = accounts[0];
      connectBtn.style.display = 'none';
      connectedBox.style.display = 'flex';
      await refreshLive();
      display();
    } catch (e) {
      if (e && e.code === 4001) showErr('Connection request rejected.');
      else showErr((e && e.message) || 'Failed to connect.');
    }
  }

  function disconnect() {
    connectedAccount = null;
    connectBtn.style.display = 'inline-block';
    connectedBox.style.display = 'none';
    acctEl.textContent = '';
    balEl.textContent = '';
    display();
  }

  connectBtn.addEventListener('click', connect);
  disconnectBtn.addEventListener('click', disconnect);

  copyBtn.addEventListener('click', function () {
    var addr = addrEl.textContent;
    var onDone = function () {
      copyBtn.textContent = 'Copied!';
      copyBtn.classList.add('copied');
      setTimeout(function () { copyBtn.textContent = 'Copy address'; copyBtn.classList.remove('copied'); }, 1800);
    };
    function fallbackCopy(text, done) {
      var ta = document.createElement('textarea');
      ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); done(); } catch (e) { done(); }
      document.body.removeChild(ta);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(addr).then(onDone, function () { fallbackCopy(addr, onDone); });
    } else {
      fallbackCopy(addr, onDone);
    }
  });

  if (typeof window.ethereum !== 'undefined') {
    window.ethereum.on('accountsChanged', function (accounts) {
      if (accounts.length === 0) disconnect();
      else { connectedAccount = accounts[0]; refreshLive(); display(); }
    });
    window.ethereum.on('chainChanged', function () { refreshLive(); });
  }

  display();
})();
</script>
