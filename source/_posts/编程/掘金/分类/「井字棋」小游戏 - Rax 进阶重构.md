
---
title: '「井字棋」小游戏 - Rax 进阶重构'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8663a6b31ff94b6b91eae2cfc80c58a7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 23:00:45 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8663a6b31ff94b6b91eae2cfc80c58a7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">前言</h1>
<p>在之前实现的 <a href="https://juejin.cn/post/6981641681611259911" target="_blank" title="https://juejin.cn/post/6981641681611259911">Rax.js+Ts+ESlint「旅游官网」实战项目</a> 的基础上，利用 React 官方项目例子  <a href="https://link.juejin.cn/?target=https%3A%2F%2Freact.docschina.org%2Ftutorial%2Ftutorial.html" target="_blank" rel="nofollow noopener noreferrer" title="https://react.docschina.org/tutorial/tutorial.html" ref="nofollow noopener noreferrer">GoBang 井字棋小游戏</a> 来进一步熟悉 Rax 框架。</p>
<p>该<strong>井字棋</strong>小游戏例子在官方文档中实例已经写得很清楚详细，本文就不稍加介绍了嘿，主要是将该小游戏以 Rax 进行重构，并且使用 function 组件和 hooks 的方式进行项目案例的更新替代。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8663a6b31ff94b6b91eae2cfc80c58a7~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现功能效果如下：</p>
<blockquote>
<ol>
<li>tic-tac-toe(三连棋)游戏的所有功能</li>
<li>能够判定玩家何时获胜</li>
<li>能够记录游戏进程</li>
<li>允许玩家查看游戏的历史记录，也可以查看任意一个历史版本的游戏棋盘状态</li>
</ol>
</blockquote>
<p>而本篇文章的目标是进阶优化完善升级小游戏项目的功能点：</p>
<blockquote>
<ol>
<li>在游戏历史记录列表显示每一步棋的坐标，格式为 (列号, 行号)。</li>
<li>在历史记录列表中加粗显示当前选择的项目。</li>
<li>使用两个循环来渲染出棋盘的格子，而不是在代码里写死（hardcode）。</li>
<li>添加一个可以升序或降序显示历史记录的按钮。</li>
<li>每当有人获胜时，高亮显示连成一线的 3 颗棋子。</li>
<li>当无人获胜时，显示一个平局的消息。</li>
</ol>
</blockquote>
<h1 data-id="heading-1">项目</h1>
<h2 data-id="heading-2">Gobang 小游戏嵌入旅游项目</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35f63cb250d948e492d4673a62b2a8ca~tplv-k3u1fbpfcp-watermark.image" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重点：<strong>利用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Frax.js.org%2Fdocs%2Fguide%2Fspa-route" target="_blank" rel="nofollow noopener noreferrer" title="https://rax.js.org/docs/guide/spa-route" ref="nofollow noopener noreferrer">Rax 的路由</a>进行跳转。</strong></p>
<h3 data-id="heading-3">路由配置</h3>
<blockquote>
<p>/src/app.json</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"routes"</span>: [
    &#123;
      <span class="hljs-attr">"path"</span>: <span class="hljs-string">"/"</span>,
      <span class="hljs-attr">"source"</span>: <span class="hljs-string">"pages/Home/index"</span>
    &#125;,
    &#123;
      <span class="hljs-attr">"path"</span>: <span class="hljs-string">"/gobang"</span>,
      <span class="hljs-attr">"source"</span>: <span class="hljs-string">"pages/Gobang/index"</span>
    &#125;
  ],
  <span class="hljs-attr">"window"</span>: &#123;
    <span class="hljs-attr">"title"</span>: <span class="hljs-string">"柃木🎈"</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">旅游导航</h3>
<blockquote>
<p>/src/components/Header.tsx</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> &#123; history &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rax-app'</span>;

