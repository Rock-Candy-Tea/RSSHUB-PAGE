
---
title: 'Bidding时代全面到来之前，如何实现Waterfall调优'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202207/22/111456b7ivwpo1w5iuuw5o.png'
author: GameRes 游资网
comments: false
date: Fri, 22 Jul 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202207/22/111456b7ivwpo1w5iuuw5o.png'
---

<div>   
<div align="center">
<img aid="1047242" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111456b7ivwpo1w5iuuw5o.png" data-original="https://di.gameres.com/attachment/forum/202207/22/111456b7ivwpo1w5iuuw5o.png" width="600" id="aimg_1047242" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111456b7ivwpo1w5iuuw5o.png" referrerpolicy="no-referrer">
</div><br>
广告收入是媒体收入的一个重要来源，特别是免费的媒体资源。<br>
<br>
举例说明一下，每当流量侧出现一个潜在的广告展示机会的时候，流量主需要考虑的是——到底展示哪个广告，才能让这次曝光机会产生最大的收益？而每个广告平台的eCPM并不是对所有APP、所有地区都一成不变的，不可能保证每次匹配给流量方的广告都是同样的价格。<br>
<br>
在无法对广告价值进行实时精准判断的情况下，会依照历史数据对广告层级进行排名能够有效地实现广告展示收益的最大化。<br>
<br>
<strong><font color="#de5650">分量策略的演变</font></strong><br>
<br>
<strong>01.Waterfall</strong><br>
<br>
聚合工具基本已经成为应用广告变现的标配，开发者可以使用聚合工具快速实现多个广告渠道分量策略，整体提升广告收益。<br>
<br>
可参考文章《<a href="https://www.gameres.com/895946.html" target="_blank">一篇文章学会广告变现聚合</a>》详细了解。<br>
<br>
对于分量策略经常被提及的就是Waterfall。<br>
<br>
Waterfall，也称为「瀑布流模型」，传统Waterfall中开发者会根据历史情况预先给各个广告平台，按照预期的eCPM从高至低排列，分别对各广告平台进行请求，当上一层没有返回广告时就向下一层进行请求，直到有广告返回。<br>
<br>
这样Waterfall可以大幅度提升FillRate，同时提升整体的eCPM。<br>
<br>
<div align="center">
<img aid="1047243" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111456iiibzfgsm9fstsgg.png" data-original="https://di.gameres.com/attachment/forum/202207/22/111456iiibzfgsm9fstsgg.png" width="600" id="aimg_1047243" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111456iiibzfgsm9fstsgg.png" referrerpolicy="no-referrer">
</div><br>
Waterfall 的策略设计很大程度上会依赖「聚合工具」实现逻辑，不同的「聚合工具」虽然虽然实现的技术逻辑相同或相似，但是在具体请求条件限制、超时判断、配置灵活度等细节都各不相同。<br>
<br>
所以如果想更深入地研究Waterfall的设计与执行效果，除了需要明确自身产品的广告场景需求（网络情况、用户平均广告频次、用户广告需求间隔、客户端负载情况等），还需要对聚合工具的使用、产品技术的实现和功能支持程度有一定了解。<br>
<br>
为了帮助各位优化师更全面地了解Waterfall的逻辑实现，我整理了以下几个常用在Waterfall里的概念术语（这些术语并不是每个聚合工具都能找到，只是做了常见的一些汇总）：<br>
<br>
<div align="center">
<img aid="1047244" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111457jpjrcjyx4cym88qh.png" data-original="https://di.gameres.com/attachment/forum/202207/22/111457jpjrcjyx4cym88qh.png" width="600" id="aimg_1047244" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111457jpjrcjyx4cym88qh.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1047245" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111457lgl4lwdodl6o88o6.png" data-original="https://di.gameres.com/attachment/forum/202207/22/111457lgl4lwdodl6o88o6.png" width="600" id="aimg_1047245" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111457lgl4lwdodl6o88o6.png" referrerpolicy="no-referrer">
</div><br>
获取高清表格请在「OPMETA优化研习社」公众号后台回复：waterfall<br>
<br>
<strong>02.In-app-bidding</strong><br>
<br>
bidding的概念在程序化购买（RTB）中被大家广泛认知，后又衍生出header bidding。从2019年开始，各家network也开始支持in-app bidding这种形式，希望逐渐淘汰掉Waterfall的传统模式。<br>
<br>
从实现的理想模型来讲，bidding有着完全超越waterfall的优势：更低的认知成本、更便捷的运营维护方式、更高的收益。<br>
<br>
<div align="center">
<img aid="1047246" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111457ueb9jttfx96rt4t0.png" data-original="https://di.gameres.com/attachment/forum/202207/22/111457ueb9jttfx96rt4t0.png" width="600" id="aimg_1047246" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111457ueb9jttfx96rt4t0.png" referrerpolicy="no-referrer">
</div><br>
所以bidding被行业推崇，尤其在2021年Facebook Audience Network开始只支持in-app-bidding方式后，in-app bidding的概念被推到了顶峰。<br>
<br>
现实来看，bidding的效果着实有些骨感。一方面，虽然大部分广告渠道都陆续支持了bidding功能，但是近两年行业内广告变现的效果越来越差；<br>
<br>
另一方面，由于很多广告渠道仍不支持bidding或为了保护自身聚合优势不对第三方聚合开放bidding接口，导致聚合不得不需要同时兼容bidding和Waterfall两种方式，这就提到了下面要说的混合模式（Hybrid）。<br>
<br>
<strong>03.Hybrid</strong><br>
<br>
Hybrid可以说是一种妥协的产物，它的实现目的是同时兼容waterfall和in-app bidding两种方式，但是执行策略就要取决于聚合工具的兼容逻辑。<br>
<br>
Hybrid的实现方式有很多，相互之间差距不大，以下给出一个参考：<br>
<br>
<div align="center">
<img aid="1047247" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111458kbrfs9nbmsdvtvd1.jpg" data-original="https://di.gameres.com/attachment/forum/202207/22/111458kbrfs9nbmsdvtvd1.jpg" width="600" id="aimg_1047247" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111458kbrfs9nbmsdvtvd1.jpg" referrerpolicy="no-referrer">
</div><br>
优先请求Bidding，随后Bidding出价结果会和传统瀑布流中的各个分层进行比较，形成新的Waterfall排序，最终让出价最高的平台获得展示机会。<br>
<br>
Hybrid在这个过渡阶段会以主要的分层方案存在，并且这个时间会持续相当一段时间。<br>
<br>
关于bidding后续有机会可以单独拿出一部分内容和大家详细聊聊，包括in-app bidding的交互逻辑、使用方式、以及Facebook只支持biding真的是为了提高开发者收益嘛？敬请期待哦！<br>
<br>
<strong><font color="#de5650">Waterfall配置策略</font></strong><br>
<br>
行业内关于Waterfall搭建说的最多的就是“三明治原则”。<br>
<br>
但是关于“三明治”具体的搭建方式和调整细节在网上能找到的并不多，以下是根据我自身的经验进行的整理说明：<br>
<br>
<strong>01.搭建阶段</strong><br>
<br>
原则：<br>
<br>
<ul><li>有数据参考，高中低</li><li>无数据参考，选自动或随机<br>
</li></ul><br>
搭建Waterfall的基本前提是已经成功对接若干广告渠道（至于如何选择广告渠道，后续会单独出一篇内容聊聊）<br>
<br>
在第一次配置时，如果能够获取到可以参考的各广告渠道数据（无论各个平台相同类别应用还是benchmark的eCPM），都可以帮助搭建最初“高中低”三部分。<br>
<br>
如果没有参考数据也不用担心，大部分聚合工具都会提供一个自动算法功能，Waterfall会按照自动算法策略进行相应的广告请求。<br>
<br>
<div align="center">
<img aid="1047248" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111458yyzbiii2xk180vbw.png" data-original="https://di.gameres.com/attachment/forum/202207/22/111458yyzbiii2xk180vbw.png" width="600" id="aimg_1047248" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111458yyzbiii2xk180vbw.png" referrerpolicy="no-referrer">
</div><br>
注：waterfall自动模式和手动模式<br>
<br>
<strong>- 自动模式：</strong>每个聚合平台会根据应用情况，根据自身算法逻辑对各广告层级进行排序，若启用自动模式，最开始会按照算法排序的顺序请求广告。而后，当这款应用的历史数据积累到一定量后，聚合平台会自动根据历史数据中各平台的eCPM高低，重新排序。（自动算法一般会兼顾聚合平台历史数据和自身平台产品利益，比如会优先请求自身的network）。<br>
<br>
<strong>- 手动模式：</strong>严格按照应用开发者自己手动对各广告层级的排序进行请求，除非应用开发者自行操作改变配置，否则永远不会变动。<br>
<br>
如果前两者都无法取得既定效果，甚至可以采用随机模式。<br>
<br>
无论怎样，这个阶段的目的是为了使大部分的广告层级获得置信的展现量级，测出每个层级的eCPM表现。<br>
<br>
一般来讲，Google AdMob的出价是会比其他广告平台要略高的，所以可以在前期搭建waterfall的时候，将AdMob排在waterfall前列，优先请求填充。<br>
<br>
AdMob也有自己的auto-high（尽可能投放价格较高的广告）和auto-mid（投放高价广告的同时兼顾一定的填充率），也可以在冷启动阶段就放入Waterfall，并手动将auto-high和auto-mid的广告层级排在waterfall前列优先请求填充。<br>
<br>
<div align="center">
<img aid="1047249" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111458gdvm14fjkdacadj3.png" data-original="https://di.gameres.com/attachment/forum/202207/22/111458gdvm14fjkdacadj3.png" width="600" id="aimg_1047249" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111458gdvm14fjkdacadj3.png" referrerpolicy="no-referrer">
</div><br>
<strong>02.调优：Trigger 1</strong><br>
<br>
搭建后，放量到一个阶段，我们是需要对Waterfall进行更改调优的。到这个阶段我们称为第一个Trigger。<br>
<br>
这个阶段开始真正意义上搭建第一个“三明治”的层级：高价层、中价层、托底层。<br>
<br>
原则：<br>
<br>
<ul><li>开始放量</li><li>等待置信</li><li>调整底价</li><li>排序层级<br>
</li></ul><br>
<strong>开始放量</strong><br>
<br>
一般为了使各个层级快速得到置信的数据，是需要量来配合的（足够的DAU）。在没有存量的时候一般可以买量进行配合，建议使用通用渠道来进行买量如Google或Facebook。<br>
<br>
<strong>等待置信</strong><br>
<br>
置信在这一阶段最为重要，数据达到一定量级才能说明问题。<br>
<br>
一般数据的粒度要精确到「层级+国家」，展现要在这个粒度上累计到至少1000广告展现（当然越多越置信），放量时间最好能平稳的持续一周（最少3天）。<br>
<br>
<strong>调整底价</strong><br>
<br>
置信后，处理积累的层级数据。然后设置各个层级底价（大部分对层级进行新建，不会在原来基础上改底价）。<br>
<br>
一般来说，我会按照这个标准来初次调整Waterfall：<br>
<br>
<ul><li>高价层底价——整体eCPM×2</li><li>中价层底价——整体eCPM×1.3</li><li>托底层——不设置底价<br>
</li></ul><br>
例：我的一款应用集成了AdMob、Unity和Applovin三个平台，在初次搭建Waterfall并使用自动模式后，三天内单个广告层级的展现量超过了1000次，且整体eCPM为$10。<br>
<br>
这时，我会调整我的Waterfall为手动模式。<br>
<br>
再设置<br>
<br>
<ul><li>高价层：AdMob $20，Unity $18，Applovin $18</li><li>中价层：AdMob $13，Unity $13，Applovin $13</li><li>托底层：Admob auto，Unity auto，Applovin auto<br>
</li></ul><br>
<strong>排序层级</strong><br>
<br>
对各个层级进行排序。<br>
<br>
这里分享下我常用的表格模版。<br>
<br>
<div align="center">
<img aid="1047250" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111459v1cszg4sc2egz19w.png" data-original="https://di.gameres.com/attachment/forum/202207/22/111459v1cszg4sc2egz19w.png" width="600" id="aimg_1047250" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111459v1cszg4sc2egz19w.png" referrerpolicy="no-referrer">
</div><br>
此外，也可以对地域单独创建Waterfall，如分国家或T1、T2、T3地区。参考数据就要细分到相应粒度。<br>
<br>
<strong>03.调优：Trigger 2</strong><br>
<br>
原则：<br>
<br>
<ul><li>按优先级排序罗列数据</li><li>先看整体，后看局部</li><li>一查填充，二查收入</li><li>优化层级，托底托住<br>
</li></ul><br>
在首次按照“三明治原则”搭建Waterfall后，放量测试，再一次达到数据置信，可以再次进行Waterfall调优。这时候我们需要注意，不要从单层Waterfall的表现看问题，要分析整体情况。<br>
<br>
很多人接入了聚合后会经历这样的场景：层级A的eCPM很高但是填充占比不高，反而是底层吃了很多的填充。于是就把顶层的底价降低了想要让顶层多吃点填充量，但是这样一来层级A的eCPM也跟着降低了，总体的收入反而变少了。<br>
<br>
一般来说，理想的Waterfall各层级填充占比为：高价层10%-20%（最高层6、7%合理，过低则需降低底价设置），中价层为30%-60%，其余为托底层，其填充率需要达到80%以上。<br>
<br>
<div align="center">
<img aid="1047251" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111459s7jjia3jc93zrcjj.png" data-original="https://di.gameres.com/attachment/forum/202207/22/111459s7jjia3jc93zrcjj.png" width="334" id="aimg_1047251" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111459s7jjia3jc93zrcjj.png" referrerpolicy="no-referrer">
</div><br>
调整思路：填充率高，向上添加高底价层级；填充率低，调低或向下添加较低底价层级。<br>
<br>
以<strong>高价层举例</strong><br>
<br>
若是Waterfall高价层某层级填充占比高于25%，则可以考虑是高价层的底价还不够高，开发者的这款应用还能够吃到更高eCPM的广告填充。相应地，若是Waterfall高价层填充率低于10%，则可以考虑适当降低高价层的底价设置，或是添加价位稍低于高价层，但高于中价层底价的广告层级。<br>
<br>
<strong>如果填充为0的话</strong><br>
<br>
首先排查问题，是否广告平台遭遇封禁等。<br>
<br>
<strong>如果填充低</strong><br>
<br>
不要马上下定论开始降底价或删除操作，特别是高价层，可以综合看看这个层级的收入占比，有时可能填充低，但是收入占比较高，也是值得留下。<br>
<br>
<strong>托底层</strong><br>
<br>
托底层只需要看填充率，不用看收入占比，只是为了吃量，托底层如果没托住，先排查问题，没问题的话需要增加其他填充佳的平台。<br>
<br>
这时候有人可能会提出疑问：<br>
<br>
为了尽可能吃到更高的eCPM，那为什么我不能每相差$1设置一个底价呢？<br>
<br>
<div align="center">
<img aid="1047252" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111459mgcg8ugvt3fnau4h.gif" data-original="https://di.gameres.com/attachment/forum/202207/22/111459mgcg8ugvt3fnau4h.gif" width="240" id="aimg_1047252" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111459mgcg8ugvt3fnau4h.gif" referrerpolicy="no-referrer">
</div><br>
如果不考虑加载效率的话，无限价格步数分层当然能使收益达到最高。但是要考虑客户端负载和广告串行请求的效率问题，如果玩家在使用应用的前几分钟触发了广告，那么可能广告无法加载出来，进而影响玩家体验，也浪费了展示机会。凭经验来看一般Waterfall能支持20-40个层级，但是也取决于聚合工具技术能力。<br>
<br>
以下为我在这个阶段常用的表格模版（按照Waterfall优先级从上至下排序）<br>
<br>
<div align="center">
<img aid="1047253" zoomfile="https://di.gameres.com/attachment/forum/202207/22/111459d9z1hzoca5apwong.png" data-original="https://di.gameres.com/attachment/forum/202207/22/111459d9z1hzoca5apwong.png" width="600" id="aimg_1047253" inpost="1" src="https://di.gameres.com/attachment/forum/202207/22/111459d9z1hzoca5apwong.png" referrerpolicy="no-referrer">
</div><br>
<strong>04.调优：Trigger 3到n</strong><br>
<br>
原则：<br>
<br>
<ul><li>循环Trigger-2思路</li><li>放长周期，切忌频调</li><li>稳定目标参考黄金比</li><li>优化的心态是稳定微调<br>
</li></ul><br>
最后这个阶段说起来相对就简单很多，但操作很容易变得迷失。<br>
<br>
整体上是要逐渐地放长观察数据周期，最开始一周一调，待数据稳定，逐渐地可能变成两周或者一个月。<br>
<br>
Tips: 一定要耐住性子，按兵不动、观察数据、细致入微会更有效，频繁调整通常会适得其反<br>
<br>
数据波动的时候除了关注自己的产品也要多观察市场情况，有些时候的波动是市场整体变化导致，如一些节日或政策变化。<br>
<br>
经过数轮的调优后，我们的Waterfall将处于一个稳定的阶段，这时我们主要以「监测」为主，除非遇到异常波动，否则不用再定期调优。<br>
<br>
如果出现异常波动，则参考「 Trigger2部分」重新回到周期性调优阶段。<br>
<br>
处于稳定阶段的产品主要有以下几个特点：<br>
<br>
<ul type="1" class="litype_1"><li>新增用户数稳定：买量稳定，展现才能稳定</li><li>买量渠道相对稳定：有规律地优化渠道，买量渠道大幅变化会导致用户属性等发生变化</li><li>广告场景等设计没有重大更新</li><li>两周时间内，eCPM和填充率的波动幅度不超过20%<br>
</li></ul><br>
需要注意的是，除了第一次调整，单次调整切忌调整过多变量，单次调整数个变量会导致无法判断哪个地方的改动是有效的、或失误的，进而影响后续的分析调优。<br>
<br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
Bidding时代全面到来之前，Waterfall的调优仍会是很多产品变现的无奈之举。<br>
<br>
Waterfall调优无论是行业里说的三明治原则，还是另有调优他路，都不是变现的唯一方法，也不是最佳方法。<br>
<br>
跟随市场方向变化、不断调优尝试，合理实验、认证猜想才是真正的优化圣经！<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：OPMETA优化研习社</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/F4d4K2-9p1AeivvwvXEsJg</font></font><br>
<br>
  
</div>
            