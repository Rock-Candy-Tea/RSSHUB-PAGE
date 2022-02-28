
---
title: 'Apache InLong (incubating) 进入1.0 时代！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2adaeed4ddeffcf2fbefd1021d66479efaa.png'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 07:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2adaeed4ddeffcf2fbefd1021d66479efaa.png'
---

<div>   
<div class="content">
                                                                                            <p>Apache InLong（应龙）是一个一站式的海量数据集成平台，提供自动、安全、可靠和高性能的数据传输能力，同时支持批和流，方便业务构建基于流式的数据分析、建模和应用。<strong>InLong 支持大数据领域的采集、汇聚、缓存和分拣功能，用户只需要简单的配置就可以把数据从数据源导入到实时计算引擎或者落地到离线存储。</strong></p> 
<h3><strong>1 <strong><strong>Apache InLong</strong></strong>(incubating) 简介</strong></h3> 
<p>Apache InLong（应龙）是腾讯捐献给 Apache 社区的一站式海量数据集成框架，提供自动、安全、可靠和高性能的数据传输能力，方便业务构建基于流式的数据分析、建模和应用。InLong 项目原名 TubeMQ ，专注于高性能、低成本的消息队列服务。<strong>为了进一步释放 TubeMQ 周边的生态能力，我们将项目升级为 InLong，专注打造一站式海量数据集成框架。</strong></p> 
<p>Apache InLong 以腾讯内部使用的 TDBank 为原型，依托万亿级别的数据接入和处理能力，整合了数据采集、汇聚、存储、分拣数据处理全流程，拥有简单易用、灵活扩展、稳定可靠等特性。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-2adaeed4ddeffcf2fbefd1021d66479efaa.png" referrerpolicy="no-referrer"></p> 
<p><strong><span>Apache InLong 服务于数据采集到落地的整个生命周期，按数据的不同阶段提供不同的处理模块，主要包括：</span></strong></p> 
<ul> 
 <li><span>inlong-agent，数据采集 Agent，支持从指定目录或文件读取常规日志、逐条上报。后续也将扩展 DB 采集、HTTP 上报等能力。</span></li> 
 <li><span>inlong-dataproxy，一个基于 Flume-ng 的 Proxy 组件，支持数据发送阻塞和落盘重发，拥有将接收到的数据转发到不同 MQ（消息队列）的能力。</span></li> 
 <li><span>inlong-tubemq，腾讯自研的消息队列服务，专注于大数据场景下海量数据的高性能存储和传输，在海量实践和低成本方面有着良好的核心优势。</span></li> 
 <li><span>inlong-sort，对从不同的 MQ 消费到的数据进行 ETL 处理，然后汇聚并写入 Hive、ClickHouse、HBase、Iceberg 等存储系统。</span></li> 
 <li><span>inlong-manager，提供完整的数据服务管控能力，包括元数据、任务流、权限，OpenAPI 等。</span></li> 
 <li><span>inlong-audit，提供独立于数据流向、覆盖全流程的审计的数据审计服务。</span></li> 
 <li><span>inlong-dashboard，用于管理数据接入的前端页面，简化整个 InLong 管控平台的使用。</span></li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-bb4f773e906486acfadb168305544bef545.png" referrerpolicy="no-referrer"></p> 
<p><span>1.0 版本之前（包括 0.9.0 到 0.12.0），InLong 专注于打通基础链路和建设配套能力上。</span></p> 
<p><span>基础链路方面，完成了基于 TubeMQ 和 Apache Pulsar 两个消息队列的数据链路，分别满足低成本高性能、高一致性高性能的使用场景。</span></p> 
<p><span>配套能力建设方面，完成了各个模块部署步骤的简化，同时增加单机、Docker Compose 和 Kubernetes 部署；完成了各个模块指标体现建设，丰富了各维度监控指标；完成了全链路数据审计能力，让数据“位置”清晰可查。</span></p> 
<p><span><strong>在后续的版本中，InLong 将首先提供插件化的支持，方便快速扩展新的采集、入库流向；增加数据流管理，包括心跳状态、数据流启停等；同时强化全链路稳定性、性能，增加批量数据采集能力和多集群管理能力。</strong></span></p> 
<h3><strong>2 </strong><span><strong>Apache InLong <strong>(incubating) </strong>1.0.0 </strong></span><span><strong>版本主要特性</strong></span></h3> 
<p><span><strong><span>刚刚发布的 1.0.0-incubating 主要包括以下内容：</span></strong></span></p> 
<p><span>该版本关闭了约 124+ 个 issue，包含 8 个重大 feature 和 36 个 improvements。</span></p> 
<ul> 
 <li><span><strong>InLong Sort 支持单租户分拣</strong></span></li> 
</ul> 
<p><span>在 1.0.0 版本中，Sort 增加了单租户级别的分拣能力，可支持一条采集流启动一个 Flink 任务，为后续数据流状态管理提供了基础。</span></p> 
<ul> 
 <li><span><strong>InLong Sort 支持 Flink 1.13.5 版本</strong></span></li> 
