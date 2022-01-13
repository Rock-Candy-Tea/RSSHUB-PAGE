
---
title: 'Windows怎么看？2GB内存的树莓派4就能跑Ubuntu 22.04'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220113/s_de99be0a071f4923b39e6cdbba900277.jpg'
author: 快科技（原驱动之家）
comments: false
date: Thu, 13 Jan 2022 15:23:18 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220113/s_de99be0a071f4923b39e6cdbba900277.jpg'
---

<div>   
<p>Canonical今天宣布，即将在4月份发布的Ubuntu 22.04 LTS版本会进一步降低硬件配置需求，内存不再必须4GB或者更多，2GB就能完整运行。</p>
<p><strong><span style="color:#ff0000;">官方就展示了只有2GB内存的树莓派4，已经成功跑起来Ubuntu 22.04。</span></strong></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220113/de99be0a071f4923b39e6cdbba900277.jpg" target="_blank"><img alt="Ubuntu 22.04降低硬件需求：2GB内存的树莓派4就能跑" h="800" src="https://img1.mydrivers.com/img/20220113/s_de99be0a071f4923b39e6cdbba900277.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>这背后优化的秘密，就是<strong>Zswap</strong>。</p>
<p>我们知道，无论Windows、Linux，内存剩余容量不足的时候，系统就会通过虚拟内存(swap file)的方式，在硬盘上暂存内存数据，但硬盘的读写速度远低于内存，结果就是系统运行缓慢、卡顿。</p>
<p><strong>Zswap则可以视为一种压缩工具，在一个线程要被转移到分页文件的时候对其进行压缩，并检查新的小文件是可以留在内存中，还是需要转移到虚拟内存，而解压缩Zswap文件要比从虚拟内存中读取快得多，从而大大提升小内存设备的系统响应速度。</strong></p>
<p>Linux内核默认支持Zswap，默认关闭，开启命令为：</p>
<p><em>$ sudo sed -i -e 's/$/ zswap.enabled=1/' /boot/firmware/cmdline.txt</em></p>
<p>不过，Ubuntu 22.04会默认开启此功能，包括在所有的树莓派4设备上。</p>
<p>此外，Ubuntu 22.04还加入了另外两种小内存优化机制，一直名为<strong>z3fold</strong>的分配符，可以增加压缩对象的数量，二是<strong>lz4</strong>压缩算法，在压缩率和压缩速度之间取得更好的平衡。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20220113/be6fc04323294536a55f4ab7be56eb60.png" style="text-align: -webkit-center;" target="_blank"><img alt="Ubuntu 22.04降低硬件需求：2GB内存的树莓派4就能跑" h="385" src="https://img1.mydrivers.com/img/20220113/s_be6fc04323294536a55f4ab7be56eb60.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/ubuntu.htm"><i>#</i>Ubuntu</a><a href="https://news.mydrivers.com/tag/neicun.htm"><i>#</i>内存</a><a href="https://news.mydrivers.com/tag/shumeipai.htm"><i>#</i>树莓派</a><a href="https://news.mydrivers.com/tag/shumeipai4.htm"><i>#</i>树莓派4</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            