
---
title: '重磅｜Apache ShardingSphere 5.0.0 即将正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic2.zhimg.com/v2-d724034a9145ae1db3d745cee7d0c10d_b.jpg'
author: 开源中国
comments: false
date: Wed, 10 Nov 2021 16:40:00 GMT
thumbnail: 'https://pic2.zhimg.com/v2-d724034a9145ae1db3d745cee7d0c10d_b.jpg'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <div>
  <span><span>Apache ShardingSphere 5.0.0 GA 版在经历 5.0.0-alpha 及 5.0.0-beta 接近两年时间的研发和打磨，终于将在 11 月份与大家正式见面！</span></span>
 </div> 
</blockquote> 
<div style="text-align:left"> 
 <div>
  <span><span>11 月 10 日是 Apache ShardingSphere 进入 Apache 基金会的三周年纪念日。在这特殊的一天，ShardingSphere 的核心 Team 也响应社区的呼唤，</span></span>
  <span> </span>
  <strong><span>将 5.0.0 GA 版作为三周年纪念日的礼物呈现给社区及整个分布式数据库和安全生态领域。</span></strong>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  <span><span>自 5.0.0 系列研发伊始，ShardingSphere 就逐渐脱离简单的分布式数据库中间件解决方案的行业定位。取而代之的是，</span></span>
  <span> </span>
  <strong><span>Database Plus 理念将成为 5.0.0 及今后版本的新定位及新航标。通过重新塑造分布式可插拔体系，连通用户实际落地场景，为社区及整个数据库行业带来新风向及更有价值的解决方案。</span></strong>
  <span> </span>
  <span><span>5.0.0 GA 版将成为这一理念的首个实践版本，集成整个 Global 级别 ShardingSphere 社区的贡献力量，更大价值地回报给整个 Apache 全球社区及行业领域。</span></span>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  <span><span>Database Plus 是指在碎片化的数据库基础服务之上构建标准层和生态层，从而对上层应用提供统一标准化的数据库使用规范，尽可能屏蔽底层数据库差异化带来的业务干扰。</span></span>
  <span> </span>
  <strong><span>在连接上层应用与底层数据库的链路上，通过流量及数据劫持与解析，为用户提供分布式、数据库脱敏安全、数据库网关、数据路由压测等核心能力的增强。</span></strong>
  <span> </span>
  <span><span>在这一理念的支撑下，5.0.0 GA 版将带来以下内容的升级和优化。</span></span>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div>
    <img height="200" src="https://pic2.zhimg.com/v2-d724034a9145ae1db3d745cee7d0c10d_b.jpg" width="200" referrerpolicy="no-referrer">
   </div> 
   <div>
     
   </div> 
  </div> 
 </div> 
</div> 
<blockquote> 
 <div>
  <span><span>潘娟｜Trista</span></span>
 </div> 
 <div>
  <span><span>SphereEx 联合创始人兼 CTO, Apache member, Apache ShardingSphere PMC, Apache brpc(Incubating) & Apache AGE(Incubating) mentor, 中国木兰开源社区导师。 曾负责京东数科数据库智能平台的设计与研发，现专注于分布式数据库 & 中间件生态及开源领域。被评为《2020 中国开源先锋人物》，OSCAR 2021 尖峰开源人物。</span></span>
 </div> 
 <div>
  <strong><span>* 相关链接</span></strong>
 </div> 
 <div>
  <span>Bio:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftristazero.github.io" target="_blank">https://tristazero.github.io</a></span>
 </div> 
 <div>
  <span>LinkedIn:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fpanjuan" target="_blank">https://www.linkedin.com/in/panjuan</a></span>
 </div> 
 <div>
  <span>GitHub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FtristaZero" target="_blank">https://github.com/tristaZero</a></span>
 </div> 
 <div>
  <span>Twitter:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftwitter.com%2FtristaZero" target="_blank">https://twitter.com/tristaZero</a></span>
 </div> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><em><span>1 架构层面</span></em></h2> 
<div style="text-align:left"> 
 <div>
  <strong><span>Database Plus 可插拔核心架构基本完成</span></strong>
 </div> 
 <div>
   
 </div> 
