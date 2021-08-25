
---
title: 'Cocos 引擎 3D 技术再升级，打造赛博朋克极致渲染效果'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20210825/1629885712_218775.png'
author: 3DMGame
comments: false
date: Wed, 25 Aug 2021 10:02:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20210825/1629885712_218775.png'
---

<div>   
<p style="text-indent:2em;">
近年来，游戏开发行业进入了技术军备竞赛，在保证玩法创意的同时，都在尽可能地提升画面的精美程度和复杂场景的渲染流畅度，玩家对游戏画质的要求也日益挑剔。昨日，主流游戏引擎之一 
Cocos 官方发布了一个赛博朋克风格的 3D 渲染效果技术演示，这个基于最新发布的 Cocos Creator 3.3 
制作的实时渲染，刷新了行业对其3D技术能力的认知，得到了不少游戏开发者的认可，技术演示中展现了包括延迟渲染管线技术、Cluster Light 
Culling、Cluster Reflection Probe、指数高度雾在内的多个特性。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210825/1629885712_218775.png" alt="Cocos 引擎 3D 技术再升级，打造赛博朋克极致渲染效果" referrerpolicy="no-referrer">
</p>
<p style="text-align:center;text-indent:2em;">
Cocos 3D技术演示部分画面
</p>
<p style="text-indent:2em;">
说到 Cocos 
，许多游戏开发者对它的印象都停留在2D游戏领域，因为其开源、易上手、高性能和跨平台等产品特性，深受游戏开发者的青睐。然而这次推出的赛博朋克 3D 
技术演示，打破了许多人对 Cocos 只擅长做2D游戏的固有印象，给人眼前一亮的感觉。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210825/1629885712_521414.png" alt="Cocos 引擎 3D 技术再升级，打造赛博朋克极致渲染效果" referrerpolicy="no-referrer">
</p>
<p style="text-align:center;text-indent:2em;">
Cocos 3D技术演示部分画面
</p>
<p style="text-indent:2em;">
<strong>技术释放想象力 Cocos 构建强大3D渲染能力</strong>
</p>
<p style="text-indent:2em;">
对于游戏玩家来说，一款好的3D游戏画面和体验缺一不可。就画面而言，Cocos 
推出的赛博朋克技术演示，不论是从画面的质感与细节的精细程度，都能看出Cocos 在3D游戏领域已经具备了相对成熟的技术。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210825/1629885711_470111.png" alt="Cocos 引擎 3D 技术再升级，打造赛博朋克极致渲染效果" referrerpolicy="no-referrer">
</p>
<p style="text-align:center;text-indent:2em;">
Cocos 3D技术演示部分画面
</p>
<p style="text-indent:2em;">
我们可以看到画面中，各种霓虹灯的灯光效果构成了充斥着整个赛博朋克世界，当画面中有成千上百个光源的时候，Cocos 通过 Cluster Light 
Culling 
技术进行光源信息的计算，因为让每个像素对所有光源都进行一次光照计算也是吃不消的，需要先剔除掉影响不到像素的光源，然后按照距离选取离像素最近的几个光源来渲染，就能快速提升在光源的计算效率。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210825/1629885711_921620.png" alt="Cocos 引擎 3D 技术再升级，打造赛博朋克极致渲染效果" referrerpolicy="no-referrer">
</p>
<p style="text-align:center;text-indent:2em;">
Cocos Creator 编辑器内画面
</p>
<p style="text-indent:2em;">
同时，不论是地面上水滩的倒影，或者是房间镜子里的反射，都极大地增加了渲染的难度，这里 Cocos 则是利用 Cluster Reflection 
Probe 
技术，将整个世界烘焙到一张环境贴图中，渲染镜面的时候根据视角跟物体表面法线计算出反射方向，从环境贴图中读取反射方向的光照信息，整合到光照计算中，这样便可大大增强渲染的真实感。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210825/1629885711_556351.png" alt="Cocos 引擎 3D 技术再升级，打造赛博朋克极致渲染效果" referrerpolicy="no-referrer">
</p>
<p style="text-align:center;text-indent:2em;">
Cluster Reflection Probe 开启反射球效果展示
</p>
<p style="text-indent:2em;">
除了在渲染方面之外，整个世界充斥着环境污染营造出来的氛围感同样引人入胜，这是 Cocos 
通过指数高度雾来增加了雾的通透性，通过动态天空盒技术塑造白天和夜晚不同的氛围感，而这些只是其中的一部分，还有更多的技术我们都可以在赛博朋克技术演示里去发现。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210825/1629885711_491419.png" alt="Cocos 引擎 3D 技术再升级，打造赛博朋克极致渲染效果" referrerpolicy="no-referrer">
</p>
<p style="text-align:center;text-indent:2em;">
指数高度雾
</p>
<p style="text-indent:2em;">
<strong>Cocos Creator 3.3发布 多项性能优化效果显著</strong>
</p>
<p style="text-indent:2em;">
作为一个低调的技术型品牌，Cocos 深耕行业多年，沉下心钻研技术，早已有了大量的技术储备，短短的几分钟视频，预示着 Cocos 从 2D 游戏领域到 
3D 游戏领域的华丽转身。
</p>
<p style="text-indent:2em;">
而在最新的 Cocos Creator 3.3 版本中，里面不仅优化了许多相应的技术，更是加强了引擎的整体性能。如果说今年年初3.0版本的出现，外界对 
Cocos 的3D技术还存在质疑，相信3.3版本的更新，则是对所有质疑最有力的证明。
</p>
<p style="text-indent:2em;">
通过测试发现，Cocos Creator 3.3 
的启动性能、运行性能和物理性能都有了极大提升，特别是在小游戏平台，三项重要数据都达到了80分以上，启动性能更是翻了一番，而启动性能的优劣是能直接影响到用户的去留问题，这意味着所有开发者可以用更快的时间获客，在买量成本不带攀升的游戏行业，这无疑是极具竞争力的一点。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210825/1629885711_182770.png" alt="Cocos 引擎 3D 技术再升级，打造赛博朋克极致渲染效果" referrerpolicy="no-referrer">
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210825/1629885710_950233.png" alt="Cocos 引擎 3D 技术再升级，打造赛博朋克极致渲染效果" referrerpolicy="no-referrer">
</p>
<p style="text-align:center;text-indent:2em;">
微信小游戏《快上车》升级后启动性能翻倍提升
</p>
<p style="text-indent:2em;">
同时，Cocos Creator 3.3 
在编辑器体验优化下了不少功夫，包括优化场景相机的漫游模式、增加了加速开关、场景灯光的开关、增加模型的最大最小坐标显示、增加 Transform Gizmo 
的吸附功能等等。
</p>
<p style="text-indent:2em;">
值得一提的是，Cocos 
引擎还支持跨平台的优势，同时极大增强了引擎的兼容性，既能发原生游戏，又能直接发小游戏端、网游、H5等，给了开发者更多的选择空间，能更专注于游戏内容的创作。
</p>
<p style="text-indent:2em;">
这意味着，通过 Cocos Creator，游戏开发者不仅能够做类似赛博朋克风格的中重度游戏，低算力 IoT 设备的交互 UI 
也都能够完成，同时既可以开发出独立APP，也可以被集成嵌入到其他APP里。
</p>
<p style="text-indent:2em;">
高效、灵活、免费开源等优势，吸引了大量开发者加入到 
Cocos，其中不乏市场爆款游戏，包括《剑与远征》、《动物餐厅》、《少年三国志》、《列王的纷争》、《保卫萝卜》等等。目前，Cocos 
在全球拥有150万的注册开发者，30万的月活跃开发者，遍布全球超过203个国家和地区，覆盖超过16亿玩家设备。
</p>
<p style="text-indent:2em;">
对于开发者来说，作为底层技术的游戏引擎越厉害，游戏开发者能够触及的“上限”也就越高。 Cocos 
的目标就是让游戏开发者不用再花过多的力气在技术层面，从而更加关注游戏设计与玩法创新，推动这个年轻的行业迈向更高的高度。
</p>          
</div>
            