
---
title: '安全专家发现ATM机NFC功能漏洞，仅用一台手机就可改变金额，甚至强制提现'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210630/v2_5f877342f2154b9e81d4207799590e56_img_000'
author: 36kr
comments: false
date: Wed, 30 Jun 2021 11:14:01 GMT
thumbnail: 'https://img.36krcdn.com/20210630/v2_5f877342f2154b9e81d4207799590e56_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/wfD1YXgBftgcblr2gN1guQ">“大数据文摘”（ID:BigDataDigest）</a>，作者：王烨，36氪经授权发布。</p> 
<p>你有多久没去ATM取过钱了？</p> 
<p>由于移动支付的诞生，中国民众现在出门很少带现金了，为了跟上“移动化”的潮流，银行的ATM机经过不断升级已经有了NFC、无卡取款甚至是刷脸取款。</p> 
<p>从诞生之初，ATM就一直被不法分子觊觎，毕竟ATM里面有大量现金，附近还无人值守，是一个天然吸引犯罪的地方。</p> 
<p>一般来说，银行在考虑到ATM存在被抢风险的情况下，都会把ATM机建造的很坚固，但是依然有人选择“硬来”；</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_5f877342f2154b9e81d4207799590e56_img_000" data-img-size-val="360,202" referrerpolicy="no-referrer"></p> 
<p>当然，也有人选择智取。近期，一位安全公司的研究人员发现了现在ATM机中NFC功能的漏洞，利用这个漏洞，可以修改交易金额，甚至可以让ATM直接吐钱。</p> 
<h2 label="一级标题" style>安全顾问入侵ATM机多，修改金额只需一部手机</h2> 
<p>安全公司IOActive的研究员和顾问何塞普·罗德里格斯（Josep Rodriguez）去年开始一直在挖掘和报告所谓的NFC芯片的漏洞，这些芯片被用于全球数百万台ATM机。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_c1bede365db2479a8b7fb7875ab84382_img_000" data-img-size-val="937,373" referrerpolicy="no-referrer"></p> 
<p>在ATM机上，NFC功能可以让你在ATM机上挥动银行卡，而不是刷卡或插入银行卡，从而进行支付或从提款机中取钱。</p> 
<p>为此，罗德里格斯开发了一个Android应用程序，可以让他的智能手机模仿银行卡的NFC通信功能，并利用NFC系统固件中的缺陷入侵ATM机或者销售点终端。</p> 
<p>也就是说，仅仅利用一部智能手机，罗德里格斯就可以侵入ATM机或者销售点终端收集和传输银行卡数据，悄悄地改变交易数额，甚至锁定设备。</p> 
<p>罗德里格斯说，他甚至可以强迫至少一个品牌的ATM机直接支付现金ーー由于与ATM供应商签订了保密协议，他拒绝详细说明或公开披露这些漏洞。</p> 
<p>“例如，你可以修改固件并将价格改为1美元，即使屏幕显示你要支付50美元。你可以使设备失效，或者安装一种勒索软件。这有很多可能性，”罗德里格斯表示，“如果你发动连锁攻击，并向ATM机的处理器发送一个特殊的有效载荷，你就可以在ATM机上找到突破口——比如提现。”</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_cdba9f562bd14d2d874f892fcfd8349d_img_000" data-img-size-val="800,450" referrerpolicy="no-referrer"></p> 
<p>罗德里格斯担任顾问多年来一直在测试ATM机的安全性。他表示，一年前他开始探索ATM机的NFC是否可以成为黑客入侵的捷径。</p> 
<p>NFC读卡器通常由支付技术公司ID tech销售，罗德里格斯从eBay上购买NFC阅读器和销售点设备，很快发现其中许多都有同样的安全缺陷——他们没有验证通过NFC从银行卡发送到读卡器的数据包（APDU）大小。</p> 
<p>因此，罗德里格斯创建了一个定制的应用程序，通过他的支持NFC的Android手机向ATM机或销售点设备发送一个精心制作的APDU，这个程序比设备预期的要大几百倍，这样，罗德里格斯能够触发一个“缓冲区溢出”（buffer overflows），这是一种有几十年历史的软件漏洞，黑客可以利用该漏洞破坏目标设备的内存，并运行自己的代码。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_ca5f2511e0b94ec1b97ce53d77024123_img_000" data-img-size-val="605,186" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>多家ATM机供应商受影响，打补丁需要很长时间</h2> 
<p>罗德里格斯说，他在7个月至1年前通<a class="project-link" data-id="34661" data-name="知了" data-logo="https://img.36krcdn.com/20200729/v2_43a759f031664fbb84fd810d8e620f06_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/34661" target="_blank">知了</a>受影响的ATM机和销售点终端供应商，其中包括ID Tech、Ingenico、Verifone、Crane Payment Innovations、BBPOS、Nexgo，以及未透露姓名的ATM供应商。</p> 
<p>即便如此，他警告称，受影响的系统数<a class="project-link" data-id="629729" data-name="量之" data-logo="https://img.36krcdn.com/20201107/v2_e8475c59dec2413fb14114f385aed6d9_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/629729" target="_blank">量之</a>多，以及许多销售点终端和ATM机不会定期接收软件更新，而且在许多情况下需要物理访问才能进行更新，这意味着这些设备中的许多可能仍然容易受到攻击。</p> 
<p>罗德里格斯说：“给成千上万的自动取款机打补丁，这需要很多时间。”</p> 
<p>为了展示这些挥之不去的漏洞，罗德里格斯与《连线》杂志分享了一段视频，视频中，他在自己居住的马德里街头的一台ATM机的NFC感应区上挥舞一部智能手机，并让这台机器显示<a class="project-link" data-id="3969340" data-name="一条" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969340" target="_blank">一条</a>错误信息。</p> 
<p>罗德里格斯要求《连线》杂志不要发布这段视频，因为担心承担法律责任。他也没有提供劫机攻击的视频演示，因为他说，他只能在IOActive向受影响的ATM供应商提供安全咨询的机器上进行合法测试，IOActive已经与该供应商签署了保密协议。</p> 
<p>安全公司SRLabs的创始人、著名的固件黑客卡斯滕·诺尔（Karsten Nohl）回顾了罗德里格斯的工作，他说，这些发现是“对嵌入式设备上运行的软件脆弱性的极好研究”。但是诺尔也指出了这项发现的一些局限性，正是这些局限降低了它在现实世界中被不法分子利用的可能性。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_09862b31b0364387b7676f43388226fb_img_000" data-img-size-val="1080,608" referrerpolicy="no-referrer"></p> 
<p>诺尔指出，被入侵的NFC读卡器只能窃取信用卡的磁条数据，而不能窃取受害者的个人识别码或EMV芯片中的数据。事实上，ATM提现还要求目标ATM的代码有一个额外的、明显的漏洞。</p> 
<p>当《连线》联系受影响的公司时，ID Tech、BBPOS和Nexgo没有回应置评请求，ATM行业协会也拒绝置评。</p> 
<p>Ingenico公司在一份声明中回应说，由于它的安全缓解措施，罗德里格斯的缓冲区溢出技术只能使其设备崩溃，而不能执行攻击代码，但是，“考虑到给我们的客户带来的不便和影响，”Ingenico还是发布了一个补丁。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_cb31624511b34df1ab2d8498504ff7f7_img_000" data-img-size-val="480,270" referrerpolicy="no-referrer"></p> 
<p>Verifone公司则表示，早在罗德里格斯报告之前，他们就已经发现并修复了罗德里格斯在2018年指出的漏洞。但罗德里格斯说，他去年在一家餐馆的Verifone设备上测试了他的NFC攻击技术，发现它仍然很脆弱。</p> 
<p><img src="https://img.36krcdn.com/20210630/v2_0e9014eeb63746e4b49c80520a1a7e92_img_000" data-img-size-val="1000,667" referrerpolicy="no-referrer"></p> 
<p>在保密了整整一年之后，罗德里格斯计划在未来几周的网络研讨会上分享漏洞的技术细节，部分原因是为了让受影响厂商的客户引起重视。他希望更广泛地呼吁人们关注嵌入式设备安全的糟糕状况，他发现，像缓冲溢出这样简单的漏洞存在于如此之多的常用设备中ーー这些设备正处理着人们敏感的财务信息。</p> 
<p>“这些漏洞已经存在多年，我们每天都在使用这些设备来处理我们的信用卡，我们的钱，”他说。“它们需要<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>保护。”</p>  
</div>
            