</div> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> 
  <div>
   <span><span>基础层：提供多种接入端及接入形态，灵活满足用户不同场景的需求；</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>插拔层：作为可插拔核心架构，提供面向基础架构的支撑能力；</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>功能层：提供多种贴合用户需求的功能插件，方便用户选择和自由组合；</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>产品层：面向最终用户，提供面向行业和特定场景的标品方案。</span></span>
  </div> </li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div style="text-align:center">
    <img src="https://pic3.zhimg.com/v2-f3d031b851c32f2a381a252bca2fa4d2_b.jpg" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  <strong><span>多接入端混合模式生产可用</span></strong>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  <span><span>ShardingSphere JDBC 及 ShardingSphere Proxy 在经过一年的打磨和测试验证后，通过大型社区用户提供相关生产案例，已验证生产可行性。此外，SphereEx 将基于 ShardingSphere 生态，计划在 2022 年初推出面向 CloudNative 的 ShardingSphere Sidecar 接入端 POC 开源版。这三种模式在真实生产环境中既可实现单独部署，也可以使用多接入端混合部署的形式，均面向核心架构共享，进而能够接入形态多样的 ShardingSphere 生态，形式如下图所示。</span></span>
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div style="text-align:center">
    <img src="https://pic2.zhimg.com/v2-d90a6424e0f566dacdb444b3e795b8c9_b.jpg" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  <strong><span>分布式 SQL 打造标准化集群管理</span></strong>
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  <span><span>Apache ShardingSphere 首创提出 DistSQL（分布式 SQL）的独特 SQL 方言，用于与 ShardingSphere 整个生态打通，成为与 ShardingSphere 分布式数据库生态的标准化交互语言，用于一条 SQL 创建、修改、删除分布式数据库表、脱敏/加密数据库表及提供分布式调度管理能力。</span></span>
 </div> 
</div> 
<div style="text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><code class="language-java"><span style="color:#d73a49">CREATE</span> SHARDING <span style="color:#d73a49">TABLE</span> RULE t_order (
RESOURCES(resource_0,resource_1),
SHARDING_COLUMN=order_id,
<span style="color:#d73a49">TYPE</span>(<span style="color:#d73a49">NAME</span>=hash_mod,PROPERTIES(<span style="color:#032f62">"sharding-count"</span>=<span>4</span>)),
GENERATED_KEY(<span style="color:#d73a49">COLUMN</span>=another_id,<span style="color:#d73a49">TYPE</span>(<span style="color:#d73a49">NAME</span>=snowflake,PROPERTIES(<span style="color:#032f62">"worker-id"</span>=<span>123</span>)))
),t_order_item (
DATANODES(<span style="color:#032f62">"resource_$&#123;0..1&#125;.t_order$&#123;0..1&#125;"</span>),
DATABASE_STRATEGY(<span style="color:#d73a49">TYPE</span>=standard,SHARDING_COLUMN=user_id,SHARDING_ALGORITHM=database_inline),
TABLE_STRATEGY(<span style="color:#d73a49">TYPE</span>=standard,SHARDING_COLUMN=order_id,SHARDING_ALGORITHM=database_inline),
GENERATED_KEY(<span style="color:#d73a49">COLUMN</span>=another_id,<span style="color:#d73a49">TYPE</span>(<span style="color:#d73a49">NAME</span>=snowflake,PROPERTIES(<span style="color:#032f62">"worker-id"</span>=<span>123</span>)))
);

<span style="color:#d73a49">ALTER</span> SHARDING <span style="color:#d73a49">TABLE</span> RULE t_order (
RESOURCES(resource_0,resource_1),
SHARDING_COLUMN=order_id,
<span style="color:#d73a49">TYPE</span>(<span style="color:#d73a49">NAME</span>=hash_mod,PROPERTIES(<span style="color:#032f62">"sharding-count"</span>=<span>10</span>)),
GENERATED_KEY(<span style="color:#d73a49">COLUMN</span>=another_id,<span style="color:#d73a49">TYPE</span>(<span style="color:#d73a49">NAME</span>=snowflake,PROPERTIES(<span style="color:#032f62">"worker-id"</span>=<span>123</span>)))
),t_order_item (
DATANODES(<span style="color:#032f62">"resource_0.t_order$&#123;0..1&#125;"</span>),
DATABASE_STRATEGY(<span style="color:#d73a49">TYPE</span>=standard,SHARDING_COLUMN=user_id,SHARDING_ALGORITHM=database_inline),
TABLE_STRATEGY(<span style="color:#d73a49">TYPE</span>=standard,SHARDING_COLUMN=order_id,SHARDING_ALGORITHM=database_inline),
GENERATED_KEY(<span style="color:#d73a49">COLUMN</span>=another_id,<span style="color:#d73a49">TYPE</span>(<span style="color:#d73a49">NAME</span>=<span style="color:#d73a49">uuid</span>,PROPERTIES(<span style="color:#032f62">"worker-id"</span>=<span>123</span>)))
);

