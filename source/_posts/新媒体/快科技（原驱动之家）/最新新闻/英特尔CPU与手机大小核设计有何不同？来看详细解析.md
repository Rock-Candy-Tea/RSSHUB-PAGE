
---
title: '英特尔CPU与手机大小核设计有何不同？来看详细解析'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220722/S6fe7f182-d96a-4c1c-8258-a06fc600dbc3.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 22 Jul 2022 06:32:35 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220722/S6fe7f182-d96a-4c1c-8258-a06fc600dbc3.jpg'
---

<div>   
<p>我们都知道，英特尔在12代酷睿处理器中采用了全新的架构设计，也就是异构混合架构。<span style="color:#ff0000;"><strong>这一架构主要就是通过P-Core性能核+E-Core能效核设计，来弥补以往架构核心数量不足的短板。</strong></span>而这种设计也被大家习惯性地称为“大小核”。</p>
<p>在这种异构架构中，P-Core，即所谓的大核主要通过高频率与超线程负责重负载任务；而E-Core，即所谓的小核则主要负责较轻负载任务，以及多线程性能吞吐与协同能力。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220722/6fe7f182-d96a-4c1c-8258-a06fc600dbc3.jpg" target="_blank"><img alt="英特尔CPU与手机大小核设计有何不同" h="431" src="https://img1.mydrivers.com/img/20220722/S6fe7f182-d96a-4c1c-8258-a06fc600dbc3.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>同时，P-Core与E-Core采用了不同的微架构设计，前者为全新的Golden Cove微架构，后者为Gracemont微架构。</p>
<p>我们都知道，在ARM架构下，异构设计早已有之。而因为ARM架构下的异构设计中，一个核心主要负责性能，另一个核心主要负责低能耗，因此被用户形象的称为大小核设计。</p>
<p>由于ARM架构主要面向移动级平台，如智能手机、平板电脑等，因此其大小核相对而言更加偏向能耗这一部分，毕竟对于这些移动级设备来说，低能耗、长续航、低热量是首先需要解决的问题。</p>
<p>但是对于PC而言，尤其是游戏本或桌面级PC来说，本身其实并不存在功耗和散热方面的担忧，<span style="color:#ff0000;"><strong>因此英特尔P-Core+-E-Core混合架构设计，严格意义上来说并不等同于ARM架构的大小核。</strong></span></p>
<p>其实就“大小核”来说，首先要清楚的一点是，在一个大小核异构架构下，大核是相对于小核而大的，小核是相对于大核而小的，<strong>如果跨越系统平台去单纯说小核一定就小，大核一定就大，无疑是不够严谨的。</strong></p>
<p>那么英特尔的“大小核”与ARM的大小核究竟有何不同呢？</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220722/40c39664-1287-4f6e-8078-587accc93cdb.jpg" target="_blank"><img alt="英特尔CPU与手机大小核设计有何不同" h="293" src="https://img1.mydrivers.com/img/20220722/S40c39664-1287-4f6e-8078-587accc93cdb.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>首先明确的一点是，12代酷睿Alder Lake的E-Core并不是单纯意义上的小核心。</p>
<p>因为在英特尔异构架构体系下，Gracemont微架构的E-Core承担的是协同性的多线程吞吐性能提升，其实际性能超过了Skylake和Zen 2，而Skylake和Zen 2绝对不是小核心，它只是相对于Golden Cove的P-Core而言，能耗低一些。</p>
<p>其次从命名来看，Gracemont无疑是源自Atom这一脉，其上一代微架构为Tremont，相对于Golden Cove微架构的P-Core而言，Gracemont微架构的E-Core确实要小一些，但其实际性能相对于Tremont来说，IPC提升超过20%。</p>
<p>其实对于12代酷睿来说，E-Core更重要的意义在于负责多线程任务的处理，如渲染、压缩/解压缩等等。</p>
<p>而在Tremont上改进后的Gracemont，其实在渲染方面有着非常出色的性能表现。这源于其双前端六解码、以及整数浮点分离的设计。要知道，这种设计在ARM架构的小核中是没有的。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220722/dc175c12-311b-4024-848a-af6eb987543a.jpg" target="_blank"><img alt="英特尔CPU与手机大小核设计有何不同" h="594" src="https://img1.mydrivers.com/img/20220722/Sdc175c12-311b-4024-848a-af6eb987543a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>此外英特尔在混合架构之下对缓存进行了扩容，在增加了P-Core的二级缓存和E-Core的每核二级缓存的情况下，英特尔同时在共享L3智能缓存上也进行了增强和扩容。根据不同的核心数，英特尔12代酷睿处理器L3智能缓存最高提高到30MB，有效提高内存数据量、降低延时。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220722/2deb6f64-aa17-4b60-9507-50f8f8324309.jpg" target="_blank"><img alt="英特尔CPU与手机大小核设计有何不同" h="306" src="https://img1.mydrivers.com/img/20220722/S2deb6f64-aa17-4b60-9507-50f8f8324309.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>而在频率方面，E-Core睿频能力从3.6GHz起步到3.9GHz，表现也是相当不错了。</p>
<p>其实对于大小核设计，大家很容易被误导的一个地方是，“大小核”三个字就是简单描述核心的大小。其实从本质上来讲，这种描述忽略了大与小的参照系。</p>
<p><strong>在一个拥有大核心和小核心的异构架构中，大小核的界定除了考虑到核心面积之外，其实还要考虑到其发挥的作用。</strong></p>
<p>ARM架构下的小核心存在的主要任务就是负责低能耗，而<strong>12代酷睿中的“小核心”可并不是单单负责低能耗，它还要承担起更重负载的多线程任务，</strong>因此12代酷睿的“大小核”与ARM架构的大小核，其本质有着明显差异。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220722/20aa4845ab4a4e07a991ad81247b96bf.jpg" target="_blank"><img alt="英特尔CPU与手机大小核设计有何不同？来看详细解析" h="400" src="https://img1.mydrivers.com/img/20220722/s_20aa4845ab4a4e07a991ad81247b96bf.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：振亭</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/intel.htm">Intel</a><a href="https://news.mydrivers.com/tag/yingteer.htm">英特尔</a><a href="https://news.mydrivers.com/tag/shouji.htm">手机</a>  </p>
        
</div>
            