
---
title: 'EventMesh 1.3.0 发布！支持 CloudEvents 协议、Standalone、可观测性等'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3bf26be6fe6f48c05cd2935c33097373d7b.png'
author: 开源中国
comments: false
date: Thu, 06 Jan 2022 11:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3bf26be6fe6f48c05cd2935c33097373d7b.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><strong><span><span style="color:#353535">CloudEvents</span></span></strong></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535">每一个发生（Occurrence）都会产生事件（Event），包含了相关的上下文和数据。每一个事件都具有数据唯一标识。</span></span><em><span><span style="color:#a0a0a0">事件代表事实，因此不包括目的地，而消息则传达意图，将数据从源头传送到特定的目的地。<img alt height="309" src="https://oscimg.oschina.net/oscnet/up-3bf26be6fe6f48c05cd2935c33097373d7b.png" width="800" referrerpolicy="no-referrer"></span></span></em></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535">缺乏通用的描述事件的方式意味着开发人员必须不断地重新学习如何消费事件。这也限制了类库、工具和基础设施在跨环境时发送事件数据的潜力，如SDK、事件路由器或跟踪系统等。我们从事件数据中实现的可移植性和生产力总体上受到了阻碍。CloudEvents是一个用通用格式描述事件数据的规范，以提供跨服务、跨平台和跨系统的互操作性。CloudEvents得到了大量的行业关注，从主要的云提供商到流行的SaaS公司都有。CloudEvents由云原生计算基金会（CNCF）主办，于2018年5月15日获批为云原生沙盒级项目。</span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><strong><span><span style="color:#353535">Eventing</span></span></strong></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535">在服务器端代码中，事件通常用于连接不同的系统，其中一个系统的状态变化会导致另一个系统的代码执行。例如，当源接收到外部信号（如 HTTP 或 RPC）或观察到一个变化的值（如 IoT 传感器）时，可能会产生一个事件。<br> 为了说明系统如何使用 CloudEvents，下面的图显示了来自源的事件如何触发一个动作。</span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535"><img alt height="385" src="https://oscimg.oschina.net/oscnet/up-7a55124ea9e65230a4b08eb2834bc188170.png" width="780" referrerpolicy="no-referrer"></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535">源(Source)生成消息(Message)，其中事件(Event)被封装在协议中。事件到达目的地，触发一个由事件数据提供的动作(Action)。源是源类型的一个特定实例，它允许staging和测试实例。一个特定源类型的开放源软件可以由多个公司或供应商部署。事件可以通过各种行业标准协议（如HTTP、AMQP、MQTT、SMTP）、开源协议（如Kafka、NATS、RocketMQ、RabbitMQ）或平台/供应商特定的协议（AWS Kinesis、Azure Event Grid）来递送。动作处理定义了由特定源的特定事件触发的行为或效果的事件。虽然不在本规范的范围内，但生成事件的目的通常是为了让其他系统能够轻松地对它们无法控制的源中的变化做出反应。源和动作通常是由不同的开发人员建立的。通常情况下，源是一个托管服务，而动作是无服务器函数（如AWS Lambda或Google Cloud Functions）中的自定义代码。EventMesh支持扩展多种协议，内部协议流转示意图如下：</span></span><br> <img alt height="296" src="https://oscimg.oschina.net/oscnet/up-fd36c5706c1ea63adb99bb5c452b70a64af.png" width="1200" referrerpolicy="no-referrer"></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><strong><span><span style="color:#353535">Standalone</span></span></strong></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535">EventMesh</span></span><span><span style="color:#353535">支持了Standalone Connector功能，在Standalone模式下EventMesh不依赖于任何外部存储组件，方便用户快速体验EventMesh收发事件能力以及相关特性，极大地降低了用户初次体验EventMesh的门槛，我们不建议在生产环境使用该模式，仅在本地体验即可。</span></span></span></span></span><br>  </p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><strong><span><span style="color:#353535">OpenTelemetry</span></span></strong></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535">EventMesh</span></span><span><span style="color:#353535">支持了OpenTelemetry的集成，该功能极大的提升了EventMesh的可观测性，集成OpenTelemetry标准化了EventMesh的Metrics与Tracing数据，方便后续对接不同的采集器，目前分别支持将Metrics数据导出到Prometheus，以及将Tracing数据导出到Zipkin。后续还会根据社区内部的需求支持更多的采集器。</span></span></span></span></span><br>  </p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><strong><span><span style="color:#353535">插件化优化</span></span></strong></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535"><img alt height="708" src="https://oscimg.oschina.net/oscnet/up-8aff292f9d5a9a06ba127337f6538513584.png" width="1200" referrerpolicy="no-referrer"></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535">1.3.0</span></span><span><span style="color:#353535">版本极大的提升了EventMesh的可插拔能力，相较于1.2.0版本基于JDK SPI的插件化加载架构，1.3.0版本采用了注解的方式完善了各个类型插件的加载，提供了多种插件在运行时共存的能力，同时相较于1.2.0版本除了支持存储插件Rocketmq-connector以外，我们还提供了Standalone-connector插件，可以通过简单配置实现插件之间的切换与加载；同时协议部分我们也完善了插件化的扩展与支持，在原有的EventMesh原生协议基础上，扩展支持了CloudEvents协议，以此为例，可以很方便用户后续在协议层面进行其他的扩展，后续版本还将丰富更多类型的插件。</span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><strong><span><span style="color:#353535">致谢</span></span></strong></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535">EventMesh 1.3.0 </span></span><span><span style="color:#353535">的发布离不开 EventMesh社区的贡献者，在这里感谢为社区做出贡献的小伙伴们：</span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><strong><span><span style="color:#353535">Committers:</span></span></strong><br> <span><span style="color:#353535">qqeasonchen</span></span><span><span style="color:#353535">、xwm1992、ruanwenjun、lrhkobe、iNanos、vongosling、wqliang、keranbingaa、yiliuchen、jonyangx</span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><strong><span><span style="color:#353535">Contributors:</span></span></strong><br> <span><span style="color:#353535">tydhot</span></span><span><span style="color:#353535">、jzhou59、yuzhao244、wangshaojie4039、xiaoyang-sde、dongzl、hagsyn、msdhinesh-geek、sarihuangshanrong、Alonexc、AhahaGe、horoc、zhannicholas、dengqunhua、Roc-00、yuzhoumao、sunxi92、liangyuanpeng、SteveYurongSu</span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535">非常感谢各位的积极参与和贡献，同时EventMesh社区非常期待有更多的用户、开发者、厂商参与到EventMesh生态的建设中来。</span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><strong><span><span style="color:#353535">预告</span></span></strong></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><span><span style="color:#353535">在后续的版本中，如下特性将会与大家见面：</span></span></span></span></span></p> 
<ul> 
 <li style="text-align:left"><span><span style="background-color:white"><span><span><span><span style="color:#353535">支持Grpc协议，提升EventMesh传输的性能与效率</span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span style="background-color:white"><span><span><span><span style="color:#353535">支持WasmEdge，增加EventMesh的边缘计算的能力，支持更广泛的应用场景</span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span style="background-color:white"><span><span><span><span style="color:#353535">支持Serverless Workflow工作流编排</span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span style="background-color:white"><span><span><span><span style="color:#353535">支持Event Sourcing与分布式事务</span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span style="background-color:white"><span><span><span><span style="color:#353535">......</span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><strong><span><span style="background-color:white"><span><span><span style="color:#353535">EventMesh</span></span><span><span style="color:#353535">社区欢迎更多的用户、开发者参与讨论共建。</span></span></span></span></span></strong></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><span><span style="background-color:white"><span><strong><span><span style="color:#353535">项目地址</span></span></strong></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-eventmesh" target="_blank"><span><span style="background-color:white"><span><u><span><span style="color:#353535">https://github.com/apache/incubator-eventmesh</span></span></u></span></span></span></a></p>
                                        </div>
                                      
</div>
            