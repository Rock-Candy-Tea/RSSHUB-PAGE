
---
title: 'macOS端Zoom获更新 修复高危安全漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0816/47066d87efbceac.png'
author: cnBeta
comments: false
date: Tue, 16 Aug 2022 00:20:03 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0816/47066d87efbceac.png'
---

<div>   
<strong>援引国外科技媒体 MacRumors 报道，Zoom 已经发布了新版补丁，修复了存在于 macOS 端应用中的漏洞，允许黑客入侵接管用户的操作系统。</strong>在<a href="https://explore.zoom.us/en/trust/security/security-bulletin/" target="_blank">安全公告</a>中，Zoom 承认存在 CVE-2022-28756 这个问题，并表示在最新的 5.11.5 版本中已经提供了修复，用户应该理解下载安装。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0816/47066d87efbceac.png" alt="QQ截图20220816081635.png" referrerpolicy="no-referrer"></p><p style="text-align: left;">Objective-See Foundation 的联合创始人兼安全专家帕特里克·沃德尔（Patrick Wardle）率先发现了这个漏洞，并在上周召开的 Def Con 黑客大会上公开演示。该漏洞存在于 Zoom 的 macOS 安装包内，需要特别的用户权限来执行。</p><p style="text-align: left;">通过利用该工具，沃德尔利用 Zoom 安装包的加密签名来安装恶意程序。接下来，攻击者可以接管用户的系统，允许修改、删除和添加文件。</p><p style="text-align: left;">在引用 Zoom 的更新之后，沃德尔表示：“感谢 Zoom 能够如此快地修复这个问题。反转补丁，Zoom 安装程序现在调用 lchown 来更新更新 .pkg 的权限，从而防止恶意使用”。</p><p style="text-align: left;">您可以通过首先在 Mac 上打开应用程序并从屏幕顶部的菜单栏中点击 zoom.us（这可能因您所在的国家/地区而异）来在 Zoom 上安装 5.11.5 更新。然后，选择检查更新，如果可用，Zoom 将显示一个窗口，其中包含最新的应用程序版本，以及有关更改内容的详细信息。从这里，选择更新开始下载。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1304009.htm" target="_blank">利用macOS端Zoom安装器漏洞 黑客可以接管你的Mac</a></p></div>   
</div>
            