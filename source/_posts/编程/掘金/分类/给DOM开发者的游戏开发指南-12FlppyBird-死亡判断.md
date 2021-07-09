
---
title: '给DOM开发者的游戏开发指南-12.FlppyBird-死亡判断'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/605bff2f541a480b89fcf16fbedd29d4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 05:08:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/605bff2f541a480b89fcf16fbedd29d4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>仓库地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhaiyoucuv%2FWhatIsGameDevelopment" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/haiyoucuv/WhatIsGameDevelopment" ref="nofollow noopener noreferrer">github.com/haiyoucuv/W…</a></p>
<p>引入概念：<code>碰撞</code> <code>盒式碰撞</code></p>
<p>上节我们完成了障碍创建的优化，性能提升一大截</p>
<p>本节将完成死亡条件的判断, 本案例的碰撞检测的方式包含一些强引用，并不适用于大型项目的开发</p>
<ul>
<li>
<h3 data-id="heading-0">1.落到地面死亡</h3>
</li>
<li>
<h3 data-id="heading-1">2.撞到障碍死亡</h3>
</li>
<li>
<h3 data-id="heading-2">3.死亡暂停游戏</h3>
</li>
</ul>
<h2 data-id="heading-3">落地死亡</h2>
<p>首先先修改一下<code>Bird</code>类, 增加一个<code>dieLine</code>的参数，表示为死亡线，如果我们的玩家碰到这根线则判定为死亡</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bird</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Sprite</span> </span>&#123;
<span class="hljs-comment">/* ... */</span>
dieLine; <span class="hljs-comment">// 死亡线</span>
<span class="hljs-comment">/* ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>FlppyStage</code>中的<code>ready</code>，在所有节点都<code>addChild</code>之后设置鸟的死亡线</p>
<blockquote>
<p>因为dom限制，无法在节点不在渲染的时候拿到clientWidth等属性，故要在在所有节点都<code>addChild</code>之后才设置鸟的死亡线</p>
</blockquote>
<p>因为地面放在<code>landMgr</code>的最底下，且<code>landMgr</code>的大小和<code>body</code>一样，故<code>land</code>和<code>Bird</code>在同一空间下</p>
<p>得到死亡线高度为<code>winSize.height - land1.size.height</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FlppyBird</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">GameStage</span> </span>&#123;

<span class="hljs-comment">/* ... */</span>

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">ready</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-comment">/* ... */</span>

<span class="hljs-comment">// 死亡线</span>
bird.dieLine = winSize.height - land1.size.height;

<span class="hljs-comment">/* ... */</span>
&#125;

<span class="hljs-comment">/* ... */</span>

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>Bird</code>的<code>update</code>函数</p>
<ul>
<li>撞到死亡线即停留在死亡线</li>
<li>打印 <code>坠机了，你死了</code></li>
</ul>
<blockquote>
<p>因为锚点在左上角的关系，故在计算是否死亡时，应将dieLine减去自己的高度</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bird</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Sprite</span> </span>&#123;

<span class="hljs-comment">/* ... */</span>

dieLine; <span class="hljs-comment">// 死亡线</span>

<span class="hljs-comment">/* ... */</span>

<span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">super</span>.update();

<span class="hljs-comment">// v = v0 + a * t²</span>
<span class="hljs-built_in">this</span>.speed += <span class="hljs-built_in">this</span>.gravity; <span class="hljs-comment">// 速度 = 速度 + 加速度 * 时间²</span>

<span class="hljs-keyword">let</span> top = <span class="hljs-built_in">this</span>.top + <span class="hljs-built_in">this</span>.speed;  <span class="hljs-comment">// 更新位置</span>

<span class="hljs-comment">// dieLine 因为锚点在左上角所以dieLine应该减去自己的高度</span>
<span class="hljs-keyword">const</span> dieLine = <span class="hljs-built_in">this</span>.dieLine - <span class="hljs-built_in">this</span>.size.height;

<span class="hljs-comment">// 如果大于dieLine了就停在dieLine</span>
<span class="hljs-keyword">if</span> (top > dieLine) &#123;
top = dieLine;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"坠机了，你死了"</span>);
&#125;

