
---
title: 'Elasticsearch 8 发布，兼容 7.x API、新的 KNN 搜索 API'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0211/152931_bbF7_4937141.png'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 15:02:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0211/152931_bbF7_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 Apache 许可证下作为开源软件发布。官方客户端在 Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby 和许多其他语言中都是可用的。</p> 
<p><img height="409" src="https://static.oschina.net/uploads/space/2022/0211/152931_bbF7_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>时隔近三年，Elasticsearch 8 正式发布，新增的功能包括：</p> 
<h3>7.x REST API 兼容性</h3> 
<p>8.0 为 Elasticsearch REST APIs 引入了一些重大的变化。虽然更新你的应用程序以适应这些变化十分重要，但在升级后寻找和更新每一个 API 调用可能对开发者而言十分痛苦且容易出错。为了使这个过程变得更加容易，Elasticsearch 已经在 REST API 中增加了对 7.x 兼容性 header 的支持。这些可选的 header 文件让你向 8.0 集群发出 7.x 兼容的请求，并收到 7.x 兼容的响应。</p> 
<p>虽然官方仍然建议开发者更新你的应用程序以使用原生的 8.0 请求和响应，但 7.x API 兼容 header 文件让你可以在更长的时间内安全地进行这些更改。</p> 
<h3>安全功能在默认情况下被启用和配置</h3> 
<p>在没有安全保障的情况下运行 Elasticsearch 会让你的集群暴露在任何可以向 Elasticsearch 发送请求的用户面前。在以前的版本中，你必须明确地启用 Elasticsearch 的安全功能，如认证、授权和网络加密（TLS）。从 Elasticsearch 8.0 开始，当第一次启动 Elasticsearch 时，安全功能被默认启用和配置。</p> 
<p>在启动时，Elasticsearch 8.0 会生成注册令牌，你可以用它来连接 Kibana 实例或在安全的 Elasticsearch 集群中注册其他节点，而无需生成安全证书或更新 YAML 配置文件。只需在启动新节点或 Kibana 实例时使用生成的注册令牌，Elastic Stack 就会为你处理所有安全配置。</p> 
<p><strong>已知问题：</strong></p> 
<ul> 
 <li>如果你在 Linux ARM 或 macOS M1 等 arch64 平台上从归档中安装 Elasticsearch，那么在首次启动节点时，不会自动生成 <code>elastic</code> 用户密码和 Kibana 注册令牌。节点启动后，需要用 <code>bin/elasticsearch-reset-password</code> 工具生成 <code>elastic</code> 密码：</li> 
</ul> 
<pre><code>bin/elasticsearch-reset-password -u elastic
</code></pre> 
<ul> 
 <li>然后，用 <span style="background-color:rgba(135,131,120,0.15)">bin/elasticsearch-create-enrollment-token</span> 工具为 Kibana 创建一个注册令牌： </li> 
