
---
title: 'FFmpeg合并基于AV1图像格式的AVIF多路复用器'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0513/1e4f3fc2b0a6475.jpg'
author: cnBeta
comments: false
date: Fri, 13 May 2022 09:59:45 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0513/1e4f3fc2b0a6475.jpg'
---

<div>   
<strong>广泛被使用的FFmpeg多媒体编码库今天合并了对基于AV1免版税视频编解码技术的图像格式的AVIF多路传输支持。</strong>目前互联网应用当中对AVIF图像格式的支持正在增加--特别是现在已经有了广泛的主流网络浏览器支持，并且AVIF已经证明能够提供比JPEG更好的压缩效率和更好的细节保存。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0513/1e4f3fc2b0a6475.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>在现有的MOV/MP4多路复用器代码的基础上，AVIF多路复用支持现在已经被添加到FFmpeg库中。FFmpeg中的AVIF多路复用支持可用于将其他格式的静止图像转换为AVIF，以及更复杂的用途，如将图像转换为AVIF动画图像。</p><p>这个用于FFmpeg的AVIF复用器是由Google的Vignesh Venkatasubramanian开发的。</p><p>更多关于这个用于FFmpeg的AVIF多路复用器的细节，请参阅本次提交：</p><p><a href="https://github.com/FFmpeg/FFmpeg/commit/84241e63cf2f3cc8f7d8a19e86b99f5af95d2a64" _src="https://github.com/FFmpeg/FFmpeg/commit/84241e63cf2f3cc8f7d8a19e86b99f5af95d2a64" target="_blank">https://github.com/FFmpeg/FFmpeg/commit/84241e63cf2f3cc8f7d8a19e86b99f5af95d2a64</a><br></p>   
</div>
            