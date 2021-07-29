
---
title: '小科普 _ 硬盘的HMB功能有啥用？'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/61017a718e9f090ede5866e9_1024.jpg'
author: ZAKER
comments: false
date: Wed, 28 Jul 2021 18:08:30 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/61017a718e9f090ede5866e9_1024.jpg'
---

<div>   
<p>咱们在买 SSD 的时候不难发现，有好多不知道干啥用的特性，还都是英文缩写，诸如 S.M.A.R.T、TRIM、LDPC ECC、DevSleep 等等，那么我们今天就来讲讲 HMB 是干什么的。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202107/61017a718e9f090ede5866e9_1024.jpg" data-height="540" data-width="1080" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/61017a718e9f090ede5866e9_1024.jpg" referrerpolicy="no-referrer"></div></div>HMB 全称 HostMemory Buffer 主机内存缓冲器，属于 NVM Express（NVMe）的基本特性之一。SSD 肯定需要 NAND 闪存颗粒，同时由 Controller 主控调度，<p></p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres1.myzaker.com/202107/61017a718e9f090ede5866ea_1024.jpg" data-height="739" data-width="1080" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/61017a718e9f090ede5866ea_1024.jpg" referrerpolicy="no-referrer"></div></div>为了提升随机读写性能，有些硬盘会设计一个外置硬件的 DRAM 高速缓存，用来缓冲数据和存储映射表（Map Table），主流比例是 1000:1，也就是 1GB 容量搭配 1MB 缓存，1TB 的盘搭配 1GB 的缓存。<p></p><p></p><div class="img_box" id="id_imagebox_2" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_2" data-original="http://zkres1.myzaker.com/202107/61017a718e9f090ede5866eb_1024.jpg" data-height="608" data-width="1080" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/61017a718e9f090ede5866eb_1024.jpg" referrerpolicy="no-referrer"></div></div>性能表现会比差不多规格的 DRAM-less 无缓存方案好一点。当然也有模拟 SLC Cache 缓存方案，空闲后二次转存、释放空间。有些低价的盘没装缓存、甚至主控本身就不支持外置缓存，这时候就要用到 HMB 技术了，<p></p><p></p><div class="img_box" id="id_imagebox_3" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_3" data-original="http://zkres1.myzaker.com/202107/61017a718e9f090ede5866ec_1024.jpg" data-height="790" data-width="1080" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/61017a718e9f090ede5866ec_1024.jpg" referrerpolicy="no-referrer"></div></div>它可以共享系统内存作为缓存，需要 NVMe1.2 版本、在 Win10 1703 版本之后就可以使用（和 SLC 缓存不冲突、可以同时存在）。其实和 NVIDIA 的 TC、AMD 的 HM 共享显存技术差不多，你显存不够用、爆了，就会调用内存。（响应延迟、带宽速度还是有差异的）（延迟：主控 SRAM<HMB<FTL）<p></p><p></p><div class="img_box" id="id_imagebox_4" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_4" data-original="http://zkres1.myzaker.com/202107/61017a718e9f090ede5866ed_1024.jpg" data-height="794" data-width="1080" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/61017a718e9f090ede5866ed_1024.jpg" referrerpolicy="no-referrer"></div></div>Windows 的 HMB 功能也有其局限性，它最多只能分配 64MB 共享缓存给 NVMe SSD，比例太低，所以效果肯定和独立外置 DRAM 缓存有差距，并且得走 PCIe 通道带来额外的延迟。<p></p><p>总的来说就是：有总比没有好，但也没好多少。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            