
---
title: 'EventMesh v1.2.0 发布，新增 7 名 contributor（务必阅读！！！）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b81a4536cf41e68bfd94629a5e3928fad14.png'
author: 开源中国
comments: false
date: Wed, 11 Aug 2021 16:39:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b81a4536cf41e68bfd94629a5e3928fad14.png'
---

<div>   
<div class="content">
                                                                                            <p>作者：薛炜明</p> 
<p style="text-align:justify">这个版本是EventMesh进入apache孵化的首个版本，我非常荣幸能够担任本次EventMesh这个大版本的Release Manager。</p> 
<p style="text-align:justify">在这个版本中，社区贡献者们完成了大量的优化和问题修复，极大地提高了应用的安全性、稳定性、可用性，上线版本的新功能特性以及修复优化，主要是以几个方面：</p> 
<p><strong>特性介绍</strong></p> 
<ul> 
 <li> <p>Connector&Adaptor</p> <p>可插拔式对接多种事件存储、支持适配多种协议、适配多种Schema</p> </li> 
 <li> <p>Binding</p> <p>支持将事件与topic、schema绑定，提供事件的构建、转换、路由以及多种过滤模式</p> </li> 
 <li> <p>Distributed Primitives</p> <p>EventMesh不仅支持云本地部署，还支持集群部署。对于分布式事件传递，eventmesh提供了两种消费模式，在集群模式下，一个事件只能传递给每组中的一个实例，而在广播模式下，每组中的每个实例都可以接收到每一个事件。</p> </li> 
 <li> <p>Scaling</p> <p>基于云原生的弹性能力，EventMesh具有水平自动扩缩容的能力</p> </li> 
 <li> <p>Orchestration</p> </li> 
</ul> 
<p>       EventMesh可作为不同服务之间的协调器，支持对工作流进行编排。因此，如果工作流中出现故障，可以执行补偿操作从故障中恢复。</p> 
<ul> 
 <li> <p>State Abstraction</p> </li> 
</ul> 
<p>        支持对接稳定、可信和有状态的服务。订阅者通过EventMesh可以使用最适合这些订阅者性能需求的任何存储来重建源系统的状态:SQL/NoSQL、对象存储、基于文件的存储等。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b81a4536cf41e68bfd94629a5e3928fad14.png" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#7a4fd6">EventMesh架构图</span></strong></p> 
<p><strong>新增特性</strong></p> 
<ul> 
 <li> <p>支持RocketMQ 作为事件存储</p> </li> 
 <li> <p style="text-align:left">支持Spi 进行插件化扩展实现以适应各种事件存储</p> </li> 
 <li> <p style="text-align:left">支持Http模式发布/订阅，心跳管理和订阅信息维护</p> </li> 
 <li> <p style="text-align:left">支持在docker容器下运行eventmesh</p> </li> 
</ul> 
<p><strong>优化</strong></p> 
<ul> 
 <li> <p>优化eventmesh-connector-api中的接口设计</p> </li> 
 <li> <p style="text-align:left">Tcp模式eventmesh异步化下发广播消息到客户端</p> </li> 
 <li> <p style="text-align:left">将rocketmq插件配置从运行态eventmesh-runtime中拆分</p> </li> 
 <li> <p style="text-align:left">清理遗留、易混淆的属性、概念</p> </li> 
 <li> <p style="text-align:left">Openmessaging-api升级到 2.2.1-pubsub 版本</p> </li> 
