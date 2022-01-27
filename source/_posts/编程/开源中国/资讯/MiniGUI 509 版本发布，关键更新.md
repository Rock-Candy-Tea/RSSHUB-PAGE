
---
title: 'MiniGUI 5.0.9 版本发布，关键更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-85630ea04c64c097faca5bf886605e2c7ca.png'
author: 开源中国
comments: false
date: Thu, 27 Jan 2022 10:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-85630ea04c64c097faca5bf886605e2c7ca.png'
---

<div>   
<div class="content">
                                                                                            <p>飞漫软件于 2022 年 1 月 26 日<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FUWiQ4vue2mZNQsBbfn-HWA" target="_blank">宣布</a>，正式发布 MiniGUI 5.0.9 版本。</p> 
<p>对国内开源软件的发展稍有了解的人都知道，MiniGUI 的第一个版本发布于 1999 年。MiniGUI 是中国最早的几个开源项目之一，是最具代表性的原创国产基础软件之一，经历了开源软件在国内萌芽、发展、消沉，而后在近几年随国内自主可控的春风重装上阵的整个过程。</p> 
<p>MiniGUI 5.0.9 是 MiniGUI 5.0 系列的最新缺陷修正版本。该版本的发布，意味着经过若干版本迭代后，MiniGUI 5.0 走向成熟，进入了商用推广阶段。</p> 
<p>MiniGUI 5.0 是 MiniGUI 发展中的重要里程碑版本。用一句话总结：MiniGUI 5.0 将桌面级的窗口系统功能带给了嵌入式设备。我们首先了解一下 MiniGUI 5.0 自目前业界广泛使用的 MiniGUI 3.0/3.2 版本以来的三个主要技术进步。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span style="color:#004b68"><strong>三大技术进步</strong></span></h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span><strong>1) 独立的窗口合成器</strong></span></h3> 
<p>自 MiniGUI 5.0 起，MiniGUI 的多进程模式开始支持合成图式（compositing schema）。合成图式是现代桌面操作系统和智能手机操作系统的图形及窗口系统使用的技术，其基本原理很简单：系统中所有进程创建的每一个窗口都使用独立的缓冲区来各自渲染其内容，而系统中有一个扮演合成器（compositor）角色的进程，负责将这些内容根据窗口的 Z 序以及叠加效果（如半透明、模糊等）合成在一起并最终显示在屏幕上。</p> 
<p>合成图式为窗口系统提供各种视觉效果和新奇交互效果带来了可能。在合成图式之前，大部分窗口系统使用共享缓冲区图式，通过管理和维护窗口的层叠关系以及相互之间的剪切来实现多窗口的管理。传统的共享缓冲区图式很难在多进程环境下实现不规则窗口、半透明或模糊叠加效果，而合成图式则可以轻松解决这些问题，而且还可以方便实现窗口切换时的动画效果。</p> 
<p>在不使用合成器的情形下，窗口切换时的动画效果只能作用于单个进程中的多个窗口，应用开发者要仔细编码来处理窗口切换动画的实现细节，这样，一方面让单个进程的执行逻辑变得更为复杂，程序更容易出现缺陷，另一方面无法充分利用 Linux 等通用操作系统内核提供的多进程管理能力。而有了合成器之后，每个进程只需创建窗口并在窗口中绘制，无需关心其中的内容是如何被展示到屏幕上的——这项工作由独立的合成器来完成。这样，应用开发者不必关心窗口切换动画的实现细节，于是大大简化了窗口切换动画的实现。</p> 
<p>经过几个版本的迭代，MiniGUI 5.0 的合成图式已然成熟。由飞漫软件发起的开源操作系统项目 HybridOS 以及 HybridOS Lite 均基于 MiniGUI 5.0 的合成图式。</p> 
<p>开发者可定制自己的合成器（compositor），并通过加载动态库的形式装载自定义合成器或者第三方合成器。在整个系统的不同运行阶段，甚至可以在多个合成器之间进行切换。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span><strong>2) 完整的 Unicode 支持</strong></span></h3> 
<p>在 MiniGUI 4.0 的开发中，重构了 MiniGUI 的底层字符集、编码及字体支持模块：</p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p>提供了完整的 Unicode 支持接口，符合 Unicode 12.0.0 标准及相关规范。</p> </li> 
 <li> <p>提供了用于支持复杂书写系统（如阿拉伯文、泰文、印度语、蒙文、藏文等）的相关接口，用于复杂或者混合文字的排版、字体成型和渲染。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">为支持复杂文字，在保持接口稳定性和兼容性的基础上增强了 MiniGUI 逻辑字体和设备字体的相关接口。</p> </li> 