<span class="hljs-built_in">this</span>.top = top;

&#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行代码发现<code>bird</code>会停在地面，并且控制台打印 <code>坠机了，你死了</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/605bff2f541a480b89fcf16fbedd29d4~tplv-k3u1fbpfcp-watermark.image" alt="12_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">盒子碰撞</h2>
<p>盒子碰撞是使用游戏对象的包围盒检测是否有交集来判断是否碰撞</p>
<p>将盒子映射到x轴和y轴，得到线段A1->A2, B1->B2, A3->A4, B3->B4</p>
<p>如果A1->A2和B1->B2有交集，且A3->A4和B3->B4也有交集，则可认定两个盒子相交，即两个对象碰撞</p>
<p>如图 无交集 判定为无碰撞
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e80341fbaea841b3a173354286bf0005~tplv-k3u1fbpfcp-watermark.image" alt="12_2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图 只有一条轴上的映射有交集 判定为无碰撞
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45e468e3537e46fd9642e5f865b768d1~tplv-k3u1fbpfcp-watermark.image" alt="12_3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图 两条轴上的映射都有交集 判定为碰撞
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17a6be1bce6541f7a47523bc26b44261~tplv-k3u1fbpfcp-watermark.image" alt="12_4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码实现</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 盒子碰撞
 * <span class="hljs-doctag">@param </span>rect1 &#123;top, left, size:&#123;width, height&#125;&#125;
 * <span class="hljs-doctag">@param </span>rect2 &#123;top, left, size:&#123;width, height&#125;&#125;
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;boolean&#125;</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">boxCollisionTest</span>(<span class="hljs-params">rect1, rect2</span>) </span>&#123;
<span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">top</span>: t1, <span class="hljs-attr">left</span>: l1 &#125; = rect1;
<span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">width</span>: w1, <span class="hljs-attr">height</span>: h1 &#125; = rect1.size;

<span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">top</span>: t2, <span class="hljs-attr">left</span>: l2 &#125; = rect2;
<span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">width</span>: w2, <span class="hljs-attr">height</span>: h2 &#125; = rect2.size;

<span class="hljs-keyword">const</span> b1 = t1 + h1,
b2 = t2 + h2,
r1 = l1 + w1,
r2 = l2 + w2;

<span class="hljs-keyword">return</span> ((t1 > t2 && t1 < b2) || (t2 > t1 && t2 < b1))  <span class="hljs-comment">// 检查 t1->b1 和 t2->b2 的交集</span>
&& ((l1 > l2 && l1 < r2) || (l2 > l1 && l2 < r1));   <span class="hljs-comment">// 检查 l1->r1 和 l2->r2 的交集</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">改造<code>PieMgr</code></h2>
<ul>
<li>传入我们的主角<code>bird</code></li>
<li>在移动<code>pie</code>之后检查碰撞</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * PieMgr
 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PieMgr</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">GameObject</span> </span>&#123;

<span class="hljs-comment">/* ... */</span>

bird;   <span class="hljs-comment">// 玩家</span>

<span class="hljs-comment">/* ... */</span>

<span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">super</span>.update();

