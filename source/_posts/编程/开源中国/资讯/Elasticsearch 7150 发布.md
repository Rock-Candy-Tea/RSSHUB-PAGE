
---
title: 'Elasticsearch 7.15.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7627'
author: 开源中国
comments: false
date: Sat, 25 Sep 2021 07:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7627'
---

<div>   
<div class="content">
                                                                                            <p>Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 Apache 许可证下作为开源软件发布。官方客户端在 Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby 和许多其他语言中都是可用的。</p> 
<p>Elasticsearch 7.15.0 正式发布，该版本更新内容如下：</p> 
<h3>突破性变化</h3> 
<p><strong>Infra/Core</strong></p> 
<ul> 
 <li>移除 quota-aware-fs 插件</li> 
</ul> 
<p><strong>搜索</strong></p> 
<ul> 
 <li>移除 vector field（矢量场）的 xpack actions</li> 
</ul> 
<h3>弃用</h3> 
<p><strong>存储</strong></p> 
<ul> 
 <li>弃用 SimpleFS，以 NIOFS 代之</li> 
</ul> 
<h3>新功能</h3> 
<p><strong>EQL</strong></p> 
<ul> 
 <li>增加多值字段支持</li> 
 <li>向下兼容支持多值字段更新</li> 
</ul> 
<p><strong>Geo</strong></p> 
<ul> 
 <li>移除 vector tile 功能标志</li> 
</ul> 
<p><strong>Infra/Node 生命周期</strong></p> 
<ul> 
 <li>移除 Node Shutdown API 功能标志</li> 
</ul> 
<p><strong>机器学习</strong></p> 
<ul> 
 <li>在 AD 作业配置中添加 model_prune_window 字段</li> 
</ul> 
<p><strong>映射</strong></p> 
<ul> 
 <li>无符号 longs 应该与索引排序兼容</li> 
</ul> 
<h3><strong>升级</strong></h3> 
<p><strong>Ingest</strong></p> 
<ul> 
 <li>将 Tika 升级到 1.27</li> 
</ul> 
<p><strong>网络</strong></p> 
<ul> 
 <li>将 Netty 升级到 4.1.66</li> 
</ul> 
<p><strong>查询语言</strong></p> 
<ul> 
 <li>升级 ANTLR 并将其移动到 QL</li> 
</ul> 
<p><strong>快照/恢复</strong></p> 
<ul> 
 <li>将 GCS SDK 升级到 1.117.1</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F7.15%2Frelease-notes-7.15.0.html%23deprecation-7.15.0" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/7.15/release-notes-7.15.0.html#deprecation-7.15.0</a></p>
                                        </div>
                                      
</div>
            