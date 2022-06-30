
---
title: 'Elasticsearch 8.3.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3216'
author: 开源中国
comments: false
date: Thu, 30 Jun 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3216'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 基于 Java 开发，并在 SSPL + Elastic License 双重授权许可下作为开源软件发布。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Elasticsearch 8.3.0 现已发布，该版本更新内容如下：</p> 
<h4>已知问题</h4> 
<ul> 
 <li>8.3.0 存在一个问题，该问题可能会导致在使用 SAS 令牌时创建和访问针对 Azure 快照存储库的快照的认证失败。这会影响已部署 8.3.0 的 self-managed 客户。Elastic Cloud Azure 部署当前未升级到 8.3.0，因此不受影响（<span style="background-color:#ffffff; color:#212529">issue</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F88140" target="_blank">#88140</a>）</li> 
</ul> 
<h3><span><span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>弃用</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<div> 
 <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Authentication</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <div> 
  <ul> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>不推荐在没有相应绑定密码的情况下在 LDAP 或 Active Directory (AD) 领域中配置绑定 DN <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85326" target="_blank">#85326</a>（</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span style="background-color:#ffffff; color:#212529">issue</span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F47191" target="_blank">#47191</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
  <p> </p> 
  <h3>Enhancements</h3> 
  <div> 
   <p><strong>Aggregations</strong></p> 
   <div> 
    <ul> 
     <li><span><span>在<code>random_sampler</code>aggregation 中提高最小和最大性能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85118" target="_blank">#85118</a></span></span></li> 
    </ul> 
   </div> 
   <p><span><span><strong>Authentication</strong></span></span></p> 
   <div> 
    <ul> 
     <li><span><span>支持 JWT Realm Tokens 中的可配置声明 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86533" target="_blank">#86533</a></span></span></li> 
     <li><span><span>由于文档或字段级别安全性的许可要求而禁用用户角色时发出警告 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85393" target="_blank">#85393</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F79207" target="_blank">#79207</a>）</span></span></li> 
     <li><span><span><code>TokenService</code>解码 JWT，将警告更改为调试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86498" target="_blank">#86498</a></span></span></li> 
    </ul> 
   </div> 
   <p><span><span><strong>Authorization</strong></span></span></p> 
   <div> 
    <ul> 
     <li><span><span>改进运行时被拒绝的错误信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85501" target="_blank">#85501</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F72904" target="_blank">#72904</a>）</span></span></li> 
     <li><span><span>提高 boolean-only response 的“Has Privilege”性能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86685" target="_blank">#86685</a></span></span></li> 
     <li><span><span>放宽角色 API 中角色名称的限制 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86604" target="_blank">#86604</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F86480" target="_blank">#86480</a>）</span></span></li> 
     <li><span><span>[Osquery] 通过访问 osquery_manager 扩展<code>kibana_system</code>角色… <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86609" target="_blank">#86609</a></span></span></li> 
    </ul> 
   </div> 
   <p><span><span><strong>Autoscaling</strong></span></span></p> 
   <div> 
    <ul> 
     <li><span><span>在所需节点中添加对 CPU 范围的支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86434" target="_blank">#86434</a></span></span></li> 
    </ul> 
    <p><span><span>......</span></span></p> 
    <h3><span><span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>New features</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
    <div> 
     <p><strong>Geo</strong></p> 
     <div> 
      <ul> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>与 geogrid 聚合一起使用的新 geo_grid 查询 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86596" target="_blank">#86596</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F85727" target="_blank">#85727</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
      </ul> 
     </div> 
     <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Health</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
     <div> 
      <ul> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>为 health impacts 添加对<code>impact_areas</code>的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85830" target="_blank">#85830</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F85829" target="_blank">#85829</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>为 shards allocation actions 添加故障排除指南 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F87078" target="_blank">#87078</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>为剩余的 health indicators 添加潜在影响 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86197" target="_blank">#86197</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>Health api drill down <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85234" target="_blank">#85234</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F84793" target="_blank">#84793</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>跟踪从每个节点看到的主历史记录的新服务 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85941" target="_blank">#85941</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>按索引优先级排序影响索引名称 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85347" target="_blank">#85347</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
      </ul> 
     </div> 
     <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Mapping</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
     <div> 
      <ul> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>为 metrics usecases 添加对字段名称中点的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86166" target="_blank">#86166</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F63530" target="_blank">#</a> 63530 ）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>Synthetic source <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85649" target="_blank">#85649</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
      </ul> 
     </div> 
     <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>SQL</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
     <div> 
      <ul> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>SQ：在 SQL 查询中允许部分结果 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85897" target="_blank">#85897</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F33148" target="_blank">#33148</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
      </ul> 
     </div> 
     <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Search</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
     <div> 
      <ul> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>将快照作为简单的存档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86261" target="_blank">#86261</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F81210" target="_blank">#81210</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
      </ul> 
     </div> 
     <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>TSDB</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
     <div> 
      <ul> 
       <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>TSDB：在时间序列索引上实现 downsampling <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85708" target="_blank">#85708</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F69799" target="_blank">#69799</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F65769" target="_blank">#65769</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
      </ul> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div> 
<p>更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F8.3%2Frelease-notes-8.3.0.html" target="_blank">查看官方公告</a>。</p> 
<p><strong>下载地址：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fcn%2Fdownloads%2Felasticsearch" target="_blank">https://www.elastic.co/cn/downloads/elasticsearch</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            