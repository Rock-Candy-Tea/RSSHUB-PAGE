
---
title: 'GPU延迟对比：AMD RDNA2完胜NVIDIA安培'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210419/s_4c0c9fdf346842faa4635da862fbf953.jpg'
author: 快科技（原驱动之家）
comments: false
date: Mon, 19 Apr 2021 19:16:22 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210419/s_4c0c9fdf346842faa4635da862fbf953.jpg'
---

<div>   
<p>CPU缓存与内存延迟测试，相信大家都有所耳闻，但是GPU同样的测试却几乎没人做过。</p>
<p>Chips And Cheese就做了一次特别的测试，对比考察了AMD、NVIDIA GPU架构的缓存、显存迟问题。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210419/4c0c9fdf346842faa4635da862fbf953.jpg" target="_blank"><img alt="GPU延迟对比：AMD RDNA2完胜NVIDIA安培" h="243" src="https://img1.mydrivers.com/img/20210419/s_4c0c9fdf346842faa4635da862fbf953.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>首先是<span style="color:#ff0000;"><strong>AMD RDNA2、NVIDIA Ampere两家最新架构的比拼，代表是RX 6900 XT、RTX 3090，前者在几乎所有阶段都完胜。</strong></span></p>
<p><strong>RNDA2架构创新性地加入了Infinity Cache无限缓存</strong>，提升带宽的同时，延迟也可圈可点，二级缓存命中率上只增加了大约20ns的延迟，明显低于Ampere。</p>
<p>更惊人的是，<strong>RDNA2显存延迟和Ampere几乎一模一样，但是别忘了，Ampere只有两个层级的缓存，RDNA2却有四个。</strong></p>
<p>Ampere的缓存架构更加传统，SM阵列私有一级缓存到二级缓存要增加超过100ns的延迟，RDNA2从零级缓存到二级缓存则只增加了约66ns。看起来，GA102核心面积过大，也直接增加了延迟。</p>
<p><strong>这正好可以解释AMD RDNA2架构在低分辨率下性能、能效更优秀，因为二级缓存、三级缓存延迟很低，更适合执行较小的负载。</strong>Ampere则相反，高负载下优势明显，比如说4K分辨率。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210419/65920f5c8a9144ad85b19f7e14faefdf.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="GPU延迟对比：AMD RDNA2完胜NVIDIA安培" h="298" src="https://img1.mydrivers.com/img/20210419/s_65920f5c8a9144ad85b19f7e14faefdf.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>说完了GPU之间的对比，那么GPU、CPU放在一起怎么样呢？这里以RX 6900 XT、Intel四代酷睿i7-4770为例来看看。</p>
<p>CPU的缓存自然不是一个级别的，所以这里Y轴用了线性数据，可以看到全程大大低于RDNA2，搭配DDR3-1600 CL9内存延迟只有63ns，RX 6900 XT、GDDR6的组合则有226ns，另外末级缓存平均延迟分别是53.42ns、123.2ns。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210419/4b044a15dbd348378d755ffd057cb968.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="GPU延迟对比：AMD RDNA2完胜NVIDIA安培" h="243" src="https://img1.mydrivers.com/img/20210419/s_4b044a15dbd348378d755ffd057cb968.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>再看看前几代的NVIDIA GPU，包括Maxwell架构的GTX 980 Ti、Pascal架构的GTX 1080、Turing架构的RTX 2060 Mobile。</p>
<p><strong>Maxwell、Pascal其实差不多，前者整体略高一些</strong>，可能是受制于芯片面积较大、核心频率较低。</p>
<p><strong>Turing则已经有了Ampere的样子</strong>，一级缓存延迟低得多，二级差不多，奇怪的是显存延迟在32MB之后偏高，原因未知。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210419/a1a9543e2a7d45c887de7258c1b71366.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="GPU延迟对比：AMD RDNA2完胜NVIDIA安培" h="283" src="https://img1.mydrivers.com/img/20210419/s_a1a9543e2a7d45c887de7258c1b71366.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>AMD考察了TeraScale架构的HD 5850/6950、GCN架构的HD 7970，再加上RX 6900 XT，<strong>很明显在逐代降低，而且是各级缓存都在同时进步。</strong></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210419/c6610e325fb54be49f061acaca713958.jpg" target="_blank"><img alt="GPU延迟对比：AMD RDNA2完胜NVIDIA安培" h="400" src="https://img1.mydrivers.com/img/20210419/s_c6610e325fb54be49f061acaca713958.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/amd.htm"><i>#</i>AMD</a><a href="https://news.mydrivers.com/tag/nvidia.htm"><i>#</i>NVIDIA</a><a href="https://news.mydrivers.com/tag/xianka.htm"><i>#</i>显卡</a><a href="https://news.mydrivers.com/tag/rdna.htm"><i>#</i>RDNA</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            