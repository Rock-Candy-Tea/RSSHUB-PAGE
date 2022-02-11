
---
title: '学习一遍ChIPseeker的使用'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/9376801-86e2329c6f71cf39.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/9376801-86e2329c6f71cf39.png'
---

<div>   
<blockquote>
<p>刘小泽写于2020.5.23-24<br>
Y叔的原文在：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F3CMj0xejiV-FSMC-Vxd_-w" target="_blank">https://mp.weixin.qq.com/s/3CMj0xejiV-FSMC-Vxd_-w</a></p>
</blockquote>
<h3>0 ChIPseeker的诞生</h3>
<p>Y叔一开始使用<code>ChIPpeakAnno</code>进行注释，但使用UCSC genome browser检验结果的时候，发现对不上；另外之前在使用<code>ChIPpeakAnno</code>过程中写了一些可视化函数。后来经过漫长的半夜宿舍苦战，写出了ChIPseeker</p>
<h3>1 ChIP-seq简介</h3>
<p>ChIP是指染色质免疫沉淀，它通特异结合抗体将DNA结合蛋白免疫沉淀，可以用于捕获蛋白质（如转录因子，组蛋白修饰）的DNA靶点。之前结合芯片就有ChIP-on-chip，后来二代测序加持诞生了ChIP-seq。优点是：不再需要设计探针（探针往往存在着一定的偏向性）</p>
<p>2007年来自三个不同的实验室，几乎是同时间出来（最长差不了3个月），分别发CNS，一起定义了这个<code>ChIPseq</code>技术</p>
<ul>
<li>Johnson DS, Mortazavi A et al. (2007) Genome-wide mapping of in vivo protein–DNA interactions. Science 316: 1497–1502</li>
<li>Robertson G et al.(2007) Genome-wide profiles of STAT1 DNA association using chromatin immunoprecipitation and massively parallel sequencing. Nature Methods 4: 651–657</li>
<li>Schmid et al. (2007) ChIP-Seq Data reveal nucleosome architecture of human promoters. Cell 131: 831–832</li>
</ul>
<p><strong>主要有4步</strong>：Cross-linking、Sonication、IP、Sequencing</p>
<p><strong>简而言之是</strong>：DNA和蛋白质交联(cross-linking)、超声(sonication)将染色体随机切割、利用抗原抗体的特异性识别(IP)、把<strong>目标蛋白</strong>相结合的DNA片段沉淀下来，反交联释放DNA片段，最后是测序(sequencing)</p>
<h5>分析流程示例图1：</h5>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="951" data-height="724"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-86e2329c6f71cf39.png" data-original-width="951" data-original-height="724" data-original-format="image/png" data-original-filesize="103323" src="https://upload-images.jianshu.io/upload_images/9376801-86e2329c6f71cf39.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">Peak calling with MACS2</div>
</div>
<h5>分析流程示例图2：</h5>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1462" data-height="1028"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-fc0c4ea9dfa9d447.png" data-original-width="1462" data-original-height="1028" data-original-format="image/png" data-original-filesize="414911" src="https://upload-images.jianshu.io/upload_images/9376801-fc0c4ea9dfa9d447.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image-20200523211551406</div>
</div>
<p>原始数据=》质控=》比对=》拿到DNA片段在染色体上的位置信息=》peak calling （去除背景噪音）=》拿到peaks（protein binding site）=》下游分析（可视化、找相关基因、motif分析等等）</p>
<h3>2 必须知晓的BED文件</h3>
<p>全称是：Browser Extensible Data，为基因组浏览器而生</p>
<p>包括3个必须字段和9个可选字段：</p>
<h5>3个必须</h5>
<ul>
<li>1 chrom - 染色体名字</li>
<li>2 chromStart - 染色体起始位点（起始于0，而不是1）许多软件忽略了这一点，存在一个碱基的位移（如peakAnalyzer, ChIPpeakAnno存在这个问题），Homer、ChIPseeker没有</li>
<li>3 chromEnd - 染色体终止位点</li>
</ul>
<h5>9个可选</h5>
<ul>
<li>4 name - 名字</li>
<li>5 score - 分值(0-1000), 用于genome browser展示时上色。</li>
<li>6 strand - 正负链，对于ChIPseq数据来说，<strong>一般</strong>没有正负链信息。</li>
<li>7 thickStart - 画矩形的起点</li>
<li>8 thickEnd - 画矩形的终点</li>
<li>9 itemRgb - RGB值</li>
<li>10 blockCount - 子元件（比如外显子）的数目</li>
<li>11 blockSizes - 子元件的大小</li>
<li>12 blockStarts - 子元件的起始位点</li>
</ul>
<p>一般只用前5个足矣（MACS的输出结果也是前5个字段）</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1234" data-height="338"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-3b9247dadd7444ef.png" data-original-width="1234" data-original-height="338" data-original-format="image/png" data-original-filesize="103747" src="https://upload-images.jianshu.io/upload_images/9376801-3b9247dadd7444ef.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>第5列score的含义是：the summit height of fragment pileup. 也即是片段堆积的峰高</p>
<h3>3 使用<code>covplot</code>可视化BED数据</h3>
<blockquote>
<p>一般拿到数据后，会先可视化一下数据的全景</p>
</blockquote>
<pre><code class="R"># 自带示例数据（这也是Bioconductor包的一个特点，提交R包需要有说明书和测试数据）
library(ChIPseeker)
library(ggplot2)

