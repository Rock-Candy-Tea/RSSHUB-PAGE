
---
title: 'Apache Solr 8.10 发布，Java 企业级搜索引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4308'
author: 开源中国
comments: false
date: Thu, 30 Sep 2021 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4308'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Solr 是 Apache Lucene 项目中流行的、快速的、开源的 NoSQL 搜索平台。它的主要功能包括强大的全文搜索、命中标示、分面搜索和分析、丰富的文档解析、地理空间搜索、广泛的 REST API 以及并行 SQL。Solr 是企业级的、安全的和高度可扩展的，提供容错的分布式搜索和索引，并为世界上许多的互联网网站提供搜索和导航功能。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Solr 8.10 重点更新包括：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>嵌套文档的 Partial/Atomic Updates（原子更新）。这使得嵌套文档的原子更新成为可能，而不需要提供整个嵌套的层次结构</li> 
 <li>引入了类别路由别名功能，根据字段的值，以数据驱动的方式将文件分配到集合中</li> 
 <li>REINDEXCOLLECTION 命令用于重新索引现有的集合</li> 
 <li>集合 RENAME 命令支持在大多数集合管理命令中使用别名</li> 
 <li>SolrCloud 集合的只读模式</li> 
 <li>对许多请求参数不正确或不存在的值的处理得到了改进。在这种情况下，响应是 400 http 代码，而不是之前的 500</li> 
 <li>In-place 更新对使用 route.field 创建的集合有效</li> 
 <li>当每个 note 中存在多个副本时，Asynchronous Collection API 调用不会过早地返回完成状态</li> 
 <li>Range Facets 和 Terms Component 的性能在某些情况下得到了优化</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcwiki.apache.org%2Fconfluence%2Fdisplay%2FSOLR%2FReleaseNote810" target="_blank">https://cwiki.apache.org/confluence/display/SOLR/ReleaseNote810</a></p>
                                        </div>
                                      
</div>
            