<span style="color:#d73a49">DROP</span> SHARDING <span style="color:#d73a49">TABLE</span> RULE t_order, t_order_item;</code></pre> 
</div> 
<div style="text-align:left"> 
 <div>
  <strong><span>分布式治理能力大幅度提升</span></strong>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  <span><span>在存算分离的 ShardingSphere 生态里，数据库（存储节点）与 Proxy 及 JDBC（计算节点）的分布式治理、在线用户元数据 DDL 变更、存储节点及计算节点的运行时上下线、熔断与禁用、高可用能力都在这个版本基本完善，此外分布式锁功能也在规划当中。</span></span>
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div style="text-align:center">
    <img src="https://pic4.zhimg.com/v2-049d258d9b8f96be484f2815720242af_b.png" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  <strong><span>APM 及监控展示能力全面升级</span></strong>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  <span><span>优化并增加更多 ShardingSphere 运行时状态指标，通过 agent 动态加载机制，为用户提供各种 Metrics 及 Tracing 的监控指标，方便对接 APM 系统及 Grafana dashboard。</span></span>
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><em><span>2 功能层面</span></em></h2> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div style="text-align:center">
    <img src="https://pic2.zhimg.com/v2-efa296325578a6e20238a663a249ae51_b.jpg" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  <span><span>ShardingSphere 社区将继续打磨产品，并不断融入行业新想法和新场景，持续发声和反馈。同时，社区的核心 Team 也非常愿意为想要参与开源的同学带来相关指导和提供更多的实战 Issue，方便新同学、老朋友能在 ShardingSphere 社区找到发光点、学习新知、结交来自全球各地的开发者。希望能与大家在 ShardingSphere 社区相遇！</span></span>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  <span><span>作为本次的 Release Manager，Apache ShardingSphere 社区 PMC 孟浩然将为大家带来关于此次新特性的全面解读，扫描下方二维码即可观看。</span></span>
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div style="text-align:center">
    <img src="https://pic2.zhimg.com/v2-732572b492b4ce0f8d4249f534523051_b.jpeg" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><em><span>3<span> </span></span><strong><span>欢迎参与 Apache ShardingSphere Dev Meetup</span></strong></em></h2> 
<div style="text-align:left"> 
 <div>
  <span><span>11 月 13 日，由 Apache ShardingSphere 社区主办的【Apache ShardingSphere Dev Meetup】将于北京市海淀区中关村大街 32 号智能制造创新中心 1 楼多功能厅举办。本次活动以【开放原生，包容生态 | Apache ShardingSphere 新形态探索之旅】为主题，聚焦最近更新的 Apache ShardingSphere 5.0.0 正式版本的新特性，国内三大顶级开源社区共同携手，从社区建设、技术合作、生态共建等多个角度，探索开源社区治理的新方式。</span></span>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  <span><span>欢迎大家点击【</span></span>
  <span> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzNjgwODk2Mw%3D%3D%26mid%3D2247485533%26idx%3D1%26sn%3D158358dc3e9459fcc7b4ca9de82e0b53%26chksm%3Dfaf1d331cd865a2761792f882ed6556cf4d3de1b0d88d13124f50e2ce7e3ce452f49f0867842%26scene%3D21%23wechat_redirect" target="_blank"><span><span>这里</span></span></a>
  <span> </span>
  <span><span>】报名参加。</span></span>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  <span><span>接下来我们也将持续为大家带来 Apache ShardingSphere 5.0.0 的正式发布报道、功能特性解读等技术文章，欢迎锁定我们的系列更新！</span></span>
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  <strong><span><span>🔗ShardingSphere GitHub 地址：</span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fshardingsphere" target="_blank"><span><span>https://github.com/apache/shardingsphere</span></span></a></strong>
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  <span><span>* 在使用 ShardingSphere 的过程中，如果您发现任何问题，有新的想法、建议，欢迎点击“</span></span>
  <span> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2Fcommunity%2Fcn%2Fcontribute%2Fsubscribe%2F" target="_blank"><span><span>链接</span></span></a>
  <span> </span>
  <span><span>“通过 Apache 邮件列表参与到 ShardingSphere 的社区建设中。</span></span>
 </div> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            