files <- getSampleFiles()
# 有5个文件
> basename(unlist(files))
[1] "GSM1174480_ARmo_0M_peaks.bed.gz"                   
[2] "GSM1174481_ARmo_1nM_peaks.bed.gz"                  
[3] "GSM1174482_ARmo_100nM_peaks.bed.gz"                
[4] "GSM1295076_CBX6_BF_ChipSeq_mergedReps_peaks.bed.gz"
[5] "GSM1295077_CBX7_BF_ChipSeq_mergedReps_peaks.bed.gz"

covplot(files[[5]])
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1516" data-height="1086"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-513e2fd3fbc88c5d.png" data-original-width="1516" data-original-height="1086" data-original-format="image/png" data-original-filesize="201781" src="https://upload-images.jianshu.io/upload_images/9376801-513e2fd3fbc88c5d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h4>还支持多个文件同时画</h4>
<p><strong>只要转为GRanges对象即可</strong></p>
<pre><code class="R"># 比如要画第4、5个文件（MACS生成的BED文件包含常规的5列）
peak=GenomicRanges::GRangesList(CBX6=readPeakFile(files[[4]]),CBX7=readPeakFile(files[[5]]))
</code></pre>
<p>画图</p>
<pre><code class="R">covplot(peak, weightCol="V5") + facet_grid(chr ~ .id)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1528" data-height="1086"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-a25c4221fd01a4a6.png" data-original-width="1528" data-original-height="1086" data-original-format="image/png" data-original-filesize="232639" src="https://upload-images.jianshu.io/upload_images/9376801-a25c4221fd01a4a6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p><strong>取小区间</strong>，例如只取几条染色体，还能定义染色体的区间大学</p>
<pre><code class="R">covplot(peak, weightCol="V5", chrs=c("chr17", "chr18"), 
        xlim=c(4e7, 5e7)) + facet_grid(chr ~ .id)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1502" data-height="1092"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-0e6ffa1b4c3fa8e8.png" data-original-width="1502" data-original-height="1092" data-original-format="image/png" data-original-filesize="80106" src="https://upload-images.jianshu.io/upload_images/9376801-0e6ffa1b4c3fa8e8.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<blockquote>
