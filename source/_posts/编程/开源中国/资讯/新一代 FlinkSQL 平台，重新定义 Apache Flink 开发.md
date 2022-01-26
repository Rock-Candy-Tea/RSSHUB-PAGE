
---
title: '新一代 FlinkSQL 平台，重新定义 Apache Flink 开发'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-502abd74dc2ea271d5e104225b057402b6b.png'
author: 开源中国
comments: false
date: Wed, 26 Jan 2022 18:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-502abd74dc2ea271d5e104225b057402b6b.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:start"><span>前言</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 0.5.1 已发布，它将重新定义 Apache Flink 的开发运维，让其如虎添翼，降本增效。</span></p> 
<h2 style="text-align:start"><span>现状</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Flink Forward Asia 2021 刚刚结束，从 Apache Flink 中文社区发起人、阿里巴巴开源大数据平台负责人王峰（花名莫问）老师得知 Apache Flink 将不止于计算，数仓架构或兴起一轮变革，并且看到越来越多的企业开始大规模应用 Flink 来建设平台。美团数据开发平台负责人鞠大升老师在圆桌会议中提到 FlinkSQL 平台的建设目前是企业应用 Flink 的一道门槛，而平台建设将直接影响 Flink 任务从开发到运维的一系列投入成本。投入资源的大厂商目前纷纷建立了自己的 Flink 平台及运维团队，也有部分厂商选择了基于开源项目的 flink-streaming-platform-web 构建了自己的任务平台，而更多的厂商还在止步于平台的门槛。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>而未来批流一体的趋势下，以及流式数仓的新动向，FlinkSQL 的场景将更加广泛且易用。</span></p> 
<h2 style="text-align:start"><span>简介</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>实时即未来，Dinky 为 Apache Flink 而生，让 Flink SQL 纵享丝滑，并致力于实时计算平台建设。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 架构于 Apache Flink，增强 Flink 的应用与体验，探索流式数仓。即站在巨人肩膀上创新与实践，Dinky 在未来批流一体的发展趋势下潜力无限。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>最后，Dinky 的发展皆归功于 Apache Flink 等其他优秀的开源项目的指导与成果。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDataLinkDC%2Fdlink" target="_blank">https://github.com/DataLinkDC/dlink</a></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="749" src="https://oscimg.oschina.net/oscnet/up-502abd74dc2ea271d5e104225b057402b6b.png" width="1530" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start"><span>适用场景</span></h2> 
<h3 style="text-align:start"><span>交互式 FlinkSQL 开发与调试平台</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>多数企业内部大都建立了自己的 Flink 任务托管平台，在 FlinkSQL 的趋势下，其 sql 的开发与调试的需求日益显现。Dinky 则可以提供开源领域最专业的 FlinkSQL 开发与调试环境，避免盲写口径带来的诸多问题与高成本。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在部署 Dinky 之后，通过搭建相关外部执行环境，如 Yarn-Session，可以使用共享会话功能或者 FlinkSQLEnv 来持久化 Flink 的 Catalog；通过 Select 和 Show 实时数据图表预览功能，为 FlinkSQL 进行 OLAP 或子句查询提供了强力支持；基于自定义文档与上下文的自动提示与补全则可以快速辅助编写 sql，避免书写错误、官网翻 UDF 和配置等；语法片段则可以实现全局变量或者sql片段，使得sql语句可以被复用；CREATE AGGTABLE 则可以提供目前 SQL API 不支持的表值聚合函数的定义与使用；语法校验与逻辑检查则可以用真实环境来校验语句，具备指导修改的能力，做到通过即用的效果；支持血缘分析与查看 JobPlan；支持其他数据源的 SQL 查询与执行的能力，例如执行 Mysql、Doris 等的语句。</span></p> 
<h3 style="text-align:start"><span>FlinkSQL Server</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>假如您具备自己的数据平台，但在实时任务方面支持欠佳，同时又想继续使用自身成熟的项目、权限和资源等管理，您可以通过部署 Dinky 作为 FlinkSQL Server，数据平台使用 OpenAPI 来提交与运维任务，进行来弥补实时模块的欠缺。后续社区也将提供 Dinky 作为组件接入其他平台进行生产实践的案例与经验分享。</span></p> 
<h3 style="text-align:start"><span>实时计算平台</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 具备各种模式的 Flink 任务提交以及 SavePoint 的自动化管理，可以通过它开发 FlinkSQL 的流式或离线任务，并交由它自动地提交及恢复任务，满足实时计算平台的基本功能需求，后续 0.6 将上线运维中心，进一步增强其数据开发闭环的运维能力。</span></p> 
<h2 style="text-align:start"><span>核心特性</span></h2> 
<h3 style="text-align:start"><span>支持 Flink SQL 所有模式的自动化提交</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 提供了 Local、Standalone、Yarn-Session、Yarn-Per-Job、Yarn-Application、K8S-Session 和 K8S-Application 的 FlinkSQL 任务提交以及 SavePoint 的自动托管与恢复。</span></p> 
<h3 style="text-align:start"><span>支持 Select 和 Show 的交互式图表查询</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 提供了 Local、Standalone、Yarn-Session 和 K8S-Session 的 Select 与 Show 语句的查询结果反馈，可以表格、折线图、条形图、饼图等多种形式展现，并支持 ChangLog 和 Table 的两种数据方式，甚至支持其他数据源的 SQL 查询，如 Mysql、Oracle、Clickhouse、Doris 等，可通过 SPI 插件化扩展。在开源领域与 Zeppelin 相似。</span></p> 
<h3 style="text-align:start"><span>支持 Flink SQL 所有语法与底层配置</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 自身模拟了 Flink 真实的运行环境，可以支持 Flink SQL 所有语法与 Configuration，并对语句集进行了优化，额外提供了语法片段、AGGTABLE 表值聚合、FlinkSQLEnv 环境复用等增强功能。如同 MybatisPlus 和 Mybatis 一样，只做增强和优化，不做修改。</span></p> 
<h3 style="text-align:start"><span>支持企业级 SQL 平台开发交互功能</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 的核心优势在于提供了全面的企业级 SQL 平台开发交互的能力，如环境会话、自动提示与补全、语法高亮美化、语法校验与逻辑验证、异常反馈、JobPlan 图、血缘分析、SQL 导出、各种快捷键等功能，此外还支持集群、Jar、数据源、文档的管理。</span></p> 
<h3 style="text-align:start"><span>支持插件式扩展能力</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 内部众多功能采用了如 SPI 等的插件设计，可以自定义扩展各种能力，如数据源、Flink 内核版本、Flink CDC、Flink Connector、Dinky 自身引擎能力等。其开放的扩展能力设计，使其可以轻松实现各种数据业务需求如实时入仓（Hive、Doris、ClickHouse 等）、实时入湖（Hudi、Iceberg 等）、流式数仓（Kafka）等。</span></p> 
<h3 style="text-align:start"><span>支持无侵入和 OpenAPI 的能力</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 支持部署在 Flink 集群、Hadoop 集群、K8S 集群之外，且不需要在各集群内部署任何插件，不对已有环境造成侵入，开箱即用。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 自身提供了多种 OpenAPI 接口，可以将自己的核心功能接口提供给第三方系统，当作 FlinkSQL Server 来完成 SQL 作业的代理提交与运维。第三方系统可以是企业内建数据平台、作业调度平台、业务系统等。</span></p> 
<h3 style="text-align:start"><span>开箱即用且轻量</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 目前部署极为简单，只依赖 Mysql 作为业务库，支持前后端分离部署。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 操作简易且业务简单，且为简单的 SpringBoot 项目，非常适合基于此项目建立企业内部的实时计算平台并且根据自身业务进行二次定制开发。</span></p> 
<h3 style="text-align:start"><span>生态实践分享</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 会定期分享基于 Dinky 如何快速构建各种生态对接的实践和经验分享，也会同步分享各企业在使用 Dinky 构建新一代数据平台的思路与踩坑经验。</span></p> 
<h2 style="text-align:start"><span>Roadmap</span></h2> 
<h3 style="text-align:start"><span>运维中心</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 0.6.0 将围绕运维中心进行建设，包括任务生命周期管理、运行监控、作业日志、钉钉报警推送、流作业自动恢复等。</span></p> 
<h3 style="text-align:start"><span>元数据中心</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 0.7.0 将实现元数据中心建设，目前支持对外部元数据的采集功能，将建设统一的元数据管理，使其可以不需要依赖第三方元数据平台，独自进行更加适合实时数仓的元数据管理操作，统一规范拥有大量数据表、复杂关系的建设需求。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>此外，基于元数据建立血缘和影响分析的能力。</span></p> 
<h3 style="text-align:start"><span>企业级管理功能</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 0.7.0 将实现企业级管理能力，如多租户、项目、角色、权限、审计等。</span></p> 
<h3 style="text-align:start"><span>可视化功能</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 后续将实现海量库表数据同步可视化任务构建、StreamGraph 的可视化修改等功能。</span></p> 
<h3 style="text-align:start"><span>Flink 更多增强功能</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dinky 后续将提供更多的 Flink 增强功能，如多版本 Flink-Client Server、</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>自动扩缩容、SQL 翻译及生成、Dlink-Jdbc 、离线任务依赖调度等。</span></p> 
<h2 style="text-align:start"><span>致语</span></h2> 
<h3 style="text-align:start"><span>aiwenmo</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Apache Flink 近年来发展尤为迅速且社区火爆，在 Flink Forward Asia 2021 上更是将重新定义实时数仓架构。Dlink 作为 FlinkSQL 的交互式开发平台，显著得降低了 FlinkSQL 任务的开发与运维成本，目前正迈向流式数仓的建设目标。 </span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>作为 Dlink 的发起人，见证了从灵感到开源的落地，虽然道阻且长，但是社区的陪伴与鼓励是勇往直前的最大动力。而 Dinky 的定义，则指明了前进的方向——架构于 Apache Flink 的批流一体 DataOps。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>最后，我们会响应国家十四五数字经济发展规划，为各行业的数字化转型提供开源的实时数据平台建设方案。</span></p> 
<h3 style="text-align:start"><span>walkhan</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Dlink 作为 FlinkSQL的一款交互式开发平台，从0.1版本锥形到如今的0.5版本，经过这几个版本的迭代，已经解决了使用 FlinkSQL 用户的一些痛点，并具备生产可用级别。也为最近几年比较火热的流批一体化打下了坚实的基础。Dlink 社区秉承自由开放共享的精神，希望更多的人能参与进来共建 Dlink 社区。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>开源是一种文化，也是一种精神。这种文化和精神必须秉承着自由，开放共享的理念，造福于全人类。Flink 作为当今火热的流批一体化计算引擎以及作为我的开源引路人，我将在外部生态 Dinky 社区持续为 Flink 的发展尽我的一点绵薄之力。由此，经过几个月 Dinky 开源社区对我的认可，正式成为社区成员之一。我也会秉承自由，开放的开源文化精神，为 Dinky 开源社区的推动发展做出贡献。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>最后祝愿 Dinky 社区越做越好，以一种开放自由的开源文化迎接新的挑战和机遇。</span></p> 
<h3 style="text-align:start"><span>coderTomato</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>偶然的机会在 GitHub 上发现了 dlink 开源项目，dlink 是一款依托于实时框架 Flink 的可视化的 FlinkSQL 交互式开发平台，使用户能够在 web 编辑器中编写 FlinkSQL，其提供的 sql 语法高亮、自动补全、sql 逻辑校验、血缘分析、任务启停等功能，大大降低了 Flink 的使用门槛，基于 Dlink 的简单易用，轻量级的特性，以被我司大数据平台作为流式作业提交的工具。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>作为 Dlink 的使用者和贡献者，见证了 Dlink 从 0.1 版本到如今的 0.5 版本的迭代，功能的逐步完善。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>最后祝愿 Dlink 社区发展越来越好，让更多的人参与进来一起做大做强 Dlink 社区。</span></p> 
<h3 style="text-align:start"><span>xbg</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>偶然机会在开源中国了解到 Dinky，Dinky 是一款可视化的 Flink Sql 的交互式开发平台产品，依托当前最火的实时框架 Flink ，极大方便了开发人员编写 Flink SQL 作业的全过程，具有开箱即用，轻量级等优秀特点。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在 Flink Forward Asia 2021 的分享中，基本看到 SQL 语言作为数据开发的第一语言，被众多大公司和大平台进行实时场景的开发与应用，也证明了 Dinky 依托 Flink SQL 开展全流程开发平台和 Flink 生态的发展路线一致，致力于流批一体的应用更具普遍性和快速性，共同发展。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>感谢 Dinky 开发者和建设者，在包容的开源文化和中国数字化建设发展方向作出的贡献，致敬！</span></p> 
<h2 style="text-align:start"><span>精彩瞬间</span></h2> 
<h3 style="text-align:start"><span>登录</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-ee611f4f95f0c1cb1a1cb0f488d2b6d64f9.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>首页</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-6b06a18bd6d6b771ef2775aa1f70068f600.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>FlinkSQL Studio</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-22491b433186e69367c2a77a7b383978831.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>自动补全</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-861429fd4820d6d8079a2fd698fd257153e.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>ChangeLog 预览</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-abf7e499a54e9cdffcd69215eb6d76f7636.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>折线图</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-7a5ee710c8685456a7b234017c3b2f4bf75.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>Table 预览</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-29d6e8a485f50da29712c11cf178c258005.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>校验</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-354b05d87951c31f97941544813d7d90f05.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>JobPlan</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-dcfbde67e752ca690a9ada1c47ca454a1c5.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>导出</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-a8e895ec6b76fd91803e4b293cc3f1401dd.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>血缘</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-830a79fd82e744ef8ace89fac20e2d34e3f.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>savepoint</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-f6c00a63d95de8bedea3ede177774f2e147.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>会话</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-57c98cdac1912ba8bd7e7688cdb33b47e6e.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>元数据</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-9e2d973a33544d0f015f907564dde0a7336.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>集群实例</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-3ab59e91ae55dd606c705c6d589501edbcf.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>集群配置</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-99598a6318b9c85ccaaf469663322578657.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            