</ul> 
<p><span>社区的同学之前就提过升级 Flink 版本，以支持在 InLong 中使用 FLink SQL。1.0.0 版本中，Sort 完成了对 Flink 1.13.5 的升级，方便 Sort 扩展新的 Sink 以及对接公有云场景。</span></p> 
<ul> 
 <li><span><strong>InLong Sort 支持 Standalone 模式</strong></span></li> 
</ul> 
<p><span>Sort 可以对 MQ 中的数据进行 ETL 处理，初期 Sort 只有 Flink 版本，虽然能使用到 Flink 强大的实时处理能力，但却增加了 InLong 项目对部署环境的要求，用户必须要有 Flink 集群才能运行 InLong。</span></p> 
<p><span>1.0.0 版本开始，InLong 引入了 Sort Standalone 模块，支持非 Flink 场景下的数据分拣。</span></p> 
<ul> 
 <li><span><strong>全流程审计数据的埋点和展示</strong></span></li> 
</ul> 
<p><span>上一个版本，InLong 引入了数据审计模块，但未完成数据的埋点和展示，审计服务不能完全使用。</span></p> 
<p><span>1.0.0 版本中，InLong Audit 不仅优化了审计 API 和容灾的场景，还完成了全组件的埋点和数据展示，实现了审计模块部署即可用。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-42490b7156da88c0fb810219cebc28bca39.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><span><strong>支持通过认证访问 Apache Pulsar</strong></span></li> 
</ul> 
<p><span>在之前的版本中，InLong 支持了基于 Apache Pulsar 数据链路。在实际场景中，Pulsar 集群都带有认证，在 1.0.0 版本中，实现访问带有认证的 Apache Pulsar 集群。</span></p> 
<ul> 
 <li><span><strong>DataProxy 支持 HTTP/UDP 协议</strong></span></li> 
</ul> 
<p><span>为了方便用户直接使用 DataProxy SDK 扩展 InLong 采集端的能力，1.0.0 版本在原有 TCP 协议的基础上，我们开放了 DataProxy HTTP/UDP 协议的支持。</span></p> 
<ul> 
 <li><span><strong>Agent DB 采集支持 SQL 采集</strong></span></li> 
</ul> 
<p><span>DB 采集是数据集成领域很常见的使用场景，InLong 开始补齐这块能力，实现对主流关系型数据库，增量/全量不同场景的支持。</span></p> 
<p><span>1.0.0 版本优先实现了通过 SQL 采集 MySQL 的数据，在后续的版本中完成对其它数据库以及 Binlog 的采集。</span></p> 
<ul> 
 <li><span><strong>其他特性及问题修复</strong></span></li> 
</ul> 
<p><span>相关内容请参考版本发版说明（文末标注），其中详细列出了本次版本的特性、提升 和 Bug 修复，以及具体的贡献者。</span></p> 
<h3><span><strong>3 </strong></span><span><strong>Apache InLong<span> </span><strong><strong>(incubating)</strong></strong> 后续规划</strong></span></h3> 
<p><span>后续版本，我们会进一步强化 InLong 的基础能力建设，同时扩展更多的数据源端和目标端，覆盖更多的使用场景，主要包括：</span></p> 
<ul> 
 <li><span>插件化能力</span></li> 
 <li><span>新增 Iceberg、ClickHouse 、Kafka 流向</span></li> 
 <li><span>新增关系数据库 Binlog 采集、Kafka 采集</span></li> 
</ul> 
<h3><span><strong>4 </strong></span><span><strong>Apache InLong(incubating) </strong></span><span><strong>贡献者招募</strong></span></h3> 
<p><span>Apache InLong(incubating) 当前共有 84 名 Contributor，</span><span>仍处在项目孵化的初期，还有很多待办事项，包括：Feature 开发、社区运营，文档翻译等，期待更多开源爱好者加入 InLong，一起将 InLong 打造成 Apache 顶级项目。</span></p> 
<p><span><strong>以下为 InLong 项目的时间线：</strong></span></p> 
<ul> 
 <li><span>2021年12月22日，发布 0.12.0 版本</span></li> 
 <li><span>2021年11月5日，发布 0.11.0 版本</span></li> 
 <li><span>2021年9月3日，发布 0.10.0 版本</span></li> 
 <li><span>2021年7月12日，发起更名后第一个版本 0.9.0 投票</span></li> 
 <li><span>2021年4月11日，完成社区改名，改为 Apache InLong</span></li> 
 <li><span>2021年2月11日，发起社区改名变更申请</span></li> 
 <li><span>2020年12月20日，进行项目改名讨论和投票</span></li> 
 <li><span>2020年5月30日，按照 Apache 社区规范发布第一个社区版本</span></li> 
 <li><span>2019年11月3日，进入 Apache 社区孵化</span></li> 
 <li><span>2019年9月12日，TubeMQ 对外开源并捐献给 Apache 社区</span></li> 
</ul> 
<hr> 
<ul> 
 <li>Apache InLong 项目官方网站：<span style="color:#021eaa">https://inlong.apache.org</span></li> 
 <li>Apache InLong GitHub 地址：<span style="color:#021eaa">https://github.com/apache/incubator-inlong</span></li> 
 <li>Apache InLong 版本发布历史：<span style="color:#021eaa">https://github.com/apache/incubatorinlong/blob/master/CHANGES.md</span></li> 
</ul>
                                        </div>
                                      
</div>
            