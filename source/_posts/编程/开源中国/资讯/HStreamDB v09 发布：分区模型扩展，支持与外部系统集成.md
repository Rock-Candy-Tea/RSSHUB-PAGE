
---
title: 'HStreamDB v0.9 发布：分区模型扩展，支持与外部系统集成'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2350'
author: 开源中国
comments: false
date: Mon, 08 Aug 2022 17:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2350'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>HStreamDB 最新版本 v0.9 现已正式发布！</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>v0.9 主要有以下亮点更新：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>stream 分区模型扩展，支持用户直接访问分区上指定位置的数据；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增 HStreamDB 的内部数据集成框架 HStream IO；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>集群转用基于 SWIM 的成员发现和故障检测机制；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>全新的流处理引擎；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>升级了 Java 和 Go 客户端，并新增了 Python 客户端。</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>Stream 分区模型扩展</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>v0.9 对之前的分区模型进行了扩展，允许用户直接操作和访问 stream 内部的分区，从而可以对 stream 中的数据分布和分区伸缩进行精细化控制。HStreamDB 采用的是 key-range-based 分区机制，stream 下的所有分区共同划分整个 key space，每个分区归属一段连续的子空间(key range)。若 record 所带 partitionKey 的哈希值落在某个子空间内，那么这条 record 将会被存储在对应的分区中。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>具体地，v0.9 的分区模型新增了以下能力:</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>在创建 stream 的时候配置初始分区数</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>通过 </span><span><code>partitionKey</code></span><span> 将写入的 record 分发到相应的 stream 的分区</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>直接从任意位置读取指定分区的数据</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>查看 stream 包含的分区和各个分区对应的 key range</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在之后的版本中，我们将支持通过分区分裂和合并对 stream 进行动态伸缩。</span></p> 
<h2 style="text-align:start"><span>HStream IO 发布</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>HStream IO 是 v0.9 包含的一个内部数据集成框架，包含 source connectors、sink connectors、IO runtime 等组件，它能够实现 HStreamDB 和多种外部系统的互联互通，促进数据在整个企业数据栈内的高效流转以及实时价值释放。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>v0.9 提供了以下的 connectors，可支持多种数据库之间的增量同步。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Source connectors:</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhstreamdb%2Fhstream-connectors%2Fblob%2Fmain%2Fdocs%2Fspecs%2Fsink_mysql_spec.md" target="_blank"><span>source-mysql</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhstreamdb%2Fhstream-connectors%2Fblob%2Fmain%2Fdocs%2Fspecs%2Fsource_postgresql_spec.md" target="_blank"><span>source-postgresql</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhstreamdb%2Fhstream-connectors%2Fblob%2Fmain%2Fdocs%2Fspecs%2Fsource_sqlserver_spec.md" target="_blank"><span>source-sqlserver</span></a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Sink connectors:</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhstreamdb%2Fhstream-connectors%2Fblob%2Fmain%2Fdocs%2Fspecs%2Fsink_mysql_spec.md" target="_blank"><span>sink-mysql</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhstreamdb%2Fhstream-connectors%2Fblob%2Fmain%2Fdocs%2Fspecs%2Fsink_postgresql_spec.md" target="_blank"><span>sink-postgresql</span></a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>用户可以通过对应的 SQL commands 创建和管理 IO task，具体可参考</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhstream.io%2Fdocs%2Fen%2Flatest%2Fio%2Foverview.html" target="_blank"><span>文档</span></a></span><span>了解 HStream IO 的功能和使用。</span></p> 
<h2 style="text-align:start"><span>新的流处理引擎</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>v0.9 基于迭代和差分计算原理重新实现了流处理引擎，显著提升了吞吐量，并降低了延迟。此外，新的引擎还支持多路 Join 语句、子查询(sub-queries)和更普适的物化视图(materialized view)。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>该特性仍然处于开发阶段，属于实验性的功能，用户可以参考</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhstream.io%2Fdocs%2Fen%2Flatest%2Fguides%2Fsql.html" target="_blank"><span> SQL 指南</span></a></span><span> 进行试用。</span></p> 
<h2 style="text-align:start"><span>基于 Gossip 的 HServer 集群</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>v0.9 对 HServer 的集群实现进行了重构，新的实现主要采用了 gossip style 的集群机制和基于 SWIM 的故障检测机制，取代了上一版本中基于 ZooKeeper 的实现。新的实现将提高集群的可扩展性，并减少对外部系统的依赖。</span></p> 
<h2 style="text-align:start"><span>Advertised Listeners</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>生产中的部署和使用可能涉及复杂的网络设置。例如，如果服务器集群是内部托管的，它需要一个外部可见的 IP 地址让客户连接到集群，尤其是当遇到使用 docker 或者云托管等情况，会使环境更加复杂。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>为了确保来自不同网络环境的客户端能够与集群进行交互，HStreamDB 0.9 支持配置 advertised listerners。在配置了 advertised listerners 后，服务器可以根据客户端发送请求的端口，为不同的客户端返回相应的地址。</span></p> 
<h2 style="text-align:start"><span>统一的 HStream CLI</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>为了使 CLI 更加统一和简易，我们已经将旧的 HStream SQL Shell 和其他一些节点管理功能迁移到新的 HStream CLI。HStream CLI 目前支持启动交互式 SQL Shell、发送集群 bootstrap 请求和检查服务器节点状态等功能。用户可以通过参考 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhstream.io%2Fdocs%2Fen%2Flatest%2Fcli%2Fcli.html" target="_blank"><span>CLI 文档</span></a></span><span>了解具体的使用方法。</span></p> 
<h2 style="text-align:start"><span>基于 Grafana 的监控</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>v0.9 新增了通过 Prometheus 和 Grafana 对 HStreamDB 集群进行监控的支持，HStreamDB 内部的 Metrics 将通过 exporter 存储到 Prometheus 并最终展示在 Grafana 面板上。具体的部署和使用流程可以参考</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhstream.io%2Fdocs%2Fen%2Flatest%2Fmonitoring%2Fgrafana.html%23installations-and-set-up" target="_blank"><span>文档</span></a></span><span>。</span></p> 
<h2 style="text-align:start"><span>支持用 Helm 在 K8s 上进行部署</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>v0.9 提供了 HStreamDB 的 Helm Chart，现在可通过 Helm 在 K8s上快速部署 HStreamDB 集群，更加详细的使用步骤可以参考</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhstream.io%2Fdocs%2Fzh%2Flatest%2Fdeployment%2Fdeploy-helm.html" target="_blank"><span>文档</span></a></span><span>。</span></p> 
<h2 style="text-align:start"><span>客户端版本升级和改进</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Java 客户端 v0.9.0、Go 客户端 v0.2.0、Python 客户端 v0.2.0 均已发布，提供对 HStreamDB 0.9 的支持。详情请见：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Java 客户端 v0.9.0：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhstreamdb%2Fhstreamdb-java%2Freleases%2Ftag%2Fv0.9.0" target="_blank">https://github.com/hstreamdb/hstreamdb-java/releases/tag/v0.9.0</a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Go 客户端 v0.2.0：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhstreamdb%2Fhstreamdb-go%2Freleases%2Ftag%2Fv0.2.0" target="_blank">https://github.com/hstreamdb/hstreamdb-go/releases/tag/v0.2.0</a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Python 客户端 v0.2.0：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhstreamdb%2Fhstreamdb-py%2Freleases%2Ftag%2Fv0.2.0" target="_blank">https://github.com/hstreamdb/hstreamdb-py/releases/tag/v0.2.0</a></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            