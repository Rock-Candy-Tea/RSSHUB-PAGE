
---
title: 'Netty 4.1.67.Final 发布，异步事件驱动的网络应用框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7096'
author: 开源中国
comments: false
date: Wed, 18 Aug 2021 06:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7096'
---

<div>   
<div class="content">
                                                                                            <p>Netty 4.1.67.Final 已经发布。Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。</p> 
<p>该版本主要的变化包括：</p> 
<ul> 
 <li>当请求没有连接头时，服务器 h2c 升级失败；</li> 
 <li>删除 io.netty.http2.validateContentLength SystemProperty；</li> 
 <li>为 KQueue MacOS 增加对客户端 TCP FastOpen 的支持；</li> 
 <li>使 TCP_FASTOPEN 通道选项传输不可知；</li> 
 <li>修复委托/异步 SSL 的错误；</li> 
 <li>如果还有东西要发送到远程对等点，请确保我们始终包装；</li> 
 <li>JdkZlibDecoder 在 GZIP 页脚被分割时可能会损坏数据；</li> 
 <li>将 DnsNameResolver.cnameCache() 改为公共的；</li> 
 <li>当没有 SslHandler 时，移除 ApplicationProtocolNegotiationHandler；</li> 
 <li>增加 PromiseNotifier 静态方法，负责取消传播；</li> 
 <li>在关闭流时将权重分配给子代；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2021%2F08%2F16%2F4-1-67-Final.html" target="_blank">https://netty.io/news/2021/08/16/4-1-67-Final.html</a></p>
                                        </div>
                                      
</div>
            