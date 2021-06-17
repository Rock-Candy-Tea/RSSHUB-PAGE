
---
title: '技巧：如何切换Windows 11任务栏的三种尺寸'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0617/8e4c6152b263c73.jpg'
author: cnBeta
comments: false
date: Thu, 17 Jun 2021 03:20:34 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0617/8e4c6152b263c73.jpg'
---

<div>   
Windows 11 镜像已经于昨日偷跑，相信已经有一些愿意尝鲜的小伙伴在兼容设备或者虚拟机上测试了。Windows 11 是带 Windows 10X Shell 和一些现代化功能的 Windows 10 增强版本，包括开始菜单、Windows Search 和 Action Center 等 UI 元素都借鉴于 Windows 10X。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0617/8e4c6152b263c73.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0617/8e4c6152b263c73.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">本站昨日的报道中已经介绍了如何恢复含有动态磁贴的经典开始菜单，并将开始或搜索按钮等任务栏图标调整到左边。而外媒 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Lastest 通过深入挖掘，发现在 Windows 11 系统中任务栏还有大、中、小三种不同的尺寸。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0617/56d60938b4e0e1d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0617/56d60938b4e0e1d.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">中</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0617/325bc5eee2526a9.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0617/325bc5eee2526a9.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">大</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0617/6af2a27ca6352d5.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0617/6af2a27ca6352d5.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">小</p><p style="text-align: left;">其中中号是任务栏的默认设置，在桌面和平板电脑之间进行了平衡。而大号则适用于平板设备，小号则带来更紧凑的外观。目前，如果你想改变任务栏的大小，你需要通过以下步骤修改“TaskbarSi”值。</p><blockquote style="text-align: left;"><p style="text-align: left;">1. 打开注册表编辑器，导航到以下路径。</p><p style="text-align: left;">2. HKEY_CURRENT_USER\Software\Microsoft\ Windows\CurrentVersion\Explorer\Advanced\</p><p style="text-align: left;">3. 创建一个名为 "TaskbarSi"的新 DWORD 条目。改变DWORD值来修改任务栏的大小。</p><p style="text-align: left;">     0 = 小</p><p style="text-align: left;">     1 = 中</p><p style="text-align: left;">     2 = 大</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0617/615923b0b56afc9.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0617/615923b0b56afc9.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">4.关闭注册表编辑器，并重新启动Windows资源管理器以查看变化。</p></blockquote><p style="text-align: left;">目前，似乎没有任何方法可以通过本地设置应用程序来做这件事。现代和重新设计的设置应用程序很可能会包括改变任务栏大小的选项。任务栏定制设置并不一定令人惊讶，因为Windows 10X的预览版也有三种任务栏尺寸。</p>   
</div>
            