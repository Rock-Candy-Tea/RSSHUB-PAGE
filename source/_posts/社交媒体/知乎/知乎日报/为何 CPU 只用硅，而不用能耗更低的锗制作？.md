
---
title: '为何 CPU 只用硅，而不用能耗更低的锗制作？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic1.zhimg.com/v2-c085855ea40ccfdb3e70ee7bad672171_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2022-02-15 05:08:26
thumbnail: 'https://pic1.zhimg.com/v2-c085855ea40ccfdb3e70ee7bad672171_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">


<div class="answer">

<strong>
<img class="avatar" src="https://pic1.zhimg.com/v2-c085855ea40ccfdb3e70ee7bad672171_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">温戈，</span><span class="bio">想当作家的 数字芯片设计工程师 公众号：OpenIC</span>
<a href="https://www.zhihu.com/question/28935966/answer/2347216215" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p><strong>有趣的是，世界上第一个晶体管和第一块集成电路都是用锗做的。</strong></p>
<p><strong>晶体管的诞生</strong></p>
<p>如果谈起 20 世纪最伟大的发明，每个人心中都会有不同的答案：计算机、原子弹、青霉素……但毫无疑问的是，晶体管以及基于晶体管的发明极大推动了科技的进步和社会的发展。</p>
<p>世界上第一台电子计算机 ENIAC 诞生于 1946 年，如图所示。它由 17468 个电子管、6 万个电阻器、1 万个电容器和 6 千个开关组成，重达 30 吨，占地 160 平方米，耗电功率约为 174 千瓦，耗资 45 万美元。ENIAC 虽然每秒只能运行 5 千次加法运算，但它仍然是一项伟大的发明。它主要由电子管组成，电子管有诸多缺点，如体积大、功耗高、电源利用效率低等，很难满足人们对计算效率的期待，这使得业界开始寻找晶体管的替代品。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-3e01d498ad1099f1810ab018033751cf_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>工程师在操作 ENIAC</figcaption></figure>
<p>故事开始于隶属于美国电话电报公司（American Telephone & Telegraph，AT&T）的贝尔实验室。一战后，AT&T 的研发部门在不断扩张，1925 年，时任 AT&T 总裁的 Walter Gifford 收购了西方电子的研发部门，成立了贝尔电话实验室，由芝加哥大学的物理学家——Frank Jewitt 担任总裁。在今后的很多年里，多项伟大的发明都出自贝尔实验室，比如蜂窝式电话系统、太阳能硅光电池、通信卫星等。当然还有我们今天的主角——晶体管。</p>
<p>1936 年，时任贝尔研究室主任的 Mervin Joe Kelly 决定建立一个部门来研究固态物理，希望用半导体材料制造出比真空电子管更可靠、功耗更低、体积更小、效率更高的替代品，为此，他招募了多位青年才俊，威廉·肖克利（William Shockley）赫然在列。然而，不久后，第二次世界大战爆发，这个部门不得不解散，这项研究也因此而搁置。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-e795225f192ab868d34111ea961d7272_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>默文·乔·凯利（Mervin Joe Kelly）</figcaption></figure>
<p>1945 年二战结束后，由威廉·肖克利找来了号称可以建造任何东西的实验物理学家沃尔特·布拉顿和明尼苏达大学的理论物理学家约翰·巴丁(John Bardeen)，还有其他一众物理学家、化学家、工程师，再次成立了半导体研究小组。经过近两年的潜心研究，终于有了成果。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-124014c15a83d9ea85ca66538d987bc3_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>左起分别为巴丁、肖克利和布拉顿</figcaption></figure>
<p>1947 年 12 月 16 日，研究小组测试了他们的新装置，为其输入了频率为 1000 赫兹的信号，结果在输出端获得了 30%的功率增益和 15%的电压增益，这个结果振奋人心！一周后，就在大部分美国人都已经进入圣诞假期时，贝尔实验室的科学家们陆续来到办公室，<strong>正式向世界演示了第一个基于锗半导体的具有放大功能的点接触式晶体管</strong>。半导体产业的传奇之路也由此开启！</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-3f054ea6cdaa2445fd539e201c5acfe4_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>左图为点触式锗晶体管，右图为其电路示意图</figcaption></figure>
<p>在点触式锗晶体管发明以后的几十年，晶体管也在发生着变迁，其性能也在飞快地进步，材料也不断的推陈出新。</p>
<p>在晶体管发明出来之后，还有一点小小的插曲，就是晶体管的命名。当时贝尔实验室小组的成员想了好几个名字，包括“晶体三极真空管”、“固态三极真空管”、“半导体三极真空管”等。但最终采用了约翰·皮尔斯提出的 “晶体管” 一词。据约翰·皮尔斯回忆说: “我之所以提出这个名字，着重考虑了该器件是做什么的。那时，它本应该是电子管的复制品。电子管有跨导，晶体管就应该有跨阻。此外，这个器件的名称应当与变阻器，电热调节器等其它器件名称相匹配，于是我建议采用“晶体管”这个名字”。</p>
<p><strong>集成电路的发明</strong></p>
<p>在 2000 年诺贝尔奖的颁奖典礼上，瑞典皇家科学院宣布，将本年度诺贝尔物理奖授予三位科学家，他们是俄罗斯圣彼得堡约飞物理技术学院的若尔斯·阿尔费罗夫、美国加利福尼亚大学的赫伯特·克勒默和德州仪器公司的杰克·基尔比。彼时，距离集成电路的发明已经过去了 42 年，而这 42 年漫长的时光，证明了集成电路在推动人类发展的过程中，扮演的无与伦比的重要性。<strong>在获奖感言中，基尔比感叹道：“要是诺伊斯还活着的话，肯定会和他分享诺贝尔奖”。</strong>集成电路诞生的舞台上，聚光灯照向了这两位半导体先驱。</p>
<p>杰克·基尔比出生于 1923 年，家乡在美国密苏里州首府——杰佛逊市。基尔比的父亲是一名电气工程师，在童年时代，基尔比经常在父亲的公司玩，对各种电气设备展现出了浓厚的兴趣。1947 年，基尔比从伊利诺大学毕业，获得电子工程学士学位，随后进入全球联通公司的中心实验室工作。他一边工作一边在威斯康辛大学米尔沃基分校攻读硕士学位。这一期间，基尔比和芭芭拉·安吉斯结婚，几年后，他们有了两个女儿。1958 年，基尔比加入了德州仪器公司。那年夏天，多数同事都在南海岸度假的时候，基尔比却在构思集成电路。此时，基尔比已经在微型电路研究方向积累了相当丰富的理论知识，在他心中把晶体管、二极管、电阻、电容、电感等元件都做在一块半导体晶片上的想法愈发强烈。</p>
<p>功夫不负有心人，<strong>1958 年 9 月，在助手谢泼德的帮助下，向德州仪器的高层们展示了第一块锗集成电路­</strong>——相移振荡器，所示。当基尔比在输入端接上电源，输出端接上示波器，一道完美的正弦波形划过屏幕，开启了现在的信息时代之路。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-95824d473c66f1ddf369b526016c9ad5_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>罗伯特·诺伊斯出生于 1923 年，家乡在<a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%25E7%25BE%258E%25E5%259B%25BD/125486" target="_blank" rel="nofollow noreferrer">美国</a><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%25E7%2588%25B1%25E8%258D%25B7%25E5%258D%258E%25E5%25B7%259E" target="_blank" rel="nofollow noreferrer">爱荷华州</a>柏林顿市。1939 年，诺伊斯一家搬到了爱荷华州的格林内尔，此时的诺伊斯开始展现出了发明家特质。12 岁时，他和哥哥制造了一架重 25 磅，4 英尺高，翼展 16 英尺的滑翔机，爬上屋顶准备体验一下飞翔的感觉，却以自由落体的方式落地。虽然中学时代的诺伊斯是一位“破坏发明家”，但学习成绩却非常棒！考上了当地最好的格林纳尔学院攻读物理学并于 1949 年获得学士学位，随后进入麻省理工学院，并于 1953 年获得固体物理学博士学位。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-640450169ad9abeddc7cac0a873afc1a_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>1957 年，诺伊斯作为联合创始人创立了仙童半导体。1958 年，仙童半导体在一片晶圆上生产晶体管和其他电子元器件，再将晶圆切成单个电子元器件，最后用导线连接起来。诺伊斯发现切割和再连线的动作着实多此一举，完全可以在一块硅晶圆上实现完整的电路。1959 年春，诺伊斯起草了基于平面工艺的集成电路的专利申请书。<strong>1959 年，诺伊斯发明了第一块单片硅集成电路</strong>，如图所示。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-a2899780786d8bff7f39e16f226dfc05_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>诺伊斯发明的硅集成电路</figcaption></figure>
<p>基尔比和诺伊斯几乎在同一时间发明了集成电路，这也引起了一场长达多年的专利权诉讼。基尔比的专利虽然申请在前，却在 1964 年 6 月 23 日才被批准，而诺伊斯的申请虽然比基尔比稍晚，但早在 1961 年 4 月 26 日就被批准了。但因为两人几乎同时且独立发明了集成电路，最终，法院判决两个专利都有效。多年以后，当人们享受着集成电路带来的科技成果时，也应记得两位“集成电路之父”。<strong>因为他们传奇的一生，是所有人在童年时代，梦想着要成为的样子。</strong></p>
<p><strong>硅相比锗的优点</strong></p>
<p>几乎所有的半导体材料都可以做成应用于模拟电路的放大器，或者数字电路的电子开关。但无奈，硅的优点太多了，这让它成为了半导体行业的主角。</p>
<p><strong>优点 1：含量丰富</strong></p>
<p>2021 年，《自然》杂志就发出呼吁，称全球的沙子已经不够用了，目前沙子、砾石的开采速度已经超过了自然恢复速度。并且，曾经有一句广为流传的话：硅谷每年制造的晶体管数量，比下的雨都多。</p>
<p>地壳中硅的含量占 26.3%，仅次于氧。而锗元素是一种典型的稀有<strong>分散元素</strong>，在地壳中含量约<strong>百万分之七。</strong><sup>[1]</sup>简而言之，不仅含量比硅少了好几个数量级，且在地壳中分布分散，难以开采。</p>
<p><strong>优点 2：易于提纯</strong></p>
<p>硅提纯技术非常成熟，纯度可以达到 10 个 9。</p>
<p><strong>优点 3：性质稳定</strong></p>
<p>硅的物理性质和化学性质都非常稳定，单个晶体管在 CPU 的一生中坏的概率极小的，再加上芯片设计的冗余设计，CPU 基本不会坏。这也是我们很少听到电子产品中 CPU 坏的原因。</p>
<p><strong><strong>优点 4：禁带宽度高，热稳定性好</strong></strong></p>
<p>锗的禁带宽度约为 0.66ev，而硅的禁带宽度约为 1.12ev。不用说工业、军用、航空航天等领域，哪怕是自家的主机，CPU 满载时，温度达到七八十度都是有可能的。所以后来就有了 AMD 和 Intel 谁家的 CPU 烤肉更快更香等实验及争论，为电子发烧友们所津津乐道。</p>
<p>除以上外，硅的掺杂扩散工艺多种多样、制造过程中容易形成二氧化硅绝缘层等。当然锗自身也有优点，比如电子的迁移率高，压降低，速度快，开启电压低等，但瑜不抵瑕，<strong>一代半导体“贵族”锗就这样沉没在半导体的辉煌历史之中。</strong></p>
<p><strong>总结</strong></p>
<p>半导体行业经过近 70 年的发展，半导体材料经历了 3 次明显的更新换代和发展。第一代半导体材料主要是指硅、锗等元素半导体材料；第二代半导体材料主要是指化合物半导体材料，如砷化镓、锑化铟，在 4G 时代，它们作为大部分通信设备的材料，应用领域包括移动通信、卫星通信、导航等领域；第三代半导体材料主要是以碳化硅（SiC）、氮化镓（GaN）为代表的复合半导体材料。相比于第一、二代半导体材料，第三代半导体材料具有更高的禁带宽度、击穿电压、电导率和热导率等，更适合应用在高功率和高频高速领域，如新能源汽车、手机快充、5G 射频器件等。相比于第一代和第二代半导体材料，第三代半导体材料并不是迭代和替换的关系，而是应用领域有所不同。</p>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/28935966">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            