<p>在看完数据全景之后，就会想知道这些peaks和什么类型的基因有关</p>
</blockquote>
<h3>4 annotatePeak进行peaks的注释</h3>
<p>需要使用BED文件（作为query）+注释文件（作为target）</p>
<h4>重点是如何获取注释文件</h4>
<p>注释信息一般要包含基因的起始终止，基因的外显子、内含子及它们的起始终止、非编码区域位置、功能元件的位置等</p>
<p>ChIPseeker没有物种限制，但<strong>前提是物种本身有这些注释信息</strong>（不能说物种连参考基因组也没有，那就真的是巧妇难为无米之炊）</p>
<p>需要一个TxDb对象，例如<code>TxDb.Hsapiens.UCSC.hg19.knownGene</code>，然后ChIPseeker就会从中提取信息</p>
<pre><code class="R"># 三步走（提供TxDb注释、提供bed文件、进行注释）
require(TxDb.Hsapiens.UCSC.hg19.knownGene)
txdb = TxDb.Hsapiens.UCSC.hg19.knownGene
f = getSampleFiles()[[4]]
x = annotatePeak(f, tssRegion=c(-1000, 1000), TxDb=txdb)
</code></pre>
<p>看到这里有个参数<code>tssRegion</code> ，它指定了启动子区域（而启动子区域是没有明确定义的，需要自己指定，这里指定了上下游1kb）</p>
<h4>看一下大体结果：</h4>
<pre><code class="R">> x
Annotated peaks generated by ChIPseeker
1331/1331  peaks were annotated
Genomic Annotation Summary:
             Feature  Frequency
9           Promoter 48.1592787
4             5' UTR  0.7513148
3             3' UTR  4.2073629
1           1st Exon  0.7513148
7         Other Exon  3.9068370
2         1st Intron  6.5364388
8       Other Intron  4.8835462
6 Downstream (<=300)  1.1269722
5  Distal Intergenic 29.6769346
</code></pre>
<h4>看一下详细结果：</h4>
<pre><code class="R">as.GRanges(x) %>% head(3)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="3302" data-height="410"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-a9737cecfc01e85e.png" data-original-width="3302" data-original-height="410" data-original-format="image/png" data-original-filesize="199544" src="https://upload-images.jianshu.io/upload_images/9376801-a9737cecfc01e85e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h4>可以转为数据框，方便输出：</h4>
<pre><code class="R">tmp=as.data.frame(x)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1786" data-height="384"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-94d6094aa228eba1.png" data-original-width="1786" data-original-height="384" data-original-format="image/png" data-original-filesize="110615" src="https://upload-images.jianshu.io/upload_images/9376801-94d6094aa228eba1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h4>关于注释的类型：</h4>
<h5>注释类型一：genomic annotation（annotation这一列）</h5>
<p>指peak在基因组的位置：落在什么地方，例如外显子、内含子或是UTR</p>
<h5>注释类型二：nearest gene annotation（annotation后面的列）</h5>
<p>指peak最近的基因：不管peak落在内含子、基因间区还是其他位置，按照peak相对于转录起始位点的距离，都能找到一个离它最近的基因【一般做基因表达调控的，会关注promoter区域，离结合位点最近的基因更可能被调控】</p>
<blockquote>
<p>这个距离是根据转录起始位点来计算，一个基因具有多个转录本，因此一个基因可能有多个转录起始位点。注释的结果就会看到有一列是转录本ID</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1412" data-height="266"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-3d4bf6bd496edf68.png" data-original-width="1412" data-original-height="266" data-original-format="image/png" data-original-filesize="62001" src="https://upload-images.jianshu.io/upload_images/9376801-3d4bf6bd496edf68.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>注释类型三：flankDistance（三列: flank_txIds, flank_geneIds和flank_gene_distances）</h5>
<p>指peak上下游某个范围内（比如-5kb《=》5kb范围内）都有什么基因</p>
<pre><code class="R"># 传个参数flankDistance
x2 = annotatePeak(f, tssRegion=c(-1000, 1000), TxDb=txdb, addFlankGeneInfo=TRUE, flankDistance=5000)
</code></pre>
<h4>让基因名变得友好</h4>
<p>上面得到的结果都是以geneId（Entrez ID）给出，如果想要Symbol名称，可以再传参数<code>annoDb</code></p>
<pre><code class="R">library(org.Hs.eg.db)
x3 = annotatePeak(f, tssRegion=c(-1000, 1000), TxDb=txdb, 
                  addFlankGeneInfo=TRUE, flankDistance=5000,
                  annoDb = "org.Hs.eg.db")
