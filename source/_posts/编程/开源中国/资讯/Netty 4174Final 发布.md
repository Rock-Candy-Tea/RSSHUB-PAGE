
---
title: 'Netty 4.1.74.Final 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8186'
author: 开源中国
comments: false
date: Thu, 10 Feb 2022 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8186'
---

<div>   
<div class="content">
                                                                                            <p>Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。</p> 
<p>Netty 4.1.74.Final 是一个错误修复版本，更新内容如下：</p> 
<ul> 
 <li>引入 Http2DataChunkedInput 来发送分块的 Http2 数据帧 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12066" target="_blank">#12066</a>)</li> 
 <li>当分散读取用于数据报时，不要将 writerIndex 设置为不正确的值 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12076" target="_blank">#12076</a>)</li> 
 <li>支持 TLSv1.3 的 RFC 8879 证书压缩 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12012" target="_blank">#12012</a>)</li> 
 <li>在失败的情况下释放 DnsQuery，以防止泄漏发生 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12048" target="_blank">#12048</a>)</li> 
 <li>在 DnsNameResolver 中传播 BindException (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12034" target="_blank">#12034</a>)</li> 
 <li>避免掩盖 Mac DNS 提供商可用性失败的原因 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12039" target="_blank">#12039</a>)</li> 
 <li>将 Fragment-Host 声明添加到分发本地库的捆绑包中 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12018" target="_blank">#12018</a>)</li> 
 <li>在解析 ipv6 地址时不要剥离 scopeId (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12019" target="_blank">#12019</a>)</li> 
 <li>尽量不要将对象回收到终止的线程中 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11996" target="_blank">#11996</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2022%2F02%2F08%2F4-1-74-Final.html" target="_blank">https://netty.io/news/2022/02/08/4-1-74-Final.html</a></p>
                                        </div>
                                      
</div>
            