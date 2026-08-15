---
layout: farshid_default
permalink: /metamask/
title: "MetaMask — Connect & Receive"
description: "Connect MetaMask to reveal your wallet address, balance and a scan-to-receive QR code. Private test page."
sitemap: false
noindex: true
---

> **MetaMask Connect** — Connect your wallet and get your receive address + QR code. — https://pirahansiah.com/metamask/

<style>
.mm-hero { text-align: center; padding: 26px 16px 6px; }
.mm-hero h1 { font-size: 2rem; margin: 0 0 8px; }
.mm-hero p { color: var(--text-muted); margin: 0 0 6px; }
.mm-card {
  max-width: 460px;
  margin: 22px auto;
  padding: 28px 24px;
  border-radius: 20px;
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  text-align: center;
}
.mm-btn {
  display: inline-block;
  padding: 12px 26px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  color: #fff;
  background: linear-gradient(135deg, var(--farshid-blue), var(--farshid-purple));
  box-shadow: 0 4px 18px rgba(10,132,255,0.35);
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.mm-btn:hover { transform: translateY(-1px); box-shadow: 0 6px 22px rgba(10,132,255,0.45); }
.mm-btn.ghost { background: var(--glass-bg-strong); box-shadow: none; }
.mm-addr {
  display: block;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.82rem;
  word-break: break-all;
  background: rgba(0,0,0,0.28);
  padding: 10px 12px;
  border-radius: 10px;
  margin: 12px 0;
  color: #7ee0a3;
}
.mm-row { margin: 10px 0; color: var(--text-muted); font-size: 0.92rem; }
.mm-row b { color: var(--text); }
.mm-qr { margin: 12px auto 4px; }
.mm-qr canvas { border-radius: 12px; }
.mm-err {
  margin-top: 14px;
  padding: 12px;
  border-radius: 10px;
  background: rgba(255,55,95,0.15);
  border: 1px solid rgba(255,55,95,0.4);
  color: #ff8a9b;
  font-size: 0.88rem;
  display: none;
}
.mm-note { color: var(--text-muted); font-size: 0.8rem; margin: 20px auto 0; text-align: center; max-width: 520px; }
</style>

<div class="mm-hero">
  <h1>MetaMask — Connect &amp; Receive</h1>
  <p>Connect your wallet to reveal your address, native balance and a scan-to-receive QR code.</p>
</div>

<div class="mm-card" id="mm-card">
  <div id="mm-connect">
    <button class="mm-btn" id="mm-connect-btn" type="button">Connect MetaMask</button>
  </div>

  <div id="mm-view" style="display:none;">
    <div class="mm-row"><b id="mm-network">—</b></div>
    <div class="mm-qr"><canvas id="mm-qr" width="200" height="200"></canvas></div>
    <code class="mm-addr" id="mm-addr"></code>
    <div class="mm-row">Balance: <b id="mm-balance">—</b></div>
    <div style="margin-top:14px; display:flex; gap:10px; justify-content:center; flex-wrap:wrap;">
      <button class="mm-btn ghost" id="mm-copy" type="button">Copy Address</button>
      <button class="mm-btn ghost" id="mm-disconnect" type="button">Disconnect</button>
    </div>
  </div>

  <div class="mm-err" id="mm-err"></div>
</div>

<p class="mm-note">Private test page — not linked from anywhere on the site. Requires the MetaMask browser extension.</p>

<script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.4/lib/browser.min.js"></script>
<script>
(function () {
  var view = document.getElementById('mm-view');
  var connectBox = document.getElementById('mm-connect');
  var errBox = document.getElementById('mm-err');
  var addrEl = document.getElementById('mm-addr');
  var netEl = document.getElementById('mm-network');
  var balEl = document.getElementById('mm-balance');
  var qrCanvas = document.getElementById('mm-qr');

  var CHAINS = {
    '0x1': { name: 'Ethereum Mainnet', sym: 'ETH' },
    '0xaa36a7': { name: 'Sepolia Testnet', sym: 'ETH' },
    '0x2105': { name: 'Base', sym: 'ETH' },
    '0x38': { name: 'BNB Smart Chain', sym: 'BNB' },
    '0x89': { name: 'Polygon', sym: 'POL' },
    '0xa4b1': { name: 'Arbitrum One', sym: 'ETH' },
    '0xa': { name: 'Optimism', sym: 'ETH' }
  };

  function showErr(msg) { errBox.textContent = msg; errBox.style.display = 'block'; }
  function clearErr() { errBox.style.display = 'none'; errBox.textContent = ''; }

  function render(account) {
    addrEl.textContent = account;
    connectBox.style.display = 'none';
    view.style.display = 'block';
    if (window.QRCode) {
      try { QRCode.toCanvas(qrCanvas, account, { width: 200, margin: 1 }); } catch (e) {}
    }
  }

  async function refresh(account) {
    clearErr();
    try {
      var chainId = await window.ethereum.request({ method: 'eth_chainId' });
      var c = CHAINS[chainId] || { name: chainId, sym: '' };
      netEl.textContent = c.name + (c.sym ? '  ·  ' + c.sym : '');
      var bal = await window.ethereum.request({ method: 'eth_getBalance', params: [account, 'latest'] });
      balEl.textContent = (parseInt(bal, 16) / 1e18).toFixed(6) + (c.sym ? ' ' + c.sym : '');
    } catch (e) {
      balEl.textContent = '—';
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
      render(accounts[0]);
      refresh(accounts[0]);
    } catch (e) {
      if (e && e.code === 4001) showErr('Connection request rejected.');
      else showErr((e && e.message) || 'Failed to connect.');
    }
  }

  function disconnect() {
    view.style.display = 'none';
    connectBox.style.display = 'block';
    addrEl.textContent = '';
    balEl.textContent = '—';
    netEl.textContent = '—';
  }

  document.getElementById('mm-connect-btn').addEventListener('click', connect);
  document.getElementById('mm-disconnect').addEventListener('click', disconnect);
  document.getElementById('mm-copy').addEventListener('click', function () {
    var a = addrEl.textContent;
    if (!a) return;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(a).then(function () {
        var b = document.getElementById('mm-copy');
        b.textContent = 'Copied!';
        setTimeout(function () { b.textContent = 'Copy Address'; }, 1500);
      });
    }
  });

  if (typeof window.ethereum !== 'undefined') {
    window.ethereum.on('accountsChanged', function (accounts) {
      if (accounts.length === 0) disconnect();
      else { render(accounts[0]); refresh(accounts[0]); }
    });
    window.ethereum.on('chainChanged', function () {
      if (addrEl.textContent) refresh(addrEl.textContent);
    });
  }
})();
</script>
