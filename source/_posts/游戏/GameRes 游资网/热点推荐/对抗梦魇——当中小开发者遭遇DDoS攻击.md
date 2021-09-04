
---
title: '对抗梦魇——当中小开发者遭遇DDoS攻击'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202108/25/143227qzfilinlxnlodeoe.png'
author: GameRes 游资网
comments: false
date: Wed, 25 Aug 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202108/25/143227qzfilinlxnlodeoe.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2511663">
<div align="center">
<img id="aimg_1003587" aid="1003587" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143227qzfilinlxnlodeoe.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143227qzfilinlxnlodeoe.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143227qzfilinlxnlodeoe.png" referrerpolicy="no-referrer">
</div><br>
想象一下：你完成了一天的工作，疲惫地回到家门口，只想好好泡个澡，美美地睡一觉，这时你却发现怎么也打不开自家的门锁。你意识到有些不对劲，从疑惑到焦急再到愤怒，你试尽了想到的所有办法，最后还是只能找来开锁师傅。终于，你打开了家门，却发现屋中一片狼藉——家里进贼了。精疲力竭的你还没能厘清遭受了多少损失，又在客厅的墙上发现了一条留言：“如果不想再被撬门堵锁的话，就准备好赎金”。<br>
<br>
现实世界里，这样的“入室行窃”似乎已渐渐远去，但在网络空间，类似的惨剧却愈演愈烈——DDoS攻击和随之而来的敲诈勒索已经成为中小游戏开发者如影随形的梦魇。<br>
<br>
DDoS攻击又名“分散式阻断服务攻击”，方式多种多样，常见的有UDPFLOOD、TCP反射、CC攻击……绝大部分玩家从未听过这些术语，但这些花样所造成的直接后果大家都不陌生，那就是“炸服”。<br>
<br>
说白了，针对游戏公司的DDoS攻击就是通过各种方式，耗尽目标的服务器资源，使得其他正常玩家无法登陆或是不能使用游戏内的一些功能。攻击者的目的大多是为了勒索钱财，胁迫游戏公司们花钱消灾。<br>
<br>
<div align="center">
<img id="aimg_1003581" aid="1003581" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143221avc5rh5nclb7l3sk.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143221avc5rh5nclb7l3sk.png" width="368" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143221avc5rh5nclb7l3sk.png" referrerpolicy="no-referrer">
</div><br>
俗称“呼死你”的电话轰炸也可视为一种DDoS攻击<br>
<br>
这类攻击曾经多针对大型企业，外界新闻也多数聚焦于此，如之前索尼和Capcom被黑客攻击并盗取数据事件。<br>
<br>
但如今越来越多的黑手伸向了中小手游制作者。相对于大公司，小工作室的防范能力更弱，也更依赖于单一产品，毫无疑问属于软柿子。但也正是这些“软柿子”的激烈反抗，开始让DDoS攻击进入普通玩家的视野。<br>
<br>
八月初上线的《弈剑行》在被黑客勒索后，开发团队选择了直接停服下线，拒绝向黑客团队交纳赎金，因此而受到了关注。这场风波让许多人意识到已经有大量小型开发商遭到了DDoS攻击的荼毒；<br>
<br>
<div align="center">
<img id="aimg_1003591" aid="1003591" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143230y5nm1cnm6cdm6l1i.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143230y5nm1cnm6cdm6l1i.png" width="592" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143230y5nm1cnm6cdm6l1i.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2">《弈剑行》《江湖悠悠》《小小五千年》《天黑装备铺》《超级幻影猫2》《影之刃3》</font></div><div align="center"><font size="2">《离玥传》《姬魔链战纪》《四叶草剧场》《弹力果冻》……受害者的名单还远不止此</font></div><br>
只是这种程度的曝光显然不足以让黑客们停手。时间过去还不到两周，十字星工作室的《半盏复古行》同样在开服当天遭到了DDoS攻击。<br>
<br>
这一次，开发者则选择在网络上通过文字来直播这一场没有硝烟的战役。<br>
<br>
<strong>“黑客一把薅上了我们与玩家之间的门”</strong><br>
<br>
《半盏复古行》（下称《半盏》）是十字星工作室花了两年时间制作的剧情向休闲合成游戏，玩家将在其中扮演一名古董修复师，体验古董收集，萌宠养成，剧情闯关等玩法。<br>
<br>
在游戏上线前，开发团队有着许多顾虑，担心玩家能否接受剧情风格、生怕游戏里还留有尚未被发现的Bug……团队成员优化游戏到上线前的一刻，希望能带给玩家一场古董修复之旅，却没料到最先等待修复的，是被黑客们攻击的自家游戏。<br>
<br>
<div align="center">
<img id="aimg_1003592" aid="1003592" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143231r6ohvavcz37muaj2.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143231r6ohvavcz37muaj2.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143231r6ohvavcz37muaj2.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2">开发者们藏在盒子里的宝物并没能如愿顺利地展示给玩家</font></div><br>
上午10点是游戏原定的开服时间，大部分玩家却发现自己并不能进入游戏，随后官方也发出紧急维护的公告，将开服时间推迟两小时。<br>
<br>
此时还有不少玩家以为这是运营借机发放游戏福利的噱头，毕竟“开服炸服发补偿”早已成为手游界的惯例，被视为吸引玩家的方式之一。<br>
<br>
和玩家一样搞不清状况的还有十字星的研发团队，他们正在等待着玩家对游戏的反馈，却只知道服务器始终处于异常状态，直至从发行方得到了确切的消息——“我们被黑客攻击了。”<br>
<br>
足以想见，这则消息所造成的冲击不亚于刚经历了一场分娩的母亲却被告知自己的孩子被人拐走。还来不及有更多的情绪，团队成员们就强打起精神，投身与黑客的这场拉锯战之中，试图夺还自己的作品。<br>
<br>
这一切的发生并非没有征兆。<br>
<br>
在《半盏》的删档测试和预下载阶段，都曾有黑客对服务器发起过小量级多角度的试探攻击，只是当时都应付了过来。几年前，十字星的另一款游戏《螺旋圆舞曲》也曾在上线时遭遇黑客攻击，同样在技术人员的努力下硬扛几个小时挨了过去。<br>
<br>
但这一回，黑客来势汹汹，技术团队才意识到之前的小打小闹原来只是踩点和烟雾弹。<br>
<br>
游戏尚未开服，服务器的外网接口就遭到扫描。黑客首先利用游戏的“游客登录”机制，伪造了大量虚假用户，耗尽了服务器资源。<br>
<br>
《半盏》被迫关闭了“游客”功能。对方又立刻投入了大量可验证的真实手机号，通过“一键登陆”继续攻击，向服务器灌入了堪比正常情况数万倍的瞬时流量，远超中小型游戏公司的防御能力。<br>
<br>
团队勉强应付完这边的流量冲击，正准备防范于未然关闭游戏的充值功能时，黑客又一次捷足先登，通过CC攻击利用付费接口让服务器瘫痪……<br>
<br>
黑客显然是有备而来，技术团队却往往只能等他们攻击之后，才能采取针对性的防范措施，因此始终处于被动挨打的局面。<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1003580" aid="1003580" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143221vlyyh121kk12hty7.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143221vlyyh121kk12hty7.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143221vlyyh121kk12hty7.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">技术团队通宵鏖战，但还是疲于应付层出不穷的攻击</font></div><br>
在游戏上线的前夜，《半盏》的技术团队就这样通宵达旦地抵御着黑客一轮又一轮的进攻，依旧没能让游戏如期开服，服务器的开放一延再延。<br>
<br>
“感觉就像是我们准备了一个世界在等待玩家，然后黑客过来一把把门给薅上了。”《半盏》的开发者说。<br>
<br>
<strong>就让光来照亮阴影</strong><br>
<br>
时间一分一秒地流逝。<br>
<br>
对于《半盏》这类体量不大的休闲游戏而言，开服首日是至关重要的一天，这一天往往就是获得平台推荐和玩家关注的最好机会。<br>
<br>
来自等待开服的玩家的压力越来越大，与黑客之间的拉扯却看不见尽头。十字星的团队曾经不太理解《弈剑行》的开发者为什么会宁愿放弃倾注心血的游戏也要“玉石俱焚”，但此时的他们对于“自己作品被蹂躏而产生的愤怒与绝望”早已感同身受。<br>
<br>
“想要做些什么”的心情最终让他们决定将这场黑暗中的角力摆到灯光下，告知了玩家和同行们自己的游戏正受到黑客攻击，并且每两小时更新一次进展。<br>
<br>
<div align="center">
<img id="aimg_1003593" aid="1003593" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143232gabe54vzasa3kby3.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143232gabe54vzasa3kby3.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143232gabe54vzasa3kby3.png" referrerpolicy="no-referrer">
</div><br>
这样的做法本质上属于“自揭其短”，很多时候只会让玩家怀疑游戏开发者的技术水平，进一步对于游戏的投入和消费都有所顾虑，对已经产生的损失则于事无补，因此大部分游戏公司并不倾向这么做。但当时《半盏》的团队已经对游戏的前景相当悲观，在他们看来，这很可能就是与玩家最后的交流机会了，思虑再三还是决定坦诚相待，将选择权交给玩家。<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1003582" aid="1003582" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143222c0xmrzi3mmc23l3x.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143222c0xmrzi3mmc23l3x.png" width="564" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143222c0xmrzi3mmc23l3x.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">毕竟玩家也并没有义务去了解开发商的苦衷</font></div><br>
幸运的是，或许正因为过去《弈剑行》等开发者同样选择了开诚布公，得以让普通玩家们也对DDoS攻击有所认识。在《半盏》公开自己的遭遇后，还是收到了许多来自玩家的支持与鼓励，支撑起了原本已到临界状态的开发团队。<br>
<br>
只可惜实际情况并没能马上随之乐观起来。<br>
<br>
《半盏》的举动似乎反而激怒了黑客团伙，此时的他们已经先后发动了8轮攻击，动用了超过十万个真实的身份信息和被他们挟持的网络设备（俗称“肉鸡”），绕过WAF防火墙直接攻击服务器。<br>
<br>
如果说之前的攻击模式还只是拉帮结伙地到人店里干坐着不消费，那现在就堪比直接扔石块砸场子了。<br>
<br>
即便在腾讯云安全技术团队加入支援之后，黑客团队依然持续通过不同方式进行攻击。有好几次，在技术团队以为抵御住了攻势想要喘一口气的时候，黑客再度突袭使服务器崩溃。黑客团伙在这一过程中甚至未曾现身进行勒索和谈判，只是孜孜不倦地发动着攻击，仿佛只为了拖垮这家公司，给业界立一个“下马威”。<br>
<br>
《半盏》的技术团队面对的困境还不止于此。为了测试防御效果，团队最终在晚上九点半开放了服务器，让玩家们登陆游戏。这也就意味着接下来团队不仅要面对黑客的流量攻击，还要像淘金一半从中清洗出那些正常玩家的数据，尽可能保护这些用户避免回档删档等状况。这几乎依赖于人工判断和处理，也成为了技术团队最难熬的一段时光。<br>
<br>
这也就是为什么许多游戏遭遇DDoS攻击时宁可始终闭门不开。<br>
<br>
经历了又一个漫长的夜晚，《半盏》的团队终于暂时填补完了现有的漏洞，整体攻防趋于平衡，大部分玩家们可以正常地进入游戏。<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1003590" aid="1003590" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143230j4kkqyhh9nqgnz9q.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143230j4kkqyhh9nqgnz9q.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143230j4kkqyhh9nqgnz9q.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">在游戏进入正常运营后，黑客们也依旧没有消停</font></div><br>
终于腾出手来的工作室也已通过TapTap的渠道统一报案，正对被攻击材料进行保存和公证，将进一步向广州市天河区派出所、网警、经侦等相关部门报案。<br>
<br>
然而扫尾工作这才刚刚开始——密集的攻防战给游戏带来了大量有待修复的Bug，网络动荡造成的回档、充值等问题还有待处理，允诺玩家的延迟开服补偿也要以大家都能接受的方式进行发放……这些都会直接影响游戏的收入和后续运营，这场无妄之灾给游戏带来的影响还远没有结束。<br>
<br>
《半盏》的经历只是一个缩影，曾经以及将要遭遇类似情况的中小工作室还有许多。<br>
<br>
<strong>游戏开发者的“阿喀琉斯之踵”</strong><br>
<br>
古希腊神话中的英雄阿喀琉斯曾浸于冥河因而刀枪不入，唯独后脚踝没能泡入河中，最终被一支毒箭射中失去了性命。<br>
<br>
对于中小游戏工作室而言，DDoS攻击就是那支瞄准死穴的毒箭。<br>
<br>
DDoS攻击几乎伴随互联网而生，只要提供在线服务，就可能成为DDoS攻击的受害者。早期的DDoS攻击大多是个人黑客出于炫耀、报复等目的而实施，现如今则早已发展为犯罪团伙敲诈勒索互联网企业的手段，首当其冲的就是游戏行业。<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1003586" aid="1003586" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143226bc7deudd55zel2dl.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143226bc7deudd55zel2dl.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143226bc7deudd55zel2dl.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">根据“腾讯安全”发布的《2020年DDoS威胁报告》，针对游戏行业进行的DDoS攻击占了近八成</font></div><br>
早在端游时代，网游厂商就成为了黑客们利用DDoS攻击进行敲诈勒索的对象；在手游时代来临后，棋牌类游戏则又成了重灾区。这些厂商大多财大气粗，往往懒得与黑客团队纠缠，直接花钱了事，也不愿意对外公开。因此在很长时间里，普通玩家并不太了解DDoS攻击所造成的危害。<br>
<br>
或许是越来越难从大公司身上榨到油水，又或者是DDoS攻击成本的进一步降低让黑客们意识到“蚊子腿也是肉”，总之，近年来黑客群体愈发盯上了中小体量的手游工作室，专挑走小众精品路线的作品下手，趁着游戏开服的当口发动攻击，甚至还摸索出了一条筛选的捷径——那就是TapTap上的“编辑推荐”。<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1003584" aid="1003584" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143225xqrt577qdtqzqj2e.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143225xqrt577qdtqzqj2e.png" width="595" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143225xqrt577qdtqzqj2e.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">《半盏》同样是在获得“编辑推荐”后不久就遇到了黑客展开的攻击</font></div><br>
由于TapTap推荐的产品多为中小团队所开发，这类团队大多缺乏网络安全的攻防经验，过于依赖云服务器供应商所提供的网络安全服务，一门心思扑在自家产品的研发上，恰恰留给黑客团队可乘之机。<br>
<br>
云服务商所提供的基础防护大多相当脆弱，一旦客户的峰值流量超出预设带宽，就会把指向客户接口的流量全部丢包，俗称“扔进黑洞”，直到一定冷却时间后再释放出来。黑客就利用这一机制，循环往复地把游戏开发者的接口打入黑洞。<br>
<br>
要是开发者不幸把关键模块架设在了云服务器上，那这时候就很难采取什么技术上的防范手段了，要么加钱升级为“高级防护服务”，要么向黑客妥协缴纳赎金，相当于同时被云服务商和黑客双重绑架。熟知行情的黑客们则会趁机开出一个较低于“高防服务”价格的金额，胁迫开发者就范。<br>
<br>
“不甘心”是遭遇DDoS攻击的技术人员们事后最常流露的情绪。<br>
<br>
黑客在技术上并没有什么显著的优势，但他们经验老道、以逸待劳，深知中小开发者的软肋和应对惯性，因此总能卡着节奏占据先手。在复盘过程中，大家往往能意识到一些并不复杂的事先防范技巧：“要是没暴露关键端口就好了”“如果应用部署走的是内网机制就好了”“要是再来一遍的话，肯定不会让黑客得手”……<br>
<br>
但不是所有人都还有第二次机会。<br>
<br>
对于许多小团队而言，两万元的赎金和五万元的高防并没有太大差异，都意味着好不容易熬到了游戏上线，却还要再出一笔血。更重要的是，在游戏上线的第一天遭遇DDoS攻击导致“炸服”，通常会造成不可逆的用户流失（并浪费可能是唯一一次的平台推荐位），足以就此决定一款游戏的生死，即便把游戏赎了回来，也可能早已变成被撕票的“尸体”。<br>
<br>
也正是因此，一些中小开发者的反抗反而比大型公司激烈得多，抱着“大不了关门”的心态和黑客杠到底，让对方讨不着半点便宜。<br>
<br>
要是每家公司都这样“宁为玉碎，不为瓦全”，会不会让黑客们放弃这块硬骨头？没有人知道答案，但即便能成功，这样的代价也未免太过高昂。毕竟没有谁真的心甘情愿让自己的作品成为祭品。<br>
<br>
<strong>浮上水面的冰山一角</strong><br>
<br>
饱受黑客困扰的也不止是国内的游戏企业。早些年，日本手游“开服即炸服”的传统还常常沦为笑柄，如今回头来看，许多小团队其实同样是深受DDoS攻击困扰，有苦难言。也是国内的手游产业日趋发达，才让大家更加深入地认识到这一现象。<br>
<br>
<div align="center">
<img id="aimg_1003585" aid="1003585" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143225yf0gvagp23y20ny3.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143225yf0gvagp23y20ny3.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143225yf0gvagp23y20ny3.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2">日本开发者同样深受DDoS攻击的困扰，而且和大部分国内企业一样，</font></div><div align="center"><font size="2">大公司通常并不愿意承认自己遭到了难以应付的网络攻击，小团队则在默默挣扎中悄无声息地逝去</font></div><br>
DDoS攻击长久以来都是世界性的网络安全难题，这类攻击的发起位置来源遍布全球各地，难以定位作案者真正的所在地。<br>
<br>
侦破这类案件的难点还不只是“境外作案”。<br>
<br>
几年前国内破获的“暗夜小组”就是一个藏身于柬埔寨实施 DDoS 攻击来敲诈国内互联网企业的组织，最终在深圳公安机关的不懈努力下全部落网，对11人以“破坏计算机信息系统罪” 判处有期徒刑一至二年不等。<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1003583" aid="1003583" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143223pgvvl0ggicpikga6.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143223pgvvl0ggicpikga6.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143223pgvvl0ggicpikga6.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">“暗夜小组”在2017年对腾讯云服务器进行“DDoS”攻击，给后者造成经济损失人民币114358元</font></div><br>
这个组织在当时还保留着以往黑客团体不仅求“利”还要图“名”的传统，社团架构严密，实施从上游到下游一手包办的“一条龙”犯罪，作案人员线上身份和线下身份一一对应，这也让办案人员得以建立起完整的证据链，最终将他们定罪。<br>
<br>
但是“高度分工、流水线作业”正在成为这类犯罪的新趋势。<br>
<br>
在这个黑色产业中，一些人专职植入木马，收集“肉鸡”，再将这些受控制的终端批量兜售给其他组织，这些人也被称为“肉鸡商人”；收购 “肉鸡”的则往往是DDoS攻击的直接发起者，他们在整个产业链中扮演着“打手”，也是行踪最为隐蔽的角色；还有一些人手中握有大量的个人信息，借此搭建起用于“洗钱”的支付网络，接触受害者进行敲诈勒索，有如项目的“承包商”；此外还有大量的掮客周旋于这些人之间，参与中介和担保等活动，使得整个交易链条更加隐蔽，也让犯罪门槛变得越来越低。<br>
<br>
<div align="center">
<img id="aimg_1003579" aid="1003579" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143220ckcbmm6jjoswxm0x.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143220ckcbmm6jjoswxm0x.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143220ckcbmm6jjoswxm0x.png" referrerpolicy="no-referrer">
</div><br>
一位技术人员带着几分自嘲地表示：“黑客之间的分工合作和资源共享可能比我们这些正规程序员还要紧密。”<br>
<br>
<div align="center">
<img id="aimg_1003578" aid="1003578" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143219t6lllycpnhyofpfb.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143219t6lllycpnhyofpfb.png" width="573" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143219t6lllycpnhyofpfb.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2">不久前广州市中级人民法院就通报了一起17岁少年仅靠购买的DDoS攻击套餐，</font></div><div align="center"><font size="2">就使得国内航空公司票务系统瘫痪的案件</font></div><br>
相关产业的伪装性也远超大众的想象，一边是大家连黑客的尾巴都难以抓到，另一边则是作案工具就藏在大伙的眼皮底下——在一些线上交易平台，所谓的“DDoS抗压测试”“网络攻防教学”实际上就可能被利用为网络袭击的工具，甚至卖家就是披着皮的“肉鸡商”。<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1003589" aid="1003589" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143229u5a55ag61gabx4aw.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143229u5a55ag61gabx4aw.png" width="575" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143229u5a55ag61gabx4aw.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">但由于缺乏直接证据，最多也只能让这些卖家下架商品或是封禁账号</font></div><br>
黑客们的身份同样扑朔迷离。近期勒索中小游戏公司的黑客有不少自称来自名为ACCN的组织，但目前并没有任何证据表明这些人出自同一组织，作案手法也不尽相同，更没法确认他们是来自中国台湾地区的黑客。但从勒索者的角度而言，他们乐于默契地公用同一个幌子，让大众形成刻板印象，相信他们是某个地区的固定组织，以此来更好地隐藏自己的身份。<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1003588" aid="1003588" zoomfile="https://di.gameres.com/attachment/forum/202108/25/143228y6yqulvw3z5fa9af.png" data-original="https://di.gameres.com/attachment/forum/202108/25/143228y6yqulvw3z5fa9af.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/25/143228y6yqulvw3z5fa9af.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">在中国台湾地区的相关报道中，</font></div><div align="center"><font size="2">ACCN则是一个台湾犯罪分子与内地黑客勾结敲诈当地企业的组织</font></div><br>
事到如今大家也不难察觉，这样盘根错节的产业链实则早已超出了单纯的“黑客”范畴，牵扯到了信息安全的方方面面。<br>
<br>
由于移动智能设备的快速普及，使得世界范围内被绑架的“肉鸡”数量都远超以往，用户不经意间下载安装的“破解”“刷单”软件都足以盗取机主的信息，或是让一台手机成为黑客团体的作案工具。在2013年的产业报告里，峰值流量300G的DDoS攻击就已经是不容小觑的行业事件，现如今攻击流量的单位则早已突破TB。<br>
<br>
信息安全与我们每一个人都息息相关，中小游戏企业遭遇的DDoS勒索也只是显露的冰山一角，自然难以独立得到解决。<br>
<br>
<strong>结语</strong><br>
<br>
短时间内大环境难以改变，中小开发者能采取的方法也只有联合起来“自救”。<br>
<br>
如果能有更多的技术交流，那么就不必有更多的技术人员体会相同的“不甘”；如果能大家一起合购“高防”按需使用，那么就不必再为开服的第一天担惊受怕；如果能有联合举证共同诉讼，那么获取公道的可能性也会有所提升；如果能……<br>
<br>
能做的事确实还有许多，但对于大部分的中小工作室而言，光是依靠自己的作品生活下去就已经竭尽全力，并没有余力去落实这些事。<br>
<br>
可偏偏就是这些小开发者，成功让这么多年来藏于暗处的黑客暴露在了大众面前，让玩家们认识到了这是怎样的一群人，又在做着怎样的恶行。当那些遭遇黑客攻击的工作室向玩家介绍情况时，他们总是在一遍又一遍地道歉，想尽补偿方法来挽留玩家，但本该道歉的并不是他们。<br>
<br>
中小开发者与黑客之间的对抗还远看不到终点，但他们决不妥协的勇气多少点燃了些许光芒，至少今后的开发者们碰上类似的状况可以堂堂正正地说一句“我们被黑客攻击了”，无需再为自己身为受害者而感到羞愧。<br>
<br>
毕竟驱散阴霾的第一步，就是让它暴露于阳光下。<br>
<br>
<font size="2"></font><br>
<font size="2">来源：游戏研究社</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/1ZqnqCiy5VhxsM1hTpBPcw</font><br>
<br>
<br>
</td></tr></tbody></table>



  
</div>
            