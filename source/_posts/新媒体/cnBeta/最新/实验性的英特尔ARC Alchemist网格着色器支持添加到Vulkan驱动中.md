
---
title: '实验性的英特尔ARC Alchemist网格着色器支持添加到Vulkan驱动中'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0204/2b21c680af6a498.jpg'
author: cnBeta
comments: false
date: Thu, 03 Feb 2022 23:43:43 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0204/2b21c680af6a498.jpg'
---

<div>   
最近，英特尔披露了最新的ANV Vulkan驱动，用于Linux操作系统，提供网格着色器，将在新的DG2，或ARC Alchemist独立显卡中实施。这种独特的网状阴影被认为是"实验性的"，目前仍在测试中。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0204/2b21c680af6a498.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0204/2b21c680af6a498.jpg" title alt="intel-alchemist-4k-background-1-1480x833.jpg" referrerpolicy="no-referrer"></a></p><p>新的实验性网格着色器可以扩大几何阶段的可扩展性，使其非常容易集成到引擎运行时。网格着色器可以将删减程序封装在一个单独的API调用中，这就绕过了繁琐的状态和资源设置程序。</p><p>目前，Vulkan的网格着色器使用NVIDIA的VK_NV_mesh_shader扩展为Linux工作。</p><p><img src="https://static.cnbetacdn.com/article/2022/0204/c5122fdf5d9f5f8.jpg" title alt="graph.jpg" referrerpolicy="no-referrer"></p><p><strong>英特尔在其规范中解释了这个新的扩展：</strong></p><blockquote><p>这个扩展提供了一个新的机制，允许应用程序通过可编程的网格着色生成几何基元的集合。它是现有的可编程基元着色管道的替代方案，后者依赖于通过固定函数装配器以及固定函数顶点获取来生成输入基元。</p><p>利用新的可编程着色器类型：任务和网格着色器来生成这些集合，由固定功能的基元组装和光栅化逻辑来处理。当任务和网格着色器被调度时，它们取代了核心的预栅格化阶段，包括顶点阵列属性获取、顶点着色器处理、细分化和几何着色器处理。</p></blockquote><p>去年12月，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>的Linux用户看到了实验性的网格着色被纳入该公司的Radeon RADV驱动，开发人员将其实施到Mesa 22.0中。现在，英特尔将在他们即将推出的硬件中看到这个同样的机会。AMD公司的RDNA2显卡支持网状着色器，现在英特尔将能够在他们即将推出的DG2图形硬件中纳入同样的支持。</p><p><a href="https://static.cnbetacdn.com/article/2022/0204/31cf3a13ee98620.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0204/31cf3a13ee98620.jpg" title alt="mesh-shading-740x415.jpg" referrerpolicy="no-referrer"></a></p><p>英特尔的开源驱动工程师团队已经开发了几个月的网状着色器支持。随着Mesa 22.0级别的引入，该实现变得活跃起来。</p><p>本次合并请求将提供多达13个补丁，以获得Vulkan网格着色器对Xe HP（DG2）的支持。VK_NV_mesh_shader支持隐藏在"ANV_EXPERIMENTAL_NV_MESH_SHADER"环境中，正在等待官方激活。随着英特尔ARC Alchemist的出现，在发布官方的跨厂商Vulkan网格着色器扩展之前应该不需要有长时间的等待。</p>   
</div>
            