
---
title: 'Apache Cassandra 4.0 发布，最快、最可扩展和最安全'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a195d98a7d725352499dd1cb507d2c57f5a.png'
author: 开源中国
comments: false
date: Thu, 29 Jul 2021 07:09:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a195d98a7d725352499dd1cb507d2c57f5a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>在经历了<a href="https://www.oschina.net/news/151624/cassandra-4-0-delay">推迟</a>之后，Apache Cassandra 4.0 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.apache.org%2Ffoundation%2Fentry%2Fthe-apache-cassandra-project-releases" target="_blank">正式发布</a>。这是一套开源分布式 Key-Value 存储系统，它最初由 Facebook 开发，用于储存特别大的数据。</p> 
<p>Apache Cassandra 副总裁 Nate McCall 称，Cassandra 4.0 是一个漫长的过程，也是迄今为止测试最彻底的 Cassandra。最新版本速度更快、可扩展性更强，并支持企业安全功能，可在云中以前所未有的规模进行生产。</p> 
<p><img height="188" src="https://oscimg.oschina.net/oscnet/up-a195d98a7d725352499dd1cb507d2c57f5a.png" width="500" referrerpolicy="no-referrer"></p> 
<p>Cassandra v4.0 可以轻松处理非结构化数据，每秒写入数千次。经过三年的酝酿，v4.0 带来了  1000 多项 bug 修复、改进和新特性，其中包括有：</p> 
<ul> 
 <li>更高的速度和可扩展性 — 在扩展操作期间流式传输数据最多可提高 5 倍，读写吞吐量最多可提高 25%；从而提供更具弹性的架构，尤其是在云和 Kubernetes 部署中。</li> 
 <li>提高一致性 — 保持数据副本同步以优化增量修复，以实现更快、更高效的操作和跨数据副本的一致性。</li> 
 <li>增强的安全性和可观察性 — 审计日志跟踪用户访问和活动，对工作负载性能的影响最小。新的捕获和重放支持对生产工作负载进行分析，以帮助确保符合 SOX、PCI、GDPR 或其他要求的监管和安全合规性。</li> 
 <li>新的配置设置 — 公开的系统指标和配置设置为操作员提供了灵活性，以确保他们可以轻松访问优化部署的数据。</li> 
 <li>最小化延迟 —  Garbage Collector 的暂停时间减少到几毫秒，而不会随着堆大小的增加而降低延迟。</li> 
 <li>更好的压缩 — 改进的压缩效率减轻了磁盘空间上不必要的压力并提高了读取性能。</li> 
</ul> 
<p>官方表示，目前 Cassandra 4.0 已通过 Amazon、Apple、DataStax、Instaclustr、iland、Netflix 和其他通常运行多达 1000 个节点的集群并具有数百个实际用例和模式的社区强化和测试。</p> 
<p>Apache Cassandra 社区部署了多个测试和质量保证 (QA) 项目和方法来部署迄今为止最稳定的版本。在测试和 QA 期间，社区生成了尽可能接近现实生活的可重现工作负载，同时根据模型有效验证集群状态，而不会暂停工作负载本身。</p> 
<p>Apache Cassandra 贡献者 Scott Andreas 称，“Apache Cassandra 的贡献者们努力工作，致力于将 Cassandra 4.0 作为该项目迄今为止最稳定的版本发布，从而为部署到生产关键的云服务做好准备。Cassandra 4.0 还带来了新特性，例如更快的主机更换、主动数据完整性断言、增量修复和更好的压缩。该项目对高级验证工具的投资意味着 Cassandra 用户可以期待顺利的升级。一旦发布，Cassandra 4.0 也将为未来功能的开发和数据库的长期演进提供了稳定的基础。”</p> 
<p>除了 Cassandra 4.0 之外，该项目还宣布转向一年一次的发布周期，发布的版本将得到三年的支持。</p> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.apache.org%2Ffoundation%2Fentry%2Fthe-apache-cassandra-project-releases" target="_blank">https://blogs.apache.org/foundation/entry/the-apache-cassandra-project-releases</a></p>
                                        </div>
                                      
</div>
            