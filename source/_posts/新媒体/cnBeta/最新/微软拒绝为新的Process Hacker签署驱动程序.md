
---
title: '微软拒绝为新的Process Hacker签署驱动程序'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1025/5609d519fbc3297.jpg'
author: cnBeta
comments: false
date: Mon, 25 Oct 2021 01:29:48 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1025/5609d519fbc3297.jpg'
---

<div>   
<strong>David Xanatos 透露，微软拒绝为新的 Process Hacker 签署驱动程序，而没有给出任何进一步的理由。</strong>这意味着这个工具的较新版本（以及 ProcessExplorer 等工具）不能再使用。
Process Hacker 是一款多功能系统监控软件，不少研究人员可以利用该工具来监控自己的系统资源，调试软件或检测恶意软件。<br>
 <p style="text-align:center"><strong><a href="https://static.cnbetacdn.com/article/2021/1025/5609d519fbc3297.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1025/5609d519fbc3297.jpg" alt="75476zte.jpg" referrerpolicy="no-referrer"></a></strong></p><p style="text-align: left;"><strong>Process Hacker项目地址</strong></p><p style="text-align: left;">● 官方网站：<a href="https://processhacker.sourceforge.io/">https://processhacker.sourceforge.io/</a></p><p style="text-align: left;">● GitHub：<a href="https://github.com/processhacker/processhacker">https://github.com/processhacker/processhacker</a></p><p style="text-align: left;"><strong>系统要求：</strong></p><p style="text-align: left;">Windows 7 及以上版本，支持 32 位或 64 位。</p><p style="text-align: left;"><strong>功能介绍</strong></p><p style="text-align: left;">● 提供详细的系统活动信息概览，支持高亮显示;</p><p style="text-align: left;">● 提供图标数据和统计数据，可帮助我们快速追踪目标资源和进程;</p><p style="text-align: left;">● 不能编辑或删除文件?追踪正在使用目标文件的进程;</p><p style="text-align: left;">● 活动网络连接诊断，可直接关闭连接;</p><p style="text-align: left;">● 获取实时磁盘访问信息;</p><p style="text-align: left;">● 以内核模式查看栈内存数据，支持WOW64和.NET;</p><p style="text-align: left;">● 越过 services.msc：创建、编辑和控制服务;</p><p style="text-align: left;">● 体积小，可移动，无需安装;</p><p style="text-align: left;">● 100%<a href="https://www.gnu.org/philosophy/free-sw.en.html"> 免费软件 </a>(遵循<a href="https://www.gnu.org/licenses/gpl-3.0.en.html"> GPL v3 </a>许可证协议)。</p><p style="text-align: left;"><strong>David Xanatos 表示：</strong></p><blockquote style="text-align: left;"><p style="text-align: left;">我相信很多人都熟悉 Process Hacker 工具，这是一个非常高级的任务管理器，其用户界面需要很多时间来适应。</p><p style="text-align: left;">看起来该工具的开发者在获得 MSFT 签署的新驱动程序方面遇到了巨大的问题，正如他在 Github 讨论中报告的那样。</p><p style="text-align: left;">签署过程每次都失败，没有任何错误信息，微软声称“这超出了我们的支持范围”......但微软只是无休止地搞我，直到证书过期。</p><p style="text-align: left;">在提交给微软 Winget 时也发生了完全相同的问题。</p><p style="text-align: left;">我厌倦了给微软发电子邮件，但从未得到关于这种行为的回应。你也可以看到有多少次软件包因无法解释的原因而失败，在提交驱动程序时也发生了完全相同的问题：microsoft/winget-pkgs#373</p><p style="text-align: left;">微软的 Process Explorer 有同样的功能，所以他们没有资格阻止竞争对手，然后去把完全相同的功能包含在自己的软件中。</p><p style="text-align: left;">微软一直在秘密地通过他们的 SAC 产品增加比 Process Hacker 更强大的功能--SAC 在设计上没有任何安全性--他们显然不是因为任何实际的技术问题而针对这个项目，而是因为我们比他们的产品更受欢迎，所以他们使用了他们对Netscape Navigator使用的相同（非法和反竞争）的策略来消除竞争，但也给这个项目贴上恶意的标签，试图误导竞争监管机构。</p><p style="text-align: left;">微软的大部分改变仅限于用阻止竞争对手软件的签名检查来限制 Windows API（例如 CreateWindowInBand、NtQuerySystemInformation、NtQueryInformationProcess 等等），而不是直接针对驱动程序本身。</p><p style="text-align: left;">添加到这些函数和类中的签名检查只阻止第三方，这包括有签名的二进制文件。由于那些只针对微软的签名检查，即使我们解决了提交问题，我们也无法实现与任务管理器和进程浏览器相同的功能。</p><p style="text-align: left;">Always-on-top, Auto-elevation, DPS statistics, Default taskmgr application preferences (Microsoft hardcoded taskmgr.exe blocking competitors), GPU statistics (最近在Windows 10和Windows 11上被故意破坏)和 DirectUI 框架是我想实现的一些功能的例子，目前由任务管理器实现，但被微软专用签名限制，而我们迫切需要的PPL等更高级的新安全也是微软专用签名限制。</p><p style="text-align: left;">现在唯一允许使用这些和其他功能的证书仅限于微软的Windows证书--与任务管理器和进程资源管理器使用的证书相同--而SAC拥有比其他任何东西（包括进程黑客）更强大的功能，但绝对没有任何安全性。</p><p style="text-align: left;">多年来我一直向微软员工抱怨这些东西，但攻击越来越严重，自从去年他们给项目贴上恶意标签后，我就开始要求我们的竞争监管机构起诉该公司......微软声称现在热爱开源，并且更加透明，但他们在SAC、taskmgr和procxp上做的那些鬼事，同时攻击竞争对手，试图限制竞争，扼杀项目，这真是太疯狂了。</p></blockquote>   
</div>
            