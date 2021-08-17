
---
title: '带你全景俯瞰云原生与 Kubernetes'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/ad832ff0579678c70d89248d8f7dd5f2.jpeg'
author: Dockone
comments: false
date: 2021-08-17 04:09:17
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/ad832ff0579678c70d89248d8f7dd5f2.jpeg'
---

<div>   
<br><h3>前言</h3>互联网后台架构技术的发展一日千里。身处技术变革浪潮的后台同学，应该都深切地感受到了云原生技术在公司内外的蓬勃发展。<strong>云原生技术正在逐渐成为后台工程师与架构师们的必修课，而 Kubernetes 正是云原生的基石，聚光灯下的焦点。</strong><br>
<br>Kubernetes 是一个被写了很多次的主题，本文并不希望事无巨细地阐述其所有内容。事实上，仅凭一篇文章的篇幅也无法写透这个宏大的主题。即便写出来，也会变成毫无重点的堆砌，很难快速消化吸收。因此，<strong>本文更倾向于作为 Kubernetes 入门的一张 Big Picture，记录笔者在接触 Kubernetes 的过程中关注的那些问题点。</strong><br>
<br><strong>由于从业经历的不同，不同人在陈述同一个主题时，切入的角度往往有所不同。举例来说：不同的互联网公司（特别是头部公司），通常有自己偏爱的技术文化。譬如在进程间通信这个方向，Amazon 就比较推崇 Service Interfaces（没办法，老板喜欢）。而国内某大厂的同学在做技术选型时，则更偏爱采用 Shared Memory。</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210815/ad832ff0579678c70d89248d8f7dd5f2.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/ad832ff0579678c70d89248d8f7dd5f2.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>何为云原生与云原生应用？</h3><strong>学习一个事物时，通常都需要先做基础的两点功课：首先要了解它的背景与外延，其次了解它的内涵</strong>。首先了解它的外延，是为了分辨它在整张 Big Picture 中的位置。Kubernetes 的背景，就是云原生技术。于是，我们不禁要问几个问题：<br>
<h4>何为云原生？</h4>Cloud Native 最早是在 2013 年由 Pivotal 公司的 Matt Stine 提出的。2015 年 CNCF（Cloud Native Computing Foudation，云原生计算基金会）成立。官方发布的云原生 v1.0 定义是：“云原生技术有利于各组织在公有云、私有云和混合云等新型动态环境中，构建和运行<strong>可弹性扩展</strong>的应用。<strong>云原生的代表技术包括容器、服务网格、微服务、不可变基础设施和声明式 API</strong>。这些技术能够构建<strong>容错性好、易于管理和便于观察</strong>的<strong>松耦合系统</strong>。结合可靠的自动化手段，云原生技术使工程师能够轻松地对系统作出频繁和可预测的重大变更。” 在该定义中，容器、不可变基础设施、声明式 API 都与 Kubernetes 直接相关。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210815/9f27d0e12bc2c54ed4be4cb240af4eb5.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/9f27d0e12bc2c54ed4be4cb240af4eb5.jpeg" class="img-polaroid" title="2.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>何为云原生应用？</h4>按字面意思的理解，云原生应用是指在云上生长出来的应用，云上的“原住民”。然而这也没有解释它与传统应用的区别，也没有说明它为何更“高级”？2017 年，Red Hat 架构师、《Kubernetes Patterns》的作者 Bilgin Lbryam 给云原生应用下了一个比较准确而连贯的定义（参见文献）：<br>
<ul><li><strong>以微服务原则进行划分设计。</strong>  </li><li><strong>使用 DevOps 和 CI/CD 的方式进行开发和交付。</strong>  </li><li><strong>以容器技术进行打包发布。</strong>  </li><li><strong>在云基础设施上运行并被调度。</strong></li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210815/2b4b62065f164b00320fe8dd3d2e489e.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/2b4b62065f164b00320fe8dd3d2e489e.jpeg" class="img-polaroid" title="3.jpeg" alt="3.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>小结</h4>云原生是当前互联网后台一个非常具有前景的技术领域。首先，这片土地足够广阔，可以让每一个后台同学去学习与深耕。其次，这个方向也足够主流与实用，看看业内如火如荼的各种技术峰会、培训课、岗位招聘。云原生并不是那种没有实用价值的“屠龙之技”，值得深入去钻研。<br>
<h3>何为 Kubernetes？提供什么能力？解决什么问题？</h3>本节来了解 Kubernetes 的内涵，即它涵盖了哪些内容，提供了哪些能力。<strong>如果说 Istio 是一艘快艇的话，Kubernetes 就是一艘巨轮，驰骋在更广阔的海域</strong>。用最简短的语言描述 Kubernetes，<strong>可以说，Kubernetes 是一个容器编排系统（Container Ochestration）。那么，“编排”二字包含了哪些核心内容？</strong><br>
<ul><li><strong>镜像管理（Image）</strong>：管理与分发。</li><li><strong>容器管理（Container）</strong>：创建、调度、状态监控、自动伸缩。</li><li><strong>服务管理（Service）</strong>：发布升级、服务发现与负载均衡。</li><li><strong>配置管理（Config）</strong>：ConfigMap 是普通配置，Secret 是敏感数据。配置也是非常重要的，有很多细节可以深入展开。</li><li><strong>流量治理（Traffic）</strong>：日志、监控、鉴权等。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210815/6caeeddf562d7bcd93107cccb46300a3.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/6caeeddf562d7bcd93107cccb46300a3.jpeg" class="img-polaroid" title="4.jpeg" alt="4.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Kubernetes 集群架构</h3>上文是从外部视角去描述并确定我们讨论的这个主题，Kubernetes 的边界。本节将描述 Kubernetes 集群的内部结构。相信后台同学看完之后，都会有似曾相识的感觉。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210815/eda7c54ca80c696dcd93854800c2dddb.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/eda7c54ca80c696dcd93854800c2dddb.jpeg" class="img-polaroid" title="5.jpeg" alt="5.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>Kubernetes 的架构是非常经典的 Master-Worker 架构模式</strong>，我们可以借此机会复习下互联网大规模分布式系统的设计思路。<strong>Master 相当于大脑和心脏，负责接收外部请求、管理与调度 Worker 节点。Worker 相当于四肢，每一台 Worker 都干着相同的工作，随时可以被踢除或加入，以实现横向伸缩</strong>。自 Google 在 2003 到 2006 年连续发布了著名的“三驾马车”论文之后，业界数不清的分布式系统均是采用这套架构。<br>
<h4>Master 组件</h4><ul><li><strong>kube-apiserver</strong>：对外暴露可以操作整个 Kubernetes 集群的 REST API。</li><li><strong>kube-scheduler</strong>：负责调度 Worker 上的 Pods。</li><li><strong>kube-controller-manager</strong>：管理各种 Kubernetes 定义的 controller。</li><li><strong>etcd</strong>：Key-Value 存储组件，采用 Raft 协议，存储集群的各种状态数据，包括配置、节点、Pod 等。</li></ul><br>
<br><h4>Worker/Node 组件</h4><ul><li><strong>kubelet</strong>：是一个 Agent，监控 Node 上的 container 是否正常运行。</li><li><strong>kube-proxy</strong>：操纵机器上的 iptables 网络规则，执行转发。</li><li><strong>container runtime</strong>：容器运行的基础环境，负责下载镜像与运行容器。</li></ul><br>
<br><h3>问答系列：Questions about Kubernetes？</h3><strong>真理越辩越明。很多看似理所当然的东西，背后都是作者们经过深思熟虑后的选择。</strong>  想对某个技术领域有深入了解，需要日夜泡在其中。一个比较实用的方式是不停地对自己发问，姑且称之为“问题反馈闭环”。按照国外大佬们的造词功力，可能叫做“沉思录”。前面几个小节只是一枚敲门砖，可以说是让我们站在门口。只有不断发问与复盘，才能慢慢迈过门槛，走进深水区。<br>
<h4>有了 Kubernetes，为何还需要 Istio？</h4>Kbernetes 并不提供精细化的流量调度能力，例如精细化路由、分布式限流等。<br>
<h4>GKE（Google Kubernetes Engine）与 Kubernetes 的区别？</h4>GKE 只是托管 Kubernetes 集群的一个平台，面向企业与用户提供快速搭建与维护自己 Kubernetes 集群的能力。业界还有阿里的 ACK，腾讯的 TKE，华为的 CCE 等竞品。有个说法很形象：Kubernetes 只是一套毛坯样板，而像 GKE 这样的平台则相当于房地产商，开发并出售一套套精装修的商品房，让你可以拎包入住。<br>
<ul><li><strong>GKE 是开箱即用（Out-of-Box）的</strong>：做好了控制台页面，客户只需要点击就能完成自己的 Kubernetes 集群的创建。</li><li><strong>GKE 是多租户的</strong>：面向不同的企业和用户。</li></ul><br>
<br><h4>何为不可变基础设施（Immutable Infrastructure）？</h4>不得不佩服西方人的抽象能力。具体定义参见：<a href="https://blog.csdn.net/chaocai2004/article/details/103827372" rel="nofollow" target="_blank">https://blog.csdn.net/chaocai2 ... 27372</a><br>
<h4>何为声明式 API（Declarative API）？</h4>同样是云原生的八大原则之一。提起声明式，是不是想起了 SQL 这款声明式查询语言？参见：<a href="https://blog.csdn.net/KevinBetterQ/article/details/104012293" rel="nofollow" target="_blank">https://blog.csdn.net/KevinBet ... 12293</a><br>
<h4>一个 Kubernetes 集群的最大规模（最多可以容纳多少 Node、Pod、Container）？</h4>Kubernetes 官方有一个页面专门回答了这个问题，参见：<a href="https://kubernetes.io/docs/setup/best-practices/cluster-large/" rel="nofollow" target="_blank">https://kubernetes.io/docs/set ... arge/</a>。可以进一步追问这个问题，制约集群规模的瓶颈是哪个部分？CPU/存储/数据同步？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210815/0f94ded922185eab0b6394b4f6181805.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/0f94ded922185eab0b6394b4f6181805.jpeg" class="img-polaroid" title="6.jpeg" alt="6.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>为何推荐一个容器只部署一个进程？</h4>最主要应该还是设计思想的考虑，就是倡导一个容器只做一件事。其次是为了解耦，因为在同一个容器内，一个进程的挂掉会导致容器杀掉其他所有进程。<br>
<h4>同一个 Pod 内的容器可否使用共享内存通信？</h4>可以。同一个 Pod 内的容器共享同一个 IPC 命名空间，它们可以使用标准的进程间通信方式来互相通信，比如“SystemV 信号量”与“POSIX 共享内存”。<br>
<h4>同一个 Pod 内的容器可否使用 Unix Domain Socket 通信？</h4>可以。同一个 Pod 内的容器是共享网络与存储的。因此，不仅可以使用 UDS 通信，也可以支持部署一个日志 Agent 采集同一个 Pod 内的业务服务的日志。<br>
<h4>Kubernetes 能否根据机器负载进行自动扩缩容，而不是人工调整 replica 数量？</h4>可以。该特性称作 HPA（Horizontal Pod Autoscaling），还有一个与之对称的概念 VPA（Vertical Pod Autoscaling）。<br>
<h4>Kubernetes 为何选择 etcd 作为数据存储，而不是其他分布式 KV 存储？</h4>Kubernetes 使用 etcd 存储集群的 API objects、服务发现、配置与状态数据。etcd 拥有如下特点，可以说是一个比较全面的选手：<br>
<ul><li><strong>持久化能力</strong>：有些 KV 缓存并不具备该能力，比如 memcache。</li><li><strong>数据一致性</strong></li><li><strong>高可用</strong></li><li><strong>高性能</strong></li><li><strong>安全性</strong>：支持基于 TLS 与 SSL 的鉴权。 也可以看看 etcd 官网自己是怎么说的。最后可能还有一点，etcd 是使用 Golang 开发的，是 Clouad Native 阵营里的“自己人”。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210815/c09adb04a704afcb0880eed88626ab47.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/c09adb04a704afcb0880eed88626ab47.jpeg" class="img-polaroid" title="7.jpeg" alt="7.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>小结</h3>本文提供了一个切入 Kubernetes 的角度，在一定程度上破除“Kubernetes 很复杂”的印象。为了避免篇幅过长，本文重点回答了 What 与 Why 的问题（什么是 Kubernetes？为什么需要它？拿它来做什么？），而没有回答 How 的问题。距离 Kubernetes v1.0 发布已经过去了 6 年，这片水面下的冰山不可谓不深，需要上下求索。万里长征第一步，相信我们已经有了一个不错的开始。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/xMlvQzfgFZGgghV31tTVyw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/xMlvQzfgFZGgghV31tTVyw</a><br>
<br>作者：delphisfang，腾讯全民 K 歌基础架构团队后台开发工程师。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            