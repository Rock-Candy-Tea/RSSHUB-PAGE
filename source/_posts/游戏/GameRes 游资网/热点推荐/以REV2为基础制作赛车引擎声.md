
---
title: '以REV2为基础制作赛车引擎声'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202110/20/151218c3sbwqtlstnjyhcz.jpg'
author: GameRes 游资网
comments: false
date: Wed, 20 Oct 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202110/20/151218c3sbwqtlstnjyhcz.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2517055">
汽车引擎声一直是游戏声音设计工作中难度比较大的部分，难度主要来自以下几个方面：<br><br><strong>1、音频品质要求高，采集难度大。</strong><br><br>
竞速游戏这个细分品类已经有了不短的历史，引擎声在该类游戏中尤为重要，各家竞速游戏大厂在这方面都各怀绝技，甚至不乏为竞速游戏单独开发游戏引擎的厂家，高端竞速游戏在不断的拔高玩家对于音频品质的要求。且此类音频的原始素材获取难度较大，高端车型价格昂贵，即使只是租来进行录制，也是一笔不小的花费。录制的过程也不是录音棚里架几只话筒就可以搞定的，对场地和录音手法都有非常高的要求。<br><br><strong>2、发生机制复杂多变。</strong><br><br>
一辆车在行驶时会有非常多的部件同时发出声音，且各自发声的原理和变化趋势都不尽相同，想要做好车辆的声音，不仅需要扎实的游戏音频设计制作功底，同时要需要对汽车的机械原理进行研究，理清楚内燃机、传动轴、离合器、变速箱、涡轮、悬挂、排气管等等东西的工作原理和工作方式，才可能在游戏中模拟出自然的汽车声。<br><br><strong>3、游戏中对于音频的交互性要求非常高</strong><br><br>
游戏中车辆的声音需要随着游戏的进程，车辆的状态，玩家的操作实时变化，且符合物理规律和听觉习惯。但是游戏中的声音大部分都基于采样——存储——触发——播放这一简单的逻辑来运行，声音采样的内容都是固定的。虽然现在的游戏声音引擎大多提供了可控采样、可控音高、可控滤波等等改变声音的方式，但是这些手段依然难以满足竞速游戏日益高涨的音效品质需求。<br><br>
4、一个良好的赛车游戏对于音频程序的要求很高，发动机声音的制作需要一个可以模拟发动机工作原理的程序内核作为基础，且该程序内核可以提供各种模拟真实车辆运行时各种细节变化的参数供音频引擎使用才可以。<br><br>
最近一段时间，笔者出于个人兴趣对Wwise内提供的车辆引擎插件REV2进行了一些简单的研究，结合UE4的赛车游戏模板搭建了一个Demo，其实机效果还算不错，为低成本制作拟真赛车声提供了可能，现在将制作过程和效果和大家分享。<br><br><div align="center">
<span id="flv_I99"></span>
</div>
<br><strong><font color="#de5650">一、REV插件简介</font></strong><br><br>
REV是Wwiss的合作友商CRANKCASE AUDIO推出的一款插件，其本质是一个专门针对车辆引擎声的粒子合成器。关于REV的背景和详细参数大家可以参阅REV的用户手册，每个下载了REV插件的用户都可以在这里找到它。<br><br><div align="center">
<img id="aimg_1016133" aid="1016133" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151218c3sbwqtlstnjyhcz.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151218c3sbwqtlstnjyhcz.jpg" width="513" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151218c3sbwqtlstnjyhcz.jpg" referrerpolicy="no-referrer">
</div>
<br>
为了方便大家理解后续的文章，此处我们简单介绍下REV的几个关键参数及其使用方法：<br><br><div align="center">
<img id="aimg_1016134" aid="1016134" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151218da0aaipnaerur3g7.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151218da0aaipnaerur3g7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151218da0aaipnaerur3g7.jpg" referrerpolicy="no-referrer">
</div>
<br>
该截图包含了使用REV最关键的几个选项和参数。蓝色方框为目前载入的发动机采样模型。Import Model键可以切换其他模型载入。REV官方提供了很多现成的高质量采样可以直接使用，只要取得授权就可以直接运用到自己的游戏里。<br><br>
红色方框为控制REV发声的所有所需参数，发动机声音的所有变化均通过这几个参数控制来实现：<br><br><ul>
<li>
<strong>Throttle：</strong>油门，可以模拟不同油门大小下发动机的声音变化。</li>
<li>
<strong>Gain：</strong>发动机音量，可以控制总体发动机音量的大小。</li>
<li>
<strong>RPM：</strong>发动机的转速，用来控制声音随着发动机转速而改变。</li>
<li>
<strong>Gear：</strong>档位，配合车辆的换档操作。</li>
<li>
<strong>Velocity：</strong>车辆的速度，用来控制声音随着车辆速度发声改变。<br>
</li>
</ul>
<br>
然后，我们需要为这些参数建立各自对应的Game Parameters。比如像这样：<br><br><div align="center">
<img id="aimg_1016135" aid="1016135" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151219n6qz5htubm4u6l4h.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151219n6qz5htubm4u6l4h.jpg" width="249" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151219n6qz5htubm4u6l4h.jpg" referrerpolicy="no-referrer">
</div>
<br>
然后将这些RTPC全部对应起来：<br><br><div align="center">
<img id="aimg_1016136" aid="1016136" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151219ed6etf8v8kqv6ueb.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151219ed6etf8v8kqv6ueb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151219ed6etf8v8kqv6ueb.jpg" referrerpolicy="no-referrer">
</div>
<br>
这样，REV就可以接受游戏引擎发出的参数，从而实时模拟游戏中车辆的状态发声了。接下来，我们建立一个引擎声的事件并把它导入UE4。<br><br><strong><font color="#de5650">二、在UE4中调用REV的声音</font></strong><br><br>
打开一个UE4的高级载具模板工程，然后打开载具蓝图，观察其声音设置。可以发现它的声音设置非常简单，只是挂接了一个通过载具前进速度调制的发动机loop声，其表现力非常的一般。<br><br><div align="center">
<img id="aimg_1016137" aid="1016137" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151220w55aeuuc5qekoe5z.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151220w55aeuuc5qekoe5z.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151220w55aeuuc5qekoe5z.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<span id="flv_Umn"></span>
</div>
<br>
我们将这个声音去除，添加Wwise的声音，并修改参数的设置，不仅仅读取速度，同时也读取车辆的档位和发动机转速，且将这些数据发送RTPC。<br><br><div align="center">
<img id="aimg_1016138" aid="1016138" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151221kop5kppjjzkwpkfn.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151221kop5kppjjzkwpkfn.jpg" width="595" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151221kop5kppjjzkwpkfn.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1016139" aid="1016139" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151221ojis0002wi2r2liw.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151221ojis0002wi2r2liw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151221ojis0002wi2r2liw.jpg" referrerpolicy="no-referrer">
</div>
<br>
然后UE4就开始读取和调制Wwise的声音，我们可以得到了如下效果：<br><br><div align="center">
<span id="flv_BuP"></span>
</div>
<br>
由于REV本身的声音品质比较优秀，引擎声的质感的确提升了。但是，总体的听感依然不佳，且出现了一些非常不符合现实情况的听感。比如，在达到高速状态后，发动机转速就保持5700转不动了，因为发动机转速不再变化，声音也就没有了变化，高速状态下的声音机械感非常重。这种情况在现实世界中是绝对不会出现的，发动机不可能保持一个固定转速纹丝不动。且因为所有内燃机都是有转速保护机制，当超过最大转速后会强制中断油料供给，俗称“断油”。所以为了避免这种非正常发声，我们需要对声音的发声机制进行优化。<br><br>
想要解决这个问题其实并不简单，因为它不是简单的调整一两个参数就可以解决的，我们需要暂时先从游戏引擎中跳脱出来，总体的了解一下内燃机的工作原理，才能够找到正确的解决该问题的方法。<br><br><strong><font color="#de5650">三、汽车引擎发声机制详解</font></strong><br><br>
本段落我们将会对车辆的动力结构和运行原理进行介绍，主要包含内燃机、离合器、变速箱这三个部分。<br><br><strong>1、内燃机</strong><br><br>
内燃机的家族其实十分庞大，细分种类也非常多，如果全部详解介绍其工程结构及其种类划分等将是一个非常巨大的工程。所以此段落我们只简单的介绍其工作原理。其他的全部忽略。后期需要针对车辆做细分的时候再去了解发动机的缸数、冲程数亦或者是转子发动机这类的特殊概念也不迟。<br><br>
以最常见的往复活塞式内燃机为例。雾状的汽油和空气的混合物从进气口进入，被火花塞点燃，推动活塞向下，驱动转子，然后排气口打开，活塞向上，将燃烧后的废气排出，进入下一次循环。这就是内燃机的工作流程。<br><br><div align="center">
<img id="aimg_1016140" aid="1016140" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151222pdrrkyki7gidrmcl.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151222pdrrkyki7gidrmcl.jpg" width="418" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151222pdrrkyki7gidrmcl.jpg" referrerpolicy="no-referrer">
</div>
<br>
在这一个流程中有三个参数和游戏的声音制作息息相关——油门、发动机转速和扭矩。<br><br>
油门和大家都比较好理解，油门越大，进入内燃机内部的燃油就越多，点燃后的燃烧就越剧烈，产生的动力就越大。<br><br>
发动机转速也非常好理解，一般游戏里影响车辆声音变化的最主要参数，就是发动机转速。<br><br>
但是扭矩这个参数，大多数对于内燃机工作原理不太了解的人很容易将之忽略。或者简单的将它理解为发动机动力的大小，认为它和油门、发动机转速是成正比关系的。这样的认知其实是有偏差的。<br><br>
扭矩是用来表示内燃机完成一次完整的循环所输出动力的大小，用一个不算严谨，但是易于理解的公式来讲的话就是：<br><br>
扭矩*发动机转速=发动机动力<br><br>
在这里我要强调两个常见的误区：<br><br>
误区一：发动机转速越快，扭矩越大。<br><br>
错，随着发动机转速的提升，在超过一定的阈值后，扭矩反而会变小。<br><br>
误区二：发动机转速越快，发动机功率越大，输出动力越大。<br><br>
错，中低转速时，发动机功率的确是随着转速上升的，但是在达到高转速后，发动机功率会随着转速的提升而下降。<br><br>
为了方便大家更好的认识扭矩、功率和发动机转速之间的关系。这里提供了一个图示，分别为涡轮增压发动机和自吸气发动机的工况图。<br><br><div align="center">
<img id="aimg_1016141" aid="1016141" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151222tubik3blivpui6bp.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151222tubik3blivpui6bp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151222tubik3blivpui6bp.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1016142" aid="1016142" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151223vz08t8086y1t6izw.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151223vz08t8086y1t6izw.jpg" width="364" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151223vz08t8086y1t6izw.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">大众EA211 1.4TSI发动机扭矩输出图</font></font></div>
<br>
对于不太熟悉内燃机的朋友来说，以上两点有那么一点反直觉，但是对于有一定车辆驾驶经验的朋友们来说，以上两点不难理解。<br><br>
所有车主在高速公路上驾驶车辆时，都会选择一个合适的档位，保持发动机的转速处于中高区间，每次的升档操作也都是在发动机转速稍微偏快之后，而不是等发动机转速顶满再升档。因为并不是发动机转速越快产生动力越大，所以一旦发动机转速超过了能够输出最大动力的节点，那么这个时候就应该换挡了，保持发动机始终处于动力输出较大的区间，就可以在消耗相同燃料的情况下跑更远的距离，这种做法俗称“省油”。但某些竞速游戏中可能出现发动机接近顶满再换挡的现象，原因下文再叙。<br><br>
根据我们上文的分析，我们就可以找到上一段游戏视频中车辆出现发动机转速顶满的原因——扭矩变化设置不合理或车辆阻力设置不合理。<br><br>
正常竞速游戏中，在车辆接近最高速时，发动机转速应该处于功率输出最大值对应的转速，该转速通常大约为最大转速的90%-95%左右。超过该转速后发动机单位时间内提供的动力会下降，所以无法继续提速。游戏中应当设置合理的发动机扭矩或功率曲线，以模拟该效果，否则发动机的声音变化就不符合真实车辆的运行逻辑，从而失去拟真感。所以我对UE4车辆蓝图中的扭矩曲线做了如下修改（虽然我们的小白车连车壳都没有，但是也要假装自己有一个涡轮增压发动机）。<br><br><div align="center">
<img id="aimg_1016143" aid="1016143" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151223r9nrr5otw9krnaio.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151223r9nrr5otw9krnaio.jpg" width="403" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151223r9nrr5otw9krnaio.jpg" referrerpolicy="no-referrer">
</div>
<br>
该曲线其实也不严谨，大家可以根据需求调整自己的扭矩曲线。如此调整之后，则不会再轻易到达最大转速。<br><br><div align="center">
<span id="flv_zV5"></span>
</div>
<br>
但是如果这中间还调整过其他的参数，我们可能遇到新的问题。车辆的档位切换不太顺畅，甚至可能出现车辆挂档挂不上去的情况。3档挂4档后会瞬间退回3档。为了解决这两个问题，接下来我们来看车辆引擎里另一个很重要的部件——变速箱。<br><br><strong>2、变速箱</strong><br><br>
变速箱是用来调整发动机转速和车速之间关系的装置。我们可以通过一个极度简化的图来了解变速箱的工作原理，变速箱就是图中右边那个会改变自身大小的齿轮。齿轮越小，发动机转动一周可以驱动汽车移动的距离越远，但是发动机的负载更大。<br><br><div align="center">
<img id="aimg_1016144" aid="1016144" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151224i2q2zm2vkt0055tt.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151224i2q2zm2vkt0055tt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151224i2q2zm2vkt0055tt.jpg" referrerpolicy="no-referrer">
</div>
<br>
因为变速箱的存在，不同档位下相同的发动机转速可以获得不同的车速，这样我们就可以通过换挡让发动机一直保持在高功率转速区间工作。在游戏引擎中，每个档位的参数通常使用“齿轮比”来调节，看完上图后，齿轮比的含义想必大家也都很清楚了。<br><br>
我们可以看一下UE4的变速箱设置，可以简单解释一下这里的几个参数的作用。<br><br><div align="center">
<img id="aimg_1016145" aid="1016145" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151224l0c33py11d1ad15k.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151224l0c33py11d1ad15k.jpg" width="402" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151224l0c33py11d1ad15k.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">（注：该图里的参数数值也仅为针对演示demo的调节，可以根据游戏和手感需求选择其他的数值。）</font></font></div>
<br>
自动变速——勾选与否决定了车辆是自动切换档位，还是玩家操作手动切换档位。<br><br>
齿轮切换时间及齿轮自动盒体延迟——控制换挡过程的时长。<br><br>
最终比——该值会同时影响所有档位，取值越小，车辆可以达到的最高时速越大，同时车辆的负载越大。<br><br>
齿比——每个档位发动机转速和车速之间的比值，值越小相同发动机转速下车速越快，负载越大。<br><br>
上齿比——自动变速模式下，当发动机转速达和最大转速的比值大于该值时触发升档。<br><br>
下齿比——自动变速模式下，当发动机转速达和最大转速的比值低于该值时触发降档。<br><br>
理解了变速箱的原理和游戏中引擎中的相关设置之后，我们就可以解决之前遇到的问题了。<br><br>
如果自动变速的车辆换挡时机不对，那么原因是各档位齿轮比设置的不合理。比如如果各档位的齿轮比设置都是一样的话，那么每个档位的加速度都是相同的，就没有了档位之间的区别。<br><br>
如果出现挂挡失败，反复升降档位的情况，那么原因就是两个档位之间齿轮比差异过大，或者车辆发动机扭矩不足，导致升档后发动机负载过大无法继续提速，从而转速下降又触发了降档。<br><br>
另外，还有一个部件对于控制车辆档位切换至关重要，那就是离合器。<br><br><strong>3、离合器</strong><br><br>
关于离合器的结构和工作原理，我们同样用一个极简的图示来解释：<br><br><div align="center">
<img id="aimg_1016146" aid="1016146" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151224phye8zb9s8dvy8jv.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151224phye8zb9s8dvy8jv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151224phye8zb9s8dvy8jv.jpg" referrerpolicy="no-referrer">
</div>
<br>
离合器的主要功能是控制内燃机和变速箱的结合，其最大的优点是可以控制结合的力度，可以缓慢的结合到一起，也可以缓慢放开，就算发动机转速很快的时候进行结合和松开的操作也不会产生机械损伤。离合器如何做到这一点，我们暂时不用深究。对于音频设计师来说我们需要明白的是——离合器控制动力的传输和换挡机制的触发。<br><br>
在驾驶模拟游戏中，非核心玩家一般是不会使用手动离合的，且在非拟真驾驶类游戏中，甚至玩家可能无法控制离合。玩家的操作只有油门、转向、刹车。档位切换就全部交给自动变速机制了。那么我们需要设计一个符合现实车辆运行逻辑的离合机制。但是如果细究离合的运用方法，可能较为复杂。所以我们简化一下：当发动机给车辆输出动力的时候，离合就应当闭合。当发动机停止给车辆输出动力时离合就应当打开。在UE4的demo中我们可以直接使用油门来控制离合，其他非驾驶模拟类游戏也可以采用这种方法。<br><br><div align="center">
<img id="aimg_1016147" aid="1016147" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151224e8zpf4pr1r18v48w.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151224e8zpf4pr1r18v48w.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151224e8zpf4pr1r18v48w.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1016148" aid="1016148" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151225zixz222sssizz2ml.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151225zixz222sssizz2ml.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151225zixz222sssizz2ml.jpg" referrerpolicy="no-referrer">
</div>
<br>
UE4中自身的载具模块也是同样的运行逻辑，当你松开油门，车辆自然减速，发动机转速下降是不会触发降档机制的，会一直下降到0。为了方便大家更好的理解离合的开闭对于声音表现的影响，我们可以通过视频来对比一下不同情况下的声音表现：<br><br><div align="center">
<span id="flv_k9N"></span>
</div>
<br>
在现实生活中，如果离合完全打开下的情况下踩油门，车是不会动的，所以这种情况下匹配行驶的声音效果不佳，换档时的声音质感非常的松软。<br><br>
离合全程闭合的情况下，车辆在自然减速甚至刹车的过程中都会触发升档的声音，这也非常不合理。尤其在刹车时，我们希望车辆尽快停下，当然要断开发动机的动力供给，所以肯定不该通过降档提升发动机转速。<br><br>
如果游戏内的交互逻辑如果可以写的更加精细和复杂，有更加拟真的离合控制逻辑更好。如果没有，那么通过油门控制离合是一种简易且有效的方法。了解完离合器的工作原理以及它对声音的影响后，我们就可以回到Wwise中来设置离合的参数了：<br><br><div align="center">
<img id="aimg_1016149" aid="1016149" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151225rs7kjqr0j40ssz0k.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151225rs7kjqr0j40ssz0k.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151225rs7kjqr0j40ssz0k.jpg" referrerpolicy="no-referrer">
</div>
<br>
Enableshifting：这个参数就是用来控制离合的，当该参数取值为on，rev就会在档位发声变化时播放档位切换的声音，取值为off就不会触发档位切换声，我们将它和油门的参数绑定在一起，当油门被摁下时，离合就结合。<br><br>
当我们完成了对于档位、离合、发动机参数的所有调整后，我们就可以得到这样的声音。其听感基本符合正常车辆的运行表现。<br><br><div align="center">
<span id="flv_CEz"></span>
</div>
<br>
但是，这只有发动机的声音，其实还缺失了非常多的细节。下一章节我们来给车辆添加更多的声音细节。<br><br><strong><font color="#de5650">四、更加丰富的车辆声音细节</font></strong><br><br>
我们大致可以将车辆声音的发声源拆解为如下几个部分，然后分别探讨他们的做法。<br><br><div align="center">
<img id="aimg_1016150" aid="1016150" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151225m6aysoznsshzs5oq.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151225m6aysoznsshzs5oq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151225m6aysoznsshzs5oq.jpg" referrerpolicy="no-referrer">
</div>
<br>
内燃机、离合器和变速箱部分我们已经在上文讨论了。接下来讨论其他车辆部件的发声规则和制作方法。<br><br><strong>1、胎噪与风噪</strong><br><br>
胎噪的制作以loop采样为主。给loop添加多段随机素材减少重复感，同时增加车辆速度的RTPC来调制loop的音高、音量以及不同强度之间的过渡。而且需要制作不同的地面材质，利用switch来切换。最后如果可以获取车辆轮胎和地面的摩擦系数更好，可以使用该参数来控制轮胎打滑声的触发和变化。我这边偷了个懒，没有计算轮胎和地面的摩擦，固定在刹车和转向时会触发声音。<br><br><div align="center">
<img id="aimg_1016151" aid="1016151" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151226dwwwcw2twyvbtsww.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151226dwwwcw2twyvbtsww.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151226dwwwcw2twyvbtsww.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>2、悬挂</strong><br><br>
悬挂的种类其实很多，我们这里并不详细探讨悬挂的工作原理和种类划分，只探讨它对声音的影响。因为悬挂的本质是一个缓冲减震装置，保证车辆在崎岖不平的道路上行驶时的稳定性。当车辆产生颠簸时，发动机的发声会受到一定的影响，且悬挂会影响车轮受到的压力，导致车辆的负载产生变化。所以这里针对车辆的悬挂系统我们要做两件事：<br><br><ul>
<li>制作会随着悬挂受力情况变化而改变的车身抖动的声音。</li>
<li>使悬挂的抖动可以对发动机和胎噪的发声产生一点影响<br>
</li>
</ul>
<br>
为了完成这两件事，首先我们需要获取车辆的悬挂偏移参数，这里我一共获取了5个RTPC，分别是pianyi1、pianyi2、pianyi3、pianyi4对应四个轮子各自的悬挂偏移，然后将这四个参数求和得到一个总体的偏移量“zhendong”：<br><br><div align="center">
<img id="aimg_1016152" aid="1016152" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151226it5p9sk9tkdml78l.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151226it5p9sk9tkdml78l.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151226it5p9sk9tkdml78l.jpg" referrerpolicy="no-referrer">
</div>
<br>
然后我们需要制作不同力度的车辆抖动声音，并使用偏移程度和车速来同时调制他们：<br><br><div align="center">
<img id="aimg_1016153" aid="1016153" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151227bcbbzv5coc8nvw1t.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151227bcbbzv5coc8nvw1t.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151227bcbbzv5coc8nvw1t.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="left">然后再让悬挂对发动机和胎噪也产生一点影响：</div>
<br><div align="center">
<img id="aimg_1016154" aid="1016154" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151227umfermqqbmjmfewj.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151227umfermqqbmjmfewj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151227umfermqqbmjmfewj.jpg" referrerpolicy="no-referrer">
</div>
<br>
这样就可以制作出随着车辆颠簸而动态变化的声音。<br><br><strong>3、涡轮</strong><br><br>
对于涡轮的原理我们也做一下简单的介绍，其实涡轮就是一个超高转速的风扇，用来增加发动机的进气量，从而使发动机可以在一个冲程之内燃烧更多的燃油，来提升发动机的性能。前文我们讨论扭矩的时候就同时提供了涡轮增压型和自吸型两种发动机的扭矩和功率变化图。涡轮增压发动机更容易达到最大扭矩且保持的时间更长。具体涡轮的工作原理我们就赘述了，我们只关注一个问题——涡轮发出什么样的声音，以及它在什么样的情况下发出声音。<br><br>
涡轮的种类不同，发出的声音会略有差异，不过在游戏中的表现大致都是高频的转子转动声，因为涡轮本身就是一个超高转速的风扇，其转速可以轻松达到每分钟上万转，甚至十万转以上。<br><br>
其发声的区间一般是发动机达到一定转速以后。通常是至少达到2000RPM 以上才开始发挥作用，也只有这个时候涡轮的转速才足够高，其运转的声音才会被人所察觉。且在涡轮的声音可以被察觉后，其声音的变化幅度要小于发动机。<br><br>
发动机转速下降以后，涡轮的声音不一定停止，一些高性能赛车为了避免“涡轮迟滞”，会安装偏时点火装置，保持车辆发动机转速下降后涡轮依然可以继续工作。所以涡轮的声音制作需要根据不同的车辆定制，没有通用解。<br><br>
在我的游戏工程里，我就偷懒了，没有考虑特殊情况，涡轮的触发绑定发动机转速，且并未使用涡轮的采样。而是使用了一个经过处理的电钻的声音来模拟涡轮。<br><br><div align="center">
<img id="aimg_1016155" aid="1016155" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151227yeuzuv4ojo1duve1.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151227yeuzuv4ojo1duve1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151227yeuzuv4ojo1duve1.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>4、排气管</strong><br><br>
对于高品质竞速游戏，排气管在汽车运行时的声音是需要单独制作的，loop拼接过度的做法基本可以满足需求。这里我们着重强探讨一个在游戏中被夸大处理的声音——回火。<br><br>
现实生活中，“回火”一般出现在大排量性能车型上。在游戏里该机制的美术特效和音效表现是提升玩家游戏感的重点机制之一。为了制作好回火的声音，我们需要对回火的发声机制进行一定的分析。引起“回火”的原因，大致可以分为三种：<br><br><ul><li>
<strong>稳定回火</strong><br>
</li></ul>
<br>
发生时机：只发生在车辆高速高负荷运行时。<br><br>
表现特征：尾焰稳定且持续。<br><br>
发声类型：持续且稳定的燃烧声，不会带有爆鸣声。<br><br>
发生原因：某些车型中，为了给三元催化器和发动机气缸降温，会在发动机温度过高（高负载高转速运行时）的情况下，增加气缸内的喷油量，这样气缸内的油气混合物就不能完全燃烧，因为燃油过量了。这些过量的气化燃油会在排气管口遇到空气后继续燃烧，此时赛车的排气管就会有轻微的淡蓝色尾焰。在游戏中这种稳定尾焰通常会用在各种超高速行驶的状态下，如非常常见的氮气加速。<br><br><ul><li>
<strong>爆鸣回火</strong><br>
</li></ul>
<br>
发生时机：发动机进气量严重不足时，通常是高速启动，或者车辆在高负荷行驶状态下突然减小油门的时候。<br><br>
表现特征：尾焰呈现短暂的点状喷射。<br><br>
发声类型：类似爆炸的清脆爆破声。<br><br>
发生原因：由于发动机进气量不足，气缸内的燃油燃烧非常不充分，于是排气冲程时，未烧净的高温汽油随着气流经过了高温炽热的排气头段和三元催化器（再度被加温），高温的气化燃油由于氧气不足无法燃烧。所以当这些废弃来到排气口，接触到外界的新鲜空气的一瞬间就会发声爆燃，继而引发爆鸣回火。<br><br><ul><li>
<strong>偏时点火</strong><br>
</li></ul>
<br>
发生时机：换挡收油之后。<br><br>
表现特征：尾焰持续时间较短但是爆炸感不强。<br><br>
发声类型：排气管的低频轰鸣，闷响。<br><br>
发生原因：竞速赛车中，换挡收油后排气量会降低，导致增压涡轮转速降低，重新加速踩油门的时候会带来涡轮迟滞，为了让赛车获得更好的加速性能。赛车中装备一种名为偏点火系统的装置，英文为"Anti-Lag System"，简称ALS系统。偏时点火是在发动机不需要提供动力时停止点火动作，刻意让油气在排气门开启后进入排气头段。头段温度极高，油气一接触即爆炸，强大的爆炸压力便会推动涡轮机的排气叶片，使得涡轮机内的增压端叶片高速运转，保持增压状态，使车辆即使在低速或是换档收油时不失去增压效果。此类火焰是在发动机内点燃随着排气管排出，所以一般爆破感不强，声音听起来略闷。<br><br>
在我的演示工程中，其实没有单独制作排气管的声音，因为车的模型根本没有排气管，而且我调整的车辆手感并不像高性能赛车，也没有回火特效，所以我就只在发动机转速下降到4100转一下的时候会固定触发一下回火，没有制作其他更加复杂的声音表现。<br><br>
我们来看一下添加完各种细节的车辆声音：<br><div align="center">
<span id="flv_lJn"></span>
</div>
<br>
制作到这里，就基本得到了文章开头处的车辆声音效果。也基本包含了车辆行驶所需的全部声音。如果想要继续提升品质，那么之前提到的所有声音都可以继续找到更加高品质的音频，也可以写出更加严谨的程序来完成更加复杂的控制，有兴趣的朋友们可以继续研究。<br><br><strong><font color="#de5650">五、REV的粒子合成器</font></strong><br><br>
之前的章节基本全都在讨论如何给汽车添加更多的声音，而对于REV本身的使用方法则讨论不多，本章节将给大家简单介绍REV自身的粒子合成功能，也就是如果我们不想用REV官方的采样，要如何自己制作引擎声的粒子模型。<br><br>
首先我们需要准备三段引擎声的采样，分别为怠速状态loop，引擎声从怠速到最高速的匀加速采样和最高速到怠速的匀减速采样，类似这样：<br><br>
然后打开REV的主界面，点击Open in REV.Tool，进入rev的粒子合成器。<br><br><div align="center">
<img id="aimg_1016156" aid="1016156" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151228r7qohq2ioz20s4iu.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151228r7qohq2ioz20s4iu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151228r7qohq2ioz20s4iu.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1016157" aid="1016157" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151228topoepop552kprpo.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151228topoepop552kprpo.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151228topoepop552kprpo.jpg" referrerpolicy="no-referrer">
</div>
<br>
然后点击File——Open wav file。载入我们之前准备好的均加速采样。然后REV会分析采样的共振峰频谱，并显示出来。<br><br><div align="center">
<img id="aimg_1016158" aid="1016158" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151229itto2pfmqejzt4to.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151229itto2pfmqejzt4to.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151229itto2pfmqejzt4to.jpg" referrerpolicy="no-referrer">
</div>
<br>
可以看到频谱略杂乱，这是因为我选择的音频采样不够纯净，其中包含了一定的机械运转声，导致其共振峰变化不够连续，如果可以获得更为纯净的发动机音频采样，效果会好很多。<br><br>
点击auto tag harmonics 在频谱中选择一组共振峰，理论上优秀的采样共振峰是连续的，可以选区中很长的曲线，但是由于我准备的素材不好，所以选取的频谱是断续的。然后点击start cycle tracking，或者切换模式自己手动选择共振峰范围。<br><br><div align="center">
<img id="aimg_1016159" aid="1016159" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151229i3ucn22w6ecw63ry.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151229i3ucn22w6ecw63ry.jpg" width="195" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151229i3ucn22w6ecw63ry.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1016160" aid="1016160" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151229qgj4eracjcjg3jjg.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151229qgj4eracjcjg3jjg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151229qgj4eracjcjg3jjg.jpg" referrerpolicy="no-referrer">
</div>
<br>
完成操作后rev会分析频谱，生成粒子模型，拖动频谱上的线可以试听不同转速下的加速声。<br><br><div align="center">
<img id="aimg_1016161" aid="1016161" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151230f1ap13w6166ww3pp.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151230f1ap13w6166ww3pp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151230f1ap13w6166ww3pp.jpg" referrerpolicy="no-referrer">
</div>
<br>
蓝线上的黑色小圈表示不同的转速节点，调节黑圈的间距可以调节不同转速之间声音的变化范围。<br><br>
之后我们可以放大频谱，使用select cycle调整生成的共振峰曲线，可以将某一段不合理的采样，从我们的整体模型中剔除。<br><br><div align="center">
<img id="aimg_1016162" aid="1016162" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151230t44ebpaeuuspimx6.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151230t44ebpaeuuspimx6.jpg" width="293" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151230t44ebpaeuuspimx6.jpg" referrerpolicy="no-referrer">
</div>
<br>
最后点击file——save partial document。将生成的粒子模型保存下来。再打开我们的减速采样，如法炮制，生成减速采样的粒子模型。完成之后切换到model选项卡。<br><br><div align="center">
<img id="aimg_1016163" aid="1016163" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151230cf3cfm8b3muauccy.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151230cf3cfm8b3muauccy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151230cf3cfm8b3muauccy.jpg" referrerpolicy="no-referrer">
</div>
<br>
把我们之前制作的粒子模型和怠速loop加入进来。点击simulate。就生成了新的完整的车辆引擎声模型。我们可以在simulation页面调整和试听模型的效果，比如音量配比，加减档的时间和音量等。<br><br><div align="center">
<img id="aimg_1016164" aid="1016164" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151231x5tjj888jh3e58db.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151231x5tjj888jh3e58db.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151231x5tjj888jh3e58db.jpg" referrerpolicy="no-referrer">
</div>
<br>
最后点击save，生成我们自己的.model文件。<br><br>
回到rev的插件界面，点击import model，找到我们自己生成的model载入，就可以在游戏里使用我们自己生成的引擎声了。<br><br><div align="center">
<img id="aimg_1016165" aid="1016165" zoomfile="https://di.gameres.com/attachment/forum/202110/20/151231fvw5kmo8klwwws9d.jpg" data-original="https://di.gameres.com/attachment/forum/202110/20/151231fvw5kmo8klwwws9d.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/20/151231fvw5kmo8klwwws9d.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们打包bnk，在UE4中重新构建声音，就可以得到新的引擎声，来跑一下看看效果吧。<br><br><div align="center">
<span id="flv_B08"></span>
</div>
<br><strong><font color="#de5650">结语</font></strong><br><br>
以上就是我个人对于如何使用REV 插件和如果制作汽车声音的相关分享，目前虽然涉及的面较为广泛，但是最终的呈现效果还有待提升。汽车引擎声只是我个人日常工作中很小的一部分，但是由于该类声音的特殊性，我对于这类声音的制作和研究非常有兴趣。期待可以和更多的同行好友多加交流。<br><br><font size="2"><font color="#808080"></font></font><br><font size="2"><font color="#808080">来源：Audiokinetic官方</font></font><br><font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/aZcMDxw6AncojFmEAYVf4g</font></font><br><br><br><br>
</td></tr></tbody></table>


  
</div>
            