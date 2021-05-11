
---
title: 'Pipewire 0.3.27 发布，多媒体处理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5207'
author: 开源中国
comments: false
date: Tue, 11 May 2021 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5207'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PipeWire 是用于处理多媒体管道的服务器和用户空间 API 的多媒体处理工具，包括提供视频源（例如来自捕获设备或应用程序提供的流）并将其与客户端复用、访问视频源进行消费、生成用于音频和视频处理的图形。</p> 
<p>Pipewire 0.3.27 正式发布，该版本更新内容如下：</p> 
<p>亮点：</p> 
<ul> 
 <li>修复了导致蓝牙设备停止工作的问题；</li> 
 <li>修复了由于 DBus 插件清理错误导致的切换用户时的会话管理器崩溃；</li> 
 <li>改进监控端口的 volume 处理；</li> 
 <li>修复 GStreamer v4l2 支持；</li> 
 <li>在 pipewire-pulse 中实施 module-remap-sink 和 module-remap-source；</li> 
 <li>大量修复和改进；</li> 
</ul> 
<p>PipeWire：</p> 
<ul> 
 <li>将 loopback 代码移到模块中，并在 pw-loopback 和 pipewire-pulse 中使用。修复了一些清理崩溃的问题；</li> 
 <li>状态文件不再有 X 权限；</li> 
 <li>将 i18n 核心移到一个私有 header 文件中；</li> 
 <li>Stream 现在可以宣传属性并接收属性的更新；</li> 
 <li>修复了一个问题，即用错误的索引来寻址一个端口。它会导致蓝牙设备停止工作；</li> 
</ul> 
<p>SPA 插件：</p> 
<ul> 
 <li>只在我们创建的通道上做 LFE 过滤；</li> 
 <li>改进设备的名称和描述；</li> 
 <li>改进 DBus 连接和源的清理工作，以避免销毁时的崩溃；</li> 
 <li>改进音量处理。硬件、软件和显示器音量现在被正确分开和处理；</li> 
 <li>增加了对 S8 和 S8P 格式的支持；</li> 
</ul> 
<p>工具：</p> 
<ul> 
 <li>pw-cli 现在也能从 JSON 数组中创建 Struct；</li> 
</ul> 
<p>会话管理器：</p> 
<ul> 
 <li>会话管理器现在也可以创建被动链接，这使得有可能在不使用时将 effect chains 和 sink 一起暂停使用；</li> 
 <li>匹配规则现在检查完整的属性值而不是只检查开始部分；</li> 
 <li>处理多个待定参数的枚举，只取最后的结果；</li> 
</ul> 
<p>GStreamer 插件：</p> 
<ul> 
 <li>GStreamer 插件现在建议明确地处理 DMABUF。这是目前避免 v4l2 设备的 memcpy 的唯一方法；</li> 
</ul> 
<p>设备支持：</p> 
<ul> 
 <li>与 pulseaudio 同步 ACP，合并上游补丁而不是我们的 hack 来解决缺少双工设备的问题；</li> 
 <li>V4l2 设备不再暴露他们的 fd 了。以前的 fd 和 mmap 偏移量被传递给客户端来访问缓冲区 内存，但这可能会产生安全问题；</li> 
</ul> 
<p>蓝牙：</p> 
<ul> 
 <li>关机时不要取消配置文件的注册，因为这可能会导致延迟，只需关闭 dbus 连接；</li> 
 <li>蓝牙设备现在尝试使用 graph 中的全局采样率；</li> 
</ul> 
<p>PulseAudio 服务器：</p> 
<ul> 
 <li>使用新的 loopback 模块实现 remap-sink 和 remap-source；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.freedesktop.org%2Fpipewire%2Fpipewire%2F-%2Freleases" target="_blank">https://gitlab.freedesktop.org/pipewire/pipewire/-/releases</a></p>
                                        </div>
                                      
</div>
            