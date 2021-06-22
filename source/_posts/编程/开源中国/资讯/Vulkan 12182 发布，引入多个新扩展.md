
---
title: 'Vulkan 1.2.182 发布，引入多个新扩展'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6942'
author: 开源中国
comments: false
date: Tue, 22 Jun 2021 06:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6942'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Vulkan 1.2.182 已经发布，除了各种文档修复和说明之外，该版本还增加了一些新的扩展。</p> 
<p><strong>主要更新扩展</strong></p> 
<ul> 
 <li>VK_EXT_acquire_drm_display：这个扩展允许应用程序使用 Linux 上的直接渲染管理器（DRM）接口对显示器进行独占控制。这对 Wayland 合成器、VR 和其他用途非常有用。</li> 
 <li>VK_EXT_physical_device_drm：该扩展允许查询物理设备的 DRM（直接渲染管理器）属性。这项工作可以实现 Vulkan 物理设备与 Linux 上 DRM 节点的匹配。该扩展对于由 Vulkan 驱动的 Wayland 合成器非常有用。</li> 
 <li>VK_EXT_multi_draw：多重绘制支持，允许直接向驱动传递整个绘制序列。这个多图扩展是由 Valve、NVIDIA、Intel、Igalia、AMD、Samsung 和 Khronos 合作完成的。</li> 
 <li>VK_HUAWEI_subpass_shading：华为贡献的扩展允许应用程序在渲染通道的一个子通道中执行一个子通道着色管道。</li> 
 <li>VK_NV_ray_tracing_motion_blur：NVIDIA 贡献了这个扩展，用于光线追踪运动模糊处理和移动几何体的快速追踪。</li> 
</ul> 
<p>详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FVulkan-Docs%2Fcommit%2F1b32e9d5beeee44d81520cbf35193047e60dbf6b" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            