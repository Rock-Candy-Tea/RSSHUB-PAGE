
---
title: 'Elasticsearch 7.12.1 发布，基于 Lucene 库的搜索引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7208'
author: 开源中国
comments: false
date: Thu, 29 Apr 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7208'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 Apache 许可证下作为开源软件发布。官方客户端在 Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby 和许多其他语言中都是可用的。</p> 
<p>Elasticsearch 7.12.1 正式发布，该版本部分更新内容如下：</p> 
<p>CCR：</p> 
<ul> 
 <li>防止使用 CCR 来跟踪快照备份的索引 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F70580" target="_blank">#70580</a></li> 
</ul> 
<p>特性/数据流：</p> 
<ul> 
 <li>允许关闭一个数据流的写入索引 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F70908" target="_blank">#70908</a> (issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F70861" target="_blank">#70861</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F70903" target="_blank">#70903</a>)</li> 
 <li>改进数据流翻转，简化数据流的集群元数据验证  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F70934" target="_blank">#70934</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F70905" target="_blank">#70905</a>)</li> 
</ul> 
<p>机器学习:</p> 
<ul> 
 <li>让 ML 原生进程在 x86_64 的 glibc 2.33 下工作 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Fml-cpp%2Fpull%2F1828" target="_blank">#1828</a></li> 
</ul> 
<p>快照/恢复</p> 
<ul> 
 <li>调整冻结的写缓冲区和线程池 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F71172" target="_blank">#71172</a></li> 
 <li>为 <code>full_copy</code> 可搜索快照添加 CFS 索引缓存支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F70646" target="_blank">#70646</a></li> 
 <li>调整 Lucene 元数据文件的 blob 缓存文档的长度 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F69431" target="_blank">#69431</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F69283" target="_blank">#69283</a>)</li> 
 <li>始终使用 CacheService 来缓存元数据 blob <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F70668" target="_blank">#70668</a> (issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F70728" target="_blank">#70728</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F70763" target="_blank">#70763</a>)</li> 
 <li>为可搜索的快照碎片延迟加载软删除 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F69203" target="_blank">#69203</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F7.12%2Frelease-notes-7.12.1.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/7.12/release-notes-7.12.1.html</a></p>
                                        </div>
                                      
</div>
            