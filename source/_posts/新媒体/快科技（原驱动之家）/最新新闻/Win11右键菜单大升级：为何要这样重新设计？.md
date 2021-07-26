
---
title: 'Win11右键菜单大升级：为何要这样重新设计？'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210726/S8b82a5ab-b53d-4274-a7c4-6151b026d1f6.jpg'
author: 快科技（原驱动之家）
comments: false
date: Mon, 26 Jul 2021 18:09:57 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210726/S8b82a5ab-b53d-4274-a7c4-6151b026d1f6.jpg'
---

<div>   
<p>在Win11中，微软对UWP和Win32传统软件的右键菜单都进行了现代化改造。作为更新的一部分，微软还改进了右键菜单的操作和内容，为Win32应用引入了新的体验。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210726/8b82a5ab-b53d-4274-a7c4-6151b026d1f6.jpg" target="_blank"><img alt="Win11右键菜单大升级：为何要这样重新设计？" h="315" src="https://img1.mydrivers.com/img/20210726/S8b82a5ab-b53d-4274-a7c4-6151b026d1f6.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>和Win10不同，Win11的变化更多更丰富。如果你体验了Win11的预览版，那么应该会知道，微软对右键菜单的设计之变更有多大。</strong>但目前Win11新的右键菜单仍处于早期阶段，这让它缺失了很多经典右键菜单中的可用选项。</p>
<p>对于这个问题，微软的一个应对之法是，<strong>当你右键点击传统软件的时候，在弹出的快捷菜单中加入一个“显示更多选项”的项目，如果你点击这个地方，就会展现开和Win10、Win8乃至Win7一样的原始的右键菜单内容。</strong></p>
<p>虽然这个额外展开的右键菜单也支持圆角等新特性，但是基本设计毫无变化。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210726/752799b2-c98e-4735-ac9d-cfa2c99183f8.jpg" target="_blank"><img alt="Win11右键菜单大升级：为何要这样重新设计？" h="384" src="https://img1.mydrivers.com/img/20210726/S752799b2-c98e-4735-ac9d-cfa2c99183f8.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>为什么Win11要如此设计呢？这是由于，从Windows XP以来，右键菜单就一直在不规范的环境中发展，很多命令都依赖于资源管理器组件（Explorer.exe）。</p>
<p>微软不允许用户定制右键菜单内容，也不允许用户阻止应用程序在菜单中添加新的选项，这在Win10和更旧版本的WIndows中，引发了性能和可靠性方面的问题——相信很多朋友都遇到过右键菜单乱七八糟的情况，开个右键菜单得等半天，但又不能删掉某些右键菜单的选项。</p>
<p>在Win11中，情况有了改观。<strong>有了“显示更多选项”这个设定，Win11可以在不影响系统整体性能的前提下，兼容加载传统的右键菜单内容。传统右键菜单的机制没有被删除，依赖旧API的应用程序依然可以通过这个设计继续工作。</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210726/852b0682-a144-43af-98c1-a721c496326b.png" target="_blank"><img alt="Win11右键菜单大升级：为何要这样重新设计？" h="981" src="https://img1.mydrivers.com/img/20210726/S852b0682-a144-43af-98c1-a721c496326b.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>除了性能上的改进，Win11右键菜单也调整了一些选项的位置，例如常见的Windows命令被放到了右键菜单的顶部。就如上面的截图所示，新的右键菜单带有常见的操作命令logo，例如剪贴、复制、粘贴、删除和重命名。</p>
<p>另外，微软正计划将“打开”和“打开方式”分组，以减少杂乱。现在“刷新”选项已经重新加入到了右键菜单中，这方便了那些经常刷新其桌面/文件夹内容的用户。</p>
<p>Win11的另一个细节上的改进，在于共享功能变得更加优秀。在之前，Edge浏览器等应用内置了共享对话框，现在这个机制在Win11中得到了大幅改进。</p>
<p>共享对话框的界面得到了更新，现在用户可以在共享区中，轻松发现可用的应用程序或者设置。例如，当你使用邮件应用的时候，可以和多个Outlook和Gmail账户连接，得以轻松发现联系人的置顶入口，以便给自己发送一封邮件。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210726/596d2ff5-28cb-4520-8220-7b00d8951a25.png" target="_blank"><img alt="Win11右键菜单大升级：为何要这样重新设计？" h="829" src="https://img1.mydrivers.com/img/20210726/S596d2ff5-28cb-4520-8220-7b00d8951a25.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>之前，共享对话框是UWP应用和微软内置应用的专属，而在Win11中，微软允许所有Win32应用程序都调用相关接口。</p>
<p>除了UWP和桌面应用，如果Edge浏览器中的PWA网页应用使用Web Share Target API，那么也可以调用新的分享对话框。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210726/5baedbabba31408bb2027d5ab830dda5.png" target="_blank"><img alt="Win11右键菜单大升级：为何要这样重新设计？" h="399" src="https://img1.mydrivers.com/img/20210726/s_5baedbabba31408bb2027d5ab830dda5.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.pconline.com.cn/win10/1434/14340364.html">太平洋电脑网</a></span>
<span>责任编辑：陈驰</span>
</p>
        
</div>
            