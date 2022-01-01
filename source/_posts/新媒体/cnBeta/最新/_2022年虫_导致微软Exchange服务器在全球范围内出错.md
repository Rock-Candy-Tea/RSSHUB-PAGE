
---
title: '_2022年虫_导致微软Exchange服务器在全球范围内出错'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0101/e86ecb25ec46600.png'
author: cnBeta
comments: false
date: Sat, 01 Jan 2022 13:13:14 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0101/e86ecb25ec46600.png'
---

<div>   
许多企业网管的新年庆祝活动被公司邮件系统的一条错误报告报告打断了，他们的Exchange服务器出现了"FIP-FS扫描引擎加载失败 - 无法将"2201010001"转换为长（2022/01/01 00:00 UTC）"的错误。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0101/e86ecb25ec46600.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0101/e86ecb25ec46600.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p>这个问题似乎是由于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>使用更新版本的前两个数字来表示更新的年份，这导致日期的"长"版本溢出。</p><p>目前，似乎主要的解决方法是通过使用Set-MalwareFilteringServer -BypassFiltering $True -identity <server name>禁用Exchange服务器上的反恶意软件扫描器，并重新启动Microsoft Exchange Transport服务。</p><p>这是一个有趣的“2022年虫”问题，微软目前还没有确认这个问题，但作为网络管理员的你如果受到影响，在Reddit这里可以得到一些同行的支持：</p><p><a href="https://www.reddit.com/r/sysadmin/comments/rt91z6/exchange_2019_antimalware_bad_update/" _src="https://www.reddit.com/r/sysadmin/comments/rt91z6/exchange_2019_antimalware_bad_update/" target="_blank">https://www.reddit.com/r/sysadmin/comments/rt91z6/exchange_2019_antimalware_bad_update/</a><br></p>   
</div>
            