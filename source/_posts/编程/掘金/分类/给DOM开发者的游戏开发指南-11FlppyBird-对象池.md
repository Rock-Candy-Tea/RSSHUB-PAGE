
---
title: '给DOM开发者的游戏开发指南-11.FlppyBird-对象池'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4996bed1a7945ca9dfb644cbb8a4cfa~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 05:05:45 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4996bed1a7945ca9dfb644cbb8a4cfa~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>仓库地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhaiyoucuv%2FWhatIsGameDevelopment" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/haiyoucuv/WhatIsGameDevelopment" ref="nofollow noopener noreferrer">github.com/haiyoucuv/W…</a></p>
<p>引入概念：<code>对象池</code></p>
<p>上节我们完成了障碍的动态创建</p>
<p>但是运行一段时间发现，dom节点树上有n个障碍，卡得一批</p>
<p>这些移出屏幕的障碍，不仅占了大量内存，而且他们其实完全不需要更新和渲染</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4996bed1a7945ca9dfb644cbb8a4cfa~tplv-k3u1fbpfcp-watermark.image" alt="11_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">对象池</h2>
<p>使用对象池，回收对象，保存在池中，需要的时候不必再重新创建，只需要从池中获取就可以</p>
<p>对象移除显示列表的时候，放回池中就可以了</p>
<ul>
<li>创建<code>ObjectPool</code>类</li>
<li>用一个静态变量来保存对象</li>
<li>实现静态方法<code>put</code>接口，传入<code>name</code>来区分保存对象的类型，这样可以保存不同的类型的对象</li>
<li>实现静态方法<code>get</code>接口，传入<code>name</code>来获取相应的类型的对象</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 一个简单的通用对象池
 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ObjectPool</span> </span>&#123;

<span class="hljs-keyword">static</span> objs = &#123;&#125;;

<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">put</span>(<span class="hljs-params">name, obj</span>)</span> &#123;
<span class="hljs-keyword">const</span> pool = ObjectPool.objs[name] || (ObjectPool.objs[name] = []);

pool.push(obj);
&#125;

<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">name</span>)</span> &#123;
<span class="hljs-keyword">const</span> pool = ObjectPool.objs[name] || (ObjectPool.objs[name] = []);

<span class="hljs-keyword">if</span> (pool.length <= <span class="hljs-number">0</span>) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;

<span class="hljs-keyword">return</span> pool.shift();
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">改造<code>PieMgr</code></h2>
<ul>
<li>创建<code>Pie</code>时先从对象池中获取，如果没有，则新创建</li>
<li>当<code>Pie</code>移出屏幕后，从托管列表中移除，从子节点移除，并且放回对象池</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PieMgr</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">GameObject</span> </span>&#123;

<span class="hljs-comment">/* ... */</span>

<span class="hljs-comment">/**
 * 创建Pie
 */</span>
<span class="hljs-function"><span class="hljs-title">createPie</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-comment">// 使用对象池 如果对象池中取不到，说明对象池空了，需要新创建</span>
<span class="hljs-keyword">const</span> pie = ObjectPool.get(<span class="hljs-string">"pie"</span>) || <span class="hljs-keyword">new</span> Pie();
<span class="hljs-built_in">this</span>.addChild(pie);
<span class="hljs-built_in">this</span>.pieArr.push(pie);  <span class="hljs-comment">// 加入列表统一管理</span>
pie.top = <span class="hljs-built_in">Math</span>.random() * -<span class="hljs-number">150</span>; <span class="hljs-comment">// 高度随机</span>
pie.left = winSize.width;   <span class="hljs-comment">// 从屏幕左边出现</span>
&#125;

<span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">super</span>.update();

<span class="hljs-comment">// 所有的Pie同时向左移动</span>
<span class="hljs-keyword">const</span> &#123; speed, pieArr &#125; = <span class="hljs-built_in">this</span>;
pieArr.forEach(<span class="hljs-function">(<span class="hljs-params">pie</span>) =></span> &#123;
pie.left -= speed;
<span class="hljs-keyword">if</span> (pie.left <= -pie.size.width) &#123;  <span class="hljs-comment">// 如果移出屏幕</span>
<span class="hljs-built_in">this</span>.pieArr.splice(<span class="hljs-built_in">this</span>.pieArr.indexOf(pie), <span class="hljs-number">1</span>);    <span class="hljs-comment">// 从托管列表里移除</span>
<span class="hljs-built_in">this</span>.removeChild(pie);                              <span class="hljs-comment">// 从子节点移除</span>
ObjectPool.put(<span class="hljs-string">"pie"</span>, pie);                         <span class="hljs-comment">// 加入对象池</span>
&#125;
&#125;);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行案例，挂机10分钟，一点也不卡，显示列表最多也只有两个<code>Pie</code>同时存在</p>
<h1 data-id="heading-2">挂机一天也不卡，牛逼</h1></div>  
</div>
            