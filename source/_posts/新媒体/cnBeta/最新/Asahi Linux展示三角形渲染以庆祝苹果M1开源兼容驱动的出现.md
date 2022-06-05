
---
title: 'Asahi Linux展示三角形渲染以庆祝苹果M1开源兼容驱动的出现'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0605/6feb1124b48990f.png'
author: cnBeta
comments: false
date: Sun, 05 Jun 2022 00:11:28 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0605/6feb1124b48990f.png'
---

<div>   
虽然针对苹果M1的Mesa代码在运行基本测试（如glmark2）方面取得了进展，但这一直是在macOS及其内核驱动下运行的一项努力。本周，Asahi Linux团队庆祝了他们首次使用完全开源的驱动栈运行的三角形渲染。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0605/6feb1124b48990f.png" title alt="图片.png" referrerpolicy="no-referrer"><br></p><p>自去年以来，Asahi Linux的开发人员在Mesa中已经有了早期的<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>M1代码，并由Alyssa Rosenzweig领导这一图形逆向工程工作。大部分早期的OpenGL驱动工作都是在macOS下进行的，因为那里发生的逆向工程工作，苹果没有公布任何规格或其他平台的驱动。另外对于Gallium3D/Mesa的工作，如让着色器编译器工作并将结果与macOS驱动栈进行比较，而在得到DRM/KMS Linux驱动之前，能够利用macOS的内核驱动当然是很有用的。</p><p><a href="https://static.cnbetacdn.com/article/2022/0605/5fdb53e0a066ec1.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0605/5fdb53e0a066ec1.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p><p>对于今天使用Asahi Linux的用户来说，图形加速方面的状况比较可怜，只有一个基本的帧缓冲器驱动，OpenGL加速只能利用LLVMpipe。但是本周，随着Asahi的开发人员正在研究最新的实验性Linux内核和Mesa代码，他们现在已经成功地用这个完全开源的驱动堆栈渲染了他们的第一个三角形。与之前的成就不同，不依赖于现有的macOS内核驱动。(不过事实证明这第一个三角形似乎是来自他们的基于m1n1的环境，还算不上是一个合适的Linux驱动栈，但这仍旧是一个好消息)。</p><p>虽然还需要一段时间，我们才能期望在苹果M1硬件上玩具有现代GL功能和良好性能的OpenGL游戏，但Asahi Linux团队正在取得不错的进展，未来希望在适当的时候也能有一个不错的开源Vulkan驱动栈。</p>   
</div>
            