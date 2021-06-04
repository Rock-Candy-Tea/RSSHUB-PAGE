
---
title: 'Elasticsearch 7.13.1 发布，基于 Lucene 库的搜索引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4622'
author: 开源中国
comments: false
date: Fri, 04 Jun 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4622'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 Apache 许可证下作为开源软件发布。官方客户端在 Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby 和许多其他语言中都是可用的。</p> 
<p>Elasticsearch 7.13.1 正式发布，该版本部分更新内容如下：</p> 
<p>Engine</p> 
<ul> 
 <li>修复对冻结索引的 PIT 创建的非法访问；</li> 
</ul> 
<p>Geo</p> 
<ul> 
 <li>修复 Rectangle() 错误信息中的错别字；</li> 
</ul> 
<p>Infra/Core</p> 
<ul> 
 <li>验证系统索引是否也是隐藏索引；</li> 
</ul> 
<p>Infra/Scripting</p> 
<ul> 
 <li>作为 Painless 沙盒的一部分，将 LinkageError 添加到捕获的错误中；</li> 
</ul> 
<p>Machine Learning</p> 
<ul> 
 <li>从获取类别 Grok 模式创建中减少警告日志记录；</li> 
</ul> 
<p>Search</p> 
<ul> 
 <li>搜索分析器应该默认配置索引分析器而不是默认值</li> 
</ul> 
<p>Snapshot/Restore</p> 
<ul> 
 <li>当 unfreezing cold/frozen 索引时，不要删除写入块；</li> 
 <li>修复并发快照和索引删除的错误；</li> 
 <li>修复版本库分析器 API 规范的位置；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F7.13%2Frelease-notes-7.13.1.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/7.13/release-notes-7.13.1.html</a></p>
                                        </div>
                                      
</div>
            