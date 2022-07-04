
---
title: 'Vulkan 1.3.219 发布，新增两个扩展'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6735'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6735'
---

<div>   
<div class="content">
                                                                                            <p>Vulkan 1.3.219 已发布，更新内容除了改进和修正文档说明之外，还包含两个新扩展。</p> 
<p>两个新的 Vulkan 扩展分别为：</p> 
<p><strong style="color:#121212">VK_EXT_multisampled_render_to_single_sampled</strong> - 展示了对单采样附件执行多采样渲染的能力，而无需额外的内存或带宽开销。这取决于设备/驱动程序的实现和其他因素，目前此扩展可在使用 Google、Arm、Qualcomm 和 Imagination 供应商的移动设备上运行。</p> 
<p><strong style="color:#121212">VK_EXT_shader_module_identifier </strong>- 此扩展使应用程序/游戏能够查询与 Vulkan 着色器模块关联的小标识符。在随后的游戏/应用程序运行中，可以使用相同的标识符代替 Vulkan 着色器模块。这对于处理缓存到磁盘的 SPIR-V 模块以及可以提前启动 Vulkan 管道缓存的着色器预编译系统非常有用。这个扩展是由 Valve、Igalia、NVIDIA、Arm 和 Collabora 开发的，所以很快就会在一些 Linux 驱动程序中使用它，并用于 VKD3D-Proton 等。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FVulkan-Docs%2Fcommit%2F080f66a96b61419b8663872d6cab6ce68a3123e8" target="_blank">通过 Vulkan-Docs</a> 了解有关 Vulkan 1.3.219 更新的更多详细信息。</p>
                                        </div>
                                      
</div>
            