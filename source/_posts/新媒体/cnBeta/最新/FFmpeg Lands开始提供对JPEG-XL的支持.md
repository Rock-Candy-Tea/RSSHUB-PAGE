
---
title: 'FFmpeg Lands开始提供对JPEG-XL的支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0424/6c92d64fe7bb55a.png'
author: cnBeta
comments: false
date: Sun, 24 Apr 2022 10:44:25 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0424/6c92d64fe7bb55a.png'
---

<div>   
<strong>上周六，广泛被使用的FFmpeg合并了对JPEG-XL图像编解码器的支持。</strong>FFmpeg正在利用libjxl库来处理JPEG-XL内容，并支持图像编码和解码。这项工作包括将JPEG-XL图像作为流进行多路复用/解复用，以及围绕这个编解码器的其他FFmpeg支持工作。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0424/6c92d64fe7bb55a.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0424/6c92d64fe7bb55a.png" title alt="1024px-JPEG_XL_logo.svg.png" referrerpolicy="no-referrer"></a></p><p>JPEG XL 基于Google 的 PIK 格式和Cloudinary的 FUIF 格式（该格式基于FLIF），它的默认设置能在实现接近无损的视觉效果的同时，提供良好的压缩效果，这一项目希望成为其他光栅有损和无损图像格式的通用替代品。</p><p>JPEG-XL比特流在2021年年底定稿，并且我们已经可以开始在网络上看到各种开源和闭源应用的采用。JPEG-XL的目标是免版税的，尽管今年早些时候，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>被授予了一项围绕"rANS"（范围不对称数字系统）数据压缩的专利，因为这被JPEG-XL所使用而引起了一些关注。</p><p>我们将在接下来的日子里看到JPEG-XL的长期采用情况。</p><p><strong>了解更多：</strong></p><p><a href="https://github.com/FFmpeg/FFmpeg/search?q=jpeg-xl&type=commits" _src="https://github.com/FFmpeg/FFmpeg/search?q=jpeg-xl&type=commits" target="_blank">https://github.com/FFmpeg/FFmpeg/search?q=jpeg-xl&type=commits</a><br></p><p><img src="https://static.cnbetacdn.com/article/2022/0424/12e8e0d0b434f3e.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p>   
</div>
            