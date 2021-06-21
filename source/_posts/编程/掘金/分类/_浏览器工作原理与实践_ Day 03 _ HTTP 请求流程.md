
---
title: '_浏览器工作原理与实践_ Day 03 _ HTTP 请求流程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b536da56e6694f99b37eefd086fbeb8f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 19:14:11 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b536da56e6694f99b37eefd086fbeb8f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">前言</h2>
<p>学习资源来自极客时间 - 李兵老师 <a href="https://time.geekbang.org/column/article/113513" target="_blank" rel="nofollow noopener noreferrer">《浏览器工作原理与实践》</a>。接下来，让我们一起每日打卡，check完成所有课程吧 ~</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> <a href="https://juejin.cn/post/6974754464536199182" target="_blank">Day 01 Chrome架构：仅仅打开了1个页面，为什么会有4个进程？</a></li>
<li class="task-list-item"><input type="checkbox" checked disabled> <a href="https://juejin.cn/post/6976055580674752548" target="_blank">Day 02 TCP协议：如何保证页面文件能被完整送达浏览器？</a></li>
<li class="task-list-item"><input type="checkbox" checked disabled> Day 03 HTTP请求流程：为什么很多站点第二次打开速度会很快？</li>
</ul>
<h3 data-id="heading-1"><strong>阅读本文你会学到什么？</strong></h3>
<p>浏览器中的HTTP请求从发起到结束一共经历如下8个阶段：</p>
<ul>
<li>构建请求</li>
<li>查找缓存</li>
<li>准备IP和端口</li>
<li>等待TCP队列</li>
<li>建立TCP连接</li>
<li>发起HTTP请求</li>
<li>服务器处理请求</li>
<li>服务器返回请求</li>
<li>断开连接</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b536da56e6694f99b37eefd086fbeb8f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
通过HTTP请求路径，两个经常会碰到的问题</p>
<ol>
<li>涉及到了Cache流程</li>
<li>涉及到如何使用Cookie来进行状态管理</li>
</ol>
<p>在<a href="https://juejin.cn/post/6976055580674752548" target="_blank">上一篇文章</a>中介绍了TCP协议是如何保证数据完整传输的，相信你还记得，一个 TCP 连接过程包括了建立连接、传输数据和断开连接三个阶段。</p>
<p>而 HTTP 协议，正是建立在 TCP 连接基础之上的。<strong>HTTP 是一种允许浏览器向服务器获取资源的协议，是 Web 的基础</strong>，通常由浏览器发起请求，用来获取不同类型的文件，例如 HTML 文件、CSS 文件、JavaScript 文件、图片、视频等。此外，<strong>HTTP 也是浏览器使用最广的协议</strong>，所以要想学好浏览器，就要先深入了解 HTTP。</p>
<p>不知道你是否有过下面这些疑问：</p>
<ol>
<li>为什么通常在第一次访问一个站点时，打开速度很慢，当再次访问这个站点时，速度就很快了？</li>
<li>当登录过一个网站之后，下次再访问该站点，就已经处于登录状态了，这是怎么做到的呢？</li>
</ol>
<p>这一切的秘密都隐藏在 HTTP 的请求过程中。所以，在今天这篇文章中，我将通过分析一个 HTTP 请求过程中每一步的状态来带你了解完整的 HTTP 请求过程，希望你看完这篇文章后，能够对 HTTP 协议有个全新的认识。</p>
<h2 data-id="heading-2">浏览器端发起HTTP请求流程</h2>
<p>如果你在浏览器地址栏里键入极客时间网站的地址：<a href="http://time.geekbang.org/index.html%EF%BC%8C" target="_blank" rel="nofollow noopener noreferrer">time.geekbang.org/index.html，</a> 那么接下来，浏览器会完成哪些动作呢？下面我们就一步一步详细“追踪”下。</p>
<h3 data-id="heading-3">1. 构建请求</h3>
<p>首先，浏览器构建<strong>请求行</strong>信息（如下所示），构建好后，浏览器准备发起网络请求。</p>
<pre><code class="hljs language-js copyable" lang="js">GET /index.html HTTP1<span class="hljs-number">.1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2. 查找缓存</h3>
<p>在真正发起网络请求之前，浏览器会先在浏览器缓存中查询是否有要请求的文件。其中，<strong>浏览器缓存是一种在本地保存资源副本，以供下次请求时直接使用的技术。</strong></p>
<p>当浏览器发现请求的资源已经在浏览器缓存中存有副本，它会拦截请求，返回该资源的副本，并直接结束请求，而不会再去源服务器重新下载。这样做的好处有：</p>
<ul>
<li>缓解服务器压力，提升性能（获取资源的耗时更短了）。</li>
<li>对于网站来说，缓存是实现快速资源加载的重要组成部分。</li>
</ul>
<p>当然，如果缓存查找失败，就会进入网络请求过程了。</p>
<h3 data-id="heading-5">3. 准备IP地址和端口</h3>
<p>不过，先不急，在了解网络请求之前，我们需要先看看 HTTP 和 TCP 的关系。因为浏览器使用 <strong>HTTP 协议作为应用层协议</strong>，用来封装请求的文本信息；并使用 <strong>TCP/IP 作传输层协议</strong>将它发到网络上，所以在 HTTP 工作开始之前，浏览器需要通过 TCP 与服务器建立连接。也就是说 <strong>HTTP 的内容是通过 TCP 的传输数据阶段来实现的</strong>，你可以结合下图更好地理解这二者的关系。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f16b5a3230f94e4299591350e75a4c4a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
那接下来你可以思考这么“一连串”问题：</p>
<ul>
<li>HTTP 网络请求的第一步是做什么呢？结合上图看，是和服务器建立 TCP 连接。</li>
<li>那建立连接的信息都有了吗？<a href="https://juejin.cn/post/6976055580674752548" target="_blank">上一篇文章</a>中，我们讲到建立 TCP 连接的第一步就是需要准备 IP 地址和端口号。</li>
<li>那怎么获取 IP 地址和端口号呢？这得看看我们现在有什么，我们有一个 URL 地址，那么是否可以利用 URL 地址来获取 IP 和端口信息呢？</li>
</ul>
<p>在上一篇文章中，我们介绍过数据包都是通过 IP 地址传输给接收方的。由于 IP 地址是数字标识，比如极客时间网站的 IP 是 39.106.233.176, 难以记忆，但使用极客时间的域名（time.geekbang.org）就好记多了，所以基于这个需求又出现了一个服务，负责把域名和 IP 地址做一一映射关系。这套域名映射为 IP 的系统就叫做“<strong>域名系统</strong>”，简称 <strong>DNS</strong>（Domain Name System）。</p>
<p>所以，这样一路推导下来，你会发现在<strong>第一步浏览器会请求 DNS 返回域名对应的 IP</strong>。当然浏览器还提供了 <strong>DNS 数据缓存服务</strong>，如果某个域名已经解析过了，那么浏览器会缓存解析的结果，以供下次查询时直接使用，这样也会减少一次网络请求。</p>
<p>拿到 IP 之后，接下来就需要获取端口号了。通常情况下，如果 URL 没有特别指明端口号，那么 HTTP 协议默认是 80 端口。</p>
<h3 data-id="heading-6">4. 等待TCP队列</h3>
<p>现在已经把端口和 IP 地址都准备好了，那么下一步是不是可以建立 TCP 连接了呢？</p>
<p>答案依然是“不行”。Chrome 有个机制，同一个域名同时最多只能建立 6 个 TCP 连接，如果在同一个域名下同时有 10 个请求发生，那么其中 4 个请求会进入排队等待状态，直至进行中的请求完成。</p>
<p>当然，如果当前请求数量少于 6，会直接进入下一步，建立 TCP 连接。</p>
<h3 data-id="heading-7">5. 建立TCP连接</h3>
<p>排队等待结束之后，终于可以快乐地和服务器握手了，在 HTTP 工作开始之前，浏览器通过 TCP 与服务器建立连接。而 TCP 的工作方式，我在上一篇文章中已经做过详细介绍了，如果有必要，你可以自行回顾下，这里我就不再重复讲述了。</p>
<h3 data-id="heading-8">6. 发送HTTP请求</h3>
<p>一旦建立了 TCP 连接，浏览器就可以和服务器进行通信了。而 HTTP 中的数据正是在这个通信过程中传输的。</p>
<p>你可以结合下图来理解，浏览器是如何发送请求信息给服务器的。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da3c597775dc482c977aed750f4819e0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先浏览器会向服务器发送<strong>请求行</strong>，它包括了<strong>请求方法</strong>、<strong>请求 URI（Uniform Resource Identifier）和 HTTP 版本协议</strong>。</p>
<p>发送请求行，就是告诉服务器浏览器需要什么资源，最常用的请求方法是 <strong>Get</strong>。比如，直接在浏览器地址栏键入极客时间的域名（time.geekbang.org），这就是告诉服务器要 Get 它的首页资源。</p>
<p>另外一个常用的请求方法是 <strong>POST</strong>，它用于发送一些数据给服务器，比如登录一个网站，就需要通过 POST 方法把用户信息发送给服务器。如果使用 POST 方法，那么浏览器还要准备数据给服务器，这里准备的数据是通过<strong>请求体</strong>来发送。</p>
<p>在浏览器发送请求行命令之后，还要以<strong>请求头</strong>形式发送其他一些信息，把浏览器的一些基础信息告诉服务器。比如包含了浏览器所使用的操作系统、浏览器内核等信息，以及当前请求的域名信息、浏览器端的 Cookie 信息，等等。</p>
<h2 data-id="heading-9">服务器端处理 HTTP 请求流程</h2>
<p>历经千辛万苦，HTTP 的请求信息终于被送达了服务器。接下来，服务器会根据浏览器的请求信息来准备相应的内容。</p>
<h3 data-id="heading-10">1. 返回请求</h3>
<p>一旦服务器处理结束，便可以返回数据给浏览器了。你可以通过工具软件 curl 来查看返回请求数据，具体使用方法是在命令行中输入以下命令：</p>
<pre><code class="hljs language-js copyable" lang="js">curl -i  https:<span class="hljs-comment">//time.geekbang.org/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这里加上了-i是为了返回响应行、响应头和响应体的数据，返回的结果如下图所示，你可以结合这些数据来理解服务器是如何响应浏览器的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cabebde062b442096e82d1d179ce448~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先服务器会返回<strong>响应行</strong>，包括协议版本和状态码。</p>
<p>但并不是所有的请求都可以被服务器处理的，那么一些无法处理或者处理出错的信息，怎么办呢？服务器会通过请求行的<strong>状态码</strong>来告诉浏览器它的处理结果，比如：</p>
<ul>
<li>最常用的状态码是 200，表示处理成功；</li>
<li>如果没有找到页面，则会返回 404。</li>
</ul>
<p>随后，正如浏览器会随同请求发送请求头一样，服务器也会随同响应向浏览器发送<strong>响应头</strong>。响应头包含了服务器自身的一些信息，比如服务器生成返回数据的时间、返回的数据类型（JSON、HTML、流媒体等类型），以及服务器要在客户端保存的 Cookie 等信息。</p>
<p>发送完响应头后，服务器就可以继续发送<strong>响应体</strong>的数据，通常，响应体就包含了 HTML 的实际内容。</p>
<p>以上这些就是服务器响应浏览器的具体过程。</p>
<h3 data-id="heading-11">2. 断开连接</h3>
<p>通常情况下，一旦服务器向客户端返回了请求数据，它就要关闭 TCP 连接。不过如果浏览器或者服务器在其头信息中加入了：</p>
<pre><code class="hljs language-js copyable" lang="js">Connection:Keep-Alive 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么 TCP 连接在发送后将仍然保持打开状态，这样浏览器就可以继续通过同一个 TCP 连接发送请求。<strong>保持 TCP 连接可以省去下次请求时需要建立连接的时间，提升资源加载速度</strong>。比如，一个 Web 页面中内嵌的图片就都来自同一个 Web 站点，如果初始化了一个持久连接，你就可以复用该连接，以请求其他资源，而不需要重新再建立新的 TCP 连接。</p>
<h3 data-id="heading-12">3. 重定向</h3>
<p>到这里似乎请求流程快结束了，不过还有一种情况你需要了解下，比如当你在浏览器中打开 geekbang.org 后，你会发现最终打开的页面地址是 <a href="https://www.geekbang.org./" target="_blank" rel="nofollow noopener noreferrer">www.geekbang.org。</a></p>
<p>这两个 URL 之所以不一样，是因为涉及到了一个<strong>重定向操作</strong>。跟前面一样，你依然可以使用 curl 来查看下请求 geekbang.org 会返回什么内容？</p>
<p>在控制台输入如下命令：</p>
<pre><code class="hljs language-js copyable" lang="js">curl -I geekbang.org
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这里输入的参数是-I，和-i不一样，-I表示只需要获取响应头和响应行数据，而不需要获取响应体的数据，最终返回的数据如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9da2b952a87442c689c03f8dc77d782b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中你可以看到，响应行返回的状态码是 301，状态 301 就是告诉浏览器，我需要重定向到另外一个网址，而需要重定向的网址正是包含在响应头的 Location 字段中，接下来，浏览器获取 Location 字段中的地址，并使用该地址重新导航，这就是一个完整重定向的执行流程。这也就解释了为什么输入的是 geekbang.org，最终打开的却是 <a href="https://www.geekbang.org/" target="_blank" rel="nofollow noopener noreferrer">www.geekbang.org</a> 了。</p>
<p>不过也不要认为这种跳转是必然的。如果你打开 <a href="https://12306.xn--cn,-928d6ex3d8no70aji0adthr4k9z5a4bi1jke1qti3f.xn--siqr4s59m7s4b/" target="_blank" rel="nofollow noopener noreferrer">12306.cn，你会发现这个站点是打不开的。这是因为</a> 12306 的服务器并没有处理跳转，所以必须要手动输入完整的 <a href="https://www.12306.cn/" target="_blank" rel="nofollow noopener noreferrer">www.12306.cn</a> 才能打开页面。</p>
<h2 data-id="heading-13">问题解答</h2>
<p>说了这么多，相信你现在已经了解了 HTTP 的请求流程，那现在我们再回过头来看看文章开头提出的问题。</p>
<h3 data-id="heading-14">1. 为什么很多站点第二次打开速度会很快？</h3>
<p>如果第二次页面打开很快，主要原因是第一次加载页面过程中，缓存了一些耗时的数据。</p>
<p>那么，哪些数据会被缓存呢？从上面介绍的核心请求路径可以发现，<strong>DNS 缓存</strong>和<strong>页面资源缓存</strong>这两块数据是会被浏览器缓存的。其中，DNS 缓存比较简单，它主要就是在浏览器本地把对应的 IP 和域名关联起来，这里就不做过多分析了。</p>
<p>我们重点看下浏览器资源缓存，下面是缓存处理的过程：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a82454213a0c48a5a96fdd8d3ba0fa23~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先，我们看下服务器是通过什么方式让浏览器缓存数据的？</p>
<p>从上图的第一次请求可以看出，当服务器返回 <strong>HTTP响应头</strong>给浏览器时，浏览器是<strong>通过响应头中的 Cache-Control 字段来设置是否缓存该资源</strong>。通常，我们还需要为这个资源设置一个缓存过期时长，而这个时长是通过 Cache-Control 中的 Max-age 参数来设置的，比如上图设置的缓存过期时间是 2000 秒。</p>
<pre><code class="hljs language-js copyable" lang="js">Cache-Control:Max-age=<span class="hljs-number">2000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这也就意味着，在该缓存资源还未过期的情况下, 如果再次请求该资源，会直接返回缓存中的资源给浏览器。</p>
<p>但如果缓存过期了，浏览器则会继续发起网络请求，并且在 <strong>HTTP 请求头</strong>中带上：</p>
<pre><code class="hljs language-js copyable" lang="js">If-None-Match:<span class="hljs-string">"4f80f-13c-3a1xb12a"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>服务器收到请求头后，会根据 If-None-Match 的值来判断请求的资源是否有更新。</p>
<ul>
<li>如果没有更新，就返回 304 状态码，相当于服务器告诉浏览器：“这个缓存可以继续使用，这次就不重复发送数据给你了。”</li>
<li>如果资源有更新，服务器就直接返回最新资源给浏览器。</li>
</ul>
<p>关于缓存的细节内容特别多，具体细节你可以参考这篇 <a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Caching" target="_blank" rel="nofollow noopener noreferrer">HTTP 缓存</a>，在这里我就不赘述了。</p>
<p>简要来说，很多网站第二次访问能够秒开，是因为这些网站把很多资源都缓存在了本地，浏览器缓存直接使用本地副本来回应请求，而不会产生真实的网络请求，从而节省了时间。同时，DNS 数据也被浏览器缓存了，这又省去了 DNS 查询环节。</p>
<h3 data-id="heading-15">2. 登录状态是如何保持的？</h3>
<p>通过上面的介绍，你已经了解了缓存是如何工作的。下面我们再一起看下登录状态是如何保持的。</p>
<ul>
<li>用户打开登录页面，在登录框里填入用户名和密码，点击确定按钮。点击按钮会触发页面脚本生成用户登录信息，然后调用 POST 方法提交用户登录信息给服务器。</li>
<li>服务器接收到浏览器提交的信息之后，查询后台，验证用户登录信息是否正确，如果正确的话，会生成一段表示用户身份的字符串，并把该字符串写到响应头的 Set-Cookie 字段里，如下所示，然后把响应头发送给浏览器。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Set</span>-Cookie: UID=3431uad;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>浏览器在接收到服务器的响应头后，开始解析响应头，如果遇到响应头里含有 Set-Cookie 字段的情况，浏览器就会把这个字段信息保存到本地。比如把UID=3431uad保持到本地。</li>
<li>当用户再次访问时，浏览器会发起 HTTP 请求，但在发起请求之前，浏览器会读取之前保存的 Cookie 数据，并把数据写进请求头里的 Cookie 字段里（如下所示），然后浏览器再将请求头发送给服务器。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">Cookie: UID=3431uad;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>服务器在收到 HTTP 请求头数据之后，就会查找请求头里面的“Cookie”字段信息，当查找到包含UID=3431uad的信息时，服务器查询后台，并判断该用户是已登录状态，然后生成含有该用户信息的页面数据，并把生成的数据发送给浏览器。</li>
<li>浏览器在接收到该含有当前用户的页面数据后，就可以正确展示用户登录的状态信息了。</li>
</ul>
<p>好了，通过这个流程你可以知道浏览器页面状态是通过使用 Cookie 来实现的。Cookie 流程可以参考下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c367222eb0f40bbafba3e8983b570b8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单地说，如果服务器端发送的响应头内有 Set-Cookie 的字段，那么浏览器就会将该字段的内容保持到本地。当下次客户端再往该服务器发送请求时，客户端会自动在请求头中加入 Cookie 值后再发送出去。服务器端发现客户端发送过来的 Cookie 后，会去检查究竟是从哪一个客户端发来的连接请求，然后对比服务器上的记录，最后得到该用户的状态信息。</p>
<h2 data-id="heading-16">思考</h2>
<p>如果一个页面的网络加载时间过久，你是如何分析卡在哪个阶段的？</p>
<ol>
<li>并发请求过多（大于6），TCP连接进入等待状态</li>
<li>资源大，下载时间过长</li>
<li>对于一些资源的重复请求，TCP连接没有connection=keep-alive, 消耗连接时间</li>
<li>网络慢、连接超时</li>
<li>网络传输丢包，需要不断重传</li>
</ol></div>  
</div>
            