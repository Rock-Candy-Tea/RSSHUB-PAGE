
---
title: 'Weston 11.0 发布，Wayland 合成器的参考实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=253'
author: 开源中国
comments: false
date: Sat, 24 Sep 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=253'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#333333">Weston 是 Wayland 合成器的参考实现，同时也是一个开箱即用的多用途桌面环境。Weston 为汽车、嵌入式、机械、工业、机顶盒和电视等非桌面用途提供了一个非常基础的全功能桌面环境。</span></p> 
<p style="margin-left:0px">目前 Weston 11.0 发布了，此版本在色彩管理的基础设施方面有改进，比如提供了实验性的色彩管理支持，它可以与监视器 ICC 配置文件一起使用。还可以将监视器设置为 HDR 模式，并从 Weston 配置文件中提供 HDR 特性。但公告中还提及：现在 Weston <strong>还不能生成任何 HDR 内容。</strong></p> 
<p style="margin-left:0px"><strong>其次还有这些亮点优化：</strong></p> 
<ul> 
 <li>各种 RDP 改进。</li> 
 <li>DRM 后端的性能改进。</li> 
 <li>支持 wp_single_pixel_buffer_v1 协议。</li> 
 <li>weston_buffer 重构。</li> 
 <li>同时运行多个后端（例如 KMS + RDP）和 DRM 后端中的多 GPU 支持的基础。（目前此功能尚未支持，可能会在将来的版本中提供。）</li> 
</ul> 
<p><strong>重大更改：</strong></p> 
<ul> 
 <li>cms-static 和 cms-colord 插件现已弃用。</li> 
 <li>从桌面 shell 中删除了许多功能：多工作区、缩放、曝光。</li> 
 <li>wl_shell 支持已被删除（被 xdg-shell 取代）。</li> 
 <li>fbdev 后端已被移除（被 KMS 取代）。</li> 
 <li>weston-launch 和 launcher-direct 已被移除（被 libseat 取代）。</li> 
 <li>weston-info 和 weston-gears 客户端已被删除（weston-info 由wayland-info 取代）。</li> 
 <li>现在默认设置 KMS max-bpc 属性，如果你遇到黑色带有（故障）显示器的屏幕，请尝试在 weston.ini 中降低它。</li> 
 <li>Weston 现在将在内存不足时中止，这意味着 Weston 不适合适用于内存受限的环境。</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.freedesktop.org%2Farchives%2Fwayland-devel%2F2022-September%2F042410.html" target="_blank">https://lists.freedesktop.org/archives/wayland-devel/2022-September/042410.html</a></p>
                                        </div>
                                      
</div>
            