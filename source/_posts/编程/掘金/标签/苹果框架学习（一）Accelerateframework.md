
---
title: '苹果框架学习（一）Accelerate.framework'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=7463'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 04:54:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=7463'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">文章目录</h3>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23Accelerateframework_1" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#Accelerateframework_1" ref="nofollow noopener noreferrer">苹果框架学习（一）Accelerate.framework</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%231_Accelerate_3" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#1_Accelerate_3" ref="nofollow noopener noreferrer">1. Accelerate简介</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%231__31" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#1__31" ref="nofollow noopener noreferrer">1. 神经网络</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2311__33" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#11__33" ref="nofollow noopener noreferrer">1.1 训练神经网络识别数字</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2312_BNNS_40" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#12_BNNS_40" ref="nofollow noopener noreferrer">1.2 BNNS</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%232__46" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#2__46" ref="nofollow noopener noreferrer">2. 目录、文件和数据存档</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2321__47" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#21__47" ref="nofollow noopener noreferrer">2.1 压缩一个文件</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2322__50" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#22__50" ref="nofollow noopener noreferrer">2.2 解压单文件</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2323__54" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#23__54" ref="nofollow noopener noreferrer">2.3 压缩文件系统目录</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2324__57" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#24__57" ref="nofollow noopener noreferrer">2.4 解压缩和解压存档目录</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2325__60" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#25__60" ref="nofollow noopener noreferrer">2.5 将字符串压缩并保存到文件系统</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2326__63" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#26__63" ref="nofollow noopener noreferrer">2.6 解压缩和解析归档字符串</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%233___67" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#3___67" ref="nofollow noopener noreferrer">3. 压缩</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2331__68" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#31__68" ref="nofollow noopener noreferrer">3.1 使用缓冲区压缩压缩和解压数据</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2332__72" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#32__72" ref="nofollow noopener noreferrer">3.2 压缩字符串，将其写入文件系统，然后使用缓冲区压缩解压相同的文件。</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2333__77" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#33__77" ref="nofollow noopener noreferrer">3.3 用输入和输出过滤器压缩和解压数据</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2334_Swift_81" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#34_Swift_81" ref="nofollow noopener noreferrer">3.4 压缩和解压文件与Swift流压缩</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%234__85" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#4__85" ref="nofollow noopener noreferrer">4. 图像处理要点</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2341__86" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#41__86" ref="nofollow noopener noreferrer">4.1 创建一个核心图形图像格式</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2342__92" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#42__92" ref="nofollow noopener noreferrer">4.2 从核心图形图像创建和填充缓冲区</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2343_vImage_97" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#43_vImage_97" ref="nofollow noopener noreferrer">4.3 从vImage缓冲区创建一个核心图形图像</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2344__102" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#44__102" ref="nofollow noopener noreferrer">4.4 构建一个基本的图像处理工作流</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2345_vImage_107" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#45_vImage_107" ref="nofollow noopener noreferrer">4.5 将vImage操作应用到感兴趣的区域</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2346__111" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#46__111" ref="nofollow noopener noreferrer">4.6 优化图像处理性能</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2347_vImage_115" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#47_vImage_115" ref="nofollow noopener noreferrer">4.7 vImage</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%235__119" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#5__119" ref="nofollow noopener noreferrer">5. 信号处理要点</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2351_StridevDSP_120" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#51_StridevDSP_120" ref="nofollow noopener noreferrer">5.1 用Stride控制vDSP操作</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2352__124" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#52__124" ref="nofollow noopener noreferrer">5.2 使用线性插值来构造新的数据点</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2353_vDSP_128" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#53_vDSP_128" ref="nofollow noopener noreferrer">5.3 利用vDSP实现基于矢量的算法</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2354__132" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#54__132" ref="nofollow noopener noreferrer">5.4 用抽取法重新采样信号</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2355_vDSP_136" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#55_vDSP_136" ref="nofollow noopener noreferrer">5.5 vDSP</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%236__141" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#6__141" ref="nofollow noopener noreferrer">6. 核心视频互操作</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2361__142" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#61__142" ref="nofollow noopener noreferrer">6.1 读取和写入核心视频像素缓冲区</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2362_vImage_146" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#62_vImage_146" ref="nofollow noopener noreferrer">6.2 应用vImage操作的视频样本缓冲区</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2363_vImage_150" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#63_vImage_150" ref="nofollow noopener noreferrer">6.3 实时视频效果与vImage</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2364__154" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#64__154" ref="nofollow noopener noreferrer">6.4 核心视频互操作性</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%237__158" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#7__158" ref="nofollow noopener noreferrer">7. 向量、矩阵和四元数</a></p>
</li>
<li>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2371__159" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#71__159" ref="nofollow noopener noreferrer">7.1 使用向量</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2372__163" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#72__163" ref="nofollow noopener noreferrer">7.2 使用矩阵</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2373__167" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#73__167" ref="nofollow noopener noreferrer">7.3 使用四元数</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2374__171" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#74__171" ref="nofollow noopener noreferrer">7.4 通过改变立方体的顶点来旋转它</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2375_simd_175" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#75_simd_175" ref="nofollow noopener noreferrer">7.5 simd</a></p>
</li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%238__179" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#8__179" ref="nofollow noopener noreferrer">8. 傅里叶变换和余弦变换</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2381__180" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#81__180" ref="nofollow noopener noreferrer">8.1 求复合正弦波的各分量频率</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2382__184" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#82__184" ref="nofollow noopener noreferrer">8.2 使用窗口与离散傅里叶变换</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2383__188" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#83__188" ref="nofollow noopener noreferrer">8.3 噪声信号提取</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2384__192" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#84__192" ref="nofollow noopener noreferrer">8.4 半色调降噪与二维快速傅里叶变换</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2385__196" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#85__196" ref="nofollow noopener noreferrer">8.5 快速傅里叶变换</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2386__200" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#86__200" ref="nofollow noopener noreferrer">8.6 离散傅里叶变换</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2387__204" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#87__204" ref="nofollow noopener noreferrer">8.7 离散余弦变换</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%239__209" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#9__209" ref="nofollow noopener noreferrer">9. 音频处理</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2391_vDSP_210" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#91_vDSP_210" ref="nofollow noopener noreferrer">9.1 均衡音频与vDSP</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2392_IIR_214" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#92_IIR_214" ref="nofollow noopener noreferrer">9.2 双二次IIR滤波器</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2393__218" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#93__218" ref="nofollow noopener noreferrer">9.3 离散余弦变换</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2310__223" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#10__223" ref="nofollow noopener noreferrer">10. 图像格式之间的转换</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23101__225" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#101__225" ref="nofollow noopener noreferrer">10.1 构建一个基本的转换工作流</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23102__229" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#102__229" ref="nofollow noopener noreferrer">10.2 转换彩色图像到灰度</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23103__233" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#103__233" ref="nofollow noopener noreferrer">10.3 标准化处理的任意图像格式</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23104_ARGB_237" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#104_ARGB_237" ref="nofollow noopener noreferrer">10.4 将亮度和色度平面转换为ARGB图像</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23105__241" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#105__241" ref="nofollow noopener noreferrer">10.5 转换</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2311__244" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#11__244" ref="nofollow noopener noreferrer">11. 图像重采样</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23111_vImage_245" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#111_vImage_245" ref="nofollow noopener noreferrer">11.1 在vImage重采样</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23112__249" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#112__249" ref="nofollow noopener noreferrer">11.2 减少再采样图像中的伪影</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23113__253" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#113__253" ref="nofollow noopener noreferrer">11.3 图像剪切</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2312__256" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#12__256" ref="nofollow noopener noreferrer">12. 卷积和形态</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23121__257" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#121__257" ref="nofollow noopener noreferrer">12.1 模糊图像</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23122__261" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#122__261" ref="nofollow noopener noreferrer">12.2 增加散景效果</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23123__265" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#123__265" ref="nofollow noopener noreferrer">12.3 卷积</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23124__269" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#124__269" ref="nofollow noopener noreferrer">12.4 形态</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2313__272" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#13__272" ref="nofollow noopener noreferrer">13. 色彩和色调调整</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23131__273" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#131__273" ref="nofollow noopener noreferrer">13.1 调整图像的亮度和对比度</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23132_278" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#132_278" ref="nofollow noopener noreferrer">13.2.调整饱和度和应用色调映射</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23133__283" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#133__283" ref="nofollow noopener noreferrer">13.3 调整图像的色调</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23134_vImage_288" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#134_vImage_288" ref="nofollow noopener noreferrer">13.4 用vImage指定直方图</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23135__293" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#135__293" ref="nofollow noopener noreferrer">13.5 变换</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23136__298" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#136__298" ref="nofollow noopener noreferrer">13.6 柱状图</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2314_vImage__vDSP_303" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#14_vImage__vDSP_303" ref="nofollow noopener noreferrer">14. vImage / vDSP互操作性</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23141__305" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#141__305" ref="nofollow noopener noreferrer">14.1 在一系列捕获的图像中找到最清晰的图像</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23142__309" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#142__309" ref="nofollow noopener noreferrer">14.2 将声音可视化为声谱图</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2315__313" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#15__313" ref="nofollow noopener noreferrer">15. 稀疏矩阵</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23151__314" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#151__314" ref="nofollow noopener noreferrer">15.1 创建稀疏矩阵</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23152__318" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#152__318" ref="nofollow noopener noreferrer">15.2 实现迭代的方法</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23153__322" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#153__322" ref="nofollow noopener noreferrer">15.3 用直接方法解决系统</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23154__326" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#154__326" ref="nofollow noopener noreferrer">15.4 用迭代方法求解系统</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23155__330" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#155__330" ref="nofollow noopener noreferrer">15.5 创建一个稀疏矩阵从坐标格式数组</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23156__334" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#156__334" ref="nofollow noopener noreferrer">15.6 稀疏的解决者</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2316__339" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#16__339" ref="nofollow noopener noreferrer">16. 算术和超越函数</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2317__342" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#17__342" ref="nofollow noopener noreferrer">17. 线性代数</a></p>
</li>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23171_Vandermonde_343" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#171_Vandermonde_343" ref="nofollow noopener noreferrer">17.1 用Vandermonde方法求插值多项式</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%23172_BLAS_346" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#172_BLAS_346" ref="nofollow noopener noreferrer">17.2 BLAS</a></li>
</ul>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2318__349" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#18__349" ref="nofollow noopener noreferrer">18. 明确的集成</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2319__353" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#19__353" ref="nofollow noopener noreferrer">19. 枚举</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501%2320__462" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501#20__462" ref="nofollow noopener noreferrer">20. 协议</a></p>
</li>
</ul>
<h1 data-id="heading-1">苹果框架学习（一）Accelerate.framework</h1>
<h1 data-id="heading-2">1. Accelerate简介</h1>
<p>Accelerate框架能做什么？</p>
<blockquote>
<p>进行大规模的数学计算和图像计算，优化为高性能和低能耗。</p>
</blockquote>
<p>通过利用其向量处理能力，Accelerate在CPU上提供高性能、节能的计算。下面的加速库抽象了这种能力，使为它们编写的代码在运行时执行适当的处理器指令:</p>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fbnns" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/bnns" ref="nofollow noopener noreferrer">BNNS</a>. 为训练和推理而构造和运行神经网络的子程序。</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fvimage" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/vimage" ref="nofollow noopener noreferrer">vImage</a>。广泛的图像处理功能，包括核心图形和核心视频互操作、格式转换和图像处理。</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fvdsp" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/vdsp" ref="nofollow noopener noreferrer">vDSP</a>。数字信号处理函数，包括一维和二维快速傅里叶变换、双二次滤波、向量和矩阵运算、卷积和类型转换。</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fveclib%2Fvforce" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/veclib/vforce" ref="nofollow noopener noreferrer">vForce</a>。在向量上执行算术和超越函数的函数。</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fsparse_solvers" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/sparse_solvers" ref="nofollow noopener noreferrer">Sparse Solvers</a>, <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fblas" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/blas" ref="nofollow noopener noreferrer">BLAS</a>,，和LAPACK。在稀疏和密集矩阵上执行线性代数的库。</p>
</li>
</ul>
<p>虽然不是加速框架的一部分，以下库是密切相关的:</p>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fapplearchive" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/applearchive" ref="nofollow noopener noreferrer">苹果公司存档(Apple Archive. )</a>。对目录、文件和数据执行多线程无损压缩的框架。</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fcompression" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/compression" ref="nofollow noopener noreferrer">压缩(Compression)</a>。支持LZFSE、LZ4、LZMA和ZLIB算法的无损数据压缩算法。</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fsimd" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/simd" ref="nofollow noopener noreferrer">simd</a>。一种对小向量和矩阵进行计算的模块。</p>
</li>
</ul>
<h1 data-id="heading-3">1. 神经网络</h1>
<h2 data-id="heading-4">1.1 训练神经网络识别数字</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Ftraining_a_neural_network_to_recognize_digits" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/training_a_neural_network_to_recognize_digits" ref="nofollow noopener noreferrer">苹果官方训练神经网络识别数字demo:点击这里下载</a></p>
<p>建立一个简单的神经网络，训练它识别随机产生的数字。</p>
<h2 data-id="heading-5">1.2 BNNS</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fbnns" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/bnns" ref="nofollow noopener noreferrer">BNNS</a><br>
实现和运行训练和推理的神经网络。</p>
<p>加速框架的BNNS库是一个函数集合，您可以使用它来构建用于训练和推理的神经网络。macOS、iOS、tvOS和watchOS都支持它。BNNS为这些平台上支持的所有cpu提供了高性能和低能耗优化例程。</p>
<h1 data-id="heading-6">2. 目录、文件和数据存档</h1>
<h2 data-id="heading-7">2.1 压缩一个文件</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcompressing_single_files" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/compressing_single_files" ref="nofollow noopener noreferrer">压缩一个文件</a><br>
压缩一个文件并将结果存储在文件系统上。</p>
<h2 data-id="heading-8">2.2 解压单文件</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fdecompressing_single_files" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/decompressing_single_files" ref="nofollow noopener noreferrer">解压单文件</a><br>
从压缩文件重新创建单个文件。</p>
<h2 data-id="heading-9">2.3 压缩文件系统目录</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcompressing_file_system_directories" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/compressing_file_system_directories" ref="nofollow noopener noreferrer">压缩文件系统目录</a><br>
压缩整个目录的内容，并将结果存储在文件系统上。</p>
<h2 data-id="heading-10">2.4 解压缩和解压存档目录</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fdecompressing_and_extracting_an_archived_directory" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/decompressing_and_extracting_an_archived_directory" ref="nofollow noopener noreferrer">解压缩和解压存档目录</a><br>
Recreate an entire file system directory from an archive file.</p>
<h2 data-id="heading-11">2.5 将字符串压缩并保存到文件系统</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcompressing_and_saving_a_string_to_the_file_system" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/compressing_and_saving_a_string_to_the_file_system" ref="nofollow noopener noreferrer">将字符串压缩并保存到文件系统</a><br>
压缩Unicode字符串的内容并将结果存储在文件系统中。</p>
<h2 data-id="heading-12">2.6 解压缩和解析归档字符串</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fdecompressing_and_parsing_an_archived_string" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/decompressing_and_parsing_an_archived_string" ref="nofollow noopener noreferrer">解压缩和解析归档字符串</a><br>
从存档文件重新创建字符串</p>
<h1 data-id="heading-13">3. 压缩</h1>
<h2 data-id="heading-14">3.1 使用缓冲区压缩压缩和解压数据</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcompressing_and_decompressing_data_with_buffer_compression" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/compressing_and_decompressing_data_with_buffer_compression" ref="nofollow noopener noreferrer">使用缓冲区压缩压缩和解压数据</a><br>
压缩字符串，将其写入文件系统，然后使用缓冲区压缩解压相同的文件。</p>
<h2 data-id="heading-15">3.2 压缩字符串，将其写入文件系统，然后使用缓冲区压缩解压相同的文件。</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcompressing_and_decompressing_files_with_stream_compression" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/compressing_and_decompressing_files_with_stream_compression" ref="nofollow noopener noreferrer">压缩字符串，将其写入文件系统，然后使用缓冲区压缩解压相同的文件。</a><br>
根据文件的路径扩展名对文件执行压缩或适当的解压。</p>
<h2 data-id="heading-16">3.3 用输入和输出过滤器压缩和解压数据</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcompressing_and_decompressing_data_with_input_and_output_filters" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/compressing_and_decompressing_data_with_input_and_output_filters" ref="nofollow noopener noreferrer">用输入和输出过滤器压缩和解压数据</a><br>
使用输入和输出过滤器压缩和解压流数据或来自内存的数据。</p>
<h2 data-id="heading-17">3.4 压缩和解压文件与Swift流压缩</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcompressing_and_decompressing_files_with_swift_stream_compression" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/compressing_and_decompressing_files_with_swift_stream_compression" ref="nofollow noopener noreferrer">压缩和解压文件与Swift流压缩</a><br>
对所有文件执行压缩，对扩展类型支持的文件执行解压缩。</p>
<h1 data-id="heading-18">4. 图像处理要点</h1>
<h2 data-id="heading-19">4.1 创建一个核心图形图像格式</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcreating_a_core_graphics_image_format" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/creating_a_core_graphics_image_format" ref="nofollow noopener noreferrer">创建一个核心图形图像格式</a><br>
为vImage之间的转换提供核心图形图像格式的描述。</p>
<h2 data-id="heading-20">4.2 从核心图形图像创建和填充缓冲区</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcreating_and_populating_buffers_from_core_graphics_images" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/creating_and_populating_buffers_from_core_graphics_images" ref="nofollow noopener noreferrer">从核心图形图像创建和填充缓冲区</a><br>
从核心图形图像初始化vImage缓冲区。</p>
<h2 data-id="heading-21">4.3 从vImage缓冲区创建一个核心图形图像</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcreating_a_core_graphics_image_from_a_vimage_buffer" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/creating_a_core_graphics_image_from_a_vimage_buffer" ref="nofollow noopener noreferrer">从vImage缓冲区创建一个核心图形图像</a><br>
创建vImage缓冲区的可显示表示。</p>
<h2 data-id="heading-22">4.4 构建一个基本的图像处理工作流</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fbuilding_a_basic_image-processing_workflow" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/building_a_basic_image-processing_workflow" ref="nofollow noopener noreferrer">构建一个基本的图像处理工作流</a><br>
用vImage调整图像的大小。</p>
<h2 data-id="heading-23">4.5 将vImage操作应用到感兴趣的区域</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fapplying_vimage_operations_to_regions_of_interest" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/applying_vimage_operations_to_regions_of_interest" ref="nofollow noopener noreferrer">将vImage操作应用到感兴趣的区域</a><br>
将vImage操作的效果限制在感兴趣的矩形区域。</p>
<h2 data-id="heading-24">4.6 优化图像处理性能</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Foptimizing_image_processing_performance" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/optimizing_image_processing_performance" ref="nofollow noopener noreferrer">优化图像处理性能</a><br>
改善你的应用程序的性能转换图像缓冲格式从交错到平面。</p>
<h2 data-id="heading-25">4.7 vImage</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fvimage" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/vimage" ref="nofollow noopener noreferrer">vImage</a><br>
使用CPU的向量处理器处理大型图像。</p>
<h1 data-id="heading-26">5. 信号处理要点</h1>
<h2 data-id="heading-27">5.1 用Stride控制vDSP操作</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcontrolling_vdsp_operations_with_stride" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/controlling_vdsp_operations_with_stride" ref="nofollow noopener noreferrer">用Stride控制vDSP操作</a><br>
定期选择性地对向量的元素进行操作。</p>
<h2 data-id="heading-28">5.2 使用线性插值来构造新的数据点</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fuse_linear_interpolation_to_construct_new_data_points" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/use_linear_interpolation_to_construct_new_data_points" ref="nofollow noopener noreferrer">使用线性插值来构造新的数据点</a><br>
使用线性插值来填补数值数据数组中的空白。</p>
<h2 data-id="heading-29">5.3 利用vDSP实现基于矢量的算法</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fusing_vdsp_for_vector-based_arithmetic" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/using_vdsp_for_vector-based_arithmetic" ref="nofollow noopener noreferrer">利用vDSP实现基于矢量的算法</a><br>
用vDSP矢量-矢量和矢量-标量运算提高了常见数学任务的性能。</p>
<h2 data-id="heading-30">5.4 用抽取法重新采样信号</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fresampling_a_signal_with_decimationv" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/resampling_a_signal_with_decimationv" ref="nofollow noopener noreferrer">用抽取法重新采样信号</a><br>
通过指定抽取因子和应用自定义抗混叠滤波器来降低信号的采样率。</p>
<h2 data-id="heading-31">5.5 vDSP</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fvdsp" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/vdsp" ref="nofollow noopener noreferrer">vDSP</a><br>
在大矢量上进行基本的算术运算和常用的数字信号处理程序。</p>
<h1 data-id="heading-32">6. 核心视频互操作</h1>
<h2 data-id="heading-33">6.1 读取和写入核心视频像素缓冲区</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Freading_from_and_writing_to_core_video_pixel_buffers" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/reading_from_and_writing_to_core_video_pixel_buffers" ref="nofollow noopener noreferrer">读取和写入核心视频像素缓冲区</a><br>
在核心视频像素缓冲器和vImage缓冲器之间传输图像数据，以集成vImage操作到核心图像工作流</p>
<h2 data-id="heading-34">6.2 应用vImage操作的视频样本缓冲区</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fapplying_vimage_operations_to_video_sample_buffers" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/applying_vimage_operations_to_video_sample_buffers" ref="nofollow noopener noreferrer">应用vImage操作的视频样本缓冲区</a><br>
使用vImage的any-to-any功能来对从设备摄像头流出的视频帧进行实时图像处理。</p>
<h2 data-id="heading-35">6.3 实时视频效果与vImage</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Freal-time_video_effects_with_vimage" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/real-time_video_effects_with_vimage" ref="nofollow noopener noreferrer">实时视频效果与vImage</a><br>
使用vImage应用效果的视频馈送实时。</p>
<h2 data-id="heading-36">6.4 核心视频互操作性</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcore_video_interoperability" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/core_video_interoperability" ref="nofollow noopener noreferrer">核心视频互操作性</a><br>
在Core Video和vImage之间传递图像数据。</p>
<h1 data-id="heading-37">7. 向量、矩阵和四元数</h1>
<h2 data-id="heading-38">7.1 使用向量</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fworking_with_vectors" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/working_with_vectors" ref="nofollow noopener noreferrer">使用向量</a><br>
使用向量来计算几何值，计算点积和叉积，以及在值之间进行插值。</p>
<h2 data-id="heading-39">7.2 使用矩阵</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fworking_with_matrices" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/working_with_matrices" ref="nofollow noopener noreferrer">使用矩阵</a><br>
解联立方程，在空间中变换点。</p>
<h2 data-id="heading-40">7.3 使用四元数</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fworking_with_quaternions" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/working_with_quaternions" ref="nofollow noopener noreferrer">使用四元数</a><br>
旋转球体表面上的点，并在它们之间插入。</p>
<h2 data-id="heading-41">7.4 通过改变立方体的顶点来旋转它</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Frotating_a_cube_by_transforming_its_vertices" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/rotating_a_cube_by_transforming_its_vertices" ref="nofollow noopener noreferrer">通过改变立方体的顶点来旋转它</a><br>
使用四元数插值将立方体旋转到一系列关键帧之间进行转换。</p>
<h2 data-id="heading-42">7.5 simd</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fsimd" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/simd" ref="nofollow noopener noreferrer">simd</a><br>
对小向量和矩阵进行计算。</p>
<h1 data-id="heading-43">8. 傅里叶变换和余弦变换</h1>
<h2 data-id="heading-44">8.1 求复合正弦波的各分量频率</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Ffinding_the_component_frequencies_in_a_composite_sine_wave" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/finding_the_component_frequencies_in_a_composite_sine_wave" ref="nofollow noopener noreferrer">求复合正弦波的各分量频率</a><br>
使用一维快速傅里叶变换计算信号的频率成分。</p>
<h2 data-id="heading-45">8.2 使用窗口与离散傅里叶变换</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fusing_windowing_with_discrete_fourier_transforms" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/using_windowing_with_discrete_fourier_transforms" ref="nofollow noopener noreferrer">使用窗口与离散傅里叶变换</a><br>
将信号数据与窗序列值相乘以减少频谱泄漏。</p>
<h2 data-id="heading-46">8.3 噪声信号提取</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fsignal_extraction_from_noise" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/signal_extraction_from_noise" ref="nofollow noopener noreferrer">噪声信号提取</a><br>
使用加速的离散余弦变换去噪信号。</p>
<h2 data-id="heading-47">8.4 半色调降噪与二维快速傅里叶变换</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fhalftone_descreening_with_2d_fast_fourier_transform" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/halftone_descreening_with_2d_fast_fourier_transform" ref="nofollow noopener noreferrer">半色调降噪与二维快速傅里叶变换</a><br>
减少或删除图像中的周期性工件。</p>
<h2 data-id="heading-48">8.5 快速傅里叶变换</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Ffast_fourier_transforms" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/fast_fourier_transforms" ref="nofollow noopener noreferrer">快速傅里叶变换</a><br>
将时域和空域复数值的向量和矩阵变换到频域，反之亦然。</p>
<h2 data-id="heading-49">8.6 离散傅里叶变换</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fdiscrete_fourier_transforms" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/discrete_fourier_transforms" ref="nofollow noopener noreferrer">离散傅里叶变换</a><br>
将时域和空域复数值的向量变换到频域，反之亦然。</p>
<h2 data-id="heading-50">8.7 离散余弦变换</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fdiscrete_cosine_transforms" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/discrete_cosine_transforms" ref="nofollow noopener noreferrer">离散余弦变换</a><br>
将时域和空域的实值向量变换到频域，反之亦然。</p>
<h1 data-id="heading-51">9. 音频处理</h1>
<h2 data-id="heading-52">9.1 均衡音频与vDSP</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fequalizing_audio_with_vdsp" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/equalizing_audio_with_vdsp" ref="nofollow noopener noreferrer">均衡音频与vDSP</a><br>
形状音频输出使用离散余弦变换和双二次滤波器。</p>
<h2 data-id="heading-53">9.2 双二次IIR滤波器</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fbiquadratic_iir_filters" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/biquadratic_iir_filters" ref="nofollow noopener noreferrer">双二次IIR滤波器</a><br>
对单通道和多通道数据应用双二次滤波器。</p>
<h2 data-id="heading-54">9.3 离散余弦变换</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fdiscrete_cosine_transforms" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/discrete_cosine_transforms" ref="nofollow noopener noreferrer">离散余弦变换</a><br>
将时域和空域的实值向量变换到频域，反之亦然。</p>
<h1 data-id="heading-55">10. 图像格式之间的转换</h1>
<h2 data-id="heading-56">10.1 构建一个基本的转换工作流</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fbuilding_a_basic_conversion_workflow" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/building_a_basic_conversion_workflow" ref="nofollow noopener noreferrer">构建一个基本的转换工作流</a><br>
通过将CMYK图像转换为RGB图像，学习转换任意到任意函数的基本原理。</p>
<h2 data-id="heading-57">10.2 转换彩色图像到灰度</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fconverting_color_images_to_grayscale" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/converting_color_images_to_grayscale" ref="nofollow noopener noreferrer">转换彩色图像到灰度</a><br>
转换彩色图像到灰度使用矩阵乘法。</p>
<h2 data-id="heading-58">10.3 标准化处理的任意图像格式</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fstandardizing_arbitrary_image_formats_for_processing" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/standardizing_arbitrary_image_formats_for_processing" ref="nofollow noopener noreferrer">标准化处理的任意图像格式</a><br>
转换资产与不同的颜色空间和位深度到一个标准的工作格式应用vImage操作。</p>
<h2 data-id="heading-59">10.4 将亮度和色度平面转换为ARGB图像</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fconverting_luminance_and_chrominance_planes_to_an_argb_image" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/converting_luminance_and_chrominance_planes_to_an_argb_image" ref="nofollow noopener noreferrer">将亮度和色度平面转换为ARGB图像</a><br>
从设备的摄像头提供的亮度和色度信息创建一个可显示的ARGB图像。</p>
<h2 data-id="heading-60">10.5 转换</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fconversion" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/conversion" ref="nofollow noopener noreferrer">转换</a><br>
将图像转换为不同的格式。</p>
<h1 data-id="heading-61">11. 图像重采样</h1>
<h2 data-id="heading-62">11.1 在vImage重采样</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fresampling_in_vimage" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/resampling_in_vimage" ref="nofollow noopener noreferrer">在vImage重采样</a><br>
了解vImage如何在几何操作期间对图像数据重新采样。</p>
<h2 data-id="heading-63">11.2 减少再采样图像中的伪影</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Freducing_artifacts_in_resampled_images" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/reducing_artifacts_in_resampled_images" ref="nofollow noopener noreferrer">减少再采样图像中的伪影</a><br>
当使用自定义重采样过滤器缩放图像时，避免由默认的Lanczos算法引入的振铃效应。</p>
<h2 data-id="heading-64">11.3 图像剪切</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fimage_shearing" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/image_shearing" ref="nofollow noopener noreferrer">图像剪切</a><br>
水平和垂直剪切图像。</p>
<h1 data-id="heading-65">12. 卷积和形态</h1>
<h2 data-id="heading-66">12.1 模糊图像</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fblurring_an_image" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/blurring_an_image" ref="nofollow noopener noreferrer">模糊图像</a><br>
过滤器图像与自定义和高速内核卷积。</p>
<h2 data-id="heading-67">12.2 增加散景效果</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fadding_a_bokeh_effect" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/adding_a_bokeh_effect" ref="nofollow noopener noreferrer">增加散景效果</a><br>
应用膨胀模拟散景效应。</p>
<h2 data-id="heading-68">12.3 卷积</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fconvolution" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/convolution" ref="nofollow noopener noreferrer">卷积</a><br>
对图像应用卷积核。</p>
<h2 data-id="heading-69">12.4 形态</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fmorphology" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/morphology" ref="nofollow noopener noreferrer">形态</a><br>
膨胀和侵蚀图像。</p>
<h1 data-id="heading-70">13. 色彩和色调调整</h1>
<h2 data-id="heading-71">13.1 调整图像的亮度和对比度</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fadjusting_the_brightness_and_contrast_of_an_image" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/adjusting_the_brightness_and_contrast_of_an_image" ref="nofollow noopener noreferrer">调整图像的亮度和对比度</a></p>
<p>使用函数来应用线性或指数曲线。</p>
<h2 data-id="heading-72">13.2.调整饱和度和应用色调映射</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fadjusting_saturation_and_applying_tone_mapping" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/adjusting_saturation_and_applying_tone_mapping" ref="nofollow noopener noreferrer">调整饱和度和应用色调映射</a></p>
<p>将RGB图像转换为离散亮度和色度通道，并应用颜色和对比度处理。</p>
<h2 data-id="heading-73">13.3 调整图像的色调</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fadjusting_the_hue_of_an_image" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/adjusting_the_hue_of_an_image" ref="nofollow noopener noreferrer">调整图像的色调</a></p>
<p>转换一个RGB图像到L</p>
<p>a</p>
<p>b*色彩空间和应用色调调整。</p>
<h2 data-id="heading-74">13.4 用vImage指定直方图</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fadjusting_the_hue_of_an_image" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/adjusting_the_hue_of_an_image" ref="nofollow noopener noreferrer">用vImage指定直方图</a></p>
<p>计算一幅图像的直方图，并将其应用于另一幅图像。</p>
<h2 data-id="heading-75">13.5 变换</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Ftransform" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/transform" ref="nofollow noopener noreferrer">变换</a></p>
<p>对图像应用颜色转换。</p>
<h1 data-id="heading-76">13.6 柱状图</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fhistogram" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/histogram" ref="nofollow noopener noreferrer">柱状图</a></p>
<p>计算和或操作图像的直方图。</p>
<h1 data-id="heading-77">14. vImage / vDSP互操作性</h1>
<h2 data-id="heading-78">14.1 在一系列捕获的图像中找到最清晰的图像</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Ffinding_the_sharpest_image_in_a_sequence_of_captured_images" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/finding_the_sharpest_image_in_a_sequence_of_captured_images" ref="nofollow noopener noreferrer">在一系列捕获的图像中找到最清晰的图像</a><br>
共享图像数据之间的vDSP和vImage计算最锐的图像从括号照片序列。</p>
<h2 data-id="heading-79">14.2 将声音可视化为声谱图</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fvisualizing_sound_as_an_audio_spectrogram" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/visualizing_sound_as_an_audio_spectrogram" ref="nofollow noopener noreferrer">将声音可视化为声谱图</a><br>
在vDSP和vImage之间共享图像数据，使设备麦克风捕获的音频可视化。</p>
<h1 data-id="heading-80">15. 稀疏矩阵</h1>
<h2 data-id="heading-81">15.1 创建稀疏矩阵</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcreating_sparse_matrices" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/creating_sparse_matrices" ref="nofollow noopener noreferrer">创建稀疏矩阵</a><br>
为分解和求解系统创建稀疏矩阵。</p>
<h2 data-id="heading-82">15.2 实现迭代的方法</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fimplementing_iterative_methods" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/implementing_iterative_methods" ref="nofollow noopener noreferrer">实现迭代的方法</a><br>
使用迭代方法比直接方法更快地解决大问题，并以更低的内存开销。</p>
<h2 data-id="heading-83">15.3 用直接方法解决系统</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fsolving_systems_using_direct_methods" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/solving_systems_using_direct_methods" ref="nofollow noopener noreferrer">用直接方法解决系统</a><br>
使用直接方法来解决系数矩阵是稀疏的方程组。</p>
<h2 data-id="heading-84">15.4 用迭代方法求解系统</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fsolving_systems_using_iterative_methods" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/solving_systems_using_iterative_methods" ref="nofollow noopener noreferrer">用迭代方法求解系统</a><br>
使用迭代方法来求解系数矩阵是稀疏的方程组。</p>
<h2 data-id="heading-85">15.5 创建一个稀疏矩阵从坐标格式数组</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fcreating_a_sparse_matrix_from_coordinate_format_arrays" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/creating_a_sparse_matrix_from_coordinate_format_arrays" ref="nofollow noopener noreferrer">创建一个稀疏矩阵从坐标格式数组</a><br>
使用单独的坐标格式数组来创建稀疏矩阵。</p>
<h2 data-id="heading-86">15.6 稀疏的解决者</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fsparse_solvers" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/sparse_solvers" ref="nofollow noopener noreferrer">稀疏的解决者</a><br>
解系数矩阵是稀疏的方程组。</p>
<h1 data-id="heading-87">16. 算术和超越函数</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fveclib" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/veclib" ref="nofollow noopener noreferrer">vecLib</a><br>
在大向量上执行计算。</p>
<h1 data-id="heading-88">17. 线性代数</h1>
<h2 data-id="heading-89">17.1 用Vandermonde方法求插值多项式</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Ffinding_an_interpolating_polynomial_using_the_vandermonde_method" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/finding_an_interpolating_polynomial_using_the_vandermonde_method" ref="nofollow noopener noreferrer">用Vandermonde方法求插值多项式</a><br>
利用LAPACK求解一个线性系统，并找到一个插值多项式在一系列已知数据点之间构造新的点。</p>
<h2 data-id="heading-90">17.2 BLAS</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fblas" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/blas" ref="nofollow noopener noreferrer">BLAS</a><br>
苹果实现的基本线性代数子程序(BLAS)。</p>
<h1 data-id="heading-91">18. 明确的集成</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fquadrature" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/quadrature" ref="nofollow noopener noreferrer">Quadrature</a><br>
在有限或无限区间上近似函数的定积分。</p>
<h1 data-id="heading-92">19. 枚举</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fbnns-c5d" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/bnns-c5d" ref="nofollow noopener noreferrer">BNNS</a><br>
充当到BNNS的Swift覆盖的命名空间的枚举。</p>
<p><strong>Base Classes</strong></p>
<ul>
<li>
<p>class BNNS.Layer<br>
The base class for layer objects that wrap filters and manage deinitialization.</p>
</li>
<li>
<p>class BNNS.UnaryLayer<br>
The base class for layers that accept a single input.</p>
</li>
<li>
<p>class BNNS.BinaryLayer<br>
The base class for layers that accept two inputs.</p>
</li>
</ul>
<p><strong>Type Methods</strong></p>
<p>- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">static func applyActivation(activation: BNNS.ActivationFunction,</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">input: --BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor,</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">batchSize: Int, filterParameters: BNNSFilterParameters?)</a></p>
<p>- Applies the specified activation function.</p>
<p>- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">static func applyInTopK(k: Int, input: BNNSNDArrayDescriptor, testIndices:</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">BNNSNDArrayDescriptor, output:</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">BNNSNDArrayDescriptor, axis: Int, batchSize:</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">Int, filterParameters: BNNSFilterParameters?)</a></p>
<p>Applies an in-top-k filter directly to an input. <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer"></a></p>
<p>- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">static func applyReduction(BNNS.ReductionFunction,</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor,</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">weights: BNNSNDArrayDescriptor?,</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">filterParameters: BNNSFilterParameters?)</a></p>
<p>Applies the specified reduction function.</p>
<p>- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">static func applyTopK(k: Int, input: BNNSNDArrayDescriptor,</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">bestValues: BNNSNDArrayDescriptor, bestIndices: BNNSNDArrayDescriptor,</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">axis: Int, batchSize: Int, filterParameters:</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">BNNSFilterParameters?)</a></p>
<p>Applies a top-k filter directly to an input.</p>
<p>- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">static func compare(BNNSNDArrayDescriptor, BNNSND</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">ArrayDescriptor, filterParameters: BNNSFilterParameters?)</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer"></a></p>
<p>- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">static func transpose(input: BNNSNDArrayDescriptor, out</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">put: BNNSNDArrayDescriptor, firstTransposeAxis: Int, secondTransposeAxis: Int, filterParameters: BNNSFilterParameters?)</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer"></a></p>
<p><strong>Classes</strong><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.ActivationLayer</a><br>
A layer object that wraps an activation filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.BinaryArithmeticLayer</a><br>
A layer object that wraps a binary arithmetic filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.BroadcastMatrixMultiplyLayer</a><br>
A layer object that wraps a broadcast matrix multiply filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.ConvolutionLayer</a><br>
A layer object that wraps a convolution filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.DropoutLayer</a><br>
A layer object that wraps a dropout filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.FullyConnectedLayer</a><br>
A layer object that wraps a fully connected filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.FusedConvolution</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">NormalizationLayer</a></p>
<p>A layer object that wraps a fused, convolution normalization layer and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.FusedFullyConnectedNorma</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">lizationLayer</a></p>
<p>A layer object that wraps a fused, fully connected normalization layer and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.FusedLayer</a><br>
The base class for fused convolution-normalization and fully connected-normalization layers.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.GramLayer</a><br>
A layer object that wraps a Gram matrix filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.LossLayer</a><br>
A layer object that wraps a loss filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.NormalizationLayer</a><br>
A layer object that wraps a normalization filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.PaddingLayer</a><br>
A layer object that wraps a padding filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.PermuteLayer</a><br>
A layer object that wraps a permute filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.PoolingLayer</a><br>
A layer object that wraps a pooling filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.ReductionLayer</a><br>
A layer object that wraps a reduction filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.ResizeLayer</a><br>
A layer object that wraps a resize filter and manages its deinitialization.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">class BNNS.UnaryArithmeticLayer</a><br>
A layer object that wraps a unary arithmetic filter and manages its deinitialization.</p>
<p><strong>Structures</strong><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">struct BNNS.AdamOptimizer</a><br>
An optimizer that uses the Adam optimization algorithm.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">struct BNNS.RMSPropOptimizer</a><br>
An optimizer that uses the root-mean-square prop (RMSProp) optimization method.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">struct BNNS.RelationalOperator</a><br>
Constants that describe relational operations.</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">struct BNNS.SGDMomentumOptimizer</a><br>
An optimizer that uses the stochastic gradient descent (SGD) with the momentum optimization method.</p>
<p><strong>Enumerations</strong><br>
enum BNNS.ActivationFunction<br>
Constants that describe activation functions.</p>
<p>enum BNNS.ArithmeticBinaryFunction<br>
Constants that describe binary arithmetic functions.</p>
<p>enum BNNS.ArithmeticUnaryFunction<br>
Constants that describe unary arithmetic functions.<br>
enum BNNS.ConvolutionPadding</p>
<p>Constants that describe convolution padding modes.<br>
enum BNNS.ConvolutionType<br>
Constants that describe convolution types.</p>
<p>enum BNNS.DataLayout<br>
Constants that describe the data layout of an n-dimensional array descriptor shape.<br>
enum BNNS.DescriptorType</p>
<p>Constants that describe the input and output types of an arithmetic operation.<br>
enum BNNS.Error<br>
enum BNNS.InterpolationMethod</p>
<p>enum BNNS.LearningPhase<br>
Constants that describe the learning phase of a normalization operation.<br>
enum BNNS.LossFunction</p>
<p>Constants that describe loss functions.<br>
enum BNNS.LossReduction<br>
An enumeration that describes loss reduction functions.</p>
<p>enum BNNS.NormalizationType<br>
Constants that describe normalization types.<br>
enum BNNS.PaddingMode</p>
<p>Constants that define padding modes.<br>
enum BNNS.PoolingType<br>
Constants that describe pooling types.</p>
<p>enum BNNS.ReductionFunction<br>
Constants that describe reduction functions.</p>
<p>enum BNNS.Shape<br>
Constants that describe the size and data layout of an n-dimensional array descriptor.</p>
<h1 data-id="heading-93">20. 协议</h1>
<p>protocol <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fbnnsoptimizer" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/bnnsoptimizer" ref="nofollow noopener noreferrer">BNNSOptimizer</a></p>
<p>protocol <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Faccelerate%2Fbnnsscalar" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/accelerate/bnnsscalar" ref="nofollow noopener noreferrer">BNNSScalar</a></p>
<p>**由于文章篇幅有限，只能点到即止地介绍当前一些工作成果和思考，各个 <strong>framework</strong> 还有一些新的方向在探索，如果你对 iOS 底层原理、架构设计、构建系统、如何面试有兴趣了解，**你也可以私信我及时获取最新资料以及面试相关资料。如果你有什么意见和建议欢迎给我留言！</p>
<p><strong>喜欢iOS的小伙伴可以关注我，一起学习交流！！！</strong></p>
<p>原文链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F108232755" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/108232755" ref="nofollow noopener noreferrer">blog.csdn.net/kyl28288954…</a></p></div>  
</div>
            