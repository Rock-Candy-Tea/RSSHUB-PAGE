
---
title: '新发现的Mirai Botnet正在操纵各类物联网设备进行DDoS攻击'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0706/e16779834dc06e6.png'
author: cnBeta
comments: false
date: Tue, 06 Jul 2021 12:54:42 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0706/e16779834dc06e6.png'
---

<div>   
<strong>网络安全专家披露了有关一个新发现的受Mirai启发的僵尸网络"mirai_ptea"的细节。它利用了KGUARD提供的数字录像机（DVR）中一个未公开的缺陷，传播并执行分布式拒绝服务（DDoS）攻击。</strong>中国安全公司360在2021年3月23日对缺陷进行了首次调查，然后在2021年6月22日检测到积极的僵尸网络企图。<br>
<p>自2016年Mirai僵尸网络出现以来，它已经与一系列大规模的DDoS攻击有关。</p><p>2016年10月，欧洲和北<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://mideajiadian.jd.com/" target="_blank">美的</a>DNS服务提供商Dyn的用户失去了对主要互联网平台和服务的访问。从那时起，Mirai的众多版本涌现，部分原因是源代码在互联网上可以获得，Mirai_ptea也不例外。</p><p>据研究人员称，Mirai僵尸网络是一个新型的基于物联网（IoT）设备的恶意软件，它入侵了30万个物联网设备，如无线摄像头、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,699,700" target="_blank">路由器</a>和数字录像机。它扫描物联网设备并使用默认密码，然后将密码添加到僵尸网络中，然后用来对网站和互联网基础设施发动DDoS攻击。</p><p>网络安全研究人员没有透露有关安全漏洞的全部细节，以防止进一步的利用，但研究人员说，KGUARD DVR固件在2017年之前有脆弱的代码，可以在没有认证的情况下远程执行系统命令。至少有大约3000台在线发布的设备容易受到这个漏洞的影响。</p><p><a href="https://static.cnbetacdn.com/article/2021/0706/e16779834dc06e6.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0706/e16779834dc06e6.png" title alt="Snip20210629_1.png" referrerpolicy="no-referrer"></a></p><p>除了使用Proxy与命令和控制（C2）服务器连接外，对mirai_ptea样本的分析还披露了对所有敏感资源信息的广泛加密。它被解码以建立与C2服务器的连接，并检索攻击命令以执行，包括发起DDoS攻击。</p><p>"僵尸源IP的地理分布[......]主要集中在美国、韩国和巴西，"研究人员说，据报告，感染者遍布欧洲、亚洲、澳大利亚、北美和南美，以及非洲部分地区。</p><p>2017年，新泽西州范伍德的21岁的帕拉斯·贾、宾夕法尼亚州华盛顿的20岁的约西亚-怀特和路易斯安那州梅泰里的21岁的道尔顿-诺曼因创建Mirai物联网僵尸网络而被起诉。这三人承认共谋违反了《计算机欺诈和滥用法》。</p><p><strong>阅读中文报告全文：</strong></p><p><a href="https://blog.netlab.360.com/mirai_ptea-botnet-is-exploiting-undisclosed-kguard-dvr-vulnerability/" _src="https://blog.netlab.360.com/mirai_ptea-botnet-is-exploiting-undisclosed-kguard-dvr-vulnerability/" target="_blank">https://blog.netlab.360.com/mirai_ptea-botnet-is-exploiting-undisclosed-kguard-dvr-vulnerability/</a><br></p>   
</div>
            