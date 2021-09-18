
---
title: '微软发布的PrintNightmare修复程序再次破坏企业打印机正常使用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0918/6b8c5a564f0b65d.webp'
author: cnBeta
comments: false
date: Sat, 18 Sep 2021 14:39:53 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0918/6b8c5a564f0b65d.webp'
---

<div>   
因为 PrintNightmare 漏洞问题微软已经花费几个月进行修复，此漏洞危害较高并且在修复方面也是相当麻烦的。微软在本周推出的累积更新里对此安全漏洞进行最后的收尾，按微软说明此次收尾工作解决四个潜在的安全问题。<br>
<p>好消息是漏洞可能已经被成功修复了，坏消息是此次<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>推出的修复程序再次导致大量企业打印机无法正常使用。</p><p>每次用户尝试打印时系统都会弹出提示要求填写管理员凭据，后经微软调查此故障与打印机使用的驱动程序有关。</p><p><a href="https://img.lancdn.com/landian/public/thumb/Windows10.png" rel="nofollow"><img src="https://static.cnbetacdn.com/article/2021/0918/6b8c5a564f0b65d.webp" title alt="2021-09-15-image-3-p.webp" referrerpolicy="no-referrer"></a></p><p><strong>问题说明：</strong></p><p>安装KB5005033或后续更新后在某些使用 Point and Print 的环境中 , 某些打印机可能会显示信任打印机的提示。</p><p>同时当用户通过应用程序尝试访问打印服务器或打印客户端连接时，需要提供管理员凭据才能安装到打印服务器。</p><p>发生此故障的原因是打印客户端和打印服务器上使用相同文件名的打印驱动导致，但服务器具有较新版本的文件。</p><p>当打印客户端尝试连接到打印服务器时，会自动发现新驱动文件并提示更新打印客户端上的驱动程序但存在冲突。</p><p><img src="https://static.cnbetacdn.com/article/2021/0918/66a70875e411e92.webp" title alt="2021-09-15-image-35-j.webp" referrerpolicy="no-referrer"></p><p><strong>解决方案：</strong></p><p>首先企业需确保打印设备均使用最新的驱动程序，如果可能的话请在打印客户端和服务器上使用相同版本的驱动。</p><p>企业可以在环境里调整打印机驱动程序，如果在环境里更新驱动程序依然无法解决问题的话请联系打印机制造商。</p><p>受影响的平台包括<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 所有版本、Windows 8.1 所有版本、Windows 7、Windows Server 所有版本。</p><p>如需帮助请联系打印机制造商或参见 KB5005652 号更新的常见问题部分中的Q1/A1部分：<a href="https://support.microsoft.com/en-us/topic/kb5005652-manage-new-point-and-print-default-driver-installation-behavior-cve-2021-34481-873642bf-2634-49c5-a23b-6d8e9a302872" target="_blank" rel="noopener">KB5005652 Q1/A1</a>。</p>   
</div>
            