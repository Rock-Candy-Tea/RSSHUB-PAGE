
---
title: 'Elasticsearch 7.13.3 发布，修复影响所有版本的严重漏洞'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3691'
author: 开源中国
comments: false
date: Fri, 09 Jul 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3691'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 Apache 许可证下作为开源软件发布。官方客户端在 Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby 和许多其他语言中都是可用的。</p> 
<p>Elasticsearch 7.13.3 正式发布，该版本更新内容如下：</p> 
<h3>安全更新</h3> 
<ul> 
 <li>在 Elasticsearch Grok 解析器中发现一个不受控制的递归漏洞，可能导致拒绝服务攻击。有能力向 Elasticsearch 提交任意查询的用户可以创建一个恶意的 Grok 查询，使 Elasticsearch 节点崩溃。7.13.3 之前的所有 Elasticsearch 版本都受到这个缺陷的影响。用户必须升级到 Elasticsearch 7.13.3 版本才能获得修复。</li> 
</ul> 
<h3>漏洞修复</h3> 
<ul> 
 <li><strong>Autoscaling</strong> 
  <ul> 
   <li>避免不必要地扩展空层 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74086" target="_blank">#74086</a></li> 
  </ul> </li> 
 <li><strong>CompositeAggs</strong> 
  <ul> 
   <li>修复格式化纪元日期时的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F73955" target="_blank">#73955</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F68963" target="_blank">#68963</a>)</li> 
  </ul> </li> 
 <li><strong>EQL</strong> 
  <ul> 
   <li>从正在进行的序列搜索中删除“field”部分 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74824" target="_blank">#74824</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F74582" target="_blank">#74582</a>)</li> 
   <li>从不受支持的 pipe 错误消息中删除“yet” <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74850" target="_blank">#74850</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F70844" target="_blank">#70844</a>)</li> 
  </ul> </li> 
 <li><strong>Features</strong> 
  <ul> 
   <li>改进 grok 处理器中的循环引用检测</li> 
  </ul> </li> 
 <li><strong>Network</strong> 
  <ul> 
   <li>在 <code>OutboundHandler</code> 中对请求进行序列化之前增加请求 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74256" target="_blank">#74256</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F74253" target="_blank">#74253</a>)</li> 
  </ul> </li> 
 <li><strong>Recovery</strong> 
  <ul> 
   <li>回收用于基于文件恢复的缓冲区 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74117" target="_blank">#74117</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F65921" target="_blank">#65921</a>)</li> 
  </ul> </li> 
 <li><strong>SQL</strong> 
  <ul> 
   <li>修复带条件的 literal projection <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74083" target="_blank">#74083</a> (issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F64567" target="_blank">#64567</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F74064" target="_blank">#74064</a>)</li> 
   <li>修复无列索引的查询 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74312" target="_blank">#74312</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F53001" target="_blank">#53001</a>)</li> 
  </ul> </li> 
 <li><strong>Search</strong> 
  <ul> 
   <li>禁用 <code>FunctionScoreQuery</code> 和 <code>ScriptScoreQuery</code> 的查询缓存 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74060" target="_blank">#74060</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F73925" target="_blank">#73925</a>)</li> 
   <li>修复 <code>CombinedFieldQuery</code>  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74678" target="_blank">#74678</a></li> 
   <li>修复 <code>FieldCapabilitiesResponse</code> 序列化的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74504" target="_blank">#74504</a></li> 
   <li>存储异步搜索响应时使用最小版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74642" target="_blank">#74642</a></li> 
  </ul> </li> 
 <li><strong>Snapshot/Restore</strong> 
  <ul> 
   <li>正确记录缓存预热期间抛出的异常 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74419" target="_blank">#74419</a></li> 
   <li>修复快照记录不正确的最大段数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74291" target="_blank">#74291</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F74249" target="_blank">#74249</a>)</li> 
   <li>共享缓存的恢复范围应与页面大小一致 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74439" target="_blank">#74439</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F74372" target="_blank">#74372</a>)</li> 
  </ul> </li> 
 <li><strong>Transform</strong> 
  <ul> 
   <li>用 <code>_all</code> 通配符替换缺失的转换ID <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F74130" target="_blank">#74130</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F74218" target="_blank">#74218</a>)</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F7.13%2Frelease-notes-7.13.3.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/7.13/release-notes-7.13.3.html</a></p>
                                        </div>
                                      
</div>
            