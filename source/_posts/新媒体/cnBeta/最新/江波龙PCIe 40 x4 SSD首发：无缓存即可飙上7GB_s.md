
---
title: '江波龙PCIe 4.0 x4 SSD首发：无缓存即可飙上7GB_s'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0328/557720aab7c18de.jpg'
author: cnBeta
comments: false
date: Mon, 28 Mar 2022 06:04:12 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0328/557720aab7c18de.jpg'
---

<div>   
这两年，SSD陆续从PCIe 3.0过渡到PCIe 4.0时代，<strong>江波龙宣布，旗下团队FORESEE成功研发出首款PCIe 4.0 SSD—— XP2100。</strong>FORESEE XP2100 SSD采用<strong>DRAM-less无缓存架构、3D TLC闪存</strong>，M.2 2280标准形态，无需散热片，容量可选256GB、512GB、1TB，<strong>支持市场主流的NVMe 1.4协议，已经通过UNH-IOL认证，Intel Modern Standby、Google、AMD等其他认证也正在进行中。</strong><br>
 <p><a href="https://img1.mydrivers.com/img/20220328/b1a839862d23491bb358b3731e8ebdc5.jpg" style="text-align: -webkit-center;" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0328/557720aab7c18de.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0328/557720aab7c18de.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0328/557720aab7c18de.jpg" referrerpolicy="no-referrer"></a></p><p><a href="https://img1.mydrivers.com/img/20220328/fa9e74606aa9492ba9300348b2bcf7c1.jpg" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0328/a4dc0090e4e33f7.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0328/a4dc0090e4e33f7.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0328/a4dc0090e4e33f7.jpg" referrerpolicy="no-referrer"></a></p><p>性能方面，<strong>顺序读取可达5.3GB/s，顺序写入也有4.9GB/s，随机读写速度达到800K IOPS、600K IOPS。</strong></p><p>可靠性方面，平均故障间隔时间150万小时，提供3年质保，但写入寿命暂未公布。</p><p>江波龙还透露，会持续提升<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a>产品质量和服务质量，<strong>XP2100将会搭配2400MT/s NAND闪存，顺序读取性能可进一步达到顶级的7GB/s。</strong></p><p><a href="https://img1.mydrivers.com/img/20220328/1e8618b7e5e44ed08ad8c3e566d73e9e.jpg" style="text-align: -webkit-center;" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0328/cbcf54aabdd82e0.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0328/cbcf54aabdd82e0.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0328/cbcf54aabdd82e0.jpg" referrerpolicy="no-referrer"></a></p><p>PCIe 4.0大家都很熟悉了，NVMe 1.4则往往容易被忽略，江波龙也顺带做了一番小科普。</p><p>NVMe 1.4版本早在2019年6月就发布了，其中最重要的新功能就是<strong>I/O Determinism，包含NVMe Set、PLM两个部分</strong>，可为商用PC、服务器、数据中心等专业需求提供技术支持。</p><p>其中，<strong>NVMe Set改良了写入时的分工机制，等于“大硬盘分成多个小硬盘”，划清界限</strong>，互不打扰，防止IO延迟产生性能波动。</p><p>比如一块4TB SSD，以往的NVMe 1.3协议下，就算支持4通道，都只会当作单一的4TB空间，任意写入，容易出现通道之间的挤塞，自然影响性能。</p><p><strong>NVMe 1.4则会把4TB分割成4个1TB的空间，交给每一个通道独立控制，就能有效缩减延迟。</strong></p><p><strong>PLM全称Predictable Latency Mode(可预测延迟模式)，优势是提供了内存级别的速度和低延迟，哪怕电源断电，数据也能保留，从而提高系统QoS。</strong></p><p>PLM会把系统划分为DTWIN（Deterministic Window）、 NDWIN（Non-Deterministic Window），其中在DTWIN内SSD为读写指令提供Deterministic latency以提高系统的QoS，而在NDWIN下，SSD就不需要提供Deterministic latency，以便完成SSD内部的GC垃圾回收或TRIM整理等操作。</p><p><a href="https://img1.mydrivers.com/img/20220328/748202bff86a4769b39973a9cc779842.jpg" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0328/fb71b319993e647.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0328/fb71b319993e647.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0328/fb71b319993e647.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            