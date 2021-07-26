
---
title: '云原生分布式流数据库 HStreamDB 0.5 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5416'
author: 开源中国
comments: false
date: Mon, 26 Jul 2021 14:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5416'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>HStreamDB 是一款专为流式数据设计的云原生分布式数据库，可针对大规模实时数据流的接入、存储、处理、分发等环节进行全生命周期管理。</strong>它使用标准 SQL (及其流式拓展）作为主要接口语言，以实时性作为主要特征，旨在简化数据流的运维管理以及实时应用的开发，不仅支持高效存储和管理大规模数据流，还能够在动态变化的数据流上进行复杂的实时分析。</p> 
<p>在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg3NjAyMjM0NQ%3D%3D%26mid%3D2247486997%26idx%3D1%26sn%3D8a3446783d3a89a9b0d8788249d9e0ef%26scene%3D21%23wechat_redirect" target="_blank">《当数据库遇上流计算：流数据库的诞生》</a>一文中，我们介绍了流数据库的概念。以此为产品设计理念基础，我们所开发的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg3NjAyMjM0NQ%3D%3D%26mid%3D2247487153%26idx%3D1%26sn%3D1e50f70cbd514ffbdc42aeff4d93ce17%26scene%3D21%23wechat_redirect" target="_blank">HStreamDB</a> 于今年初正式开源。</p> 
<p>今天，EMQ HStreamDB 团队非常高兴地向大家宣布：<strong>HStreamDB v0.5 正式发布</strong><strong>！</strong></p> 
<p>下载地址：https://github.com/hstreamdb/hstream</p> 
<h4>版本更新</h4> 
<p>在此次发布的 0.5 版本中，我们除了对原有的功能（如：对数据流的管理、数据的写入与消费）进行了升级，还新增加了很多对使用 HStreamDB 进行开发具有重大意义的功能特性，例如 Java SDK、MySQL 和 Clickhouse Connector，以及对物化视图的支持等。</p> 
<p><strong><strong>◆  </strong>增加对物化视图的支持</strong></p> 
<p>提供物化视图功能，支持在持续更新的数据流上进行复杂的查询和分析操作。同时，HStreamDB 内部的增量计算引擎会根据数据流的变化实时更新物化视图，用户可通过 SQL 语句查询物化视图获得实时的数据洞察。</p> 
<p><strong><strong>◆  </strong>增加 Java SDK，方便基于 HStreamDB 的开发</strong></p> 
<p>这是我们主要推荐的使用 HStreamDB 的方式，用户可以查阅文档（https://docs.hstream.io/develop/java-sdk/installation/）了解如何安装以及使用 Java 进行开发。</p> 
<p><strong><strong>◆  </strong>提供 Sink Connector</strong></p> 
<p>我们提供了两种 Sink Connector，包括 MySQL 和 Clickhouse。用户可以通过 SQL 语句轻松指定哪些数据需要导入到特定的数据库中。</p> 
<p><strong><strong>◆  </strong>新增 Dashboard</strong></p> 
<p>用户可以通过 Dashboard 来完成对 HStreamDB 内部资源的管理。</p> 
<p><strong><strong>◆  </strong>重构 Server，基于 gRPC 设计实现了 Server 的接口</strong></p> 
<p>基于 gRPC 的重新设计了 HStream Server，使 Server 的实现清晰，增强了 Server 的可扩展能力。</p> 
<p><strong><strong>◆  </strong>改进了基于 SQL 的流数据处理</strong></p> 
<p>新增了大量 SQL 函数，完善和优化了聚合函数。增强了对流处理任务的管理功能。</p> 
<p><strong><strong>◆  </strong>优化了低层存储逻辑</strong></p> 
<h4>发展规划</h4> 
<p>在之后的版本中，我们将朝着以下目标继续努力：</p> 
<p><strong><strong>◆  </strong>提升 HStream Server 的扩展能力</strong></p> 
<ul> 
 <li> <p>实现 HStream Server 集群支持</p> </li> 
 <li> <p>支持多个 consumer 进行共享订阅和并行消费</p> </li> 
 <li> <p>优化控制平面元数据存储</p> </li> 
</ul> 
<p><strong><strong>◆  </strong>增强运维和监控能力</strong></p> 
<ul> 
 <li> <p>支持使用 k8s 进行部署</p> </li> 
 <li> <p>实现统计监控框架</p> </li> 
 <li> <p>丰富 Dashboard 功能</p> </li> 
</ul> 
<p><strong><strong>◆  </strong>增强流处理能力</strong></p> 
<ul> 
 <li> <p>优化流引擎的实现，提升处理效率</p> </li> 
 <li> <p>增加 SQL 优化器，优化执行计划生成</p> </li> 
 <li> <p>实现流任务调度框架，支持并行处理</p> </li> 
</ul> 
<p><strong><strong>◆  </strong>提升易用性</strong></p> 
<ul> 
 <li> <p>改进 Java SDK</p> </li> 
 <li> <p>完善用户文档，提供更多教程和示例</p> </li> 
 <li> <p>提供更多应用案例</p> </li> 
</ul> 
<p><strong><strong>◆  </strong>丰富 HStreamDB 生态，提升集成能力</strong></p> 
<ul> 
 <li> <p>重构 Connector 框架，方便开发者自行实现所需的 Connector</p> </li> 
 <li> <p>实现分级存存储</p> </li> 
 <li> <p>实现更多常用系统的 Connector 支持</p> </li> 
</ul> 
<p>我们也计划在下个阶段完成与 EMQ X 的集成，这将不仅能验证 HStreamDB 功能完善程度，更意味着一个为物联网应用开发量身打造的产品组合的诞生。</p> 
<h4>未来展望</h4> 
<p>HStreamDB 作为流数据库这一基础软件品类的开创者，正向着能够被投入生产环境使用这一阶段性目标稳步前进。我们将继续推进 HStreamDB 的开发，完善功能，稳定性能，保证可靠。相信在不远的将来，用户便能使用 HStreamDB 更加快速地开发实时应用，更加简单地获取即时数据洞察。同时，我们也在此感谢广大社区成员的每一次使用和每一次贡献。敬请期待一个更加完善成熟的 HStreamDB。</p>
                                        </div>
                                      
</div>
            