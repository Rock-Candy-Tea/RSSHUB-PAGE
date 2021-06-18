
---
title: 'Chrome浏览器在服务端出现断网情况下提出RESET Flag从而发起重复请求'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b84c05fdbc294af6a9c1237a2e245138~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 22:04:24 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b84c05fdbc294af6a9c1237a2e245138~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>公司产品在上线运行中，有使用人员反映发起了一笔账务请求，记账100元，前端正常交易完成后，后台记了两笔100元的账务，引发了很危险的短款账务问题。</p>
<p>经多方核实，确认现在确实存在客户端通讯重复发送了两次，且仅接受第二次的返回信息导致了此问题发生。</p>
<p>凡事先从自省入手，我们先不去吐槽为啥服务端没有做好幂等性和防重功能，先分析下到底客户端是不是真的有问题，因此产生了以下的分析排查过程。</p>
<h3 data-id="heading-1">问题分析</h3>
<p>客户端采用CEF框架，基于Chromium 76版本；发起请求基于axios框架，前端框架采用Vue.js 2.0技术。</p>
<p>1、总结整个网络部署架构图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b84c05fdbc294af6a9c1237a2e245138~tplv-k3u1fbpfcp-watermark.image" alt="Untitled Diagram (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p align="center">图1、网络部署架构图</p>
<p>2、根据上图的网络架构，依次从后到前拿到生产日志，首先分析两次请求的服务端日志是否完全一致，结论为两次服务端日志比对完全一致。</p>
<p>3、观察业务网关日志，发现两笔请求间隔19s，无任何其他信息。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0823f7d274df4a6d80cd83bc90aa2517~tplv-k3u1fbpfcp-watermark.image" alt="afa日志.jpg" loading="lazy" referrerpolicy="no-referrer">
​</p><p align="center">图2、业务网关日志截图</p><p></p>
<p>4、观察反向代理服务器日志，发现两笔请求之间都存在websocket尝试重新握手重连的情况：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a797d9aa84a14eaa802d883209b12d32~tplv-k3u1fbpfcp-watermark.image" alt="反向代理日志.jpg" loading="lazy" referrerpolicy="no-referrer">
​</p><p align="center">图3、反向代理服务器日志截图</p><p></p>
<p>该日志反映出上下两笔相同的POST请求，中间出现了网络断开的情况，因此导致了websocket进行了重连。</p>
<p>5、观察客户端日志，的确出现了网络断开情况，websocket尝试重连，并在后续重连成功。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d10a21fdb2c4223b78eee281a77b976~tplv-k3u1fbpfcp-watermark.image" alt="客户端日志.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p align="center">图4、客户端日志截图</p>
<p>6、从上图此时排查客户端日志，发现客户端日志在发起通讯请求日志后，未接收到任何http异常日志记录，仅有websocket异常日志记录，从客户端视角看，只是发了一次请求，过了19s后收到200响应状态码。</p>
<p><strong>综上问题分析：</strong>
我们发现客户端应用层只发起了一次http请求，此时网络出现波动，反向代理服务器记录客户端发起了两笔http请求，中间夹杂着一次websocket重连，服务端也是收到两笔请求，因此下一步需要排查客户端与反向代理服务器之前到底因为什么原因导致了问题出现。</p>
<h3 data-id="heading-2">场景重现</h3>
<p>1、到底在<strong>客户端与反向代理服务器之间</strong>是谁进行了重发，导致了这次问题呢</p>
<p>2、首选怀疑的是nginx的重发机制，可以看到nginx在出现异常时，会重新请求后台服务。
<a href="https://www.cnblogs.com/yxy-linux/p/8744837.html" target="_blank" rel="nofollow noopener noreferrer">nginx 重发机制 - yxy_linux - 博客园 (cnblogs.com)</a>。但根据一开始说明的架构，对ngnix参数进行修改，测试时确实出现了重发，但网关日志中记录了一条，<strong>与本次现象不符</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b84c05fdbc294af6a9c1237a2e245138~tplv-k3u1fbpfcp-watermark.image" alt="Untitled Diagram (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3、再次怀疑的是axios重发，在github上也见到相关的帖子，有人反馈过使用axios导致重复提交问题，不过由于缺少重现场景，问题关闭</p>
<p><a href="https://github.com/axios/axios/issues/2825" target="_blank" rel="nofollow noopener noreferrer">Axios send the same request twice and ignore the first response, only receives the second response. · Issue #2825 · axios/axios · GitHub</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80023a29dcc74bae8834f58282f5f570~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210607150558614" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查看axios源码发现，axios底层发送也是使用XMLHttpRequest实现，从axios过程来看，不存在重发代码处理</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3322d7b44654421a011924e705dc165~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210607150737505" loading="lazy" referrerpolicy="no-referrer"></p>
<p>4、随着上面nginx与axios机制排除后，把目光转向了Http协议，网上搜索发现http对重发有处理，可以看到网页说明跟这次现象很像，都是中途出现了<strong>断网</strong>。<a href="https://segmentfault.com/a/1190000005894812" target="_blank" rel="nofollow noopener noreferrer">HTTP请求重发 - SegmentFault 思否</a></p>
<p>根据上述场景，对问题复现。</p>
<p>5、<strong>断掉客户端网络</strong>，尝试重现。本地两台PC机，一台模拟客户端，一台模拟服务端，两台PC机通过路由器相连，客户端使用axios直接发post请求，服务端接收请求会睡眠几秒模拟处理业务流程再返回，使用wireshark抓包观察客户端服务端发包情况，尝试问题复现。</p>
<p>客户端点击按钮发送post请求，立即拔开网线，等待几秒后把网线插回，客户端立刻收到了Disconnect异常，生产环境未出现此类异常，因此此<strong>场景不正确</strong>。</p>
<div align="center"> 
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5661f328a8f4485896e1eb7598fcb90c~tplv-k3u1fbpfcp-watermark.image" alt="Untitled Diagram (2).png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2f3452492e54ae6a8238ad16c3f0ebc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p align="center">图5、浏览器测试截图</p>
</div>
<p>6、<strong>断掉服务端网络</strong>，尝试重现。客户端点击按钮发送post请求，服务端收到请求后立即拔网线，等待几秒后把网线插回，观察客户端Network情况及抓包数据：</p>
<div align="center"> 
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5147dedc30e1486dba51ce1a55cb0f27~tplv-k3u1fbpfcp-watermark.image" alt="Untitled Diagram (3).png" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>客户端Network显示发送了两次请求，一次为OPTION请求，页面显示为Preflight请求，一次为正常POST请求。几毫秒后Preflight的OPTION请求返回，POST请求一直处于pending状态。（图6）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/376504cb02d149599611011894958543~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210607145004468" loading="lazy" referrerpolicy="no-referrer"></p>
<p align="center">图6、浏览器测试截图</p>
<p>之后观察wireshark日志，发现在拔开服务端网线，等待一段时间，再插回网线的一小段时间后，客户端会再次发起一次请求，且此时客户端无感知，Network一直显示pending状态，之后服务端处理完第二次请求后返回给客户端，客户端接收到服务端正常响应报文，状态码200。该场景与生产完全一致，复现完成，<strong>100%可以复现</strong>。（图7、8）</p>
<div align="center"> 
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/777325d7392947b0989cf28498344925~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210607145133194" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f440633cbb4f7488921751d492e540~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210604142557725" loading="lazy" referrerpolicy="no-referrer"></p>
<p align="center">图7、Wireshark测试截图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b905354600e149989f78ae3d12f1ffd6~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210607145232776" loading="lazy" referrerpolicy="no-referrer"></p>
<p align="center">图8、浏览器测试截图</p>
</div>
<h3 data-id="heading-3">问题结论：</h3>
<p>1、综上排查分析，是客户端浏览器发起了HTTP1.1协议的请求，在服务端的网络出现异常断开的情况下，给浏览器发送了一个RESET指令，浏览器自发地发起了第二笔请求，且对应用层无感知。下一步就需要思考为什么浏览器会自发地发起了第二笔请求，且对应用层无感知，导致应用层视角看是发起了一笔请求，接收到了第二笔的响应结果。</p>
<p>2、首先，平台使用的76版本的Chromium内核浏览器默认现在都使用了HTTP1.1协议，其中的连接方式为：Connection:Keep-Alive,此种连接方式可以改善这种状态，即在一次TCP连接中只进行一次握手阶段（如图7wireshark所示），后续可以持续发送多份数据而不会断开连接。通过使用keep-alive机制，可以减少tcp连接建立次数，也意味着可以减少TIME_WAIT状态连接，以此提高性能和提高httpd服务器的吞吐率(更少的tcp连接意味着更少的系统内核调用,socket的accept()和close()调用)。那么，是否可以通过关闭KeepAlive解决该问题？</p>
<p>3、Connection:Keep-Alive属于浏览器<a href="https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_header_name" target="_blank" rel="nofollow noopener noreferrer">不允许修改协议头</a>，那么除了Keep-Alive以外，还有哪些情况会导致重复链接呢？通过观察wireshark和浏览器的Network，发现正常的POST请求前会发送一次OPTIONS请求，该请求的目的是：浏览器会首先使用 OPTIONS 方法发起一个预请求，判断接口是否能够正常通讯，如果不能就不会发送真正的请求过来，如果测试通讯正常，则开始真正的请求。因此，会不会是OPTIONS请求产生了一些影响？</p>
<p>4、从这一角度出发，我们先思考和查证了一下，什么Content-Type类型会导致发送OPTIONS请求。通过写一个简单的XmlHttpRequest发送POST请求给服务端，wireshark抓包发现，简单的XmlHttpRequest在服务端网络断开的情况下，重连后也不会发送第二笔请求，只有axios才会发送第二笔，那么需要对两种情况的抓包分析报文头进行比对。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc8f91a9e0a3471f86a388e55c53614a~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210607145334642" loading="lazy" referrerpolicy="no-referrer"></p>
<p align="center">图9、Wireshark测试截图</p>
<p>5、通过比对两种请求的发包情况（图9），XmlHttpRequest发送的content-type为：text/plain，而axios发送的content-type为：application/json。那么下一步，我们手动将axios默认的application/json的content-type改成text/plain，发现再次断开服务端网络重连后，浏览器不会再次自动发送第二笔请求了（图10、图11）。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f1b2f7030174d1788bfb4a7844671eb~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210607145444390" loading="lazy" referrerpolicy="no-referrer"></p>
<p align="center">图10、Wireshark测试截图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d96499064294792a0e1d018f02c78a6~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210607145509716" loading="lazy" referrerpolicy="no-referrer"></p>
<p align="center">图11、浏览器测试截图</p>
<p>6、因此，导致此次反向代理服务器之后整个链路收到两笔请求的最根本原因，就是<strong>content-type:application/json内容类型，浏览器判定会在服务端网络恢复后自动重发请求，且对应用层无感知。</strong></p>
<h3 data-id="heading-4">解决思路：</h3>
<p>那么content-type到底有哪些种类？是否有一些定义和归类？通过查找发现：HTTP请求分为简单请求与复杂请求，简单请求不会发送OPTIONS预请求，简单请求需要满足以下条件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89483dcea32844f2823f6687b1b63e8e~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210604164331872" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，简单请求的content-type一般为：text/plain，multipart/form-data，application/x-www-form-urlencoded。</p>
<p>经过我们多次使用各种content-type类型与不同种类浏览器（chrome与firefox）验证，总结了几种情况如下：</p>






























<table><thead><tr><th>Content-type</th><th>chrome是否会默认重发第二次</th><th>firefox是否会默认重发第二次</th></tr></thead><tbody><tr><td>application/json</td><td>会</td><td>会</td></tr><tr><td>text/plain</td><td>否</td><td>会</td></tr><tr><td>application/x-www-form-urlencoded。</td><td>否</td><td>否</td></tr><tr><td>multipart/form-data</td><td>未测</td><td>未测</td></tr></tbody></table>
<p>最终得出结论，客户端发送http请求，最合适应该为application/x-www-form-urlencoded。</p>
<h3 data-id="heading-5">最终建议解决问题方式：</h3>
<p>将客户端axios的content-type，手动改为application/x-www-form-urlencoded，由于该content-type为form-data，因此需要使用qs对body进行序列化改造。</p>
<h3 data-id="heading-6">遗留问题</h3>
<p>底层是什么原因，导致浏览器重发，具体哪些会重发，哪些不会？</p>
<h3 data-id="heading-7">参考材料：</h3>
<p><a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17" target="_blank" rel="nofollow noopener noreferrer">www.w3.org/Protocols/r…</a>
<a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Connection" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a>
<a href="https://dev.to/p0oker/why-is-my-browser-sending-an-options-http-request-instead-of-post-5621" target="_blank" rel="nofollow noopener noreferrer">dev.to/p0oker/why-…</a>
<a href="https://dev.to/effingkay/cors-preflighted-requests--options-method-3024" target="_blank" rel="nofollow noopener noreferrer">dev.to/effingkay/c…</a>
<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a>
<a href="https://segmentfault.com/a/1190000005894812" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000000…</a>
<a href="https://blog.csdn.net/edward30/article/details/8661105" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/edward30/ar…</a></p></div>  
</div>
            