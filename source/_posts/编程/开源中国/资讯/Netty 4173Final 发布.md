
---
title: 'Netty 4.1.73.Final 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8033'
author: 开源中国
comments: false
date: Fri, 14 Jan 2022 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8033'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Netty 4.1.73.Final 正式发布，因为这个版本修复了 Netty "核心部分" 的一些错误，因此官方强烈建议用户尽快升级。该版本具体更新内容如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>使 PooledByteBufAllocator 的 "pinned memory" 反映出正在使用的缓冲区（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11990" target="_blank">#11990</a>)</li> 
 <li>确保在 fin_wait2 状态下启用<span> </span><code>SO_LINGER</code><span> </span>和调用<span> </span><code>showdownOutput</code><span> </span>以启动 TCP 半关闭的一方仍能接收和处理处于 close_wait 状态的另一端发送的数据 （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11982" target="_blank">#11982</a>)</li> 
 <li>配置缓存对齐时正确计算 elementSize （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11987" target="_blank">#11987</a>)</li> 
 <li>WebSocketServerProtocolHandshakeHandler 应该在没有聚合的情况下工作（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11976" target="_blank">#11976</a>)</li> 
 <li>修复：如果没有触发 channelRead，则使 ByteToMessageDecoder 不调用 channelReadComplete 中的 read() 。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11966" target="_blank">#11966</a>)</li> 
 <li>添加基于锁的消息传递队列以帮助调试 Recycler 的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11972" target="_blank">#11972</a>)</li> 
 <li>修复 ByteBufUtil.indexOf(buf， buf)（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11970" target="_blank">#11970</a>)</li> 
 <li>默认情况下不定期重新读取 /etc/hosts （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11943" target="_blank">#11943</a>)</li> 
 <li>修复 ArrayIndexOutOfBounds (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11939" target="_blank">#11939</a>)</li> 
 <li>允许禁用重复的本地库检查（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11928" target="_blank">#11928</a>)</li> 
 <li>如果内容相同，则允许相同的本地库（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11927" target="_blank">#11927</a>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2022%2F01%2F12%2F4-1-73-Final.html" target="_blank">https://netty.io/news/2022/01/12/4-1-73-Final.html</a></p>
                                        </div>
                                      
</div>
            