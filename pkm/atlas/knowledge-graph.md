---
layout: default
title: Knowledge Atlas
---

<div id="ka"></div>

{% raw %}
<style>
@keyframes spin{to{transform:rotate(360deg)}}
#ka-loader{padding:40px;text-align:center;color:#666}
#ka-loader div{border:4px solid #f3f3f3;border-top:4px solid #3498db;border-radius:50%;width:30px;height:30px;animation:spin 1s linear infinite;margin:0 auto 15px}
.kb{margin-bottom:36px}.kl{column-count:2;column-gap:40px;list-style:none;padding:0;margin:0}
@media(max-width:600px){.kl{column-count:1}}
.ki{margin-bottom:10px;break-inside:avoid}
.kk{color:#0076df;text-decoration:none;font-size:1rem;display:block;border-left:3px solid #eee;padding-left:11px;transition:color .2s,border-color .2s}
.kk:hover{color:#004a8d;border-left-color:#3498db;background:#f9f9f9}
.kc{font-size:.75rem;letter-spacing:.1em;color:#888;text-transform:uppercase;border-bottom:1px solid #eee;padding-bottom:6px;margin-bottom:12px;font-weight:600}
</style>
<script>
(function(){
  var el=document.getElementById('ka');
  el.innerHTML='<div id="ka-loader"><div></div>Loading…</div>';
  var CACHE='atlas_v2',repo='pirahansiah/pirahansiah.github.io',branch='main';
  function run(data){
    var items=data.tree.filter(function(i){
      return i.type==='blob'&&i.path.startsWith('contents/')&&i.path.endsWith('.md')
        &&!i.path.includes('/index.md')&&!i.path.split('/').some(function(p){return p[0]==='.'});
    }).map(function(i){
      var clean=i.path.replace(/\.md$/,'');
      var segs=clean.split('/');
      var name=segs.pop();
      var cat=segs.slice(1).join(' / ').toUpperCase()||'ROOT';
      return{
        title:name.replace(/[-_]/g,' ').replace(/\b\w/g,function(c){return c.toUpperCase()}),
        url:'/'+clean+'/',
        cat:cat
      };
    });
    if(!items.length){el.innerHTML='<p>No .md files found in /contents/.</p>';return;}
    items.sort(function(a,b){return a.title.localeCompare(b.title)});
    var grouped={};
    items.forEach(function(i){(grouped[i.cat]=grouped[i.cat]||[]).push(i)});
    var html='<h2 style="font-weight:300;border-bottom:2px solid #333;padding-bottom:8px;margin-bottom:32px">Knowledge Atlas ('+items.length+' pages)</h2>';
    Object.keys(grouped).sort().forEach(function(cat){
      html+='<div class="kb"><div class="kc">'+cat+'</div><ul class="kl">';
      grouped[cat].forEach(function(f){
        html+='<li class="ki"><a class="kk" href="'+f.url+'">'+f.title+'</a></li>';
      });
      html+='</ul></div>';
    });
    el.innerHTML=html;
  }
  try{
    var cached=sessionStorage.getItem(CACHE);
    if(cached){run(JSON.parse(cached));return;}
  }catch(e){}
  fetch('https://api.github.com/repos/'+repo+'/git/trees/'+branch+'?recursive=1')
    .then(function(r){
      if(r.status===403||r.status===429)throw new Error('rate_limited');
      if(!r.ok)throw new Error('http_'+r.status);
      return r.json();
    })
    .then(function(data){
      try{sessionStorage.setItem(CACHE,JSON.stringify(data))}catch(e){}
      run(data);
    })
    .catch(function(err){
      var msg=err.message==='rate_limited'
        ?'GitHub API rate limit hit (60 req/hr). Refresh in a few minutes.'
        :'Could not load atlas: '+err.message;
      el.innerHTML='<div style="background:#fff5f5;border:1px solid #feb2b2;padding:16px;color:#c53030;border-radius:6px"><strong>Error:</strong> '+msg+'</div>';
    });
})();
</script>
{% endraw %}