
---
title: '春色满园关不住，带你体验阿里云 Knative'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/9e04fb9b9b8c462e80cc46efcc7a41fc.jpg'
author: Dockone
comments: false
date: 2021-06-08 13:26:48
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/9e04fb9b9b8c462e80cc46efcc7a41fc.jpg'
---

<div>   
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/9e04fb9b9b8c462e80cc46efcc7a41fc.jpg" alt="首图.jpg" referrerpolicy="no-referrer"><br>
<br>作者 | 元毅<br>
<br><strong>导读：</strong>Knative 是基于 Kubernetes 的开源 Serverless 应用编排框架。阿里云 Knative 在社区 Knative 基础之上，与阿里云产品进行了深度的融合，给你带来最纯粹的容器化 Serverless 体验。<br>
​<br>
<br><h1>关于 Knative</h1>​<br>
<br>Knative 是基于 Kubernetes 的开源 Serverless 应用编排框架。实际上 Knative 包含的不单单是 Workload，它还有 Kubernetes 原生的流程编排引擎和完备的事件系统。Knative 目标是基于 Kubernetes 提供应用 Serverless 工作负载编排的标准化。Knative 核心模块主要包括事件驱动框架 Eventing 和部署工作负载的 Serving。<br>
​<br>
<br><h2>1. Serverless 服务引擎 - Serving</h2>​<br>
<br>Knative Serving 核心能力就是其简洁、高效的应用托管服务，这也是其支撑 Serverless 能力的基础。当然作为 Serverless Framework 就离不开按需分配资源的能力，Knative 可以根据应用的请求量在高峰时期自动扩容实例数，当请求量减少以后自动缩容实例数，可以非常自动化地帮助您节省成本。<br>
​<br>
<br>Serving 还提供了流量管理能力和灵活的灰度发布能力。流量管理能力可以根据百分比切分流量，灰度发布能力可以根据流量百分比进行灰度。<br>
​<br>
<br><h3>1）简单的应用模型</h3>​<br>
<br>提供了极简的应用模型 - Knative Service ，同时满足服务部署、服务访问以及灰度发布的能力。可以用下面的公式表述：Knative Service = 工作负载（Deployment）+ 服务访问（ Service ）+ 灰度流量（ Ingress ）。<br>
​<br>
<br>应用模型如下图<br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/13dfff73ba3d44c187d938e433a43a73.png" alt="1.png" referrerpolicy="no-referrer"><br>
<ul><li>Service：对 Serverless 应用模型的抽象，通过 Service 管理应用的生命周期；</li><li>Configuration：用于配置应用期望的信息。每次更新 Service 就会更新 Configuration；</li><li>Revision：Configuration 的每次更新都会创建一个快照，用来做版本管理；</li><li>Route：将请求路由到 Revision，并可以向不同的 Revision 转发不同比例的流量。</li></ul><br>
<br>​<br>
- 应用托管<br>
   - Kubernetes 是面向 IaaS 管理的抽象，通过 Kubernetes 直接部署应用需要维护的资源比较多；<br>
   - 通过 Knative Service 一个资源就能定义应用的托管。<br>
<ul><li>流量管理<br>
<ul>- Knative 通过 Gateway 结果应用流量，然后可以对流量按百分比进行分割，这为这为弹性、灰度等基础能力做好了基础。</ul></li></ul><br>
<br>​<br>
- 灰度发布<br>
   - 支持多版本管理，应用同时有多个版本在线提供服务很容易实现；<br>
   - 不同版本可以设置不同的流量百分比，对灰度发布等功能实现起来很容易。<br>
<br>​<br>
- 弹性<br>
   - Knative 帮助应用节省成本的核心能力是弹性，在流量增加的时候自动扩容，容，流量下降的时候自动缩容；<br>
   - 每一个灰度的版本都有自己的弹性策略，并且弹性策略和分配到当前版本的流量流量是相关联的。Knative 会根据分配过来的流量多少进行扩容或者缩容的决策。<br>
