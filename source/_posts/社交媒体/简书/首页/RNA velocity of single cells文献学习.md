
---
title: 'RNA velocity of single cells文献学习'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/18922188-66cc3b7db1831b75.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/18922188-66cc3b7db1831b75.png'
---

<div>   
<p>在之前的一个视频学习系列笔记里，有一篇笔记提到了RNA velocity（<a href="https://www.jianshu.com/p/adb692e71bf9" target="_blank">Single cell RNA-seq data analysis with R视频学习笔记（八）</a>），但当时没有仔细的去对RNA velocity进行详细的了解。这篇文献学习笔记就是对这个模型进行更详细的了解。</p>
<p>文献：RNA velocity of single cells<br>
发表于2018年，Nature。<br>
如果想下载这篇文献，而又没Nature官网权限的童鞋可以在这里下载：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FYanFang0620%2Fshared-paper%2Fblob%2Fmaster%2FRNA%2520velocity%2520of%2520single%2520cells.pdf" target="_blank">here</a></p>
<p>（笔记里很多补充图没有放上来，想看的可以从上面链接下载文章看）</p>
<p>【摘要】<br>
RNA丰度是单个细胞状态的一个强大的指标。单细胞RNA测序可以精确的、高通量的揭示RNA丰度。然而，这种方法只能捕捉某一个时间点的“快照”（snapshot），对于分析胚胎形成或者组织重建的这种需要观测连续时间的“事件”就比较困难了。这里我们提出了“RNA velocity”（RNA速度），可以直接测定在单细胞测序结果中的“未成熟”mRNA和“成熟”mRNA。RNA velocity是一个高维度载体，可以预测单个细胞在时间轴上的“未来的”几个小时的状态。我们利用神经嵴系验证了RNA velocity的精确度，证明了它可以用在多种测序平台上，利用它揭示了发育中的小鼠海马体的分支谱系树，并测定了人类脑胚胎的转录动力学。</p>
<p>【正文】<br>
在发育过程中，分化过程发生在时间轴上的几小时到数天不等。而未成熟的mRNA（unspliced）和成熟的mRNA（spliced）的相对丰度可以评估基因剪切和降解的速率。我们推断这种信号可以在单细胞测序数据中被检测到，从而可以揭示在动态的过程中，整个转录的速率和变化。</p>
<p>所有的单细胞RNA测序方法都是依赖于oligo-dT引物，通过富集带有polyA的mRNA分子来得到测序材料。尽管如此，现有的测序平台（SMART-seq2, STRT/<br>
C1, inDrop and 10x Genomics）的测序结果中，都含有15-25%的reads包含未成熟带有内含子的序列（图1a）。在常规bulk RNA-seq里含有14.6%的未成熟mRNA reads，单细胞测序中含有20%的未成熟mRNA reads。在10x Genomics文库里，这一类mRNA的reads主要是由于PCR扩增时候产生的。</p>
<p>为了量化时间依赖的mRNA前提和成熟的mRNA，我们给转录动力学假定了一个简单的模型，成熟的mRNA丰度由未成熟mRNA产生的spliced mRNA和降解的速度来决定（图1b）。在这个动态的过程中，转录速率a上升，导致了unspliced的mRNA增加，从而导致成熟的mRNA的增多（图1c），直到一个新的稳定状态。反之亦然。在基因表达的诱导过程里，未成熟的mRNA的存在超出了预期（图1d）。这两种mRNA的平衡是在未来状态里成熟mRNA丰度的一个重要指标，也是意味着决定了细胞未来的状态。</p>
<p>为了证明这个模型可以用来推断在“未来时间里”成熟的mRNA丰度，我们用bulk-RNA-seq方法检测了小鼠肝脏的日周期的一个时间过程。未成熟的mRNA水平在每一个时间点都与随后一个时间点上成熟的mRNA水平相似（图1e），许多与节律相关的基因也展示出了unspliced mRNA的上调的趋势（图1f,g）。这一模型可以让我们在每一个周期里进行测定，准确捕捉昼夜节律周期发展的预期方向(图1h)。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1519" data-height="701"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-66cc3b7db1831b75.png" data-original-width="1519" data-original-height="701" data-original-format="image/png" data-original-filesize="362379" src="https://upload-images.jianshu.io/upload_images/18922188-66cc3b7db1831b75.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">图1</div>
</div>
<p>接下来，为了证明在单细胞水平上，这个模型也可以预测转录动力学，我们分析了近期发表的老鼠嗜铬细胞的数据，是SMARTseq2平台测序的（图2a）。在发育过程中，相当比例的嗜铬细胞（即肾上腺髓质的神经内分泌细胞）源自Schwann细胞前体，为我们的模型提供了一个简单的测试，并可以通过谱系跟踪来验证。图2b和c里绿色/灰色的图代表着基因的表达情况，绿色代表表达水平高；而红色/蓝色图则表达未成熟mRNA和成熟mRNA，说明Serpin2这个基因是处在一个被抑制的状态，而Chga基因处于被激活的状态。RNA速度对单个细胞进行评估，准确地再现了该数据的转录动力学，包括细胞的分化，比如细胞向嗜铬细胞方向发展(图2d)。RNA速度还捕获了嗜铬的细胞-周期动力学，包括PCA分析和细胞周期相关基因的分析。</p>
<p>有很多的技术可以对velocity在低维里进行可视化。细胞状态的推测可以嵌入一个低维空间里（比如PCA，图2d）或者tSNE（图2h）。在一个很大的数据集了，RNA velocity更容易被可视化（图Fig. 2i）。因为细胞可以同时拥有多个独立的RNA velocity存在，比如分化、成熟和增殖。</p>
<p>细胞特异性的RNA velocity评估提供了一个自然的基础对细胞命运进行定量建模。有效的可推测的时间轴，取决于你要研究的生物过程。比如用EdU标记的嗜铬祖细胞，我们可以推测的“未来”时间是2.5-3.8小时（图Fig. 2f, g）。由于这种推测是线性的，所以推测时间轴也依赖于基因表达轨迹的形状。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="915" data-height="892"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-5469ef8602658c1f.png" data-original-width="915" data-original-height="892" data-original-format="image/png" data-original-filesize="561343" src="https://upload-images.jianshu.io/upload_images/18922188-5469ef8602658c1f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">图2</div>
</div>
<p>我们接着利用RNA velocity对小鼠的海马体的风雨谱系的分支进行分析。去除血管、免疫细胞、GABAergic 和卡哈尔Retzius神经元后，t-SNE图揭示了一个复杂的分支（图3a）。我们使用已知的标记基因鉴定了星形细胞、少突细胞前体 (OPCs)、齿状回颗粒神经元和锥体神经元五个细胞群：the subiculum, CA1, CA2, CA3，hilus。单个基因的相位图展示了特异的基因表达的诱导和抑制（图3b）。采用马尔可夫速度随机游走模型可以自动识别分支的终端和root(图3c)，展示了RNA速度可以在没有已知的发育过程的前提下，确定谱系的方向。</p>
<p>在微观层面上，“命运”选择是一个倾向于非决定性过程，这个过程涉及到基因的表达，一旦转录因子的反馈loop建立后，细胞的“命运”便被“锁定”了。比较一个pre-OPC群里的细胞和一个处于过度期（narrow passage）的细胞的未来状态的可能性分布，显然后者更可能成为一个OPC细胞（图 3d）。在图3e里，单细胞分支谱系里，如果一个细胞的Prox1基因被激活，那么变形成granule神经元，如果Prox1基因被抑制，那么细胞会分化成neuroblasts。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1768" data-height="822"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-97344686a7478dbc.png" data-original-width="1768" data-original-height="822" data-original-format="image/png" data-original-filesize="1175197" src="https://upload-images.jianshu.io/upload_images/18922188-97344686a7478dbc.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">图3</div>
</div>
<p>为了证明RNA速度可以在人体胚胎内被检测到，我们进行了基于液滴的单细胞RNA-seq的实验，分析了在怀孕十周后人类前脑的发育过程，主要研究谷氨酸能神经元谱系(图4a)。我们发现由增殖的前体细胞状态(radial glia)通过一系列中间成神经细胞的状态向更成熟的分化的谷氨酸能神经元（表达SLC17A7）产生了一个很强的velocity模式。我们利用多重原位杂交实验，验证了皮质神经元发育的已知和新的标记物，(图4b, c)。这些在组织中分层的基因(图4c)与单细胞RNA-seq数据中基因的伪时间分布密切相关（图4b）。</p>
<p>我们利用PCA来把细胞根据分化的“拟时间”进行排序，确定了未成熟mRNA始终先出现于成熟的mRNA（图4d）。从4d里还可以看到不同的动力学特征。比如RNASEH2B基因属于fast动力学，因为它的unspliced和spliced RNA差不多。相反的，DCX，ELAVL4 和STMN2基因在刚开始有一个快速的转录，随后的转录速度下降（蓝色线下降），成熟的mRNA有一个明显的滞后轨迹。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="628" data-height="962"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-249fc0895cd6fa7c.png" data-original-width="628" data-original-height="962" data-original-format="image/png" data-original-filesize="515517" src="https://upload-images.jianshu.io/upload_images/18922188-249fc0895cd6fa7c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">图4</div>
</div>
<p>由于RNA速度是基于真实的转录动力学，这方法有望为我们的研究带来更坚实的定量基础，帮助我们了解细胞在基因表达空间中的动态分化。RNA速度已经可以用来进行详细的对整个有机体的动态过程的研究，为谱系分析提供很大的便利，特别是在人类胚胎中。</p>
  
</div>
            