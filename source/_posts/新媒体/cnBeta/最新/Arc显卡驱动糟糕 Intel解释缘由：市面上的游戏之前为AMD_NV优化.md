
---
title: 'Arc显卡驱动糟糕 Intel解释缘由：市面上的游戏之前为AMD_NV优化'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://img1.mydrivers.com/img/20220806/76933bec772a44eca4568dbdf0c8821f.png'
author: cnBeta
comments: false
date: Sat, 06 Aug 2022 11:36:22 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220806/76933bec772a44eca4568dbdf0c8821f.png'
---

<div>   
Intel的Arc游戏显卡已经上市，虽然目前主要是A380这一款，但接下来还会有更高端的Arc 5、Arc 7系列上市，性能可以匹敌到RTX
3060/3070级别。当然，对Intel的Arc显卡，大家现在都知道硬件设计还是可圈可点，尤其是AV1编码很有优势，但是最大的麻烦还是驱动优化，A380在实际游戏中的表现被多家外媒形容为糟糕，表现不让人满意。<br>
  <p>对于这个问题，Intel高管Tom Petersen日前在采访中做了解释，<strong>他尤其提到了基于DX9、DX11这样的老游戏中表现更差，最新的DX12游戏中反而还不错，</strong>这是为何呢？</p><p>根据Tom Petersen的解释，<strong>DX9及DX11这样的游戏是不同的，需要<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>API和驱动来处理游戏中内存的管理</strong>，而这些游戏之前都是为<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>及NVIDIA的GPU架构优化的，毕竟之前Intel根本没有独显业务。</p><p>Intel的显卡架构跟NVIDIA的是非常不同的，因此在DX11及之前的旧游戏中就需要花大量时间和精力去调整优化，才能符合之前的游戏工作方式的预期。</p><p>至于DX12及Vulkan两种最新的API，规范就很不一样了，<strong>游戏内存管理是游戏引擎实现的</strong>，不会有DX9/DX11游戏的问题，Arc显卡的表现就好很多。</p><p><a href="https://img1.mydrivers.com/img/20220806/76933bec772a44eca4568dbdf0c8821f.png" target="_blank"><img alt="Arc显卡驱动糟糕 Intel解释：游戏之前为AMD/NV优化" h="400" src="https://img1.mydrivers.com/img/20220806/76933bec772a44eca4568dbdf0c8821f.png" w="600" referrerpolicy="no-referrer"></a></p>   
</div>
            