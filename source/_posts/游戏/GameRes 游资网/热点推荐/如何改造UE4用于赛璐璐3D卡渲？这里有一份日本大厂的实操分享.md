
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
此外，高光（镜面反射光）要素也进行了一系列的特殊处理，其中最明显的就是头发。高光处理时，首先生成一张将Blinn-Phong模型二值化以后的高光遮罩，紧贴在高光出现的部位。头发中间部分的高光偏圆偏小，周边部分的则是偏细长。这些形状差异，是根据相对物件重心的距离，来扩大或缩小高光遮罩而实现的。<br><br><div align="center">
<img id="aimg_1010661" aid="1010661" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142559lqqzn8a3xnhjkghx.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142559lqqzn8a3xnhjkghx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142559lqqzn8a3xnhjkghx.jpg" referrerpolicy="no-referrer">
</div>
<br>
需要注意的是，即便角色的轮廓没有逆光，也需要加上边缘光的处理，来强化与背景分开的立体感。边缘光的处理，是基于深度buffer的内容用Sobel filter提取出边缘数据，然后加强其亮度。不过这种做法需要追加一条渲染管线。<br><br>
另外在filter的阶段，通过offset可以调节轮廓线的粗细，也能顺着轮廓添加边缘光。而且在不希望出现边缘光的地方（比如因为角色背部的光源生成阴影的地方等），还可以实施进一步的遮罩处理。<br><br><div align="center">
<img id="aimg_1010662" aid="1010662" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142559ph955a55tkbl7clh.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142559ph955a55tkbl7clh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142559ph955a55tkbl7clh.jpg" referrerpolicy="no-referrer">
</div>
<div align="center">
<img id="aimg_1010663" aid="1010663" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142559qxx3a7yb3rbrbufu.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142559qxx3a7yb3rbrbufu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142559qxx3a7yb3rbrbufu.jpg" referrerpolicy="no-referrer">
</div>
<br><strong><font color="#de5650">02：轮廓线的处理</font></strong><br><br>
轮廓线在动画风当中占据了相当重要的位置，它的处理也需要下功夫。<br><br>
轮廓线的处理是依靠深度值进行判定，然后通过Sobel filter检测边缘部分，在深度值较大的一侧绘制轮廓线。角色数据中，顶点色2是轮廓线使用的数据，其中通过ID编排，存放了不同部位、不同粗细的数据，在绘制轮廓线的时候会被使用。在面部这类不希望出现轮廓线的地方，可以调整深度值，让它更不容易呈现出轮廓线。<br><br><div align="center">
<img id="aimg_1010664" aid="1010664" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142600no5c65c3lfdzrr9i.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142600no5c65c3lfdzrr9i.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142600no5c65c3lfdzrr9i.jpg" referrerpolicy="no-referrer">
</div>
<br>
通过反转深度值就可以指定不希望出现轮廓线的位置了。<br><br><div align="center">
<img id="aimg_1010665" aid="1010665" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142600g93fovz71evvwv5f.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142600g93fovz71evvwv5f.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142600g93fovz71evvwv5f.jpg" referrerpolicy="no-referrer">
</div>
<br>
值得注意的是，轮廓线可以想象成在角色的外侧进行了绘制。这是因为当画面太小时，如果在物件内部绘制轮廓线，会让物件看起来更小。<br><br>
此外，前面提到的部件ID也会在物件边界部分的轮廓线上进行计算，即通过ID检测出边缘，然后在深度值较大一侧绘制轮廓线。<br><br>
而在手指等深度值相差较小的，很难分配ID的部位，就需要使用通过法线来判断轮廓线的方法。同时，手绘法线也在事先准备好了，这里也会合成这方面的数据。<br><br><div align="center">
<img id="aimg_1010666" aid="1010666" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142600nppvhavuihhihpsp.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142600nppvhavuihhihpsp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142600nppvhavuihhihpsp.jpg" referrerpolicy="no-referrer">
</div>
<div align="center">
<img id="aimg_1010667" aid="1010667" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142600lwp2rwwwo8r8w6tw.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142600lwp2rwwwo8r8w6tw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142600lwp2rwwwo8r8w6tw.jpg" referrerpolicy="no-referrer">
</div>
<br>
《蓝色协议》的角色还会表现出动画、原画中常见的，眉毛呈现在头发上面的效果，这是模拟透过头发看见眉毛的效果。技术上，则是先制作一张眉毛形状的遮罩，防止头发覆盖眉毛的处理手法。换句话说，单纯为了这个效果，就追加了一层渲染管线。<br><br><div align="center">
<img id="aimg_1010668" aid="1010668" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142601jby5q0060xpqfx0a.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142601jby5q0060xpqfx0a.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142601jby5q0060xpqfx0a.jpg" referrerpolicy="no-referrer">
</div>
<br>
除此之外，轮廓线对Temporal AA的兼容性不好，容易被模糊处理，所以需要使用Responsive AA的抗锯齿处理。Responsive AA会使用模板，尽可能保持现在的图像轮廓，再实现一个类似Temporal AA的效果，尽管抗锯齿效果会偏弱，但对于张力比较强的图像来说，这种效果反而更好。<br><br><div align="center">
<img id="aimg_1010669" aid="1010669" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142601stxztf3uh7h822i2.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142601stxztf3uh7h822i2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142601stxztf3uh7h822i2.jpg" referrerpolicy="no-referrer">
</div>
<br>
另外外部物件的阴影有时也会落到角色身上，但除了面部阴影以外的不会使用到角色的selfshadow，所以处理角色的shadow map（比如落到地面上的阴影）时，只使用角色自身的影子。<br><br>
不过，游戏使用了一些类似selfshadow的表现来作为代替。即使用offsetshadow比较临近物体的深度数据和通常画像的深度数据，然后写入一张用来区分基本色和阴影色的二值化buffer。这样一来阴影部分就会扩散开来。<br><br><div align="center">
<img id="aimg_1010670" aid="1010670" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142601ruz53ldto3o83blr.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142601ruz53ldto3o83blr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142601ruz53ldto3o83blr.jpg" referrerpolicy="no-referrer">
</div>
<div align="center">
<img id="aimg_1010671" aid="1010671" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142602enud7f66yd6lu73p.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142602enud7f66yd6lu73p.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142602enud7f66yd6lu73p.jpg" referrerpolicy="no-referrer">
</div>
<br>
最后用diffuse后处理，使明亮部分进行扩散，这个功能也可以用Bloom代替，但是会与特效部分的Bloom处理冲突，所以项目组最后选择在另一边使用这个功能。<br><br><div align="center">
<img id="aimg_1010672" aid="1010672" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142602i3p5zp4pk2a8taka.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142602i3p5zp4pk2a8taka.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142602i3p5zp4pk2a8taka.jpg" referrerpolicy="no-referrer">
</div>
<br>
进行这一连串的处理之后，《蓝色协议》的3D赛璐璐风就实现了出来。当然，这也是在原本的UE4的渲染管线之上，追加了多层处理工序，deferred rendering的6个G-buffer几乎所有通道都被用上了。在大井隆義看来，要做好赛璐璐动画风格的3D渲染，绝对不是一件处理起来比较简单的事情。<br><br><div align="center">
<img id="aimg_1010673" aid="1010673" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142602o3m1o441d442w89o.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142602o3m1o441d442w89o.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142602o3m1o441d442w89o.jpg" referrerpolicy="no-referrer">
</div>
<div align="center">
<img id="aimg_1010674" aid="1010674" zoomfile="https://di.gameres.com/attachment/forum/202109/23/142602y5rf6mmark6ax03f.jpg" data-original="https://di.gameres.com/attachment/forum/202109/23/142602y5rf6mmark6ax03f.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/23/142602y5rf6mmark6ax03f.jpg" referrerpolicy="no-referrer">
</div>
<br>
万代南梦宫Studio这次针对UE4引擎的改造，基本都是集中在渲染通道的追加上，除此之外的引擎升级问题算是勉强处理完了。而这些改造比起追求物理的真实性，更倾向于实现创作者的想法和追求。「如果这么改动，会不会更有感觉？」这种不断探求的欲望，是大井隆義认为最重要的思考。<br><br><strong><font color="#de5650">03：结语</font></strong><br><br>
在葡萄君的上一篇文章中提到过这个产品的技术探索思路：用大量细节的打磨，去摸索制作组最希望达到的效果。<br><br>
这决定了《蓝色协议》不会简单套用市面上某个模板，其实不难发现，自《蓝色协议》曝光以来的两年里，这款产品细微处的技术手法一直有不小的变化，我也很想看看最终这款产品会变成什么样，拿出什么级别的技术呈现。<br><br>
而每次看到类似的技术分享，葡萄君都会忍不住期待一下，3D卡渲已经成为标配和竞争入场券的国内市场里，什么时候会迎来风格与细节技术明显分化的产品浪潮。也希望在这个浪潮到来之前，这类技术分享能为开发者提供一些不同的思路。<br><br>
文章来源：<br><br>
https://www.4gamer.net/games/467/G046741/20210826001/<br><br>
游戏葡萄编译整理<br><font size="2"><br></font><br><font size="2"></font><br><font size="2">来源： 游戏葡萄</font><br><font size="2">原文：https://mp.weixin.qq.com/s/hbsC-stlRyfOgTYX7P6Msg</font><br><br><br>
</td></tr></tbody></table>


  
</div>
            