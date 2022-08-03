
---
title: '阿里云云效 vs 腾讯云CODING，DevOps孰强孰弱？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://image.woshipm.com/wp-files/2022/08/RA0AzzudDJrwKNCCivpo.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 02 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/08/RA0AzzudDJrwKNCCivpo.jpg'
---

<div>   
<blockquote><p>编辑导语：DevOps这个话题在IT、开发等领域是相对热门的，它意味着开发运维一体化，是推动业务发展与自动化交付的有效方式。国内便有不少DevOps平台可供企业使用。那么这些DevOps平台目前的发展现状如何？本文作者进行了分析评测，一起来看。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5549768 aligncenter" src="https://image.woshipm.com/wp-files/2022/08/RA0AzzudDJrwKNCCivpo.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h3>摘要</h3>
<p>本文旨在通过对比国内两款DevOps代表性产品——阿里云云效、腾讯云CODING，分析两者在产品定位、核心功能和产品战略等方面的差异及优势，探讨国内DevOps平台的发展现状和趋势，为DevOps在中国的发展提供参考。</p>
<p>DevOps（Development & Operations），即开发运维一体化，是近些年来IT领域比较热门的话题。</p>
<p>DevOps的主要灵感来源于敏捷开发和精益生产，是软件开发管理领域继敏捷开发之后的又一次升级。随着DevOps的快速崛起，其概念已经逐渐被神话，亚马逊甚至将DevOps上升到哲学层面来讨论。在DevOps的基础上又衍生出许多新的概念，如DevSecOps（开发、安全和运营一体化）和BizDevOps（业务、开发和运营一体化）等，使得大家对DevOps的感知云里雾里。</p>
<p>我比较赞成Gartner对DevOps的定义：使用敏捷方法，提供业务驱动的协作和自动化交付解决方案。</p>
<h2 id="toc-1">一、行业背景</h2>
<p>DevOps的兴起离不开云计算技术的发展和对企业高效生产的追求。工信部发布的 《2021年通信业统计公报》显示，云计算已经成为新兴业务中增长最快的领域，相关业务较上年增长 91.5%，硬件基础设施规模的提高为DevOps提供了肥沃的土壤。随着容器技术的成熟，DevOps小步快跑，节省资源的优势逐渐战胜了传统开发的“瀑布模型”。</p>
<h3>1. 行业缘起</h3>
<p>伴随着信息技术产生的社会价值和企业价值越发显著，IT从业人员的人力成本也在不断提高。</p>
<p>传统的“瀑布模型 ”在开发阶段中要等待上一阶段完成所有工作才能进入下一阶段，其不但拖延了开发效率，拉长了产品迭代周期，增加了开发人员的人工成本，而且一次性开发也面临着需求变更风险和市场满意验证的风险。这使企业意识到要通过内生途径提高IT部门的运行效率和工作质量，塑造企业的IT竞争优势的重要性。</p>
<p>敏捷开发应运而生，敏捷开发将大的开发任务划分为很多个小的任务，将大的时间段划分为小的时间段，完成一个开发小任务就测试这部分的功能，这样就可以应对快速变化的需求，同时也能通过看板等工具，时刻监督团队内部的开发进度，提高开发效率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/WIowkpiuiWEvw4s9jwq6.png" alt width="1534" height="320" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图1 敏捷开发与瀑布模型流程</p>
<p>从图1可以看出，虽然敏捷开发开发实现了开发效率的提升，但是仍然停留在开发和测试的阶段，开发主要关注的是新功能和新需求，导致缺乏运维阶段的稳定性考虑，运维过程复杂繁重，开发和运维的矛盾爆发，DevOps也终于闪亮登场。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/J0lT2sdLBGJE46EM6ADi.png" alt width="2821" height="1024" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2 DevOps、敏捷开发与瀑布模型流程</p>
<p>对比前面所说的瀑布式开发和敏捷开发，从图2我们可以明显看出，DevOps贯穿了软件全生命周期，而不仅限于开发阶段。而随着精益生产和敏捷开发的逐步发展，小步快跑，快速验证的DevOps已经涵盖了计划、编码、构建、测试、发布、部署、运维和监控的全流程。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/XRtOeLCKQolbMbe0zM9F.png" alt width="600" height="284" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图3 DevOps全流程各阶段</p>
<h3>2. 市场现状</h3>
<p>根据中国 DevOps 现状调查报告（2021 年）显示，中国企业 DevOps 落地实践成熟度向全面级继续扩张，超八成企业已在不同程度上实践敏捷开发，同比增长近三成。</p>
<p>Gartner 2022年重要战略技术趋势预测，到2025年，新数字项目中将有超过95%将云原生平台作为基础，而这一数据在2021年为40%，基于云原生的DevOps也将迎来快速发展的第二阶段。</p>
<p><strong>1）发展阶段</strong></p>
<p>技术的发展可以划分为技术萌芽期、期望膨胀期、泡沫破裂低谷期、复苏期和成熟期。根据Gartner2020中国ICT技术成熟度曲线显示，DevOps在2022到2025年将迈入生产成熟期，与其相关的容器云、多云环境和中台架构也将逐步迈向成熟模式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/lpeQhsAgF1eDWRj8DbRS.png" alt width="1078" height="756" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图4 Gartner2020中国ICT技术成熟度曲线</p>
<p><strong>2）市场规模</strong></p>
<p>根据IDC发布的2021年《全球公共云服务半年度跟踪报告》显示：全球公共云服务市场同比猛增29.0%，总收入高达4086亿美元 ，总体继续保持稳健增长的态势。</p>
<p>其中支持数字优先战略的基础云服务（IaaS、PaaS）收入增长了38.5%，这说明企业越来越依赖于围绕广泛部署的计算服务、数据/人工智能服务、应用框架服务所构建的云创新平台来推动创新。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/6vX4vj0So07SsDfkoXa4.png" alt width="1080" height="267" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图5 IDC2021年全球公共云服务半年度跟踪报告</p>
<p>IDC报告显示，2021年下半年中国公有云服务整体市场规模（IaaS/PaaS/SaaS）达到151.3亿美元，从IaaS+PaaS市场来看，2021年下半年同比增长43.0%，未来5年，中国公有云市场会以复合增长率30.9%继续高速增长，预计到2026年，市场规模将达到1057.6亿美元，中国公有云服务市场的全球占比将从2021年的6.7%提升为9.9%，DevOps也将迎来新的发展浪潮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/59VnwucrC2J1jTwbGP6Y.png" alt width="821" height="760" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图6 IDC中国公有云服务市场规模预测（2021年下半年）</p>
<p>根据QYR（恒州博智）的统计及预测，2021年全球DevOps市场销售额达到了67亿美元，预计2028年将达到264亿美元，年复合增长率（CAGR）为20.7%（2022-2028）。</p>
<p>全球DevOps的核心生产商包括Datadog、亚马逊和Azure，前五大厂商的市场份额约为33%。北美是全球最大的市场，约占51%的份额，之后是欧洲和中国，分别占27%和10%。但从目前中国在云基础设施上的投入来看，年复合增长率20.7%这一数字可能相对保守。</p>
<p>根据艾瑞咨询2020年中国DevOps发展研究显示，2020年国内DevOps服务的市场规模达到27亿元，伴随着疫情的催化作用，很多厂商开始意识到云计算和DevOps服务的优势，如阿里云首次实现年度盈利，字节跳动开始自研云平台，互联网下半场的重点从C端逐渐向B端发展，未来5年DevOps的CAGR有望超过30%，市场发展前景良好。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/3S9EQEaP7Vru6uNniolQ.png" alt width="1182" height="498" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图7 2017-2025年中国DevOps云平台及时付费软件工具市场规模及增速（艾瑞咨询）</p>
<p><strong>3）产业链</strong></p>
<p>当前DevOps形成的产业链已经比较清晰，主要是根据DevOps整个流程中的各个阶段来展现，包括计划、编码、构建、测试、发布、部署、运维和监控的各个流程。</p>
<p>一体化的DevOps平台正在成为全球范围内的DevOps发展趋势，国内企业通常采用一体化平台+开源软件的方式构建自己的DevOps体系。目前国际很多大型科技企业已经开始布局一体化的DevOps平台，像阿里云云效，Azure和华为云DevCloud等，腾讯云2019年收购CODING之后也逐步像一体化平台发展。</p>
<p>一体化平台可以实现项目管理、CICD、测试、监控、云端编程以及制品仓库等功能，可以降低用户在不同平台之间跳转的时间和精力的浪费，提高效率和用户体验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/au3t6iApqWOI3WWPBGgG.png" alt width="1262" height="755" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图8 2020年DevOps研发/运维流程与工具链图谱（艾瑞咨询）</p>
<p><strong>4）发展趋势</strong></p>
<p>新冠病毒造成了一场人类悲剧，影响了全世界数百万人的生活和企业。DevOps比以往任何时候都变得更加重要和不可或缺。随着业务格局的变化和技术以闪电般的速度发展，DevOps也在不断发展以适应不断变化的需求。未来DevOps将向更安全、更智能、更高效的方向发展。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/cnQTEvCZ6PEVLxfjBY7r.png" alt width="1381" height="579" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图9 艾瑞咨询DevOps发展趋势预测</p>
<p>① DevSecOps（开发安全运维一体化）</p>
<p>由新冠引起的跨地点工作的远程工作设置，为安全漏洞打开了大门。随着安全和网络攻击风险的爆炸式增长，将安全注入业务运营每一层的需求比以往任何时候都更加重要。企业将越来越多地采用DevSecOps流程，使用自动化质量安全测试，通过早期测试和缓解漏洞，来提高安全敏捷性，将安全性引入DevOps，实现团队开发效率的提高。</p>
<p>② AIOps（智能运维）</p>
<p>AIOps将人工智能的能力与运维相结合，通过机器学习的方法来提升运维效率，更好的维护和提升资源性能。通过自动化运维等方式，在系统出现故障时为用户提供运维支持服务。借助应用容器化条件下统一的运行环境，开发人员得以在更大程度上进入运维侧，通过自动化的监控工具实时掌握系统和软件的故障状况。</p>
<p>目前我国企业在这一领域的发展仍比较有限，只有不足20%的企业具备智能化监控和决策能力。在DevOps和AIOps中利用预测分析使组织能够把重点放在改进DevOps服务上。它让基础架构和运营团队更深入地了解正在使用的资源和服务，以及未来如何使用它们以获得最佳结果。</p>
<p>③ AI和ML + DevOps</p>
<p>AI和ML + DevOps能够实现DevOps处理任务的自动化，当今数据生成的数量、种类和速度，对于采用传统方法和过时技术的组织来说，在日常运营中处理如此大量的数据是一项繁重的任务。人工智能 (AI) 和机器学习 (ML) 驱动的DevOps方法使组织能够计算和分析任何规模的数据。此外，它还促进了他们的工作流程，从而改变了团队高效开发、交付、部署和管理应用程序的方式。</p>
<p>④ 标准统一</p>
<p>随着DevOps的不断成熟和发展，DevOps也逐渐迈向标准化。2020年9月，由中国信息通信研究院牵头，联合云计算开源产业联盟、高效运维社区、DevOps 时代社区、BATJ、清华大学、南京大学、通信及金融等行业顶尖企事业单位专家共同制定的研发运营一体化（DevOps）能力成熟度模型》完成了首轮评估，它是全球首个DevOps标准，当前该标准已被众多金融、通信和互联网等行业名企纷纷采用并通过评估。</p>
<p>2021年中国 DevOps 现状调查报告显示，研发运营一体化（DevOps）能力成熟度评估受关注程度持续上涨。63.64%的受访者对 DevOps 能力成熟度评估感兴趣，相比2020 年增长近一成；另有29.86%、26.69%和17.45%的受访者关注 CMMI认证、ISO 体系认证和中国信通院开展的金牌运维评估。</p>
<p>⑤ 一体化</p>
<p>DevOps理念是打通软件工程中各个曾经由独立的团队和不同的软件工具来实现的工作，在对企业文化、管理方式等“软实力”提出新要求的同时，也不断催促着市场打磨出能够提供相应的生产力和创造性的软件研发工具，集成度更高、生态系统更完整的工具链将成为这一行业未来大趋势。</p>
<h3>3. 小结</h3>
<p>DevOps的出现在敏捷开发的基础上，把整个设计、开发、测试、运维的过程颗粒化，实现软件开发的快速更新和迭代，降低了需求变更和软件质量验证的风险，促进了团队内部工作流的互联互通，提高了工作效率。</p>
<p>从市场现状来看，随着容器技术和云原生等技术不断成熟，DevOps的发展正在逐步从快速发展期过度到成熟期。从市场规模来看，中国云计算的增长率高于国际平均水平，国内互联网巨头们主要服务对象开始从C端向B端转移，中国DevOps的市场份额还有很大的提升空间，有望实现30%以上的年复合增长率。</p>
<p>从产业链和发展趋势来看，目前DevOps的各个阶段都有了代表性厂商，后续的发展趋势是云平台+开源软件的主流构建方法，需要建立功能完备，标准统一的一体化平台。未来DevOps也将与人工智能、机器学习、机器人流程自动化等领域进行融合，减少人工操作的复杂性，促进DevOps的标准化、数据化、自动化和智能化发展。</p>
<h2 id="toc-2">二、竞品分析</h2>
<p>B端产品的核心竞争力是极简主义，DevOps的核心竞争力是基于管理模式的效率提升和过程追溯。</p>
<h3>1. 竞品选择</h3>
<p>本文选择阿里云云效和腾讯云CODING作为竞品分析的对象，原因如下。</p>
<p><strong>1）市场份额</strong></p>
<p>在市场份额方面，自IDC中国公有云市场数据报告诞生以来，阿里云的市场份额始终位居中国市场第一，也是国内首次实现年度盈利的公有云厂商。</p>
<p>另外据IDC报告的2021年下半年中国IaaS+PaaS市场前五大市场份额占比显示，阿里云和腾讯云位于中国市场前两名。选择阿里云云效和腾讯云CODING也是因为两者作为国内的互联网两大巨头，在竞争格局上更为相似。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/MbD5cAxdDCR8mih3rlyO.png" alt width="855" height="755" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图10 IDC中国公有云IaaS+PaaS市场份额2021年上半年</p>
<p><strong>2）技术实力</strong></p>
<p>阿里云云效是阿里巴巴多年研发效能理念方法、工具实践、业务实操等经验沉淀，目前汇集了10万企业、百万级别的开发者。</p>
<p>阿里云把把在2020年计划未来三年再投 2000 亿元，用于云操作系统、服务器、芯片、网络等重大核心技术研发攻坚和面向未来的数据中心建设。2022年最新的阿里巴巴财报显示，2022年阿里巴巴全年的技术相关成本费用超过了1200亿，可见阿里云的技术研发投入所言不虚。</p>
<p>腾讯云CODING成立于 2014 年 2 月，2019年8月被腾讯全资收购。旗下一站式软件研发管理平台—CODING（CODING.net）上线稳定运行8年，目前已累积超过300万开发者用户，5万家企业团队，服务涵盖互联网、金融、政企等不同行业客户。2021年10月，宣布战略从DevOps工具转向云原生时代的研发工具。</p>
<p>腾讯云于2020年同期也提出了投资计划，计划未来五年将投入5000亿元布局新基建，用于云计算、区块链、服务器、超算中心、人工智能、5G 网络、网络安全、量子计算、音视频通讯、大型数据中心以及物联网操作系统等方面，腾讯过去三年也累计投入了1366亿元研发经费。</p>
<p>基于以上原因，无论从市场份额、使用人数还是研发投入的角度看，阿里云和腾讯云都是居于国内云计算的前列，且二者都属于互联网行业的巨头，具有相同的行业背景。但是腾讯云CODING是2019年腾讯全资收购的，所以其产品相较于阿里云云效的原生性难免又有所差异，这也为本次产品分析增添了一分趣味。</p>
<h3>2. 市场定位</h3>
<p>阿里云云效是云原生时代一站式BizDevOps平台，阿里云云效强调了DevOps平台的Biz（Business，业务）属性。支持公共云、专有云和混合云多种部署形态，通过云原生新技术和研发新模式，助力创新创业和数字化转型企业快速实现研发敏捷和组织敏捷，打造“双敏”组织，实现多倍效能提升。</p>
<p>使用云效可以免搭建、免维护，注册即用；一站式打通DevOps账号及数据；集成钉钉，实现成员、消息的及时同步；无缝对接阿里云ECS、ACK等；丰富的研发效能数据洞察；精细化企业级安全防控能力。可见阿里云云效在自有生态上实现了一体化的IasS+PaaS生态。</p>
<p>腾讯云CODING的slogan是让开发变得更简单，提高应用效率和可靠性。这有一定的局限，DevOps平台面向的客户不仅仅是开发人员，还涉及到项目管理、效率评价等管理领域，需要强调平台的业务属性，但从腾讯云收CODING之后可以看出，CODING正在向端到端的一体化平台发展，并开放了合作伙伴计划。提供了丰富的 OpenAPI 接口，注册应用即可使用，无需审核，可以满足 CODING 与第三方系统的集成对接要求。</p>
<p>两者都是追求效率的提升，在整体格局上，阿里云云效可以依靠阿里云的技术积淀实现云钉一体化，在自有生态方面具备优势。但是在开放生态方面，腾讯云CODING却走在了一向以开放平台为特色的阿里前边，提供丰富的接口与合作伙伴共建生态。</p>
<p>7月28日，2022开放原子全球开源峰会期间，阿里巴巴首席技术官程立提到“云是数字世界的基座，云也为开源软件提供了最佳运行环境，云+开源共同成为数字世界的根”，由此我们可以期待阿里云云效的进一步开放生态，将技术与合作伙伴共享。</p>
<h3>3. 用户分析</h3>
<p>阿里云云效为企业提供产品、培训咨询等服务内容，致力于解决企业、政府等在数字化转型过程中的组织能力提升、DevOps落地等问题。阿里云云效的服务客户涵盖金融、制造、城市政务、医药、零售等多个行业。</p>
<p>从占有率来看，阿里云是第一梯队的龙头。从全球的云计算产业市场份额来看，阿里云也是国内唯一一个有成功海外经验的云计算厂商，从阿里云云效官网来看客户总量超过10万。</p>
<p>从腾讯云CODING的官网客户来看，金融领域的服务或者企业占比最大，其次是游戏、医疗、电商、零售、视频、互联网、智慧交通、AI等领域，客户范围非常广泛。腾讯云CODING的用户部分来自生态链用户的拓展，比如腾讯游戏和微保。从CODING官网数据来看，在服务总量上已经超过5万家企业。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/5WgW8KOGfgCOachhqdA0.png" alt width="1553" height="838" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图11腾讯云CODING客户案例列表</p>
<h3>4. 核心功能对比</h3>
<p>本文查阅了两款产品的官方文档和宣传资料，总结两款产品的核心功能如图12和图13所示。</p>
<p>阿里云云效：项目协作、代码管理、流水线、应用交付、云端开发、制品仓库、测试管理、知识库、效能洞察。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/Xy7vS6paTD0CIz9ANDZI.png" alt width="3502" height="1134" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图12阿里云云效工具链</p>
<p>腾讯云CODING：代码管理、项目协同、测试管理、持续集成、制品仓库、持续部署、团队知识库、云端开发。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/HsotkSPV13UekevvRC8u.png" alt width="1622" height="857" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图13 CODING云上研发工作流</p>
<p>由图可见，两款产品在功能模块上大体相同。本文将从项目协作、代码管理、持续集成、持续部署、测试管理、团队知识库、制品仓库和云端开发层面对两款产品进行详细比较。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/b8pUxz6TBNA4AUTDAsUk.png" alt width="1059" height="801" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图14阿里云云效和腾讯云CODING核心功能对比雷达图</p>
<p>在项目协作方面，阿里云云效支持自动化规则设置，可以在需求状态变更后，通过钉钉或邮件通知相关人员，及时传递信息，支持多项目和单项目管理，功能比较完善给9分；腾讯云CODING可以实现待规划的看板式拖拽效果，体验效果较好，但尚有提升空间，给7分。</p>
<p>在代码管理方面，阿里云云效的代码管理是自研平台，在代码安全层面，云效可以购买高级版实现安全风控，给8分；腾讯云CODING是使用Git进行代码管理，创建应用的速度更快，给6分。</p>
<p>在持续集成和持续部署方面，阿里云云效和腾讯云CODING都能够实现基本的功能，但阿里云云效可以实现端到端的服务，将持续集成和部署集中在一条流水线上，给阿里云云效打8分，腾讯云CODING打7分。</p>
<p>在测试管理方面，阿里云云效支持思维导图用例导入，腾讯云CODING支持自动化用例库，测试报告和测试概览等功能，阿里云云效打5分，腾讯云CODING打8分。</p>
<p>在团队知识库方面，虽然阿里云云效不限制文件的容量，但不支持导入PDF文件和其他格式文件，腾讯云CODING限制文献容量为30G，还支持API文档，给阿里云云效打4分，腾讯云CODING打8分。</p>
<p>在制品仓库方面，两者都能满足开发者需求，各打8分。</p>
<p>在云端开发方面，腾讯云CODING推出了国内第一款WebIDE 产品——Cloud Studio，目前已经投入使用，打9分；阿里云云效也推出了面向云原生的 WebIDE 产品，正处在产品公测期，打6分。</p>
<h3>5. 小结</h3>
<p>从整体来看，阿里重战略，腾讯重体验。阿里云云效凭借阿里云的基础设施数量和云钉一体化的战略可以实现用户量的优势，阿里云云效的功能比较全，尤其在安全方面的能力可圈可点，还提供效能洞察和交付平台等独特功能，在向端到端的生产交付方向努力。</p>
<p>腾讯云CODING的功能比较简练，市场定位清晰，交互体验较好，基础功能没有短板，产品由原来的注重开发层面逐渐向一体化方向发展，希望凭借合作伙伴的力量构建完整生态。</p>
<h2 id="toc-3">三、策略分析</h2>
<h3>1. 商业模式</h3>
<p>阿里云云效和腾讯云CODING在商业模式方面都采用了产品销售和服务付费两种方式。</p>
<p>在产品销售方面区分为基础版、高级版和资源存储容量包。</p>
<p>两者都选择基础版不付费来先扩大用户量，阿里云云效的高级版售价为618元/人/年，腾讯云CODING的高级版售价为599元/人/年。阿里云云效的资源存储容量包为1188元/公司/年，腾讯云CODING的资源存储容量包为1999元/公司/年。</p>
<p>阿里云云效高级版增添功能：效能洞察和代码安全检查，并为高级版用户提供阿里云官网工单5 * 12h中英文在线支持和专业敏捷研发培训。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/LvPlC1hTFzT44mgkk2kU.png" alt width="1103" height="757" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图15阿里云云效产品售价</p>
<p>腾讯云CODING高级版增添功能：OKR、项目集、工作负载、访问审计、水印设置、IP白名单和工作负载等功能，没有服务培训。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/uYjDbMXxZiJdZv2frBt8.png" alt width="1617" height="743" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图16 腾讯云CODING产品售价</p>
<p>在服务付费方面，阿里云云效提供了三种服务方案，其形式主要为按次付费，服务方案如下图。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/axioUuAmWV4qYKDXkmCZ.png" alt width="1470" height="556" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图17阿里云云效服务售价</p>
<p>腾讯云CODING的服务付费模式是按月付费，提供持续服务，服务方案如下。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/mtXaQBb7bdYT6KGHXHTI.png" alt width="1473" height="1271" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图18腾讯云CODING服务售价</p>
<p>总体而言，阿里云云效的基础版具备产品的绝大部分功能，如果在安全方面有较高要求可以选择升级到高级版，这种版本设计主要服务于金融和政府等对安全性要求较高的企业。</p>
<p>腾讯云CODING在基础版上会有很大的资源限制，一般需要购买1999元的资源存储包来进行扩展，高级版在功能上也倾向于项目管理的可视化和安全性考察。在服务付费方面，阿里云云效倾向于按次收费，且服务价格较高，适用于DevOps实践水平高的企业；腾讯云CODING采用按月付费，适用于频繁需要服务的客户。</p>
<h3>2. 产品策略</h3>
<p>阿里云云效依靠阿里云基础设施建设，打造云钉一体化的生态系统，帮助企业快速落地双敏研发模式。阿里云云效产品技术负责人陈鑫在云效峰会上指出，企业在落实敏捷实践存在以下问题。</p>
<p>第一是企业希望加强需求质量，一次性把事情做对。第二是研发流程全面线上化。第三是角色细分带来的沟通碎片化等新问题。第四是信息孤岛问题。</p>
<p>为了解决企业以上切实痛点，阿里云云效提出了业务价值驱动的数字化研发协作理念，并对现有的产品进行了重大升级。阿里云云效认为未来研发协同应该分为三个阶段，分别是定义价值、集体创造价值和持续改进。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/KoLGTdfSZyITn0fDpnh3.png" alt width="1327" height="641" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图19阿里云云效数字研发协作模式</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/6EeZ9X5L6SS5kUEAVUe8.png" alt width="1300" height="720" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图20阿里云云效基于云端的一体化开发平台</p>
<p>腾讯云CODING最早是做代码托管，经过不断演进，引进了非常多的上下游产业链相关工具，包括持续集成、敏捷项目管理、持续部署、制品库等。</p>
<p>现在的产品定位是云原生时代的研发工具领跑者，而不局限于 DevOps。产品战略逐渐向发展合作伙伴方向转移，包括商务销售伙伴、交付实施伙伴和咨询服务伙伴。目的是配合工具和实施的落地，帮助团队不仅仅是购入一款工具，而是能更好的导入方法论，带动组织变革。通过云+端的形式，让云原生开发回归原始而又简单。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/3Eagu9aFUcrQA0KhJvrv.png" alt width="1202" height="641" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图21腾讯云COIDNG开发模式</p>
<p>展望未来CODING的发展方向， CODING 创始人兼 CEO 张海龙在腾讯云 CIF 工程效能峰会上指出，第一个是 Value Stream，要加强交付物价值的衡量。第二个是 AI，帮助开发者写出更加完备、高质量的代码，通过 AI 的能力做出辅助开发者 Code Review。第三个是安全，强调 DevSecOps，把安全性融入到整个研发测试环境里。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/ekZrJKhWFE21huobKarr.png" alt width="1443" height="546" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图22腾讯云CODING行业展望</p>
<h2 id="toc-4">四、总结</h2>
<p>随着中国云计算产业的迅速发展，国内互联网巨头腾讯和阿里都开始将业务逐渐B端倾斜，阿里云凭借电商基因和尽早的布局，在IaaS领域的市场份额远超腾讯云，具有用户基数优势，使得阿里云云效在安全服务方面有高质量的技术团队支撑，能够和钉钉打出端到端的组合拳。</p>
<p>腾讯云CODING是国内最早的代码托管企业，在WEBIDE领域具备先发优势，同时腾讯云CODING注重用户体验，将简单、高效作为产品追求的目标，向一体化平台演进。</p>
<p>在云计算技术的不断趋于成熟背景下，阿里云云效和腾讯云CODING都在向安全领域发起进攻，未来的DevOps的形态一定是安全、简单、高效与管理模式的不断融合，去赋能企业安全生产，快速迭代，催生出更灵活、更量化、更标准的管理模式。</p>
<p>本材料所有内容来源于网络公开资料，经整理归纳总结形成本文档。仅供学习使用。</p>
<h3>引用</h3>
<ol>
<li>艾瑞咨询：2020年中国DevOps应用发展研究——艾瑞云原生系列报告（二）https://report.iresearch.cn/report/202012/3702.shtml</li>
<li>云计算中国产业联盟：2020年中国DevOps现状调查报告https://www.yanbaoke.com/info/9a6ySMG3joJD4PxdAkWSB9</li>
<li>工业与信息化部：2021年通信业统计公报https://wap.miit.gov.cn/gxsj/tjfx/txy/art/2022/art_e8b64ba8f29d4ce18a1003c4f4d88234.html</li>
<li>恒州博智：2022-2028全球与中国DevOps市场现状及未来发展趋势https://www.qyresearch.com.cn/reports/devops-p1487635.html</li>
<li>Gartner：2022年重要战略技术趋势https://www.gartner.com/cn/information-technology/insights/top-technology-trends</li>
<li>Veritis：The Future of DevOps: 2021 Key Trends and Predictionshttps://veritis.com/blog/the-future-of-devops-2021-key-trends-and-predictions/</li>
<li>南京大学：DevOps·云原生2021年度中国调查报告http://softeng.nju.edu.cn/tech-reports/2021DevOpsAnnualReport.pdf</li>
<li>微软：2020-2021年企业DevOps报告https://azure.microsoft.com/zh-cn/resources/enterprise-devops-report-20202021/</li>
<li>零一智库-国内四大云计算巨头的“算力竞赛”https://www.01caijing.com/finds/report/details/317211.htm</li>
<li>2021腾讯云CIF工程效能峰会https://coding.net/cifcon/living</li>
<li>2021阿里巴巴研发效能峰会https://developer.aliyun.com/topic/n-live2021</li>
</ol>
<p> </p>
<p>本文由 @齐新雷 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5547162" data-author="1355546" data-avatar="https://image.woshipm.com/wp-files/2022/07/weDHvvUoNm6r3ahN5yX0.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            