tmp3=as.data.frame(x3)
</code></pre>
<p>会再增加3列：ENSEMBL、SYMBOL、GENENAME（如果这里使用的TxDb是Ensemble ID，那么结果就会是Entrez ID、SYMBOL、GENENAME三列）</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2210" data-height="384"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-d43d6aeacc1edaea.png" data-original-width="2210" data-original-height="384" data-original-format="image/png" data-original-filesize="161644" src="https://upload-images.jianshu.io/upload_images/9376801-d43d6aeacc1edaea.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h4>按正负链分开注释</h4>
<p>一般ChIPseq数据通常情况下是没有正负链信息的（有特殊的实验可以有）</p>
<p>但如果要做，可以先给peaks分别赋予正负链的信息，然后指定参数<code>sameStrand=TRUE</code> 并分别做两次</p>
<p>这个参数的意思是：（logical）whether find nearest/overlap gene in the same strand</p>
<h4>只注释基因的上游或下游</h4>
<p>提供了<code>ignoreDownstream</code>和 <code>ignoreUpstream</code>，默认是FALSE</p>
<h4>关于TxDb的知识</h4>
<p>上面一起操作的前提是物种本身有这些注释信息，而注释信息主要是用TxDb</p>
<h5>同一物种的不同版本TxDb</h5>
<p>例如<code>TxDb.Hsapiens.UCSC.hg19.knownGene</code>和<code>TxDb.Hsapiens.UCSC.hg38.knownGene</code> 的注释结果是不同的，不能混用。用哪个取决于上游分析比对使用的哪个版本的基因组</p>
<p>不同的版本中基因坐标是不一样的，如果硬要替换，可以使用<code>liftOver</code>将基因组版本坐标进行转换</p>
<h5>支持多少物种？</h5>
<p>Bioconductor上有30个左右TxDb，也只能覆盖一小部分物种（<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fbioconductor.org%2Fpackages%2F3.11%2Fdata%2Fannotation%2F" target="_blank">https://bioconductor.org/packages/3.11/data/annotation/</a>），但UCSC和Ensemble的基因组都可以被ChIPseeker支持，因此所有物种都支持</p>
<h5>除了基因注释还能注释lincRNA</h5>
<p>比如就可以利用：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fbioconductor.org%2Fpackages%2F3.11%2Fdata%2Fannotation%2Fhtml%2FTxDb.Hsapiens.UCSC.hg19.lincRNAsTranscripts.html" target="_blank">https://bioconductor.org/packages/3.11/data/annotation/html/TxDb.Hsapiens.UCSC.hg19.lincRNAsTranscripts.html</a></p>
<pre><code class="R">require("TxDb.Hsapiens.UCSC.hg19.lincRNAsTranscripts")
linc_txdb=TxDb.Hsapiens.UCSC.hg19.lincRNAsTranscripts
x=annotatePeak(peak, TxDb=linc_txdb)
as.GRanges(x)
</code></pre>
<h5>如何自己制作TxDb？</h5>
<p>使用<code>GenomicFeatures</code>包来制作TxDb对象</p>
<ul>
<li>makeTxDbFromUCSC： 通过UCSC在线制作TxDb</li>
<li>makeTxDbFromBiomart: 通过ensembl在线制作TxDb</li>
<li>makeTxDbFromGRanges：通过GRanges对象制作TxDb</li>
<li>makeTxDbFromGFF：通过解析GFF文件制作TxDb</li>
</ul>
<blockquote>
<p><strong>比如在线从UCSC生成TxDb：</strong></p>
</blockquote>
<pre><code class="R">require(GenomicFeatures)
# makeTxDbFromUCSC()函数依赖RMariaDB这个包
# BiocManager::install('RMariaDB')
hg19.refseq.db <- makeTxDbFromUCSC(genome="hg19", table="refGene")
# 可能会遇到一个报错：namespace ‘DBI’ 1.0.0 is already loaded, but >= 1.1.0 is required =>自己升级
# remove.packages("DBI", lib="~/Library/R/3.6/library")
# packageurl <- "https://cran.r-project.org/src/contrib/DBI_1.1.0.tar.gz"
# install.packages(packageurl, repos=NULL, type="source")
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1946" data-height="1014"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-5445ec3031425890.png" data-original-width="1946" data-original-height="1014" data-original-format="image/png" data-original-filesize="337175" src="https://upload-images.jianshu.io/upload_images/9376801-5445ec3031425890.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>然后可以对比一下：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2346" data-height="1013"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-572ac5a621d7886b.png" data-original-width="2346" data-original-height="1013" data-original-format="image/png" data-original-filesize="583755" src="https://upload-images.jianshu.io/upload_images/9376801-572ac5a621d7886b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<blockquote>
<p><strong>再比如自己下载GTF然后生成TxDb</strong><br>
以大豆（glycine_max）为例</p>
</blockquote>
<pre><code class="R"># 下载
download.file('ftp://ftp.ensemblgenomes.org/pub/plants/release-47/gff3/glycine_max/Glycine_max.Glycine_max_v2.1.47.chr.gff3.gz',destfile = 'Glycine_max_v2.1.47.chr.gff3.gz')
# 解压
R.utils::gunzip('Glycine_max_v2.1.47.chr.gff3.gz')
# 制作
glycine <- makeTxDbFromGFF("Glycine_max_v2.1.47.chr.gff3")
</code></pre>
<h5>有了TxDb怎么查看呢？</h5>
<blockquote>
<p>最详细的操作在官方文档：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fbioconductor.org%2Fpackages%2Frelease%2Fbioc%2Fvignettes%2FGenomicFeatures%2Finst%2Fdoc%2FGenomicFeatures.pdf" target="_blank">https://bioconductor.org/packages/release/bioc/vignettes/GenomicFeatures/inst/doc/GenomicFeatures.pdf</a></p>
</blockquote>
<p>不管是从Bioconductor下载的还是自己制作的，都是一个GenomicFeatures对象</p>
<p>如果简单对名称操作，会返回这个注释文件的基本信息。要把TxDb当成一个数据库来对待，而不是一个简单的数据框或者矩阵。因此它的提取方法也会比较特别</p>
<ul>
<li><p>如果想看其中包含的类目，可以用<code>columns(txdb)</code></p></li>
<li><p>如果想指定提取转录本或外显子信息，可以：<code>transcripts(txdb) 或者 exons(txdb)</code></p></li>
<li><p>如果想看全部的信息，可以：<code>AnnotationDbi::select(glycine, columns=columns(glycine), keys=keys(glycine), keytype=c("GENEID"))</code></p></li>
</ul>
<p>需要注意，如果使用这个<code>select</code>的时候，同时加载了<code>tidyverse</code>，那么同名的<code>select</code>就会发生冲突导致报错，这时可以用显式指定的形式来规范（如下图）</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2186" data-height="468"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-837697767da4a68f.png" data-original-width="2186" data-original-height="468" data-original-format="image/png" data-original-filesize="211328" src="https://upload-images.jianshu.io/upload_images/9376801-837697767da4a68f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>可视化</h3>
<h4>peak在整个染色体的分布</h4>
<p>见：第3部分=》 使用<code>covplot</code>可视化BED数据</p>
<h4>peak在某个窗口的结合谱图</h4>
<blockquote>
<p>一般有两种方式：一是直接使用BED文件，二是一步步手动进行</p>
</blockquote>
<h5>第一种：直接使用BED文件</h5>
<pre><code class="R">peakHeatmap(f, weightCol="V5", TxDb=txdb, 
            upstream=3000, downstream=3000, 
            color=rainbow(length(f)))
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1740" data-height="994"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-c608294b07770404.png" data-original-width="1740" data-original-height="994" data-original-format="image/png" data-original-filesize="153060" src="https://upload-images.jianshu.io/upload_images/9376801-c608294b07770404.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>其实看运行日志也能看出来做了什么，首先根据转录起始位点指定上下游（也就是热图的窗口区间范围），然后把peaks比对到这个窗口，并生成矩阵以进行可视化</p>
<p>稍微查看一下这个<code>peakHeatmap</code>函数，就会发现以上说的几步：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1192" data-height="1526"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-c02c4abd08bfd42d.png" data-original-width="1192" data-original-height="1526" data-original-format="image/png" data-original-filesize="461131" src="https://upload-images.jianshu.io/upload_images/9376801-c02c4abd08bfd42d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>当然，如果是多个文件也是可以的</p>
<pre><code class="R">files=getSampleFiles()
peakHeatmap(files, TxDb=txdb, 
            upstream=3000, downstream=3000, 
            color=rainbow(length(files)))
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1644" data-height="1026"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-889481bf7793d278.png" data-original-width="1644" data-original-height="1026" data-original-format="image/png" data-original-filesize="77346" src="https://upload-images.jianshu.io/upload_images/9376801-889481bf7793d278.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>第二种：一步步手动进行</h5>
<p>如果说第一种提供了一个打包好的计算过程，那么第二种就是把第一种拆分运行</p>
<pre><code class="R">promoter <- getPromoters(TxDb=txdb, 
                  upstream=3000, downstream=3000)
