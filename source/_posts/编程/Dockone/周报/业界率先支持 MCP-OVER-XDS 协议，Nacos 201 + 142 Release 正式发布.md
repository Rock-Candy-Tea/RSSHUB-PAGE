
---
title: '业界率先支持 MCP-OVER-XDS 协议，Nacos 2.0.1 + 1.4.2 Release 正式发布'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/af809329ff234b668fcaec67039443ad.jpg'
author: Dockone
comments: false
date: 2021-05-18 08:03:18
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/af809329ff234b668fcaec67039443ad.jpg'
---

<div>   
<br>来源 | <a href="https://mp.weixin.qq.com/s/j-Wl_gJWo8sno876U2Xajw">阿里巴巴云原生公众号</a><br>
​<br>
Nacos 是阿里巴巴开源的服务发现与配置管理项目，本次同时发布两个版本：<br>
​<br>
1. 发布 2.0.1 版本，主要致力于支持 MCP-OVER-XDS 协议，解决 Nacos 与 Istio 数据服务同步问题。<br>
1. 发布 1.4.2 版本，极大增强 K8s 环境中 JRaft 集群 Leader 选举的稳定性。<br>
<br><h2>Nacos 2.0.1</h2>2.0.1 主要变更为：<br>
​<br>
1. 在 nacos-istio 插件及模块中，支持 MCP-OVER-XDS 协议，解决 Nacos 与 Istio 数据服务同步问题。<br>
1. 增强了 Jraft 协议在 K8s 环境中的 Leader 选举的稳定性。<br>
1. 修复了频繁抛出 Server is Down 错误的问题。<br>
<br>具体变更为：<br>
​<br>
<code class="prettyprint">[#3484] Support ldap login.<br>
[#4856] Support mcp over xds.<br>
[#5137] Support service list add view subscriber.<br>
[#5367] Support client encryption plugin for nacos 2.0.<br>
[#5307] Push support config some parameters<br>
[#5334] Fix Server is Down problem in k8s environment.<br>
[#5361] Check isUseGrpcFeatures() when register instance using GRPC protocol.<br>
[#5486] Refactor Distro Config as singleton and replace GlobalConfig.<br>
[#5169] Fix instance beat run only by responsible server.<br>
[#5175] Fix publishConfig lost type.<br>
[#5178] Fix NPE when init server list failed.<br>
[#5182] Fix throw NoSuchFieldException in ConfigController when service connect to nacos.<br>
[#5204] Fix query error when pageNo is larger than service number.<br>
[#5268] Fix subscriber app unknown<br>
[#5327] Fix ThreadPool usage problem and add some monitor for distro.<br>
[#5384] Fix the problem of unable to shutdown NacosConfigService.<br>
[#5404] Fix frequently udp push for client 1.X.<br>
[#5419] Fix Nacos 2.0 client auth may invalid for non public namespace.<br>
[#5442] change state to UP when received status form old version server.<br>
[#5096] Add unit tests in nacos 2.0.<br>
[#5171][#5421][#5436][#5450][#5464] Fix IT for nacos 2.0.</code><br>
<br><h2>Nacos 1.4.2</h2><ol><li>该版本优化了 JRaft 模块，与最新的 nacos-k8s 项目配合使用，极大增强集群选主的稳定性。</li><li>另外，该版本了修复有关“Server is Down”问题的提示及众多 1.4.1 版本中的 Bug。</li></ol><br>
<br>具体变更为：<br>
​<br>
<code class="prettyprint">[#4452] Add config compare features.<br>
[#4602] Add new way for export config.<br>
[#4996] Make log level changeable for nacos-core module.<br>
[#5367] Add pre-plugin in client for encrypting config.<br>
[#3922] Method createServiceIfAbsent in ServiceManager require sync.<br>
[#4274] skip master-select task when db.num is 1.<br>
[#4753] Use SafeConstructor to parse yaml configuration.<br>
[#4762] Naming health check thread num support user define it by self.<br>
[#4770] Beta publish: change the way of select betaIps, from input to select.<br>
[#4778] Make SecurityProxy.accessToken threadsafe in single writer multi reader.<br>
[#4903] Add securuty hint for login page.<br>
[#4917] Raft ops interface add auth.<br>
[#4980] Log4J2NacosLogging.loadConfiguration() return directly When location is blank.<br>
[#5010] Fix the usage of TemplateUtils.<br>
[#5190] Add some hint log when login failed.<br>
[#5234] Solve the problem that page can be edited while publishing-config request is processing.<br>
[#5331] Fix the mouse hovers over the margin in a pointer state and cannot be clicked.<br>
[#5350] Add hint and detail reason for consistence status Down.<br>
[#5439] Support specified naming UDP push port for client.<br>
[#5434] Optimize the ConfigType.isValidType method.<br>
[#3779] Check groupName can't be empty.<br>
[#4661] ConfigServletInner#doGetConfig code optimization.<br>
[#3610] Fix the press F1 to full screen issue in new config page.<br>
[#3876] Fix push empty service name.<br>
[#4306] Fix search service by group error problem.<br>
[#4573,#4629] Jraft leader status check error.<br>
[#4672] Fix cloning configuration lost description.<br>
[#4699] Fix metadata batch operation may delete instance problem.<br>
[#4756] Fix config list sort and search problem.<br>
[#4787] Losting member if parsing host throw UnknownHostException.<br>
[#4806] Fix addListener method comment.<br>
[#4829] Remove instance when distro and raft remove instances data.<br>
[#4852] Fix main.js is too large problem.<br>
[#4854] Modify Header to support Keys Ignore Case.<br>
[#4898] Fix instance list page bug.<br>
[#4925] Fix member list change will cover member status and metadata problem.<br>
[#5078] Fix the problem of inconsistent results for querying subscriber list data multiple times.<br>
[#5026] Fix MetricsHttpAgent metrics twice.<br>
[#5018] Check group and dataId in groupKey.<br>
[#5114] ConcurrentHashSet.java is not compatible with jdk1.6 or 1.7.<br>
[#5253] Fix missing auth identity header error.<br>
[#5291] Fix Beat task will stop when throw unexpected exception.<br>
[#5301] Respond all kinds of collections for istio's request.<br>
[#5351] Fix Consistence status can't switch to UP after Jraft election.<br>
[#5390] Fix ip verify error.<br>
[#5427] Fix NPE if Jraft leader is null in CurcuitFilter.<br>
[#5437] Fix config beta feature will lost dump event problem.<br>
[#5451] Fix the tag can't be removed problem.<br>
[#4822][#4823][#4824][#4825][#4979][#5506] Fix dependency security problem.<br>
[#5277] Subscriber list servername add required.<br>
[#5380][#5418] Add and enhance unit test.</code><br>
<br><h2>社区</h2>随着 Nacos 2.0.1 及 1.4.2 的发布 Nacos 社区又新增了一位 Committer：haoyann，这位同学在推进多数据源支持、鉴权及安全性、配置模块优化与完善等内容中作出许多贡献，并积极参与社区讨论。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/af809329ff234b668fcaec67039443ad.jpg" alt="haoyann_commiter.jpg" referrerpolicy="no-referrer"><br>
<br>Nacos 社区欢迎更多愿意参与共建的小伙伴加入，包括但不限于：<br>
​<br>
- 源代码<br>
- 文档<br>
- 社区讨论<br>
- 多语言实现<br>
- 周边生态产品结合<br>
<br>积极参与将可以获得 Nacos 社区赠送的精美小礼品～<br>
<br><h2>About Nacos</h2>Nacos 致力于帮助您发现、配置和管理微服务。Nacos 提供了一组简单易用的特性集，帮助您快速实现动态服务发现、服务配置、服务元数据及流量管理。<br>
​<br>
Nacos 帮助您更敏捷和容易地构建、交付和管理微服务平台。Nacos 是构建以“服务”为中心的现代应用架构 (例如微服务范式、云原生范式) 的服务基础设施。
                                
                                                              
</div>
            