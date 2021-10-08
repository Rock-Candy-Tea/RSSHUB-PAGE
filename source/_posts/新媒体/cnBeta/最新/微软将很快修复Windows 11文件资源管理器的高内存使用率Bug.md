
---
title: '微软将很快修复Windows 11文件资源管理器的高内存使用率Bug'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1008/00446caed6c854b.jpg'
author: cnBeta
comments: false
date: Fri, 08 Oct 2021 04:09:12 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1008/00446caed6c854b.jpg'
---

<div>   
微软最近开始向使用 Windows 10 2004（及以上版本）的用户推送 Windows 11 升级包，全新的 UI 设计着实让人眼前一亮。然而本次更新也引入了一个严重的性能问题，<strong>一些用户发现，文件资源管理器（Explorer.exe）的内存占用率，似乎高得有些离谱。</strong><br>
<p><a href="https://static.cnbetacdn.com/article/2021/1008/00446caed6c854b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1008/00446caed6c854b.jpg" referrerpolicy="no-referrer"></a></p><p><a href="https://www.windowslatest.com/2021/10/07/windows-11-file-explorer-high-memory-usage-bug-is-getting-a-fix/" target="_self">Windows Latest</a> 指出：安装 Windows 11 之后，陆续有用户报告了诸多性能问题。</p><p>AMD 方面很快<a href="https://www.amd.com/en/support/kb/faq/pa-400" target="_self" textvalue="证实">证实</a>，性能问题乃 Windows 11 的新安全特性所致。然而<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>重新设计的文件资源管理器，显然也存在着另一个 Bug 。</p><p>在 Reddit 和论坛上，用户一直在抱怨他们的 Windows 11 设备正经历着极高的内存使用率，进而对整体性能都产生了负面影响（比如游戏帧率下降）。</p><p><a href="https://static.cnbetacdn.com/article/2021/1008/a5c62cd0a0df817.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1008/a5c62cd0a0df817.jpg" referrerpolicy="no-referrer"></a></p><p>据悉，微软在 Windows 11 上沿用了 Windows 10 时代的文件资源管理器设计，同时套用了更新的 Windows UI 库。</p><p>在新版 WinUI 的加持下，Windows 11 用户看到了文件资源管理器的新图标、现代控件、按钮、以及其它视觉调整。</p><p>与 Windows 10 的“朴素”质感相比，Windows 11 在命令 / 标题栏使用了被称作 Mica 的图层材质，以更好地适配桌面背景和应用程序窗口。</p><p>此外文件资源管理器的右键菜单，现也更新采用了 Fluent 设计元素，以匹配操作系统的其余部分。</p><p><img src="https://static.cnbetacdn.com/article/2021/1008/a9a628b31a5e90d.png" referrerpolicy="no-referrer"></p><p>由用户报告可知，Windows 11 中的新版文件资源管理器，有时会导致 70~99% 的峰值资源占用，将 CPU 的使用率拉得很高。而且在每次打开时，Explorer.exe 的内存使用量都会增加。</p><p>让人感到无语的是，其实早在上月，就有 Insider 测试者向 Windows 开发团队上报了 Windows 11 中存在的高内存使用率 Bug 。但在向公众推送正式版之前的 Dev 测试通道，仍忽略了这一点。</p><p>综合不断涌现的用户报告，不难推测上述问题与 Windows 11 文件资源管理器的内存泄露 Bug 有关。参考上月底的一则<a href="https://insider.windows.com/en-us/feedbackhub/fb?contextid=395&feedbackid=22ad0246-596b-4b47-82fd-21f980106ef4" target="_self">反馈中心</a>帖子，微软声称其已在 Build 22454 中实施了改进。</p><p>遗憾的是，除非你是 Dev 通道的测试者（据说已测试一个多月），否则可能要多等待几周，才会收到微软的补丁推送。</p>   
</div>
            