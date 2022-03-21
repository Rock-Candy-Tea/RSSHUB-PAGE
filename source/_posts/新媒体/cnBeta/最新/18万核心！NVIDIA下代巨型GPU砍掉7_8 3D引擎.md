
---
title: '1.8万核心！NVIDIA下代巨型GPU砍掉7_8 3D引擎'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/03/a0f7e908afc401c.jpg'
author: cnBeta
comments: false
date: Mon, 21 Mar 2022 12:56:06 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/03/a0f7e908afc401c.jpg'
---

<div>   
明天，NVIDIA GTC 2022图形大会即将召开，代号“Hopper”的下一代计算架构也有望首次公开。著名芯片专家Locuza今天曝出猛料，贴出了<strong>Hopper架构大核心GH100的架构图，确认共有8组GPC(图形处理集群)，每组GPC包含9组TPC(纹理处理集群)，而每组TPC包括2组SM(流失多处理器单元)。</strong><br>
 <p>假设CUDA核心的12基本组合方式不变，每组SM还是128个，那就是<strong>总计144组SM、18432个CUDA核心</strong>，与此前传闻相符。</p><p></p><p><a href="https://static.cnbetacdn.com/article/2022/03/a0f7e908afc401c.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/03/a0f7e908afc401c.jpg" referrerpolicy="no-referrer"></a></p><p><br></p><p>不过，GH100核心是专门面向高性能计算、人工智能等领域的，不需要强大的图形功能，因此这一次，<strong>8组GPC里边其实只有一组自带3D引擎。</strong></p><p>至于其他七组GPC，是原生未集成3D引擎，还是硬件屏蔽了，暂时不得而知(可能是后者)。</p><p>当然，NVIDIA完全可以彻底取消3D图形功能，毕竟加速计算卡都不带视频输出接口。</p><p><a href="https://img1.mydrivers.com/img/20220321/b62c2eabb3e14623a6b5b04ccd614d4c.jpg" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0321/cca08b5746250be.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0321/cca08b5746250be.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0321/cca08b5746250be.jpg" referrerpolicy="no-referrer"></a></p><p>另外，<strong>GH100核心将集成48MB二级缓存，同时有12个512-bit显存控制器，每个控制器对应2MB缓存。</strong></p><p>对比上代Ampere架构计算核心GA100 40MB增加不算多，不过对比<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Instinct MI250系列的16MB多出来整整两倍。</p><p>只是，传闻称，下一代Ada Lovelace游戏卡架构的大核心AD102，将有多达96MB二级缓存，两倍于GH100。</p><p>从架构图看，<strong>GH100还是单一设计的大核心(台积电5nm工艺)，同时还可能会有一个GH202，MCM方式双芯堆叠，但是按惯例，它们俩都不一定会开启所有CUDA核心，一般来说会屏蔽15-20％，以提高良品率。</strong></p><p><a href="https://img1.mydrivers.com/img/20220321/05857ef3c81f4513910d5d4d6bb2b966.png" style="text-align: -webkit-center;" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/0321/418d4c53f8b995c.png" referrerpolicy="no-referrer"></a></p>   
</div>
            