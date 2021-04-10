
---
title: 'Knative 基于流量的灰度发布和自动弹性实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/5cdf48d38d358deb6d911cab62acf9c4.png'
author: Dockone
comments: false
date: 2021-04-10 12:10:05
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/5cdf48d38d358deb6d911cab62acf9c4.png'
---

<div>   
<br>作者| 李鹏（元毅）<br>
来源 | <a href="https://mp.weixin.qq.com/s/62dsJSvWgVKdnIcSu0JjIQ">阿里巴巴云原生公众号</a><br>
<br><h1>Knative</h1>Knative 提供了基于流量的<strong>自动扩缩容能力</strong>，可以根据应用的请求量，在高峰时自动扩容实例数；当请求量减少以后，自动缩容实例，做到自动化地节省资源成本。此外，Knative 还提供了基于流量的<strong>灰度发布能力</strong>，可以将流量的百分比进行灰度发布。<br>
<br>在介绍 Knative 灰度发布和自动弹性之前，先带大家了解一下 ASK Knative 中的<strong>流量请求机制</strong>。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210406/5cdf48d38d358deb6d911cab62acf9c4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/5cdf48d38d358deb6d911cab62acf9c4.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>如上图所示，整体的流量请求机制分为以下部分：<br>
<ul><li>左侧是 Knative Service 的版本信息，可以对流量设置百分比；下面是路由策略，在路由策略里，通过 Ingress controller 将相应的路由规则设置到阿里云 SLB；</li><li>右侧是对应创建的服务版本 Revision，在版本里对应有 Deployment 的资源，当流量通过 SLB 进来之后，直接根据相应的转发规则，转到后端服务器 Pod 上。</li></ul><br>
<br>除了流量请求机制外，上图还展示了相应的弹性策略，如 KPA、HPA 等。<br>
<br><h1>Service 生命周期</h1>Service 是直接面向开发者操作的资源对象，包含两部分的资源：Route 和 Configuration。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210406/a5065401e04f3652e834d07ae1104ba7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/a5065401e04f3652e834d07ae1104ba7.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>如上图所示，用户可以通过配置 Configuration 里面的信息，设置相应的镜像、内容以及环境变量信息。<br>
<br><h2>1. Configuration</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210406/1830ec81c0c738e8d44f66f42490d2b8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/1830ec81c0c738e8d44f66f42490d2b8.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Configuration 是：<br>
<ul><li>管理容器期望的状态；</li><li>类似版本控制器，每次更新 Configuration 都会创建新的版本（Revision）。</li></ul><br>
<br>如上图所示，与 Knative Service 相比较，Configuration 和它的配置很接近，Configuration 里配置的就是容器期望的资源信息。<br>
<br><h2>2. Route</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210406/8a8e7767542ee227242aee1e18fe6350.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/8a8e7767542ee227242aee1e18fe6350.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Route 可以：<br>
<ul><li>控制流量分发到不同的版本（Revision）；</li><li>支持按照百分比进行流量分发。</li></ul><br>
<br>如上图所示，一个 Route 资源，下面包括一个 traffic 信息，traffic 里面可以设置对应的版本和每个版本对应的流量比例。<br>
<br><h2>3. Revision</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210406/28039b929da0d202dfea6f42a958b24d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/28039b929da0d202dfea6f42a958b24d.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>一个 Configuration 的快照；</li><li>版本追踪、回滚。</li></ul><br>
<br>Knative Service 中版本管理的资源：Revision，它是 Configuration 的快照，每次更新 Configuration 就会创建一个新的 Revision，可以通过 Revision 实现版本追踪、灰度发布以及回滚。在 Revision 资源里面，可以直接地看到配置的镜像信息。<br>
<br><h1>基于流量的灰度发布</h1><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210406/78a4f0b5bd149ad3163f1092876eee07.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/78a4f0b5bd149ad3163f1092876eee07.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>如上图所示，假如一开始我们创建了 V1 版本的 Revision，这时如果有新的版本变更，那么我们只需要更新 Service 中的 Configuration，就会相应的创建出 V2 版本。然后通过 Route 对 V1 和 V2 设置不同的流量比例，上图中 V1 是 70%，V2 是 30%，流量会按照 7:3 的比例分别分发到两个版本上。一旦 V2 版本验证没有问题，接下来就可以通过调整流量比例的方式进行继续灰度，直到新的版本 V2 达到 100%。<br>
<br>在灰度的过程中，一旦发现新版本有异常，随时可以调整流量比例进行回滚。假设灰度到 30% 的时候，发现 V2 版本有问题，我们就可以把比例调回去，在原来的 V1 版本上设置流量 100%，实现回滚操作。<br>
<br>除此之外，我们还可以在 Route 中通过 traffic 对 Revision 打上一个 Tag，打完 Tag 之后，在 Knative 中会自动对当前的 Revision 生成一个可直接访问的 URL，通过这个 URL 我们可以直接把相应的流量打到当前的某一个版本上去，这样可以实现对某个版本的调试。<br>
<br><h1>自动弹性</h1>在 Knative 中提供了<strong>丰富的弹性策略</strong>，除此之外，ASK Knative 中还扩展了一些相应的弹性机制，接下来分别介绍以下几个弹性策略：<br>
<ul><li>Knative Pod 自动扩缩容 （KPA）；</li><li>Pod 水平自动扩缩容 （HPA）；</li><li>支持定时 + HPA 的自动扩缩容策略；</li><li>事件网关（基于流量请求的精准弹性）；</li><li>扩展自定义扩缩容插件。</li></ul><br>
<br><h2>1. 自动扩缩容-KPA</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210406/591b2eb1559296cb0d92dc0a3077191c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/591b2eb1559296cb0d92dc0a3077191c.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>▲Knative Pod 自动扩缩容（KPA）<br>
<br>如上图所示，Route 可以理解成流量网关；Activator 在 Knative 中承载着 0~1 的职责，当没有请求流量时， Knative 会把相应的服务挂到 Activator Pod 上面，一旦有第一个流量进来，首先会进入到 Activator，Activator 收到流量之后，会通过 Autoscaler 扩容 Pod，扩容完成之后 Activator 把请求转发到相应的 Pod 上去。一旦 Pod ready 之后，那么接下来相应的服务会通过 Route 直接打到 Pod 上面去，这时 Activator 已经结束了它的使命。<br>
<br>在 1~N 的过程中，Pod 通过 kube-proxy 容器可以采集每个 Pod 里面的请求并发指数­，也就是请求指标。Autoscaler 根据这些请求指标进行汇聚，计算相应的需要的扩容数，实现基于流量的最终扩缩容。<br>
<br><h2>2. 水平扩缩容-HPA</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210406/55a13efbc69dc82a8180554c95592c89.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/55a13efbc69dc82a8180554c95592c89.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>▲Pod 水平自动扩缩容（HPA）<br>
<br>它其实是将 K8s 中原生的 HPA 做了封装，通过 Revision 配置相应的指标以及策略，使用 K8s 原生的 HPA，支持 CPU、Memory 的自动扩缩容。<br>
<br><h2>3. 定时+HPA 融合</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210406/06b6c38306e99c60f04941b3beb2c78b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/06b6c38306e99c60f04941b3beb2c78b.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>提前规划容量进行资源预热；</li><li>与 CPU、Memory 进行结合。</li></ul><br>
<br>在 Knative 之上，我们将定时与 HPA 进行融合，实现提前规划容量进行资源预热。我们在使用 K8s 时可以体会到，通过 HPA 进行扩容时，等指标阈值上来之后再进行扩容的话，有时满足不了实际的突发场景。对于一些有规律性的弹性任务，可以通过定时的方式，提前规划好某个时间段需要扩容的量。<br>
<br>我们还与 CPU、Memory 进行结合。比如某个时间段定时设置为 10 个 Pod，但是当前 CPU 对阈值计算出来需要 20 个 Pod，这时会取二者的最大值，也就是 20 个 Pod 进行扩容，这是服务稳定性的最基本保障。<br>
<br><h2>4. 事件网关</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210406/9335b8dec15ce8cc56d933e813910fcb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/9335b8dec15ce8cc56d933e813910fcb.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>基于请求数自动弹性；</li><li>1 对 1 任务分发。</li></ul><br>
<br>事件网关是基于流量请求的精准弹性。当事件进来之后，会先进入到事件网关里面，我们会根据当前进来的请求数去扩容 Pod，扩容完成之后，会产生将任务和 Pod 一对一转发的诉求。因为有时某个 Pod 同一时间只能处理一个请求，这时候我们就要对这种情况进行处理，也就是事件网关所解决的场景。<br>
<br><h2>5. 自定义扩缩容插件</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210406/1872eb75cc790332ee111b9e60105894.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210406/1872eb75cc790332ee111b9e60105894.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>自定义扩缩容插件有 2 个关键点：<br>
<ul><li>采集指标；</li><li>调整 Pod 实例数。</li></ul><br>
<br>指标从哪来？像 Knative 社区提供的基于流量的 KPA，它的指标是通过一个定时的任务去每个 Pod 的 queue-proxy 容器中拉取 Metric 指标。通过 controller 对获取这些指标进行处理，做汇聚并计算需要扩容多少 Pod。<br>
<br>怎么执行扩缩容？其实通过调整相应的 Deployment 里面的 Pod 数即可。<br>
<br>调整采集指标和调整 Pod 实例数，实现这两部分后就可以很容易地实现自定义扩缩容插件。<br>
<br><h1>实操演示</h1>下面进行示例演示，演示内容主要有：<br>
<ul><li>基于流量的灰度发布；</li><li>基于流量的自动扩缩容。</li></ul><br>
<br>演示过程观看方式：_<a href="https://developer.aliyun.com/live/246127_" rel="nofollow" target="_blank">https://developer.aliyun.com/live/246127_</a><br>
<br><h2>作者简介</h2>李鹏，花名：元毅，阿里云容器平台高级开发工程师，2016 年加入阿里， 深度参与了阿里巴巴全面容器化、连续多年支持双十一容器化链路。专注于容器、Kubernetes、Service Mesh 和 Serverless 等云原生领域，致力于构建新一代 Serverless 平台。当前负责阿里云容器服务 Knative 相关工作。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            