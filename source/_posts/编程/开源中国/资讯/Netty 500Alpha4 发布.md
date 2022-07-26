
---
title: 'Netty 5.0.0.Alpha4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3122'
author: 开源中国
comments: false
date: Tue, 26 Jul 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3122'
---

<div>   
<div class="content">
                                                                                            <p>Netty 5.0.0.Alpha4 已发布，此版本删除了大量重复代码，并对 API 进行了清理。除此之外还增加了在使用 JDK NIO 实现时，对 Unix Domain Socket 的支持。</p> 
<p><strong>主要变化</strong></p> 
<ul> 
 <li>支持创建包含<span style="color:#333333"> ProtocolFamily 的所有 </span>SocketChannel 和 DatagramChannel 实现。<span style="color:#333333">ProtocolFamily 会影响像是否应该使用 </span>Unix Domain Socket 这样<span style="color:#333333">的情况，不过它</span>也允许删除 Domain*Channel 的实现，使事情变得“一致”</li> 
 <li>将 ChannelOption.RECVBUF_ALLOCATOR 更名为 RECVBUFFER_ALLOCATOR</li> 
 <li>支持 JDK 的 Unix Domain Socket</li> 
 <li>将 EventLoop / IoHandler 更改为 take / IoHandle 进行注册，以便将来可以将其他东西而不是 Channel 注册到EventLoop中</li> 
 <li>清理 RecvBufferAllocator</li> 
 <li>修复在 macOS 本地实现中的 disconnect() 实现</li> 
 <li>用 java Locks 替代 synchronized，以更好地支持 Loom</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fmilestone%2F258%3Fclosed%3D1" target="_blank">点此查看详情</a>。</p> 
<p style="margin-left:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2022%2F07%2F22%2F5-0-0-Alpha4.html" target="_blank">公告写道</a>，为了让开发者能够在使用 4.1 的同时尝试体验 Netty 5，开发团队选择将两个版本放到不同的包，以便它们共存。因为这是一个新的主要版本，所以会包含许多破坏性的变化，这些变化主要受 Netty 4.1.x 生命周期汲取的经验影响。</p> 
<p style="margin-left:0">接下来，开发团队会将 Netty 的默认分支更改为 main，因此对 4.1 版本所能接受的变化会更加严格，此举主要是为了保证 4.1 版本回滚的可能性下降到最低。当然，重要的错误修复也会被移植到 4.1。综上所述，开发团队目前没有计划停止对 4.1.x 的支持，而是同时支持 Netty 5 和 4.1.x。</p> 
<p style="margin-left:0">Netty 5 迁移指南：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fwiki%2FNetty-5-Migration-Guide" target="_blank">https://github.com/netty/netty/wiki/Netty-5-Migration-Guide</a></p> 
<p style="margin-left:0">下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fdownloads.html" target="_blank">https://netty.io/downloads.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            