
---
title: '用R画弧形图（Arc Diagram）'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/18922188-0d71769fa306c027.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/18922188-0d71769fa306c027.png'
---

<div>   
<p>在前几篇里我用cytoscape软件构建了网络图（<a href="https://www.jianshu.com/p/d75e1199f8b1" target="_blank">如何将WGCNA导出的基因共表达网络进行可视化</a>），见下图。但是看上去好像什么信息也看不出来，因为基因和基因之间的connectivity实在是太多了，全都糊在一起，看不出有哪些基因位于网络的中心，或者说看不出哪些基因和其他基因的联系很多。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1200" data-height="419"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-0d71769fa306c027.png" data-original-width="1200" data-original-height="419" data-original-format="image/png" data-original-filesize="353463" src="https://upload-images.jianshu.io/upload_images/18922188-0d71769fa306c027.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>当然你可以把cytoscape里的每一个基因的degree.layout导出来，里面有每一个基因有多少条edge与其相连，然后做一个bar图（<a href="https://www.jianshu.com/p/631381890ad4" target="_blank">用R画Circular barplot图</a>）,但是对于图里的数字（比如60和20）并没有非常直观的展示。偶然看到简书里一篇文章写的非常好（<a href="https://www.jianshu.com/p/a236227503e4" target="_blank">R数据可视化18:弧形图</a>）,做出的图形是这样的：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1200" data-height="560"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-84b9f4b116d460d7.png" data-original-width="1200" data-original-height="560" data-original-format="image/png" data-original-filesize="280731" src="https://upload-images.jianshu.io/upload_images/18922188-84b9f4b116d460d7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">这样的图可以清晰的显示出哪些基因之间的联系非常多，哪些基因形成一个“小社区”。图片来自：https://www.jianshu.com/p/a236227503e4</div>
</div>
<h4>（一）弧形图需要的数据</h4>
<p>弧形图需要的数据是从cytoscape里导出的，你也可以自己制作（如果数据不多的话）：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1601" data-height="903"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-2372aa52a3169a50.png" data-original-width="1601" data-original-height="903" data-original-format="image/png" data-original-filesize="386484" src="https://upload-images.jianshu.io/upload_images/18922188-2372aa52a3169a50.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">在cytoscape右下角处选择“edge table”，然后点击“export”，就会得到一个excel表</div>
</div>
<p>导出的表长这样：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1065" data-height="181"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-d31c892773cd5eda.png" data-original-width="1065" data-original-height="181" data-original-format="image/png" data-original-filesize="32957" src="https://upload-images.jianshu.io/upload_images/18922188-d31c892773cd5eda.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>我们需要的是这个表的“name”列。你需要在excel里把“ (interacts with) ”替换成空格（注意括号两边也有空格），这一步在excel里相当简单，就不赘述了。替换完成后的表长这样：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="797" data-height="174"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-504941985e8e3530.png" data-original-width="797" data-original-height="174" data-original-format="image/png" data-original-filesize="28379" src="https://upload-images.jianshu.io/upload_images/18922188-504941985e8e3530.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">现在基因和基因之间只有一个空格，一会儿要在R里根据这个空格将这一列分成两列</div>
</div>
<h4>（二）数据的预处理</h4>
<pre><code>> x = read.csv("turquiose_weight_morethan0.35_edge_interaction_edited.csv",header = T,sep = ",")
#先从原始矩阵里提取信息，并构建需要的数据框
> data = as.data.frame(x$name)
> colnames(data) = "V"
#把这列按照空格分成2列
> library(stringr)
> data <- str_split_fixed(data$V," ", 2)
> colnames(data) = c("from","to")
#给表格加一列，这一列是注明两个基因间是否有作用，如果有作用，标注1，没有的话标注0
#这里每一行都是2个基因，所以我们要加一列“1”
> to_add = as.data.frame(rep(1,1245)) #每一行都是1，一共是1245行
> colnames(to_add) = "value"
> data = cbind(data,to_add)
> head(data)
    from    to value
1  Spry1 Fbln1     1
2 Pdgfrl Fbln1     1
3    Dcn  Rgl1     1
4  Spry1 Prelp     1
5  Spry1    Cp     1
6  Spry1  Tgm2     1
</code></pre>
<p>现在得到的表格就是我们需要的。</p>
<h4>（三）计算基因的interact次数（edge条数）</h4>
<pre><code>> library(tidyverse)
> c(as.character(data$from), as.character(data$to)) %>%
  as_tibble() %>% 
  group_by(value) %>% #按照value进行分组
  summarize(n=n()) -> co
#修改列名
> colnames(co) <- c("name", "n")
#排序，按照降序排列
> co <- co[order(co$n,decreasing = T),]
#分组(for color)
> A = sum(co$n >=60)
> B = sum(co$n >=50) - A 
> C = sum(co$n >=40) - A - B
> D = sum(co$n >=30) - (A+B+C)
> E = sum(co$n >=20) - (A+B+C+D)
> f = sum(co$n >=10) - (A+B+C+D+E)
> G = sum(co$n < 10)
#把分组信息加到表里
> co <- data.frame(
  co,
  group=c(rep('A', A), rep('B', B), rep('C', C), rep('D', D),rep('E',E),rep('F',f),rep('G',G))
)
> head(co) 
   name  n group
1 Spry1 68     A
2  C1ra 67     A
3 Hmox1 67     A
4 Timp3 55     B
5  Rgl1 54     B
6 Prelp 53     B
</code></pre>
<h4>（四）给基因鉴定“小社区”</h4>
<pre><code>> library(igraph)
> mygraph <- graph_from_data_frame(data, vertices = co, directed = FALSE)
# 鉴定社区
> com <- walktrap.community(mygraph)
#重新整理数据
> coline <- co %>% 
  mutate(grp = com$membership) %>%
  arrange(grp) %>%
  mutate(name=factor(name, name))
> mygraph2 <- graph_from_data_frame(data, vertices = coline, directed = FALSE)
</code></pre>
<h4>（五）作图</h4>
<pre><code>#作图
> library(RColorBrewer)
> library(ggraph)
> mycolor<-colorRampPalette(brewer.pal(7, "Set3"))  #调色板请看：https://www.datanovia.com/en/blog/the-a-z-of-rcolorbrewer-palette/
> ggraph(mygraph2, layout="linear") + 
  geom_edge_arc(edge_colour="black", edge_alpha=0.2, edge_width=0.3, fold=TRUE) +
  geom_node_point(aes(size=n, color=as.factor(grp), fill=co$group), alpha=0.6) +
  scale_size_continuous(range=c(1,10)) +
  scale_color_manual(values=mycolor(50)) +
  geom_node_text(aes(label=name), angle=90, hjust=1, nudge_y = -1.1, size=2.8) +
  theme_void() +
  theme(
    legend.position="none",
    plot.margin=unit(c(0,0,0.5,0), "null"),
    panel.spacing=unit(c(0,0,2,0), "null") ) +
  expand_limits(x = c(-3, 1.2), y = c(-14, 1.2)) 
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2111" data-height="516"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-dbbd650f5c0671d6.png" data-original-width="2111" data-original-height="516" data-original-format="image/png" data-original-filesize="617460" src="https://upload-images.jianshu.io/upload_images/18922188-dbbd650f5c0671d6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
  
</div>
            