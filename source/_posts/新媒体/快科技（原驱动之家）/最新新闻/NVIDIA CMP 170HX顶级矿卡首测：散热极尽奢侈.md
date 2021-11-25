
---
title: 'NVIDIA CMP 170HX顶级矿卡首测：散热极尽奢侈'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211125/s_0c722bcf466e4b819facf0bdcf9be5ea.jpg'
author: 快科技（原驱动之家）
comments: false
date: Thu, 25 Nov 2021 13:45:42 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211125/s_0c722bcf466e4b819facf0bdcf9be5ea.jpg'
---

<div>   
<p>NVIDIA对于挖矿真是上心！不但推出了专门的CMP HX系列矿卡，甚至将安培家族用于加速计算卡的顶级大核心A100也拿了过来，这就是CMP 170HX，据说还有个更高端的CMP 220HX。</p>
<p><a class="f14_link" href="https://news.mydrivers.com/1/780/780634.htm" target="_blank">之前我们曾经见过CMP 170HX的样品</a>，现在有国外博主也拿到了一块，并进行了拆解、简单测试。这也是NVIDIA亲自出品的第一块矿卡。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211125/0c722bcf466e4b819facf0bdcf9be5ea.jpg" target="_blank"><img alt="NVIDIA CMP 170HX顶级矿卡首测：散热极尽奢侈" h="300" src="https://img1.mydrivers.com/img/20211125/s_0c722bcf466e4b819facf0bdcf9be5ea.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>该卡的造型和A100 PCIe加速计算卡基本一致，<strong>无风扇被动散热</strong>(类似服务器方案依赖整机风扇)，双插槽厚度，自然没有视频接口。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211125/8e61132e0521400b9c31d4576b363a5d.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="NVIDIA CMP 170HX顶级矿卡首测：散热极尽奢侈" h="340" src="https://img1.mydrivers.com/img/20211125/s_8e61132e0521400b9c31d4576b363a5d.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>外壳是铝材质</strong>，没有任何标记之类的，<strong>内部则是一大块铜质散热片</strong>，覆盖整个PCB电路板。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211125/11533c91fe254bac82e359495531a391.jpg" target="_blank"><img alt="NVIDIA CMP 170HX顶级矿卡首测：散热极尽奢侈" h="363" src="https://img1.mydrivers.com/img/20211125/s_11533c91fe254bac82e359495531a391.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211125/58701fcc10144de68183c27f6664f777.jpg" target="_blank"><img alt="NVIDIA CMP 170HX顶级矿卡首测：散热极尽奢侈" h="373" src="https://img1.mydrivers.com/img/20211125/s_58701fcc10144de68183c27f6664f777.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>PCB板造型也很别致，尾部一个弧形缺口，而辅助供电不是常见的PCIe 6/8针，是<strong>常见于主板上给CPU辅助供电的PES 8针</strong>，因此需要转接。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211125/82a9bd8e9eff44f1a80183494523b461.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="NVIDIA CMP 170HX顶级矿卡首测：散热极尽奢侈" h="309" src="https://img1.mydrivers.com/img/20211125/s_82a9bd8e9eff44f1a80183494523b461.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>电路板布局紧凑，用料相当高级，<strong>而GPU芯片本身和周边基板全部覆盖上了厚实的散热顶盖。</strong></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211125/66dcdd57f0eb40cf82a62bb01bdb76bc.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="NVIDIA CMP 170HX顶级矿卡首测：散热极尽奢侈" h="386" src="https://img1.mydrivers.com/img/20211125/s_66dcdd57f0eb40cf82a62bb01bdb76bc.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>内核代号为GA100-105F。</strong></p>
<p>GPU-Z可以识别出大部分信息，比如<strong><span style="color:#ff0000;">CMP 170HX型号、4480个流处理器、140个纹理单元、128个ROP光栅单元、SK海力士8GB HBM2显存、1140-1410MHz核心频率，等等。</span></strong></p>
<p>相比之下，A100加速卡有6912个流处理器，这里屏蔽了超过三分之一，显存原本也有80/40GB之多，现在只剩下8GB，当然也足够了，毕竟以太坊DAG文件还不到5GB。</p>
<p><strong><span style="color:#ff0000;">挖矿性能实测以太坊在165MH/s左右，但不能调节频率，功耗虽然可以在200-250W之间变动，但完全不影响挖矿算力。</span></strong></p>
<p><strong>DirectX、OpenGL、Vulkan、CUDA等图形相关技术统统被屏蔽。</strong>虽然GPU-Z识别显示支持CUDA，但根本没法用，甚至无法使用CUDA内核渲染Blender。</p>
<p>这也就注定了，它除了挖矿，啥都不能干。</p>
<p>但就是这么个家伙，<strong><span style="color:#ff0000;">据说要5000美元！</span></strong></p>
<p style="text-align: center"><img alt="NVIDIA CMP 170HX顶级矿卡首测：散热极尽奢侈" h="450" src="https://img1.mydrivers.com/img/20211125/da0385fe-deb9-45dc-9199-614e17f02a74.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p style="text-align: center;"><img alt="NVIDIA CMP 170HX顶级矿卡首测：散热极尽奢侈" h="800" src="https://img1.mydrivers.com/img/20211125/22c430ef-0792-4f0f-b8e9-b2fe885803c8.jpg" style="text-align: center; border: 1px solid black;" w="600" referrerpolicy="no-referrer"></p>
<p style="text-align: center"><img alt="NVIDIA CMP 170HX顶级矿卡首测：散热极尽奢侈" h="800" src="https://img1.mydrivers.com/img/20211125/612cc66b-f5e9-43a7-bf66-e8a388c45f94.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/nvidia.htm"><i>#</i>NVIDIA</a><a href="https://news.mydrivers.com/tag/wakuang.htm"><i>#</i>挖矿</a><a href="https://news.mydrivers.com/tag/kuangka.htm"><i>#</i>矿卡</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            