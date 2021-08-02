
---
title: '【今天你更博学了么】一个神奇的前端动画 API requestAnimationFrame ｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6abbc01ab3864c71af8dd8ba5a39df23~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 19:28:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6abbc01ab3864c71af8dd8ba5a39df23~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">前言</h1>
<p>先上一个面试题：做前端少不了跟动画打交道，那么实现一个动画有哪些方式呢？</p>
<ul>
<li><strong>JavaScript</strong>：<code>setTimeout</code> 和 <code>setInterval</code></li>
<li><strong>Css3</strong>：<code>transition</code> 和 <code>animation</code></li>
<li><strong>Html</strong>：<code>canvas</code> 和 <code>SVG</code></li>
<li><strong>requestAnimationFrame</strong> <strong>API</strong></li>
<li>...</li>
<li>你还知道哪些方式可以实现动画?</li>
</ul>
<h1 data-id="heading-1">requestAnimationFrame  API</h1>
<h2 data-id="heading-2">是什么</h2>
<p>本文主要学习 <code>requestAnimationFrame API</code> ， 顾名思义，<strong>请求动画帧</strong>，也称 <strong>帧循环</strong>。</p>
<p>文中贴的 <code>js</code> 代码全都是真实代码，复制即可运行。</p>
<h2 data-id="heading-3">怎么玩</h2>
<p>我们学习一个东西，肯定是要先看看 <code>MDN</code> 怎么说的。</p>
<blockquote>
<p><strong>window.requestAnimationFrame()</strong>  </p>
<p>告诉浏览器——你希望执行一个动画，并且要求浏览器在下次重绘之前调用指定的回调函数更新动画。该方法需要传入一个回调函数作为参数，该回调函数会在浏览器下一次重绘之前执行。</p>
</blockquote>
<p><strong>浏览器的重绘与回流</strong> 后续会单独出一篇文章来学习。现在不懂也没关系，不影响我们学习 <code>requestAnimationFrame API</code> 。</p>
<p>我们先初步认识一下它，根据文档。我们给它传递一个回调函数 <code>test</code> 。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//html代码全文通用，所以只在此贴出一次</span>
<body>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>requestAnimationFrame API<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'begin'</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"begin"</span>></span>开始<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'end'</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"end"</span>></span>停止<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</body>

