
---
title: '如何改造UE4用于赛璐璐3D卡渲？这里有一份日本大厂的实操分享'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202109/23/142556yrksxs4dl1r66oyz.jpg'
author: GameRes 游资网
comments: false
date: Thu, 23 Sep 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202109/23/142556yrksxs4dl1r66oyz.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2515355">
<div class="quote"><blockquote>用大量细节的打磨，去摸索制作组最希望达到的效果。</blockquote></div>
<br>
当今市场中，3D卡渲无疑是最热门的一个技术竞争领域，此前也有不少厂商分享了各自基于不同引擎的3D卡渲实现技术。<br><br>
前几个月葡萄君分享了万代南宫旗下一款基于UE4制作的赛璐璐3D卡渲产品《蓝色协议》的技术经验，提及它的风格选择、实现思路，以及相关的基本手法。<br><br>
就在前不久日本举办的CEDEC 2021开发者大会上，万代南梦宫Studio的执行技术总监大井隆義又以《实装篇》为题，进一步分享了《蓝色协议》在实现赛璐璐3D卡渲时，针对UE4引擎进行的技术改造。<br><br><div align="center">
<img id="aimg_1010653" aid="1010653" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142556yrksxs4dl1r66oyz.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142556yrksxs4dl1r66oyz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142556yrksxs4dl1r66oyz.jpg" referrerpolicy="no-referrer">
</div>
<br>
在大井隆義看来，一般的赛璐璐shading手法，要么不使用游戏引擎自带的光照系统，自行处理光照，要么是对引擎渲染出来的画像进行后处理让它看起来有动画的风格。这类手法的参考资料已经非常多了，但不改造引擎的做法有好有坏。<br><br>
比如在UE4当中，不使用光照系统，相当于抛弃了UE4自身画面表现极其丰富的一大特色，转用后处理的做法，又相当于在已经渲染好的东西上再加一层多余的表演处理。于是万代南梦宫Studio尝试的是：如何在不遏制UE4功能的前提下，针对想要实现的渲染效果进行最小限度的引擎改造。<br><strong><font color="#de5650"><br></font></strong><br><strong><font color="#de5650">01：光照的处理</font></strong><br><br>
首先是为了生成阴影的光照处理。在《蓝色协议》中，比较独特的地方是，1个角色模型对应着两种法线数据。其中一种是模型数据自身的法线，另一种则是画师绘制的法线。下图右上是模型法线，右下是手绘法线。<br><br><div align="center">
<img id="aimg_1010654" aid="1010654" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142556pyy3yc5fypypfy5f.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142556pyy3yc5fypypfy5f.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142556pyy3yc5fypypfy5f.jpg" referrerpolicy="no-referrer">
</div>
<br>
直观地对比一下就能看出，模型法线呈现出了3D角色丰富的立体感，而另一套法线看起来就比较糊，尤其是角色面部的细节层次感不强。<br><br>
原因在于，在通常的动画作品中，大多数的角度来看，在光源相反的脸颊边缘，都会以简洁的线条来区分出面部的阴影。而鼻子这类突出的位置，大多数情况都不会重点绘制阴影（具体情况根据画风也有差别）。所以使用相对模糊的法线数据，反而能呈现出更贴近动画风格的阴影表现。<br><br><div align="center">
<img id="aimg_1010655" aid="1010655" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142556r1a2u3nuj6j1jhn1.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142556r1a2u3nuj6j1jhn1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142556r1a2u3nuj6j1jhn1.jpg" referrerpolicy="no-referrer">
</div>
<br>
此外，角色面部还搭在了捏脸功能，总共可以分割为6个部件。如果将这些部件单独计算为一个物件进行输入，每个部件都会呈现出自己的边缘，所以需要将他们囊括为一个整体进行输入，边缘部分的法线才能衔接顺畅。<br><br><div align="center">
<img id="aimg_1010656" aid="1010656" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142557sfzim59b9shis995.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142557sfzim59b9shis995.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142557sfzim59b9shis995.jpg" referrerpolicy="no-referrer">
</div>
<br>
通过手绘法线的数据以及主光源数据，就可以计算出角色的阴影。在《蓝色协议》中用到的皮肤阴影，属于动画术语中的一级阴影。要实现这个效果，首先需要准备一张二值化处理（将图像上的像素点的灰度值设置为0或255，即黑白化）后的遮罩。再保证即便存在再多光源，作用到角色阴影的只有主光源。<br><br><div align="center">
<img id="aimg_1010657" aid="1010657" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142557plft446n36shs3lz.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142557plft446n36shs3lz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142557plft446n36shs3lz.jpg" referrerpolicy="no-referrer">
</div>
<br>
然后用主光源，以及通过手绘法线得到的二值化阴影数据进行对比，在明亮处使用角色基本色，在暗处则使用阴影色来进行着色。这样一来，一个角色的动画式着色就算完成了一大半。其中关键在于角色阴影只受主光源的影响这一点。<br><br><div align="center">
<img id="aimg_1010658" aid="1010658" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142558yws5s3jocoevsgjb.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142558yws5s3jocoevsgjb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142558yws5s3jocoevsgjb.jpg" referrerpolicy="no-referrer">
</div>
<br>
当存在主光源以外的点光源时，为了保证不出现干扰的阴影效果，光照效果需要无视法线只呈现与光源的距离关系。这种情况下，亮度过高的情况会比较常见，所以需要再做调整。下面这张幻灯片也是亮度过高的例子。<br><br><div align="center">
<img id="aimg_1010659" aid="1010659" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142558quuyvkjxgg26g8x0.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142558quuyvkjxgg26g8x0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142558quuyvkjxgg26g8x0.jpg" referrerpolicy="no-referrer">
</div>
<br>
天空光、间接光也是如此，在渲染的时候都会基本无视发法线，这样就可以将外部光的色彩影响控制在最小的范畴内。尽管不是完全没有影响，但这种做法首要考虑的是优先呈现角色自身的颜色。毕竟蓝天背景下，背景求的颜色是蓝色，如果影响到角色也泛蓝，就会显得很奇怪。<br><br><div align="center">
<img id="aimg_1010660" aid="1010660" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142558v4p0qxxe48q9ql47.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142558v4p0qxxe48q9ql47.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142558v4p0qxxe48q9ql47.jpg" referrerpolicy="no-referrer">
</div>
<br>
此外，高光（镜面反射光）要素也进行了一系列的特殊处理，其中最明显的就是头发。高光处理时，首先生成一张将Blinn-Phong模型二值化以后的高光遮罩，紧贴在高光出现的部位。头发中间部分的高光偏圆偏小，周边部分的则是偏细长。这些形状差异，是根据相对物件重心的距离，来扩大或缩小高光</td></tr></tbody></table>
  
</div>
            