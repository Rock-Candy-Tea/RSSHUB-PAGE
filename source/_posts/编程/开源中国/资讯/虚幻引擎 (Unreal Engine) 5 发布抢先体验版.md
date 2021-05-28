
---
title: '虚幻引擎 (Unreal Engine) 5 发布抢先体验版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7cab746300260a134bdb6f44f77a67a8afd.png'
author: 开源中国
comments: false
date: Fri, 28 May 2021 07:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7cab746300260a134bdb6f44f77a67a8afd.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>虚幻引擎 5 的抢先体验版现已推出！</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7cab746300260a134bdb6f44f77a67a8afd.png" referrerpolicy="no-referrer"></p> 
<p>发布公告称：“此版本尚未达到生产标准，但你可以通过它首次接触到一些在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.unrealengine.com%2Fzh-CN%2Fblog%2Fa-first-look-at-unreal-engine-5" target="_blank">去年的公布</a>演示中令你兴奋万分的技术——更不用说它还将包含一些你从未见过的技术。”</p> 
<p>下面总结了如今已经可以公开测试的重要新功能。</p> 
<h1>Nanite</h1> 
<p>Nanite是一个<strong>虚拟化微多边形几何体系统</strong>，你可以通过它创作具有海量几何体细节的游戏，省去将细节烘焙到法线贴图或手动编辑LOD等费时费力的工作。 </p> 
<p>想象一下，直接导入由数以百万计的多边形组成的电影级美术资源——从ZBrush雕刻到摄影测绘扫描的任何资源——将它们布置数百万次之多，而且自始至终保持实时帧率，没有任何明显的保真度损失。觉得这不可能吗？时代变了！</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-125e402f7318855eb5b5879aa93f9c0880f.png" referrerpolicy="no-referrer"></p> 
<h1>Lumen</h1> 
<p>接下来是Lumen，一种全动态全局光照解决方案。有了Lumen，你就可以创建动态、逼真的场景，其中的间接光照能够实时适应直接光照或几何体的变化——例如根据天时改变太阳的角度，打开手电筒或打开房门。</p> 
<p>有了Lumen，你再也不需要编辑光照贴图UV，等待光照贴图烘焙或放置反射捕捉；你只需要在虚幻编辑器中创建和编辑光源，然后就能看到游戏在主机上运行时的最终光照效果。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-3838cd69f34b1b15b4f7988fa93ad2bc43f.png" referrerpolicy="no-referrer"></p> 
<h1>开放世界场景</h1> 
<p>我们始终致力于让各种规模的团队都能更方便、更快捷、更协作地创建开放世界场景。如今你可以试用一些将让我们实现这个目标的步骤。</p> 
<p>首先是新的<strong>世界分区</strong>系统，它能够自动将世界场景划分为网格，并在需要时流送所需网格。然后是新的<strong>每Actor一文件</strong>系统，它将使协作变得更方便——你和你的团队成员现在可以同时处理同一个世界场景的同一个区域，而不会相互干扰。</p> 
<p>最后是<strong>数据分层</strong>，它让你能够创建同一个世界场景的不同变体——例如日间和夜间版本，或者通过游戏玩法启用的特定数据集——作为同一空间中的分层。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4acf2320401f2b2094c4073b9a84b4470f9.png" referrerpolicy="no-referrer"></p> 
<h1>动画</h1> 
<p>如果你总是需要转到虚幻引擎之外来创建或编辑动画，不仅费时而痛苦，也妨碍了迭代。这就是为什么我们在虚幻引擎5中扩展和增强了我们的动画工具集，让你能够直接在情境中创作异常精美的角色。</p> 
<p><strong>控制绑定</strong>等对美术师友好的工具可以让你快速创建骨架绑定，并在多个角色之间共享；你可以在Sequencer中摆好他们的姿势，并使用新的<strong>姿势浏览器</strong>将这些姿势作为资源保存和运用；还可以使用新的<strong>全身IK</strong>解算器轻松创作自然的动作。与此同时，<strong>运动扭曲</strong>可以让你动态调节角色的根动作来适应不同目标——例如用一个动画就做出跃过不同高度的墙壁的动作。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-201d1030aedfa876a59a8768704993f50a7.png" referrerpolicy="no-referrer"></p> 
<h1>MetaSounds</h1> 
<p>你可曾梦想过，在创作音频体验时拥有和外观开发一样多的控制能力和灵活性？我们在UE5中将推出一种制作音频的全新方法。<strong>MetaSounds</strong>是一个高性能的系统，可以让你全面控制音源的音频DSP图表生成，管理音频渲染的各个方面，推动实现次世代的程序化音频体验。</p> 
<p>MetaSounds好比一条完全可程控的材质和渲染管线，将材质编辑器为着色器实现的所有程序化内容创建的优点都带到了音频领域：动态的数据驱动资源，将游戏参数映射到声音播放的功能，工作流程的大幅改进，等等。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-22b4975e11f16ff37f5513c287097c85f8f.png" referrerpolicy="no-referrer"></p> 
<h1>增强的编辑器UI和工作流程</h1> 
<p>改头换面的时候到了！在UE5中，虚幻编辑器将获得新颖的外观、精简的工作流程和对屏幕空间的优化利用，使它用起来更方便、更快捷、更赏心悦目。</p> 
<p>这个抢先体验版中的新功能包括：轻松调出和隐藏内容浏览器，将任何编辑器选项卡驻停到可折叠侧边栏，以腾出更多空间用于视口交互；一个新的收藏系统，用于快速访问“细节”面板中的常用属性；主工具栏上新增的“创建”按钮，方便将Actor放入场景；还有经过简化的新建项目流程。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c41655f6750637321b63138989ea6b9d1b5.png" referrerpolicy="no-referrer"></p> 
<p>有关所有新功能的详细信息，请参见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.unrealengine.com%2F5.0%2Fzh-CN%2FReleaseNotes%2F" target="_blank">版本说明</a>。</p> 
<h1>获取虚幻引擎5抢先体验版</h1> 
<p>如果你已经是虚幻引擎用户，可以从Epic Games启动程序获取UE5抢先体验版和“遗迹峡谷”示例项目。如果你还是新手上路，可先从下方的按钮开始。同时我们也建议你先了解一下虚幻引擎4.26。</p> 
<ul> 
 <li><a href="com.epicgames.launcher://ue/ue5ea" target="_blank">获取UE5抢先体验版</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.unrealengine.com%2Fzh-CN%2Fdownload" target="_blank">从UE 4.26开始</a></li> 
</ul>
                                        </div>
                                      
</div>
            