<span class="hljs-comment">//js</span>
(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀hello ~ requestAnimationFrame'</span>);
  &#125;
  requestAnimationFrame(test)
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，控制台成功的输出了一次 <code>log</code> 。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6abbc01ab3864c71af8dd8ba5a39df23~tplv-k3u1fbpfcp-watermark.image" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是它只执行了一次，怎么做动画呢？别急，再看看 <code>MDN</code> 怎么说。</p>
<blockquote>
<p><strong>注意：若你想在浏览器下次重绘之前继续更新下一帧动画，那么回调函数自身必须再次调用<code>window.requestAnimationFrame()</code></strong></p>
</blockquote>
<p>原来在回调函数中要再次调用 <code>requestAnimationFrame</code> 才可以，修改代码再试一下。</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">let</span> n = <span class="hljs-number">0</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
    n++
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`🚀🚀hello ~ requestAnimationFrame <span class="hljs-subst">$&#123;n&#125;</span>`</span>);
    requestAnimationFrame(test)
  &#125;
  requestAnimationFrame(test)
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下，确实是一直在执行了。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/868d062f031645d4a690a1c2ef33b5f4~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">执行频率</h2>
<p>这时候有小伙伴就要问了，我没有像 <code>setTimeout</code> 和 <code>setInterval</code> 那样设置时间，它为什么会间隔执行呢？</p>
<p>再看看文档怎么说。</p>
<blockquote>
<p>回调函数执行次数通常是每秒 <strong>60</strong> 次，但在大多数遵循 <code>W3C</code> 建议的浏览器中，回调函数执行次数通常与   <strong>浏览器屏幕刷新次数</strong> 相匹配。</p>
</blockquote>
<p>这回就知道了，原来它根本就不用手动设置执行间隔时间，而是根据 <strong>浏览器屏幕刷新次数</strong> 自动调整了,也就是说浏览器屏幕刷新多少次，它就执行多少次。看到这我只想说一句 <strong>厉害坏了</strong> 。</p>
<p>那么什么是 <strong>浏览器屏幕刷新次数</strong> 呢？</p>
<p><strong>屏幕刷新频率（次数）：</strong> 屏幕每秒出现图像的次数。普通笔记本为60Hz。</p>
<h2 data-id="heading-5">回调参数</h2>
<p>老规矩，先看文档。</p>
<blockquote>
<p>回调函数会被传入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FDOMHighResTimeStamp" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/DOMHighResTimeStamp" ref="nofollow noopener noreferrer"><code>DOMHighResTimeStamp</code></a>参数，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FDOMHighResTimeStamp" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/DOMHighResTimeStamp" ref="nofollow noopener noreferrer"><code>DOMHighResTimeStamp</code></a>指示当前被 <code>requestAnimationFrame()</code> 排序的回调函数被触发的时间。</p>
</blockquote>
<p>修改代码来看一下这个参数。</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params">timestamp</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`🚀🚀hello ~ requestAnimationFrame <span class="hljs-subst">$&#123;timestamp&#125;</span>`</span>);
    requestAnimationFrame(test)
  &#125;
  requestAnimationFrame(test)
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b645e5bf3f24d98ab0eb3ca23a18076~tplv-k3u1fbpfcp-watermark.image" alt="4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好家伙，精确到到小数点后三位。那么文档这段文字是什么意思呢？</p>
<blockquote>
<p>在同一个帧中的 <strong>多个回调函数</strong> ，它们每一个都会接受到一个 <strong>相同的时间戳</strong> ，即使在计算上一个回调函数的工作负载期间已经 <strong>消耗了一些时间</strong> 。该时间戳是一个十进制数，单位毫秒，最小精度为1ms(1000μs)。</p>
</blockquote>
<p>修改代码，我们同时执行两个 <code>requestAnimationFrame</code>  来看一下。</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test1</span>(<span class="hljs-params">timestamp</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`🚀🚀hello ~ requestAnimationFrame1 <span class="hljs-subst">$&#123;timestamp&#125;</span>`</span>);
    requestAnimationFrame(test1)
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test2</span>(<span class="hljs-params">timestamp</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`🚀🚀hello ~ requestAnimationFrame2 <span class="hljs-subst">$&#123;timestamp&#125;</span>`</span>);
    requestAnimationFrame(test2)
  &#125;
  requestAnimationFrame(test1)
  requestAnimationFrame(test2)

&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，两个 <code>requestAnimationFrame</code> 在控制台输出的时间戳是一样的。也就是浏览器刷新一次的时候，执行所有的 <code>requestAnimationFrame</code> ，并且它们的回调参数是一模一样的。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f779dd8e9fca40aa9aa8ba61b583fa4b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">浏览器的自我拯救</h2>
<blockquote>
<p>为了提高性能和电池寿命，因此在大多数浏览器里，当<code>requestAnimationFrame()</code> 运行在后台标签页或者隐藏的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTML%2FElement%2Fiframe" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/iframe" ref="nofollow noopener noreferrer"><code><iframe></code></a> 里时，<code>requestAnimationFrame()</code> 会被暂停调用以提升性能和电池寿命。</p>
</blockquote>
<p>这个就厉害了，你要是当时没有浏览页面，并且也没关掉，那么 <code>requestAnimationFrame() </code>一直在这跑，多消耗性能啊。人家开发者早都想到了，也就是说，只要你当前没看我，那我就偷懒了（<code>是不是跟你们上班一样，领导没盯着你，你就刷掘金摸鱼</code>）。</p>
<p>上个代码验证一下，为了方便，我添加了一个 <code>button</code> 。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> beginBtn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#begin"</span>)
  beginBtn.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">() =></span> &#123;
    requestAnimationFrame(test)
  &#125;)
  
  <span class="hljs-keyword">let</span> n = <span class="hljs-number">0</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
    n++
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`🚀🚀hello ~ requestAnimationFrame <span class="hljs-subst">$&#123;n&#125;</span>`</span>);
    requestAnimationFrame(test)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，控制台打印到一半（高度）的时候，我切到另一个页面，几秒钟后我切回来的时候，依然是接着一半的位置进行输出。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06944559d44f44b3896aea12d5fdb3d0~tplv-k3u1fbpfcp-watermark.image" alt="动画.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">返回值</h2>
