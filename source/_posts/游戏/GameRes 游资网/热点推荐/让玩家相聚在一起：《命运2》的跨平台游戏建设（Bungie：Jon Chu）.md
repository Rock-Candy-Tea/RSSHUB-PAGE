
---
title: '让玩家相聚在一起：《命运2》的跨平台游戏建设（Bungie：Jon Chu）'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202208/29/095501fc3y93ijn4d393cp.png'
author: GameRes 游资网
comments: false
date: Mon, 29 Aug 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202208/29/095501fc3y93ijn4d393cp.png'
---

<div>   
GDC是全球游戏行业最具规模、最有权威、最有影响力的专业峰会。每年的GDC大会上，全球顶尖的游戏开发者们将齐聚在这里，交流彼此的想法，构想游戏业的未来方向。本篇为大家介绍的是来自Bungie公司高级技术项目经理Jon Chu的演讲“Bringing players together: Building Cross Play in 'Destiny 2' ”。<br>
<br>
<div align="center">
<img aid="1051654" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095501fc3y93ijn4d393cp.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095501fc3y93ijn4d393cp.png" width="600" id="aimg_1051654" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095501fc3y93ijn4d393cp.png" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1051655" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095502tu2su4oum2a5e92a.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095502tu2su4oum2a5e92a.png" width="139" id="aimg_1051655" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095502tu2su4oum2a5e92a.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Jon Chu</font></font></div><div align="center"><font size="2"><font color="#808080">Senior Technical Program Manager, Bungie</font></font></div><br>
<strong><font color="#de5650">演讲标题：</font></strong><br>
<br>
Bringing players together: Building Cross Play in 'Destiny 2'<br>
让玩家相聚在一起：《命运2》的跨平台游戏建设<br>
<br>
<strong><font color="#de5650">演讲者信息：</font></strong><br>
<br>
Jon Chu是Bungie公司的高级技术项目经理。作为一个工程向团队的负责人，他在管理多个游戏项目的进度中，负责把控产品远景和项目未来的发展路线。在Bungie工作的3年里，Jon的大部分时间都在关注工具和引擎的开发：例如提升UI设计的工作流程，为游戏活动更新《命运2》引擎，提高开发效率等。近期他正在带领工作室的多个小组探寻游戏行业的前沿领域，其中最重要的则是《命运2》的跨平台游戏建设工作。<br>
<br>
<strong><font color="#de5650">演讲概述：</font></strong><br>
<br>
本篇演讲围绕着《命运2》的跨平台建设为核心，分享了Bungie团队在建设过程中关于游戏开发、团队管理、以及设计细节的经验。跨平台游戏的开发运营不仅仅要着眼于游戏内的玩家互动，不同平台玩家的社交需求也是需要重点关注的。在不断地拓宽多平台玩家的互动边界时，往往也会引入新的风险：例如一些对现有玩家生态可能产生损害的行为。因此如何在发展跨平台游戏的同时保护好玩家，是制作团队前期就需要评估的问题。在开发阶段，对于核心代码架构有较大影响的改变应尽早进行，以提升系统的持续稳定性。游戏上线时应尽可能逐步推进，以留有充足的时间测试、完善各项功能。<br>
<br>
<strong><font color="#de5650">一、Bungie和《命运》系列</font></strong><br>
<br>
Bungie是美国著名的游戏制作商，由Alex Seropian于1991年5月成立，最初位于芝加哥。2000年微软收购Bungie，并于2001年11月15日同步发售了第一人称射击游戏《光环：战斗进化》为Xbox护航。2010年4月，Bungie与动视合作开发了《命运》，2017年发行《命运2》。《命运2》是一个大型多人在线FPS动作游戏。游戏中玩家将扮演充满光的力量的守护者来捍卫人性，同时将参与各类搜寻、射击任务来升级自己的装备和武器，帮助角色成长为终极怪物收割机。<br>
<br>
至今为止玩家可以在7个不同平台上游玩《命运2》，包括：PS4，PS5，Xbox One，Xbox Series One X/S，Stadia，Steam，Microsoft PC商店。<br>
<br>
<div align="center">
<img aid="1051656" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095502w0jsz545hjo8svks.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095502w0jsz545hjo8svks.png" width="600" id="aimg_1051656" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095502w0jsz545hjo8svks.png" referrerpolicy="no-referrer">
</div><br>
《命运2》的游戏本体代码库体积非常巨大，一部分的游戏引擎可以追溯到同样是由Bungie开发的《光环》系列，但许多游戏自研引擎中的核心系统代码是非常难以更改的，这也对跨平台游戏开发形成了极大的挑战。<br>
<br>
<div align="center">
<img aid="1051657" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095503g7kd9l0ub50686z5.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095503g7kd9l0ub50686z5.png" width="600" id="aimg_1051657" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095503g7kd9l0ub50686z5.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">二、团队构成及时间线</font></strong><br>
<br>
《命运2》的跨平台开发主要由4个核心团队，约50名员工提供直接支持。包括工程师、测试人员、设计师、制作人、技术经理等等。除此之外，还得到了发行、市场、分析小组、玩家支持与社群小组，及网络运维小组的支持保障。这些都是在疫情期间所有人远程办公的情况下完成的。这四个核心团队分别为：<br>
<br>
引擎客户端小组：负责底层引擎代码调整，如游戏匹配和网络通信；<br>
<br>
UI-UX小组：负责游戏交互体验的设计，以及跨平台好友管理功能设计；<br>
<br>
服务小组：负责由跨平台而引入的一系列新服务的接入支持；<br>
<br>
Bungie.net小组：负责网页版和手机版Bungie.net的体验，以及《命运2》相关App的开发运营。<br>
<br>
<div align="center">
<img aid="1051658" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095503musqtrtzkv4m75rv.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095503musqtrtzkv4m75rv.png" width="600" id="aimg_1051658" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095503musqtrtzkv4m75rv.png" referrerpolicy="no-referrer">
</div><br>
整个跨平台项目共耗时约一年半时间。自2020年夏季预研开始，之后是技术攻坚和第三方审核等工作。2021年初，跨平台游玩得以在两个平台上进行测试，在经过Bungie内部测试及Beta测试后，2021年8月的Lost赛季，跨平台游戏正式对外发布。Jon在演讲中提到，在工作室中很流行的一句话是：<br>
<br>
我们不能控制结果，但是我们可以控制执行过程。<br>
<br>
We can't control our outcomes, but we can control our executions.<br>
<br>
<div align="center">
<img aid="1051659" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095504evyuyuarrtg2buyg.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095504evyuyuarrtg2buyg.png" width="442" id="aimg_1051659" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095504evyuyuarrtg2buyg.png" referrerpolicy="no-referrer">
</div><br>
在项目开发的过程中，项目组专注于提升玩家体验，并结合反馈做出正确的选择与调整，在跨平台游戏正式上线之后，也收获了广大玩家的好评。<br>
<br>
<strong><font color="#de5650">三、跨平台游戏开发：七项挑战</font></strong><br>
<br>
在《命运2》跨平台游戏相关开发过程中，开发者总结了七项关键的经验与挑战：<br>
<br>
<strong>搭建全新系统</strong><br>
<br>
首先，在推动游戏跨平台升级的过程中，需要搭建一些新的系统和改进服务以适应新的需求。《命运2》原先开发时使用的许多系统都是基于平台级API（应用程序接口）的，核心游戏使用的是Bungie的自研专利引擎，这些支持跨平台游戏的接口需要在引擎内部复刻出来，许多系统与服务的重构将开发的规模提升到了平台级别以上。其中例如通信或UI这类核心的涉及底层核心系统改动的功能，需要尽早计划安排。<br>
<br>
其次，在跨平台功能升级的过程当中，不可避免的需要将一些平台级别的服务迁移到平台之外，这时通常面临的是使用第三方服务还是自建服务的选择。打通跨平台游玩渠道的最大益处是能让玩家在游戏时不受平台限制，在不同平台间迁移的体验变得更流畅。若在项目一开始时就将云游戏和移动端游戏考虑在内，则能帮助跨平台之间的游戏体验更好地衔接。<br>
<br>
<strong>通信系统</strong><br>
<br>
作为跨平台开发中的核心需求，通信系统（Networking）是保障不同平台的玩家能够在《命运2》中顺利沟通的一大重要模块，也是核心系统中规模及改动影响最大的。《命运2》在不同平台上的游戏包体会有一些区别，为了系统的整体稳定性，最终开发者决定创建一个映射层来准确响应不同平台的通信需求。<br>
<br>
<div align="center">
<img aid="1051660" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095504q59o79ko00ddo0k0.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095504q59o79ko00ddo0k0.png" width="600" id="aimg_1051660" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095504q59o79ko00ddo0k0.png" referrerpolicy="no-referrer">
</div><br>
<strong>玩家身份系统</strong><br>
<br>
玩家在游戏中花费了大量的时间精力去提升他们的角色，玩家所对应的角色可以看作是其在游戏宇宙中的延伸。玩家的昵称和身份也代表着特殊的含义。“Bungie ID”使用了[昵称#1234]的形式，平台打通后，玩家中即使存在相同的昵称也可以使用#号后面的4位数字区分开来，作为玩家在游戏中的唯一标识，开发团队将不同平台的昵称统一绑定在了Bungie ID中。<br>
<br>
<strong>好友系统</strong><br>
<br>
玩家的好友池在跨平台游戏中已经由单平台延伸到了所有平台，于是新的社交系统“Bungie社交网络”诞生了。玩家可通过搜索Bungie ID来查找到对应的好友，进行“浏览玩家资料-发送好友请求-查看好友请求-接受/拒绝好友申请”一系列操作，以及设置屏蔽、隐身等其他功能。新的身份系统也给好友列表的UI增添了许多的复杂性，列表中需要添加更多信息（如头像、平台信息等）以分辨不同玩家。<br>
<br>
<div align="center">
<img aid="1051661" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095504xf2i8o2hwh9g6uwg.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095504xf2i8o2hwh9g6uwg.png" width="600" id="aimg_1051661" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095504xf2i8o2hwh9g6uwg.png" referrerpolicy="no-referrer">
</div><br>
<strong>组队邀请会话</strong><br>
<br>
《命运2》游戏中，玩家组成的队伍成为“火力战队”，当跨平台邀请好友组队时，系统是无法直接调用另一个平台的API的，于是需要构建新的组队服务来进行管理，包括邀请消息提示，以及其他相对应的UI套件等等。<br>
<br>
<div align="center">
<img aid="1051662" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095505wi0i4wi034xi8l0x.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095505wi0i4wi034xi8l0x.png" width="600" id="aimg_1051662" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095505wi0i4wi034xi8l0x.png" referrerpolicy="no-referrer">
</div><br>
<strong>玩家交流系统</strong><br>
<br>
和其他多人在线游戏类似，玩家可通过语音、文字聊天与战队的成员交流。《命运2》一开始使用的是平台层级的语音系统：如PS平台使用索尼的API， Xbox平台使用的微软的API。而跨平台交流中，系统需要自行将来自不同平台玩家的语音消息进行编码和解码，于是开发团队转而寻求第三方语音服务的帮助，以实现跨平台玩家语音功能。类似的，对于文字聊天来说，游戏中原本使用Steam平台的API，其他平台玩家的加入会使得文字聊天系统需要向更高层级迁移。<br>
<br>
<strong>内部沟通管理</strong><br>
<br>
从《命运2》的经验来看，在团队管理的过程中有三个要点：<br>
<br>
合理设置同步点，确保项目卡点能够迅速被处理；<br>
<br>
强调各部门间进度对齐的重要性，尤其是在规模较大的团队居家办公的情况下；<br>
<br>
同时也要注意合理分配会议时间和实际工作时间。<br>
<br>
在类似《命运2》跨平台游戏这样一个大规模的项目管理上，内部的沟通和意见梳理非常重要。自2021年9月以来非常紧张的开发时间，以及疫情期间远程办公给团队间信息同步带来的挑战，都给团队的目标对齐和沟通效率提出了非常高的要求。为此，开发团队划分了功能小组（如玩家交流系统）及业务部门（测试工程部门），并定期举行例会，便于同步项目进度及某个特殊功能的未来开发计划。<br>
<br>
<div align="center">
<img aid="1051663" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095505c2jbfw8wk0ezs8of.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095505c2jbfw8wk0ezs8of.png" width="600" id="aimg_1051663" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095505c2jbfw8wk0ezs8of.png" referrerpolicy="no-referrer">
</div><br>
以好友列表功能为例，每周例会主要用于探讨好友系统的交互以及客户端中的其他功能，“屏蔽”功能应如何设计及实现就是在例会上提出的，会议中工程师和设计师围绕玩家体验和反馈，对“屏蔽”功能在跨平台上的表现进行讨论。随后的技术会议中，工程师则会探讨具体的实现方式。核心组成员每周的例行测试则是为了跟进项目整体进度和评估体验。<br>
<br>
<strong>匹配机制调整</strong><br>
<br>
在《命运2》的跨平台项目中，考虑到游戏的公平性和平衡性，开发者针对不同的游戏活动设计了不同的匹配池。如手柄和键鼠玩家的可竞争性，或是主机和PC平台的安全等级区别，项目组经过玩家和社群调研评估后决定，在某些模式下主机和PC玩家应拥有各自不同的匹配池，核心是为了维护游戏公平性和保护玩家：合作情境下所有玩家都进入同一个匹配池，而竞争模式下主机玩家（Stadia，Xbox主机，PS）与PC玩家（Steam，Microsoft PC Store）分别在各自的匹配池中。在一定的情况下主机玩家可以选择进入PC的匹配池，而PC玩家不能选择进入主机匹配池。<br>
<br>
<div align="center">
<img aid="1051664" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095506fghg4h4h4h8hzccb.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095506fghg4h4h4h8hzccb.png" width="600" id="aimg_1051664" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095506fghg4h4h4h8hzccb.png" referrerpolicy="no-referrer">
</div><br>
<strong>社交系统调整</strong><br>
<br>
不同平台的玩家都拥有各自遵循的游戏道德准则。当打破平台间的边界，让所有玩家走到一起时，玩家们会接触到一些不曾接触过的新的社交行为，这其中也有可能产生例如骚扰、谩骂等违规或是不道德的行为。对于拓宽玩家交互边界所要承担的风险，《命运2》团队的决定是在昵称中使用统一的屏蔽词和过滤器，以规避不同平台过滤规则不一的风险，且被屏蔽的账号无法通过切换平台来继续骚扰其他玩家。通过一系列玩家社交系统的调整，开发团队可以尽最大可能保护玩家，以确保所有玩家能够拥有最佳的游戏体验。<br>
<br>
<div align="center">
<img aid="1051665" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095506f6napongs7a8e7y2.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095506f6napongs7a8e7y2.png" width="600" id="aimg_1051665" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095506f6napongs7a8e7y2.png" referrerpolicy="no-referrer">
</div><br>
<strong>平台认证需求</strong><br>
<br>
跨平台功能的开发意味着和不同的平台方合作，其中包括索尼，Valve，谷歌，微软等等。不同平台对于游戏有不同的需求：一些平台要求玩家身份应与平台昵称相对应，也有一些平台要求不在玩家界面展示其他平台的标识。在预研阶段，开发团队仔细浏览分析了所有平台方的设计需求，标注并重点关注与初始设计中有出入的部分。在保持团队工作专业性和玩家体验最优化的同时，也要与平台方密切合作，尽力寻求多方的共赢点，从而满足所有平台方的需求。<br>
<br>
<strong>自制 vs. 引进</strong><br>
<br>
前文中提到，在《命运2》的跨平台系统开发中，许多新系统的引入需要开发者在自行开发还是引进第三方服务中做出抉择，其中主要需要考虑的几点因素为：<br>
<br>
解决方案提供的库当中必须囊括所有运营平台；<br>
<br>
虽然自行处理数据的成本小于使用第三方的成本，但是长期维护系统所带来的持续成本是高昂的；<br>
<br>
第三方平台接入的难易度以及文档、培训以及后续支持。<br>
<br>
以第三方文字过滤器为例，一些供应商在过滤不文明用语时加入了机器学习模块来分析语境，这些系统能将例如"You are a f***ing idiot"识别为侮辱性语言，而"This game is f***ing awesome"为正向舆论，类似的模型训练效果需要雇佣更专业的技术人员。同时需要考虑的其他因素有：该解决方案是否应用于所有有需求的语言，有无其他工具帮助管理识别屡次违规的成员，以及这个流程对现有流程有何影响。最终，《命运2》的跨平台团队引入了第三方语音聊天解决方案和文字聊天过滤器。而对于文字聊天功能，开发团队选择搭建自有的文字聊天服务，以便于未来系统的拓展。<br>
<br>
<div align="center">
<img aid="1051666" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095507ihhh1bivmshh1hmc.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095507ihhh1bivmshh1hmc.png" width="600" id="aimg_1051666" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095507ihhh1bivmshh1hmc.png" referrerpolicy="no-referrer">
</div><br>
<strong>功能模块逐步上线</strong><br>
<br>
对于《命运2》来说，跨平台游戏项目开发之前游戏就已经运营了一段时间，要在不干扰游戏正常运营的情况下对跨平台功能进行落地，是一项非常富有挑战的任务。Bungie跨平台项目组的主要策略为：首先工作室内部先进行了约10人左右的测试，保证程序不会崩溃，然后再把测试规模扩大到内部约500名员工。测试规模逐步扩大可以给所有平台的技术调整留下充足的时间。《命运2》中会提前一个赛季将变动较大的技术模块与新增的UI引入，以便于给后续的测试和稳定性维护留足时间，也使得开发者有足够的时间去收集反馈并做出调整。如此一来，在内部Alpha测试和Beta公测之间，开发者能够对即将上线的内容拥有足够的信心。<br>
<br>
然而这种更新模式也不是完美的。在游戏早期逐步加入跨平台游戏功能模块，也带来了一些风险：玩家曾经无意中提前进入了跨平台游戏模式。这些“意外”在暴露了系统bug的同时，也拉高了玩家对于正式上线的期待值。<br>
<br>
<div align="center">
<img aid="1051667" zoomfile="https://di.gameres.com/attachment/forum/202208/29/095507ock2oj4bjgc2cmws.png" data-original="https://di.gameres.com/attachment/forum/202208/29/095507ock2oj4bjgc2cmws.png" width="600" id="aimg_1051667" inpost="1" src="https://di.gameres.com/attachment/forum/202208/29/095507ock2oj4bjgc2cmws.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
跨平台游戏开发意味着要调整许多依赖于平台层的接口和引擎，以加入许多全新的系统及服务来支持跨平台功能。新加入的系统和服务需要衡量开发与维护成本，以辅助决定该功能是开启自研或是接入第三方服务。在跨平台功能开发的过程中许多第一方的需求会影响到游戏设计和玩家体验，这些特定需求需要在项目早期进行梳理以便能够更有序地嵌入整个开发流程中。<br>
<br>
打通平台之间的壁垒意味着将拓宽玩家社群边界，也意味着可能产生未曾见过的玩家违规行为的风险。在项目早期应及时分析提出此类风险，并寻找对应解决方案以保护游戏玩家生态。在项目早期应尽早将涉及底层代码调整的功能优先级提高，从而降低新功能对整个系统稳定性的影响。功能分批上线时，可依次扩大测试规模，为功能的正式上线提供及时反馈和保障。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：雷火UX用户体验中心</font></font><br>
<br>
  
</div>
            