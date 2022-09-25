
---
title: '腾讯光子陈玉钢谈《Apex Legends Mobile》渲染优化实践'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202208/25/100609neh8m7hnxsh85iif.jpg'
author: GameRes 游资网
comments: false
date: Thu, 25 Aug 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202208/25/100609neh8m7hnxsh85iif.jpg'
---

<div>   
在近期由腾讯游戏学堂举办的TGDC2022腾讯游戏开发者大会上，腾讯互娱光子工作室群《Apex Legends Mobile》项目引擎组负责人陈玉钢以《Apex Legends Mobile》项目为例，通过讲述在该项目中解决渲染优化的难点，向行业者展示了如何利用合理的技术手段、借助现有的技术软件、结合主流的技术机制来达到良好的优化效果。<br>
<br>
<div align="center">
<img aid="1051326" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100609neh8m7hnxsh85iif.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100609neh8m7hnxsh85iif.jpg" width="600" id="aimg_1051326" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100609neh8m7hnxsh85iif.jpg" referrerpolicy="no-referrer">
</div><br>
陈玉钢：大家晚上好，我是来自于光子Apex手游项目引擎组的陈玉钢，今天给大家带来的分享是Apex 手游渲染优化。<br>
<br>
在分享之前，先给大家介绍一下Apex手游这个项目的优化难点，特别是在渲染优化方面的一些挑战。<br>
<br>
首先Apex手游是一个需要高度还原端游的项目，实际上我们也做到了不错的还原度，在这方面众多游戏媒体和玩家也给了我们一些还不错的评价。<br>
<br>
<div align="center">
<img aid="1051327" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100611rmfp8q89r8ydnwn4.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100611rmfp8q89r8ydnwn4.jpg" width="600" id="aimg_1051327" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100611rmfp8q89r8ydnwn4.jpg" referrerpolicy="no-referrer">
</div><br>
左边两张图分别是Apex端游和手游的训练场，相信大家粗略一看已经不太能轻易分辨哪个是手游、哪个是端游。然后端游的场景本身就非常复杂，需要比较好的PC才能跑得起来，为了比较好地还原端游的场景表现，我们的美术、TA、策划在各个层面做了大量的优化，当然引擎底层我们也做了很多针对手机平台的改进。<br>
<br>
另外，了解Apex的同学应该都知道，除了场景，最重要的还有大量英雄技能。这些技能通常都有非常高的辨识度，很多技能都有独特的表现需求。比如右边这两张图，上面是恶灵的踏入虚空，在进入虚空状态的时候，整个场景都需要有一个去色的渲染结果；下面是寻血猎犬的扫描，被扫描的那些角色或者目标是需要有一个复杂的描边填色，而且有的时候根据逻辑可能需要有一些穿墙的渲染表现。<br>
<br>
端游是可以通过后处理来实现这些效果，但是在手游后处理是非常昂贵的，特别在低端机，基本上都是不能开户处理的，这也对我们的渲染管线优化提出了更高的挑战。<br>
<br>
除了来自还原度方面的挑战，同时我们还是一款英雄射击游戏，也就意味着对帧率的要求非常高，在我们的策划看来，30帧和40帧有着完全不同的游戏体验。<br>
<br>
我们是希望在主流设备能稳定的跑到40-60帧，新的旗舰手机能跑到90甚至120帧。而由于移动端设备环境特别复杂，散热情况也不是很好，我们甚至遇到过手机壳对帧率的影响，所以即使跑到了60帧，也还远远不够，还需要不断地做功耗上的优化，这样就能给平台层或给环境更多的性能上的容错空间，才能在大部分情况下保持稳定的高帧率。<br>
<br>
<div align="center">
<img aid="1051328" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100615hzlzai44udlha3qr.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100615hzlzai44udlha3qr.jpg" width="600" id="aimg_1051328" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100615hzlzai44udlha3qr.jpg" referrerpolicy="no-referrer">
</div><br>
作为一款公平竞技的游戏，高DAU也是最基础的目标，对于引擎优化来说也就意味着需要比较好的适配性，我们需要兼容到六七年前的设备，确保他们基础的游戏体验。这对我们引擎的伸缩性也有更高的要求。<br>
<br>
总的来说，Apex手游在性能上存在三个方面的主要挑战：高度复杂的场景和Gameplay表现，导致基础开销非常高；同时作为一款英雄射击的玩法的游戏，也需要比较高帧率才有较为畅快的游玩体验；而作为主打公平竞技BR玩法的产品，较好的适配性也是必须的。我们团队需要在这三大挑战下，把端游起码要上百W功耗计算能力才能跑动的内容，塞到只有几W功耗预算的手机上，并且能够流畅地跑起来。<br>
<br>
在这样的背景下，我们已经进行了各个层面大量的优化。今天给大家分享主要的内容是，我们引擎团队对场景渲染优化和 RenderPass优化两个部分。<br>
<br>
<div align="center">
<img aid="1051329" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100617mvoge9dzgjged969.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100617mvoge9dzgjged969.jpg" width="600" id="aimg_1051329" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100617mvoge9dzgjged969.jpg" referrerpolicy="no-referrer">
</div><br>
场景渲染优化部分。首先会大概介绍一下Apex端游场景特点、手游光照策略，还有内容管理方面的一些细节，包括关卡怎么拆分的，材质怎么合并的，最后详细分享一下我们场景的渲染过程是如何优化的。<br>
<br>
因为我们首要目标还是说尽可能还原端游，这里先大概说一下端游场景特点。<br>
<br>
首先从场景光照方面，场景中有大量复杂光源，场景光照也特别复杂，但另外一点好在没有日夜变化的需求，相对来说我们就不是那么有必要做动态光照的支持。<br>
<br>
从场景内容方面来看，这是开放世界的场景，对象的密度特别高，可以看一下右图，到处都有大量物体，层次结构特别复杂，甚至会导致常规的剔除手段不能很好地工作。这个稍后也会详细说一下。<br>
<br>
<div align="center">
<img aid="1051330" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100619vhfllfp5pcsmka59.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100619vhfllfp5pcsmka59.jpg" width="600" id="aimg_1051330" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100619vhfllfp5pcsmka59.jpg" referrerpolicy="no-referrer">
</div><br>
具体从场景光照方面来看一下。首先从光源角度来看，场景中有大量的大型面光源，尺寸通常可以达到上百米大小；强度和影响范围也是特别大的，比如像右边的岩浆，它可以影响到几百米之外墙壁的shading的结果；色彩也是非常丰富的，除了岩浆，上面还有大的Landmark，一个冰柱，它是偏冷色调的，而且复杂不同色彩的光源经常会交织在一起。<br>
<br>
<div align="center">
<img aid="1051331" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100622ikevdy3zkw8q367w.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100622ikevdy3zkw8q367w.jpg" width="600" id="aimg_1051331" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100622ikevdy3zkw8q367w.jpg" referrerpolicy="no-referrer">
</div><br>
场景也特别复杂，这就导致光线传播过程中的遮挡和反射特别复杂，这个时候很多光照的Trick就不是那么好用了。<br>
<br>
为了更好地还原端游的光照效果，需要的是一个相对来说比较完备的全局光照。但是因为没有TOD的需求，即没有更复杂的动态光照的需求，我们需要的是相对准确的静态全局光照。<br>
<br>
静态全局光照主要分两个点：首先是间接光，会针对不同类型的物体，比如说不同大小，或者是动态、静态的，用不同的表达方式表达间接光照；阴影，在间接光照方案的基础上，会有一些不同的优化参数，针对不同画质也会开发不同的策略，这个稍后也会详细说一下。<br>
<br>
<div align="center">
<img aid="1051332" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100624n1zq9x8l9wu8ulk9.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100624n1zq9x8l9wu8ulk9.jpg" width="600" id="aimg_1051332" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100624n1zq9x8l9wu8ulk9.jpg" referrerpolicy="no-referrer">
</div><br>
Lightmap当然是最主要的间接光表达方式，我们在室内室外、山体、地形大量的地方使用lightmap。我们在Alpha通道集成了ShadowMask作为阴影的处理，这个稍后会详细说到。另外在高画质为了更好提高光照品质，我们保留了用于提升暗部细节的Directional SH部分。<br>
<br>
除了Lightmap, 针对中小型物体，我们使用单点光照烘焙，简单来说就是会在Primitive上烘焙一组球谐系数来表达间接光。然后在光子技术中心的支持下，实现了多点光照烘焙，也就是在一个稍大一点稍复杂的Primitive上可以烘焙多组球谐系数来表达更为复杂的光照情况。<br>
<br>
最后，会使用ILC（间接光缓存）来处理角色和载具这些动态物体的间接光照，我们在虚幻官方的实现基础上，进一步又做了二阶优化，还对它的排布做了自适应的优化。<br>
<br>
<div align="center">
<img aid="1051333" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100632ws3shs3fftftjjiz.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100632ws3shs3fftftjjiz.jpg" width="600" id="aimg_1051333" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100632ws3shs3fftftjjiz.jpg" referrerpolicy="no-referrer">
</div><br>
再看一下我们阴影部分的主要优化策略。最主要的当然还是用CSM，刚才也说了，因为我们大规模地使用Lightmap，就在Lightmap的Alpha通道集成了基于DistanceField的ShadowMask，这样我们就有了全局基于烘焙的shadow，CSM所要覆盖的距离就自然不需要那么远了。这样做就很多好处，首先画CSM的Drawcall就少了，然后因为相同精度下更近的距离，所以shadow的品质也可以提高。<br>
<br>
<div align="center">
<img aid="1051334" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100635azv577axxsqez6e6.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100635azv577axxsqez6e6.jpg" width="600" id="aimg_1051334" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100635azv577axxsqez6e6.jpg" referrerpolicy="no-referrer">
</div><br>
我们还对静态物体的ShadowDepth做了缓存，这样能减少重复Drawcall的提交。<br>
<br>
另外我们对低画质也开发了更为高性能的阴影方案，在这个方案下只有动态物体会画阴影，所有静态物体都会用烘焙好的ShadowMask。如果没有Lightmap的物体，就跟Probe一样烘焙一个Probes shadow。<br>
<br>
<div align="center">
<img aid="1051335" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100636bixzvbcmyjjibjej.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100636bixzvbcmyjjibjej.jpg" width="600" id="aimg_1051335" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100636bixzvbcmyjjibjej.jpg" referrerpolicy="no-referrer">
</div><br>
刚才说的是光照方面，再看一下场景方面。<br>
<br>
场景内容首先是一个开放大世界的场景，典型的BR的场景大概是2公里×2公里左右，虽然说不是特别大，但是大世界该有的问题基本都会有，而且因为对象密度更高了，所以其实到处都是性能热点。<br>
<br>
因为是开放世界，玩家的视角是比较自由，摄像机的镜头位置到处都是可达的，这样PVS类优化就不是那么好用了。<br>
<br>
内容复杂，这个刚才也说了。<br>
<br>
<div align="center">
<img aid="1051336" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100637celea1dlugea1uxa.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100637celea1dlugea1uxa.jpg" width="600" id="aimg_1051336" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100637celea1dlugea1uxa.jpg" referrerpolicy="no-referrer">
</div><br>
我们怎么优化？分两个层面，首先是场景内容管理层面，用特别细粒度关卡管理这些物体，尽可能合并模型的材质；在渲染过程，在虚幻的基础上又进一步优化了各个阶段的合批和裁剪，并且基于已经优化好的合批和裁剪进一步做了基于簇的裁剪和管线，这个稍后也会详细分享一下。<br>
<br>
详细看一下关卡方面，刚才也说了我们使用了特别细粒度的关卡，一个场景中的子关卡通常可以达到500个以上，我们再对这些子关卡根据距离进行分层的管理，不同的层会有不同的加载距离，这样就可以避免很多不那么重要物体加载到内存中，然后大量使用LevelLOD来呈现远景，这样就会进一步地减少Primitive加载到内存里。<br>
<br>
这样做有很多好处，首先内存少了，因为要管理的Primitive的actor也可以变少，Uobject的数量也能减少，对机器的压力也能够比较好地进行优化，因为Primitive大幅度减少了，在InitViews的耗时也可以比较好地优化。<br>
<br>
当然，大量的子关卡会导致关卡管理本身的压力会比较大，为此我们也改进了WorldComposition，进一步做了分帧优化和加载预测。<br>
<br>
再来详细看一下材质合并。为什么要做材质合并？非常复杂的模型里面贴图是非常多，就会导致模型的材质会非常多，通常会达到十几个子材质，Drawcall的压力就会特别大。<br>
<br>
<div align="center">
<img aid="1051337" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100639fuosdzwyldwwg4wz.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100639fuosdzwyldwwg4wz.jpg" width="600" id="aimg_1051337" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100639fuosdzwyldwwg4wz.jpg" referrerpolicy="no-referrer">
</div><br>
以典型的建筑为例，首先Apex里的建筑精度要求是非常高的，通常一个Texel要表达厘米甚至毫米为单位的面积，直接给它拍平了，用Flatten模式去合这样的贴图出来，精度肯定是不能达到要求的，所以从贴图的角度我们肯定是尽量希望复用这些贴图的资源。所以从另外一个角度，从顶点角度，肯定也不希望加额外的顶点去引导UV，我们希望这些UV是可连续、可插值。<br>
<br>
最常用技巧是Tiling：区域贴图在模型上进行重复映射，这样相同面积、相同预算的贴图就可以表达比较高的精度。<br>
<br>
目前主流Tiling方案是Atlas Tiling，简单来说会把需要Tiling的，多个贴图合并成一个大的Atlas贴图、渲染时通过模型顶点的UV，插值计算出在Atlas空间里的UV。但非常常见的问题是有接缝，主要原因之一是Atlas的UV不可避免的会产生跳变，UV产生跳变之后，自动算出来的mip（音）会容易产生跳变，这样相邻的像素就很容易出现颜色的抖动。<br>
<br>
<div align="center">
<img aid="1051338" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100640ib8ttvd8wvxv9g2b.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100640ib8ttvd8wvxv9g2b.jpg" width="600" id="aimg_1051338" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100640ib8ttvd8wvxv9g2b.jpg" referrerpolicy="no-referrer">
</div><br>
我们的方案是：把要Tiling贴图合并在Texture Array里，这样计算出Array的UV基本上就和Tiling的UV空间是一样的，可以对齐的，只是说W分量不一样，这样就很好地避免跳变了。<br>
<br>
基于Array的Tiling还是有一个缺陷，只能支持固定贴图尺寸的Tiling，比如说Texture Array固定的是256×256的，如果我们要Tiling一个512的就做不到了。所以我们进一步做了多Slice合并，我们会把比如说四个256×256合并成一个512的，这样就能比较灵活地支持多种尺寸的Tiling。<br>
<br>
接下来介绍一下我们静态合批的策略，我们主要是使用HISM来做静态合批。<br>
<br>
<div align="center">
<img aid="1051339" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100641uv1ev3jw3w367kbg.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100641uv1ev3jw3w367kbg.jpg" width="600" id="aimg_1051339" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100641uv1ev3jw3w367kbg.jpg" referrerpolicy="no-referrer">
</div><br>
HISM是层级实例化静态模型的简称，相比更为简单的实例化，静态模型有着更好的伸缩性。它能根据层级簇来管理可见性和LOD的切换，也就是能比较好地优化GPU的压力。在我们的优化下HISM的Drawcall也有比较大幅度的优化，稍后也会详细说一下。<br>
<br>
另外我们在低端机通过大幅度调整 LOD Distance Scale 让实例在更近的距离切换低LOD，这样可以在损失一定效果的情况下，进一步减少GPU和Drawcall压力。<br>
<br>
但是HISM有个问题是Drawcall特别容易被不可见的簇打断。根本原因是单个Drawcall需要连续的InstanceBuffer，大家可以看右图  左上部分，在裁剪后012和678是可见的，345是不可见的，那由于InstanceBuffer连续性被不可见的345打断了，012和678就必须分为两个Drawcall来提交。<br>
<br>
<div align="center">
<img aid="1051340" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100643agnwugxeek653m76.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100643agnwugxeek653m76.jpg" width="600" id="aimg_1051340" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100643agnwugxeek653m76.jpg" referrerpolicy="no-referrer">
</div><br>
我们进一步优化了这个问题，简单来说我们还是会在剔除后动态合并剩下的这两个Buffer，比如说012和678，但是Buffer合并的成本都是非常高的，如果每一帧做大量Buffer的合并，对性能的影响也是非常大的。所以为了避免每帧重新合并，我们加了一个LRU的Cache来管理合并后的Buffer。<br>
<br>
具体来说，我们会在合并Buffer之前，先通过可见簇的组合key去LRUCache里查，如果存在已经合并好的Buffer，我们就不再做重复的合并，就直接获取提交就可以了，如果不存在，就会重新把这些Buffer合并，并且加入到LRUCache里，记做一次CacheMiss。这样就可以极少量内存开销来尽可能地避免Buffer重新合并。<br>
<br>
做完这些之后，在我们的跑分场景测试下来，通常来说CacheMiss都能降低到5%以下，也就是能降低95%的Buffer组装需求，这样HISM就能进一步合批。我们场景最多能减少30-40的Drawcall，并且几乎没有额外开销。<br>
<br>
<div align="center">
<img aid="1051341" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100645u2h1lhk2mklm8xnu.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100645u2h1lhk2mklm8xnu.jpg" width="600" id="aimg_1051341" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100645u2h1lhk2mklm8xnu.jpg" referrerpolicy="no-referrer">
</div><br>
接下来是动态合批部分，虚幻从422开始就提供了GPUScene来做动态实例化合批。先简单介绍一下GPUScene的流程，首先在Primitive Add To Scene的时候通过ComputerShader上传相关的PrimitiveData到GPU的一个统一的Buffer里，在Shader里通过Primitive ID去Fetch其中相应的PrimitiveData。提交的时候通过合并PrimitiveID合并到一个PrimitiveBuffer里面，来合并能合批的Drawcall。<br>
<br>
但是这个机制在移动设备上还是有一些问题：<br>
<br>
首先它需要依赖ComputeShader来做数据更新，为了更好的兼容性，我们不太希望这种基础功能对ComputeShader有依赖。<br>
<br>
另外GPUScene在Android 平台需要在VertexShader里做TextureBuffer Fetch，这样对很多GPU的优化都不太友好。我们在部分高通的手机上发现开启GPUScene之后，渲染模式从binning模式转到direct模式，了解的同学也知道，这个模式转变对性能的影响是特别大的。<br>
<br>
除此之外，GPUScene还需要额外地维护一个PrimitiveID Buffer到Instance Index的映射。<br>
<br>
<div align="center">
<img aid="1051342" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100647tzezc410zenceoh4.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100647tzezc410zenceoh4.jpg" width="600" id="aimg_1051342" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100647tzezc410zenceoh4.jpg" referrerpolicy="no-referrer">
</div><br>
对此我们开发了一个基于Uniform的动态合批机制。简单来说，就是每帧把能合批的PrimitiveData合并到一个Uniform 数组里，然后在VertexShader里 再根据内置的InstanceID去Uniform数组里取相应的PrimitiveData。<br>
<br>
这样的好处当然是不需要ComputeShader来做数据更新，直接在CPU组装好就可以了，也不需要维护PrimitiveID Buffer，因为直接就可以用内置的InstanceID，比如说OpenGL里面其实GL InstanceID，去数据里面取就可以了。更不需要VertexBufferFetch，因为直接就通过读取Uniform数组的值就可以了，Uniform数组当然会比VertexBufferFetch要快特别多的。<br>
<br>
但是基于Uniform合批也是有限制的，主要是因为Uniform 尺寸的限制，所以我们也会比较激进地限制动态合批的数量上限。<br>
<br>
修改后在我们的跑分场景测了一下，发现相比GPUScene，低端机的帧时间能从28ms降低到22ms。<br>
<br>
剔除也是渲染优化的关键步骤，主要分为遮挡剔除和视锥剔除两个部分。<br>
<br>
遮挡剔除我们主要用的是光子技术中心提供软光栅组件，能在极少CPU消耗的情况下有效地进行Drawcall剔除，这方面也有不少资料。<br>
<br>
<div align="center">
<img aid="1051343" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100647hrnkg88cn8bkkkk7.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100647hrnkg88cn8bkkkk7.jpg" width="600" id="aimg_1051343" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100647hrnkg88cn8bkkkk7.jpg" referrerpolicy="no-referrer">
</div><br>
视锥剔除我们也进行了一些改进，主要是在视锥剔除过程中加了基于屏占比的剔除，还有就是我们光子技术中心的小伙伴对视锥裁剪做了一个基于分区改进，简单来说就是把场景对象进行分区管理和剔除，也有不错的收益。<br>
<br>
<div align="center">
<img aid="1051344" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100649clyjknoz3fkz1oey.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100649clyjknoz3fkz1oey.jpg" width="600" id="aimg_1051344" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100649clyjknoz3fkz1oey.jpg" referrerpolicy="no-referrer">
</div><br>
在刚才说到那些剔除方案的基础上，我们发现还是有大量三角形是没有像素贡献的，甚至profile还发现还有大量无效的Drawcall被提交了，进一步分析发现Apex场景有非常多大型的模型。<br>
<br>
大家可以看一下右图，我们场景里有大量这种巨型山体，还有很多类似尺寸的Landmark，这部分物体通常都有非常大的BoundingBox，很难被现有的剔除管线有效地剔除，比如说如果BoundingBox几百米的时候，就很容易和我们的视锥产生相交，哪怕它是一个像素一个三角形，都是不可见的。特别是我们很多模型的遮挡关系也很复杂，比如右下图这种细小的缝隙，会导致后面大量模型无法剔除。所以我们需要有一个更细粒度的剔除管线。<br>
<br>
首先想到的方案当然是PC和主机上早已流行的GPU Dirven，但是这是我们的一个基础问题，也就是几乎所有机型都要能够兼容，这样的话 ComputeShader的兼容性又是一个不可避免的问题。还有我们光子技术中心也在这方面有非常多的一些探索，发现目前海外主流的设备还是不太合适大规模地使用GPU Dirven，部分机型还是负优化。<br>
<br>
其次也存在一些不那么激进的组合方案，比如美术用工具拆分模型，再用HLOD把它们组合起来，也能一定程度降物体的剔除粒度，进而改进剔除效率。但是对Apex这种场景重载的项目来说，需要特别多的对象和内存来管理这些模型，同时对于美术也不太友好。<br>
<br>
<div align="center">
<img aid="1051345" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100650kjpdg3jzgaol85o5.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100650kjpdg3jzgaol85o5.jpg" width="600" id="aimg_1051345" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100650kjpdg3jzgaol85o5.jpg" referrerpolicy="no-referrer">
</div><br>
为了更好地解决刚才说的那些问题，我们在GPU Dirven和Meshlet的启发下开发了一套基于三角形簇的剔除管线。可以看一下右图，我们会自动的把模型所包含的三角形……[00:47:45]根据空间位置分簇，在运行时进行非常细粒度的视锥剔除和遮挡剔除，并且在我们不断的优化下，这个剔除管线已经适用于场景里的绝大部分模型。<br>
<br>
整个剔除管线是基于CPU的，几乎没有兼容性问题。我们在所有设备都开启了此功能。并且针对不同设备的特性，还配置了不同的剔除粒度级别。<br>
<br>
整个过程只需要极少数的CPU和内存消耗就可以完成，而由于可以剔除更多的Drawcall，对于整个CPU而言往往还是正向的优化。<br>
<br>
<div align="center">
<img aid="1051346" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100651j0ee0tb0uebazz40.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100651j0ee0tb0uebazz40.jpg" width="600" id="aimg_1051346" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100651j0ee0tb0uebazz40.jpg" referrerpolicy="no-referrer">
</div><br>
下面我大体介绍一下这个新的剔除管线。刚才说了，整个管线是基于CPU的，主要分两个阶段：<br>
<br>
首先会在模型DDC数据生成的时候，分析三角形空间结构来生成簇信息，这样就有了大量廉价的计算资源来计算更合理簇的结构，而且也不太会影响一般项目的打包时间。<br>
<br>
然后运行时在常规剔除之后，会根据模型里簇的BoundingBox再次进行更细粒度的剔除。簇的视锥剔除当然就可以直接在CPU完成，刚才也说到我们是基于软光栅来做遮挡剔除的，簇的遮挡剔除自然也能基于软光栅的深度Buffer来进行遮挡查询。<br>
<br>
整个管线是全自动的，美术基本上无需关心也没有感知，就更不容易犯错了。<br>
<br>
<div align="center">
<img aid="1051347" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100651ybo191pkixdojk8z.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100651ybo191pkixdojk8z.jpg" width="600" id="aimg_1051347" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100651ybo191pkixdojk8z.jpg" referrerpolicy="no-referrer">
</div><br>
更详细的原理，我们先从数据结构开始，可以看一下右图，为了提高剔除效率和更好的伸缩性，这里使用的是二叉层级簇。这个球会被拆分成H1/H2两个层级，每个层级都会把父级簇拆分成两个子簇。父级簇包含子簇的所有三角形，自然而然Bounding Box也会有这样的包含关系。在运行时如果发现父级簇是不可见的或者全可见的，就可以无需继续遍历子簇，直接复用父级簇的可见状态就行了。<br>
<br>
<div align="center">
<img aid="1051348" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100652in7z702zht00h00p.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100652in7z702zht00h00p.jpg" width="600" id="aimg_1051348" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100652in7z702zht00h00p.jpg" referrerpolicy="no-referrer">
</div><br>
在DDC数据生成时，我们对IndexBuffer进行了重排序，使得所有簇所包含三角形在IndexBuffer中都是连续的段，这个段我们称之为Section，这样我们就能在运行时通过Section的Begin和End来提交任意簇的Drawcall，并且借助Mesh中已有的IndexBuffer再附加极少量Metadata，就能存储大量三角形和簇的信息。<br>
<br>
运行时主要过程是基于MeshDrawCommand管线，关键流程在常规剔除之后的MeshPassSetup线程处理。我们在MeshDrawCommand里添加了对Cluster元数据的引用，在VisibleMeshDrawCommand上加了少量字段来代表剔除后可见的Section列表，这样就可以和虚幻整个渲染管线串起来。<br>
<br>
具体在剔除过程中，我们使用深度优先遍历层级簇进行可见性测试，这个过程中包含视锥剔除和遮挡剔除。如果簇的Bounding Box因为在视锥外，或者软光栅Buffer测试后是不可见的，也就意味着所有子簇都是不可见的，就没必要往下进行深度的遍历。<br>
<br>
我们又进一步改进了视锥剔除算法，使得检测的时候也能判定 簇的Bounding Box 是否全在视锥内，如果全在视锥内，就意味着所有子簇就都在视锥内了，子簇自然就无需进行视锥检测了。剔除完毕后就会把可见的Section存储到VisibleMeshDrawCommand的可见列表里，后续就可以直接提交了。<br>
<br>
基于簇的剔除在Apex落地之后还是有着不错的性能提升，大家看右侧是我们场景某处的截图，右下侧是这个视角下Culling后冻结渲染状态的视图，可以看到左边没开启Cluster Culling的时候会有大量视锥外的三角形被提交，开启后就能够比较有效地剔除了。<br>
<br>
下图的表格是分别在地图各种视角下的剔除数据，其中在空中的时候效果最差，但是三角形剔除率大部分时候也能达到30%以上。Drawcall也有极少量的优化。比较好的情况是在街巷和室内，有时候甚至达到超过60%的三角形剔除率和5%-10%的Drawcall剔除率，这方面也是Apex的主战场。<br>
<br>
<div align="center">
<img aid="1051349" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100654fv1dldzvr4dq6d32.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100654fv1dldzvr4dq6d32.jpg" width="600" id="aimg_1051349" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100654fv1dldzvr4dq6d32.jpg" referrerpolicy="no-referrer">
</div><br>
从耗时来看是非常少的，我们基本都是控制在0.5ms以下，而由于多线程处理也几乎不影响帧时间，并且Drawcall的剔除也能优化CPU的耗时。此外，还需要少量内存来存储簇和一些必要的缓存。由于簇结构的设计，这部分数据的内存占用也是非常少的。<br>
<br>
总结一下渲染优化的这部分内容，主要是四个方面：<br>
<br>
首先场景光照方面，我们继续延用了虚幻官方移动端的光照模型，大量使用Lightmap，灵活使用ILC和Probes来实现相对完备的静态全局光照。<br>
<br>
<div align="center">
<img aid="1051350" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100656yn9u3nce7ns3nqpg.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100656yn9u3nce7ns3nqpg.jpg" width="600" id="aimg_1051350" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100656yn9u3nce7ns3nqpg.jpg" referrerpolicy="no-referrer">
</div><br>
场景内容方面，主要是进行了大量的模型和材质合并，用比较小粒度的关卡来管理对象，再借助LevelLOD来渲染远景，就避免大量Primitive加载到内存里。<br>
<br>
合批方面，我们大量使用HISM，并且进一步扩展了HISM，改进了Drawcall被打断的问题。并且开发了基于Uniform的动态合批机制，相比GPUScene可以更好地适配现代主流移动端设备。<br>
<br>
最后剔除方面，我们除了主流的一些机制优化外，还开发了更为激进的基于簇的剔除管线，并且有一些不错的效果。<br>
<br>
前面分享的是关于场景渲染部分的内容，接下来给大家分享一下RenderPass这部分的优化。了解GPU优化的同学应该都知道，RenderPass的优化在基于TBR架构的移动端GPU上特别重要，其主要原因是因为RenderTarget的Load/Store会导致非常高的带宽开销，而且对GPU并行性也不友好。<br>
<br>
这一部分会先大致介绍一下UE4在Mobile上的RenderPass情况，然后我们在这基础上做了哪些改进，最后会跟大家分享一下我们新的HDR管线。<br>
<br>
我们是基于UE4 Mobile forward 的管线，这里大致先介绍一下forward的管线。其中HDR部分，大家可以看一下右图，大体的流程是：首先在HDR空间里的BasePass 做 Shading，然后经过一个多Pass的后处理合并到LDR空间，最后画UI。<br>
<br>
<div align="center">
<img aid="1051351" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100656x8i3ig8dgg95x99h.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100656x8i3ig8dgg95x99h.jpg" width="600" id="aimg_1051351" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100656x8i3ig8dgg95x99h.jpg" referrerpolicy="no-referrer">
</div><br>
上图是后处理详细展开后的流程（完整的后处理流程的功能很多，这里只说一下常用的功能）。从BasePass输出开始，主要会分三条路径，最上面是多Pass的 bloom，中间是人眼自适应，下面是Tonemapping和调色的LUT的Pass，然后一起汇集到Tonemap Pass来合并最终到LDR的效果。<br>
<br>
<div align="center">
<img aid="1051352" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100657dy6ylkruyat61iry.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100657dy6ylkruyat61iry.jpg" width="600" id="aimg_1051352" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100657dy6ylkruyat61iry.jpg" referrerpolicy="no-referrer">
</div><br>
可以看到完整HDR管线的Pass是非常复杂的，我们都知道在移动设备上切换Pass的成本非常高，所以UE4官方也提供了LDR的管线，用于适配更低端机器。<br>
<br>
<div align="center">
<img aid="1051353" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100700qs1y3aoozaey61v3.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100700qs1y3aoozaey61v3.jpg" width="600" id="aimg_1051353" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100700qs1y3aoozaey61v3.jpg" referrerpolicy="no-referrer">
</div><br>
LDR就非常简单了，整个管线从BasePass到UI始终都是在 Back-buffer就能完成，无需其他RenderTarget，自然也就没有Load/Store的开销。当然，LDR功能也是非常简单的的，只能支持在BasePass里做一下Gamma矫正，没有Tonemapping，更没有其他后处理效果。<br>
<br>
为了进一步提升移动端性能，我们改进了HDR管线。主要分三个点：首先我们对Bloom进行了分帧优化，减少了两个Pass和不少指令；然后对Tonemapping部分，我们取消了之前依赖LUTPass的计算流程，而是采用拟合ACES曲线的方法来处理，稍后也会详细介绍；再就是自动曝光也就是人眼自适应部分，我们也<br>
<br>
会使用基于PixelShaderPass的方案，并且也添加了分帧优化。<br>
<br>
<div align="center">
<img aid="1051354" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100703n36x132616kcj15e.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100703n36x132616kcj15e.jpg" width="600" id="aimg_1051354" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100703n36x132616kcj15e.jpg" referrerpolicy="no-referrer">
</div><br>
具体来看一下Tonemapping这部分，虚幻目前默认的Tonemap是Flimic Tonemapping，这个公式本身的计算特别复杂，刚才也说了虚幻是通过缓存到LUT里还做优化的。但是这样有两个小问题：首先需要有一个额外的Pass去画LUT，然后就是LUT的UVW，就是最终合到LDR的时候，要通过UVW采样LUT贴图，UVW就是场景的颜色，在色彩丰富的时候，采样时地址的跳变是特别厉害，对GPU Cache不太友好。<br>
<br>
<div align="center">
<img aid="1051355" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100707eh4vx0xnzixqnn0p.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100707eh4vx0xnzixqnn0p.jpg" width="600" id="aimg_1051355" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100707eh4vx0xnzixqnn0p.jpg" referrerpolicy="no-referrer">
</div><br>
我们是选择将UE4 Filmic的曲线拟合到以经典ACES为基函数的曲线上，这样做有几个好处：首先Filmic参数是可以复用的，也就是美术能继续用Filmic空间的参数和调整效果；拟合是预计算好的，运行时只需要少量指令就可以达到不错的效果。<br>
<br>
再来看一下自动曝光部分。刚才也说了，我们是基于Pixel Shader Pass的，用1/64 和 1x1 两个pass来统计屏幕空间的亮度和计算自适应过程。在开启Bloom的时候，我们会借助Bloom Pass的输出来生成初步的亮度统计贴图，就是刚才60分之一的pass，没开启就直接用BasePass输出的SceneColor。<br>
<br>
考虑到自动曝光亮度变化对实时性的要求是很低的，我们这里简单的做了个分帧优化，每一帧只需要额外的一个pass就能完成人眼自适应了。<br>
<br>
我们来简单Review一下针对HDR管线的修改，下图左右两边分别是UE4官方的HDR和我们改进后的 Render Pass细节图：<br>
<br>
<div align="center">
<img aid="1051356" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100710xm8vguyqc22ovunc.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100710xm8vguyqc22ovunc.jpg" width="600" id="aimg_1051356" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100710xm8vguyqc22ovunc.jpg" referrerpolicy="no-referrer">
</div><br>
首先我们对Bloom加了分帧处理，减少了两个Pass；<br>
<br>
其次我们使用拟合的方法做Filmic Tonemapping，不再需要额外LUT Pass，而且运行时只需要少数指令就能达到不错的效果；<br>
<br>
最后我们也用了基于PixelShader Pass的方案来做自动曝光，并且进一步减少了Pass数量。<br>
<br>
<div align="center">
<img aid="1051357" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100714uz7b7g972gbdu44d.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100714uz7b7g972gbdu44d.jpg" width="600" id="aimg_1051357" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100714uz7b7g972gbdu44d.jpg" referrerpolicy="no-referrer">
</div><br>
针对LDR我们也做了一些修改，主要是为了保持HDR和LDR的效果一致性，并且改进后的Tonemapping也足够的简单，我们在LDR的BasePass也做了Tonemapping。另外和CODM一样，我们也在LDR下加了基于ILC的自动预曝光调整，这样整个效果和HDR就更为接近了。<br>
<br>
<div align="center">
<img aid="1051358" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100718iuo9z79oqh9yu71y.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100718iuo9z79oqh9yu71y.jpg" width="600" id="aimg_1051358" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100718iuo9z79oqh9yu71y.jpg" referrerpolicy="no-referrer">
</div><br>
虽然我们对HDR管线做了不少改进，但是HDR相比LDR Pass依然很多，所以就导致GPU带宽比较重，特别是在高帧率的情况下，带宽高会导致功耗更高，也更容易发热。为此我们也开发对移动端GPU更为友好的HDR管线，我们称之为Lite-HDR。<br>
<br>
<div align="center">
<img aid="1051359" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100721fubdxhdhbbddko4m.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100721fubdxhdhbbddko4m.jpg" width="600" id="aimg_1051359" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100721fubdxhdhbbddko4m.jpg" referrerpolicy="no-referrer">
</div><br>
Lite-HDR主要设计目标是Back-buffer-only，简单来说在这个管线下，希望从BasePass到UI，始终都是在Back-buffer上进行的，就可以做到不需要额外切换RendeRtarget。通过TBR架构独有的SubPass来做后处理，这样整个管线就无需额外的Load/Store了，对GPU并行性也更为友好。<br>
<br>
<div align="center">
<img aid="1051360" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100724ex0r8v6qc8svn00v.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100724ex0r8v6qc8svn00v.jpg" width="600" id="aimg_1051360" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100724ex0r8v6qc8svn00v.jpg" referrerpolicy="no-referrer">
</div><br>
刚才说到我们对Tonemapping进行了Pass改进，不需要额外的Pass，那现在就可以直接搬到SubPass里。但是Back-buffer有个问题是不支持浮点数格式的RenderTarget，也就是没办法直接存储HDR空间的颜色。<br>
<br>
解决方法有几个，比如用MemoryLess的 MRT 来存HDR空间的颜色，然后在后续的Tonemapping的SubPass里 Fetch MRT 来做后处理，当然在Mali平台可以用Pixel Local Storage 达到类似的效果。还有就是使用HDR32bpp编码方式，这方面虚幻本身也自带了多种编解码方式，简单来说就是可以把场景的颜色HDR空间颜色编码到一个整数空间，这里就不详细说了。<br>
<br>
<div align="center">
<img aid="1051361" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100728r22l21qsp4pls1fc.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100728r22l21qsp4pls1fc.jpg" width="600" id="aimg_1051361" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100728r22l21qsp4pls1fc.jpg" referrerpolicy="no-referrer">
</div><br>
自动曝光，主要依赖ImageStore来做亮度统计，也是分两步，首先在SubPass绘制很多屏幕空间平铺的点，然后在pixel shader把fetch到的亮度通过ImageStore存储到一个小的texture里，就刚才说的60分之一texture里面。第二个pass也用类似的方法，在屏幕上绘制一个小的方块，2x2就好了，然后采样小的texture存储的小图，再做亮度统计存储就可以了。<br>
<br>
<div align="center">
<img aid="1051362" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100732m3o7x1bson9obosb.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100732m3o7x1bson9obosb.jpg" width="600" id="aimg_1051362" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100732m3o7x1bson9obosb.jpg" referrerpolicy="no-referrer">
</div><br>
解决完刚才说的那些问题，LiteHDR基本就完成了。我们在移动设备上测试了一下，LiteHDR相比HDR在移动端确实有着不错的收益，带宽的优化当然是预期内的，还有就是对Last Level Cache的读写也能减少，我们在iOS平台测试发现GPU 耗时也有一些优化。<br>
<br>
当然，Lite-HDR自然也是有不少限制，比如说设备必须支持Frame Buffer Fetch或者类似的机制，像PC和主机的GPU就没法支持，否则我们无法使用任何基于Subpass的机制。目前还不支持Bloom和抗锯齿，当然我们也有一些计划在后续的版本里尝试。<br>
<br>
<div align="center">
<img aid="1051363" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100735v8f988fmtyi8imee.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100735v8f988fmtyi8imee.jpg" width="600" id="aimg_1051363" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100735v8f988fmtyi8imee.jpg" referrerpolicy="no-referrer">
</div><br>
简单小结一下：首先对原有HDR管线做了一些改进，保持了UE4原有的效果，同时减少了GPU带宽和指令，然后在LDR通过添加极少量指令来提升效果。<br>
<br>
另外我们针对移动端GPU，添加了全新的LiteHDR管线，除了少数特性不支持外，保留了HDR管线几个主要的特性，这样我们在大部分有条件跑LiteHDR的设备上能获得更好的性能。<br>
<br>
<div align="center">
<img aid="1051364" zoomfile="https://di.gameres.com/attachment/forum/202208/25/100739svhq0q553j2h3dah.jpg" data-original="https://di.gameres.com/attachment/forum/202208/25/100739svhq0q553j2h3dah.jpg" width="600" id="aimg_1051364" inpost="1" src="https://di.gameres.com/attachment/forum/202208/25/100739svhq0q553j2h3dah.jpg" referrerpolicy="no-referrer">
</div><br>
最后总结一下今天分享的内容：场景渲染优化部分主要是介绍了一下我们针对场景渲染的一些常规优化，以及已有方案的使用和改进；然后详细分享了一下我们的合批机制和基于三角形簇的裁剪管线。<br>
<br>
Render Pass部分，主要介绍了我们基于UE4现有管线的一些改进，也详细分享了我们针对移动端GPU设计的LiteHDR管线。<br>
<br>
很多人说渲染优化其实并不难做，发现哪里消耗大直接砍掉就行了。但是可以看到我们还是为了更好地保持还端游原度，往往会在确保品质的前提下寻求更好的渲染策略，或者开发对美术需求和手机硬件平台更为有效的优化机制，而且确实也取得了还不错的效果。<br>
<br>
谢谢大家。<br>
<br>
<strong><font color="#de5650">主持人：感谢陈玉钢带来的精彩分享，关于以上的议题，线上观众向您提出一些问题，请您解答。</font></strong><br>
<br>
<strong>陈玉钢：</strong>第一个问题是，刚才说到的那个剔除后，会不会导致有大量的额外Drawcall？<br>
<br>
确实会有这样的问题，从几个方面：<br>
<br>
首先我们知道额外的Drawcall通常是不需要切状态的，什么意思呢？比如说我们不需要重新绑定texture，不需要切Uniform，它其实就只需要一个APIcall就可以完成，所以通常来说它不会有特别大的，可能没有大家想象中这么大CPU的压力。<br>
<br>
另一方面，刚才篇幅有限，其实我们会在culling之后，我们会合并剩下的Visible Section，我们会设置一个阈值，如果是小于这个阈值的，比如说发现Visible Section的gap之间是小于这个阈值的，我们会把invisible 这一段合并起来，合并起来之后这个Drawcall就可以比较好去优化，我们测试来基本上都是对整个Drawcall的数量来说都是正向的优化。<br>
<br>
第二个问题，Bloom分帧会不会容易有一些渲染错误？<br>
<br>
看怎么分帧，我们会把中间两个比较低频，也就是说分辨率比较低的那两个pass做分帧，高频的不做分帧。<br>
<br>
另外还有一点，我们通常Apex里面跑的是帧率比较高的时候，在帧率比较高的时候，比如说40、50帧的时候，很难发现中间比较低频的两个Pass分帧有什么肉眼可见的错误，是基本上看不太出来的。<br>
<br>
我的回答就到这里。<br>
<br>
  
</div>
            