<blockquote>
<p>一个 <code>long</code> 整数，请求 ID ，是回调列表中唯一的标识。是个非零值，没别的意义。</p>
</blockquote>
<p>以下代码点击开始的时候，输出 <code>requestAnimationFrame</code> 的返回值。可以看见，每执行一次，数值就会 <strong>+1</strong></p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> beginBtn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#begin"</span>)
  
  <span class="hljs-keyword">let</span> myRef;
  
  beginBtn.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">() =></span> &#123;
    myRef = requestAnimationFrame(test)
  &#125;)
  
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
    myRef = requestAnimationFrame(test)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ myRef:'</span>, myRef);
  &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5986620e466b417caff52b5806c71e3c~tplv-k3u1fbpfcp-watermark.image" alt="44.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">终止执行</h2>
<blockquote>
<p>你可以传这个值给 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWindow%2FcancelAnimationFrame" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Window/cancelAnimationFrame" ref="nofollow noopener noreferrer"><code>window.cancelAnimationFrame()</code></a> 以取消回调函数。</p>
</blockquote>
<p>那如果我想要在特定的条件下终止 <code>requestAnimationFrame</code> 怎么办呢，官方也给出了答案，那就是
<code>cancelAnimationFrame API</code> 。 只需要把 <code>requestAnimationFrame</code> 的返回值作为参数传递给 <code>cancelAnimationFrame</code> 就可以了。</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> beginBtn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#begin"</span>)

  <span class="hljs-keyword">const</span> endBtn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#end"</span>)

  <span class="hljs-keyword">let</span> myRef;

  beginBtn.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">() =></span> &#123;
    myRef = requestAnimationFrame(test)
  &#125;)

  endBtn.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">() =></span> &#123;
    cancelAnimationFrame(myRef)
  &#125;)

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
    myRef = requestAnimationFrame(test)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ myRef:'</span>, myRef);
  &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，当我点击开始的时候控制台持续输出内容，当我点击停止的时候，控制台停止输出。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0517eae946ef4d2780941dd4f67cc983~tplv-k3u1fbpfcp-watermark.image" alt="动画3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实不用这个 <code>API</code> 也可以达到终止执行的目的，比如简单的 <code>if语句</code> 。</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params">timestamp</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`🚀🚀hello ~ requestAnimationFrame <span class="hljs-subst">$&#123;timestamp&#125;</span>`</span>);
    <span class="hljs-keyword">if</span> (timestamp < <span class="hljs-number">500</span>) &#123;
      requestAnimationFrame(test)
    &#125;
  &#125;
  requestAnimationFrame(test)
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，当 <code>timestamp</code> 超过500的时候就停止了。当然还有更多可能性，这就要靠小伙伴们开动聪明的脑袋瓜子了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e6797870f5343bb884ea3d8d937932e~tplv-k3u1fbpfcp-watermark.image" alt="445.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">小技巧</h2>
<p>我们这样就可以把每两次执行的时间间隔传递给外部使用了。外部拿到以后就可以搞事情了，比如时间间隔累加到 <strong>1000</strong> 就执行什么什么操作~</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">let</span> startTime = <span class="hljs-built_in">Date</span>.now();

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleTicker</span>(<span class="hljs-params"></span>) </span>&#123;
    foo(<span class="hljs-built_in">Date</span>.now() - startTime);
    startTime = <span class="hljs-built_in">Date</span>.now();
    requestAnimationFrame(handleTicker);
  &#125;

  requestAnimationFrame(handleTicker);

  <span class="hljs-keyword">let</span> t = <span class="hljs-number">0</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">timeInterval</span>) </span>&#123;
    t += timeInterval
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ t:'</span>, t);
    <span class="hljs-keyword">if</span> (t > <span class="hljs-number">1000</span>) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ 搞事情'</span>);
      t = <span class="hljs-number">0</span>
    &#125;
  &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，当 <code>t</code> 累加大于 <code>1000</code> 的时候，就搞了一次事情，然后重置 <code>t</code> ，以此类推。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c33318385d3e4b5993bf8f275f7b9b3d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">动画演示</h2>
