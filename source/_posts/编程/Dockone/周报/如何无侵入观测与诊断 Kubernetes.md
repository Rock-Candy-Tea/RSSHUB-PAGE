
---
title: '如何无侵入观测与诊断 Kubernetes'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210608/958efc9cbec425829ac8221ba4007e0d.png'
author: Dockone
comments: false
date: 2021-06-08 04:41:30
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210608/958efc9cbec425829ac8221ba4007e0d.png'
---

<div>   
<br><h3>Pixie 简介</h3>Pixie 是 New Relic 开源的 Kubernetes 观测与诊断平台，它基于 eBPF，无需修改应用就可以通过 PxL 脚本对系统和应用进行诊断、观测以及调试。Pixie 未来将捐献给 CNCF，所以你可以放心使用而无需担心源码控制问题。<br>
<br>Pixie的主要特性包括：<br>
<ul><li>自动测量（Instrumentation）：得益于 Linux 内核的 eBPF，Pixie 自动收集来自各种协议（如HTTP、DNS、gRPC等）、系统指标以及网络层的应用请求，无需修改应用程序代码。</li><li>完全脚本化：Pixie 提供的 PxL 脚本可用来脚本化分析所有数据，并提供了丰富的预定义脚本以供参考。</li><li>集群内边缘计算：Pixie 所有的数据收集和处理都在 Kubernetes 集群之内，无需把海量数据发送到远端云中再进行集中处理，从而不仅省去了网络传输的开销，更可以保证数据处理的性能以及安全隔离。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210608/958efc9cbec425829ac8221ba4007e0d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210608/958efc9cbec425829ac8221ba4007e0d.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Pixie 安装部署</h3>Pixie 提供了 Helm、YAML以及CLI等多种安装部署方法，推荐使用 CLI 进行部署。其部署步骤如下：<br>
<pre class="prettyprint">bash -c "$(curl -fsSL https://withpixie.ai/install.sh)"  <br>
px auth login  <br>
px deploy<br>
</pre><br>
注意：<br>
<ul><li>第二步需要打开浏览器去 <a href="https://work.withpixie.ai/" rel="nofollow" target="_blank">https://work.withpixie.ai/</a> 注册一个账户，用作 Pixie UI 的反向代理认证使用。</li><li>由于部署过程中 px 会检查所有 Node 的 Linux 内核版本，集群中包含 Windows 节点时会部署失败。</li></ul><br>
<br>默认情况下，Pixie 的 UI 界面会通过 <a href="https://work.withpixie.ai/" rel="nofollow" target="_blank">https://work.withpixie.ai</a> 反向代理到刚部署的集群中去。如果你不想使用 Pixie 管理的反向代理，也可以将数据传输模式切换为隔离模式：<br>
<pre class="prettyprint">px get viziers  <br>
px config update -c <YOUR_CLUSTER_ID> --passthrough=false<br>
</pre><br>
<h3>Pixie 初体验</h3>打开上述的 UI 网站，选择刚才部署的集群，从预置脚本列表中选择 px/cluster，最后再点击 RUN 就可以得到整个集群的概况。如下图所示，它列出了集群中所有的 Namespace、Service、Node、Pod以及 Service Graph。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210608/af5d4d3f823b10172ab19eb34fb0c7dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210608/af5d4d3f823b10172ab19eb34fb0c7dc.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
界面中所有列出的资源都可以点击得到对应资源更具体的观测信息。比如点击 Service 列表中的 <code class="prettyprint">pl/vizier-cloud-connector</code>，就可以得到这个 Service 的请求度量以及 Pod 列表等：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210608/f64c4f7dcb6f4301d2fef1b81eea569d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210608/f64c4f7dcb6f4301d2fef1b81eea569d.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当然，上述所有 UI 中的操作也可以通过 CLI 来完成：<br>
<pre class="prettyprint"># 列出所有脚本  <br>
px run -l  <br>
# 运行 px/cluster  <br>
px run px/cluster  <br>
# 运行 px/service 并指定 service 名称  <br>
px run px/service -- -service pl/vizier-cloud-connector  <br>
# 以交互式方式运行脚本  <br>
px live px/service -- -service pl/vizier-cloud-connector<br>
</pre><br>
px run 运行的结果还会输出相同脚本在 UI 中的链接，方便用户一键切换到 UI 界面，这在数据量比较大的时候非常有用，因为通常 UI 界面的展示效果会更为直观。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210608/0a03145418667013b73fd49c80ef442e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210608/0a03145418667013b73fd49c80ef442e.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>PxL 脚本</h3>通常，Pixie 预定义的脚本可能并不能满足实际应用的观测与诊断，这时就需要编写自己的 PxL 脚本。PxL 脚本可以从已有的采集数据源中查询和过滤数据，也可以扩展采集数据源。比如，下面是一个查询过去30s 所有网络连接信息：<br>
<pre class="prettyprint"># cat conn-stats.pxl  <br>
# Import Pixie's module for querying data  <br>
import px  <br>
<br>
# Load the last 30 seconds of Pixie's `conn_stats` table into a Dataframe.  <br>
df = px.DataFrame(table='conn_stats', start_time='-30s')  <br>
<br>
# Display the DataFrame with table formatting  <br>
px.display(df)<br>
</pre><br>
然后，通过 px 命令执行这个脚本：<br>
<pre class="prettyprint">px live -f conn-stats.pxl<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210608/955f7becdd8ac2fd632b6ad65a6cc897.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210608/955f7becdd8ac2fd632b6ad65a6cc897.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
PxL 脚本的使用类似于 Python 知名数据处理库 Pandas，基本上可以说是 Pandas 的一个子集。比如，对于上述得到的网络连接统计数据，可以进一步按 Pod 和 Service 分组，然后过滤掉未定义 Service 的连接信息，得到所有 Service 和 Pod 的网络连接统计：<br>
<pre class="prettyprint"># cat service-conns.pxl  <br>
# Import Pixie's module for querying data  <br>
import px  <br>
<br>
# Load the last 30 seconds of Pixie's `conn_stats` table into a Dataframe.  <br>
df = px.DataFrame(table='conn_stats', start_time='-30s')  <br>
<br>
# Each record contains contextual information that can be accessed by the reading ctx.  <br>
df.pod = df.ctx['pod']  <br>
df.service = df.ctx['service']  <br>
<br>
# Group data by unique values in the 'pod' column and calculate the  <br>
# sum of the 'bytes_sent' and 'bytes_recv' for each unique pod grouping.  <br>
df = df.groupby(['pod', 'service']).agg(  <br>
bytes_sent=('bytes_sent', px.sum),  <br>
bytes_recv=('bytes_recv', px.sum)  <br>
)  <br>
<br>
# Force ordering of the columns (do not include _clusterID_, which is a product of the CLI and not the PxL script)  <br>
df = df[['service', 'pod', 'bytes_sent', 'bytes_recv']]  <br>
<br>
# Filter out connections that don't have their service identified.  <br>
df = df[df.service != '']  <br>
<br>
# Display the DataFrame with table formatting  <br>
px.display(df)<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210608/de66f427051d4cce1a2eed417164ef84.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210608/de66f427051d4cce1a2eed417164ef84.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
PxL 文档提供了 bpftrace、动态追踪 Go 程序、DNS 追踪、火焰图以及 Slack 告警等多个示例，更详细的使用方法请参考其官方文档 <a href="https://docs.pixielabs.ai/" rel="nofollow" target="_blank">https://docs.pixielabs.ai/</a>。<br>
<h3>总结</h3>Pixie 的出现可以说是非常惊艳。虽然 Kubernete 开源社区也已经出现了很多基于 eBPF 的观测和排错工具，但很多工具的使用都依赖于特定的条件。比如 Cilium 开源的 Hubble 工具要求集群使用 Cilium 网络插件。而 Pixie 则不依赖于任何网络插件和云平台，可以在各个公有云和本地部署中使用。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/pngrQmwuEcjk6Qfm59DWow" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/pngrQmwuEcjk6Qfm59DWow</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            