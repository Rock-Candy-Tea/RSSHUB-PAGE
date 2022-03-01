
---
title: 'Windows8的开发者曾使用ASCII猫图当报错信息'
categories: 
 - 图片
 - 煎蛋
 - 首页
headimg: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom'
author: 煎蛋
comments: false
date: Sun, 27 Feb 2022 10:08:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom'
---

<div>   
<blockquote><p>|Good Night Moon!</p></blockquote><img src="https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom" referrerpolicy="no-referrer"><p>Windows 8平板电脑在显示和交互上应用了层的概念，每层堆叠在下一个层上。最基础的层是开始图层和应用层：如果您使用应用程序，则应用层占据全屏幕。如果您点“开始”，则开始图层覆盖应用层。当最后一个应用程序退出，则自动进入开始层。所以始终应该有一个全屏幕层。</p>
<p>在开发期间，当然，不可避免地会出错，既不显示开始层也没有应用层，导致黑屏。</p>
<p>现在，黑屏可以有多种原因。视频驱动程序崩溃；视频驱动程序正常工作，但是Compositor已崩溃，因此没有任何内容给视频驱动；或者Compositor可能正常工作，但shell已经崩溃了，因此Compositor没有东西可以呈现；或者shell可以运行，但它忘了在屏幕上放置东西。</p>
<p>对于最后一个情况，Windows 8 shell项目组创建了一个在所有其他图层下面的后备层。如果没有其他图层存在，那么至少您还有一个窗口。在早期调试版本中，窗口是猫的ASCII绘图。这样，如果你看到了猫，你就知道哪里出了问题：shell正在运行，但忘了在屏幕上放置东西。</p>
<p><strong>为什么是猫？</strong></p>
<p>我猜那个窗口的开发人员喜欢猫。</p>
<p>事实上，开发人员非常喜欢猫，他们有一系列猫图。在System Startup时，他们将第一个猫图片放到了窗口上，再次崩溃时，会循环到下一张猫图。每次猫喵喵一句话，合起来是一段问候？</p>
<p>在实践中，ASCII猫从未有机会完整发言，因为很少会连续因同一问题崩溃9次。</p>
<blockquote class="wp-embedded-content" data-secret="4OxrjOLrAS"><p><a href="https://devblogs.microsoft.com/oldnewthing/20220208-00/?p=106232">The cats sitting on a fence in early builds of Windows 8</a></p></blockquote>
<p><iframe title="“The cats sitting on a fence in early builds of Windows 8” — The Old New Thing" class="wp-embedded-content" sandbox="allow-scripts" security="restricted" style="position: absolute; clip: rect(1px, 1px, 1px, 1px);" src="https://devblogs.microsoft.com/oldnewthing/20220208-00/?p=106232/embed#?secret=4OxrjOLrAS" data-secret="4OxrjOLrAS" width="500" height="282" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe> </p>
<p>因为ASCII占用内存，Windows 性能团队后来要求开发团队移除了猫图像。</p>  
</div>
            