<p>标题都说是一个神器的动画 <code>API</code> 了，不假装贴个动画就会被说 <strong>“标题党”</strong> 了。所以我还是决定实现一个简单的 <code>demo</code> 吧。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-id">#box</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">background-color</span>: blue;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>requestAnimationFrame API<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'begin'</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"begin"</span>></span>开始<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'end'</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"end"</span>></span>停止<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'box'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> beginBtn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#begin"</span>)
  <span class="hljs-keyword">const</span> endBtn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#end"</span>)
  <span class="hljs-keyword">const</span> box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#box"</span>)
  <span class="hljs-keyword">let</span> myRef;

  beginBtn.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">() =></span> &#123;
    myRef = requestAnimationFrame(test)
  &#125;)

  endBtn.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">() =></span> &#123;
    cancelAnimationFrame(myRef)
  &#125;)

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
    box.style.width = <span class="hljs-string">`<span class="hljs-subst">$&#123;myRef&#125;</span>%`</span>
    myRef = requestAnimationFrame(test)
  &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d62ea51c9c1a447ca58aef278f4701cc~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">兼容性</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/211d1616c25e468389725da9bbdf17cc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>兼容性如图所示，这里放出链接，小伙伴们需要查阅详情的话请点击自行查找。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/" ref="nofollow noopener noreferrer">Can I Use</a></p>
<p>这篇文章讲了一些底层原理，并且给出了 <code>requestAnimationFrame</code> 的全平台兼容处理，本人并没有替大家探雷，有需求的自行冲浪 ~</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Flibin-1%2Fp%2F6099746.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/libin-1/p/6099746.html" ref="nofollow noopener noreferrer">深入理解requestAnimationFrame</a></p>
<h1 data-id="heading-12">比试比试</h1>
<h2 data-id="heading-13">setTimeout && setInterval</h2>
<p><code>setTimeout</code> 和 <code>setInterval</code> 的问题是，它们不够精确。它们的内在运行机制决定了 <strong>时间间隔参数</strong> 实际上只是指定了把动画代码添加到 <strong>浏览器UI线程队列</strong> 中以等待执行的时间。如果队列前面已经加入了其它任务，那动画代码就要等前面的 <strong>任务完成后</strong> 再执行，并且如果时间间隔过短（小于16.7ms）会造成丢帧，所以就会导致动画可能不会按照预设的去执行，降低用户体验。</p>
<p><code>requestAnimationFrame</code> 采用 <strong>浏览器时间间隔</strong> ，保持最佳绘制效率，不会因为间隔时间过短，造成过度绘制，消耗性能；也不会因为间隔时间太长，使用动画卡顿不流畅，让各种网页动画效果能够有一个 <strong>统一</strong> 的刷新机制，从而节省系统资源，提高系统性能，改善视觉效果。</p>
<h2 data-id="heading-14">CSS3动画</h2>
<p><code>CSS3</code> 的<code>transition</code> 和 <code>animation</code> 搭配使用可以说是非常强大了，但是也有的触手伸不到的地方，比如说
<code>scrollTop</code>，另外 <code>CSS3</code> 动画支持的贝塞尔曲线也是有限的。</p>
<p>那么，<code>CSS3</code> 做不到的就可以用到 <code>requestAnimationFrame</code> 来解决了。</p>
<h1 data-id="heading-15">参考</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWindow%2FrequestAnimationFrame" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Window/requestAnimationFrame" ref="nofollow noopener noreferrer">MDN window.requestAnimationFrame</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Flibin-1%2Fp%2F6099746.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/libin-1/p/6099746.html" ref="nofollow noopener noreferrer">深入理解requestAnimationFrame</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/" ref="nofollow noopener noreferrer">Can I Use</a></p></div>  
</div>
            