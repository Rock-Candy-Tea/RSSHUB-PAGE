
---
title: '探索用Figma做游戏UI设计'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202208/12/112004fv7vnx88gkoc2r2i.png'
author: GameRes 游资网
comments: false
date: Fri, 12 Aug 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202208/12/112004fv7vnx88gkoc2r2i.png'
---

<div>   
<strong><font color="#de5650">前言</font></strong><br>
<br>
Figma本身是一个矢量设计软件，所以个人认为Figma比较适用于制作一些偏扁平、卡通的游戏UI风格。纵观全网Figma基本都是To B 、To C类的产品应用，很少人会往这个游戏这个方向研究了，因此我开启了一段Figma针对扁平类游戏UI设计的探索之旅，结合Figma Config 2022姗姗来迟的AutoLayout 4.0的使用，以英雄联盟鲜明的海克斯科技风格代表性更高。(以下案例仅为个人示范，与官方产品效果及资源无关)<br>
<br>
<div align="center">
<img aid="1049877" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112004fv7vnx88gkoc2r2i.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112004fv7vnx88gkoc2r2i.png" width="600" id="aimg_1049877" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112004fv7vnx88gkoc2r2i.png" referrerpolicy="no-referrer">
</div><br>
此次练习设计主要总结了一些设计技巧：<br>
<br>
异形的自适应按钮、自适应面板背景（AL4.0绝对定位+约束拉伸）<br>
<br>
 数字、字母动画（AfterDelay嵌套）<br>
<br>
<strong><font color="#de5650">01/ 异形按钮的做法</font></strong><br>
<br>
起初一个同事在大群里问，像这种异形的渐变按钮在Figma里面做Autolayout组件吗？<br>
<br>
<div align="center">
<img aid="1049884" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112013u5qfc9i0j4v94dtc.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112013u5qfc9i0j4v94dtc.png" width="600" id="aimg_1049884" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112013u5qfc9i0j4v94dtc.png" referrerpolicy="no-referrer">
</div><br>
由于当时正在使用skewDat插件。于是就想到两种解决办法：<br>
<br>
对文本Autolayout之后，Autolayout层用skewDat插件倾斜 -10度，再对里面的文字倾斜10度，就得到了（负负得正）。<br>
<br>
把两边异形的部分单独抽出来，中间部分就可以做自适应。<br>
<br>
<div align="center">
<img aid="1049885" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112020nijtjpxjoizjo8oe.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112020nijtjpxjoizjo8oe.png" width="600" id="aimg_1049885" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112020nijtjpxjoizjo8oe.png" referrerpolicy="no-referrer">
</div><br>
但其实以上两种方法，都会有一些问题：<br>
<br>
尺寸上会有小数点，不够精确（像素控感到难受）<br>
<br>
不能做不规则渐变填充（45度、角度渐变等）<br>
<br>
 不能给整个形状增加描边（如上图最后一个按钮）<br>