tagMatrix <- getTagMatrix(f, 
                          windows=promoter)
tagHeatmap(tagMatrix, xlim=c(-3000, 3000), 
           color="red")
</code></pre>
<h4>看看结合的强度</h4>
<h5>第一种：直接使用BED文件</h5>
<pre><code class="R">plotAvgProf2(files[[4]], TxDb=txdb, 
             upstream=3000, downstream=3000,
             xlab="Genomic Region (5'->3')", 
             ylab = "Read Count Frequency",
             conf = 0.95, resample = 1000)# 添加置信区间
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1698" data-height="1084"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-27db18b83725e678.png" data-original-width="1698" data-original-height="1084" data-original-format="image/png" data-original-filesize="150905" src="https://upload-images.jianshu.io/upload_images/9376801-27db18b83725e678.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>第二种：手动进行</h5>
<p>使用上面的tagMatrix计算结果</p>
<pre><code class="R">plotAvgProf(tagMatrix, xlim=c(-3000, 3000),
            xlab="Genomic Region (5'->3')", 
            ylab = "Read Count Frequency")
</code></pre>
<h5>支持多个数据比较</h5>
<pre><code class="R">tagMatrixList <- lapply(files, getTagMatrix, 
                        windows=promoter)
# 添加置信区间并分面
plotAvgProf(tagMatrixList, xlim=c(-3000, 3000), 
            conf=0.95,resample=500, facet="row")
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1692" data-height="1090"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-8d14c1fe0ec41276.png" data-original-width="1692" data-original-height="1090" data-original-format="image/png" data-original-filesize="298580" src="https://upload-images.jianshu.io/upload_images/9376801-8d14c1fe0ec41276.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>这个结果和上面<code>peakHeatmap</code>的结果一致，前3个样本不是调控转录的</p>
<p>除了关注转录起始位点（研究转录调控），还能看蛋白与外显子/内含子起始位置的结合谱，使用<code>getBioRegion</code>函数，可以指定<code>'gene', 'transcript', 'exon', 'intron'</code></p>
<h4>注释结果之注释类型一：genomic annotation</h4>
<p>指peak在基因组的位置：落在什么地方，例如外显子、内含子或是5’ /3‘UTR</p>
<h5>饼图</h5>
<pre><code class="R">peakAnno <- annotatePeak(files[[4]], 
                         tssRegion=c(-3000, 3000),
                         TxDb=txdb, annoDb="org.Hs.eg.db")
