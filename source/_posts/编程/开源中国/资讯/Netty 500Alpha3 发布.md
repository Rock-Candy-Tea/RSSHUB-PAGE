
---
title: 'Netty 5.0.0.Alpha3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9710'
author: 开源中国
comments: false
date: Tue, 12 Jul 2022 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9710'
---

<div>   
<div class="content">
                                                                                            <p>Netty 5.0.0.Alpha3 已发布，这是一个重要的里程碑，此版本迁移了所有代码——以使用新的<code>Buffer</code><span style="background-color:#ffffff; color:#333333"><span> </span>API</span>，并完全移除<code>ByteBuf</code><span style="background-color:#ffffff; color:#333333">。<span> </span></span></p> 
<p><strong><span style="background-color:#ffffff; color:#333333"><span>主要变化</span></span></strong></p> 
<ul> 
 <li>所有代码现在使用<code>Buffer</code><span> </span>（新的 buffer API）</li> 
 <li>移除<code>ChannelInboundHandler</code></li> 
 <li>移除<code>Http2MultiplexCodec</code>和<code>Http2MultiplexCodecBuilder</code></li> 
 <li>为<code>Buffer</code>,<span> </span><code>EventLoop</code>,<span> </span><code>Future</code>添加多个便捷的方法</li> 
 <li><code>ChannelHandlerContext</code>不再对<code>AttributeMap</code>进行扩展</li> 
 <li>将 half-closure 作为 Channel 的 core-concept</li> 
 <li>支持双向发送 "custom" 事件</li> 
 <li>Remove blocking methods from<span> </span><code>Future</code><span> </span>interface, people need to use<span> </span><code>Future.asStage()</code><span> </span>to gain access to blocking methods</li> 
 <li>从<code>Future</code>接口移除阻塞方法，开发者需要使用<code>Future.asStage()</code><span> </span>才能访问阻塞方法</li> 
 <li>移除<code>Channel.Unsafe</code></li> 
 <li>从<code>Channel</code>API 移除<code>ChannelOutboundBuffer</code><span>，作为</span><code>AbstractChannel</code>的实现细节</li> 
 <li>移除<code>@Sharable</code><span>，使用</span><code>ChannelHandler.isSharable()</code><span>替代</span></li> 
 <li><span>移除</span><code>EventLoop.Unsafe</code>，并添加<code>EventLoop.registerForIo(...)</code><span> </span>/<span> </span><code>EventLoop.deregisterForIo(...)</code></li> 
 <li>将<code>Channel.bytesBeforeUnwritable()</code>重命名为<code>Channel.writableBytes()</code></li> 
 <li>添加 ProtocolEvent 并让 SSL 和 WebSocket 实现使用它</li> 
 <li>将通用逻辑移动至<code>AbstractChannel</code>，从而使实现更容易重用代码，还要确保重命名受保护的方法，以更加一致</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2022%2F07%2F08%2F5-0-0-Alpha3.html" target="_blank">详情</a>。</p>
                                        </div>
                                      
</div>
            