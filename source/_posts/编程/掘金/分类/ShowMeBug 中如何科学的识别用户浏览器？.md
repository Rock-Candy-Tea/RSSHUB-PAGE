
---
title: 'ShowMeBug 中如何科学的识别用户浏览器？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a22e9cb8383a411ab5099e145c32f5e2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 01:10:00 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a22e9cb8383a411ab5099e145c32f5e2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>经常有用户在 ShowMeBug 在线面试过程中，使用一些奇怪的浏览器来打开链接进行视频面试，然后出现一些音视频卡顿等问题。</p>
<p>多次排查后发现产品的音视频功能一但使用了浏览器的 WebRTC 特性，就会对浏览器的要求特别高，如不在正常的浏览器支持范围内，就容易出现问题。所以我们在检测这个问题时，通常有两种方法识别出浏览器的型号和版本。</p>
<p><strong>第一种方法</strong>：使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmodernizr.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://modernizr.com/" ref="nofollow noopener noreferrer">modernizr</a> 来进行 <code>feature detection</code>， 通过探测这些 API 是否存在，来判读是否可以使用 WebRTC，毕竟 WebRTC 是有浏览器 API 组成。</p>
<p>不过，这种方法不够严谨，WebRTC 是一项很新的技术，今年 1 月份才正式成为官方标准，但目前只支持部份浏览器，稳定性也还需要进一步加强。</p>
<blockquote>
<p>The World Wide Web Consortium (W3C) and the Internet Engineering Task Force (IETF) announced today that Web Real-Time Communications (WebRTC), which powers myriad services, is now an official standard, bringing audio and video communications anywhere on the Web.</p>
<p>今年 1 月，W3C 和 IETF 宣布，为无数服务提供支持的 WebRTC 现已成为官方标准。</p>
<p><em>———— 2021.01.26</em></p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2F2021%2F01%2Fpressrelease-webrtc-rec.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/2021/01/pressrelease-webrtc-rec.html" ref="nofollow noopener noreferrer">网络实时通信 (WebRTC) 改变了通信格局；成为万维网联盟 (W3C) 建议书和多个互联网工程任务组 (IETF) 标准</a></p>
<p>显然，feature detection 不符合我们的应用场景，目前不满足我们的需求，所以此方法 pass。</p>
<p><strong>第二种方法</strong>，也是我们目前采用的，业内比较通用的办法就是检测 User-Agent。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">curl http:<span class="hljs-comment">//202.38.95.46:12001/ -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) HEICORE/49.1.2623.213 Safari/537.36"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-0">User-Agent 是什么</h3>
<p>用户不能直接去互联网上获取信息，需要一个软件作为载体去代表用户的行为，这个软件就是 User-Agent （用户代理），浏览器就是一种典型的 User-Agent 。</p>
<p>用户使用不同的软件去用统一的协议去做相同的事情。这也是定义在 http 请求里的，每一条 http 请求一定会携带 User-Agent 头 。</p>
<p>网站的服务者可以通过 User-Agent 头来判断用户使用了什么浏览器，当然也可以根据 User-Agent 的内容来提供差异化的服务。</p>
<h3 data-id="heading-1">标准语法和历史</h3>
<p>原本 User-Agent 浏览器的语法是很清晰的</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">User-Agent: <product> / <product-version> <comment>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTTP%2FHeaders%2FUser-Agent" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent" ref="nofollow noopener noreferrer">User-Agent - HTTP | MDN</a></p>
<p>因为可以根据 User-Agent 的内容来提供差异化的服务，所以当年在浏览器大战时期，浏览器的实现各不相同。当年 Mozilla （Firefox 的前身）浏览器最强的，很多网站都只对 Mozilla 提供高质量的服务，后来有人把自己伪装成了 Mozilla （没错，就是 IE 先开始的）。从此 <code>Mozilla/5.0</code> 就变成了 User-Agent 的第一段。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebaim.org%2Fblog%2Fuser-agent-string-history%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webaim.org/blog/user-agent-string-history/" ref="nofollow noopener noreferrer">History of the browser user-agent string</a></p>
<p>后来的浏览就在这上面不断扩充，就像今天这样：</p>
<p>Linux / Firefox</p>
<pre><code class="hljs language-bash copyable" lang="bash">Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Mac OS / Safari</p>
<pre><code class="hljs language-bash copyable" lang="bash">Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Chromium OS  / Chrome</p>
<pre><code class="hljs language-bash copyable" lang="bash">Mozilla/5.0 (X11; CrOS x86_64 13904.16.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.25 Safari/537.36
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Windows / Edge</p>
<pre><code class="hljs language-bash copyable" lang="bash">Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4482.0 Safari/537.36 Edg/92.0.874.0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就变成了去识别 User-Agent 变得很困难，目前的识别基本上都是使用正则表达式，配合自己的 User-Agent 库来判断。</p>
<p>这方面的库有很多，对比很多后，这个库是比较全的
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fua-parser-js" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/ua-parser-js" ref="nofollow noopener noreferrer">ua-parser-js</a></p>
<p>目前几乎所有的网站识别浏览器都是 User-Agent 来判断，有两个接口：</p>
<p>前端有浏览器接口：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">window</span>.navigator.userAgent
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后端可以通过浏览器的 http request header 来拿到 User-Agent</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">user-agent: Mozilla/<span class="hljs-number">5.0</span> (Macintosh; Intel Mac OS X <span class="hljs-number">10_15_7</span>) AppleWebKit/<span class="hljs-number">537.36</span> (KHTML, like Gecko) Chrome/<span class="hljs-number">92.0</span><span class="hljs-number">.4515</span><span class="hljs-number">.107</span> Safari/<span class="hljs-number">537.36</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">如何使用 User-Agent</h3>
<p>在移动端因为算力的问题，在有些老旧的处理器上也会出现卡顿的情况，不过，我们可以在浏览器里跑一下 Benchmark 来判断算力是否够用，移动端的 User-Agent 会携带处理器信息（可以去查数据库来判断）</p>
<p>所以说，目前所进行的操作是：<strong>检测用户浏览器 ——> 给予提示，并在文档页显示支持性列表</strong></p>
<p>最后，要通过定义的规则生成这样一个表格：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a22e9cb8383a411ab5099e145c32f5e2~tplv-k3u1fbpfcp-watermark.image" alt="Screen_Shot_2021-08-13_at_17.09.59.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了降低未来的维护成本要使用一套数据源，既可以检测，又可以在文档页生成列表</p>
<p><code>ua-parser-js</code> 的返回结果的数据结构比较科学，直接复用这一数据结构</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">interface</span> Result &#123;
  <span class="hljs-attr">ua</span>: <span class="hljs-built_in">string</span>;
  browser: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
    version: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
  &#125;;
  device: &#123;
    <span class="hljs-attr">model</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
    <span class="hljs-keyword">type</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
    vendor: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
  &#125;;
  engine: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
    version: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
  &#125;;
  os: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
    version: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
  &#125;;
  cpu: &#123;
    <span class="hljs-attr">architecture</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们可以定义三条规则：</p>
<ul>
<li><code>daily_list</code> （某个测试版的浏览器）</li>
<li><code>white_list</code> （测试过没有问题的浏览器）</li>
<li><code>black_list</code> （已知有问题的浏览器）</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 存在优先级关系: daily_list > white_list > black_list</span>
<span class="hljs-comment">//</span>
<span class="hljs-comment">// https://www.npmjs.com/package/ua-parser-js</span>
<span class="hljs-comment">// @params: ua-parser-js.result</span>
<span class="hljs-comment">// @params: &#123; <list_name>: <whiteList | blackList>&#125;</span>
<span class="hljs-comment">// @return: string(list_name)</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">browserDetect</span>(<span class="hljs-params">ua, list</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; daily_list, white_list, black_list &#125; = list
  <span class="hljs-keyword">if</span> (checkList(ua, daily_list)) <span class="hljs-keyword">return</span> <span class="hljs-string">'daily_list'</span>
  <span class="hljs-keyword">if</span> (checkList(ua, white_list)) <span class="hljs-keyword">return</span> <span class="hljs-string">'white_list'</span>
  <span class="hljs-keyword">if</span> (checkList(ua, black_list)) <span class="hljs-keyword">return</span> <span class="hljs-string">'black_list'</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于这种数据结构，加入一种简单的语法。支持版本号判断，加入这个几种符号的支持：<code>></code>, <code>≥</code>, <code>=</code>, <code><</code>, <code>≤</code></p>
<p>由于没有现成可以用的，所以要自己写一段判断</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fcompare-versions" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/compare-versions" ref="nofollow noopener noreferrer">compare-versions</a></p>
<p>这样的话配置文件就可以这样写：<code>config/browser.yml</code></p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-comment"># https://www.npmjs.com/package/ua-parser-js</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># 本文件的语法是在这个库之上做的修改</span>

<span class="hljs-comment"># 白名单，完全没有问题的版本</span>
<span class="hljs-attr">white_list:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">browser:</span>
      <span class="hljs-attr">name:</span> <span class="hljs-string">"Chrome"</span>
      <span class="hljs-attr">version:</span> <span class="hljs-string">">= 85.0.0.0"</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">browser:</span>
      <span class="hljs-attr">name:</span> <span class="hljs-string">"Firefox"</span>
      <span class="hljs-attr">version:</span> <span class="hljs-string">">= 85.0.0.0"</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">browser:</span>
      <span class="hljs-attr">name:</span> <span class="hljs-string">"Edge"</span>
      <span class="hljs-attr">version:</span> <span class="hljs-string">">= 45.0.0.0"</span>
    <span class="hljs-attr">device:</span>
      <span class="hljs-attr">type:</span> <span class="hljs-string">"mobile"</span>
    <span class="hljs-attr">os:</span>
      <span class="hljs-attr">name:</span> <span class="hljs-string">"Android"</span>
      <span class="hljs-attr">version:</span> <span class="hljs-string">">= 10.0"</span>

<span class="hljs-attr">black_list:</span>
  <span class="hljs-comment"># 老版本的 Edge 不支持</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">browser:</span>
      <span class="hljs-attr">name:</span> <span class="hljs-string">"Edge"</span>
      <span class="hljs-attr">version:</span> <span class="hljs-string">"< 80.0.0.0"</span>
    <span class="hljs-attr">os:</span>
      <span class="hljs-attr">name:</span> <span class="hljs-string">"Windows"</span>

  <span class="hljs-comment"># 手机微信内置浏览器</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">browser:</span>
      <span class="hljs-attr">name:</span> <span class="hljs-string">"WeChat"</span>
    <span class="hljs-attr">device:</span>
      <span class="hljs-attr">type:</span> <span class="hljs-string">"mobile"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用我们产品的用户，上至自己编译浏览器自己用的极客，下至用微信内置浏览器的小白，
所以要在 beta 版、dev 版、canary 开发版、nightly 版等各种版本中给予提示，检测 WebRTC 不稳定，就可能会有问题。</p>
<blockquote>
<p>曾经有人用了开发版的浏览器，面试中出现音视频不稳定，直到他更新了的版本之后才恢复正常。</p>
</blockquote>
<p>由于开发版浏览器并不会在 ua 里面携带 dev 的标识，只能通过版本号来判断。可以使用 caniuse-lite 的数据库，取出最新稳定版的的版本号，然后进行版本号比对。</p>
<p>但是 caniuse-lite 的数据库有 <code>1.3M</code> 如果直接使用，会打包整个数据库。这个体积的增加了太多，需要优化一下，所以采用把查询结果打包成文件的办法，实际上真正有用的数据非常的少。</p>
<p>创建一个生成器，可以动态创建这个文件 <code>latest_browser_list_generator.js</code></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-meta">#!/usr/bin/env node</span>

<span class="hljs-keyword">const</span> browserslist = <span class="hljs-built_in">require</span>(<span class="hljs-string">'browserslist'</span>)
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)

