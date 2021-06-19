
---
title: '能挖的料不少！告诉你Win11还有啥隐藏功能'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210619/S568e6440-fd44-45f2-bc1c-5ee3399d2907.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sat, 19 Jun 2021 14:32:33 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210619/S568e6440-fd44-45f2-bc1c-5ee3399d2907.jpg'
---

<div>   
<p>近日，微软下一代操作系统Windows 11在网络上偷跑。全新的UI设计，给人了耳目一新的感觉。</p>
<p>随着试用人数增加，越来越多的隐藏功能开始被网友们挖掘出来，接下来咱们就一起看一看吧。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210619/568e6440-fd44-45f2-bc1c-5ee3399d2907.jpg" target="_blank"><img alt="能挖的料不少！告诉你Win11还有啥隐藏功能" h="346" src="https://img1.mydrivers.com/img/20210619/S568e6440-fd44-45f2-bc1c-5ee3399d2907.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
Win11这些隐藏功能你玩过没？</p>
<p><strong>1. 恢复Win10经典菜单</strong></p>
<p>Win11引入了全新开始菜单，一个最大变化就是取消了动态磁贴。不过也许是预览版缘故，目前这个菜单还存在很多问题，其中最明显的就是不允许用户自行调整大小，那么该如何恢复之前的开始菜单呢？</p>
<p>1） 打开注册表编辑器；</p>
<p>2） 进入HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced；</p>
<p>3） 在右窗格中新建一个“DWORD（32位）值”，重命名为“Start_ShowClassicMode”；</p>
<p>4） 双击“Start_ShowClassicMode”，并将其赋值为“1”；</p>
<p>5） 重启Win11后，就能看到Win10的经典版菜单了；</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210619/052debde-be09-4058-bb75-3e77408c9df0.jpg" target="_blank"><img alt="能挖的料不少！告诉你Win11还有啥隐藏功能" h="437" src="https://img1.mydrivers.com/img/20210619/S052debde-be09-4058-bb75-3e77408c9df0.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
恢复Win10经典开始菜单</p>
<p>恢复经典模式后，开始菜单会自动回归左下角，这会让整个界面看起来有些怪异。</p>
<p>因此如果你真的决定要这么做，还要先打开“Settings”→“Personalization”→“Taskbar”，将Taskbar alignment的值修改成“Left”（任务栏居左），这样整体效果才会和谐一些。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210619/b8af8a2a-a650-4579-8876-4489d26aef86.jpg" target="_blank"><img alt="能挖的料不少！告诉你Win11还有啥隐藏功能" h="533" src="https://img1.mydrivers.com/img/20210619/Sb8af8a2a-a650-4579-8876-4489d26aef86.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
通过注册表恢复的经典开始菜单</p>
<p><strong>2. 调整任务栏尺寸</strong></p>
<p>Win11并没有提供任务栏尺寸调节，对于很多用惯了Win10的小伙伴来说，其实是不太好适应的。但有网友发现，微软还是为我们提供了一个注册表键值，可以对任务栏的尺寸进行一些细微调整。</p>
<p>1） 打开注册表编辑器；</p>
<p>2） 进入HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced；</p>
<p>3） 在右窗格中新建一个“DWORD（32位）值”，重命名为“TaskbarSi”；</p>
<p>4） 双击“TaskbarSi”为其赋值，其中“0”代表小尺寸，“1” 代表中尺寸，“2” 代表大尺寸；</p>
<p>5） 重启Windows Explorer（Windows资源管理器）后，效果就出来了；</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210619/01e9d0a8-9979-4973-bf0b-d51c4644b906.jpg" target="_blank"><img alt="能挖的料不少！告诉你Win11还有啥隐藏功能" h="190" src="https://img1.mydrivers.com/img/20210619/S01e9d0a8-9979-4973-bf0b-d51c4644b906.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
三组尺寸对比</p>
<p><strong>3. 任务栏隐藏工具条</strong></p>
<p>除了之前的系统托盘，Win11也在任务栏中添加了一个隐藏式工具栏。打开方法是：右击任务栏空白区，点击“Taskbar settings”，然后在设置面板勾选“Show Windows Ink Workspace button”，这时任务栏右侧会多出一个“Pen”图标，点击即可进入工具栏。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210619/edd1a43c-e0fb-4159-8306-b0692abb6075.gif" target="_blank"><img alt="能挖的料不少！告诉你Win11还有啥隐藏功能" h="655" src="https://img1.mydrivers.com/img/20210619/Sedd1a43c-e0fb-4159-8306-b0692abb6075.gif" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
添加隐藏工具栏</p>
<p>Win11默认提供“Whiteboard（白板）”、“Snip & Sketch（截图工具）”两组工具，点击旁边的设置按钮可以对其快速编辑（最多可添加4个工具）。利用这种方法，我们可以在工具栏中添加一些常用应用，且不会占据宝贵的任务栏空间。</p>
<p><strong>4. “带鱼屏”优化</strong></p>
<p>和Win10一样，Win11默认也提供了窗口分屏功能，当我们将鼠标悬停到最大化按钮时，即可看到新增加的浮动式面板。不过很少有人注意到，Win11其实还对时下越来越多的“带鱼屏”做了优化。当你的屏幕横纵比超过一定限值时，就会自动激活三个隐藏式分屏方案，分别是“左/中/右”、“左主/右辅”、“左辅/右主”。这三种方案即可通过浮动面板调出，也能用鼠标直接拖拽窗口激活。总之对于“带鱼屏”用户来说，绝对是个好消息。</p>
<p align="center"><img alt="能挖的料不少！告诉你Win11还有啥隐藏功能" h="560" src="https://img1.mydrivers.com/img/20210619/4cef4bf103994705b2dadf61bd9bf0be.gif" style="border: 1px solid black; height: 480px; width: 600px;" w="700" referrerpolicy="no-referrer"><br>
隐藏在“最大化”按钮中的浮动分屏面板</p>
<p align="center"><img alt="能挖的料不少！告诉你Win11还有啥隐藏功能" h="327" src="https://img1.mydrivers.com/img/20210619/ea1d18c63f194a8ab0eae569be317e9a.gif" style="border: 1px solid black; height: 280px; width: 600px;" w="700" referrerpolicy="no-referrer"><br>
 “带鱼屏”用户可自动激活隐藏分屏模式</p>
