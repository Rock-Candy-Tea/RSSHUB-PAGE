
---
title: 'openLooKeng V1.2.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6108'
author: 开源中国
comments: false
date: Thu, 15 Apr 2021 14:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6108'
---

<div>   
<div class="content">
                                                                    
                                                        <p>自去年6月开源以来，openLooKeng社区得到越来越多朋友的支持。社区内，小伙伴们对openLooKeng的性能给予了肯定和赞赏，同时也给出了许多有价值的建议。暖春3月，在众人的期待下，openLooKeng迎来了新版本V1.2.0。openLooKeng V1.2.0是在旧版本的基础上进行优化，并基于小伙伴们的体验和建议，新增一些技术，以提高引擎性能，争取为大家带来更丝滑流畅的体验。</p> 
<p><strong>于引擎内核来说，主要增强两个维度：融合分析场景和性能。</strong></p> 
<p><strong>» 查询容错增强，提高引擎执行的可靠性</strong></p> 
<p>在批查询处理运行的过程中，当某个工作节点出现故障时，可在其他节点上恢复任务，比如对Hive数据源的 insert 和 create table as select 操作。针对长时间运行的批查询处理任务，相比上一个版本，稳定性和可靠性有了极大的提升。</p> 
<p><strong>» 查询性能的优化：基于 StarTree 的查询预聚合能力增强</strong></p> 
<p>StarTree旨在优化低延迟、聚合查询语句。我们通过StarTree查询预聚合能力，为用户构建所需要的不同维度和不同聚合操作的 cube。在以后的查询过程中，如果遇到任何可匹配的聚合子查询，引擎将直接从cube中读取数据，避免在原始表上执行查询，从而提高查询性能。</p> 
<p><strong>» 引入 CTE（公共表表达式）优化技术，减少内存使用</strong></p> 
<p>在执行计划优化过程中引入CTE（公共表表达式）技术。当一个复杂查询中，存在某个子查询（例如 with语句）被多次使用，优化器会为重复的子查询自动生成一个CTE节点，该CTE节点的输出会被执行计划流程中的多个父节点消费。也就是说，重复的子查询只会执行一次，化繁为简， 同时也减少内存占用，引擎获得更好的性能。</p> 
<p><strong>» 通用算子下推框架，让 Connectors 参与到执行计划优化中</strong></p> 
<p>为了让算子下推过程更加简单灵活，我们采用新的通用算子下推框架，让每个Connector可以参与到执行计划优化中。引擎在进行执行计划优化时，能够自行应用Connector的优化规则，使得算子下推过程变得更加高效。</p> 
<p><strong>» 增强HIVE ORC的数据维护性能</strong></p> 
<p>该特性优化了数据写入和数据修改（更新和删除）的处理速度，并不影响『读性能』的流畅度；支持并发访问Hive Metastore，提高元数据操作性能，从而进一步优化数据写入和修改的性能。</p> 
<p><strong>于引擎门户来说，主要集中在南向生态方面的优化。</strong></p> 
<p><strong>» HBase Connector性能优化</strong></p> 
<p>针对单表查询性能的提升，我们新增了分片算法。另外，该性能支持 HBase 访问 Snapshot 的模式，从而提升多并发查询性能。</p> 
<p><strong>» 数据源UDF（User-Defined Function）支持下推</strong></p> 
<p>引擎支持外部函数（UDF）的注册，也支持将其下推到JDBC数据源。为了让大家拥有更好的体验，用户可以在不迁移自己数据源UDF的情况下，使用已有的UDF, 提高UDF的复用度。</p> 
<p>以上便是openLooKeng新版本V1.2.0 在性能优化上较为亮眼的地方。当然，<strong>作为大数据领域的关键项目，openLooKeng十分看重引擎的易用性和安全性</strong>。针对这两点，新版本V1.2.0做出如下增强：</p> 
<p><strong>» 易用性 | 增强Admin Dashboard UI用户体验</strong></p> 
<ul> 
 <li>优化定时全量加载导致的UI页面卡顿，</li> 
 <li>增强查询历史和查询结果的分页显示，</li> 
 <li>优化新增连接器的参数配置，</li> 
 <li>UI 界面支持Kerberos 和密码登录，支持查询历史按用户进行过滤。</li> 
</ul> 
<p><strong>» 安全性 | 基于Ranger的细粒度权限管控：支持行过滤和列掩码</strong></p> 
<p>增加行过滤和列掩码，增加认证用户模拟权限控制，提供更细化的权限控制粒度。</p> 
<hr> 
<p>看了这么多，是不是很想动手一试？感兴趣的朋友可以下载体验。</p> 
<p>新版本下载地址: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenlookeng.io%2Fzh-cn%2Fdownload.html" target="_blank">https://openlookeng.io/zh-cn/download.html</a></p> 
<p>如果您对新版本V1.2.0有其他建议，欢迎发邮件至 <strong><em><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ausers%40openlookeng.io" target="_blank">users@openlookeng.io</a></em></strong> 告知我们。openLooKeng社区感谢朋友们的支持，期待并欢迎更多朋友们的参与。</p> 
<p>• • •</p> 
<p>openLooKeng是一款开源的高性能数据虚拟化引擎，提供统一SQL接口，具备跨数据源/数据中心分析能力，为大数据用户提供极简的数据分析体验。欢迎加入openLooKeng社区，一起做点有意思的事儿，让大数据更简单！</p> 
<p>openLooKeng开源社区官方网站: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenlookeng.io%2Fzh-cn%2F" target="_blank">https://openlookeng.io/zh-cn/</a></p> 
<p>openLooKeng代码仓地址: <a href="https://gitee.com/openlookeng">https://gitee.com/openlookeng</a></p>
                                        </div>
                                      
</div>
            