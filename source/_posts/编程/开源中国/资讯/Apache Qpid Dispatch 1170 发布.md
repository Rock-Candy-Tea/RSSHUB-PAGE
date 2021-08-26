
---
title: 'Apache Qpid Dispatch 1.17.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7521'
author: 开源中国
comments: false
date: Thu, 26 Aug 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7521'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Qpid Dispatch 是一个轻量级的 Advanced Message Queuing Protocol 1.0 消息路由（AMQP 1.0），用 C 编写并基于 Qpid Proton 构建。它提供了一个 AMQP 端点之间灵活且可扩展的互连，无论它们是客户端、代理或其他支持 AMQP 的服务。</p> 
<h3>新功能和改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-1539" target="_blank">DISPATCH-1539</a> - Python 2 已经过期</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-2108" target="_blank">DISPATCH-2108</a> - TCP 适配器应该汇总监听器和连接器的统计数据</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-2142" target="_blank">DISPATCH-2142</a> - 在 TCP 适配器中使用专用缓冲区</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-2178" target="_blank">DISPATCH-2178</a> - 不要单独构建 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flibqpid-dispatch.so" target="_blank">libqpid-dispatch.so</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-2198" target="_blank">DISPATCH-2198</a> - [http2] 实现包含 q2 阻塞/非阻塞的 http2 流量控制</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-2201" target="_blank">DISPATCH-2201</a> - 删除 router_node.c 中 type_registered 全局标志；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-2211" target="_blank">DISPATCH-2211</a> - [http2] system_tests_grpc 在 http2 缓冲区泄漏的情况下失败；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-2212" target="_blank">DISPATCH-2212</a> - [http2] 当创建AMQP消息时，将其主题字段设置为方法（请求时）和状态（响应时）；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-2215" target="_blank">DISPATCH-2215</a> - [http2] read_data_callback 中错误的 printf 格式指定器；</li> 
</ul> 
<h3>Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-1619" target="_blank">DISPATCH-1619</a> - 系统测试从未关闭由 wait_router_connected 创建的连接</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-1623" target="_blank">DISPATCH-1623</a> - 调查为什么控制台有时会在登录后几秒内放弃与路由的连接</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-1865" target="_blank">DISPATCH-1865</a> - [http2] curl 客户端在针对 HTTP2 适配器运行多个客户端时挂起。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-1878" target="_blank">DISPATCH-1878</a> - 客户端应用程序无法通过 tcpListener 获得响应；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-1896" target="_blank">DISPATCH-1896</a> - [http2] 从服务器收到的 GOAWAY frame 没有传播到客户端</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-1963" target="_blank">DISPATCH-1963</a> - http1 适配器的内存泄漏</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FDISPATCH-1975" target="_blank">DISPATCH-1975</a> - TCP 适配器在网络上只发送 512 字节的数据包；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fqpid.apache.org%2Freleases%2Fqpid-dispatch-1.17.0%2Frelease-notes.html" target="_blank">https://qpid.apache.org/releases/qpid-dispatch-1.17.0/release-notes.html</a></p>
                                        </div>
                                      
</div>
            