<span class="hljs-comment">// 所有的Pie同时向左移动</span>
<span class="hljs-keyword">const</span> &#123; speed, pieArr &#125; = <span class="hljs-built_in">this</span>;
pieArr.forEach(<span class="hljs-function">(<span class="hljs-params">pie</span>) =></span> &#123;
<span class="hljs-comment">// 移动</span>
pie.left -= speed;
<span class="hljs-keyword">if</span> (pie.left <= -pie.size.width) &#123;  <span class="hljs-comment">// 如果移出屏幕</span>
<span class="hljs-built_in">this</span>.pieArr.splice(<span class="hljs-built_in">this</span>.pieArr.indexOf(pie), <span class="hljs-number">1</span>);    <span class="hljs-comment">// 从托管列表里移除</span>
<span class="hljs-built_in">this</span>.removeChild(pie);                              <span class="hljs-comment">// 从子节点移除</span>
ObjectPool.put(<span class="hljs-string">"pie"</span>, pie);                         <span class="hljs-comment">// 加入对象池</span>
<span class="hljs-keyword">return</span>;
&#125;

<span class="hljs-comment">// 检查碰撞</span>
<span class="hljs-comment">// 重构盒子，因为pie.up和pie.down的坐标是相对于pie的，所以要重构正方形的left和top</span>
<span class="hljs-keyword">const</span> pieUpBox = &#123;
<span class="hljs-attr">left</span>: pie.left,
<span class="hljs-attr">top</span>: pie.top + pie.up.top,
<span class="hljs-attr">size</span>: pie.up.size,
&#125;

<span class="hljs-keyword">const</span> pieDownBox = &#123;
<span class="hljs-attr">left</span>: pie.left,
<span class="hljs-attr">top</span>: pie.top + pie.down.top,
<span class="hljs-attr">size</span>: pie.down.size,
&#125;
<span class="hljs-keyword">if</span> (boxCollisionTest(<span class="hljs-built_in">this</span>.bird, pieUpBox) || boxCollisionTest(<span class="hljs-built_in">this</span>.bird, pieDownBox)) &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"撞到障碍，你死了"</span>);
&#125;
&#125;);
&#125;
&#125;

<span class="hljs-keyword">const</span> pieMgr = <span class="hljs-built_in">this</span>.pieMgr = <span class="hljs-keyword">new</span> PieMgr(<span class="hljs-number">4</span>, <span class="hljs-number">1000</span>, bird);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行案例得到效果
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8a9552e879f4d74a0298aafea2d9284~tplv-k3u1fbpfcp-watermark.image" alt="12_5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/170644037bde4ce58d03b4ca78a651ed~tplv-k3u1fbpfcp-watermark.image" alt="12_6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">死亡暂停游戏</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6dc740e45814ec0b51377cacd9f7531~tplv-k3u1fbpfcp-watermark.image" alt="12_7.png" loading="lazy" referrerpolicy="no-referrer">
在本案例中我们可以简单的将暂停游戏简单的理解为暂停循环</p>
<ul>
<li>在FlppyBird的<code>update</code>中插入控制变量<code>pause</code></li>
<li>如果<code>pause</code>为真则不执行<code>super.update</code></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FlppyBird</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">GameStage</span> </span>&#123;

pause = <span class="hljs-literal">false</span>;

<span class="hljs-comment">/* ... */</span>

<span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.pause) <span class="hljs-keyword">return</span>;
<span class="hljs-built_in">super</span>.update();
&#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用事件通知游戏暂停</p>
<p>本案例不带大家实现自己的事件收发器</p>
<p>借用强大的<code>document</code>来实现事件收发</p>
<p>每一个dom节点其实都继承了一个事件收发器，所以可以直接利用dom节点做事件收发</p>
<ul>
<li>在<code>FlppyBird</code>的<code>ready</code>中监听<code>playerDie</code>事件，并在<code>destroy</code>中移除</li>
<li>将之前的死亡打印，变为发送<code>playerDie</code>事件</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FlppyBird</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">GameStage</span> </span>&#123;

<span class="hljs-comment">/* ... */</span>

pause = <span class="hljs-literal">false</span>;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">ready</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">"playerDie"</span>, <span class="hljs-built_in">this</span>.pauseGame);
&#125;

<span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.pause) <span class="hljs-keyword">return</span>;
<span class="hljs-built_in">super</span>.update();
&#125;

pauseGame = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
<span class="hljs-built_in">console</span>.error(e.data);
<span class="hljs-built_in">this</span>.pause = <span class="hljs-literal">true</span>;
&#125;

&#125;


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bird</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Sprite</span> </span>&#123;

<span class="hljs-comment">/* ... */</span>

<span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">super</span>.update();

<span class="hljs-comment">// v = v0 + a * t²</span>
<span class="hljs-built_in">this</span>.speed += <span class="hljs-built_in">this</span>.gravity; <span class="hljs-comment">// 速度 = 速度 + 加速度 * 时间²</span>

