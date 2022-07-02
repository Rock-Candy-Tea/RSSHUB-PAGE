
---
title: 'Elasticsearch v8.3.1 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3579'
author: 开源中国
comments: false
date: Sat, 02 Jul 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3579'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div> 
   <p style="margin-left:0px">Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 基于 Java 开发，并在 SSPL + Elastic License 双重授权许可下作为开源软件发布。</p> 
   <p style="margin-left:0px">Elasticsearch 8.3.1 现已发布，该版本更新内容如下：</p> 
   <h3 style="margin-left:0px"><strong>Bug 修复</strong></h3> 
   <p><span style="color:#212529"><strong>Audit</strong></span></p> 
   <ul> 
    <li>支持删除审计日志的 <span style="color:#212529">ignore </span>过滤器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F87675" target="_blank">#87675</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F68588" target="_blank">#68588</a>）</li> 
   </ul> 
   <p><span style="color:#212529"><strong>Ingest</strong></span></p> 
   <ul> 
    <li>不忽略批量 API  中的 upserts 管道 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F87719" target="_blank">#87719</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F87131" target="_blank">#87131</a>）</li> 
    <li>Geoip 处理器应遵守 <code>ignore_missing</code> 缺少数据库的情况 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F87793" target="_blank">#87793</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F87345" target="_blank">#87345</a>）</li> 
   </ul> 
   <p><span style="color:#212529"><strong>Machine Learning</strong></span></p> 
   <ul> 
    <li>提高经过训练的模型统计 API 性能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F87978" target="_blank">#87978</a></li> 
   </ul> 
   <p><span style="color:#212529"><strong>Snapshot/Restore</strong></span></p> 
   <ul> 
    <li>使用提供的 SAS 令牌，不使用可能产生无效签名的 SDK   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F88155" target="_blank">#88155</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F88140" target="_blank">#88140</a>）</li> 
   </ul> 
   <p><span style="color:#212529"><strong>Stats</strong></span></p> 
   <ul> 
    <li>在管理池上运行 <code>TransportClusterInfoActions</code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F87679" target="_blank">#87679</a></li> 
   </ul> 
   <p><span style="color:#212529"><strong>Transform</strong></span></p> 
   <ul> 
    <li>具有系统权限的 <code>_refresh</code> 与具有用户权限的 <code>delete by query</code> 分开执行 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F88005" target="_blank">#88005</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F88001" target="_blank">#88001</a>） </li> 
   </ul> 
   <h3 style="margin-left:0px"><strong>增强 </strong></h3> 
   <p><span style="color:#212529"><strong>Discovery </strong></span><strong>插件</strong></p> 
   <ul> 
    <li>从 discovery-azure中删除多余的 jackson 依赖项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F87898" target="_blank"> #87898</a> </li> 
   </ul> 
   <p><span style="color:#212529"><strong>Performance</strong></span></p> 
   <ul> 
    <li>警告大型预读对搜索的影响 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F88007" target="_blank">#88007</a></li> 
   </ul> 
   <p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F8.3%2Frelease-notes-8.3.1.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/8.3/release-notes-8.3.1.html</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            