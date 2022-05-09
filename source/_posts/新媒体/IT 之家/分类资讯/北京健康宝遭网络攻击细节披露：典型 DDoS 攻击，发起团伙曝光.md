
---
title: '北京健康宝遭网络攻击细节披露：典型 DDoS 攻击，发起团伙曝光'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/5/1cc938be-eb43-48ed-9531-12629e6cc6f8.png'
author: IT 之家
comments: false
date: Mon, 09 May 2022 05:47:58 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/5/1cc938be-eb43-48ed-9531-12629e6cc6f8.png'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1649408" rel="nofollow">蓝海岸Nibiru</a> 的线索投递！</div>
            <p data-vmark="5061"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 5 月 9 日消息，今日，360 网络安全研究院披露了北京健康宝被网络攻击的部分细节信息。通过其积累的安全威胁数据，可以确定<strong>这次事件的发起方是其内部命名为 Rippr 的团伙</strong>。<strong>该团伙使用了已经披露过的恶意代码家族 Fbot 作为攻击武器</strong>。此次事件的 Fbot 变种，最早发现于 2 月 10 日，自被发现以来就异常活跃地参与到 DDoS 攻击中。截至今日，短短三个月，<strong>被跟踪到的攻击事件就超过 15 万次</strong>。</p><p data-vmark="7d03">据人民日报此前报道，4 月 28 日，在北京召开的第 318 场疫情防控新闻发布会上，北京市委宣传部对外新闻处副处长隗斌通报，4 月 28 日，<strong>北京健康宝使用高峰期遭受网络攻击</strong>，经初步分析，网络攻击源头来自境外，北京健康宝保障团队进行及时有效应对，受攻击期间，北京健康宝相关服务未受影响。</p><p data-vmark="aa54">IT之家了解到，360 网络安全研究院表示，<strong>可以确认这是一起典型的网络拒绝服务攻击（DDoS 攻击）事件</strong>，也就是说攻击者利用大量被入侵的网络设备，如 IOT 设备、个人电脑、服务器等，向受害者服务器发送海量的网络流量，影响其正常服务。</p><p data-vmark="88cf" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/5/1cc938be-eb43-48ed-9531-12629e6cc6f8.png" w="1080" h="230" alt="BotMon 系统截获的原始攻击指令" title="北京健康宝遭网络攻击细节披露：典型 DDoS 攻击，发起团伙曝光" width="1080" height="175" referrerpolicy="no-referrer"></p><p data-vmark="e683" style="text-align: center;">▲ BotMon 系统截获的原始攻击指令，目标 IP 已做打码处理 | 图源：360 网络安全研究院</p><p data-vmark="5fec">据介绍，从攻击时间上来看，指令发出的时间是 28 号早上 8 点 41。从攻击方法上来看，使用了 360 网络安全研究院内部命名为 ATK_256，ATK_261 的 DDoS 攻击方式。</p><p data-vmark="1f86">该僵尸网络将涉事的 3 个 C2 域名通过 DNS 域名映射到多个 IP 的方式做负载均衡。通过从这 3 个 C2 的历史攻击指令发现的一些基本特征和对该家族运营团伙 Rippr 历史认识，360 网络安全研究院认为<strong>它的主要目的是通过对外提供 DDoS 服务，以及挖矿来盈利，不涉及政治诉求</strong>。</p><p data-vmark="95ec">360 网络安全研究院指出，截至目前为止，<strong>该僵尸网络在全球范围内依然活跃</strong>，预期随着本次报告登出，涉及的 C2 和恶意样本会被安全社区提取使用，黑客也许会通过再一次更新 C2 地址来应对。</p>
          
</div>
            