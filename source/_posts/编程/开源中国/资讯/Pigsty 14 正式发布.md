
---
title: 'Pigsty 1.4 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fbdd4f0b944d8cb8c2d10b68bee3565aab1.png'
author: 开源中国
comments: false
date: Thu, 31 Mar 2022 23:46:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fbdd4f0b944d8cb8c2d10b68bee3565aab1.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#222222">Pigsty v1.4 现已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FdKVDLcnGtaWjdARo9rZncQ" target="_blank">发布</a>。全新的模块化架构：四大内置模块 INFRA，NODES，PGSQL，REDIS 可以独立使用并自由组合；新增时序数据仓库 MatrixDB 部署与监控支持；新建设了全球 CDN 加速下载；此外，Pigsty 完成种子轮融资，产品定位与战略进行重大升级，作者表示其也将全职出来投入到此项目中。</span></p> 
<p><img height="372" src="https://oscimg.oschina.net/oscnet/up-fbdd4f0b944d8cb8c2d10b68bee3565aab1.png" width="500" referrerpolicy="no-referrer"></p> 
<h2><span>模块化架构</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>公告指出，Pigsty v1.4 中最给力的特性是对底层架构的重大重构，尽管听上去比较枯燥，但这一点确实很重要。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>在 1.4 中，整个系统解耦成 4 个独立的模块，可以独立维护，自由排列组合使用。</span><strong><span style="color:#ac39ff"><code>INFRA</code></span></strong><span>是Pigsty的基础设施部分，包括监控/告警/可视化/日志/DNS/NTP等公共组件。</span><strong><span style="color:#ffa900"><code>NODES</code></span></strong><span>是主机节点管理模块，</span><span style="color:#007aaa"><strong><code>PGSQL</code></strong></span><span>是PostgreSQL数据库部署管控模块，</span><span style="color:#ff4c00"><strong><code>REDIS</code></strong></span><span>是Redis数据库部署管控模块。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="428" src="https://oscimg.oschina.net/oscnet/up-80da209637d3cd65c3c4bfadcc3a464384f.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><em><span style="color:#000000"><span style="background-color:#ffffff">全新的 Pigsty v1.4 监控首页</span></span></em></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>如果你想将Pigsty当作单机的开箱即用的PostgreSQL发行版来使用，那么在一台机器上依次安装 </span><span style="color:#ac39ff"><strong>INFRA</strong></span><span>, </span><span style="color:#ffa900"><strong>NODES</strong></span><span>, </span><span style="color:#3daad6"><strong>PGSQL</strong></span><span> 三个模块，就会有一个立即可用的，自我监控管理的数据库实例。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>如果你想要一个生产环境的大规模主机监控系统，那么在一台机器上安装</span><span style="color:#ac39ff"><strong>INFRA</strong></span><span>模块，在所有被监控的机器节点上安装</span><span style="color:#ffa900"><strong>NODES</strong></span><span>模块即可。所有的主机节点会配置有软件源，软件包，DNS，NTP，节点监控，日志收集，DCS Agent这些生产环境所需的组件。纳入Pigsty管理的主机会带有详细的监控信息，并可以用于进一步部署各式各样的数据库模块。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>如果你想部署管理大量的PostgreSQL集群，很简单，在这些纳入Pigsty管理的节点上再加装 </span><span style="color:#3daad6"><strong>PGSQL</strong></span><span>模块即可。您可以一键部署各种各样的PGSQL集群：单实例，一主N从的高可用集群，同步集群，法定人数提交的同步集群，带有离线ETL角色的集群，异地容灾的备集群，延迟复制集群，Citus分布式集群，TimescaleDB集群，MatrixDB数据仓库集群。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>如果你想部署并监控管理很多Redis集群，也很简单。只要在Pigsty托管的节点上加装</span><span style="color:#ff4c00"><strong>REDIS</strong></span><span>模块即可。而且后续添加新类型的数据库也更加容易了：</span><span style="color:#3da742"><strong>KAFKA</strong></span><span>, </span><span style="color:#3da742"><strong>MINIO</strong></span><span>, </span><span style="color:#3da742"><strong>MYSQL</strong></span><span>，…… 这些模块都可以用一种类似的方式加入到Pigsty中。一个成功的开源项目离不开开发者的贡献，而简洁优雅的架构，可以极大降低贡献的门槛。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty 1.4 在模块化上进行了大量的工作。无论是配置项，命名空间，剧本，标签，监控面板，全部按照这四个模块进行分类统筹。例如，下面是按照模块划分的剧本与配置项：</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="432" src="https://oscimg.oschina.net/oscnet/up-8f2aafc38fbbdf31f1d850442120c2e97f8.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0px; margin-right:0px"><em><span style="color:#000000"><span style="background-color:#ffffff">模块化后的剧本与配置参数</span></span></em></p> 
<h2><span>全新数据库支持</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>PostgreSQL是一个相当全能、相当完美的数据库内核了，但正所谓：红花还需绿叶配，一个好汉三个帮。当组织与数据成长到一定规模后，使用专有数据组件的需求也会随之出现。最典型的两类是：以Redis为代表的缓存，以及以Greenplum为代表的数据仓库。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="325" src="https://oscimg.oschina.net/oscnet/up-b0f0c233cc571e31024bffb5f244d0ba986.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#222222">Redis可以进一步强化业务系统的OLTP处理能力，分担数据库压力，模型简单易用，受到广受开发者的喜爱。而Greenplum则可以显著强化业务系统的OLAP能力，采用与PostgreSQL一致的语言、驱动与接口，将数据分析的量级从几十TB提升到PB乃至ZB的级别。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="302" src="https://oscimg.oschina.net/oscnet/up-c23ead286c856572c65a166341b9f360e68.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#222222">Redis与Greenplum在两个方向上扩展了PostgreSQL的能力边界，这两者都是PostgreSQL的拍档，经常在一起组合使用。因此，Pigsty在v1.4中提供了对Redis与Greenplum的初步支持。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="402" src="https://oscimg.oschina.net/oscnet/up-65225ae21773b0d3adc9d625f54e78e39f6.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><em>Redis Overview 面版</em></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>不过，Pigsty支持的并不是原生的Greenplum，而是它的一个分支：MatrixDB。Greenplum的正式版本目前仍然是6.x，基于PostgreSQL 9.6内核，有些太老了。而MatrixDB则基于Greenplum 7和PostgreSQL 12内核，还有额外的时序功能支持。因此Pigsty目前使用MatrixDB作为Greenplum的替代实现。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty v1.4 最得意的一点在于，并没有一个专门的 <strong>MATRIXDB</strong> 模块，MatrixDB的部署完全复用了 <strong>PGSQL</strong> 模块。您可以用熟悉的配置参数来配置 MatrixDB。在 Pigsty 看来，一套MatrixDB数据仓库在逻辑上就是N对标准的一主一从PGSQL集群：一个标准的Master集群（Master & Standby），以及很多组散布在多个节点上的Segment集群（Primary & Mirror）。所有PGSQL的面板都可以直接用在MatrixDB上。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="686" src="https://oscimg.oschina.net/oscnet/up-a9ad8fb4e6617ba216d97a8e14ab2d502a9.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><em><span style="background-color:#ffffff">PGSQL MatrixDB 面版</span></em></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>专用的Dashboard：PGSQL Matrix用于展示一套MatrixDB的核心监控指标，其他监控面板均复用已有的PGSQL面板。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="569" src="https://oscimg.oschina.net/oscnet/up-897d318239c5000913372136b6ea2c9ecbb.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#000000"><em><span style="background-color:#ffffff">定义上面的4节点MatrixDB只需要这些配置</span></em></span></p> 
<h2><span>监控系统演进</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>监控系统一直以来在Pigsty中扮演着核心角色。在1.4中，Pigsty的监控系统也有着很显著的改进。</span></p> 
<h3><span>主机监控</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty v1.4 引入了一个全新的功能：节点监控，这也是模块化改造的一个直接成果。</span>这并不是说以前Pigsty没有关于机器节点的监控指标，而是在以前，机器的监控指标是1:1与PostgreSQL实例绑定的。对于一个PostgreSQL数据库发行版来说，这样的设计是没有问题的。但随着Pigsty的发展，这样的设计就开始显得不合时宜了。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="288" src="https://oscimg.oschina.net/oscnet/up-0e6cecb5c668f76093320bde5627504dd60.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><em><span style="color:#000000"><span style="background-color:#ffffff">NODES Overview面板，提供所有节点的导航</span></span></em></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff">用户可能有各种各样的使用方式与部署策略，例如，在一个节点上部署多个数据库实例，甚至部署多种不同类型的数据库。在这种情况下，合适的做法是把节点的管理与监控单独抽离出来，不与具体的数据库类型绑定。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>这样做有两个显著的好处：一是如果用户不需要数据库监控与管理，只需要节点的监控与管理，那么会比以前简单很多；第二是一个节点上可以部署多个甚至多种数据库，并复用同样的节点监控指标数据。任何时候，你只要点击IP地址，就可以跳转到具体的NODES Instance，查看该节点的详情。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="532" src="https://oscimg.oschina.net/oscnet/up-18b6fddf4e3a23332975e133e8954a87f63.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>曾经的PGSQL Node 现在变为 NODES Instance</span></p> 
</blockquote> 
<p><span><span style="background-color:#ffffff">节点监控提供了全局概览，集群，以及单个节点三种不同的层次。节点的<strong>集群</strong>可以配置为默认与PostgreSQL数据库集群保持一致，也可以有独立的身份配置。方便您从不同的角度来透视集群资源。</span></span></p> 
<p><img height="738" src="https://oscimg.oschina.net/oscnet/up-2df82e035349b890f4376861128e7d1c689.png" width="500" referrerpolicy="no-referrer"> </p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>新增的Nodes Cluster 面板，关注一组节点的聚合指标与集群内的水平对比</span></p> 
</blockquote> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>虽然Pigsty的定位是开箱即用的PostgreSQL发行版，但其中也包含着主机监控的最佳实践。有些用户根本不care数据库，只是拿Pigsty做主机监控…。</span></p> 
<h3><span>日志收集</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>在Pigsty 1.4中，Loki与Promtail日志收集组件升级为整个系统的默认组件。Loki是Grafana出品的日志收集方案，采用与Prometheus类似的标签体系，与PromQL类似的LogQL。是一个轻量化，优雅简洁的日志收集、处理、分析解决方案。经过了一年时间的测试与打磨，现在Loki已经成为了Pigsty的默认组成部分。会实时收集各式各样的日志：节点的syslog, dmesg, cron日志，数据库postgres/pgbouncer/patroni的日志，以及Redis日志。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="317" src="https://oscimg.oschina.net/oscnet/up-2d1fe103f82ef38d406c83e0cf051349adf.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>INFRA板块的 LOGS Instance监控面板，可以实时浏览搜索所有日志。</span></p> 
</blockquote> 
<p><span style="background-color:#ffffff; color:#222222">ELK对于SRE的日志需求过重，其实大家想要的就是一个高效快速的大规模并行GREP，Loki在这件事上干的很出色。</span></p> 
<p><span style="background-color:#ffffff; color:#222222">此外，除了节点日志，你也可以从新的INFRA Overview面板，查阅基础设施产生的实时日志数据。</span> </p> 
<p><img height="542" src="https://oscimg.oschina.net/oscnet/up-9091c81ea8ae523cdc5f54ecde118214294.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>INFRA板块的Overview面板，可以看到基础设施的各项日志</span></p> 
</blockquote> 
<h3><span>PGSQL监控</span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty v1.4 提供了对新数据库种类的监控支持，但对于经典的PostgreSQL监控也没有落下。在1.4中，大量PGSQL的监控面板进行了调整与重置，最具有代表性的就是PGSQL Cluster面板。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="390" src="https://oscimg.oschina.net/oscnet/up-216461417c9d65ada6cad2e4e9f1a00c9c3.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>全新的 PGSQL Cluster 监控面板首屏</span></p> 
</blockquote> 
<p><span>PGSQL Cluster是Pigsty数据库监控中最核心的监控面板之一，承上启下，用于呈现一个自治数据库集群的关键状态。新的设计隐藏了不必要的信息，聚焦于集群资源。您可以从首屏快速点击集群内的资源对象，前往细分的监控面板：包括节点，实例，负载均衡器，服务，数据库，服务组件。</span></p> 
<p><span style="background-color:#ffffff; color:#222222">除了集群资源对象，PGSQL Cluster的首屏只呈现最关键的监控指标，报警事件，集群/实例压力水位。其他细节都隐藏在下面的专题栏中。</span></p> 
<p><img height="465" src="https://oscimg.oschina.net/oscnet/up-a04cb6d6934b1a2e9f75db7664b998b6fde.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>成员详情表在默认隐藏的第二栏中</span></p> 
</blockquote> 
<p><span>第二个显著改进是新增的 PGSQL Databases 面板。在过去，数据库内监控只关注单个实例内的单个对象。但对于表、索引这样的业务对象，我们更关注的是它们在整个集群内的整体指标。PGSQL Databases面板为此而生。您可以查询某一个数据库在整个集群内的表现，水平对比集群间不同实例的差异：</span></p> 
<p><img height="754" src="https://oscimg.oschina.net/oscnet/up-cc35fd79d5fa8664225004a8318ffe7d98e.png" width="500" referrerpolicy="no-referrer"> </p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>PGSQL Databases面板：agg(metrics&#123;datname=*&#125;) by (ins)</span></p> 
</blockquote> 
<p><span>更重要的是，你可以看到每一张表，每一类查询在集群范围内的汇总视图。例如，你可以查阅一张表或一类查询在集群主库与从库实例上的QPS，或者确认某一个索引在集群不同实例上的使用情况，从而对业务与应用进行有针对性的优化。</span> </p> 
<p><img height="526" src="https://oscimg.oschina.net/oscnet/up-a200d33decacc19c39cf8a4ea03339d93a4.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>库内对象在集群层面的汇总展示：Tables & Queries，点击下钻。</span></p> 
</blockquote> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>带颜色的TreeMap可以快速反映出两个维度的属性：对于表而言，大小代表表占用的空间，颜色代表表被访问的频次。对于查询而言，大小代表在此查询上耗费的总时长，颜色代表该类查询的平均响应时间。</span></p> 
<h3><span>应用面版</span></h3> 
<p><span>除了<strong>INFRA</strong>，<strong>NODES</strong>，<strong>PGSQL</strong>，<strong>REDIS</strong>四个核心模块外，Pigsty Grafana的首页还有一个板块：<strong>APP</strong>。这是留给用户自己的应用的。任何带有</span><strong><span><code>APP</code></span></strong><span>和</span><strong><span><code>Overview</code></span></strong><span>标签的监控面版会被列入Pigsty的面版导航中。Pigsty自带了一个开箱即用的小应用 PGLOG，用来分析PG自身的CSV日志，您可以快速从日志中定位异常，并快速定位跳转到具体连接的详情页。</span></p> 
<p><img height="276" src="https://oscimg.oschina.net/oscnet/up-f8625f83c1d0a5a78d12049ee2f58083ae3.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>PGLOG Overview，使用</span><span>快捷方式快速将日志灌入应用表中分析。</span></p> 
</blockquote> 
<p><span>此外，Pigsty还建立一个专用的代码仓库：Vonng/pigsty-app ，用于盛放Pigsty样例应用：</span><strong><span>https://github.com/Vonng/pigsty-app</span></strong><span> 。目前的应用包括：</span> </p> 
<ul> 
 <li><span>ISD：NOAA全球地表气象站历史天气数据查询</span></li> 
 <li><span>COVID：WHO新冠疫情数据查询</span></li> 
 <li><span>DBENG：DB-Engine 数据库流行度趋势与预测</span></li> 
 <li><span>APPLOG：Apple应用隐私日志可视化</span></li> 
 <li><span>WORKTIME：国内大公司上下班时间查询</span></li> 
</ul> 
<p><span>后续将不断添加更多数据应用的样例。</span></p> 
<p><img height="266" src="https://oscimg.oschina.net/oscnet/up-fbd59c9b0a8eb7144b5e079961b6d7f3e3b.png" width="500" referrerpolicy="no-referrer"> </p> 
<p><span style="background-color:#ffffff; color:#777777">DBEng Trend: 使用权威网站DBEngine流行度趋势数据，预测PostgreSQL什么时候会成为世界上最流行的关系型数据库。</span></p> 
<p> </p> 
<h2><span>安装体验优化/CDN</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>此前Pigsty使用Github作为发布平台，中国大陆访问起来还是比较吃力的。经常需要从百度网盘镜像下载，再手工拷贝到服务器上去。用户的体验就是我们的追求，所以我们又启用了全球CDN加速域名 </span><span style="color:#3daad6"><strong><span><code>http://download.pigsty.cc</code></span></strong></span><span> ，朗朗上口，非常好记。例如最新的软件源码包与离线软件包的下载地址分别为：</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"> </p> 
<ul> 
 <li><span style="color:#007aaa"><strong><span>http://download.pigsty.cc/v1.4.0/pigsty.tgz</span></strong></span><span> （2MB）</span></li> 
 <li><span style="color:#007aaa"><strong><span>http://download.pigsty.cc/v1.4.0/pkg.tgz</span></strong></span><span>（940MB）</span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty的软件包进行了一次重新梳理与瘦身，从原本的1.3GB压缩至v1.4的940MB。需要安装Greenplum与MatrixDB的用户，单独下载另一个离线软件包 matrix.tgz （338MB）即可。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>一键安装是Pigsty的光荣传统。尽管如此，<strong>下载</strong>一直以来都是最最不让人省心的地方。因此在Pigsty v1.4中提供了专用的下载脚本 </span><strong><span><code>download</code></span></strong><span>，可用于自动下载并解压可选的软件包 </span><span style="color:#3daad6"><strong>pkg.tgz, matrix.tgz, app.tgz</strong></span><span>。这个脚本会自动检测您的网络环境是不是在墙内，如果在墙外使用默认的Github Releaes，在墙内则使用腾讯云CDN下载。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>当然，</span><strong><span><code>download </code></span></strong><span>本身也是 pigsty源码包的一部分，因此官方还提供了一条类似<strong>homebrew </strong>的一键安装命令，用来一键下载最新的 pigsty 源码包。于是，现在安装Pigsty的流程如下所示了：</span></p> 
<pre><span style="color:#0073bf">bash </span>-c <strong>"</strong><strong>$</strong><span style="color:#0073bf">(curl </span>-fsSL http://download.pigsty.cc/get)<strong>" </strong><em># </em><em>下载
</em><span style="color:#0073bf">./download </span>pkg matrix app   <em># </em><em>下载并解压可选的扩展软件包（可选步骤）
</em><span style="color:#0073bf">cd </span>~/pigsty <strong>&& </strong><span style="color:#0073bf">./configure  </span><em># </em><em>配置
</em><span style="color:#0073bf">make </span>install                <em># </em><em>安装</em>
</pre> 
<h2><span>典型用户案例</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>探探是Pigsty最大的用户案例，也始终是第一个吃螃蟹的人。2022年3月份，探探下线了最后一套遗留的旧PostgreSQL数据库 <code>pg.meta.tt</code></span><span>，生产环境所有数据库均已迁移至Pigsty，一百套集群全部由Pigsty v1.3.1所托管（监控系统版本为1.4）。所有集群的高可用自动切换也已经启用，历时近两年的</span><span><strong><span>数据库飞升项目</span></strong></span><span>正式宣告完工。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="324" src="https://oscimg.oschina.net/oscnet/up-4473af4f054dbb8faaad88e2eda6060ac86.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>探<span style="background-color:#ffffff; color:#777777">探主生产环境的Pigsty部署：240实例13400核的PostgreSQL OLTP集群。</span></span></p> 
</blockquote> 
<p><span style="color:#0080ff"><strong><span style="background-color:#ffffff">在探探，Pigsty经过了长时间，大规模，高强度，惨无人道的实际生产环境测试</span></strong></span><span style="background-color:#ffffff">。在两年的时间里不断打磨完善，最终演变为今天的样子。在近日的混沌工程演练中，运维随机挑选数据库机器进行多次宕机演练，Pigsty在无人值守的情况下可以自动进行高可用主从/流量切换。从库宕机无业务影响，主库宕机对业务写入影响不超过在1分钟。</span></p> 
<p><img height="804" src="https://oscimg.oschina.net/oscnet/up-40f4110943cca158f003a27b726a60773b6.png" width="500" referrerpolicy="no-referrer"> </p> 
<blockquote> 
 <p><span style="background-color:#ffffff; color:#777777">一次典型从库宕机现场，读流量迅速由主库承担，业务只有极个别现场查询中断报错，而后立即恢复。</span></p> 
</blockquote> 
<p><img height="630" src="https://oscimg.oschina.net/oscnet/up-42c718aa8ef469d81a8d2141c5d9c8d2bfe.png" width="500" referrerpolicy="no-referrer"> </p> 
<blockquote> 
 <p><span style="background-color:#ffffff; color:#777777">一次典型主库宕机现场。主库宕机30s后，从库被提升新主库，影响30s业务写入请求后自愈。</span></p> 
</blockquote> 
<h2><span>潜在合作伙伴</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>公告指出，一个篱笆三个桩，一个好汉三个帮。想要做大事，首先要确定的一点就是，谁是我们的敌人，谁是我们的朋友。Pigsty定位了两个潜在的合作伙伴Sealos，Bytebase，准备进行进一步接触。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Sealos是一个很有趣的开源项目，可以把整个运行中的K8s集群打成镜像，然后一键部署到其他地方，Pigsty和Sealos很互补：很多SaaS都是DB + App的方式。有了一个开箱即用的数据库，就差一个开箱即用的应用生态了，把SaaS软件丢进K8s里整体打成镜像，交付什么Gitlab，Jira，Confluence，Odoo，Habour，金蝶啥的就很简单了，拉起来填个数据库连接串全部搞定。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>另一个比较关注的项目是<strong>ByteBase</strong>，这是一个做数据库Schema Migration的工具。用Go开发清清爽爽无依赖，使用PostgreSQL作为后端数据库，又可以用来做PostgreSQL的模式变更管理。那确实是极好的，Pigsty可以用来做<strong>ByteBase</strong>的Backend Database，<strong>ByteBase</strong>也可以作为Pigsty的Migrator，预计在下个版本中会添加一个对ByteBase基本的集成与支持。</span></p> 
<h2><span>产品定位转换</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>Pigsty，是Postgres in Graph STYle的缩写，即图形化PostgreSQL的意思，在最初，它是一个针对PostgreSQL开发的专业监控系统。后来，随着各种各样功能的引入（声明式定义，一键部署，高可用PG，自动流量切换，数据分析与可视化组件），Pigsty在1.0的时候，定位调整为“<strong><span>开箱即用的PostgreSQL数据库发行版</span></strong></span><span>”。而现在，Pigsty v1.3提供了Redis部署监控的支持，1.4又引入了时序数据仓库MatrixDB监控部署支持。单一的 </span><span><strong><span>PG发行版</span></strong></span><span> 定位已经限制了Pigsty的想象力与可能性。</span></p> 
<h4><span>开箱即用的发行版</span></h4> 
<h4><span style="color:#b2b2b2">RedHat for Linux</span></h4> 
<ul> 
 <li><span>Pigsty打包最新PostgreSQL内核（14），集成强力的地理空间插件PostGIS3.2，时序数据库插件TimescaleDB2.6，分布式扩展插件Citus10，以及上百功能扩展，全部一键安装，开箱即用。</span></li> 
 <li><span>Pigsty集成了完整的大规模数据库监控管控解决方案：Grafana，Prometheus，Loki，Ansible，CMDB。亦可作为生产级应用运行时直接使用，监控管理其他数据库与应用。</span></li> 
 <li><span>Pigsty集成了数据分析生态的常用工具：Jupyter，Echarts，Grafana，PostgREST，Postgres。可以低代码的方式，开发交互性数据应用与数据可视化作品。快速产出作品原型，并以标准的方式分享，演示与交付。</span></li> 
</ul> 
<h4><span>多快好省的开发者工具：</span></h4> 
<h4><span style="color:#b2b2b2">HashiCorp for Database!</span></h4> 
<ul> 
 <li><span>Pigsty采用Infra as Data的设计理念，用户描述自己想要什么样的数据库集群，而Pigsty自动为您创建！Just like Kubernetes!</span></li> 
 <li><span>Pigsty提供灵活丰富的部署支持，本地沙箱，云端，多云部署。无论是高规格物理机还是1核1G虚机均可运行，保持生产、预发、开发、测试环境高度一致。</span></li> 
 <li><span>Pigsty可以极大简化数据库部署实施维护工作，极大降低PostgreSQL数据库运维与使用的门槛，量产DBA，有效降低软硬件人力成本。使用云厂商服务器的牛，耕云数据库的田，也能减少50%以上的TCO，自建机房更是能节省80%的成本费用。</span></li> 
</ul> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>Pigsty为DBA留下了两个安全出口：PITR备份与等保安全加固。</span></p> 
</blockquote> 
<h4><span>自动驾驶SRE解决方案：</span></h4> 
<h4><span style="color:#b2b2b2">Alternative for RDS!</span></h4> 
<ul> 
 <li><span>终极可观测性：监控是有效管理的基石。没有完善的监控，SRE无从谈起。Pigsty带有终极的可观测性，以BI的思路设计监控系统，从最顶层的全局洞察到最细节的每一个对象，都可以获取实时洞察，为决策提供数据支撑，做到“心中有数”。</span></li> 
 <li><span>高可用数据库集群：Pigsty集成了久经考验的生产级高可用数据库架构方案：主从异地容灾，硬件故障自愈，高可用自动切换，自带连接池与负载均衡器，提供分布式数据库般的体验。冷备份与延时从库可有效应对各类软件故障与人为故障，确保系统稳定运行。极大简化运维工作。</span></li> 
 <li><span>Pigsty还可以作为完整的SRE解决方案：主机监控，应用部署，并将逐步添加其他数据库的部署与监控：Redis/Greenplum/Kafka/Minio，或支持其他SaaS服务，制作POC，交付Demo等。</span></li> 
</ul> 
<h2><span>未来路线规划</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>作者表示，从长期来看，他希望在 Pigsty 中再添加 Minio，Kafka 支持，让整个产品形成一个以PostgreSQL为核心的整体解决方案，覆盖中小型企业完整生命周期的数据存储需求，打造一个开源的、私有的云数据库管控整体解决方案。关系型数据库PostgreSQL作为核心，缓存Redis强化TP能力，数仓Greenplum/MatrixDB强化大规模数据分析能力，对象存储Minio用于备份管理以及存储图像音视频等数据，消息队列Kafka提供数据总线的能力。通过完备的ETL/CDC支持将这些数据组件融为一体，实现turning the database inside-out！</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span>从短期来看，Pigsty将尽可能充分利用元节点上的CMDB。CMDB模式应当尽快适配多模数据库，命令行工具也应当及时更新，提供类似于云CLI工具的使用体验。多云部署与云厂商适配也应当尽快弄起来。监控面板也有大量的改善空间，包括Catalog数据挖掘与呈现，日志分析与提炼。从可观测性的角度讲，Blackbox黑盒探测与Mtail/Promtail日志衍生指标还有不小的创新空间。数据库模式演化，可以考虑使用开源的解决方案Bytebase。PostgREST的能力也有待进一步发掘。冷备份/PITR是Pigsty留给DBA们的一个安全出口，但也应当准备一个Best Pracetice指南。</span></p> 
<p>详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FdKVDLcnGtaWjdARo9rZncQ" target="_blank">查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            