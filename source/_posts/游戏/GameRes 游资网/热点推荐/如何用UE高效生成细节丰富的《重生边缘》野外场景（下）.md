
---
title: '如何用UE高效生成细节丰富的《重生边缘》野外场景（下）'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202203/07/092053u01omcu7101c02ih.png'
author: GameRes 游资网
comments: false
date: Mon, 07 Mar 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202203/07/092053u01omcu7101c02ih.png'
---

<div>   
<font color="#808080"><i>以下文章来源于NExT Studios ，作者引擎全开的</i></font><br>
<br>
<a href="https://www.gameres.com/893210.html" target="_blank">上篇文章中</a>，我们从地形、崖壁、植被、河流、道路五个方面介绍了NExT Studios 在使用虚幻引擎4开发《重生边缘》的过程中，过程化内容生成的一些尝试。<br>
<br>
本篇将针对工具加入场景制作后，如何解决新的工具在实际工作中遇到的各种问题，以及分享一些试验性工作。<br>
<br>
<strong><font color="#de5650">直达现场</font></strong><br>
<br>
<div align="center"><a href="https://www.bilibili.com/video/BV1kZ4y1f7WU" target="_blank">Unreal Open Day2021虚幻引擎技术开放日现场演讲：《重生边缘》中的过程化内容生成</a></div><br>
<strong><font color="#de5650">我是进度条</font></strong><br>
<br>
<strong>过程化内容生成中容易遇到哪些流程问题？</strong><br>
<br>
比如生成的效果达不到美术的要求；工具的使用门槛太高，他们不想用；工具不够稳定，他们觉得折腾的成本太高；或者涉及多人协作的问题，这个事情到底是程序员做、TA做、还是关卡美术做？多个关卡美术的协作需求如何解决？等等。只有解决了这些问题才算是一个合格可用的工具链。<br>
<br>
基于前面的分享，相信大家也能看出，我们的目的是：并不追求全地图自动化生成，而是根据需求做一些定制，提高制作效率。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032669" zoomfile="https://di.gameres.com/attachment/forum/202203/07/092053u01omcu7101c02ih.png" data-original="https://di.gameres.com/attachment/forum/202203/07/092053u01omcu7101c02ih.png" width="600" id="aimg_1032669" inpost="1" src="https://di.gameres.com/attachment/forum/202203/07/092053u01omcu7101c02ih.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">过程化内容生成管线</font></font></div><br>
自动生成内容和人工编辑内容之间的冲突问题如何解决？生成内容之间的关卡切分问题如何考虑？不同子关卡的生成限制如何保证结果的稳定性？<br>
<br>
我们总结出来两个原则，第一是生成的内容不能覆盖人工编辑的内容。第二是各个子关卡之间尽量地独立地编辑和生成。就像 Unreal 大世界里的地图，通常会编辑成多个子关卡，方便多个美术协作，然而对于过程化生成的内容，也需要去做这样的支持。比如可以对world composite做一个支持，支持地形自动切分到子关卡。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032670" zoomfile="https://di.gameres.com/attachment/forum/202203/07/092101esmkrqrlogkomvqe.png" data-original="https://di.gameres.com/attachment/forum/202203/07/092101esmkrqrlogkomvqe.png" width="600" id="aimg_1032670" inpost="1" src="https://di.gameres.com/attachment/forum/202203/07/092101esmkrqrlogkomvqe.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">自动切分到子关卡</font></font></div><br>
关于生成的内容（大量贴花、崖壁、河流等）之间，也都需要切到子关卡。只有切分了子关卡，才能做独立地剔除和 level streaming，同时也能支持不同的人来编辑和生成不同的子关卡。<br>
<br>
对于不同的子关卡，我们生成的限制是需要保证结果的稳定性：不管是多块一起计算出来的结果，还是单块单独计算出来的结果，应该是一致的。这样才能够保证按照子关卡的方式去工作。<br>
<br>
<strong>地形和建筑的稳定性如何解决？</strong><br>
<br>
对于地形来说，我们没办法很好地解决。因为关卡与关卡之间会有一道必然的交界，如果只更新了其中的一块，另外一块就接不上了。<br>
<br>
虽然可以对整个地形做整体的侵蚀或美化，做一次全量更新，但这对于整个开发来说是非常不友好的行为，因为需要协调所有人，把所有的关卡文件都解锁。我觉得更实用的做法是做局部的更新，比如只更新刷过mask的区域。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032671" zoomfile="https://di.gameres.com/attachment/forum/202203/07/092103cg67n6od6m72mg29.png" data-original="https://di.gameres.com/attachment/forum/202203/07/092103cg67n6od6m72mg29.png" width="600" id="aimg_1032671" inpost="1" src="https://di.gameres.com/attachment/forum/202203/07/092103cg67n6od6m72mg29.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">局部更新mask</font></font></div><br>
对于有些建筑区域，比如某处建了一栋房子，要求地基是平的，我们不想在生成地形的时候改变地表，很可能房子就悬空了。我们可以使用volume把区域框起来，跳过这个区域的侵蚀生成。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032672" zoomfile="https://di.gameres.com/attachment/forum/202203/07/092104lkte5vdb3ktdvkde.png" data-original="https://di.gameres.com/attachment/forum/202203/07/092104lkte5vdb3ktdvkde.png" width="600" id="aimg_1032672" inpost="1" src="https://di.gameres.com/attachment/forum/202203/07/092104lkte5vdb3ktdvkde.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">volume排除侵蚀区域</font></font></div><br>
<strong>跟美术编辑的冲突问题如何解决？</strong><br>
<br>
有时候过程化生成的内容跟美术编辑的内容在同一个数据集里面，就会产生冲突问题。到底用谁的呢？Unreal提供了Edit Layer的功能，它跟Photoshop的图层一样，可以把生成的单独放一层，人工编辑的单独放一层，甚至还可以开更多的层，这样就可以混合人工编辑和我们生成的数据，得到想要的效果。但有的时候可能并不想要混合效果，而想要替换效果（比如说河流河道可以替换掉原有的地形）。我们又开发了一个Edit Layer的覆盖混合模式，用来支持这样的需求，同时也扩展了Unreal权重绘制的工具，用来绘制mask，支持这种覆盖混合和很多层的表现。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032673" zoomfile="https://di.gameres.com/attachment/forum/202203/07/092105ch08468h6pcc0dhn.gif" data-original="https://di.gameres.com/attachment/forum/202203/07/092105ch08468h6pcc0dhn.gif" width="600" id="aimg_1032673" inpost="1" src="https://di.gameres.com/attachment/forum/202203/07/092105ch08468h6pcc0dhn.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Edit Layer覆盖混合模式</font></font></div><br>
还有一种冲突比较常见，比如说美术在某处放棵树，只是用来做装饰的，但是我们生成植被的时候很可能就把这棵树给生成没了，那这不是他们想看到的。所以我们针对生成的树都会打标记，每个instance上都会有一个特殊的属性，这样就能够区分出来到底哪些树是我们生成的，哪些树是美术编辑的。再重新生成的时候，就可以把原来生成的树全部删掉，做一次全量更新，但美术摆的树并不会被删掉，而且也可以选择避开他们。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032674" zoomfile="https://di.gameres.com/attachment/forum/202203/07/092106v8ttuyhkyttzynzx.png" data-original="https://di.gameres.com/attachment/forum/202203/07/092106v8ttuyhkyttzynzx.png" width="600" id="aimg_1032674" inpost="1" src="https://di.gameres.com/attachment/forum/202203/07/092106v8ttuyhkyttzynzx.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">很容易树没了</font></font></div><br>
<strong>数据导入导出的问题如何处理？</strong><br>
<br>
我们沿用了Unreal Landscape Spline曲线生成，这些数据需要导出到Houdini当中进行运算，其实这也是为编辑的操作习惯而做的妥协，也避免了再开发全新的一套曲线编辑工具。<br>
<br>
我们把Unreal Landscape Spline重新做了算法量化，导出成一个 JSON，然后在Houdini当中提取这些关键点做重建，这样就可以基于这条曲线去做算法实现。我们也加了各种各样的自定义属性，比如说曲线的类型，因为它会有不同的内容（路、护栏、河等），他们是属于不同曲线的。曲线的宽度还有优先级也都是通过这种方式添加到 JSON 文件里。<br>
<br>
针对生成的内容。我们也做了一个简单的热力图扫描工具，可以选择任意一个Unreal当中的某个stat，比如针对面数去做统计，生成可视化的表现，方便美术在生成完或者关卡编辑完后去做性能自查。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032675" zoomfile="https://di.gameres.com/attachment/forum/202203/07/092107k5koo9hegi96ighd.png" data-original="https://di.gameres.com/attachment/forum/202203/07/092107k5koo9hegi96ighd.png" width="600" id="aimg_1032675" inpost="1" src="https://di.gameres.com/attachment/forum/202203/07/092107k5koo9hegi96ighd.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">热力图性能分析面板</font></font></div><br>
<strong>一些试验性的探索</strong><br>
<br>
如果只是针对之前提的那几个功能的话，可能整个工作流是大同小异的，但是每个项目其实需求都不一样。比如说有的项目完全不用Houdini，生成算法全在Unreal里程序员自己实现。还有的项目可能因为不喜欢数据互相导来导去，选择整个的关卡布局是在Houdini当中进行制作，然后再导入Unreal，这个时候就不能改了。还有的像我们一样，频繁导入导出，需要很多数据交换，那我们需要程序员不断地处理这些特殊的需求。<br>
<br>
所以我们在把这种工具推广到不同项目的时候，就需要重构整个管线。我们支持了蓝图节点编辑，让原来Houdini的HDA文件生成一个蓝图的异步节点，其所需要的数据准备是通过蓝图来进行的（包括数据输出的后处理），这样就具备了非常高的灵活性，能满足很多奇奇怪怪的需求。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032676" zoomfile="https://di.gameres.com/attachment/forum/202203/07/092108b1ks9jjt6d1spmfj.png" data-original="https://di.gameres.com/attachment/forum/202203/07/092108b1ks9jjt6d1spmfj.png" width="600" id="aimg_1032676" inpost="1" src="https://di.gameres.com/attachment/forum/202203/07/092108b1ks9jjt6d1spmfj.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">可定制的生成流程</font></font></div><br>
我们生成完，可以给它打个 tag 或者设置一些类似 virtual texture的属性，然后生成一个actor，甚至改变它的材质。在这套机制下，解放了程序员的生产力，不用他们专门开发特性。因为有的时候我发现不是这些功能实现不了，而是美术等不了，或者用户等不了，反复折腾的时候他们就不想用了。<br>
<br>
另外，我们把数据的输入输出做了抽象，比如抽象成图，或者曲线，或是一些点，然后把这些数据做了抽象之后，甚至可以通过网络来传输这些数据，把生成的服务放到一台更强健的GPU工作站上。而且把数据做完抽象之后，也不限于只用Houdini来做，可以搭建一些自己的服务，用 Maya或Blender也都可以，因为数据的交换变得非常简单。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032677" zoomfile="https://di.gameres.com/attachment/forum/202203/07/092109t9h4lgbjd4hiw9qz.png" data-original="https://di.gameres.com/attachment/forum/202203/07/092109t9h4lgbjd4hiw9qz.png" width="600" id="aimg_1032677" inpost="1" src="https://di.gameres.com/attachment/forum/202203/07/092109t9h4lgbjd4hiw9qz.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">生成服务器</font></font></div><br>
我们也做了些机器学习的一些尝试，比如说基于GAN算法的现实世界生成，或者是地表地形的风格化迁移等。还有一个很常见的问题是在用Houdini做这些工作的时候，数据的导入导出和计算都需要非常长的等待，有些团队会倾向于在引擎中自己实现生成算法，我们在这方面也做了一些简单的尝试，参考了《地平线：零之曙光》（Horizon Zero Dawn）的做法，使用GPU加速的方式做地表地形的生成和植被的分布。<br>
<br>
<strong><font color="#de5650">应用探索</font></strong><br>
<br>
过程化内容生成的技术除了应用在游戏开发中，还有其他应用场景。例如NExT跟新华社合作的数字航天员小诤的火星视频中，我们使用了过程化内容生成的技术模拟火星的地貌。UE5的Nanite可以在不限制三角形数量的情况下做大量的几何细节，这应该也是后续游戏制作的趋势之一。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：NExT Studios</font></font><br>
<br>
  
</div>
            