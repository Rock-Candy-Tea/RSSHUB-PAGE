
---
title: '英特尔Arc Alchemist GPU将在Linux平台上获得Resizable BAR支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0131/b329771542f9ef6.png'
author: cnBeta
comments: false
date: Sun, 30 Jan 2022 18:09:34 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0131/b329771542f9ef6.png'
---

<div>   
早在2020年，随着AMD和NVIDIA在其显卡上实现对该功能的支持，Resizable BAR成为玩家当中的热门话题，但现在，英特尔也已确认在其即将推出的Arc Alchemist GPU上增加对该技术的支持。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0131/b329771542f9ef6.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0131/b329771542f9ef6.png" title alt="Intel-ARC-Alchemist-Flagship-GPU-Graphics-Card.png" referrerpolicy="no-referrer"></a></p><p>在Phoronix的一份报告中，最新的Linux图形内核在补丁中提到了"Resizable BAR"或ReBAR支持。最新的补丁包括对Linux平台上<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>内核图形驱动的small <br> BAR恢复支持。</p><p><strong>以下是该补丁的内容：</strong></p><blockquote><p>从DG2开始，我们将为设备本地内存提供可调整大小的BAR支持，但在某些情况下，最终的BAR大小仍可能小于本地内存的总大小。在这种情况下，只有部分本地内存可以被CPU访问，而其余部分只能通过GPU访问。这个系列增加了所需的基本功能，以确保整个本地内存范围是可用的。</p><p>考虑到该补丁是为Linux 5.17发出的，我们有可能看到Resizable BAR支持最早在Linux 5.18被添加。因此，如果用户不想在Linux生态系统中使用英特尔的GPU的ReBAR，他们将不得不升级到最新的Linux和MESA版本。英特尔已经在其台式机平台上提供了Resizable BAR支持，从300系列开始，考虑到其他GPU制造商在台式机和笔记本电脑上都提供了这项技术，英特尔很可能也会在其Arc Alchemist GPU系列上遵循同样的路线。</p></blockquote><p>ReBAR本质上定义了可以映射多少独立的GPU内存空间，今天的PC通常被限制在256MB的映射内存。有了BAR，系统可以访问所有的GPU内存，消除瓶颈以实现更快的性能。到目前为止，BAR显示的性能数字参差不齐，在一些游戏中有所提高，而在另一些游戏中没有性能优势。还有一些情况是，启用BAR后，系统产生的性能较低，但这只是一小部分，所以启用它并不是一个坏主意，很高兴看到英特尔也在努力使这种功能出现在开源平台。</p><p><a href="https://static.cnbetacdn.com/article/2022/0131/ceb5f5d91ef9da3.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0131/ceb5f5d91ef9da3.jpg" title alt="Intel-Arc-Alchemist-GPUs-Resizable-BAR.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            