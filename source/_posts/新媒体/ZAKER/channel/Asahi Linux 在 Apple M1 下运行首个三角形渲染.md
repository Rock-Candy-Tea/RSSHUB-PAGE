
---
title: 'Asahi Linux 在 Apple M1 下运行首个三角形渲染'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202206/62a1973a8e9f091def639698_1024.jpg'
author: ZAKER
comments: false
date: Thu, 09 Jun 2022 02:30:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202206/62a1973a8e9f091def639698_1024.jpg'
---

<div>   
<p>整理 | 彭慧中 责编 | 屠敏</p><p>虽然针对苹果 M1 的 Mesa （开放源代码库 Mesa 是一个纯基于软件的图形 API，它的代码兼容于 OpenGL）代码已经取得了进展，可以运行像 glmark2 （开源的 glmark2 是对 OpenGL 2.0 和 ES 2.0 的基准测试程序）这样的基本测试，但这历来都是在 macOS 及其内核驱动下运行的。本周，Asahi Linux 团队庆祝了他们首次在 M1 芯片上的 Linux 系统下使用完全开源的驱动程序堆栈运行的三角形渲染。</p><p>图源推特</p><p>自去年以来，Asahi Linux 的开发者们在 Alyssa Rosenzweig 的领导下，在 Mesa 中已经有了早期的苹果 M1 代码，这得益于图形工具逆向工程的努力。大部分早期的 OpenGL 驱动工作都是在 macOS 下进行的，苹果也没有公布任何规格或其他平台的驱动。另外，对于 Gallium3D/Mesa 的工作，例如让着色器编译器工作并将结果与 macOS 驱动程序堆栈进行比较是很有用的，而在得到 DRM/KMS Linux 驱动之前，能够利用 macOS 的内核驱动当然也是再好不过的了。</p><p>对于目前使用 Asahi Linux 的用户来说，只有一个基本的帧缓冲器驱动程序，而 OpenGL 加速只是利用 LLVMpipe。但是本周，一直致力于研究最新的实验性 Linux 内核和 Mesa 代码的 Asahi 公司的开发人员已经成功地用这个完全开源的驱动程序堆栈渲染了他们的第一个三角形。 ( 更新：事实证明，这第一个三角形似乎是来自他们基于 m1n1 的环境，而不是一个合适的 Linux 驱动程序堆栈。 ) </p><p>虽然还需要一段时间才能期望在具有现代图形功能和良好性能的 Apple M1 硬件上玩 OpenGL 游戏，但 Asahi Linux 团队正在取得不错的进展，未来希望有一个不错的开源 Vulkan 驱动程序堆栈。</p><p>推特上不少用户也表示对这样的进展喜闻乐见，纷纷感叹 Asahi Linux 团队进展之神速。正如用户 River Wang 所说：" 在不远的将来，我可以看到基于苹果芯片的游戏潜力被完全释放，而这正是因为 Linux，而不是 macOS，也不是 Windows。"</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202206/62a1973a8e9f091def639698_1024.jpg" data-height="218" data-width="926" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202206/62a1973a8e9f091def639698_1024.jpg" referrerpolicy="no-referrer"></div></div><p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            