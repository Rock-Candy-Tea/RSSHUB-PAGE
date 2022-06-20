
---
title: 'Netty 4.1.78.Final 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9866'
author: 开源中国
comments: false
date: Mon, 20 Jun 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9866'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。</p> 
<p>Netty 4.1.78.Final 是一个错误修复版本，具体更新内容如下：</p> 
<ul> 
 <li>修正了一个错误，即在已经有 OPT 记录的 DNS 查询中加入了 OPT 记录 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12370" target="_blank">#12370</a>)</li> 
 <li>修复了当用 HTTP POST 上传的文件在名称中含有反斜杠时引起的错误 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12334" target="_blank">#12334</a>)</li> 
 <li>修复了 BlockHound 集成中的一个问题，该问题有时会导致 <code>NetUtil</code> 被报告为执行阻塞操作 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12414" target="_blank">#12414</a>)</li> 
 <li>修复了 <code>JdkSslContext</code> 的一个类似 BlockHound 的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12435" target="_blank">#12435</a>)</li> 
 <li>修复了一个罕见的 <code>NullPointerException</code> 错误，当 <code>ReferenceCountedOpenSslEngine</code> 从其构造函数中抛出 <code>OutOfMemoryError</code>，然后又被最终确定时，可能会发生这个问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12434" target="_blank">#12434</a>)</li> 
 <li><code>SslHandler</code> 现在将套接字文件描述符添加到 BIO 中，当 SslEngine 支持这个时（boringssl 和 libressl），这允许跟踪和观察工具在每个连接的基础上监控加密流量 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12438" target="_blank">#12438</a>)</li> 
 <li>现在可以在 <code>EmbeddedEventLoop</code> 中显式地步入调度时钟，这对制作具有确定性调度的自动化测试很有用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12459" target="_blank">#12459</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2022%2F06%2F14%2F4-1-78-Final.html" target="_blank">https://netty.io/news/2022/06/14/4-1-78-Final.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            