plotAnnoPie(peakAnno)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1550" data-height="852"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-b9400aa6432c8a88.png" data-original-width="1550" data-original-height="852" data-original-format="image/png" data-original-filesize="186374" src="https://upload-images.jianshu.io/upload_images/9376801-b9400aa6432c8a88.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>柱状图</h5>
<pre><code class="R">plotAnnoBar(peakAnno)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1670" data-height="1096"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-8f2d719f9b4aab41.png" data-original-width="1670" data-original-height="1096" data-original-format="image/png" data-original-filesize="92921" src="https://upload-images.jianshu.io/upload_images/9376801-8f2d719f9b4aab41.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>注意第一个问题：关于上图中的各种Features分类</h5>
<p>看到这里的分类有下游（Downstream）但没有上游，这是因为Promoter定义为了转录起始位点（TSS）的上下游区域，包含了上游；另外这个下游是是基因间区的一部分，更确切是指紧接着基因的下游；这里的上游和下游其实都是基因间区，单独拿出来是因为和基因直接连接，是很近的区域=》近端基因间区</p>
<p>当然，基因间区还包含更远的间区（Distal intergenic）=》远端基因间区</p>
<p>默认下游的范围是3kb，但是可以自己调整</p>
<pre><code class="R"># 比如调成500
options(ChIPseeker.downstreamDistance = 500)
</code></pre>
<p>还有一个需求就是：自定义分类</p>
<pre><code class="R"># 依然是设置options，用于总结结果
f2=getSampleFiles()[[5]]
options(ChIPseeker.ignore_1st_exon = T)
options(ChIPseeker.ignore_1st_intron = T)
options(ChIPseeker.ignore_downstream = T)
options(ChIPseeker.ignore_promoter_subcategory = T)
x=annotatePeak(f2)
plotAnnoPie(x)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1420" data-height="854"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-84c9b4b9393409d5.png" data-original-width="1420" data-original-height="854" data-original-format="image/png" data-original-filesize="117431" src="https://upload-images.jianshu.io/upload_images/9376801-84c9b4b9393409d5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>注意第二个问题：peak的位置可能不是唯一的</h5>
<p>这是因为，一个peak所在的位置，可能是一个基因的外显子，同时又是另一个基因的内含子。为了解决这个问题，有以下几种方案：</p>
<ul>
<li>第一种：使用参数<code>genomicAnnotationPriority</code>指定优先顺序</li>
</ul>
<p>默认顺序是：Promoter => 5’ UTR => 3’ UTR => Exon => Intron => Downstream => Distal Intergenic</p>
<ul>
<li>第二种：饼图+韦恩图</li>
</ul>
<pre><code class="R">vennpie(peakAnno)
</code></pre>
<p>优点是：直观；缺点是：无法显示全部的信息</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="958" data-height="816"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-03ebc9deba952b96.png" data-original-width="958" data-original-height="816" data-original-format="image/png" data-original-filesize="77266" src="https://upload-images.jianshu.io/upload_images/9376801-03ebc9deba952b96.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>第三种：UpSetR +  vennpie</li>
</ul>
<pre><code class="R">upsetplot(peakAnno, vennpie=TRUE)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1670" data-height="1082"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-9097c6b03095c2f6.png" data-original-width="1670" data-original-height="1082" data-original-format="image/png" data-original-filesize="156639" src="https://upload-images.jianshu.io/upload_images/9376801-9097c6b03095c2f6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>多个文件的区域注释</h5>
<pre><code class="R">peakAnnoList <- lapply(files, annotatePeak, 
                       TxDb=txdb,tssRegion=c(-3000, 3000))
