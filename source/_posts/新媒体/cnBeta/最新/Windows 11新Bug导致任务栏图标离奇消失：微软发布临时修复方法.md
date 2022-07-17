
---
title: 'Windows 11新Bug导致任务栏图标离奇消失：微软发布临时修复方法'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0717/943ab701ae194c5.png'
author: cnBeta
comments: false
date: Sun, 17 Jul 2022 07:47:04 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0717/943ab701ae194c5.png'
---

<div>   
近日，有用户在微软反馈中心提交了新的Bug，表示自己的Windows 11系统任务栏图标因为不明原因“离奇消失”，并且找不到修复方法。目前，<strong>微软已经对该Bug做出了回应，明确Bug原因的同时，给出了临时修复方法。</strong><br>
 <p><a href="https://img1.mydrivers.com/img/20220717/6c8fda3ef3d349c9a5de8aa52500f3bc.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/0717/943ab701ae194c5.png" referrerpolicy="no-referrer"><br></a></p><p>据悉，该Bug的罪魁祸首是<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11的IRIS服务，该服务疑似与Windows聚焦等功能有关，但<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>从未明确承认过。</p><p>想要修复该Bug，需要用管理员模式打开命令符管理器（CMD），然后输入命令<strong>“<strong>reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\IrisService /f && shutdown -r -t 0</strong>”</strong>。</p><p><a href="https://img1.mydrivers.com/img/20220717/b529e632c0be41838098f712e8130649.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/0717/f15cd21382fe98b.jpg" referrerpolicy="no-referrer"><br></a></p><p>该命令会删除IRIS服务的注册表值，从而解决问题。</p><p>一般来说，在输入该命令后，系统会自动重启，在开机后问题就会得到解决。</p><p>值得一提的是，<strong>早在2020年，Windows 10就曾出现过任务栏不显示图标的Bug</strong>，不过当时出现问题的诱因是设备内存不足。</p>   
</div>
            