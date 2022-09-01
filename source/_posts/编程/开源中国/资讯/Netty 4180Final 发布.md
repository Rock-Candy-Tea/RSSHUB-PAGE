
---
title: 'Netty 4.1.80.Final 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6871'
author: 开源中国
comments: false
date: Thu, 01 Sep 2022 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6871'
---

<div>   
<div class="content">
                                                                                            <p>Netty 4.1.80 已正式发布，此版本主要是修复错误，不过也包含了一项重要变化：在使用多核时显著提升了 HTTP/1.x 的性能。如果对 JVM 和性能感兴趣，查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12709" target="_blank">#12709</a> 中记录的所有详细信息。</p> 
<p>Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2022%2F08%2F26%2F4-1-80-Final.html" target="_blank"><strong>主要变化</strong></a></p> 
<ul> 
 <li>修复由于 instanceof 检查导致的 HttpObjectEncoder 可伸缩性问题（修复 #12708）</li> 
 <li>无法找到/加载 MacOSDnsServerAddressStreamProvider 时改进日志记录 <span style="color:#333333">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12732" target="_blank">#12732</a><span style="color:#333333">)</span></li> 
 <li>将 stdlib write/read 替换为 send/recv（修复 #12673）</li> 
 <li>支持 pkcs1<span style="color:#333333"> (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12670" target="_blank">#12670</a><span style="color:#333333">)</span></li> 
 <li>为 PooledByteBufAllocator 添加 Blockhound 异常 <span style="color:#333333"> (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F1212653349" target="_blank">#12653</a><span style="color:#333333">)</span></li> 
 <li>修复接收零大小数据包 (zero-sized datagrams) 时的 epoll 错误<span style="color:#333333"> (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12644" target="_blank">#12644</a><span style="color:#333333">)</span></li> 
 <li>避免在 header 验证失败异常中引入 header 值<span style="color:#333333"> (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12642" target="_blank">#12642</a><span style="color:#333333">)</span></li> 
 <li>避免在 JdkZlibEncoder 中分配大缓冲区 <span style="color:#333333">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12641" target="_blank">#12641</a><span style="color:#333333">)</span></li> 
 <li>原生镜像支持：原生镜像默认设置 IS_EXPLICIT_TRY_REFLECTION_SET_ACCESSIBLE 为 true<span style="color:#333333"> (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12638" target="_blank">#12638</a><span style="color:#333333">)</span></li> 
 <li>在 macOS 上使用 disconnectx(...) <span style="color:#333333"> (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12629" target="_blank">#12629</a><span style="color:#333333">)</span></li> 
 <li>用分配器上的 Java 锁替换同步（修复 #12621）</li> 
 <li>不使用 FixedRecvByteBufAllocator 的静态实例<span style="color:#333333"> (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12594" target="_blank">#12594</a><span style="color:#333333">)</span></li> 
 <li>为 stomp headers 添加转义<span style="color:#333333"> (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F12585" target="_blank">#12585</a><span style="color:#333333">)</span></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fdownloads.html" target="_blank">下载地址</a></p>
                                        </div>
                                      
</div>
            