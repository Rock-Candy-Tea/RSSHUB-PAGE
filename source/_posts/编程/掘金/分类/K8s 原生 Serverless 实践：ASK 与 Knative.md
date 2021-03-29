
---
title: 'K8s 原生 Serverless 实践：ASK 与 Knative'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4994842eb51b4a7a8780ea8c974e4cce~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 28 Mar 2021 22:37:24 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4994842eb51b4a7a8780ea8c974e4cce~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="头图.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4994842eb51b4a7a8780ea8c974e4cce~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>作者 | 李鹏（元毅）</p>
<h1 data-id="heading-0">一、为什么需要 Knative</h1>
<p><img alt="1.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/383524a763d243c9a89febf221d40a5d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>K8s 目前已成为云原生市场上的主流操作系统，K8s <strong>对上</strong>通过数据抽象暴露基础设施能力，比如 Service、Ingress、Pod、Deployment 等，这些都是通过 K8s 原生 API 给用户暴露出来的能力；而<strong>对下</strong> K8s 提供了基础设施接入的一些标准接口，比如 CNI、CRI、CRD，让云资源以一个标准化的方式进入到 K8s 的体系中。</p>
<p>K8s 处在一个承上启下的位置，云原生用户使用 K8s 的目的是为了交付和管理应用，也包括灰度发布、扩容缩容等。但是对用户来说，实现这些能力，通过直接操作 K8s API 难免有些复杂。另外节省资源成本和弹性对于用户来说也越来越重要。</p>
<p>那么，如何才能简单地使用 K8s 的技术，并且实现按需使用，最终实现降本增效的目的呢？<strong>答案就是 Knative</strong>。</p>
<h1 data-id="heading-1">二、Knative简介</h1>
<h2 data-id="heading-2">1. Knative 是什么</h2>
<ul>
<li><strong>定义</strong></li>
</ul>
<p><img alt="2.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36d38f6c6b5f4d97a52ef84a501a2343~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Knative 是一款基于 Kubernetes 的 Serverless 编排引擎，Knative 一个很重要的目标是制定云原生跨平台的编排标准，它通过整合容器构建、工作负载以及事件驱动来实现这一目的。</p>
<p>Knative 社区当前贡献者主要有 Google、Pivotal、IBM、Red Hat，可见其阵容强大，另外还有 CloudFoundry、OpenShift 这些 PAAS 提供商也都在积极地参与 Knative 的建设。</p>
<ul>
<li><strong>核心模块</strong></li>
</ul>
<p><img alt="3.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/641480a6f5af496cafca1734d572d869~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Knative 核心模块主要包括两部分：事件驱动框架 Eventing 和提供工作负载的 Serving，接下来本文主要介绍 Serving 相关的一些内容。</p>
<h2 data-id="heading-3">2. 流量灰度发布</h2>
<p>以一个简单的场景为例：</p>
<ul>
<li><strong>在 K8s 中实现基于流量的灰度发布</strong></li>
</ul>
<p><img alt="4.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc80bef7ba0b4053b71363a76a3a1856~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果要在 K8s 中实现基于流量的灰度发布，需要创建对应的 Service 与 Deployment，弹性相关的需要 HPA 来做，然后在流量灰度发布时，要创建新的版本。</p>
<p>以上图为例，创始版本是 v1，要想实现流量灰度发布，我们需要创建一个新的版本 v2。创建 v2 时，要创建对应的 Service、Deployment、HPA。创建完之后通过 Ingress 设置对应的流量比例，最终实现流量灰度发布的功能。
 </p>
<ul>
<li><strong>在 Knative 中实现基于流量的灰度发布</strong></li>
</ul>
<p><img alt="5.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3eb192053f74f7298d4729256b1f296~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如上图所示，在 Knative 中想要实现基于流量的灰度发布，只需要创建一个 Knative Service，然后基于不同的版本进行灰度流量，可以用 Revision1 和 Revision2 来表示。在不同的版本里面，已经包含了自动弹性。
 
