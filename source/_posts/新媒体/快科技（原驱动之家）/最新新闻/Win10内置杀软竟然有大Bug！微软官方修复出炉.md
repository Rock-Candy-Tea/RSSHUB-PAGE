
---
title: 'Win10内置杀软竟然有大Bug！微软官方修复出炉'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210507/Sdd2b1f48-e52e-4a17-b469-5550d1351765.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 07 May 2021 00:30:55 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210507/Sdd2b1f48-e52e-4a17-b469-5550d1351765.jpg'
---

<div>   
<p>根据用户和媒体的测试报道，Win10内置的杀毒软件Windows Defender被发现存在一个大Bug：Windows Defender会持续产生数以千计的文件，填入Win10的系统盘，这就导致大量硬盘空间被占用。</p>
<p>该问题被用户广泛上报，Windows Defender被认为是该故障的主因。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210507/dd2b1f48-e52e-4a17-b469-5550d1351765.jpg" target="_blank"><img alt="Win10内置杀软竟然有大Bug！微软官方修复出炉" h="315" src="https://img1.mydrivers.com/img/20210507/Sdd2b1f48-e52e-4a17-b469-5550d1351765.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>据了解，Windows Defender目前以装载所有版本的Win10当中，并通过Windows Update进行维护更新。</p>
<p>经过四月最后一周的某次更新后，用户察觉Windows Defender会产生大量文件，这些文件和操作系统的安装位置处于同一分区，占用了系统驱动器空间。</p>
<p>受影响的用户在微软社区和Reddit社区中成，Windows Defender的历史文件目录（C:\ProgramData\Microsoft\Windows Defender\Scans\History\Store）当中，充满了这些文件。这些文件本身并不大，也不会有什么损害，但海量的文件会占用巨大的空间。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210507/bea9aff0-157d-4bf1-ac03-4b7fa7600c94.jpg" target="_blank"><img alt="Win10内置杀软竟然有大Bug！微软官方修复出炉" h="426" src="https://img1.mydrivers.com/img/20210507/Sbea9aff0-157d-4bf1-ac03-4b7fa7600c94.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>这个Bug也会影响Windows Server系统，某些用户报告称，Windows Defender产生了多达1800万个文件。</p>
<p>一名用户在Reddit中反馈，有三台服务器受到了影响。在某天晚上，突然硬盘空间被极速耗尽，某一个服务器中出现了1800万个文件，另一个服务器则有1300万个。</p>
<p>经过数小时后，才将这些文件定位出来，以便于删除处理。由于磁盘空间的分配机制，这些文件会在硬盘上占据50~60GB空间，毫无疑问微软搞砸了某些东西。</p>
<p>那么问题来了，要如何得知Windows Defender有没有生成这些莫名其妙的文件？</p>
<p>最简单的方法，就是通过资源管理器检查。</p>
<p>首先，在资源管理器的设置中，打开隐藏文件的可见。</p>
<p>其次，在地址栏中，输入“C:\ProgramData\Microsoft\”，并进入该目录。</p>
<p>之后，进入“Windows Defender”目录，如果需要管理员权限的话就授权，然后在该目录的“Scans\History\Store”中，就可以看到有没有零碎的小文件了。</p>
<p>如果你遇到了这个Bug，那么可以观察到大量少于1M的文件，这些文件可以安全删除，没有别的害处。</p>
<p>对于这个Bug，目前微软也已经给出了修复方案。</p>
<p><span style="color:#ff0000;"><strong>在Window Defender的1.1.18100.6新版中，该问题已经被修复。</strong></span></p>
<p>如果你想要获得相关更新，在Win10设置的系统更新中，检查更新即可。</p>
<p>如果要确认是否修复了相关问题，那么开启Windows Defender后，在安全引擎的“关于”页面中查看版本号，如果已经是1.1.18100.6新版，即不存在该Bug。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210507/222dbd4a1b6b406d8134fc19d615815f.jpg" target="_blank"><img alt="Win10内置杀软竟然有大Bug！微软官方修复出炉" h="337" src="https://img1.mydrivers.com/img/20210507/s_222dbd4a1b6b406d8134fc19d615815f.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/weiruan.htm"><i>#</i>微软</a><a href="https://news.mydrivers.com/tag/windows_10.htm"><i>#</i>Windows 10</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.pconline.com.cn/win10/1418/14183824.html">太平洋电脑网</a></span>
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            