
---
title: 'Elasticsearch 8.1.3 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2209'
author: 开源中国
comments: false
date: Fri, 22 Apr 2022 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2209'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 基于 Java 开发，并在 SSPL + Elastic License 双重授权许可下作为开源软件发布。</p> 
<p style="margin-left:0px">Elasticsearch 8.1.3 正式发布，该版本更新内容如下：</p> 
<h3 style="margin-left:0px"><strong>Bug fixes</strong></h3> 
<p style="margin-left:0px"><strong>Authorization</strong></p> 
<ul> 
 <li><span style="color:#2e3033">解析超级用户时，忽略 app priv 失败 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85519" target="_blank">#85519</a> </li> 
</ul> 
<p style="margin-left:0px"><span style="color:#212529"><strong>Machine Learning</strong></span></p> 
<ul> 
 <li><span style="color:#2e3033">避免在<strong> </strong></span>renormalizer 中出现多队列<span style="color:#212529">分位数文档（multiple queued quantiles documents）</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85555" target="_blank">#85555</a><span style="color:#212529"> (issue: </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F85539" target="_blank">#85539</a><span style="color:#212529">)</span></li> 
</ul> 
<p style="margin-left:0px"><strong>Mapping</strong></p> 
<ul> 
 <li><span style="color:#212529">不在</span><span style="color:#2e3033">重复的内容字段过滤器中失败 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85382" target="_blank">#85382</a> </li> 
</ul> 
<p style="margin-left:0px"><span style="color:#212529"><strong>Search</strong></span></p> 
<ul> 
 <li><span style="color:#212529">修复使用<strong> </strong></span><span style="color:#555555"><code>indices.queries.cache.all_segments</code></span><span style="color:#212529"><strong> </strong></span><span style="color:#2e3033">跳过缓存因素 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85510" target="_blank">#85510</a>  </li> 
</ul> 
<p style="margin-left:0px"><span style="color:#212529"><strong>Snapshot/Restore</strong></span></p> 
<ul> 
 <li><span style="color:#2e3033">公开 GCS 存储库的代理设置 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85785" target="_blank">#85785</a><span style="color:#212529"> (issue: </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F84569" target="_blank">#84569</a><span style="color:#212529">)</span></li> 
</ul> 
<p style="margin-left:0px"><span style="color:#212529"><strong>Watcher</strong></span></p> 
<ul> 
 <li>当数据流指向多个索引时，避免 Watcher 验证错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85507" target="_blank">#85507</a><span style="color:#212529"> (issue: </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F85508" target="_blank">#85508</a><span style="color:#212529">) </span></li> 
 <li>在 WARN 级别记录 Watcher 的集群状态验证错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85632" target="_blank">#85632</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F8.1%2Frelease-notes-8.1.3.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/8.1/release-notes-8.1.3.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            