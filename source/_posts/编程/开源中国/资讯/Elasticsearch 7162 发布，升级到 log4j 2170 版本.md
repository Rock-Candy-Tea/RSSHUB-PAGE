
---
title: 'Elasticsearch 7.16.2 发布，升级到 log4j 2.17.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8438'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 07:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8438'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 Apache 许可证下作为开源软件发布。官方客户端在 Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby 和许多其他语言中都是可用的。</span></p> 
<p>Elasticsearch 7.16.2 发布了，升级了 log4j 版本并解决了一些小问题，完整内容如下：</p> 
<h3><strong>功能改进-Enhancements</strong></h3> 
<ul> 
 <li>将 boost 映射的弃用通知添加到 API <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81605" target="_blank">#81605</a>（<span style="color:#212529">issue：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F78396" target="_blank">#78396</a>）</li> 
 <li>改进 Docker 镜像的 cacert 脚本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81659" target="_blank">#81659</a></li> 
</ul> 
<h3><strong>Bug 修复-Bug fixes</strong></h3> 
<p><span style="color:#212529"><strong>权限-Authorization</strong></span></p> 
<ul> 
 <li><span style="color:#2e3033">为 <code>kibana_system</code> 添加 APM和 端点 ILM 策略的删除权限 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81811" target="_blank">#81811</a></li> 
</ul> 
<p><strong>基础/日志-</strong><span style="color:#212529"><strong>Infra/Logging</strong></span></p> 
<ul> 
 <li><span style="color:#2e3033">在弃用记录器（</span><span style="color:#212529">deprecation logger</span><span style="color:#2e3033">）中添加 doPrivileged 部分 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81819" target="_blank">#81819</a><span style="color:#212529"> (issue： </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F81708" target="_blank">#81708</a><span style="color:#212529">)</span></li> 
</ul> 
<p><span style="color:#2e3033"><strong>Java 高级 REST 客户端</strong></span></p> 
<ul> 
 <li>更改 HLRC <code>LifecyclePolicy</code> ，以允许所有有效的 ILM 操作 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81483" target="_blank">#81483</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F81461" target="_blank">#81461</a>）</li> 
</ul> 
<p><span style="color:#212529"><strong>机器学习-Machine Learning</strong></span></p> 
<ul> 
 <li>存在多个 unicode 脚本时，修复 <span style="color:#555555"><code>LangIdent</code> </span>模型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81876" target="_blank">#81876</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F80675" target="_blank">#80675</a>）</li> 
 <li>模型快照升级需要一个统计端点 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81641" target="_blank">#81641</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F81519" target="_blank">#81519</a>）</li> 
</ul> 
<p><strong>打包-</strong><span style="color:#212529"><strong>Packaging</strong></span></p> 
<ul> 
 <li>在默认 Docker 映像中将默认 shell 更改为 bash <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81828" target="_blank">#81828</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F80820" target="_blank">#80820</a>）</li> 
</ul> 
<h3 style="margin-left:0px"><strong>回归-Regressions</strong></h3> 
<p style="margin-left:0px"><strong>基础/脚本-</strong><span style="color:#212529"><strong>Infra/Scripting</strong></span></p> 
<ul> 
 <li>修复 Painless 中的超类功能接口解析 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81698" target="_blank">#81698</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F81696" target="_blank">#81696</a>）</li> 
</ul> 
<h3 style="margin-left:0px"><strong>升级</strong></h3> 
<p><strong>基础设施/记录-</strong><span style="color:#212529"><strong>Infra/Logging</strong></span></p> 
<ul> 
 <li>升级到 log4j 2.17.0  版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81902" target="_blank">#81902</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F7.16%2Frelease-notes-7.16.2.html%23upgrade-7.16.2" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/7.16/release-notes-7.16.2.html#upgrade-7.16.2</a></p>
                                        </div>
                                      
</div>
            