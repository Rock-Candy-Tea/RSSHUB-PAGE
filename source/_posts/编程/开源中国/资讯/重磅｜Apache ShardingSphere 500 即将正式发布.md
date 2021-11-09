
---
title: '重磅｜Apache ShardingSphere 5.0.0 即将正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fb3d8bed2bb5b0711b848ae1766360257a3.png'
author: 开源中国
comments: false
date: Tue, 09 Nov 2021 01:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fb3d8bed2bb5b0711b848ae1766360257a3.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0; text-align:justify"><span>Apache ShardingSphere 5.0.0 GA 版在经历 5.0.0-alpha 及 5.0.0-beta 接近两年时间的研发和打磨，终于将在 11 月份与大家正式见面！</span></p> 
<p style="color:#333333; margin-left:10px; margin-right:10px; text-align:justify"><span>11 月 10 日是 Apache ShardingSphere 进入 Apache 基金会的三周年纪念日。在这特殊的一天，ShardingSphere 的核心 Team 也响应社区的呼唤，<span style="color:#e36c09">将 5.0.0 GA 版作为三周年纪念日的礼物呈现给社区及整个分布式数据库和安全生态领域。</span></span></p> 
<p style="color:#333333; margin-left:10px; margin-right:10px; text-align:justify"><span>自 5.0.0 系列研发伊始，ShardingSphere 就逐渐脱离简单的分布式数据库中间件解决方案的行业定位。取而代之的是，<span style="color:#e36c09">Database Plus 理念将成为 5.0.0 及今后版本的新定位及新航标。通过重新塑造分布式可插拔体系，连通用户实际落地场景，为社区及整个数据库行业带来新风向及更有价值的解决方案。</span>5.0.0 GA 版将成为这一理念的首个实践版本，集成整个 Global 级别 ShardingSphere 社区的贡献力量，更大价值地回报给整个 Apache 全球社区及行业领域。</span></p> 
<p style="color:#333333; margin-left:10px; margin-right:10px; text-align:justify"><span>Database Plus 是指在碎片化的数据库基础服务之上构建标准层和生态层，从而对上层应用提供统一标准化的数据库使用规范，尽可能屏蔽底层数据库差异化带来的业务干扰。<span style="color:#e36c09">在连接上层应用与底层数据库的链路上，通过流量及数据劫持与解析，为用户提供分布式、数据库脱敏安全、数据库网关、数据路由压测等核心能力的增强。</span>在这一理念的支撑下，5.0.0 GA 版将带来以下内容的升级和优化。</span></p> 
<h2><span><span style="color:#000000"><strong>1 </strong></span><span style="color:#000000"><strong>架构层面</strong></span></span></h2> 
<h3><span>Database Plus 可插拔核心架构基本完成</span></h3> 
<ul> 
 <li>基础层：提供多种接入端及接入形态，灵活满足用户不同场景的需求；</li> 
 <li>插拔层：作为可插拔核心架构，提供面向基础架构的支撑能力；</li> 
 <li>功能层：提供多种贴合用户需求的功能插件，方便用户选择和自由组合；</li> 
 <li><span>产品层：面向最终用户，提供面向行业和特定场景的标品方案。</span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:center"><img alt src="https://oscimg.oschina.net/oscnet/up-fb3d8bed2bb5b0711b848ae1766360257a3.png" referrerpolicy="no-referrer"></p> 
<h3><span>多接入端混合模式生产可用</span></h3> 
<p style="color:#333333; margin-left:10px; margin-right:10px; text-align:justify"><span>ShardingSphere JDBC 及 ShardingSphere Proxy 在经过一年的打磨和测试验证后，通过大型社区用户提供相关生产案例，已验证生产可行性。<span style="color:#e36c09">此外，SphereEx 将基于 ShardingSphere 生态，计划在 2022 年初推出面向 CloudNative 的 ShardingSphere Sidecar 接入端 POC 开源版。这三种模式在真实生产环境中既可实现单独部署，也可以使用多接入端混合部署的形式，均面向核心架构共享，进而能够接入形态多样的 ShardingSphere 生态，</span>形式如下图所示。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e7396535df0dbffbdbce4e45c7f46e8c749.png" referrerpolicy="no-referrer"></p> 
<h3><span>分布式 SQL 打造标准化集群管理</span></h3> 
<p><span style="color:#e36c09">Apache ShardingSphere 首创提出 DistSQL（分布式 SQL）的独特 SQL 方言，用于与 ShardingSphere 整个生态打通，成为与 ShardingSphere 分布式数据库生态的标准化交互语言，</span><span>用于一条 SQL 创建、修改、删除分布式数据库表、脱敏/加密数据库表及提供分布式调度管理能力。</span></p> 
<h3><span>分布式治理能力大幅度提升</span></h3> 
<p style="color:#333333; margin-left:10px; margin-right:10px; text-align:justify"><span>在存算分离的 ShardingSphere 生态里，数据库（存储节点）与 Proxy 及 JDBC（计算节点）的分布式治理、在线用户元数据 DDL 变更、存储节点及计算节点的运行时上下线、熔断与禁用、高可用能力都在这个版本基本完善，此外分布式锁功能也在规划当中。</span></p> 
<h3><span>APM 及监控展示能力全面升级</span></h3> 
<p><span>优化并增加更多 ShardingSphere 运行时状态指标，通过 agent 动态加载机制，为用户提供各种 Metrics 及 Tracing 的监控指标，方便对接 APM 系统及 Grafana dashboard。</span></p> 
<h2><span><span style="color:#000000"><strong>2 </strong></span><span style="color:#000000"><strong>功能层面</strong></span></span></h2> 
<p style="color:#333333; margin-left:10px; margin-right:10px; text-align:justify"><img alt src="https://oscimg.oschina.net/oscnet/up-a217bdf796efb6ef94836c5bcc1b9ff6691.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:10px; margin-right:10px; text-align:justify"><span>ShardingSphere 社区将继续打磨产品，并不断融入行业新想法和新场景，持续发声和反馈。同时，社区的核心 Team 也非常愿意为想要参与开源的同学带来相关指导和提供更多的实战 Issue，方便新同学、老朋友能在 ShardingSphere 社区找到发光点、学习新知、结交来自全球各地的开发者。希望能与大家在 ShardingSphere 社区相遇！</span></p>
                                        </div>
                                      
</div>
            