<p><strong>5. “副键盘”与“手写板”</strong></p>
<p>Win11重新设计了软键盘模块，除了键位更加简洁外，还隐藏了两组新功能。首先是“副键盘”，Win11的副键盘可以提供符号、表情、颜文字、剪贴板等额外数据录入，相比Win10明显方便得多。</p>
<p>其次当我们点击左上角设置按钮时，还可以通过“Handwriting（手写板）”调出隐藏的“手写板”功能，方便在不同环境下完成录入。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210619/dfacb457-0ba0-41ad-b416-edb93b255e30.gif" target="_blank"><img alt="能挖的料不少！告诉你Win11还有啥隐藏功能" h="337" src="https://img1.mydrivers.com/img/20210619/Sdfacb457-0ba0-41ad-b416-edb93b255e30.gif" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
“副键盘”和“手写板”</p>
<p><strong>写在最后</strong></p>
<p>从目前反馈到的结果看，网上所流传的Win11镜像仍然只是一个早期版本，未来将会有更多功能被加入进来，所有的一切都要等微软6月24日才会揭晓。那么面对这样的Win11，你是否会喜欢呢？</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/weiruan.htm"><i>#</i>微软</a><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.pconline.com.cn/win10/1428/14281099.html">太平洋电脑网</a></span>
<span>责任编辑：陈驰</span>
</p>
        
</div>
            