</ul> 
<pre><code>bin/elasticsearch-create-enrollment-token -s kibana</code></pre> 
<h3>更好地保护系统索引</h3> 
<p>系统索引为 Elastic 功能存储配置和内部数据。一般来说，系统索引仅保留供这些功能内部使用。虽然有可能，但直接访问或改变系统索引会导致不稳定和其他问题。</p> 
<p>在 Elasticsearch 8.0 中做了一些改变来保护系统索引不被直接访问。要访问系统索引的话，用户现在必须把 <code>allow_restricted_indices</code> 权限设置为 <code>true</code>。</p> 
<p><code>superuser</code> 角色也不再给予系统索引的写入权限。因此，内置的 <code>elastic</code> superuser 默认不能改变系统索引。</p> 
<p>此后，开发者应使用 Kibana 或相关的 Elasticsearch APIs 来管理某个功能的数据，而不是访问系统索引。如果你直接访问系统索引，Elasticsearch 将在 API 响应的 header 中和废弃日志中返回警告。</p> 
<h3>新的 KNN 搜索 API</h3> 
<p>Elasticsearch 8.0 中推出了 KNN 搜索 API 的技术预览版。通过使用 <code>dense_vector</code> 字段，k-nearest neighbor（KNN）搜索可以找到与查询向量最近的 k 个向量（这是由相似度指标来衡量的）。KNN 通常被用来支持推荐引擎和基于自然语言处理（NLP）算法的相关性排名。</p> 
<p>以前，Elasticsearch 只支持精确的 KNN 搜索，使用带向量函数的 <code>script_score</code> 查询。虽然这种方法保证了准确的结果，但它往往导致搜索速度缓慢，而且在大型数据集上不能很好地扩展。作为对较慢的索引和不完美的准确性的交换，新的 KNN 搜索 API 让你在更大的数据集上以更快的速度运行近似的 KNN 搜索。</p> 
<h3>为 <code>keyword</code>、 <code>match_only_text</code> 和 <code>text</code> 字段节省存储空间</h3> 
<p>该版本更新了倒排索引，这是一个内部数据结构，可以使用更节省空间的编码。这一变化将使 <code>keyword</code>、 <code>match_only_text</code> 字段以及 <code>text</code> 字段受益。在使用应用程序日志的基准测试中，这一转变为 <code>message</code> 字段（映射为 <code>match_only_text</code>）的索引大小减少了 14.4%，总体上减少了 3.5% 的磁盘占用空间。</p> 
<h3>加快 <code>geo_point</code>、<code>geo_shape</code> 和范围字段索引速度</h3> 
<p>新版本优化了多维点（multi-dimensional points）的索引速度，多维点是用于 <code>geo_point</code>、<code>geo_shape</code> 和范围字段的内部数据结构。Lucene 级别的基准测试显示，这些字段类型的索引速度提高了 10-15%。主要由这些字段组成的 Elasticsearch 索引和数据流可能会在索引速度方面有显著的改进。</p> 
<h3>PyTorch 模型支持自然语言处理（NLP）</h3> 
<p>现在可以上传在 Elasticsearch 之外训练的 PyTorch 模型，并使用它们进行推理。第三方模型支持为 Elastic Stack 带来了现代自然语言处理（NLP）和搜索用例。</p> 
<h3>其他变化</h3> 
<p>Aggregations：</p> 
<ul> 
 <li>删除邻接 matrix 设置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F46327" target="_blank">#46327</a> (issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F46257" target="_blank">#46257</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F46324" target="_blank">#46324</a>)</li> 
 <li>删除 <code>MovingAverage</code> 管道聚合 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F39328" target="_blank">#39328</a></li> 
 <li>删除弃用的 <code>_time</code> 和 <code>_term</code> 排序 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F39450" target="_blank">#39450</a></li> 
 <li>删除弃用的日期历史间隔 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F75000" target="_blank">#75000</a></li> 
</ul> 
<p>Allocation：</p> 
<ul> 
 <li>删除<code>include_relocations</code>设置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F47717" target="_blank">#47717</a> (issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F46079" target="_blank">#46079</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F47443" target="_blank">#47443</a>)</li> 
</ul> 
<p>Analysis：</p> 
<ul> 
 <li>清理分析中的版本化弃用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F41560" target="_blank">#41560</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F41164" target="_blank">#41164</a>)</li> 
 <li>删除预先配置的 <code>delimited_payload_filter</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F43686" target="_blank">#43686</a> (issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F41560" target="_blank">#41560</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F43684" target="_blank">#43684</a>)</li> 
</ul> 
<p>Authentication：</p> 
<ul> 
 <li>除非明确禁用，否则始终添加文件和本机 Realm <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F69096" target="_blank">#69096</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F50892" target="_blank">#50892</a>)</li> 
 <li>默认情况下不要在 Policy 中设置 NameID 格式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F44090" target="_blank">#44090</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F40353" target="_blank">#40353</a>)</li> 
 <li>为 Realm 配置强制设置顺序 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F51195" target="_blank">#51195</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F37614" target="_blank">#37614</a>)</li> 
</ul> 
<p>Cluster Coordination：</p> 
<ul> 
 <li>删除连接超时 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F60873" target="_blank">#60873</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F60872" target="_blank">#60872</a>)</li> 
 <li>删除对延迟状态恢复挂起主控器的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F53845" target="_blank">#53845</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F51806" target="_blank">#51806</a>)</li> 
