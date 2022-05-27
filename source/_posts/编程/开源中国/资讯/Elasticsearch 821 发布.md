
---
title: 'Elasticsearch 8.2.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9057'
author: 开源中国
comments: false
date: Fri, 27 May 2022 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9057'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 基于 Java 开发，并在 SSPL + Elastic License 双重授权许可下作为开源软件发布。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Elasticsearch 8.2.1 现已发布，该版本更新内容如下：</p> 
<h4><strong>Bug fixes</strong></h4> 
<p><strong>Aggregations</strong></p> 
<div> 
 <ul> 
  <li><span><span>修复<code>AdaptingAggregator</code> <code>toString</code>方法<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86042" target="_blank">#86042</a></span></span></li> 
  <li><span><span>未映射字段的后键解析的复杂性较低<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86359" target="_blank">#86359</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F85928" target="_blank">#85928</a>）</span></span></li> 
 </ul> 
</div> 
<p><span><span><strong>Authentication</strong></span></span></p> 
<div> 
 <ul> 
  <li><span><span>setting user 时确保身份验证是线上兼容的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86741" target="_blank">#86741</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F86716" target="_blank">#86716</a>）</span></span></li> 
 </ul> 
</div> 
<p><span><span><strong>Cluster Coordination</strong></span></span></p> 
<div> 
 <ul> 
  <li><span><span>避免破坏 add/clear voting exclusions  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86657" target="_blank">#86657</a></span></span></li> 
 </ul> 
</div> 
<p><span><span><strong>Geo</strong></span></span></p> 
<div> 
 <ul> 
  <li><span><span>当有界六边形网格在其中一个极点上包含 bin 时，修复有界六边形网格 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86460" target="_blank">#86460</a></span></span></li> 
  <li><span><span>修复 mvt 多边形方向 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86555" target="_blank">#86555</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F86560" target="_blank">#86560</a>）</span></span></li> 
 </ul> 
</div> 
<div> 
 <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>ILM+SLM</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <div> 
  <ul> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>修复<code>max_primary_shard_size</code>调整 factor math 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86897" target="_blank">#86897</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>迁移到数据层路由后的重新路由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86574" target="_blank">#86574</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F86572" target="_blank">#86572</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
 </div> 
 <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Infra/Core</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <div> 
  <ul> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>修复<code>assertDefaultThreadContext</code>枚举允许的 headers <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86262" target="_blank">#86262</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>转发端口 MDP 弃用信息 API <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86103" target="_blank">#86103</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>使数据目录再次与符号链接一起工作 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85878" target="_blank">#85878</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F85701" target="_blank">#85701</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>在 Fleet actions 数据流上设置自动扩展副本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85511" target="_blank">#85511</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>不要为非主系统索引自动创建别名 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85977" target="_blank">#85977</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F85072" target="_blank">#85072</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
 </div> 
 <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Ingest</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <div> 
  <ul> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>如果 geoip 系统索引被阻止，请勿下载 geoip 数据库 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86842" target="_blank">#86842</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>修复使用对象字段作为丰富策略的匹配字段时的 NPE <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86089" target="_blank">#86089</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F86058" target="_blank">#86058</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>处理<code>.geoip_databases</code>是一个别名或一个具体的索引的问题  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85792" target="_blank">#85792</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F85756" target="_blank">#85756</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
 </div> 
 <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Machine Learning</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <div> 
  <ul> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>调整<code>PyTorch</code>模型的内存开销 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86416" target="_blank">#86416</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>修复启用自动缩放时<code>_ml/info</code>报告的<code>max_model_memory_limit</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86660" target="_blank">#86660</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>提高大型集群中作业统计的可靠性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86305" target="_blank">#86305</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>使自动缩放和任务分配使用相同的 memory staleness definition <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86632" target="_blank">#86632</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F86616" target="_blank">#86616</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>修复可能导致模型边界在检测到 seasonality 后膨胀的 edge case <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Fml-cpp%2Fpull%2F2261" target="_blank">#2261</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
 </div> 
 <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Packaging</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <div> 
  <ul> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>修复忽略用户定义的堆设置的 edge case <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86438" target="_blank">#86438</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F86431" target="_blank">#86431</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
 </div> 
 <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Security</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <div> 
  <ul> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>Authentication.token 现在使用来自现有身份验证的版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F85978" target="_blank">#85978</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
 </div> 
 <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Snapshot/Restore</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <div> 
  <ul> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>对部分/完全挂载的索引的纯源快照有更好的故障处理 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86207" target="_blank">#86207</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>在 Windows 中检查可搜索快照缓存预分配是否成功 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86192" target="_blank">#86192</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F85725" target="_blank">#85725</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>在关机期间延迟可搜索的快照分配 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86153" target="_blank">#86153</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F85052" target="_blank">#85052</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>支持在未提供的情况下生成 AWS 角色会话名称 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86255" target="_blank">#86255</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
 </div> 
 <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Stats</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <div> 
  <ul> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>正确计算冻结数据层遥测的磁盘使用量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86580" target="_blank">#86580</a>（issue：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F86055" target="_blank">#86055</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
 </div> 
</div> 
<h4>Upgrades</h4> 
<div> 
 <p><strong>Packaging</strong></p> 
</div> 
<div> 
 <div> 
  <ul> 
   <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>切换到 OpenJDK 并升级到 18.0.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F86554" target="_blank">#86554</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
 </div> 
</div> 
<p> 更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F8.2%2Frelease-notes-8.2.1.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/8.2/release-notes-8.2.1.html</a></p>
                                        </div>
                                      
</div>
            