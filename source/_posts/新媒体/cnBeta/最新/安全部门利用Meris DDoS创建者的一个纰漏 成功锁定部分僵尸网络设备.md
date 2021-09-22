
---
title: '安全部门利用Meris DDoS创建者的一个纰漏 成功锁定部分僵尸网络设备'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0922/571bf8cdd17bda9.jpg'
author: cnBeta
comments: false
date: Tue, 21 Sep 2021 23:42:56 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0922/571bf8cdd17bda9.jpg'
---

<div>   
<strong>俄罗斯电信巨头 Rostelecom 旗下网络安全部门 Rostelecom-Solar 周一表示，发现并利用恶意软件创建者的一个纰漏，成功封锁了 Meris DDoS 僵尸网络部分设备。</strong>Meris 僵尸网络在今年早些时候首次被发现，是目前互联网上最大的 DDoS 僵尸网络，其规模估计约为 25 万个受感染的系统。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0922/571bf8cdd17bda9.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0922/571bf8cdd17bda9.jpg" alt="7w946jyk.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在过去几个月里，该僵尸网络被攻击者滥用，对俄罗斯、英国、美国和新西兰等几个国家的互联网服务提供商和金融实体进行了 DDoS 勒索攻击。由于这些勒索攻击，很多公司因为僵尸网络的巨大威力而被迫下线。其中最凶猛的几次攻击，Meris 今年两次打破了最大容量 DDoS 攻击的记录，一次是在 6 月，另一次是在 9 月。</p><p style="text-align: left;">Cloudflare 和 Qrator 实验室等互联网基础设施公司在其客户受到攻击后对该僵尸网络进行了分析，发现绝大多数受感染的系统都是 MikroTik 网络设备，如<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,699,700" target="_blank">路由器</a>、交换机和接入点。</p><p style="text-align: left;">在上周的一篇博文中，MikroTik表示，攻击者滥用了其RouterOS中的一个旧漏洞（CVE-2018-14847），利用业主尚未更新的设备组装了他们的僵尸网络。</p><p style="text-align: left;">但在周一发表的研究报告中，Rostelecom-Solar 表示，在对这种新的威胁（也一直在攻击其一些客户）进行例行分析时，其工程师发现，一些受感染的路由器正在向一个未注册的域名 cosmosentry[.com] 伸出援手，要求提供新的指令。</p><p style="text-align: left;">Rostelecom-Solar的工程师说，他们抓住了运营商的错误，注册了这个域名并将其转化为一个“天坑”（sinkhole）。经过几天的追踪，研究人员说他们收到了来自约 45000 台受感染的 MikroTik 设备的 ping，这个数字估计约为僵尸网络整个规模的五分之一。</p><p style="text-align: left;">该公司本周说：“不幸的是，我们不能对我们控制下的设备采取任何积极行动（我们没有权力这样做）。目前，大约 45,000 台 MikroTik 设备转向我们的天坑域”。</p><p style="text-align: left;">为了防止MikroTik路由器所有者检测到这些与cosmosentry[.]com的可疑连接，Rostelecom-Solar表示，他们已经设置了一个占位符信息，告知他们谁拥有这个域名以及为什么他们的路由器会进行连接。</p><p style="text-align: left;">此外，研究人员表示，他们还在Meris恶意软件的代码中发现了一些线索，这些线索也让人了解到这个僵尸网络是如何被组装起来的。根据 Rostelecom-Solar 团队的说法，Meris僵尸网络似乎是通过Glupteba组装的，这是一种针对<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>电脑的恶意软件，通常被用作其他各种恶意软件的加载器。</p><p style="text-align: left;">Meris代码的相似性以及许多使用内部IPping Rostelecom天坑的路由器证实了该公司的理论，即Meris是通过Glupteba恶意软件完全或部分组装的。然而，目前还不清楚是Glupteba团伙自己建立了Meris僵尸网络，还是另一个团伙租用了Glupteba感染的主机来部署MikroTik模块，最终产生 Meris。</p>   
</div>
            