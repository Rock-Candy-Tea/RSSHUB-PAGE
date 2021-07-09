
---
title: '新发现的Bandidos恶意软件变身Chrome插件瞄准南美洲商业网络'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0709/e2cb53b53cde3e3.jpg'
author: cnBeta
comments: false
date: Fri, 09 Jul 2021 14:52:54 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0709/e2cb53b53cde3e3.jpg'
---

<div>   
<strong>ESET的网络安全研究人员昨天披露了一项针对南美商业网络的恶意软件间谍活动，其中大部分行动集中在委内瑞拉。Bandidos是Bandook的改进版，这种恶意软件旨在针对医疗保健、软件服务、零售、制造和建筑等行业的企业。</strong>Bandook由Dark
Caracal开发，在2015年至2017年间被用来收集情报，该组织声称代表哈萨克斯坦和黎巴嫩政府利益行事。<br>
 <p>根据对最新攻击的连锁分析，潜在受害者的个人电脑可以通过打开包含PDF附件的恶意电子邮件而受到感染。该邮件提供了下载托管在pCloud、Spideroak或Google Cloud上的档案包的网址，以及解压所需的密码。解开下载的文件会暴露出一个恶意软件载荷，并将其注入正在运行的Internet Explorer会话。</p><p>在ESET检查的最新形式的Bandook中总共检测到132个命令，比Check Point能识别的多12个。这表明，该感染背后的网络犯罪组织正在不断发展其恶意工具，以使其具有更多的能力和影响力。</p><p>ESET的网络安全研究员Fernando Tavella解释说，该恶意软件的巧妙之处在于它利用了浏览器扩展和凭证，这个被称为ChromeInject的功能是其能够快速传播的主要原因。当与攻击者的命令和控制服务器建立通信时，有效载荷会下载一个DLL文件，该文件可以导出并创建一个恶意的Chrome扩展，该恶意扩展试图检索受害者提交给URL的任何凭证，然后这些凭证被存储在Chrome的本地存储中。</p><p>该恶意软件的功能极其丰富，其载荷能够进行文件修改，捕捉屏幕截图，控制受害者电脑上的鼠标指针，列出目录内容，终止正在运行的进程，安装恶意DLL文件，从受感染的电脑上卸载自己，从特定的网络地址下载恶意文件，甚至将收集的信息发送到远程服务器。</p><p><a href="https://static.cnbetacdn.com/article/2021/0709/e2cb53b53cde3e3.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0709/e2cb53b53cde3e3.jpg" title alt="bandidos-malware-targeting-networks-in-south-america-533485-3.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            