<span class="hljs-keyword">let</span> top = <span class="hljs-built_in">this</span>.top + <span class="hljs-built_in">this</span>.speed;  <span class="hljs-comment">// 更新位置</span>

<span class="hljs-comment">// dieLine 因为锚点在左上角所以dieLine应该减去自己的高度</span>
<span class="hljs-keyword">const</span> dieLine = <span class="hljs-built_in">this</span>.dieLine - <span class="hljs-built_in">this</span>.size.height;

<span class="hljs-comment">// 如果大于dieLine了就停在dieLine</span>
<span class="hljs-keyword">if</span> (top > dieLine) &#123;
top = dieLine;
<span class="hljs-comment">// 发送死亡事件</span>
<span class="hljs-keyword">const</span> event = <span class="hljs-keyword">new</span> Event(<span class="hljs-string">"playerDie"</span>);
event.data = <span class="hljs-string">"坠机了，你死了"</span>;
<span class="hljs-built_in">document</span>.dispatchEvent(event);
&#125;

<span class="hljs-built_in">this</span>.top = top;

&#125;

&#125;


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PieMgr</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">GameObject</span> </span>&#123;

<span class="hljs-comment">/* ... */</span>

bird;   <span class="hljs-comment">// 玩家</span>

<span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">super</span>.update();

<span class="hljs-comment">// 移动</span>
<span class="hljs-comment">// 所有的Pie同时向左移动</span>
<span class="hljs-keyword">const</span> &#123; speed, pieArr &#125; = <span class="hljs-built_in">this</span>;
pieArr.forEach(<span class="hljs-function">(<span class="hljs-params">pie</span>) =></span> &#123;
pie.left -= speed;
<span class="hljs-keyword">if</span> (pie.left <= -pie.size.width) &#123;  <span class="hljs-comment">// 如果移出屏幕</span>
<span class="hljs-built_in">this</span>.pieArr.splice(<span class="hljs-built_in">this</span>.pieArr.indexOf(pie), <span class="hljs-number">1</span>);    <span class="hljs-comment">// 从托管列表里移除</span>
<span class="hljs-built_in">this</span>.removeChild(pie);                              <span class="hljs-comment">// 从子节点移除</span>
ObjectPool.put(<span class="hljs-string">"pie"</span>, pie);                         <span class="hljs-comment">// 加入对象池</span>
<span class="hljs-keyword">return</span>;
&#125;

<span class="hljs-comment">// 检查碰撞</span>
<span class="hljs-comment">// 重构盒子，因为pie.up和pie.down的坐标是相对于pie的，所以要重构正方形的left和top</span>
<span class="hljs-keyword">const</span> pieUpBox = &#123;
<span class="hljs-attr">left</span>: pie.left,
<span class="hljs-attr">top</span>: pie.top + pie.up.top,
<span class="hljs-attr">size</span>: pie.up.size,
&#125;

<span class="hljs-keyword">const</span> pieDownBox = &#123;
<span class="hljs-attr">left</span>: pie.left,
<span class="hljs-attr">top</span>: pie.top + pie.down.top,
<span class="hljs-attr">size</span>: pie.down.size,
&#125;
<span class="hljs-keyword">if</span> (boxCollisionTest(<span class="hljs-built_in">this</span>.bird, pieUpBox) || boxCollisionTest(<span class="hljs-built_in">this</span>.bird, pieDownBox)) &#123;
<span class="hljs-comment">// 发送死亡事件</span>
<span class="hljs-keyword">const</span> event = <span class="hljs-keyword">new</span> Event(<span class="hljs-string">"playerDie"</span>);
event.data = <span class="hljs-string">"撞到障碍，你死了"</span>;
<span class="hljs-built_in">document</span>.dispatchEvent(event);
&#125;
&#125;);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行案例，发现两种死亡方式都可以正常暂停游戏</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2debcceb096f42e68557441c8419f0e9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3e670fcff31410d8555db432dfd8cb6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            