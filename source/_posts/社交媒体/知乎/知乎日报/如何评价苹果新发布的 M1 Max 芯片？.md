
---
title: '如何评价苹果新发布的 M1 Max 芯片？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pica.zhimg.com/v2-81a3d915727b978183a7149c2cfd9953_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2021-10-21 10:09:00
thumbnail: 'https://pica.zhimg.com/v2-81a3d915727b978183a7149c2cfd9953_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">
如何评价Apple新发布的M1 Max芯片？

<div class="answer">

<strong>
<img class="avatar" src="https://pica.zhimg.com/v2-81a3d915727b978183a7149c2cfd9953_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">YY硕，</span><span class="bio">机器人工程师</span>
<a href="https://www.zhihu.com/question/493188474/answer/2177950884" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>M1 系列芯片这个性能完全不是单单为了笔记本电脑而设计的。</p>
<p>苹果的思路很清晰，开发这样的性能怪兽需要天价的投入，需要首先在消费级产品上应用来收回开发成本。但是芯片开发完成以后，苹果就可以把这一系列天生基于嵌入式系统的芯片做定制化的嵌入式操作系统和 SDK，然后一波操作给包括但不限于以下的嵌入式应用场景带来革命：</p>
<ol>
<li>无人驾驶、无人机和机器人。这个领域吵吵着搞异构计算好多年了，没有什么大玩家真的能做出来把车体实时控制、海量传感器数据处理、流畅用户交互都把握得很好的异构芯片。M1 Max 400Gbps 内存带宽吞吐，打游戏并用不上，但是同时处理起 6 路激光雷达和 6 路高清相机传感器给无人驾驶系统和机器人提供周围感知这就随随便便体现出性能优势了。隔壁英伟达和地平线应该正在瑟瑟发抖。M1 新的两个系列刚出，并没有实用的案例，但是我在华盛顿大学搞足式机器人的朋友说一个基于 M1 芯片的 Mac Mini 直接怼上机器人，全套每秒 500 次的实时控制和非线性优化解算跑起来完全没有问题，最妖的是这些算法是跑在 Mac 里的 Linux 虚拟机上，众所周知虚拟机会拖慢很多性能，但就算如此一台 M1 跑整台四足机器人的控制器都没有问题。M1 尚且如此，M1 Max 要是装上机器人说不定能实时跑波士顿动力人形机器人 Atlas 上的控制器（目前强如波士顿动力有一部分算法也是离线跑的）。</li>
<li>虚拟现实。VR/AR 设备多年来最大的问题就是没办法在小空间里怼进足够的计算量处理高清视频流和空间姿态解算。一台让人不产生眩晕感的眼镜，必须能够以 120FPS 以上刷新 1080P 的图像，同时提供延迟小于 10ms 的空间姿态解算，所以需要极快地收到图像、用 GPU 处理图像、用 CPU 处理图像和其他传感器获得空间姿态、然后再用 GPU 渲染图像。因此在 GPU 和 CPU 之间来回花式倒腾图像是不行的，GPU 和 CPU 共用内存正是为这个事情而生。据我所知 Apple 内部有好几个做虚拟现实的组，目测基于 M1 或者其他变种芯片的眼镜产品已经在路上了。</li>
<li>任何需要低能耗的嵌入式系统，如投影仪、电视、商场广告牌、特种监控设备等等。Intel 多年来把芯片板级的接口和手册开放下游系统集成公司，无数的公司通过把 Intel 芯片魔改到形态各异的板子来支持广大的制造业、物流业等一切需要嵌入式显示和计算的商业场景。我们不知道 Apple 会在多大程度上开放 M1 的板级生态，但是一旦开放的话这些行业必然是洪水滔天人人投入 Apple 怀抱，毕竟低功耗对普通用户来说就是电脑热一点而已，但是对于行业客户而言，低功耗代表着嵌入式系统在供电方面的元器件选型、板子散热、电源稳定性都可以低一档，板子成本大幅降低，用户使用的能耗成本更是降低四五倍。</li>
</ol>
<p>总地来说，M1 如果也开始把软件生态做起来能够支持整个嵌入式行业的话，对世界的贡献不亚于 iPhone 的诞生。</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-9fd363f8cd3992eb709f6985f90693ce_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/493188474">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            