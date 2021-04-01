
---
title: 'Netty 4.1.61.Final 发布，异步事件驱动的网络应用框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3757'
author: 开源中国
comments: false
date: Thu, 01 Apr 2021 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3757'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Netty 4.1.61.Final 已经发布。Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。本次更新除了修复各种错误之外，还包含了一个安全修复（CVE-2021-21295）的后续工作，可能会影响使用 codec-http2 包和代理 HTTP/2 到 HTTP/1.1 的用户。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>在 HTTP2 解码器中验证 Content-Length 头</li> 
 <li>添加 UDP_GRO 支持</li> 
 <li>在没有 ThreadGroup 的情况下，DefaultThreadFactory 不能使用 Thread.currentThread()</li> 
 <li>在交叉编译的时候使用 gcc10 来支持 LSE</li> 
 <li>允许在转换 CONNECT 请求时使用空路径</li> 
 <li>确保即使设置了 endStream 标志，也能正确地将异常传播给流</li> 
 <li>连接前不发送 GOAWAY 帧</li> 
 <li>当使用 DatagramChannels 时，如果字节数小于配置的字节数，继续读取</li> 
 <li>允许配置每个事件循环要写入的最大消息数</li> 
 <li>使用 TCP 快速打开修复程序刷新 SslHandler</li> 
 <li>支持带有 SegmentedDatagramPacket 的 CompositeByteBuf</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2021%2F03%2F30%2F4-1-61-Final.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            