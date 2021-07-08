
---
title: 'web性能优化 HTTP 缓存'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75185291548d4c68b6163c75a14380f5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 23:24:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75185291548d4c68b6163c75a14380f5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>通过网络获取内容既速度缓慢又开销巨大。较大的响应需要在客户端与服务器之间进行多次往返通信，这会延迟浏览器获得和处理内容的时间，还会增加访问者的流量费用。因此，缓存并重复利用之前获取的资源的能力成为性能优化的一个关键方面。</p>
<p>好在每个浏览器都自带了 HTTP 缓存实现功能。您只需要确保每个服务器响应都提供正确的 HTTP 标头指令，以指示浏览器何时可以缓存响应以及可以缓存多久。</p>
<blockquote>
<p>注：如果您在应用中使用 Webview 来获取和显示网页内容，可能需要提供额外的配置标志，以确保 HTTP 缓存得到启用、其大小根据用例进行了合理设置并且缓存将持久保存。务必查看平台文档并确认您的设置！</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75185291548d4c68b6163c75a14380f5~tplv-k3u1fbpfcp-zoom-1.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当服务器返回响应时，还会发出一组 HTTP 标头，用于描述响应的内容类型、长度、缓存指令、验证令牌等。例如，在上图的交互中，服务器返回一个 1024 字节的响应，指示客户端将其缓存最多 120 秒，并提供一个验证令牌（“x234dff”），可在响应过期后用来检查资源是否被修改。</p>
<h3 data-id="heading-0">通过 ETag 验证缓存的响应</h3>
<ul>
<li>服务器使用 ETag HTTP 标头传递验证令牌。</li>
<li>验证令牌可实现高效的资源更新检查：资源未发生变化时不会传送任何数据。</li>
</ul>
<p>假定在首次获取资源 120 秒后，浏览器又对该资源发起了新的请求。首先，浏览器会检查本地缓存并找到之前的响应。遗憾的是，该响应现已过期，浏览器无法使用。此时，浏览器可以直接发出新的请求并获取新的完整响应。不过，这样做效率较低，因为如果资源未发生变化，那么下载与缓存中已有的完全相同的信息就毫无道理可言！</p>
<p>这正是验证令牌（在 ETag 标头中指定）旨在解决的问题。服务器生成并返回的随机令牌通常是文件内容的哈希值或某个其他指纹。客户端不需要了解指纹是如何生成的，只需在下一次请求时将其发送至服务器。如果指纹仍然相同，则表示资源未发生变化，您就可以跳过下载。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/025dc92cab024f2da8df91b2ea5ae2b4~tplv-k3u1fbpfcp-zoom-1.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上例中，客户端自动在“If-None-Match” HTTP 请求标头内提供 ETag 令牌。服务器根据当前资源核对令牌。如果它未发生变化，服务器将返回“304 Not Modified”响应，告知浏览器缓存中的响应未发生变化，可以再延用 120 秒。请注意，您不必再次下载响应，这节约了时间和带宽。</p>
<p>作为网络开发者，您如何利用高效的重新验证？浏览器会替我们完成所有工作：它会自动检测之前是否指定了验证令牌，它会将验证令牌追加到发出的请求上，并且它会根据从服务器接收的响应在必要时更新缓存时间戳。<strong>我们唯一要做的就是确保服务器提供必要的 ETag 令牌。检查您的服务器文档中有无必要的配置标志。</strong></p>
<blockquote>
<p>提示：HTML5 Boilerplate 项目包含所有最流行服务器的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fh5bp%2Fserver-configs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/h5bp/server-configs" ref="nofollow noopener noreferrer">配置文件样例</a>，其中为每个配置标志和设置都提供了详细的注解。在列表中找到您喜爱的服务器，查找合适的设置，然后复制/确认您的服务器配置了推荐的设置。</p>
</blockquote>
<h3 data-id="heading-1">Cache-Control</h3>
<ul>
<li>每个资源都可通过 Cache-Control HTTP 标头定义其缓存策略</li>
<li>Cache-Control 指令控制谁在什么条件下可以缓存响应以及可以缓存多久。</li>
</ul>
<p>从性能优化的角度来说，最佳请求是无需与服务器通信的请求：您可以通过响应的本地副本消除所有网络延迟，以及避免数据传送的流量费用。为实现此目的，HTTP 规范允许服务器返回 Cache-Control 指令，这些指令控制浏览器和其他中间缓存如何缓存各个响应以及缓存多久。</p>
<blockquote>
<p>Cache-Control 标头是在 HTTP/1.1 规范中定义的，取代了之前用来定义响应缓存策略的标头（例如 Expires）。所有现代浏览器都支持 Cache-Control，因此，使用它就够了。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da331beb70d944a9b012685e1fcddfbc~tplv-k3u1fbpfcp-zoom-1.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>“<strong>no-cache”和“no-store”</strong>
“no-cache”表示必须先与服务器确认返回的响应是否发生了变化，然后才能使用该响应来满足后续对同一网址的请求。因此，如果存在合适的验证令牌 (ETag)，no-cache 会发起往返通信来验证缓存的响应，但如果资源未发生变化，则可避免下载。
相比之下，“no-store”则要简单得多。它直接禁止浏览器以及所有中间缓存存储任何版本的返回响应，例如，包含个人隐私数据或银行业务数据的响应。每次用户请求该资产时，都会向服务器发送请求，并下载完整的响应。</p>
</li>
<li>
<p><strong>“public”与“private”</strong>
如果响应被标记为“public”，则即使它有关联的 HTTP 身份验证，甚至响应状态代码通常无法缓存，也可以缓存响应。大多数情况下，“public”不是必需的，因为明确的缓存信息（例如“max-age”）已表示响应是可以缓存的。
相比之下，浏览器可以缓存“private”响应。不过，这些响应通常只为单个用户缓存，因此不允许任何中间缓存对其进行缓存。例如，用户的浏览器可以缓存包含用户私人信息的 HTML 网页，但 CDN 却不能缓存。</p>
</li>
<li>
<p><strong>“max-age”</strong>
指令指定从请求的时间开始，允许获取的响应被重用的最长时间（单位：秒）。例如，“max-age=60”表示可在接下来的 60 秒缓存和重用响应。</p>
</li>
</ol>
<h3 data-id="heading-2">定义最佳 Cache-Control 策略</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/577564e9b2e24a308f4bb3d501050e21~tplv-k3u1fbpfcp-zoom-1.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照以上决策树为您的应用使用的特定资源或一组资源确定最佳缓存策略。在理想的情况下，您的目标应该是在客户端上缓存尽可能多的响应，缓存尽可能长的时间，并且为每个响应提供验证令牌，以实现高效的重新验证。</p>





















