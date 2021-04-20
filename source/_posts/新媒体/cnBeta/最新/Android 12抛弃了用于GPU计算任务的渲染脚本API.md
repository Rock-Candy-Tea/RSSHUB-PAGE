
---
title: 'Android 12抛弃了用于GPU计算任务的渲染脚本API'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0420/bbac61962827a4c.png'
author: cnBeta
comments: false
date: Tue, 20 Apr 2021 07:58:19 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0420/bbac61962827a4c.png'
---

<div>   
<strong>早在 Android 3.0（Honeycomb）时代，谷歌就引入了 RenderScript API，以便开发者能够在 CPU / GPU 上运行高性能工作负载，而无需借助 NDK 或 GPU 专用型 API 。</strong>然而随着 OpenCL GPU 计算、Vulkan API 的引入、以及在 Android SDK 和 NDK 代码间共享位图硬件缓冲区等改进，谷歌已决定在 Android 12 中弃用历史悠久的渲染脚本 API 。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/0420/bbac61962827a4c.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://android-developers.googleblog.com/2021/04/android-gpu-compute-going-forward.html" target="_self">Android DevBlog</a>）</p><p>谷歌在 Android 开发者博客中提到，其已不建议将 RenderScript 用于对性能需求至关重要的任务，并转向可在 GPU 硬件层级上高效运作、且具有出色的跨平台体验的 Vulkan API 。</p><p>在谷歌提供的一个示例应用中，可显著知晓 RenderScript 和与之等效的 Vulkan API 的运行差异。不过对于那些仍为旧设备提供支撑的开发者来说，他们也将不得不维护两套代码方案。</p><p>最后，对于将 RenderScript 用于模糊等高性能图像处理功能集的应用，谷歌提供了一个 Android 库来代替大多数不再被推荐使用的 Intrinsics 函数。</p><p>尽管这些 API 仍可继续在 Android 12 上运行，但谷歌表示，开发者会在尝试编译 RenderScript 代码时收到相关警告。</p>   
</div>
            