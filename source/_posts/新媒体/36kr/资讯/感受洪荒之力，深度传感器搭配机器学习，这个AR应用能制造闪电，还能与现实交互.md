
---
title: '感受洪荒之力，深度传感器搭配机器学习，这个AR应用能制造闪电，还能与现实交互'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220217/v2_8d261fb8164f4f378f49631acd183341_img_000'
author: 36kr
comments: false
date: Thu, 17 Feb 2022 07:59:01 GMT
thumbnail: 'https://img.36krcdn.com/20220217/v2_8d261fb8164f4f378f49631acd183341_img_000'
---

<div>   
<p>年轻人，你渴望力量吗？</p> 
<p>就是那种能在指尖召唤闪电，随手一扔就能造成大量伤害的力量。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220217/v2_8d261fb8164f4f378f49631acd183341_img_000" referrerpolicy="no-referrer"></p> 
<p>现在，你只需要动动你的手指，就能在指尖形成一股能量，这股能量也能和现实世界产生互动，这个闪电还会消散形成细小的电流，在物体边缘上下流动，留下粉色的光芒。</p> 
<p>就像这样：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220217/v2_4360e2a3c9b34158b63a98cc8fefd1c1_img_000" referrerpolicy="no-referrer"></p> 
<p>这款名叫<strong>Let's All Be Wizards!</strong>的应用已经<a class="project-link" data-id="187722" data-name="上线了" data-logo="https://img.36krcdn.com/20220120/v2_4ea0942a63674b4d8b32a55f9a5167b9_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4210300001?mp=zzquote" target="_blank">上线了</a>App Store，售价<strong>2.99美元</strong>。不过由于需要利用到<strong>LiDAR</strong>，因此目前也只有iPhone 12 Pro和iPhone 13 Pro用户能够<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20210807/v2_966db147ab4646ef82349f069ce61219_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>这股力量。</p> 
<p>没想到吧，如此神奇的力量竟然也隐藏在你的手机中。</p> 
<p>相关视频在Reddit和LinkedIn上都引起了十分热烈的讨论和围观，比如有网友就赞叹到，“和房间的联动也太厉害了吧”。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220217/v2_96d6170fbb4847cf854d2c0db83336bb_img_000" referrerpolicy="no-referrer"></p> 
<p>还有人表示，“这肯定是一个很棒的NFT”。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220217/v2_215c8b1ac4d147108b81aa7297e32e29_img_000" referrerpolicy="no-referrer"></p> 
<p>接下来就和文摘菌<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>来看看这股力量的<a class="project-link" data-id="28387" data-name="源泉" data-logo="https://img.36krcdn.com/20210806/v2_f22ebf248fd946debb31c0454b3b7445_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/28387" target="_blank">源泉</a>吧~</p> 
<h2><strong>深度传感器+机器学习，LiDAR也是关键之一</strong></h2> 
<p>首先，除了一台支持LiDAR的苹果手机外，还需要准备到Unity 2020.3LTS和ARFoundation。</p> 
<p>既然力量要从手中展现，那就必然要对手部进行捕捉，这就需要60FPS手部检测（60 FPS hand detection）</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220217/v2_a469f8dd3d584f5c97bf8addf54dfb56_img_000" referrerpolicy="no-referrer"></p> 
<p>以及3D骨骼世界检测（3D Bones world detection）。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220217/v2_42fe65020e55464caa68e5da65f19507_img_000" referrerpolicy="no-referrer"></p> 
<p>也正是基于此，LiDAR就显得尤为必要，因为位置允许手上的准确照明（次表面散射）或边缘检测（用于最后返回的火花）以真正将原生世界和虚拟世界融合在一起。<strong>如果没有实时深度估计，这些功能都不可能实现。</strong></p> 
<p>空间网格上的照明也是通过5个渲染器通道来实现的：</p> 
<ul> 
 <li>每个像素（屏幕空间）的法线和距离</li> 
 <li>背景相机和手部遮挡</li> 
 <li>手部次表面散射照明</li> 
 <li>光晕和游戏空间fx（实际上，每个能量球一次通过）</li> 
 <li>透明和不透明对象</li> 
