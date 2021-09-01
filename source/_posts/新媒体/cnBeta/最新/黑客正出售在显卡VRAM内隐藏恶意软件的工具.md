
---
title: '黑客正出售在显卡VRAM内隐藏恶意软件的工具'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0901/3314a1f0389f931.webp'
author: cnBeta
comments: false
date: Wed, 01 Sep 2021 11:59:11 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0901/3314a1f0389f931.webp'
---

<div>   
想在电脑杀毒软件检查系统RAM时将恶意代码隐藏起来？很简单，只需将其隐藏在显卡的VRAM中。最近有人在网上出售一种能够实现这种功能的概念验证工具，这对Windows用户来说可能是个坏消息。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0901/3314a1f0389f931.webp" title alt="2021-02-02-image-j.webp" referrerpolicy="no-referrer"></p><p>Bleeping Computer写道，最近有人在一个黑客论坛上出售一种PoC。他们没有透露关于该工具的太多细节，但其工作原理是在GPU内存缓冲区分配地址空间来存储恶意代码，并从那里执行它。</p><p>卖家补充说，该代码只在支持OpenCL 2.0或更高版本的<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>电脑上工作。他们证实它在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>的Radeon RX 5700和Nvidia的GeForce GTX 740M和GTX 1650显卡上可以工作。它也适用于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的UHD 620/630集成图形。</p><p>8月8日，论坛上出现了宣传该工具的帖子。大约两周后（8月25日），卖家透露，他们已经将PoC卖给了别人。8月29日，研究小组Vx-underground在Twitter上说，恶意代码使GPU在其内存空间中执行二进制。它将"很快"展示这一技术。</p><p>我们过去曾见过基于GPU的恶意软件，例如你可以在GitHub上找到开源的Jellyfish攻击方式，这是一个基于Linux的GPU rootkit PoC，利用了OpenCL的LD_PRELOAD技术。JellyFish背后的研究人员还发布了基于GPU的键盘记录器和基于GPU的Windows远程访问木马的PoC。</p><p><img src="https://static.cnbetacdn.com/article/2021/0901/519e957440698d5.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>这种方法的技术核心是通过DMA[直接内存访问]直接从GPU监控系统的键盘缓冲区，除了页表之外，在内核的代码和数据结构中没有任何挂钩或修改。对攻击代码原型实现的评估表明，基于GPU的键盘记录器可以有效地记录所有的用户按键，将它们存储在GPU的内存空间中，甚至可以就地分析记录的数据，而运行时间的开销甚至可以忽略不计。</p><p>早在2011年，安全人员就发现了一种新的恶意软件威胁，利用GPU来挖掘比特币。但是最近PoC的卖家说，他们的方法与JellyFish不同，因为它不依赖代码映射回用户空间。</p>   
</div>
            