
---
title: 'Facebook开发新的THP收缩机制以避免Linux内存浪费'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0826/a6e2519a9a7a5eb.webp'
author: cnBeta
comments: false
date: Fri, 26 Aug 2022 09:25:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0826/a6e2519a9a7a5eb.webp'
---

<div>   
Meta/Facebook的工程师宣布了他们在THP Shrinker方面的工作，这是一种让Linux的透明页（THP）工作更有效率的方法，主要原理是通过移除未被充分利用的透明页来避免内存浪费。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0826/a6e2519a9a7a5eb.webp" title alt="image.webp" referrerpolicy="no-referrer"></p><p>THP对于某些工作负载来说，通过减少TLB缓存的未命中状态可以提高效率，但是2MB与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_110018%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">4K</a>b的页面大小如果没有得到有效利用，反而会导致大量的内存浪费。</p><p>Facebook的工程师在他们的一个平台上发现，由于THP没有得到充分利用，甚至让每台机器造成了大约2.7GB的内存浪费。</p><p>Facebook正在为Linux内核开发的THP收缩机制旨在解决这种浪费，与此同时仍然可以享受THP以提高CPU效率的优势，THP Shrinker将分割利用率最低的大内存页面。</p><p>THP Shrinker旨在避免浪费RAM，并尽可能让大内存页面透明并对外开放，使其无条件地启用，从而替代了基于madevise系统调用的选择。</p><p>Facebook的工程师们正在努力围绕这个THP Shrinker增加额外的调整，并可能与CPU/IO/内存压力事件挂钩。最终，工程师希望通过THP收缩器可以直接废除Linux的madvise THP模式，并切换到THP为所有应用程序启用。</p><p>关于这个有趣的内核开发的更多细节，请看lore.kernel.org：</p><p><a href="https://lore.kernel.org/lkml/cover.1661461643.git.alexlzhu@fb.com/" _src="https://lore.kernel.org/lkml/cover.1661461643.git.alexlzhu@fb.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="aecdc1d8cbdc809f98989f9a989f989a9d80c9c7da80cfc2cbd6c2d4c6dbeec8cc80cdc1c3">[email protected]</span>/</a><br></p><p>现在这个THP收缩器只是500多行的新内核代码。</p>   
</div>
            