plotAnnoBar(peakAnnoList)

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1650" data-height="1076"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-80c08e711a8fd637.png" data-original-width="1650" data-original-height="1076" data-original-format="image/png" data-original-filesize="105823" src="https://upload-images.jianshu.io/upload_images/9376801-80c08e711a8fd637.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h4>注释结果之注释类型二：nearest gene annotation</h4>
<p>指peak最近的基因：不管peak落在内含子、基因间区还是其他位置，按照peak相对于转录起始位点的距离，都能找到一个<strong>离它最近的基因</strong></p>
<pre><code class="R">plotDistToTSS(peakAnno,
    title="Distribution of transcription factor-binding loci\nrelative to TSS")
</code></pre>
<h5>同样也支持多个文件</h5>
<pre><code class="R">plotDistToTSS(peakAnnoList)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1660" data-height="1090"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-29f06a8fb66d8d4d.png" data-original-width="1660" data-original-height="1090" data-original-format="image/png" data-original-filesize="95216" src="https://upload-images.jianshu.io/upload_images/9376801-29f06a8fb66d8d4d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>距离最近的基因在不同样本的交集</h5>
<pre><code class="R"># 先得到基因列表
genes <- lapply(peakAnnoList, function(i) 
    as.data.frame(i)$geneId)
> names(genes)
[1] "ARmo_0M"    "ARmo_1nM"   "ARmo_100nM" "CBX6_BF"    "CBX7_BF"  
                
