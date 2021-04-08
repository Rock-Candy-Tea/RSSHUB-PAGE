
---
title: '新发现：11代酷睿在两种内存Gear配置模式下性能有差别'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0408/f546a4add2f3bc9.jpg'
author: cnBeta
comments: false
date: Thu, 08 Apr 2021 11:22:29 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0408/f546a4add2f3bc9.jpg'
---

<div>   
11代酷睿桌面处理器已经正式发售，TPU针对内存部分进行了测试有了进一步发现，和大家分享下。先说理论部分，11代酷睿重新设计了内存控制器，定义为Gear（齿轮）工作模式，对应在BIOS中就是Gear 1和Gear 2两种设定。<br>
<p>其中Gear 1工作模式为 1:1，也就是CPU内存控制器和内存工作频率之比是1:1，内存控制器和内存同步工作，此模式下可以最大内存效能，内存延迟最低。</p><p>Gear 2模式就是2:1，内存控制器和内存异步工作，此模式通过减少一半的内存倍频的方式降低内存控制器的频率，好让内存不受内存控制器的限制更加容易超频。</p><p><strong>在TPU测试中选取的是酷睿i5-11400F，匹配DDR4-3733内存在Gear 2工况下，CPU整体跑分比Gear1工况平均快了1.5%。</strong></p><p>其中Cinebench R23多线程快了3.42%、MySQL快了6%、渲染和媒体测试快了1~3%。在更强调单线程的游戏测试中，Gear2才比Gear 1略慢。</p><p>另外值得注意的是，Gear 2模式下功耗也更低，Gear 1则要多出5~10瓦。</p><p><img src="https://static.cnbetacdn.com/article/2021/0408/f546a4add2f3bc9.jpg" referrerpolicy="no-referrer"></p><p><img src="https://static.cnbetacdn.com/article/2021/0408/02e0caab2b14de5.jpg" referrerpolicy="no-referrer"></p><p><img src="https://static.cnbetacdn.com/article/2021/0408/913c736eea93d49.jpg" referrerpolicy="no-referrer"></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0408/82c89399fbb9c8a.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0408/82c89399fbb9c8a.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0408/82c89399fbb9c8a.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            