</ol> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span><strong>3) 支持多点触摸屏以及 GPU 加速</strong></span></h3> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p>支持除键盘鼠标之外的其他输入设备，如多点触摸屏、手势、游戏杆、平板笔等。</p> </li> 
 <li> <p>新增 <span style="background-color:#ffd7d5; color:#ab1942">drm</span> 图形引擎，可通过全新的 Linux DRI/DRM 图形栈支持现代的显示卡或者 GPU，用于实现硬件加速的 2D/3D 图形渲染。</p> </li> 
 <li> <p>通过汇编代码，针对 ARM （32 及 64 位）架构提供了基于矢量运算指令的优化。</p> </li> 
</ol> 
<p>除了以上三个主要的增强之外，MiniGUI 4.0/5.0 还调整了一些底层架构，重构了一些底层模块。有兴趣的读者可以阅读完整的发布说明文档并顺手点亮 MiniGUI 仓库的星星：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>MiniGUI 5.0 系列：</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FVincentWei%2Fminigui%2Fblob%2Frel-5-0%2FRELEASE-NOTES.md" target="_blank">https://github.com/VincentWei/minigui/blob/rel-5-0/RELEASE-NOTES.md</a></p> </li> 
 <li> <p>MiniGUI 4.0 系列：</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FVincentWei%2Fminigui%2Fblob%2Frel-4-0%2FRELEASE-NOTES.md" target="_blank">https://github.com/VincentWei/minigui/blob/rel-4-0/RELEASE-NOTES.md</a></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span style="color:#004b68"><strong>MiniGUI 和 HybridOS、HVML 的关系</strong></span></h2> 
