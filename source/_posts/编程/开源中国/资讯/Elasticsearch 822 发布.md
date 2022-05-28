
---
title: 'Elasticsearch 8.2.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5943'
author: 开源中国
comments: false
date: Sat, 28 May 2022 07:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5943'
---

<div>   
<div class="content">
                                                                                            <p>Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 基于 Java 开发，并在 SSPL + Elastic License 双重授权许可下作为开源软件发布。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Elasticsearch 8.2.2 现已发布，该版本更新内容如下：</p> 
<h4><strong>Bug fixes</strong></h4> 
<p><span><span><strong>Audit</strong></span></span></p> 
<div> 
 <ul> 
  <li><span><span>修复 audit logging，使其在<code>origin.address</code>中一致包含 port number <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86732" target="_blank">#86732</a></span></span></li> 
 </ul> 
</div> 
<p><span><span><strong>CCR</strong></span></span></p> 
<div> 
 <ul> 
  <li><span><span>修复 CCR following 数据流时，follower 的索引被关闭而破坏数据流的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F87076" target="_blank">#87076</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F87048" target="_blank">#87048</a>）</span></span></li> 
 </ul> 
</div> 
<p><span><span><strong>Geo</strong></span></span></p> 
<div> 
 <ul> 
  <li>将 null value tags 添加到 vector tiles 的防护<span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F87051" target="_blank"> #87051</a></span></span></li> 
 </ul> 
</div> 
<p><span><span><strong>Infra/Core</strong></span></span></p> 
<div> 
 <ul> 
  <li><span><span>调整突发 cpu 的 osprobe 断言 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86990" target="_blank">#86990</a></span></span></li> 
 </ul> 
</div> 
<p><span><span><strong>Machine Learning</strong></span></span></p> 
<div> 
 <ul> 
  <li><span><span>修复集群生命周期早期的 ML task auditor <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F87023" target="_blank">#87023</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F87002" target="_blank">#87002</a>）</span></span></li> 
  <li><span><span>分类中的 Adjacency weighting 修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Fml-cpp%2Fpull%2F2277" target="_blank">#2277</a></span></span></li> 
 </ul> 
</div> 
<h4><strong><span><span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>增强功能</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<div> 
 <p><span><span><strong>Machine Learning</strong></span></span></p> 
 <div> 
  <ul> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>使 ML native processes 与 glibc 2.35 兼容（Ubuntu 22.04 需要）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Fml-cpp%2Fpull%2F2272" target="_blank">#2272</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
  <p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F8.2%2Frelease-notes-8.2.2.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/8.2/release-notes-8.2.2.html</a></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            