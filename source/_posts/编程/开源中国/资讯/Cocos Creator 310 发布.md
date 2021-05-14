
---
title: 'Cocos Creator 3.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-55d053f08cfbcd1cfe538fe434f87fbc754.JPEG'
author: 开源中国
comments: false
date: Fri, 14 May 2021 07:18:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-55d053f08cfbcd1cfe538fe434f87fbc754.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Cocos Creator 3.1 现已发布。Creator 3.0 统一了 2D 与 3D 的开发工作流，兼顾了轻量与重度游戏的开发体验，融合了几乎所有 Creator 2.x 与 Creator 3D 1.x 版本的功能。而 3.1 与 3.0 版本相比，增加了许多新功能，各方面性能也得到了优化。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>添加了延迟渲染管道，用户可以在项目设置中选择延迟渲染管道：</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-55d053f08cfbcd1cfe538fe434f87fbc754.JPEG" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>引入多线程渲染架构。Creator 在 v3.1中初步将传统的单线程架构拆分为两个主线程，一个是渲染线程，一个是设备线程。除了主线程的拆分，Creator 还将命令缓冲区的提交过程并行化，以加快渲染效率。多线程的渲染架构图如下：</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1140059861274f7c60d2c8f26ed860cdd89.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>增加了 PhysX 物理支持，目前支持除 Android x86 以外的原生平台，在 iOS上 的性能提升超过100%（如果需要在网络平台上预览，可以参考 example-3d 中的 physics-3d 项目，主要内容在预览-模板文件夹中修改）。</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-39ac6dda0548d850be84237b7d1ab781e94.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>编辑器现在支持骨骼八面体显示，用户可以直观地看到模型骨骼的分布状态。</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6a96f1e999683681d39000c668814e36578.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>支持在 FBX/glTF 资源的检查器上预览动画。</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6b42799ccba13ad108a25f3edd46ef8ca50.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>更新了曲线编辑器，支持分别编辑左、右斜率，并支持直接显示曲线的循环模式。</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b3ec823bae2c876abd9020d9ca4a9920d31.png" referrerpolicy="no-referrer"></p> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdiscuss.cocos2d-x.org%2Ft%2Fcocos-creator-3-1-0-released%2F53555" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            