<span class="hljs-keyword">const</span> list = &#123;
  <span class="hljs-string">'firefox'</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-string">'chrome'</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-string">'edge'</span>: <span class="hljs-literal">true</span>,
&#125;

<span class="hljs-keyword">const</span> latest = browserslist(<span class="hljs-string">"last 1 version"</span>).filter(<span class="hljs-function"><span class="hljs-params">i</span> =></span> list[i.split(<span class="hljs-string">' '</span>)[<span class="hljs-number">0</span>]])
fs.writeFileSync(<span class="hljs-string">'latest_browser_list.js'</span>, <span class="hljs-string">`export default <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(latest)&#125;</span>`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后定期执行这两个就可以了</p>
<ul>
<li><code>npx browserslist@latest --update-db</code></li>
<li><code>node latest_browser_list_generator.js</code></li>
</ul>
<p>当然，这个可以用 GitHub action 或 GitLab CI 来每周执行一次</p>
<h3 data-id="heading-3">除此之外，360 浏览器的检测方法</h3>
<p>360 浏览器隐藏了自己的 UA 。360 浏览器只有在访问自己的网站（比如：<code>360.cn</code>）是才会在 UA 里携带 <code>QIHU 360SE</code> （360 安全浏览器）或 <code>QIHU 360EE</code> （360 极速浏览器）字段</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.v2ex.com%2Ft%2F425627" target="_blank" rel="nofollow noopener noreferrer" title="https://www.v2ex.com/t/425627" ref="nofollow noopener noreferrer">360 安全浏览器和 360 极速浏览器的判断 - V2EX</a></p>
<p>对待国内浏览器（这个可以检测到 360）</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmumuy%2Fbrowser" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mumuy/browser" ref="nofollow noopener noreferrer">GitHub - mumuy/browser: Useragent analysis tool.浏览器分析判断工具 - 用户代理、操作系统信息</a></p>
<p>不过这个库的作者并没有提供可以直接使用包，只能把核心代码提取出来。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">  <span class="hljs-comment">// https://github.com/mumuy/browser/blob/4a50ee18cc76a5013dea3596bb33fbab9ed584c3/Browser.js#L111-L143</span>
  <span class="hljs-keyword">if</span> (_window.chrome) &#123;
    <span class="hljs-keyword">let</span> chrome_version = u.replace(<span class="hljs-regexp">/^.*Chrome\/([\d]+).*$/</span>, <span class="hljs-string">'$1'</span>)
    <span class="hljs-keyword">if</span> (_window.chrome.adblock2345 || _window.chrome.common2345) &#123;
      match[<span class="hljs-string">'2345Explorer'</span>] = <span class="hljs-literal">true</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
      _mime(<span class="hljs-string">'type'</span>, <span class="hljs-string">'application/360softmgrplugin'</span>) ||
      _mime(<span class="hljs-string">'type'</span>, <span class="hljs-string">'application/mozilla-npqihooquicklogin'</span>)
    ) &#123;
      is360 = <span class="hljs-literal">true</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (chrome_version > <span class="hljs-number">36</span> && _window.showModalDialog) &#123;
      is360 = <span class="hljs-literal">true</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (chrome_version > <span class="hljs-number">45</span>) &#123;
      is360 = _mime(<span class="hljs-string">'type'</span>, <span class="hljs-string">'application/vnd.chromium.remoting-viewer'</span>)
      <span class="hljs-keyword">if</span> (!is360 && chrome_version >= <span class="hljs-number">69</span>) &#123;
        is360 = _mime(<span class="hljs-string">'type'</span>, <span class="hljs-string">'application/hwepass2001.installepass2001'</span>) || _mime(<span class="hljs-string">'type'</span>, <span class="hljs-string">'application/asx'</span>)
      &#125;
    &#125;
  &#125;

  <span class="hljs-comment">// 修正</span>
  <span class="hljs-keyword">if</span> (match[<span class="hljs-string">'Mobile'</span>]) &#123;
    match[<span class="hljs-string">'Mobile'</span>] = !(u.indexOf(<span class="hljs-string">'iPad'</span>) > -<span class="hljs-number">1</span>)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (is360) &#123;
    <span class="hljs-keyword">if</span> (_mime(<span class="hljs-string">'type'</span>, <span class="hljs-string">'application/gameplugin'</span>)) &#123;
      match[<span class="hljs-string">'360SE'</span>] = <span class="hljs-literal">true</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
      _navigator &&
      <span class="hljs-keyword">typeof</span> _navigator[<span class="hljs-string">'connection'</span>] !== <span class="hljs-string">'undefined'</span> &&
      <span class="hljs-keyword">typeof</span> _navigator[<span class="hljs-string">'connection'</span>][<span class="hljs-string">'saveData'</span>] == <span class="hljs-string">'undefined'</span>
    ) &#123;
      match[<span class="hljs-string">'360SE'</span>] = <span class="hljs-literal">true</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      match[<span class="hljs-string">'360EE'</span>] = <span class="hljs-literal">true</span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过这里要注意：<code>navigator.mimeTypes</code> 已经从 Web 标准中移除（也许未来的某天这个方法就没法用了）</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigator%2FmimeTypes" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/Navigator/mimeTypes" ref="nofollow noopener noreferrer">Navigator.mimeTypes - Web APIs | MDN</a></p>
