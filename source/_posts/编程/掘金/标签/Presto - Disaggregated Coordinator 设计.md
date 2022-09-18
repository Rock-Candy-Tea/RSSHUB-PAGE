
---
title: 'Presto - Disaggregated Coordinator 设计'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://cors.zfour.workers.dev/?http://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54a0bb1a719b4ba6afe0188306e02efd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 18:51:20 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54a0bb1a719b4ba6afe0188306e02efd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Some Takeaways：</p>
<ol>
<li>
<p>Presto 受人诟病的单 Coordinator 架构，在 266 版本之后有了改善，引入了为高可用而设计的分离式 Coordinator 设计。单 Coordinator 架构的问题主要有：</p>
<ol>
<li>
<p>复杂、多阶段查询占用 Coordinator 资源的问题，只能依赖垂直扩展来提升 Coordinator 的能力</p>
</li>
<li>
<p>单 Coordinator 存在单点故障风险</p>
</li>
</ol>
</li>
<li>
<p>通过引入一个新的组件 - ResourceManager 使得 Coordinator 和 Worker 一样，具备水平扩展能力。ResourceManager 采用多主架构（Multi-Master）运行</p>
</li>
<li>
<p>ResourceManager 本身也有多个实例（以保证高可用），用来收集 Coordinator 以及 Worker 的数据，反映出集群的全貌，并提供资源管理相关的数据，同时 ResourceManager 并非在查询的关键路径上；ResourceManager 节点也会运行一个嵌入的服务发现功能</p>
</li>
<li>
<p>原来由 Coordinator 承担的一些资源管理类型的任务，如可用 Worker 资源的评估、资源组的管理都解耦到 ResourceManager 中</p>
</li>
</ol>
<hr>
<p><strong>Meta</strong>** **: Swapnil Tailor, Tim Meehan, Vaishnavi Batni, Abhisek Saikia, Neerad Somanchi</p>
<h2 data-id="heading-0">Overview</h2>
<p>Presto's architecture originally only supported a single coordinator and a pool of workers. This has worked well for many years but created some challenges.</p>
<ul>
<li>
<p>With a single coordinator, the cluster can scale up to a certain number of workers reliably. A large worker pool running complex, multi-stage queries can overwhelm an inadequately provisioned coordinator, requiring upgraded hardware to support the increase in worker load.</p>
</li>
<li>
<p>A single coordinator is a single point of failure for the Presto cluster.</p>
</li>
</ul>
<p>To overcome these challenges, we came up with a new design with a disaggregated coordinator that allows the coordinator to be horizontally scaled out across a single pool of workers.</p>
<h2 data-id="heading-1">Architecture</h2>
<div data-type="transform-warn" data-index="16"> 
<p><img src="https://cors.zfour.workers.dev/?http://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54a0bb1a719b4ba6afe0188306e02efd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>A disaggregated coordinator setup supports a pool of coordinators with the help of a new component, the resource manager.</p>
<h4 data-id="heading-2">Resource Manager</h4>
<p>The resource manager aggregates data from all coordinators and workers, and constructs a global view of the cluster. Clusters support multiple resource managers, each acting as a primary. The discovery service runs on each resource manager. The resource manager is not in the critical path for the query. Rather, it is a complementary process that can survive momentary unavailability.</p>
<h4 data-id="heading-3">Coordinator</h4>
<p>The coordinator sends heartbeats at regular intervals to all the resource managers. These heartbeats contain information about the queries handled by the coordinator, which the resource managers use to refresh their global view of the cluster. The coordinator fetches aggregated resource group information periodically from the resource manager.</p>
<h4 data-id="heading-4">Worker</h4>
<p>Each worker sends regular heartbeats with memory and cpu utilization to the resource managers. The resource managers track these metrics for the worker pool.</p>
<h2 data-id="heading-5">Query Execution Flow</h2>
<div data-type="transform-warn" data-index="27"> 
<p><img src="https://cors.zfour.workers.dev/?http://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15df9372f0564604b7e1d57dd2534418~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>With the introduction of a resource manager, the query execution flow looks slightly different.</p>
<ul>
<li>
<p>A query is submitted to one of the coordinators in the cluster.</p>
</li>
<li>
<p>The coordinator prepares the query for execution by parsing, analyzing and assigning it to a given resource group.</p>
</li>
<li>
<p>A heartbeat is sent to each resource manager when the query is created by the coordinator.</p>
</li>
<li>
<p>The coordinator polls the resource manager at regular intervals to fetch cluster level resource group information.</p>
</li>
<li>
<p>The coordinator polls the resource manager to get active worker information. This information is used for query scheduling.</p>
</li>
<li>
<p>The rest of the query execution remains the same.</p>
</li>
</ul>
<h2 data-id="heading-6">Memory Management</h2>
<div data-type="transform-warn" data-index="38"> 
<p><img src="https://cors.zfour.workers.dev/?http://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c687d4b842b4763bc6adbffc361d490~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>The resource manager needs up to date information about memory and cpu utilization of the worker pool for resource group queuing. Currently, this information is periodically collected by the coordinator. In the disaggregated coordinator setup, resource managers receive query-level statistics from coordinator heartbeats, and memory pool information from worker heartbeats. This information is periodically polled by the coordinator to help make local decisions (i.e. queue/run a query, kill a query when the cluster is low on memory).</p>
<h2 data-id="heading-7">Resource Management</h2>
<div data-type="transform-warn" data-index="43"> 
<p><img src="https://cors.zfour.workers.dev/?http://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/064b0f93ea054f698f5eeacc70301418~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>The resource managers runs in multi-master mode. To support that, coordinators post query updates to all resource managers. The resource manager aggregates this information. The coordinator polls a resource manager to fetch up to date information about resource group usage in the cluster.</p>
<h2 data-id="heading-8">Resource Group Consistency Model</h2>
<p>Resource groups in a disaggregated coordinator setup are eventually consistent. While this may lead to over-admission in certain scenarios, in practice this is mitigated by gating the resource group to only allow queries to run when certain freshness guarantees have been met (as opposed to the previous logic of checking every millisecond). This may mean if the cluster’s resource managers are down, then queries may be queued in the coordinator’s resource groups. This is to ensure coordinators don’t over-admit queries in the face of resource manager unavailability.</p>
<p>More details about flags can be found here which can help tune the cluster’s resource groups to the desired consistency.</p>
<h2 data-id="heading-9">Discovery Service</h2>
<div data-type="transform-warn" data-index="51"> 
<p><img src="https://cors.zfour.workers.dev/?http://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0f74ec775d7450cac4a720ea35477ba~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>An embedded version of the discovery server runs on resource managers in distributed mode. Discovery servers stay in sync by passing updates they receive to other discovery servers in the cluster.</p>
<h2 data-id="heading-10">Configuration</h2>
<p>Minimal configuration to enable a disaggregated coordinator cluster can be found in here .</p>
<p>No changes needed in jvm.config and node.properties .</p>
<p>Recommended release version to use disaggregated coordinator in production: 0.266</p>
<p>There were lightning talks about the Disaggregated Coordinator at past PrestoCons. Videos and slides can be accessed using the following links:</p>
<ol>
<li>
<p>Lightning Talk in 2020 Prestocon: video</p>
</li>
<li>
<p>Lightning Talk in 2021 PrestoCon about Production Rollout: video and slides</p>
</li>
</ol></div>  
</div>
            