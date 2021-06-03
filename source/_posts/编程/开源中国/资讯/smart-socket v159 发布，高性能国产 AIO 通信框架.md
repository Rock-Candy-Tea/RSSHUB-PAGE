
---
title: 'smart-socket v1.5.9 发布，高性能国产 AIO 通信框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ee55c6b1022cf040b1cd9339794bc499665.png'
author: 开源中国
comments: false
date: Thu, 03 Jun 2021 11:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ee55c6b1022cf040b1cd9339794bc499665.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:justify">smart-socket 是一个 AIO 通信框架，可以快速、轻松地开发 Client/Server 网络应用程序。它大大简化了网络编程难度和复杂度，可广泛应用与各类TCP/UDP的通信场景。</p> 
<p style="text-align:justify">本次发布为广大 smart-socket 用户奉上一款非常实用的传输层码流监控插件：StreamMonitorPlugin。开发这款插件的初衷是为了帮助新手朋友们更好的理解通信开发，理解面向协议编程。</p> 
<p style="text-align:justify">smart-socket 开源以来，经常会收到一些咨询：「为什么对方一发送数据，连接就断开了？」、「为什么收不到对方发的数据？」通常这种情况下很多人的第一反应是：「smart-socket 是不是有 bug！」。而当我寻问：「你的通信协议是什么？」，对方：「呃...不知道！我就是发送个字符串」。</p> 
<p style="text-align:justify">显然，没有正确的理解「协议」，不仅写不出正确的代码，也提不出正确的问题。希望通过这款 StreamMonitorPlugin 插件，将通信过程中传输的字节流直观的展示出来，帮助大家更好的理解协议，写出正确的编解码算法。而对于有专业开发经验的朋友而言，运用这款插件也能为开发、调试带来很多的便利，至少无需再用 wireshark 来抓码流了（ps：反正我用的很香）。</p> 
<p style="text-align:justify">插件的运行效果如下所示：<span style="color:#3498db">蓝色字体表示输入字节流</span>，<span style="color:#e74c3c">红色字体表示输出字节流</span></p> 
<p style="text-align:justify"><img src="https://oscimg.oschina.net/oscnet/up-ee55c6b1022cf040b1cd9339794bc499665.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:justify">更新内容</h4> 
<ul> 
 <li>新特性：新增传输层码流监控插件：<span style="color:#000000">StreamMonitorPlugin。</span></li> 
 <li>优化：订正 QuickTimeTask 中的单词拼写错误问题。</li> 
 <li>优化：新增传输通道代理对象：AsynchronousSocketChannelProxy<span style="color:#000000">，并重构 TLS/SSL 通道 对象：</span><span style="color:#000000">SslAsynchronousSocketChannel</span><span style="color:#000000"> 。</span></li> 
 <li><span style="color:#000000">bugfix：修复监控插件：</span><span style="color:#000000">MonitorPlugin 历史连接总数统计错误问题。</span></li> 
</ul> 
<h4 style="text-align:left">Maven</h4> 
<pre style="text-align:left"><code><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>org.smartboot.socket<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>aio-pro<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>1.5.9<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></code></pre>
                                        </div>
                                      
</div>
            