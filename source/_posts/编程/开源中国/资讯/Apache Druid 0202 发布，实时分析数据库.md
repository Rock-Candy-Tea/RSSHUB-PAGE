
---
title: 'Apache Druid 0.20.2 发布，实时分析数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6043'
author: 开源中国
comments: false
date: Sat, 03 Apr 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6043'
---

<div>   
<div class="content">
                                                                                            <p>Apache Druid 0.20.2 发布了。Druid 是一个分布式的、支持实时多维 OLAP 分析的数据处理系统。它既支持高速的数据实时摄入处理，也支持实时且灵活的多维数据分析查询。因此 Druid 最常用的场景就是大数据背景下、灵活快速的多维 OLAP 分析。 另外，Druid 还有一个关键的特点：它支持根据时间戳对数据进行预聚合摄入和聚合分析，因此也有用户经常在有时序数据处理分析的场景中用到它。 </p> 
<p>此版本引入了新的配置来解决 CVE-2021-26919：认证用户可以从恶意的 MySQL 数据库系统中执行任意代码。建议用户启用新配置，以缓解易受攻击的 JDBC 连接属性。这些配置将应用于所有 JDBC 连接以进行提取和查找，但不适用于元数据存储。更多细节可参见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdruid.apache.org%2Fdocs%2Flatest%2Fconfiguration%2Findex.html%23ingestion-security-configuration" target="_blank">安全配置</a>。</p> 
<ul> 
 <li><code>druid.access.jdbc.enforceAllowedProperties</code>：当为 true 时，Druid 将<code>druid.access.jdbc.allowedProperties</code>应用于以<code>jdbc:postgresql:</code>或<code>jdbc:mysql:</code>开头的 JDBC 连接。如果为 false，则 Druid 允许任何类型的 JDBC 连接，而无需 JDBC 属性验证。默认情况下，此配置设置为 false，以不中断滚动升级。此配置现已弃用，可以在以后的版本中删除。在这种情况下，将始终强制执行 allow list。</li> 
 <li><code>druid.access.jdbc.allowedProperties</code>：定义一个 allowed JDBC 属性的列表。如果<code>druid.access.jdbc.enforceAllowedProperties</code>被设置为 true，则 Druid 始终为所有以<code>jdbc:postgresql:</code>或<code>jdbc:mysql:</code>开头的 JDBC 连接强制执行该列表。已针对 MySQL connector 5.1.48 和 PostgreSQL connector 42.2.14 测试了此选项。其他 connector 版本可能无法使用。</li> 
 <li><code>druid.access.jdbc.allowUnknownJdbcUrlFormat</code>：如果为 false，则 Druid 仅接受以<code>jdbc:postgresql:</code>或<code>jdbc:mysql:</code>开头的 JDBC 连接。如果为 true，则 Druid 允许 JDBC 连接到任何类型的数据库，但仅只对 PostgreSQL 和 MySQL 执行<code>druid.access.jdbc.allowedProperties</code>。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Freleases%2Ftag%2Fdruid-0.20.2" target="_blank">https://github.com/apache/druid/releases/tag/druid-0.20.2</a> </p>
                                        </div>
                                      
</div>
            