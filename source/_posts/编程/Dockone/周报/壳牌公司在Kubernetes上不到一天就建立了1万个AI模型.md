
---
title: '壳牌公司在Kubernetes上不到一天就建立了1万个AI模型'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220109/6a8f26edf1070c202f036bf76ea6d43b.png'
author: Dockone
comments: false
date: 2022-01-11 08:10:38
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220109/6a8f26edf1070c202f036bf76ea6d43b.png'
---

<div>   
<br>现在，壳牌能够在2个小时而不是4个星期建立数千个机器学习模型，同时能够有效缩短代码的编写时间，从2个星期缩短到4个小时。<br>
<h3>向绿色和可再生能源扩展</h3>在2015年的联合国气候变化大会上，195个国家签署了《巴黎协定》，这是一项在全球范围内减少温室气体排放的协议。该协议的长期目标是将全球温度的上升限制在工业化前水平的2摄氏度以下，并最终在21世纪下半叶达到全球净零排放。随着全球电力消耗预计在2050年翻倍，许多组织已经开始过渡到成为净零排放企业。<br>
<br>以石油巨头著称的壳牌公司近年来已将其重点从化石燃料扩展到绿色和可再生能源，如风能和太阳能。据壳牌公司机器学习平台技术主管Alex Iankoulski说，该公司的目标是在2030年前通过其可再生和能源解决方案倡议（以前的新能源）为发展中国家的1亿人提供可靠的电力供应。<br>
<br><blockquote><br>壳牌正在投资于低碳技术，包括风能和太阳能等可再生能源，电动汽车充电和氢气充电等移动性方案，以及互联的电网。壳牌正在为其新能源业务每年投资多达20亿美元，该业务专注于开发更清洁的能源解决方案。<br>
  ——Alex Iankoulski，Shell</blockquote>为了有效运营其可再生和能源解决方案，包括向客户分配电力，壳牌需要一个智能、快速和灵活的控制系统。更重要的是，该系统必须能够利用人工智能（AI），以便有效地管理计算和存储资源。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220109/6a8f26edf1070c202f036bf76ea6d43b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220109/6a8f26edf1070c202f036bf76ea6d43b.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>壳牌公司的能源供应链（<a href="https://www.youtube.com/watch?v=ick5hI5YI0k&list=PLj6h78yzYM2Nd1U4RMhv7v88fdiFqeYAP&index=146">Image credit</a>）</em><br>
<br>壳牌公司依靠Arrikto的MLOps平台来使用Kubeflow，这是一个开源项目，旨在使Kubernetes上的机器学习（ML）工作流可移植和可扩展。此外，建立在Kubernetes之上将使壳牌公司能够在容器的帮助下快速启动和关闭环境。“Kubernetes和机器学习的结合实际上是天作之合，”Arrikto的社区和营销副总裁Jimmy Guerrero解释说。<br>
<br><blockquote><br>首先，容器允许我们在笔记本电脑上创建测试和试验机器学习模型。我们非常清楚，我们可以使用容器将这些相同的模型带到生产中。这里的想法并不新鲜——我们想一次编写，复制，然后到处运行。其次，笔记本电脑上的机器学习工作流程可能完全用一种语言编写，比如说Python，但当我们把这些模型带到生产中时，我们可能会想与各种不同的服务和应用程序进行交互。这些都是像数据管理、安全、前端可视化等方面的东西，在这里我们可能想采用一个基于微服务的架构。在这里，对我们来说用Kubernetes来实现是一件轻而易举的事情。<br>
  ——Jimmy Guerrero，Arrikto</blockquote>然而，大规模部署人工智能并非没有问题。根据Alex的描述，在为壳牌的可再生和能源解决方案建立基础时，存在多种技术挑战。<br>
