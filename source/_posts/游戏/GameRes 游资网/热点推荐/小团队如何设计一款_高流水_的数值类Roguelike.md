
---
title: '小团队如何设计一款_高流水_的数值类Roguelike'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202103/30/113233mohqyhmhohqgyg5b.jpg'
author: GameRes 游资网
comments: false
date: Invalid Date
thumbnail: 'https://di.gameres.com/attachment/forum/202103/30/113233mohqyhmhohqgyg5b.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2490862">
导语：《提灯与地下城》再次抬高了Roguelike的天花板。<br>
<br>
以Roguelike为标签的小众市场最近又热闹了起来。《黑帝斯》收下TGA年度最佳动作游戏奖；《重生细胞》登顶iOS付费榜首；近日面市的《loop hero》首周销量突破50万份，《重生旅人》《无间冥寺》也均收获市场口碑；3月2日上线的《提灯与地下城》（以下简称“提灯”）更是稳居畅销榜前十超过一周时间，目前预计iOS单渠道流水就有6千万元。这些产品集中亮相，给行业注入了生机。<br>
<br>
<div align="center">
<img id="aimg_969069" aid="969069" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113233mohqyhmhohqgyg5b.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113233mohqyhmhohqgyg5b.jpg" width="458" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113233mohqyhmhohqgyg5b.jpg" referrerpolicy="no-referrer">
</div><br>
Roguelike究竟是什么样的游戏？这里我们再次诠释下：2008年，国际Roguelike发展会议对这类游戏做出了明确的定义，认为具有生成随机性、进程单向性、不可挽回性、游戏非线性、画面朴素性、系统复杂性可被称作Roguelike（以下称“Roguelike”）游戏，这一定义被命名为“柏林诠释”。<br>
<br>
不过随着行业发展，不少Roguelike游戏跳脱出了这一“柏林框架”，增加了许多新元素，在Roguelike+X这道填空题中做出了更多的变化。譬如兼具视觉与动作爽感的《空洞骑士》、打磨射击体验的《霓虹深渊》、卡牌构筑的《杀戮尖塔》、同步回合制的《不思议的皇冠》和音乐类的《节奏地牢》。<br>
<br>
不可否认，这些微创新的佳作都在将这个品类“做宽”，然后受到越来越多玩家的簇拥，进而得以在市场上大放异彩。<br>
<br>
同样地，《提灯》也并非是一款严格意义上的Roguelike游戏。虽有随机关卡，复杂系统，但并无不可挽回、进程单向性的特性，所以称它为Roguelite会更为贴切——如《提灯》的亮点在于，复杂的数值系统所带来的成长体验击中了硬核玩家的需求所在，玩家们在社群中讨论最多是关于某个关卡要搭配哪把武器，技能先升级哪个最好、培养哪种契约兽，装备如何配置等等。该作的发行商青瓷游戏COO曾祥硕在一次演讲中也表达了对这一用户的理解：“Roguelike硬核玩家的目的就是挑战力更难，你要给我最牛逼的怪物让我去打，更为复杂的系统让我去研究，他想要的追求可以类比是体育精神：更高、更强、更快。”<br>
<br>
<div align="center">
<img id="aimg_969070" aid="969070" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113233bsu8x6cgdqwxmmzh.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113233bsu8x6cgdqwxmmzh.jpg" width="408" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113233bsu8x6cgdqwxmmzh.jpg" referrerpolicy="no-referrer">
</div><br>
由此看来，《提灯》能做到近400万玩家注册，肯定得益于青瓷对于该游戏核心用户的需求把握，游戏后来也的确做到了超过30万的PCU（最高同时在线人数）。这也成为业界热议的焦点——到底这款游戏用了什么新的方式去重新装入数值这套内核，而游戏的整个数值成长体系又是如何搭建的，和Roguelike又有多少关联的地方？本文将深入拆解《提灯》的核心数值系统，思考现今Roguelike+数值的市场潜力。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">系统设计</font></strong><br>
<br>
<div align="center">
<img id="aimg_969071" aid="969071" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113234l3vcr6ri32ci22ni.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113234l3vcr6ri32ci22ni.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113234l3vcr6ri32ci22ni.jpg" referrerpolicy="no-referrer">
</div><br>
《提灯》可以看作是一款纯粹的数值类Roguelite，开发商吉事屋将自己对于Roguelike的理解在这部作品上进行了重新表达，同时也几乎是摒弃了叙事、社交、美术等产品要素的追求，全力以赴在数值体验上。那么它也有着以下特色：<br>
<br>
随机生成，轻度刷关：采用2D卡通的朴素画风、俯视角竖屏设计的《提灯》在关卡中沿袭了该品类的道具随机掉落、怪物随机出现和地图随机生成的鲜明特性，还以古早味。同时在战斗中精简了操作性，只要“刷刷刷”就可以玩下去，实现单手操作的简便，迎合当下广泛休闲玩家的需求。<br>
<br>
多线性的数值养成：开发商对数值体验贯注一心，在游戏内容中追求复杂多样的数值系统，由多个纵向的装备+技能+契约兽组搭的战斗build，丰富了游戏的可玩性和耐玩度。<br>
<br>
这与Diablo（暗黑破坏神）似乎有着异曲同工之妙，角色、关卡和装备等养成系统彼此交叉耦合。以角色为基，配合养成系统衍生出各式数值体验和build流，同时随机关卡既是资源的产出地，也是成长数值的验证。<br>
<br>
<div align="center">
<img id="aimg_969072" aid="969072" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113234q31s44mco2ebmy9g.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113234q31s44mco2ebmy9g.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113234q31s44mco2ebmy9g.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">“刷刷刷”游戏循环模型</font></font></div><br>
“肝”是这款游戏最让玩家经常揶揄之处，他们时不时会吐槽刷图太累、装备难弄、宠物难养，但这些内容又总能让他们嗜此不疲，就连网上的开挂器、代刷等买卖交易也均是提供“肝等级”、“肝装备”和“肝宠物”三大服务。<br>
<br>
而“肝等级”，就不得不提到涨等级经验的关卡设计。<br>
<br>
<strong>1.1关卡系统</strong><br>
<br>
<div align="center">
<img id="aimg_969073" aid="969073" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113234mnpz9psomlfl9nxs.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113234mnpz9psomlfl9nxs.jpg" width="465" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113234mnpz9psomlfl9nxs.jpg" referrerpolicy="no-referrer">
</div><br>
正如上文所述，战斗关卡以深渊这一地下城的场景元素，主打竖屏自动刷怪的“傻瓜式”操作和Roguelike的随机设计。<br>
<br>
轻度化：“刷刷刷”的关卡系统比Diablo简化许多，为了追求轻度性，实现手段有三：其一是怪物站位固定，剔除了移动战斗的复杂性；其二是自动刷怪，玩家只要移动至怪物单位，就会触发自动战斗机制；其三是不要求玩家清掉所有怪物。单个关卡设有10层地下城，只要玩家找到每层的入口，干掉关卡boss即可通关，这也解决了刷图的效率问题。<br>
<br>
战斗中途还设有撤退按钮、获得回城石可以直接回城、技能魔力值自动回复、免费复活一次等这些“亲民”设计无一不是从Roguelike过去的那种严格规则中进行再度创新，弱化惩罚机制，减轻玩家的挫败感，以低门槛的要求吸纳更多除硬核玩家以外的泛用户群体。<br>
<br>
新鲜感：在完成轻度性之余，作为一款类Roguelike游戏，刺激玩家新鲜感的巧思也是必不可少。此时关卡的随机性已呼之欲出。具体体现在地图随机、掉落随机、怪物随机三个要素。玩家每次进入同一张地图，路径走向随之变化，空间构造几乎都有所不同。这种变化也赋予怪物、道具位置的随机性。<br>
<br>
还有提灯调节、许愿池、洞口、中等怪物的设计增加道具掉落爆率，不间断地给予玩家“开盲盒”的惊喜感。<br>
<br>
关卡难度设计：依据关卡难度的测算，怪物和角色的数值大致是按照一定的公式，设计出约1:10的比例关系。打比方说，影响战斗最大的两个属性是生命和伤害，如果怪物伤害设为1，角色生命便是10，反之同理。<br>
<br>
<div align="center">
<img id="aimg_969074" aid="969074" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113235n334x34kli34tj33.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113235n334x34kli34tj33.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113235n334x34kli34tj33.jpg" referrerpolicy="no-referrer">
</div><br>
这仅是战斗双方的力量对比，如果分析通关难度，还需涉及时间概念，引入秒伤数值，即单位时间内造成的伤害值。举例来看，如果怪物生命10，伤害1，攻速2秒；角色生命10，伤害1，攻速1.25秒，消灭怪物所需的攻击次数为首领生命/角色伤害=10次，总用时为攻击次数*攻击时间=12.5秒，而怪物总用时是10*2=20秒，所以角色能更快击败怪物。因此只要怪物数值在这个比例之下，就可以满足通过条件。当然boss的这个比例还会更大，1:50、1:100……用时也与之翻倍。<br>
<br>
另外，战斗双方本身的数值比拼只是“大趋势”，而角色的技能效果和契约兽的辅助能力也会一定程度上影响结果走向，怪物也会设定特殊效果相互抗衡，在实际中产生“小变化”，令战斗体验横生趣味。<br>
<br>
<strong>小结：</strong><br>
<br>
1.轻度化即要求轻松和高效，但关卡设计中还存在与该目的相驳之处。第一，令玩家痛心疾首的是没有扫荡功能和手动跑图，即使游戏实现了单手操作，但在战斗中，玩家还得付诸时间，投注于屏幕上；第二，因仿Diablo的装备过渡设计，在关卡内频繁地掉落装备，致使玩家经常在关卡内更换装备，拖慢刷图效率；第三，单局怪物数量不合理，再次令战斗陷入拖沓局面，容易造成玩家压力太大。<br>
<br>
2.新鲜感构筑还留有缺陷。其一，玩法重复，除了关卡难度有所变化之外，开局第一张图和后续关卡不做差异化处理，许愿池、洞口等传统内容一直延续，没有新意。怪蛋岛和无尽深渊亦是如此，反复“开蛋”和首领挑战贯穿着整条关卡线；其二，尽管关卡次数加入精力值的设置，防止玩家借助脚本和外挂无休止的刷图，以及避免玩家对内容体验过度，产生疲倦感，但是这一设置仍有不足。目前，精力值消耗过慢，300左右的精力值，1点精力的消耗大约要花费1至2分钟，导致玩家一天的刷图时间可以达到5至8小时，结果还是会造成玩家后面对重复的玩法倍感枯燥，且在随机性的机制下，玩家一时得不到明显的成长体验后也容易流失；其三，简单重复的关卡场景设计差强人意，视觉体验明显不足。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_969075" aid="969075" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113235lf9jyeyxirxerhy6.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113235lf9jyeyxirxerhy6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113235lf9jyeyxirxerhy6.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">好游快爆评价</font></font></div><br>
3.撤退设有短暂的惩戒时间，大约2秒，遭受怪物攻击伤害一次。这一时间帧从玩家体验上很好地隔开战斗和移动两种状态，另一点或许也是官方并不希望玩家中断自己的战斗流程来打断自己的心流体验。<br>
<br>
1.2养成系统<br>
<br>
<div align="center">
<img id="aimg_969076" aid="969076" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113235fwswiu0z1uyirv8p.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113235fwswiu0z1uyirv8p.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113235fwswiu0z1uyirv8p.jpg" referrerpolicy="no-referrer">
</div><br>
用战斗肝等级，而肝装备和宠物的便是养成系统。正如玩家热议的那样，养成体系以加强角色战力属性的装备系统、战斗加成的技能系统，以及契约兽系统构成。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_969077" aid="969077" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113236zcztgkh8wwgicirh.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113236zcztgkh8wwgicirh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113236zcztgkh8wwgicirh.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">养成道具资源表</font></font></div><br>
1.2.1装备系统<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_969078" aid="969078" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113236d0zr1vb5549414ms.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113236d0zr1vb5549414ms.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113236d0zr1vb5549414ms.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">装备系统</font></font></div><br>
装备设计：装备系数有三：等级、部位和品质。装备等级偶数制（2，4，6……），配置部位10处：头部、衣物、腿部、手部、披风、武器、戒指、项链、灯具以及圣物，按品质高低划分：白<蓝<紫<金<橙、绿<红。红色品质目前还待完善，当前游戏内只上线了熔岩红装四件套。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_969079" aid="969079" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113236qh9z5yh5azhhtzh3.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113236qh9z5yh5azhhtzh3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113236qh9z5yh5azhhtzh3.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">角色属性数值</font></font></div><br>
养成情况：装备的养成通过加强装备属性，然后间接提升角色战力属性，因此装备属性和角色属性并无二异。衣物、披风、护腿和头冠增强的是抵抗性质的属性，如生命、防御、免暴；护手、武器、戒指和项链增强的是伤害性质的属性，如攻击、暴击、暴击伤害。该系统的两大养成功能为镶嵌和改造，分别提升装备的基础属性和高级属性。前者消耗宝石、打孔石，后者则消耗装备碎片、坩埚以及金币。<br>
<br>
<div align="center">
<img id="aimg_969080" aid="969080" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113236jr0k3d8krkf13rs7.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113236jr0k3d8krkf13rs7.jpg" width="425" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113236jr0k3d8krkf13rs7.jpg" referrerpolicy="no-referrer">
</div><br>
首先镶嵌是通过放置不同种类宝石，加强装备对应的攻击、暴击、暴伤、生命、防御和免暴属性。因部位与属性的相关关系，所以此处也有一个相应的前提条件即生命、防御和免暴宝石只能镶嵌于衣物、披风、护腿和头冠，而攻击、暴击、暴伤宝石只能镶嵌于护手、武器、戒指和项链。装备养成差异化的设计还能够平衡玩家对于每种宝石的消耗，不会单一追求某类宝石而导致其他宝石贬值。<br>
<br>
同时加入道具的等级设计，以合成的方式合成高一级的宝石，从而补充高级宝石的产出，正向消耗低阶宝石。<br>
<br>
<div align="center">
<img id="aimg_969081" aid="969081" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113237t1w6oszy7z97wks4.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113237t1w6oszy7z97wks4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113237t1w6oszy7z97wks4.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">宝石icon</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_969082" aid="969082" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113237enz8b20bnn2t56gi.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113237enz8b20bnn2t56gi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113237enz8b20bnn2t56gi.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">宝石加成数值</font></font></div><br>
另外，宝石镶嵌的一个必要条件是先有镶嵌位。为了丰富游戏的策略性，单个装备顶多有三个镶嵌位，但游戏加入“绑锁”设计，借助打孔石解锁，且装备分解后打孔石不会回到玩家手中。这一设计与装备过渡形成矛盾体，倒逼玩家步步判断是否给当前装备解锁。<br>
<br>
相比镶嵌100%的增益效果，改造功能有概率会产生负面效果，即在消耗装备碎片和金币后，出现削弱装备高级属性的情况。但是如果装备的某条属性数值较高，可以消耗一个坩埚锁定该属性词条，避免被削弱，这也是需要玩家研究策略的思考点。<br>
<br>
另一点，碎片为装备分解物，单个装备可分解5个相应品质的碎片，消耗碎片以养成装备不失为一种正向的释放，鼓励玩家多刷装备，分解改造。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_969083" aid="969083" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113237ymwhk0s114188akd.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113237ymwhk0s114188akd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113237ymwhk0s114188akd.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">改造消耗数值</font></font></div><br>
<strong>小结：</strong><br>
<br>
1.在设计上，每一偶数等级的装备，含一系列不同部位、不同品质。同一部位、同一品质还设多副属性不一的装备，等级、部位、品质以及属性，这便造就了装备的丰富度，足以满足玩家前期的研究需求，组建不同的装备build。<br>
<br>
<div align="center">
<img id="aimg_969084" aid="969084" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113237lknwtjqf87477n4y.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113237lknwtjqf87477n4y.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113237lknwtjqf87477n4y.jpg" referrerpolicy="no-referrer">
</div><br>
2.两个功能分别加成基础和高级属性，宝石、碎片等道具再分开加成，这种分而治之的设计，不仅符合玩家常识（衣物+保护值，武器+伤害值），平衡各个道具和装备的价值，还合理地控制变量，不会出现集中累加导致数值爆炸，游戏节奏过快的问题。<br>
<br>
3.装备分解后，曾消耗过的宝石、碎片归还给玩家，从而减轻玩家养成操作的惩罚机制。<br>
<br>
4.道具设有升级、进阶功能，可以根据游戏内容情况无限往后拓展，以便长线运营。<br>
<br>
5.开不开镶嵌位、锁不锁词条，一系列的选择障碍，可以实现在复杂中强化策略性，让游戏可玩、耐玩的目的。<br>
<br>
1.2.2技能系统<br>
<br>
<div align="center">
<img id="aimg_969085" aid="969085" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113238x7hzbd8ao1cao7bi.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113238x7hzbd8ao1cao7bi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113238x7hzbd8ao1cao7bi.jpg" referrerpolicy="no-referrer">
</div><br>
技能设计：技能种类总计8个主动+10个被动，前者是为了控制人物养成节奏与游戏整体节奏，后者是为了游戏的好玩度，其效果在战斗中得以体现，一定程度上影响战斗的结局。战斗时玩家仅可配置4个技能格，主动技能手动释放，被动概率性自动触发。大多数的技能自行一体，仅同心术会按其技能等级效果，一定比例将契约兽的生命、防御和攻击值加于角色属性中。<br>
<br>
养成情况：技能升级消耗魔法卷轴、金币。消耗数值按一定规律类推，每一级别的技能加成也按固定比例升级。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_969086" aid="969086" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113238g9f6s6t66u129ss1.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113238g9f6s6t66u129ss1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113238g9f6s6t66u129ss1.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">技能养成消耗数值</font></font></div><br>
<strong>小结：</strong><br>
<br>
<ul type="1" class="litype_1"><li>从技能的效果看，无疑给战斗效果加分。比如主动的技能释放带来的明显的伤害效果，被动技能的自动躲闪、回血、加防和给怪物的debuff，厚实刷图场景下的战斗趣味。</li><li>技能升级的深度同样可以往后拉长，做长线准备。</li><li>在限制技能携带数量的前提下，玩家可以研究不同副本的技能选择，打出多种技术流。但由于技能的养成幅度过窄，以及特效、属性飘字重叠等原因，让玩家很难在视觉冲击上感受成长变化。<br>
</li></ul><br>
1.2.3契约兽系统<br>
<br>
<div align="center">
<img id="aimg_969087" aid="969087" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113238ooz3kobk23yrt89r.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113238ooz3kobk23yrt89r.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113238ooz3kobk23yrt89r.jpg" referrerpolicy="no-referrer">
</div><br>
契约兽设计：契约兽作为角色以外的另一个养成个体，辅助角色战斗，但成长独立。培养内容含天赋、基础属性和技能。目前游戏内已上线22个契约兽，涉及5个种类（格斗、防御、治疗、超能和冒险），6种品质（普通、珍奇、超稀有、超觉醒、超巨力和终极化）。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_969088" aid="969088" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113239gvcncblvb6bsncbb.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113239gvcncblvb6bsncbb.jpg" width="451" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113239gvcncblvb6bsncbb.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">契约兽属性图</font></font></div><br>
养成情况：其培养模块也可谓是更为丰富，等级、进化、技能、觉醒、天赋置换和契约兽装备。糅合多项提升途径的契约兽培养系统，所需的道具种类也多样。<br>
<br>
<div align="center">
<img id="aimg_969089" aid="969089" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113239hag12d8gb077a1g2.gif" data-original="https://di.gameres.com/attachment/forum/202103/30/113239hag12d8gb077a1g2.gif" width="480" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113239hag12d8gb077a1g2.gif" referrerpolicy="no-referrer">
</div><br>
首先，“食用”兽肉提升契约兽等级，兽肉按品阶划分为小块（+300经验）、普通（+1500经验）、高级（+7500经验）、顶级（+45000经验）。可以发现的是，前三者加成比例是前者*5，顶级兽肉的加成则是前者*6，可见顶级兽肉性价比更高。<br>
<br>
<div align="center">
<img id="aimg_969090" aid="969090" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113239wfsx1ckns1npnr0p.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113239wfsx1ckns1npnr0p.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113239wfsx1ckns1npnr0p.jpg" referrerpolicy="no-referrer">
</div><br>
其次，契约兽进化相应设定级别，自初代至三世，装备碎片的产消设计也如法炮制地应用于进化之中。进化所需的契约兽精华和契约兽之心或巨心，资源从契约兽分解中所得。之心和巨心来源于珍奇和超稀有以上的契约兽，也只适用于对应品质的契约兽。超稀有以上品质的契约兽，产率远低于珍奇契约兽，设计之心和巨心两种道具分开消耗，从而也达到控制不同品质的宠物的成长难度的目的。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_969091" aid="969091" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113240hjbuxj7ux1t5jlzn.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113240hjbuxj7ux1t5jlzn.jpg" width="324" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113240hjbuxj7ux1t5jlzn.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">进化消耗数值</font></font></div><br>
再者，与角色相仿的是，契约兽也具备技能：专属、基础和特殊三类技能。契约兽进化会同比提升专属技能等级，而其他技能的获取和升级则借助技能书，实现这一功能便是学习和融合，前者习得技能，后者解锁技能。<br>
<br>
<div align="center">
<img id="aimg_969092" aid="969092" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113240j189deauqz9ywtwq.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113240j189deauqz9ywtwq.jpg" width="471" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113240j189deauqz9ywtwq.jpg" referrerpolicy="no-referrer">
</div><br>
学习功能旨在配置新技能。目前珍奇品质设有5个技能格，超稀有以上6个。起先契约兽仅拥有专属和基础两个技能，消耗不同的技能书则可以增加相应技能。技能书可分为通用类和附属类，通用类共三个等级，加强契约兽属性；附属类顾名思义，即强化通用类的技能效果。<br>
<br>
在这之上，游戏又在这里设置“绑锁”，将后两个技能格锁住，解锁便是融合功能所负责的内容。玩家可以牺牲一只10级的同系契约兽技能，消耗一个融合石解锁另一只的新技能，即融合不仅解锁技能格，还可以把A的技能转至B身上。该功能的高明之处在于减轻惩罚，即便玩家技能学习失误，也可以通过融合将技能转移至所要培养的契约兽。<br>
<br>
然后，跟融合功能不同的是，天赋置换是A和B的天赋交换，且只能是同种契约兽。玩家发生天赋改造行为只会在拥有低品质的满天赋契约兽的前提下，这样他们才会用高品质向低品质互换天赋。但满天赋契约兽产出概率极低，改造功能相当于摆设。不过游戏内又为天赋培养增设了一个小功能：消耗迷幻彩糖，可以提升或降低小于1的天赋值。<br>
<br>
<div align="center">
<img id="aimg_969093" aid="969093" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113240ewc9l2lblb2w5qn2.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113240ewc9l2lblb2w5qn2.jpg" width="385" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113240ewc9l2lblb2w5qn2.jpg" referrerpolicy="no-referrer">
</div><br>
接着，契约兽觉醒是一个成长的根本性变化，按数值提升的逻辑来说，等级<进化<觉醒。一次觉醒相当于10次进化，而且契约兽属性、技能和天赋均会发生质变，觉醒后的契约兽在后续培养跨度上也更大。觉醒阶级分为超觉醒、超巨力和终极化三段位。具体觉醒条件如下：<br>
<br>
<div align="center">
<img id="aimg_969094" aid="969094" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113241rtzhrj2roacwoabf.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113241rtzhrj2roacwoabf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113241rtzhrj2roacwoabf.jpg" referrerpolicy="no-referrer">
</div><br>
最后，契约兽装备设计4个等级4个部位5种品质。同一部位装备，能以逐级逐阶的方式合成高品质，合成比例3：1，间数累计20次，可见难度之大。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_969095" aid="969095" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113241p96ni09cviyz0l8i.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113241p96ni09cviyz0l8i.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113241p96ni09cviyz0l8i.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">契约兽装备</font></font></div><br>
<strong>小结：</strong><br>
<br>
<ul type="1" class="litype_1"><li>同样地，契约兽分解后，契约兽心、精华等道具均会悉数还与玩家，无处不在的惩罚消除机制，为玩家大胆研究提供保障。</li><li>从功能和道具两点做长线设计，属性词缀、进化级别、技能书、契约兽装备等后续还能继续深挖养成坑，延伸成长线。</li><li>不同的培养机制针对性作育天赋、契约兽属性和技能属性，觉醒、融合也有等级、种类、品质等要求条件，在这些严格规则下，控制游戏节奏。</li><li>以多种契约兽和培养机制吸引养宠玩家，同时内容的丰富度也保证玩家的留存。<br>
</li></ul><br>
<div align="center">
<img id="aimg_969096" aid="969096" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113242oipj9l9jl99j9oqo.gif" data-original="https://di.gameres.com/attachment/forum/202103/30/113242oipj9l9jl99j9oqo.gif" width="480" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113242oipj9l9jl99j9oqo.gif" referrerpolicy="no-referrer">
</div><br>
<strong>1.3资源系统</strong><br>
<br>
<div align="center">
<img id="aimg_969097" aid="969097" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113243t88agg323233xndg.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113243t88agg323233xndg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113243t88agg323233xndg.jpg" referrerpolicy="no-referrer">
</div><br>
知晓数值消耗，那么也得让玩家有资源可肝。<br>
<br>
对于一个普通玩家来说，攫取战斗关卡的产出是最为普遍的方式。<br>
<br>
关卡内容的资源投放几乎可以满足玩家前期的成长（排除与金钱挂钩的钻石、特殊契约兽以及不重要或稀少的道具外），但在游戏内兼具多种商业化活动的前提下，这种光肝不氪的成长也可想而知，其节奏相对缓慢。<br>
<br>
就单局的产出来看，各项道具数远低于各个养成系统的起始点，而又因精力值的限制，普通玩家单日获取量受限，成长进度自然迟缓。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_969098" aid="969098" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113243y5me7m8moie993lz.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113243y5me7m8moie993lz.jpg" width="455" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113243y5me7m8moie993lz.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">单局掉落截图</font></font></div><br>
而对于硬核的活跃玩家和付费玩家而言，资源的优渥度高于普通玩家是理所应当的事。对于这两类玩家，曾祥硕曾言到：“在细分品类要做大一定要迈出商业化的槛，泛用户中付费的需求是充值要变强，不仅充值变强，所有都要变强，一眼能看出付费玩家，他需要社交圈。硬核用户什么都要自己打，他要肝，他要技术流。”<br>
<br>
其中，对于活跃玩家而言，与普通玩家区别的是，可以更快囊括游戏内的绝大部分活动奖励。<br>
<br>
为什么会这么说？具体来看促活设计中的任务、成就、派遣活动的资源产出。<br>
<br>
任务产出：任务的设计目的就是提供目标性奖励，鼓励玩家活跃。无论是单日任务、单周任务，还是主线任务，活跃玩家理应所花的周期时间相对更短。在关卡产出的基础之上，还可更快收罗任务产出；<br>
<br>
成就产出：成就产出也是同样的道理，撇开第四项因涉及付费门槛之外，前三者关乎装备战力、宠物培养和关卡进度的成就奖励，毫无意外活跃玩家获得更快；<br>
<br>
派遣产出：派遣奖励数额取决于契约兽的进化段位，鉴于活跃玩家的契约兽培养进度的优势，自然在派遣活动上的收获更足。<br>
<br>
<div align="center">
<img id="aimg_969099" aid="969099" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113243jememdy0lz58zef5.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113243jememdy0lz58zef5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113243jememdy0lz58zef5.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">活动资源产出表（n表所占当前升级经验按一定比例掉落的范围值）</font></font></div><br>
通过估算三者单日产出的最大额度，也足见收益较关卡产出更为丰沛。<br>
<br>
尽管复杂的数值系统能满足硬核玩家研究技术的乐趣，但超200万用户中，想必泛用户所占比例不小，而经济系统所发挥的效用，不仅是协调数值，也是稳固用户之间的分层生态。<br>
<br>
而泛用户的付费需求又当如何满足？据曾祥硕所言，这类用户的付费需求是充值后要有明眼可见的成长，欲求更为充分的养成体验。那么游戏中的经济系统是否能实现他们心中所求。<br>
<br>
具体来看，商业化内容包含女神祝福、罗德夫投资以及五郎店。<br>
<br>
女神祝福：奖励设计为刷图次数翻倍+效率提升+额外任务奖励。如果同样的肝，很明显付费玩家所获资源是其他玩家的2倍，这对付费玩家而言吸引力十足。并且两种祝福可以叠加，也避免让已充25元档的玩家再充98元档后的挫败感，从而也能提高玩家对98元档的转化。<br>
<br>
罗德夫投资：瞄准玩家的得失心，先让玩家付出成本，后期再以诱惑力十足的投资回报留住玩家，提升玩家的留存。活动分为28元档和68元档，奖励条件分为达成角色等级和契约兽进化等级。其奖励设计更为优厚，性价比更高，并独有的高级资源产出，譬如高级技能书、装备、顶级兽肉、稀缺道具，同时替玩家省了赌博随机掉落的时间。<br>
<br>
五郎店：活动时间分为单日和单周。单日充值额度为6/18/30元档，奖励为钻石和契约兽巨心。单周充值额度为18/30/128/328/648元档，同投资活动一样，这里同样是一些高级资源的唯一产出地，譬如特殊契约兽、派遣道具以及高级黄金罐。<br>
<br>
<strong>小结：</strong><br>
<br>
可以发现，从关卡-活动-付费，奖励回报层层递进。经济系统的奖励，不仅是高级且稀缺道具的产出地，资源产出丰厚，另一点，也是最为重要的一点，即大量钻石的积攒。<br>
<br>
为什么说它重要？因为钻石不仅仅与充值额度挂钩，更是作为一般等价物，在游戏内兑换其他资源。而兑换的场所则在于杂货铺、兑换店和罐子头这样的交易系统。<br>
<br>
众所周知，《提灯》没有联机功能，更像是一款单机游戏，玩家各自独立，不会发生自由贸易。玩家的交易需求就只能容纳在标准化的交易场所里。杂货铺和罐子头均不设置交易次数和刷新次数，并含有各个养成系统的成长道具，也就意味着，只要有钱，就能不断roll道具、兑换道具，升级战力。另外前面也说到关卡不做等级绑定，只和战力相关，这让高战力的大R巨R们更快地可以拿到后续关卡中掉落的优质奖励，成长体验更足，这也让其他层次的玩家无法媲美。<br>
<br>
<strong><font color="#de5650">产品总结</font></strong><br>
<br>
“深渊黑暗，记得提灯啊！”这句slogan恐怕是每个玩家在进入游戏后输入的第一条兑换码。该作融入独特的“灯芯亮度调节”玩法，结合地下城探险与宠物养成进化玩法，引入顶级装备刷图可得的无限制全局掉落机制，粘合成一款刷刷刷的Roguelike游戏，圈住了不同类型受众的爽点。<br>
<br>
宛若游戏写在应用商店里的意思，针对普通玩家，易于上手的竖屏操作、随机掉落体验和简单易懂的功能设计都让他们倍感游戏的乐趣所在；又如对于硬核玩家来说，海量的装备和词缀、技能、天赋，随意搭配build，无疑满足了他们想要的可玩性和复杂度。而几十种形态各异的契约兽和丰富的培养系统，也餍足爱宠玩家的收集养成欲。<br>
<br>
<div align="center">
<img id="aimg_969100" aid="969100" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113243xsietd4pseeroyoo.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113243xsietd4pseeroyoo.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113243xsietd4pseeroyoo.jpg" referrerpolicy="no-referrer">
</div><br>
不过从游戏体验上，《提灯》都只能算是做到了尽善尽美，还有诸多的地方令人心存疑窦。<br>
<br>
<strong>优点：</strong><br>
<br>
<ul type="1" class="litype_1"><li>数值：主打纵向成长，养成系统彼此相对独立。减少交叉耦合的关系，不仅降低用户的理解门槛，更是缩减数值的影响因子，同时关卡和经济也容易估计对不同玩家一个产出阈值，二者综合起来便于各项数值的计算，统计角色战力进度，从中逆推关卡的难度设计，避免数值Bug的出现。加之每个系统下又细分对不同属性数值的加成，使数值成长的节奏趋向可控。</li><li>留深坑：从功能和道具两点做长线设计，等级，类别，品质等等，后续均可继续深挖，填补游戏内容。</li><li>策略性：开镶嵌位、锁词条，契约兽融合，技能升级等，在复杂的数值系统中设下更多的“选择题”，强化成长的策略性。</li><li>耐玩度：在等级、类别和品质的划分因子下，可以快速打造富足的养成内容来保证游戏的耐玩度。</li><li>随机性：随机关卡、随机掉落、随机怪物的Roguelike元素刺激玩家的投机心理，增强对玩法内容的探索欲。</li><li>激励设计：装备、宠物分解后，身上的养成道具大多会返还给玩家，“失去—找回”的惩罚消除机制让玩家感知游戏的良心，可以不计成本地试错，为玩家对数值的研究提供天然的保障。且这种机制只是材料的转移，并非数值层叠，所以也不会出现数值暴涨的问题。</li><li>付费体验：交易活动不做次数限制，高付费玩家的成长体验愈发良好，转化越高，助推游戏商业化。<br>
</li></ul><br>
<strong>缺点：</strong><br>
<br>
<ul type="1" class="litype_1"><li>关卡战斗的轻度化尚待完善，关卡内的随机内容仍可新增，提供新意。</li><li>由于自动刷怪的设计，游戏的策略性主要体现于战斗之外的养成系统，而随意试错，反而降低了策略性。</li><li>对于零氪玩家来说，成长进度过慢，掉落收益太低，功能开启过于滞后，难以反哺至战斗体验上，整体在前期留存能力上还有待深究。</li><li>没有社交玩法，单一排行榜也刺激不了玩家的优越感，这些无疑让整体的游戏内容变得单薄，容易让泛用户流失。</li><li>没有职业设计，个别装备、契约兽具有属性优势，技能数量偏少，导致每个人的build体验趋于雷同，差异化体验不明显。</li><li>活动略显单一，如果加入更多随机玩法和奖励数额，还可以提升收费能力。<br>
</li></ul><br>
<strong><font color="#de5650">品类展望</font></strong><br>
<br>
2018年成立的8人工作室—吉事屋，用两年的时间，就做出了一款上线不到一个月，就拥有近400万注册和6000多万流水的《提灯》。其实不难发现，笃定Roguelike这条赛道的，大都是小团队，《提灯》的，《黑帝斯》的20人SuperGiant，《死亡细胞》的11人Motion Twin等等，为何小团队会对这个品类倾心？<br>
<br>
我们知道，制作成本、技术要求、项目管理、开发人手等无一不是小团队所避不可及的掣肘。而Roguelike程序化的随机道具和关卡会大大降低制作成本，技术要求也不高，吉事屋曾用Cocos来实现《提灯》的Demo，并且这种小而精的产品让团队更容易把控项目，如果是制作《提灯》这般的单机Roguelike更是不成问题。天生的非线性流程内容的设计也在耐玩度和丰富性上有着得天独厚的优势，让团队短时间内不用担心因内容消耗过快造成用人短缺的局面。<br>
<br>
那么小团队做Roguelike，真的能以小博大吗？如今这么多好作品突然扎堆的趋势下，似乎预示着这个小众品类已有不容小觑的市场规模，而且不少新作已经在路上。心动代理的单机Roguelike《龙套英雄》在前不久拿到了版号，B站投资了克苏鲁题材Roguelike《无光之夜》的开发商成都洛斯特，《小小勇者》《虚无之印》等更多的Roguelike游戏挤进TapTap的预约榜，《霓虹深渊》《不思议的皇冠》等诸多PC端的精品也已开启手游预约，可以见得这个小众品类的热度，或还会在未来延续，此刻加入，不失为一个机会点。<br>
<br>
<div align="center">
<img id="aimg_969101" aid="969101" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113244hi4kkscjskcqt9jq.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113244hi4kkscjskcqt9jq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113244hi4kkscjskcqt9jq.jpg" referrerpolicy="no-referrer">
</div><br>
而我们也知道，当下Roguelike创新的方向很多，厂商往往会选择其中一个或者几个维度来深挖。<br>
<br>
<div align="center">
<img id="aimg_969102" aid="969102" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113244noen20w0lxox0hss.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113244noen20w0lxox0hss.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113244noen20w0lxox0hss.jpg" referrerpolicy="no-referrer">
</div><br>
在笔者看来，近年来爆火的Roguelike可分为两类：一是以《黑帝斯》等为首的操作类，二则是《提灯》这样的数值类。有不少在该赛道上的从业者表示，《黑帝斯》已经是操作类的天花板了，突破的希望几乎为零，那么数值类这样的一个“填表项目”不仅能够在短时间内完成，而且可以博的机会或许还能更大些。<br>
<br>
而雷霆和青瓷算是这个细分品类的佼佼者，已成功运营《贪婪洞窟》《不思议迷宫》等多款经典的Roguelike游戏，此次的《提灯》也是由青瓷代为发行运营，在产品上还和《贪婪洞窟》有着诸多相似之处，包括词缀属性、装备、技能等设计。所以，对于制作Roguelike+数值，我们不妨从这两家的产品哲学中窥见一二：<br>
<br>
<ul><li><strong>产品设计方面，首先弱化战斗操作。</strong>无论是《贪婪洞窟》，还是《不思议迷宫》，亦或是现在的《提灯》，都采用自动战斗机制，无疑是迎合了当代广泛的休闲玩家，其低门槛也容易转化更多的非游戏用户；其次将心力放在数值策划上，突出特色。作为一款Roguelike+数值的游戏，数值体验是玩家的核心需求所在。开发者往往会担心如果数值系统设计得过于复杂，不利于玩家留存。而事实却证明，这类游戏的玩家反倒更愿意通过研习复杂的数值来获得成长体验，进而满足自己的成就感；最后，萌宠系统不可或缺。《不思议迷宫》和《提灯》都在宠物培育上注入功力，可见养宠玩家也是这类游戏的核心玩家。</li><li><strong>用户思考方面，突破细分游戏用户规模局限性的桎梏，鲸吞泛用户。</strong>曾祥硕袒露过，公司产品的底层逻辑就是，在满足硬核用户需求的同时，用商业化吸纳泛用户。毋庸置疑，小团队要在细分品类上做大做强，就必须考虑更多元的用户。《提灯》的数值系统+轻度操作+付费设计，背后逻辑都是在让这款游戏尽量地满足不同用户的口味。</li><li><strong>长线运营方面，留足内容，保持新鲜。</strong>Roguelike游戏框架较小，容纳不了那么多内容，所以做长线关键在于投放内容的方式。而青瓷投放内容的策略，是做阶段性处理，不会一次性把内容都消耗完，玩家没玩到的部分就一直会有新鲜感，这个部分会让游戏在不更新的情况下仍然有一定的生命周期。通过《不思议迷宫》的版本内容，我们可以发现，时至今日，这款老游仍在更新全新内容，刺激玩家玩下去的动力。《提灯》也将提前放出预告：社交玩法、关卡副本、词缀属性、新道具投放等等丰厚的内容吊足玩家胃口。<br>
</li></ul><br>
<div align="center">
<img id="aimg_969103" aid="969103" zoomfile="https://di.gameres.com/attachment/forum/202103/30/113244bb5kb725q55g5ggt.jpg" data-original="https://di.gameres.com/attachment/forum/202103/30/113244bb5kb725q55g5ggt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/30/113244bb5kb725q55g5ggt.jpg" referrerpolicy="no-referrer">
</div><br>
此外，当今不少表现优异的Roguelike游戏无一不是以独特的标签深入人心。所谓师夷长技以制夷，腾讯互娱天美工作室群策划副总监张伟就曾提到：<br>
<br>
<i>千万不要过于相信“木桶理论”而去做“大而全”的游戏，因为作为小团队，不可能把游戏做的面面俱到。你必须要有非常长的长板，以此来吸引玩家，在保证游戏各方面体验没有太大问题的前提下，专注一根长板，会提高游戏的成功率。</i><br>
<br>
而《提灯》正是发挥其所长。虽在战斗、画面、剧情等方面劣迹斑斑，但也突出表达了让玩家津津乐道的数值体验。这个事实也证明了近年来不被看好的数值游戏在市场上依然大有可为。当然，《提灯》后续版本能否解决Roguelike的边际效应问题，给予玩家足够的新意？加入社交玩法后还能不能保证数值平衡？内容成本还能在控制范围内吗？新增内容还能保留Roguelike那味吗？是昙花一现还是保持持久活力，这一切都尚未可知。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：游戏陀螺</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/ikR0U7o7dS4Dw0oPezvEGA</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            