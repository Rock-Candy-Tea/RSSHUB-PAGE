
---
title: """""""""""'网易开年第一款MMO，《天谕》手游背后的技术究竟有多强？'"""""""""""
categories: 
    - 游戏
    - GameRes 游资网 - 列表
author: GameRes 游资网 - 列表
comments: false
date: Mon, 11 Jan 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202101/11/105226ivg6ar1khg62hdd6.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2481060">
《天谕》手游被网易寄予了厚望，它是2015年《天谕》端游的IP续作，也是网易2021年开年的首款MMO游戏。1月8日上线后，游戏稳坐iOS免费榜首至今，并且在TapTap热门榜和新品榜高居头名，好游快爆平台评分也有8.6分。<br>
<br>
<div align="center">
<img id="aimg_952635" aid="952635" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105226ivg6ar1khg62hdd6.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105226ivg6ar1khg62hdd6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105226ivg6ar1khg62hdd6.jpg" referrerpolicy="no-referrer">
</div><br>
在MMO表现技术不断拉高标准的竞争环境下，网易选择Unity作为《天谕》手游的开发引擎，让低端设备也能实现云层、海底、植被等资源的高效渲染，最终呈现出高品质的美术表现。此次采访主旨为了解网易是如何利用Unity引擎功能，完成移动端美术技术的硬品质呈现。<br>
<br>
以下为工作室的采访分享，葡萄君整理：<br>
<br>
<strong>能简单介绍一下《天谕》手游和它的开发背景吗？</strong><br>
<br>
网易天谕手游：《天谕》手游由网易雷火游戏事业部开发，目前旗下游戏主要为《天谕》端游等MMORPG类型的产品。《天谕》端游于2011年3月立项的，并于2015年6月正式上线运营，上线初期便打破了30万人同时在线的记录。目前端游仍保持稳定长线运营，积累下一批核心玩家。<br>
<br>
因此在2016年8月，我们决定正式立项《天谕》手游，选择Unity引擎围绕「 日月生息」、「万物有灵」、「一见倾心」和「肆意冒险」的设计思路，打造一款业界标杆级的MMORPG手游。<br>
<br>
《天谕》手游是一款以东方幻想为主题的MMORPG游戏，游戏为玩家打造出能够在云海穿梭飞翔探索的世界，并且有丰富的职业选择、高难度副本挑战，以及高自由度捏脸系统，带给玩家独特的开放世界游戏体验。<br>
<br>
《天谕》手游已于2021年1月8日全平台公测，我们期望游戏能带给玩家不一样的游戏体验，同时也希望天谕IP能够不断壮大，带给玩家更多不同类型的游戏作品。<br>
<br>
<div align="center">
<img id="aimg_952636" aid="952636" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105229tnqud838686q8fc3.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105229tnqud838686q8fc3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105229tnqud838686q8fc3.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_952638" aid="952638" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105232bygy0yt6b1beo5y1.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105232bygy0yt6b1beo5y1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105232bygy0yt6b1beo5y1.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>游戏采用的无缝大世界是众多亮点之一，可以分享下它的实现方式吗？</strong><br>
<br>
网易天谕手游：项目场景需求是大场景(2500 x 2500)，远视距(标志物件2000米)，场景丰富(日月升息, 万物有灵，大量三级物件)。引擎原生的单场景机制会造成场景资源占用内存过大，面数、drawcall压力大，多图加载耗时长等问题。<br>
<br>
<div align="center">
<img id="aimg_952639" aid="952639" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105235ydomzxsz9tetblla.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105235ydomzxsz9tetblla.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105235ydomzxsz9tetblla.jpg" referrerpolicy="no-referrer">
</div><br>
我们尝试过使用引擎提供的多场景机制，遇到了一些难以规避的问题。不过在此基础上，引擎也为我们提供了一些大场景的制作思路，并实现了大场景流式加载方案。<br>
<br>
制作阶段，我们给美术人员提供多人编辑工具，一个大场景可以分给若干人员，每人负责一块。制作完成后合并为一个大场景进行打光烘焙，提升制作效率。<br>
<br>
场景制作完成之后，我们会根据场景中物件的大小、类别、重要程度等信息，给每个物件计算一个推荐视距，美术人员可以在此基础上对特殊物件视距进行调整。<br>
<br>
<div align="center">
<img id="aimg_952640" aid="952640" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105238h9pmpqkp4tct9f38.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105238h9pmpqkp4tct9f38.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105238h9pmpqkp4tct9f38.jpg" referrerpolicy="no-referrer">
</div><br>
之后我们将大场景导出成配置文件和物件prefab，配置文件里面记录每个物件的资源路径、坐标、旋转、scale等信息。这个过程中，我们会根据物件的视距，对它们做分层和分块处理，并结构化存储在配置文件中，以提高运行时编辑场景物件的效率。<br>
<br>
运行时，系统会根据主角位置的变化，去计算当前需要加载/卸载的物件，并分帧进行加卸载操作，以保证只有玩家周围可以看到的物件在内存中，而离玩家较远的物件可以及时卸载。<br>
<br>
这样就基本解决了前面提到内存占用大、面数、drawcall高、切图时间长等问题。在此基础上，我们还做了一些其他工作，来优化流式加载中的效果和性能，包括：<br>
<br>
<ul><li>遮挡剔除优化面数，drawcall</li><li>Texture Streaming优化贴图内存</li><li>机型适配, 画质分级，整体缩放场景视距</li><li>使用LOD优化面数、内存</li><li>定制SRP Batch方案最优化渲染状态切换开销，优化drawcall开销</li><li>场景静态物件No GameObject化的优化实例化耗时</li><li>合理的缓存和资源总量控制，优化内存和实例化耗时</li><li>采用Vulkan技术降低功耗开销<br>
</li></ul><br>
游戏中采用了Unity最新的DOTS技术的JobSystem多线程管理器来实现鱼群的效果，可以分享下JobSystem的使用经验以及使用前后的数据对比吗？<br>
<br>
<div align="center">
<img id="aimg_952641" aid="952641" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105241xtu4afyuecxdc89t.gif" data-original="https://di.gameres.com/attachment/forum/202101/11/105241xtu4afyuecxdc89t.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105241xtu4afyuecxdc89t.gif" referrerpolicy="no-referrer">
</div><br>
网易天谕手游：Unity的DOTS在多线程开发的易用性和安全性方面提供了保障，《天谕》手游借此开发了多种鱼群生态行为和优化算法，实现了40余种、8000多条，不同鱼群生态的海底效果。<br>
<br>
我们在iPhone6s 单worker线程跑5000条鱼的情况下，按照耗时能达到理论上250帧 ，在核心数更多的手机上，可以有更加优秀的性能表现。Unity的DOTS确实为更底层的性能提升提供了可能性，是一个革命性的技术。<br>
<br>
以下是iphone 6s上5000条鱼可以跑250帧的耗时分布：<br>
<br>
<div align="center">
<img id="aimg_952642" aid="952642" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105243or755d58j8hrhjtr.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105243or755d58j8hrhjtr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105243or755d58j8hrhjtr.jpg" referrerpolicy="no-referrer">
</div><br>
《天谕》手游实现了对游戏性能优化高要求的千人同屏玩法，可以分享一下项目组的性能优化经验吗？<br>
<br>
<div align="center">
<img id="aimg_952643" aid="952643" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105246q7n37aegnx9xvy5x.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105246q7n37aegnx9xvy5x.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105246q7n37aegnx9xvy5x.jpg" referrerpolicy="no-referrer">
</div><br>
网易天谕手游：首先，我们要非常感谢Unity技术团队每个月来项目组驻场，持续为项目提供性能分析和优化服务，毕竟优化这件事不是一蹴而就的。<br>
<br>
群战在客户端上做过的的优化主要包括：<br>
<br>
<ul><li>热点代码（比如战斗逻辑、位置同步等）本地化，降低CPU消耗；</li><li>加入了特效分级和总量控制机制，限定同屏特效的数量和消耗；</li><li>AI人数加入逻辑个数限制和模型显示数量限制，以及模型LOD分级，从逻辑和渲染两个方面控制人物消耗；</li><li>动画逻辑制定了分帧和总量控制系统，减少瞬时卡顿；</li><li>合理的特效、动画、角色模型等的缓存逻辑；</li><li>实现游戏动态分辨率方案，自动根据特效的播放量进行分辨率的动态改变，降低功耗。<br>
</li></ul><br>
<strong>游戏中的次世代渲染技术也是一大亮点，手机端的云海渲染方式可以分享下吗？</strong><br>
<br>
网易天谕手游：为了构建幻想的立体海天大世界，我们实现了很多次时代渲染技术。手机游戏的渲染技术的难点是必须对所有已经在PC和主机上使用的渲染技术进行深度优化和方案改进。<br>
<br>
比如云海使用在手机上实现超高品质的可造型、可穿行、可随24小时天气变换的云海效果。<br>
<br>
首先，通过多张3D Texture存储云的形态，美术可通过模型和曲线的形式编辑云海，实现任意造型。<br>
<br>
<div align="center">
<img id="aimg_952644" aid="952644" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105248clxzpucpls7zpzc4.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105248clxzpucpls7zpzc4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105248clxzpucpls7zpzc4.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_952645" aid="952645" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105249igadl34dmt0443ax.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105249igadl34dmt0443ax.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105249igadl34dmt0443ax.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_952646" aid="952646" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105252imvca3p5dzdopaws.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105252imvca3p5dzdopaws.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105252imvca3p5dzdopaws.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_952647" aid="952647" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105253nnn99zulxvnllgag.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105253nnn99zulxvnllgag.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105253nnn99zulxvnllgag.jpg" referrerpolicy="no-referrer">
</div><br>
我们使用Ray Marching做云海的绘制。<br>
<br>
为了流畅性，我们做了很深度的性能优化，比如使用Sphere Tracing降低步进、使用Jittering 解决采样率不足的问题，使用Mixed Resolution Rendering降低Fragment的渲染开销，使用TAA降噪。在万米高空、层云多叠、资源爆炸的情况下，在非常低端的手机上，依然可以流畅的体验云海效果。<br>
<br>
TAA前：<br>
<br>
<div align="center">
<img id="aimg_952648" aid="952648" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105255fd33aqm52vaa05ca.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105255fd33aqm52vaa05ca.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105255fd33aqm52vaa05ca.jpg" referrerpolicy="no-referrer">
</div><br>
TAA后：<br>
<br>
<div align="center">
<img id="aimg_952649" aid="952649" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105256hvk8zk8j9kksywv1.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105256hvk8zk8j9kksywv1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105256hvk8zk8j9kksywv1.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_952650" aid="952650" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105257ah8gee5cf3tkaex2.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105257ah8gee5cf3tkaex2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105257ah8gee5cf3tkaex2.jpg" referrerpolicy="no-referrer">
</div><br>
海量鱼群、海底水体以及超大规模植被的渲染工作，也是开发者比较关注的点，可以分享这些如何在Unity引擎中实现吗？<br>
<br>
网易天谕手游：鱼群渲染主要是采用Unity DOTS进行比较深度的性能优化，可以实现海量的鱼群渲染。<br>
<br>
<div align="center">
<img id="aimg_952651" aid="952651" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105258a2v2wyuwgl57lwkl.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105258a2v2wyuwgl57lwkl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105258a2v2wyuwgl57lwkl.jpg" referrerpolicy="no-referrer">
</div><br>
海底的渲染我们通过模拟水体吸收光的特性，定制了特殊的雾效和屏幕后期处理方案。让整体的色彩氛围能够符合水下的感受。<br>
<br>
另外，海中还有很多特殊的光影效果，比如焦散、海面射入海底的光线散射、水中漂浮物。我们也实现了定制化的渲染方案，让整体的海底氛围感能够得到比较好的表现。<br>
<br>
<div align="center">
<img id="aimg_952652" aid="952652" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105259fj7j5o7jayioqibi.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105259fj7j5o7jayioqibi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105259fj7j5o7jayioqibi.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_952653" aid="952653" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105300wy3k3vi3vkshoodi.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105300wy3k3vi3vkshoodi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105300wy3k3vi3vkshoodi.jpg" referrerpolicy="no-referrer">
</div><br>
超大规模植被的渲染主要的挑战来自于渲染性能的压力，我们几乎每个大地图都规划大量的植被，比如苏澜的花海、盈川的草海。它的优化可以从几个方面来做：<br>
<br>
<ul><li>降低Overdraw开销，一个是尽量减少PS的开销，我们几乎把所有的光影计算都放在VS来完成，这样PS的开销就特别小；</li><li>比较好的LOD方案，我们一般会做3级LOD，在切换LOD的时候做一定的随机切换保证过渡的平滑性，通过LOD方案可以降低面数和Overdraw；</li><li>因为数量特别多，遮挡剔除也是需要按照块来进行层级的剔除，这样能够减少遮挡剔除带来的计算开销；</li><li>另外，草海花海这种数量特别多的资源需要特殊的存储方式来用最小的文件大小来记录每个草的位置和旋转信息。<br>
</li></ul><br>
<div align="center">
<img id="aimg_952654" aid="952654" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105301ztllplpfgynxjtct.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105301ztllplpfgynxjtct.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105301ztllplpfgynxjtct.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_952655" aid="952655" zoomfile="https://di.gameres.com/attachment/forum/202101/11/105302irnjn7dkmonnhnor.jpg" data-original="https://di.gameres.com/attachment/forum/202101/11/105302irnjn7dkmonnhnor.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/11/105302irnjn7dkmonnhnor.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>你们是否考虑在移动平台上加入光线追踪的功能？</strong><br>
<br>
网易天谕手游：我们会在游戏后续的版本迭代中加入光追的功能，未来可以针对各类不规则表面的玻璃曲面、镜面、盔甲、水面，实现非常真实的反射效果。<br>
<br>
<strong>你们在为《天谕》手游做引擎选型时，是如何考虑的？</strong><br>
<br>
网易天谕手游：Unity具有非常好的开发者基础，这让我们可以快速在项目立项之初组建一只经验丰富的研发团队。开发的过程中，Unity方便易用、迭代速度快，可以大幅降低大型游戏的开发成本，并且成本可控。<br>
<br>
新版Unity发布了DOTS和SRP功能。DOTS是一个革命性的技术，对大规模的角色对象模拟提供了更深度的优化。SRP则提供了定制引擎渲染管线更便捷的方案，降低了很多我们渲染定制的工作量。另外SRP的渲染性能也比老的内置渲染管线有很大的提升，是一个非常有价值的技术。<br>
<br>
其次，Unity中国区提供了全面的性能优化支持和技术美术支持，有一批固定的工程师长期跟随驻扎在我们的项目现场。Unity官方在很多方面会提前给出开发建议，节约了项目组探索尝试的时间成本。<br>
<br>
这两年Unity在工具链上也提供给开发者更多便利的开发工具，比如收集崩溃数据的Backtrace及自动化性能测试工具UPR，让我们可以安心使用全套工具链，把精力放在开发高品质游戏本身。<br>
<br>
<font size="2"><font color="#808080">来源：游戏葡萄</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/9V9AvaCwtQeezXKNxjhbVA</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            