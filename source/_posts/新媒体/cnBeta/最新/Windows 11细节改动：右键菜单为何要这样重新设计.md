
---
title: 'Windows 11细节改动：右键菜单为何要这样重新设计'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0726/0383ab9ce121943.jpg'
author: cnBeta
comments: false
date: Mon, 26 Jul 2021 10:48:19 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0726/0383ab9ce121943.jpg'
---

<div>   
在Windows 11中，微软对UWP和Win32传统软件的右键菜单都进行了现代化改造。作为更新的一部分，微软还改进了右键菜单的操作和内容，为Win32应用引入了新的体验。和Windows 10不同，Windows 11的变化更多更丰富。如果你体验了Windows 11的预览版，那么应该会知道，微软对右键菜单的设计之变更有多大。<br>
<p><em><img src="https://static.cnbetacdn.com/article/2021/0726/0383ab9ce121943.jpg" referrerpolicy="no-referrer"></em></p><p>但目前Windows 11新的右键菜单仍处于早期阶段，这让它缺失了很多经典右键菜单中的可用选项。</p><p>对于这个问题，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>的一个应对之法是，当你右键点击传统软件的时候，在弹出的快捷菜单中加入一个“显示更多选项”的项目，如果你点击这个地方，就会展现开和Windows 10、Win8乃至Win7一样的原始的右键菜单内容。虽然这个额外展开的右键菜单也支持圆角等新特性，但是基本设计毫无变化。</p><p><em><img src="https://static.cnbetacdn.com/article/2021/0726/9ccbf224f64b708.jpg" referrerpolicy="no-referrer"></em></p><p>为什么Windows 11要如此设计呢？这是由于，从Windows XP以来，右键菜单就一直在不规范的环境中发展，很多命令都依赖于资源管理器组件（Explorer.exe）。微软不允许用户定制右键菜单内容，也不允许用户阻止应用程序在菜单中添加新的选项，这在Windows 10和更旧版本的WIndows中，引发了性能和可靠性方面的问题——相信很多朋友都遇到过右键菜单乱七八糟的情况，开个右键菜单得等半天，但又不能删掉某些右键菜单的选项。</p><p>在Windows 11中，情况有了改观。有了“显示更多选项”这个设定，Windows 11可以在不影响系统整体性能的前提下，兼容加载传统的右键菜单内容。传统右键菜单的机制没有被删除，依赖旧API的应用程序依然可以通过这个设计继续工作。</p><p><em><img src="https://static.cnbetacdn.com/article/2021/0726/8288202bed53d01.png" referrerpolicy="no-referrer"></em></p><p>除了性能上的改进，Windows 11右键菜单也调整了一些选项的位置，例如常见的Windows命令被放到了右键菜单的顶部。就如上面的截图所示，新的右键菜单带有常见的操作命令logo，例如剪贴、复制、粘贴、删除和重命名。</p><p>另外，微软正计划将“打开”和“打开方式”分组，以减少杂乱。现在“刷新”选项已经重新加入到了右键菜单中，这方便了那些经常刷新其桌面/文件夹内容的用户。</p><p>Windows 11的另一个细节上的改进，在于共享功能变得更加优秀。在之前，Edge浏览器等应用内置了共享对话框，现在这个机制在Windows 11中得到了大幅改进。</p><p>共享对话框的界面得到了更新，现在用户可以在共享区中，轻松发现可用的应用程序或者设置。例如，当你使用邮件应用的时候，可以和多个Outlook和Gmail账户连接，得以轻松发现联系人的置顶入口，以便给自己发送一封邮件。</p><p><em><img src="https://static.cnbetacdn.com/article/2021/0726/1d04f4bb9ef7476.png" referrerpolicy="no-referrer"></em></p><p>之前，共享对话框是UWP应用和微软内置应用的专属，而在Windows 11中，微软允许所有Win32应用程序都调用相关接口。</p><p>除了UWP和桌面应用，如果Edge浏览器中的PWA网页应用使用Web Share Target API，那么也可以调用新的分享对话框。</p>   
</div>
            