<ul><li><strong>基础设施</strong>需要是云原生的且与云厂商无关的。通过这种方式，如果平台必须在不同的云服务上或同时在多个云服务上运行，代码就不需要重写了。</li><li><strong>部署</strong>必须是可重复的、可审计的和可逆的，使开发人员能够检查公司系统中运行的内容以及它是如何被部署到那儿的。</li><li><strong>扩展性</strong>要保证系统能够运行在各种不同大小规模的硬件和集群中。软件应该在一台笔记本电脑上和大型云服务中运行良好。</li><li><strong>工具</strong>应该是基于网络和自我服务的，使运营团队能够专注于自动化，而不是重复的手工任务。</li><li><strong>计算</strong>资源必须是动态分配的。在计算资源上运行的工作负载应该是有弹性的和可重复的。</li><li><strong>存储</strong>必须是高速和具有成本效益的，以实现存储和计算资源的解耦。</li><li><strong>数据</strong>在任何时候都是安全的，但对授权用户是可用的。它还应该是版本化的，因此可以跟踪变化并在必要时进行恢复。安全必须是端到端的企业级。</li><li><strong>编排</strong>必须是透明的，不会对用户造成干扰。</li></ul><br>
<br><h3>在Kubernetes上运行</h3>壳牌在Amazon Elastic Kubernetes Service（EKS）上为其可再生能源和能源解决方案部署了基础设施。 Kubernetes API是用于编排工作负载的通用语言，与云服务无关。<br>
<br>Arrikto的首席技术官和联合创始人<a href="https://www.linkedin.com/in/vkoukis/">Vangelis Koukis</a>指出，通过实施<a href="https://about.gitlab.com/topics/gitops/">GitOps</a>方法，团队可以以可重复的方式在不同的Kubernetes集群之上进行部署。<br>
<br><blockquote><br>一切都从Git仓库开始。我们选择不使用kfctl工具，所以我们可以用最简单的Kubernetes原生的应用清单的方式进行部署。因此，我们支持带回滚的无缝升级。<br>
  ——Vangelis Koukis，Arrikto</blockquote><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220109/837259755b8d7adbc82e3a42ea522d65.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220109/837259755b8d7adbc82e3a42ea522d65.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>通过GitOps部署（<a href="https://static.sched.com/hosted_files/kccncna20/ea/KubeConVirtual_Nov18_2020_MachineLearningOnKubernetesAtShell_AlexIankoulski_VangelisKoukis_2.pdf">Image credit</a>）</em><br>
<br>GitOps将<a href="https://en.wikipedia.org/wiki/Infrastructure_as_code">基础设施作为代码</a>，基础设施的状态对应于仓库中的提交。<br>
<br>利用<a href="https://microk8s.io/">MicroK8s</a>等工具，轻型工作负载可以在一台笔记本电脑上运行。对于较重的工作负载，亚马逊EKS会根据需求自动进行无缝扩展。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220109/2522666b0c11f12f795b61557c665f51.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220109/2522666b0c11f12f795b61557c665f51.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>通过GitOps升级（<a href="https://static.sched.com/hosted_files/kccncna20/ea/KubeConVirtual_Nov18_2020_MachineLearningOnKubernetesAtShell_AlexIankoulski_VangelisKoukis_2.pdf">Image credit</a>）</em><br>
<br>通过遵循<a href="https://www.altoros.com/blog/devops-five-key-challenges-and-five-tips/">DevOps</a>模式，工具被转移到左边，使开发人员能够运行他们自己的Visual Studio代码服务器，在Git存储库中管理代码，并最终在Kubeflow上运行工作负载。<br>
<br>为了使计算资源具有弹性和可重复性，团队在Kubernetes Pods内使用基于Docker镜像的容器。<br>
<h3>数据管理和安全性</h3>通过将存储从亚马逊弹性文件系统（EFS）转移到使用Arrikto的数据管理平台Rok提供的本地和挂载文件系统，团队可以生成成千上万的特定时间点的快照，为工作负载提供端到端的可重复性。<br>
<br><blockquote><br>我们来以一个时间机器为例。假设我们对notebook服务器每10分钟快照一次。你可以回到过去，重现你运行的所有实验的数据。快照也可以发生在一个管道的每一步，所以你可以确切地知道是什么系列的事件导致了一个特定模型的产生。于是，你可以调查任何结果的偏差。<br>
  ——Vangelis Koukis，Arrikto</blockquote>使用Rok，团队可以在不同地区的多个集群中管理存储。Vangelis解释说，每个集群作为一个本地独立的对象存储。Rok Registry能够创建具有细粒度访问控制的私有和公共组。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220109/7233ad17b8faa1fc760007e61dc97284.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220109/7233ad17b8faa1fc760007e61dc97284.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>与Rok共享数据集和环境（<a href="https://static.sched.com/hosted_files/kccncna20/ea/KubeConVirtual_Nov18_2020_MachineLearningOnKubernetesAtShell_AlexIankoulski_VangelisKoukis_2.pdf">Image credit</a>）</em><br>