</ul> 
<p><strong>Bug修复</strong></p> 
<ul> 
 <li> <p style="text-align:left">修复Tcp模式删除订阅会话失败</p> </li> 
 <li> <p style="text-align:left">修复在 PullConsumer 消费主题中的消息后，ConsumerGroup队列偏移量未正确同步</p> </li> 
 <li> <p style="text-align:left">修复解析 Long 时出现java.lang.NumberFormatException</p> </li> 
 <li> <p style="text-align:left">解决EventMesh SDK 的 LiteConsumer HTTP 客户端中的竞态条件问题</p> </li> 
 <li> <p style="text-align:left">解决Rocketmq 插件空指针异常</p> </li> 
 <li> <p style="text-align:left">修复消费者拉取请求消息的属性“bizSeqNo”为空问题</p> </li> 
 <li> <p style="text-align:left">修复多个监听实例，只有最后启动的实例能接收消息问题</p> </li> 
 <li> <p style="text-align:left">修复EventMesh ProxyTcpRetryer抛出NumberFormatException问题</p> </li> 
 <li> <p style="text-align:left">修复rocketmq-connector插件进行 tcp 推送时 throw操作超时异常</p> </li> 
 <li> <p style="text-align:left">修复发送同步RR(request-response) msg失败异常</p> </li> 
 <li> <p style="text-align:left">修复rocketmq-connector插件无法成功发送和接收msg异常</p> </li> 
 <li> <p style="text-align:left">解决发布/订阅客户端无法启动问题</p> </li> 
 <li> <p style="text-align:left">修复当onChange为NEW时，发生NullPointException问题</p> </li> 
</ul> 
<p><strong>文档代码风格优化</strong></p> 
<ul> 
 <li> <p style="text-align:left">修订包名，完善测试用例</p> </li> 
 <li> <p style="text-align:left">补充eventmesh 项目必要的发布文件</p> </li> 
 <li> <p style="text-align:left">补充eventmesh 模块下的每个源文件的许可证</p> </li> 
 <li> <p style="text-align:left">代码结构和文件命名规范</p> </li> 
 <li> <p style="text-align:left">提供docker中运行eventmesh详细指引</p> </li> 
 <li> <p style="text-align:left">补充协议文档</p> </li> 
</ul> 
<p style="text-align:left">本次 1.2.0 版本一共包含 Feature 4 个，Improvement 5 个，Bug Fix 13 个，文档和代码格式优化 6 个。据不完全统计，这些贡献来自近十多位 Eventmesh社区的 Contributor，感谢大家加入到Eventmesh社区共同打造动态的云原生事件基础设施。</p> 
<p><strong>新增贡献者</strong></p> 
<p style="text-align:left">Eventmesh 1.2.0 的发布离不开 Eventmesh社区的贡献者，本次版本新增了以下几位contributor分别是：</p> 
<p style="text-align:left"><strong>SteveYurongSu</strong>（清华大学）、<strong>liangyuanpeng</strong>(云兴科技)、<strong>ruanwenjun</strong>（ebay）、<strong>zhangxiaopengmm</strong>(csii)、<strong>sunxi92</strong>（民生银行）、<strong>yuzhoumao</strong>（密歇根大学）、<strong>jinrongluo</strong></p> 
<p style="text-align:left">在这里非常感谢各位的积极参与和贡献，同时EventMesh社区非常期待有更多的用户、开发者、厂商参与到EventMesh生态的建设中来。</p> 
<p><strong>源项目地址：</strong></p> 
<p><u>https://github.com/apache/incubator-eventmesh/tree/v1.2.0</u></p> 
<p><strong>预告</strong></p> 
<p>EventMesh v1.3.0版本社区内已经在如火如荼地讨论开发中了，v1.3.0版本将提供：</p> 
<ul> 
 <li> <p>更广泛的事件存储集成(Kafka\Redis\...)</p> </li> 
 <li> <p>CloudEvents事件标准协议集成</p> </li> 
 <li> <p>OpenTelementry集成，提升可观测性</p> </li> 
 <li> <p>OpenSchema集成，支持多种类型数据编解码(Avro\Protobuf\JSON\...)</p> </li> 
 <li> <p>支持协议插件化（Http/TCP/Grpc）</p> </li> 
 <li> <p>支持Acl与Registry插件化集成</p> </li> 
 <li> <p>提供Event Streaming实时的事件处理与计算</p> </li> 
 <li> <p>...</p> </li> 
</ul> 
<p>EventMesh社区欢迎更多的用户、开发者参与讨论共建。</p> 
<p><strong>交流群</strong></p> 
<p>添加项目负责人微信  ApacheEventMesh  进入社区群</p>
                                        </div>
                                      
</div>
            