<br>
文字不能入侵到异形部分<br>
<br>
后来，在不断的实践过程中也发现了基于Autolayout 3.0更优的解法，类似于做点9图的效果得到更好的设计延展（限高，宽度自适应/限宽，高度自适应）。在AutoLayout4.0发布后，这个方法有了绝对定位的加持，实现变得更容易了(宽高可自适应)。<br>
<br>
<strong><font color="#de5650">02/ 异形设计的自适应</font></strong><br>
<br>
在大多数To B 、To C的应用场景中，常规的按钮如纯色、渐变、幽灵、投影/发光按钮+各种直角、圆角、全圆角，AutoLayout都能轻松的完成自适应。<br>
<br>
但在游戏设计中，按钮的背景一般都不会做的规矩和太扁平，总会做一些和游戏主题匹配的样式，会有一些特殊的异形装饰，类似海克斯科技里除了常规的矩形按钮，还有被圆和三角形切割的异形按钮，因此也特意用Figma做了一些比较知名的游戏按钮来做验证。<br>
<br>
<div align="center">
<img aid="1049867" zoomfile="https://di.gameres.com/attachment/forum/202208/12/111950f5k28zh28h1kspag.png" data-original="https://di.gameres.com/attachment/forum/202208/12/111950f5k28zh28h1kspag.png" width="600" id="aimg_1049867" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/111950f5k28zh28h1kspag.png" referrerpolicy="no-referrer">
</div><div align="center">
<img aid="1049868" zoomfile="https://di.gameres.com/attachment/forum/202208/12/111951cwwb3o5qjmzjqatq.png" data-original="https://di.gameres.com/attachment/forum/202208/12/111951cwwb3o5qjmzjqatq.png" width="600" id="aimg_1049868" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/111951cwwb3o5qjmzjqatq.png" referrerpolicy="no-referrer">
</div><br>
常规按钮：可以拆解成一层文本，和一个填充/渐变层，通过添加Autolayout完美自适应宽高。<br>
<br>
游戏按钮：可以拆解成一层文本，和一个可以自适应拉伸的背景组件，在AutoLayout 4.0 后也能完美地自适应宽高。<br>
<br>
那具体应该怎样才能做到自适应，同时文字和背景层能很好的分离切换呢？<br>
<br>
<strong><font color="#ffffff"><font style="background-color:darkred">2.1 AL3.0 & 4.0 中的实现原理</font></font></strong><br>
<br>
其实早期在Figma官方介绍Autolayout 3.0的Playground文件中，就隐藏了一种思路：<br>
<br>
<div align="center">
<img aid="1049869" zoomfile="https://di.gameres.com/attachment/forum/202208/12/111952qcjyk8o1ffczgk12.png" data-original="https://di.gameres.com/attachment/forum/202208/12/111952qcjyk8o1ffczgk12.png" width="600" id="aimg_1049869" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/111952qcjyk8o1ffczgk12.png" referrerpolicy="no-referrer">
</div><br>
仔细观察这几个头像，通过父级定宽FixedWidth + Autolayout + SpaceBetween的方法，因此我们按钮还是拆成一个文本结构层、一个背景拉伸层，并且一般按钮来说都是定高的，只需要水平自适应文本长度。借助这个点，结合Autolayout的Spaces Between 来完成按钮和背景重叠一起的效果。<br>
<br>
<strong><font color="#ffffff"><font style="background-color:darkred">2.2 AutoLayout 4.0+组件属性</font></font></strong><br>
<br>
得益于负间距、绝对定位、堆叠顺序、组件属性的特性，可以省略一层文本结构层，通过组件属性直接赋能在主按钮上。背景层的处理使用绝对定位，以及约束填满整个按钮的大小，这样就可以轻松实现宽高自适应的按钮背景了。<br>
<br>
剩下的重点是制作出 可自适应拉伸的按钮背景图层 即可。<br>
<br>
<strong><font color="#ffffff"><font style="background-color:darkred">2.3 自适应拉伸核心细节</font></font></strong><br>
<br>
Figma中做自适应拉伸主要使用约束Constraints的Top、Bottom、Left 、Right和Top&Bottom、Left&Right进行定位以及布尔运算的Union、Subtract进行加减运算，这样出的图像既能够自适应拉伸，也能够保持一个整体同时方便调整样式。<br>
<br>
最终的效果类似CSS3 Border-Image 边框图像、Android 的 9-patch 拉伸图、iOS的Slicing 拉伸、Flutter的centerSlice。<br>
<br>
<div align="center">
<img aid="1049870" zoomfile="https://di.gameres.com/attachment/forum/202208/12/111953a7cr7c1fp14hbwfx.png" data-original="https://di.gameres.com/attachment/forum/202208/12/111953a7cr7c1fp14hbwfx.png" width="600" id="aimg_1049870" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/111953a7cr7c1fp14hbwfx.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#ffffff"><font style="background-color:darkred">2.4 按钮重叠核心细节</font></font></strong><br>
<br>
<strong> 文本结构层：</strong>文本图标层可以建立不同的Variants+Autolayout，来实现切换纯文、左图标+文本、文本+右图标等多种方式。（Autolayout 3）<br>
<br>
<div align="center">
<img aid="1049871" zoomfile="https://di.gameres.com/attachment/forum/202208/12/111954bo5duyy04dqhtdut.png" data-original="https://di.gameres.com/attachment/forum/202208/12/111954bo5duyy04dqhtdut.png" width="600" id="aimg_1049871" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/111954bo5duyy04dqhtdut.png" referrerpolicy="no-referrer">
</div><br>
当然也可以使用AutoLayout 4 通过添加组件属性，一个组件就能完成。<br>
<br>
<div align="center">
<img aid="1049872" zoomfile="https://di.gameres.com/attachment/forum/202208/12/111954rjmhhpn77dh7j1hj.png" data-original="https://di.gameres.com/attachment/forum/202208/12/111954rjmhhpn77dh7j1hj.png" width="600" id="aimg_1049872" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/111954rjmhhpn77dh7j1hj.png" referrerpolicy="no-referrer">
</div><br>
<strong>按钮背景层：</strong>背景层内的元素注意使用约束Constraints的Left & Right和Top & Bottom。如果有多个按钮背景层做切换 ，也可以使用Variants。<br>
<br>
<div align="center">
<img aid="1049873" zoomfile="https://di.gameres.com/attachment/forum/202208/12/111955m5mnmnoo9dgnfotx.png" data-original="https://di.gameres.com/attachment/forum/202208/12/111955m5mnmnoo9dgnfotx.png" width="600" id="aimg_1049873" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/111955m5mnmnoo9dgnfotx.png" referrerpolicy="no-referrer">
</div><br>
<strong> 整体按钮AL3.0：</strong>做水平自适应按钮，使用垂直方向的AutoLayout，间距设置Auto即为Spaces Between效果，Padding设为0。(垂直自适应按钮，则使用水平方向的AutoLayout，宽度设置为固定宽度。<br>
<br>
整体按钮宽度设为Hug Contents ，高度均需设为按钮的固定高度如32。<br>
<br>
 文本结构层BtnText的Resizing宽度设置Hug Contents或Fill Container用于Padding调整左右边距，高度同整体按钮。<br>
<br>
按钮背景层BtnBg的Resizing宽度设置Fill Container用于自适应拉伸宽度，高度同整体按钮。<br>
<br>
注：如果出现背景层盖住了文本层，交换一下图层顺序即可。<br>
<br>
<div align="center">
<img aid="1049874" zoomfile="https://di.gameres.com/attachment/forum/202208/12/111955bf7za5dzaabbkfiq.png" data-original="https://di.gameres.com/attachment/forum/202208/12/111955bf7za5dzaabbkfiq.png" width="600" id="aimg_1049874" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/111955bf7za5dzaabbkfiq.png" referrerpolicy="no-referrer">
</div><br>
<strong>整体按钮AL4.0：</strong>嵌套一层父级AutoLayout，Padding可以用于方便调整文本层和背景层之间的内填充。<br>
<br>
其中文本结构层BtnText的Resizing宽度设置为Hug Contents，Hug Contents，这样按钮可以单行或多行自适应。<br>
<br>
背图层设置为绝对定位，宽高同父级AutoLayout，并且设置约束Constraints的Left & Right和Top & Bottom，这样就可以完美自适应宽高。<br>
<br>
注：如果出现背景层盖住了文本层，交换一下图层顺序即可，或者在AL更多设置中调整CanvasStacking的顺序。<br>
<br>
<div align="center">
<img aid="1049875" zoomfile="https://di.gameres.com/attachment/forum/202208/12/111956ifsr44ef6888yfri.png" data-original="https://di.gameres.com/attachment/forum/202208/12/111956ifsr44ef6888yfri.png" width="600" id="aimg_1049875" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/111956ifsr44ef6888yfri.png" referrerpolicy="no-referrer">
</div><div align="center">
<img aid="1049886" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112452kql3bjkqa1jq6hlo.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112452kql3bjkqa1jq6hlo.png" width="600" id="aimg_1049886" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112452kql3bjkqa1jq6hlo.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#ffffff"><font style="background-color:darkred">2.5 虚化蒙版细节</font></font></strong><br>
<br>
细心的同学会发现LOL这个Play按钮在hover的时候，会有一些朦胧的烟雾流动效果。这个核心的细节点主要是把遮罩的描边图层加一层LayerBlur，这样作为蒙版的时候就能有类似PS的虚化效果。<br>
<br>
<strong><font color="#ffffff"><font style="background-color:darkred">2.6 自适应面板背景</font></font></strong><br>
<br>
在游戏设计中，弹窗面板一般都是固定几个大中小尺寸的，这样方便统一。从截图可以看出，LOL手游中基本上也就是有大中小三个基础尺寸，也会有做定宽自适应高，定高自适应宽的弹窗。<br>
<br>
<div align="center">
<img aid="1049876" zoomfile="https://di.gameres.com/attachment/forum/202208/12/111959o60u1zy66mrjnm2u.png" data-original="https://di.gameres.com/attachment/forum/202208/12/111959o60u1zy66mrjnm2u.png" width="600" id="aimg_1049876" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/111959o60u1zy66mrjnm2u.png" referrerpolicy="no-referrer">
</div><br>
有了前面的自适应拉伸基础后，其实面板背景就已经学会了，这样就可以很方便地延伸出不同的面板背景。<br>
<br>
<div align="center">
<img aid="1049878" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112005omr6v2ohivmzi5mf.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112005omr6v2ohivmzi5mf.png" width="600" id="aimg_1049878" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112005omr6v2ohivmzi5mf.png" referrerpolicy="no-referrer">
</div><br>
在AL4.0的加强下，这个面板实现更轻松。在对文字内容的AL基础上，只需要给背景设为绝对定位并且设置约束Constraints的Left & Right和Top & Bottom，这样就可以完美自适应宽高。<br>
<br>
<strong><font color="#de5650">03/ 数字、字母动画</font></strong><br>
<br>
在游戏设计中，不乏使用数字增长的效果强调个人资产数据。<br>
<br>
在过去的一些原型动画设计工具如Flinto、Principle都没奢望过能做数字滚动的效果，但Figma不一样，组件内的交互让我有了些想法。那在Figma中应该怎么做呢？<br>
<br>
<strong><font color="#ffffff"><font style="background-color:darkred">3.1 数字滚动动画</font></font></strong><br>
<br>
我们可以简单的分析思路：<br>
<br>
【原子】把0~9，A~Z拆分成独立的原子组件，方便统一管理大小、样式。<br>
<br>
【自循环】把0~9~0，A~Z~A使用AfterDelay建立自循环动画，如每个状态停留100ms，那10个刚好1000ms（1秒）。由于自循环后会直接播放，所以可以给一个【-】作为起始帧，也方便后续调整延迟。<br>
<br>
【输出结果】把自循环动画 → 原子(最终结果)，建立组件集系列。<br>
<br>
<div align="center">
<img aid="1049879" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112007jzkhiguwxw58v5k4.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112007jzkhiguwxw58v5k4.png" width="600" id="aimg_1049879" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112007jzkhiguwxw58v5k4.png" referrerpolicy="no-referrer">
</div><br>
最后在需要的地方直接调用Number to / 具体数系列的组件，在【-】状态分别调整Delay延迟时间，让字母错开完成结束。<br>
<br>
<div align="center">
<img aid="1049880" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112007bl1xx3pqz1t11z18.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112007bl1xx3pqz1t11z18.png" width="600" id="aimg_1049880" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112007bl1xx3pqz1t11z18.png" referrerpolicy="no-referrer">
</div><br>
注意：<br>
<br>
 在原子级组件，建议设置每个组件的宽高一致，因为大部分字体都是非等宽字体，对1、7、E、F、I、J、L、M、W显示的宽度差比较大， 后期对组合结果进行Autolayout排列的时候，非等宽的组件会出现异常，缺失动画。<br>
<br>
 由于Figma会记录元素最终的渲染状态，就会导致数字动画在原型流Prototype Flow里只能播放一次，需要手动按R重置。<br>
<br>
<div align="center">
<img aid="1049881" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112008rm8rbt7rd55drx4x.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112008rm8rbt7rd55drx4x.png" width="600" id="aimg_1049881" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112008rm8rbt7rd55drx4x.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#ffffff"><font style="background-color:darkred">3.2 重复字母翻动动画</font></font></strong><br>
<br>
2021全球总决赛中，有这么一个影视包装设计画面 Make / Break ，那这个效果其实Figma也能轻松实现。<br>
<br>
得益于文本继承的特性，可以只设计一个动画组件就可以完成核心步骤。<br>
<br>
 Start帧，以两行的方式输入同一个字符，勾选ClipContent裁剪超出Frame的内容用于只显示第一行字母，以SmartAnimate切换至End帧。<br>
<br>
End帧，调整位置，显示第二行字母，以 1ms 延迟Instance的方式直接跳转回Start帧。<br>
<br>
最后在调用的时候，调整每个组件的Delay延迟时间，让字母错开播放。<br>
<br>
特别说明的是：这个效果在原型播放约3次以后，会变慢（原因未知）,可以按R来重置效果。<br>
<br>
<div align="center">
<img aid="1049882" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112010oxhhpyhh45kh1dbr.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112010oxhhpyhh45kh1dbr.png" width="600" id="aimg_1049882" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112010oxhhpyhh45kh1dbr.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">04/ 一些期望的Feature</font></strong><br>
<br>
基于上面的讨巧的方法，有了一些大胆的期望：<br>
<br>
 背景图层的填充模式提供一种 类似Slicing的拉伸模式，即可使用轻便的AutoLayout结构自适应宽高拉伸<br>
<br>
<div align="center">
<img aid="1049883" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112011pi07a0750c68rt27.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112011pi07a0750c68rt27.png" width="600" id="aimg_1049883" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112011pi07a0750c68rt27.png" referrerpolicy="no-referrer">
</div><br>
<font size="2"></font><br>
<font size="2">来源：腾讯游戏学堂</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/pF3NIG6lSSEahlZU-OenGA</font><br>
<br>
<br>
  
</div>
            