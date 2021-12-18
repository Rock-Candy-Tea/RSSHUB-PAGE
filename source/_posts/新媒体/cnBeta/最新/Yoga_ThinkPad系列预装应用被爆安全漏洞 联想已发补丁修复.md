
---
title: 'Yoga_ThinkPad系列预装应用被爆安全漏洞 联想已发补丁修复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1218/adf640d2f752b23.webp'
author: cnBeta
comments: false
date: Sat, 18 Dec 2021 02:32:10 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1218/adf640d2f752b23.webp'
---

<div>   
并非所有的 PC 漏洞都是由微软造成的。有时候，预装在笔记本中的应用也会带来严重的问题。<strong>近日，安全研究人员发现联想 Yoga 和 ThinkPad 系列笔记本中内置的管理软件存在漏洞，有被黑客攻击和利用的潜在风险。</strong>安全专家在 ImControllerService 服务中发现了两个漏洞，可被利用来获得权限升级，从而控制系统。<br>
 <p style="text-align: left;">这些漏洞是：</p><p style="text-align: left;"><strong>CVE-2021-3922: </strong>在IMController（联想系统接口基础的一个软件组件）报告了一个竞赛条件漏洞，这可能允许本地攻击者连接并与 IMController 子进程的命名管道互动。</p><p style="text-align: left;"><strong>CVE-2021-3969：</strong>联想系统界面基础的软件组件IMController中报告了一个检查使用时间（TOCTOU）的漏洞，这可能允许本地攻击者提升权限。</p><p style="text-align: left;">虽然这些漏洞是本地漏洞，但攻击者经常将漏洞连锁起来，最终控制你的电脑，这意味着即使是本地漏洞也需要打补丁。幸运的是，联想对 IMController 组件进行了更新，使其达到1.1.20.3版本，并修复了该问题。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1218/adf640d2f752b23.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1218/db8b0c999116f77.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1218/190bde2143d4737.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">该更新将被自动推送，或者你可以通过重启电脑或重启"系统界面基础服务"来手动触发更新。要检查你是否已经有最新版本的联想IMController。</p><p style="text-align: left;">1. 打开文件管理器，进入C:（<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>） （Lenovo） （ImController） （PluginHost）。</p><p style="text-align: left;">2. 右键点击Lenovo.Modern.ImController.PluginHost.exe，选择属性。</p><p style="text-align: left;">3. 点击"详细信息"选项卡。</p><p style="text-align: left;">4. 阅读该文件的版本。</p>   
</div>
            