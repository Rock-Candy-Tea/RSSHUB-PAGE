
---
title: '一套亿级用户的IM架构技术干货(下篇)：可靠性、有序性、弱网优化等'
categories: 
 - 编程
 - 掘金
 - — 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/894527d66c5143c9b712331c06baf438~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 22 Mar 2021 00:23:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/894527d66c5143c9b712331c06baf438~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文内容和编写思路是基于邓昀泽的“大规模并发IM服务架构设计”、“IM的弱网场景优化”两文的提纲进行的，感谢邓昀泽的无私分享。</p>
<h1 data-id="heading-0">1、引言</h1>
<p>接上篇《<a href="http://www.52im.net/thread-3393-1-1.html" target="_blank" rel="nofollow noopener noreferrer">一套亿级用户的IM架构技术干货(上篇)：整体架构、服务拆分等</a>》，本文主要聚焦这套亿级用户的IM架构的一些比较细节但很重要的热门问题上，比如：消息可靠性、消息有序性、数据安全性、移动端弱网问题等。</p>
<p>以上这些热门IM问题每个话题其实都可以单独成文，但限于文章篇幅，本文不会逐个问题详细深入地探讨，主要以抛砖引玉的方式引导阅读者理解问题的关键，并针对问题提供专项研究文章链接，方便有选择性的深入学习。希望本文能给你的IM开发带来一些益处。</p>
<h1 data-id="heading-1">2、系列文章</h1>
<p>为了更好以进行内容呈现，本文拆分两了上下两篇。</p>
<p><strong>本文是2篇文章中的第2篇：</strong></p>
<blockquote>
<p>《<a href="http://www.52im.net/thread-3393-1-1.html" target="_blank" rel="nofollow noopener noreferrer">一套亿级用户的IM架构技术干货(上篇)：整体架构、服务拆分等</a>》</p>
<p>《<a href="http://www.52im.net/thread-3445-1-1.html" target="_blank" rel="nofollow noopener noreferrer">一套亿级用户的IM架构技术干货(下篇)：可靠性、有序性、弱网优化等</a>》（本文）</p>
</blockquote>
<p>本篇主要聚焦这套亿级用户的IM架构的一些比较细节但很重要的热门问题上。</p>
<h1 data-id="heading-2">3、消息可靠性问题</h1>
<p>消息的可靠性是IM系统的典型技术指标，对于用户来说，消息能不能被可靠送达（不丢消息），是使用这套IM的信任前提。</p>
<p>换句话说，如果这套IM系统不能保证不丢消息，那相当于发送的每一条消息都有被丢失的概率，对于用户而言，一定会不会“放心”地使用它，即“不信任”这套IM。</p>
<p>从产品经理的角度来说，有这样的技术障碍存在，再怎么费力的推广，最终用户都会很快流失。所以一套IM如果不能保证消息的可靠性，那问题是很严重的。</p>
<p>**PS：**如果你对IM消息可靠性的问题还没有一个直观的映象的话，通过《<a href="http://www.52im.net/thread-3182-1-1.html" target="_blank" rel="nofollow noopener noreferrer">零基础IM开发入门(三)：什么是IM系统的可靠性？</a>》这篇文章可以通俗易懂的理解它。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/894527d66c5143c9b712331c06baf438~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>如上图所示，消息可靠性主要依赖2个逻辑来保障：</strong></p>
<ul>
<li>1）上行消息可靠性；</li>
<li>2）下行消息可靠性。</li>
</ul>
<p><strong>1）针对上行消息的可靠性，可以这样的思路来处理：</strong></p>
<p>用户发送一个消息（假设协议叫PIMSendReq），用户要给这个消息设定一个本地ID，然后等待服务器操作完成给发送者一个PIMSendAck（本地ID一致），告诉用户发送成功了。</p>
<p>如果等待一段时间，没收到这个ACK，说明用户发送不成功，客户端SDK要做重试操作。</p>
<p><strong>2）针对下行消息的可靠性，可以这样的思路来处理：</strong></p>
<p>服务收到了用户A的消息，要把这个消息推送给B、C、D 3个人。假设B临时掉线了，那么在线推送很可能会失败。</p>
<p>**因此确保下行可靠性的核心是：**在做推送前要把这个推送请求缓存起来。</p>
<p>这个缓存由存储系统来保证，MsgWriter要维护一个（离线消息列表），用户的一条消息，要同时写入B、C、D的离线消息列表，B、C、D收到这个消息以后，要给存储系统一个ACK，然后存储系统把消息ID从离线消息列表里拿掉。</p>
<p>针对消息的可靠性问题，具体的解决思路还可以从另一个维度来考虑：即实时消息的可靠性和离线消息的可靠性。</p>
<p><strong>有兴趣可以深入读一读这两篇：</strong></p>
<blockquote>
<p>《<a href="http://www.52im.net/thread-294-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息送达保证机制实现(一)：保证在线实时消息的可靠投递</a>》</p>
<p>《<a href="http://www.52im.net/thread-594-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息送达保证机制实现(二)：保证离线消息的可靠投递</a>》</p>
</blockquote>
<p>而对于离线消息的可靠性来说，单聊和群聊又有很大区别，有关群聊的离线消息可靠投递问题，可以深入读一读《<a href="http://www.52im.net/thread-3069-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM开发干货分享：如何优雅的实现大量离线消息的可靠投递</a>》。</p>
<h1 data-id="heading-3">4、消息有序性问题</h1>
<p>消息的有序性问题是分布式IM系统中的另一个技术“硬骨头”。</p>
<p>因为是分布式系统，客户端和服务器的时钟可能是不同步的。如果简单依赖某一方的时钟，就会出现大量的消息乱序。</p>
<p>比如只依赖客户端的时钟，A比B时间晚30分钟。所有A给B发消息，然后B给A回复。</p>
<p><strong>发送顺序是：</strong></p>
<blockquote>
<p>客户端A：“XXX”</p>
<p>客户端B：“YYY”</p>
</blockquote>
<p><strong>接收方的排序就会变成：</strong></p>
<blockquote>
<p>客户端B：“YYY”</p>
<p>客户端A：“XXX”</p>
</blockquote>
<p>因为A的时间晚３０分钟，所有A的消息都会排在后面。</p>
<p>如果只依赖服务器的时钟，也会出现类似的问题，因为2个服务器时间可能也不一致。虽然客户端A和客户端B时钟一致，但是A的消息由服务器S1处理，B的消息由服务器S2处理，也会导致同样消息乱序。</p>
<p>为了解决这种问题，我的思路是通过可以做这样一系列的操作来实现。</p>
<p><strong>1）服务器时间对齐：</strong></p>
<p>这部分就是后端运维的锅了，由系统管理员来尽量保障，没有别的招儿。</p>
<p><strong>2）客户端通过时间调校对齐服务器时间：</strong></p>
<p>比如：客户端登录以后，拿客户端时间和服务器时间做差值计算，发送消息的时候考虑这部分差值。</p>
<p>在我的im架构里，这个能把时间对齐到100ms这个级，差值再小的话就很困难了，因为协议在客户端和服务器之间传递速度RTT也是不稳定的（网络传输存在不可控的延迟风险嘛）。</p>
<p><strong>3）消息同时带上本地时间和服务器时间：</strong></p>
<p>具体可以这样的处理：排序的时候，对于同一个人的消息，按照消息本地时间来排；对于不同人的消息，按照服务器时间来排，这是插值排序算法。</p>
<p>**PS：**关于消息有序性的问题，显然也不是上面这三两句话能讲的清楚，如果你想更通俗一理解它，可以读一读《<a href="http://www.52im.net/thread-3189-1-1.html" target="_blank" rel="nofollow noopener noreferrer">零基础IM开发入门(四)：什么是IM系统的消息时序一致性？</a>》。</p>
<p>**另外：**从技术实践可行性的角度来说，《<a href="http://www.52im.net/thread-866-1-1.html" target="_blank" rel="nofollow noopener noreferrer">一个低成本确保IM消息时序的方法探讨</a>》、《<a href="http://www.52im.net/thread-714-1-1.html" target="_blank" rel="nofollow noopener noreferrer">如何保证IM实时消息的“时序性”与“一致性”？</a>》这两篇中的思路可以借鉴一下。</p>
<p>实际上，消息的排序问题，还可以从消息ID的角度去处理（也就是通过算法让消息ID产生顺序性，从而根据消息ID就能达到消息排序的目的）。</p>
<p><strong>有关顺序的消息ID算法问题，这两篇非常值得借鉴：</strong>《<a href="http://www.52im.net/thread-1998-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息ID技术专题(一)：微信的海量IM聊天消息序列号生成实践（算法原理篇）</a>》、《<a href="http://www.52im.net/thread-2747-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息ID技术专题(三)：解密融云IM产品的聊天消息ID生成策略</a>》，我就不废话了。</p>
<h1 data-id="heading-4">5、消息已读同步问题</h1>
<p><strong>消息的已读未读功能，如下图所示：</strong></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c00adc3ddaf49be9a8a5debe46585b8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上图就是钉钉中的已读未读消息。这在企业IM场景下非常有用（因为做领导的都喜欢，你懂的）。</p>
<p>已读未读功能，对于一对一的单聊消息来说，还比较好理解：就是多加一条对应的回执息（当用户阅读这条消息时发回）。</p>
<p>但对于群聊这说，这一条消息有多少人已读、多少人未读，想实现这个效果，那就真的有点麻烦了。对于群聊的已读未读功能实现逻辑，这里就不展开了，有兴趣可以读一下这篇《<a href="http://www.52im.net/thread-1611-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM群聊消息的已读回执功能该怎么实现？</a>》。</p>
<p>回归到本节的主题“已读同步”的问题，这显示难度又进一级，因为已读未读回执不只是针对“账号”，现在还要细分到“同一账号在不同端登陆”的情况，对于已读回执的同步逻辑来说，这就有点复杂化了。</p>
<p>在这里，根据我这边IM架构的实践经验，提供一些思路。</p>
<p>**具体来说就是：**用户可能有多个设备登录同一个账户（比如：Web PC和移动端同时登陆），这种情况下的已读未读功能，就需要来实现已读同步，否则在设备1看过的消息，设备2看到依然是未读消息，从产品的角度来说，这就影响用户体验了。</p>
<p><strong>对于我的im架构来说，已读同步主要依赖2个逻辑来保证：</strong></p>
<ul>
<li>1）同步状态维护，为用户的每一个Session，维护一个时间戳，保存最后的读消息时间；</li>
<li>2）如果用户打开了某个Session，且用户有多个设备在线，发送一条PIMSyncRead消息，通知其它设备。</li>
</ul>
<h1 data-id="heading-5">6、数据安全问题</h1>
<h3 data-id="heading-6">6.1 基础</h3>
<p>IM系统架构中的数据安全比一般系统要复杂一些，从通信的角度来说，它涉及到socket长连接通信的安全性和http短连接的两重安全性。而随着IM在移动端的流行，又要在安全性、性能、数据流量、用户体验这几个维度上做权衡，所以想要实现一套完善的IM安全架构，要面临的挑战是很多的。</p>
<p>IM系统架构中，所谓的数据安全，主要是通信安全和内容安全。</p>
<h3 data-id="heading-7">6.2 通信安全</h3>
<p>所谓的通信安全，这就要理解IM通信的服务组成。</p>
<p><strong>目前来说，一个典型的im系统，主要由两种通信服务组成：</strong></p>
<ul>
<li>1）socket长连接服务：技术上也就是多数人耳熟能详的网络通信这一块，再细化一点也就是tcp、udp协议这一块；</li>
<li>2）http短连接服务：也就是最常用的http rest接口那些。</li>
</ul>
<p>对于提升长连接的安全性思路，可以深入阅读《<a href="http://www.52im.net/thread-970-1-1.html" target="_blank" rel="nofollow noopener noreferrer">通俗易懂：一篇掌握即时通讯的消息传输安全原理</a>》。另外，微信团队分享的《<a href="http://www.52im.net/thread-310-1-1.html" target="_blank" rel="nofollow noopener noreferrer">微信新一代通信安全解决方案：基于TLS1.3的MMTLS详解</a>》一文，也非常有参考意义。</p>
<p>如果是通信安全级别更高的场景，可以参考《<a href="http://www.52im.net/thread-217-1-1.html" target="_blank" rel="nofollow noopener noreferrer">即时通讯安全篇（二）：探讨组合加密算法在IM中的应用</a>》，文中关于组合加密算法的使用思路非常不错。</p>
<p>至于短连接安全性，大家就很熟悉了，开启https多数情况下就够用了。如果对于https不甚了解，可以从这几篇开始：《<a href="http://www.52im.net/thread-1574-1-1.html" target="_blank" rel="nofollow noopener noreferrer">一文读懂Https的安全性原理、数字证书、单项认证、双项认证等</a>》、《<a href="http://www.52im.net/thread-1890-1-1.html" target="_blank" rel="nofollow noopener noreferrer">即时通讯安全篇（七）：如果这样来理解HTTPS，一篇就够了</a>》。</p>
<h3 data-id="heading-8">6.3 内容安全</h3>
<p>这个可能不太好理解，上面既然实现了通信安全，那为什么还要纠结“内容安全”？</p>
<p>我们了解一下所谓的密码学三大作用：加密（ Encryption）、认证（Authentication），鉴定（Identification） 。</p>
<p><strong>详细来说就是：</strong></p>
<blockquote>
<p>加密：防止坏人获取你的数据。</p>
<p>认证：防止坏人修改了你的数据而你却并没有发现。</p>
<p>鉴权：防止坏人假冒你的身份。</p>
</blockquote>
<p>在上节中，恶意攻击者如果在通信环节绕开或突破了“鉴权”、“认证”，那么依赖于“鉴权”、“认证”的“加密”，实际上也有可有被破解。</p>
<p>针对上述问题，那么我们需要对内容进行更加安全独立的加密处理，就这是所谓的“端到端加密”（E2E）。</p>
<p>比如，那个号称无法被破解的IM——Telegram，实际上就是使用了端到端加密技术。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9144642354448608741b939d5e05baf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>关于端到端加密，这里就不深入探讨，这里有两篇文章有兴趣地可以深入阅读：</strong></p>
<blockquote>
<p>《<a href="http://www.52im.net/thread-764-1-1.html" target="_blank" rel="nofollow noopener noreferrer">移动端安全通信的利器——端到端加密（E2EE）技术详解</a>》</p>
<p>《<a href="http://www.52im.net/thread-763-1-1.html" target="_blank" rel="nofollow noopener noreferrer">简述实时音视频聊天中端到端加密（E2EE）的工作原理</a>》</p>
</blockquote>
<h1 data-id="heading-9">7、雪崩效应问题</h1>
<p>在分布式的IM架构中，存在雪崩效应问题。</p>
<p>我们知道，分布式的IM架构中，为了高可用性，用户每次登陆都是根据负载均衡算法分配到不同的服务器。那么问题就来了。</p>
<p>**举个例子：**假设有5个机房，其中A机房故障，导致这个机房先前服务的用户都跑去B机房。B机房不堪重负也崩溃了，A+B的用户跑去机房C，连锁反应会导致所有服务挂掉。</p>
<p>防止雪崩效应需要在服务器架构，客户端链接策略上有一些配合的解决方案。服务器需要有限流能力作为基础，主要是限制总服务用户数和短时间链接用户数。</p>
<p>在客户端层面，发现服务断开之后要有一个策略，防止大量用户同一时间去链接某个服务器。</p>
<p><strong>通常有2种方案：</strong></p>
<ul>
<li>1）退避：重连之间设置一个随机的间隔；</li>
<li>2）LBS：跟服务器申请重连的新的服务器IP，然后由LBS服务去降低短时间分配到同一个服务器的用户量。</li>
</ul>
<p>这2种方案互不冲突，可以同时做。</p>
<h1 data-id="heading-10">8、弱网问题</h1>
<h3 data-id="heading-11">8.1 弱网问题的原因</h3>
<p>鉴于如今IM在移动端的流行，弱网是很常态的问题。电梯、火车上、开车、地铁等等场景，都会遇到明显的弱网问题。</p>
<p>那么为什么会出现弱网问题？</p>
<p>要回答这个问题，那就需要从无线通信的原理上去寻找答案。</p>
<p>因为无线通信的质量受制于很多方面的因素，比如：无线信号强弱变化快、信号干扰、通信基站分布不均、移动速度太快等等。要说清楚这个问题，那就真是三天三夜都讲不完。</p>
<p><strong>有兴趣的读者，一定要仔细阅读下面这几篇文章，类似的跨学科科谱式文章并不多见：</strong></p>
<blockquote>
<p>《<a href="http://www.52im.net/thread-2402-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM开发者的零基础通信技术入门(十一)：为什么WiFi信号差？一文即懂！</a>》</p>
<p>《<a href="http://www.52im.net/thread-2406-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM开发者的零基础通信技术入门(十二)：上网卡顿？网络掉线？一文即懂！</a>》</p>
<p>《<a href="http://www.52im.net/thread-2415-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM开发者的零基础通信技术入门(十三)：为什么手机信号差？一文即懂！</a>》</p>
<p>《<a href="http://www.52im.net/thread-2419-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM开发者的零基础通信技术入门(十四)：高铁上无线上网有多难？一文即懂！</a>》</p>
</blockquote>
<p><strong>弱网问题是移动端APP的必修课，下面这几篇总结也值得借鉴：</strong></p>
<blockquote>
<p>《<a href="http://www.52im.net/thread-1587-1-1.html" target="_blank" rel="nofollow noopener noreferrer">移动端IM开发者必读(一)：通俗易懂，理解移动网络的“弱”和“慢”</a>》</p>
<p>《<a href="http://www.52im.net/thread-1588-1-1.html" target="_blank" rel="nofollow noopener noreferrer">移动端IM开发者必读(二)：史上最全移动弱网络优化方法总结</a>》</p>
<p>《<a href="http://www.52im.net/thread-1413-1-1.html" target="_blank" rel="nofollow noopener noreferrer">现代移动端网络短连接的优化手段总结：请求速度、弱网适应、安全保障</a>》</p>
<p>《<a href="http://www.52im.net/thread-2678-1-1.html" target="_blank" rel="nofollow noopener noreferrer">百度APP移动端网络深度优化实践分享(三)：移动端弱网优化篇</a>》</p>
</blockquote>
<h3 data-id="heading-12">8.2 IM针对弱网问题的处理</h3>
<p>对于IM来说，弱网问题并不是很复杂，核心是做好消息的重发、排序以及接收端的重试。</p>
<p><strong>为了解决好弱网引发的IM问题，通常可以通过以下手段改善：</strong></p>
<ul>
<li>1）消息自动重发；</li>
<li>2）离线消息接收；</li>
<li>3）重发消息排序；</li>
<li>4）离线指令处理。</li>
</ul>
<p>下面将逐一展开讨论。</p>
<h3 data-id="heading-13">8.3 消息自动重发</h3>
<p>坐地铁的时候，经常遇到列车开起来以后，网络断开，发送消息失败。</p>
<p><strong>这时候产品有2种表现形式：</strong></p>
<ul>
<li>a、直接告诉用户发送失败；</li>
<li>b、保持发送状态，自动重试3-5次（3分钟）以后告诉用户发送失败。</li>
</ul>
<p>**显然：**自动重试失败以后再告诉用户发送失败体验要好很多。尤其是在网络闪断情况下，重试成功率很高，很可能用户根本感知不到有发送失败。</p>
<p>**从技术上：**客户端IMSDK要把每条消息的状态监控起来。发送消息不能简单的调用一下网络发送请求，而是要有一个状态机，管理几个状态：初始状态，发送中，发送失败，发送超时。对于失败和超时的状态，要启用重试机制。</p>
<p><strong>这里还有一篇关于重试机制设计的讨论帖子，有兴趣可以看看：</strong>《<a href="http://www.52im.net/thread-280-1-1.html" target="_blank" rel="nofollow noopener noreferrer">完全自已开发的IM该如何设计“失败重试”机制？</a>》。</p>
<p>《<a href="http://www.52im.net/thread-294-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息送达保证机制实现(一)：保证在线实时消息的可靠投递</a>》一文中关于消息超时与重传机制的实现思路，也可以参考一下。</p>
<h3 data-id="heading-14">8.4 离线消息接收</h3>
<p>现代IM是没有“在线”这个状态的，不需要给用户这个信息。但是从技术的层面，用户掉线了还是要正确的去感知的。</p>
<p><strong>感知方法有几条：</strong></p>
<ul>
<li>a、信令长连接状态：如果长时间没收到到服务器的心跳反馈，说明掉线了；</li>
<li>b、网络请求失败次数：如果多次网络请求失败，说明”可能“掉线了；</li>
<li>c、设备网络状态检测：直接检测网卡状态就好，一般Android/iOS/Windows/Mac都有相应系统API。</li>
</ul>
<p>正确检测到网络状态以后，发现网络从”断开到恢复“的切换，要去主动拉取离线阶段的消息，就可以做到弱网状态不丢消息（从服务器的离线消息列表拉取）。</p>
<p>上面文字中提到的网络状态的确定，涉及到IM里网络连接检查和保活机制问题，是IM里比较头疼的问题。</p>
<p><strong>一不小心，又踩进了IM网络保活这个坑，我就不在这里展开，有兴趣一定要读读下面的文章：</strong></p>
<blockquote>
<p>《<a href="http://www.52im.net/thread-281-1-1.html" target="_blank" rel="nofollow noopener noreferrer">为何基于TCP协议的移动端IM仍然需要心跳保活机制？</a>》</p>
<p>《<a href="http://www.52im.net/thread-2697-1-1.html" target="_blank" rel="nofollow noopener noreferrer">一文读懂即时通讯应用中的网络心跳包机制：作用、原理、实现思路等</a>》</p>
<p>《<a href="http://www.52im.net/thread-209-1-1.html" target="_blank" rel="nofollow noopener noreferrer">微信团队原创分享：Android版微信后台保活实战分享(网络保活篇)</a>》</p>
<p>《<a href="http://www.52im.net/thread-120-1-1.html" target="_blank" rel="nofollow noopener noreferrer">移动端IM实践：实现Android版微信的智能心跳机制</a>》</p>
<p>《<a href="http://www.52im.net/thread-121-1-1.html" target="_blank" rel="nofollow noopener noreferrer">移动端IM实践：WhatsApp、Line、微信的心跳策略分析</a>》</p>
</blockquote>
<h3 data-id="heading-15">8.5 重发消息排序</h3>
<p>弱网逻辑的另一个坑是消息排序。</p>
<p>假如有A、B、C 3条消息，A、C发送成功，B发送的时候遇到了网络闪断，B触发自动重试。</p>
<p>那么接收方的接收顺序应该是 A B C还是A C B呢？我观察过不同的IM产品，处理逻辑各不相同，这个大家有兴趣可以去玩一下。</p>
<p>这个解决方法是要依赖上一篇服务架构里提到的差值排序，同一个人发出的消息，排序按消息附带的本地时间来排。不同人的消息，按照服务器时间排序。</p>
<p>具体我这边就不再得复，可以回头看看本篇中的第四节“4、消息有序性问题”。</p>
<h3 data-id="heading-16">8.6 离线指令处理</h3>
<p>部分指令操作的时候，网络可能出现了问题，等网络恢复以后，要自动同步给服务器。</p>
<p>举一个例子，大家可以试试手机设置为飞行模式，然后在微信里删除一个联系人，看看能不能删除。然后重新打开网络，看看这个数据会不会同步到服务器。</p>
<p>类似的逻辑也适用于已读同步等场景，离线状态看过的信息，要正确的跟服务器同步。</p>
<h3 data-id="heading-17">8.7 小结一下</h3>
<p>IM的弱网处理，其实相对还是比较简单的，基本上自动重试+消息状态就可以解决绝大部分的问题了。</p>
<p>一些细节处理也并不复杂，主要原因是IM的消息量比较小，网络恢复后能快速的恢复操作。</p>
<p>视频会议在弱网下的逻辑，就要复杂的多了。尤其是高丢包的弱网环境下，要尽力去保证音视频的流畅性。</p>
<h1 data-id="heading-18">9、本文小结</h1>
<p>《一套亿级用户的IM架构技术干货》这期文章的上下两篇就这么侃完了，上篇涉及到的IM架构问题倒还好，下篇一不小心又带出了IM里的各种热门问题“坑”，搞IM开发直是一言难尽。。。</p>
<p>建议IM开发的入门朋友们，如果想要系统地学习移动端IM开发的话，应该去读一读我整理的那篇IM开发“从入门到放弃”的文章（哈哈哈），就是这篇《<a href="http://www.52im.net/thread-464-1-1.html" target="_blank" rel="nofollow noopener noreferrer">新手入门一篇就够：从零开发移动端IM</a>》。具体我就不再展开了，不然这篇幅又要刹不住车了。。。（本文同步发布于：<a href="http://www.52im.net/thread-3445-1-1.html" target="_blank" rel="nofollow noopener noreferrer">www.52im.net/thread-3445…</a>）</p>
<h1 data-id="heading-19">10、参考资料</h1>
<p>[1] <a href="https://links.jianshu.com/go?to=https%3A//mp.weixin.qq.com/s/FDFpss7CR0vrNMIHQaETIw" target="_blank" rel="nofollow noopener noreferrer">大规模并发IM服务架构设计</a></p>
<p>[2] <a href="https://links.jianshu.com/go?to=https%3A//mp.weixin.qq.com/s/OcysUzBXtF6m__TOfHZysQ" target="_blank" rel="nofollow noopener noreferrer">IM的弱网场景优化</a></p>
<p>[3] <a href="http://www.52im.net/thread-3182-1-1.html" target="_blank" rel="nofollow noopener noreferrer">零基础IM开发入门(三)：什么是IM系统的可靠性？</a></p>
<p>[4] <a href="http://www.52im.net/thread-294-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息送达保证机制实现(一)：保证在线实时消息的可靠投递</a></p>
<p>[5] <a href="http://www.52im.net/thread-3069-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM开发干货分享：如何优雅的实现大量离线消息的可靠投递</a></p>
<p>[6] <a href="http://www.52im.net/thread-217-1-1.html" target="_blank" rel="nofollow noopener noreferrer">即时通讯安全篇（二）：探讨组合加密算法在IM中的应用</a></p>
<p>[7] <a href="http://www.52im.net/thread-310-1-1.html" target="_blank" rel="nofollow noopener noreferrer">微信新一代通信安全解决方案：基于TLS1.3的MMTLS详解</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            