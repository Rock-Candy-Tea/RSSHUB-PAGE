
---
title: 'Pigsty 近况与 v1.4 前瞻'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bf5c38cc84a1a1e1e74994e667e41269c82.png'
author: 开源中国
comments: false
date: Wed, 02 Mar 2022 07:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bf5c38cc84a1a1e1e74994e667e41269c82.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">Pigsty v1.4 将于 3 月内发布，对监控系统进行了显著改进；探探所有PostgreSQL完整搬迁至Pigsty；Pigsty开始接洽VC</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>探探全量迁移至 Pigsty</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>探探是Pigsty最大的用户案例，也始终是第一个吃螃蟹的人。今天探探下线了最后一套遗留的旧PostgreSQL数据库 <code>pg.meta.tt</code></span><span>。至此，探探主生产环境所有数据库均已迁移至Pigsty，近一百套集群全部由Pigsty v1.3.1 所托管。所有集群全部启用了高可用自动切换，历时近两年的</span><span><strong><span>数据库飞升项目</span></strong></span><span>正式宣告完工。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><img alt height="476" src="https://oscimg.oschina.net/oscnet/up-bf5c38cc84a1a1e1e74994e667e41269c82.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"> </p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>探探主生产环境的Pigsty部署：96集群12688核的PostgreSQL OLTP集群。</span></p> 
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span style="color:#0080ff"><strong><span style="background-color:#ffffff">在探探，Pigsty经过了长时间，大规模，高强度的实际生产环境测试</span></strong></span><span style="background-color:#ffffff">。在两年的时间里不断打磨完善，最终演变为今天的样子。在近日的混沌工程演练中，运维随机挑选数据库机器进行多次宕机演练，Pigsty在无人值守的情况下可以自动进行高可用主从/流量切换。从库宕机无业务影响，主库宕机对业务写入影响不超过在1分钟。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span style="background-color:#ffffff"><img alt height="811" src="https://oscimg.oschina.net/oscnet/up-075040ff768a0398d4495f3cf7380914a80.png" width="500" referrerpolicy="no-referrer"></span></p> 
<blockquote> 
 <p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span style="background-color:#ffffff; color:#777777">一次典型从库宕机现场，读流量迅速由主库承担，业务只有极个别现场查询中断报错，而后立即恢复。</span></p> 
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span style="background-color:#ffffff; color:#777777"><img alt height="621" src="https://oscimg.oschina.net/oscnet/up-3ab285fd9a9516165478f2d2f17d2ef8cf1.png" width="500" referrerpolicy="no-referrer"></span></p> 
<blockquote> 
 <p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span style="background-color:#ffffff; color:#777777">一次典型主库宕机现场。主库宕机30s后，从库被提升新主库，影响30s业务写入请求后自愈。</span></p> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>Pigsty 与 VC</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><span style="background-color:#ffffff">Pigsty是一个开源项目，致力于PostgreSQL的推广，极大降低数据库的使用与管理门槛，显著拉高社区用户使用PostgreSQL的下</span>限<span style="background-color:#ffffff">。</span><span style="background-color:#ffffff">依托于PostgreSQL中文社区，属于用爱发电的公益开源项目。</span></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>不过，数据库作为信息系统的核心组件，很多用户在使用中反馈，希望有专业的商业服务来兜底。因此Pigsty也不排斥进行一些商业化方面的探索，</span>最近接触了一些VC机构，也与不少投资人聊过。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img alt height="576" src="https://oscimg.oschina.net/oscnet/up-6022168782852962b33568c741701cbd10a.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>Pigsty的用户痛点与产品定位</span></p> 
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span style="background-color:#ffffff">今日，Pigsty很荣幸通过了由陆奇博士主办的创业孵化器 奇绩创坛 的面试，有机会进入 2022春季创业营。如果您也对投资Pigsty感兴趣，现在确实是一个好机会哦，请联系我。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>Pigsty v1.4 新特性前瞻</span></h2> 
<p> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>最近经常听到一类用户的反馈：</span></p> 
<ol start style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Pigsty可不可以用来监控管理其他类型的数据库？</span></p> <p style="margin-left:.5rem; margin-right:0"><span style="color:#b2b2b2">例如Redis，MySQL，Greenplum？</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><span style="background-color:#ffffff">Pigsty的工作假设，DB：</span><span style="background-color:#ffffff">Node 1</span>:<span style="background-color:#ffffff">1部署是否合理？</span></span></p> <p style="margin-left:.5rem; margin-right:0"><span style="color:#b2b2b2">如何支持单机多实例的部署与监控？</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Pigsty的主机监控能不能独立使用？</span></p> <p style="margin-left:.5rem; margin-right:0"><span style="background-color:#ffffff; color:#b2b2b2">我不想用数据库，只想用主机节点监控怎么弄？</span></p> </li> 
</ol> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>应。Pigsty 将于3月内发布<span style="background-color:#ffffff">v1.4 ，对这些用户关心的问题做出回应</span>，带来一系列体验改进与新功能特性，包括：</span></p> 
<ol style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>独立的主机节点监控部署功能</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>改进的PostgreSQL数据库监控</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>对Greenplum/MatrixDB部署与监控的初步支持</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>改进的监控数据模型，支持单机多实例。</span></p> </li> 
</ol> 
<p><img alt height="376" src="https://oscimg.oschina.net/oscnet/up-935de446564dbd0b093b4abd56f011d5bc1.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote>
 <span>Pigsty v1.4 Home 主页</span>
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>节点监控</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty v1.4 引入了一个全新的功能：节点监控。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>这并不是说以前Pigsty没有关于机器节点的监控指标，而是在以前，机器的监控指标是1:1与PostgreSQL实例绑定的。对于一个PostgreSQL数据库发行版来说，这样的设计是没有问题的。但随着Pigsty的发展，这样的设计就开始显得不合时宜了。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>用户可能有各种各样的使用方式与部署策略，例如，在一个节点上部署多个数据库实例，甚至部署多种不同类型的数据库。在这种情况下，合适的做法是把节点的管理与监控单独抽离出来，不与具体的数据库类型绑定。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>这样做有两个显著的好处：一是如果用户不需要数据库监控与管理，只需要节点的监控与管理，那么会比以前简单很多；第二是一个节点上可以部署多个甚至多种数据库，并复用同样的节点监控指标数据。</span></p> 
<p> <img alt height="553" src="https://oscimg.oschina.net/oscnet/up-da6ed723b26033f4b1c37a3996b356b7f4e.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote>
 <span>Node Overview 面板，关注所有节点的指标。</span>
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">虽然Pigsty的定位是开箱即用的PostgreSQL发行版，但其中也包含着主机监控的最佳实践。有些用户根本不care数据库，只是拿Pigsty做主机监控…。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff"><img alt height="739" src="https://oscimg.oschina.net/oscnet/up-ad58b9deed8fde89f7cb9c6a06a7f24c97b.png" width="500" referrerpolicy="no-referrer"></span></p> 
<blockquote>
 <span>新增的Nodes Cluster 面板，关注一组节点的聚合指标与集群内的水平对比</span>
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff"><span style="background-color:#ffffff">节点监控提供了全局概览，集群，以及单个节点三种不同的层次。节点的集群可以独立配置，也可以配置为默认与PostgreSQL数据库集群保持一致。</span></span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>多数据库支持</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>节点监控与置备的剥离，为第二件事打下了基础，那就是多数据库支持。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><img alt height="298" src="https://oscimg.oschina.net/oscnet/up-4b391f0cbef87731983c7374a0956469df3.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#333333">PostgreSQL是一个相当全能、相当完美的数据库内核了，但正所谓：红花还需绿叶配，一个好汉三个帮。当组织与数据成长到一定规模后，使用专有数据组件的需求也会随之出现。最典型的两类是：以Redis为代表的缓存，以及以Greenplum为代表的数据仓库。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#333333"><img alt height="333" src="https://oscimg.oschina.net/oscnet/up-b4ba9698accdcc7adbd6a4bd7c250c19033.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Redis可以进一步强化业务系统的OLTP处理能力，分担数据库压力，模型简单易用，受到广受开发者的喜爱。而Greenplum则可以显著强化业务系统的OLAP能力，采用与PostgreSQL一致的语言、驱动与接口，将数据分析的量级从几十TB提升到PB乃至ZB的级别。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Redis与Greenplum在两个方向上扩展了PostgreSQL的能力边界，这两者都是PostgreSQL的拍档，经常在一起组合使用。因此，Pigsty在v1.4中提供了对Redis与Greenplum的初步支持。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><img alt height="681" src="https://oscimg.oschina.net/oscnet/up-559f97aad4b11cbc569f7154ec2c074b4d4.png" width="500" referrerpolicy="no-referrer"></span></p> 
<blockquote> 
 <p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span style="background-color:#ffffff; color:#777777">Redis Overview 监控面板</span></p> 
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span style="background-color:#ffffff; color:#777777"><img alt height="606" src="https://oscimg.oschina.net/oscnet/up-a7e9358174cd2151b75fc7bf4c604141e0d.png" width="500" referrerpolicy="no-referrer"></span></p> 
<blockquote>
 <span>复用 Postgers 剧本，声明一个MatrixDB集群</span>
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>PG监控例行改进</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty v1.4 提供了对新数据库种类的监控支持，但对于经典的PostgreSQL监控也没有落下。在1.4中，大量PGSQL的监控面板进行了调整与重置，最具有代表性的就是PGSQL Cluster面板。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><img alt height="324" src="https://oscimg.oschina.net/oscnet/up-a683c71b2f224d1998a7ae891bdea42a0b3.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"> </p> 
<blockquote>
 <span>全新的 PGSQL Cluster 监控面板</span>
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>PGSQL Cluster是Pigsty数据库监控中最核心的监控面板之一，承上启下，用于呈现一个自治数据库集群的关键状态。新的设计隐藏了不必要的信息，聚焦于集群资源。您可以从首屏快速点击集群内的资源对象，前往细分的监控面板：包括节点，实例，负载均衡器，服务，数据库，服务组件。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>除了集群资源对象，PGSQL Cluster的首屏只呈现最关键的监控指标，报警事件，集群/实例压力水位。其他细节都隐藏在下面的专题栏中。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><img alt height="417" src="https://oscimg.oschina.net/oscnet/up-1d0e5197afd67d9114efef0383c633e9e54.png" width="500" referrerpolicy="no-referrer"></span></p> 
<blockquote>
 <span>成员详情表在默认隐藏的第二栏中</span>
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>第二个显著改进是 PGSQL Database 面板。在过去，这个监控面板的存在感与使用频率并不高。因此在v1.4中，PGSQL Database进行了彻底的改版。从笼统地介绍一个数据库实例的库级指标，变为关注整个数据库集群内部对象的详情。例如，您可以查阅一张表或一类查询在集群主库与从库实例上的QPS，或者确认某一个索引在集群不同实例上的使用情况，从而对业务与应用进行有针对性的优化。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>其他一些新的主题监控面板也在制作打磨完善中。例如，关注集群维护任务的PGSQL Maintenance面板，可以观察备份、创建索引、垃圾回收任务的实时进度。PGSQL Shard面板，则关注多个水平分片的业务集群之间的横向比较。这些Dashboard都将在生产环境中不断打磨优化，臻至成熟后进入到Pigsty中。</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>使用方式与接口</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty v1.4 提供了一系列新的 Playbook / 剧本。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">在 v1.4 中，Pigsty的使用方式变得更加直观了。如果您将Pigsty用作单机数据库或监控核心，只需要执行 <span style="color:#0080ff">meta.yml</span> 即可。如果你希望部署额外的数据库集群，使用 <span style="color:#0080ff">node.yml</span> 将这些节点先纳入管理，而后选择对应数据库的剧本（<span style="color:#0080ff"> pgsql.yml </span>, <span style="color:#0080ff">redis.yml</span>, <span style="color:#0080ff">gpsql.yml </span>）执行即可。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#0080ff">meta.yml</span><span> 用于替代以前的 </span><span style="color:#0080ff">infra.yml</span><span> ，负责在单台节点上完整安装一套Pigsty系统。包括一套完整就绪的的PostgreSQL数据库。同时，新增的 </span><span style="color:#0080ff">meta-remove.yml </span><span>剧本用于Pigsty的卸载。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#0080ff">node.yml</span><span> 从 </span><span style="color:#0080ff">pgsql.yml</span><span> 中剥离，用于将新的节点纳入Pigsty管理。执行此剧本，会自动将目标节点置备为指定的状态，并安装DCS（Consul Agent）与节点监控。如果你希望使用 Pigsty 在部署数据库集群，则应当使用此剧本将目标节点先纳入 Pigsty 管理。同时，新增的 </span><span style="color:#0080ff">node-remove.yml</span><span> 剧本用于将节点从Pigsty中移除。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#0080ff">pgsql.yml</span><span> 现在移除了节点初始化的部分，只负责在已经初始化好的节点上部署PostgreSQL集群与实例，并将其纳入监控。一些新的开关选项被添加至相关的Ansible Roles中，但主体配置仍与先前保持兼容。</span><span style="color:#0080ff">pgsql-remove.yml</span><span> 剧本亦进行了相应调整，移除DCS服务现在由 </span><span style="color:#0080ff">node-remove.yml</span><span> 负责。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#0080ff">redis.yml</span><span> 也移除了节点初始化的部分，您需要在已经初始化好的节点上执行此剧本以部署Redis服务。新增的</span><span style="color:#0080ff"> redis-remove.yml</span><span> 剧本用于从目标节点上移除Redis服务。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#0080ff">gpsql.yml</span><span> 是新增的，用于部署MatrixDB的剧本（实际上是Greenplum 7的超集），目前仍然处于Beta阶段，可以对MatrixDB/Greenplum提供基本的部署与安装支持。</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>未来的路线图</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>从长期来看，我希望在 Pigsty 中再添加 Minio，Kafka 支持，让整个产品形成一个以PostgreSQL为核心的整体解决方案，覆盖中小型企业完整生命周期的数据存储需求，打造一个开源的、私有的云数据库管控整体解决方案。关系型数据库PostgreSQL作为核心，缓存Redis强化TP能力，数仓Greenplum/MatrixDB强化大规模数据分析能力，对象存储Minio用于备份管理以及存储图像音视频等数据，消息队列Kafka提供数据总线的能力。通过完备的ETL/CDC支持将这些数据组件融为一体，实现turning the database inside-out！</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">从中期来看，Pigsty将尽可能充分利用元节点上的CMDB。CMDB模式应当尽快适配多模数据库，命令行工具也应当及时更新，提供类似于云CLI工具的使用体验。多云部署与云厂商适配也应当尽快弄起来。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>从短期来看，Pigsty的监控面板还有大量的改善空间，包括Catalog数据挖掘与呈现，日志分析与提炼。从可观测性的角度讲，Blackbox黑盒探测与Mtail日志衍生指标还有很大挖掘空间。此外，针对Greenplum的定制Dashboard也将提上日程。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">当然，这些都需要大量的人力脑力投入。作者表示，一个人用爱发电速度毕竟有限，特别是最近在热恋中，对Pigsty的爱被分走了很多。所以，也非常欢迎大家一起来Contrib，一起打造一款属于我们自己的 “RDS” 。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff; color:#333333">详情可</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FO2VBjnRXL5LAH4oMvGZS2g" target="_blank">查看发布公告</a><span style="background-color:#ffffff; color:#333333">。 </span></p>
                                        </div>
                                      
</div>
            