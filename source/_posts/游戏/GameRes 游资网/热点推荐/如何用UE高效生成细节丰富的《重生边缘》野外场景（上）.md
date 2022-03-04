
---
title: '如何用UE高效生成细节丰富的《重生边缘》野外场景（上）'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202203/01/090122nwtsenjwcndj22cx.jpg'
author: GameRes 游资网
comments: false
date: Tue, 01 Mar 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202203/01/090122nwtsenjwcndj22cx.jpg'
---

<div>   
<font color="#808080"><i>以下文章来源于NExT Studios ，作者引擎全开的</i></font><br>
<br>
“过程化内容生成”也叫“程序内容生成”（Procedural Content Generation=PCG），是一种自动为游戏、模拟或电影创建数字资产的方式，可以大大提高内容生成的效率。<br>
<br>
NExT Studios 在使用虚幻引擎4开发《重生边缘》（SYNCED：Off-Planet）的过程中，在过程化生成场景方面进行了一些尝试：除了介绍各种生成内容的思路外，还分享了针对过程化生成工具加入场景制作后，如何解决新的工具在实际工作中遇到的各种问题，以及一些实验性工作分享。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032085" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090122nwtsenjwcndj22cx.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090122nwtsenjwcndj22cx.jpg" width="600" id="aimg_1032085" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090122nwtsenjwcndj22cx.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《重生边缘》主地图</font></font></div><br>
主地图曝光！最初只有3个场景美术，作为中途加入者，会遇到哪些问题？如何提高过程化生成工具的工作效率<br>
<br>
主地图3x3公里，大约有 20 个 POI、16 层地表、9 万多棵树、30 多种植被、 20 公里长的路和 6 公里的河流。最初除了Unreal Editor之外，我们没有过程化生成的积累，在加入过程化生成内容的时候，也不能覆盖已有的 prototype 关卡，同时需要兼顾关卡美术和关卡策划的操作习惯（他们在Unreal Editor中进行数据编辑工作，但过程化生成算法是在Houdini中实现，需要导入导出数据），各个生成元素之间有一定数据依赖关系（比如河流改动会影响地形的高度图和材质层，地形高度图改动也会影响到植被的分布等）......我们面临许多挑战。<br>
<br>
我们开发了约30个工具，但因为场景中每个 POI 的风格和设计都非常不一样，较难提取统一的理性规律，所以工具的目的是调整关卡布局时，加速周边环境的修改，大部分的生成内容集中在野外区域。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032086" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090122xjq5exrzzdzxpzp1.gif" data-original="https://di.gameres.com/attachment/forum/202203/01/090122xjq5exrzzdzxpzp1.gif" width="480" id="aimg_1032086" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090122xjq5exrzzdzxpzp1.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">场景结构</font></font></div><br>
地表侵蚀的作用？地表材质层的权重分布如何计算？<br>
<br>
把mask转成地形后做侵蚀美化是基础功能，侵蚀会改变高度图的表现，也会生成地表材质层的权重分布。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032087" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090123qtx5ygytbq7lxqyy.gif" data-original="https://di.gameres.com/attachment/forum/202203/01/090123qtx5ygytbq7lxqyy.gif" width="480" id="aimg_1032087" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090123qtx5ygytbq7lxqyy.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">侵蚀前后地形对比</font></font></div><br>
地表权重图是在Houdini当中进行计算的，大概原理是：根据高度图的斜率计算出大体分布，然后配合例如雨水冲刷的效果，根据每一层的石头和沙地的规则，定义出不同的权重图，然后导入引擎，就可以得到混合好的地表效果。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032088" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090123upzb9ggg3g03hg95.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090123upzb9ggg3g03hg95.jpg" width="600" id="aimg_1032088" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090123upzb9ggg3g03hg95.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">混合好的地表效果</font></font></div><br>
垂直面地表崖壁岩石如何生成？如何在地表上呈现更丰富的细节？人物卡进mesh里如何处理？<br>
<br>
我们当时参考了一些业界资料，比如《孤岛惊魂5》（Far Cry 5）、《刺客信条》（Assassin's Creed）。一开始我们根据地形的坡度，提取它的区域转成mesh，然后生成UV，贴上我们想要的纹理后，用displacement map模拟了岩石表面的凹凸，但是近看的效果不理想。于是我们尝试了另外一种方案——mesh贴片。像贴瓦片一样，把固定的mesh往所需区域里重复粘贴，这样可以用比较低的面数达到更好的效果，因为它的几何细节会更多一些。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032089" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090126yzc6at6wochaaowa.gif" data-original="https://di.gameres.com/attachment/forum/202203/01/090126yzc6at6wochaaowa.gif" width="600" id="aimg_1032089" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090126yzc6at6wochaaowa.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">mesh贴片效果</font></font></div><br>
在生成崖壁的mesh的时候，崖壁下方和与地表过渡的地方，可以用与岩石纹理类似的地表材质来表现，因此生成了相应的地表材质权重层。还需要处理生成的岩石与地表的过渡：生成mesh的时候，把权重写到了顶点色里面，然后采样地形的纹理做柔和地过渡。岩石下方我们可以生成一些碎石或砂石，这样会有更具细节的地表表现。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032090" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090127ijxskkeeetmu2dsi.gif" data-original="https://di.gameres.com/attachment/forum/202203/01/090127ijxskkeeetmu2dsi.gif" width="480" id="aimg_1032090" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090127ijxskkeeetmu2dsi.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">增加细节前后的岩壁对比</font></font></div><br>
在实际运用中还会遇到一些尴尬的问题，例如人物有时会卡在生成的mesh里。这是因为Unreal根据不规则的mesh默认生成的碰撞体有很大瑕疵，这时我们会针对这些不是闭包类的mesh生成特殊碰撞体，然后再一起导入引擎。<br>
<br>
如何计算获得视觉均匀的植被分布？植被间距如何考量？如何进行撒点操作？<br>
<br>
我们参考了《孤岛惊魂5》（Far Cry 5），这几乎是业界最详细的分享。我们的整体生态和植被组成是不一样的，我们选择的是温带针叶林。具体做法是：我们根据高度图生成各种各样的mask，再配合噪声模拟随机分布。在此之上，我们可以把光照、风向和气候影响也考虑在内，生成更多的mask，通过运算得到我们想要的分布。<br>
<br>
有了植被的区域后，我们可以在区域中进行撒点操作：一种操作是直接在区域中进行随机撒点，另一种是围绕某个目标点周围进行随机撒点。我们可以在第二种情况下生成伴生的灌木，一般情况下我们不可能一次只生成一种植被。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032091" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090128nqbu0hb1qviqqhau.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090128nqbu0hb1qviqqhau.jpg" width="600" id="aimg_1032091" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090128nqbu0hb1qviqqhau.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">两种撒点方法</font></font></div><br>
我们针对每种植被定义了三种半径，用来防止树与树之间的重合。根据这些规则，我们量化这些点的位置，让离得较近的点更易被判断。如果这些点都被包围的时候，我们无法移动把它排除掉，我们就删掉它。<br>
<br>
通过这样不断迭代，我们可以获得非常均匀、没有互相穿插的效果。但在不同的树种之间（例如高大的树木和低矮的灌木间），其实可以有一定的穿插，这是我们定义外半径和内半径的原因。对于大地图上的不同的区域，会有不同的生态分布。我们可以通过全地图刷mask来区分我们每一部分使用怎样的生成规则。比如说在海边，我们会以一些草地沙石为主，山上则以森林为主。<br>
<br>
<div align="center">
<img aid="1032092" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090128o26evdcmcdycta4v.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090128o26evdcmcdycta4v.jpg" width="600" id="aimg_1032092" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090128o26evdcmcdycta4v.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1032093" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090129xrwf4orvvoy79d4y.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090129xrwf4orvvoy79d4y.jpg" width="600" id="aimg_1032093" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090129xrwf4orvvoy79d4y.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1032094" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090129i6xz9dls9nx2mrj6.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090129i6xz9dls9nx2mrj6.jpg" width="600" id="aimg_1032094" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090129i6xz9dls9nx2mrj6.jpg" referrerpolicy="no-referrer">
</div><br>
河流如何生成？下游比上游还要高如何处理？转折度大的河流如何处理平滑？生成完河道之后，地表的纹理细节如何调整？<br>
<br>
在《重生边缘》中，河流是表现类的效果，不影响游戏的玩法，所以过高的高度差、过深的水面都是策划和美术不想要的，所以我们希望做很浅的溪流。我们算法上也学习过《地平线》（Horizon）的分享，整个生成过程大概分成：<br>
<br>
• 我们先有大概的曲线，根据地形高度图做自然滑落。相当于把一条绳子扔在地表上，它会自然地弯曲；<br>
<br>
• 有些地方地势比较高，我们可以挖一条河道，这时会改变地形的高度；<br>
<br>
• 因为我们不想生成过大高度差，从高地往低地过渡时，我们需要形成多级小瀑布；<br>
<br>
• 然后我们根据河流的地形地势分布和弯曲度，生成河面河道宽度的变化。<br>
<br>
• 最后我们在河道里撒上一些碎石和水花去装饰，并生成河流的流向。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032095" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090130ayggg3fpg3rpoad2.gif" data-original="https://di.gameres.com/attachment/forum/202203/01/090130ayggg3fpg3rpoad2.gif" width="480" id="aimg_1032095" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090130ayggg3fpg3rpoad2.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">河流生成过程</font></font></div><br>
河道生成的其他问题：<br>
<br>
• 支流跟主流交叉的地方，可能高度并不一样，我们需要对齐高度；<br>
<br>
• 有可能下游高于上游高度，这时候需要用下游的高度去往上游去做修正；<br>
<br>
• 转折度较大和多个支流交叉的区域，我们不可能生成很多层的河面的mesh，所以做平滑处理，从平滑后的河道形状提取出河面，再对河面mesh进行切割和减面，这样对性能的优化很有帮助。<br>
<br>
如何减少河面流向图的内存占用？如何编辑河流的走向和效果？<br>
<br>
对于河面的流向图，如果用全地图的flow map一张纹理来覆盖的话，会浪费非常多的UV空间。考虑到更高效性能和更低内存占用，我们把流向信息写到顶点色里，只需占用两个通道。<br>
<br>
生成完河道后，地表的纹理会随之变化，我们可以铺设鹅卵石，或在河岸边缘生成潮湿泥沙的效果增加河岸表现，生成相应的植被分布增加细节等。<br>
<br>
我们使用Unreal Landscape Spline的内置功能来对河流进行曲线编辑，因为它比较符合美术的操作习惯。我们先拖拽出河流经过的区域，然后编辑各个支流大致的路径，设置每条支流的起始点，之后一键生成。这时候我们可以根据地势做自然弯曲，挖出河道、生成地表的纹理，生成河面的mesh，还有河面流向的数据，包括水花、石头等等。<br>
<br>
<div align="center">
<img aid="1032096" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090130x9duyccizyikgkdo.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090130x9duyccizyikgkdo.jpg" width="600" id="aimg_1032096" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090130x9duyccizyikgkdo.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1032097" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090130m0861s5izqz1u6dq.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090130m0861s5izqz1u6dq.jpg" width="600" id="aimg_1032097" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090130m0861s5izqz1u6dq.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1032098" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090131h3s3ffyijnn3yyvj.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090131h3s3ffyijnn3yyvj.jpg" width="600" id="aimg_1032098" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090131h3s3ffyijnn3yyvj.jpg" referrerpolicy="no-referrer">
</div><br>
裂缝长草、土路破损、路口过渡、车轮印记等道路上的“细节加分项”如何实现？多层贴花的优先级如何制定？<br>
<br>
游戏当中的道路基本是关卡策划在编辑，它对玩法是有一定影响的，当我们加入做生成工具的时候，路网已有大约百分之八九十的完成度，所以我们并不是生成道路本身的路网，而是选择去增加一些细节“加分项”。比如裂缝长草、公路破损、不同道路之间的过渡、交叉口的车轮印记等。<br>
<br>
实现的思路就是使用海量贴花（在 GDC 2017 的 Ghost Recon Wildlands: Terrain Tools and Technology 中有类似分享）来实现，包括路面的破损、道路中间的车轮印、车道标记、水迹效果、路边的落叶的尘土的效果，都是通过贴花的方式来实现的。但裂缝里长的草不是贴花，是在生成裂缝贴花的时候，顺便把裂缝草的位置一起计算出来。<br>
<br>
还有一个比较实用的功能，用Unreal Landscape Spline做道路的时候并不能很好地处理交叉口，我们生成了任意角度交叉口的贴花，掩盖了衔接处的接缝问题。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032099" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090131n11y4yw91f1tyn1a.gif" data-original="https://di.gameres.com/attachment/forum/202203/01/090131n11y4yw91f1tyn1a.gif" width="600" id="aimg_1032099" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090131n11y4yw91f1tyn1a.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">道路交叉口贴花</font></font></div><br>
有了多层贴花，我们需要定义呈现层次的优先级问题，所以我们制定了“同级融合，高级覆盖低级”的贴花规则。全体的半透明材质的贴花数量加起来有数万个，有很重的overdraw，会带来非常严重的性能问题。所以我们使用了 Unreal 的Runtime Virtual Texture 来进行优化，把地表混合的结果跟道路和贴花混合的结果缓存到了一张巨大的虚拟纹理上面，可以大大降低地表绘制的开销。<br>
<br>
另外我们在道路曲线计算完毕之后，可以根据道路曲线的分布来调整地表的权重分布。比如我们可以在道路的周边去生成相应地表的过渡效果（裂缝、草、破损尘土、水迹、路口交叉口车轮的印记），另外还有道路的附属物（比如护栏、电线杆）等。<br>
<br>
<div align="center">
<img aid="1032100" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090132lxcz0z96ne26wccx.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090132lxcz0z96ne26wccx.jpg" width="600" id="aimg_1032100" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090132lxcz0z96ne26wccx.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1032101" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090132f2gp6dpzdfggp3fh.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090132f2gp6dpzdfggp3fh.jpg" width="600" id="aimg_1032101" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090132f2gp6dpzdfggp3fh.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1032102" zoomfile="https://di.gameres.com/attachment/forum/202203/01/090134e4778vui36y3nirg.jpg" data-original="https://di.gameres.com/attachment/forum/202203/01/090134e4778vui36y3nirg.jpg" width="600" id="aimg_1032102" inpost="1" src="https://di.gameres.com/attachment/forum/202203/01/090134e4778vui36y3nirg.jpg" referrerpolicy="no-referrer">
</div><br>
针对工具加入场景制作后，如何解决新的工具在实际工作中遇到的各种问题，以及更多实验性工作的分享，敬请期待下期推送！<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：NExT Studios</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/50f9AUIs3sAY-zBnCil2PQ</font></font><br>
<br>
  
</div>
            