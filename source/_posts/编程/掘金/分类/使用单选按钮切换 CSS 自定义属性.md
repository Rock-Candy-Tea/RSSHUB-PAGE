
---
title: '使用单选按钮切换 CSS 自定义属性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecb89acc075b4901b5d438389f353fef~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 06:40:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecb89acc075b4901b5d438389f353fef~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
</blockquote>
<p>我们有一组单选按钮，分别切换不同的背景颜色，其主要结构如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"controls"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"color"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"night-fade"</span> <span class="hljs-attr">checked</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"color"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"warm-flame"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"color"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"spring-warmth"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以往，我们可以使用 JavaScript 来检测用户何时与单选按钮交互并相应地附加一个类。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> bgColor = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'body'</span>)
<span class="hljs-keyword">const</span> controls = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.controls'</span>)

<span class="hljs-keyword">let</span> currentClass = <span class="hljs-string">'night-fade'</span>

<span class="hljs-keyword">const</span> onChange = <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (!e.target.value || !e.target.checked) <span class="hljs-keyword">return</span>

  <span class="hljs-keyword">if</span> (bgColor.classList.contains(currentClass)) &#123;
    bgColor.classList.replace(currentClass, e.target.value)
  &#125; <span class="hljs-keyword">else</span> &#123;
    bgColor.classList.add(e.target.value)
  &#125;

  currentClass = e.target.value
&#125;

controls.addEventListener(<span class="hljs-string">'change'</span>, onChange)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们为每个类添加 CSS <code>background-image</code> 来切换背景：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to top, <span class="hljs-number">#a18cd1</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#fbc2eb</span> <span class="hljs-number">100%</span>);
&#125;

<span class="hljs-selector-tag">body</span><span class="hljs-selector-class">.warm-flame</span> &#123;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">45deg</span>, <span class="hljs-number">#ff9a9e</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#fad0c4</span> <span class="hljs-number">99%</span>, <span class="hljs-number">#fad0c4</span> <span class="hljs-number">100%</span>);
&#125;

<span class="hljs-selector-tag">body</span><span class="hljs-selector-class">.spring-warmth</span> &#123;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to top, <span class="hljs-number">#fad0c4</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#ffd1ff</span> <span class="hljs-number">100%</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecb89acc075b4901b5d438389f353fef~tplv-k3u1fbpfcp-watermark.image" alt="b7e2e755-9df1-45c0-bc20-c73fb479359a (1).gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然而，现在我们可以有更好的选择：<strong>CSS 自定义属性（也称变量）</strong>。它可以使你的 CSS、JS 看起来更加简洁、方便，我们同样使用它来完成上面的效果。</p>
<h2 data-id="heading-0">自定义属性</h2>
<p>我们可以全局范围内，也就是 <code>:root</code> 内为接下来需要用到背景色值，都分配一个自定义属性：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-pseudo">:root</span> &#123;
  --bg-<span class="hljs-attribute">color</span>-night-fade: <span class="hljs-built_in">linear-gradient</span>(to top, <span class="hljs-number">#a18cd1</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#fbc2eb</span> <span class="hljs-number">100%</span>);
  --bg-<span class="hljs-attribute">color</span>-warm-flame: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">45deg</span>, <span class="hljs-number">#ff9a9e</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#fad0c4</span> <span class="hljs-number">99%</span>, <span class="hljs-number">#fad0c4</span> <span class="hljs-number">100%</span>);
  --bg-<span class="hljs-attribute">color</span>-spring-warmth: <span class="hljs-built_in">linear-gradient</span>(to top, <span class="hljs-number">#fad0c4</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#ffd1ff</span> <span class="hljs-number">100%</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们在本地范围内，也就是需要应用背景色的元素内（这里是 <code>body</code>）定义了一个新的 <code>--bg-color</code> 变量指定一个初始背景色。它将用于后面在单选按钮改变时，通过 JS 动态改变 <code>--bg-color</code> 内的值，使得 <code>background-image</code> 和 <code>--bg-color</code> 同步更新。</p>
<p>我们使用第一个 <code>--bg-color-night-fade</code> 变量作为第一个单选按钮选项相对应的初始值：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
  --bg-<span class="hljs-attribute">color</span>: <span class="hljs-built_in">var</span>(--bg-color-night-fade);
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">var</span>(--bg-color);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，监听表单下单选按钮的 <code>change</code>，在 <code>onChange</code> 事件处理程序中，我们使用与所选 <code>radio</code> 相对应的自定义属性更新 <code>--bg-color</code> 的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> bgColor = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'body'</span>)
<span class="hljs-keyword">const</span> controls = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.controls'</span>)

<span class="hljs-keyword">const</span> onChange = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (!e.target.value || !e.target.checked) <span class="hljs-keyword">return</span>
  
  bgColor.style.setProperty(<span class="hljs-string">'--bg-color'</span>, <span class="hljs-string">`var(--bg-color-<span class="hljs-subst">$&#123;e.target.value&#125;</span>)`</span>)
&#125;

controls.addEventListener(<span class="hljs-string">'change'</span>, onChange)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以在这👉<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Flio-zero%2Fpen%2FbGqqRqe" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/lio-zero/pen/bGqqRqe" ref="nofollow noopener noreferrer">查看效果</a>。</p></div>  
</div>
            