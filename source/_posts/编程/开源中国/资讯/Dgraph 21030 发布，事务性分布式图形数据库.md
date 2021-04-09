
---
title: 'Dgraph 21.03.0 发布，事务性分布式图形数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1898'
author: 开源中国
comments: false
date: Fri, 09 Apr 2021 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1898'
---

<div>   
<div class="content">
                                                                                            <p>Dgraph 是一个可扩展的，分布式的，低延迟的图数据库，目标是提供 Google 生产水平的规模和吞吐量，在超过 TB 的结构数据里，为用户提供足够低延迟的实时查询。Dgraph 支持 GraphQL 作为查询语言，响应 JSON。</p> 
<p>Dgraph 21.03.0 发布了，本次更新内容如下：</p> 
<h3>变化：</h3> 
<ul> 
 <li>Feat(flags): 扩展 badger 以接受所有有效选项；</li> 
 <li>Feat(Dgraph): 只读副本；</li> 
 <li>将多个 flags 合并为几个 SuPerflags；</li> 
 <li>Fix(commit): 使 txn context 更强大；</li> 
 <li>Fix(Query): 针对非法的数学运算返回错误；</li> 
 <li>重命名 Badger 指标；</li> 
 <li>Fix(Backups): 新的 badge Superflag、NumGoroutines 选项解决了 OOM 崩溃；</li> 
 <li>删除还原跟踪器，因为它不是必需的；</li> 
</ul> 
<h3>添加：</h3> 
<ul> 
 <li>GraphQL 
  <ul> 
   <li>Feat(GraphQL): 现在在 GraphQL admin 可以使用零个 HTTP 端点；</li> 
   <li>Feat(GraphQL): 允许多个 JWKUrls 进行身份验证；</li> 
   <li>Feat(Apollo): 添加对 @provides 和 @requires 指令的支持；</li> 
   <li>Feat(GraphQL): 升级 GraphQL-transport-ws 模块；</li> 
   <li>Feat(GraphQL): 添加对 regexp、in 和 array 的身份验证令牌支持；</li> 
   <li>Feat(GraphQL): 将对 IN 过滤器的支持扩展到所有标量数据类型；</li> 
  </ul> </li> 
 <li>core 
  <ul> 
   <li>Feat(query): 添加机制以限制未决查询的数量；</li> 
   <li>Perf(bulk): 重用分配器；</li> 
   <li>Perf(compression): 在导出和备份中使用带有 BestSpeed 的 gzip；</li> 
   <li>Feat(flags): 添加查询超时作为限制配置；</li> 
   <li>Opt(reindex): 插入新的 predicate 时不要尝试建立索引；</li> 
   <li>Perf(txn): 对 context 键和 predicates 进行重复数据删除；</li> 
   <li>Feat(flags): 使用保险柜存储 ACL 机密；</li> 
   <li>Feat(bulk): 添加/jemalloc HTTP 端点；</li> 
   <li>Feat(metrics): 添加 Dgraph txn 指标；</li> 
   <li>Feat(Bulk Loader + Live Loader): 支持通过 s3/minio 加载文件；</li> 
   <li>Feat(Monitoring): 添加对磁盘空间和备份数量的监控；</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdgraph-io%2Fdgraph%2Freleases" target="_blank">https://github.com/dgraph-io/dgraph/releases</a></p>
                                        </div>
                                      
</div>
            