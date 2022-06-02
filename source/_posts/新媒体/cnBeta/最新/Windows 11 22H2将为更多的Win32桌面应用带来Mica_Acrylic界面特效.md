
---
title: 'Windows 11 22H2将为更多的Win32桌面应用带来Mica_Acrylic界面特效'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0602/98b31873aad3d66.jpg'
author: cnBeta
comments: false
date: Thu, 02 Jun 2022 09:58:33 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0602/98b31873aad3d66.jpg'
---

<div>   
Windows 11的原生应用程序，如文件资源管理器和其他外壳应用程序默认使用圆角和亚克力（Acrylic）等流畅设计元素。除了圆角，Windows 11的另一个重要设计特征是云母（Mica）等材料风格，它使应用程序的背景颜色与桌面一致。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0602/98b31873aad3d66.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0602/98b31873aad3d66.jpg" title alt="Windows-11-Mica-for-Win32-apps.jpg" referrerpolicy="no-referrer"></a></p><p>Mica与Acrylic类似，但它的工作方式略有不同。正如<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>所描述的，<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Mica材料通过将背景与应用程序对齐来创建一个"颜色层次"，以区分应用程序的多个打开实例，如文件资源管理器等。</p><p>目前，开发者不能在他们的Win32应用程序中启用这种新材料。然而，这将很快发生变化。从22H2版本开始，开发者可以在他们传统的Win32应用程序（即桌面程序）的容器/窗口中轻松启用云母或亚克力风格。这已在该公司发布的一份新文件中得到确认。</p><p>云母生活在桌面窗口管理器（DWM）内，一个名为"DWM_SYSTEMBACKDROP_TYPE"的新的Windows 11变量将允许开发者在其桌面应用程序中指定云母或亚克力材料。"用于指定窗口的系统绘制的背景材料的标志，包括在非客户端区域后面，"支持文件中写道。按照微软的说法，有四个常量可供开发者选择。</p><p><a href="https://static.cnbetacdn.com/article/2022/0602/1ed8c8acf3594f8.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0602/1ed8c8acf3594f8.png" title alt="Windows-11-Mica.png" referrerpolicy="no-referrer"></a></p><p>DWMSBT_AUTO：基础行为，在这个常量中，桌面窗口管理器（DWM）将自动决定应用程序窗口的系统绘制的背景材料。</p><p>DWMSBT_NONE：开发者可以跳过云母或亚克力，如果他们有自己的应用程序窗口的定制设计。例如，Spotify有自己的标题。当这个值被设置时，微软不会填充任何系统背景。</p><p>DWMSBT_MAINWINDOW：应用与长效窗口对应的背景材料效果。</p><p>DWMSBT_TRANSIENTWINDOW：应用与瞬时窗口对应的背景材料效果。</p><p>DWMSBT_TABBEDWINDOW：应用与带有标签标题栏的窗口相对应的背景材料效果。</p><p>Mica是桌面窗口管理器（DWM）的一部分，这使得它可以用于广泛的应用程序。事实上，有一个名为"Mica for Everyone"的第三方开源工具，它使用DwmSetWindowAttribute和其他方法，在所有应用程序中强制启用Mica。</p><p><a href="https://static.cnbetacdn.com/article/2022/0602/c00f3544d486f1a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0602/c00f3544d486f1a.jpg" title alt="Mica-material.jpg" referrerpolicy="no-referrer"></a></p><p>虽然这个更新听起来对每个人都是一个好消息，但还是有一个问题。微软说，这个新的变量是Windows 11 22H2（Build 22621）的专属。换句话说，如果开发者针对的是之前版本的操作系统，他们就只能使用旧的材料风格。</p>   
</div>
            