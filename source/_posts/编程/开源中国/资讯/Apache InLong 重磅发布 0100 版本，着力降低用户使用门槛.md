
---
title: 'Apache InLong 重磅发布 0.10.0 版本，着力降低用户使用门槛'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b3eb6ee244cef5b19fee435fcbbe16b2d57.png'
author: 开源中国
comments: false
date: Fri, 17 Sep 2021 14:10:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b3eb6ee244cef5b19fee435fcbbe16b2d57.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div>
   <img alt src="https://oscimg.oschina.net/oscnet/up-b3eb6ee244cef5b19fee435fcbbe16b2d57.png" referrerpolicy="no-referrer">
  </div> 
  <div>
    
  </div> 
  <div> 
   <blockquote> 
    <p>导语：Apache InLong 以腾讯内部使用的TDBank为原型，依托万亿级别的数据接入和处理能力，整合了数据采集、汇聚、存储、分拣数据处理全流程，拥有简单易用、灵活扩展、稳定可靠等特性。</p> 
   </blockquote> 
   <p>Apache InLong(孵化中) 刚刚发布了 0.10.0 版本，该版本是升级为 InLong（中文名：应龙） 后的第二个版本，着力解决InLong应用门槛高问题。该版本吸引腾讯内外 10 多位开发者参与，关闭超过 120 个issue， 开发超过 8 个重要Feature。</p> 
   <h2><strong>Apache InLong简介</strong></h2> 
   <p>Apache InLong（应龙）是腾讯捐献给 Apache 社区的一站式数据流接入服务平台，提供自动、安全、高性能、分布式的数据发布订阅能力，基于该系统用户可以轻松构建基于流式的数据应用。InLong 项目原本叫TubeMQ ，专注高性能、低成本的消息队列服务。为了进一步释放 TubeMQ 周边生态能力，我们将项目升级为 InLong ，专注打造一站式数据流接入服务平台。</p> 
   <p>Apache InLong 以腾讯内部使用的 TDBank 为原型，依托万亿级别的数据接入和处理能力，整合了数据采集、汇聚、存储、分拣数据处理全流程，拥有简单易用、灵活扩展、稳定可靠等特性。</p> 
   <div>
    <img alt src="https://oscimg.oschina.net/oscnet/up-e74e7d414e24faaf8dda586a7ba578d2c2a.png" referrerpolicy="no-referrer">
   </div> 
   <p>Apache InLong 服务于数据采集到落地的整个生命周期，按数据的不同阶段提供不同的处理模块，主要包括：</p> 
   <ul> 
    <li> <p>inlong-agent ，数据采集 Agent ，支持从指定目录或文件读取常规日志，进行逐条的数据上报。后续也将扩展 DB 采集，扩展HTTP上报等能力。</p> </li> 
    <li> <p>inlong-dataproxy ，一个基于 Flume-ng 的 Proxy 组件，支持数据发送阻塞、落盘重发，拥有将接收数据后转发到不同MQ（消息队列）的能力。</p> </li> 
    <li> <p>inlong-tubemq ，腾讯自研的消息队列服务，专注服务大数据场景下海量数据的高性能存储和传输，在海量实践和低成本方面有着比较好的核心优势。</p> </li> 
    <li> <p>inlong-sort ，从不同的 MQ 消费数据后进行 ETL 处理，然后将数据汇聚并写入 Hive、ClickHouse、Hbase、IceBerg 等。</p> </li> 
    <li> <p>inlong-manager ，提供完整的数据服务管控能力，包括元数据、OpenAPI、任务流、权限等。</p> </li> 
    <li> <p>inlong-website ，一个用于管理数据接入的前端页面，简化整个 InLong 管控平台的使用。</p> </li> 
   </ul> 
   <h2><strong>Apache InLong 0.10.0版本简介</strong></h2> 
   <p>我们从上个版本（ 0.9.0 ）始，将 TubeMQ 升级为 InLong ，第一次将全链路数据接入能力开源出来。随着 0.9.0 发布后，我们组织了一次线上 Meetup ，探讨了大家在初次尝鲜 InLong 过程当中遇到的问题，发现大多数同学反馈 InLong 的“使用门槛太高，部署难度太大”。InLong 包括 6 个模块，并且每个模块拥有单独的编译打包、配置、启停脚本，完整的使用 InLong 还依赖 MySQL、Hive、Flink 集群等第三方服务组件，真正把 InLong 用起来的社区用户寥寥无几。</p> 
   <p>为了解决社区用户反馈的”开头难“问题， 我们将 0.10.0 版本开发目标设定为“<strong>降低 InLong 使用门槛，方便社区用户用起来</strong>”，在新版本中主要完成了以下几个方面的工作，来简化 InLong 的安装和使用：</p> 
   <ul> 
    <li> <p>所有组件 Docker 化，提供一键安装能力</p> </li> 
    <li> <p>进一步整合 InLong 所有模块，简化模块配置</p> </li> 
    <li> <p>提供 Example Demo ，手把手教如何使用 InLong</p> </li> 
   </ul> 
   <h2><strong>Apache InLong 0.10.0 版本主要特性</strong></h2> 
   <h3><strong>全面拥抱 GitHub</strong></h3> 
   <p>在之前版本，InLong 的所有 Issue 由Jira管理，提交新的 PR 需要在 Jira 和 GitHub 来回跳转。同时，由于 Jira 和 GitHub 账号不通，新的贡献者需要先单独注册 Jira 账号和配置权限。在最近发布的 0.10.0 版本中，我们将 Jira Issue 历史迁移到了 GitHub Issue ，并设置了配套的 Issue 模板，方便开发者创建 Issue 和关联 PR 。同时，我们将 CI 工具由 Travis 迁移到 GitHub Actions ，配置了独立的 Workflow 进行代码编译、UT，很大程度提高了 PR 的合入效率。</p> 
   <h3><strong>支持 Docker-Compose 一键部署</strong></h3> 
   <p>InLong 拥有超过 6 个模块，完整的使用 InLong 还依赖 MySQL、Hive、Flink 集群等第三方服务组件，为了方便新用户快速了解 InLong ，直观感受 InLong 的特性，在 0.10.0 版本中，我们将所有组件 Docker 化，借助 Docker-Compose 提供一键安装能力，感兴趣的用户可以参考 InLong Standalone Using Docker Compose 体验。</p> 
   <p><strong>InLong Standalone Using Docker Compose地址：</strong></p> 
   <p>https://github.com/apache/incubator-inlong/blob/master/docker/docker-compose/README.md</p> 
   <h3><strong>增加 Hive 入库 Example</strong></h3> 
   <p>0.9.0 版本我们只开放了 InLong 入库Hive的能力，为了指导大家快速将采集的数据分拣到 Hive ，我们增加Hive入库Example，Step by Step帮助用户快速开始使用 InLong 。</p> 
   <p><strong>入库Hive示例：</strong></p> 
   <p>https://inlong.apache.org/zh-cn/docs/example.html</p> 
   <h3><strong>InLong Manger 整合 OpenAPI 和 API</strong></h3> 
   <p>InLong Manager 为 WebSite 提供了统一的访问 API ，为了方便其它模块获取元数据信息提供了统一的 OpenAPI 。在之前的版本中， API 和 OpenAPI 分别有两个独立的项目管理，安装时需要单独配置和启动，使用不同的端口提供服务。在 0.10.0 版本中，我们整合了 OpenAPI 和 API ，使用不同 URL Path 进行区分，通过一个项目来管理两套 API ，实现 Manager 只用部署一次的效果。</p> 
   <h3><strong>InLong Sort 增加 Pulsar 分拣能力</strong></h3> 
   <p>TubeMQ 的架构在性能和成本上拥有天然的优势，但没有多副本机制，可能会丢数据，而 Apache Pulsar 可以弥补这方面的不足。同时，为了实现 InLong 能够快速复用已有的消息队列服务，我们计划全链路支持 Pulsar ，在 0.10.0 版本中，InLong Sort 优先支持了 Pulsar 数据源的分拣能力，在后续版本中会完善 DataProxy->Pulsar、Manager->Pulsar ，实现 InLong 全链路支持 Apache Pulsar 。当然，我们也希望在未来全链路支持 Kafka 。</p> 
   <h3><strong>InLong Sort 支持指标系统</strong></h3> 
   <p>InLong Sort 中需要统计各个阶段数据条数的指标数据，如读入数据的条数，解析阶段失败/成功的数据条数，入库条数。指标系统用来统计系统各个阶段的数据条数，为了保证指标和数据语义的一致，我们通过 Flink 的 side output stream 输出指标。同时配合flink的窗口机制对指标进行预聚合，保证输出指标的量级不会太大。在 0.10.0 版本中，首先支持了通过日志的方式输出指标（At-least-once），后续我们计划扩展输出指标的系统，如 MySQL ，HBase 等，同时支持输出指标的 Exactly-once 。</p> 
   <h3><strong>InLong WebSite 国际化</strong></h3> 
   <p>上个版本重点是整合所有 InLong 所有模块，前端国际化没有来得及做，在这个版本一起优化了。InLong 当前还有很多待翻译的文档，计划在后续版本一起完善，期待英语不错的社区爱好者加入翻译大军。</p> 
   <h3><strong>InLong TubeMQ 优化 Web API</strong></h3> 
   <p>该特性将以往元数据变更后需要外部被动、批量的加载调整为 由 Master 自动的分批加载，并且数据加载与后续的配置变更同步进行。</p> 
   <h3><strong>InLong Agent 重构 DataProxy 配置获取方式</strong></h3> 
   <p>InLong Agent 采集到数据后，会将数据发送到 DataProxy ，所以 DataProxy 的配置信息需要 Agent 提前拿到。在上个版本的实现中，我们在每个接入任务的Agent配置文件中指定 DataProxy 的地址等信息。而在 0.10.0 版本中，我们重构了这部分实现，交由 Manager 管理 DataProxy 地址等信息，Agent 中配置的接入任务直接通过 Manager OpenAPI 获取。</p> 
   <h3><strong>进一步整合 InLong 各模块</strong></h3> 
   <p>在上个版本，InLong 各个模块编译后的二进制文件分散在不同目录，启停配置、命名、端口使用等也不统一，InLong 给人一种“拼凑”的印象。在 0.10.0 版本中，为了进一步强化 InLong 整体性，我们将各个模块编译结果输出到统一目录，增加Maven编译 InLong WebSite ，并规范了目录、脚本等名称，重新整理了安装部署文档，使所有模块更加统一。</p> 
   <h2><strong>Apache InLong 后续规划</strong></h2> 
   <p>在 InLong 后续版本规划中，我们会进一步释放 InLong 的能力，覆盖更多的使用场景，主要包括</p> 
   <ul> 
    <li> <p>支持 Apache Pulsar 全链路数据接入能力</p> </li> 
    <li> <p>支持 ClickHouse、Apache Iceberg、Apache HBase 等数据流向</p> </li> 
    <li> <p>InLong on Kubernetes</p> </li> 
   </ul> 
   <h2><strong>Apache InLong 贡献者招募</strong></h2> 
   <p>Apache InLong目前还处在项目孵化的初期，还有很多工作需要做，包括社区运营、文档翻译、Feature 开发等，期待更多的开源爱好者一起共建。在过去的一个版本，Apache InLong 新增国内外贡献者 6 名，实现快速增长。当前社区重于代码，我们急需更多的贡献者加入快速发展的项目社区，努力将 InLong 打造成 Apache 顶级项目，以下为 InLong 重要发展时间点：</p> 
   <ul> 
    <li> <p>2019年9月12日，TubeMQ 对外开源并捐献给 Apache 社区；</p> </li> 
    <li> <p>2019年11月3日，进入 Apache 社区孵化；</p> </li> 
    <li> <p>2020年5月30日，按照 Apache 社区规范发布第一个社区版本；</p> </li> 
    <li> <p>2020年12月20日，进行项目改名讨论和投票；</p> </li> 
    <li> <p>2021年2月11日，发起社区改名变更申请；</p> </li> 
    <li> <p>2021年4月11日，完成社区改名，调整为 Apache InLong；</p> </li> 
    <li> <p>2021年7月12日，发起更名后第一个版本 0.9.0 投票。</p> </li> 
   </ul> 
   <p><strong>Apache InLong项目官方网站：</strong></p> 
   <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finlong.apache.org%2Fzh-cn%2F" target="_blank">https://inlong.apache.org/zh-cn/</a></p> 
   <p><strong>Apache InLongGitHub地址：</strong></p> 
   <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-inlong" target="_blank">https://github.com/apache/incubator-inlong</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            