<br><h3>2）丰富的弹性策略</h3>​<br>
作为 Serverless 框架，其核心能力就是自动弹性，Knative 中提供了丰富的弹性策略：<br>
<ul><li>基于流量请求的自动扩缩容 - KPA</li><li>基于 CPU、Memory 的自动扩缩容 - HPA</li><li>支持定时 + HPA 的自动扩缩容策略</li><li>事件网关，提供请求与 Pod 1 对 1 处理能力<br>
### ​</li></ul><br>
<br><h2>2. Serverless 事件驱动框架 - Eventing</h2>​<br>
事件驱动是 Serverless 的标配，在 Knative 中同样提供了事件驱动框架 - Eventing。<br>
​<br>
Knative 的 Eventing 提供了完整的事件模型，可以很容易地接入各个外部系统的事件。事件接入以后通过 CloudEvent 标准在内部流转。<br>
​<br>
在 Knative Eventing 提供两种事件转发方式：<br>
​<br>
- 事件源直接转发到服务；<br>
- 事件源转发到 Broker / Trigger ，然后通过过滤转发到服务。<br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/402ce134c10c4cb682463fd219e6acb2.png" alt="2.png" referrerpolicy="no-referrer"><br>
<br>对于在使用过程中究竟应该使用哪种方式进行转发呢？其实很简单，Broker / Trigger 模型是基于底层消息系统实现的，对于像 Github、Gitlab、K8s APIserver 这样的事件源来说，需要对消息事件进行缓冲处理、保证消息传输可靠性，那么我们建议通过事件源转发到 Broker / Trigger 进行事件流转。<br>
​<br>
对于事件源本身就是消息系统来说，像 MNS、Kafka、RocketMQ来说，使用事件源直接转发到服务更为高效。<br>
​<br>
讲到这里，就不得不提 Knative 的事件源。我把它比喻成事件驱动引擎，Knative Eventing 正是通过这些事件源驱动事件流转。<br>
​<br>
Knative 社区提供了丰富的事件源，如 Kafka、GitHub 等。此外还接入消息云产品事件源，如 MNS、RocketMQ 等。<br>
<br><h1>阿里云 Knative</h1>​<br>
阿里云 Knative 在社区原生的 Knative 之上，与阿里云资源体系进行了全方位的整合，提供了更为丰富的能力以及云产品级别的支持。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/c8ee57e77c534bed8d602625989e88ee.png" alt="3.png" referrerpolicy="no-referrer"><br>
<br><h2>1. 与阿里云产品融合</h2>​<br>
- 丰富的消息云产品事件源：Kafka 、MNS 、RocketMQ<br>
- 服务访问：SLB<br>
- 存储：NAS 、云盘等<br>
- 可观测性：日志服务、ARMS<br>
- IaaS 资源：ECS 、ECI<br>
<br><h2>2. 天然集成阿里云  K8s  生态</h2>​<br>
- 支持阿里云标准版 Kubernetes，专有版 Kubernetes；<br>
- 支持阿里云 Serverless Kubernetes（ASK）， 并且在 ASK 中将 Knative 管控组件全托管，为用户节省了资源以及运维成本。<br>
<br><h1>一个例子</h1>​<br>
接下来以一个发送弹幕的示例来介绍一下如何玩转阿里云 Knative。先看一下效果：<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/aae91d0a88c94b77a068296c2d061632.png" alt="4.png" referrerpolicy="no-referrer"><br>
<br>架构示意图：<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/02be9b39c158462dbd4b7d28250fae6e.png" alt="5.png" referrerpolicy="no-referrer"><br>
<br>流程说明：<br>
<ul><li>用户通过弹幕 Web 服务发送弹幕到阿里云 Kafka；</li><li>Kafka Source 事件源监听到弹幕消息，然后发送到弹幕消息处理服务；</li><li>弹幕消息处理服务接收到消息，然后自动弹性扩容实例进行消息处理，并将处理完成的消息发送给弹幕服务；</li><li>最后弹幕通过 Web 服务界面展示给用户；</li></ul><br>
<br><h1>总结</h1>​<br>
最后我们总结一下阿里云 Knative 能给我们带来哪些能力：<br>
​<br>
- 服务部署低门槛、易上手<br>
- Serverless 按需使用资源<br>
- 事件驱动与消息云产品无缝对接<br>
- 天然集成阿里云 K8s 生态<br>
- 与阿里云产品打通<br>
<br>希望这些能力能给你带来真正的按需使用，降低运维、资源使用成本的诉求，这也是 Serverless 思想理念所追求的目标。
                                
                                                              
</div>
            