<br>在性能方面，与100GB的亚马逊EFS实例相比，使用非易失性存储器标准（NVMe）固态硬盘（SSD）的标准m5d.4xlarge实例的每秒读取输入/输出操作（IOPS）超过10倍，写入IOPS为400倍。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220109/c03e1340b3315647544e9ee830eab0e6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220109/c03e1340b3315647544e9ee830eab0e6.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>本地存储更快（<a href="https://static.sched.com/hosted_files/kccncna20/ea/KubeConVirtual_Nov18_2020_MachineLearningOnKubernetesAtShell_AlexIankoulski_VangelisKoukis_2.pdf">Image credit</a>）</em><br>
<br>至于安全问题，团队实施了单点登录（SSO）、单点注销（SLO）、集中认证、基于命名空间的隔离和共享命名空间。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220109/0246c68e7e9b7530215df2118b29cf32.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220109/0246c68e7e9b7530215df2118b29cf32.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>带有SSO/SLO的端到端安全（<a href="https://static.sched.com/hosted_files/kccncna20/ea/KubeConVirtual_Nov18_2020_MachineLearningOnKubernetesAtShell_AlexIankoulski_VangelisKoukis_2.pdf">Image credit</a>）</em><br>
<br>此外，利用OpenID Connect（OIDC）AuthService，该团队将Kubeflow扩展为OIDC客户端。OIDC AuthService与Istio和Envoy代理紧密结合。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220109/286a4ed3e8ca9f70103b4db1e68e1455.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220109/286a4ed3e8ca9f70103b4db1e68e1455.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>实施Kubeflow安全（<a href="https://static.sched.com/hosted_files/kccncna20/ea/KubeConVirtual_Nov18_2020_MachineLearningOnKubernetesAtShell_AlexIankoulski_VangelisKoukis_2.pdf">Image credit</a>）</em><br>
<h3>利用Kubeflow进行快速建模</h3>有了Kubeflow，团队可以快速建立模型，并利用数据帮助优化与壳牌的可再生和能源解决方案有关的操作。据壳牌的首席数据科学家Masoud Mirmomeni说，Kubeflow给公司带来了三大优势。<br>
<br>首先，Kubeflow提供了一个自助服务模式，使数据科学家能够获得计算能力和存储，以及在安全的云环境中使用预配置的ML工具包。<br>
<br><blockquote><br>现在，我们可以拥有所有这些基础能力，从零开始轻松地做机器学习项目。如果你想用老式的方法做这件事，那将需要几周甚至几个月的时间。现在，我们可以在几分钟内做到这一点。<br>
  ——Masoud Mirmomeni，Shell</blockquote>其次，在Kubeflow自动管线引擎（<a href="https://github.com/kubeflow-kale/kale">KALE</a>）的帮助下，数据科学家可以简单地将他们的代码传递给运营团队。这减少了将ML代码推向生产所需的时间。<br>
<br>第三，由于壳牌使用的是Kubernetes，计算和存储的<strong>资源很容易被共享</strong>。例如，Notebooks服务器使用的计算能力受到监控，当资源闲置时，它们会被释放，并可用于其他工作负载。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220109/c59c1b7e47e11b5f95556f1e5ed28b5b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220109/c59c1b7e47e11b5f95556f1e5ed28b5b.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>壳牌公司机器学习工作流程的一个例子（<a href="https://static.sched.com/hosted_files/kccncna20/ea/KubeConVirtual_Nov18_2020_MachineLearningOnKubernetesAtShell_AlexIankoulski_VangelisKoukis_2.pdf">Image credit</a>）</em><br>
<br><blockquote><br>Kubeflow将为数据科学家和机器学习工程师创造非常高效的平台，以进行合作，分享想法，并从他们自己的项目和经验中学习。它还将通过有效地管理计算和存储资源来降低模型建设的成本。<br>
  ——Masoud Mirmomeni，Shell</blockquote>通过Kubeflow，壳牌大大减少了数据科学家和ML工程师建立模型的时间。以前，建立10,000个模型所需的时间将涉及两周的编码和四周的执行。现在，该团队可以在不到四个小时内编写代码，并在两个小时内建立所有模型。<br>
<h3>想要了解更多细节？看视频！</h3>壳牌的Alex Iankoulski和Arrikto的Vangelis Koukis解释了壳牌的可再生和能源解决方案的基础设施是如何建立的。<br>
<br><a href="https://youtu.be/ick5hI5YI0k" rel="nofollow" target="_blank">https://youtu.be/ick5hI5YI0k</a><br>
<br><strong>原文链接：<a href="https://www.altoros.com/blog/shell-builds-10000-ai-models-on-kubernetes-in-less-than-a-day/">Shell Builds 10,000 AI Models on Kubernetes in Less than a Day</a>（翻译：小灰灰）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            