
---
title: 'Elasticsearch 7.17.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1331'
author: 开源中国
comments: false
date: Wed, 02 Mar 2022 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1331'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px"><span style="color:#333333">Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 Apache 许可证下作为开源软件发布。官方客户端在 Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby 和许多其他语言中都是可用的。</span></p> 
<p style="margin-left:0px">Elasticsearch 7.17.1 现已发布，具体更新内容如下：</p> 
<h3>功能改进</h3> 
<ul> 
 <li>弃用驼峰格式的日期信息 API <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83839" target="_blank">#83839</a></li> 
 <li>在受限名称中使用相同的系统索引模式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84180" target="_blank">#84180</a></li> 
 <li>更新 YAML REST 测试，以检查所有响应中的产品标头 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83290" target="_blank">#83290</a></li> 
 <li>根据外部设置调整 <code>indices.recovery.max_bytes_per_sec</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82819" target="_blank">#82819</a></li> 
 <li>弃用 API 中的 Surface 脚本弃用警告 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84040" target="_blank">#84040</a><span style="color:#212529"> (issue: </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F82936" target="_blank">#82936</a><span style="color:#212529">)</span></li> 
</ul> 
<h3 style="margin-left:0px"><strong>Bug fixes</strong></h3> 
<ul> 
 <li>向后兼容版本 7.17.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83715" target="_blank">#83715</a>（<span style="color:#212529">issue</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83339" target="_blank">#83339</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83533" target="_blank">#83533</a>）</li> 
 <li>修复数据流的自动缩放 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83302" target="_blank">#83302</a><span style="color:#212529"> (issue: </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F82857" target="_blank">#82857</a><span style="color:#212529">)</span></li> 
 <li><span style="color:#212529">正确处理具有 500 个或更多实例的大型 GCE 区域 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83785" target="_blank">#83785</a><span style="color:#212529"> (issue: </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83783" target="_blank">#83783</a><span style="color:#212529">) </span></li> 
 <li>如果它无法计算签名区域，则 <code>GeometryNormalizer</code> 不应失败 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84051" target="_blank">#84051</a>（<span style="color:#212529">issue</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83946" target="_blank">#83946</a>）</li> 
 <li>不允许 ILM 中的负年龄解释 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84043" target="_blank">#84043</a></li> 
 <li>...</li> 
</ul> 
<h3>升级</h3> 
<ul> 
 <li>将矢量切片 google protobuf 更新为 3.16.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83402" target="_blank">#83402</a></li> 
 <li>捆绑的 JDK 升级到 17.0.2+8 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83243" target="_blank">#83243</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83242" target="_blank">#83242</a>）</li> 
 <li>...</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F7.17%2Frelease-notes-7.17.1.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/7.17/release-notes-7.17.1.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            