
---
title: '勒索过苹果的黑客REvil又来了？这次是7000万美元赎金'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210708/v2_4f4515b67f96436cb1edad90cd8adce8_img_000'
author: 36kr
comments: false
date: Thu, 08 Jul 2021 09:11:59 GMT
thumbnail: 'https://img.36krcdn.com/20210708/v2_4f4515b67f96436cb1edad90cd8adce8_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/seNi2l-EXPCNgjtSfXIfaA">“CSDN”（ID:CSDNnews）</a>，作者：Carol，36氪经授权发布。</p> 
<p>上周五，美国软件开发商 Kaseya Ltd. 遭遇了勒索软件 REvil 的攻击，攻击主要集中在 Kaseya VSA 软件上，这次攻击影响了多个托管服务提供商及其一千多名客户。</p> 
<p><img src="https://img.36krcdn.com/20210708/v2_4f4515b67f96436cb1edad90cd8adce8_img_000" data-img-size-val="600,400" referrerpolicy="no-referrer"></p> 
<p>Kaseya 是一家来自瑞典的 IT 公司，于1999年获得了美国专利局认证的 Kaseya VSA（虚拟系统管理）专利和连接算法专利。Kaseya VSA 是一个基于云的 MSP 平台，允许提供商为其客户执行补丁管理和客户端监控，该平台为客户提供了一套基于 Web 的新一代自动化 IT 系统管理解决方案。MSP 是一种通过建立自己的网络运作中心(NOC，Network Operating Center)来为企业提供24×7×365的系统管理服务的业务。MSP 可以实现远程的管理、实时的监控和对企业系统运作情况的统计。</p> 
<p>为了获得更好的服务，在对 MSP 进行选择时，企业一般会选择有强大的市场占有率的产品品牌。Kaseya 就是这样一个品牌，至今，Kaseya 在全球已经拥有了超过10000家客户，其中包括50%以上的全球100强 IT 管理服务提供商及各大龙头企业，分别来自银行业、金融业、零售业、贸易业、教育机构、政府机构、医疗机构和交通运输业等领域。截止2011年底，全球有超过1300万台以上的终端和设备通过 Kaseya 的软件进行管理。</p> 
<h2 data-foldable-wrapper></h2> 
<h2 label="一级标题" style>为什么是 Kaseya？</h2> 
<p>正是因为很多大型企业和技术服务供应商都选择使用 Kaseya VSA，Kaseya 才被选中成为此次供应链攻击的对象。</p> 
<p>供应链攻击是一种面向软件开发人员和供应商的攻击方式。攻击者通过在应用中寻找不安全的网络协议、未受保护的服务器基础结构和不安全的编码做法，来感染合法应用，分发恶意软件。</p> 
<p>一般来说，软件由受信任的供应商构建和发布, 因此这些应用和更新版本已被签名并经过相关安全认证。在软件供应链攻击中, 供应商可能未意识到他们的应用或更新在发布到公众时已经受到恶意代码的感染，因此一旦供应链攻击成功，恶意代码将以与应用相同的信任和权限运行。</p> 
<p>MSP 对于勒索软件团伙来说是一个高价值的目标，它们提供了一种通过单一漏洞感染许多公司的简单渠道，但发起攻击需要黑客对 MSP 及其使用的软件有深入了解。</p> 
<p>REvil 就是个中好手。REvil 拥有一个精通 MSP 使用的技术的分支机构，长期以来一直针对这些公司及其常用软件进行研究。与其他勒索软件一样，REvil 的勒索软件会锁住受害者的电脑，直到受害者以比特币的形式支付数字赎金。</p> 
<p><img src="https://img.36krcdn.com/20210708/v2_23a09e1b846144279b6290ae3a88c0fb_img_000" data-img-size-val="1080,636" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>REvil 勒索软件示例</p> 
<h2 data-foldable-wrapper></h2> 
<h2 label="一级标题" style>Kaseya 是否会支付赎金？</h2> 
<p>REvil 不仅精心挑选了他们的猎物，为保万无一失，他们甚至精心挑选了攻击时间。通常来说，多数大规模勒索软件攻击都是在周末的深夜进行，因为此时监控网络的人员较少。REvil 却选择在周五中午发起攻击，在即将到来的周末之前，员工的工作时间可能缩短且效率不高。</p> 
<p>REvil 精心策划的攻击实施得相当顺利。周五，Kaseya 收到了客户的报告，报告显示 Kaseya VSA 本地产品管理的端点出现了异常行为，不久后，Kaseya 进一步发现勒索软件正在端点上执行。基于用户的报告， Kaseya 的执行团队迅速召开了会议并决定采取两个步骤来阻止恶意软件的传播：向本地客户发送通知，要求用户关闭他们的 VSA 服务器以及关闭 Kaseya 的 VSA SaaS 基础设施。</p> 
<p>通过调查，Kaseya 的安全团队发现勒索软件使用了 Kaseya VSA 中的一个漏洞，并宣布将尽快发布补丁。据称，此次网络攻击是 REvil 有史以来发起的规模最大的一次攻击，已有八个已知的大型 MSP 受到攻击，并且可能已导致全球多达 4 万台电脑被感染。</p> 
<p>根据暗网博客上发布的信息，REvil 勒索软件团伙声称已经锁定了超过 100 万个系统。</p> 
<p><img src="https://img.36krcdn.com/20210708/v2_fae50dd10cb64ecba4ec14a02b036a2c_img_000" data-img-size-val="700,367" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>博客信息</p> 
<p>翻译内容如下：上周五（02.07.2021）我们对 MSP 供应商发起了一次攻击。超过 100 万的系统被感染。如果有人想就通用解密器进行谈判--我们的价格是 70000000 美元（BTC），我们将公开发布解密器，解密所有受害者的文件，所以每个人都将能够在不到一个小时内从攻击中恢复。如果你对这样的交易感兴趣，请按照受害者的 "readme"文件说明与我们联系。</p> 
<p>至今，Kaseya 并未表明是否会考虑支付赎金。官方发布的信息表示，越来越多的 MSP、经销商及其客户受到了此次攻击事件的影响，Kaseya 声明将继续展开调查、公布信息，尽力降低客户的损失。</p> 
<p><img src="https://img.36krcdn.com/20210708/v2_d9d61aa019ef4ccd9426c1e65c9322bc_img_000" data-img-size-val="1080,557" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Kaseya 官方说明</p> 
<h2 label="一级标题" style>惯犯 REvil ，作案太频繁</h2> 
<p>7000万美元听上去是一个天文数字，但是这不是 REvil 第一次狮子大开口了。2020 年 5 月，REvil 声称破译了唐纳德·特朗普公司用于保护其数据的椭圆曲线密码术，并为他们盗窃的数据索要4200万美元的赎金。</p> 
<p>最开始，REvil 因从服务于全球影视娱乐巨星的律师事务所—— Grubman Shire Meiselas & Sacks 窃取了近 1 TB的信息并勒索赎金而闻名，从此以后 REvil 就与LadyGaga、<a class="project-link" data-id="630767" data-name="埃尔顿" data-logo="https://img.36krcdn.com/20200729/v2_eaad8c45f33f45fd98ab6caa208225de_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/630767" target="_blank">埃尔顿</a>·约翰、<a class="project-link" data-id="442969" data-name="罗伯特" data-logo="https://img.36krcdn.com/20201021/v2_3d2a6833865340f297135f1f48edf605_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/442969" target="_blank">罗伯特</a>·德尼罗和麦当娜等知名巨星的名字紧紧联系在<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210601/v2_2bbe1c6ad79748b3be29e04d8999edac_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>。</p> 
<p>打出名号之后，作为黑客界的“明星”，REvil 的犯案频率简直可以评为劳模，仅2021年就凭借其每月至少一起的作案频率频频占据头版头条。</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>3 月 18 日，REvil 附属公司在网络上声称，他们已从跨国硬件和电子公司宏碁安装勒索软件并盗取大量数据，并为此索取5000万美元的赎金。</p></li> 
 <li><p>3 月 27 日，REvil 攻击哈里斯联盟，并在其博客上发布了联盟的多份财务文件。</p></li> 
 <li><p>4 月，REvil 窃取了广达电脑即将推出的苹果产品的计划，并威胁要公开发布这些计划，除非他们收到 5000 万美元作为赎金。</p></li> 
 <li><p>5 月 30 日，全球最大肉类供应商 JBS 受到 REvil 勒索软件的攻击，该公司不得不将所有美国牛肉工厂暂时关闭，并中断了家禽和猪肉工厂的运营。最终，JBS 还是向 REvil支付了 1100 万美元的比特币赎金。</p></li> 
 <li><p>6 月 11 日，全球再生能源巨擘 Invenergy 证实其作业系统遭到了勒索软件的攻击，REvil声称对此事负责。</p></li> 
</ul> 
<p>7月仅仅过去两天，REvil 就按捺不住对 Kaseya 出手了。</p> 
<h2 label="一级标题" style>为何受害企业却只能打碎牙往肚里咽？</h2> 
<p>除了组织本身以外，REvil 还招募了很多附属机构为他们分发勒索软件，这些附属机构和勒索软件开发商都将从支付赎金产生的收入中获利，也代表着最终赎金会有多个去向，因此 REvil 团伙确切位置难以确定。</p> 
<p>对于该组织，各国政府也深恶痛绝，多次下令进行严厉打击。不幸的是，之前的事件基本是以 REvil 勒索成功告终，这次的 Kaseya 事件又会怎样结束呢？</p>  
</div>
            