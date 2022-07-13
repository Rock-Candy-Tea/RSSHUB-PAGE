
---
title: 'Netty 4.1.79.Final 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2903'
author: 开源中国
comments: false
date: Wed, 13 Jul 2022 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2903'
---

<div>   
<div class="content">
                                                                                            <p>Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。</p> 
<p>Netty 4.1.79.Final 是一个错误修复版本，具体更新内容如下：</p> 
<ul> 
 <li>PEM 证书解析器不再容易受到 PemReader 中的指数回溯的影响</li> 
 <li>HTTP POST body 中的 RFC 非法的额外 & 符号不再被拒绝</li> 
 <li>增加了 <code>io.netty.osClassifiers</code> 系统属性，以避免读取 <code>os-release</code> 文件</li> 
 <li>修复了 <code>SslHandler</code> 中的一个 bug，这样即使 <code>handlerAdded</code> 抛出异常， <code>handlerRemoved</code> 也能正常工作</li> 
 <li>在 arch64 上使用正确的 OSGi 处理器指令，使得在 ARM 上使用 OSGi 成为可能</li> 
 <li>现在对以双斜杠开头的 HTTP 路径的解析方式与浏览器相同</li> 
 <li><code>isCompleted</code> 标志现在可以正确地保留在来自 <code>HttpData.reservedDuplicate()</code> 的对象上</li> 
 <li><code>HttpUtil.isOriginForm()</code> 和 <code>isAsteriskForm()</code> 方法现在正确地符合 RFC 7230</li> 
 <li>修复了允许在事件循环线程之外调用 <code>EpollDatagramChannel</code> 的多播方法的问题</li> 
 <li>增加了对 LoongArch64 处理器架构的支持</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2022%2F07%2F11%2F4-1-79-Final.html" target="_blank">https://netty.io/news/2022/07/11/4-1-79-Final.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            