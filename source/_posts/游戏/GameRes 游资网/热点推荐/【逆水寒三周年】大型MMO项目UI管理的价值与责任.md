
---
title: '【逆水寒三周年】大型MMO项目UI管理的价值与责任'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202106/29/132927ai8yf2u2igkv6wwu.jpg'
author: GameRes 游资网
comments: false
date: Tue, 29 Jun 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202106/29/132927ai8yf2u2igkv6wwu.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2502462">
<div align="center">
<img id="aimg_988799" aid="988799" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132927ai8yf2u2igkv6wwu.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132927ai8yf2u2igkv6wwu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132927ai8yf2u2igkv6wwu.jpg" referrerpolicy="no-referrer">
</div><br>
《逆水寒》作为一款大型MMO端游，UI工作的复杂和压力相当巨大，虽然最艰难紧张的时间是17年到19年，但是如今想来还是心有余悸。大型MMO端游流程复杂、资源繁多。开发过程中，参与人员多、开发进度紧，特别在上线以后，常常需要根据实际情况紧急调整内容。在《逆水寒》上线三周年之际，我们将开发和运营中的UI管理工作经验整理出来。<br>
<br>
本文只讨论UI管理工作，对于UI品质的全盘设计工作，以后另文总结。<br>
<br>
<strong><font color="#de5650">一、工作背景</font></strong><br>
<br>
《逆水寒》开发初期也存在着各种大型游戏开发中遇到的问题，开发率低下且设计质量不高。<br>
<br>
<strong>从品质表现来说：</strong><br>
<br>
过于弹窗化的设计阻碍了玩家和游戏世界的交流，且弹窗没有深度，深层信息全靠叠加弹窗，交互工作更像是排版工。<br>
<br>
<strong>从开发效率来说：</strong><br>
<br>
整体效率太低，阻碍了整体游戏的开发进度。虽然看起来是【品质】和【效率】两个问题，但其实本质上还是UI工作管理的不合理造成的。UI工作关键点不过三者【流程】【工具】【人员】，将这三者调整到最优，是UI管理工作的核心。<br>
<br>
<div align="center">
<img id="aimg_988800" aid="988800" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132928q0v3hshqh8u8ccch.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132928q0v3hshqh8u8ccch.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132928q0v3hshqh8u8ccch.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>从流程来说：</strong><br>
<br>
我们需要一个高效运转的工作流程：流程中的每个环节都可以产生有效的价值；每个环节都有严格规范的标准进行要求；各个环节之间灵活衔接互相促进，而不是互相制约。<br>
<br>
<strong>从工具来说：</strong><br>
<br>
工具包括制作工具、资源管理、协作沟通三者。逆水寒有着先进的自研引擎，在画面渲染方面非常出色。使用起来非常适合专业的技术大佬，但对不懂代码的UI同学来说有一定难度。此外在研发前期设计UI框架时，缺乏专业设计师来探索未来的设计风格，导致基础结构以平面弹窗为主。<br>
<br>
<strong>从人员来说：</strong><br>
<br>
需要加强设计师对自己方案的责任感，对自己的方案要落实跟进到底，荣誉与付出挂钩。要对自己的方案有一定专业追求，要对情绪体验、操作流程、信息结构等多方面进行思考，而非单纯注重界面美观程度。<br>
<br>
好的UI管理体系是能够【自主】【高效】的运转起来，并且给项目组节省极大的开发成本的。<br>
<br>
<strong><font color="#de5650">二、工作流程</font></strong><br>
<br>
优化UI工作管理，第一步是从全局角度审视，让整个UI流程合理且高效。之前《逆水寒》的UI流程存在两个问题：第一，所有环节依次进行，每个环节和依赖上一环节的完成度，如果出现一个环节延迟，那么后续所有工作都必须推迟，整个开发效率会变得十分缓慢且不可控；第二，交互设计师只输出设计文档，不对自己方案的落实结果负责，经常导致游戏中实际情况覆盖补全，再反复讨论修改，必然消耗更多的时间。<br>
<br>
因此对UI整体工作流程的优化至少要解决以上两个问题，让每个环节的人员可以机动利用时间完成要做的事情，同时加强交互设计的交付标准和责任意识。<br>
<br>
<strong>1、删减多余环节</strong><br>
<br>
原有交互设计师只进行方案设计，输出交互文档，并不参与实际开发工作。这样存在几个问题：一、单纯的文档非常容易遗漏玩家各种操作和玩法极端情况，倘若开发中出现这样的问题，不论策划找交互反复沟通，或是自己处理，更多沟通以后和之前的文档也大相径庭了。二、交互文档交付下游工作后，接手程序和美术可能并不清楚游戏中已有相似功能，于是出现重复开发，极大增加项目成本。<br>
<br>
<div align="center">
<img id="aimg_988801" aid="988801" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132928z3bg32glb3jkfvl3.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132928z3bg32glb3jkfvl3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132928z3bg32glb3jkfvl3.jpg" referrerpolicy="no-referrer">
</div><br>
如此，必须对不产生实际价值的工作量进行删减：<br>
<br>
① 交互设计和动效美术都需要将自己的方案直接做进引擎中，特别是交互这样自己更清楚实际的情况，对界面最终效果负责。在有重复功能时可以直接复用已有控件，节省下游工作量。<br>
<br>
② 程序只负责功能开发，专业的人做专业的事情，保证功能稳定是程序更应该花精力做的事情。<br>
<br>
<strong>2、串联变为并联</strong><br>
<br>
曾经UI的开发流程是典型的瀑布式开发：<br>
<br>
沟通需求——交互设计——视觉设计——动效设计——界面制作——程序开发——验收测试<br>
<br>
于是存在着瀑布式开发的典型问题，1、每个环节过于依赖上一环节，但是任何一个环节如果出现问题（比如员工请假、工作太满），后续环节都要相应延期，倘若后续再有什么问题，那整个流程的进度完全不可控。2、到下游环节发现上游已完成的工作存在问题，如此返工会严重浪费开发时间。<br>
<br>
<div align="center">
<img id="aimg_988802" aid="988802" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132928tu9aem6suabxzezg.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132928tu9aem6suabxzezg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132928tu9aem6suabxzezg.jpg" referrerpolicy="no-referrer">
</div><br>
这就需要我们的流程既能解开每个环节的互相依赖，也能在各个环节之间建起高效快捷的沟通方式。<br>
<br>
调整之后的流程变成了：<br>
<br>
策划需求——交互设计/界面制作——视觉设计/程序开发——界面替换/动效制作——交付测试<br>
<br>
<div align="center">
<img id="aimg_988803" aid="988803" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132928evwz2laxgg3a6gax.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132928evwz2laxgg3a6gax.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132928evwz2laxgg3a6gax.jpg" referrerpolicy="no-referrer">
</div><br>
我们从交互设计着手，要求交互在初期设计方案的同时，需要将游戏界面的初级功能文件制作出来，在所有资源都到齐并且程序开发完成后，对界面进行正式化调整。这样一方面促使交互设计师在设计的过程中更清楚的了解具体的游戏环境，另一方面也要求交互设计师必须对自己设计方案的最总结果进行负责。<br>
<br>
程序工作和美术工作同时进行，交互设计跟进，这样在开发环节发现任何问题都可以直接进行调整。<br>
<br>
在任务管理平台上，也会总任务和子任务的挂接关系，表现整个流程的责任关系。当每个环节的子任务完成后，交互验收总需求，就可以将总任务关闭，交由负责策划和QA再进行更多验收（比如服务器功能等）。<br>
<br>
<div align="center">
<img id="aimg_988804" aid="988804" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132929y5z6a6gk7gel5l7q.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132929y5z6a6gk7gel5l7q.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132929y5z6a6gk7gel5l7q.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>3、需求交替进行</strong><br>
<br>
理想情况下，每个环节的参与人员一个流程内只做一个需求，一个流程走完正好一个月左右。但是下一个需求不会等上一个完成才来，因此每个人员的工作也是交替进行，上一个需求的前几步交付出去，下一个需求就开始了。如果安排合理，开发周期从之前的几个月继续缩短。如果开发压力不是很急，在这里为了保证设计质量，不太建议并行2个以上的需求，毕竟设计不是靠加班就能想出更好idea的工作。（但我们当时开发压力真的很急，这里也非常感激所有在逆水寒上线前奋力加班的UI同学们。）<br>
<br>
<strong>理想的开发流程：</strong><br>
<br>
如果每个环节都需要参与，并且正常执行的话，一个完整的流程应该是这样<br>
<br>
<div align="center">
<img id="aimg_988805" aid="988805" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132929eiypyycicicugcgn.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132929eiypyycicicugcgn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132929eiypyycicicugcgn.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>实际的开发情况：</strong><br>
<br>
然而，实际并不是所有需求都要把全部流程走一遍，这就需要交互设计同学能够在前期判断出如何合理调配资源可以做到更好更快。并且有些开发设计和开发可能比较简单，就不需要每个环节都占用一周时间。<br>
<br>
<div align="center">
<img id="aimg_988806" aid="988806" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132930ocyayyycaszelcho.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132930ocyayyycaszelcho.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132930ocyayyycaszelcho.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">三、工具优化</font></strong><br>
<br>
工具包括【制作工具】【资源管理】【协作沟通】三部分，因为我们是自研引擎，对于实际制作工具的优化虽是个非常艰难的过程，但对于其他项目并没有太大参考价值，所以这里对资源管理进行一些总结。<br>
<br>
<strong>1、【制作工具】重要的所见即所得</strong><br>
<br>
为了保障界面制作的效果，一个所见即所得的界面编辑工具尤为重要。界面工具往往包括几个功能：资源管理、元件制作、界面拼接、游戏内验收。一些较为成熟的工具（Unity等）会同时包括这几个功能，如果有需要优化的需求，就要求助于技术人员，优化工具带来的效率提升对于项目成本的减少是非常可观的。<br>
<br>
<strong>2、【资源管理】多级资源管理</strong><br>
<br>
初期《逆水寒》将资源分为通用资源和专用资源。但在设计的过程中，我们希望，每个系统有自己的性格，有自己的定位，并不能都简单粗暴的用同一套资源。因此存在一批在特定系统中较为通用的资源（比如结婚系统的红色弹窗和相应资源），但既不全局通用，也不只有单独页面使用。为了同时保证资源复用，又不过于增加包体大小，我们增加了中间层级资源管理。<br>
<br>
<div align="center">
<img id="aimg_988807" aid="988807" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132930etckzg8k7kkcqnye.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132930etckzg8k7kkcqnye.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132930etckzg8k7kkcqnye.jpg" referrerpolicy="no-referrer">
</div><br>
<font color="#de5650">一级资源为全局通用资源</font><br>
<br>
这部分资源会在游戏启动时加载，影响启动速度，所以需要严格控制大小。这个文件也会做检测，当导入太大资源时会有提示。（因为曾经有设计师把任何自己认为可复用的图都往里导，致使整个UI组开发效率变慢）。此外这个文件需要方便所有人查看，因此我们对其做了定时导出，每天凌晨导出最新一版到共享服务器中，来上班时打开文件夹可直接查看最新版本，随时查找复用。<br>
<br>
<font color="#de5650">二级资源为系统通用资源</font><br>
<br>
《逆水寒》存在着大量以系统为单位的界面，比如帮会系统、婚姻系统等，这些系统有自己独立的设计元素，在系统内部大量复用。因此我们以系统为单位将资源进行聚合，形成部分二级通用资源。这部分资源只在某一系统内复用，既不会影响全局，也不会在单独界面中重复储存。<br>
<br>
<font color="#de5650">三级资源为界面专用资源</font><br>
<br>
每个界面会配有自己的资源文件，彼此不通用。将每个界面专有资源放在这里，也方便识别和管理。<br>
<br>
<strong>3、【资源管理】通用机制制作</strong><br>
<br>
图素资源一般是组合为控件在游戏中被使用，那么直接将通用图素制作为通用控件，岂不是更方便？<br>
<br>
<font color="#de5650">① 通用控件制作</font><br>
<br>
应该有许多项目也是这么做的，将各种较为通用的控件进行统一制作，在开发中随时调用。比如进度条，使用时可以调整控件参数以适用于所需要的环境。但当时《逆水寒》的通用控件数量不多，且存在重复开发。于是后来在新方案制作的过程中，将可以复用的控件进行制作，节省未来的开发量。<br>
<br>
<font color="#de5650">② 实时更新资源</font><br>
<br>
为了保证游戏的整体性，每个游戏都会制定一套自己的设计规范，并有一套通用资源库对其进行保证。但随着游戏的继续开发，游戏内容不断扩展，游戏的通用控件库也会随之更新。倘若控件库是静态的文档形式，必然产生维护成本。但贯彻通用规范又在很大程度上依靠大家自觉，这就又带来了管理成本。所以我们构建了一个更为自动化的控件库：<br>
<br>
<ul><li><strong>【自动更新】</strong>将通用控件库整理之后，也做了每天定时导出，如此对控件库中出现的不符合统一性的问题可以及时调整，减少维护成本。</li><li><strong>【直接调用】</strong>提高了复用的便捷性，允许设计和开发人员直接调用公共库组件，减少了重复制作的工作量，也保证了玩家体验的统一性。</li><li><strong>【允许拓展】</strong>减低限制，过于限制创意人员的发挥也会带来游戏品质下降。因此部分控件是允许一定程度的自由发挥的。在约定好交互方式下，美术可以替换其中的资源和样式或修改参数，以产生更多的可能性。<br>
</li></ul><br>
<font color="#de5650">③ 更多表现效果</font><br>
<br>
在项目过程中，我们发现已有需要有更多表现机制才能带来更多的游戏体验，因此这里和技术大佬们一起研究开发了一些新的表现方法。<br>
<br>
<div align="center">
<img id="aimg_988808" aid="988808" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132934ghmm1hkuoouewwkm.gif" data-original="https://di.gameres.com/attachment/forum/202106/29/132934ghmm1hkuoouewwkm.gif" width="394" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132934ghmm1hkuoouewwkm.gif" referrerpolicy="no-referrer">
</div><br>
如在强调氛围时，优化了全屏粒子特效。与之前相比，可以通过参数调整粒子的渐变、线性、轨迹等，只要填入合适的参数，可以生成变化多样的效果。<br>
<br>
<strong>4、【资源管理】主题化制作界面</strong><br>
<br>
当游戏上线运营后，经常要根据玩家反馈迅速调整游戏内容，这对界面输出的速度提出了更高的要求，甚至一周之内要完成交互、美术、开发等全部工作（比如《逆水寒》经脉系统）。在实际的开发过程中，我们发现在【战场】【比赛】【装备】三大模块的此类需求最多，于是将相似主题的控件进行归类，形成专用库。如果出现相关需求，设计者可以直接使用模块化的组件快速制作界面。同时也开放了部分可以替换资源的接口，防止连美术样式也一样，会让玩家对不同玩法产生迷惑。<br>
<br>
<div align="center">
<img id="aimg_988809" aid="988809" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132934xlwln1w5urjcerwv.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132934xlwln1w5urjcerwv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132934xlwln1w5urjcerwv.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>5、【协作沟通】打通岗位协作</strong><br>
<br>
常有策划或美术在自己的工作中，需要调用UI资源的情况。<br>
<br>
<font color="#de5650">① 图标、称号、头像等</font><br>
<br>
游戏策划最经常调用的是图标资源，如道具、头像、头像框、称号等。如果需求方不了解已有资源的情况，就要麻烦交互来帮忙查找，在一来一回的交流中，双方都很耗费精力。所以将资源直接开放给所有需求方，会便捷很多。但又不能完全开放图标资源的编辑权限，防止过多编辑导致其他引用链接出现问题。这就需要将此类资源做仅可读导出，方便需求方可以查看资源样式和资源名，直接使用资源名称。<br>
<br>
<font color="#de5650">② 查看所有界面</font><br>
<br>
对于全部游戏界面也会进行定期导出，方便所有人可以及时查看全部游戏界面的最新效果。也方便设计师的日常走查，如果哪个界面出现表现问题，可以在每天最新的导出文件中直接查看。<br>
<br>
<font color="#de5650">③ 通用界面机制</font><br>
<br>
有些较为通用的界面也可以像控件一样做成通用机制，比如结算、二次确认等。当策划做玩法设计需要结算界面时，可以直接调用该界面控件，填上要显示的奖励物品和数量即可。根据实际情况做了14中分类：<br>
<br>
<div align="center">
<img id="aimg_988810" aid="988810" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132934nppvpijlcvz0vj8c.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132934nppvpijlcvz0vj8c.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132934nppvpijlcvz0vj8c.jpg" referrerpolicy="no-referrer">
</div><br>
为了方便多层次需求，相同功能的界面也会制作不同规格界面，如小玩法结算：<br>
<br>
<div align="center">
<img id="aimg_988811" aid="988811" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132935d0556chco89oo8mm.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132935d0556chco89oo8mm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132935d0556chco89oo8mm.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">四、人员管理</font></strong><br>
<br>
<strong>1、规范交付标准</strong><br>
<br>
越是大型游戏，参与的人员越多，越需要大家更为紧密的配合。不仅自己的工作要做好，也要配合好相关职能的工作，整个团队才能更高效的运转，因此要对每个环节的工作要求和交付标准进行规范。<br>
<br>
交互设计师将工作成果交付美术和程序之前，需要给出交互文档以及工程文件，那么这两者就需要达到下游人员需要的标准。再正式界面交付QA前，也需要对最终效果有一定要求。<br>
<br>
<ul><li><strong>交互文档：</strong>作为交互设计师产出的产品，应该考虑用户（相关的策划、美术、程序和QA）的使用情景，如果以后转交工作，那么也要方便后面接手的设计师。<br>
</li></ul><br>
有些内容可以参考，根据实际需求来选用：<br>
<br>
<ul><li><strong>文档信息：</strong>记录需求及变更、设计师姓名、方案版本、修改记录等。</li><li><strong>现有问题分析：</strong>一般用于迭代设计，会对当前的设计方案进行走查和记录。</li><li><strong>竞品分析：</strong>可以选用，对相关竞品进行分析，方便自己思考也方便以后接手人员更快了解情况。</li><li><strong>功能结构图：</strong>一般用于系统设计，对整个系统的功能结构进行分析和设计。</li><li><strong>任务流程图：</strong>一般用于玩法设计，对玩家操作的各种情况进行分析和规范。</li><li><strong>交互设计原型：</strong>必不可少的一部分，是对交互方案的系统化阐释。并标记出初级界面各个界面及控件名称，方便程序开发时快速查找。</li><li><strong>各类资源需求：</strong>单独将需要的需求列出来，方便美术、音效等岗位人员可以快速了解需要做的工作。</li><li><strong>验收问题跟进：</strong>在最终界面做完以后进行自我验收，并整理出来问题进行跟进。<br>
</li></ul><br>
<div align="center">
<img id="aimg_988812" aid="988812" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132935tkr2xwlrmq70hxdm.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132935tkr2xwlrmq70hxdm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132935tkr2xwlrmq70hxdm.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>2、确定责任归属</strong><br>
<br>
交互设计师需要跟进整个流程，并对最终结果负责。当然中间程序和美术的环节，不能过于限制相关同学的发挥，毕竟专业的事情交给专业的人来做，每个人都要对自己的工作负责。此外为了方便下游人员直接开始工作，每个环节结束后的提交会有一定的要求，比如需要填写提交路径，或者修改文件名称，这样其他人看到就可以开始自己的工作了。<br>
<br>
<div align="center">
<img id="aimg_988813" aid="988813" zoomfile="https://di.gameres.com/attachment/forum/202106/29/132936ht33kj6531zfsoo6.jpg" data-original="https://di.gameres.com/attachment/forum/202106/29/132936ht33kj6531zfsoo6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/29/132936ht33kj6531zfsoo6.jpg" referrerpolicy="no-referrer">
</div><br>
只做效果图不考虑设计细节也不对整个方案负责到底的交互设计师是非常不合格的，这样会使得团队中帮其处理实现细节和跟进落实的其他人非常受打击。毕竟好看效果图最好展示工作，但好不好用却非常不好展示。<br>
<br>
<strong><font color="#de5650">五、到底意难平</font></strong><br>
<br>
作为一个次世代端游，《逆水寒》UI所呈现的效果远远不应该只有现在表现出的效果。我们的期望效果是，强沉浸感、临场感的，是可以借鉴主机游戏做场景化UI或者行为导向型UI。<br>
<br>
实际总是和理想存在差距，现在也还有诸多问题，比如弹窗化的基础框架没办法修改；没有办法将UI置于场景中，强调沉浸感；很难让UI随玩家行为进行变化等。面对各种前期问题和限制，又要平衡效率和质量。<br>
<br>
好在努力提高效率后，设计师团队有了更多的精力对品质进行思考。在游戏上线以后，逐步开始对每个系统进行叙事化独立包装和，让游戏整体氛围更加热闹，让每个界面也更有故事性，把国风武侠的世界融入玩家操作中。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：GameTube</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/jaSFDj3c2oDGdcMF0jlSOA</font></font><br>
</td></tr></tbody></table>



  
</div>
            