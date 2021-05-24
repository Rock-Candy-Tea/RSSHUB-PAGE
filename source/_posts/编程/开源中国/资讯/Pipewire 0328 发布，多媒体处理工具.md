
---
title: 'Pipewire 0.3.28 发布，多媒体处理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8021'
author: 开源中国
comments: false
date: Sun, 23 May 2021 23:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8021'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PipeWire 是用于处理多媒体管道的服务器和用户空间 API 的多媒体处理工具，包括提供视频源（例如来自捕获设备或应用程序提供的流）并将其与客户端复用、访问视频源进行消费、生成用于音频和视频处理的图形。</p> 
<p>Pipewire 0.3.28 正式发布，该版本更新内容如下：</p> 
<p><strong>亮点</strong></p> 
<ul> 
 <li>实现了 Freewheeling，这使得它有可能以 ardour 输出项目；</li> 
 <li>添加了一个新的功能强大的过滤器链模块，该模块可用于从 ladspa 和内置插件创建各种过滤器链；</li> 
 <li>现在实现了更多的 pulseaudio 模块：module-ladspa-sink、module-ladspa-source、module-pipe-sink、module-tunnel-sink、module-tunnel-source、module-zeroconf-discover；</li> 
 <li>修复了注销/登录后设备不会出现的错误；</li> 
 <li>修复了将音量重置为 0 和设备没有音频的错误；</li> 
 <li>配置文件现在被安装在 data dir 中，首先检查 /etc/pipewire 和 $HOME 中的系统覆盖；</li> 
</ul> 
<p><strong>PipeWire</strong></p> 
<ul> 
 <li>为 JACK 客户端实现 freewheeling；</li> 
 <li>增加过滤链模块，可用于从 ladspa 和内置插件中构建任意的图形；</li> 
 <li>添加新属性以轻松设置算法参数；</li> 
 <li>添加 module-pulse-tunnel，以在与 PulseAudio 兼容服务器之间来回传送音频；</li> 
 <li>添加一个 avahi zeroconf 发现模块，在广播 PulseAudio 设备时创建脉冲隧道；</li> 
 <li>现在，应用程序的监视器端口以 monitor 前缀命名，以避免与输出端口混淆；</li> 
</ul> 
<p><strong>GStreamer</strong></p> 
<ul> 
 <li>修复了 pipewiresink 插件；</li> 
</ul> 
<p><strong>SPA plugins</strong></p> 
<ul> 
 <li>将事件添加到 dbus 插件，这可用于检测 dbus 断开连接；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.freedesktop.org%2Fpipewire%2Fpipewire%2F-%2Freleases" target="_blank">https://gitlab.freedesktop.org/pipewire/pipewire/-/releases</a></p>
                                        </div>
                                      
</div>
            