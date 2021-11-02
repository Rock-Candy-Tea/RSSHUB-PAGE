
---
title: '提升性能、降低功耗：Firefox 94开始在Linux上启用EGL后端'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1102/3f7c41d6e6b3312.png'
author: cnBeta
comments: false
date: Tue, 02 Nov 2021 06:01:19 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1102/3f7c41d6e6b3312.png'
---

<div>   
<strong>Mozilla Gfx 团队刚刚在一篇博客文章中宣布，从 Firefox 94 开始，他们将在 Linux 桌面客户端上引入 EGL 后端和配套的图形驱动支持。</strong>据悉，EGL 不仅能够提升性能、降低功耗，还可以带来其它一些益处。此前 Firefox 开发团队更倾向于在 Linux 上启用 GLX 而非 EGL，但在稳定了一段时间之后，Mozilla 终于有了更充分的利用去使用它。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1102/3f7c41d6e6b3312.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Firefox 的 EGL 支持，起初是为了 Android 平台而启用的。</p><p>Mozilla 指出，Firefox 的 EGL 代码，不仅仅受益于 OpenGL ES 的过程改进。结合 Firefox 的 DMA-BUF 支持，其已实现了包括“零拷贝”（zero-copy）在内的更多优势。</p><p>此外还有 Wayland 支持的持续改进，随着 Wayland 变得相当普及（且同样使用 EGL），Firefox 团队也终于将开发精力从 GLX 迁移到了 GLX 。</p><blockquote><p>至于即将于本周到来的 Firefox 94，它将在 Mesa 21.x（或更新版本）的驱动程序上运行时启用 EGL 后端。</p><p>一旦英伟达 495 系列驱动程序被更广泛地采用，其闭源驱动程序上的 Firefox EGL 也将成为默认设置。</p><p>另外只有最近刚转入测试版的 NVIDIA 495 系列驱动程序，才包含了 Firefox 所需的 EGL_NV_robustness_video_memory_purge 扩展。</p></blockquote><p>在 Linux 桌面上使用 EGL 的话，Firefox 有望达成更好的 WebGL 性能 —— 因为它支持刷新部分屏幕内容（update / damage）、减少代码错误、以及默认的硬件视频解码，从而降低资源和能源开销。</p>   
</div>
            