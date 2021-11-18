
---
title: 'Apache InLong(incubating) 发布 0.11.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1118/185252_cOTK_4252687.png'
author: 开源中国
comments: false
date: Thu, 18 Nov 2021 18:53:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1118/185252_cOTK_4252687.png'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p style="margin-left:0; margin-right:0"><strong>InLong(应龙)</strong> : 中国神话故事里的神兽，引流入海，借喻 InLong 系统提供数据接入能力。</p> 
</blockquote> 
<p style="margin-left:0; margin-right:0">Apache InLong(incubating) 由原 Apache TubeMQ（incubating）改名而来，伴随着名称的改变，InLong 也由单一的消息队列升级为一站式的数据集成解决方案，支持了大数据领域的采集、汇聚、缓存和分拣功能，用户只需要简单的配置就可以把数据从数据源导入到实时计算引擎或者落地到离线存储。</p> 
<p style="margin-left:0; margin-right:0">刚刚发布的 0.11.0-incubating 版本是改名之后的第三个版本，这个版本：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">进一步降低用户的使用门槛，支持 InLong 所有模块 on Kubernets，并且对官网进行了重构，用户可以更加方便地查阅相关文档</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持更多的业务场景，增加 DataProxy -> Pulsar 的数据流向，覆盖对数据完整性、一致性更高要求的场景</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持更多语言的 SDK，这个版本开放了生产级别的 TubeMQ Go SDK，方便使用 Go 语言的用户接入</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">该版本关闭 80+ 个 issue，包含四个重大 feature 和 35 个 improvements 。</p> 
<h4 style="margin-left:0px; margin-right:0px"><strong>Apache InLong(incubating) 简介</strong></h4> 
<p style="margin-left:0; margin-right:0"><span style="color:#548bde"><strong>Apache InLong (https://inlong.apache.org) （应龙）</strong></span>是腾讯捐献给 Apache 社区的一站式数据流接入服务平台，提供自动、安全、可靠和高性能的数据传输能力，方便业务构建基于流式的数据分析、建模和应用。InLong 项目原名 TubeMQ ，专注于高性能、低成本的消息队列服务。为了进一步释放 TubeMQ 周边的生态能力，我们将项目升级为 InLong，专注打造一站式数据流接入服务平台。</p> 
<p style="margin-left:0; margin-right:0">Apache InLong 以腾讯内部使用的 TDBank 为原型，依托万亿级别的数据接入和处理能力，整合了数据采集、汇聚、存储、分拣数据处理全流程，拥有简单易用、灵活扩展、稳定可靠等特性。</p> 
<p><img height="273" src="https://static.oschina.net/uploads/space/2021/1118/185252_cOTK_4252687.png" width="700" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0">Apache InLong 服务于数据采集到落地的整个生命周期，按数据的不同阶段提供不同的处理模块，主要包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">inlong-agent，数据采集 Agent，支持从指定目录或文件读取常规日志、逐条上报。后续也将扩展 DB 采集、HTTP 上报等能力。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">inlong-dataproxy，一个基于 Flume-ng 的 Proxy 组件，支持数据发送阻塞和落盘重发，拥有将接收到的数据转发到不同 MQ（消息队列）的能力。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">inlong-tubemq，腾讯自研的消息队列服务，专注于大数据场景下海量数据的高性能存储和传输，在海量实践和低成本方面有着良好的核心优势。注：InLong 0.11.0 后台增加了对 Apache Pulsar 的支持，全链路数据流和管控工作会在下个版本完成。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">inlong-sort，对从不同的 MQ 消费到的数据进行 ETL 处理，然后汇聚并写入 Hive、ClickHouse、Hbase、Iceberg 等存储系统。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">inlong-manager，提供完整的数据服务管控能力，包括元数据、任务流、权限，OpenAPI 等。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">inlong-website，用于管理数据接入的前端页面，简化整个 InLong 管控平台的使用。</p> </li> 
</ul> 
<h4 style="margin-left:0px; margin-right:0px"><strong>0.11.0 版本主要特性</strong></h4> 
<p style="margin-left:0; margin-right:0"><strong>InLong on Kubernetes</strong></p> 
<p style="margin-left:0; margin-right:0">InLong 包括了数据采集、数据汇聚、数据缓存，数据分拣以及集群管控等多个组件，为了方便用户的使用和支持云原生特性，InLong 的所有组件都已支持部署在 Kubernetes。感谢 @shink 贡献的这个特性，具体可以参考：<span style="color:#548bde">INLONG-1308<span>[1]</span></span></p> 
<p style="margin-left:0; margin-right:0"><strong>DataProxy -> Pulsar 数据流打通</strong></p> 
<p style="margin-left:0; margin-right:0">在 0.11.0 版本之前，InLong 的数据缓存层只能支持 TubeMQ，TubeMQ 适用于超大规模数据量的场景，在极端场景下存在丢失少量数据的风险；为了提供可靠的数据采集和传输，Inlong 0.11.0 版本增加了对于 Apache Pulsar 的支持，现在 InLong 支持数据从 Agent -> DataProxy -> TubeMQ / Pulsar -> Sort 的链路。Pulsar 的引入，使得 InLong 覆盖的应用场景更加丰富，可以满足更多用户的需求。感谢 @baomingyu 对于这个特性的贡献，更多信息请参考：<span style="color:#548bde">INLONG-1330<span>[2]</span></span></p> 
<p style="margin-left:0; margin-right:0"><strong>Go 语言 SDK</strong></p> 
<p style="margin-left:0; margin-right:0">在 0.11.0 版本前，TubeMQ 支持 Java、C++ 和 Python 三种语言的 SDK。随着 Go 语言的应用越来越多，社区对于 Go 语言 SDK 的需求也日益迫切，0.11.0 版本正式引入了 TubeMQ 的 Go 语言 SDK。丰富了多语言 SDK，也降低了 Go 语言用户的接入和使用难度。感谢 @TszKitLo40 贡献的这个特性，更多详情请参考：<span style="color:#548bde">INLONG-624<span>[3]</span>，INLONG-1578<span>[4]</span>，INLONG-1584<span>[5]</span>，INLONG-1666<span>[6]</span>，INLONG-1682<span>[7]</span></span></p> 
<p style="margin-left:0; margin-right:0"><strong>官网重构</strong></p> 
<p style="margin-left:0; margin-right:0">InLong 0.11.0 版本采用 Docusaurus 重构了<span style="color:#548bde">官网(</span><u>https://inlong.apache.org</u><span style="color:#548bde">)</span>，提供了更加简洁、直观的文档管理和展示能力。感谢 @leezng 对于这个特性的贡献。更多详情请参考：<span style="color:#548bde">INLONG-1631<span>[8]</span>，INLONG-1632<span>[9]</span>，INLONG-1633<span>[10]</span>，INLONG-1634<span>[11]</span>，INLONG-1635<span>[12]</span>，INLONG-1636<span>[13]</span>，INLONG-1637<span>[14]</span>，INLONG-1638<span>[15]</span></span></p> 
<p style="margin-left:0; margin-right:0">除了上述重大 feature，InLong 0.11.0 版本还有其他的关键改进，包括但不限于：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在主 Repo 中增加了贡献指引，<span style="color:#548bde">INLONG-1623<span>[16]</span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">增加 Inlong-Manager 对 DataProxy 的配置管理，<span style="color:#548bde">INLONG-1595<span>[17]</span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化了 github issue 模板，<span style="color:#548bde">INLONG-1585<span>[18]</span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">代码规范 Checkstyle 优化，<span style="color:#548bde">INLONG-1571<span>[19]</span>，INLONG-1593<span>[20]</span>，INLONG-1662<span>[21]</span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Agent 引入消息过滤器，<span style="color:#548bde">INLONG-1641<span>[22]</span></span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">0.11.0 版本还修复了~45个 bug，在此，感谢所有为 Inlong 社区做出贡献的各位同学（排名不分先后）：shink，baomingyu，TszKitLo40，pierre94，yuanboliu，dockerzhang，leezng，ruanwenjun，leo65535，healchow，EMsnap，luchunliang，gosonzhang，guangxuCheng</p> 
<h4 style="margin-left:0px; margin-right:0px"><strong>Apache InLong(incubating) 后续规划</strong></h4> 
<p style="margin-left:0; margin-right:0">在 InLong 后续版本中，我们会进一步释放 InLong 的能力，覆盖更多的使用场景，主要包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">支持 Apache Pulsar 全链路数据接入能力，包括后端处理和前端管理</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持 ClickHouse、Apache Iceberg、Apache HBase 等数据存储功能</p> </li> 
</ul> 
<h4 style="margin-left:0px; margin-right:0px"><strong>Apache InLong(incubating) 贡献者招募</strong></h4> 
<p style="margin-left:0; margin-right:0">Apache InLong(incubating) 当前共有 62 名 contributor，仍处在项目孵化的初期，还有很多待办事项，包括：Feature 开发、社区运营，文档翻译等，期待更多开源爱好者加入 InLong，一起将 InLong 打造成 Apache 顶级项目。</p> 
<p style="margin-left:0; margin-right:0">以下为 InLong 项目的时间线：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">2021年11月5日，发布 0.11.0 版本</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">2021年9月3日，发布 0.10.0 版本</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">2021年7月12日，发起更名后第一个版本 0.9.0 投票</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">2021年4月11日，完成社区改名，改为 Apache InLong</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">2021年2月11日，发起社区改名变更申请</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">2020年12月20日，进行项目改名讨论和投票</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">2020年5月30日，按照 Apache 社区规范发布第一个社区版本</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">2019年11月3日，进入 Apache 社区孵化</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">2019年9月12日，TubeMQ 对外开源并捐献给 Apache 社区</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>Apache InLong 项目官方网站</strong></p> 
<p style="margin-left:0; margin-right:0"><u>https://inlong.apache.org</u></p> 
<p style="margin-left:0; margin-right:0"><strong>Apache InLong GitHub 地址</strong></p> 
<p style="margin-left:0; margin-right:0"><u>https://github.com/apache/incubator-inlong</u></p> 
<p style="margin-left:0; margin-right:0"><strong>参考资料</strong></p> 
<p style="margin-left:0; margin-right:0">[1]<span>INLONG-1308:https://github.com/apache/incubator-inlong/issues/1308</span></p> 
<p style="margin-left:0; margin-right:0">[2]<span>INLONG-1330:https://github.com/apache/incubator-inlong/issues/1330</span></p> 
<p style="margin-left:0; margin-right:0">[3]<span>INLONG-624:https://github.com/apache/incubator-inlong/issues/624</span></p> 
<p style="margin-left:0; margin-right:0">[4]<span>INLONG-1578:https://github.com/apache/incubator-inlong/issues/1570</span></p> 
<p style="margin-left:0; margin-right:0">[5]<span>INLONG-1584:https://github.com/apache/incubator-inlong/issues/1584</span></p> 
<p style="margin-left:0; margin-right:0">[6]<span>INLONG-1666:https://github.com/apache/incubator-inlong/issues/1666</span></p> 
<p style="margin-left:0; margin-right:0">[7]<span>INLONG-1682:https://github.com/apache/incubator-inlong/issues/1682</span></p> 
<p style="margin-left:0; margin-right:0">[8]<span>INLONG-1631:https://github.com/apache/incubator-inlong/issues/1631</span></p> 
<p style="margin-left:0; margin-right:0">[9]<span>INLONG-1632:https://github.com/apache/incubator-inlong/issues/1632</span></p> 
<p style="margin-left:0; margin-right:0">[10]<span>INLONG-1633:https://github.com/apache/incubator-inlong/issues/1633</span></p> 
<p style="margin-left:0; margin-right:0">[11]<span>INLONG-1634:https://github.com/apache/incubator-inlong/issues/1634</span></p> 
<p style="margin-left:0; margin-right:0">[12]<span>INLONG-1635:https://github.com/apache/incubator-inlong/issues/1635</span></p> 
<p style="margin-left:0; margin-right:0">[13]<span>INLONG-1636:https://github.com/apache/incubator-inlong/issues/1636</span></p> 
<p style="margin-left:0; margin-right:0">[14]<span>INLONG-1637:https://github.com/apache/incubator-inlong/issues/1637</span></p> 
<p style="margin-left:0; margin-right:0">[15]<span>INLONG-1638:https://github.com/apache/incubator-inlong/issues/1638</span></p> 
<p style="margin-left:0; margin-right:0">[16]<span>INLONG-1623:https://github.com/apache/incubator-inlong/issues/1623</span></p> 
<p style="margin-left:0; margin-right:0">[17]<span>INLONG-1595:https://github.com/apache/incubator-inlong/issues/1595</span></p> 
<p style="margin-left:0; margin-right:0">[18]<span>INLONG-1585:https://github.com/apache/incubator-inlong/issues/1585</span></p> 
<p style="margin-left:0; margin-right:0">[19]<span>INLONG-1571:https://github.com/apache/incubator-inlong/issues/1571</span></p> 
<p style="margin-left:0; margin-right:0">[20]<span>INLONG-1593:https://github.com/apache/incubator-inlong/issues/1593</span></p> 
<p style="margin-left:0; margin-right:0">[21]<span>INLONG-1662:https://github.com/apache/incubator-inlong/issues/1662</span></p> 
<p style="margin-left:0; margin-right:0">[22]<span>INLONG-1641:https://github.com/apache/incubator-inlong/issues/1641</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            