<table><thead><tr><th align="left">Cache-Control</th><th align="left">指令和说明</th></tr></thead><tbody><tr><td align="left">max-age=86400</td><td align="left">浏览器以及任何中间缓存均可将响应（如果是“public”响应）缓存长达 1 天（60 秒 x 60 分钟 x 24 小时）。</td></tr><tr><td align="left">private, max-age=600</td><td align="left">客户端的浏览器只能将响应缓存最长 10 分钟（60 秒 x 10 分钟）。</td></tr><tr><td align="left">no-store</td><td align="left">不允许缓存响应，每次请求都必须完整获取。</td></tr></tbody></table>
<p>根据 HTTP Archive，在排名最高的 300,000 个网站（按照 Alexa 排名）中，所有下载的响应中几乎有半数可由浏览器缓存，这可以大量减少重复的网页浏览和访问。当然，这并不意味着您的特定应用有 50% 的资源可以缓存。一些网站的资源 90% 以上都可以缓存，而其他网站可能有许多私密或时效要求高的数据根本无法缓存。</p>
<blockquote>
<p>请审核您的网页，确定哪些资源可以缓存，并确保它们返回正确的 Cache-Control 和 ETag 标头。</p>
</blockquote>
<h3 data-id="heading-3">废弃和更新缓存的响应</h3>
<ul>
<li>在资源“过期”之前，将一直使用本地缓存的响应。</li>
<li>您可以通过在网址中嵌入文件内容指纹，强制客户端更新到新版本的响应。</li>
<li>为获得最佳性能，每个应用都需要定义自己的缓存层次结构。</li>
</ul>
<p>客户端缓存和快速更新？您可以在资源内容发生变化时更改它的网址，强制用户下载新响应。通常情况下，可以通过在文件名中嵌入文件的指纹或版本号来实现 - 例如 style.x234dff.css。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92baae00d0984ef9b8df095e070bfe0f~tplv-k3u1fbpfcp-zoom-1.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4"><strong>缓存检查清单</strong></h3>
<p>不存在什么最佳缓存策略。您需要根据通信模式、提供的数据类型以及应用特定的数据更新要求，为每个资源定义和配置合适的设置，以及整体的“缓存层次结构”。</p>
<p>在制定缓存策略时，您需要牢记下面这些技巧和方法：</p>
<ol>
<li>
<p><strong>使用一致的网址</strong>
如果您在不同的网址上提供相同的内容，将会多次获取和存储这些内容。提示：请注意，网址区分大小写。</p>
</li>
<li>
<p><strong>确保服务器提供验证令牌 (ETag)</strong>
有了验证令牌，当服务器上的资源未发生变化时，就不需要传送相同的字节。</p>
</li>
<li>
<p><strong>确定中间缓存可以缓存哪些资源</strong>
对所有用户的响应完全相同的资源非常适合由 CDN 以及其他中间缓存进行缓存。</p>
</li>
<li>
<p><strong>为每个资源确定最佳缓存周期</strong>
不同的资源可能有不同的更新要求。为每个资源审核并确定合适的 max-age。</p>
</li>
<li>
<p><strong>确定最适合您的网站的缓存层次结构</strong>
您可以通过为 HTML 文档组合使用包含内容指纹的资源网址和短时间或 no-cache 周期，来控制客户端获取更新的速度。</p>
</li>
<li>
<p><strong>最大限度减少搅动</strong>
某些资源的更新比其他资源频繁。如果资源的特定部分（例如 JavaScript 函数或 CSS 样式集）会经常更新，可以考虑将其代码作为单独的文件提供。这样一来，每次获取更新时，其余内容（例如变化不是很频繁的内容库代码）可以从缓存获取，从而最大限度减少下载的内容大小。</p>
</li>
</ol>








































<table><thead><tr><th>打开页面方式</th><th>IE6（httpwatch）</th><th>FF3.5（httpfox）</th></tr></thead><tbody><tr><td>1. 第一次打开页面</td><td>200</td><td>200</td></tr><tr><td>2. 重启浏览器打开页面</td><td>cache，即时发生资源修改也不会重新请求</td><td>cache，即时发生资源修改也不会重新请求</td></tr><tr><td>3. F5刷新</td><td>304，发生修改的资源状态为200</td><td>304，发生修改的资源状态为200</td></tr><tr><td>4. Ctrl+F5刷新</td><td>200，强制全新请求</td><td>200</td></tr><tr><td>5. 后退</td><td>cache,简单直接地从缓存加载</td><td>cache,简单直接地从缓存加载</td></tr><tr><td>6. 在已访问页面地址栏回车</td><td>cache</td><td>cache</td></tr></tbody></table></div>  
</div>
            