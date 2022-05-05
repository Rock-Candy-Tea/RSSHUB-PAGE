
---
title: '苹果Safari用户吐槽微软Outlook频繁提示下载异常的iFrame文件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0505/472a67914f0aa8a.png'
author: cnBeta
comments: false
date: Thu, 05 May 2022 05:26:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0505/472a67914f0aa8a.png'
---

<div>   
近段时间，许多 Safari 浏览器用户抱怨称 —— <strong>在访问微软 Outlook 电子邮件服务的时候，应用程序总会尝试在 macOS 系统上下载一个名为“TokenFactoryIframe”的神秘文件。</strong>Windows Latest 尝试复现了这一问题，证实 Outlook 每隔几秒（或至少每次访问 Apple 平台上的 Outlook 服务时）都会下载该文件。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0505/472a67914f0aa8a.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图自：Microsoft 官网）</p><p>该问题似乎又错误推送到 Outlook 服务器端的配置文件引起，而无关于 Safari 浏览器或 macOS 操作系统。不久后，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>在一份声明中承认了该问题，但尚未解释为何会弹出文件下载框。</p><p>一种猜测是，Microsoft 365 平台遇到了 HTML 错误，毕竟 iframe 是网站上常见的交互式内容托管方式。此外据 <a href="https://www.reddit.com/r/Outlook/comments/uh927i/i_download_a_file_every_time_i_open_outlook_on/" target="_self">Reddit</a> 网友爆料，问题似乎于 5 月 2 号（周一）那天开始出现。</p><p><img src="https://static.cnbetacdn.com/article/2022/0505/6e733f5353a5457.png" alt="3.png" referrerpolicy="no-referrer"></p><p>参考该公司发言人的说法，问题仅限于 Safari 浏览器。在正式修复到来之前，macOS 用户可暂时切换到其它浏览器，以避免受到持续的困扰。</p><p>尴尬的是，<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Latest 也收到了一些与 Apple 平台上的 Google Chrome 和 Mozilla Firefox 浏览器相关的问题报告。</p><p><img src="https://static.cnbetacdn.com/article/2022/0505/90ff3a5e8b4f221.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>庆幸的是，引发问题的 TokenFactoryIFrame 并被包含任何恶意内容（文件大小为 0），看不顺眼的用户可随时将它从系统中清除，而不必担心造成任何后果。</p><p><strong>有需要的朋友，可参考如下方法，以临时屏蔽 TokenFactoryIframe 的下载：</strong></p><blockquote><p>（1）启动 Safari 浏览器，但不要急着访问 Outlook 。</p><p>（2）点击 Safari 顶部菜单，并转至‘首选项’。</p><p>（3）先点击‘网站’，在从左侧‘通用’列中选择‘下载’。</p><p>（4）在允许的网站列表中，禁用掉 Outlook 和 <a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a> 的网站权限。</p><p>（5）保存退出 Safari 浏览器，然后重新登陆 Outlook 。</p></blockquote><p>需要注意的是，这么做也会阻止浏览器下载问题站点的所有附件。</p><p>如果你可以在 macOS 上正常使用 Google Chrome 等第三方浏览器（不一定每个人都有这么好的运气），大可暂时放弃 Safari、并等待微软正式修复 Outlook 服务器上的错误配置。</p>   
</div>
            