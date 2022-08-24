
---
title: 'Google TAG发现一款工具 可下载Gmail等平台的完整收件箱内容'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0824/e3bc44dab0e5c56.webp'
author: cnBeta
comments: false
date: Wed, 24 Aug 2022 04:04:24 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0824/e3bc44dab0e5c56.webp'
---

<div>   
<strong>Google 威胁分析小组（TAG）设法获得了一款工具，可用于下载 Gmail、Microsoft Outlook、Yahoo 等主流电子邮件平台的完整收件箱</strong>内容。该工具叫做 HYPERSCAPE，已经有证据表明用于对未知目标发起攻击。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0824/e3bc44dab0e5c56.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0824/89b4cb09ff68a11.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0824/bcab8a455d64031.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0824/9eae823f728c639.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0824/91f4c113976cca6.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0824/7f90f36738803ce.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">有国家背景的持续性威胁组织似乎正在使用 HYPERSCAPE 来提取收件箱中的所有电子邮件，而 Google 设法获得了该工具的一个版本。该团队目前正模拟这款工具，以观察它的破坏力。</p><p style="text-align: left;">Google 表示 HYPERSCAPE 可以在攻击者的终端上工作。换句话说，受害者不必被诱骗下载任何恶意软件，来让该工具完成其工作。但是，攻击者确实需要访问帐户凭据或受害者的会话 cookie。攻击者首先需要成功登录受害者的帐户，然后才能部署该工具。</p><p style="text-align: left;">似乎该工具欺骗了目标电子邮件服务，使其认为它是通过过时的浏览器访问的。为确保功能可靠，电子邮件服务会切换到基本 HTML 视图。此视图虽然在功能上会有限制，但电子邮件可正常访问。</p><p style="text-align: left;">一旦该工具强制电子邮件服务切换到基本的 HTML 视图，它就会将收件箱的语言更改为英语。此后，HYPERSCAPE 变成了一种抓取工具。它开始一一打开电子邮件并将它们下载为 .eml 格式。</p><p style="text-align: left;">为了逃避检测，HYPERSCAPE 确保以前未读的电子邮件继续标记为未读。成功下载所有电子邮件后，该工具会删除所有警告电子邮件，将语言恢复为原始状态，然后消失。</p><p style="text-align: left;">目前，HYPERSCAPE 似乎针对的是位于伊朗的账户。但是，其他威胁团体很可能会获得该工具。</p>   
</div>
            