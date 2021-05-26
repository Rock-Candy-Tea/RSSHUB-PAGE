
---
title: 'ArangoDB 3.7.12 发布，分布式多模型数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9343'
author: 开源中国
comments: false
date: Tue, 25 May 2021 23:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9343'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ArangoDB 3.7.12 正式发布了。ArangoDB 是一个分布式原生的多模型数据库，具有灵活的文档、图形和键值数据模型。使用方便的 SQL 查询语言或 JavaScript 扩展构建高性能应用程序。</p> 
<ul> 
 <li>修复 DEVSUP-764 (SEARCH-7)：LEVENSHTEIN_MATCH 函数的 BM25 分数不一致；</li> 
 <li>增加了 2 个选项，允许对 HTTP API 的 root 调用进行 HTTP 重定向定制： 
  <ul> 
   <li><code>-http.permanent-redirect-root</code>：如果为 True（默认），使用永久的重定向，如果为 False，则退回到临时重定向；</li> 
   <li><code>-http.redirect-root-to</code>：将 root 网址重定向到指定的路径（如果没有设置（默认），则重定向到 "/_admin/ardvark/index.html"）；</li> 
  </ul> </li> 
 <li>修复 BTS-417：在某些情况下，如果近距离扫描的两个界限（下限和上限）使用相同的操作符表达，例如，<code>FILTER doc.beginDate >= lb AND ub >= doc.beginDate</code>，则索引没有考虑两个界限；</li> 
 <li>修复 BTS-416：在关闭过程中，Shard leader 错误地报告说它不能弃用 Shard follower，而不是正确地指出关闭的原因；</li> 
 <li>修正 BTS-354：与 getCollection 相关的断言；</li> 
 <li>修正 BTS-403：热恢复也必须清除相关的 <code>Current</code> 键。覆盖的 <code>Plan</code> 条目需要反映在 <code>Current</code> 中，以避免维护工作中的冲突；</li> 
 <li>修正 #14122：当优化器规则 "inline-subqueries" 被应用时，它可能会重命名查询中的一些变量。然而，变量重命名并不是针对遍历 PRUNE 条件进行的，所以 PRUNE 条件仍然可以引用过时的变量，这将使查询失败，出现如下错误： 
  <ul> 
   <li>Query: AQL: missing variable ... for node ... while planning registers</li> 
  </ul> </li> 
 <li>修复了连接池中的一个 UAF 错误；</li> 
 <li>修复 DEVSUP-749：修复在同一集合上执行并发的视图/链接 DDL 操作和索引 DDL 操作时的潜在死锁；</li> 
 <li>修复了数据库创建不成功时错误报告中的错误，这导致了向机构报告这一错误的循环；</li> 
 <li>修复了如果 HTTP 版本不是 1.0 或 1.1，以及 Content-Length 过大（>1GB）的错误响应；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffossies.org%2Flinux%2Farangodb%2FCHANGELOG" target="_blank">https://fossies.org/linux/arangodb/CHANGELOG</a></p>
                                        </div>
                                      
</div>
            