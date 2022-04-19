
---
title: '7-Zip被爆零日安全漏洞：可提权执行代码 但用户可简单操作使其失效'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0419/8575a5c41007b03.webp'
author: cnBeta
comments: false
date: Tue, 19 Apr 2022 02:20:22 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0419/8575a5c41007b03.webp'
---

<div>   
文件压缩软件 7-Zip 被爆零日安全漏洞，允许攻击者提权并执行任意代码。<strong>目前开发团队并未发布补丁，但普通用户可以通过简单操作来让这个漏洞失效。</strong>上周，研究人员 Kağan Çapar 发现并公布了 7-Zip 的一个零日漏洞，该漏洞可以授予权限升级和命令执行。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0419/8575a5c41007b03.webp" referrerpolicy="no-referrer"></p><p>它被命名为 <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29072" target="_blank">CVE-2022-29072</a>，影响到运行 21.07 版本的 Windows 用户--截至目前的最新版本。</p><p style="text-align: left;">正如下面的视频所显示的，对系统有有限访问权的攻击者可以通过打开 7-Zip 的“帮助”窗口，在“帮助->内容”下，将一个扩展名为 .7z 的文件拖入该窗口来激活该漏洞。任何具有该扩展名的文件都可以使用。它不一定是一个真正的7z档案。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0419/915e7f7866997c6.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0419/e9172e618c6502a.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">通过在7zFM.exe进程下运行一个子进程，该漏洞可以提升攻击者的权限，让他们在目标系统上运行命令。恰帕尔将此归咎于7z.dll文件的错误配置和堆溢出。</p><p style="text-align: left;">Windows的HTML帮助文件也可能负有一定的责任，因为其他程序可以通过它允许执行命令。Çapar 提到了一个类似的漏洞，该漏洞通过 Windows HTML 帮助文件和 WinRAR 起作用。</p><p style="text-align: left;"><strong>删除 7-Zip 根文件夹中的“7-zip.chm”文件可以缓解这个问题，直到开发人员打上补丁。</strong></p>   
</div>
            