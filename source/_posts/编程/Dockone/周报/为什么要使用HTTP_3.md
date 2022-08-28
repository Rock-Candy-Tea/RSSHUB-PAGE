
---
title: '为什么要使用HTTP_3'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220815/33bd84c310eb931981b04beef3211491.png'
author: Dockone
comments: false
date: 2022-08-28 07:08:20
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220815/33bd84c310eb931981b04beef3211491.png'
---

<div>   
<br>超文本传输协议的第三个主要版本，即 <strong>HTTP/3</strong>， 于 2022 年 6 月 6 日被采纳为 <a href="https://www.rfc-editor.org/info/rfc9114">IETF</a> （互联网工程任务组）标准。可能有人也会像我一样，在得知此<a href="https://www.theregister.com/2022/06/07/http3_rfc_9114_published/">消息</a>后会感到非常高兴，当然，大家可能对此也不太关心，毕竟现在的网络运行良好，没必要关注新的变化。但是，如果你也好奇发生这种变化的原因，接下来我们将简短地介绍背后的历史，并讨论为何应该采用 HTTP/3。<br>
<br><blockquote><br>HTTP/3 是超文本传输协议（HTTP）的第三个版本，之前以 HTTP-over-QUIC 被大家熟知。QUIC 最初由谷歌开发，是 HTTP/2 的下一代协议。谷歌和 Facebook 等公司已经在使用 QUIC 来加快网络速度。</blockquote><h3>HTTP简史</h3>过去，有两种互联网协议可以选择。甚至在 Web 出现之前，我们仍然需要通过网络将信息包（或数据报）从一台机器发送到另一台机器。对于游戏开发者来说，一个比较重要的协议是 <strong>UDP</strong>（用户数据报协议），遵循快速、即发即弃的标准：在网络上发出一个数据包，数据包有可能会被接收，也可能会丢失。举一个比较形象的例子，你在游戏中打出的子弹，通过网络传输，显示在目标玩家的机器上，即使个别子弹在传输过程中丢失，也不会对整个游戏产生过多影响。<br>
<br>但是对于像 Web 这样更稳定的系统，底层协议使用 <strong>TCP 协议</strong>才是正确之选。这是一个更正式的系统，它保证了数据包传递的可靠性和顺序性。首先创建可靠的连接，然后基于连接传输信息流。在 Web 出现之前，我记得连接到互联网需要使用 Trumpet Winsock ——被称作为“TCP/IP 堆栈”。我们曾在一家历史悠久的公司中，使用 Trumpet Winsock 与 <a href="https://en.wikipedia.org/wiki/CIX_(website)">CIX</a>（英国在线会议系统）交互。如今，CIX 已是一个韩国男团的名字。<br>
<br>最终，基于 TCP/IP 编写的万维网和 HTTP 接管了互联网，成为主流。另外， TLS（传输层安全）提供了加密能力，并在 HTTP/2 就绪时成为事实上的安全标准。<br>
<br>PC 之间的连接通常是有线的，任何损失都是由于旧铜线上的噪音造成的，TCP 则非常适合收集偶尔出错的数据包。随着网络的发展，UDP 的使用越来越少了。<br>
<h3>QUIC 初探</h3>今天的互联网环境已大不相同，家中的 PC 有很好的光纤连接和良好的线路，但大多数用户通过手机或笔记本电脑使用互联网。当使用网络的地点发生切换时，网络信号可能会受到墙体的阻挡或反弹，导致网络连接通常会被切断并重连。这恰恰是 TCP 不喜欢的场景——如果没有正式的初始化连接和良好的握手，TCP 内心真的不想进行通信。事实上，TCP 对最后一个杂散数据包（stray packet）的严格统计和等待意味着用户必须等待网页加载、新应用程序下载，或者超时后重新建立连接。<br>
<br>因此，通过利用 UDP 的非正式性，并允许网络可以动态地使用一些智能的能力，新的 QUIC（快速 UDP 互联网连接）形式得到了更多的关注。<br>
<br>虽然我们不希望在网络本身中看到太多智能化的东西，但如今我们对自动决策机制已越来越适应。QUIC 可以理解一个站点是由多个文件组成的，它不会因为一个文件没有完成加载而破坏整个连接。<br>
<br>QUIC 遵循的另一个趋势是内置安全性。而之前加密是可选的（即 HTTP 或 HTTPS）QUIC 始终是加密的。尽管开销可能会变大，但当下每个站点都应该加密。这不仅仅是为了确保中间人看不到你点的是什么类型的橙汁，更要确保你是在与真正的橙汁供应商进行交易。<br>
<br>虽然协议格式一直在改进，但随着时间的推移 QUIC 也在真正解决不同的问题。<br>
<h3>活跃度</h3>那么 QUIC 现在发展的如何呢？ 可以从三个方面来考虑：浏览器、云基础设施和用户代码。<br>
<br>首先是浏览器支持情况。下面的表格来自 <a href="https://caniuse.com/">Can I Use</a>：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220815/33bd84c310eb931981b04beef3211491.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220815/33bd84c310eb931981b04beef3211491.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
显然，谷歌是非常热衷推广 QUIC 的——从 v87（2020 年末）开始的 Chrome 版本已经能够使用 HTTP/3 协议。不出意料，鉴于苹果过往在浏览器开发方面的<a href="https://thenewstack.io/apples-browser-engine-ban-is-holding-back-web-app-innovation/">表现</a>，Safari 目前是落后的。<br>
<br>可以使用下面的网站来检查浏览器是否符合 HTTP/3（可能需要重新加载）：<br>
<ul><li><a href="https://cloudflare-quic.com/">cloudflare-quic.com</a></li><li><a href="https://quic.nginx.org/">quic.nginx.org</a></li><li><<a href="https://http3.is/" rel="nofollow" target="_blank">https://http3.is</a>/></li></ul><br>
<br>那对于现有的网站来说呢？如果需要测试现有站点是否支持 HTTP/3，可以使用 <a href="https://geekflare.com/tools/http3-test" rel="nofollow" target="_blank">https://geekflare.com/tools/http3-test</a> 进行测试。好消息是，如果你的网站在 HTTP/2 下运行良好，那么它在 HTTP/3 下也会运行良好，甚至会表现更好。<br>
<h3>谁在推广 HTTP/3?</h3>那么，现在谁在推广 HTTP/3 呢？ 毫无疑问，谷歌是其中之一。还有 CDN 供应商，例如 Cloudflare 和 Fastly，他们吃饭的家伙什儿就是网络响应速度。因此，实现 HTTP/3 最简单的方法是通过 CDN，这也是一项让移动用户受益良多的变化。<br>
<br>目前确实存在使用 QUIC 构建的服务器（例如 Litespeed），但采用率参差不齐。许多服务器依赖于第三方库，复用现有的、经过验证的成果则不再奏效。现有的服务器软件，如 Node.js、NGINX 和 Apache，开始采用新的内部结构时就失去了用户体验优势。相反，如果是新的服务器软件，由于还未经过充分验证和使用，可能更容易采用新的协议。使用 Web 服务器的关键在于它是可靠的、经过良好测试和维护的。<br>
<h3>适配 HTTP/3</h3>在正常情况下，我会深入研究一些代码——但我觉得现阶段这样做有点为时过早。有很多项目可能都在定期变化，所以目前只需要浅尝一下即可。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220815/3f3bb8c2e14d9fdbbdf56cab8f2587bf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220815/3f3bb8c2e14d9fdbbdf56cab8f2587bf.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通过一些简单的项目示例（例如，一个简单的服务器和一个简单的客户端），我们可以剖析一下不同的层级。<br>
<br>首先是连接。更高级别的通道最初会在两个端点之间建立。然后创建连接标识符，连接一旦建立，如果下层的协议发生变化（例如，电话切换 wi-fi），连接仍然存在，以避免重新开始协商。<br>
<br>连接会开启多个携带各自数据类型的 Stream 流，Stream 流之间相互独立，互不干扰。<br>
<br>下面仍然是数据包。每个数据包，就像一封地址明了的信件，包含连接和加密信息。信封里面是数据帧。这些就代表正在传输的实际数据。<br>
<br>正如我之前所说，进步实际上只是反映了不断变化的使用模式。当下，我们重视安全性和速度，因为我们不再将网络视为不可靠的魔法——因此用它来管理个人事务。HTTP/3 将有助于解决这些问题。可能 Web3 和新兴的元宇宙世界会更加棘手，也许这些领域的新想法未来会为 HTTP/4 的发展做出贡献。<br>
<br><strong>原文链接：<a href="https://thenewstack.io/http-3-is-now-a-standard-why-use-it-and-how-to-get-started/">HTTP/3 Is Now a Standard: Why Use It and How to Get Started</a>（翻译：李加庆）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            