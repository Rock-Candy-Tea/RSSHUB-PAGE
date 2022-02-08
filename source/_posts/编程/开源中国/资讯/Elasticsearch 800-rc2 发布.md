
---
title: 'Elasticsearch 8.0.0-rc2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5697'
author: 开源中国
comments: false
date: Tue, 08 Feb 2022 07:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5697'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Freleases%2Ftag%2Fv8.0.0-rc2" target="_blank">Elasticsearch 8.0.0-rc2 已发布</a>。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">新特性</h3> 
<div style="text-align:left"> 
 <p><strong>Snapshot/Restore</strong></p> 
 <div> 
  <ul> 
   <li>支持 Kubernetes 服务帐户的 IAM 角色<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81255" target="_blank">#81255</a><span> </span>(issue:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F52625" target="_blank">#52625</a>)</li> 
  </ul> 
 </div> 
 <p><strong>Watcher</strong></p> 
 <div> 
  <ul> 
   <li>对 Watcher 历史模板名称使用<code>startsWith</code>而不是完全匹配<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82396" target="_blank">#82396</a></li> 
  </ul> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">功能增强</h3> 
<div style="text-align:left"> 
 <p><strong>Cluster Coordination</strong></p> 
 <div> 
  <ul> 
   <li>减少<code>TaskBatcher</code>的 lock-heavy<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82227" target="_blank">#82227</a><span> </span>(issue:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F77466" target="_blank">#77466</a>)</li> 
  </ul> 
 </div> 
 <p><strong>ILM+SLM</strong></p> 
 <div> 
  <ul> 
   <li>避免不必要的<code>LifecycleExecutionState</code><span>重新计算</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81558" target="_blank">#81558</a><span> </span>(issues:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F77466" target="_blank">#77466</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F79692" target="_blank">#79692</a>)</li> 
   <li>将未更改的 ILM 策略更新为无操作<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82240" target="_blank">#82240</a><span> </span>(issue:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F82065" target="_blank">#82065</a>)</li> 
  </ul> 
 </div> 
 <p><strong>Infra/Core</strong></p> 
 <div> 
  <ul> 
   <li>阻止在未升级到 7.x 而先升级到 8.0 的情况<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82321" target="_blank">#82321</a><span> </span>(issue:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F81865" target="_blank">#81865</a>)</li> 
  </ul> 
 </div> 
 <p><strong>Machine Learning</strong></p> 
 <div> 
  <ul> 
   <li>将<code>deployment_stats</code><span>添加到训练模型统计信息</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F80531" target="_blank">#80531</a></li> 
   <li><code>use_auto_machine_memory_percent</code><span>设置项</span>现在的默认值为<code>max_model_memory_limit</code><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F80532" target="_blank">#80532</a><span> </span>(issue:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F80415" target="_blank">#80415</a>)</li> 
  </ul> 
 </div> 
 <p><strong>Network</strong></p> 
 <div> 
  <ul> 
   <li>改进缓慢的 inbound 处理，引入响应类型<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F80425" target="_blank">#80425</a></li> 
  </ul> 
 </div> 
 <p><strong>Search</strong></p> 
 <div> 
  <ul> 
   <li>在 kNN 搜索中检查嵌套字段<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F80516" target="_blank">#80516</a><span> </span>(issue:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F78473" target="_blank">#78473</a>)</li> 
  </ul> 
 </div> 
</div> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F8.0%2Frelease-notes-8.0.0-rc2.html" target="_blank">详情查看 release notes</a>。</p>
                                        </div>
                                      
</div>
            