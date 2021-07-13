
---
title: '从输入URL到页面呈现【超详细】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44e2592df7234d509ba8ecdb462d7056~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 01:25:39 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44e2592df7234d509ba8ecdb462d7056~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">解析地址栏中的信息</h2>
<p>浏览器监听用户输入的信息并尝试匹配你想要访问的网址或关键词。以掘金为例，在浏览器地址栏中输入信息，然后回车，浏览器会进行以下判断：</p>
<ul>
<li>判断是否是合法的 URL 链接；</li>
<li>是。继续判断 URL 是否完整，如果不完整，浏览器可能会对域进行猜测，对输入的内容添加前缀、后缀、或者前后缀来补全 URL，常见的 URL 通产包括：
<ul>
<li>协议：如 <code>http</code> <code>https</code> <code>websocket</code></li>
<li>域名（主机名）：可能是IP地址，也可能是域名。域名可能由根域名、顶级域名、二级域名等组成，域名的叫法是根据域名从右向左以 <code>.</code> 分隔进行划分，比如：<code>juejin.cn.</code>，<code>.</code> 代表根域名，<code>.cn</code> 代表顶级域名，<code>juejin.cn</code> 代表二级域名（也就是主机名）</li>
<li>端口号：http 协议默认端口号为 80，https 协议默认端口号为 443。浏览器会自动隐藏默认端口号。</li>
<li>路径：以 <code>/</code> 划分每一层目录，比如：<code>/web/user</code></li>
<li>查询：以 <code>?</code>  开始，以 <code>&</code> 分隔键值对，如：<code>?username="张三"&age=16</code></li>
<li>哈希：以<code>#</code> 开始，利用它可实现定位到当前页面的具体位置</li>
</ul>
</li>
<li>否。浏览器将输入的内容作为搜索条件，使用用户设置的默认搜索引擎进行查询并返回结果</li>
</ul>
<h2 data-id="heading-1">查找强缓存</h2>
<p>浏览器进程通过进程间通信（IPC）将 URL 请求发送给网络进程，网络进程接收到URL请求后，会发起真正的请求。但在请求之前，网络进程会查找本地是否缓存了该资源。如果有缓存资源，那么直接返回资源给浏览器进程。首选，查找强缓存资源，如果有则检查强缓存资源是否过期，没过期直接使用该资源，过期则重新向服务器请求资源。强缓存涉及到两个字段：</p>
<ul>
<li><code>Expires</code>。即过期时间<code>（Expires=Wed, 21 Oct 2015 07:28:00 GMT）</code>，HTTP/1.0 采用此字段，它存在于服务器返回的响应头中，告知浏览器在过期时间范围内直接使用缓存资源。但它有个很大的缺点，当服务器和客户端的时间不一致时，那么服务器返回的时间是不准确的，因此，HTTP/1.1 抛弃了这个字段而采用了 <code>Cache-Control</code>字段</li>
<li><code>Cache-Control</code>。即过期时长<code>（Cache-Control:max-age=3600）</code>，HTTP/1.1 采用此字段，它也存在于服务器返回的响应头中，告知浏览器在过期时长范围内直接使用缓存资源。它还可以设置其他指令，下面列举一些关键指令：
<ul>
<li><code>public</code>。浏览器和代理服务器都可以缓存资源</li>
<li><code>private</code>。只能浏览器缓存资源，代理服务器不能缓存资源</li>
<li><code>no-cache</code>。跳过强缓存阶段。向服务器发送请求，进入协商缓存阶段</li>
<li><code>no-store</code>。不缓存</li>
<li><code>s-maxage</code>。代理服务器的缓存时间</li>
<li><code>must-revalidate</code>。一旦缓存过期，就必须回到源服务器验证</li>
</ul>
</li>
</ul>
<p>扩展：</p>
<ul>
<li>怎么设置强缓存？可以在服务端代码中设置 <code>Cache-Control</code> 字段以及他对应的值；</li>
<li>强缓存资源缓存在哪儿？ <code>memory cache</code> 或 <code>disk cache</code> ，也就是内存或硬盘中，一般会将图片、脚本文件、字体文件缓存在 <code>memory cache</code> 中；将样式文件缓存在 <code>disk cache</code> 中。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44e2592df7234d509ba8ecdb462d7056~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddd879d011c5440098335cd5655ba296~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>访问缓存的优先级？遵循三级缓存原理：先在 <code>memory cache</code> 中找，有则直接使用；没有再去 <code>disk cache</code> 中找，有则指直接使用；没有就进行网络请求，将请求返回的资源根据响应头字段信息进行缓存。</li>
</ul>
<h2 data-id="heading-2">DNS域名解析</h2>
<p>如果在强缓存中没有找到所需资源，那么直接进入网络请求流程。通常情况下，我们在浏览器的地址栏中输入的都是域名，而在网络通信中是以 IP 地址确定目的主机的，所以还得通过域名找到对应的 IP 地址。
DNS 又是什么？DNS全名是 <code>domain name system（域名系统）</code>，它将域名和 IP 地址映射关系保存在一个分布式数据库中，所以我们可以通过 DNS 找到对应的 IP，而这个查找的过程就是 DNS 域名解析。下面以 <code>juejin.cn.</code>来分析域名的解析过程：</p>
<ul>
<li>浏览器 DNS 缓存。浏览器从 URL 中提取出主机名，从浏览器 DNS 中查找是否有缓存记录，有则直接使用缓存IP，完成解析；</li>
<li>hosts 文件。从本机的 hosts 文件中查找是否有缓存记录，有则返回对应 IP，完成解析；</li>
<li>本地 DNS 服务器。向本地 DNS 服务器发送查询请求，有则本地 DNS 服务器将记录作为响应返回给主机，完成解析；</li>
<li>ISP（互联网服务提供商）DNS缓存。本地 DNS 服务器将查询请求转发给 ISP 提供的 DNS 服务器，有则将记录作为响应返回给本地 DNS 服务器，本地 DNS 服务器返回给主机，完成解析；</li>
<li>根域名服务器。根据本地 DNS 服务器的设置（是否设置转发器）进行查询，若是未用转发模式，本地 DNS 就把请求发至 13 台根域名服务器 ，根域名服务器收到请求后会判断这个域名（<code>.cn</code>）是谁来授权管理，并会返回一个负责该顶级域名服务器的一个IP。若是转发模式，该 DNS 服务器就会把请求转发至上一级 DNS 服务器，由上一级服务器进行解析，上一级服务器如果不能解析，或找根域名服务器或将请求转至上上级，以此循环；</li>
<li>顶级域名服务器。从根域名服务器得到顶级域名服务器地址后，本地 DNS 服务器向顶级域名服务器发送查询请求，收到本地域名服务器请求后会查看区域文件记录，有则将记录作为响应返回给本地 DNS 服务器，由本地 DNS 服务器返回给主机，完成解析。如果自己无法解析，它就会找一个管理（<code>.cn</code>）域的二级域名服务器 IP 返回给本地DNS服务器；</li>
<li>二级域名服务器。从顶级域名服务器得到二级域名服务器地址后，本地 DNS 服务器向二级域名服务器发送查询请求，二级域名服务器收到本地域名服务器请求后会查看区域文件记录，若有则将记录返回给本地 DNS 服务器，完成解析。到这一步还是没能完成解析，那域名可能存在错误而产生异常。</li>
</ul>
<p>递归查询：
客户端向本地 DNS 服务器发起查询请求，等待本地域名服务器返回结果。本地 DNS 服务器若无法解析，自己会以DNS客户机的身份向其他域名服务器发起查询请求，直到将查询结果返回给客户端为止。</p>
<p>迭代查询：本地 DNS 服务器首先向根域名服务器发起查询请求，若根域名没有找到对应记录就将下一个目标域名服务器的 IP 返回给本地 DNS 服务器（也称为根提示），直到将查询结果返回给客户端为止。</p>
<h2 data-id="heading-3">建立TCP连接</h2>
<p>建立连接遵循三次握手原则。三次握手的主要目的就是确认双方的接收能力和发送能力是否正常、指定自己的初始化序列号为后面的可靠性传送做准备。实质上就是连接服务器指定端口，建立 TCP 连接，并同步连接双方的序列号和确认号，交换 TCP 窗口大小信息。现在，客户端处于 <code>Closed</code> 状态，服务端处于 <code>Listen</code> 状态</p>
<ul>
<li>客户端给服务端发出一个连接SYN报文，并指明<code>同步位SYN=1，初始序号seq=x</code>，然后客户端处于 <code>SYN_SEND</code> 状态；</li>
<li>服务器收到客户端的SYN报文后，会以自己的 SYN 报文 <code>（SYN=1，ACK=1）</code> 作为应答，并且指定自己的初始化序列号 <code>seq=y</code> ，同时会把客户端的 <code>seq + 1 = x + 1</code> 作为 ack 的值 <code>（ack=x+1）</code> ，表示自己已经收到客户端的 <code>SYN报文</code>，此时服务器处于 <code>SYN_REVD</code> 状态；</li>
<li>客户端收到 <code>SYN报文</code> 后，会发送一个 ACK 报文 <code>（ACK=1）</code> 作为应答，并且之地当自己的序列号 <code>seq=x+1</code> ，同时会把服务器的 <code>seq + 1 = y + 1</code> 作为 ack 的值 <code>（ack=y+1）</code> ，表示自己已经收到服务器的 <code>SYN报文</code> ，此时客户端处于 <code>ESTABLISHED</code> 状态，服务器收到 ACK 报文之后，也处于 ESTABLISHED 状态，此时，双方已建立起了连接。</li>
</ul>
<h2 data-id="heading-4">客户端发起请求，服务器处理请求</h2>
<p>客服端会将请求行、请求头，请求体的相应信息发送给服务器。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f462a5c3d99d4fdaa51f55a0c01b40a4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
服务器收到请求后进行逻辑处理，并根据处理结果返回响应数据（响应行、响应头、响应体等）。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04085d369cde4d99981e9200d3c32882~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这里提一下 HTTP 数据传输过程中的优化策略。在 HTTP 数据传输的过程中会将报文进行拆包（将报文拆分成小的数据包），依次传输给接收方，接收方每次接收到数据包后必须向发送方确认，如果发送方没有收到这个确认的消息，就判定为数据包丢失，并重新发送该数据包，接收方需要完成组包（将每次接收的数据包按顺序组装为完整的数据包）从而获得完整的数据包。</p>
<h2 data-id="heading-5">关闭TCP连接</h2>
<p>数据传输完毕后还要根据 <code>Connection</code> 字段判断是否需要断开连接，若请求头或响应头中包含 <code>Connection: Keep-Alive</code> 表示持久连接，之后请求同一站点的资源会复用此连接；不满足上述情况就需要断开连接，断开连接遵循四次挥手原则。断开连接这个动作可以由客户端或者服务器任一方发起，此时，客户端和服务器都处于 <code>ESTABLISHED</code> 状态，假设由客户端发起关闭请求，则流程如下：</p>
<ul>
<li>客户端发起一个连接释放 FIN 报文段 <code>（FIN=1）</code> ，报文中指定一个序列号 <code>（seq=u）</code> ，并停止发送数据，关闭 TCP 连接。客户端进入 <code>FIN_WAIT1（终止等待1）</code> 状态，等待服务器的确认；</li>
<li>服务器收到连接释放的FIN报文段后，会发出 ACK 报文 <code>（ACK=1）</code> ，并指定自己的序列号 <code>（seq=v）</code> ，同时会把客户端的 <code>seq + 1 = u + 1</code> 作为 ack 的值 <code>（ack=u+1）</code>，表明已经收到客户端的报文了。服务端进入 <code>CLOSE_WAIT（关闭等待）</code> 状态，此时的TCP处于半关闭状态，客户端到服务端的连接释放。客户端收到服务端的确认后，进入 <code>FIN_WAIT2（终止等待2）</code> 状态，等待服务端发出的连接释放报文段；</li>
<li>若此时服务器已经没有数据需要发送给客户端了，服务器就会发出连接释放报文段 <code>（FIN=1, ACK=1, 序列号seq=w, 确认号ack=u+1）</code> ，服务端进入 <code>LAST_ACK（最后确认）</code> 状态，等待客户端的确认；</li>
<li>客户端收到服务端的连接释放报文后，对此发出确认报文段 <code>（ACK=1, seq=u+1, ack=w+1）</code> ，客户端进入 <code>TIME_WAIT（时间等待）</code> 状态。此时TCP未释放掉，需要经过时间等待计时器设置的时间<code>2MSL</code>后，客户端才进入 <code>CLOSED</code> 状态。</li>
</ul>
<h2 data-id="heading-6">处理响应信息</h2>
<p>网络进程接收到响应数据后开始解析响应头，解析到响应状态码会根据不同的码值进行处理，下面列举一下常用的状态码：</p>
<ul>
<li><code>200 OK</code>。请求处理成功，响应数据放在响应体中。</li>
<li><code>301 Moved Permanently</code> 。永久重定向，如果以前的域名地址不再使用，需要更换新的域名地址来访问资源，可以将响应状态码置为301，浏览器默认会做缓存优化，再次访问原地址时会自动访问重定向的那个地址</li>
<li><code>302 Found</code>。临时重定向，若只是暂时不使用原地址可以返回 <code>302</code> 状态码。如：网站正在维护，那么可以在当前域给出一个解释页面来通知访问者</li>
<li><code>304 Not Modified</code>。协商缓存。浏览器首次请求资源时，服务器会将 <code>Last-Modified</code> 和 <code>ETag</code> 两个字段放在响应头中返回给浏览器。
<ul>
<li><code>Last-Modified</code>。即资源的最后修改时间，当浏览器第二次向服务器发起请求时，会在请求头中携带 <code>If-Modified-Since</code> 字段，服务器拿到请求头中的 <code>If-Modified-Since</code> 字段后会将字段值与当前服务器中该资源的<code>Last-Modified</code> 字段值比较。若 <code>If-Modified-Since</code> 的值小于服务器中 <code>Last-Modified</code> 的值 ，表明服务器上的资源更新过，服务器会更新 <code>Last-Modified</code> 的值并将新的资源返回给浏览器，响应状态码为 <code>200</code> ；否则返回 <code>304</code> 状态码，告诉浏览器直接使用缓存资源；</li>
<li><code>Etag</code>。即资源最后修改的内容，根据文件内容生成 <code>hash</code> 值。当浏览器第二次向服务器发起请求时，会在请求头中携带 <code>If-None-Match</code> 字段，服务器拿到请求头中的 <code>If-None-Match</code> 字段后会将字段值与当前服务器中该资源的 <code>Etag</code> 相比较，若两值不相等，服务器将更新 <code>Etag</code> 的值并返回新的资源给浏览器，响应状态码为 <code>200</code> ；否则返回 <code>304</code> 状态码，告诉浏览器直接使用缓存资源。当 <code>Etag</code> 与 <code>Last-Modified</code> 同时存在时，先根据 <code>Etag</code> 判断，再根据 <code>Last-Modified</code> 判断返回什么状态码。</li>
</ul>
</li>
<li><code>400 Bad Request</code>。请求参数有误</li>
<li><code>401</code>。身份认证</li>
<li><code>403 Forbidden</code>。服务器禁止访问</li>
<li><code>404 Not Found</code>。服务器未找到相应资源</li>
<li><code>500 Internal Server Error</code>。服务器出错了</li>
<li><code>503 Service Unavailable</code>。服务器繁忙，暂时无法处理响应服务</li>
</ul>
<p>解析到响应数据类型会判断 <code>Content-Type</code> 字段，它会告诉浏览器服务器返回的响应体数据是什么类型，然后浏览器会根据它的值来决定如何显示响应体的内容。如果值是 <code>application/octet-stream</code> 字节流类型，通常会按下载类型来处理；如果值是 <code>text/html</code> 类型则准备渲染进程。</p>
<h2 data-id="heading-7">准备渲染进程</h2>
<p>通常情况下打开一个 Tab 页就要启动一个渲染进程，但这里有个<code>同一站点（same-site）</code>的特例，属于同一站点的Tab页使用同一个渲染进程。同一站点的特性包括：</p>
<ul>
<li>根域名加上协议相同</li>
<li>属于同一个根域名下的所有子域名加上不同的端口号</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 同一站点</span>
<span class="hljs-attr">https</span>:<span class="hljs-comment">//time.geekbang.org</span>
https:<span class="hljs-comment">//www.geekbang.org</span>
https:<span class="hljs-comment">//www.geekbang.org:8080</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">提交文档阶段</h2>
<p>渲染进程准备好后进入提交文档阶段。流程如下：</p>
<ul>
<li>首先当浏览器进程接收到网络进程的响应头数据之后，便向渲染进程发起“提交文档”的消息。</li>
<li>渲染进程接收到“提交文档”的消息后，会和网络进程建立传输数据的“管道”。</li>
<li>等文档数据传输完成之后，渲染进程会返回“确认提交”的消息给浏览器进程。</li>
<li>浏览器进程在收到“确认提交”的消息后，会更新浏览器界面状态，包括了安全状态、地址栏的 URL、前进后退的历史状态，并更新 Web 页面。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/225bc41a996240ed8c3ca8f978d04644~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">构建DOM树</h2>
<p>浏览器无法直接理解和使用 HTML ，所以需要将 HTML 转换为浏览器能够理解的 DOM 树结构。可在浏览器的控制台输入 <code>document</code> 进行查看。具体转换过程如下：</p>
<ul>
<li>转换（字节->字符）：浏览器从磁盘或网络读取 HTML 的原始字节，并根据文件的指定编码（如：UTF-8）把它们转换成各个字符</li>
<li>令牌化（字符->令牌）：浏览器将字符转换为符合 W3C 标准的令牌（如：<code><html></code> <code><body></code>），以及其他尖括号内的字符串。每个令牌都具有特殊含义和一组规则</li>
<li>词法分析（令牌->节点）：发出的令牌转换成定义其属性和规则的“对象”</li>
<li>DOM构建（节点->DOM）：由于 <code>html</code> 标记定义不同标记之间的关系，创建的对象链接在一个树数据结构内，此结构也会捕获原始标记中定义的父项-子项关系： <code>HTML</code> 对象是 <code>body</code> 对象的父项， <code>body</code> 是 <code>paragraph</code> 对象的父项，依此类推。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/452ddfa40d51410a9c65bdb24a41ad57~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
在解析 HTML 文件的过程中，可能中途需要网络进程去下载脚本文件以及样式文件，那么就有一个阻塞 DOM 解析以及渲染的问题，具体可参考 <a href="https://juejin.cn/post/6844903497599549453" target="_blank" title="https://juejin.cn/post/6844903497599549453">原来 CSS 与 JS 是这样阻塞 DOM 解析和渲染的</a> 这篇文章，把结论贴一下：</p>
<ul>
<li>CSS 不会阻塞 DOM 的解析，但会阻塞 DOM 渲染。</li>
<li>JS 阻塞 DOM 解析，但浏览器会"偷看"DOM，预先下载相关资源。</li>
<li>浏览器遇到 <code><script></code> 且没有 <code>defer</code> 或 <code>async</code> 属性的标签时，会触发页面渲染，如果前面 CSS 资源尚未加载完毕，浏览器就会等待它加载完毕再执行脚本。</li>
</ul>
<h2 data-id="heading-10">样式计算</h2>
<p>把 CSS 转换为浏览器能够理解的结构：浏览器无法直接理解 CSS 样式，所以当渲染引擎接收到 CSS 文本时，会执行转换操作，将 CSS 文本转换为 styleSheets 。可在浏览器的控制台输入 <code>document.styleSheets</code> 进行查看。具体转换过程如下：</p>
<ul>
<li>转换样式表中的属性值，使其标准化：比如，在编写代码时使用的是十六进制的颜色，需要转换成 rgb 的格式，李兵老师的课程有说把 em 单位转为 px 单位，bold 转为 700 ，我打开 Chrome 的开发者工具看并没有转，这里跟老师的描述有点出入。</li>
<li>计算出 DOM 树中节点的样式：主要通过继承规则和层叠规则来进行计算。计算完成之后输出每个 DOM 节点的样式，并保存到 ComputedStyle 的结构内。</li>
<li>继承规则：子节点如果没有设置 <code>font-size</code>、<code>color</code>、<code>font-family</code> 几个属性的样式，那么可以继承父节点的样式，如果父节点也没有设置其样式，那么默认使用 UserAgent 样式。注意：只有可继承属性才能继承。</li>
<li>层叠规则：它是一个定义了如何合并来自多个源的属性值的算法。</li>
</ul>
<h2 data-id="heading-11">布局阶段</h2>
<p>计算出 DOM 树中可见元素的几何位置。具体过程如下：</p>
<ul>
<li>创建布局树：遍历 DOM 树中所有可见节点，生成一棵只包含可见节点的布局树。不可见的节点会被忽略，不会出现在布局树上，不可见节点包括：1. 不会渲染输出的节点（script/link/meta/head），2. 通过 css 隐藏的节点（display: none）会被忽略掉。</li>
<li>布局计算：计算布局树节点的几何位置，并将计算出的信息保存到布局树中。</li>
</ul>
<h2 data-id="heading-12">分层</h2>
<p>由于页面中有很多复杂的效果，如一些复杂的 3D 变换、页面滚动，或者使用 z-index 做 z 轴排序等，为了更加方便地实现这些效果，渲染引擎还需要为特定的节点生成专用的图层，并生成一棵对应的图层树（LayerTree）。通常情况下，并不是布局树中每个节点都包含一个图层，如果一个节点没有对应的层，那么这个节点就从属于父节点的图层。这些图层经过合成变为最终的页面。渲染引擎为特定节点创建单独的图层的条件包括：</p>
<ul>
<li>拥有层叠上下文属性的元素会被提升为单独的一层。以下是层叠上下文属性示意图：</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f62b8df095f4dd180147a18214d0c3a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>需要剪裁（clip）的地方也会被创建为图层。当一个元素设置了固定宽高而里面的内容超出了这个元素，那么超出的部分会被剪裁，渲染引擎会创建一个单独的图层来存放被剪裁的内容</li>
</ul>
<h2 data-id="heading-13">图层绘制</h2>
<p>构建完图层树之后，渲染引擎会对图层树中的每个图层进行绘制。渲染引擎会把一个图层的绘制拆分成很多小的绘制指令，然后再把这些指令按照顺序组成一个待绘制列表。</p>
<h2 data-id="heading-14">栅格化（raster）</h2>
<p>绘制列表准备好之后，主线程会把绘制列表提交给合成线程，由合成线程来完成具体的绘制操作。先了解一下什么是视口（viewport）？视口就是屏幕上页面的可见区域。随着业务的复杂性，某些情况下图层可能会很长，而用户通过视口只能看见页面的一小部分，如果一次性绘制图层会产生很大的开销，所以合成线程会将图层划分为图块（tile），图块大小通常是 <code>256x256</code> 或者 <code>512x512</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c4cb92fbca6496284521704a1810584~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
合成线程会按照视口附近的图块来优先生成位图，实际生成位图的操作是由栅格化来执行的。所谓栅格化，是指将图块转换为位图。栅格化过程都会使用 GPU 来加速生成，使用 GPU 生成位图的过程叫快速栅格化，生成的位图被保存在 GPU 内存中。</p>
<h2 data-id="heading-15">合成和显示</h2>
<p>所有的图层进行光栅化之后，合成线程就会生成一个绘制图块的 <code>DrawQuad</code> 命令，合成线程将这个命令发给浏览器进程，由浏览器进程中的 <code>viz</code> 组件接收 <code>DrawQuad</code> 命令，它会根据命令将页面内容绘制到内存中，最后将内存中的内容显示到屏幕上。</p>
<h2 data-id="heading-16">参考文章</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftime.geekbang.org%2Fcolumn%2Fintro%2F216" target="_blank" rel="nofollow noopener noreferrer" title="https://time.geekbang.org/column/intro/216" ref="nofollow noopener noreferrer">浏览器工作原理与实践</a></li>
<li><a href="https://juejin.cn/post/6844903764566999054#heading-12" target="_blank" title="https://juejin.cn/post/6844903764566999054#heading-12">实践这一次,彻底搞懂浏览器缓存机制</a></li>
</ul></div>  
</div>
            