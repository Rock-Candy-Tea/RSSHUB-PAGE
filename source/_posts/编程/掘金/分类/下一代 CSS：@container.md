
---
title: '下一代 CSS：@container'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4be6d1ff8df461db078df669d59ae14~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 06:58:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4be6d1ff8df461db078df669d59ae14~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://css-tricks.com/next-gen-css-container/" target="_blank" rel="nofollow noopener noreferrer">Next Gen CSS: @container</a></li>
<li>原文作者：<a href="https://css-tricks.com/author/unakravets/" target="_blank" rel="nofollow noopener noreferrer">Una Kravets</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/next-gen-css-container.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/PassionPenguin" target="_blank" rel="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：<a href="https://github.com/Chorer" target="_blank" rel="nofollow noopener noreferrer">Chorer</a>、<a href="https://github.com/KimYangOfCat" target="_blank" rel="nofollow noopener noreferrer">Kim Yang</a></li>
</ul>
</blockquote>
<p>Chrome 正在试验 CSS <code>@container</code> 查询器功能，这是由 <a href="https://css.oddbird.net/rwd/query/" target="_blank" rel="nofollow noopener noreferrer">Oddbird</a> 的 <a href="https://twitter.com/TerribleMia" target="_blank" rel="nofollow noopener noreferrer">Miriam Suzanne</a> 和一群网络平台开发者支持的 CSS 工作组 <a href="https://github.com/w3c/csswg-drafts/issues?q=is%3Aissue+label%3Acss-contain-3+" target="_blank" rel="nofollow noopener noreferrer">Containment Level 3 规范</a>。<code>@container</code> 查询器使我们能够<strong>根据父容器的大小来设置元素的样式</strong>。</p>
<blockquote>
<p><code>@container</code> API 不稳定，会受到语法变化的影响。如果你想要自己尝试一下，可能会遇到一些错误。请将这些错误报告给相应的浏览器引擎！<strong>报告错误的链接如下：</strong></p>
<ul>
<li><a href="https://bugs.chromium.org/p/chromium/issues/list" target="_blank" rel="nofollow noopener noreferrer">Chrome</a></li>
<li><a href="https://bugzilla.mozilla.org/home" target="_blank" rel="nofollow noopener noreferrer">Firefox</a></li>
<li><a href="https://bugs.webkit.org/query.cgi?format=specific&product=WebKit" target="_blank" rel="nofollow noopener noreferrer">Safari</a></li>
</ul>
</blockquote>
<p>你可以把这些想象成一个媒体查询（<code>@media</code>），但不是依靠 <strong>viewport</strong> 来调整样式，而是你的目标元素的父容器会调整这些样式。</p>
<h1 data-id="heading-0">容器查询将是自 CSS3 以来 Web 样式的最大变化，将会改变我们对“响应式设计”含义的看法。</h1>
<p>viewport 和用户代理不再是我们创建响应式布局和 UI 样式的唯一目标。通过容器查询，元素将能够定位自己的父元素并相应地应用自己的样式。这意味着存在于侧边栏、主体或头图中的相同元素可能会根据其可用大小和动态看起来完全不同。</p>
<h1 data-id="heading-1"><code>@container</code> 实例</h1>
<p>在<a href="https://codepen.io/una/pen/LYbvKpK" target="_blank" rel="nofollow noopener noreferrer">本示例</a>中，我在父级中使用了两张带有以下标记的卡片：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card-container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">figure</span>></span> ...<span class="hljs-tag"></<span class="hljs-name">figure</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"meta"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>...<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"time"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"notes"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"desc"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"links"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span>></span>...<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我在将查询容器样式的父级（<code>.card-container</code>）上设置 Containment（<a href="https://css-tricks.com/almanac/properties/c/contain/" target="_blank" rel="nofollow noopener noreferrer"><code>contain</code> 属性</a>）。我还在 <code>.card-container</code> 的父级上设置了一个相对网格布局，因此它的 <code>inline-size</code> 将根据该网格而改变。这就是我使用 <code>@container</code> 查询的内容：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.card-container</span> &#123;
  contain: layout inline-size;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我可以查询容器样式来调整样式！这与使用基于宽度的媒体查询设置样式的方式非常相似，当元素<strong>小于指定尺寸</strong>时使用 <code>max-width</code> 设置样式，当元素<strong>大于指定尺寸</strong>时使用 <code>min-width</code>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 当父容器宽度小于 850px，
不再显示 .links
并且减小 .time 字体尺寸 */</span>

