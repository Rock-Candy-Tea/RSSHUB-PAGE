
---
title: '跟《动物餐厅》小游戏学习App游戏化设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/Z3Y4r6qvrtb4uIKX6ElV.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 18 May 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/Z3Y4r6qvrtb4uIKX6ElV.jpg'
---

<div>   
<blockquote><p>编辑导读：很多产品为了让用户停留更久，会对界面做出一些游戏化的设计，让用户在一个个小游戏中忘却时间。而本文作者从一个爆款小游戏《动物餐厅》中获得灵感，谈谈如何学习它的游戏化设计，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4574639 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/Z3Y4r6qvrtb4uIKX6ElV.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>最近笔者和她的朋友们都疯狂地迷上了<动物餐厅>这款小游戏，被这个游戏的新奇玩法、NPC背后耐人寻味的故事、可爱的画风设计等等所吸引，每天反复多次地登上去玩，甚至有时候为了得到小鱼干无所不用其极。因此，笔者对这款小游戏进行了剖析，找寻它让用户为之着迷的魔力。</p>
<h2 id="toc-1">01 产品概况</h2>
<ul>
<li>上线后DAU超过500万</li>
<li>高次日留存：次日留存超50%</li>
<li>活跃时长高</li>
<li>打开频次高：用户每天平均登录10次</li>
</ul>
<p>以上。</p>
<p>自从这款小游戏在2019年4月多渠道上线后，其数据表现是很漂亮的。它在4个月不到的时间里DAU就超过了500万，同时次日留存最高可达50%以上。由于其多样化的玩法和多场景的经营方式，用户每次登录游戏后，其停留时间长，且每天都会多次登录游戏，以完成各种各样的任务。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/9PiXdavAcKWrRy5D7YFD.png" alt width="408" height="190" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">[截止至2021.05.15，其版本评分还是挺高的]</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/8lIcdeDfhxLwVjz6SKgg.png" alt width="139" height="29" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">02 产品分析</h2>
<h3>1. 基础层</h3>
<p>【产品定位】：</p>
<p>很治愈的养成类经营小游戏，可佛可肝，广告和增值服务是其变现手段</p>
<p>【目标核心用户】：</p>
<p>20-40岁的女性用户群体</p>
<p>【底层玩法】：</p>
<p>用户只需通过不断点击招募按钮或者看一小段广告来招募客人，然后客人点餐并支付用户小鱼干。玩家通过使用小鱼干，可以解锁一些餐厅设施、菜谱、员工和提升星评。此外，通过提升星评又能进一步解锁设施、菜谱，或者其他场景、其他货币体系和人物故事等。</p>
<p style="text-align: center;"><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/ojkxw3AsBRqhnvejxKtU.png" alt width="481" height="243" referrerpolicy="no-referrer">[用户评论词云]</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/8lIcdeDfhxLwVjz6SKgg.png" alt width="139" height="29" referrerpolicy="no-referrer"></p>
<p>分析了从2019年至今的用户评论，其关键词主要是“可爱”、“广告”、“小鱼干”等，也体现了动物餐厅的确是一个画风可爱又治愈的小游戏，用户对其广告和小鱼干都异常渴求。用户对于小鱼干的渴求是因为小鱼干是主要货币，越玩到后面，所需要的小鱼干就越多；而用户对于广告的渴求是源于广告的本质也是一种货币。用户通过观看广告，可以获得额外的机会或者快速地招揽客人，以获得更多的小鱼干和提升星评，有时候甚至能得到稀有物品。</p>
<p>访谈了几位深度用户，大家都表示对广告又爱又恨：广告虽烦，却恨不得平台每天能多供应几个，有位玩家甚至夸张地表示：“这辈子的广告都在动物餐厅看完了”。</p>
<h3>2. 框架&设计层</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/sy31FPKDBtzz1V9FRxic.png" alt width="1998" height="892" referrerpolicy="no-referrer"></p>
<p>从框架层来说，导航区和按钮区固定于顶部与底部，两个区域的展示元素会因经营场景的改变而有所变化；每个场景都会有一部分可移动的元素和一部分不可移动的元素，但每个场景可移动的元素占比又有所不同。此外，这个游戏的产出（如货币、星评、花朵等）都是先随意地洒落在地上，需要用户亲自去拾取，这就使得整个页面都是可操作的，给予了用户最大化的自由。</p>
<p>从设计层来说，可以用四个词语来形容这个小游戏的设计风格：「画风清新」、「色调治愈」、「BGM轻松」、「弹幕可爱」。每个场景的设施都别具风格，而且根据不同季节、不同节日，页面背景和页面元素都会有所调整，如春季的花园是满眼的绿，下着淅淅沥沥的小雨，冬季的鱼塘和前院则是白雪皑皑；让用户在游戏里也能真切地感受到四季变迁、节日氛围，温暖而治愈。</p>
<h3>3. 业务层</h3>
<p>在这一层，将会从用户的体验路径出发，以明确经营策略，笔者将其拆解成三大版块：经营场景、按钮设定、基础货币。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/f6KcnP5kb40Zklkmmriw.png" alt width="405" height="351" referrerpolicy="no-referrer"></p>
<p><strong>1）经营场景</strong></p>
<p>整个游戏由「6大场景」、「7大页面」组成，其中餐厅和厨房场景是初始化场景，没有解锁的条件；而其他的场景都是需要用户先把前面的初始化场景经营好，拿到特定的星评数量后才能逐步解锁的进阶场景。六大场景的剖析如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/HnsYj38H7ttC7qKdDqFC.png" alt width="1710" height="1006" referrerpolicy="no-referrer"></p>
<p>餐厅、厨房场景是这款游戏的核心，通过宣传招募而来的顾客、不请自来的特殊顾客都会在这个场景展现，有时候还会分享他们的故事。有趣的是，还会有一些是季节限定客人，只有在特定季节，在花园的许愿池里获得季节限定花朵，才能解锁这些客人。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/l4NR2g56T7WQykdkPSTU.png" alt width="1993" height="585" referrerpolicy="no-referrer"></p>
<p>[可可爱爱的春季限定客人]：</p>
<p>在前院，这是整个游戏设计里用户自由度最高的一个场景：用户可以随意放置所有设施的位置，这就使得用户的前院场景实现了“千人千面”。当用户去好友家拜访时，往往会因好友的设计有感而发，从而把自身的庭院建设得更加美丽。在这个场景，大大地提升了用户的自我成就感和社区融合感。</p>
<p>此外，除了一些常规操作，还隐藏了一个小彩蛋——种植体系。若好友有种植植物，还可以帮好友浇水；当然，若用户自己在前院解锁了植物的相关设施，也可以每天给自己浇水。植物有三个生长阶段：幼苗期—生长期—成熟期，当植物成长到成熟期时，就会获得和植物有关的一些彩蛋礼品。整个种植体系进一步丰富了前院的游戏化场景。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/svbUwnYJdgFhDydaFazp.png" alt width="618" height="360" referrerpolicy="no-referrer"></p>
<p>[植物生长的三个阶段]：</p>
<p>而在自助场景，也有一个小彩蛋——召唤特殊客人。通过玩扭蛋机，可以搜集各种各样的玩偶，当收集玩偶到特定数量时，则可以解锁特殊客人。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/IWd93Uam1UOosuO9yqld.png" alt width="597" height="294" referrerpolicy="no-referrer"><br>
[当成功召唤特殊的隐藏客人，其背后也藏有剧情待用户去摸索]：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/qb4MDzzLT4KujyYZZdyL.png" alt width="720" height="425" referrerpolicy="no-referrer"></p>
<p>在花园场景，除了可以种植花朵，把花朵放在花瓶里以获得更多奖励或者解锁客人；还可以在许愿池里许愿以获得稀有物品。另外，通过把花园里的物品放进信使海德薇的信件里，就可以让信使带回来不同的明信片或者信件，可以解锁特定设施、菜谱，也可以对现有菜谱进行涨价，甚至还能推动这个小游戏中故事情节的发展。</p>
<p>鱼塘场景的操作相对于花园场景玩法更简洁些，只是通过不同的海鲜解锁不同的摊主。但是，花园场景和鱼塘场景也有相似之处：可以随意摆放场景产出的位置。在花园，用户可以让成熟的花朵随意摆放，也可以把花朵摞起来摆成各种各样的形状或者字母；而在鱼塘，用户也有着一样的操作权限。页面堆积成山的物品，会让前来拜访的好友觉得这个用户超级富有，不禁感叹“富贵人家”，因此，在这两个场景，也大大地激发了用户的创作兴趣。</p>
<p>在外卖场景的外卖食品，都是使用通过在花园和鱼塘里获得的物品进行兑换的，这就把三大场景紧紧联系在一起了。外卖场景作为最后才开放的场景，其实是一个彩蛋场景，充满了稀奇古怪的创意。</p>
<p>第一，做外卖不仅仅是会得到客人的好评，有时候还会有差评，但是可以通过再送一单外卖进行补救，完全贴近现实经营餐厅的场景。</p>
<p>第二，解锁了打包台设施后，点击打包台的灯，还可以让页面变暗，当不小心点到台灯时，页面变暗的一瞬间充满了意外。</p>
<p>第三，解锁了“招牌商店”设施后，则可以进一步解锁壁纸、特殊设施、纪念物。壁纸可以使得餐厅背景更加多样化，也会让很多还未能解锁外卖场景的好友羡慕嫉妒恨；而纪念物则是餐厅员工的一些独特饰品。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/7yejX59pLxpNyvDzgcb9.png" alt width="639" height="401" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/Zom4whClwYSgeaBHkCTP.png" alt width="1037" height="508" referrerpolicy="no-referrer"></p>
<p>[招牌商店的一些设施，通过消耗铃铛获得]：</p>
<p>值得一提的是，在特殊设施中，可以购买鱼塘场景和花园场景的收纳柜。可能很多人会觉得疑惑：既然已经让用户可以随意放置花园和鱼塘场景的物品，为什么还要在外卖场景的招牌商店里让用户可以买收纳柜呢？其实，收纳柜完全就是强迫症用户的福音：不希望花朵/海鲜堆满了页面，反而希望页面能够干净整洁。因此，这样的设计才是真正给予了用户最大的选择权：既可以自行DIY物品的摆放位置，也可以把东西都分门别类地放置在收纳柜。</p>
<p><strong>2）按钮设定</strong></p>
<p>从按钮的设定来说，其实是分成了前院和其他场景。</p>
<p>在前院场景，按钮的设定是和其他场景的有所不同：前院除了可以解锁设施，还可以通过<集合>按钮顾客，获取更多的奖励；也可以给顾客们拍集体照，然后分享给好友，以炫耀自己已经解锁的一些新客人，可谓“一钮两用”。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/kNf9zJQkcfZwucsihWkc.png" alt width="380" height="280" referrerpolicy="no-referrer"></p>
<p>[使用<集合>按钮后，顾客留下的奖励]：</p>
<p>而在其他场景，底部按钮的操作都是一致的，其剖析基本如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/vihr7Cbxj2tViU4YaYeK.png" alt width="1989" height="1137" referrerpolicy="no-referrer"></p>
<p><strong>3）基础货币</strong></p>
<p>在这个游戏中，基础货币有四种：小鱼干、盘子、胶卷和铃铛，四种货币的解剖如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/pW4IYtue4cRiXcQDcj27.png" alt width="515" height="226" referrerpolicy="no-referrer"></p>
<p>几大货币体系之间看似相互独立，实则环环相扣。比如说，当星评达到了一定量级，便可以使用小鱼干代替盘子兑换扭蛋的次数；外卖场景的菜谱涨价消耗的是小鱼干；在前院有部分设施是需要小鱼干才能解锁的，而解锁后的设施又会提升前院的收益，以获得更多的小鱼干/胶卷。同理，在前院获得胶卷还能提升喇叭的宣传属性，以招呼到更多客人，提升餐厅小鱼干收益。</p>
<p>此外，在外卖场景使用铃铛解锁的设施也能帮助提升整个餐厅的属性等等。当然，这些货币之间的玩法都需要用户慢慢摸索的，游戏界面也不是在用户一上来就把四种货币全部介绍完，通过逐步解锁场景，逐步开放货币体系，搭建了一个有趣而又暗藏玄机的用户成长体系。</p>
<p>若是一上来就让用户可以使用多种货币，用户必定觉得眼花缭乱、主次不分，甚至会忽略掉看似毫不起眼的外卖场景。然而，随着用户自行摸索，慢慢升级，就会发现外卖场景这个充满意外设计和特殊惊喜的“大彩蛋”，自然也会对这个游戏沉迷上瘾了。</p>
<p>除了这四种基础货币，游戏在后面还衍生了一种氪金货币，钻石——即可以通过充值购买钻石，以换取基础货币。当然，为了满足不想氪金，但是又想有机会获得钻石的用户，游戏支持用户每天可以免费领取10个钻石，以及可以通过观看额外的广告获取钻石，完全符合“可佛可肝”的游戏定位。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/hd6dClnyKSnjKhD9RY9n.png" alt width="621" height="313" referrerpolicy="no-referrer"></p>
<p>[120和360档次的钻石还是很容易就能攒到的]</p>
<h2 id="toc-3">03 营销逻辑</h2>
<p>经过上面的剖析，不难看出，《动物餐厅》致力于打造成精品化小游戏，在游戏设计理念上充分运用了PBL理论和八角行为分析法，实现了玩家对游戏“上瘾且牵挂”。</p>
<h3>1. PBL理论</h3>
<p>PBL理论源于宾夕法尼亚大学副教授凯文·韦巴赫和丹·亨特教授编著的《游戏化思维》，指的是points（点数）、badges（徽章）、leaderboards（排行榜）。PBL理论已经普遍应用于游戏化设计，以提升用户活跃和用户留存。</p>
<p>回归动物餐厅小游戏，点数对应的是用户获得的星评，是一种对外显示用户目前成就的方式：当点数（星评）越高，用户可解锁的设施和顾客就越多，享受的特权也越多；徽章对应的是收集机制，是一种可视化的成就，用以表明用户在游戏化过程中的阶段性收获：游戏中属于收集机制的有招待客人名录、纪念物列表、花园信件列表，用户可以看到自己解锁的客人、纪念物和信件，以及还能知道还有哪些尚未解锁，这种机制既能让用户获得成就感，也为用户提供了一定的指示，让其清楚应努力的目标和方向，从而提升用户游戏积极性；而排行榜功能也在这款游戏里表现得淋漓尽致：除了好友排行榜，还有游戏所在区服的排行榜、用户所在省份的排行榜，甚至还能把游戏分享到微信群以查看群排行榜，排行榜让用户知道自己相对于其他用户的水平如何，激发了用户的攀比心理和活跃度，从而提升了游戏的用户留存和用户黏性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/HNrfSs0HB73VIU9pTeNG.png" alt width="564" height="358" referrerpolicy="no-referrer"></p>
<p>[通过点击未获得的纪念品icon，可查看相关描述和提示]</p>
<h3>2. 八角行为分析法</h3>
<p>八角行为分析法是游戏化大师周郁凯（Yu-kai Chou）提出的，经过对人性的深度剖析，他认为能够让用户自愿沉迷于游戏主要依赖八大核心驱动力：成就感「Accomplishment」、使命感「Meaning」、创造力「Empowerment」、稀缺性「Scarcity」、逃避心「Avoidance」、未知性「Unpredictability」、拥有感「Ownership 」和社交影响「Social Influence」。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/FEuWiTZxOiyj8u95zcdb.png" alt width="445" height="427" referrerpolicy="no-referrer"></p>
<p>接下来，我们从八大核心驱动力切入，剖析这个游戏对于各个驱动力的应用案例：</p>
<p><strong>1）成就感</strong></p>
<p>成就感是在游戏中被应用得最广泛的驱动力之一：通过设定成长性的任务或者排行榜等，用户在指引下克服困难、完成任务、获得奖励，从而在游戏中不断成长，获得成就感。动物餐厅传达给用户的目标，表面上看起来是不断积攒货币、解锁设施、提升星级；但是其实这个游戏是高度开放性的，并没有给用户传达很清晰明确的目的，而是让用户自行摸索、自行创造，去打造一个属于自己的“理想餐厅”。</p>
<p><strong>2）使命感</strong></p>
<p>使命感强调了在游戏中用户对于自身重要性的感知，意识到自身的每一个行动都是有意义的。在动物餐厅中，使命感让用户形成了“以建设餐厅为己任”、“我是餐厅的主人，我要努力经营好它”的责任心。如限定时间内的离线收益（餐厅累积收入）、限定金额的离线收益（小费台）、顾客不定时的回归订单、成熟周期不一致的花朵等玩法设计组合成的牵挂机制，都会让这些充满使命感的用户心心念念，并在一天中反复登录游戏，大大提升了用户活跃及在线时长。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/qVvD1r3cGxNisMEcorFb.png" alt width="1835" height="650" referrerpolicy="no-referrer"></p>
<p><strong>3）创造力</strong></p>
<p>这个驱动力在动物餐厅体现得淋漓尽致：只提供一些基本的设施，页面整体去UI化，给予用户最大化的自由发挥想象力和创造力。</p>
<p><strong>4）稀缺性</strong></p>
<p>在这个游戏中，有很多东西是无法马上获得的；又或者能获得的概率很小。比如有些设施只能在特定的时间可以购买；又如每个季节都有几位限定客人，必须要通过季节限定的花朵才能召唤到，而这些花朵只能在特定的时间通过在许愿池许愿获得；此外，在池塘场景，有些海产也只在特定时间才会有且能钓到的难度也会增加。这种对于稀缺物品的渴望，使得用户更加沉迷于游戏，甚至会很积极地收集攻略和在社区交流信息。</p>
<p><strong>5）逃避心</strong></p>
<p>最典型的是外卖场景，用户派送外卖很有可能会获得差评，而且补救差评是有时效的，过了指定时间后，用户就无法挽回这个差评了。为了逃避这个损失，用户不得不反复登录游戏，确保自己的外卖遭到差评时得以及时补救。</p>
<p><strong>6）未知性</strong></p>
<p>这个游戏充满了奇遇和未知。首先，每次信使带回来的物品/信件是未知的，用户既可以通过自行探索找到规律，也可以通过收集攻略提高获得自己想要的物品的概率。其次，餐厅各类型的NPC、神秘客人等会不定时出现或者满足条件后触发，带来意外和惊喜，如奇奇怪怪的NPC有借钱的小兔子、会撒钱的富二代熊猫、会放屁赶走客人的獾、帮你宣传的小电视、会通过唱歌帮忙招客的鹦鹉歌手等；神秘客人则是带有身份或者故事背景的，他们往往会和用户有对话，并且对话都是富有哲理或者是反射社会现状的（汶川地震、全球气候变暖、虐待动物等），有趣的游戏富有教育意义。</p>
<p>次之，用户不经意的行为会触发新场景，或者收获意外的礼物：比如招待某个客人达一定次数，就会留下一个特殊的纪念品；又比如餐厅会随机出现一些小礼品或者可以让员工佩戴的饰品。</p>
<p><strong>7）拥有感</strong></p>
<p>其实拥有感也是让用户获得成就感的一种方式，当用户获得了稀缺物品，或者拥有的东西比别人多，成就感往往就很容易诞生。在动物餐厅中，通过可视化的收集列表、可以拜访的好友的家，展示用户拥有的一切物品和设施，用户的拥有感感知会更加强烈，也会为了追求一些物品的拥有感而在这个游戏中付出更多心思和时间。</p>
<p><strong>8）社交影响</strong></p>
<p>社交影响，是指游戏中驱使我们去进行社交的一些玩法设计。从针对「游戏好友」的社交驱动来说，用户为了获得更多的货币和邀请卡，必须添加游戏好友并且坚持每天访问好友的家，才有机会在好友的家获取到这些物品。除此之外，如果用户有在前院种树，想要树木生长速度加快，就必须邀请好友帮忙浇水。从针对「现实微信好友」的社交驱动来说，当用户看广告的数量已达上限，还想继续获得机会的话，可以通过分享给微信好友/微信群获得机会。支持通过分享获得机会的场景有花园的许愿池、餐厅宣传、前院集合等，对用户进行分享有很大的驱动力。</p>
<h2 id="toc-4">04 APP游戏化设计</h2>
<p>聚焦应用市场，随着应用市场的软件越来越多，很多APP为了提升用户活跃和用户留存，都在想方设法抢占用户一天中花在自己APP的时间，其打法也是让人眼花缭乱。其中，很多APP都已经在逐步引入游戏化设计，比较典型的有马蜂窝（旅游类）、支付宝（第三方支付）、发现精彩（金融类）等。</p>
<p>为了在其业内打造差异化，首先，这几个APP都基于其品牌定位设计了游戏IP，并根据其主营业务进行玩法设计。以马蜂窝为例，作为一个主打旅游攻略的旅游类APP，其游戏IP设定为一家客栈的老板，负责打理这家客栈的生意、招待客人，偶尔还可以出去旅游，带回一些纪念品以装饰客栈。由于游戏场景符合APP定位，用户教育成本低且用户接受程度高。</p>
<p>另外，这几个APP的游戏设计也结合了用户成长体系和牵挂机制，如小蜂客栈的预订订单、蚂蚁庄园的每日登录领奖励、小羊之家的游乐园赢道具，令其游戏玩法更加丰富。</p>
<p>其实，它们也体现了PBL理论和八角行为分析的，各位看官可以自行摸索一下，看看这几个APP在进行游戏化设计时，是如何运用这些理论的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/7W6jv0i7yxKEYHQh7cUY.png" alt width="1508" height="994" referrerpolicy="no-referrer"></p>
<p>总而言之，游戏最能让用户上瘾也最能黏住用户，当我们在考虑APP游戏化时，其实可以借鉴一下这些比较热门的游戏，思考其产品设计逻辑及背后的理论，指导我们进行功能及玩法设计。</p>
<h3>#参考资料#</h3>
<ol>
<li><a href="http://www.gamelook.com.cn/2019/07/366896">http://www.gamelook.com.cn/2019/07/366896</a></li>
<li><a href="https://baijiahao.baidu.com/s?id=1639850336762190699&wfr=spider&for=pc">https://baijiahao.baidu.com/s?id=1639850336762190699&wfr=spider&for=pc</a></li>
<li><a href="https://www.qimai.cn/app/comment/appid/1479366779/country/cn">https://www.qimai.cn/app/comment/appid/1479366779/country/cn</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/79386696">https://zhuanlan.zhihu.com/p/79386696</a></li>
<li>《流量池》 杨飞著</li>
<li>《游戏化实战：人类行为学×游戏机制，打造产品吸引力》[美] Yu-kai Chou著</li>
</ol>
<p> </p>
<p>本文由 @糖芽 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4568490" data-author="1040746" data-avatar="http://image.woshipm.com/wp-files/2020/09/34Khzbeh9jCRdKRHmlPv.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            