<p>判断 360 的版本，是做了一个版本的对应关系</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// https://github.com/mumuy/browser/blob/4a50ee18cc76a5013dea3596bb33fbab9ed584c3/Browser.js#L283-L292</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get360SEVersion</span>(<span class="hljs-params">u</span>) </span>&#123;
  <span class="hljs-keyword">let</span> hash = &#123; <span class="hljs-string">'86'</span>: <span class="hljs-string">'13.0'</span>, <span class="hljs-string">'78'</span>: <span class="hljs-string">'12.0'</span>, <span class="hljs-string">'69'</span>: <span class="hljs-string">'11.0'</span>, <span class="hljs-string">'63'</span>: <span class="hljs-string">'10.0'</span>, <span class="hljs-string">'55'</span>: <span class="hljs-string">'9.1'</span>, <span class="hljs-string">'45'</span>: <span class="hljs-string">'8.1'</span>, <span class="hljs-string">'42'</span>: <span class="hljs-string">'8.0'</span>, <span class="hljs-string">'31'</span>: <span class="hljs-string">'7.0'</span>, <span class="hljs-string">'21'</span>: <span class="hljs-string">'6.3'</span> &#125;
  <span class="hljs-keyword">let</span> chrome_version = u.replace(<span class="hljs-regexp">/^.*Chrome\/([\d]+).*$/</span>, <span class="hljs-string">'$1'</span>)
  <span class="hljs-keyword">return</span> hash[chrome_version] || <span class="hljs-string">''</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get360EEVersion</span>(<span class="hljs-params">u</span>) </span>&#123;
  <span class="hljs-keyword">let</span> hash = &#123; <span class="hljs-string">'86'</span>: <span class="hljs-string">'13.0'</span>, <span class="hljs-string">'78'</span>: <span class="hljs-string">'12.0'</span>, <span class="hljs-string">'69'</span>: <span class="hljs-string">'11.0'</span>, <span class="hljs-string">'63'</span>: <span class="hljs-string">'9.5'</span>, <span class="hljs-string">'55'</span>: <span class="hljs-string">'9.0'</span>, <span class="hljs-string">'50'</span>: <span class="hljs-string">'8.7'</span>, <span class="hljs-string">'30'</span>: <span class="hljs-string">'7.5'</span> &#125;
  <span class="hljs-keyword">let</span> chrome_version = u.replace(<span class="hljs-regexp">/^.*Chrome\/([\d]+).*$/</span>, <span class="hljs-string">'$1'</span>)
  <span class="hljs-keyword">return</span> hash[chrome_version] || <span class="hljs-string">''</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">最后</h2>
<p>虽然我们分享了如何科学识别检测用户浏览器的方法，但是为了网络环境的健康，为了不重蹈浏览器大战时的覆辙，呼吁大家不要针对特定浏览器提供差异化内容。</p></div>  
</div>
            