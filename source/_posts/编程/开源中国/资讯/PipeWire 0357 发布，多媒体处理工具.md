
---
title: 'PipeWire 0.3.57 发布，多媒体处理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=250'
author: 开源中国
comments: false
date: Sun, 04 Sep 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=250'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">PipeWire 是用于处理多媒体管道的服务器和用户空间 API 的多媒体处理工具，包括提供视频源（例如来自捕获设备或应用程序提供的流）并将其与客户端复用、访问视频源进行消费、生成用于音频和视频处理的图形。</span></p> 
<p>该版本主要更新内容：</p> 
<ul> 
 <li>支持 conf.d/ 文件的屏蔽。（<a href="https://www.oschina.net/pipewire/pipewire/-/issues/2629">#2629</a>）</li> 
 <li>在可用时使用 org.freedesktop.portal.Realtime。这会进行正确的 PID/TID 映射，<span style="background-color:#ffffff; color:#121212">用于从 Flatpaks 的沙箱中将线程设置为实时。</span></li> 
 <li>修复脉冲隧道中的速率调整逻辑，这将导致使用隧道时增加延迟和中断。（<a href="https://www.oschina.net/pipewire/pipewire/-/issues/2548">#2548</a>）</li> 
 <li>添加 OPUS 作为新的供应商编解码器，添加 OPUS-A2DP 规范。PipeWire 现在可以通过蓝牙发送和接收 OPUS 数据。</li> 
 <li>添加了 AAC 解码器，因此 PipeWire 现在也可以用作 A2DP AAC 接收器。</li> 
 <li>修复一些使用错误采样率的问题。（<a href="https://www.oschina.net/pipewire/pipewire/-/issues/2614">#2614</a>）</li> 
 <li>修复源的速率匹配。这修复了跟随源会生成许多重新同步警告的错误。</li> 
 <li>更多错误修正和改进。</li> 
</ul> 
<p>更多内容可查看更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.freedesktop.org%2Fpipewire%2Fpipewire%2F-%2Ftags%2F0.3.57" target="_blank">https://gitlab.freedesktop.org/pipewire/pipewire/-/tags/0.3.57</a></p>
                                        </div>
                                      
</div>
            