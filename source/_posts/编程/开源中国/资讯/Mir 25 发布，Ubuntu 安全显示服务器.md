
---
title: 'Mir 2.5 发布，Ubuntu 安全显示服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1879'
author: 开源中国
comments: false
date: Fri, 15 Oct 2021 06:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1879'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Mir 是一套用于构建基于 Wayland 的 Shell 库。Mir 简化了 Shell 作者需要处理的复杂性：它提供了一个稳定的、经过良好测试的、高性能的平台，具有触控、鼠标和平板电脑输入、多显示器功能和安全的客户端-服务器通信。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>ABI 摘要</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>弃用 mirclient</li> 
 <li>弃用 mirprotobuf</li> 
 <li>mircommon ABI 升级至 8</li> 
 <li>mirplatform ABI 升级至 23</li> 
 <li>mirserver ABI 升级至 56</li> 
 <li>mirwayland ABI 升级至 3</li> 
 <li>mirplatformgraphics ABI 升级至 19</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">增强</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[Wayland] 将 wlr_layer_shell_unstable_v1 版本从 3 升级至 4</li> 
 <li>[Wayland] 为 Layer Shell 增加 focus_mode 表面属性</li> 
 <li>[Wayland] 添加 zwp_virtual_keyboard_v1</li> 
 <li>[Wayland] 添加 zwp_text_input_v3 和 zwp_input_method_v2</li> 
 <li>[Wayland] 允许带有 DRM_FORMAT_MOD_INVALID 的 zwp_linux_buffer_params_v1.add()</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>当 surface 和 role 以错误的顺序销毁时，Mir 会崩溃</li> 
 <li>使 GTK 隐藏光标的方法在 Mir 上生效</li> 
 <li>[input] 修复 InputDeviceHub 的线程安全问题</li> 
 <li>[Xwayland] 改进弹出窗口的类型和定位</li> 
 <li>[Xwayland] 使用 SurfaceStateTracker 来跟踪窗口状态</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMirServer%2Fmir%2Freleases" target="_blank">https://github.com/MirServer/mir/releases</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            