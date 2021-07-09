
---
title: '苹果框架学习（二） Metal（上）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=3316'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 22:03:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=3316'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">文章目录</h3>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%23_Metal_1" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#_Metal_1" ref="nofollow noopener noreferrer">苹果框架学习（二） Metal</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%23Metal_3" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#Metal_3" ref="nofollow noopener noreferrer">Metal简介</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%231_Essentials_21" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#1_Essentials_21" ref="nofollow noopener noreferrer">1. Essentials</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2311__22" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#11__22" ref="nofollow noopener noreferrer">1.1 基本任务和概念</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2312_OpenGLMetal_26" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#12_OpenGLMetal_26" ref="nofollow noopener noreferrer">1.2 将OpenGL代码迁移到Metal</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2313_MetalArm_30" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#13_MetalArm_30" ref="nofollow noopener noreferrer">1.3 将您的Metal代码移植到苹果Arm芯片</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%232_GPUs_33" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#2_GPUs_33" ref="nofollow noopener noreferrer">2. GPUs</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2321_GPU_36" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#21_GPU_36" ref="nofollow noopener noreferrer">2.1 获取默认GPU</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2322_macOSGPU_42" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#22_macOSGPU_42" ref="nofollow noopener noreferrer">2.2 macOS中的GPU选择</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2323_protocol_MTLDevice_46" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#23_protocol_MTLDevice_46" ref="nofollow noopener noreferrer">2.3 protocol MTLDevice</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2324_GPU__54" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#24_GPU__54" ref="nofollow noopener noreferrer">2.4 GPU 特征</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%233_Command_Setup_91" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#3_Command_Setup_91" ref="nofollow noopener noreferrer">3. Command Setup</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2331__94" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#31__94" ref="nofollow noopener noreferrer">3.1 建立一个命令结构</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2332_Metal_98" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#32_Metal_98" ref="nofollow noopener noreferrer">3.2 准备你的Metal应用程序在后台运行</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2333_protocol_MTLCommandQueue_102" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#33_protocol_MTLCommandQueue_102" ref="nofollow noopener noreferrer">3.3 protocol MTLCommandQueue</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2334_protocol_MTLCommandBuffer_107" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#34_protocol_MTLCommandBuffer_107" ref="nofollow noopener noreferrer">3.4 protocol MTLCommandBuffer</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2335_protocol_MTLCommandEncoder_111" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#35_protocol_MTLCommandEncoder_111" ref="nofollow noopener noreferrer">3.5 protocol MTLCommandEncoder</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2336__115" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#36__115" ref="nofollow noopener noreferrer">3.6 计数器采样</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%234__118" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#4__118" ref="nofollow noopener noreferrer">4. 并行计算</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%235__143" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#5__143" ref="nofollow noopener noreferrer">5. 射线跟踪</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%236__184" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#6__184" ref="nofollow noopener noreferrer">6. 渲染</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%237_Presentation_216" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#7_Presentation_216" ref="nofollow noopener noreferrer">7. Presentation</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%238_Shaders_222" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#8_Shaders_222" ref="nofollow noopener noreferrer">8. Shaders</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%239_Resources_231" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#9_Resources_231" ref="nofollow noopener noreferrer">9. Resources</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2310__278" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#10__278" ref="nofollow noopener noreferrer">10. 对象大小调整和定位</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2311__296" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#11__296" ref="nofollow noopener noreferrer">11. 填充向量和矩阵</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2312_Time_302" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#12_Time_302" ref="nofollow noopener noreferrer">12. Time</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2313_Tools_305" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#13_Tools_305" ref="nofollow noopener noreferrer">13. Tools</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2314_GPU_325" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#14_GPU_325" ref="nofollow noopener noreferrer">14. GPU编程技术</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2315_Reference_348" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#15_Reference_348" ref="nofollow noopener noreferrer">15. Reference</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501%2316_Related_Documentation_355" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501#16_Related_Documentation_355" ref="nofollow noopener noreferrer">16. Related Documentation</a></p>
</li>
</ul>
<h1 data-id="heading-1">苹果框架学习（二） Metal</h1>
<h1 data-id="heading-2">Metal简介</h1>
<p>Metal是渲染高级3D图形和执行数据并行计算使用图形处理器。</p>
<p>图形处理器(gpu)被设计用来快速渲染图形和执行数据并行计算。当您需要直接与设备上可用的gpu通信时，请使用Metal框架。渲染复杂场景或执行高级科学计算的应用程序可以利用这种能力实现最大的性能。这些应用程序包括:</p>
<ul>
<li>
<p>渲染复杂3D环境的游戏</p>
</li>
<li>
<p>视频处理应用程序，比如Final Cut Pro</p>
</li>
<li>
<p>数据处理应用程序，比如那些用于进行科学研究的应用程序</p>
</li>
</ul>
<p>Metal与其他补充其功能的框架携手工作。使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetalkit" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metalkit" ref="nofollow noopener noreferrer">MetalKit</a>可以简化将Metal内容显示在屏幕上的任务。使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetalperformanceshaders" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metalperformanceshaders" ref="nofollow noopener noreferrer">Metal Performance着色器</a>来实现自定义渲染函数或利用现有函数的大型库。</p>
<p>许多高级Apple框架都构建在Metal之上，以利用其性能，包括<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fcoreimage" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/coreimage" ref="nofollow noopener noreferrer">Core Image</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fspritekit" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/spritekit" ref="nofollow noopener noreferrer">SpriteKit</a>和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fscenekit" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/scenekit" ref="nofollow noopener noreferrer">SceneKit</a>。使用这些高级框架之一可以避免您接触到GPU编程的细节，但是编写定制的Metal代码可以使您获得最高水平的性能。</p>
<h1 data-id="heading-3">1. Essentials</h1>
<h2 data-id="heading-4">1.1 基本任务和概念</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fbasic_tasks_and_concepts" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/basic_tasks_and_concepts" ref="nofollow noopener noreferrer">基本任务和概念</a><br>
通过一系列示例代码项目熟悉Metal</p>
<h2 data-id="heading-5">1.2 将OpenGL代码迁移到Metal</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmigrating_opengl_code_to_metal" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/migrating_opengl_code_to_metal" ref="nofollow noopener noreferrer">将OpenGL代码迁移到Metal</a><br>
用Metal替换应用程序中已弃用的OpenGL代码。</p>
<h2 data-id="heading-6">1.3 将您的Metal代码移植到苹果Arm芯片</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fporting_your_metal_code_to_apple_silicon" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/porting_your_metal_code_to_apple_silicon" ref="nofollow noopener noreferrer">将您的Metal代码移植到苹果Arm芯片</a><br>
创建一个版本的Metal应用程序，运行在苹果硅和英特尔的Mac电脑上。</p>
<h1 data-id="heading-7">2. GPUs</h1>
<p>在运行时访问GPU设备。图形处理器是Metal开发的基础。</p>
<h2 data-id="heading-8">2.1 获取默认GPU</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fgetting_the_default_gpu" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/getting_the_default_gpu" ref="nofollow noopener noreferrer">获取默认GPU</a><br>
选择要在其上运行Metal代码的系统默认GPU设备。</p>
<p>要使用Metal框架，首先要获得一个GPU设备。应用程序与Metal交互所需的所有对象都来自一个在运行时获得的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmtldevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/mtldevice" ref="nofollow noopener noreferrer">MTLDevice</a>。iOS和tvOS设备只有一个GPU可以通过调用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">MTLCreateSystemDefaultDevice()</a>来访问:</p>
<h2 data-id="heading-9">2.2 macOS中的GPU选择</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">macOS中的GPU选择</a><br>
通过考虑GPU能力、功率或性能特征，选择一个或多个GPU来运行您的Metal代码。</p>
<h2 data-id="heading-10">2.3 protocol MTLDevice</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmtldevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/mtldevice" ref="nofollow noopener noreferrer">protocol MTLDevice</a><br>
图形处理器的Metal接口，用于绘制图形或进行并行计算。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmtldevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/mtldevice" ref="nofollow noopener noreferrer">MTLDevice</a>协议定义了到GPU的接口。您可以查询<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmtldevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/mtldevice" ref="nofollow noopener noreferrer">MTLDevice</a>为您的Metal应用程序提供的独特功能，并使用MTLDevice发出所有的Metal命令。不要自己执行这个协议;相反，在iOS或tvOS中，在运行时使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2F1433401-mtlcreatesystemdefaultdevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/1433401-mtlcreatesystemdefaultdevice" ref="nofollow noopener noreferrer">MTLCreateSystemDefaultDevice()</a> 从系统请求GPU;在macOS中，使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2F2928189-mtlcopyalldeviceswithobserver" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/2928189-mtlcopyalldeviceswithobserver" ref="nofollow noopener noreferrer">MTLCopyAllDevicesWithObserver(handler:)</a>获取可用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmtldevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/mtldevice" ref="nofollow noopener noreferrer">MTLDevice</a>对象的列表。关于选择正确的GPU(s)的完整讨论，请参见获取默认GPU。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmtldevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/mtldevice" ref="nofollow noopener noreferrer">MTLDevice</a>对象是在Metal中执行任何操作的go-to对象，因此应用程序与之交互的所有Metal对象都来自于运行时获得的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmtldevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/mtldevice" ref="nofollow noopener noreferrer">MTLDevice</a>实例。mtldevice创建的对象开销大但持久;其中许多对象被设计为初始化一次，并在应用程序的整个生命周期中重用。然而，这些对象特定于发出它们的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmtldevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/mtldevice" ref="nofollow noopener noreferrer">MTLDevice</a>。如果使用多个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmtldevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/mtldevice" ref="nofollow noopener noreferrer">MTLDevice</a>实例或希望从一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmtldevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/mtldevice" ref="nofollow noopener noreferrer">MTLDevice</a>切换到另一个MTLDevice，则需要为每个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fmtldevice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/mtldevice" ref="nofollow noopener noreferrer">MTLDevice</a>创建一组单独的对象。</p>
<h2 data-id="heading-11">2.4 GPU 特征</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fgpu_features" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/gpu_features" ref="nofollow noopener noreferrer">GPU 特征</a><br>
查找特定GPU家族的特征信息。</p>
<p><strong>Metal Feature Sets</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fgpu_features%2Fusing_metal_feature_set_tables" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/gpu_features/using_metal_feature_set_tables" ref="nofollow noopener noreferrer">使用Metal特征设置表</a><br>
根据Metal软件版本和GPU家族查找功能可用性。<br>
Metal中功能的可用性是由GPU支持的Metal软件版本和家族功能集的组合决定的。Metal功能集表提供了功能的可用性，特定的数值限制，以及对不同GPU家族的像素格式支持。</p>
<p><strong>Apple GPU Families</strong><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fmetal%2Fgpu_features%2Funderstanding_gpu_family_4" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/metal/gpu_features/understanding_gpu_family_4" ref="nofollow noopener noreferrer">理解GPU家族4</a><br>
了解A11的特性，包括光栅顺序组、平铺着色器和图像块。</p>
<p>GPU家族4描述了A11芯片和苹果设计的图形处理单元(GPU)架构带来的新特性和性能提升。</p>
<p>iOS和tvOS设备中的gpu实现了一种称为基于tile的延迟渲染(TBDR)的渲染技术，以优化性能和功耗。在传统的即时模式(IM)渲染器中，当一个三角形被提交给GPU处理时，它会立即被渲染到设备内存中。即使三角形被后来提交给GPU的其他原语遮挡，三角形也会被光栅化和片段函数处理。</p>
<p><strong>基于Tile延迟渲染</strong><br>
TBDR对IM架构做了一些重要的改变，在所有的原语都提交之后处理场景。屏幕被分割成小块，分别进行处理。所有几何体的交叉块被同时处理，并且遮挡碎片被丢弃在光栅化和碎片着色阶段之前。块被渲染到GPU上的快速本地内存中，只有在渲染完成后才被写到设备内存中。</p>
<p>TBDR允许顶点和片段阶段异步运行——比IM提供了显著的性能改进。当运行渲染通道的片段阶段时，硬件并行地执行未来渲染通道的顶点阶段。顶点阶段通常大量使用固定功能硬件，而片段阶段使用数学和带宽。完全重叠它们允许设备同时使用GPU上的所有硬件块。</p>
<p>TBDR使用的平铺内存有三个重要特征。首先，着色器核心和瓷砖存储器之间的带宽比GPU和设备存储器之间的带宽高很多倍，并比例与着色器核心的数量。其次，访问瓷砖内存的内存访问延迟比访问设备内存的延迟低很多倍。最后，平铺内存比设备内存消耗更少的能量。</p>
<p>在基于A7到a10的设备上，Metal没有明确地描述这种基于瓷砖的架构;相反，您使用它来为底层实现提供提示。例如，加载和存储操作控制哪些数据被加载到本地内存以及哪些数据被写到设备内存中。类似地，无内存缓冲区指定仅在渲染过程中使用的每像素中间数据;在实践中，这些数据存储在GPU的快速本地内存中的一个tile中。</p>
<p><strong>A11 GPU上的Metal2</strong></p>
<p>在A11中，苹果设计的GPU提供了几个显著增强TBDR的功能。这些特性是通过额外的Metal 2 api提供的，并允许您的应用程序和游戏实现新的性能和功能级别。</p>
<p>这些特性包括imageblock、平铺阴影、光栅顺序组和imageblock样本覆盖率控制。A11 GPU上的Metal 2也提高了碎片丢弃的性能。</p>
<p>总的来说，这些特性提供了对内存布局的更好控制和对存储在tile中的数据的访问，并提供了更细粒度的同步以保持GPU上的更多工作。最终结果是，与以前相比，您可以在一次渲染传递中执行更广泛的计算，并将计算保持在快速的本地内存中。</p>
<p>在A11上的Metal 2还简化了技术的实现，如地下散射、顺序无关的透明度和基于瓷砖的照明算法。</p>
<h1 data-id="heading-12">3. Command Setup</h1>
<p>建立基础设施，以执行您的自定义代码的GPU。</p>
<h2 data-id="heading-13">3.1 建立一个命令结构</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">建立一个命令结构</a><br>
了解Metal如何在GPU上执行命令。</p>
<h2 data-id="heading-14">3.2 准备你的Metal应用程序在后台运行</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">准备你的Metal应用程序在后台运行</a><br>
通过暂停未来的GPU使用和确保之前的工作安排，准备你的应用移到后台</p>
<h2 data-id="heading-15">3.3 protocol MTLCommandQueue</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">MTLCommandQueue</a><br>
一种为GPU执行组织命令缓冲区的队列。</p>
<h2 data-id="heading-16">3.4 protocol MTLCommandBuffer</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">MTLCommandBuffer</a><br>
为GPU存储要执行的编码命令的容器。</p>
<h2 data-id="heading-17">3.5 protocol MTLCommandEncoder</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108258874%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108258874?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">MTLCommandEncoder</a><br>
一种将GPU命令写入命令缓冲区的编码器。</p>
<h2 data-id="heading-18">3.6 计数器采样</h2>
<p>计数器采样<br>
检索关于GPU如何执行你的命令的信息。</p>
<h1 data-id="heading-19">4. 并行计算</h1>
<p>Process arbitrary calculations in parallel on the GPU.</p>
<p>Processing a Texture in a Compute Function<br>
Perform data-parallel computations on texture data.</p>
<p>Creating Threads and Threadgroups<br>
Learn how Metal organizes compute-processing workloads.</p>
<p>Calculating Threadgroup and Grid Sizes<br>
Calculate the optimum sizes for threadgroups and grids when dispatching compute-processing workloads.</p>
<p>class MTLComputePipelineDescriptor<br>
An object used to customize how a new compute pipeline state object is compiled.</p>
<p>protocol MTLComputePipelineState<br>
An object that contains a compiled compute pipeline.</p>
<p>class MTLComputePassDescriptor<br>
A configuration for a compute pass, used to create a compute command encoder.</p>
<p>protocol MTLComputeCommandEncoder<br>
An object used to encode commands in a compute pass.</p>
<h1 data-id="heading-20">5. 射线跟踪</h1>
<p>Accelerating Ray Tracing Using Metal<br>
Implement ray-traced rendering using GPU-based parallel processing</p>
<p>protocol MTLAccelerationStructure<br>
A collection of model data, organized to allow for GPU-accelerated intersection of rays with the model.</p>
<p>class MTLAccelerationStructureDescriptor<br>
A base class for classes that define the configuration for a new acceleraton structure.</p>
<p>class MTLAccelerationStructureGeometryDescriptor<br>
A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.</p>
<p>class MTLAccelerationStructureBoundingBoxGeometryDescriptor<br>
A description of a list of bounding boxes to turn into an acceleration structure.</p>
<p>class MTLAccelerationStructureTriangleGeometryDescriptor A description of a list of triangle primitives to turn into an acceleration structure. </p>
<p>class MTLPrimitiveAccelerationStructureDescriptor<br>
A description of an acceleration structure that contains geometry primitives.</p>
<p>class MTLInstanceAccelerationStructureDescriptor A description of an acceleration structure built from instances of primitive acceleration structures. </p>
<p>struct MTLAccelerationStructureInstanceDescriptor<br>
A description of an instance in an instanced geometry acceleration structure.</p>
<p>protocol MTLIntersectionFunctionTable<br>
A table of visible functions that Metal calls to perform ray-tracing intersection tests.</p>
<p>class MTLIntersectionFunctionTableDescriptor<br>
A description that describes how to create an intersection function table.</p>
<p>class MTLIntersectionFunctionDescriptor<br>
A description of a visible function that performs an intersection test.</p>
<p>protocol MTLAccelerationStructureCommandEncoder<br>
A object used to encode commands that build or refit acceleration structures.</p>
<p><strong>由于文章篇幅有限只能点到即止地介绍当前一些工作成果和思考</strong></p>
<h3 data-id="heading-21">各个  Metal 还有一些新的方向在探索，如果你对 iOS 底层原理、架构设计、构建系统、如何面试有兴趣了解，你也可以私信我及时获取最新资料以及面试相关资料。如果你有什么意见和建议欢迎给我留言！</h3>
<p><strong>喜欢iOS的小伙伴可以关注我，一起学习交流！！！</strong></p>
<p>**原文链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755" title="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755" target="_blank">blog.csdn.net/kyl28288954…</a><br>
**</p></div>  
</div>
            