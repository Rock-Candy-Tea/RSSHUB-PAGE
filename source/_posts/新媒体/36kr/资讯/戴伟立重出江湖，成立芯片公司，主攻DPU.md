
---
title: '戴伟立重出江湖，成立芯片公司，主攻DPU'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210721/v2_1d160dc71ae14c49aeb93cf654033c3e_img_000'
author: 36kr
comments: false
date: Wed, 21 Jul 2021 02:45:59 GMT
thumbnail: 'https://img.36krcdn.com/20210721/v2_1d160dc71ae14c49aeb93cf654033c3e_img_000'
---

<div>   
<p>自2016年戴伟立和周秀文夫妇离开Marvell之后，就很少有二人的消息。但现在，我们发现他们又重回半导体赛道，或者说就从未离开过半导体这个赛道。是的，他们创立了一家DPU公司。要知道二人在半导体上造诣不可谓不深，时隔5年，两人再次出山，落子DPU，足见他们对DPU前景的看好。</p> 
<p>撇开云速度的竞赛不谈，DPU现已成为超大规模者的标准，<a class="project-link" data-id="7133" data-name="阿里巴巴" data-logo="https://img.36krcdn.com/20201030/v2_504c85fa199d4413a7f31069f7faa667_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/7133" target="_blank">阿里巴巴</a>和<a class="project-link" data-id="28215" data-name="百度" data-logo="https://img.36krcdn.com/20210325/v2_fa02010c4a8b46da9f4e1d3b1fd59f22_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/28215" target="_blank">百度</a>早已是DPU的用户，而<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>则被怀疑将它们置于幕后，<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a>正在FPGA方面做类似的事情。VMware也已宣布了将SmartNIC集成到VMware Cloud Foundation中Project Monterey的项目。面对CPU摩尔定律的放缓，越来愈多的行业共识是：CPU不能浪费在网络和存储等一些看家功能上，必须专注于核心的计算。而SmartNIC正好可以卸载从网络功能到许多数据平面和控制平面功能的所有内容，DPU不火不行！</p> 
<h2 label="一级标题">创立DPU公司，“梦想很大”</h2> 
<p>在过去十年中，计算成本一直趋于平稳，但网络和存储负载一直在增加，最重要的是，网络性能和计算性能的差距一直在扩大（如下图所示）。早在2018 年超过 70%的以太网端口的出货速度就约为10G/秒，在该性能水平上，为网络接口提供服务所需的处理开销开始成为一个问题。</p> 
<p><img src="https://img.36krcdn.com/20210721/v2_1d160dc71ae14c49aeb93cf654033c3e_img_000" data-img-size-val="869,472" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc">图源：THE NEXT PLATFORM</p> 
<p>据THE NEXT PLATFORM报道，微软拥有100万个或者更多基于FPGA的“Catapult”智能网卡，亚马逊也拥有与自主研发的Arm处理器数量相同的“Nitro”智能网卡。但放眼整个超大规模者，包括企业、云构建商，电信公司等总共大约有1200万-1400万台服务器，但可能只有200万到300万机器才拥有智能网卡。而这些玩家自研智能网卡的可能性几乎为0，所以这里面还有巨大的市场空间。</p> 
<p>再加上现在越来愈多的客户都开始将虚拟机托管到云服务器中，这就使得云网络和安全性变得相当复杂。因此，一些行业前瞻者看到了将一些工作卸载到SmartNIC中的潜力，这样既可以释放CPU内核，又可以进一步将客户工作负载与其他租户和更广泛的互联网的危险隔离开来。戴伟立和周秀文也看到了这个机会。</p> 
<p>他们所成立的公司名字叫【DreamBigSemi】，成立于2019年，从这个名字就可以看出他们的“梦想很大”。DreamBigSemi主要是为数据中心和存储加速提供全面的低成本、低延迟和高吞吐量SmartNIC解决方案。而且Dream Big Semiconductor 团队在颠覆性技术方面拥有无与伦比的良好记录。其中周秀文任执行主席，戴伟立任执行副主席，除了我们所熟知的这两位之外，SOHAIL SYED任CEO。SOHAIL SYED也是一个了不起的<a class="project-link" data-id="3969467" data-name="人物" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969467" target="_blank">人物</a>，Sohail 是一个很强的创业者，成功创办了包括 Questarium（被 Marvell 收购）和 FIRQuest（被 Corigine 收购）在内的多家公司。</p> 
<p><img src="https://img.36krcdn.com/20210721/v2_90e73daff6144e27a2aa272bef7dc843_img_000" data-img-size-val="1080,511" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc">图片来自DreamBig Semiconductor官网</p> 
<p>DreamBig Semiconductor总部位于美国加利福尼亚州圣何塞，但在全球不同地区设有办事处。值得一提的是，他们的团队大部分是base在巴基斯坦，这或许是与中美脱钩的一个表现。</p> 
<p>要知道，二人合作创立的Marvell如今在半导体界也是举足轻重。此次DPU的再次出发，与Marvell或将终有一战。</p> 
<p>Marvell从很早之前就开始做SmartNIC的研究。到2020年9月，Marvell的基于OCTEON的LiquidIO® SmartNIC就已经出货了100万个。OCTEON®系列也成为SmartNIC云应用中部署最广泛的数据处理单元 (DPU)。面对已经如此强大的Marvell，不知道DreamBigSemi如何在其中分得一杯羹。</p> 
<p>目前Marvell最新的解决方案是LiquidIO III，它已经发展到一个SmartNIC平台，结合了此前广泛部署的OCTEON TX2 DPU 和多达36个基于 Arm V8 的内核、5个x100G 网络连接、多达2个PCI Express Gen 4x16主机接口和6个DDR4 3200控制器通道。甲骨文就是LiquidIO III 的首批客户之一，</p> 
<p>在DPU发展的前期，尽早抢滩云厂商的市场很重要。据了解，Marvell 还与多家云超大规模数据中心运营商合作开发定制解决方案，使他们能够将自己的知识产权与 Marvell 强化且广泛部署的 OCTEON LiquidIO SmartNIC DPU相结合。</p> 
<h2 label="一级标题">“美满”夫妇的半导体创业史</h2> 
<p>1995年戴伟立和周秀文创立了Marvell，两人在加州大学伯克利分校就读时相识。两人都是移民，戴伟立出生于上海，周秀文则出生于印度尼西亚雅加达。两人经营Marvell超过20年，并在短时间内实现创纪录的盈利能力和规模后，于2000年将公司上市。Marvell也成为了世界顶尖的半导体公司。</p> 
<p><img src="https://img.36krcdn.com/20210721/v2_76affa7c521d43b980c2b6ce08abd2d4_img_000" data-img-size-val="959,639" referrerpolicy="no-referrer"></p> 
<p>直到2016年，因为财务问题，Marvell董事会将双方逐出局。其实这不过是资本游戏的一个例子。当年乔布斯也被董事会赶出了自己创立的苹果公司。</p> 
<p>虽然两人都辞去了职位，但是却从来没有离开半导体界。2019年9月16日，电子设备多标准连接IP解决方案公司宣布周秀文博士已加入其董事会。2020年9月，NUVIA的B轮融资了2.4亿美元，这其中就有戴伟立和周秀文的参与。</p> 
<p>周秀文号称印尼神童，他对电子产品的热情从很早就开始了，13岁时他在印度尼西亚就成为了一名合格的无线电维修技术员，从那时起，他就一直在设计组件和系统。他还是 IEEE 的研究员。它提出的FLC和MoChi技术也颇具领先性。</p> 
<p>戴伟立也是业界追捧的代表性女性之一，由于她对技术和社会的贡献，《新闻周刊》将戴女士评为“震撼世界的 150 位女性”之一，被 CNN 国际评为“领先女性”系列：领先女性技术充电、领先女性原则公平和关怀、 为未来成功而进行教育，以及领导女性激励他人。此外，《福布斯》杂志将戴女士列为“全球 100 位最具影响力的女性”之一。</p> 
<h2 label="一级标题">DPU的气候已成熟</h2> 
<p>十年前，当硬件加速技术的第一波重大<a class="project-link" data-id="457408" data-name="浪潮" data-logo="https://img.36krcdn.com/20200729/v2_5b609246f3cb44ad9d5f461d993a1fa0_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/457408" target="_blank">浪潮</a>袭来时。GPU 产品开始湖出现。现在，随着 FPGA 的逻辑单元扩展到300万以上，我们还将其与其他可组合处理块紧密耦合，用于网络、内存、存储和计算。在这种情况下，计算意味着通过SoC块或甚至ACAP实现芯片上的核心集群。不得不说，现在SoC以及 FPGA 已经成熟到可以成为 SmartNIC的基础技术的地步。正是这样的进步，第二波硬件加速的浪潮开始出现。</p> 
<p>而在DPU这条路的探索上，也是仁者见仁智者见智，所采用的架构呈现出多面开花的局面：</p> 
<p>（1）选择基于FPGA的SmartNIC阵营的表示，他们可以像<a class="project-link" data-id="362640" data-name="处理网" data-logo="https://img.36krcdn.com/20201113/v2_570744d52691420d9c270f1d0e33719c_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/362640" target="_blank">处理网</a>络和存储一样处理计算，在开发上，可以如CPU一样具有高度的可编程性，也可以像在SoC解决方案上一样快速开发新功能，如赛灵思宣称，其Alveo U25与基于Arm多核的SmartNIC相比，在相<a class="project-link" data-id="51403" data-name="同功" data-logo="https://img.36krcdn.com/20200729/v2_052c082c2c7749ef8999deb700ed36e1_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/51403" target="_blank">同功</a>率下，性能可提高10倍。</p> 
<p>不过基于FPGA也分为两种，一种是基于FPGA的智能网卡，另外一种是由于对向后兼容性的需求催生了另一种类型的SmartNIC——FPGA增强型SmartNIC。它为NIC添加了 FPGA功能。有三种方法可以开发FPGA增强的SmartNIC设计。第一种是简单地将FPGA连接到现有NIC。另一种选择是设计下一代SmartNIC ASIC，在芯片上集成FPGA阵列。第三种选择是在SmartNIC ASIC的设计中增加一个高速的芯片对芯片互连，并开发一个FPGA芯片组来连接到SmartNIC ASIC。据悉，国外公司Fungible正在研究将硬件可编程 FPGA与ASIC网络控制器相结合。</p> 
<p>（2）也有选择基于Arm多核架构的，这种方式的好处在于，可以卸载明确定义的任务，例如标准化的安全和存储协议，如博通和<a class="project-link" data-id="3969182" data-name="英伟达" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969182" target="_blank">英伟达</a>，英伟达还认为GPU可以从与DPU融合中受益，他们的EGX平台正在做这方面的努力。但多核SmartNIC卡也有一些限制，一是，它们基于软件可编程处理器，由于缺乏处理器并行性，这些处理器在用于网络处理时速度较慢；二是，这些多核ASIC中的固定功能硬件引擎缺乏 SmartNIC 卸载越来越需要的数据平面可编程性和灵活性。同时，多核 SmartNIC ASIC中的固定功能引擎无法扩展来处理新的加密或安全算法，因为它们缺乏足够的可编程性，只能适应轻微的算法更改。</p> 
<p>（3）采用异构架构的则认为，异构具有更高的灵活性，并能带来更高效的数据处理效率，以及更直接的使用接口和更佳的虚拟化支持，如国内<a class="project-link" data-id="635000" data-name="中科驭数" data-logo="https://img.36krcdn.com/20200729/v2_b4a6bc1433ff4d2aa298abb2c9418473_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/635000" target="_blank">中科驭数</a>的KPU架构，他们将四类异构核组织起来，分别处理网络协议，OLAP\OLTP处理，机器学习和安全加密运算核。</p> 
<p>随着SmartNIC市场的最终崛起，它将与下一波基于FPGA、或ARM内核、或异构架构的硬件加速器汇聚在<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>。这将在加速市场中形成各种叠加，改变我们对计算未来的看法。虽然目前不知道DreamBigSemi是采用哪种方式来走DPU这条路的。但有一点是，戴伟立和周秀文双方的加入，DPU这个角逐场更加热闹了。</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s?__biz=MzU3OTA0MjQ3Mg==&mid=2247605864&idx=1&sn=4852129f09abf9ae3f59a9c6fef3b952&chksm=fd6f33afca18bab9419910269bbcb47ae0ffe9b097db439e6a4394ae6bbbb772f9414f0ebec6&scene=27#wechat_redirect">“半导体行业观察”（ID:icbank）</a>，作者：杜芹DQ，36氪经授权发布。</p>  
</div>
            