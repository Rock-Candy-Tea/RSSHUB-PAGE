
---
title: 'Hi-C技术的初步了解'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/18922188-f4a2144afb6b2345.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/18922188-f4a2144afb6b2345.png'
---

<div>   
<p>最近的一次组会上看到实验室的同学汇报的结果里有Hi-C的图，所以我就悄咪咪的去了解了一下Hi-C技术的原理。整理一下。</p>
<h4>Q1: Hi-C的全称是什么？</h4>
<p>A: 高通量染色体构象捕获技术（High-throughput chromosome conformation capture）</p>
<h4>Q2: 简单的说，Hi-C技术是干嘛的？</h4>
<p>A: Hi-C 是以整个细胞核为研究对象，利用高通量测序技术，研究全基因组范围内整个染色质 DNA 在空间位置上的关系，捕获不同基因座位上之间的空间交互信息。Hi-C 可以与 RNA-Seq、ChIP-Seq 等数据进行联合分析，从基因调控网络和表观遗传网络来阐述生物体性状形成的相关机制。（参考文章：<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fwww.biomart.cn%2Fspecials%2Fgeneontology%2Farticle%2F537732" target="_blank">Hi-C 技术</a>, <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.plob.org%2Farticle%2F12842.html" target="_blank">Hi-C技术到底能做什么？</a>）</p>
<h4>Q3: Hi-C的实验流程是什么？</h4>
<p>A: 可以参考哈佛大学录制的视频，20多分钟，里面介绍了详细的实验流程。这个视频的好处是还可以选择播放速度，英文不太好的童鞋也不用担心，让它慢一点播放就行了。点这里：<a href="https://links.jianshu.com/go?to=%255Bhttps%3A%2F%2Fwww.jove.com%2Fvideo%2F1869%2Fhi-c-a-method-to-study-the-three-dimensional-architecture-of-genomes%255D%28https%3A%2F%2Fwww.jove.com%2Fvideo%2F1869%2Fhi-c-a-method-to-study-the-three-dimensional-architecture-of-genomes%29" target="_blank">Hi-C: A Method to Study the Three-dimensional Architecture of Genomes.</a></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1129" data-height="399"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-f4a2144afb6b2345.png" data-original-width="1129" data-original-height="399" data-original-format="image/png" data-original-filesize="254110" src="https://upload-images.jianshu.io/upload_images/18922188-f4a2144afb6b2345.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>一般流程：<br>
<strong>（1）</strong>细胞（2 x 10^ 7至2.5 x 10 ^7）用甲醛交联，如此一来，在空间上相互作用的染色质片段之间产生共价键（上图中DNA片段：蓝色，红色。中间的环状的是protein）。<br>
<strong>（2）</strong>染色质用限制酶（此处为HindIII；限制位点：虚线）消化。产生的粘性末端被核苷酸填充一部分，并且被标记生物素（紫色点）。<strong>这里需要注意的是，你需要有一个空白对照，即没有HindIII处理的样品，因为你需要跑胶检查你的酶切结果。</strong><br>
<strong>（3）</strong>连接：是在极稀的条件下进行的，有利于分子内连接。这时HindIII酶切位点就没了，多出了一个NheI位点。再进行酶切。<br>
<strong>NOTE:这里要进行质量检测：</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1288" data-height="432"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-eb8830cd3c4908f0.png" data-original-width="1288" data-original-height="432" data-original-format="image/png" data-original-filesize="331041" src="https://upload-images.jianshu.io/upload_images/18922188-eb8830cd3c4908f0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>上图里，A图是分别用不同量的3C和Hi-C文库跑的胶。一般来说Hi-C文库的连接效率要比3C稍微低一些，所以会有一些弥散的感觉。质量控制步骤应显示3C和Hi-C库均大于10 kb。DNA条带弥散表明连接效率差。B图里分别是不同的对照和进行两次酶切的DNA胶结果图。NheI切割了70％的Hi-C扩增子。<br>
（4）纯化和剪切DNA。<br>
（5）使用链霉亲和素珠分离生物素标记的片段。然后进行测序。</p>
<h4>Q4: 如何知道Hi-C测序的质量如何？</h4>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="580" data-height="274"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-e000f57161a2d952.png" data-original-width="580" data-original-height="274" data-original-format="image/png" data-original-filesize="82075" src="https://upload-images.jianshu.io/upload_images/18922188-e000f57161a2d952.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>A: 上图A中，与随机产生的read（绿色）相比，染色体内（蓝色）和染色体间（红色）相互作用的片段的reads明显更接近HindIII限制性酶切位点。随着距HindIII位点的距离增加，染色体内读数和染色体间读数曲线都迅速减小,直到染色体在〜500 bp处达到平稳为止。500bp是用于测序的最大片段大小。图B说的是，通常，55％的可比对的reads 对代表染色体间相互作用。15％表示间隔小于20 kb的染色体内片段之间的相互作用，而30％的reads表示间隔大于20 kb的染色体内的相互作用。这种分布可以作为质量控制的一种形式。</p>
<h4>Q5: Hi-C数据的分析流程是什么？</h4>
<p>参考：<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fwww.biotrainee.com%2Fthread-1551-1-1.html" target="_blank">生信技能树：3D基因组之Hi-C数据分析(大全)</a>， <a href="https://links.jianshu.com/go?to=%255Bhttps%3A%2F%2Fwww.jianshu.com%2Fp%2F94cd5a8e829e%255D%28https%3A%2F%2Fwww.jianshu.com%2Fp%2F94cd5a8e829e%29" target="_blank">三维基因组学研究之Hi-C</a></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="551" data-height="706"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-e7caacf8b7b23a33.png" data-original-width="551" data-original-height="706" data-original-format="image/png" data-original-filesize="278328" src="https://upload-images.jianshu.io/upload_images/18922188-e7caacf8b7b23a33.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>（1）数据过滤。<br>
（2）比对：比对的方式主要分两种，一种判断每条reads是否含有酶切位点，有则去掉酶切位点之后的数据在进行bowtie2单端比对；另一种采用单端比对的策略，以25bp为起始长度，每次增加5bp直到该reads比对到基因组具有唯一性。<br>
（3）寻找酶切片段；比对寻找到reads pairs在基因组物理位置之后，通过插入片段大小的限制搜索reads pairs两端每条read所对应的最近的酶切片段。酶切片段的位置代表了DNA交互产生的大致位置。<br>
（4）筛选fragment pairs<br>
（5）HiC分析：只需要Valid Pairs<br>
Binning：将Valid Pairs的交互信息mapping到基因组的位置，最终转换成为每两个bin的交互强度。<br>
（6）交互矩阵标准化；标准化方法主要分为两类，一类是基于矩阵，进行数学上的标准化，例如迭代等，另一类是基于生物学意义（例如mappingability）上的标准化。<br>
（7）可视化</p>
<h4>Q6: Hi-C测序的结果图怎么看？</h4>
<p>A: 染色质相互作用可以用热图表示，其中x轴和y轴代表基因组顺序的基因座。通常来说，线性基因组中非常接近的DNA片段将倾向于相互频繁交互。所以在热图中可以看到对角线的相互作用很高（下图）。下图展示的是14号染色体内的基因座相互作用：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="363" data-height="407"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-818e862dce0306b0.png" data-original-width="363" data-original-height="407" data-original-format="image/png" data-original-filesize="230622" src="https://upload-images.jianshu.io/upload_images/18922188-818e862dce0306b0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>上面图A对应于14号染色体上染色体内相互作用的热图。每个像素代表1-Mb位点和另一个1-Mb位点之间的所有相互作用。红色密度对应于reads的数量。刻度线每个刻度10 Mb。使用Hi-C数据集计算给定基因组内一对基因座(loci)的平均接触概率，产生一个期望矩阵（B）。matrix A和B两个矩阵的商是观察/期望的矩阵（C），其中富集显示为红色。块模式变得更加明显。Person相关矩阵（D）说明了14染色体的每对基因座的相互作用相关性。</p>
<p>你还可以看染色体之间的相互作用：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="600" data-height="261"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-5e79d8fa3da6c297.png" data-original-width="600" data-original-height="261" data-original-format="image/png" data-original-filesize="145845" src="https://upload-images.jianshu.io/upload_images/18922188-5e79d8fa3da6c297.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>上图A中，相互作用的概率随着染色体1上基因距离的变化而降低，最终在90Mb达到平稳（蓝色线）。不同染色体间相互作用的水平对于不同的染色体对是不同的。1号染色体上的基因座最有可能与10号染色体上的基因座（绿色）相互作用，最不可能与21号染色体上的基因座（红色）相互作用。相对于染色体内相互作用，染色体间的相互作用被消除了。图B里所有染色体之间的观察/预期热图。红色表示富集。一般富含基因的小染色体往往存在更多的相互作用。</p>
<h4>Q7: TAD图怎么看？</h4>
<p>我在实验室人的汇报里看到类似如下的图：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1048" data-height="189"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-caf71b396eea5e39.png" data-original-width="1048" data-original-height="189" data-original-format="image/png" data-original-filesize="173288" src="https://upload-images.jianshu.io/upload_images/18922188-caf71b396eea5e39.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>参考：<a href="https://links.jianshu.com/go?to=%255Bhttps%3A%2F%2Fwww.jianshu.com%2Fp%2F7c6189280234%255D%28https%3A%2F%2Fwww.jianshu.com%2Fp%2F7c6189280234%29" target="_blank">TAD:拓扑关联结构域简介</a><br>
这其实是染色质相互作用图里对角线一侧的数据。这种重复出现的（红色三角）内部互作频率高，组间互作频率低的domain，称为topologically assocaited domain, 简称TAD。这个图怎么理解呢，我发现了<code>生信修炼手册</code>公众号里的一张图片，非常简单易懂：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="591" data-height="486"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-bcfa3a0cba9788b2.png" data-original-width="591" data-original-height="486" data-original-format="image/png" data-original-filesize="221096" src="https://upload-images.jianshu.io/upload_images/18922188-bcfa3a0cba9788b2.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>两个大红三角的中间被称为：TAD边界。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="536" data-height="234"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-2761b84fd058dc5d.png" data-original-width="536" data-original-height="234" data-original-format="image/png" data-original-filesize="134040" src="https://upload-images.jianshu.io/upload_images/18922188-2761b84fd058dc5d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>那么如何识别染色质中的TAD,这里有一个名词：DI，方向性指数。用于量化基因组区域的上游或下游相互作用偏差的程度，发现在TAD边界区的偏差很大。（参考：<a href="https://links.jianshu.com/go?to=%255Bhttps%3A%2F%2Fwww.jianshu.com%2Fp%2Fbc2c87fa449a%255D%28https%3A%2F%2Fwww.jianshu.com%2Fp%2Fbc2c87fa449a%29" target="_blank">3D基因组入门笔记</a>）</p>
<p>TAD与Chip-Seq结果一起看（图片来自：<a href="https://www.jianshu.com/u/e235caa4ff16" target="_blank">3D基因组入门笔记</a>）：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="923" data-height="580"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-ed6ba89bfeceddfa.png" data-original-width="923" data-original-height="580" data-original-format="image/png" data-original-filesize="595719" src="https://upload-images.jianshu.io/upload_images/18922188-ed6ba89bfeceddfa.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>TAD图和Chip-seq一起看，可以看在TAD边界处或内部，不同的protein或者染色质修饰mark的结合情况。比如上面这个图，CTCF可以帮助染色体折叠，那么它结合的地方，显然是很难与其他地方相互作用的，所以与绝缘子相关。</p>
  
</div>
            