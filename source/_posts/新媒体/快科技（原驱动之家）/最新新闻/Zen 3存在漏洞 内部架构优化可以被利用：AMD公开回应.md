
---
title: 'Zen 3存在漏洞 内部架构优化可以被利用：AMD公开回应'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210406/s_e83e5a649baf48489405099e089ea499.png'
author: 快科技（原驱动之家）
comments: false
date: Tue, 06 Apr 2021 07:14:38 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210406/s_e83e5a649baf48489405099e089ea499.png'
---

<div>   
<p>之前有安全机构曾爆出Zen 3存在漏洞，内部架构优化可以被利用，对此AMD已经正式回应。</p>
<p><strong>AMD方面已经证实，Zen 3 CPU内部的微架构优化可以被利用，其方式类似于几代前困扰Intel CPU的Spectre漏洞。禁用该优化是可能的，但会带来性能上的损失，AMD认为除了最关键的处理器部署外，其他所有处理器都不值得这样做。</strong></p>
<p>在最近发布的一份名为《AMD预测存储转发的安全分析》的白皮书中，AMD描述了该漏洞的性质，并讨论了相关的后果。简单来说，预测性存储转发(PSF)的实现，由于其性质所致从而重新打开了之前受到Spectre v1、v2和v4威胁的攻击路线。</p>
<p>AMD将PSF描述为一种硬件优化，"旨在通过预测负载和存储之间的依赖关系来提高代码执行的性能"。与分支预测（一种启用了之前Spectre攻击的功能）一样，PSF进行预测，以使处理器更快地执行后续指令，然而当PSF做出错误的预测时，就会产生漏洞。</p>
<p><strong>AMD表示，不正确的预测可能是两种情况的结果。"首先，有可能存储/负载对有一段时间的依赖性，但后来不再有依赖性。" 这种情况是自然发生的，因为存储和负载在程序执行过程中会发生变化。第二种情况发生在 "如果PSF预测器结构中有一个别名"，而这个别名在不该使用的时候被使用了。这两种情况都可以被恶意代码触发，至少理论上是这样。</strong></p>
<p>Ryzen 5000和Epyc 7003系列处理器使用Zen 3架构，受此漏洞影响。</p>
<p>依靠软件沙盒来保证安全的程序是最容易受到PSF攻击的。使用硬件隔离的程序 "可能被认为是安全的"，不会受到PSF攻击，因为PSF投机不会跨地址空间发生。它也不会跨权限域发生。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210406/e83e5a649baf48489405099e089ea499.png" target="_blank"><img alt="Zen 3存在漏洞 内部架构优化可以被利用：AMD公开回应" h="331" src="https://img1.mydrivers.com/img/20210406/s_e83e5a649baf48489405099e089ea499.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/amd.htm"><i>#</i>AMD</a><a href="https://news.mydrivers.com/tag/intel.htm"><i>#</i>Intel</a></p>
<p class="url">
     
<span>责任编辑：雪花</span>
</p>
        
</div>
            