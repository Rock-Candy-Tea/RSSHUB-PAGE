
---
title: '谈谈Http(万字长文 看完或许就懂了)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efd14b8355f943e8a698756df41d14ad~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 01:03:25 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efd14b8355f943e8a698756df41d14ad~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h1 data-id="heading-0">浏览器背后的故事</h1>
<blockquote>
<p>输入网址-根据域名寻找目标服务器所对应的IP地址(DNS服务器)-根据IP地址进行服务器通信,通信协议就是Http协议。</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efd14b8355f943e8a698756df41d14ad~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">HTTP是什么</h1>
<blockquote>
<p>协议(如三方协议，租房协议)</p>
</blockquote>
<ul>
<li>
<p>协：两个或多个参与者</p>
</li>
<li>
<p>议：对参与者的一种行为约定和规范</p>
</li>
</ul>
<blockquote>
<p>传输</p>
</blockquote>
<ul>
<li>
<p>把一堆东西从A搬到B，或者从B搬到A，即A<===>B</p>
</li>
<li>
<p>双向协议，先发起传输动作的叫请求方,接到传输的叫响应方。</p>
</li>
<li>
<p>虽然东西实在AB间传输，但没有限制只有AB两个角色，允许中间有中转，可以是A<===>X<===>B</p>
</li>
</ul>
<blockquote>
<p>超文本</p>
</blockquote>
<ul>
<li>
<p>文本：字符文字，图片，音频，视频甚至是压缩包等。</p>
</li>
<li>
<p>超文本：超越了普通文本的文本，它是文本，音频，视频等的混合体，最关键的是含有超链接，能够从一个超文本跳跃到另一个超文本，形成复杂的非线性，网状的结构。我们最熟悉的就是HTML，它本身是纯文字文件，但内部有很多标签定义了图片，音频，视频等连接。</p>
</li>
</ul>
<blockquote>
<p>总结</p>
</blockquote>
<p>HTTP是一个在计算机世界里专门在两点之间传输文本，图片，音频等超文本数据的约定和规范。</p>
<h1 data-id="heading-2">前生今世</h1>
<blockquote>
<p>HTTP 0.9</p>
</blockquote>
<ul>
<li>采用纯文本格式，只有GET方法，响应之后立即关闭连接。</li>
</ul>
<blockquote>
<p>HTTP 1.0</p>
</blockquote>
<ul>
<li>引入了头部，状态码，POST&HEAD方法, 重定向，使用 header 中的 If-Modified-Since 和 Expires 作为缓存失效的标准</li>
</ul>
<blockquote>
<p>HTTP 1.1</p>
</blockquote>
<ul>
<li>增加PUT,DELETE等方法，持久链接开启了keepalive， 缓存e-tag</li>
</ul>
<blockquote>
<p>HTTP 2.0</p>
</blockquote>
<ul>
<li>基于Google的SPDY协议</li>
<li>增强核心:二进制分帧， 头部压缩， 多路复用， 服务器推送</li>
</ul>
<blockquote>
<p>HTTP 3.0</p>
</blockquote>
<ul>
<li>基于Google的QUIC协议</li>
<li>没有队头阻塞的多路复用</li>
</ul>
<h1 data-id="heading-3">透过TCP/IP看HTTP</h1>
<ul>
<li>Http协议是构建在TCP/IP协议之上的，是TCP/IP的一个子集。</li>
</ul>
<h2 data-id="heading-4">TCP/IP</h2>
<blockquote>
<p>TCP/IP协议是一系列与互联网相关联的协议集合起来的总称</p>
</blockquote>
<blockquote>
<p>分层管理是TCP/IP协议的重要特征</p>
</blockquote>
<h2 data-id="heading-5">TCP/IP协议族分层</h2>
<blockquote>
<p>应用层-HTTP</p>
</blockquote>
<ul>
<li>通过系统调用与传输层进行通信，如：FTP,DNS,HTTP等</li>
</ul>
<blockquote>
<p>传输层-TCP</p>
</blockquote>
<ul>
<li>
<p>通过系统调用向应用层提供处于网络连接中的两台计算机之间的数据传输功能</p>
</li>
<li>
<p>有两个性质不同的协议：TCP和UDP</p>
</li>
</ul>
<blockquote>
<p>网络层-IP</p>
</blockquote>
<p>处理网络上流动的数据包，规定了通过怎样的路径达到对方计算机并把数据包传给对方。</p>
<blockquote>
<p>链路层-网络</p>
</blockquote>
<p>处理网络硬件部分</p>
<h2 data-id="heading-6">DNS</h2>
<p>因IP地址难记一般访问网址都是使用域名进行访问，而TCP/IP协议使用的是IP地址进行访问，必须有个服务把域名转换成IP地址，它就是DNS。</p>
<h2 data-id="heading-7">TCP三次握手</h2>
<p>使用TCP协议进行通信的双方必须先建立连接</p>
<blockquote>
<p>第一次握手</p>
</blockquote>
<p>客户端发送SYN报文，传达信息：“你好，我想建立连接”；</p>
<blockquote>
<p>第二次握手</p>
</blockquote>
<p>服务端回传SYN+ACK报文，传达信息：“好的，可以建立链接”；</p>
<blockquote>
<p>第三次握手</p>
</blockquote>
<p>客户端回传ACK报文，传到信息：“好的，我知道了，那我们连接；</p>
<blockquote>
<p>为什么不是两次</p>
</blockquote>
<p>根本原因: 无法确认客户端的接收能力。</p>
<blockquote>
<p>为什么不是四次</p>
</blockquote>
<p>三次握手的目的是确认双方发送和接收的能力，那四次握手可以吗？
当然可以，100 次都可以。但为了解决问题，三次就足够了，再多用处就不大了。</p>
<blockquote>
<p>三次握手过程中可以携带数据么</p>
</blockquote>
<p>第三次握手的时候，可以携带。前两次握手不能携带数据。</p>
<p>如果前两次握手能够携带数据，那么一旦有人想攻击服务器，那么他只需要在第一次握手中的 SYN 报文中放大量数据，那么服务器势必会消耗更多的时间和内存空间去处理这些数据，增大了服务器被攻击的风险。</p>
<p>第三次握手的时候，客户端已经处于ESTABLISHED状态，并且已经能够确认服务器的接收、发送能力正常，这个时候相对安全了，可以携带数据。</p>
<h2 data-id="heading-8">TCP四次挥手</h2>
<blockquote>
<p>第一次挥手</p>
</blockquote>
<p>客户端发送FIN报文，传达信息：“你好，我要断开链接”；</p>
<blockquote>
<p>第二次挥手</p>
</blockquote>
<p>服务端回传ACK报文，传达信息：“好的，我知道了，稍等下我可能还有话要说”；</p>
<blockquote>
<p>第三次挥手</p>
</blockquote>
<p>服务端回传FIN+ACK报文，传达信息：“巴拉巴拉说了一通，我说完了”；</p>
<blockquote>
<p>第四次次挥手</p>
</blockquote>
<p>客户端回传ACK报文，传到信息：“好的，我知道了”；这个时候，客户端需要等待足够长的时间，具体来说是2个 MSL(Maximum Segment Lifetime，报文最大生存时间), 在这段时间内如果客户端没有收到服务端的重发请求，那么表示ACK成功到达，挥手结束，否则客户端重发 ACK。</p>
<blockquote>
<p>等待2MSL的意义:</p>
</blockquote>
<p>如果不等待，客户端直接跑路，当服务端还有很多数据包要给客户端发，且还在路上的时候，若客户端的端口此时刚好被新的应用占用，那么就接收到了无用数据包，造成数据包混乱。所以，最保险的做法是等服务器发来的数据包都死翘翘再启动新的应用。</p>
<p>那，照这样说一个 MSL 不就不够了吗，为什么要等待 2 MSL?</p>
<p>1 个 MSL 确保四次挥手中主动关闭方最后的 ACK 报文最终能达到对端</p>
<p>1 个 MSL 确保对端没有收到 ACK 重传的 FIN 报文可以到达</p>
<blockquote>
<p>为什么是四次挥手而不是三次:</p>
</blockquote>
<p>因为服务端在接收到FIN, 往往不会立即返回FIN, 必须等到服务端所有的报文都发送完毕了，才能发FIN。因此先发一个ACK表示已经收到客户端的FIN，延迟一段时间才发FIN。这就造成了四次挥手。
如果是三次挥手会有什么问题？
等于说服务端将ACK和FIN的发送合并为一次挥手，这个时候长时间的延迟可能会导致客户端误以为FIN没有到达客户端，从而让客户端不断的重发FIN。</p>
<h1 data-id="heading-9">HTTP协议结构和通讯原理</h1>
<ul>
<li>简单快速:只需传送请求方法和路径，由于简单规模小所以哦通信速度快。</li>
<li>灵活：允许传输任意类型的数据对象。</li>
<li>无连接：每次连接只请求一个请求，请求完即断开连接。(延伸keep-alive)</li>
<li>无状态：服务器对处理事务无记忆，如果需要处理前面的信息则必须重传，这样可能导致每次连接传送的数据量增大。(延伸cookie,session)</li>
<li>明文传输</li>
</ul>
<h1 data-id="heading-10">迷之兄弟(URI与URL)</h1>
<blockquote>
<p>URL是URI的子集,但不是所有的URI都是URL</p>
</blockquote>
<blockquote>
<p>URI和URL最大的区别是访问机制(ftp,http,telnet...)</p>
</blockquote>
<blockquote>
<p>URN是唯一标识的一部分,是身份信息</p>
</blockquote>
<h1 data-id="heading-11">HTTP请求报文</h1>
<blockquote>
<p>请求行 - 请求头 - 空行 - 实体</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/266f13d2109940e196442a378ccff55c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>报文头</p>
</blockquote>
<ul>
<li>请求报文头 (request Headers)</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73cdcded696a4c74ac634c72504420c6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>响应报文头 (response Headers)</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af3b3a5ac438412eaa90691f261c3218~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Content-Type</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ce23647410d44a29ec240b0585f3c62~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-12">HTTP 实体数据</h1>
<p>数据格式（text img video application） 压缩方式 支持语言 字符集</p>
<h1 data-id="heading-13">HTTP响应报文</h1>
<blockquote>
<p>状态行 - 响应头 - 空行 - 响应体</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4514c86ab3e34524ab7d616468846086~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">HTTP请求方法</h1>
<blockquote>
<p>GET POST PUT HEAD DELETE OPTIONS TRACE CONNECT</p>
</blockquote>
<h1 data-id="heading-15">HTTP状态码</h1>
<blockquote>
<p>1Xx 等待继续</p>
</blockquote>
<blockquote>
<p>2xx成功</p>
</blockquote>
<blockquote>
<p>3xx</p>
</blockquote>
<ul>
<li>301永久重定向做 缓存优化(如域名到期 访问前域名laoction到新的域名，浏览器就记住了新域名)</li>
<li>302临时转义 不做缓存优化(只有这次访问新地址,下次还是访问老地址)</li>
<li>304本地缓存</li>
</ul>
<blockquote>
<p>4xx客户端错误</p>
</blockquote>
<ul>
<li>400错误请求</li>
<li>401未授权</li>
<li>403用户得到授权（与401错误相对），但是访问是被禁止的。</li>
<li>404资源不存在</li>
<li>405请求行中指定的请求方法不能被用于请求相应的资源</li>
</ul>
<blockquote>
<p>5xx</p>
</blockquote>
<ul>
<li>500服务器错误</li>
<li>503服务器负载</li>
</ul>
<h1 data-id="heading-16">HTTP状态管理：Cookie与Session</h1>
<blockquote>
<p>Cookie(存放在客户端)</p>
</blockquote>
<p>服务器向客户端颁发cookie凭证(set-cookie)，客户端浏览器会把cookie存储起来，当再次请求服务器时把请求地址和cookie一同发送给服务器，服务器检查该cookie，以此辨别用户状态。</p>
<p>设置cookie失效时间很长就会保存很长的时间(Expires和Max-Age)。
可以设置cookie的作用域,让浏览器仅发送给特定的服务器和URL。(Domain和Path指定了Cookie所属的域名和路径)，浏览器会在发送cookie前会从URL中提取出host和path部分,对比cookie的属性,如果不满足条件,就不会在请求头里发送cookie。</p>
<p>对客户端是可见的，一些程序可以窥探，赋值或者修改内容。敏感信息尽量不要往cookie中写，或者把cookie信息进行加密。</p>
<p>js脚本使用document.cookie来读写cookie,可能会导致XSS攻击,属性HttpOnly会告诉浏览器,此cookie只能通过浏览器HTTP协议传输,禁止其他方式访问,脚本攻击就无从谈起。</p>
<p>属性SameSite设置为Strict可以严格限定cookie不能随着跳转链接跨站发送,可以防范CSRF攻击。</p>
<p>属性Secure表示cookie仅能用于HTTPS协议的传输。</p>
<blockquote>
<p>Session(存放在服务器)</p>
</blockquote>
<p>保存在服务器上，客户端访问服务器的时候，服务器吧客户端信息以某种形式（生成SessionID和对应的Session）记录在服务器上。客户端再次访问时通过SessionID查找该客户的状态即可。</p>
<p>保存SessionID的正是Cookie，这样浏览器就能把SessionID发送给服务器。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eca3ead195f04e059ef7d90650385168~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>或者另外一种方法是URL重写，将SessionID拼接到URL后面，一路径附加信息的方式</p>
<ul>
<li>
<p>Session超时失效(为了防止内存溢出，服务器会把长时间没有活跃的Session从内存中删除)</p>
</li>
<li>
<p>过多用户会导致服务器压力过大</p>
</li>
</ul>
<h1 data-id="heading-17">HTTP的长连接和短连接</h1>
<p>HTTP协议是基于请求/响应模式的,因此只要服务器给了响应,本次HTTP请求就结束了。</p>
<p>HTTP的长连接和短链接本质上是TCP长连接和短链接。</p>
<p>HTTP/1.0中,默认使用的是短连接，也就是说,浏览器和服务器每进行一次HTTP操作,就建立一次连接,结束就中断。</p>
<p>HTTP/1.1起,默认使用长连接,保持连接状态。(响应头Connection:keep-alive)</p>
<p>短连接：建立连接-数据传输-关闭连接 建立连接-数据传输-关闭连接 ...</p>
<p>长连接：建立连接-数据传输-保持连接-数据传输-关闭连接</p>
<h1 data-id="heading-18">HTTP缓存</h1>
<blockquote>
<p>前面已写过一篇专门谈谈HTTP缓存的传送门</p>
</blockquote>
<p><a href="https://juejin.cn/post/6976915922321833991" target="_blank" title="https://juejin.cn/post/6976915922321833991">juejin.cn/post/697691…</a></p>
<blockquote>
<p>Cache-Control 请求/响应头,缓存控制字段</p>
</blockquote>
<ul>
<li>no-store:所有内容都不缓存。</li>
<li>no-cache:缓存,但是浏览器使用花奴才能前,都会请求服务器判断缓存资源是否是最新。</li>
<li>max-age=x(单位秒):请求缓存后的X秒不再发发起请求。</li>
<li>s-maxage=x(单位秒):代理服务器请求源站缓存后的X秒不再发起请求,只对CDN缓存有效。</li>
<li>public:客户端和代理服务器(CDN)都可缓存。</li>
<li>private:只有客户端可以缓存。</li>
<li>Last-Modified:响应头,资源最新修改时间,由服务器告诉浏览器。</li>
<li>if-Modified-Since:请求头,资源最新修改时间,由浏览器告诉服务器,和Last-Modified是一对,它两会进行对比。</li>
<li>Etag:响应头,资源标识,由服务器告诉浏览器。</li>
<li>if-None-Match:请求头,缓存资源标识,由浏览器告诉服务器(其实就是上次服务器给的Etag),和Etag是一对,它两会进行对比。</li>
</ul>
<blockquote>
<p>DNS缓存</p>
</blockquote>
<p>主要就是在浏览器本地把对应的 IP 和域名关联起来，这样在进行DNS解析的时候就很快。</p>
<blockquote>
<p>浏览器缓存(HTTP缓存)</p>
</blockquote>
<p>先看一张经典的流程图，结合理解</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af5b1b2ed717487f8c0c07b61a407122~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>浏览器缓存，也称Http缓存，分为强缓存和协商缓存。优先级较高的是强缓存，在命中强缓存失败的情况下，才会走协商缓存。</p>
<p>如果命中强缓存不会发送请求到服务器，未命中会发送资源加载请求到服务器并不会返回文件（问缓存的的文件你有没有更新），服务器判断本地缓存是否有效，有效返回304使用本地缓存，无效服务器就将资源返回。</p>
<ul>
<li>强缓存</li>
</ul>
<p>强缓存是利用 http 头中的 Expires 和 Cache-Control 两个字段来控制的。强缓存中，当请求再次发出时，浏览器会根据其中的 expires 和 cache-control 判断目标资源是否“命中”强缓存，若命中则直接从缓存中获取资源，不会再与服务端发生通信。</p>
<p>实现强缓存，过去我们一直用expires。当服务器返回响应时，在 Response Headers中将过期时间写入expires 字段。像这样
expires: Wed, 12 Sep 2019 06:12:18 GMT</p>
<p>可以看到，expires 是一个时间戳，接下来如果我们试图再次向服务器请求资源，浏览器就会先对比本地时间和 expires 的时间戳，如果本地时间小于 expires 设定的过期时间，那么就直接去缓存中取这个资源。</p>
<p>从这样的描述中大家也不难猜测，expires 是有问题的，它最大的问题在于对“本地时间”的依赖。如果服务端和客户端的时间设置可能不同，或者我直接手动去把客户端的时间改掉，那么 expires 将无法达到我们的预期。</p>
<p>考虑到 expires 的局限性，HTTP1.1 新增了Cache-Control字段来完成 expires 的任务。expires 能做的事情，Cache-Control 都能做；expires 完成不了的事情，Cache-Control 也能做。因此，Cache-Control 可以视作是 expires 的完全替代方案。在当下的前端实践里，我们继续使用expires 的唯一目的就是向下兼容。
cache-control: max-age=31536000</p>
<p>在 Cache-Control 中，我们通过max-age来控制资源的有效期。max-age 不是一个时间戳，而是一个时间长度。在本例中，max-age 是 31536000 秒，它意味着该资源在 31536000 秒以内都是有效的，完美地规避了时间戳带来的潜在问题。</p>
<p>Cache-Control 相对于 expires 更加准确，它的优先级也更高。当Cache-Control与expires同时出现时，我们以 Cache-Control 为准。</p>
<p>为什么要强缓存 服务器配置有限 并发数有限</p>
<ul>
<li>协商缓存</li>
</ul>
<p>协商缓存依赖于服务端与浏览器之间的通信。协商缓存机制下，浏览器需要向服务器去询问缓存的相关信息，进而判断是重新发起请求、下载完整的响应，还是从本地获取缓存的资源。如果服务端提示缓存资源未改动（Not Modified），资源会被重定向到浏览器缓存，这种情况下网络请求对应的状态码是 304。</p>
<p>协商缓存的实现,从 Last-Modified 到 Etag,Last-Modified 是一个时间戳，如果我们启用了协商缓存，它会在首次请求时随着 Response Headers 返回：
Last-Modified: Fri, 27 Oct 2017 06:35:57 GMT</p>
<p>随后我们每次请求时，会带上一个叫 If-Modified-Since 的时间戳字段，它的值正是上一次 response 返回给它的 last-modified 值：
If-Modified-Since: Fri, 27 Oct 2017 06:35:57 GMT</p>
<p>服务器接收到这个时间戳后，会比对该时间戳和资源在服务器上的最后修改时间是否一致，从而判断资源是否发生了变化。如果发生了变化，就会返回一个完整的响应内容，并在 Response Headers 中添加新的 Last-Modified 值；否则，返回如上图的 304 响应，Response Headers 不会再添加 Last-Modified 字段。</p>
<p>使用 Last-Modified 存在一些弊端，这其中最常见的就是这样两个场景：</p>
<p>我们编辑了文件，但文件的内容没有改变。服务端并不清楚我们是否真正改变了文件，它仍然通过最后编辑时间进行判断。因此这个资源在再次被请求时，会被当做新资源，进而引发一次完整的响应——不该重新请求的时候，也会重新请求。</p>
<p>当我们修改文件的速度过快时（比如花了 100ms 完成了改动），由于 If-Modified-Since 只能检查到以秒为最小计量单位的时间差，所以它是感知不到这个改动的——该重新请求的时候，反而没有重新请求了。</p>
<p>这两个场景其实指向了同一个bug——服务器并没有正确感知文件的变化。为了解决这样的问题，Etag 作为 Last-Modified 的补充出现了。</p>
<p>Etag 是由服务器为每个资源生成的唯一的标识字符串，这个标识字符串可以是基于文件内容编码的，只要文件内容不同，它们对应的 Etag 就是不同的，反之亦然。因此 Etag 能够精准地感知文件的变化。</p>
<p>Etag 的生成过程需要服务器额外付出开销，会影响服务端的性能，这是它的弊端。因此启用 Etag 需要我们审时度势。正如我们刚刚所提到的——Etag 并不能替代 Last-Modified，它只能作为 Last-Modified 的补充和强化存在。</p>
<p>Etag 在感知文件变化上比 Last-Modified 更加准确，优先级也更高。当 Etag 和 Last-Modified 同时存在时，以 Etag 为准。</p>
<ul>
<li>expires与cache-control区别</li>
</ul>
<p>expires是绝对时间，服务器与浏览器时间不同步会有问题。
cache-control是相对时间</p>
<ul>
<li>last-modify和Etag区别</li>
</ul>
<p>last-modify：精度问题 到秒
Etag:没有精度问题，只要文件改变，e-tag值就改变</p>
<blockquote>
<p>缓存位置</p>
</blockquote>
<p>当强缓存命中或者协商缓存中服务器返回304的时候，我们直接从缓存中获取资源。那这些资源究竟缓存在什么位置呢？</p>
<ul>
<li>Service Worker Cache</li>
</ul>
<p>Service Worker 是一种独立于主线程之外的 Javascript 线程。它脱离于浏览器窗体，因此无法直接访问 DOM。这样独立的个性使得 Service Worker 的“个人行为”无法干扰页面的性能，这个“幕后工作者”可以帮我们实现离线缓存、消息推送和网络代理等功能。我们借助 Service worker 实现的离线缓存就称为 Service Worker Cache。
Service Worker 的生命周期包括 install、active、working 三个阶段。一旦 Service Worker 被 install，它将始终存在，只会在 active 与 working 之间切换，除非我们主动终止它。这是它可以用来实现离线存储的重要先决条件.</p>
<ul>
<li>Memory Cache 和 Disk Cache</li>
</ul>
<p>Memory Cache是指存在内存中的缓存。从优先级上来说，它是浏览器最先尝试去命中的一种缓存。从效率上来说，它是响应速度最快的一种缓存。 内存缓存是快的，也是“短命”的。它和渲染进程“生死相依”，当进程结束后，也就是 tab 关闭以后，内存里的数据也将不复存在。</p>
<p>Disk Cache就是存储在磁盘中的缓存，从存取效率上讲是比内存缓存慢的，但是他的优势在于存储容量和存储时长。</p>
<p>比较大的JS、CSS文件会直接被丢进磁盘，反之丢进内存
内存使用率比较高的时候，文件优先进入磁盘</p>
<ul>
<li>Push Cache</li>
</ul>
<p>Push Cache 是指 HTTP2 在 server push 阶段存在的缓存。这块的知识比较新，应用也还处于萌芽阶段，应用范围有限不代表不重要——HTTP2 是趋势、是未来。在它还未被推而广之的此时此刻，我仍希望大家能对 Push Cache 的关键特性有所了解：
Push Cache 是缓存的最后一道防线。浏览器只有在 Memory Cache、HTTP Cache 和 Service Worker Cache 均未命中的情况下才会去询问 Push Cache。
Push Cache 是一种存在于会话阶段的缓存，当 session 终止时，缓存也随之释放。
不同的页面只要共享了同一个 HTTP2 连接，那么它们就可以共享同一个 Push Cache。</p>
<blockquote>
<p>md5/hash缓存</p>
</blockquote>
<p>通过不缓存html,为静态文件添加MD5或者hash标识,解决浏览器无法跳过缓存过期时间主动感知文件变化的问题。</p>
<blockquote>
<p>CDN缓存</p>
</blockquote>
<p>服务器将文件给CDN,CDN进行缓存,同时CDN返回给浏览器,当浏览器文件超过过期时间,会找到CDN,第一种情况,CDN缓存时间未过期返回304给浏览器。第二种情况CDN发现自己缓存的文件过期了,自己发送请求给服务器拿货最新的文件再返回给浏览器。CDN的优势在于分流,类似一个平台可以通过登录手动更新缓存变相解决了文件变化了,浏览器无法感知。</p>
<h1 data-id="heading-19">HTTPS</h1>
<p>HTTP以明文的方式进行传输,相当于裸奔，有可能被中间人恶意拦截篡改。</p>
<blockquote>
<p>什么是安全</p>
</blockquote>
<p>机密性 完整性 身份认证 不可否认</p>
<blockquote>
<p>对称加密(秘钥加密)</p>
</blockquote>
<ul>
<li>
<p>加密解密使用相同秘钥,第一次通信服务器返回秘钥,浏览器使用此秘钥进行加密传输</p>
</li>
<li>
<p>但如果中间人第一次就拦截到了秘钥，中间人一样可以解密恶意拦截篡改。</p>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc65f93b67b3474489d0788f47e547e8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>非对称加密(公钥加密)</p>
</blockquote>
<ul>
<li>
<p>加密解密使用不同秘钥，第一次通信服务器返回公钥，接着浏览器生成一个用于对称加密的秘钥,用公钥对此秘钥进行加密发送给服务器，服务器用非对称加密的私钥来解开公钥的加密获得对称加密的秘钥，然后使用对称加密的秘钥进行内容加密传输给浏览器。</p>
</li>
<li>
<p>中间人能劫持到公钥，但不知道私钥是什么所以不能解密，但是中间人依然可以搞破坏，劫持公钥返回虚假公钥，浏览器使用此虚假公钥对对称加密的秘钥进行加密，中间人就能通过虚假私钥获取到秘钥，然后篡改内容发送给服务器。</p>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0023bd2ec12e4c91915f8ab12af1ebd9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>证书机构(第三方)</p>
</blockquote>
<p>服务端先把公钥发给证书颁发机构,由证书颁发机构去申请证书,证书颁发机构有一对自己的公钥和私钥,机构用自己的私钥来加密服务端发来的公钥,并且通过服务端网址等信息生成一个证书签名,证书签名同样通过了机构私钥的加密，这样制作完成了一个证书,机构把此证书发送给服务端。</p>
<p>当浏览器向服务端请求通信时,服务端直接返回证书给浏览器,浏览器验证证书真伪,各大浏览器已经维护了所有权威机构证书的名称和公钥,所以只要知道是哪个机构颁布的证书就能从本地找到机构的公钥解密出证书的签名,</p>
<p>如果能解密成功，就可以得到证书机构给我们网站颁发的证书了，其中当然也包括了服务端的公钥。</p>
<p>接着浏览器生成一个用于对称加密的秘钥,用公钥对此秘钥进行加密发送给服务器，服务器用非对称加密的私钥来解开公钥的加密获得对称加密的秘钥，然后使用对称加密的秘钥进行内容加密传输给浏览器。</p>
<p>证书签名是由服务端网址等信息生成的,并且通过了机构的私钥加密,中间人是没办法篡改的,所以中间人无法造假证书。</p>
<blockquote>
<p>结论</p>
</blockquote>
<p>HTTPS是在HTTP的基础上增加了一个安全层，一系列的加码认证流程都是在这安全层当中完成的。</p>
<p>HTTPS = HTTP + TLS,由HTTP over TCP/IP 变成了 HTTP over SSL/TLS。</p>
<p>TLS是传输层加密协议,它的前身是SSL协议。建立在传输层和应用层之间也就是HTTP和TCP之间</p>
<p>HTTPS会先与服务器TCP握手,然后执行TLS握手,才能建立安全连接。</p>
<h1 data-id="heading-20">SPDY</h1>
<blockquote>
<p>HTTP缺陷</p>
</blockquote>
<ul>
<li>
<p>单路连接</p>
</li>
<li>
<p>只允许由客户端主动发起请求</p>
</li>
<li>
<p>HTTP头部冗余，浪费带宽</p>
</li>
</ul>
<blockquote>
<p>SPDY的改进</p>
</blockquote>
<ul>
<li>
<p>多路复用 请求优化,在一个SPDY连接内可以有无限个并行的请求,也就是说允许多个并发的HTTP请求公用一个TCP会话，减少TCP连接。</p>
</li>
<li>
<p>支持服务器推送技术</p>
</li>
<li>
<p>压缩了HTTP头,舍弃掉了一些不必要的HEAD信息</p>
</li>
<li>
<p>强制使用SSL传输协议</p>
</li>
</ul>
<h1 data-id="heading-21">HTTP 2.0</h1>
<blockquote>
<p>增强核心:二进制分帧</p>
</blockquote>
<ul>
<li>
<p>首部消息会以二进制的方式封到Headers层 请求体被封装到Data层</p>
</li>
<li>
<p>可以乱序发送(并行双向字节流的请求和响应),客户端和服务器可以把消息分成互不依赖的帧,乱序发送,最后再另一端根据标识重新组合起来，并行交错的发送请求,请求之间互不影响,并行交错的发送响应,响应之间互不干扰,只使用一个连接即可并行发送多个请求和响应,消除了不必要的延迟，减少页面加载时间。高优先级的流都应该优先发送,优先级不是绝对的,不同优先级混合也是必须的。</p>
</li>
</ul>
<blockquote>
<p>头部压缩</p>
</blockquote>
<p>HTTP 2.0之前头部会带有大量信息,并且每次都会发送, HTTP 2.0使用压缩的方式解决了需要传输HEAD的大小,通讯双份各自缓存一份首部表,避免了重复的Header传输又减小了传输的大小。</p>
<blockquote>
<p>多路复用</p>
</blockquote>
<p>HTTP 2.0都在同一个TCP连接上完成,把通信单位缩小成为帧,减少服务连接压力,内存占用少,连接吞吐量大。由于TCP连接少了使网络拥塞状况得以改观。</p>
<blockquote>
<p>服务器推送</p>
</blockquote>
<p>服务器可以对客户端一个请求发送多个响应,可额外向客户端推送资源。</p>
<h1 data-id="heading-22">HTTP2.0存在问题</h1>
<blockquote>
<p>队头堵塞</p>
</blockquote>
<p>因为多路复用,使用同一个TCP连接,当存在丢包的情况下,整个TCP就要等待重传,导致后面的数据都被阻塞。</p>
<blockquote>
<p>建立连接的握手延迟大</p>
</blockquote>
<h1 data-id="heading-23">QUIC(基于UDP)的特性 HTTP 3.0的底层支持协议</h1>
<blockquote>
<p>没有队头阻塞的多路复用</p>
</blockquote>
<p>因为UDP是无状态,不用事先建立连接就可以任意发送数据,根本不需要握手和挥手,丢包不会影响后面数据的传输,所以从根本上解决了队头堵塞。</p>
<h1 data-id="heading-24">关于安全</h1>
<h2 data-id="heading-25">SQL注入</h2>
<blockquote>
<p>是啥</p>
</blockquote>
<p>用户可以提交一段数据库查询代码,根据程序返回结果获取其他数据。</p>
<blockquote>
<p>防御</p>
</blockquote>
<p>采用参数化查询方式也叫预处理语句,先指定查询结果,用户输入预留占位符,然后再指定占位符的内容。</p>
<h2 data-id="heading-26">XSS(跨站脚本)攻击</h2>
<blockquote>
<p>是啥</p>
</blockquote>
<p>攻击者往Web页面里插入恶意Script代码，当用户浏览该页之时，嵌入其中Web里面的Script代码会被执行，从而达到恶意攻击用户的目的。</p>
<blockquote>
<p>三类</p>
</blockquote>
<ul>
<li>反射的 XSS攻击:</li>
</ul>
<p>xss代码在请求的url中，而后提交到服务器，服务器解析后，XSS代码随着响应内容一起传给客户端进行解析执行</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0104ce0bb6e944e9a884ef07d91d9a5c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>存储的 XSS攻击:</li>
</ul>
<p>具有攻击性的脚本被保存到了服务器端（数据库，内存，文件系统）并且可以被普通用户完整的从服务的取得并执行，从而获得了在网络上传播的能力。</p>
<ul>
<li>基于DOM或本地的XSS攻击:</li>
</ul>
<p>通过dom来触发js脚本,在网页input或者textarea中输入或者其他脚本。</p>
<blockquote>
<p>防御：</p>
</blockquote>
<ul>
<li>输入过滤</li>
</ul>
<p>采用所预期的字符的内容提交，对其他的一律过滤</p>
<ul>
<li>输出转义</li>
</ul>
<p>将不可信数据插入到HTML URL里时，对这些数据进行URL编码</p>
<ul>
<li>使用 HttpOnly Cookie</li>
</ul>
<p>将重要的cookie标记为httponly，这样的话当浏览器向Web服务器发起请求的时就会带上cookie字段，但是在js脚本中却不能访问这个cookie，这样就避免了XSS攻击利用JavaScript的document.cookie获取cookie。</p>
<h2 data-id="heading-27">CSRF(跨站请求伪造)</h2>
<blockquote>
<p>是啥</p>
</blockquote>
<p>用户登陆了a网站，然后跳转到b网站，b网站直接发送一个a网站的请求，携带的是a网站域名下的cookie，进行一些危险操作。</p>
<blockquote>
<p>防御：</p>
</blockquote>
<ul>
<li>
<p>放弃cookie在请求地址中添加 token 并验证在请求中放入黑客所不能伪造的信息，并且该信息不存在于 cookie 之中。可以在 HTTP 请求中以参数的形式加入一个随机产生的 token，并在服务器端建立一个拦截器来验证这个 token，如果请求中没有 token 或者 token 内容不正确，则认为可能是 CSRF 攻击而拒绝该请求。</p>
</li>
<li>
<p>在 HTTP 头中自定义属性并验证这里并不是把 token 以参数的形式置于 HTTP 请求之中，而是把它放到 HTTP 头中自定义的属性里。通过 XMLHttpRequest 这个类，可以一次性给所有该类请求加上 csrftoken 这个 HTTP 头属性，并把 token 值放入其中。</p>
</li>
<li>
<p>Cookie有一个新的属性——SateSite</p>
</li>
</ul>
<p>它表示，只能当前域名的网站发出的http请求，携带这个Cookie。当然，由于这是新的cookie属性，在兼容性上肯定会有问题。</p>
<ul>
<li>服务端Referer验证</li>
</ul>
<p>发送的http请求中，header中会带有Referer字段，这个字段代表的是当前域的域名，服务端可以通过这个字段来判断，是不是“真正”的用户请求。</p>
<h1 data-id="heading-28">Post Get 区别</h1>
<blockquote>
<p>缓存角度:get浏览器主动缓存 post不会</p>
</blockquote>
<p>get请求的是静态资源，则会缓存，如果是数据，则不会缓存，但是IE什么都会缓存起来</p>
<blockquote>
<p>参数角度:get放在url中 post放在请求体中</p>
</blockquote>
<p>post发送的数据更大（get有url长度被浏览器和web服务器限制）</p>
<blockquote>
<p>安全角度: get不太安全 post安全一丢丢</p>
</blockquote>
<p>post更安全（不会作为url的一部分，不会被缓存、保存在服务器日志、以及浏览器浏览记录中）</p>
<blockquote>
<p>使用角度: get主要读取 post则为修改</p>
</blockquote>
<p>post用于修改和写入数据，get一般用于搜索排序和筛选之类的操作，目的是资源的获取，读取数据</p>
<h1 data-id="heading-29">HTTP1 和 HTTP2 和 HTTP3的总结</h1>
<blockquote>
<p>HTTP1.1 的缺陷</p>
</blockquote>
<ul>
<li>高延迟 — 队头阻塞</li>
<li>无状态特性 — 阻碍交互</li>
<li>明文传输 — 不安全性</li>
<li>不支持服务端推送</li>
</ul>
<blockquote>
<p>HTTP2 基于 SPDY（由 google 推行的改进版本的 HTTP1.1），新增特性：</p>
</blockquote>
<ul>
<li>二进制分帧 - HTTP2 性能增强的核心</li>
<li>多路复用 - 解决串行的文件传输和连接数过多</li>
<li>头部压缩 — 解决巨大的 HTTP 头部通过gzip和compress压缩头部然后再发送</li>
<li>请求优先级 — 先获取重要数据</li>
<li>服务端推送 — 填补空缺</li>
<li>提高安全性</li>
</ul>
<blockquote>
<p>HTTP2 的缺陷</p>
</blockquote>
<ul>
<li>TCP 以及 TCP+TLS 建立连接的延时</li>
<li>TCP 的队头阻塞并没有彻底解决</li>
<li>多路复用导致服务器压力上升</li>
<li>多路复用容易 Timeout</li>
</ul>
<blockquote>
<p>HTTP/3 最大的改造就是使用了 QUIC，真正“完美”地解决了“队头阻塞”问题。</p>
</blockquote>
<ul>
<li>QUIC 基于 UDP 实现，是 HTTP/3 中的底层支撑协议，该协议基于 UDP，又取了 TCP 中的精华，实现了即快又可靠的协议：</li>
<li>基于UDP协议改造，实现了快速的握手；</li>
<li>多路复用，彻底解决了头阻塞问题；</li>
</ul>
<h1 data-id="heading-30">CDN(内容分发网络)</h1>
<p>专门为了解决"长距离"上网络访问速度慢二诞生的一种网络应用服务。</p>
<blockquote>
<p>核心原则</p>
</blockquote>
<p>就近访问，不访问源站直接访问边缘节点，其实就是访问缓存了源站内容的代理服务器。</p>
<blockquote>
<p>关键组成部分</p>
</blockquote>
<ul>
<li>GSLB 全局负载均衡</li>
</ul>
<p>在CDN专网中挑出一个最佳的节点，对整个CDN网络进行负载均衡，最常见的实现方式是DNS负载均衡，加入CDN后，DNS不在返回IP地址,而是一个别名记录，告诉外边我这里没法给你真正的地址，你去其他地方找找吧。因为没有拿到IP地址,DNS就会向GSLB发送请求，进入全局负载均衡系统开始智能调度根据位置,运营网络，边缘节点负载情况，带宽，响应时间等使用复杂的算法，找出一台最适合的边缘节点，把这个节点的IP地址返回给用户，用户就可以就近访问CDN的缓存代理了。</p>
<ul>
<li>缓存系统</li>
</ul>
<p>缓存系统只能有选择的缓存那些最常用的资源，提升硬件软件，使用高性能的缓存服务，缓存命中就返回，否则就要回源。</p>
<h1 data-id="heading-31">HTTP性能优化</h1>
<blockquote>
<p>开源(抓源头 开发服务器自身潜力)</p>
</blockquote>
<ul>
<li>
<p>更强的CPU 更快的网卡 更大的带宽 更多的服务器</p>
</li>
<li>
<p>物有所值的CDN</p>
</li>
<li>
<p>高性能的服务器,对于HTTP协议启动长连接，TCP和SSL简历新连接的成本是非常高的，长连接虽然不能优化连接握手，但可以把成本均摊到多次请求里，这样只有第一次请求可能会有延迟，之后的请求就不会有连接延迟了。</p>
</li>
<li>
<p>TCP新特性TCP Fast Open，可以再初次握手就传输数据，尽量在Nginx中开启此特性，减少外网和内网的握手延迟。</p>
</li>
</ul>
<blockquote>
<p>节流(减少客户端和服务器之间收发的数据量，在优先的带宽里传输更多的内容)</p>
</blockquote>
<ul>
<li>
<p>开启gzip 或br压缩</p>
</li>
<li>
<p>图片适当减低分辨率，缩小尺寸，尽量选择搞压缩率的格式，有损格式用JPEG，无损格式用Webp</p>
</li>
<li>
<p>不必要的头部字段尽量不发</p>
</li>
<li>
<p>cookie冗余度很高,减少使用cookie，减少cookie记录的数据量，总使用domain和path属性限定cookie的作用域。</p>
</li>
<li>
<p>DNS解析域名会消耗不少时间，如果网站拥有多个域名，那么域名解析获取IP是一个不小的成本，适当限制域名在两三个左右。</p>
</li>
</ul>
<blockquote>
<p>缓存</p>
</blockquote>
<ul>
<li>
<p>没有请求的请求，才是最快的请求</p>
</li>
<li>
<p>利用好强缓存和协商缓存</p>
</li>
<li>
<p>CDN加速应建立在缓存的基础上发挥到极致</p>
</li>
</ul>
<blockquote>
<p>HTTP升级</p>
</blockquote>
<ul>
<li>将协议HTTP/1升级到HTTP/2,HTTP/2的有很多有点,消除了队头阻塞，拥有头部压缩，二进制帧，多路复用，服务器推送等新特性。大幅度提升了HTTP的传输效率。</li>
</ul>
<h1 data-id="heading-32">Restful API</h1>
<p>一种新的API设计方法</p>
<p>传统API设计：把每个url当做一个功能</p>
<p>Restful API设计：把每个url当做一个唯一的资源</p>
<blockquote>
<p>如何设计成一个资源</p>
</blockquote>
<ul>
<li>
<p>尽量不使用url参数</p>
<p>传统API设计：/api/list?pageCur=2</p>
<p>Restful API设计：/api/list/2</p>
</li>
<li>
<p>用method表示操作类型</p>
<p>传统API设计：</p>
<ol>
<li>
<p>post请求：/api/creatList</p>
</li>
<li>
<p>post请求：/api/updateList?id=001</p>
</li>
<li>
<p>get请求：/api/getList?id=001</p>
</li>
</ol>
<p>Restful API设计：</p>
<ol>
<li>
<p>post请求：/api/list</p>
</li>
<li>
<p>patch请求：/api/list/001</p>
</li>
<li>
<p>get请求：/api/list/001</p>
</li>
</ol>
</li>
</ul></div>  
</div>
            