
---
title: 'CrateDB 4.6.0 发布，分布式 SQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5076'
author: 开源中国
comments: false
date: Thu, 15 Jul 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5076'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CrateDB 是一个分布式的 SQL 数据库，使得实时存储和分析大量的机器数据变得简单。CrateDB 提供了通常与 NoSQL 数据库相关的可扩展性和灵活性，最小的 CrateDB 集群可以轻松地每秒摄取数万条记录。这些数据可以在整个集群中实时地、临时地、并行地进行查询。</p> 
<p>CrateDB 4.6.0 正式发布，该版本更新内容如下：</p> 
<h3>变化</h3> 
<p><strong>性能改进</strong></p> 
<ul> 
 <li>提高了 :ref <code>hyperlog_distinct <aggregation-hyperlog-distinct></code> 聚合函数的性能；</li> 
 <li>提高了带有 <code>WHERE</code> 条件的 <code>SELECT</code> 语句的性能；</li> 
 <li>提高了 <code>INSERT FROM query</code> 语句的性能，其中 <code>query</code> 包含 <code>GROUP BY</code> 子句；</li> 
 <li>改进了用于 <code>INSERT FROM QUERY</code> 和 <code>COPY FROM</code> 操作的内部节流机制。这应该会使这些查询在集群可以腾出的情况下利用更多的资源；</li> 
 <li>增加了一项优化，提高了对至少有一个内部列有 <code>NOT NULL</code> 约束的对象列的 <code>count()</code> 聚合的性能；</li> 
</ul> 
<h3>SQL 语句和兼容性</h3> 
<ul> 
 <li>增加了 bit(n) 数据类型；</li> 
 <li>CrateDB 现在接受 <code>START TRANSACTION</code> 语句以兼容 PostgreSQL wire protocol；</li> 
 <li>为传递给 <code>COPY FROM</code> 语句的 URI 增加了对目录级通配符的支持；</li> 
</ul> 
<h3>新标量</h3> 
<ul> 
 <li>增加了 <code>array_to_string</code> 标量函数，使用分隔符和可选的空字符串将数组元素连接成一个字符串；</li> 
 <li>增加了 <code>array_min</code> 和 <code>array_max</code> 标量函数，分别返回数组中最小和最大的元素；</li> 
 <li>增加了 <code>array_sum</code> 标量函数，返回数组中所有元素的和；</li> 
 <li>增加了 <code>array_avg</code> 标量函数，返回数组中所有元素的平均值；</li> 
</ul> 
<h3>管理控制台</h3> 
<ul> 
 <li>删除了所有分析（UDC、Segment）；</li> 
 <li>删除了状态栏中的 "通知" 部分；</li> 
 <li>删除了控制台中列的 min-width，以减少滚动；</li> 
 <li>改变了控制台的语法高亮显示。双引号中的关键词现在不再高亮显示。类型用不同的颜色高亮显示；</li> 
 <li>激活了关键词的 codemirror 代码提示；</li> 
 <li>改变了滚动条的外观，使其看起来更现代；</li> 
 <li>为表视图中的 <code>varchar(n)</code> 和 <code>bit(n)</code> 类型增加了长度限制；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrate.io%2Fdocs%2Fcrate%2Freference%2Fen%2Fmaster%2Fappendices%2Frelease-notes%2F4.6.0.html" target="_blank">https://crate.io/docs/crate/reference/en/master/appendices/release-notes/4.6.0.html</a></p>
                                        </div>
                                      
</div>
            