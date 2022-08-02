
---
title: 'Google Chrome 104正式版发布：延长电池续航 启动延迟加载实验'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0802/b4328b99e5727d6.webp'
author: cnBeta
comments: false
date: Tue, 02 Aug 2022 11:33:57 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0802/b4328b99e5727d6.webp'
---

<div>   
<strong>Google Chrome浏览器104版今日发布，本次更新包括延长电池续航、页面加载实验、更好的屏幕共享工具以及Chromebooks的少量UI变化。</strong>当更新可用时，Chrome会自动在您的设备上安装更新。要立即检查和安装任何可用的更新，请点击三点菜单图标，然后点击帮助>关于Google浏览器。<br>
 <p><strong>加速页面加载的实验</strong></p><p>在互联网的早期，浏览器会一次性加载整个页面。浏览器和网站最终开始转向"延后加载"，即一些内容在可见之前不被加载。然而，Chrome浏览器只有在页面特别允许的情况下才会这样加载嵌入式内容。</p><p>Google正在测试一项名为"LazyEmbeds"的实验，该实验将自动延后加载一些嵌入式内容，而无需页面要求。该实验计划从1%的人运行稳定的Chrome 104开始。</p><p><strong>调整CPU占用率 延长电池续航</strong><br></p><p>Chrome团队从2020年的Chrome 86就开始测试“密集唤醒节流”（Intensive Wake
UpThrottling）功能。当时是因为Google发现许多网页都会于背景执行Javascript Timer（JS
Timer），而且这些JS
Timer每秒就会唤醒分页一次，虽然所使用的CPU资源不到1%，但其频繁度再加上众多的分页，即可能大量耗损CPU资源并降低电池续航力。</p><p>于是Chrome团队设计了IntensiveWake
Up Throttling机制，只要分页进入背景5分钟之后，便限制JS
Timer每分钟只能唤醒分页一次。当时的实验显示，此一机制可减少5倍的CPU使用率，并让电池寿命延长1.25个小时，之后Intensive
Wake Up Throttling即成为Chrome 88的默认功能。</p><p>这次该团队则是自Chrome 103开始测试更进阶的Quick Intensive Timer
Throttling功能，它同样是基于Intensive Wake Up Throttling的概念，也是限制JS
Timer每分钟只能唤醒分页一次，但把进入背景的5分钟缓冲时间缩短为10秒。换句话说，只要网页进入背景10秒钟之后，其JS
Timer执行频率就会从每秒一次切换至1分钟1次。</p><p>根据Chrome团队的测试，Quick Intensive Timer Throttling将能减少10%的CPU使用时间，进一步改善电池寿命。</p><p><strong>网络应用的区域捕获</strong></p><p><strong><img src="https://static.cnbetacdn.com/article/2022/0802/b4328b99e5727d6.webp" title alt="region-capture.webp" referrerpolicy="no-referrer"></strong></p><p>Google Chrome现在有能力裁剪视频轨，该功能被称为"区域捕捉"，它可以让你选择你想记录或分享的屏幕的哪一部分。</p><p>Google给出的例子主要是用于视频会议，用户现在可以选择想分享的屏幕区域。这对于在屏幕共享时隐藏视频会议控件特别有用。</p><p><strong>Chromebooks获得了一个新的"开始菜单"</strong></p><p><strong><img src="https://static.cnbetacdn.com/article/2022/0802/187304d2ba6e11e.webp" title alt="Screenshot-2022-08-01-11.11.27-AM.webp" referrerpolicy="no-referrer"></strong></p><p>Google一直在努力改造Chrome OS的界面，已经有一段时间了。最大的变化之一是应用启动器。它现在看起来更像<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>的开始菜单。新的"生产力启动器"像Windows的开始菜单一样漂浮在屏幕的角落。它的顶部有一个Google搜索栏和助理快捷方式。可以右击或轻敲并按住任何地方，按名称或图标颜色排序。与旧的启动器相比，这是一个相当大的改进。</p><p><strong>为Chromebooks设计的自动浅色和深色主题</strong></p><p><strong><img src="https://static.cnbetacdn.com/article/2022/0802/210e3a52ebb22c0.webp" title alt="Screenshot-2022-08-01-11.18.19-AM.webp" referrerpolicy="no-referrer"></strong></p><p>Chromebooks拥有"非官方"的黑暗和光明主题已经有一段时间了。值得庆幸的是，该功能正在进入稳定通道，并能让主题自动切换。以前，只有当你启用一个功能标志时，这些主题才可用。让主题在晚上和白天自动切换的能力并不存在。现在，就像Windows和macOS一样，Chromebook有完全特色的浅色和深色主题。</p><p><strong>Chromebooks的系统托盘改进</strong></p><p><strong><img src="https://static.cnbetacdn.com/article/2022/0802/cf751c293165640.webp" title alt="Screenshot-2022-08-01-11.11.43-AM.webp" referrerpolicy="no-referrer"></strong></p><p>Google也在对Chromebooks的系统托盘进行改造。这是一个显示时钟、电池和Wi-Fi的区域。Chrome OS 104将日期添加到系统托盘中，并带来了一个新的日历部件。</p><p>现在时钟被分割开来，在左边显示日期。当选择日期时会得到一个漂亮的、大的日历小部件。你可以点击日历上的一个日期，选择"在Google日历中打开"。Google还对通知的设计进行了一些调整。</p><p><strong>Chrome 104还有什么新内容？</strong></p><p>安全支付确认现在支持让用户选择不存储他们的信用卡数据用于以后的购买。</p><p>当cookie被设置为明确的Expires/Max-Age属性时，该值现在将被限制在不超过400天。</p><p>object-view-box属性让作者可以选择一个图像的一部分，在目标替换元素的内容框内绘制。</p><p>全屏伴侣窗口功能允许网络应用在多个屏幕上放置全屏内容和一个弹出窗口。</p><p>网络蓝牙现在可以通过权限策略进行控制。</p>   
</div>
            