
---
title: 'Thanos v0.24.0 发布，大规模 Prometheus 集群解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5153'
author: 开源中国
comments: false
date: Thu, 30 Dec 2021 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5153'
---

<div>   
<div class="content">
                                                                                            <p>Thanos v0.24.0 现已发布。<span style="background-color:#ffffff; color:#333333">Thanos 是一组可以组成具有长期存储期限的高可用指标系统的组件，可以将其无缝添加到现有 Prometheus 部署之上。Thanos 利用 Prometheus 2.0 存储格式在任何对象存储中经济高效地存储历史指标数据，同时保留快速查询可能。另外，它提供了所有 Prometheus 的全局查询视图，并且可以即时合并 Prometheus HA 对中的数据。</span></p> 
<p>具体更新内容如下：</p> 
<p style="text-align:start"><strong>Added</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4228" target="_blank">#4228</a> Tools thanos bucket inspect：添加 flag<code>--output</code>以提供输出方法（table、csv、tsv）。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4636" target="_blank">#4636</a> Azure：支持使用用户分配的管理身份进行认证</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4680" target="_blank">#4680</a> Query：添加<code>exemplar.partial-response</code>flag 以控制部分响应。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4679" target="_blank">#4679</a> Query：添加<code>enable-feature</code>flag 以启用负偏移和<code>@</code>修饰符，类似于 Prometheus。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4696" target="_blank">#4696</a> Query：将缓存名称添加到 tracing spans。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4710" target="_blank">#4710</a> Store：添加 metric 以捕获最后加载的块的时间戳。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4736" target="_blank">#4736</a> S3：添加使用自定义 AWS STS 端点的功能。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4764" target="_blank">#4764</a> Compact：添加<code>block-viewer.global.sync-block-timeout</code>flag 以设置 synchronization block metas 的超时。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4801" target="_blank">#4801</a> Compact：添加 Prometheus 指标以跟踪压缩和下采样的进度。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4444" target="_blank">#4444</a> UI：向 Block UI 添加标记删除和 no compaction 功能。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4576" target="_blank">#4576</a> UI：将 filter compaction level 添加到 Block UI。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4731" target="_blank">#4731</a> Rule：向 ruler 添加 stateless mode。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4612" target="_blank">#4612</a> Sidecar：添加 --prometheus.http-client 和 --prometheus.http-client-file flag，以便 sidecar 通过基本认证或 TLS 连接到 Prometheus。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4848" target="_blank">#4848</a> Compactor：添加了 Prometheus 指标以跟踪保留进度。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4856" target="_blank">#4856</a> Mixin：将 Query Frontend 添加到 Grafana 仪表板。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4868" target="_blank">#4868</a> Rule：支持 Prometheus v2.31.0 引入的规则组限制。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4897" target="_blank">#4897</a> Query：添加对查询器地址标志的验证。</li> 
</ul> 
<p style="text-align:start"><strong>Fixed</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4508" target="_blank">#4508</a> Sidecar，Mixin：重命名<code>ThanosSidecarUnhealthy</code>为<code>ThanosSidecarNoConnectionToStartedPrometheus</code>；删除<code>ThanosSidecarPrometheusDown</code>警报；删除未使用的<code>thanos_sidecar_last_heartbeat_success_time_seconds</code>指标。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4663" target="_blank">#4663</a> Fetcher：修复发现的 data races。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4754" target="_blank">#4754</a> Query：修复 stores endpoint 上可能出现的 panic。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4753" target="_blank">#4753</a> Store：验证块同步并发参数。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4779" target="_blank">#4779</a> Examples：修复 MacOS 用户的交互式测试。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4792" target="_blank">#4792</a> Store：修复 BucketedBytes 池中的 data race。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4769" target="_blank">#4769</a> Query Frontend：添加“X-Request-ID”字段和其他字段以启动 call log。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4709" target="_blank">#4709</a> Store：修复应用程序停止时的 panic。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4777" target="_blank">#4777</a> Query：修复 exemplars server 中的 data race。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4811" target="_blank">#4811</a> Query：修复 metadata、rules 和 targets servers 中的 data race。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4795" target="_blank">#4795</a> Query：修复 endpointset 中的死锁。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4928" target="_blank">#4928</a> Azure：只创建一次 http 客户端，以节省内存。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4962" target="_blank">#4962</a> Compact/downsample：如果某些块积压发生错误，则修复死锁；修复了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4430" target="_blank">这个拉取请求</a>。受影响的版本是 0.22.0 - 0.23.1。</li> 
</ul> 
<p style="text-align:start"><strong>Changed</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4864" target="_blank">#4864</a> UI：删除旧的 PromQL 编辑器。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4708" target="_blank">#4708</a> Receive：删除 gRPC 消息大小限制，修复了接收方在 hashring 中转发消息时常见的错误。</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Freleases%2Ftag%2Fv0.24.0" target="_blank">https://github.com/thanos-io/thanos/releases/tag/v0.24.0</a></p>
                                        </div>
                                      
</div>
            