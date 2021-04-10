
---
title: 'AI 事件驱动场景 Serverless 实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/936bcf9a1e581e9ca7ce790b7848ff59.jpg'
author: Dockone
comments: false
date: 2021-04-10 04:09:54
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/936bcf9a1e581e9ca7ce790b7848ff59.jpg'
---

<div>   
<br>作者 | 李鹏（元毅）<br>
来源 | <a href="https://mp.weixin.qq.com/s/kjsEGyVcPEv-Mvp_0kITfA">Serverless 公众号</a><br>
<br><h1>一、事件驱动框架：Knative Eventing</h1>事件驱动是指事件在持续事务管理过程中，进行决策的一种策略。可以通过调动可用资源执行相关任务，从而解决不断出现的问题。通俗地说是当用户触发使用行为时对用户行为的响应。在 Serverless 场景下，事件驱动完美符合其设计初衷之一：按需付费。<br>
<br><h2>1. Knative 模型</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/936bcf9a1e581e9ca7ce790b7848ff59.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/936bcf9a1e581e9ca7ce790b7848ff59.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>图：Knative 模型<br>
<br>Knative 主要包括两大部分：一是用于工作负载的 Serving，包括版本管理、灰度流量、自动弹性；二是 Eventing（事件驱动框架）。<br>
<ul><li><br>核心玩家<br>
<ul><li>Google；</li><li>IBM；</li><li>Pivotal；</li><li>RedHat；</li><li>SAP。</li></ul></li><li><br>友商相关产品<br>
<ul><li>Google CloudRun；</li><li>IBM；</li><li>Pivotal Function Service(PFC)；</li><li>OpenShift。</li></ul></li></ul><br>
<br><h2>2. 事件驱动框架：Eventing</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/8737e63e41c68e7e857d0159454e6d7f.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/8737e63e41c68e7e857d0159454e6d7f.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Knative 的 Eventing 提供了一个完整的事件模型，方便接入各个外部系统的事件。事件接入以后，通过 Cloud Event 标准在内部流转，结合 Broker-Trigger 模型进行事件处理。<br>
<br>从上图可以看到，Eventing 中包含三部分内容：<br>
<ul><li><strong>事件源</strong></li><li><strong>Broker-Trigger：</strong>事件驱动模型，这个模型在早期 16 年的版本开始出现，其原理是 Trigger 订阅 Broker 信息并过滤，最后将事件发送到对应的服务进行消费。</li><li><strong>消息系统：</strong>在 Eventing 中每个 Broker 下面对应一个消息的系统，来承载对事件的整个流转。目前社区支持的消息系统包括 Kafka、NATS、Rocket MQ、Rabbit MQ 等。</li></ul><br>
<br><h2>3. 关键特性：事件规则</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/aa1e7736bae130dde47918b05a195fc7.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/aa1e7736bae130dde47918b05a195fc7.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>事件规则的核心是 Broker-Trigger 模型，它包含以下特性：<br>
<ul><li>Trigger 的 filter 的作用是对 Event 进行内容过滤；</li><li>支持对 Event 的 Attribute 以及 Data 的内容进行过滤；</li><li>支持 Common Expression Language（CEL）表达式过滤；</li><li>支持通过 SourceAndType（事件源类型）进行过滤。</li></ul><br>
<br><h1>二、事件驱动引擎-事件源</h1><h2>1. 事件源介绍</h2>Knative 社区中提供了丰富的事件源接入，包括 Kafka、Github，也支持接入消息云产品的一些事件，比如 MNS、RocketMQ 等。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/da7e7368803dd8a8aaed095a07a48536.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/da7e7368803dd8a8aaed095a07a48536.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>如上图所示，接入事件源之后，可以通过 Broker-Trigger 模型请求相应的服务。这些服务包括一些具体场景，比如从源码构建镜像、自动化镜像发布、AI 音视频处理、定时任务等。所有的事件都需要这样的事件源来拉取，然后下发到 Eventing 整个事件流转过程。<br>
<ul><li><br>事件接入<br>
<ul><li>接入消息云产品事件源；</li><li>通过 MNS 接入更多云产品的事件。</li></ul></li><li><br>事件处理<br>
<ul><li>Knative Eventing 内部实现事件的订阅、过滤和路由机制；</li><li>事件最终通过 Knative 管理的 Serverless 服务进行消费。</li></ul></li><li><br>典型案例<br>
<ul><li>AI 音视频处理；</li><li>代码提交自动构建镜像。</li></ul></li></ul><br>
<br><h2>2. RocketMQ 事件源</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/78a3f0d95d7f4610f9e87018e77e22ae.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/78a3f0d95d7f4610f9e87018e77e22ae.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>消息队列 RocketMQ 版是阿里云基于 Apache RocketMQ 构建的低延迟、高并发、高可用、高可靠的分布式消息中间件。<br>
<br>消息队列 RocketMQ 版既可为分布式应用系统提供异步解耦和削峰填谷的能力，同时也具备互联网应用所需的海量消息堆积、高吞吐、可靠重试等特性。<br>
<br>RocketMQSource 是 Knative 平台的 RocketMQ 事件源。其可以将 RocketMQ 集群的消息以 Cloud Event 的格式实时转发到 Knative 平台，是 Apahe RocketMQ 和 Knative 之间的连接器。<br>
<br><h2>3. Kafka 事件源</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/268b1b49d63c7d3e251a8430bf89e0ea.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/268b1b49d63c7d3e251a8430bf89e0ea.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>消息队列 Kafka 版是阿里云基于 Apache Kafka 构建的高吞吐量、高可扩展性的分布式消息队列服务，广泛用于日志收集、监控数据聚合、流式数据处理、在线和离线分析等，是大数据生态中不可或缺的产品之一，阿里云提供全托管服务，用户无需部署运维，更专业、更可靠、更安全。<br>
<br><h1>三、AI 事件驱动场景实践</h1><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/4bcdf0bb77aae7ab799667787497eb5d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/4bcdf0bb77aae7ab799667787497eb5d.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>以具体场景为例，该案例是一个<strong>直播系统</strong>，系统每天都有海量的直播访问，访问量根据直播热度随时变化，弹性有波动，同时存在不定时的增量。客户的诉求，一是业务弹性波动，消息并发性比较高；二是互动实时响应，要求低延迟。<br>
<br>为了满足对消息处理的<strong>弹性波动、高并发及低延迟</strong>的要求，客户选择阿里云的 Knative 服务进行数据的弹性处理。阿里云 Knative 完全契合了用户当前的诉求，并且在接入 K8s 标准之上，提供了基于事件和消息的弹性调度。<br>
<br>当应用实例数随着业务的波峰波谷进行扩容和缩容时，真正做到了<strong>按需使用、实时弹性</strong>的能力。整个过程完全自动化，减少业务开发人员在基础设施上的负担。在这个案例中，Knative 主要提供了三个能力：<strong>极致弹性、事件处理、开箱即用。</strong><br>
<br>下面进行示例演示，演示内容主要有：<br>
<ul><li>部署 Kafka 事件源</li><li>部署事件网关</li><li>部署服务</li><li>模拟事件处理</li></ul><br>
<br>演示过程观看链接：<a href="https://developer.aliyun.com/live/246128"></a><a href="https://developer.aliyun.com/live/246128" rel="nofollow" target="_blank">https://developer.aliyun.com/live/246128</a><br>
<br><strong>作者简介：</strong><br>
李鹏，花名：元毅，阿里云容器平台高级开发工程师，2016 年加入阿里， 深度参与了阿里巴巴全面容器化、连续多年支持双十一容器化链路。专注于容器、Kubernetes、Service Mesh 和 Serverless 等云原生领域，致力于构建新一代 Serverless 平台。当前负责阿里云容器服务 Knative 相关工作。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            