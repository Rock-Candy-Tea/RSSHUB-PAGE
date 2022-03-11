
---
title: 'Netty 4.1.75.Final 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2060'
author: 开源中国
comments: false
date: Fri, 11 Mar 2022 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2060'
---

<div>   
<div class="content">
                                                                                            <p>Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。</p> 
<p>Netty 4.1.75.Final 正式发布，虽说这个版本是一个错误修复版本，但也包含两个变化，可能会改变你的应用程序的内存使用/性能特性，具体更新内容如下：</p> 
<ul> 
 <li>在制作域名套接字地址时避免读取未初始化的内存 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12085" target="_blank">#12085</a>)</li> 
 <li>HTTP/2 标头（header）验证必须拒绝重复的伪标头 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12094" target="_blank">#12094</a>)</li> 
 <li>添加 HTTP 特定的 TooLongFrameExceptions (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12084" target="_blank">#12084</a>)</li> 
 <li>允许在创建时将额外的元数据附加到 ResourceLeakTrackers (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12091" target="_blank">#12091</a>)</li> 
 <li>增加 PlatformDependent.impairMaxDirectMemory (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12118" target="_blank">#12118</a>)</li> 
 <li>将默认的 PooledByteBufAllocator 块大小从 16 MB 减少到 4 MB (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12108" target="_blank">#12108</a>)</li> 
 <li>修正了使用 spliceTo() 时的高 CPU 使用率 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12138" target="_blank">#12138</a>)</li> 
 <li>将 io.netty.allocator.useCacheForAllThreads 的默认值改为 false (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12109" target="_blank">#12109</a>)</li> 
 <li>允许在 SNI headers 中设置更宽松的字符集 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12147" target="_blank">#12147</a>)</li> 
 <li>修复在 ReferenceCountedOpenSslEngine 中对委派任务不正确的处理 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12149" target="_blank">#12149</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2022%2F03%2F10%2F4-1-75-Final.html" target="_blank">https://netty.io/news/2022/03/10/4-1-75-Final.html</a></p>
                                        </div>
                                      
</div>
            