
---
title: '纯 CSS Flex Box 响应式设计 - 故障动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef2575bfbfee4d60b37aa7a08b7e741b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 01:46:03 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef2575bfbfee4d60b37aa7a08b7e741b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h3 data-id="heading-0">使用 Flex Box，我们可以轻松地让我们的网页充当响应式容器</h3>
<p>首先，我们将快速创建一个包含以下 HTML 的文件</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"viewport flex-parent flex-col"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"nav flex-parent space-around"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-3"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content flex-parent"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sidebar-left"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main-area"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sidebar-right"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer flex-parent space-evenly"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-4"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-5"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-6"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是我们的整个页面</p>
<h2 data-id="heading-1">CSS</h2>
<p>我们要做的第一件事是对文档中的所有元素进行基本重置。这会将所有内容设置为边框框大小并删除所有边距和填充。</p>
<pre><code class="hljs language-css copyable" lang="css">*&#123;
        <span class="hljs-attribute">box-sizing</span>: border-box;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2"><code>.viewport</code></h3>
<p>我们现在可以创建<code>viewport</code>类。我们希望这个元素占据设备屏幕内的所有可用空间。<br>
只是为了强调视口的位置，我们还将给它一个大的黑色边框</p>
<pre><code class="hljs language-css copyable" lang="css">    <span class="hljs-selector-class">.viewport</span>&#123;
        <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100vh</span>;
        <span class="hljs-attribute">min-width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">5px</span> solid black;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们要让<code>viewport</code>具有响应式。<code>.viewport</code>现在是一个 Flex Box 容器！</p>
<pre><code class="hljs language-css copyable" lang="css">    <span class="hljs-selector-class">.flex-parent</span>&#123;
        <span class="hljs-attribute">display</span>: flex;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下 Flex Box 容器垂直显示，但我希望我们的<code>viewport flex-parent</code>元素水平显示。我们可以使用以下 flex 属性来实现这一点。</p>
<pre><code class="hljs language-css copyable" lang="css">    <span class="hljs-selector-class">.flex-col</span>&#123;
        <span class="hljs-attribute">flex-direction</span>: column;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">这就是 flex box 容器。</h2>
<h2 data-id="heading-4">现在我们可以开始创建 flex 里面的盒子了。</h2>
<h2 data-id="heading-5"><code>.nav</code></h2>
<p>第一个子元素将是<code>.nav</code>这是我们的一般标题区域。让我们制作<code>100%</code>容器的宽度和高度的宽度<code>20vh</code>。</p>
<pre><code class="hljs language-css copyable" lang="css">    <span class="hljs-selector-class">.nav</span>&#123;
        <span class="hljs-attribute">min-width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">min-height</span>: <span class="hljs-number">20vh</span>;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">5px</span> dashed blue;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为我们想在里面放置元素，所以<code>.nav</code>我们将给它类<code>.flex-parent</code>，我们还将在这里演示 Flex Box 的一个关键方面。</p>
<p>如果你曾经尝试过不使用 Flex Box 或 CSS 网格而使用纯 CSS 来定位某些东西，那么你就会知道要做到这一点有多困难。幸运的是，Flex Box 有一个名为的属性<code>justify-content</code>，可以通过多种方式为我们做到这一点。</p>
<h3 data-id="heading-6"><code>.space-around</code></h3>
<p>我们将使用以下代码在每个元素周围放置空白。</p>
<pre><code class="copyable">    .space-around&#123;
        justify-content: space-around;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7"><code>.space-evenly</code></h3>
<p>当我们在这里时，我们将创建另一个类供以后使用<code>space-evenly</code>，除了使用它的工作原理<code>space-around</code>与一个主要区别类似。随着<code>space-evenly</code>白色的左侧最远和最右边的元素的权利也将是间隔分布的一部分！</p>
<pre><code class="copyable">    .space-evenly&#123;
        justify-content: space-evenly;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该<code>justify-content</code>处理我们的<code>main axis</code>. 在这种情况下是<code>x axis</code>or <code>horizontal axis</code>。</p>
<h2 data-id="heading-8"><code>.nav</code> 内部元素</h2>
<p>现在我们可以去实现里面的元素了 <code>.nav</code></p>
<p>我希望能够在不影响另一个元素的情况下轻松更改一个元素的值。为此，我们将为每个元素创建一个不同的类。这不是完全必要的，但可以减轻以后的压力。</p>
<pre><code class="copyable">    .box-1&#123;
        min-width: 20vw;
        background-color: yellow;
    &#125;

    .box-2&#123;
        min-width: 20vw;
        background-color: purple;
    &#125;

    .box-3&#123;
        min-width: 20vw;
        background-color: red;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一看！内容不会从页面溢出，内部的所有内容都<code>.nav</code>随屏幕大小而变化！</p>
<h2 data-id="heading-9">我们现在可以设置其余元素的样式！</h2>
<p>首先我们将<code>.content</code>和<code>.footer</code>放到页面上</p>
<h3 data-id="heading-10"><code>.content</code></h3>
<pre><code class="copyable">    .content&#123;
        min-width: 100%;
        min-height: 80vh;
        border: 5px dashed orange;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11"><code>.footer</code></h3>
<pre><code class="copyable">    .footer&#123;
        min-width: 100%;
        min-height: 20vh;
        border: 5px solid cyan;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12"><code>.content</code> 内部元素</h2>
<h3 data-id="heading-13"><code>.sidebar-left</code></h3>
<pre><code class="copyable">    .sidebar-left&#123;
        min-width: 20%;
        background: teal;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14"><code>.main-area</code></h3>
<pre><code class="copyable">    .main-area&#123;
        min-width: 60%;
        background: green;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15"><code>.sidebar-right</code></h3>
<pre><code class="copyable">    .sidebar-right&#123;
        min-width: 20%;
        background: blue;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16"><code>.footer</code> 内部元素</h2>
<pre><code class="copyable">    .box-4&#123;
        min-width: 15%;
        background: pink;
    &#125;

    .box-5&#123;
        min-width: 30%;
        background: maroon;
    &#125;

    .box-6&#123;
        min-width: 20%;
        background: black;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">结果</h2>
<h3 data-id="heading-18">电脑</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef2575bfbfee4d60b37aa7a08b7e741b~tplv-k3u1fbpfcp-watermark.image" alt="1xo15ap1e3d43gua9eox.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">平板</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11ffd9a9051f4ad59993c94af968b0ce~tplv-k3u1fbpfcp-watermark.image" alt="qa9f670j1079j0q9mq4w.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-20">手机</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e6d0c9e151a45278c899ab4ea577f3a~tplv-k3u1fbpfcp-watermark.image" alt="5e9gxcvb60klvy1bbkb8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-21">最后</h2>
<p>我希望你对 Flex Box 是什么以及它如何更好地帮助我们轻松地进行响应式设计有更好的了解</p></div>  
</div>
            