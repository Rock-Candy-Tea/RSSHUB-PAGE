
---
title: 'Apache Flink 1.13.0 发布，流处理框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-317f5f6c50dfb075ca95907034b70e3e1d9.png'
author: 开源中国
comments: false
date: Tue, 11 May 2021 07:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-317f5f6c50dfb075ca95907034b70e3e1d9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Flink 1.13.0 现已发布，该版本使流处理应用像其他应用一样自然和简单地管理，只要改变并行进程的数量，就可以像其他应用程序一样扩展流媒体应用程序的运行。</p> 
<p><strong>反应式扩展</strong></p> 
<p>用户现在可以为 Flink 应用程序配置一个自动缩放器，但要在配置自动缩放器的时候注意到重新缩放的成本。有状态的流媒体应用程序必须在扩展时移动状态。要尝试反应式扩展模式，请添加 scheduler-mode: reactive 配置项，并部署一个应用程序集群（独立的或 Kubernetes）。</p> 
<p><strong>分析应用程序性能</strong></p> 
<p>Flink 1.13 带来了一个改进的背压度量系统（使用任务邮箱时间，而不是线程堆栈采样），以及一个重新设计的作业数据流的图形表示，用颜色编码和繁忙程度和背压的比例。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-317f5f6c50dfb075ca95907034b70e3e1d9.png" referrerpolicy="no-referrer"></p> 
<p>此外，Flink 1.13 还为 Web UI 添加了 CPU 火焰图，该火焰图是通过对线程堆栈痕迹的反复采样来构建的。每个方法的调用都用一个条形表示，条形的长度与它在样本中出现的次数成正比。启用后，图表会显示在所选操作者的新 UI 组件中。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4c95d17aa9ddf861c173dff5adbab868b8b.png" referrerpolicy="no-referrer"></p> 
<p><strong>使用保存点切换状态后端</strong></p> 
<p>用户现在可以在从保存点恢复时改变 Flink 应用程序的状态后端。这意味着应用程序的状态不再被锁定在应用程序最初启动时使用的状态后端。这使得初始启动 HashMap 状态后端（JVM Heap 中的纯内存）成为可能，一旦状态增长过大，就可以切换到 RocksDB 状态后端。Flink 现在有一个标准的保存点格式，所有的状态后端在为一个保存点创建数据快照时都会使用这个格式。</p> 
<p><strong>用户指定 Kubernetes 部署的 Pod 模板</strong></p> 
<p>原生的 Kubernetes 部署（Flink 主动与 K8s 对话以启动和停止 pod）现在支持自定义 pod 模板。有了这些模板，用户可以以 Kubernetes 的方式设置和配置 JobManagers 和 TaskManagers pods ，其灵活性超出了 Flink 的 Kubernetes 集成中直接内置的配置选项。</p> 
<p><strong>机器学习库移至单独的存储库</strong></p> 
<p>为了加速 Flink 的机器学习工作（流式、批处理和统一的机器学习）的发展，这项工作已经转移到 Flink 项目下的新仓库 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fflink-ml" target="_blank">flink-ml</a>。</p> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflink.apache.org%2Fnews%2F2021%2F05%2F03%2Frelease-1.13.0.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            