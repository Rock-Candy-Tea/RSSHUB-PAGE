
---
title: 'Netty 4.1.69.Final 发布，异步事件驱动的网络应用框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2027'
author: 开源中国
comments: false
date: Tue, 12 Oct 2021 06:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2027'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Netty 4.1.67.Final 已经发布。Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。</span></p> 
<p>该版本的主要变化包括：</p> 
<ul> 
 <li>netty-all 不会再重新打包 jars</li> 
 <li>使用 install_tool_name 和 codesign 来修补着色库的 id </li> 
 <li>为 macOS 添加服务器端 TCP FastOpen 支持 </li> 
 <li>确保 ServerChannel 实现在每个读取循环中接受多个连接 </li> 
 <li>允许在构造 HashedWheelTimer 时指定 taskExecutor </li> 
 <li>修复 SwappedByteBuf 中的 little-endian get/set 方法</li> 
 <li>确保 CompositeByteBuf.decompose(...) 返回未解包的缓冲区 </li> 
 <li>修复 ByteBufUtil indexOf ClassCastException</li> 
 <li>netty-bom 提供已解析的 tcnative 版本 </li> 
 <li>进行 xml 验证时排除目标文件夹</li> 
 <li>当帧不以 NULL 八位字节结尾时，修复 StompSubframeDecoder 中可能的泄漏</li> 
 <li>在 GLIBC 上编译的 Epoll 仅在运行时支持 GLIBC</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2021%2F10%2F11%2F4-1-69-Final.html" target="_blank">官方公告</a>。</p>
                                        </div>
                                      
</div>
            