<p>简单而言，这三个项目相互独立而又相互关联。</p> 
<p>其中，MiniGUI 为嵌入式系统提供桌面级窗口系统的功能，也提供了基于 C 语言的 GUI Toolkit 库，开发者可独立使用而开发各类 GUI 应用。</p> 
<p>HybridOS 是一个针对智能设备的操作系统，架构在 Linux 内核和 MiniGUI （合成图式）之上。目前，HybridOS 中集成了飞漫增强的 hiWebKit 引擎，可使用 Web 前端技术开发图形和多媒体应用。另外，通过飞漫开发的数据总线 hiBus，应用可以和其他模块完成数据交换及功能调用。因此，相比 MiniGUI 只提供窗口管理和 GUI 功能之外，HybridOS 则提供了完整的应用开发框架以及集成系统功能的基础设施。</p> 
<p>HVML 最初是为了解决 MiniGUI 基于 C 语言的接口不利于开发者快速开发 GUI 应用这一问题而提出，最终将成为 HybridOS 的应用编程语言。然而，HVML 可以用于更加通用的场合，比如桌面应用以及云应用的开发当中。</p> 
<p>当 HVML 成熟之后，我们可以在 HybridOS 上使用 HVML 开发应用，此时，MiniGUI 是 HybridOS 的窗口系统以及图形栈的一部分；我们也可以在 Windows、macOS、Linux 桌面系统上使用 HVML 开发应用，此时，HVML 的运行时环境基于上述桌面操作系统，和 HybridOS、MiniGUI 无关。</p> 
<p>要更详细地了解 HVML 的来龙去脉以及开发进展，推荐阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fmp%2Fappmsgalbum%3F__biz%3DMzA5MTYwNTA3MA%3D%3D%26action%3Dgetalbum%26album_id%3D1996475465217245185%23wechat_redirect" target="_blank">#HVML 话题</a> 下的文章。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span style="color:#004b68"><strong>源代码包下载</strong></span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">最后，附上 MiniGUI 5.0.9 的源代码包下载页面：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.minigui.com%2Fdownload" target="_blank">http://www.minigui.com/download</a></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">亦可访问如下用于构建 MiniGUI 的仓库：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FVincentWei%2Fbuild-minigui-5.0" target="_blank">https://github.com/VincentWei/build-minigui-5.0</a></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">或者</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.fmsoft.cn%2FVincentWei%2Fbuild-minigui-5.0" target="_blank">https://gitlab.fmsoft.cn/VincentWei/build-minigui-5.0</a></p> 
<p>另外，欢迎请<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstore.fmsoft.cn%2Fcampaign%2Fdenoteoss-lt" target="_blank">点击此处</a>，赞助飞漫主持的开源项目 MiniGUI、HybridOS 和 HVML。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span style="color:#004b68"><strong>附：商标声明</strong></span></h2> 
<p>本文提到的产品、技术或者术语名称，涉及北京飞漫软件技术有限公司在中国或其他地区注册的如下商标：</p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">飛漫</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="146" src="https://oscimg.oschina.net/oscnet/up-85630ea04c64c097faca5bf886605e2c7ca.png" width="336" referrerpolicy="no-referrer"></p> 
<ol start="2" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">FMSoft</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="126" src="https://oscimg.oschina.net/oscnet/up-5eede1381e8103223211b8c482224ffcb12.png" width="334" referrerpolicy="no-referrer"></p> 
<ol start="3" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">合璧</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="140" src="https://oscimg.oschina.net/oscnet/up-56b8988b76ee9f2a50ec123f1666dd01842.png" width="294" referrerpolicy="no-referrer"><img height="140" src="https://oscimg.oschina.net/oscnet/up-25343d8790920e5c8a9b2dd4cbde78076a5.png" width="283" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="140" src="https://oscimg.oschina.net/oscnet/up-acb428bf8d1fcc9b2dba8aaf69b38d866aa.png" width="268" referrerpolicy="no-referrer"></p> 
<ol start="4" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">HybridOS</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="164" src="https://oscimg.oschina.net/oscnet/up-edb847880d04ffcf3796451d1681002ac6e.png" width="316" referrerpolicy="no-referrer"></p> 
<ol start="5" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">HybridRun</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="116" src="https://oscimg.oschina.net/oscnet/up-87aadd2f4e8ddb1fe9a2b5e9cf71c95d7bb.png" width="340" referrerpolicy="no-referrer"></p> 
<ol start="6" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">MiniGUI</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="108" src="https://oscimg.oschina.net/oscnet/up-90621013dfe367a52d524a2684246597f51.png" width="329" referrerpolicy="no-referrer"></p> 
<ol start="7" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">xGUI</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="137" src="https://oscimg.oschina.net/oscnet/up-4bc6e3d22c5127dcfbba52e16306ac16adf.png" width="311" referrerpolicy="no-referrer"></p> 
<ol start="8" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">miniStudio</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="163" src="https://oscimg.oschina.net/oscnet/up-2c9ec9dcd5eee25407916bac989bb469032.png" width="295" referrerpolicy="no-referrer"></p> 
<ol start="9" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">HVML</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="151" src="https://oscimg.oschina.net/oscnet/up-62bf1411b6cd916c03c52a21b4bb6f333fc.png" width="309" referrerpolicy="no-referrer"></p> 
<ol start="10" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">呼噜猫</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="140" src="https://oscimg.oschina.net/oscnet/up-8b7397169a061f770803188a973936a0804.png" width="332" referrerpolicy="no-referrer"></p> 
<ol start="11" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">Purring Cat</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="122" src="https://oscimg.oschina.net/oscnet/up-f723101013e71d8fc7a2dcde5ba1bd7a0b6.png" width="380" referrerpolicy="no-referrer"></p> 
<ol start="12" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">PurC</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="137" src="https://oscimg.oschina.net/oscnet/up-5849a0715325cc0b4124d7653d97b0b913c.png" width="310" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            