从上面简单的两个图例，我们可以看到在 Knative 中实现流量灰度发布时，需要直接操作的资源明显较少。</p>
<h2 data-id="heading-4">3. Knative Serving 架构</h2>
<p><img alt="6.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/211d29a9ca194295af6dda03732031ba~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>**Service **</li>
</ul>
<p>Service 对应 Serverless 编排的抽象，通过 Service 管理应用的生命周期。Service 下又包含两大部分：Route 和 Configuration。</p>
<ul>
<li><strong>Route</strong></li>
</ul>
<p>Route 对应路由策略。将请求路由到 Revision，并可以向不同的 Revision 转发不同比例的流量。</p>
<ul>
<li><strong>Configuration</strong></li>
</ul>
<p>Configuration 配置的是相应的资源信息。当前期望状态的配置。每次更新 Service 就会更新 Configuration。</p>
<ul>
<li><strong>Revision</strong></li>
</ul>
<p>每次更新 Configuration 都会相应得到一个快照，这个快照就是 Revision，通过 Revision 实现多版本管理以及灰度发布。</p>
<p>我们可以这样理解：Knative Service ≈ Ingress + Service + Deployment + 弹性（HPA）。</p>
<h2 data-id="heading-5">4. 丰富的弹性策略</h2>
<p>当然，Serverless 框架离不开弹性， Knative 中提供了以下丰富的弹性策略：</p>
<ul>
<li>基于流量请求的自动扩缩容：KPA；</li>
<li>基于 CPU、Memory 的自动扩缩容：HPA；</li>
<li>支持定时 + HPA 的自动扩缩容策略；</li>
<li>事件网关（基于流量请求的精准弹性）。</li>
</ul>
<h1 data-id="heading-6">三、Knative 和 ASK 融合</h1>
<h2 data-id="heading-7">1. ASK：Serverless Kubernetes</h2>
<p><img alt="7.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de23e691431a4a76be25bef7735c8cdf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果要准备 ECI 资源的话，需要提前进行容量规划，这无疑违背了 Serverless 的初衷。为摆脱 ECI 资源的束缚，不必提前进行 ECI 资源规划，阿里云提出了无服务器 Serverless——ASK。用户无需购买节点，即可直接部署容器应用，无需对节点进行维护和容量规划。ASK 提供了 K8s 兼容的能力，同时极大地降低了 K8s 的使用门槛，让用户专注于应用程序，而不是底层基础设施。</p>
<p>ASK 提供了以下能力：</p>
<ul>
<li><strong>免运维</strong></li>
</ul>
<p>开箱即用，无节点管理和运维，无节点安全维护，无节点 NotReady，简化 K8s 集群管理。</p>
<ul>
<li><strong>极致的弹性扩容</strong></li>
</ul>
<p>无容量规划，秒级扩容，30s 500pod。</p>
<ul>
<li><strong>低成本</strong></li>
</ul>
<p>按需创建 Pod，支持 Spot，预留实例券。</p>
<ul>
<li><strong>兼容 K8s</strong></li>
</ul>
<p>支持 Deployment/statfulset/job/service/ingress/crd 等。</p>
<ul>
<li><strong>存储挂载</strong></li>
</ul>
<p>支持挂载云盘、NAS、OSS 存储券。</p>
<ul>
<li><strong>Knative on ASK</strong></li>
</ul>
<p>基于应用流量的自动弹性，开箱即用，缩容到最小规格。</p>
<ul>
<li><strong>Elastic Workload</strong></li>
</ul>
<p>支持 ECI 按量和 Spot 混合调度。</p>
<ul>
<li><strong>集成 ARMS/SLS 等云产品</strong></li>
</ul>
<h2 data-id="heading-8">2. Knative 运维复杂度</h2>
<p>Knative 运维主要存在三个方面的问题：Gateway、Knative 管控组件和冷启动问题。</p>
<p><img alt="8.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58625146df06485da3e3353935959450~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如上图所示，在 Knative 中管控组件会涉及到相应的 Activator，它是从 0 到 1 的一个组件；Autoscaler 是扩缩容相关的组件；Controller 是自身的管控组件以及网关。对于这些组件的运维，如果放在用户层面做，无疑会加重负担，同时这些组件还会占用成本。</p>
<p><img alt="9.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f04db887cf7437a977fc7b17d111402~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>除此之外，从 0 到 1 的冷启动问题也需要考虑。当应用请求过来时，第一个资源从开始到启动完成需要一段时间，这段时间内的请求如果响应不及时的话，会造成请求超时，进而带来冷启动问题。</p>
<p>对于上面说到的这些问题，我们可以通过 ASK 来解决。下面看下 ASK 是如何做的？</p>
<h2 data-id="heading-9">3. Gateway 和 SLB 融合</h2>
<p><img alt="10.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ad459f1e2fd48ceb7e41fca3f5369c0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>相比于之前 Istio 提供的能力，我们需要运营管控 Istio 相关的组件，这无疑加大了管控成本。实际上对于大部分场景来说，我们更关心网关的能力，Istio 本身的一些服务（比如服务网格）我们其实并不需要。</p>
<p>在 ASK 中，我们将网关这一层通过 SLB 进行了替换：
 </p>
