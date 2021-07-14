
---
title: 'MongoDB 5.0 正式发布，新增时序集合功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=954'
author: 开源中国
comments: false
date: Wed, 14 Jul 2021 07:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=954'
---

<div>   
<div class="content">
                                                                    
                                                        <p>MongoDB 5.0 正式发布，该版本部分更新内容如下：</p> 
<h3>时间序列集合</h3> 
<ul> 
 <li>MongoDB 5.0 引入了时间序列集合，它有效地存储了一段时期内的测量序列。与普通集合相比，在时间序列集合中存储时间序列数据可以提高查询效率，并减少数据和索引的磁盘使用。</li> 
</ul> 
<h3>聚合</h3> 
<ul> 
 <li> <p><strong>新的聚合操作符</strong></p> <p>MongoDB 5.0 引入了以下聚合操作：</p> 
  <ul> 
   <li><code>$count</code>: <code>$count</code> 在现有管道 <code>$group</code> 阶段和新的 MongoDB 5.0 <code>$setWindowFields</code> 阶段中使用时，提供所有文档的计数。</li> 
   <li><code>$dateAdd</code>: 将一个 <code>Date</code> 对象按指定的时间单位递增。</li> 
   <li><code>$dateDiff</code>: 返回两个日期之间的差异。</li> 
   <li><code>$sampleRate</code>: 添加 <code>$sampleRate</code> 方法，以给定的速度从管道中概率性地选择文档。</li> 
   <li><code>$rand</code>: 每次调用 <code>$rand</code> 方法时，都会生成一个0到1之间的随机浮点数。新的 <code>$sampleRate</code> 操作是基于 <code>$rand</code> 的。</li> 
  </ul> </li> 
</ul> 
<h3>窗口操作符</h3> 
<ul> 
 <li>MongoDB 5.0 引入了 <code>$setWindowFields</code> 管道阶段，允许你在一个集合中的指定跨度的文档上执行操作，称为窗口。该操作根据所选择的窗口操作符返回结果。</li> 
</ul> 
<h3>一般聚合的改进</h3> 
<ul> 
 <li> <p><code>$expr</code> 操作符：比较运算符使用索引</p> <p>从 MongoDB 5.0 开始，放在 <code>$expr</code> 操作符中的 <code>$eq</code>、 <code>$lt</code>、 <code>$lte</code>、 <code>$gt</code>和 <code>$gte</code> 操作符可以使用索引来提高性能。</p> </li> 
 <li> <p><code>$ifNull</code> 表达式接受多个输入表达式</p> <p>从 MongoDB 5.0 开始，在返回一个替换表达式之前，你可以为 <code>$ifNull</code> 表达式指定多个输入表达式。</p> </li> 
 <li> <p>聚合的 <code>let</code> 选项</p> <p>从 MongoDB 5.0 开始， <code>aggregate</code> 命令和 <code>db.collection.aggregate()</code> 辅助方法有一个 <code>let</code> 选项，用于指定一个可以在聚合管道的其他地方使用的变量列表。这允许你通过将变量与查询文本分开来提高命令的可读性。</p> </li> 
 <li> <p><code>$lookup</code> 阶段：简洁的相关子查询</p> <p>从 MongoDB 5.0 开始，聚合管道 <code>$lookup</code> 阶段支持简明的相关子查询，改善集合之间的连接。</p> </li> 
 <li> <p>变更事件输出</p> <p>从 MongoDB 5.0 开始，变更事件包含字段 <code>updateDescription.truncatedArrays</code> 来记录数组的截断。</p> </li> 
</ul> 
<h3>索引</h3> 
<ul> 
 <li> <p>删除了 <code>geoHaystack</code> 索引和 <code>geoSearch</code> 命令</p> <p>MongoDB 5.0 删除了废弃的 <code>geoHaystack</code> 索引和 <code>geoSearch</code> 命令。使用带有 <code>$geoNear</code> 的 2d 索引或支持的 geospatial 查询操作符来代替。</p> <p>将你的 MongoDB 实例升级到 5.0 并将 <code>featureCompatibilityVersion</code> 设置为 5.0 将删除任何先前存在的 <code>geoHaystack</code> 索引。</p> </li> 
 <li> <p>新的错误信息</p> <p><code>db.collection.createIndex()</code> 和 <code>db.collection.createIndexes()</code> 操作在选项指定不正确时有新的错误信息。</p> </li> 
 <li> <p>中断索引构建</p> <p>如果副本集中的一个节点在索引构建过程中完全关闭或回滚，索引构建的进度现在会被保存到磁盘上。当服务器重新启动时，索引创建将从保存的位置恢复。</p> </li> 
 <li> <p><strong><code>reIndex</code>行为改变</strong></p> <p>从 MongoDB 5.0 开始，<code>[reIndex](<https://docs.mongodb.com/v5.0/reference/command/reIndex/#mongodb-dbcommand-dbcmd.reIndex>)</code>命令和 <code>[db.collection.reIndex()](<https://docs.mongodb.com/v5.0/reference/method/db.collection.reIndex/#mongodb-method-db.collection.reIndex>)</code>shell 方法只能在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.mongodb.com%2Fv5.0%2Freference%2Fglossary%2F%23std-term-standalone" target="_blank">独立</a>实例上运行 。</p> </li> 
</ul> 
<h3>安全</h3> 
<ul> 
 <li> <p><strong>支持配置 TLS 1.3 密码套件</strong></p> <p>MongoDB 5.0引入了opensslCipherSuiteConfig参数，以便在使用TLS 1.3加密时，能够配置OpenSSL所支持的密码套件。</p> </li> 
</ul> 
<p>完整文档可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.mongodb.com%2Fv5.0%2Frelease-notes%2F5.0%2F" target="_blank">https://docs.mongodb.com/v5.0/release-notes/5.0/</a></p>
                                        </div>
                                      
</div>
            