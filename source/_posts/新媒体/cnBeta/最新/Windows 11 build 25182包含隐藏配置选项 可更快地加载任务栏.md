
---
title: 'Windows 11 build 25182包含隐藏配置选项 可更快地加载任务栏'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0823/df415537e357427.png'
author: cnBeta
comments: false
date: Tue, 23 Aug 2022 12:26:53 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0823/df415537e357427.png'
---

<div>   
微软对Windows 11中的任务栏的实验仍在继续。在该公司删除了让人眼前一亮任务栏的任务栏读取动画后，用户发现了一个新的隐藏配置，它可以让系统更快地加载任务栏。<br>
 <p>Windows 11的用户知道操作系统重新启动任务栏及其显示图标的速度是多么痛苦。显然，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>希望通过启动任务栏与Immersive Shell并行来解决这一不便，这可以有效地减少操作系统运行任务栏和启用其图标的时间。</p><p><img src="https://static.cnbetacdn.com/article/2022/0823/df415537e357427.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p><strong>如何在Windows 11 build 25182中使任务栏加载更快？</strong></p><p>从其GitHub仓库下载Vive工具：https://github.com/thebookisclosed/ViVe/releases</p><p>在方便的地方提取文件，例如，C:\Vive。</p><p>以管理员身份启动Windows终端，并切换到命令提示符配置文件。</p><p>使用CD命令导航到Vive文件夹。例如，CD C:\Vive。</p><p>输入vivetool /enable /id:39751186并按回车键。</p><p>重新启动Windows资源管理器以查看配置的运行情况。</p><p>要恢复这些变化，使用vivetool /disable /id:39751186</p><p>启用该配置后，你会注意到任务栏的启动速度加快了，但之前我们提到的图标飞升的动画依然没有出现。我们不知道微软未来会不会把这一特效带回来，或者只是一次简单的A/B实验而已。</p>   
</div>
            