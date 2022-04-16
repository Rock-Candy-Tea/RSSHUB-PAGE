
---
title: '索尼工程师帮助改进 exFAT Linux 驱动，性能提升达 73%'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202204/625959448e9f095b193be0b4_1024.jpg'
author: ZAKER
comments: false
date: Fri, 15 Apr 2022 07:39:47 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202204/625959448e9f095b193be0b4_1024.jpg'
---

<div>   
<p>IT 之家 4 月 15 日消息，exFAT（Extended File Allocation Table File System 即扩展文件分配表）是微软在 Windows Embeded 5.0 以上的版本中引入的一种适合于闪存的文件系统，常见于 SD 卡、U 盘等等。</p><p>IT 之家了解到，Linux 内核的 exFAT 文件系统驱动随着新功能、bug 修复和性能持续改进而日益完善起来。</p><p>值得一提的是，最新的 Linux exFAT 驱动程序是由一位索尼工程师带来的改进，他帮助所有人大大提高了 exFAT 性能，这一补丁应该会在今年夏天出现在 Linux 5.19 内核中。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202204/625959448e9f095b193be0b4_1024.jpg" data-height="597" data-width="578" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202204/625959448e9f095b193be0b4_1024.jpg" referrerpolicy="no-referrer"></div></div>据介绍，当 exFAT 文件系统以 "dirsync" 模式进行挂载时，这一改进大幅减少了集群归零时的块请求处理时间，大约带来了 73% 的性能提高（索尼工程师 Mo Yuezhang 在 Arm 测试平台上进行了测试）。<p></p><p>在 256kb 集群大小的情况下，创建 100 个文件夹的时间从 11 分 22 秒直接下降到 1 分 39 秒。而对于 64KB 的集群大小而言，创建 1000 个目录的时间也从 3 分 34 秒降到了 56 秒。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            