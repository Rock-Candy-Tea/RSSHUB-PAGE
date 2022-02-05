
---
title: '微软禁用MSIX AppX安装程序以使用户免遭Emotet、BazarLoader类威胁'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0205/983d9aaa95ca27e.jpg'
author: cnBeta
comments: false
date: Sat, 05 Feb 2022 08:48:42 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0205/983d9aaa95ca27e.jpg'
---

<div>   
微软今天正式宣布，它已经禁用了MSIX应用安装程序协议以防止恶意攻击。该协议允许用户直接从网络服务器上安装各种应用程序，而不需要先将其下载到本地存储。当时的想法是，这种方法将为用户节省空间，因为不需要下载整个MSIX包。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0205/983d9aaa95ca27e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0205/983d9aaa95ca27e.jpg" title alt="1644036685_ms-appinstaller_disabled_(source-_bvenhaus_techcommunity_ms).jpg" referrerpolicy="no-referrer"></a></p><p>然而，这种<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>应用程序安装包后来被发现用来分发恶意的PDF文件，如Emotet和BazarLoader恶意软件。因此，该协议在去年被禁用，但今天才正式宣布。这个Windows AppX安装程序欺骗漏洞的ID被分配为CVE-2021-43890。</p><p><strong>安全公告的贴文解释称：</strong></p><blockquote><p>我们最近被告知，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">MSI</a>X的ms-appinstaller协议可以被恶意使用。具体来说，攻击者可以欺骗App Installer来安装一个用户并不打算安装的软件包。</p><p>目前，我们已经禁用了ms-appinstaller方案（协议）。这意味着App Installer将不能直接从网络服务器上安装一个应用程序。相反，用户将需要首先将应用程序下载到他们的设备上，然后用App Installer安装该软件包。这可能会增加一些软件包的下载大小。</p></blockquote><p><strong>以下是在网站上禁用该协议的方法：</strong></p><blockquote><p>如果你在你的网站上利用了ms-appinstaller协议，我们建议你更新你的应用程序的链接，删除'ms-appinstaller:?source='字段，这样MSIX包或App Installer文件就会下载到用户的机器上再安装。</p></blockquote><p>微软还表示，它正在研究如何在未来某个时候以安全的方式重新启用该协议，比如添加某些组策略。但就目前而言，上述的变通方法是防止恶意攻击的临时解决方案。</p><blockquote><p>我们正在花时间进行彻底的测试，以确保能够以安全的方式重新启用该协议。我们正在研究引入一个组策略，允许IT管理员重新启用该协议并控制其在组织内的使用。</p></blockquote><p><strong>你可以在官方公告中找到更多细节：</strong></p><p><a href="https://techcommunity.microsoft.com/t5/windows-it-pro-blog/disabling-the-msix-ms-appinstaller-protocol-handler/ba-p/3119479" _src="https://techcommunity.microsoft.com/t5/windows-it-pro-blog/disabling-the-msix-ms-appinstaller-protocol-handler/ba-p/3119479" target="_blank">https://techcommunity.microsoft.com/t5/windows-it-pro-blog/disabling-the-msix-ms-appinstaller-protocol-handler/ba-p/3119479</a><br></p>   
</div>
            