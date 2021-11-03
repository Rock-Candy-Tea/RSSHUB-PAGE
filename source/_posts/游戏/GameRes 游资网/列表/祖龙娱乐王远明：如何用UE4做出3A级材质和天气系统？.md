
---
title: '祖龙娱乐王远明：如何用UE4做出3A级材质和天气系统？'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202110/08/112639r4duc66cw6l64340.jpg'
author: GameRes 游资网
comments: false
date: Fri, 08 Oct 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202110/08/112639r4duc66cw6l64340.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2516146">
在近日举行的北京国际游戏创新大会（BIGC 2021）上，来自祖龙娱乐的引擎专家王远明带来了「龙族幻想材质系统优化和在天气系统中的应用」主题分享，以祖龙娱乐旗下手游《龙族幻想》为例子，讲述祖龙娱乐在基于UE4引擎的移动游戏制作过程中，如何对游戏的材质以及天气系统针对移动端进行优化。<br><br><strong>以下是手游那点事整理的演讲实录：</strong><br><br>
同学们下午好。今天我给大家带来的题目是《龙族幻想》材质系统的优化，以及在天气系统中的应用。《龙族幻想》是祖龙娱乐在2019年推出的一款使用UE制作的次世代手机游戏。它也可以说是国内第一款使用UE在手机平台的MMORPG的次世代游戏，同时也证明了UE可以在移动端制作品质非常优秀的游戏。因为它之前的给人印象是优势主要在主机和PC平台。《龙族幻想》充分展示了UE在移动平台也是可以制作出性能优良和画面精美的游戏。<br><br><div align="center">
<img id="aimg_1012907" aid="1012907" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112639r4duc66cw6l64340.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112639r4duc66cw6l64340.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112639r4duc66cw6l64340.jpg" referrerpolicy="no-referrer">
</div>
<br>
所以在这里也借助这个机会，感谢UE的同学给予祖龙娱乐大力的支持，谢谢。今天我的主题分两个方面，第一方面是材质系统优化，第二个方面是天气系统。我今天讲的并不是说如何使用它来制作逼真的天气效果，而是采用一个什么样的方式、利用UE引擎的哪些特性来制作天气系统。<br><br>
可能有些同学没有玩过《龙族幻想》这个游戏，我准备了几段视频来展示游戏效果。给大家放一下。相信大家通过这三个视频，会对《龙族幻想》的天气效果变化会有初步的感觉。<br><br><div align="center">
<img id="aimg_1012908" aid="1012908" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112640wlassncx8t0c8ytt.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112640wlassncx8t0c8ytt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112640wlassncx8t0c8ytt.jpg" referrerpolicy="no-referrer">
</div>
<br>
好，我下面具体讲一些技术方面的东西。我今天带来的内容没有王总刚才的nanite那么硬核，是偏应用层的。我刚刚说有两个主要的部分。第一个部分是材质系统的优化，我主要讲的是优化，并不是全部的介绍材质系统，由于时间关系，我只讲我们对于UE引擎在材质方面做出一些优化。<br><br><strong><font color="#de5650">一、材质系统</font></strong><br><br><div align="center">
<img id="aimg_1012909" aid="1012909" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112640o6r23666z6x3bff4.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112640o6r23666z6x3bff4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112640o6r23666z6x3bff4.jpg" referrerpolicy="no-referrer">
</div>
<br>
第一部分就讲一下材质系统。材质系统我分四个方面来讲，第一方面是UMaterial，就是最核心的一类。第二部分是ShaderMap、第三个部分是在渲染方面做的一些优化，第四个是在Shadercode方面做的优化。<br><br>
在讲这个优化之前呢，我要先讲一下优化所涉及到的一些关键的类，可能程序员比较敏感点，我直接写了类的名字。从基类到派生类，以及其他的一些辅助类，UMaterialInterface，是材质的最基本的类。任何的一个材质，不管是UMaterial还是UMaterial Instance，都是UMaterialInterface的一个子类，他所表示的是一个最基础的类。<br><br><div align="center">
<img id="aimg_1012910" aid="1012910" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112640w1zga0unu1a1a1k1.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112640w1zga0unu1a1a1k1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112640w1zga0unu1a1a1k1.jpg" referrerpolicy="no-referrer">
</div>
<br>
第二个UMaterial是对应在你们编辑器里面去创建一个材质的时候，文件最终就会对应的一个UMaterial类。这里面会存储有不同的参数，在打开之后会有各种节点，效果、贴图参数之类的都会存在这个里面，它对应的就是UMaterial类。<br><br>
第三个是UMaterial Instance，当UMaterial写好之后呢，可能里面有很多参数比如一个float值，还有贴图。但是如果不用Instance，而直接用UMaterial的话，那么参数是固定的，在运行期的话是没法改的。当你把一些参数导出成Parameter参数的时候，你可以创建一个UMaterial Instance的类，再通过这个类赋值。在运行期的时候，可以通过接口来修改参数。这样的话，其实可以做到UMaterial共享，不同的参数有不同的UMaterial Instance，设置不同的参数。底层使用同样的一个UMaterial类，来达到共享以及效率的提升。<br><br>
第四个类是UMaterial Instance Dynamic，这个类是在UMaterial Instance的基础上。在运行期你可以有一些参数的设置，去设置不同的值。<br><br>
在运行期间，如果你还有一些参数需要改，那怎么办呢？有Dynamic这么一个派生类，在这里面可以放你自己想要的东西。我们后续所做的优化还有包括天气系统的实现，其实最主要就是在这个Dynamic上去存储每一个基于模型的质量等级（QualityLevel）。<br><br>
这前面的四个是有派生关系的，后面四个其实跟前面四个没有多大关系，但是他是渲染最核心的四个类。第一个是FShader，程序员都知道，渲染的时候有Computer Shader、有Vertex Shader还有Pixel Shader。FShader是一个Shader最基础的父类，他的派生类里面可以是Vertex Shader、Computer Shader，也可以是Pixel Shader。<br><br>
下一个FShaderMap，是当你做好了UMaterial之后，派生球拉好了之后、编译完了之后，你可以给这个UMaterial赋予不同的模型，会有不同的顶点结构、还有各种参数，肯定是需要有不同的Shader。<br><br>
他可以通过这个Shader以及factory去查找最终需要渲染这个Mesh所需要的一个Shader。Shader最后对应的可能是不同的，首先你需要根据当前的模型来查找到你合适的Shader。<br><br>
所以它其实是一个记录查询表。对于mesh，是可以顶点结构不一样的，需要结合vertex factory来查询。有些是不需要顶点结构，只通过一个FShaderType作为关键词就可以找到的。通过FShaderType和Vertex Factory，就可以找到一个最终的FShader，所以FShaderMap是一个类似于查询表，也是我们后续做天气系统的关键。<br><br>
FMaterial这个类包含了一个FShaderMap。他增加了些接口方便大家用。比如说我现在是一个高质量的画质，或者是一个低质量的画质，通过参数的调节，来找到一个适合的FMaterial。在拿到这个FMaterial之后呢，他会最终找到这个FShaderMap。拿到FShader Map之后呢，你可以通过刚才说的FShaderType或者是顶点结构factory去找到真实的渲染需要的Shader。<br><br>
最后一个ShaderCode，ShaderCode很简单，就是不同的Shader写完之后，编译出来的二进制的数据，一个UMaterial对应的一个文件，它可以编译出很多很多ShaderCode。一个ShaderCode，其实对应的是一个FShader的实例。<br><br><div align="center">
<img id="aimg_1012911" aid="1012911" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112641vqqz3bjaaqxqbbzq.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112641vqqz3bjaaqxqbbzq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112641vqqz3bjaaqxqbbzq.jpg" referrerpolicy="no-referrer">
</div>
<br>
这就是一个关于材质系统，最核心的八个类。关系图我只是列了上面这四个，他们是这样的一个关系：UMaterialInterface是最上面的父类，派生出来UMaterial和UMaterial Instance。UMaterial和UMaterialInstance是兄弟关系。<br><br>
UMaterialInstance还有一个子类，叫做UMaterialInstanceDynamic。Dynamic上面存在着我们的质量等级。然后在他的父类UMaterialInstance上面有一个parent，这个parent一般就指的是UMaterial，当然它也可以指向一个UMaterialInstance。<br><br>
FShader是依靠在FMaterial里面存在的渲染线程所使用的ShaderMap来查询到的。这个是一个大致的关系图，后续我还会讲，他们在运行期会是怎样这样的一个结构，是一个什么样的情况。<br><br><div align="center">
<img id="aimg_1012912" aid="1012912" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112641w0qp0hqc4ymmq1vm.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112641w0qp0hqc4ymmq1vm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112641w0qp0hqc4ymmq1vm.jpg" referrerpolicy="no-referrer">
</div>
<br>
刚才是继承关系，这个是在引擎层面上的包含关系。<br><br>
当你做好了一个材质，在编辑器里创建好了一个之，材质加载进来的时候，它会变成一个UMaterial类，UMaterial的实例。他在这里面最关键的成员是一个LoadedMaterial Resources数组。<br><br>
这个数组记录着很多ShaderMap，它是做什么用的呢？比如说我们在游戏里面，在系统设置里面，会选择高画质低画质。每一种画质每一种质量级别，对应着Loaded Material Resources这里面的一项。比如说游戏里有3种级别，高中低的画质。对应的数组里面就有三项，每一项都是一个ShaderMap，每一项最终都会得到一个ShaderMap，每一个FMaterial Resources里面他表示的一个质量等级。<br><br>
我们可以想象一下，如果你在系统设置里面选择了一个最高画质，那么在游戏引擎运行的过程中，他就会选择这个数组里面的最高画质所对应的那一个FMaterial Resources。<br><br>
在运行的时候，为什么一个模型，它会呈现出最高画质呢？是因为我们拿到了最高画质所对应的FMaterial Resources，从而拿到了他的ShaderMap。我们在画一个Mesh的时候，就可以通过FShaderType的关键标识，在这个map里找到那个FShader，找到那个最高画质的Shader，然后把它绘制出来。<br><br>
这样就达到了一个，你现在设计是最高效果，那它是一个非常好看的、很有质感的这么一个渲染效果。如果你设置的是一个最低的，那么通过这么一个流程下来，你找到的就是一个最差的FShader。那么效果可能就会很差。<br><br>
UMaterial本质上是一个数组的容器，他在运行期并不会知道需要去用哪一个质量等级，也就是不知道自己用哪一个Shader Map。他只是容器，后续是通过别的类来达到这样的选择。<br><br><div align="center">
<img id="aimg_1012913" aid="1012913" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112642f23ggi32vgf9imhe.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112642f23ggi32vgf9imhe.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112642f23ggi32vgf9imhe.jpg" referrerpolicy="no-referrer">
</div>
<br>
刚才介绍了一些这个材质系统的一些关键的类的概念，我们讲一下我们在《龙族幻想》里面做了哪些优化的措施。<br><br>
首先我们加了一个QualityBias，这个Bias就是一个偏差。我们可以设置一个全局的级别，因为当你在系统设置页面，你设置的可能是一个最高的精度，也可能是最差的精度，不管什么精度，可能你的机器差一点，设计个中等精度。那么我们通过材质的QualityBias，这个偏差值，来叠加在你设置的这个级别上。比如说0的话，你在系统设置里面选的中精度，渲染还是中精度。如果是1的话，它的这个质量级别应该会高一个等级，中就会变成高。当然这个中是不是变成高，这取决于你代码里的具体数值，看你们怎么去改引擎。<br><br>
另外在lod中，Material Slot设置好之后，在每个LOD里面，如果你们对编辑器比较熟悉，在每个LOD里面会选择用哪一个Material Slot，这样的话，就决定了那个LOD，他在这个等级的偏差到底是多少。<br><br>
到最终会体现在右下角的Dynamic，他会有一个Material 质量等级。我们会通过这个Bias，它的偏差值和系统设置里的值，来计算出它当前的这个实例，所使用的材质的等级，从而让这个模型本身达到区别于整体的画质效果。<br><br>
这样我们就可以用他来做LOD的优化。比如说这个机器可能会比较好，设置的是一个最高精度的画质，原来的引擎由于原生的功能，是只能切换LOD，切换完了之后在材质上就可以替换。但是材质替换完之后还是用最高的精度其实是一种浪费。于是我们就加了优化功能，不仅切LOD，还降低质量等级，这样的话就会更节省资源。<br><br><div align="center">
<img id="aimg_1012914" aid="1012914" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112642jg0x0uxkn0wqrbx8.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112642jg0x0uxkn0wqrbx8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112642jg0x0uxkn0wqrbx8.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们在Shader Map方面也做了一些优化，Shader Map刚才我讲他最直观的就是对应着系统设置里面的高中低那么几档，可能游戏做了很多档，不光是高中低，还有最高、最低。每一个这样的等级，都在UMaterial这个材质文件里都会对应着一个Shader Map。不管是存储资源，还是运行期的开销，还是内存显存，都是要占资源的。<br><br>
所以我们就做了优化，对于某些材质，其实不需要导出所有的质量级别。也许他本身就很挫，可能是远处的一个装饰物，永远没有走近的机会，那可能无法展示出最高精度的那一面。所以我们就加了一个flag，没有导出所有的质量等级。勾选的话才会如同原生引擎效果一样。如果不勾选的话，它会导出默认的一个级别。默认的级别我们现在是用high来作为它的默认等级。<br><br>
还有，我们又加了一个标志，是记录着哪些等级被使用。如果只有第一个的话，是否导出？只有是或者否，要么就所有的都导，要么就只导一个缺省的high。<br><br>
后来我们还有个需求，就是它可能需要导一个high是不够的，可能需要导一些。为什么有这种需求，是因为后面会讲到，我们使用了质量等级系统来做天气。有些模型可能没有雨和雪的这种效果，它也不需要雨和雪的这种质量等级。所以我们加了一个标志位，加了一个flag，来记录哪些质量等级是导出了，哪些没有导出。<br><br>
然后我们在UMaterial的函数里面，我们优化了不需要的Shader Map。这个地方其实是可以优化的，但是因为它的文件是逐字节写的，最好的方式是跳过那些不需要的Shader Map。但是现在我们并不太清楚每一个Shader Map占的容量有多少。所以对于不需要的，我们直接加载进来，然后再丢弃，保证它序列化文件的偏移值是正确的。<br><br>
当你全部读完之后，不需要的我们就把它扔掉，这样能达到节省内存的目的。第四个优化方式是当我们写了很多FShader子类的时候， FShader在这个UMaterial里面肯定是用于特定的模型，当你不用于特定模型的时候，这种组合其实是不应该生成ShaderCode代码的。<br><br>
举一个最简单的例子，我们角色的头发是用一个另外的渲染方式，我们为此改了非常多的代码、也加了很多的FShader类型。这些FShader的类型基本上导致了UE原生的FShader数量double了一下，是很恐怖的。如果我们不去通过这个函数指代需要的一些FShaderType和VertexFactory上面去使用它的话，FShader的量会很大。<br><br>
还有就是我们需要降低Material 质量等级的数量。因为UE原来是有低、中、高、最高，后来我们发现FShader数量太多了扛不住，再做了一些优化，将不需要的一些质量等级去掉，这样也会节省大量的FShader和ShaderCode，包体也会小很多。<br><br><div align="center">
<img id="aimg_1012915" aid="1012915" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112642m9iwkwzbzhibugxb.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112642m9iwkwzbzhibugxb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112642m9iwkwzbzhibugxb.jpg" referrerpolicy="no-referrer">
</div>
<br>
这个是界面。在材质上面会加了一个导出所有质量等级的选项，默认它是勾选的，只有对于一些特殊的材质才去掉。<br><br>
刚才讲了我们在游戏的系统设置里面，你会设置高中低。但是那样一来的话，可能整体的游戏都很挫。比如说你设计一个低的，后来又去设计一个高的话，有的时候你机器很差，但是我想让玩家自己的那个角色呈现出一个比较好的效果，那么我们需要针对于某些模型单独设置它的级别。这个时候我们就改了UE引擎，我们基于PrimitiveComponent来设置一个质量级别。<br><br><div align="center">
<img id="aimg_1012916" aid="1012916" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112643k44pnpotvtvonhn2.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112643k44pnpotvtvonhn2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112643k44pnpotvtvonhn2.jpg" referrerpolicy="no-referrer">
</div>
<br>
为什么放Primitive Component呢？因为他静态的Mesh和蒙皮动画都是这个类的子类。所以我把接口放在这个类上面。那么第一步需要改的，就是当你调用这个接口的时候，我们发现当你设置的Material它不是一个Dynamic Material的时候，一般情况下美术做的时候它都会是一个Instance，美术做不出来Dynamic，Dynamic只是程序运行期生成的。一般都是Material Instance这么一个类，它在这个类上是存不了数据，存不了我自己自定义的质量等级的。只有Dynamic这么一个类，它上面会存着我的材质的质量等级。<br><br>
当你发现这个材质需要设置，他不是一个Dynamic的时候，我会把它创建出一个Dynamic的一个Material类。然后再进行具体调整的方法。这个方法其实就是把当前的ShaderMap，就是FMaterial交给渲染线程。让它把这FMaterial里面对应的那个ShaderMap的Shader让渲染线程创建出来。<br><br><div align="center">
<img id="aimg_1012917" aid="1012917" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112643eyavkzifsjpnk8on.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112643eyavkzifsjpnk8on.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112643eyavkzifsjpnk8on.jpg" referrerpolicy="no-referrer">
</div>
<br>
每一个所使用的质量等级，它其实是保存在这个UMaterialInstanceDynamic类上面的。在渲染的时候，它是怎么使用的呢？在主线程你创建了Dynamic的Material Instance，获取了对应的ShaderMap交给了渲染线程，来切换渲染线程使用的ShaderMap。<br><br>
切换完之后，在FMaterial Instance Resource这个类里面，它是渲染的一个代理类，是运行在渲染线程的。运行时候它会调用这么一个方法去得到这个FShaderMap。因为最终它是要拿到Shader，渲染的时候你要拿到Shader，拿到Shader就要从ShaderMap里去拿。<br><br>
那么，它最终是调了这个函数，在这个函数里面拿到了正确的FMaterial。如果引擎不改原生的UE引擎，它怎么拿呢？他是通过全局的质量等级去拿。拿了之后呢，如果你改变了这个全局的，那所有的、整个游戏的画质全部都要改。<br><br>
我们是怎么拿的呢？我们是在这个UMaterial Instance Dynamic里面去拿到那个变量，最终需要的是这个子类变量而不是全局变量，他们的类型都是一样的。我们不读全局的变量，我们读取在Dynamic里面的变量来拿到这个ShaderMap。这样的话，我们拿到了正确的ShaderMap之后，后续的逻辑、后续的功能，都是和UE原生的一样。<br><br>
我讲一下ShaderCode。这个ShaderCode呢，是当你把材料球连好之后、质量等级建好了之后，他会编译出很多的变种。因为你的Shader Type不一样，你的顶点结构不一样，你的质量等级不一样，他会变出很多变种。这些变种都会变成一个二进制的数据，有两种存储方式，在UE里面需要设置。<br><br><div align="center">
<img id="aimg_1012918" aid="1012918" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112643bnsylzysiohhgri4.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112643bnsylzysiohhgri4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112643bnsylzysiohhgri4.jpg" referrerpolicy="no-referrer">
</div>
<br>
如果你不选这个勾的话，这些东西它是存在这个UMaterial里头的，编译完以后存在那个文件里面。如果你勾选这个勾，因为你不同的UMaterial生成的ShaderCode有可能是完全一样的，为了共享，UE就把它放到了一个超大的文件里。因为ShaderCode很多，有几万个，他会放在一个很大的文件里面去。这个UMaterial文件和那个UMaterial文件，变出来的可能是一个完全相同的ShaderCode。<br><br>
这样的话，它在你最终发布的包里面，就只存在一份，整个的包体就会小。所以我们《龙族幻想》所有的ShaderCode方面优化都是需要勾选这个勾才行的。因为我们这种庞大的游戏材质很多，如果不选这个勾，每一个都储存在Material里面的话，那整体的包体容量会很大，所以必须勾选这个。<br><br>
如果对于小游戏的话，本身包体就不是很大，那么建议可以放在这里面，不勾选这个。它的好处是你创建那个FShader的时间会比较快，会节省一点。他的包体，当你资源造好了之后，他这个Shader就已经准备好了。<br><br><div align="center">
<img id="aimg_1012919" aid="1012919" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112644u5t8tx43a0z4uqe3.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112644u5t8tx43a0z4uqe3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112644u5t8tx43a0z4uqe3.jpg" referrerpolicy="no-referrer">
</div>
<br>
接下来，再讲一下我们对于ShaderCode存储方面的优化，我记得是在UE4.17的时候，每一个Shader当你勾选的刚才那个选项之后，共享了ShaderCode之后呢，UE的方式是将每一个ShaderCode都存成一个文件，放在磁盘的某一个目录里去。<br><br>
这个我们当时觉得用的还是挺好的，后来在后续版本里它合并成一个大的文件了，这个大的文件里面包含着若干个小的ShaderCode，相当于一个虚拟文件系统。他的初衷可能想做一个这方面的优化，因为它的虚拟文件包是pak，可能是想单独为ShaderCode做一个优化。<br><br>
但是这种优化，和我们《龙族幻想》的方式还有点冲突。所以我们在新版里面，我们重新把这个大的文件分拆成之前的版本，一个ShaderCode是一个文件，文件名是它的哈希值。因为很多的游戏公司都有自己的虚拟文件系统，当面对UE的这么一个很大的文件的时候，其实是没办法使用自己的虚拟文件系统来做这个热更新的。现在这个ShaderCode按照《龙族幻想》的级别应该是在四百兆左右的大文件，如果是用UE的方式组成一个大包，那更新量是很大的。所以我们把它分拆了。<br><br>
分拆了之后若干个文件，我们需要使用自己的文件系统。我们改变了哪些ShaderCode文件，就单独更新那些文件。然后在这个FShaderCodeLibrary这个类，也做了修改。这个类的话，原来它的实现方式是你打开一个文件，首先打开那个library，那个library里面是一个很大的文件，里面再去逐个地打开读取ShaderCode。那么我们现在就是去打开单个ShaderCode文件的时候，我们就直接打开某一个文件，然后把里面的文件内容读出来。它的好处就是我们只会下载单独的ShaderCode的更新包。<br><br><div align="center">
<img id="aimg_1012920" aid="1012920" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112644e3eh02be22bd72z2.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112644e3eh02be22bd72z2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112644e3eh02be22bd72z2.jpg" referrerpolicy="no-referrer">
</div>
<br>
这是改进之后的长相。因为文件特别多，有几万个文件，在开发期的时候必须要做一个文件夹的映射。因为几万个文件都存在一个文件夹里的时候，查看会卡很久。所以我们通过ShaderCode的文件名哈希出来，把它分摊到若干个目录里去，这样每个目录的文件数量不是很多。<br><br>
然后每个文件都是以它的哈希值作为文件名的，这样的话，当你在运行的时候去加载一个ShaderCode的时候，你拿到它的哈希值，直接定位到这个文件把它读出来就ok了。然后，这样的文件通过我们的虚拟文件管理打成一个大包，我们更改了哪些文件，就只下载那些文件，做到包体的最小化。这就是我们对于材质系统所做的一些优化。<br><br><strong><font color="#de5650">二、天气系统</font></strong><br><br><div align="center">
<img id="aimg_1012921" aid="1012921" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112644topfj0ssnhjm0v4f.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112644topfj0ssnhjm0v4f.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112644topfj0ssnhjm0v4f.jpg" referrerpolicy="no-referrer">
</div>
<br>
下面我讲一下天气系统，之前我跟UE同学沟通，他们也收到了不少同学反馈说很想知道一些游戏里面的天气系统是怎么实现的，所以我觉得讲一下这个还是很有必要的。在《龙族幻想》里我们打算做天气系统的时候想到很多方案。开始想的是，我们可以通过改Shader的参数，把雨啊雪啊什么的都放在一个Shader里面，通过它的参数来做一个切换。<br><br>
最后发现这样的话，我们的材质编器里面的图就会非常多，线画的非常乱，并且效率非常低。我们后来想，要不就运行期改FShader，但改FShader其实对于每个模型，比如说当前是一个晴天的材质，里面对应的是晴天的FShader，我们需要把它改成雨，那我们去找到这个雨的FShader，把它调整一下，这也是一个方案。<br><br>
但是后来想一想，我们针对于每个模型去改FShader的这样一个架构，在UE引擎里面其实是没有的。改动会比较大，挺麻烦的。直到我们看到了质量等级。我们发现它在全局有一个功能是设置质量等级的，那我们在想，场景里面很多天气变化的时候，其实有一些模型是不会受天气变化影响。比如室内的东西，我们不能通过改全局的质量等级来切换Shade，我们就改成基于每个模型的。<br><br>
所以我们最终想到，我们可以利用材质的质量等级这么一个引擎自带的功能去实现天气系统。但是我们还需要改进，原先的功能不能满足我们的要求。<br><br>
然后第二个方面我介绍一下，就是我们需要采用这个Material Parameter Collection。因为每一个材质，它都会有一些差值。他需要有一些全局的数据，比如我们现在需要知道他是从晴天开始切换到雨天，从雨天切回晴天，那么这些全局的数据和参数，就是取用这个参数的集合。<br><br>
还有就是，我们在材质编辑器里面，我们可以通过Quality Switch这个节点来做一个不同的等级效果的LOD，我现在细化一下。我们决定用质量等级来做天气系统之后呢，我们就开始着手加，因为它原来不够，只有低中高最高。我们加了好几种，有雨和雪，雨和雪最终都加了最低、中、高、最高，很多很多。后来我们觉得这样不行，我们砍掉了很多，只留下最基础的一些。<br><br><div align="center">
<img id="aimg_1012922" aid="1012922" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112645ekzzxf5a433jx49x.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112645ekzzxf5a433jx49x.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112645ekzzxf5a433jx49x.jpg" referrerpolicy="no-referrer">
</div>
<br>
所以我们在最差的机器上没有天气的变化，因为我们只有low，没有low rain、low snow。在中等的机器上和最高级机器上，我们会有分别对应的雪和雨。比如说我们雪的变化，从medium的质量等级，切换到medium snow，然后晴天到雪、从晴天到雨还有反向的切换。<br><br>
既然做了这种质量等级的划分，我们就不需要把所有天气做在一个Shader里面。一个Shader里，我们只做两种天气的过渡，比如晴天到雪天的过渡，我觉得这个不是特别的复杂，你只需要考虑两种天气。但是如果你要在这个材质里面，还要做从雪到雨的切换的话，那这个Shader就会比较复杂，因为你要做到无缝的切换。<br><br>
当前如果是雨的话，你想切换到雪， Shader即使换了之后，你还要保证现在效果跟换之前效果是对接好的，新的这种材质里肯定也要有雨和雪的成分在里面。所以我们做了限制，我们没有雨和雪之间的切换，我们只做两种。如果想做雨到雪的话，那通过策划的玩法，先让他变到晴天，然后再通过一个玩法或者事件让他变到雪天。这样曲线救国一下，Shader的复杂度就会大大的降低。<br><br><div align="center">
<img id="aimg_1012923" aid="1012923" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112645y31yfwwyww1zy1wb.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112645y31yfwwyww1zy1wb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112645y31yfwwyww1zy1wb.jpg" referrerpolicy="no-referrer">
</div>
<br>
然后在一些低端机器上，我们会砍掉一些不必要的质量等级。比如说因为质量等级的加载是运行期做的，在UMaterial的函数里面去做的，发现是比较差的机器的话，就只保留一种Low或者是Medium。要看实际的效果。可以写一个很大的配置表，这个机器是用低还是用高，在运行期决定到底是扔掉哪些、保留哪些。<br><br><div align="center">
<img id="aimg_1012924" aid="1012924" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112645i4wdsm37sitxx536.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112645i4wdsm37sitxx536.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112645i4wdsm37sitxx536.jpg" referrerpolicy="no-referrer">
</div>
<br>
再讲一下参数集。这个参数集我并不想特别展开每一项参数的意义。因为每一个游戏，它天气效果的渲染是非常复杂的一个图表，会使用不同的参数。我现在只讲一下它使用的思路。<br><br>
天气过渡会使用到到一些全局的东西，比如说晴天到雨天，晴天到雪天过渡的一些权重，比如说时间，光线、风速，每个参数都可以在运行期改变。当你在做天气切换的时候，你需要在游戏逻辑上把一些参数设置好，让它能够有一个过渡衔接。比如说我们从晴天到雨天的过渡，当前这个模型所处的是晴天的一个Shader，这里面的雨权重就是0。<br><br><div align="center">
<img id="aimg_1012925" aid="1012925" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112646w1b4enevu5h1rbny.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112646w1b4enevu5h1rbny.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112646w1b4enevu5h1rbny.jpg" referrerpolicy="no-referrer">
</div>
<br>
切换的过程是在代码里瞬间切换的。这个时候就需要我们在切换前把这些参数的集合，比如说雨，权重设成0，才不会突变。设成0之后，我们在运行期里面去update时逐渐修改这个雨的权重值。这个雨的Shader里面，他自然就会读到雨的数值，雨的贴图的比重，晴天贴图的比重都会下降，涟漪的贴图就慢慢的呈现出来。其他的效果就会慢慢地淡入，直到达到百分之百的稳定态。这个取决于你们的TA怎么去连线材质的图。<br><br><div align="center">
<img id="aimg_1012926" aid="1012926" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112646xdsn8iplegdidaxn.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112646xdsn8iplegdidaxn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112646xdsn8iplegdidaxn.jpg" referrerpolicy="no-referrer">
</div>
<br>
这是大概的一个长相。我们的参数非常多，有标量的参数，还有矢量的参数，我只截了两个。天气材质球的连线也是相当复杂。在《龙族幻想》里面还有一些效果，是区域性的，比如说我在这个区域里面，可能是迷雾森林再走到一个别的区域里面，我们会预先保存很多的预制键，预制的一些数据集。<br><br>
这些数据集就是对刚才那堆参数预先设置好的，比如说一个充满黄色雾气的地方，还有傍晚、早晨。我们存有很多参数集的文件，当你在运行期想进入某一个区域的时候，通过逻辑把这些值加载进来，然后跟当前的值通过位置做一个lerp，取代或者是设置这个Shader读取的那套参数集。最终的效果就会发生变化，就能达到魔兽世界那种穿过一个区域到达另外一个区域的效果。<br><br><div align="center">
<img id="aimg_1012927" aid="1012927" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112647v27nbl53n3eq07qx.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112647v27nbl53n3eq07qx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112647v27nbl53n3eq07qx.jpg" referrerpolicy="no-referrer">
</div>
<br>
这是一个简单的示例，比如说像右边就是一个全局的参数集，它会有复杂的连线，这里只是展示一个用法。用上这些全局的参数之后，我们在引擎里面去改这些值，整体渲染效果就会有变化。在我们的Shader图标里面，材质图表里面充斥着大量的、对于全局的参数集合的应用，来达到这种最终的变化的效果。<br><br><div align="center">
<img id="aimg_1012928" aid="1012928" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112647urrsddq6qd7dr4zq.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112647urrsddq6qd7dr4zq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112647urrsddq6qd7dr4zq.jpg" referrerpolicy="no-referrer">
</div>
<br>
当你在材质编辑器里面去连接节点的时候，不光是通过一些刚才的那些全局的参数来达到效果，还有一个重要的是通过Quality Switch节点。在最低精度下面，我可以走这条分支，高精度我走另外一条分支，达到一个Shader的优化。<br><br><div align="center">
<img id="aimg_1012929" aid="1012929" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112647fbwujjbswke290tc.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112647fbwujjbswke290tc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112647fbwujjbswke290tc.jpg" referrerpolicy="no-referrer">
</div>
<br>
这就是刚刚说的，基于这个节点的Switch。每一个节点的Switch最终都会被编译成对应的ShaderCode，放在它自己的ShaderMap里面。延伸过来之后可能会有非常复杂的逻辑，比如说这个Low，连过来之后可能是一个非常简单的逻辑，这个高的雨、最高的雨连过来，可能它有更多的贴图、更多的采样，更多其他的效果，然后输出到一个最终的节点。<br><br><div align="center">
<img id="aimg_1012930" aid="1012930" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112648oqhhn7rtnephtwyv.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112648oqhhn7rtnephtwyv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112648oqhhn7rtnephtwyv.jpg" referrerpolicy="no-referrer">
</div>
<br>
限于时间关系，我给大家简单介绍一下在渲染优化上做的一些事。UE原生的FShader没有卸载的机制，加载进来之后就永远留在那个地方，我觉得其实是一种效果浪费。因为可能FPS游戏的Shader类型不是很多，当我们做《龙族幻想》的时候，对渲染效果要求很高。再加上我们加了很多质量等级去实现天气效果，FShader的量就会很大，这个时候如果不卸载FShader的话，就会带来很大的内存开销，因此我们做了FShader的释放。<br><br>
这个原理其实也非常简单，一个FShader创建出来会使用引用计数记录在多少个地方使用，在切场景的时候我们会统一过一遍，我们会检查一遍这些所有的FShader。如果它的引用计数为零了，我们就会把它释放掉，需要放到渲染线程，或者是RHI线程里面去释放这个Shader。在不切场景的时候，我们也会时不时做一下，但是我们在切场景的时候，在Loading条走的时候，肯定要做一遍释放检查。因为loading的时候卡一下的话也没什么关系。<br><br>
然后就是OpenGL的一个program binary data cache。这个是在OpenGL里面，安卓平台下面，当你设置一个shader的时候，你需要Link。Link有点卡，当然如果Fps游戏FShader不多的时候，不会感觉特别明显。但是《龙族幻想》有很多Shader，并且不同的模型可能Shader会不一样，他的这种卡顿就会变成一个问题。<br><br><div align="center">
<img id="aimg_1012931" aid="1012931" zoomfile="https://di.gameres.com/attachment/forum/202110/08/112648mkq1aala74a47ffl.jpg" data-original="https://di.gameres.com/attachment/forum/202110/08/112648mkq1aala74a47ffl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/08/112648mkq1aala74a47ffl.jpg" referrerpolicy="no-referrer">
</div>
<br>
当Link完了之后，生成一个program，我们会拿到这个data，把它存下来，存在一个文件里。我做了一个虚拟的文件系统，这个虚拟文件的key就是那段program的data。<br><br>
存下来以后，当第一次运行游戏时这个文件是空的，每次都会Link，然后存进去。当第二次运行的时候，情况就会变好了。以前曾经Link过的，我直接在文件里找到，通过这个Program加载进来，也不需要去设置Shader，也不需要Link，直接就可以用了。<br><br>
第三个是多个PSO cache file 。UE4自己有一个功能是对PSO的缓存，原来是叫Shader cache，后来改成pipelinecache。<br><br>
他只有一个文件，我们改进了这个功能。在录的时候，我们可以录很多个文件。比如我们在打Boss战的时候，那个Boss以前从没出来过。他一出来，不管你是Link还是怎么样，反正他会卡顿。因为就算是你Link了，他往显卡送的那一刻，往镜头送那一刻，他也会有一定的时间开销。然后当那个Boss从来没出现过，一出来就卡一下，这个效果不太好。<br><br>
还有就是我们游戏运行Loading完了之后，我们需要播一个CG，那个CG有很多也是游戏不太用到的资源，它也会卡一下。我们还是想用引擎的PSO功能，记录的功能，然后把它预热一下。但是一个不够，尤其是出现怪物的时候。然后我们就做了一个录不同的PSO的cache。PSO cache需要录渲染所有的参数，Shader，各种参数都录下来。录下来之后当你需要播这些、需要画这些文件的时候，它会在后台给你把这些东西跑一遍。这样的话，当你真正渲染模型的时候就不会卡顿，我们做了多个这样的文件。比如说，在这个Loading条结束的时候，我们需要播CG，那在Loading条结束的时候，就加载这个场景所对应的记录好的文件。当这个CG播放的时候就会非常的平滑，没有一丝的卡顿。对于boss也是这样，快到播boss的时候，我们也在后台把这个cache文件加载进来，做一下这样的预热，就会达到非常好的平滑效果。今天的分享大概就是这些，非常感谢。<br><br><font size="2"></font><br><font size="2">来源：手游那点事</font><br><font size="2">原文：https://mp.weixin.qq.com/s/YGqcmBq536OWpPGUFKKMNA</font><br><br><br>
</td></tr></tbody></table>


  
</div>
            