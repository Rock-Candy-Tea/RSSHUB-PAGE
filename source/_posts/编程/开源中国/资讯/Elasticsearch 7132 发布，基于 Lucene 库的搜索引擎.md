
---
title: 'Elasticsearch 7.13.2 发布，基于 Lucene 库的搜索引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5385'
author: 开源中国
comments: false
date: Mon, 14 Jun 2021 23:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5385'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 Apache 许可证下作为开源软件发布。官方客户端在 Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby 和许多其他语言中都是可用的。</p> 
<p>Elasticsearch 7.13.2 正式发布，该版本部分更新内容如下：</p> 
<h3>错误修复</h3> 
<p>聚合</p> 
<ul> 
 <li>增加禁用 aggs 优化的设置</li> 
</ul> 
<p>集群协调</p> 
<ul> 
 <li>在所有故障中完全写入下一个集群状态</li> 
</ul> 
<p>特性/ILM+SLM</p> 
<ul> 
 <li>总是处理不完整的 AsyncActionStep 执行</li> 
 <li>在 CopyExecutionStateStep 中复制所有执行状态</li> 
</ul> 
<p>特性</p> 
<ul> 
 <li>当 ECS 被禁用时，保留来自用户代理处理器的字段映射</li> 
</ul> 
<p>Infra/Core</p> 
<ul> 
 <li>重置功能时解析具体关联索引</li> 
</ul> 
<p>搜索</p> 
<ul> 
 <li>修复获取父级 ID 连接字段值时的错误</li> 
</ul> 
<p>快照/还原</p> 
<ul> 
 <li>在分配时修复 repo 名称</li> 
</ul> 
<p>监控</p> 
<ul> 
 <li>增加 monitoring_user 角色从 metricbeat-* 读取的能力</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F7.13%2Frelease-notes-7.13.2.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/7.13/release-notes-7.13.2.html</a></p>
                                        </div>
                                      
</div>
            