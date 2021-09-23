
---
title: 'topic - top in container, 容器版本的top'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210916/b12aac494023e29df793cb9342be7881.png'
author: Dockone
comments: false
date: 2021-09-23 04:09:56
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210916/b12aac494023e29df793cb9342be7881.png'
---

<div>   
<br>推荐一个容器中查看系统信息的工具<a href="https://github.com/silenceshell/topic">topic</a>。<br>
<br>容器通过cgroups和namespace实现了资源的轻量级隔离和限制，但容器中的/proc文件实际上是宿主机的，因此在执行top命令查看容器运行信息时，部分指标显示不正确，例如启动时间、用户数、平均负载、cpu使用率、内存使用率。<br>
<br>目前比较通用的解决方案是通过lxcfs，将容器中相应的文件通过fuse劫持read调用，在打开时显示为容器信息，从而统一解决各种系统状态诊断工具的问题。<br>
<br>考虑到部署lxcfs有一定的成本，topic(top in container)的思路则是改造top命令，去适配容器，读取容器中反映真实运行情况的系统文件，从而展示正确的容器运行信息，对于用户而言成本更低。<br>
<br>如下，在一个1c 1Gi的容器中运行<code class="prettyprint">stress --cpu 2</code>，通过topic和top查看容器的运行状态：<br>
<br>topic:<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210916/b12aac494023e29df793cb9342be7881.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210916/b12aac494023e29df793cb9342be7881.png" class="img-polaroid" title="top.png" alt="top.png" referrerpolicy="no-referrer"></a>
</div>
<br>
top:<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210916/37d5437f73898a1aa15a6b831f36f09c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210916/37d5437f73898a1aa15a6b831f36f09c.png" class="img-polaroid" title="topic.png" alt="topic.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>可以看到，topic比较好的解决了容器运行信息的问题：<br>
<ul><li>topic查看的load average是2.03，而top查看到的是1.31（实为宿主机的load average）</li><li>topic查看到的CPU使用率，其us为99.8%，而top查看到的是13.2%（实为宿主机的us信息）</li><li>topic查看到的Mem是1Gi，而top查看到的是16Gi（实为宿主机的内存信息）</li><li>topic查看到的user数是11，而top查看到的user数是1（实为宿主机的当前登录用户数）</li><li>topic查看到的容器运行时间为2days 10:35，而top查看到的是20days 1:57（实为宿主机的运行时间）</li><li>topic和top的进程相关信息显示基本一致。</li></ul><br>
<br>如果您需要试用，可以<a href="https://silenceshell-1255345740.cos.ap-shanghai.myqcloud.com/topic/topic">下载</a>topic到容器中运行（记得加上执行权限），好用可以给个Star ^_^<br>
项目地址 <a href="https://github.com/silenceshell/topic"></a><a href="https://github.com/silenceshell/topic" rel="nofollow" target="_blank">https://github.com/silenceshell/topic</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            