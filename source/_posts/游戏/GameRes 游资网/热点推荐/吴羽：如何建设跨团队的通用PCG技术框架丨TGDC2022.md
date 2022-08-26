
---
title: '吴羽：如何建设跨团队的通用PCG技术框架丨TGDC2022'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202208/17/090844b009k60k0d99zs3k.jpg'
author: GameRes 游资网
comments: false
date: Wed, 17 Aug 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202208/17/090844b009k60k0d99zs3k.jpg'
---

<div>   
8月14日-17日，由腾讯游戏学堂举办的2022腾讯游戏开发者大会（Tencent Game Developers Conference）以线上直播的形式为广大游戏开发者带来行业的最新分享。本届TGDC大会以Inspire Six Senses为主题，汇聚国内外顶尖游戏从业者以及学界专家学者，以激发游戏的创意力、想象力、洞察力、科技力、影响力和凝聚力，共同拓宽游戏产业的边界与可能性。<br>
<br>
腾讯互娱 CROS引擎技术总监吴羽，带来《如何建设跨团队的通用PCG技术框架》的分享。吴羽多年致力于游戏引擎架构设计开发工作，并在图形学和算法、高性能计算、数据库技术领域有资深经验。<br>
<br>
<div align="center">
<img aid="1050250" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090844b009k60k0d99zs3k.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090844b009k60k0d99zs3k.jpg" width="600" id="aimg_1050250" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090844b009k60k0d99zs3k.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>以下是吴羽的分享：</strong><br>
<br>
我是来自腾讯互娱CROS中台的吴羽，很荣幸代表团队介绍腾讯游戏中台在程序化生成领域，对跨团队的通用PCG技术框架的探索。首先看一段视频，大家可以想想，这样的高质量、丰富、广阔的世界，需要投入多大的游戏团队，花费多长时间才能制作出来呢？<br>
<br>
对我来说，这个问题的答案，在过去五年中发生了非常大的变化。记得在2016年的时候，要做一个8000米x8000米的自然场景。当时投入了超过100人的美术团队，通过分片包干的方式，用了整整一年的时间才搞定了这样一个场景。<br>
<br>
而在2017年又有了重大的改变，在2017年的GDC上，随着十多场关于PCG技术的演讲，一下子把PCG这个通过算法和规则的方式来自动化地生成美术资源和场景的技术，迅速地普及到整个中国游戏行业中。记得在2017年下半年，我组建了一个有2个TA加8个场景美术的团队，通过PCG技术，仅仅用了半年的时间，就完成了同样质量的一个场景，这个效率提升是非常巨大的。也是从这个时间开始，逐渐看到很多大世界的项目获得了立项。可见PCG技术在游戏，特别是美术生产的领域，有一个非常重要的地位。<br>
<br>
到现在，通过研发通用化的PCG框架，我们发现在这个基础上还能够再有三到四倍的效率提升。其中的原因是，我们从技术中台的角度，发现PCG在项目推进过程中，还是会存在两个主要的问题。<br>
<br>
第一个是人的问题。项目要推进PCG流程，就需要招聘非常复合的技术美术人才。他不仅需要和传统的TA一样，懂技术、懂美术，还需要具备Houdini的PCG技术算法能力，同时还要清楚整个项目工作流程和美术的数据流程是什么样的。而且他需要投入到项目团队，和场景美术并肩合作，通过制作和生成的方式，来生成整个世界。这样的人力缺口非常大，因为这样的复合型人才非常难找。<br>
<br>
第二个问题是，在传统的Houdini PCG流程中，上一个项目用得非常好的流程，在下一个项目要做非常大的调整。这导致整个PCG技术在跨项目使用时，复用性比较弱。同时，冷启动一个项目时，成本也会比较高。<br>
<br>
<div align="center">
<img aid="1050251" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090844gz9xfjmqzfsbbfsp.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090844gz9xfjmqzfsbbfsp.jpg" width="600" id="aimg_1050251" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090844gz9xfjmqzfsbbfsp.jpg" referrerpolicy="no-referrer">
</div><br>
作为一个技术中台团队，我们分析完这些问题以后，觉得可以通过研发一个通用化的PCG框架来解决。首先，我们提供一套PCG Flow流程工具，通过流程的方式解耦复杂的职能，比如数据流、PCG算法，把这些解耦开。其次，提供一个HDA的基础库，让这个基础库在各项目之间通用，来达成加速冷启动和项目复用的目的。<br>
<br>
下面我从PCG Flow流程、HDA武器库，以及他们在项目中的实践这三方面，给大家进行一一介绍。<br>
<br>
<strong><font color="#de5650">第一部分：PCG Flow（解耦美术效果与程序化流程）</font></strong><br>
<br>
在PCG Flow上，我们投入了一个非常专业的程序团队。这个程序团队主要解决的痛点问题就是，它提供了一个自己自定义的基于节点的操作界面、工具和功能。让TA可以根据自己的项目需求，单独定义这个数据流程。有了这个能力以后，我们就把TA的对数据流程的熟悉程度的要求、对项目熟悉程度的要求，与TA对PCG算法的要求分开来。可以让熟悉Houdini的TA，专业做PCG算法。让更加熟悉项目的TA，去处理美术流程、数据流程这方面的问题。同时，我们也提供了一个界面，可以让美术也能直接参与PCG的工作。<br>
<br>
<div align="center">
<img aid="1050252" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090845aupfiept2i7b2t3p.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090845aupfiept2i7b2t3p.jpg" width="600" id="aimg_1050252" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090845aupfiept2i7b2t3p.jpg" referrerpolicy="no-referrer">
</div><br>
除了Flow本身以外，PCG Flow的能力矩阵最大的一块，就是要打通整个数据流程。主要的挑战来自于三个方面：<br>
<br>
第一是输入部分。我们定义更加适合游戏场景，包括像点云、曲线、Mask等针对游戏领域的输入。简单来说，就是通过点线面的输入来解决输入的问题。<br>
<br>
第二，我们把Houdini Engine的整个流程打通了，把原来的老大哥Houdini HDA这样一个完整的PCG的模块，变成了整个PCG Flow中的一个子节点。这样我们就可以在Flow的任何一个地方去调用这个节点，来使用它里面的PCG算法。<br>
<br>
最后，我们还是要跟引擎做深度的整合，能够把我们的输出的结果非常好地提交到引擎的编辑器中。<br>
<br>
<div align="center">
<img aid="1050253" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090845cwf7nbvwqxwzwuuw.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090845cwf7nbvwqxwzwuuw.jpg" width="600" id="aimg_1050253" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090845cwf7nbvwqxwzwuuw.jpg" referrerpolicy="no-referrer">
</div><br>
在建立PCG Flow的这个过程中我们还提供了分层的能力，解决了美术在多人合作方面相互间的关系，以及PCG自动化生成的数据和美术手工精修数据之间的关系。<br>
<br>
在形态上，整个PCG Flow是以插件化的方式来落地的。为了更好地方便美术使用，在整体工具的易用性、输入输出的多样性和多人协作的制作效率上，都进行了一些细节的优化。在程序角度来说，我们还对它的通用性和拓展性做了一些预先的准备。我们意识到PCG的算法不止是Houdini这一种。我们还为包括基于CPU的程序化生成的算法，基于AI的生成算法，基于GPU的生成算法，都预留了空间。也为整套系统在动态实时场景内容生成方面，也留了一个口子。<br>
<br>
<div align="center">
<img aid="1050254" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090845lhuq1kq4u5w3us41.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090845lhuq1kq4u5w3us41.jpg" width="600" id="aimg_1050254" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090845lhuq1kq4u5w3us41.jpg" referrerpolicy="no-referrer">
</div><br>
这样我们就构建了一个非常有特点的PCG Flow的插件。首先，这个插件可以只依靠自己，能够把整个PCG的流程都打通。它自己去对接Houdini，项目就不用管这个事情了。第二，通过一个节点化的编辑模式，能够非常灵活直观让TA和项目中的同学来管理整体的数据流程。第三，它有比较好的扩展性。第四，通过分层，对于多人协作、自动与手工的数据关系，也提供了比较好的解决方案。第五，我们提供了比较深入的引擎集成的能力，让PCG结果能够非常好地放到引擎中去。<br>
<br>
<div align="center">
<img aid="1050255" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090846g22qbzmlki8qq1pz.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090846g22qbzmlki8qq1pz.jpg" width="600" id="aimg_1050255" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090846g22qbzmlki8qq1pz.jpg" referrerpolicy="no-referrer">
</div><br>
在整个推进过程中，作为技术中台，我们深知不能闭门造车，必须跟项目有非常好的合作。从中台角度来说，我们推进一个新的技术方向，会非常重视跟项目进行非常深入的合作。在这个合作过程中，我们会把人和技术直接地放到这个项目中去，类似于贴身服务或者外包的方式。中台要做的事情肯定不止于此，还需要非常清楚地考虑到这个技术方向后续如何做产品化、服务化，有清晰的发展路线。当我们最终能把技术和人从项目中抽回来，形成一个产品，中台的工作和迭代才真正算完成。也只有做了产品化的工作之后，它才能更加低成本、高效且迅速地推广到更多的项目中去。<br>
<br>
<div align="center">
<img aid="1050256" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090846awgb05n9pgy9bx55.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090846awgb05n9pgy9bx55.jpg" width="600" id="aimg_1050256" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090846awgb05n9pgy9bx55.jpg" referrerpolicy="no-referrer">
</div><br>
在界面这块，从程序角度而言，我们曾经有很多的想法。我们考虑过要不要用QT或C#来做一个通用化的Flow工具，这样可以在不同的工具和引擎之间复用。最后，考虑到要让项目的美术有一个非常一致的体验，我们最终使用了插件化的方式。我们会直接使用引擎编辑器的方式来构建我们的工具。这样就可以让我们的用户在他熟悉的编辑器中，有原汁原味的体验。<br>
<br>
通过和项目的深入合作，我们完成了PCG Flow产品的研发，也打通了数据流和工作流，中间做了非常多的验证，真正把它作为一个产品推到更多的项目中去。<br>
<br>
<div align="center">
<img aid="1050257" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090847p787r7hy76z8kcyc.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090847p787r7hy76z8kcyc.jpg" width="600" id="aimg_1050257" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090847p787r7hy76z8kcyc.jpg" referrerpolicy="no-referrer">
</div><br>
接下来看到PCG Flow的特性介绍视频，我也简单做一下总结。我们在建设PCG Flow的过程中投入了非常专业的程序团队，专门打造了以插件化方式提供的Flow工具，最主要解决了三个痛点。<br>
<br>
<div align="center">
<img aid="1050258" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090847ev0loqu0z0nbvdvo.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090847ev0loqu0z0nbvdvo.jpg" width="600" id="aimg_1050258" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090847ev0loqu0z0nbvdvo.jpg" referrerpolicy="no-referrer">
</div><br>
第一，提供了一个节点化的自定义的工具，能够让项目中的同学非常容易地单独去定义这个Flow本身，这样就实现了对TA职能的解耦，让关心PCG算法和关心Flow的TA，两者的职能可以分开，让更专业的人做更专业的事，也降低了职能的复杂程度。<br>
<br>
第二，提供给美术一个完整的界面，美术在这个过程中，可以通过改变这些输入——也就是点线面的输入，和改变我们的PCG Flow所暴露出来的参数，就可以非常容易地实现他想要的美术效果。他自己就可以看到效果的改变，这样美术可以更加专注于场景效果本身，而不用关心什么是PCG。他不用知道PCG。<br>
<br>
<div align="center">
<img aid="1050259" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090848ha2j5x7zz77lpsp9.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090848ha2j5x7zz77lpsp9.jpg" width="600" id="aimg_1050259" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090848ha2j5x7zz77lpsp9.jpg" referrerpolicy="no-referrer">
</div><br>
最后，通过PCG Flow这个单一的工具，我们打通了整个流程。在这个过程中，我们解决了点线面输入的问题，而且打通了Houdini的Engine，把原来的这个老大哥HDA，变成我们的一个子节点，变成一个可调用的模块。我们还提供了对于引擎深度的整合，不管是编辑器的界面显示，还是数据放到编辑器中，都做了非常好的集成。<br>
<br>
通过PCG Flow，我们基本把过于复杂的职能要求问题给解决了。对于跨项目复用和新项目冷启动的问题，我们给出的答案是，需要做一个数据驱动的HDA的基础库。<br>
<br>
<strong><font color="#de5650">第二部分：HDA武器库（数据驱动的PCG瑞士军刀）</font></strong><br>
<br>
在构建基础库的这个过程中，PCG Flow发挥了非常大的作用。只有当我们完成了PCG Flow之后，才真正地完成了TA这两个职能的解耦。这才让PCG算法，或者狭义来说就是Houdini PCG HDA这样的模块，变成了一个可以单独开发的模块。因此，我们下定决心，要把这个模块开发得更加基础、更加好用，看看它能不能跨项目复用。<br>
<br>
<div align="center">
<img aid="1050260" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090849v6d6jsi6vsd7a7to.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090849v6d6jsi6vsd7a7to.jpg" width="600" id="aimg_1050260" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090849v6d6jsi6vsd7a7to.jpg" referrerpolicy="no-referrer">
</div><br>
为此我们定了几个优化的目标：<br>
<br>
首先，希望这个基础库是足够实用的，不是闭门造车，并且它的功能全面。这就需要跟项目有非常深入的合作，同时它的功能要真的满足一个项目冷启动的时候做demo时候的需求，有一个全面性的要求。<br>
<br>
第二，我们希望在整个Flow的过程中，每一步像Houdini本身，都是可视化的。每一个中间结果都能看到产生什么样的作用，非常便于调试和知道我们在做什么事情。<br>
<br>
最后，我们希望它的可塑性非常强。而且这个可塑性并不是通过比如改一个逻辑、改一个if、改一个while来做的。我们希望它是数据驱动的。美术可以在这个过程中通过改变参数、改变输入，就能非常容易地把整个流程的结果都影响掉。<br>
<br>
<div align="center">
<img aid="1050261" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090849uzux20p25ngyyauz.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090849uzux20p25ngyyauz.jpg" width="600" id="aimg_1050261" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090849uzux20p25ngyyauz.jpg" referrerpolicy="no-referrer">
</div><br>
在HDA库的设计上，我们参考了传统软件的分层架构，有点像C++的标准库或Java的API。我们提供了很多基础的组件，这些组件包括像输入输出的组件，一些最基础的数据转换的算法节点，最基础的一些PCG算法的节点，还有效果上的节点等等。我们提供了这样一个基础库。<br>
<br>
同时，还利用了刚才Flow工具，它可以把HDA作为子节点，就可以通过Flow工具对数据流的影响，把多个子节点通过组合的方式加到Flow上，就可以把它组合成更高级的一些功能。<br>
<br>
在整个推进HDA库的过程中，我们发现要满足一个大型的项目的demo冷启动的话，需要的门槛是很高的。比如，仅仅对于场景编辑来说，至少需要具备地形和地表基础的生成能力，需要有自然场景的生成能力，需要有植被、生态系统的生成能力，需要河流的生成能力，并且基本上大概率会用到道路路网的生成功能。这些基础功能必须都要有，而且很多项目可能还会对城镇建筑的生成有一定的要求。<br>
<br>
<div align="center">
<img aid="1050262" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090850d2u2z8et8uka1yvk.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090850d2u2z8et8uka1yvk.jpg" width="600" id="aimg_1050262" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090850d2u2z8et8uka1yvk.jpg" referrerpolicy="no-referrer">
</div><br>
这就对整个HDA库（刚才提到希望它是比较完备的，有比较完整的能力）提出非常高的挑战，我们也在这中间投入了非常大的人力去完善整个基础库。<br>
<br>
完善的方式还是借助于PCG Flow本身。我们在完善过程中也发现了HDA基础库还是很有道理的。我们会发现项目所需要可以开箱即用的高级能力，很多都可以非常方便地通过Flow工具把基础的算法节点通过组合的方式就可以构建出来。这样的好处就是，可以比从零开始做一个高级算法，节约大量的时间。<br>
<br>
以我们中间的高架桥的生成功能为例。这里还有一个小故事，我们做高架桥的同学在制作这个PCG HDA模块的时候，参照了高架桥的国标。他读了将近100页的文档，所以我们做这个事情还是比较细致的。因此我们生成的高架桥不仅功能非常完善，还能够支持非常多的连接方式，同时生成出来的高架桥的车道、标线都是符合国标的。<br>
<br>
<div align="center">
<img aid="1050263" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090850z6hzdbbucv7d5l6b.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090850z6hzdbbucv7d5l6b.jpg" width="600" id="aimg_1050263" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090850z6hzdbbucv7d5l6b.jpg" referrerpolicy="no-referrer">
</div><br>
也正是在这个过程中，我们不断完善这些高级功能，通过这些高级功能来完善HDA库。这里面就要提到，其实这些高级功能很多都是跟项目一起合作做出来的。我们就会做一个判断，这些高级功能是不是适合跨项目使用，如果评估下来发现这个功能是适合跨项目使用的，我们会首先把它做通用化的处理，把一些项目直接相关的内容做剥离，做清理。后续还需要做包括像代码的优化、完善文档等等，最终把它放到HDA库中，完成一个HDA武器库的升级。这也非常符合我刚才说的中台的技术研发过程需要带得出去、带得回来的理念，这是非常好的例子。<br>
<br>
通过这样一个组合式的开发，我们就完成了最基础的高级的HDA库的构建过程。<br>
<br>
<div align="center">
<img aid="1050264" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090851fe24gzgooz3rkv22.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090851fe24gzgooz3rkv22.jpg" width="600" id="aimg_1050264" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090851fe24gzgooz3rkv22.jpg" referrerpolicy="no-referrer">
</div><br>
让我们看一下HDA库的视频介绍，同时给大家小结一下这个模块。我认为PCG的HDA武器库，给游戏的开发者提供了这样一个能力，可以让大家能够在游戏这个特定的领域，通过使用我们HDA库，就可以非常容易在自己的项目中从零开始搭建PCG流程。特别是在像场景、地形地表、自然植被、道路领域，我们做得比较完善的领域，很多高级节点是可以开箱即用的。这样对于一个项目冷启动或做一个demo的时候，就可以非常容易地完成一个起步的工作。而对于项目中所要用到的特有的功能，你可以通过更加基础的节点，通过Flow把它们组合起来，这样也可以加速你构建这些高级功能的整体效率。<br>
<br>
<div align="center">
<img aid="1050265" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090852cv9260i0v8x8lgbi.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090852cv9260i0v8x8lgbi.jpg" width="600" id="aimg_1050265" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090852cv9260i0v8x8lgbi.jpg" referrerpolicy="no-referrer">
</div><br>
因此，通过这样一个技术，我们就实现了刚才所说的目标：实现了HDA库首先能够跨项目复用；其次，里面的基础功能和高级功能的组合能够满足一个项目冷启动的需求；第三点，通过中台的运作方式，可以保证和项目合作的过程中不断完善和补充HDA库，来实现它整体的发展。<br>
<br>
<strong><font color="#de5650">第三部分：项目实践（迭代快、可回溯、流程稳）</font></strong><br>
<br>
听了这么多，大家肯定会有一个问题，这些技术到底能不能用？它在哪里得到了应用？这边就给大家一个回答。<br>
<br>
在腾讯内部，通过开源协同的方式，我们和天美、光子、魔方、北极光工作室群的10个项目都进行了深度合作，都使用我们这个PCG Flow的工具和HDA的基础库。同时，我们还通过技术合作、产品合作的方式，和腾讯以外的合作厂商也有非常深入的合作。<br>
<br>
<div align="center">
<img aid="1050266" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090853tuw9o2wd4fdw28c0.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090853tuw9o2wd4fdw28c0.jpg" width="600" id="aimg_1050266" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090853tuw9o2wd4fdw28c0.jpg" referrerpolicy="no-referrer">
</div><br>
这里我以合作厂商为例，举三个例子。<br>
<br>
第一个项目是写实FPS的项目，这个项目本身有Houdini的TA，他们已经在尝试使用这样的流程。也因为如此，整体的接入时间是比较短的，大概就用了一个月的时间就完成了这个项目的接入。完成接入之后，项目评估，采用我们的方案后，能够比较显著地提升整体项目的制作能力。能够在同样的场景制作需求下节约原来70%的TA和美术的投入。特别是TA的投入，因为大家都知道TA很难招。<br>
<br>
第二个项目是MMO ARPG的项目，这个项目在合作之初他们完全没有Houdini方面的人，PCG这一块是零。我们花了大概两个月的时间，一方面给他们做集成，一方面给他们做了培训。两个月之后他们就开始用我们的PCG工具。最近我看到他们反馈回来的数据，他们告诉我们在野外的自然场景的case下，发现用我们这个工具比他们传统的制作流程有60倍的效率提升。<br>
<br>
第三个项目是卡通风格的项目。其实我刚才说的HDA库在构建之初很多针对的是写实类的项目。接触这样一个卡通项目，我们还是花了挺多的精力，我们投入了大概有6个人月，两个同学三个月的时间，根据卡通项目特定的需求，为它改造、定制HDA库。与此同时，我们做了集成和培训的工作。根据他们的反馈交流，在场景制作方面，整体的效率提升到了原来的3倍左右，整体的提升也都是非常可观的。<br>
<br>
在和项目合作的过程中，我们刚才提到了有基础库，还把它提升到了很多可以开箱即用的高级功能。在和项目合作的过程中我们还发现PCG的技术还有很多下沉的空间，比如一些具体的模型制作，包括可以非常方便地通过HDA库的能力，去调用比如Houdini等工具中的仿真能力，通过这些仿真能力为项目快速构建符合它自己风格的模型，能够比较好地节省美术的模型制作量。<br>
<br>
<div align="center">
<img aid="1050267" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090853n9e3msxexo5o8bvv.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090853n9e3msxexo5o8bvv.jpg" width="600" id="aimg_1050267" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090853n9e3msxexo5o8bvv.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1050268" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090854mborgqrccszgvqnx.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090854mborgqrccszgvqnx.jpg" width="600" id="aimg_1050268" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090854mborgqrccszgvqnx.jpg" referrerpolicy="no-referrer">
</div><br>
对于像一些可能在现在移动平台，甚至是PC上，没有办法实时运行的、实时推算的效果，我们也可以一样使用HDA的流程，通过仿真、预烘焙的方式，把它先烘焙成离线的数据，导入到游戏引擎中。这样就可以实现在机能不足的情况下，能够实现比实时计算要好得多的效果。<br>
<br>
<div align="center">
<img aid="1050269" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090854s62arwn23wr2eazo.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090854s62arwn23wr2eazo.jpg" width="600" id="aimg_1050269" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090854s62arwn23wr2eazo.jpg" referrerpolicy="no-referrer">
</div><br>
对于像头发这样数量非常多、制作要求非常严苛的模型制作，我们发现这简直是最适合HDA应用的场景，我们也在这上面和项目一起提供了工具，可以快速地生成头发模型。<br>
<br>
<div align="center">
<img aid="1050270" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090855smo2aa2okmxtak0x.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090855smo2aa2okmxtak0x.jpg" width="600" id="aimg_1050270" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090855smo2aa2okmxtak0x.jpg" referrerpolicy="no-referrer">
</div><br>
在资产优化方面，像LOD的优化都有非常专业的工具。我们发现对于项目来说，一方面是用Houdini的方式，有可能可以非常方便地做到对低级LOD的标准化生成；另一方面，像叶子等等一些特殊的材质，传统的工具并不能很好地解决，我们通过这样HDA工具，我们可以为它定制一些具体的减面算法，能够达到更好的效果。<br>
<br>
<div align="center">
<img aid="1050271" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090856cg2vsj69e29k9jle.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090856cg2vsj69e29k9jle.jpg" width="600" id="aimg_1050271" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090856cg2vsj69e29k9jle.jpg" referrerpolicy="no-referrer">
</div><br>
在Instance这个问题上，通过引入Houdini HDA的能力，也发现它能够在项目自定义的一些instance的处理方式，包括其中一些特殊的LOD生成上能有更好的效果。<br>
<br>
<div align="center">
<img aid="1050272" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090856myzjo1fq8fezze9b.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090856myzjo1fq8fezze9b.jpg" width="600" id="aimg_1050272" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090856myzjo1fq8fezze9b.jpg" referrerpolicy="no-referrer">
</div><br>
除此之外，在游戏之外的一些领域，我们的PCG Flow和HDA库也得到了广泛的使用。这里面举三个项目的例子。<br>
<br>
首先在数字孪生，像数字长城这样的项目中，通过PCG Flow和HDA的能力，快捷显著地帮项目提升了自然植被场景的生成效率。<br>
<br>
<div align="center">
<img aid="1050273" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090856d79x97w8m81tatq4.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090856d79x97w8m81tatq4.jpg" width="600" id="aimg_1050273" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090856d79x97w8m81tatq4.jpg" referrerpolicy="no-referrer">
</div><br>
第二，和腾讯云合作的项目中，如视频所示，我们提供了道路生成的能力，能够生成非常符合整体标准和规范的道路，整体的制作和生成效率会比它之前的流程（即人工制作的流程）效率要高出非常多。<br>
<br>
最后，也是现在正在推进的项目，在航空领域的全动飞行模拟器的项目中，我们发现PCG Flow和HDA工具库能够非常显著提升，包括机场跑道这样非常复杂的标准化模型的生成，以及机场周边大量城市建筑的自动化生成的效率。<br>
<br>
<strong><font color="#de5650">展望未来&总结</font></strong><br>
<br>
做个总结，本次分享中，我希望给大家传达的主要是三个观点：<br>
<br>
第一点，PCG非常好用，已经在很多的项目得到验证。使用PCG流程可以显著地提升场景制作的效率，而且肯定是能提升一个数量级以上的，一定要用。<br>
<br>
第二点，如果你像我们一样遇到了PCG的TA招聘比较困难，职能太复杂的问题。你可以考虑像我们一样的思路，通过一个流程的工具，去把整体的复杂职能做一些解耦和拆分，这样就能让专业的人做专业的事情，对跨领域的能力要求就会降低很多。<br>
<br>
第三点，我们在实践中论证了，你是有可能去构建一个属于自己的HDA PCG算法的基础库，通过基础库的方式就可以非常方便地让我们在各个项目之间复用这些已有的能力。这样的好处就是使得它可以非常快地在项目之间交换数据、交换PCG的算法。同时也为新的项目的冷启动和制作demo场景提供给极大的加速。<br>
<br>
<div align="center">
<img aid="1050274" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090857br8vdntoob84qozr.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090857br8vdntoob84qozr.jpg" width="600" id="aimg_1050274" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090857br8vdntoob84qozr.jpg" referrerpolicy="no-referrer">
</div><br>
最后，面对未来的挑战，我们的目标是希望把PCG Flow这个工具进一步拓展它的边界，能够深入到更广阔的领域去应用。在这一块，我就提两个我们现在比较关注的方向：<br>
<br>
第一个，我们现在投入非常大精力在探索，有没有可能通过USD标准这种中间数据格式，让我们的PCG Flow的工具能够非常快捷打通更多的DCC工具和更多的引擎。我们希望，未来对于美术TA这些艺术家，他们所工作的整个场景，都可以通过标准化的方式一网打尽。<br>
<br>
第二个，我们比较看好Runtime PCG的方向。我们发现现在很多新的项目在UGC和开放世界的玩法这些领域对于运行时的动态生成能力提出了非常多的需求。这一块我们也进行了布局和预研。现在我们已经具备了基于GPU的Runtime PCG的能力，它的速度很快。同时我们考虑到兼容性的问题，把整个技术框架限定在了Shader Model 5.0的基础上。只要能符合Shader Model 5.0就可以跑。因此，我们的这个技术框架在现在这个阶段已经可以做到基本上在主流的手机上都是可以实时运行的。<br>
<br>
<div align="center">
<img aid="1050275" zoomfile="https://di.gameres.com/attachment/forum/202208/17/090858bxmmy9mgdm5dmwlw.jpg" data-original="https://di.gameres.com/attachment/forum/202208/17/090858bxmmy9mgdm5dmwlw.jpg" width="600" id="aimg_1050275" inpost="1" src="https://di.gameres.com/attachment/forum/202208/17/090858bxmmy9mgdm5dmwlw.jpg" referrerpolicy="no-referrer">
</div><br>
最后，从2017年至今，五年的时间里我一直都非常深入地参与了PCG的研发过程。在这个过程中有一帮非常可爱的小伙伴，他们放着艺术家的康庄大道不走，非常执着地去研究如何把美术的艺术化思维、抽象思维翻译成逻辑的语言、翻译成程序。也正是因为这些小伙伴们在这五年孜孜不倦的努力，也包括业界同行一起的努力，我们看到在高质量的场景，特别是比如AAA级大世界场景的制作效率上，整个业界有了一个数量级以上的提升。也正因为如此，在今天的游戏中，每一个游戏的每一个场景或多或少、直接或间接都受益于PCG技术所带来的效率和质量的提升。这也为玩家带去了更加丰富、更加细节的世界。<br>
<br>
我的演讲就到这里，PCG技术真的还只是一个开始，It is just a beginning，我们非常看好PCG技术有非常光明的未来。<br>
<br>
谢谢大家！<br>
<br>
<strong>问答环节：</strong><br>
<br>
<strong><font color="#de5650">问：随着游戏制作规模越来越大，游戏开发工业化的呼声很大，PCG和游戏工业化的关系是怎样？</font></strong><br>
<br>
<strong>吴羽：</strong>简单来说，PCG是游戏制作流水线中提升效率更加自动化的一环，它使用的一些技术确实和工业化很相关。因为这是一个非常大的问题，我尝试回答一下。我对工业化的理解至少包含两方面：<br>
<br>
首先需要做到实用化，你如果是要把一个技术能够往工业化的领域推，你必须非常贴近项目的使用。而且肯定不是一个项目，你需要了解多个项目的共性需求，才能总结出来到底哪些真的是符合这个行业的，工业化需要做的事情。<br>
<br>
另外一块，标准化也是非常重要的事情。以PCG为例，比如刚才提到的，一个是需要跟业内更多的标准化技术产生一些共鸣，比方刚才提到的USD这样的技术、Houdini这样的技术，有很多的技术，你需要跟它们有一些共鸣。第二，标准化本身，我们在公司内部也参与了很多标准化提案的工作，你如果真的要做一个工业化的事情，你把它提成一个标准也是非常重要的一步。第三点，工业化肯定不是闭门造车的，一方面要实用，另一方面也需要有更多的宣讲或开源，让你的想法能够更多地为业界所认知，大家一起来做整体工业化的事情。<br>
<br>
<strong><font color="#de5650">问：PCG技术后续会不会越来越多地应用在实时生成领域？</font></strong><br>
<br>
<strong>吴羽：</strong>我个人认为在实时生成领域，PCG技术是一个非常好的候选者，特别是考虑到像美术类的资产已经得到了比较多的验证。<br>
<br>
这里面存在一个问题，我认为它存在一定的挑战，在运行时动态实时生成的过程中，因为你会跟游戏本身的玩法绑定得比较紧密，整体的技术肯定是有用的，但技术如何做标准化、产品化，这个挑战就会非常大。<br>
<br>
因为这是在探讨PCG后续的发展，对于国内来说，我还有一个想补充的。PCG技术，除了我们看到美术为主的领域得到比较大的应用，也看到国外的很多AAA公司把PCG技术也会大量使用到策划的工作中。国外会有 technical designer（技术策划）这样的角色。我相信，PCG技术以后可能会在游戏设计、关卡生成方面也会发挥更大的作用。<br>
<br>
  
</div>
            