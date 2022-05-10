
---
title: '开源项目丨Taier 1.1 版本正式发布，新增功能一览为快'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2b8d7368e0c29c380b6fd0d03eadd632c47.png'
author: 开源中国
comments: false
date: Tue, 10 May 2022 05:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2b8d7368e0c29c380b6fd0d03eadd632c47.png'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <div> 
  <p style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#646464">2</span><span><span style="color:#646464">022 年 5 月 8 日，</span><span style="color:#00affe"><strong>Taier 1.1</strong></span><span style="color:#646464"> 版本正式发布！</span></span></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#646464"><span style="color:#646464">本次版本更新对</span> Flink 的支持升级到<strong><span style="color:#0daffe"> Flink1.12</span></strong><span style="color:#646464">，支持多种<strong><span style="color:#0daffe">流类型</span></strong>任务，新版本的使用文档已在社区中推送，大家可以随时下载查阅。</span></span></p> 
  <p style="margin-left:0; margin-right:0"><span><strong><span style="color:#646464">github 地址：</span></strong></span></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#646464">https://github.com/DTStack/Taier</span></p> 
  <p style="margin-left:0; margin-right:0"><span><strong><span style="color:#646464">gitee 地址：</span></strong></span></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#646464">https://gitee.com/dtstack_dev_0/taier</span></p> 
  <p style="margin-left:0px; margin-right:0px"><strong>一、Taier 1.1 版本介绍</strong></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#646464">Taier 是一个分布式可视化的 DAG 任务调度系统，是数栈数据中台整体架构的重要枢纽，负责调度日常庞大的任务量。</span></p> 
  <p style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#646464">它旨在降低 ETL 开发成本，提高大数据平台稳定性，让大数据开发人员可以在 Taier 直接进行业务逻辑的开发，而不用关心任务错综复杂的依赖关系与底层的大数据平台的架构实现，将工作的重心更多地聚焦在业务之中。</span></p> 
  <p style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#646464">Taier1.0 版本于 2022 年 2 月发布，在 1.0 版本发布的第二天，1.1 版本的迭代就已提上日程，并于昨日正式发布。</span></p> 
  <p style="margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#646464">本次版本更新，着重解决了 Taier 的适配性问题：对 Flink 的</span><strong><span style="color:#00affe">支持</span></strong><span style="color:#646464">升级到 1.12；Taier 中的 Spark SQL 和 Flink SQL 两个组件也实现了支持用户在任务中自定义函数，明显让 Taier 的</span><strong><span style="color:#00affe">延展性</span></strong><span style="color:#646464">有了更好的发挥；</span><strong><span style="color:#00affe">新增</span></strong><span style="color:#646464">了许多例如 Hive SQL 类型任务、实时任务运维等强大功能。</span></span></p> 
  <p style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#646464">这次版本更新对 Taier 的固有优势进行了巩固，同时也强化并改善了用户体验，进一步精细化提升产品性能。</span></p> 
  <p style="margin-left:0; margin-right:0"><strong>二、Taier 1.1 功能详解</strong></p> 
  <p style="margin-left:0; margin-right:0"><strong>01</strong><span><strong>  对 Flink 版本支持升级到 1.12</strong></span></p> 
  <p style="margin-left:0; margin-right:0"><span>Taier 作为一个分布式可视化的 DAG 任务调度系统，采用 ChunJun 作为分布式数据同步工具。1.1 版本将 Flink 版本升级到 1.12 ，支持 ChunJun 1.12 版本中新增的 transformer 算子等以及所有 Flink 原生语法及 Function</span></p> 
  <p style="margin-left:0; margin-right:0"><strong>02 </strong><span><strong>数据同步支持脚本模式、增量同步</strong></span></p> 
  <p style="margin-left:0; margin-right:0"><span>数据同步任务除向导模式外，1.1 版本新增数据同步脚本模式。脚本模式通过 json 的方式配置，无需依赖 datasourcex 的支持的数据源，直接通过 json 配置的方式提交任务，脚本模式的 json 格式无缝兼容<span style="color:#646464"> ChunJ</span><span style="color:#646464">un</span> 的数据格式，用户可以通过脚本模式调试各类数据源的数据同步。</span></p> 
  <p><img height="689" src="https://oscimg.oschina.net/oscnet/up-2b8d7368e0c29c380b6fd0d03eadd632c47.png" width="1268" referrerpolicy="no-referrer"></p> 
  <p style="margin-left:0; margin-right:0"><strong>03  </strong><span><strong>新增 Hive SQL</strong></span></p> 
  <p style="margin-left:0; margin-right:0"><span>Apache Hive 是一个构建于 Hadoop 顶层的数据仓库，可以将结构化的数据文件映射为一张数据库表，并提供简单的 SQL 查询功能，可以将 SQL 语句转换为 MapReduce 任务进行运行。Taier1.1 版本新增 Hive SQL ，支持对接 Hive 的不同版本 。</span></p> 
  <p><img height="679" src="https://oscimg.oschina.net/oscnet/up-0a599af73185e081bbf2759e0f842b12ada.png" width="1268" referrerpolicy="no-referrer"></p> 
  <p style="margin-left:0; margin-right:0"><strong>04  </strong><span><strong>新增多种实时类型任务</strong></span></p> 
  <p style="color:#646464; margin-left:0; margin-right:0; text-align:justify"><span>新增实时采集任务，支持将 MySQL、Oracle 的数据同步至 Kafka。</span></p> 
  <p><img height="683" src="https://oscimg.oschina.net/oscnet/up-f13cc3de2f491873449fa36054c4872a8a0.png" width="1269" referrerpolicy="no-referrer"></p> 
  <p style="color:#646464; margin-left:0; margin-right:0; text-align:justify"><span>新增 Flink SQL 任务，通过标准 SQL 语义的开发帮助快速完成数据任务的配置工作。</span></p> 
  <p><img height="846" src="https://oscimg.oschina.net/oscnet/up-9bb965683142f172f65a70dc8834ff5b331.png" width="1269" referrerpolicy="no-referrer"></p> 
  <p style="margin-left:0; margin-right:0"><strong>05  </strong><strong><span>新增实时任务运维</span></strong></p> 
  <p style="color:#646464; margin-left:0; margin-right:0; text-align:justify"><span>可通过实时运维中心查看实时任务的相关指标信息以及任务的详细日志信息。</span></p> 
  <p><img height="852" src="https://oscimg.oschina.net/oscnet/up-6802f808cef5002f07edb075e759b965dc0.png" width="1270" referrerpolicy="no-referrer"></p> 
  <p style="margin-left:0; margin-right:0"><strong>06  </strong><strong><span>支持用户自定义函数</span></strong></p> 
  <p style="color:#646464; margin-left:0; margin-right:0; text-align:justify"><span>用户自定义函数（User Defined Function，简称 UDF），是用户除了使用系统函数外，自行创建的函数，用于满足个性化的计算需求。自定义函数在使用上与普通的系统函数类似。</span></p> 
  <p style="color:#646464; margin-left:0; margin-right:0; text-align:justify"><span>目前 Taier1.1 版本 Spark SQL 和 Flink SQL 任务均支持自定义函数。</span></p> 
  <p style="margin-left:0; margin-right:0"><strong>07  </strong><strong><span>全新暗黑主题上线</span></strong></p> 
  <p style="color:#646464; margin-left:0; margin-right:0; text-align:justify"><span>Taier 开发界面暗黑主题上线，提供多种主题切换，用户可自行选择。Taier 1.1 可支持用户自由选择 Dark Default 主题或 Light Default 主题等等界面风格，用户体验显著提升。</span></p> 
  <p><img height="463" src="https://oscimg.oschina.net/oscnet/up-2c364d88396474361da2baf4d53ce4a3778.gif" width="1079" referrerpolicy="no-referrer"></p> 
  <p style="margin-left:0; margin-right:0"><strong>三、未来规划</strong></p> 
  <p style="color:#646464; margin-left:0; margin-right:0; text-align:justify"><span>Taier 作为一个新开源的项目，我们的迭代和更新一直在进行中，后续 Taier 将在<strong><span style="color:#00affe">扩展性、用户自主性</span></strong>方向上继续探索扩展，比如我们正在努力让用户可以基于 Taier 去自定义开发自己需要的类型任务等等。</span></p> 
  <p style="color:#646464; margin-left:0; margin-right:0; text-align:justify"><span>Taier 的每一次进步都离不开社区开发者们的帮助和建议，希望大家保持关注，和 Taier 一起继续前进，不断攀登新高峰！</span></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            