<span class="hljs-keyword">@container</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">850px</span>) &#123;
  <span class="hljs-selector-class">.links</span> &#123;
    <span class="hljs-attribute">display</span>: none;
  &#125;

  <span class="hljs-selector-class">.time</span> &#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1.25rem</span>;
  &#125;

  <span class="hljs-comment">/* ... */</span>
&#125;

<span class="hljs-comment">/* 当父容器宽度小于 650px 时，
减小 .card 元素之间的网格间距到 1rem */</span>

<span class="hljs-keyword">@container</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">650px</span>) &#123;
  <span class="hljs-selector-class">.card</span> &#123;
    gap: <span class="hljs-number">1rem</span>;
  &#125;

  <span class="hljs-comment">/* ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4be6d1ff8df461db078df669d59ae14~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">容器查询 + 媒体查询</h1>
<p>容器查询的最佳功能之一是能够将 <strong>微观上的布局</strong> 与 <strong>宏观上的布局</strong> 分开。我们可以使用容器查询设置单个元素的样式，创建细微的微观布局，并使用媒体查询（宏布局）设置整个页面布局的样式。这创造了一个新的控制水平，使界面更具响应性。</p>
<p>这是<a href="https://codepen.io/una/pen/RwodQZw" target="_blank" rel="nofollow noopener noreferrer">另一个示例</a>。它展示了使用媒体查询进行宏观布局（即日历从单面板到多面板）和微观布局（即日期布局/大小和事件边距/大小移动），以创建一个漂亮的和谐的查询。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fee7ebefd5042faa80b93e33306958f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">容器查询 + CSS 网格</h1>
<p>我个人最喜欢的查看容器查询影响的方法之一是查看它们在网格中的工作方式。以下面的植物贸易 UI 为例：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1770158c891040b3943443df6c31a205~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本网站根本没有使用媒体查询。相反，我们只使用容器查询和 CSS 网格来在不同的视图中显示购物卡组件。</p>
<p>在产品网格中，布局使用了 <code>grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));</code> 标记创建。这将创建一个布局，告诉卡片占用可用的小数空间，直到它们的大小达到 <code>230px</code>，然后下一格切换到下一行。你可以在 <a href="http://1linelayouts.glitch.me/" target="_blank" rel="nofollow noopener noreferrer">1linelayouts.com</a> 上查看更多网格技巧。</p>
<p>然后，我们有一个容器查询，当卡片宽度小于 <code>350px</code> 时，它会将卡片样式设置为采用垂直块布局，并通过应用 <code>display: flex</code>（默认情况下具有内联流）转换为水平内联布局。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@container</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">350px</span>) &#123;
  <span class="hljs-selector-class">.product-container</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0.5rem</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
    <span class="hljs-attribute">display</span>: flex;
  &#125;

  <span class="hljs-comment">/* ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这意味着每张卡片<strong>拥有自己的响应式样式</strong>。这是我们使用产品网格创建宏观布局以及使用产品卡片创建微观布局的另一个示例，酷毙了！</p>
<h1 data-id="heading-4">用法</h1>
<p>为了使用<code>@container</code>，首先需要创建一个具有 <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/contain" target="_blank" rel="nofollow noopener noreferrer">Containment</a> 的父元素。为此，我们需要在父级上设置 <code>contain: layout inline-size</code>。因为我们目前只能将容器查询应用于内联轴，所以我们只可以使用 <code>inline-size</code>。这也可以防止我们的布局在块方向上中断。</p>
<p>设置 <code>contain: layout inline-size</code> 会创建一个新的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/Containing_block" target="_blank" rel="nofollow noopener noreferrer">Containment 块</a> 和新的<a href="https://developer.mozilla.org/zh-CN/docs/Web/Guide/CSS/Block_formatting_context" target="_blank" rel="nofollow noopener noreferrer">块格式上下文</a>，让浏览器将其与布局的其余部分分开，现在我们就可以使用容器查询了！</p>
<h1 data-id="heading-5">限制</h1>
<p>目前，您不能使用基于高度的容器查询，只能使用块轴方向上的查询。为了让网格子元素与 <code>@container</code> 一起工作，我们需要添加一个容器元素。尽管如此，添加容器仍可让我们获得所需的效果。</p>
<h1 data-id="heading-6">试试看</h1>
<p>您现在可以在 Chromium 中试验 <code>@container</code> 属性，方法是导航到：<a href="https://www.google.com/chrome/canary/" target="_blank" rel="nofollow noopener noreferrer">Chrome Canary</a> 中的 <code>chrome://flags</code> 页面并打开 <strong>#experimental-container-queries</strong> 标志。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b17ae737020246c8827bc6f49b940fc3~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            