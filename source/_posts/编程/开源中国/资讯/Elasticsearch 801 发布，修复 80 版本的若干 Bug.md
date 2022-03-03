
---
title: 'Elasticsearch 8.0.1 发布，修复 8.0 版本的若干 Bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2259'
author: 开源中国
comments: false
date: Thu, 03 Mar 2022 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2259'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Elasticsearch 8.0.1 现已发布，该版本为<span> </span><a href="https://www.oschina.net/news/182013/elasticsearch-8-0-released" target="_blank">Elasticsearch 8.0</a><span> </span>的维护版本，修复了若干 Bug，具体更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug修复</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>聚合</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复与 7.17.0 的向后兼容性<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83715" target="_blank">#83715</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>分布式</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>正确处理具有 500 个或更多实例的大型区域<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83785" target="_blank">#83785</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83783" target="_blank">#83783</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>工业光模+SLM</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>不允许在解释生命周期 API 响应中出现负年龄 (negative age)<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84043" target="_blank">#84043</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>基础设施/核心</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>遇到错误的功能迁移时，始终重新运行<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83918" target="_blank">#83918</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83917" target="_blank">#83917</a>）</li> 
 <li>复制<span> </span><code>trace.id</code><span> </span>到 threadcontext stash<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83218" target="_blank">#83218</a></li> 
 <li>在<span> </span><code>ResultDeduplicator</code><span> </span>中保留上下文<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84038" target="_blank">#84038</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F84036" target="_blank">#84036</a>）</li> 
 <li>注册命名为 XContent 对象的<span> </span><code>SystemIndexMigrationTask</code><span> </span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84192" target="_blank">#84192</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F84115" target="_blank">#84115</a>）</li> 
 <li>如果<span> </span><code>_meta</code><span> </span>为空 ，则更新系统索引映射<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83896" target="_blank">#83896</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83890" target="_blank">#83890</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Ingest</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复<span> </span><code>GeoIpDownloader</code><span> </span>滚动升级期间的启动问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84000" target="_blank">#84000</a></li> 
 <li>修复首次匹配后的短路 date 模式<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83764" target="_blank">#83764</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>机器学习</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在迁移过程中重试异常检测任务恢复<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83456" target="_blank">#83456</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>监控</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将<span> </span><code>kibana_stats</code><span> </span>版本别名添加到<span> </span><code>monitoring-kibana-mb</code><span> </span>模板<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83930" target="_blank">#83930</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>打包</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加<span> </span><code>log4j-slf4j-impl</code><span> </span>到<span> </span><code>repository-azure</code><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83661" target="_blank">#83661</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83652" target="_blank">#83652</a>）</li> 
 <li><code>postinst</code><span> </span>中的密钥库升级后重启 ES<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84224" target="_blank">#84224</a> （问题 :<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F82433" target="_blank">#82433</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>恢复</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将缺失的<span> </span><code>indices.recovery.internal_action_retry_timeout</code><span> </span>添加到设置列表<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83354" target="_blank">#83354</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>SQL</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复空结果集的 txt 格式<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83376" target="_blank">#83376</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>搜索</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>避免在获取阶段急过急地加载<span> </span><code>StoredFieldsReader</code><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83693" target="_blank">#83693</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F82777" target="_blank">#82777</a>）</li> 
 <li>当没有索引匹配时，返回有效的 PIT<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83424" target="_blank">#83424</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>安全</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将 jANSI 依赖项升级到 2.4.0<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83566" target="_blank">#83566</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Snapshot/Restore</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将获取快照序列化移动到管理池<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83215" target="_blank">#83215</a></li> 
 <li><code>snapshotDeletionListeners</code><span> </span>中保留上下文<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F84089" target="_blank">#84089</a><span> </span>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F84036" target="_blank">#84036</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>转变</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复停止转换处理存储桶的条件<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82852" target="_blank">#82852</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Watcher</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>容忍 Watch 定义中的空类型数组<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83524" target="_blank">#83524</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83235" target="_blank">#83235</a>）</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>增强功能</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>基础设施/REST API</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新 YAML REST 测试，以检查所有响应中的产品标头<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83290" target="_blank">#83290</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>恢复</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>根据外部设置调整<span> </span><code>indices.recovery.max_bytes_per_sec</code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82819" target="_blank"><span> </span>#82819</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>升级</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Geo</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将矢量切片 google protobuf 更新为 3.16.1<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83402" target="_blank">#83402</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>包装</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>捆绑的 JDK 升级到 17.0.2+8<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F83243" target="_blank">#83243</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F83242" target="_blank">#83242</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F8.0%2Frelease-notes-8.0.1.html%23upgrade-8.0.1" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/8.0/release-notes-8.0.1.html#upgrade-8.0.1</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            