</ul> 
<p>正如项目作者Olivier Goguel总结的那样，“由于<strong>深度传感器</strong>和<strong>基于视觉的机器学习</strong>，我们可以实时创建手及其周围环境的数字版本，以生成虚拟和真实物体无缝交互的3D环境”。</p> 
<p>该项目也已经在GitHub上开源了，详细过程大家也可以自行前往查看：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220217/v2_c1f44de7d0bf47e8805036829d4ec235_img_000" referrerpolicy="no-referrer"></p> 
<p>项目链接：</p> 
<p>https://github.com/ogoguel/realtimehand </p> 
<h2><strong>混合现实和物体识别打破游戏和数据的束缚</strong></h2> 
<p>翻开Olivier Goguel的LinkedIn主页，文摘菌也被这满满的履历“闪瞎了眼”。</p> 
<p>作为一名电子游戏爱好者，Goguel先后在Argonaut、Lagardere Active、Mimesis Republic、Namco、Microsoft和Asobo Studio等大型电子游戏公司工作了超过25年。也正是这些经历，让他有机会将一些技术和思维应用于许多娱乐项目上，其中就包括<strong>AR/VR体验</strong>。</p> 
<p>目前他在HoloForge Interactive担任CTO一职。</p> 
<p>在HoloForge Interactive的官网上，他们就表示，他们要在个人、地点和数据融合的体验中，打破束缚，充分发挥其潜力。</p> 
<p>比如在2016年，他们就与Microsoft合作，开发了通过<strong>混合现实和物体识别</strong>进行体验的游戏Young Conker。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220217/v2_e9ef7c8d910245088c24d4664ef722d5_img_000" referrerpolicy="no-referrer"></p> 
<p>在游戏中，场景都将<strong>直接在房间里构建</strong>，比如敌人会出现在咖啡桌周围，你的沙发里可能藏着要收集的物品，你需要蹦床去看电视等等。关卡也会随着环境而适应并随之变化。</p> 
<p>在这个项目中，开发者们需要攻克以下几点难关：</p> 
<ul> 
 <li>：游戏检测环境的拓扑结构，然后找出其组成部分。系统需要检测房间中的地板、墙壁和天花板以及各种不同类型的家具，并与游戏中的角色创造独特的互动。</li> 
 <li>：玩家可以用目光移动主角，无需操纵杆即可实时精确控制游戏操作。</li> 
 <li>：游戏使用空间映射工具，并采用人工智能自动生成关卡和角色定位。</li> 
 <li>：由于游戏知道玩家的位置和正在寻找的位置，因此每个角色都可以以不同且令人惊讶的方式对玩家的存在做出反应。</li> 
</ul> 
<h2><strong>Local Lenses如何改变对城市的观看方式</strong></h2> 
<p>说到AR，文摘菌印象最深刻的还要属前年Snapchat推出的一个户外AR项目Local Lenses。</p> 
<p>这个AR项目与专注于地图的竞争对手不同，Snap计划让用户使用数字内容来改变社区的外观，用户可以“用彩色油漆装饰附近的建筑物”，效果将对朋友可见。</p> 
<p>从官方<a class="project-link" data-id="25154" data-name="安利" data-logo="https://img.36krcdn.com/20210806/v2_aa723257056b41e9afc7d1c33dc33d45_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25154" target="_blank">安利</a>视频上看，Snapchat的这个AR简直是手残党福音了，你能随意对城市进行填涂，操作起来也很简单，只需要在Snapchat上调用摄像头，City Painter就能让你在街道上方喷洒红色和蓝色的“喷泉”，然后用预先设计的涂鸦对墙面砖块进<a class="project-link" data-id="595870" data-name="行装" data-logo="https://img.36krcdn.com/20210814/v2_4d06b5a55cdf48c6990f55fe7c2b4827_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/595870" target="_blank">行装</a>饰。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220217/v2_fcd31808f05e4b818e5ddaab5b5fde56_img_000" referrerpolicy="no-referrer"></p> 
<p>看着爽快，开发Local Lens的过程可没有那么简单，首先就在于<strong>重要公共地标的3D数据太少</strong>，其次还需要<strong>选择一个用户无需担心交通问题的街道</strong>。 </p> 
<p>同时，虽然用户平时不会在每个角度上都对街道照留念，但空间的绝对大小对于开发者来说也是一个不小的难题。在这个意义上，附属于Local Lens的City Painter独辟蹊径，用3D绘制了整个卡纳比街，<strong>方便用户从任意角度进行绘制</strong>，这也改变了人们对城市的观看方法。 </p> 
<p>Snapchat从多个来源提取出了街道的视觉数据，包括<strong>用户共享的公开照片</strong>。“对于Local Lens反射出的景象，我们利用<strong>360度的相机图像</strong>，”Pan表示，“人们走<a class="project-link" data-id="28303" data-name="在街上" data-logo="https://img.36krcdn.com/20210806/v2_cbf6db084e364e2dbf31238e770a0340_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/28303" target="_blank">在街上</a>就能绘制地图，还可以把它与我们可能拥有的、任何关于该地区的公共新闻照片结合起来”。 </p> 
<p>City Painter还支持<strong>经验共享</strong>。正如Pan所说，“当你对外部环境做某事时，其他人几乎可以同步看到结果。就算后来你离开了，第二天出现了新的参观者，这些变化也将会持续存在，也就是说，这些新人能看到自己和他人所改变的空间”。 </p> 
<p>如今随着元宇宙概念逐渐被理解和研究，相信未来会有更多有趣的VR和AR项目被开发出来吧！ </p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号 <a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MjM5MTQzNzU2NA==&mid=2651710630&idx=1&sn=f8a5f311584df68f612d8c3aaf2b2ff2&chksm=bd4cc3358a3b4a23851ae6d5d19b791cdc5f36387341efb1e5384a519c1782b26b62af1618b5#rd">“大数据文摘”（ID：BigDataDigest）</a>，作者：Caleb，36氪经授权发布。</p>  
</div>
            