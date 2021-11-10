
---
title: 'XWayland 21.1.3 发布，支持 NVIDIA 495 驱动 GBM'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1110/065549_MXqh_2720166.png'
author: 开源中国
comments: false
date: Wed, 10 Nov 2021 07:07:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1110/065549_MXqh_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#121212">XWayland 21.1.3 已发布，虽然这只是小版本更新，不过增加了</span>对使用 NVIDIA 新专有驱动程序的支持，该驱动程序支持 GBM API 以增强其对 Wayland 的支持。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/1110/065549_MXqh_2720166.png" referrerpolicy="no-referrer"></p> 
<p>XWayland 21.1.3 的主要特性是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.phoronix.com%2Fscan.php%3Fpage%3Dnews_item%26px%3DXWayland-21.1.3-RC" target="_blank">支持 NVIDIA GBM 后端</a>。该代码现在支持根据后端名称设置 GLVND 库。此外，NVIDIA 还修复了使用 EGL_LINUX_DMA_BUF_EXT 创建 GBM 缓冲区对象 EGLImages 的问题。</p> 
<p>除了 NVIDIA GBM 支持，XWayland 21.1.3 的其他更新内容是基本的错误修复。</p> 
<p>10 月初，NVIDIA 发布了 495 Linux beta 测试版驱动，引入了期待已久的通用缓冲区管理器(Generic Buffer Manager API) API 支持，以改进 Wayland 支持，以及与不支持 EGLStreams 的合成器兼容，这是 NVIDIA 长期以来的首选方法。10 月底，他们发布了 NVIDIA 495.44 Linux 驱动程序，现在已经稳定，并带有 GBM 支持。因此，这个最新的驱动程序与今天的 XWayland 21.1.3 版本相搭配，对 Linux 游戏玩家来说是个好消息。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.x.org%2Farchives%2Fxorg%2F2021-November%2F060808.html" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            