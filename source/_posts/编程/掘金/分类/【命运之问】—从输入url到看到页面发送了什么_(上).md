
---
title: '【命运之问】—从输入url到看到页面发送了什么_(上)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96df541c5e3044fca5c2b59a64a56c22~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 00:22:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96df541c5e3044fca5c2b59a64a56c22~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>这不仅仅是一道高频的面试题,更是成为一个合格的前端工程师所必须掌握的内容。我在阅读很多大佬的有关于这方面知识点的文章下面总能看到有人说学这个只是为了面试,平常工作中完全用不到。可是作为一个每天都需要与浏览器打交道的职业,怎么可能会用不到这方面的知识呢？很简单的一个例子就是“首屏加载”。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96df541c5e3044fca5c2b59a64a56c22~tplv-k3u1fbpfcp-zoom-1.image" alt="chart" loading="lazy" referrerpolicy="no-referrer"></p>
<p>web性能的优化与用户留存度息息相关,而不了解浏览器的工作原理怎么能对web性能进行优化呢？这道面试题考的正是我们对于浏览器工作原理的理解。</p>
<p>本篇文章是从浏览器地址栏输入url到请求返回发生了什么?的上篇,主要介绍的是在发送请求到资源返回之间的网络请求相关。</p>
<p>话不多说,开始学习。</p>
<h2 data-id="heading-1">流程</h2>
<p>在输入url后到返回资源文件,会发生那些事情呢？</p>
<p>看下图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78df759acefc45318c83b935bd1d2ef8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>构建请求</li>
<li>查找缓存</li>
<li>准备IP和端口(DNS查询)</li>
<li>等待TCP连接</li>
<li>建立TCP连接</li>
<li>发送HTTP请求</li>
<li>服务器处理并返回请求</li>
<li>服务器断开连接</li>
</ol>
<p>一共八步,为了方便记忆,你可以理解为天龙八“步”。</p>
<h2 data-id="heading-2">浏览器端发起 HTTP 请求流程</h2>
<p>在正式进入网络请求前,浏览器会对输入的URL进行解析,判断其合法性。</p>
<p>当用户在地址栏中输⼊⼀个查询关键字时，地址栏会判断输⼊的关键字是<strong>搜索内容</strong>，还是<strong>请求的URL</strong></p>
<ul>
<li>如果是搜索内容，地址栏会使用浏览器默认的搜索引擎，来合成新的带搜索关键字的URL。</li>
<li>如果判断输⼊内容符合URL规则，比如输⼊的是baidu.com，那么地址栏会根据规则，把这段内容加上协议，合成为完整的URL，如<a href="https://www.baidu.com/%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">www.baidu.com/。</a></li>
</ul>
<p>请在这里设想一下,如果你在浏览器地址栏里键入百度网站的地址：<a href="https://www.baidu.com/" target="_blank" rel="nofollow noopener noreferrer">www.baidu.com</a>， 那么接下来，浏览器会完成哪些动作呢？下面我们就一步一步详细“追踪”下。</p>
<h3 data-id="heading-3">构建请求</h3>
<p>首先，浏览器构建<strong>请求行</strong>信息（如下所示），构建好后，浏览器准备发起网络请求。</p>
<pre><code class="copyable">GET /index.html HTTP1.1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">查找缓存</h3>
<p>在真正发起网络请求之前，浏览器会先在浏览器缓存中查询是否有要请求的文件。其中，<strong>浏览器缓存是一种在本地保存资源副本，以供下次请求时直接使用的技术</strong>。</p>
<p>当浏览器发现请求的资源已经在浏览器缓存中存有副本，它会拦截请求，返回该资源的副本，并直接结束请求，而不会再去源服务器重新下载。这样做的好处有：</p>
<ul>
<li>缓解服务器端压力，提升性能（获取资源的耗时更短了）；</li>
<li>对于网站来说，缓存是实现快速资源加载的重要组成部分。</li>
</ul>
<p>当然，如果缓存查找失败，就会进入网络请求过程了。</p>
<h3 data-id="heading-5">准备 IP 地址和端口</h3>
<p>由于我们输入的是域名，而数据包是通过<code>IP地址</code>传给对方的。因此我们需要得到域名对应的<code>IP地址</code>。这个过程需要依赖一个服务系统，这个系统将域名和 IP 一一映射，我们将这个系统就叫做<strong>DNS</strong>（域名系统）。得到具体 IP 的过程就是<code>DNS</code>解析。</p>
<p>当然，值得注意的是，浏览器提供了<strong>DNS数据缓存功能</strong>。即如果一个域名已经解析过，那会把解析的结果缓存下来，下次处理直接走缓存，不需要经过 <code>DNS解析</code>。</p>
<p>另外，如果不指定端口的话，默认采用对应的 IP 的 80 端口。</p>
<h3 data-id="heading-6">等待 TCP 队列</h3>
<p>现在已经把端口和 IP 地址都准备好了，那么下一步是不是可以建立 TCP 连接了呢？</p>
<blockquote>
<p>答案不一定的，这个得根据不同的浏览器来规定的，我们以Chrome浏览器为例，Chrome 有个机制，同一个域名同时最多只能建立 6 个 TCP 连接，如果在同一个域名下同时有 10 个请求发生，那么其中 4 个请求会进入排队等待状态，直至进行中的请求完成。</p>
</blockquote>
<blockquote>
<p>当然，如果当前请求数量少于 6，会直接进入下一步，建立 TCP 连接。</p>
</blockquote>
<h3 data-id="heading-7">建立 TCP 连接</h3>
<ol>
<li>通过<strong>三次握手</strong>(即总共发送3个数据包确认已经建立连接)建立客户端和服务器之间的连接。</li>
<li>进行数据传输。这里有一个重要的机制，就是接收方接收到数据包后必须要向发送方<code>确认</code>, 如果发送方没有接到这个<code>确认</code>的消息，就判定为数据包丢失，并重新发送该数据包。当然，发送的过程中还有一个优化策略，就是把<code>大的数据包拆成一个个小包</code>，依次传输到接收方，接收方按照这个小包的顺序把它们<code>组装</code>成完整数据包。</li>
<li>断开连接的阶段。数据传输完成，现在要断开连接了，通过<strong>四次挥手</strong>来断开连接。</li>
</ol>
<p>读到这里，你应该明白 TCP 连接通过什么手段来保证数据传输的可靠性，一是<code>三次握手</code>确认连接，二是<code>数据包校验</code>保证数据到达接收方，三是通过<code>四次挥手</code>断开连接。</p>
<p>当然，如果再深入地问，比如<strong>为什么要三次握手，两次不行吗？第三次握手失败了怎么办？为什么要四次挥手</strong>等等这一系列的问题，涉及计算机网络的基础知识，比较底层，但是也是非常重要的细节，希望你能好好研究一下，另外这里有一篇不错的文章，<a href="https://zhuanlan.zhihu.com/p/86426969" target="_blank" rel="nofollow noopener noreferrer">点击进入相应的推荐文章</a>，相信这篇文章能给你启发。</p>
<h3 data-id="heading-8">发送 HTTP 请求</h3>
<p>现在<code>TCP连接</code>建立完毕，浏览器可以和服务器开始通信，即开始发送 HTTP 请求。浏览器发 HTTP 请求要携带三样东西:<strong>请求行</strong>、<strong>请求头</strong>和<strong>请求体</strong>。</p>
<p>首先，浏览器会向服务器发送<strong>请求行</strong>,关于<strong>请求行</strong>， 我们在这一部分的第一步就构建完了，贴一下内容:</p>
<pre><code class="copyable">// 请求方法是GET，路径为根路径，HTTP协议版本为1.1
GET / HTTP/1.1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结构很简单，由<strong>请求方法</strong>、<strong>请求URI</strong>和<strong>HTTP版本协议</strong>组成。</p>
<p>同时也要带上<strong>请求头</strong>，比如我们之前说的<strong>Cache-Control</strong>、<strong>If-Modified-Since</strong>、<strong>If-None-Match</strong>都由可能被放入请求头中作为缓存的标识信息。当然了还有一些其他的属性，列举如下:</p>
<pre><code class="copyable">Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Cookie: /* 省略cookie信息 */
Host: www.baidu.com
Pragma: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后是请求体，请求体只有在<code>POST</code>方法下存在，常见的场景是<strong>表单提交</strong>。</p>
<h3 data-id="heading-9">服务器处理请求</h3>
<p>HTTP 请求到达服务器，服务器进行对应的处理。最后要把数据传给浏览器，也就是返回网络响应。</p>
<p>跟请求部分类似，网络响应具有三个部分:<strong>响应行</strong>、<strong>响应头</strong>和<strong>响应体</strong>。</p>
<p>响应行类似下面这样:</p>
<pre><code class="copyable">HTTP/1.1 200 OK
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由<code>HTTP协议版本</code>、<code>状态码</code>和<code>状态描述</code>组成。</p>
<p>响应头包含了服务器及其返回数据的一些信息, 服务器生成数据的时间、返回的数据类型以及对即将写入的Cookie信息。</p>
<p>举例如下:</p>
<pre><code class="copyable">Cache-Control: no-cache
Connection: keep-alive
Content-Encoding: gzip
Content-Type: text/html;charset=utf-8
Date: Wed, 04 Dec 2019 12:29:13 GMT
Server: apache
Set-Cookie: rsv_i=f9a0SIItKqzv7kqgAAgphbGyRts3RwTg%2FLyU3Y5Eh5LwyfOOrAsvdezbay0QqkDqFZ0DfQXby4wXKT8Au8O7ZT9UuMsBq2k; path=/; domain=.baidu.com
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">服务器断开连接</h3>
<p>一般情况下，服务器发送完数据后，就要关闭TCP连接。不过有一种情况比较特殊，我们来看看</p>
<pre><code class="copyable">Connection:Keep-Alive
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果浏览器或者在服务器中加入其头信息如上面的字段的话，TCP连接会仍然保持，这样子浏览器就可以通过同一个TCP连接发送请求，<strong>保存TCP连接可以省下去下次请求需要建立连接的时间，提升资源加载速度。</strong></p>
<h3 data-id="heading-11">重定向</h3>
<p>我们还得聊一聊一种特殊的情况，不过这个情况跟之前提过的<strong>状态码</strong>有关，我们大概知道了，服务器返回的状态码不同，会有不同的返回的结果，你肯定遇到过这样子的情况吧：<strong>当你在浏览器中打开 baidu.com 后，你会发现最终打开的页面地址是 <a href="http://www.baidu.com/" target="_blank" rel="nofollow noopener noreferrer">www.baidu.com</a> ** 这两个URL不一样的原因就是涉及到了</strong>重定向**，让我们从一张图片上面看看这种情况吧👇</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd6cfa1f95c14fcba4c3f1f301fd7ead~tplv-k3u1fbpfcp-zoom-1.image" alt="服务器返回响应行和响应头（含重定向格式）" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们看看响应行返回的状态码301，状态301告诉浏览器，你需要重新转到另外一个网址，需要重定向的地址正式包含在响应头的Location字段中。接下啦，浏览器获取Location字段中的地址，重新导航，这也就是完整的重定向的执行流程。</p>
</blockquote>
<p>这解释了为什么输入baidu.com后，最终打开的是www.baidu.com</p>
<h3 data-id="heading-12">涉及面试题</h3>
<ul>
<li>为什么很多站点第二次打开速度会很快？🚀</li>
<li>当登录过一个网站之后，下次再访问该站点，就已经处于登录状态了，这是怎么做到的呢？</li>
<li>如何使用 Cookie 来进行状态管理，说一说流程</li>
<li>TCP建立连接过程讲一讲，为什么握手需要三次？</li>
<li>UDP了解吗，与TCP相比，优点是啥，缺点呢？</li>
<li>你刚刚说了TCP连接会存在TCP队列，那加载大量图片或者其他资源的时候，该怎么解决卡顿呢</li>
</ul>
<p>为什么很多站点第二次打开速度会很快？🚀</p>
<blockquote>
<p>当然是因为耗时的数据被缓存了呀,首先端口和IP会被缓存,页面资源也会缓存。而不用进行DNS查询甚至对于一些资源请求都不用发送直接从本地拿,那打开速度当然快啦。</p>
</blockquote>
<p>当登录过一个网站之后，下次再访问该站点，就已经处于登录状态了，这是怎么做到的呢？</p>
<blockquote>
<p>首先映入脑海的当然是Cookie的存在啦,HTTP是无状态的协议,而Cookie的出现弥补<code>HTTP</code>在<strong>状态管理上的不足</strong>。</p>
</blockquote>
<p>如何使用 Cookie 来进行状态管理，说一说流程</p>
<blockquote>
<ol>
<li>客户端请求服务端</li>
<li>服务端生成Cookie信息使用 Set-Cookie 添加到响应报文头部上</li>
<li>客户端在拿到之后保存Cookie</li>
<li>在下次请求的时候通过把信息写入请求报文头部Cookie字段中传给服务端</li>
</ol>
</blockquote>
<p>TCP建立连接过程讲一讲，为什么握手需要三次？</p>
<blockquote>
<p>建立过程就不讲了,网上答案一大堆,为什么要握手三次呢?为的是确保客户端和服务端的请求响应能力都正常</p>
</blockquote>
<p>UDP了解吗，与TCP相比，优点是啥，缺点呢？
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53465e8633c148fc9c3fc1e43f08f3a4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>你刚刚说了TCP连接会存在TCP队列，那加载大量图片或者其他资源的时候，该怎么解决卡顿呢?</p>
<blockquote>
<p>解决方法一:并发连接,就是一个域名多开几个连接同时进行请求。这个浏览器以及帮我们实现了。</p>
</blockquote>
<blockquote>
<p>解决方法二:域名分片:多创建几个子域名,这样连接就更多了。</p>
</blockquote>
<blockquote>
<p>解决方法三:使用HTTP2。</p>
</blockquote></div>  
</div>
            