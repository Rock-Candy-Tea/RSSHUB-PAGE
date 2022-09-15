
---
title: '英特尔详细介绍了FFmpeg中的oneVPL CPU和GPU加速特性'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0915/81ee7be7daf5a2c.png'
author: cnBeta
comments: false
date: Thu, 15 Sep 2022 09:08:09 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0915/81ee7be7daf5a2c.png'
---

<div>   
英特尔介绍了该公司包含在FFmpeg
oneAPI工具包中的视频处理和加速库的oneVPL支持。oneVPL视频处理库有助于在处理器和公司内部的GPU加速中调用最新的12代酷睿Alder
Lake和Intel Xe硬件。加速的重点是英特尔Arc
Graphics和DG2硬件，指导媒体SDK支持前几代显卡，能够适应其他潜在的CPU和GPU后端。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0915/81ee7be7daf5a2c.png" title alt="Screenshot-2022-09-13-112729.png" referrerpolicy="no-referrer"></p><p>FFmpeg中新的oneVPL支持将与FFmpeg中的VA-API或视频加速API支持协同工作，并在英特尔GPU中提供支持。</p><p>作为英特尔对用于媒体处理的开源行业标准FFmpeg和GStreamer的长期贡献的一部分，英特尔为FFmpeg增加了对oneAPI视频处理库（oneVPL）的支持。这是一个重要的变化，因为oneVPL是英特尔对英特尔媒体SDK（Media SDK）的进化。今后，访问新的GPU媒体功能的主要方式是通过oneVPL（官方不再向Media SDK添加功能），因此公司鼓励所有英特尔GPU媒体用户切换到oneVPL，以便在硬件功能出现后尽快利用。</p><p>英特尔已经将FFmpeg的oneVPL集成放在一个"Cartwheel"存储库中，该公司在完全上传到上游之前将所有补丁或错误修复收集并组织队列。</p><p>一些补丁涉及VA-API、QSV和更多的部分。该公司仍有许多更新在存储库中，目前正在开发中，并等待在oneVPL集成中全面实施。这些更新将影响英特尔Arc Alchemist和DG2 GPU，但目前还没有任何集成上传到主队列的具体日期。</p><p>读者可以在英特尔的官方网页上查看最新的开发者文章，解释该公司如何在FFmpeg中使用oneVPL，在该公司的GPU上获得令人满意的流媒体性能。</p><p><a href="https://www.intel.com/content/www/us/en/developer/articles/technical/onevpl-in-ffmpeg-for-great-streaming-on-intel-gpus.html" _src="https://www.intel.com/content/www/us/en/developer/articles/technical/onevpl-in-ffmpeg-for-great-streaming-on-intel-gpus.html" target="_blank">https://www.intel.com/content/www/us/en/developer/articles/technical/onevpl-in-ffmpeg-for-great-streaming-on-intel-gpus.html</a><br></p><p>该报告还介绍了在FFmpeg中为英特尔GPU实现最新的oneVPL。</p>   
</div>
            