<span class="hljs-comment">// ...代码省略</span>
<span class="hljs-comment">// 在 &#123;/* navMenu */&#125; 中加入 Gobang 导航</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.navLink&#125;</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"gobang"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> history.push('gobang')&#125;>
  Gobang
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Gobang 导航</h3>
<p>Gobang 返回旅游页面</p>
<blockquote>
<p>/src/pages/Gobang/index.tsx</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> &#123; history <span class="hljs-keyword">as</span> router &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rax-app'</span>;

<span class="hljs-comment">// ... 省略</span>

<span class="hljs-comment">// 添加返回旅游页面代码</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">textAlign:</span> '<span class="hljs-attr">center</span>' &#125;&#125; <span class="hljs-attr">className</span>=<span class="hljs-string">"button buttonPrimary buttonBig buttonNoRound"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> router.push('/')&#125;>
          返回旅游页面
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">添加棋子坐标</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c253ee8a6744f8e987402892e7a9196~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重点：<strong>利用棋盘点击事件上的 <code>i</code> 来确定当前棋子坐标。</strong></p>
<h3 data-id="heading-7">Gobang 页面</h3>
<blockquote>
<p>/src/pages/Gobang/index.tsx</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 给 history 对象状态添加 nowKey 属性，记录当前坐标。</span>
<span class="hljs-keyword">const</span> [history, setHistory] = useState([
  &#123;
    <span class="hljs-attr">squares</span>: <span class="hljs-built_in">Array</span>(<span class="hljs-number">9</span>).fill(<span class="hljs-literal">null</span>),
    <span class="hljs-attr">nowKey</span>: <span class="hljs-string">''</span>,
  &#125;,
]);

