
---
title: '光子音频团队亮相GDC，分享游戏音频背后的技术与匠心'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202203/28/101221udved5xdaav4w56f.jpg'
author: GameRes 游资网
comments: false
date: Mon, 28 Mar 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202203/28/101221udved5xdaav4w56f.jpg'
---

<div>   
3月21日，2022年游戏开发者大会(GDC）正式拉开帷幕，作为一年一度的全球行业盛会，每届GDC上都会有不少“干货满满”的研发技术分享，吸引着全球游戏开发者们的目光。<br>
<br>
今年，光子工作室群旗下「光子技术中心游戏音频团队」（以下简称「光子音频团队」）携全球爆款PUBG Mobile受杜比实验室之邀参会，团队音频设计师「KaChuen」接受了杜比的采访，详尽地分享了PUBG Mobile在游戏音频技术上的前沿应用。<br>
<br>
<div align="center">
<img aid="1034797" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101221udved5xdaav4w56f.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101221udved5xdaav4w56f.jpg" width="600" id="aimg_1034797" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101221udved5xdaav4w56f.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图为光子音频设计师KaChuen在接受采访</font></font></div><br>
透过对采访内容的梳理及复盘，我们能够一窥「光子音频团队」深厚的音频技术储备。<br>
<br>
<strong><font color="#de5650">杜比全景声强化音效表现，团队在游戏适配性及音频细节设计上下足了功夫</font></strong><br>
<br>
回顾整场分享，GameRes认为可以从三个角度来概括其核心内容。<br>
<br>
<strong>杜比全景声的应用</strong><br>
<br>
KaChuen表示，为了满足玩家对高品质音频日益增长的需求，目前团队已经建成了一个可以录制小编制交响乐的录音棚、一个杜比全景声的混音棚和一个拟音棚，为PUBG Mobile进行了杜比全景声音频的制作，还计划未来应用在更多个项目中。<br>
<br>
KaChuen分享到，为了更好地应用“杜比全景声”这项前沿音频技术，团队在硬件配置及插件选择上下了不少功夫，也为杜比全景声量身定制制作方式，充分运用在游戏的武器人物音效、游戏动画中，做到了在保证手机性能稳定的前提下，大幅提高游戏音质表现。<br>
<br>
此外，在杜比全景声加持下，游戏内的“声向定位”准确度也得到了极大的提升，尤其是对那些喜欢用扬声器玩游戏的玩家来说，他们可以更容易地透过手机外放来捕捉游戏中敌人的方位信息，相较于传统HRTF需要玩家配戴耳机的要求，杜比全景声无疑极大改善了玩家游戏体验。<br>
<br>
当然，利用新技术进行创新突破的过程中总难免会需要技术攻关，KaChuen也回忆起这项音频技术加入游戏后团队遇到的技术困难，他表示，在光子PUBG Mobile项目团队和技术中心努力下，配合杜比技术工程师的相互协作，这些问题都得到了解决。<br>
<br>
<strong>移动端适配性的打磨</strong><br>
<br>
作为一款“端改手”精品，PUBG Mobile是如何在保证还原端游音效体验的同时，又兼顾到不同机型的性能，最终打磨出灵活适配、表现力极强的游戏音频的？<br>
<br>
对此，KaChuen表示，由于PUBG端游性能消耗过大，所以团队在不同的定位技术、全新的脚步声、敌我区分的新设计等诸多维度，都针对不同性能的手机，乃至外放与耳机两种收声渠道进行了优化，确保在还原端游音频效果的基础上，用更低消耗的声音配置方式满足移动端用户需求。<br>
<br>
甚至于在“大规模多人巷战”这类复杂环境出现时，团队都有根据音效类型及武器的威胁值设定，在Wwise中划分出了不同的优先级设定，优先播放威胁最大的敌方玩家的射击声，同时针对不同性能手机进行发生数限制，突出玩家当前应该听到的声音。<br>
<br>
KaChuen表示，整个针对移动端音频适配性打磨的过程，集合了光子技术中心多个团队的合力，包括光子技术中心的引擎攻坚团队、音频技术团队、音频设计师团队等，可以说是多团队智慧的结晶。<br>
<br>
<strong>立体音频细节设计</strong><br>
<br>
采访中，KaChuen也针对杜比全景声有关“敌友区分”、“立体空间脚步声来源”等细节层面的音频设计提问，进行了详细的解答。<br>
<br>
譬如在“敌友区分”维度，KaChuen表示在PUBG Mobile中，敌方的音效都有特殊HRTF空间定位处理，定位感会更加清晰，便于玩家听声辨认敌方位置，同时在人物Foley及武器相关的音频样本设计之中也会做出不同的设计。<br>
<br>
同样是基于此，当玩家身处立体空间时，团队会借助游戏引擎得出玩家与敌方的高度信息，再结合绑定Wwise RTPC参数等技巧，以及对不同来源的脚步声做特殊的频段处理，助力玩家能够快速判断出敌方玩家的位置信息(前后左右/楼上/楼下) 。此外，团队还使用了Wwise空间音频的阻挡功能，当玩家面前存在障碍物时，障碍物后面的声音会有一定的衰减，方便玩家辨别声源位置信息。<br>
<br>
透过KaChuen的分享，我们不仅可以一览PUBG Mobile在音频设计上的出彩之处，更能从中感知到「光子音频团队」对待游戏音频设计与制作的用心，以及团队十分高深的音频技术造诣。<br>
<br>
而对于「光子音频团队」本身，如果复盘其过去几年中的探索与尝试，就能够捕捉到这个团队对音频前沿技术与高质量产出的不懈坚持与追求。<br>
<br>
<strong><font color="#de5650">以国际化视野，不断开拓游戏音频表达形式</font></strong><br>
<br>
在“精品化”行业浪潮的裹挟下，当下厂商、产品间的角力已经逐渐由「点」上升至「面」，每一款头部精品的背后，都不难发现研发团队对内容、画面、声音各个细分维度不断精益求精的打磨——全球热度居高不下的PUBG Mobile也不外如是，而「光子音频团队」持续为其提供的音频技术支持，正是铸就其高光表现的重要一环。<br>
<br>
<div align="center">
<img aid="1034798" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101221qaod2r4zmvuonj2o.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101221qaod2r4zmvuonj2o.jpg" width="600" id="aimg_1034798" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101221qaod2r4zmvuonj2o.jpg" referrerpolicy="no-referrer">
</div><br>
一方面，「光子音频团队」已经先后与全球多个知名公司，如杜比、环球音乐、华纳音乐、索尼音乐建立了合作。<br>
<br>
其中，最受外界关注的，无疑是其与杜比合作搭建的“杜比全景声混录棚”，成功列入了杜比官方“杜比全景声家庭版后期制作机构”名单——在全国范围内，这一名单里的杜比全景声后期制作机构目前有35家。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1034799" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101221s2cu02jp22p4epct.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101221s2cu02jp22p4epct.jpg" width="600" id="aimg_1034799" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101221s2cu02jp22p4epct.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">光子混录棚：不规则的天花板设计，有利于强化声音扩散效果</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1034800" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101222megni99aqseegsji.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101222megni99aqseegsji.jpg" width="600" id="aimg_1034800" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101222megni99aqseegsji.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">光子混录棚：被抬高后的复合结构地板，可以阻挡外界振动以及低频声音的传播</font></font></div><br>
另一方面，「光子音频团队」也多次携手各音乐细分领域的国际大师。<br>
<br>
譬如其曾与知名电影音乐人Brian Tyler合作打造《和平精英》主题音乐《精英之战》（Battle for Peace）；也曾联手Gordy Habb和Matt Hutchinson两位顶级音乐大师，为玩家们献上了交响组曲《和平之旅》；还与维也纳交响乐团Synchron Stage音乐制作中心合作录制过管弦乐……<br>
<br>
此外，还有Austin Wintory、Neal Acree、Inon Zur、Jeff Broadbent等国际音乐大师也都长期与「光子音频团队」保持着良好的合作关系，「光子音频团队」也在一次次的合作、实践、探索的过程中，不断沉淀着经验。<br>
<br>
<div align="center">
<img aid="1034801" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101222drlvsvoqlbrus9ss.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101222drlvsvoqlbrus9ss.jpg" width="600" id="aimg_1034801" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101222drlvsvoqlbrus9ss.jpg" referrerpolicy="no-referrer">
</div><br>
在GameRes看来，从此前数年与国际大厂、全球知名音乐人的合作，再到本次受邀参与国际知名行业大会GDC并分享音频技术干货，无不彰显着「光子音频团队」的“国际化”理念。<br>
<br>
也正是得益于与全球多边合作，长期立足国际、放眼全球，驱动思路和技术与国际高度接轨的「光子音频团队」，不断提高着自身对“音频技术”的理解，同时也开拓着更拟真、更沉浸的游戏音频表达形式。<br>
<br>
那么「光子音频团队」目前究竟有哪些肉眼可见的实质性技术优势与音频制作技巧呢？<br>
<br>
<strong><font color="#de5650">秉持“专业化理念”，长线探索游戏音频的想象空间</font></strong><br>
<br>
3月25日，一档由光子工作室群全新推出，旨在带领玩家们探访光子工作室群旗下各游戏的研发幕后、各环节工作内容的栏目《追光者-光子游戏研发纪实专栏》，就将镜头聚焦向了「光子音频团队」的幕后工作，揭开了光子旗下游戏音频制作过程的神秘面纱，也让大众领略到了「光子音频团队」的“专业化”理念以及独特的“匠心精神”。我们不难洞察到如今「光子音频团队」的几大核心优势：<br>
<br>
<strong>1、先进的底层硬件支撑：</strong><br>
<br>
团队内部搭建了杜比全景声混音棚、动效拟音棚等前沿音频制作场景，辅以“杜比全景声”等先进音频技术，足以为每一款游戏音频的设计与打造，提供领先行业的强大硬件支持。<br>
<br>
<div align="center">
<img aid="1034802" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101223pz2g5x2vnoqscn4v.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101223pz2g5x2vnoqscn4v.jpg" width="600" id="aimg_1034802" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101223pz2g5x2vnoqscn4v.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>2、高度精细化的拟音环节：</strong><br>
<br>
在光子的游戏中，大到载具引擎的轰鸣声、碰撞声，小到游戏角色在草地、沙地等不同地形的脚步声反馈，甚至于烤火时的通过手搓物体模拟的烧火声、烟雾弹的效果音……悉数由「光子音频团队」在场景及道具丰富多元的“拟音室”进行还原，也正是这一个个取材自现实的音效，带给了玩家们极致拟真的听觉反馈，充分保证了游戏内场景的真实性。<br>
<br>
<div align="center">
<img aid="1034803" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101223uuzyguoxari7o74k.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101223uuzyguoxari7o74k.jpg" width="600" id="aimg_1034803" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101223uuzyguoxari7o74k.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>3、活灵活现的游戏配音：</strong><br>
<br>
时至今日，诸如“快点儿啊，我等得花儿都谢啦！”等出自《欢乐斗地主》的语音包，早已深入大众的心中，成为了中国文化特色鲜明的标签。<br>
<br>
「光子音频团队」的配音老师们，基于对受众的洞察、对玩家审美的把握、对背景文化的理解、对游戏环境的充分想象，在监修过程中认真负责，考究每个声音细节；在自配过程中深入研究，与行业翘楚切磋技艺。通过注入配音技术之外的深刻文化理解与饱满情感，方才成就了一段段广为流传的经典配音。<br>
<br>
<div align="center">
<img aid="1034804" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101224nsp8wewvwhwhdzgs.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101224nsp8wewvwhwhdzgs.jpg" width="600" id="aimg_1034804" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101224nsp8wewvwhwhdzgs.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>4、严谨且具创造力的音频设计与制作：</strong><br>
<br>
在音频设计环节，「光子音频团队」也源源不断地发挥着创造力，在保持严谨逻辑的基础上，通过与国际音乐大师、青年音乐偶像合作，融入吉他、电子琴、管弦乐等丰富乐器，让想象力为游戏赋能，为广大游戏玩家献上了一段段美妙的旋律。<br>
<br>
<div align="center">
<img aid="1034805" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101224p7l7cop0o074qvzq.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101224p7l7cop0o074qvzq.jpg" width="600" id="aimg_1034805" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101224p7l7cop0o074qvzq.jpg" referrerpolicy="no-referrer">
</div><br>
在GameRes看来，《追光者》视频中所展示出的一个个幕后故事，一方面侧写出了「光子音频团队」对硬件先进化、拟音精细化、配音生动性、设计创造力等细节维度，持续苛求的饱满“匠心精神”；另一方面，我们也从中能感知到，正是基于「光子音频团队」长线秉持着的精益求精的“专业化”理念，光子旗下产品才能屡屡突破游戏音频设计与制作的“天花板”，赋予每名玩家超一流的“沉浸式听觉享受”。<br>
<br>
<div align="center">
<img aid="1034806" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101224qs7ffky0jsuck5gu.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101224qs7ffky0jsuck5gu.jpg" width="600" id="aimg_1034806" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101224qs7ffky0jsuck5gu.jpg" referrerpolicy="no-referrer">
</div><br>
在过去几年中，「光子音频团队」一直在与国际接轨的同时，不断在软硬件层面拔高着团队的“专业度”，也借此长效探索着游戏音频的前沿发展方向，持续赋能光子旗下产品，始终走在行业音频设计的前列。<br>
<br>
得益于此，《和平精英》也在2021年荣获游戏音频界最重磅的奖项之一——游戏音频网络协会大奖（G.A.N.G）休闲/社交游戏最佳音频奖，这也意味着「光子音频团队」的实力与成绩已经得到了行业的高度肯定。<br>
<br>
<div align="center">
<img aid="1034807" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101225va83y6byubiofitb.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101225va83y6byubiofitb.jpg" width="600" id="aimg_1034807" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101225va83y6byubiofitb.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">深耕技术、保持匠心，光子持续追求「匠心技术」的最佳表达形式</font></strong><br>
<br>
“声音”对一款游戏来说有多重要？<br>
<br>
在GameRes看来，声音作为一种十分纯粹的感官元素，可以说是每款游戏的不可或缺的重要构成要素之一。当声音与画面等其他感官元素形成共振，不仅可以营造出不同的游戏氛围，还能调动玩家情绪的起伏，甚至成为游戏核心交互的手段之一，是游戏“沉浸感”的重要组成部分。<br>
<br>
正如「光子音频团队」核心成员Bob曾说过的一般：“如果玩游戏不开声音，就像在现实生活里没有耳朵。”<br>
<br>
<div align="center">
<img aid="1034808" zoomfile="https://di.gameres.com/attachment/forum/202203/28/101225hdggd4a0xxww780w.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/101225hdggd4a0xxww780w.jpg" width="600" id="aimg_1034808" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/101225hdggd4a0xxww780w.jpg" referrerpolicy="no-referrer">
</div><br>
也正是出于对“声音”的重视，「光子音频团队」长期保持着“匠心精神”，秉承着“国际化”理念，始终走在深耕音频技术的道路上，GameRes认为这可以概括为其对「匠心技术」表达形式的一种执着与追求。<br>
<br>
「光子音频团队」的高速成长与卓越表现，其实也是光子工作室群旗下诸多优秀技术团队的一个缩影。<br>
<br>
展望未来，随着「匠心技术」逐渐成为光子的一个长线“技术标签”，可以预见的是，未来的光子还将不断突破更多技术壁垒，引领行业游戏研发迈上一个新台阶。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<br>
  
</div>
            