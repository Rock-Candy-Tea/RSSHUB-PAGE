
---
title: 'Elasticsearch 7.13.0 发布，基于 Lucene 库的搜索引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5656'
author: 开源中国
comments: false
date: Wed, 26 May 2021 23:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5656'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 Apache 许可证下作为开源软件发布。官方客户端在 Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby 和许多其他语言中都是可用的。</p> 
<p>Elasticsearch 7.13.0 正式发布，该版本部分更新内容如下：</p> 
<p><strong>映射变化：</strong></p> 
<ul> 
 <li>Geo 映射器不再接受来自多字段的外部值；</li> 
 <li>Geopoint 映射器将 geohashes 逐一传递给子字段；</li> 
</ul> 
<p><strong>设置变化：</strong></p> 
<ul> 
 <li>冻结层和多个数据路径的变化；</li> 
</ul> 
<p><strong>废弃的功能：</strong></p> 
<p>以下功能在 Elasticsearch 7.13 中已被废弃，并将在 8.0 中被彻底移除。虽然这不会对你的应用程序产生直接影响，但我们强烈建议你在升级到 7.13 后采取所述步骤更新你的代码。</p> 
<p><strong>聚合功能的废弃：</strong></p> 
<ul> 
 <li>布尔字段上的日期聚合已被弃用；</li> 
</ul> 
<p><strong>核心弃用：</strong></p> 
<ul> 
 <li>多重数据路径支持已被弃用；</li> 
 <li>在 8.0.0 中，action.destructive_requires_name 设置将默认为 true；</li> 
</ul> 
<p><strong>EQL 弃用：</strong></p> 
<ul> 
 <li>通配符函数已被废弃；</li> 
</ul> 
<p><strong>安全问题：</strong></p> 
<ul> 
 <li>文件和本地域的隐式启用已被弃用；</li> 
 <li>废弃了系统调用过滤器设置；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F7.13%2Fmigrating-7.13.html%23breaking-changes-7.13" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/7.13/migrating-7.13.html#breaking-changes-7.13</a></p>
                                        </div>
                                      
</div>
            