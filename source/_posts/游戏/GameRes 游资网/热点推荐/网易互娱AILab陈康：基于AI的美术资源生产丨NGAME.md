
---
title: '网易互娱AILab陈康：基于AI的美术资源生产丨N.GAME'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202204/20/092035bjn2ssti1p1j1spi.jpg'
author: GameRes 游资网
comments: false
date: Wed, 20 Apr 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202204/20/092035bjn2ssti1p1j1spi.jpg'
---

<div>   
2022N.GAME网易游戏开发者峰会于「4月18日-4月21日」举办，在今日的技术驱动场，来自网易互娱AI Lab的技术经理陈康做了主题为《基于AI的美术资源生产》的精彩分享。<br>
<br>
<div align="center">
<img aid="1036924" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092035bjn2ssti1p1j1spi.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092035bjn2ssti1p1j1spi.jpg" width="600" id="aimg_1036924" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092035bjn2ssti1p1j1spi.jpg" referrerpolicy="no-referrer">
</div><br>
<font color="#808080">以下是嘉宾分享实录（部分删减与调整）：</font><br>
<br>
大家好，我是来自网易互娱AILab的陈康，目前负责互娱AI Lab沪杭团队，图形学、3D视觉和语音方向的技术研发和落地，很高兴有这个机会给大家分享一下我们部门从17年底成立到现在，在基于AI的美术资源生产方面做过的一些尝试。<br>
<br>
<strong><font color="#de5650">首先，什么是美术资源呢？</font></strong><br>
<br>
这在游戏行业其实是一个专有名词，也叫美术资产。我们这边以《一梦江湖》和《王牌竞速》两款游戏为例，一个偏古风的、一个偏现代的，艺术风格上是有明显差异。但共同点是你在画面里看到的所有东西，比如说人物、人物上看到的衣服、远处的建筑、植物、车辆、甚至界面上的这些按钮图标，其实都是美术同学在DCC软件或者游戏引擎中制作出来的，所以这些东西都属于美术资产。<br>
<br>
<div align="center">
<img aid="1036925" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092036txqtxxu4wqy7wjdp.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092036txqtxxu4wqy7wjdp.jpg" width="600" id="aimg_1036925" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092036txqtxxu4wqy7wjdp.jpg" referrerpolicy="no-referrer">
</div><br>
游戏行业发展到今天，在美术资产制作方面，已经形成了一套非常成熟的工业化、流水线生产的解决方案。<br>
<br>
我们以我们部门的虚拟技术代言人，同时也是峰会的虚拟主持人i.F. 为例，给大家简单介绍一下常见美术资产的制作过程。<br>
<br>
假设你作为一名策划同学，想要美术帮你制作一个这样的角色，你会怎么跟他表达需求呢？你可能会说你想要活泼可爱的二次元妹子，处于青春期的年龄段、可能性格有点呆萌……但这种描述其实都是很主观、抽象的描述，都是二次元，《阴阳师》那种二次元和《原神》那种二次元是有很大差异的。<br>
<br>
基于这种模糊的描述，美术是没法直接制作三维模型的，因为在这过程中肯定需要不停的迭代需求，甚至有可能推翻重做，所以在三维模型环节进行这种角色设计层面的迭代，成本是非常高的。<br>
<br>
所以策划的需求一般会先给到原画师，原画师会首先把这些抽象的描述转化成具体的形象，所有形象设计层面的修改和迭代都是在原画阶段完成的。<br>
<br>
<div align="center">
<img aid="1036926" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092036omm2w68oxwtithib.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092036omm2w68oxwtithib.jpg" width="600" id="aimg_1036926" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092036omm2w68oxwtithib.jpg" referrerpolicy="no-referrer">
</div><br>
这边展示的就是i.F.的角色原画，当然在设计过程中，原画师肯定会融入的自己理解，提出一些修改。因为在这个领域美术要比策划专业的多，比如IF这个形象，头上带的这个像兔子耳朵一样的耳机，就是原画同学自己设计出来的。我们的需求是制作一个青春可爱的技术代言人，这个耳机可以在保持角色可爱风格的同时，体现出一定科技元素。<br>
<br>
角色的原画设定图完善之后，就会进入模型环节，模型师会参考这个形象制作三维模型和对应的材质贴图。这边对模型师的要求就是，制作完成的模型和贴图放到游戏引擎之后，最大程度能够还原原画设计的形象。如果是静态物体的话，一般这一步做完就结束了，后面就直接交给场景编辑师在游戏引擎中搭建游戏场景就可以了。<br>
<br>
<div align="center">
<img aid="1036927" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092037uxzqq92249bgnz9u.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092037uxzqq92249bgnz9u.jpg" width="600" id="aimg_1036927" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092037uxzqq92249bgnz9u.jpg" referrerpolicy="no-referrer">
</div><br>
但游戏角色是要能动起来的，所以模型制作完成后，还要交给绑定师架设骨骼、蒙皮、一些变形体。然后制作绑定控制器，也就是角色身上的这些奇怪的线圈和右边的面板，通过操纵这些东西，就可以驱动角色做出一些对应的动作，绑定好的角色会交给动画师，动画师会采用动作捕捉，或者手动设定关键帧的方式制作动画资源。<br>
<br>
<div align="center">
<img aid="1036928" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092037opy0soyoquurp0us.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092037opy0soyoquurp0us.jpg" width="600" id="aimg_1036928" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092037opy0soyoquurp0us.jpg" referrerpolicy="no-referrer">
</div><br>
整个美术资产的生产过程，类似一条工业流水线，一环套一环。尤其是在玩家越来越挑剔、游戏行业越来越激烈的情况下，这块的开销一直是游戏研发成本的大头。像是现在的3A大作，如果不支持开放世界，已经不好意思说自己是本世代游戏了。<br>
<br>
开放世界是怎么打造开放感的？简单来说就是生产内容。比如《刺客信条》《孤岛惊魂》这种级别的游戏，地图动不动就几十平方公里，这种规模按传统方式制作已经不现实了。所以如今的游戏开发会最大程度利用程序化手段制作美术资源。<br>
<br>
而我们的工作，本质上就是要在程序化生产这条主线下，引入一些AI技术手段，从而实现一些传统方案无法做到的效果。下面我来介绍一下我们在原画、模型和动画三个方面做过的一些尝试。<br>
<br>
<strong><font color="#de5650">AI在原画方面的应用</font></strong><br>
<br>
在原画方面，我们做了两个辅助创作的工具。第一个工具用于二次元角色线稿的自动上色，并且可以生成多套不同的上色方案，主要作用是在设计二次元形象时，为美术提供一些色彩搭配的灵感。<br>
<br>
<div align="center">
<img aid="1036929" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092037whsc7n7un3kzsrbb.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092037whsc7n7un3kzsrbb.jpg" width="600" id="aimg_1036929" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092037whsc7n7un3kzsrbb.jpg" referrerpolicy="no-referrer">
</div><br>
第二个工具用于人脸的生成和编辑，它可以基于美术绘制的人脸线稿生成真实人脸照片，并且允许编辑人脸的一些属性。这里展示的，是修改人脸年龄后的结果。<br>
<br>
<div align="center">
<img aid="1036930" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092037tuz75ly55lf89855.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092037tuz75ly55lf89855.jpg" width="600" id="aimg_1036930" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092037tuz75ly55lf89855.jpg" referrerpolicy="no-referrer">
</div><br>
由于互联网上的人脸数据非常丰富，人脸结构也相对比较简单，所以目前这个工具可以生成非常高清的人脸照片。在设计一些写实类角色时，美术可以参考这些素材进行二次创作。<br>
<br>
当然，我知道很多同学对AI在原画方面的应用还有更高的期待。比如说利用GAN或风格迁移等技术直接生成场景原画，这也是AI技术最早出圈的一批应用。不过目前想要落地还稍微有点困难，倒不是说技术本身有什么问题，主要是因为游戏原画设计追求的不一定是真实，更多是一种特定艺术风格下的视觉表达。<br>
<br>
我们随便找一幅游戏画面对比一下，就会发现这种图片跟日常照片有明显区别。在当前的数据条件下，想生成这种级别的AI模型还比较困难。所以如何让AI在原画设计方面发挥更多的作用，也是我们未来的重点方向之一。<br>
<br>
<div align="center">
<img aid="1036931" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092038hpddcudd9vpt556i.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092038hpddcudd9vpt556i.jpg" width="600" id="aimg_1036931" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092038hpddcudd9vpt556i.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">人脸模型</font></strong><br>
<br>
在模型方面，我们的主要工作围绕在人脸模型上。首先简单介绍一个基础设施——三维参数化人脸模型，这是一个基于大量三维扫描得到的三维人脸数据制作出来的双线性模型，有脸型和表情两个维度，简单说就是任意给定一组脸型参数、一组表情参数，就会得到一个对应参数下的三维人头模型。<br>
<br>
<div align="center">
<img aid="1036932" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092038dlllddgdz1dddk89.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092038dlllddgdz1dddk89.jpg" width="600" id="aimg_1036932" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092038dlllddgdz1dddk89.jpg" referrerpolicy="no-referrer">
</div><br>
在2018年，我们自己扫描并制作了一套高质量的三维参数化人脸。当时一共采集了500个中国人的数据，其中男女各占一半，年龄段涵盖10-60岁，每个人扫描了7套表情，相当于一共采集了3500个人头。<br>
<br>
<div align="center">
<img aid="1036933" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092038jqve3zohz47ncovo.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092038jqve3zohz47ncovo.jpg" width="600" id="aimg_1036933" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092038jqve3zohz47ncovo.jpg" referrerpolicy="no-referrer">
</div><br>
我相信很多从事相关研究的同学对这个模型概念非常熟悉，这是由一篇1999年的SIGRAPH论文提出的概念，专业名称叫3DMM，目前学术界有一些很出名的开源3DMM数据。那我们为什么不直接用这种开源模型呢？主要有三方面原因：<br>
<br>
首先是版权问题，我们希望这套技术真的能在游戏产品中用起来；<br>
<br>
其次是精度问题，这些开源模型的精度距离实际游戏的标准还有不小的差距，我们早期做实验也会使用这些模型，但是美术会对质量非常嫌弃。所以我们自己采集时，每一个人头后续都人工精修过；<br>
<br>
最后是人种问题，这些开源模型一般都是欧美机构发布的，他们采集的对象主要是欧美的高加索人种。这种明显的高鼻梁、深眼窝特点，一看就不是亚洲人，所以我们果断决定自己制作一套。<br>
<br>
<div align="center">
<img aid="1036934" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092038rjdc4c3rc24r03h4.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092038rjdc4c3rc24r03h4.jpg" width="600" id="aimg_1036934" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092038rjdc4c3rc24r03h4.jpg" referrerpolicy="no-referrer">
</div><br>
在AI领域，参数化人脸的主要作用是提供关于人脸的三维形状先验，所以制作好的参数化三维人脸模型可以用于从二维照片中重建三维人脸模型。我们这套参数化人脸模型，在东亚人脸照片上取得了非常好的重建效果。<br>
<br>
<div align="center">
<img aid="1036935" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092039n73avw2ia536w853.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092039n73avw2ia536w853.jpg" width="600" id="aimg_1036935" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092039n73avw2ia536w853.jpg" referrerpolicy="no-referrer">
</div><br>
当然，由于单视角照片会在深度方面存在缺失，很难还原类似鼻梁高度、眼窝这方面的特征，所以我们也开发了一套多视角的重建算法。如果条件允许，可以拍摄演员的多张照片进行重建。大家可以对比一下——右边多视角的重建结果对演员鼻子形状的还原程度，要比单视角高非常多。<br>
<br>
<div align="center">
<img aid="1036936" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092039zfny6fsj2bbpb9bj.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092039zfny6fsj2bbpb9bj.jpg" width="600" id="aimg_1036936" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092039zfny6fsj2bbpb9bj.jpg" referrerpolicy="no-referrer">
</div><br>
除了从照片中重建三维模型，这套参数化人脸还有一个更重要的应用，就是为游戏批量生成人头模型。如果游戏的人头资源标准跟我们库里的标准一致，就可以直接在参数化人脸模型的参数空间采样，把采样模型给到游戏项目使用。<br>
<br>
当然，这种情况一般不太多。因为每个游戏都会有自己特定的需求，有些游戏的角色甚至都不是传统意义上的人头。所以更常见的一种生成方式，是对项目组的模型进行自动批量变形。简单来说，就是把我们生成的模型相对于平均脸的变化，迁移到项目组的模型上面。这种迁移的变化可以是表情，可以是脸型，并且所有变形都可以用项目规定的骨骼蒙皮进行表达。<br>
<br>
<div align="center">
<img aid="1036937" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092039klgr55vl5m8rm2xm.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092039klgr55vl5m8rm2xm.jpg" width="600" id="aimg_1036937" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092039klgr55vl5m8rm2xm.jpg" referrerpolicy="no-referrer">
</div><br>
这是一组我们生成的结果，最左边是项目组提供给我们的角色模型。我们可以根据这个模型自动批量生成一批风格相同，但脸型和五官有明显区别的模型，并且每个模型都可以生成一套表情。也就是说，项目组只需要做一个静态模型，我们就能自动批量生成很多绑定好的模型。这对追求千人千面的开放世界游戏非常有价值，可以以非常低的成本让游戏里的每个NPC看起来都不一样。<br>
<br>
<div align="center">
<img aid="1036938" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092039us5osc1yhs57d2ag.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092039us5osc1yhs57d2ag.jpg" width="600" id="aimg_1036938" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092039us5osc1yhs57d2ag.jpg" referrerpolicy="no-referrer">
</div><br>
这是我们对两个Metahuman模型变形后的效果，可以看到我们生成人头模型与原始的资源标准是完全兼容的。而且以这个变形质量生成的模型，作为实际游戏的头模也绰绰有余，大家要知道，像Metahuman这种级别的模型，一个头的成本，保守一点计算都要小几十万人民币，所以这个技术是非常有价值的。<br>
<br>
为了进一步丰富我们的三维人头数据，我们也在杭州园区设计和搭建了一套三维扫描实验室。左边是我们的设计图，右边是搭建完成后的实物。这是一个正20面体，一共包含53台单反和150组定制LED灯光。后续我们还会在网易的广州和上海园区，分别搭建一套更大的，可以扫描全身的设备。<br>
<br>
<div align="center">
<img aid="1036939" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092039mmwljot51i955ltl.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092039mmwljot51i955ltl.jpg" width="600" id="aimg_1036939" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092039mmwljot51i955ltl.jpg" referrerpolicy="no-referrer">
</div><br>
三维扫描的原理其实非常简单——利用摄影测量算法，从多视角照片中计算人头的三维点云。这是我们系统扫描的一组样例，这个精度可以对标国内外一线扫描服务供应商。<br>
<br>
<div align="center">
<img aid="1036946" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092618p8xolgwxnb4b73mo.gif" data-original="https://di.gameres.com/attachment/forum/202204/20/092618p8xolgwxnb4b73mo.gif" width="600" id="aimg_1036946" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092618p8xolgwxnb4b73mo.gif" referrerpolicy="no-referrer">
</div><br>
这是基于我们扫描流程制作的一组表情基的效果，可以看到，扫描模型对演员面部细节的还原程度是非常高的。<br>
<br>
这套设备150组定制的LED灯光，也是我们花很高成本定做的。每一盏灯的开关和亮度可以独立控制，每一组灯光包含三个灯头，分别安装了一个普通无偏振的UV镜和两个偏振镜。这两个偏振镜相对于相机上安装的偏振镜方向一个是平行的，一个是垂直的。<br>
<br>
<div align="center">
<img aid="1036940" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092040f3k3zwezqk9kqs18.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092040f3k3zwezqk9kqs18.jpg" width="341" id="aimg_1036940" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092040f3k3zwezqk9kqs18.jpg" referrerpolicy="no-referrer">
</div><br>
了解摄影的同学应该很熟悉偏振镜的用法，这是一种很常用的UV镜，主要用于非金属物体表面一些不必要的反射光，可以还原物体本身的颜色。<br>
<br>
<div align="center">
<img aid="1036941" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092040awyldim3wruproo7.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092040awyldim3wruproo7.jpg" width="600" id="aimg_1036941" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092040awyldim3wruproo7.jpg" referrerpolicy="no-referrer">
</div><br>
偏振镜的原理大家在中学物理就学过——光既是粒子、也是一种电磁波，它的振动方向与传播方向是垂直的，这种类型的波叫横波，所有的横波都具有偏振现象。简单来讲，光的偏振方向与偏振镜方向平行，那么所有能量都会通过；如果是垂直的，那么所有能量都会被过滤。<br>
<br>
基于这个原理，我们只要给扫描物体拍摄4组平行偏振光和4组交叉偏振光的灯光下照片，就可以算出物体表面的材质，也就是漫反射、高光和法线的信息。每组照片都要首先打开所有灯光，然后是按照灯光在三维空间的坐标值递减亮度，XYZ三个方向分别可以产生一组灯光。<br>
<br>
<div align="center">
<img aid="1036942" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092040g9hgp1ii63i00gp1.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092040g9hgp1ii63i00gp1.jpg" width="600" id="aimg_1036942" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092040g9hgp1ii63i00gp1.jpg" referrerpolicy="no-referrer">
</div><br>
目前这套设备我们刚刚搭建完成，在人脸材质扫描方面也是刚刚起步，后续我们会逐渐加大投入。<br>
<br>
<strong><font color="#de5650">近几年工作的重心：动画</font></strong><br>
<br>
最后是动画部分，这是我们这几年工作的重心。前面提到，游戏研发总成本的大头一般是美术资产，那么美术资产成本的大头一般就是动画。因为原画、模型虽然也很贵，但大部分属于一次性开销，而动画则需要配合剧情持续产出，且高质量动画一分钟的制作成本很轻松就可以过万。<br>
<br>
在这方面，我们首先在光学动捕数据的清洗方面做了一些工作。光学动捕会在紧身动捕服表面设置很多标记点，通过多视角红外相机跟踪这些点的坐标，并算出人体骨骼的旋转、平移信息。当然，这些数据不可避免会有错误，所以会有专人负责清洗标记点。<br>
<br>
资深的动捕美术直接看标记点的轨迹曲线，就能知道出现了什么错误、怎么修改，这也是目前动捕工作流中主要的人工工作量。<br>
<br>
2018年，育碧提出了一种通过AI模型来取代这个过程的算法，发表在了SIGGRAPH上；2019年，网易投资了一家法国3A游戏工作室Quantic Dream，也就是《底特律：变人》的研发商。当时我们开始有一些技术合作，他们提出需求后，我们跟进了相关研究。一年多之后，我们找到了一种精度更高的解决方案，也发表在了SIGGRAPH上。<br>
<br>
<div align="center">
<img aid="1036947" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092619v22cfqbxcmm5jq4b.gif" data-original="https://di.gameres.com/attachment/forum/202204/20/092619v22cfqbxcmm5jq4b.gif" width="418" id="aimg_1036947" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092619v22cfqbxcmm5jq4b.gif" referrerpolicy="no-referrer">
</div><br>
目前我们已经把这套算法，以vicon软件的插件形式部署在了网易互娱和Quantic Dream的动捕工作流中。这里是一个例子：这是原始含噪音的标记点，闪来闪去的就是局部噪音，留在原地的就是跟丢的那些点，这是暂时调用我们算法得到的清洗结果。<br>
<br>
接下来介绍几个我们部门落地最多的项目：首先是一套基于普通单目摄像头的轻量级面部动捕系统，基本原理就是利用前面的三维参数化人脸模型，对视频中演员的脸型、表情头部姿态进行回归，把回归得到的系数重定向到游戏角色上。<br>
<br>
<div align="center">
<img aid="1036948" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092619wfes5fe6nf5cca9s.gif" data-original="https://di.gameres.com/attachment/forum/202204/20/092619wfes5fe6nf5cca9s.gif" width="600" id="aimg_1036948" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092619wfes5fe6nf5cca9s.gif" referrerpolicy="no-referrer">
</div><br>
当然，我们也会配合一些CV检测和识别模型，加强算法对眨眼、视线、舌头和整体情绪的捕捉精度。这个项目我们从2018年开始做，前前后后差不多有十位同事参与。其中所有算法模块都是我们自己开发，打磨到现在已经是一套非常成熟的in-house面部动捕解决方案。<br>
<br>
围绕这套算法，我们还打造了一整套工具链，有实时的动捕预览工具，有针对动捕结果进行离线调整和编辑的工具，还有Maya/Max里的动捕数据重定向插件。另外为了方便项目组接入面部动捕系统，我们还开发了一套专门适配自家算法的面部自动绑定插件。此外，核心算法我们还打包了全平台的SDK，在iPhones 6s以上的机器，可以做到单核单线程实时。<br>
<br>
<div align="center">
<img aid="1036943" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092040xc1nft53qh33qtnq.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092040xc1nft53qh33qtnq.jpg" width="600" id="aimg_1036943" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092040xc1nft53qh33qtnq.jpg" referrerpolicy="no-referrer">
</div><br>
这套系统在游戏里有非常多的应用场景，首先就是辅助动画师制作正式的游戏动画资源。相比于传统一帧一帧手key，采用动捕方案的制作效率有明显优势。而且只要演员表演到位，效果跟美术手key几乎看不出来区别；<br>
<br>
其次，它可以给营销同学快速产出一些面部动画素材，营销场景的特点是精度要求没那么高，但时效性要求很高，因为慢了就跟不上实时热点了。我们这种轻量级方案非常适合这种场景，比如某段短视频火了，用这套工具可以快速产出面部动画素材；<br>
<br>
另外，因为我们的算法会提供全平台SDK，所以也可以打包在游戏客户端里，给玩家提供一些UGC玩法。比如我们在《一梦江湖》里上线的颜艺系统，可以让玩家录制自己的表情动画。右上是我在B站上找到的一个视频——玩家录制的打哈欠动画；<br>
<br>
<div align="center">
<img aid="1036949" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092620bn8nzs3gkeh8iiik.gif" data-original="https://di.gameres.com/attachment/forum/202204/20/092620bn8nzs3gkeh8iiik.gif" width="480" id="aimg_1036949" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092620bn8nzs3gkeh8iiik.gif" referrerpolicy="no-referrer">
</div><br>
最后，这套算法还可以支持一些虚拟主播场景，比如《第五人格》秃秃杯电竞比赛的虚拟解说、云音乐look直播的虚拟主播，用的都是我们这套技术。<br>
<br>
另外，我们还配合高精度三维扫描设备，测试了面部动捕算法在超写实模型上的效果。我们雇了一位国外模特扫描模型，用模特录制的视频来驱动他对应的角色，以便更好地对比表情还原度。<br>
<br>
<div align="center">
<img aid="1036950" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092620odrrx25q96xh32r2.gif" data-original="https://di.gameres.com/attachment/forum/202204/20/092620odrrx25q96xh32r2.gif" width="600" id="aimg_1036950" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092620odrrx25q96xh32r2.gif" referrerpolicy="no-referrer">
</div><br>
还有另外一组效果，这位模特是我们部门的一位同事。从效果上可以看到，不管是扫描重建还是面部捕捉，我们的技术都足够支持这种高精度场景。<br>
<br>
跟面部动捕类似，我们也做了一套轻量级基于普通摄像头的身体动捕系统，支持单视角、多视角输入，原理类似于前面的面部捕捉，同样也会配合一些CV模型提升优化结果的合理性。这个项目我们打磨了两年时间，目前效果和稳定性都相当不错。<br>
<br>
<div align="center">
<img aid="1036951" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092620ocir6czayqhxinq7.gif" data-original="https://di.gameres.com/attachment/forum/202204/20/092620ocir6czayqhxinq7.gif" width="600" id="aimg_1036951" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092620ocir6czayqhxinq7.gif" referrerpolicy="no-referrer">
</div><br>
这是在冬奥结束之后，我们用这项技术为《哈利波特：魔法觉醒》项目制作的视频，当时很快就冲上了微博热搜。如果按传统制作方式，这种营销策划案是不太可能实现的，因为要找到能还原这套动作的演员，还要约演员和动捕棚的档期，一套下来没有六位数开销和一个多月制作周期的话，是很难完成的。但是用这套AI方案，成本就可以忽略不计。<br>
<br>
<div align="center">
<img aid="1036952" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092621pauo7lz447l5eo24.gif" data-original="https://di.gameres.com/attachment/forum/202204/20/092621pauo7lz447l5eo24.gif" width="480" id="aimg_1036952" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092621pauo7lz447l5eo24.gif" referrerpolicy="no-referrer">
</div><br>
这是更早时候，我们与《大话西游》项目组合作的一段视频。当时请了B站舞蹈区的一位知名Up主，用三部手机录了这套舞蹈动作，用我们的动捕算法得出数据，重定向到《大话西游》的角色上。<br>
<br>
<div align="center">
<img aid="1036944" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092041pkxgiiz05zqxiikk.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092041pkxgiiz05zqxiikk.jpg" width="600" id="aimg_1036944" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092041pkxgiiz05zqxiikk.jpg" referrerpolicy="no-referrer">
</div><br>
另外，我们还为《明日之后》项目组制作了一些动画素材，只用了一个单目摄像头捕捉身体和面部动作，并且只要拍得足够清晰，手指动作也可以准确捕捉。<br>
<br>
<div align="center">
<img aid="1036953" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092621r3nzey3g33e699y9.gif" data-original="https://di.gameres.com/attachment/forum/202204/20/092621r3nzey3g33e699y9.gif" width="480" id="aimg_1036953" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092621r3nzey3g33e699y9.gif" referrerpolicy="no-referrer">
</div><br>
除了基于视频输入以外，我们还做了基于音频输入生成动画的技术，比如从语音输入生成角色面部和肢体动画的工具链。这项技术我们在2018年就已经应用于不少游戏，当时做得还比较简单，只支持口型和几种简单的基础情绪。后来我们做了持续的基础升级和迭代，增加了语音驱动头动、眼动、手动、面部微表情，还有肢体动作等等。<br>
<br>
另一个从音频输入生成动画的工作，是基于音乐生成舞蹈动作。这项工作我们从2018年开始研究，经过几年迭代最终形成了一套方案，详细的技术方案在论文里有介绍，这里主要展示实际落地效果：首先是二次元女团舞；<br>
<br>
<div align="center">
<img aid="1036954" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092625w242a022jbpvorac.gif" data-original="https://di.gameres.com/attachment/forum/202204/20/092625w242a022jbpvorac.gif" width="480" id="aimg_1036954" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092625w242a022jbpvorac.gif" referrerpolicy="no-referrer">
</div><br>
这是一段韩舞的动画，也是网易CC直播年度盛典的开场舞蹈。<br>
<br>
<div align="center">
<img aid="1036945" zoomfile="https://di.gameres.com/attachment/forum/202204/20/092041diuuu1lexme9lem8.jpg" data-original="https://di.gameres.com/attachment/forum/202204/20/092041diuuu1lexme9lem8.jpg" width="600" id="aimg_1036945" inpost="1" src="https://di.gameres.com/attachment/forum/202204/20/092041diuuu1lexme9lem8.jpg" referrerpolicy="no-referrer">
</div><br>
另外，我们也会用一些网络热门歌曲合成舞蹈。去年圣诞节时，我们用虚拟偶像I.F.制作的B站互动视频，其中所有动画都是通过AI技术生成的。目前这套AI动画的解决方案已经相当成熟，在内部经过了大量项目的验证，目前也在持续为网易的各个项目组输出动作资源。<br>
<br>
<strong><font color="#de5650">数据是AI的核心</font></strong><br>
<br>
最后简单总结一下，从前面的介绍中大家可以发现，AI技术对程序化美术资源生成能产生明显的促进作用。而且根据我们的实践经验，在人脸、人体的模型和动画方面，它甚至可以在一定程度上取代一些初级执行向美术的工作。而且利用我们的AI方案，普遍可以比传统方案提升5-10倍的制作效率。<br>
<br>
但目前想让AI从事一些更高级的工作还比较困难。主要难点是高质量数据比较稀缺，大家都知道数据是AI的核心，AI模型有多少能力，很大程度上取决于人给了模型多少有价值的数据。但是游戏资产的获取门槛还是很高的，这跟照片、语音、文字这种所有人日常都在生产的数据不太一样。<br>
<br>
比如在某个景点看到一个很有特色的雕塑，绝大部分人的反应可能是掏出手机，拍一张照片记录一下，但几乎不会有人掏出电脑现场建个模。当然，随着技术进步，游戏资源的制作门槛肯定会越来越低，而且像元宇宙这样的热门应用场景，本身也要求游戏厂商让广大玩家参与到虚拟世界的内容创造过程中来。<br>
<br>
所以我相信，随着数据的持续积累，未来AI技术也有可能从事一些更高级的工作，这也是我们的努力方向，谢谢大家。<br>
<br>
N.GAME是由网易互娱学习发展举办的一年一度行业交流盛事，至今已成功举办七届。本届主题为“未来已来The Futureis Now”，邀请了20位海内外重磅嘉宾、高校学者汇聚一堂，共享行业研发经验、前沿研究成果和未来发展趋势。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<br>
  
</div>
            