<span class="hljs-comment">// 在 handleClick 事件中根据 `i` 计算出当前棋子的坐标，并调用 effect 事件更新记录。</span>
<span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">(<span class="hljs-params">i: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span></span>) =></span> &#123;
  <span class="hljs-keyword">const</span> nowKey = [(+i % <span class="hljs-number">3</span>) + <span class="hljs-number">1</span>, <span class="hljs-built_in">Math</span>.floor((+i / <span class="hljs-number">3</span>)) + <span class="hljs-number">1</span>].join(<span class="hljs-string">','</span>);
  <span class="hljs-comment">// ...省略代码</span>
  <span class="hljs-keyword">const</span> historyTemp = [...curHistory, &#123; squares, nowKey &#125;];
  setHistory(historyTemp);
&#125;

<span class="hljs-comment">// 在游戏历史记录列表显示每一步棋的坐标</span>
<span class="hljs-keyword">const</span> moves = history.map(<span class="hljs-function">(<span class="hljs-params">step, move</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> desc = move ? <span class="hljs-string">`Go to move #<span class="hljs-subst">$&#123;move&#125;</span> \n Chess position: (<span class="hljs-subst">$&#123;step.nowKey&#125;</span>)`</span> : <span class="hljs-string">'Go to game start'</span>;
  <span class="hljs-comment">// ...省略代码</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>需要更新一个 li 的外边距以及 li > button 的宽高样式。</p>
</blockquote>
<h2 data-id="heading-8">显示当前选择的历史项目</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68c211040df34604834b295a83449b2e~tplv-k3u1fbpfcp-watermark.image" alt="4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重点：<strong>历史项目上样式的 focus</strong>，伪元素和伪类是可以直接套用添加。</p>
<h3 data-id="heading-9">Gobang 样式</h3>
<blockquote>
<p>/src/pages/Gobang/index.module.css</p>
</blockquote>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">li</span> > <span class="hljs-selector-tag">button</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">160px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">position</span>: relative;
&#125;
<span class="hljs-selector-tag">li</span> > <span class="hljs-selector-tag">button</span><span class="hljs-selector-pseudo">:focus</span>:before &#123;
  content: <span class="hljs-string">""</span>;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: -<span class="hljs-number">4px</span>;
  <span class="hljs-attribute">left</span>: -<span class="hljs-number">4px</span>;
  <span class="hljs-attribute">right</span>: -<span class="hljs-number">4px</span>;
  <span class="hljs-attribute">bottom</span>: -<span class="hljs-number">4px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">4px</span> solid gold;
  <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.5s</span>;
  <span class="hljs-attribute">animation</span>: clipPath <span class="hljs-number">3s</span> infinite linear;
&#125;
<span class="hljs-keyword">@keyframes</span> clipPath &#123;
  <span class="hljs-number">0%</span>,
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">clip-path</span>: <span class="hljs-built_in">inset</span>(<span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">95%</span> <span class="hljs-number">0</span>);
  &#125;

  <span class="hljs-number">25%</span> &#123;
    <span class="hljs-attribute">clip-path</span>: <span class="hljs-built_in">inset</span>(<span class="hljs-number">0</span> <span class="hljs-number">95%</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>);
  &#125;
  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-attribute">clip-path</span>: <span class="hljs-built_in">inset</span>(<span class="hljs-number">95%</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>);
  &#125;
  <span class="hljs-number">75%</span> &#123;
    <span class="hljs-attribute">clip-path</span>: <span class="hljs-built_in">inset</span>(<span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">95%</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">循环渲染格子</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75767ae139964e7b972d1e1067497eb9~tplv-k3u1fbpfcp-watermark.image" alt="5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重点：<strong><code>Array.map()</code> 和对应的 key 值</strong></p>
<h3 data-id="heading-11">Board 棋盘</h3>
<blockquote>
<p>/src/components/Board/index.tsx</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 省略代码</span>
<span class="hljs-comment">// 给格子添加 key 值</span>
<Square key=&#123;i&#125; value=&#123;props.squares[i]&#125; onClick=&#123;<span class="hljs-function">() =></span> props.onClick(i)&#125; />;

 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
  // 使用两个循环来渲染出棋盘的格子
  &#123;[0, 1, 2].map((v) => &#123;
    return (
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;v&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.boardRow&#125;</span>></span>
        &#123;[NaN, NaN, NaN].map((v2, i) => &#123;
          return (renderSquare(v * 3 + i));
        &#125;)&#125;;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    );
  &#125;)&#125;
<span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ul>
<li>注意不能使用 <code>Array(3)</code> 来初始化空数组，当空数组时不能被渲染出来</li>
<li>key 值不能是 index 索引</li>
<li>注意传入方法 <code>renderSquare</code> 的值与外层循环的索引值的关系</li>
</ul>
</blockquote>
<h2 data-id="heading-12">排序历史记录</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f71da5b4c5dc4672bffbf1d0feabe013~tplv-k3u1fbpfcp-watermark.image" alt="6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重点：<strong>设置 sort 状态，并且调用 <code>Array.reverse()</code> 调转历史记录数组</strong></p>
<h3 data-id="heading-13">Gobang 页面</h3>
<blockquote>
<p>/src/pages/Gobang/index.tsx</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 设置 sort 状态</span>
<span class="hljs-keyword">const</span> [sort, setSort] = useState(<span class="hljs-literal">false</span>);

<span class="hljs-comment">// 判断是否需要调转历史记录数组</span>
sort && moves.reverse();

<span class="hljs-comment">// ... 省略代码</span>
<span class="hljs-comment">// 排序按钮</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>
  <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">textAlign:</span> '<span class="hljs-attr">center</span>', <span class="hljs-attr">width:</span> '<span class="hljs-attr">100px</span>' &#125;&#125;
  <span class="hljs-attr">className</span>=<span class="hljs-string">"button buttonPrimary buttonNoBig buttonRound"</span>
  <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setSort(!sort)&#125;
  >
  排序
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">标识获胜棋子</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c66ba1a0095f43289e88168378d2ce7e~tplv-k3u1fbpfcp-watermark.image" alt="7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重点：<strong>获胜时，获取到获胜棋子的编号，通过 prop 传递到棋子 <code>Square</code> 判断改变棋子样式</strong></p>
<h3 data-id="heading-15">样式</h3>
<blockquote>
<p>/src/global.css</p>
</blockquote>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 设置获胜样式 */</span>
<span class="hljs-selector-class">.winner</span> &#123;
  <span class="hljs-attribute">background</span>: firebrick <span class="hljs-meta">!important</span>;
  <span class="hljs-attribute">color</span>: white;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意需要 <code>!important</code> 否则优先级样式被覆盖。</p>
</blockquote>
<h3 data-id="heading-16">获胜棋子编号</h3>
<blockquote>
<p>/src/utils/index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 判断获胜棋子方法中</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">calculateWinner</span>(<span class="hljs-params">squares: string[]</span>) </span>&#123;
  <span class="hljs-keyword">const</span> lines = [
    [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>],
    [<span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>],
    [<span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>],
    [<span class="hljs-number">0</span>, <span class="hljs-number">3</span>, <span class="hljs-number">6</span>],
    [<span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">7</span>],
    [<span class="hljs-number">2</span>, <span class="hljs-number">5</span>, <span class="hljs-number">8</span>],
    [<span class="hljs-number">0</span>, <span class="hljs-number">4</span>, <span class="hljs-number">8</span>],
    [<span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">6</span>],
  ];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < lines.length; i++) &#123;
    <span class="hljs-keyword">const</span> [a, b, c] = lines[i];
    <span class="hljs-keyword">if</span> (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) &#123;
      <span class="hljs-comment">// 更改这一步，返回一个对象，包含获取棋子的编号 square</span>
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">winner</span>: squares[a], <span class="hljs-attr">square</span>: lines[i] &#125;;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>/src/pages/Gobang/index.tsx</p>
<p>更改判断 winner 的条件和传递获胜棋子数组</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx">- <span class="hljs-keyword">if</span> (calculateWinner(squares) || squares[i]) &#123;
+ <span class="hljs-keyword">if</span> (calculateWinner(squares)?.winner || squares[i]) &#123;
      <span class="hljs-keyword">return</span>;
&#125;
  
<span class="hljs-comment">// 当前棋盘</span>
<span class="hljs-keyword">const</span> current = history[stepNumber];
- <span class="hljs-keyword">const</span> winner = calculateWinner(current.squares);
+ <span class="hljs-keyword">const</span> calculate = calculateWinner(current.squares);
+ <span class="hljs-keyword">const</span> winner = calculate?.winner;
+ <span class="hljs-keyword">let</span> winSquare: <span class="hljs-built_in">number</span>[] | <span class="hljs-literal">undefined</span>;
  
<span class="hljs-comment">// 判断 winner 条件</span>
<span class="hljs-keyword">if</span> (winner) &#123;
  status = <span class="hljs-string">`Winner: <span class="hljs-subst">$&#123;winner&#125;</span>`</span>;
+ winSquare = calculate?.square;
<span class="hljs-comment">// ... 省略代码</span>

<span class="hljs-comment">// 传递 props</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.gameBoard&#125;</span>></span>
- <span class="hljs-tag"><<span class="hljs-name">Board</span> <span class="hljs-attr">squares</span>=<span class="hljs-string">&#123;current.squares&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;(i)</span> =></span> handleClick(i)&#125; />
+ <span class="hljs-tag"><<span class="hljs-name">Board</span> <span class="hljs-attr">squares</span>=<span class="hljs-string">&#123;current.squares&#125;</span> <span class="hljs-attr">winner</span>=<span class="hljs-string">&#123;winSquare&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;(i)</span> =></span> handleClick(i)&#125; />
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">棋盘判断获胜</h3>
<blockquote>
<p>/src/components/Board/index.tsx</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx">- <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Board</span>(<span class="hljs-params">props: &#123; squares: &#123; [x: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span> &#125;; onClick: (arg0: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span> &#125;</span>) </span>&#123;
+ <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Board</span>(<span class="hljs-params">props: &#123; squares: &#123; [x: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span> &#125;; winner?: <span class="hljs-built_in">number</span>[], onClick: (arg0: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span> &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> renderSquare = <span class="hljs-function">(<span class="hljs-params">i: <span class="hljs-built_in">number</span></span>) =></span> &#123;
    - <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Square</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;i&#125;</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;props.squares[i]&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> props.onClick(i)&#125; /></span>;
    + <span class="hljs-keyword">const</span> winner = props.winner?.includes(i);
    + <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Square</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;i&#125;</span> <span class="hljs-attr">winner</span>=<span class="hljs-string">&#123;winner&#125;</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;props.squares[i]&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> props.onClick(i)&#125; /></span>;
  &#125;;
<span class="hljs-comment">// ... 省略代码</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">棋格渲染</h3>
<blockquote>
<p>/src/components/Square/index.tsx</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx">- <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Square</span>(<span class="hljs-params">props: &#123; value: <span class="hljs-built_in">number</span>, onClick: () => <span class="hljs-built_in">void</span>; &#125;</span>) </span>&#123;
+ <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Square</span>(<span class="hljs-params">props: &#123; value: <span class="hljs-built_in">number</span>, winner?: <span class="hljs-built_in">boolean</span>, onClick: () => <span class="hljs-built_in">void</span>; &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
- <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.square&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> props.onClick()&#125;>
+ <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;</span>`$&#123;<span class="hljs-attr">props.winner</span> ? '<span class="hljs-attr">winner</span>' <span class="hljs-attr">:</span> ''&#125; $&#123;<span class="hljs-attr">styles.square</span>&#125;`&#125; <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> props.onClick()&#125;>
      &#123;props.value&#125;
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  );
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">平局</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6978163a7ad4e9bb35a56d7c5747cd4~tplv-k3u1fbpfcp-watermark.image" alt="8.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重点：<strong>很简单，判断一下历史条目的长度，改变显示内容</strong></p>
<h3 data-id="heading-20">Gobang 页面</h3>
<blockquote>
<p>/src/pages/Gobang/index.tsx</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">if</span> (winner) &#123;
  status = <span class="hljs-string">`Winner: <span class="hljs-subst">$&#123;winner&#125;</span>`</span>;
  winSquare = calculate?.square;
<span class="hljs-comment">// 判断长度，显示平局内容。</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (moves.length === <span class="hljs-number">10</span>) &#123;
  status = <span class="hljs-string">'Draw, start over game'</span>;
&#125; <span class="hljs-keyword">else</span> &#123;
  status = <span class="hljs-string">`Next player: <span class="hljs-subst">$&#123;xIsNext ? <span class="hljs-string">'X'</span> : <span class="hljs-string">'O'</span>&#125;</span>`</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-21">项目总览</h1>
<p>以上就是 Rax.js 重构 React 官方项目例子  <a href="https://link.juejin.cn/?target=https%3A%2F%2Freact.docschina.org%2Ftutorial%2Ftutorial.html" target="_blank" rel="nofollow noopener noreferrer" title="https://react.docschina.org/tutorial/tutorial.html" ref="nofollow noopener noreferrer">GoBang 井字棋小游戏</a> 并且<strong>实现进阶功能和优化项目</strong>的具体内容。下面简单进行项目总览：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4669b49ab194dea9341ed6565a16653~tplv-k3u1fbpfcp-watermark.image" alt="9.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-22">后言</h1>
<p>目前个人对于 React.js 和 Rax.js 的基础知识学习暂时到这里，后边在实际项目中成长，争取学习后继续与小友们总结分享~<br>
若学习过程有改进的地方，希望有大佬能给我指点一二。</p>
<blockquote>
<p>项目仓库：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flindadade%2Frax_travel_website" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lindadade/rax_travel_website" ref="nofollow noopener noreferrer">github</a>、
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Flin_daren%2Frax_travel_website" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/lin_daren/rax_travel_website" ref="nofollow noopener noreferrer">gitee</a></p>
</blockquote></div>  
</div>
            