
---
title: 'Apache Lucene 9.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7286'
author: 开源中国
comments: false
date: Tue, 22 Mar 2022 23:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7286'
---

<div>   
<div class="content">
                                                                                            <p>Apache Lucene 发布了最新的 9.1.0 版本，相比于 9.0 版本，该版本主要改进内容包括：</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">新特性</h4> 
<ul style="margin-left:10px; margin-right:10px"> 
 <li>Lucene JAR 采用 Java 模块化方式组织，提供模块描述和依赖信息</li> 
 <li>过滤器支持邻近向量搜索</li> 
 <li>标准的查询语法中支持内部查询</li> 
 <li>全新的令牌过滤器 SpanishPluralStemFilter 用于西班牙语复数的精确词干分析</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">优化</h4> 
<ul style="margin-left:10px; margin-right:10px"> 
 <li>高维度向量的索引吞吐量提升 30%</li> 
 <li>高维度邻接向量搜索速度提升 10%</li> 
 <li>跨不同查询类型的 count 搜索速度更快</li> 
 <li>计算分类聚合信息时速度更快</li> 
 <li>其他小的搜索速度提升，包括改进了 PointRangeQuery, MultiRangeQuery 和 CoveringRangeQuery</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">其他</h4> 
<ul style="margin-left:10px; margin-right:10px"> 
 <li>测试框架也做了模块化处理，所有包名改为 org.apache.lucene.tests.* 以避免包名冲突</li> 
 <li>Lucene现在通过支持多个图形层，忠实地实现了最近邻搜索的HNSW算法</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">还有很多其他的小改进和 bug 修复，详细列表请看</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flucene.apache.org%2Fcore%2F9_1_0%2Fchanges%2FChanges.html" target="_blank">https://lucene.apache.org/core/9_1_0/changes/Changes.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            