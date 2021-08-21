
---
title: '巴基斯坦军方被名叫_Confucius _的黑客组织用Pegasus引诱为目标'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0821/fd9c3fa2e821f38.jpg'
author: cnBeta
comments: false
date: Sat, 21 Aug 2021 07:44:06 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0821/fd9c3fa2e821f38.jpg'
---

<div>   
<strong>网络安全公司趋势科技（Trend Micro）发现了名叫Confucius的网络犯罪团伙最近进行的恶意活动。</strong>黑客们利用臭名昭著的以色列Pegasus（飞马恶意软件）诱饵发起了一场钓鱼活动，欺骗用户点击下载数据盗窃代码的恶意文件。<br>
 <p>攻击以一封干净的电子邮件开始，其中包含从巴基斯坦合法报纸文章中复制的文字。两天后，受害者收到一封新的电子邮件，其中包含冒充巴基斯坦军方官员关于Peg<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://asus.jd.com/" target="_blank">ASUS</a>间谍软件的警告，其中包括一个cutt.ly链接到加密的Word文档和一个解密密码。</p><p><a href="https://static.cnbetacdn.com/article/2021/0821/fd9c3fa2e821f38.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0821/fd9c3fa2e821f38.jpg" title alt="confucius-pegasus-spyware-1.jpg" referrerpolicy="no-referrer"></a></p><p>无论受害者采取什么行动，点击其中任何一个链接都会下载Word文档。如果目标人物输入了电子邮件中的密码，电脑屏幕上就会出现一个带有宏的文档。如果该特定机器上启用了宏，下一步就是简单地加载恶意代码。一个名为skfk.txt的.NET DLL文件就会在临时目录中被创建，该文件包含文档注释栏的材料。PowerShell被用来将该文件加载到内存中，并用于窃取数据。</p><p><a href="https://static.cnbetacdn.com/article/2021/0821/b004b250ec89fcd.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0821/b004b250ec89fcd.jpg" title alt="confucius-pegasus-spyware-2.jpg" referrerpolicy="no-referrer"></a></p><p>简单地说，当列出的扩展名的MD5哈希值匹配时，该文件就会通过C&C服务器被检索出来。没有列出的文件被保存到同一C&C服务器的不同文件夹，使用机器名对应用户名字符串。</p><p><a href="https://static.cnbetacdn.com/article/2021/0821/187f2d309468f9a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0821/187f2d309468f9a.jpg" title alt="confucius-pegasus-spyware-3.jpg" referrerpolicy="no-referrer"></a></p><p>“Confucius”网络犯罪团伙过去曾使用几个文件窃取工具对巴基斯坦军队进行网络间谍攻击。开发者在创建恶意文件时使用创新技术，其中一些技术包括使用加密文件来防止自动分析，或将有害代码隐藏在评论部分。</p><p><a href="https://static.cnbetacdn.com/article/2021/0821/f41ed297bf0b792.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0821/f41ed297bf0b792.jpg" title alt="confucius-pegasus-spyware-5.jpg" referrerpolicy="no-referrer"></a></p><p><strong>访问趋势科技博客以了解更多细节：</strong></p><p><a href="https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html" _src="https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html" target="_blank">https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html</a><br></p>   
</div>
            