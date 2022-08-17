
---
title: '元宇宙基建狂魔？Cocos v3.6 正式发布功能大更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-522820aa9aa19d74fb0e36c096e893af4c6.jpg'
author: 开源中国
comments: false
date: Wed, 17 Aug 2022 17:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-522820aa9aa19d74fb0e36c096e893af4c6.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>8月17日，国内老牌3D游戏引擎 Cocos 宣布推出 Cocos Creator v3.6，该版本从画面渲染、性能、原生化、编辑器优化等方面都大幅进化，是 Cocos 在3D领域的里程碑级版本，一推出就刷新了业内对于 Cocos 只擅长2D的刻板印象，而v3.6版本的发布，也将开拓 Cocos 在游戏、虚拟人、xr、智能座舱、教育等诸多领域的应用宽度。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><img alt height="638" src="https://oscimg.oschina.net/oscnet/up-522820aa9aa19d74fb0e36c096e893af4c6.jpg" width="1500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0.0001pt; margin-right:0px"> </p> 
<h1 style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><strong><span><span><span><strong>渲染能力、原生性能全面升级</strong></span></span></span></strong></span></span></span></span></span></h1> 
<h1 style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><strong><span><span><span><strong>推动</strong></span></span></span></strong><strong><span><span><span><strong>更高</strong></span></span></span></strong><strong><span><span><span><strong>品质3D内容开发</strong></span></span></span></strong></span></span></span></span></span></h1> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>对任何3D内容来说，画面永远是第一关注点。一直以来，业内对 Cocos 的3D渲染能力质疑声不断，这个在2D时代堪称王者的老牌引擎，曾经以《剑与远征》、《我叫MT》、《少年三国志》、《列王的纷争》、《保卫萝卜》、《TopWar》、《火焰纹章》等席卷国内外手游行业，曾经在App Annie全球最赚钱、用户数最多的前十款手游中就有5款是用 Cocos 做的，这也造就了很多人对 Cocos 只擅长 2D，不擅长 3D 的错觉。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>事实上，Cocos 的3D能力已经在很多大型游戏项目上得到了验证，而此次其发布的 Cocos Creator v3.6 更是被官方称为“两年来最重要的版本”，其引擎负责人表示 “对于开发者来说，3.6 </span></span></span><span><span><span>版本</span></span></span><span><span><span>意味着引擎在 3D & 2D 开发上体验更好、性能更高、效果更出众。 ”</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>从这句话，也能看出 Cocos 内部，对这个版本的信心，记者了解到，v3.6版本在3D画面渲染能力上颇下了一番苦工，重点优化了对3D内容非常重要的材质导入功能与渲染算法，包括了Surface Shader 自定义材质、CSM级联阴影、各向异性光照模型、GGX环境反射卷积图等重点功能，这些功能的落地，意味着 Cocos 已经能够基本满足现代3D游戏的画面需求。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>以CSM级联阴影为例，它能很好地解决画面阴影锯齿严重、形状缺失、不清晰等问题，而阴影无论是游戏或者任一元宇宙项目,都是呈现更为逼真的3D场景感的关键点之一，在 Cocos 编辑器通过CSM级联阴影，可以完美解决物体的阴影可视距离与阴影效果上的平衡问题。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><img alt height="538" src="https://oscimg.oschina.net/oscnet/up-abe153d7c91053ca302a135da6b4bce99e1.gif" width="986" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>各向异性光照模型则拓展了 Cocos 在更多材质的应用，借助这个功能，用户就在精确光源和环境光源下，通过材质与光照模型，可以制作拉丝纹路的金属、头发、丝绸等等，比如下图的面料的质感，就是在 Cocos v3.6内渲染而成的。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><img alt src="https://oscimg.oschina.net/oscnet/up-36f5fc56ae41272c076dc3d61d9da8f7dff.gif" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>更好的渲染效果一般意味着需要更强的性能开销，此次，Cocos 在性能上同样有大幅提升，而且其兼顾了 2D & 3D 内容的性能需求，测试显 v3.6 不仅3D性能大幅提升，同时其2D性能，在不同机型上都已经接近甚至超越了其一度在国内占有率超过70%的 2.x 版本。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>"原生化"也是这次 Cocos 发力点，在 v3.6 Cocos 重写了一遍底层架构，将2D渲染数据结构、2D合批管理器及渲染流程都进行了原生化，这意味着 Cocos 在原生端和小游戏端都有了更加具备针对性的性能解决方案，从下图可以看出 Cocos 完全原生化的目标实现不远了，加上其免费开源、跨平台发布的差异化优势，未来它或许将称为国内原生游戏的首选引擎。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><img alt height="780" src="https://oscimg.oschina.net/oscnet/up-c3c0c5008462b32593fc5e021135ecb04b9.png" width="1386" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span>（绿色部分即 Cocos 完成原生化的模块）</span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"> </p> 
<h1 style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><strong><span><span><span><strong>编辑器预览功能</strong></span></span></span></strong></span></span></span></span></span></h1> 
<h1 style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><strong><span><span><span><strong>真正实现开发“所见即所得”</strong></span></span></span></strong></span></span></span></span></span></h1> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>此次3.6 版本在编辑器界面上也做了非常大的改动，其中最受开发者关注的莫过于 Game View 模式。除了原有的网页预览和模拟器预览，现在 Cocos 开发者还可以使用「编辑器预览」来运行游戏。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>编辑器预览将在场景管理器中直接执行游戏逻辑，并且可以实时调试游戏场景，一方面带来更无缝的预览体验，另一方面也补足了在调试方面的短板。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><img alt height="1518" src="https://oscimg.oschina.net/oscnet/up-435f80efd4c49917eb301604b93c215bd93.jpg" width="2560" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>不仅如此，动画编辑器也实现了嵌入播放粒子和其他动画的能力，让开发者可以快速调试复杂的组合动画和粒子联动，极大得提升了游戏内动画和特效的生产效率，也是国内实现该功能的引擎。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><img alt src="https://oscimg.oschina.net/oscnet/up-6f64abcd22fa4770cf3329ddd863fe21cda.gif" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><strong><span><span><span><strong>内置出海神器「L10n」</strong></span></span></span></strong></span></span></span></span></span></h1> 
<h1 style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><strong><span><span><span><strong>助力出海开发者本地化</strong></span></span></span></strong></span></span></span></span></span></h1> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>为了更好地服务有出海需求的广大开发者，Cocos Creator 3.6 内置了全新的可视化多语言编辑器，即I10n，全程无代码化操作，开发者只需经过内容、翻译内容与构建发布三个步骤，即可将项目构建为不同语言的多个版本，随时预览，随时切换语言，对于有出海需求的厂商来说，堪称一个“神器“。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><img alt height="850" src="https://oscimg.oschina.net/oscnet/up-bfcf2c334a70c8fe8466e3840e0234390c7.png" width="1578" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0.0001pt; margin-right:0px"> </p> 
<h1 style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><strong><span><span><span><strong>抢滩元宇宙</strong></span></span></span></strong></span></span></span></span></span></h1> 
<h1 style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><strong><span><span><span><strong>Cocos 探索3D内容爆发机遇</strong></span></span></span></strong></span></span></span></span></span></h1> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>上述所有功能，不仅有益于游戏行业，同时也能够让元宇宙领域厂商通过这些强大的技术模块，抢滩“元宇宙”窗口期。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span><span><span><span>从“游戏开发工具”到“数字化生产力工具”的形态转化，这是 Cocos 近一年来一直发力的目标，在许多国内大热的元宇宙项目里都有 Cocos 的身影。不久前，百度刚推出了其首个支持快速开发独立元宇宙产品的开放平台「希壤」，其中就有基于 Cocos 打造的一站式元宇宙内容开发解决方案「希壤Lite」，借助 Cocos 引擎能力，希壤Lite 能够更轻量化地满足用户的分享与体验，并且同时支持多平台，进一步降低用户使用门槛，提供更丰富的应用场景，开辟里世界切换、社交互动、虚拟演唱会等趣味玩法。</span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><img alt height="751" src="https://oscimg.oschina.net/oscnet/up-4c1cb927b7acd49a968655fce0728abbd44.png" width="1386" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0.0001pt; margin-right:0px"><span><span><span><span><span> </span></span></span></span></span><span><span><span><span><span><span><span><span>未来，各行各业都会存在大量需要开发的3D内容，Cocos 也在不断拓展自己的能力边界。据悉，今年下半年 Cocos 将推出编辑器组件 Cocos Creator XR，以及无代码、所见即所得的虚拟角色编辑器，这些都得益于V3.6 所打下的良好基础，相信未来国内会有越来越多的行业，通过 Cocos 实现更多3D场景的落地。</span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            