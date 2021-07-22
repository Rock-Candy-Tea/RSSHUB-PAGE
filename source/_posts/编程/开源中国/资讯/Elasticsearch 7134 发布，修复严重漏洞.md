
---
title: 'Elasticsearch 7.13.4 发布，修复严重漏洞'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5893'
author: 开源中国
comments: false
date: Thu, 22 Jul 2021 06:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5893'
---

<div>   
<div class="content">
                                                                                            <p>Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 Apache 许可证下作为开源软件发布。官方客户端在 Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby 和许多其他语言中都是可用的。</p> 
<p>Elasticsearch 7.13.4 正式发布，该版本更新内容如下：</p> 
<h3><strong>安全更新</strong></h3> 
<ul> 
 <li>在 Elasticsearch 的错误报告中发现了一个内存泄露的漏洞。能够向 Elasticsearch 提交任意查询的用户可以提交一个异常的查询，这会导致返回的错误信息包含以前使用的数据缓冲区部分。这个缓冲区可能包含敏感信息，如 Elasticsearch 文档或身份认证详情。7.13.4 之前的所有 Elasticsearch 版本都受到这个漏洞的影响。</li> 
</ul> 
<h3>Bug 修复</h3> 
<ul> 
 <li>映射：在动态映射更新中调用 <code>fixRedundantIncludes</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74903" target="_blank">#74903</a>；</li> 
 <li>快照/还原：修复并发快照存储库删除问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74880" target="_blank">#74880</a>；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F7.13%2Frelease-notes-7.13.4.html%23release-notes-7.13.4" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/7.13/release-notes-7.13.4.html#release-notes-7.13.4</a></p>
                                        </div>
                                      
</div>
            