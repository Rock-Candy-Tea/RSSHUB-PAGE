
---
title: 'IBM的ModelMesh走向开源 使开发者能够大规模部署AI模型'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1013/0bd948b68147add.jpg'
author: cnBeta
comments: false
date: Wed, 13 Oct 2021 13:19:10 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1013/0bd948b68147add.jpg'
---

<div>   
模型服务是AI用例的一个关键组成部分。它涉及从人工智能模型中提供推论，以响应用户的请求。那些涉足企业级机器学习应用的人知道，通常不是一个模型提供推论，而是实际上有数百甚至数千个模型在同步运行。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1013/0bd948b68147add.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1013/0bd948b68147add.jpg" title alt="1554122456_machine_learn_story.jpg" referrerpolicy="no-referrer"></a></p><p>这在计算上是一个非常昂贵的过程，因为你不可能在每次要提供请求时都启动一个专用容器。这对在Kubernetes集群中部署大量模型的开发者来说是一个挑战，因为存在一些限制，如允许的最大荚数和IP地址以及计算资源分配。</p><p>IBM通过其专有的ModelMesh模型服务管理层为Watson产品（如Watson Assistant、Watson Natural Language Understanding和Watson Discovery）解决了这个难题。由于这些模型已经在生产环境中运行了几年，ModelMesh已经针对各种场景进行了全面测试。现在，IBM正在将这一管理层与控制器组件以及为模型服务的运行时间一起贡献给开放源码社区。</p><p>ModelMesh使开发者能够在Kubernetes之上以"极端规模"部署AI模型。它具有缓存管理的功能，也是一个平衡推理请求的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,699,700" target="_blank">路由器</a>，模型被智能地放置在pod中，对临时中断提供弹性。ModelMesh的部署可以轻松升级，无需任何外部协调机制。它自动确保一个路由新请求到它之前已经完全更新和加载。</p><p>在用一些统计数据解释ModelMesh的可扩展性时，IBM表示：</p><blockquote><p>一个部署在单个工人节点8vCPU x 64G集群上的ModelMesh实例能够打包20K个简单字符串模型。在密度测试的基础上，我们还对ModelMesh的服务进行了负载测试，通过发送成千上万的并发推理请求来模拟一个高流量的假日季节场景，所有加载的模型都以个位数毫秒的延迟进行响应。实验表明，单个工人节点支持20k个模型，每秒最多可进行1000次查询，并以个位数毫秒的延迟响应推理任务。</p></blockquote><p>IBM将ModelMesh贡献给了KServe GitHub组织，该组织早在2019年就由IBM、Google、彭博社、英伟达和Seldon联合开发。</p><p><strong>您可以在下面提到的各种GitHub存储库中查看ModelMesh的运用与实现：</strong></p><p><a href="https://github.com/kserve/modelmesh-serving">模型服务控制器</a></p><p><a href="https://github.com/kserve/modelmesh">用于协调模型放置和路由的 ModelMesh 容器 运行时适配器</a></p><p><a href="https://github.com/kserve/modelmesh-runtime-adapter">ModelMesh运行时适配器</a> - 在每个模型服务 pod 中运行的容器，充当 ModelMesh 和第三方模型服务器容器之间的中介,它还包含了负责从存储中检索模型的"拉动器"逻辑。</p><p><a href="https://github.com/triton-inference-server/server">triton-inference-server</a> - NVIDIA的Triton推理服务器</p><p><a href="https://github.com/SeldonIO/MLServer">seldon-mlserver</a> - Python MLServer，是KFServing的一部分</p>   
</div>
            