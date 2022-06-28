
---
title: '微软免费杀软Defender被曝影响Intel处理器性能 跑分低了6%'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0628/2d828505e55cc88.png'
author: cnBeta
comments: false
date: Tue, 28 Jun 2022 07:20:52 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0628/2d828505e55cc88.png'
---

<div>   
近日，有开发者在调试软件的过程中发现，微软于Windows 10/11系统中自带的Windows Defender杀毒软件，会对Intel处理器的性能造成影响。以5GHz全核运行的i9-10850K为例，<strong>在开启Windows Defender后，Cinebench的跑分成绩降低了约1000分，损失了6%左右的性能。</strong><br>
 <p><a href="https://img1.mydrivers.com/img/20220628/cf330cdb8bc6432eae868005c5ca54ba.png" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0628/2d828505e55cc88.png"><img data-original="https://static.cnbetacdn.com/article/2022/0628/2d828505e55cc88.png" src="https://static.cnbetacdn.com/thumb/article/2022/0628/2d828505e55cc88.png" referrerpolicy="no-referrer"></a></p><p>据悉，<strong>在Win10/11上使用Intel酷睿第8代到第11代的用户都出现了类似的问题，而<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>处理器则没有受到影响。</strong></p><p>该Bug出现的原因，是由于<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Defender会随机调用Intel酷睿处理器包括三个固定功能计数器在内的，所有七个硬件性能计数器。</p><p>在调用计数器的同时，Windows Defender会将这些计数器设置为“mode 2”，<strong>导致其他程序无法正常使用，造成计数器控制寄存器在0x222和0x332之间不断变化，继而影响性能。</strong></p><p>目前，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>官方尚未公布该问题的处理方法，用户可以手动覆盖计数器配置，或启用第三方杀毒软件。</p>   
</div>
            