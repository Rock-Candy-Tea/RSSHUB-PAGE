
---
title: 'Kubernetes多集群架构探索'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/033dbc41a08126714482a425fe1a212d.png'
author: Dockone
comments: false
date: 2021-08-21 10:07:54
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/033dbc41a08126714482a425fe1a212d.png'
---

<div>   
<br><h3>为什么要使用多集群？</h3>关于多集群的使用我们主要有三方面的考虑：<br><br>
<h4>单集群限制</h4>现在Kubernetes是开发到1.2版本了，但是单集群限制目前来看还是没有改变。比如单个Node还是110，一个集群也就是5000个节点左右。根据我们的使用经验，在单集群时，1个集群内部有2000个Service时，其实我们的集群已经出现了一些瓶颈。我们都知道Service会自己产生一些Service的环境变量，当我们去创建对应的Development，然后去创建对应的Service时，发现每个Pod会产生大量的Service，当然这里边有个前提，我们的Service都在同一个namespace下面，比如在生产环境，一个namespace下的Service可能有几千个，当我们去执行某些命令时会非常卡，另外环境变量比较多的话，会影响应用的启动。<br>
<h4>多云架构</h4>有赞最开始是一个多云多机房架构，就是说我们天然最少在一个云上应该有一个机器人。<br>
<h4>容灾</h4>在我们最开始容器化的时候一朵云上只有一个集群，流量是两边都存在的。在17年~18年时出现了一个故障：我们内部有一个自研的Ingress Controller出现bug之后，入口的一个核心应用发布的时候Endpoint更新了，结果我们自研的Ingress Controller并没有把Endpoint更新到它的off stream里面，因为所有的流量基本都会经过核心应用，导致机房无法使用。因此我们就开始拆集群，最起码要保证一朵云上有两个集群。<br>
<h3>有赞多集群使用情况及存在的问题</h3>我们现在使用Kubernetes多级群主要分为4个部分：<br>
<h4>整体的部署架构</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/033dbc41a08126714482a425fe1a212d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/033dbc41a08126714482a425fe1a212d.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如上图我们内部目前是这样使用的：在不同云上的不同的机房，最上面的组件yz7是统一接入层，上文提到的提到的Ingress Controller就是和它交互的。在每一朵云上有的云我们可能直接用它的公有云，有的云可能是有托管的机房，也可能会用它的公有云。<br>
<br>每朵云最少有两个Kubernetes集群，这里不一样的地方是因为有托管还有云上的，下面是一个VK的节点，我们最开始这个地方的云是自建的，会有伸缩性受限的问题存在，在使用了开源社区的某个组件后，增加了一个虚拟节点，这个虚拟的节点其实往上套了一下，对应的它机房里边的一个公有云的一个Kubernetes的集群。因此从整体来说，在集群的层面都是可以任意扩展的。<br>
<h4>应用部署</h4>有了集群之后，如何将应用和程序部署到Kubernetes？有赞内部最开始有4个环境：daily、 QA、预发和生产4个环境，最开始的daily是给研发提供环境去验证代码；QA用于测试，其环境相对是比较稳定的，但是它连的数据库与线上环境基本是一致的，所以可以在最终发到真正的线上时，还能在预发环境进行验证。后面我们把daily环境去掉了，做了一个持续交付的环境来替代Daily的需求。  <br>
<br>应用部署方面，还有其他相关联的一些系统，比如我们内部的Ingress Controller这样的系统，其实它也是需要和Kubernetes交互的，目前来说我们内部90%以上的无状态的业务应用都已全部容器化，都是通过我们的发布系统发布到对应的Kubernetes集群。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/9167e092c692f2c0f243bfb37660f537.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/9167e092c692f2c0f243bfb37660f537.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>服务发现和暴露</h4>服务发现和暴露，主要分两块，最外面接入层的流量HTTP和内部的RPC流量。  <br>
<br><strong>HTTP</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/9da3a0bc2a1f849aaec5fc44731c2ae1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/9da3a0bc2a1f849aaec5fc44731c2ae1.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
HTTP流程：我们内部有一个统一的接入软件yz7，yz7有个组件yz7-k8s-sync，这个组件和开源Ingress Controller做的工作类似，然后将对应的Endpoint写到yz7的配置里，在内存里日更新。<br>
<br><strong>RPC</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/cb67ea127fe7daa9c4e9aaf2df3f6d24.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/cb67ea127fe7daa9c4e9aaf2df3f6d24.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
RPC服务发现最开始其实是一个大的单体应用，后面逐渐进行了拆分，微服务化，然后使用了国内用的比较多的Dubbo。我们最开始做容器化时，它的服务发现都还是依托Dubbo框架，因此刚提到的使用Macvlan有一个优势，在切容器化时，虚机和容器其实是无所谓的，都注册到Dubbo里，它的注册中心都能注册到，它的调用方也都可以调到，因为网络是可达的，这是我们微服务化后使用Dubbo的第一步。<br>
<br>第二步是我们基于Istio 1.1版本拉出来的分支做的服务发现，相当于依托Kubernetes的原数据做的服务发现，也是一个逐渐渐进的过程，所以中间也是会存在它的服务发现同时依托于Kubernetes的原数据和Dubbo的etc原数据。<br>
<br>下图其实是最终我们想要呈现的架构图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/7421c03ccbd3f8fdfb3a2bd7609a5509.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/7421c03ccbd3f8fdfb3a2bd7609a5509.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这里边相当于所有的服务注册或服务发现的数据都依托于Kubernetes里的原数据。里边的 Pilot组件就是我们基于Istio社区1.1拉出来一个分支进行迭代的。Tether组件时我们自研的，最终是要接管在容器里面进出的所有流量。它现在也提供了一些能力，比如能够通过它的接口去自己实现服务的注册。<br>
<h4>弹性伸缩</h4>弹性伸缩我们现在主要分两块：一个是应用程序的弹性伸缩，还有一个是集群的弹性伸缩。  <br>
<br>应用的弹性伸缩，首先有个前提集群的规模是可以弹性的，集群的弹性伸缩，我们现在主要做了两件事：第一个是在托管的或者叫自建的机房里，我们使用了Virtual Kubelet，让其作为一个虚拟节点存在于自建的机房里，和对应机房公有云上的Kubernetes去联通；另外我们自研了一套集群节点伸缩系统，可以在上面配置节点相对应的弹性规则。<br>
<h4>使用多集群存在的问题</h4>运维困难：我们是在多环境多云多机房，然后有N个开发者的集群，对于开发者的管理员来说是非常痛苦的。比如我们新建了一个集群，如果这份原数据需要在很多系统里都进行配置，对于运维同学来说是相当痛苦的，因为相关的系统跑不起来或者程序发不起来。第二个问题多集群在新建集群时，目前来说它这份配置需要一个check list，所有的系统都要去完成变更将这份配置给加上，这个周期是比较长的。  <br>
<br>多集群间元数据的同步：主要是workload方面，目前我们的workload是通过发布系统，逐步的向每个集群发布，如此可能会导致如果一个集群挂了，就没有办法进行发布。<br>
<h3>多集群方案探索与选择</h3>我们是在今年年初开始对业界的一些多集群管理系统进行调研：<br>
<ul><li>kubefed v2：对于我们来说，API需要重新试配，其他的一些周边或配套系统也要跟着更改，改动成本比较大。</li><li>karmada：调研过程中Karmada正好开源，非常符合我们的需求。</li><li>OpenClusterManagement：组件比较多，后期运维起来会比较麻烦，而且感觉它是OpenShift里边一个组件，后期是否会和OpenShift耦合性太强，这也是我们担心的点。</li><li>kcp：项目比较早期</li></ul><br>
<br>因此，最终我们选择了Karmada。其主要的优势有以下几个方面：<br>
<ul><li>灵活的分发策略</li><li>支持多集群间的灵活调度</li><li>可使用原生 Kubernetes API</li><li>支持自定义调度</li></ul><br>
<br>目前来说卡Karmada已经满足我们的需求了，后期我们会选择Karmada作为多集群管理的方案。<br>
<br>下图为我们期望的最终应用部署架构图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/a9506611e78def1ae1c2bedc5ff41320.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/a9506611e78def1ae1c2bedc5ff41320.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Control Plane为最上面的控制面，它是纯粹的控制面的集群，不会部署真正的workload，包含Karmada和Pandora，Pandora是放置我们内部写的operator；下面为Runtime集群，也就是我们现在的Kubernetes架构，这里有个很大的变化：之前我们做发布或其他周边系统需要和Kubernetes进行交互时，可能直接通到最下面，但改成这样的话，就不需要和下边的runtime集群去交互，如何需要交互，是和Control Plane里边的对象进行交互。这样的好处是下边的集群无论怎么变化，它在这里是可以感知和控制的，可以解决我们上文提到的一些问题。<br>
<br>下图为我们做的PaaS平台，其主要解决应用交付的问题：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/b45bd00bb77b217f6c09b9a0ee9c23a6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/b45bd00bb77b217f6c09b9a0ee9c23a6.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们期望的效果是发布系统将程序或应用分发到集群里，和Kubernetes里的API Server直接交互。上面是面向用户也就是研发人员进行应用发布动作；中间层是我们pass平台对外暴露的API Server，我们希望做的PaaS平台能将无状态应用和有状态应用都能收拢到一起。整块的话，这里有Control Plane cluster的，Sync我们会同步一些原数据，主要是给UI这一层使用，然后会同步到RDS；控制面的Control Plane集群，它里边有很多Operator，其中就包括了Karmada的countrol manager，去往下面分发，这里边workload是没有的，最下面是runtime的环境。<br>
<br>总的来说，其优点主要有：<br>
<ul><li>统一控制面，所有元数据都在控制面系统中</li><li>底层集群不可用无影响</li><li>控制系统无需感知底层集群变化</li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/PbgNy2BO70EDJqNFQlkcgA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/PbgNy2BO70EDJqNFQlkcgA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            