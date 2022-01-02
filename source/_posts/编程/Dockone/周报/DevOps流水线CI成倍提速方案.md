
---
title: 'DevOps流水线CI成倍提速方案'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/bf74ca720d1f6e3c9a4d46fcdf508810.png'
author: Dockone
comments: false
date: 2022-01-02 07:08:23
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/bf74ca720d1f6e3c9a4d46fcdf508810.png'
---

<div>   
<br><h3>背景介绍</h3>我们的同学在之前发布的《<a href="http://dockone.io/article/2434434">猪八戒网CICD最佳实践之路</a>》一文中，介绍了猪八戒网的主流研发语言从PHP到Java的更替以及架构到Dubbo为核心的SOA微服务框架Nodejs提供前端Web能力的演进。随着业务的增加和架构的演进，项目工程数量的快速增⻓，交付开始变得频繁。相比PHP，Nodejs和Java对CI有更高的要求，DevOps 流水线的引入已然迫在眉睫。<br>
<br>文章详细的介绍了猪八戒网DevOps流水线的架构，介绍了流水线从无到“通路”再到“通⻋”的变化。而业务的增加对“通⻋”后的体验提出了“乘坐时间要短”、“乘坐环境要舒适平稳”、“个性化的乘坐体验”等新的要求，本文重点讨论“通⻋”后的“提速”。<br>
<br>上个世纪50年代，新中国第一条铁路，全⻓共505公里的成渝铁路全线通⻋，全程需要13个小时左右。90年代，部分绿皮⻋换成了红皮⻋，乘坐时间大幅缩短，但最快也要10小时。那个时候成渝之间主要的通勤方式还是比铁路快几个小时的高速大巴，除了大巴，当时还有⻜机。成渝高铁通⻋后，高铁已经成了成渝之间首选交通工具，成渝大巴也逐渐淡出了人们的视线。<br>
<br>“提速”对用户体验的提升最为有感知，也是让用户最容易认可的。对于互联网行业来说，速度慢会导致用户会抱怨和流失，相关统计数据显示，每增加0.1秒的加载延迟，将会导致客户活跃度下降1%。DevOps流水线“通⻋”后的“提速”策略便是化解频繁交付需求和承载能力之间矛盾的良药。<br>
<h3>了解现状</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/bf74ca720d1f6e3c9a4d46fcdf508810.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/bf74ca720d1f6e3c9a4d46fcdf508810.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/655dd71e61f687e14a502d97b8e43a20.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/655dd71e61f687e14a502d97b8e43a20.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/5e7688b698737ef45c05303a2285103e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/5e7688b698737ef45c05303a2285103e.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们使用最多语言是Java，第二是Nodejs，占比超过20%。<br><br>
<h3>分析数据</h3>有了以上的数据，我们就可以根据不同的语言在DevOps流水线的各环节的耗时数据来分析可能存在的问题。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/49607def4f17e1abbea9d4d68d25b54e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/49607def4f17e1abbea9d4d68d25b54e.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
按我们的主流开发语言项目的发布耗时来看，其中耗时最⻓的是Nodejs，占比达到了70%，按照2/8原则来看， 我们只需要花少量的精力来优化成体速度的提升，侧重点是关注Nodejs的项目的发布速度。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/618d9210f0aaf49f63401d98c18667f7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/618d9210f0aaf49f63401d98c18667f7.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通过在流水线中各位环节打标时间戳，采集了大量的日志数据后，我们分析发现，Nodejs项目在CI/CD过程中耗时最⻓的是在安装依赖和编译构建中。安装依赖的时间大量消耗在了npm install上面了，即便是我们有自己的私有npm仓库但还是消耗了大量的时间。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/f87bc6b19d40f163ca1f7e26be65c1f0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/f87bc6b19d40f163ca1f7e26be65c1f0.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
很多Nodejs项目发布的时间超过600s，部分项目甚至偶尔会超过1000s，这部分项目也是我们优化治理的“大客户”。头部大客户的数量下降了，速度起来了，就可以很好的反应策略的效果是否符合预期。<br>
<h3>制定策略</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/43bc523c7db25c096c5c941129c18335.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/43bc523c7db25c096c5c941129c18335.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>底层软件硬件调整</h4>CI过程中主要的压力还是集中在IO方向，增加CI节点提高整个CI池子的容量，把之前节点使用的硬盘更换为SSD可以增加IO吞吐量。同时把用于CI的Node节点在Kubernetes集群中隔离开来，让CI服务独享这些资源避免与其他资源发生抢占。<br>
<h4>CI 工作台优化</h4>优化CI工作台的代码，减少每次CI任务抓取Git仓库里托管项目的代码量，提高整体的代码抓取的效率，减少网络IO和磁盘IO量。<br>
<h4>强制启用内部软件源</h4>要求各业务线的项目启用在内部搭建的软件源，尽量不要使用外部软件源，减少等待外部网络的下载时间。Nodejs使用verdaccio来搭建内部源并且设置国内的Nodejs源作为上游，拉取到的包就会缓存到本地服务器，大大减少了不必要的网络开销。Java和PHP分别使用了nexus和packagist。<br><br>
<h3>实验论证</h3>考虑到底层软件硬件的升级调整对IO性能提升很容易理解，就不在这里赘述，这里着重介绍一下引入yarn和把yarn.lock提交到代码仓库后带来的速度大幅提升。<br><br>
<h4>安装yarn</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/38493383bd845381feec1d64a4c539f1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/38493383bd845381feec1d64a4c539f1.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>用yarn替换npm进行编译构建</h4>修改项目的构建文件，需要更改的片段如下：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/fa07e2df430de2bddfb84cbbef70a3e2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/fa07e2df430de2bddfb84cbbef70a3e2.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
yarn通过yarn.lock文件来分析和构建Nodejs的依赖环境，分析依赖生成yarn.lock需要花费大量的时间，如果仓库里面自带了满足依赖的yarn.lock文件，在CI的环节就会减少分析这一步。  <br>
<br>以下矩阵可以反应出yarn.lock对于安装依赖包的速度影响。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/bf4ebd482f4b8f59173a967765ff801f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/bf4ebd482f4b8f59173a967765ff801f.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
目前我们在流水线也默认启用了node_modules复用机制，npm也同样会受益，但即便是有npm的node_modules复用机制，大量测试后isntall的速度yarn更有优势，可以考虑考虑使用yarn install来提速。<br>
<h4>提交yarn.lock文件</h4>前面也提到yarn.lock对于Nodejs CI提速有很重要的作用，同时也可以保障协同开发的工程中的依赖一致性。yarn.lock也应该提交到代码仓库中。同时，yarn的官方也强烈建议大家提交。如果Git的.gitignore有限制，需要在放开yarn.lock允许提交。<br>
<br>本地代码测试的时候运行yarn install生成yarn.lock文件：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/6c5115a9f8efeffe1ea8760a3109491c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/6c5115a9f8efeffe1ea8760a3109491c.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>添加依赖包以及维护yarn.lock文件</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/6d32fc35d80ae7693e6cceed3597c26d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/6d32fc35d80ae7693e6cceed3597c26d.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
注意这些操作都可以自动增量更新package.json和yarn.lock中的依赖关系。为了不破坏yarn.lock的正确性，此文件不要手动去修改。需要使用上游更新后的包，要使用yarn upgrade来引用最新的上游依赖。<br>
<br>如果git merge操作导致yarn.lock发生变化，应该在本地重新生成新的yarn.lock文件后提交到Git，否则可能出现依赖异常导致安装失败。<br><br>
<h3>实验效果</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/59da9459ad53adfdf415799682c202c3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/59da9459ad53adfdf415799682c202c3.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从数据上来看，这套组合拳打下去，速度有了明显的提升。业务消耗在CI和CD的时间有了减少，也提高了整体的研发效率。如果结合业务线的项目按更细的颗粒度进一步拆分，优化不必要的依赖，优化Kubernetes的滚动更新的策略，整体的发布时间会进一步压缩，效率也会进一步提升。  <br>
<br>这里主要介绍了DevOps流水线中CI的这一个环节，整体的提速需要联动其他环节的协同优化，如果大家也有兴趣进一步了解，就在后面评论点赞给我们反馈吧。<br>
<br>希望以上内容能对有需要的人有所帮助。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/RFXb_KtRSjHcVCO-tcA5Sg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/RFXb_KtRSjHcVCO-tcA5Sg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            