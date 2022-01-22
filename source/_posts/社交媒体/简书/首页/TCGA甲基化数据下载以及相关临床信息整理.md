
---
title: 'TCGA甲基化数据下载以及相关临床信息整理'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/18922188-abcb96eff5cf6b54.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/18922188-abcb96eff5cf6b54.png'
---

<div>   
<p>之前的文章里已经按照教程进行了TCGA数据库的一些练习（RNA-seq、芯片、生存分析），现在学习TCGA甲基化数据的分析过程。</p>
<p>参考文章：<br>
1.<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F-E50Jvzo8aNqVgvEB0nVGA" target="_blank">甲基化的一些基础知识</a><br>
2.<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIxMjA0NzU0OA%3D%3D%26mid%3D2650983484%26idx%3D1%26sn%3D5386066548d8e218e5087ca2ff3e8554%26scene%3D21%23wechat_redirect" target="_blank">Make Decision: DNA甲基化检测方法，哪一款适合你？</a><br>
3.<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI2MDA4NTYzOA%3D%3D%26mid%3D2649533250%26idx%3D1%26sn%3D1875eb152f5bda3db0b24c3ee2c8c9d7%26scene%3D21%23wechat_redirect" target="_blank">一文了解 MethylationEPIC 850K 甲基化芯片</a><br>
4.<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA5NzE1MTYwMw%3D%3D%26mid%3D2650834021%26idx%3D1%26sn%3Dde51f4d8ab4e4f299a964e6a518a622c%26scene%3D21%23wechat_redirect" target="_blank">DNA甲基化研究方法速递</a></p>
<p>摘自参考文章1：</p>
<blockquote>
<p>目前5个甲基化数据库：<br>
（1）Roadmap：NIH的“表观组学线图计划” (Roadmap Epigenomics Mapping Consortium)，包含367个人类主要组织和细胞类型的DNA甲基化图谱<br>
（2）BLUEPRINT：欧洲“血液表观基因组项目”（BLUEPRINT of Haematopoietic Epigenomes），包含与人类复杂疾病相关的82个不同血液细胞的DNA甲基化图谱。<br>
（3）ENCODE：“DNA元件百科全书”计划（The Encyclopedia of DNA Elements），包含来自世界各国32个研究机构对206个人类不同的细胞系和组织进行了DNA甲基化水平的测定。<br>
（4）ICGC：“国际癌症基因组联盟”（The International Cancer Genome Consortium），旨在从基因组、表观基因组和转录组等多维数据层面研究癌症的发生和发展，包含27种常见癌症的9000多个样本的DNA甲基化数据，<br>
（5）TCGA：包含34种癌症类型的10000多个样本的DNA甲基化数据，并且保留了癌症患者详细的临床数据资料，为生存分析提供了大量的数据资源。</p>
</blockquote>
<p>练习的文献来自：Seven-CpG-based prognostic signature coupled with gene expression predicts survival of oral squamous cell carcinoma。<br>
目标：下载TCGA数据库中口腔癌的<strong>甲基化芯片信号值</strong>矩阵，然后挑选有N-T配对的32个病人的数据进行差异分析。</p>
<p>这些甲基化结果使用的平台是illumina公司的Human methylation 450，可检测人全基因组45万个甲基化位点，全面覆盖了96%的CpG岛，并根据需求加入了CpG岛以外的CpG位点、人类干细胞非CpG甲基化位点、正常组织与肿瘤（多种癌症）组织差异甲基化位点、编码区以外的CpG岛、miRNA启动子区域和已通过GWAS的疾病相关区域的位点，同时覆盖了Human Methylation27 BeadChip的90%的位点（Human Methylation27是世界首款DNA甲基化芯片）。</p>
<p><strong>练习之前需要提示的是</strong>：</p>
<blockquote>
<p>这个TCGA的甲基化数据很大，如果你下载完整的文件一共大概有80多个G（TCGAbiolink包下载），你需要一个大的储存空间，或者整一个移动硬盘。下载也是很费时，网速不好的话，过夜下载很正常。而且<strong>内存要求非常高</strong>，我尝试了提高系统虚拟内存，然而还是不行。于是我就换了一种方法下载。(见下面）<br>
<strong>另外：网上的几篇教程里面的甲基化数据临床样品信息似乎和我下载的不太一样，于是我就自己摸索着整理了一下，结果得到29对样品，与文献里和教程里的不一样（32对），不过没有太大关系，练习的目的旨在熟悉处理过程。如果有严重强迫症的童鞋可以移步其他教程，本篇文章绝大多数代码是自己写的，有些繁琐，但至少是自己研究了2天半的结果。</strong></p>
</blockquote>
<h4>（一）数据下载</h4>
<h5>（1）甲基化信号矩阵下载：</h5>
<p>去网站：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fxenabrowser.net%2Fdatapages%2F" target="_blank">https://xenabrowser.net/datapages/</a>，选择：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="464" data-height="39"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-abcb96eff5cf6b54.png" data-original-width="464" data-original-height="39" data-original-format="image/png" data-original-filesize="6078" src="https://upload-images.jianshu.io/upload_images/18922188-abcb96eff5cf6b54.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>出现新页面后，点击：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1484" data-height="205"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-57c0e47f6170e32e.png" data-original-width="1484" data-original-height="205" data-original-format="image/png" data-original-filesize="69997" src="https://upload-images.jianshu.io/upload_images/18922188-57c0e47f6170e32e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>再点击这里：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1110" data-height="193"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-b9cf997f9471d76e.png" data-original-width="1110" data-original-height="193" data-original-format="image/png" data-original-filesize="27140" src="https://upload-images.jianshu.io/upload_images/18922188-b9cf997f9471d76e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>下载后解压。得到一个名为HumanMethylation450的文件。</p>
<h5>（2）下载临床数据</h5>
<p>去TCGA网站上选择好TCGA-HNSC的甲基化数据，弹出的页面应该是：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1621" data-height="772"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-2c554444bf7c834e.png" data-original-width="1621" data-original-height="772" data-original-format="image/png" data-original-filesize="123352" src="https://upload-images.jianshu.io/upload_images/18922188-2c554444bf7c834e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">https://portal.gdc.cancer.gov/projects/TCGA-HNSC</div>
</div>
<p>把上面的“Biospecimen”和“clinical”两个部分的“tsv”文件都下载下来：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="604" data-height="78"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-1a5339683c99536f.png" data-original-width="604" data-original-height="78" data-original-format="image/png" data-original-filesize="5457" src="https://upload-images.jianshu.io/upload_images/18922188-1a5339683c99536f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>两个文件解压缩后，会解压出多个tsv文件，其中一个叫"sample.tsv”和“clinical.tsv”两个文件的就是我们需要的临床文件。</p>
<h4>（二）数据预处理</h4>
<h5>（1）临床数据预处理</h5>
<p>首先处理临床数据，因为我们并不需要所有的数据，我们先把样品进行过滤，读取的是“sample.tsv”文件，里面有我们要的“肿瘤/正常”信息：</p>
<pre><code>#先读取sample.tsv文件
> pd.all <- read.delim("sample.tsv", header = T, stringsAsFactors = F)
> dim(pd.all) #你会发现虽然下载页面介绍只有528个病人，但是这里的样品信息有1573个，说明每个病人的取样不止1次，后面要删掉
[1] 1573   37
> colnames(pd.all) #所有的临床信息，我们并不需要所有的
#提取部分临床信息
> pd <- pd.all[,c("case_id","case_submitter_id","sample_submitter_id","sample_type")]
> table(pd$sample_type)  #看一下样品的类型，这里有4种，只取后面的两种，即只取实体组织
Blood Derived Normal           Metastatic        Primary Tumor  Solid Tissue Normal 
                 511                    2                  978                   82 
#这里看到原位肿瘤有978个样品，远远超过了528个病人的数量，再一次验证了存在同一个病人多次取样的情况
> tissue = c("Primary Tumor","Solid Tissue Normal") #取后面两种样品类型
> pd_tissue <- pd[pd$sample_type %in% tissue,] #从所有的临床信息里提取我们要的两种类型的信息
> table(pd_tissue$sample_type)
        Primary Tumor       Solid Tissue Normal 
                978                  82
</code></pre>
<p>截至目前为止，提取出了实体组织的样品。下面要对样品进行过滤，<strong>因为有些肿瘤样品的取样多于1次</strong>：</p>
<pre><code>> table(pd_tissue$case_submitter_id) #查看case_submitter_id（例如：TCGA-CQ-A4CE）分别出现了几次
#结果里有1,2,3。
#首先我们要先去掉1的那些样品，因为这些样品一定不是配对的。
#删除在case_submitter_id（例如：TCGA-CQ-A4CE）里只出现过一次的行
#代码参考：https://blog.csdn.net/dingchenxixi/article/details/50865277
> deleteuniquelines <- function(x) &#123;# x为输入的数据框
  stand.col <- x$case_submitter_id 
  count <- table(stand.col) #table函数可以得到每个上述列每个数所出现的频数
  if (all(count < 2)) stop("no repeated records") 
  else &#123;
    ind <- sapply(stand.col, function(t) ifelse(count[as.character(t)] > 1, TRUE, FALSE))
  &#125;
  return(x[ind, ])
&#125;
> pd_tissue_filtered = deleteuniquelines(pd_tissue)
> dim(pd_tissue_filtered) #过滤完不配对的样品，还剩982个，但这里面不是全配对的，有的是同一个肿瘤样品取了两次
#[1] 982   4
#分别提取正常和肿瘤组织样品
> nt = pd_tissue_filtered[pd_tissue_filtered$sample_type =="Solid Tissue Normal",]
> tt = pd_tissue_filtered[pd_tissue_filtered$sample_type =="Primary Tumor",]
#对于正常组织，由于都只取了一次样品，所以不进行过滤
#对于肿瘤样品：只取tt里sample_submitter_id编码最后一位是"A"的样品，因为B是福尔马林固定石蜡包埋组织
#从B以后就不太好了，如果你table一下会发现还有Z，所以只取A的样品
> tt <- tt[substr(tt$sample_submitter_id,16,16) =="A",]
#取和正常对照匹配的肿瘤样品
> tt <- tt[tt$case_submitter_id %in% nt$case_submitter_id,]
> dim(tt)
[1] 82  4
#合并正常和肿瘤样品
> paired_tissue <- rbind(nt,tt)
> dim(paired_tissue)
[1] 164   4
</code></pre>
<p>到目前为止，我们提取出了成对的样品（在临床信息里）。一共是82对。下面我们需要对肿瘤发生的位置进行筛选，只取发生在口腔里的肿瘤组织和其对照，需要读取“clinical.tsv”文件：</p>
<pre><code>#读取“clinical.tsv”文件，提取肿瘤位置信息
> tumor_site <-read.delim("clinical.tsv",header = T,stringsAsFactors = F)
#这里需要注意的是，临床样品里有两列分别是“取样位置”和“肿瘤发生位置”，你要取的是“肿瘤发生的位置”
> tumor_site <- tumor_site[,c("case_id","case_submitter_id","tissue_or_organ_of_origin")]
> library(stringr)
> tumor_site[, c("anatomic_neoplasm_subdivision", "takeout")] <- str_split_fixed(tumor_site$tissue_or_organ_of_origin, ",", 2)
> tumor_site <- tumor_site[,c(1,2,4)]
> table(tumor_site$anatomic_neoplasm_subdivision) #看一下所有的肿瘤位置信息
#这里的分类信息和有些教程里的不一样，我觉得无所谓
     Anterior floor of mouth               Base of tongue             Border of tongue 
                           4                           48                            2 
                Cheek mucosa               Floor of mouth                          Gum 
                          38                          108                           16 
                 Hard palate                  Hypopharynx                       Larynx 
                           8                           18                          232 
                         Lip                    Lower gum                     Mandible 
                           6                            4                            2 
                       Mouth                   Oropharynx    Overlapping lesion of lip 
                          46                           18                          140 
                      Palate                      Pharynx Posterior wall of oropharynx 
                           2                            2                            2 
             Retromolar area                 Supraglottis                       Tongue 
                           2                            2                          260 
                      Tonsil                    Upper Gum    Ventral surface of tongue 
                          92                            2                            2 
> oscc = c("Mouth",
           "Cheek mucosa",
           "Lip",
           "Hard palate",
           "Floor of mouth",
           "gum","Upper Gum","Lower gum",
           "Anterior floor of mouth",
           "Border of tongue","Base of tongue","Tongue",
           "Ventral surface of tongue") #取口腔里发生的肿瘤
> tumor_site <- tumor_site[tumor_site$anatomic_neoplasm_subdivision %in% oscc,]
> dim(tumor_site) #我们取的肿瘤发生在口腔里的样品有528个
[1]528   3
</code></pre>
<p>我们需要知道上面82对样品里有多少是发生在口腔里的肿瘤样品：</p>
<pre><code>> tumor_site_unique <- unique(tumor_site$case_submitter_id) #取“肿瘤位置”矩阵里出现过的样品
> tumor_site_unique = as.data.frame(tumor_site_unique)
> colnames(tumor_site_unique) = "case_submitter_id"
#把“肿瘤位置”里的样品匹配到“配对肿瘤/正常”样品里
> merge_info <- paired_tissue[paired_tissue$case_submitter_id %in% tumor_site_unique$case_submitter_id,]
> dim(merge_info) #这里有36对样品
[1] 72   4
</code></pre>
<p><strong>注意！！！这里不要以为就处理完临床样品了，因为你一会儿要把临床样品和甲基化信号矩阵做交集的，所以你还得看你的id和甲基化信号矩阵的列名是不是一样的格式！！！</strong></p>
<p>读取甲基化信号矩阵：</p>
<pre><code>> methy_data <- data.table::fread("HumanMethylation450",data.table = F)
|--------------------------------------------------|
|==================================================|
> methy_data[1:4,1:4]
      sample TCGA-CN-6022-01 TCGA-CQ-5327-01 TCGA-CV-5435-11
1 cg13332474          0.0220          0.0264          0.0307
2 cg00651829          0.0209          0.4514          0.0214
3 cg17027195          0.0443          0.2414          0.0330
4 cg09868354          0.0490          0.0546          0.0469
</code></pre>
<p>你会发现，这个列名是sample_submitter_id的前15位字符，我们上面的sample_submitter_id共有16位字符，所以还要处理一下我们的临床信息：</p>
<pre><code>> merge_info$sample_submitter_id = substr(merge_info$sample_submitter_id,1,15)
> head(merge_info)
      case_id case_submitter_id sample_submitter_id
3   e7d1f0dd-eec0-4670-a2ba-00ffe38c6382      TCGA-CV-6939     TCGA-CV-6939-11
8   ebfb8c1b-471f-4acb-a1fe-287e02cadba7      TCGA-H7-A6C4     TCGA-H7-A6C4-11
43  91728cd6-ed91-49dc-9279-faedbe211a9d      TCGA-CV-6951     TCGA-CV-6951-11
73  dec3c21b-3f59-472f-8573-27b0e830aa92      TCGA-HD-A6I0     TCGA-HD-A6I0-11
91  93a265b7-6c23-4e5f-b797-c117793744bf      TCGA-CV-6936     TCGA-CV-6936-11
113 f9e82d62-fafc-45b0-97cf-d1a4a3c884a1      TCGA-WA-A7GZ     TCGA-WA-A7GZ-11
            sample_type
3   Solid Tissue Normal
8   Solid Tissue Normal
43  Solid Tissue Normal
73  Solid Tissue Normal
91  Solid Tissue Normal
113 Solid Tissue Normal
#最后千万别忘记保存
> write.table(merge_info$sample_submitter_id, file = "paired_samples_name_from_clinical.txt",quote = F, row.names = F, col.names = F)
</code></pre>
<h5>（2）甲基化矩阵预处理</h5>
<p>从580个甲基化样品里提取成对样品的甲基化信号<br>
在R里操作：</p>
<pre><code>#读取甲基化矩阵，这个矩阵很大，需要fread读取
> methy_data <- data.table::fread("HumanMethylation450",data.table = F)
> methy_data[1:4,1:4]
#将上面36对样品的肿瘤和正常分别提取出来
> nt_paired = merge_info[merge_info$sample_type=="Solid Tissue Normal",]
> tt_paired = merge_info[merge_info$sample_type=="Primary Tumor",]
#与甲基化信号矩阵进行匹配
> methy_nt = methy_data[,colnames(methy_data) %in% nt_paired$sample_submitter_id] #甲基化矩阵里只有29个正常样品和临床信息配对
> methy_tt = methy_data[,colnames(methy_data) %in% tt_paired$sample_submitter_id] #甲基化矩阵里有36个肿瘤样品，和临床信息相符
#匹配后合并肿瘤与正常样品
> methy_combine = cbind(methy_nt,methy_tt)
> table(colnames(methy_combine)) #这里并不是每一个肿瘤样品都匹配一个正常对照，所以我们要把多余的肿瘤样品去掉
#你会发现最后7个样品并不是配对的，我们需要把它们删掉
TCGA-CV-5436-01 TCGA-CV-5436-11 TCGA-CV-5439-01 TCGA-CV-5439-11 TCGA-CV-5442-01 TCGA-CV-5442-11 
              1               1               1               1               1               1 
TCGA-CV-5970-01 TCGA-CV-5970-11 TCGA-CV-5971-01 TCGA-CV-5971-11 TCGA-CV-5973-01 TCGA-CV-5973-11 
              1               1               1               1               1               1 
TCGA-CV-5976-01 TCGA-CV-5976-11 TCGA-CV-5977-01 TCGA-CV-5977-11 TCGA-CV-5979-01 TCGA-CV-5979-11 
              1               1               1               1               1               1 
TCGA-CV-6003-01 TCGA-CV-6003-11 TCGA-CV-6433-01 TCGA-CV-6433-11 TCGA-CV-6436-01 TCGA-CV-6436-11 
              1               1               1               1               1               1 
TCGA-CV-6441-01 TCGA-CV-6441-11 TCGA-CV-6933-01 TCGA-CV-6933-11 TCGA-CV-6934-01 TCGA-CV-6934-11 
              1               1               1               1               1               1 
TCGA-CV-6936-01 TCGA-CV-6936-11 TCGA-CV-6939-01 TCGA-CV-6939-11 TCGA-CV-6943-01 TCGA-CV-6943-11 
              1               1               1               1               1               1 
TCGA-CV-6951-01 TCGA-CV-6951-11 TCGA-CV-6952-01 TCGA-CV-6952-11 TCGA-CV-6953-01 TCGA-CV-6953-11 
              1               1               1               1               1               1 
TCGA-CV-6954-01 TCGA-CV-6954-11 TCGA-CV-6956-01 TCGA-CV-6956-11 TCGA-CV-6959-01 TCGA-CV-6959-11 
              1               1               1               1               1               1 
TCGA-CV-6961-01 TCGA-CV-6961-11 TCGA-CV-7103-01 TCGA-CV-7103-11 TCGA-CV-7235-01 TCGA-CV-7235-11 
              1               1               1               1               1               1 
TCGA-CV-7238-01 TCGA-CV-7238-11 TCGA-CV-7255-01 TCGA-CV-7255-11 TCGA-CV-7406-01 TCGA-CV-7438-01 
              1               1               1               1               1               1 
TCGA-H7-A6C4-01 TCGA-HD-8635-01 TCGA-HD-A6HZ-01 TCGA-HD-A6I0-01 TCGA-WA-A7GZ-01 
              1               1               1               1               1 

#把只出现过一次列名的列去掉
> deleteuniquecolumn <- function(x) &#123;# x为输入的数据框
  m = substr(colnames(x),1,12)
  stand.col <- m 
  count <- table(stand.col) #table函数可以得到每个上述列每个数所出现的频数
  if (all(count < 2)) stop("no repeated records") 
  else &#123;
    ind <- sapply(stand.col, function(t) ifelse(count[as.character(t)] > 1, TRUE, FALSE))
  &#125;
  return(x[,ind])
&#125;
> methy_paired = deleteuniquecolumn(methy_combine)
> table(colnames(methy_paired))
> rownames(methy_paired) = methy_data$sample
#保存过滤完样品的甲基化矩阵
> write.csv(methy_paired,file="OSCC_29paired_methydata.csv")
</code></pre>
<p>到这里，我们把甲基化矩阵过滤完成了，留下29对口腔肿瘤/正常样品对，这个结果与文献里的不同，我认为无所谓，主要是走一下流程。有可能是我和文献里过滤样品的方法不同也有关系。</p>
<p>过滤样品后，甲基化矩阵长这样：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1338" data-height="347"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-9955f7626c2bccec.png" data-original-width="1338" data-original-height="347" data-original-format="image/png" data-original-filesize="51502" src="https://upload-images.jianshu.io/upload_images/18922188-9955f7626c2bccec.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>（3）过滤甲基化矩阵，并整理为ChAMP对象</h5>
<pre><code>#读取上面保存的29对样品甲基化信号矩阵
> methy = data.table::fread("OSCC_29paired_methydata.csv",data.table = F)
> head(methy)
#载入需要的包
> library(ChAMP)
> library(dplyr)
> library(tibble)
#把myNorm里的列名按照pd里的sample_submitter_id顺序排
> methy_sort <- methy[,c("V1","TCGA-CV-5436-01","TCGA-CV-5436-11","TCGA-CV-5439-01",
                       "TCGA-CV-5439-11","TCGA-CV-5442-01","TCGA-CV-5442-11","TCGA-CV-5970-01",
                      "TCGA-CV-5970-11","TCGA-CV-5971-01","TCGA-CV-5971-11","TCGA-CV-5973-01",
                       "TCGA-CV-5973-11","TCGA-CV-5976-01","TCGA-CV-5976-11","TCGA-CV-5977-01",
                       "TCGA-CV-5977-11","TCGA-CV-5979-01","TCGA-CV-5979-11","TCGA-CV-6003-01",
                       "TCGA-CV-6003-11","TCGA-CV-6433-01","TCGA-CV-6433-11","TCGA-CV-6436-01",
                       "TCGA-CV-6436-11","TCGA-CV-6441-01","TCGA-CV-6441-11","TCGA-CV-6933-01",
                       "TCGA-CV-6933-11","TCGA-CV-6934-01","TCGA-CV-6934-11","TCGA-CV-6936-01",
                       "TCGA-CV-6936-11","TCGA-CV-6939-01","TCGA-CV-6939-11","TCGA-CV-6943-01",
                       "TCGA-CV-6943-11","TCGA-CV-6951-01","TCGA-CV-6951-11","TCGA-CV-6952-01",
                       "TCGA-CV-6952-11","TCGA-CV-6953-01","TCGA-CV-6953-11","TCGA-CV-6954-01",
                       "TCGA-CV-6954-11","TCGA-CV-6956-01","TCGA-CV-6956-11","TCGA-CV-6959-01",
                       "TCGA-CV-6959-11","TCGA-CV-6961-01","TCGA-CV-6961-11","TCGA-CV-7103-01",
                       "TCGA-CV-7103-11","TCGA-CV-7235-01","TCGA-CV-7235-11","TCGA-CV-7238-01",
                       "TCGA-CV-7238-11","TCGA-CV-7255-01","TCGA-CV-7255-11")]

> a = column_to_rownames(methy_sort,"V1")
> beta_value = as.matrix(a)
# beta信号值矩阵里面不能有NA值
> beta=impute.knn(beta_value) 
> sum(is.na(beta)) #这里是检查矩阵里是否还有NA
#[1] 0
> beta=beta$data
> beta=beta+0.00001
#准备pd表型文件（实际上就是样品的信息）
> pd_1 <- as.data.frame(colnames(beta))
> pd_info <- merge_info[merge_info$sample_submitter_id %in% pd_1$`colnames(beta)`,]
> colnames(pd_1) = "sample_submitter_id"
> pd <- merge(pd_1,pd_info,by = "sample_submitter_id",all.x = TRUE)
#使用ChAMP过滤
> myLoad=champ.filter(beta = beta ,pd = pd) #这一步已经自动完成了过滤
> dim(myLoad$beta) #beta就是指的是beta值，我们需要的甲基化信号
#[1] 412481     58
#保存这个ChAMP对象
> save(myLoad,file = 'OSCC_29paired_methydata_ChAMPfiltered.Rdata')
</code></pre>
<p>了解一下上面的<code>champ.filter</code>这一步都过滤了些什么：</p>
<blockquote>
<p>1.过滤掉detection p-value大于0.01的探针<br>
2.过滤掉在至少5%样本中bead count小于3的探针<br>
3.过滤掉非GpC位点的探针<br>
4.过滤掉所有SNP相关的探针<br>
5.过滤掉multi-hit探针，即映射到多个位置的<br>
6.过滤掉X和Y染色体上的探针<br>
参考文章：<a href="https://links.jianshu.com/go?to=%255Bhttps%3A%2F%2Fwww.bioinfo-scrounger.com%2Farchives%2F432%2F%255D%28https%3A%2F%2Fwww.bioinfo-scrounger.com%2Farchives%2F432%2F%29" target="_blank">甲基化芯片入门学习-ChAMP包（二）</a></p>
</blockquote>
<p>看一下这个对象长啥样：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1097" data-height="277"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-fc42827549ec5190.png" data-original-width="1097" data-original-height="277" data-original-format="image/png" data-original-filesize="55245" src="https://upload-images.jianshu.io/upload_images/18922188-fc42827549ec5190.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
  
</div>
            