<ul>
<li><strong>降成本</strong>：减少了十几个组件，大大降低运维成本和 IaaS 成本；</li>
<li><strong>更稳定</strong>：SLB 云产品服务更稳定，可靠性更高，易用性也更好。</li>
</ul>
<h2 data-id="heading-10">4. 管控组件下沉</h2>
<p><img alt="11.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27ad5af3a60e47569a4503a0066a3b79~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>对于 Knative 管控组件，ASK 做了一些托管：</p>
<ul>
<li><strong>开箱即用</strong>：用户直接使用 Serverless Framework，不需要自己安装；</li>
<li><strong>免运维、低成本</strong>：Knative 组件和 K8s 集群进行融合，用户没有运维负担，也无需承担额外的资源成本；</li>
<li><strong>高管控</strong>：所有组件都在管控端部署，升级和迭代更容易。</li>
</ul>
<h2 data-id="heading-11">5. 优雅的保留实例</h2>
<p>在 ASK 平台中，我们提供了优雅保留实例的能力，其作用是<strong>免冷启动</strong>。通过保留实例，消除了从 0 到 1 的冷启动时间。当我们缩容到 0 的时候，并没有把实例真正缩容到 0，而是缩容到一个低规格的保留实例上，目的是降低成本。</p>
<ul>
<li><strong>免冷启动</strong>：通过保留规格消除了从 0 到 1 的 30 秒冷启动时间；</li>
<li><strong>成本可控</strong>：突发性能实例成本比标准规格实例降低 40% 的成本，如果和 Spot 实例结合还能再进一步降低成本。</li>
</ul>
<h1 data-id="heading-12">四、实操演示</h1>
<p>最后进行动手实践演示，以一家咖啡店（cafe）为例，演示内容主要有：</p>
<ul>
<li>在 ASK 集群中安装 Knative；</li>
<li>部署 coffee 服务；</li>
<li>访问 coffee 服务；</li>
<li>保留实例。</li>
</ul>
<p>演示过程观看链接：<a href="https://developer.aliyun.com/live/246126" target="_blank" rel="nofollow noopener noreferrer">developer.aliyun.com/live/246126</a></p>
<p><strong>作者简介：</strong>
李鹏，花名：元毅，阿里云容器平台高级开发工程师，2016 年加入阿里， 深度参与了阿里巴巴全面容器化、连续多年支持双十一容器化链路。专注于容器、Kubernetes、Service Mesh 和 Serverless 等云原生领域，致力于构建新一代 Serverless 平台。当前负责阿里云容器服务 Knative 相关工作。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            