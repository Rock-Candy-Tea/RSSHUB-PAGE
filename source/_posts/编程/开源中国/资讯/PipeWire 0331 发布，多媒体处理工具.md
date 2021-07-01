
---
title: 'PipeWire 0.3.31 发布，多媒体处理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6141'
author: 开源中国
comments: false
date: Thu, 01 Jul 2021 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6141'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PipeWire 是用于处理多媒体管道的服务器和用户空间 API 的多媒体处理工具，包括提供视频源（例如来自捕获设备或应用程序提供的流）并将其与客户端复用、访问视频源进行消费、生成用于音频和视频处理的图形。</p> 
<p>PipeWire 0.3.31 正式发布，该版本更新内容如下：</p> 
<h3>亮点</h3> 
<ul> 
 <li>修复了 alsa-lib 1.2.5 的问题；</li> 
 <li>新的 pulseaudio 模块：module-avahi-zeroconf、module-pipe-source、module-roc-sink、module-roc-source；</li> 
 <li>JACK 的稳定性有了很大的提高，同时线程优先级也得到了改善；</li> 
 <li>处理文件描述符耗尽时的各种崩溃和锁定问题；</li> 
 <li>蓝牙现在使用硬件数据库来禁用所列设备上的非工作功能；</li> 
 <li>现在可以使用 pw-metadata 动态更改调度量和速率；</li> 
 <li>许多错误修正和改进。</li> 
</ul> 
<h2>PipeWire</h2> 
<ul> 
 <li>改进了错误情况下对上下文的清理；</li> 
 <li>现在有一个 pw-test 框架，用于改进单元测试；</li> 
 <li>改进属性序列化为有效的 JSON；</li> 
 <li>修复了一些宏，以便更好地与 coverity 一起工作；</li> 
 <li>现在检查元数据的权限。客户端需要有 M 权限才能为一个对象设置元数据；</li> 
 <li>核心元数据对象现在将删除已删除对象的元数据；</li> 
 <li>音频适配器现在将跟随图像的速率，并由重采样器动态地调整自己；</li> 
 <li>修复了音频转换器中的一个无限循环；</li> 
 <li>更优雅地处理 out-of-fds。通过断开客户端连接来处理截断的控制数据；</li> 
 <li>修复了具有许多数据流的探查器崩溃的问题；</li> 
 <li>改进 pw-filter 中的延迟处理；</li> 
 <li>改进了设备和数据流中的延迟报告；</li> 
 <li>增加了 sink/source 的例子；</li> 
</ul> 
<h2>PulseAudio 服务器</h2> 
<ul> 
 <li>确保设置了 node.description，否则某些应用程序会崩溃；</li> 
 <li>模块加载和卸载得到改进；</li> 
 <li>module-avahi-zeroconf 已实施；</li> 
 <li>module-pipe-source 已实施；</li> 
 <li>module-roc-sink 和 module-roc-source 已实施；</li> 
 <li>最大连接数已限制为 64；</li> 
 <li>更优雅地处理 out-of-fds；</li> 
 <li>修复读/写指针溢出；</li> 
 <li>source 和 sink 状态现在与监视器状态分离，并且在不播放任何内容时将报告 IDLE；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.freedesktop.org%2Fpipewire%2Fpipewire%2F-%2Freleases" target="_blank">https://gitlab.freedesktop.org/pipewire/pipewire/-/releases</a></p>
                                        </div>
                                      
</div>
            