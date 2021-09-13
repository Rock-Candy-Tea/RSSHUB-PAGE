
---
title: 'GEO数据库视频学习笔记（差异分析、可视化、GSEA）'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/18922188-bf604602c5316309.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/18922188-bf604602c5316309.png'
---

<div>   
<p>笔记回顾：<br>
1.<a href="https://www.jianshu.com/p/51711c22934d" target="_blank">GEO数据库视频学习笔记（芯片数据下载和数据读取）</a><br>
2.<a href="https://www.jianshu.com/p/d64a1ddf1128" target="_blank">GEO数据库视频学习笔记（ID转换）</a><br>
3.<a href="https://www.jianshu.com/p/c94875df0155" target="_blank">GEO数据库视频学习笔记（了解你的表达矩阵）</a></p>
<p>这一讲的视频地址是：[<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1is411H7Hq%3Fp%3D7%255D" target="_blank">https://www.bilibili.com/video/BV1is411H7Hq?p=7]</a></p>
<h4>（一）差异分析</h4>
<p>上面三个视频笔记，记录了如何获得矩阵、如何过滤探针、如何获得分组信息，具备了这些，就可以进行差异分析了。这里Jimmy大神用的是limma包（当然差异分析还有很多其他的包可以用），参考文章：<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fwww.bio-info-trainee.com%2Fbioconductor_China%2Fsoftware%2Flimma.html" target="_blank">用limma对芯片数据做差异分析</a></p>
<p>首先做分组矩阵：</p>
<pre><code>> dim(exprSet)
[1] 18821     6
> library(limma)
#这一步就是告诉design，哪几个样品是对照，哪几个样品是处理，1代表是，0代表不是
> design <- model.matrix(~0+factor(group_list))
> colnames(design)=levels(factor(group_list))
> rownames(design)=colnames(exprSet)
> design
             control Vemurafenib
control1           1           0
control2           1           0
control3           1           0
Vemurafenib1       0           1
Vemurafenib2       0           1
Vemurafenib3       0           1
attr(,"assign")
[1] 1 1
attr(,"contrasts")
attr(,"contrasts")$`factor(group_list)`
[1] "contr.treatment"
</code></pre>
<p>再做比较矩阵：</p>
<pre><code>#这个矩阵声明，我们要把Vemurafenib组跟control组进行差异分析比较
> contrast_matrix <- makeContrasts(Vemurafenib-control,levels=design)
> contrast_matrix
             Contrasts
Levels        Vemurafenib - control
  control                        -1
  Vemurafenib                     1
# 对照是用来被比的
</code></pre>
<blockquote>
<p>当你做比较矩阵的时候，如果你搞不清到底是谁和谁在比，请看文章：<br>
<a href="https://www.jianshu.com/p/616de0ee881a" target="_blank">【r<-差异分析】当使用limma时，它在比较什么</a></p>
</blockquote>
<p>然后就是差异分析了：</p>
<pre><code>> library(limma)
# step1
> fit <- lmFit(exprSet,design)
# step2
> fit2 <- contrasts.fit(fit,contrast_matrix)
> fit2 <- eBayes(fit2)
# step3
> tempOutput = topTable(fit2,coef=1,n=Inf)
> nrDEG = na.omit(tempOutput)
> head(nrDEG)
          logFC   AveExpr         t      P.Value    adj.P.Val        B
CD36   5.780170  7.370282  79.74674 1.224250e-16 2.304160e-12 26.74942
DUSP6 -4.212683  9.106625 -62.45965 1.822336e-15 1.339567e-11 25.00170
DCT    5.633027  8.763220  61.57004 2.135222e-15 1.339567e-11 24.88864
SPRY2 -3.801663  9.726468 -53.97076 9.143161e-15 4.302086e-11 23.80028
MOXD1  3.263063 10.171635  47.09632 4.109399e-14 1.318367e-10 22.58677
ETV4  -3.843247  9.667077 -47.00035 4.202860e-14 1.318367e-10 22.56798
> dif <- tempOutput[tempOutput[,"P.Value"]<0.01,] #你可以只保存p<0.01的基因，也可以不筛选，这里不是强制的
> write.csv(dif,file="Differential_limma_matrix.csv")
</code></pre>
<h5>重点到了！！！如何检查你的差异分析有没有问题？？？</h5>
<p>先看一下刚得到的差异分析矩阵：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="600" data-height="168"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-bf604602c5316309.png" data-original-width="600" data-original-height="168" data-original-format="image/png" data-original-filesize="21538" src="https://upload-images.jianshu.io/upload_images/18922188-bf604602c5316309.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>我们就以第一个基因为检查例子：CD36</p>
<pre><code>> exprSet[rownames(exprSet)=='CD36',]
    control1     control2     control3 Vemurafenib1 Vemurafenib2 Vemurafenib3 
     4.54610      4.40210      4.49239     10.25060     10.21480    10.31570 
</code></pre>
<p>在表达矩阵里，CD36这个基因在对照组里大概是4，在处理组里是10左右。那么它的logFC应该是个正数，因为表达量经过处理后上升了。可以看到limma差异分析矩阵里logFC是5.78017，是个正数，那么就应该没什么问题。如果你发现表达上调的基因logFC是个负值，那么可能是你之前的分组，或者比较矩阵没有做对。</p>
<p>简单的画个热图吧，选差异分析列表里的前25个基因：</p>
<pre><code>> library(pheatmap)
> getgene = head(rownames(dif),25)
> getgene_matrix=exprSet[getgene,]
> getgene_matrix=t(scale(t(getgene_matrix)))
> pheatmap(getgene_matrix)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="827" data-height="567"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-a604a517f2b2279c.png" data-original-width="827" data-original-height="567" data-original-format="image/png" data-original-filesize="80088" src="https://upload-images.jianshu.io/upload_images/18922188-a604a517f2b2279c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h4>（二）火山图</h4>
<p>先画一个最丑火山图：</p>
<pre><code>> plot(nrDEG$logFC,-log10(nrDEG$P.Value))
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="662" data-height="454"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-012246a508108ebd.png" data-original-width="662" data-original-height="454" data-original-format="image/png" data-original-filesize="22388" src="https://upload-images.jianshu.io/upload_images/18922188-012246a508108ebd.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>太丑了，可以给它美化一下，但是Jimmy在这个视频里并没有提到如何美化，所以我用了自己之前用过的代码：</p>
<pre><code>> library(EnhancedVolcano)
> library(airway)
> EnhancedVolcano(nrDEG,
                 lab = rownames(nrDEG),
                 x = 'logFC',
                 y = 'P.Value',
                 xlim = c(-6, 6),
                 title = 'Vemurafenib versus control',
                 pCutoff = 0.01,
                 FCcutoff = 2,
                 transcriptPointSize = 1.5,
                 transcriptLabSize = 3.0,
                 col=c('black', 'blue', 'green', 'red1'),
                 colAlpha = 1,
                 legend=c('NS','logFC','P.value',
                          'P.value & logFC'),
                 legendPosition = 'right',
                 legendLabSize = 14,
                 legendIconSize = 5.0,
                 gridlines.major = FALSE,
                 gridlines.minor = FALSE
)
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="827" data-height="567"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-8b0829a83a02c3b3.png" data-original-width="827" data-original-height="567" data-original-format="image/png" data-original-filesize="105244" src="https://upload-images.jianshu.io/upload_images/18922188-8b0829a83a02c3b3.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">是不是比前面那个黑白火山图强多了？</div>
</div>
<h4>（三）GO,KEGG,GSEA分析</h4>
<p>在视频里，关于GO和KEGG这两个部分讲的很快，没有涉及到具体的代码，需要的童鞋可以参考我之前写的文章：<br>
<a href="https://www.jianshu.com/p/82787ddada38" target="_blank">RNA-seq练习 第三部分（DEseq2筛选差异表达基因,可视化）</a></p>
<p>做完差异分析后，实际上你得到的差异基因远远小于总基因数，你只是知道它上调下调了多少实际上是不够的，因为有些基因虽然在处理后有变化，但你还需要知道这些基因哪些是非常重要的。这时就需要GSEA分析。关于这一块，视频讲的有些凌乱。。。对于GESA软件，大神也木有细讲。<strong>可以参考我之前的笔记：<a href="https://www.jianshu.com/p/aae9b0322b83" target="_blank">GSEA学习笔记</a>，里面都是非常非常详细的代码，也详细的讲了怎么看GSEA的图以及简单的原理，还有如何使用软件进行GSEA分析。</strong>这里只根据GEO数据贴上代码：</p>
<pre><code>> geneList <- nrDEG$logFC
> names(geneList) <- gene.df$ENTREZID
> geneList_new <- sort(geneList,decreasing = T)
#go_result <- gseGO(geneList  = geneList_new,
#                   ont = "BP", 
#                   OrgDb = org.Hs.eg.db,
#                   minGSSize    = 10,
#                   maxGSSize = 500,
#                   pvalueCutoff = 1)
#go_result <- setReadable(go_result,OrgDb = org.Hs.eg.db)
#go_result_df <- as.data.frame(go_result)
#gseaplot(go_result,geneSetID = c("GO:0000727"))
> kegg <-gseKEGG(geneList  = geneList_new,
               organism     = 'hsa',
               nPerm        = 1000,
               minGSSize    = 10,
               maxGSSize = 500,
               pvalueCutoff = 1,
               verbose      = FALSE)
> kegg_result <- as.data.frame(kegg)
> gseaplot(kegg,geneSetID = 'hsa03030') #这里你可以根据上一行代码得到的data.frame里任何一个通路代码来进行展示
#图就不放了
</code></pre>
<p>上面你会发现我分别用了GO和KEGG的结果来展示GESA，这就是根据富集结果来展示哪些基因（通路）是重要的一种手段。</p>
<p>参考文章；<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1078364" target="_blank">生信技能树：差异分析得到的结果注释一文就够</a></p>
  
</div>
            