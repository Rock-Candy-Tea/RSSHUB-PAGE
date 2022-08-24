
---
title: 'VMware承认Carbon Black EDR近期更新导致Windows设备蓝屏_循环重启'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0824/155d26c966c3749.webp'
author: cnBeta
comments: false
date: Wed, 24 Aug 2022 09:38:24 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0824/155d26c966c3749.webp'
---

<div>   
<strong>VMware 近日承认，使用 Carbon Black Endpoint Detection and Response (EDR)解决方案的企业 Windows 用户，可能会遇到蓝屏或者循环重启的问题。</strong>在今天早些时候发布的安全公告中，该公司表示承认导致这些问题的原因是近期为 Carbon Black 发布的威胁研究规则集。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0824/155d26c966c3749.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0824/5df386a49e94993.png" referrerpolicy="no-referrer"></p><p style="text-align: left;">受到影响的企业用户可以通过回滚更新的方式进行解决。此外，该公司还提供了临时解决方法：</p><blockquote style="text-align: left;"><p style="text-align: left;">Endpoint Standard: 在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 设备上出现突然的蓝屏（2022 年 8 月 23 日）</p><p style="text-align: left;"><strong>环境：</strong></p><p style="text-align: left;">Carbon Black Cloud Console: All Versions</p><p style="text-align: left;">Carbon Black Cloud Sensor: 3.6.x.x - 3.7.x.x</p><p style="text-align: left;">Microsoft Windows: All Support Versions</p><p style="text-align: left;"><strong>症状：</strong></p><p style="text-align: left;">设备在启动时进入蓝屏</p><p style="text-align: left;">停止代码可能会显示“PFN_LIST_CORRUPT”</p><p style="text-align: left;"><strong>导致</strong></p><p style="text-align: left;">在内部测试未显示问题迹象后，更新的威胁研究规则集已推广到 Prod01、Prod02、ProdEU、ProdSYD 和 ProdNRT</p><p style="text-align: left;"><strong>解析</strong></p><p style="text-align: left;">VMware Carbon Black 已回滚规则集，当机器签入时，它们将获得更新的规则集并自动解析。</p><p style="text-align: left;"><strong>临时解决方法</strong></p><p style="text-align: left;">通过 Carbon Black Cloud Console 将受影响的传感器置于旁路模式，以允许它们成功启动并删除规则集</p><p style="text-align: left;">一小部分受影响的设备可能需要额外的解决方法，需要重新启动到安全模式，如果是这样，请打开如下所示的支持案例</p></blockquote>   
</div>
            