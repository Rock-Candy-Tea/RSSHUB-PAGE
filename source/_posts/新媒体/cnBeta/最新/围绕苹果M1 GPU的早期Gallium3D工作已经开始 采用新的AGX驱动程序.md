
---
title: '围绕苹果M1 GPU的早期Gallium3D工作已经开始 采用新的AGX驱动程序'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0503/312e646b46a46f5.png'
author: cnBeta
comments: false
date: Sun, 02 May 2021 23:50:09 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0503/312e646b46a46f5.png'
---

<div>   
<strong>Alyssa Rosenzweig正在继续她的逆向工程和理解苹果M1 GPU的工作，最终目标是为Linux上的苹果M1 GPU编写开源的OpenGL和Vulkan支持。</strong>上个月，她开始了苹果M1图形编译器的早期阶段，开始用迄今已逆向工程的信息处理着色器。<br>
<p>她是最早一批开始为<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>M1开发早期的Gallium3D驱动程序，并开始关注OpenGL 2.1和OpenGL ES 2.0规范。</p><p>现在的状态是，Gallium3D的部分代码已经可以处理苹果M1上的glxgears和一些glmark2场景。事实上，今天她向内核打开了一个合并请求，作为这个
"AGX"驱动的初始推送。AGX Gallium3D驱动最初是基于noop Gallium3D驱动，其中一些代码来自于针对Arm
Mali的Panfrost Gallium3D驱动的工作。</p><p><a href="https://static.cnbetacdn.com/article/2021/0503/312e646b46a46f5.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0503/312e646b46a46f5.png" title alt="3J8&#125;&#123;VS&#123;DSDLTA&#125;VFTQQ_NL.png" referrerpolicy="no-referrer"></a></p><p>虽然苹果M1图形处理器已经删除了一些苹果Metal API不需要的遗留功能，但对于仍然被GPU支持但不被Metal使用的功能，还是发现了一些未记录的功能。索引缓冲区和原始类型是苹果M1图形处理器为能够支持旧的API而保留的一些功能。</p><p>围绕苹果M1
GPU的最新反向工程工作可以通过Alyssa的博客找到，且看上去正在取得进展，"AGX"Gallium3D驱动能够早期支持苹果M1的基本OpenGL处理，重点是OpenGL
2 / GLES2。但仍有待编写的是用于M1
GPU的Linux内核DRM驱动程序，显然，Vulkan驱动程序对2021年及以后的图形技术世界都是很重要的。</p><p><strong>了解更多：</strong></p><p><a href="https://rosenzweig.io/blog/asahi-gpu-part-4.html" _src="https://rosenzweig.io/blog/asahi-gpu-part-4.html" target="_blank">https://rosenzweig.io/blog/asahi-gpu-part-4.html</a><br></p>   
</div>
            