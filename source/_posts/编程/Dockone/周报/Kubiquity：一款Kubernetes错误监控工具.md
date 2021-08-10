
---
title: 'Kubiquity：一款Kubernetes错误监控工具'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210808/474354dd9f711ae43489ed17f72480a7.png'
author: Dockone
comments: false
date: 2021-08-10 01:53:15
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210808/474354dd9f711ae43489ed17f72480a7.png'
---

<div>   
<br><h3>什么是Kubiquity？</h3>Kubiquity是一个基于<a href="https://github.com/electron/electron">Electron</a>的Kubernetes健康监测应用。它结合了Kubernetes命令行工具和Prometheus指标服务器来获取集群的实时信息。用户可以通过实时跟踪每个集群的事件日志历史以及CPU和内存的使用情况，来追踪集群的异常情况。<br>
<h3>我们为什么要发明新的轮子?</h3>Kubernetes缺乏强大的错误跟踪；此外，Kubernetes开发人员希望有一个图形用户界面（GUI）来与他们的集群交互，进而分析集群。通过将Kubernetes事件日志从命令行转移到Kubiquity，K8sM8s团队建立了一个易于使用且直观的工具，供开发人员搜索和保存相关的事件。该应用程序还结合了Prometheus指标监控，提供详细的、实时的内存使用情况，以便开发人员可以看到内存高峰，并防止应用因内存不足（OOM）的而被误杀。<br>
<h3>Kubiquity如何工作？</h3>Kubiquity能连接到现有的集群，利用kubectl和Prometheus查询语句，从活跃的Kubernetes集群检索实时事件日志和资源监控指标。事件日志与Pod的CPU和内存使用量一起显示在Kubiquity应用程序里。这些信息在本地存储在Electron的JSON存储中，用户可以对事件日志进行分类和过滤，并将相关日志下载到CSV文件中，以便进一步分析或后续的操作。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210808/474354dd9f711ae43489ed17f72480a7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210808/474354dd9f711ae43489ed17f72480a7.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210808/d89cea15e2e286bd7454c2c99bf7d3eb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210808/d89cea15e2e286bd7454c2c99bf7d3eb.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210808/7b8f0836ca3148930e8ffc97ad99aa69.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210808/7b8f0836ca3148930e8ffc97ad99aa69.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>如何开始使用Kubiquity？</h3><ol><li>首先，启动一个Kubernetes集群</li><li>如果还没有使用Prometheus，请按照以下步骤安装并运行Prometheus：<a href="https://prometheus-community.github.io/helm-charts"></a><a href="https://prometheus-community.github.io/helm-charts" rel="nofollow" target="_blank">https://prometheus-community.github.io/helm-charts</a></li><li>在这里下载Kubiquity：<a href="https://github.com/oslabs-beta/Kubiquity/releases/tag/v1.0.0"></a><a href="https://github.com/oslabs-beta/Kubiquity/releases/tag/v1.0.0" rel="nofollow" target="_blank">https://github.com/oslabs-beta ... 1.0.0</a></li><li>启动Kubiquity</li><li>就这么简单</li></ol><br>
<br><h3>未来的路线图</h3>Kubiquity一直在寻求优化和改进，为开发者提供更多的功能。下面是该团队正在筹备的一些功能。<br>
<ul><li>MacOS的兼容性</li><li>通过保存某一时刻集群状态的快照从而允许时间回溯调试</li><li>GitHub集成</li><li>跟踪及存储内存和CPU的长期使用情况</li><li>基于警告和错误的建议行为</li><li>为用户提供将数据持久化到非本地数据库的选项</li></ul><br>
<br><h3>与开发者联系</h3>随着Kubernetes的需求和普及，K8sM8s团队致力于创造加速和促进Kubernetes和容器开发的产品。如果你想了解更多关于Kubiquity的信息，请访问我们的网站或给我们发邮件：<a href="mailto:kubiquityapp@gmail.com">kubiquityapp@gmail.com</a>。Kubiquity是一个开源工具——如果你想了解更多信息或做出贡献，我们欢迎所有开发者访问和Fork我们的<a href="https://github.com/oslabs-beta/Kubiquity">GitHub项目</a>。谢谢，开发愉快！<br>
<br><strong>原文链接：<a href="https://medium.com/@kubiquityapp/kubiquity-a-kubernetes-error-monitoring-tool-385b41bea0c0">Kubiquity: A Kubernetes Error Monitor Tool</a>（翻译：小灰灰）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            