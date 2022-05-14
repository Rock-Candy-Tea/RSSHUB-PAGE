
---
title: '高吞吐量(HTJ2K)​JPEG 2000图像编码库更新到OpenJPEG 2.5版'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0514/4194be031f08762.jpg'
author: cnBeta
comments: false
date: Sat, 14 May 2022 11:24:23 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0514/4194be031f08762.jpg'
---

<div>   
上周五发布的OpenJPEG 2.5是开源的JPEG 2000图像边骂库的最新更新。值得注意的是，这个BSD
2-clause库的新版本现在支持高吞吐量"HTJ2K"解码。高吞吐量JPEG
2000（HTJ2K）是为了促进更快的图像解码，其代价是稍微降低了效率。<br>
<p>HTJ2K用一个专注于矢量性能的替代编码器取代了JPEG 2000标准块状编码器，高吞吐量的JPEG 2000规范第15部分（ISO/IEC 15444-1）在2019年才被确定下来。</p><p>HTJ2K被描述为为JPEG 2000提供了"数量级的增长"，归功于其新的HT块编码器，对于那些中等到较高的压缩比特率来说，效率提升了大约10倍，对于无损编码来说更是暴增30倍（虽然编码效率比原来的J2K-1编码器低5-10%）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0514/4194be031f08762.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>通过OpenJPH项目，我们之前已经有一个HTJ2K的参考开源实现，而现在随着OpenJPEG 2.5的推出，对高通量JPEG 2000有了额外的开源支持。</p><p>OpenJPEG 2.5除了增加对HTJ2K的解码支持外，现在还支持部分比特流解码。在 OpenJPEG 编码器方面，v2.5 增加了对 TLM 标记生成的支持。OpenJPEG 2.5版本还带来了一系列bug修复来完善自身。</p><p>OpenJPEG 2.5.0的<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>/Linux/MacOS二进制文件和源代码现在可以从GitHub下载：</p><p><a href="https://github.com/uclouvain/openjpeg/releases/tag/v2.5.0" _src="https://github.com/uclouvain/openjpeg/releases/tag/v2.5.0" target="_blank">https://github.com/uclouvain/openjpeg/releases/tag/v2.5.0</a><br></p>   
</div>
            