# 然后作图(需要借助Vennerable包)
devtools::install_github("js229/Vennerable")
library(Vennerable)
vennplot(genes[2:4], by='Vennerable')
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="876" data-height="1046"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-6f6f2732af4e9042.png" data-original-width="876" data-original-height="1046" data-original-format="image/png" data-original-filesize="128427" src="https://upload-images.jianshu.io/upload_images/9376801-6f6f2732af4e9042.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>基因注释 + 富集分析</h3>
<p>利用ChIPseeker的<code>seq2gene</code> 将peak的位置与所有的基因关联起来【包括 host gene (exon/intron), promoter region and flanking gene from intergenomic region】，然后用clusterProfiler拿这些基因跑ORA，做富集</p>
<pre><code class="R">require(clusterProfiler)
bedfile=getSampleFiles()
# 将bed文件读入（readPeakFile是利用read.delim读取，然后转为GRanges对象）
seq=lapply(bedfile, readPeakFile)

genes=lapply(seq, function(i) 
    seq2gene(i, c(-1000, 3000), 3000, TxDb=txdb))
cc = compareCluster(geneClusters = genes, 
                    fun="enrichKEGG", organism="hsa")
dotplot(cc, showCategory=10)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2416" data-height="1848"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-1f4cca3bed72f6fe.png" data-original-width="2416" data-original-height="1848" data-original-format="image/png" data-original-filesize="303807" src="https://upload-images.jianshu.io/upload_images/9376801-1f4cca3bed72f6fe.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<p>欢迎关注我们的公众号～_～　　<br>
我们是两个农转生信的小硕，打造<strong>生信星球</strong>，想让它成为一个不拽术语、通俗易懂的生信知识平台。需要帮助或提出意见请后台留言或发送邮件到<a href="https://links.jianshu.com/go?to=mailto%3Ajieandze1314%40gmail.com" target="_blank">jieandze1314@gmail.com</a><br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="300" data-height="390"><img data-original-src="//upload-images.jianshu.io/upload_images/9376801-8a0adfaf13550bcd.png" data-original-width="300" data-original-height="390" data-original-format="image/png" data-original-filesize="18078" src="https://upload-images.jianshu.io/upload_images/9376801-8a0adfaf13550bcd.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">Welcome to our bioinfoplanet!</div>
</div><p></p>
  
</div>
            