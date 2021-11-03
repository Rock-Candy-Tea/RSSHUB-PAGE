
---
title: '【顶级结构】CSGO经典爆破模式地图中路结构分析'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202110/26/090954gie04x0m594e4101.jpg'
author: GameRes 游资网
comments: false
date: Tue, 26 Oct 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202110/26/090954gie04x0m594e4101.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2517307">
<div align="center">
<img id="aimg_1017143" aid="1017143" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090954gie04x0m594e4101.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090954gie04x0m594e4101.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090954gie04x0m594e4101.jpg" referrerpolicy="no-referrer">
</div>
<br><font color="#808080">本文首发知乎：</font><br><font color="#808080">https://zhuanlan.zhihu.com/p/296627234</font><br><br><strong><font color="#de5650">相关阅读：</font></strong><br><br><a href="https://www.gameres.com/890315.html" target="_blank">【顶级结构】CSGO经典爆破模式地图的A区结构分析</a><br><a href="https://www.gameres.com/890397.html" target="_blank">【顶级结构】CSGO经典爆破模式地图的B区结构分析</a><br><br><strong><font color="#de5650">引言</font></strong><br><br>
纵观CSGO爆破模式，凡是具有经典中路的地图，中路往往具有高连通性、高信息价值，T拿下了中路能够更好地组织进攻、更频繁地转点，CT拿下了中路能够更好地获取信息，因而中路成为了各张地图的兵家必争之地。<br><br>
那么如何设计一个高连通性、路径清晰、具有选择策略的中路呢，本文将从连通结构、递进关系、火线设计三个方向对CSGO爆破地图的经典中路结构进行分析。<br><br>
这里我们选择Dust2、Cache、Mirage三张地图作为我们的抽象分析对象，并对Dust2地图的中路结构进行详细分析。<br><br><strong><font color="#de5650">连通结构</font></strong><br><br>
首先我们可以对这三张地图的中路结构进行一个抽象<br><br><div align="center">
<img id="aimg_1017144" aid="1017144" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090954txp3htbntcnh2xhi.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090954txp3htbntcnh2xhi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090954txp3htbntcnh2xhi.jpg" referrerpolicy="no-referrer">
</div>
<br>
在这个图中，蓝色为CT路线，红色为T路线。A、B字母表示路径来自于哪个包点。<br><br>
可以明确看出，每个地图的中路结构都是多路径对多路径。<br><br>
造成这种构造的原因，是中路作为A、B两个包点的连接区域，必须要有直接或间接通向这两个包点的连接线路，因而会有多条CT线路在此交汇。<br><br>
为了平衡攻防双方在中路的优势，相应的也要为进攻方制造多个线路。<br><br>
为了控制地图结构的复杂度，降低玩家选择的迷惑性，CSGO的爆破地图在中路为双方提供的进攻或前压的路线不会超过3条。<br><br>
因此可以看见CSGO的爆破模式竞技地图中，中路的连通结构通常为2~3条CT路线 VS 2~3条T路线。<br><br><strong><font color="#de5650">递进结构</font></strong><br><br>
但是事实上，过于简单的地图结构会降低策略深度和游戏可玩性，作为重中之重的中路区域很多时候必须要承担相当复杂的连通功能。<br><br>
当中路需要为某些区域提供较多的行径路线，2~3条进攻路线不能满足设计需求时怎么办呢？<br><br>
CSGO的设计师采用了递进结构来隐藏多余的路线选择，并且制造出递进式的选择策略和进攻节奏。<br><br><strong><font color="#de5650">Dust2中路的CT路线——递进结构</font></strong><br><br>
Dust的中路，以中门为中线，将地图划分为了两部分，T优势区和CT优势区<br><br><div align="center">
<img id="aimg_1017145" aid="1017145" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090955bisycb918i08h31y.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090955bisycb918i08h31y.jpg" width="469" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090955bisycb918i08h31y.jpg" referrerpolicy="no-referrer">
</div>
<br>
进攻方在面对中路结构时，能够清晰地看到两个进攻路线<br><br><div align="center">
<img id="aimg_1017146" aid="1017146" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090955j8ckgdkykd9dcykc.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090955j8ckgdkykd9dcykc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090955j8ckgdkykd9dcykc.jpg" referrerpolicy="no-referrer">
</div>
<br>
这是作为递进的最外层，给玩家最直接最初步的策略选项，不管选择哪条线路都意味着一场异常艰辛的突破作战。<br><br>
这里精妙的地方在于，这两条不同的线路选择，在执行突破时面对的作战场景也不尽相同。<br><br>
在选择小道进行突破时，面对的是单向的纵轴多架点战斗场景；而在选择中门进行突破时，面对的是多向架点的战斗场景；如下图所示<br><br><div align="center">
<img id="aimg_1017147" aid="1017147" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090955trb8i9c9vhrd0ao0.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090955trb8i9c9vhrd0ao0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090955trb8i9c9vhrd0ao0.jpg" referrerpolicy="no-referrer">
</div>
<br>
而在攻下来最外层的递进空间后，小道和中门为玩家提供了短暂的可停歇修整的区域，这一片区域不会设计得特别安全，但是也能让进攻方短暂停留。<br><br><div align="center">
<img id="aimg_1017148" aid="1017148" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090955smltlgk80qex0ckg.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090955smltlgk80qex0ckg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090955smltlgk80qex0ckg.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1017149" aid="1017149" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090956nee71ho17kx6xhkk.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090956nee71ho17kx6xhkk.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090956nee71ho17kx6xhkk.jpg" referrerpolicy="no-referrer">
</div>
<br>
在这个区域之后，就是地图作者布置的第二层递进，依旧给与了玩家两个选择路线，每个路线的选择战斗场景也不尽相同，这里就不赘述了。<br><br><div align="center">
<img id="aimg_1017150" aid="1017150" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090956p4m28ot498l4lhez.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090956p4m28ot498l4lhez.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090956p4m28ot498l4lhez.jpg" referrerpolicy="no-referrer">
</div>
<br>
通过这样的两层嵌套关系，将中路进攻方面对的四个选择，递进化为两层的双向选择，玩家在递进结构的每一层只需要对两个决策进行思考。而每一层的两个选择都将面临不同的战斗场景，这样也保留了选择的策略性。<br><br><div align="center">
<img id="aimg_1017151" aid="1017151" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090956xiar0c0lack9lzct.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090956xiar0c0lack9lzct.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090956xiar0c0lack9lzct.jpg" referrerpolicy="no-referrer">
</div>
<br><strong><font color="#de5650">Dust2中路的T路线特征——远近交替</font></strong><br><br>
中路的T线路的区别，主要体现在枪线的距离上，以下是三条线路的常规交火位置的枪线距离<br><br><div align="center">
<img id="aimg_1017152" aid="1017152" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090956fny511e3av1jfm1m.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090956fny511e3av1jfm1m.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090956fny511e3av1jfm1m.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1017153" aid="1017153" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090957y56mw6o7e7vrev7n.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090957y56mw6o7e7vrev7n.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090957y56mw6o7e7vrev7n.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1017154" aid="1017154" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090957bco1zyofy1em0y1m.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090957bco1zyofy1em0y1m.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090957bco1zyofy1em0y1m.jpg" referrerpolicy="no-referrer">
</div>
<br>
可以看见中路T的三条线路为进攻方提供了从60米到10米的各种不同的枪线。其意义在于，能够让玩家根据他们使用的武器和擅长的交火方式，选择合适的进攻途径。<br><br>
但其中较为核心的一点在于，长枪线、高风险的路线一般而言是路线更近、更容易抵达的，而道路曲折的短枪线往往需要较为麻烦地抵达，在Dust2这张图上这个麻烦是绕远路。<br><br><div align="center">
<img id="aimg_1017155" aid="1017155" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090957n85pq1b88qla3qh3.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090957n85pq1b88qla3qh3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090957n85pq1b88qla3qh3.jpg" referrerpolicy="no-referrer">
</div>
<br>
这样的设计也遵从了效率预估的原则，即“更高效率的选择带来更高风险”。<br><br><strong><font color="#de5650">Dust2中路的CT防守多样</font></strong><br><br>
上面提到的，全都是为进攻方提供的策略选择，而事实上地图的作者也为防守方提供了更多的选择，最突出的，就是每条线路的多样性架点。<br><br>
与T线路的多种距离的枪线类似，CT放的每条线路也具有多个距离的枪线可供防守方选择，如下图所示。<br><br><div align="center">
<img id="aimg_1017156" aid="1017156" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090957ydbhu2dkhfkpdpak.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090957ydbhu2dkhfkpdpak.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090957ydbhu2dkhfkpdpak.jpg" referrerpolicy="no-referrer">
</div>
<br>
除此之外，也为CT方提供了前压的途径，下图是两个经典的前压思路。<br><br><div align="center">
<img id="aimg_1017157" aid="1017157" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090957ifhb6h3a63616udu.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090957ifhb6h3a63616udu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090957ifhb6h3a63616udu.jpg" referrerpolicy="no-referrer">
</div>
<br>
当然了，有前压也有反制，地图作者在T路线的尽头为进攻方设置了多处反制前压的设计，大幅增加了前压的风险。这也充分体现了“高风险->高收益”的设计思路。<br><br><div align="center">
<img id="aimg_1017158" aid="1017158" zoomfile="https://di.gameres.com/attachment/forum/202110/26/090958hi1xef9kxzkyh55y.jpg" data-original="https://di.gameres.com/attachment/forum/202110/26/090958hi1xef9kxzkyh55y.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/26/090958hi1xef9kxzkyh55y.jpg" referrerpolicy="no-referrer">
</div>
<br><strong><font color="#de5650">总结</font></strong><br><br>
经过二十年的迭代和社区智慧的汇总，走到今天CSGO的每张的每个细节都体现了极强的设计能力，然而其基本的设计理念依然没有走出传统游戏学的策略范畴。<br><br>
从Dust2地图的中路设计思路来看，主要体现如下几个核心思想：<br><br><ul>
<li>为玩家提供多样化的、有限且有意义的选择</li>
<li>为玩家提供效率预估途径——高效率（高收益）的选择伴随着高风险<br>
</li>
</ul>
<br>
具体到地图设计语言又可以总结出以下几点：<br><br><ul>
<li>用递进层级的设计，降低玩家每次面对的选择数量，但总体上依旧提供数量丰富的路线选择。</li>
<li>玩家选择不同的路线将会面对不同的战斗场景。其中一些适用的枪械也不同。例如会有长狙线，也会有可以绕远抵近狙点的侧面道路。</li>
<li>低风险的路线，往往需要额外的成本以到达。例如绕远路带来的时间成本，或者双架位带来的操作成本。</li>
<li>为防守方提供更多的可能性，包括前压手段，但是前压同样伴随着极高的风险。<br>
</li>
</ul>
<br>
本文仅分析了Dust2地图，但是具有传统中路结构的CSGO爆破地图，大多遵循这些设计理念。甚至衍生开去，那些中路魔改地图（例如Overpass和Nuke）也会在具有中路意义的路线设计上遵循这些设计理念。<br><br>
本文仅一家之谈，欢迎讨论。<br><br><font size="2"><font color="#808080"></font></font><br><font size="2"><font color="#808080">原文：https://zhuanlan.zhihu.com/p/296627234</font></font><br><br>
</td></tr></tbody></table>


  
</div>
            