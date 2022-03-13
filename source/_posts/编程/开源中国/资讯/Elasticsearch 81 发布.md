
---
title: 'Elasticsearch 8.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2252'
author: 开源中国
comments: false
date: Sun, 13 Mar 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2252'
---

<div>   
<div class="content">
                                                                                            <p>Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 SSPL + Elastic License 双重授权许可下作为开源软件发布。</p> 
<p>Elasticsearch 8.1 正式发布，该版本更新内容如下：</p> 
<h3>已知问题</h3> 
<p>在 8.1 中，当 <code>xpack.security.audit.logfile.events.emit_request_body</code> 集群设置为 <code>true</code> 时，一个错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F84784" target="_blank">#84784</a>）会导致使用过滤字段的 API 返回一个带有 <code>401</code> HTTP 状态码的 <code>null_pointer_exception</code> 错误。</p> 
<h3>重要变化</h3> 
<p>Geo</p> 
<ul> 
 <li>Fields API 应返回规范化的几何图形 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F80649" target="_blank">#80649</a> (issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F79232" target="_blank">#79232</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F63739" target="_blank">#63739</a>)</li> 
</ul> 
<h3>错误修复</h3> 
<p>Aggregations</p> 
<ul> 
 <li>重新启用 <code>BooleanTermsIT</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83421" target="_blank">#83421</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83351" target="_blank">#83351</a>)</li> 
 <li>向后兼容 7.17.0 版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83715" target="_blank">#83715</a></li> 
 <li>将浮点数和半浮点数减少到其存储的精度 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83213" target="_blank">#83213</a></li> 
</ul> 
<p>Allocation</p> 
<ul> 
 <li>修复 <code>updateMinNode</code> 条件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F80403" target="_blank">#80403</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F41194" target="_blank">#41194</a>)</li> 
 <li>使 <code>*.routing.allocation.*</code> 成为基于列表的设置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F80420" target="_blank">#80420</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F77773" target="_blank">#77773</a>)</li> 
 <li>允许在 flood-stage-blocked 索引上进行元数据更新 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81781" target="_blank">#81781</a></li> 
 <li>集群恢复后重新路由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82856" target="_blank">#82856</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F82456" target="_blank">#82456</a>)</li> 
</ul> 
<p>Authorization</p> 
<ul> 
 <li>创建 API 密钥时捕获匿名角色 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81427" target="_blank">#81427</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F81024" target="_blank">#81024</a>)</li> 
 <li>扩展 fleet-server 服务账户的权限 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82600" target="_blank">#82600</a></li> 
</ul> 
<p>Distributed</p> 
<ul> 
 <li>[GCE Discovery] 正确处理具有 500 个或更多实例的大型区域 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83785" target="_blank">#83785</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83783" target="_blank">#83783</a>)</li> 
</ul> 
<p>Engine</p> 
<ul> 
 <li>当分片失败时分叉到 <code>WRITE</code> 线程 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84606" target="_blank">#84606</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F84602" target="_blank">#84602</a>)</li> 
</ul> 
<p>ILM+SLM</p> 
<ul> 
 <li>修复 <code>PolicyStepsRegistry</code> 的 <code>cachedSteps</code> null 处理 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84588" target="_blank">#84588</a></li> 
</ul> 
<p>……</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F8.1%2Frelease-notes-8.1.0.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/8.1/release-notes-8.1.0.html</a></p>
                                        </div>
                                      
</div>
            