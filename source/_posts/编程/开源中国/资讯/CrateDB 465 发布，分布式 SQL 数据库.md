
---
title: 'CrateDB 4.6.5 发布，分布式 SQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2395'
author: 开源中国
comments: false
date: Mon, 15 Nov 2021 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2395'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CrateDB 是一个分布式的 SQL 数据库，使得实时存储和分析大量的机器数据变得简单。CrateDB 提供了通常与 NoSQL 数据库相关的可扩展性和灵活性，最小的 CrateDB 集群可以轻松地每秒摄取数万条记录。这些数据可以在整个集群中实时地、临时地、并行地进行查询。</p> 
<p>CrateDB 4.6.5 正式发布，该版本更新内容如下：</p> 
<h3>修复</h3> 
<ul> 
 <li>修正了当 <code>UNION ALL</code> 的 <code>SELECT</code> 结果包括具有相同名称但类型不同的子列的对象类型时，导致 <code>UNION ALL</code> 语句成功或抛出意外的异常。</li> 
 <li>修正了当使用 <code>%D</code> 指定符时， <code>date_format()</code> 会返回错误的值。</li> 
 <li>修正了 4.2 版本中引入的性能退步问题，该问题导致在视图或虚拟表上面的别名列上使用 <code>WHERE</code>子句的查询速度很慢。</li> 
 <li>修正了 <code>HBA</code> 中的问题</li> 
 <li>修正了一个在将代表有效多边形的 WKT 字符串转换为 <code>geo_shape</code> 时，会产生异常的问题。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrate%2Fcrate%2Freleases%2Ftag%2F4.6.5" target="_blank">https://github.com/crate/crate/releases/tag/4.6.5</a></p>
                                        </div>
                                      
</div>
            