</ul> 
<p>Distributed：</p> 
<ul> 
 <li>删除同步刷新 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F50882" target="_blank">#50882</a> (issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F50776" target="_blank">#50776</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F50835" target="_blank">#50835</a>)</li> 
 <li>删除 <code>cluster.remote.connect</code>设置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F54175" target="_blank">#54175</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F53924" target="_blank">#53924</a>)</li> 
</ul> 
<p>Engine：</p> 
<ul> 
 <li>强制合并应该拒绝设置了<code>only_expunge_deletes</code>和<code>max_num_segments</code>的请求 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F44761" target="_blank">#44761</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F43102" target="_blank">#43102</a>)</li> 
 <li>删除每个类型的索引统计 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F47203" target="_blank">#47203</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F41059" target="_blank">#41059</a>)</li> 
 <li>移除 translog 保留设置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F51697" target="_blank">#51697</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F50775" target="_blank">#50775</a>)</li> 
</ul> 
<p>Features/CAT APIs：</p> 
<ul> 
 <li>为 <code>_cat/indices</code> 删除废弃的 <code>local</code> 参数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F64868" target="_blank">#64868</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F62198" target="_blank">#62198</a>)</li> 
 <li>为 <code>_cat/shards</code> 删除废弃的 <code>local</code> 参数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F64867" target="_blank">#64867</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F62197" target="_blank">#62197</a>)</li> 
</ul> 
<p>Features/ILM+SLM：</p> 
<ul> 
 <li>默认<code>cluster.routing.allocation.enforce_default_tier_preference</code>为<code>true</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F79275" target="_blank">#79275</a> (issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F76147" target="_blank">#76147</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F79210" target="_blank">#79210</a>)</li> 
</ul> 
<p>Features/Indices APIs</p> 
<ul> 
 <li>将<code>prefer_v2_templates</code>参数默认值设为 <code>true</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F55489" target="_blank">#55489</a> (issues: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F53101" target="_blank">#53101</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F55411" target="_blank">#55411</a>)</li> 
 <li>删除弃用的<code>_upgrade</code> API <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F64732" target="_blank">#64732</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F21337" target="_blank">#21337</a>)</li> 
 <li>从 REST 层移除参数 <code>include_type_name</code></li> 
 <li>删除索引模板中的<code>template</code>字段 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F49460" target="_blank">#49460</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F21009" target="_blank">#21009</a>)</li> 
</ul> 
<p>Infra/Core</p> 
<ul> 
 <li>从数据路径中删除<code>nodes/0</code>文件夹前缀</li> 
 <li>删除<code>bootstrap.system_call_filter</code>设置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F72848" target="_blank">#72848</a></li> 
 <li>删除<code>node.max_local_storage_nodes</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F42428" target="_blank">#42428</a> (issue: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F42426" target="_blank">#42426</a>)</li> 
 <li>删除 Joda 依赖 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftranslate.google.com%2Fwebsite%3Fsl%3Dauto%26tl%3Dzh-CN%26u%3Dhttps%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F79007" target="_blank">#79007</a></li> 
 <li>删除命名日期/时间格式的驼峰式大小写 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftranslate.google.com%2Fwebsite%3Fsl%3Dauto%26tl%3Dzh-CN%26u%3Dhttps%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F60044" target="_blank">#60044</a></li> 
 <li>……</li> 
</ul> 
<p>Packaging</p> 
<ul> 
 <li>删除 SysV 初始化支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftranslate.google.com%2Fwebsite%3Fsl%3Dauto%26tl%3Dzh-CN%26u%3Dhttps%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F51716" target="_blank">#51716</a></li> 
 <li>删除对<code>JAVA_HOME</code> 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftranslate.google.com%2Fwebsite%3Fsl%3Dauto%26tl%3Dzh-CN%26u%3Dhttps%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F69149" target="_blank">#69149</a></li> 
 <li>需要 Java 17 才能运行 Elasticsearch <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftranslate.google.com%2Fwebsite%3Fsl%3Dauto%26tl%3Dzh-CN%26u%3Dhttps%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F79873" target="_blank">#79873</a></li> 
</ul> 
<p>……</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fcn%2Fblog%2Fwhats-new-elastic-8-0-0" target="_blank">https://www.elastic.co/cn/blog/whats-new-elastic-8-0-0</a></p>
                                        </div>
                                      
</div>
            