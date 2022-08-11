
---
title: '版本动态 _ Apache Linkis (Incubating) 1.1.3 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/6025dcab-9bb3-4c2e-9844-8f0900bb51b1.jpg'
author: 开源中国
comments: false
date: Thu, 11 Aug 2022 09:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/6025dcab-9bb3-4c2e-9844-8f0900bb51b1.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:8px; margin-right:8px; text-align:center"><img height="239" src="https://oscimg.oschina.net/oscnet/6025dcab-9bb3-4c2e-9844-8f0900bb51b1.jpg" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#0080ff"><strong><span style="background-color:#ffffff; color:#0080ff">Linkis 1.1.3 版本简介</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span><span style="color:#333333">GitHub：</span><u>https://github.com/apache/incubator-linkis</u></span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span style="color:#000000">Gitee：</span><u>https://gitee.com/apacheLinkis/Linkis</u></p> </li> 
</ul> 
<p style="color:#24292e; margin-left:8px; margin-right:8px; text-align:left"><strong><span>本次发布的 1.1.3 版本主要集成 Prometheus，提供 Linkis 微服务监控的基础能力；任务提交新增任务重试次数参数；增加任务与执行 EC 的关联信息记录；Flink 引擎支持将 Yarn 日志下载到 EC 日志目录；前端页面支持水印；部分安全漏洞组件升级等；修复社区反馈的已知 bug。</span></strong></p> 
<p style="color:#24292e; margin-left:8px; margin-right:8px; text-align:left"><span>缩写：</span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>COMMON: Linkis Common</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>EC: Engineconn</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>ECM: EngineConnManager</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>ECP: EngineConnPlugin</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>DMS: Data Source Manager Service</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>MDS: MetaData Manager Service</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>LM: Linkis Manager</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>PS: Linkis Public Service</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>PE: Linkis Public Enhancement</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>RPC: Linkis Common RPC</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>CG: Linkis Computation Governance</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#0080ff"><strong><span style="color:#0080ff">版本新特性</span></strong></span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#24292e">新特性 1：</span><span style="color:#24292e">集成 prometheus，提供 linkis 微服务监控的基础能力</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="background-color:#ffffff; color:#24292e">Linkis 是一组分布式的微服务，可以部署在单机、集群或 Kubernetes 环境中，因此需要有一个健壮、灵活的监控机制来监控各个微服务实例的状态。该特性支持了 Linkis 中各个微服务 (包括 EngineConn)，通过 API 端口的方式暴露标准的性能指标，随后 Prometheus 可以通过 Eureka 获取服务实例，从这些这些端点动态获取指标，并通过 Grafana 进行可视化展示。</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="background-color:#ffffff; color:#24292e"><img src="https://oscimg.oschina.net/oscnet/61c61123-4372-4509-8163-8cf6936b83d8.jpg" referrerpolicy="no-referrer"></span></p> 
<h3 style="margin-left:8px; margin-right:8px; text-align:left"><span>新特性 2：自定义变量设计</span></h3> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="background-color:#ffffff; color:#24292e">为了方便用户在执行代码时，动态替换已预先定义好的公共变量，例如执行时间。该特性实现了变量替换拦截器，来解析出所有代码中用到的变量和表达式，然后通过系统以及用户自定义的变量初始值进行替换，最终再将解析后的代码提交给 EngineConn 执行。</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/3c81c9cd-625c-4fee-89cc-ce17a7a5e665.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"> </p> 
<h3 style="margin-left:8px; margin-right:8px; text-align:left"><span>新特性 3：EngineConn 历史信息记录特性</span></h3> 
<p style="color:#24292e; margin-left:8px; margin-right:8px; text-align:left"><span>1.1.3 版本前，LinkisManager 只记录了在运行中的 EngineConn 的信息和资源使用，但是在任务结束后这些信息就丢失了。为了更好地追溯历史 EC 的使用情况，该特性完成了 EC 信息和资源信息持久化到 DB 的存储，并且支持在前端管理页面，查看已经结束 EC 的日志：</span></p> 
<p style="color:#24292e; margin-left:8px; margin-right:8px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/95b44b84-77fa-4525-a4de-221ebe295bc1.png" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:8px; margin-right:8px; text-align:left"> </p> 
<h3 style="margin-left:8px; margin-right:8px; text-align:left"><span>新特性 4：EngineConn Metrics 上报</span></h3> 
<p style="color:#24292e; margin-left:8px; margin-right:8px; text-align:left"><span>现有 EngineConn 模块，上报信息缺少引擎信息、上报的资源和进度的接口存在冗余。该特性对 EngineConn Metrics 进行优化调整，并且在上报协议中增加扩展模块，进而优化 Metrics 获得过程中的性能。</span></p> 
<h3 style="margin-left:8px; margin-right:8px; text-align:left"><span>新特性 5：CS 清理接口特性</span></h3> 
<p style="color:#24292e; margin-left:8px; margin-right:8px; text-align:left"><span>1.1.3 版本前，ContextService 统一上下文服务缺少清理机制，且缺少创建时间、更新时间字段以及批量清理的接口， 在长期累积情况下可能出现百万级数据，影响查询效率。对此，该特性在 ContextService 中补充了以上缺失信息，并添加清理清理的 restful 接口，支持按照时间范围、按照 id 列表的批零清理接口。</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#0080ff"><strong><span style="background-color:#ffffff; color:#0080ff">增强点</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[ECM] Linkis-2243 优化新注册的 ECM 服务，优化服务负载选择逻辑，减下可能存在的因为新服务可用性问题造成的影响</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[PS-Jobhistory] Linkis-2198 优化任务代码缓存文件名，增加时间参数，避免长任务存在的冲突问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[EC-Python] Linkis-2175 增加 py4j 的 watchdog 线程，监控 java 进程，防止 java 进程异常退出后，python 进程没有退出的情况</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Common] Linkis-2150 common 和 entrance 模块都存在自定义变量替换的逻辑，优化聚集到 common 模块中处理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[EC-JDBC] Linkis-2142 修复 JDBC Engine 控制台配置修改后无法立即生效的问题（cache 时间调整为配置项）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance] Linkis-2160 任务提交的消费队列支持配置特定大容量用户</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[PE] Linkis-2200 标签代码优化，去除标签 key-value 的持久化</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[EC] Linkis-1749  支持 EC 启动时 ，能够通过参数进行指定服务的端口段的限制</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Common-Storage] Linkis-2168 FileSource 中文件类型支持变量配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Common-Storage] Linkis-2161 新增对结果集导出到 excel 文件时，自动格式化参数的支持</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Gateway] Linkis-2249 优化 gateway 的 Parser 逻辑代码</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Web] Linkis-2248  用户资源展示页面按用户和创建者排序展示</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Web] Linkis-2108 前端页面布局优化调整，统一基本样式，优化二级菜单展示</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Install] Linkis-2319  调整数据源服务部署模式，默认为开启；支持安装时，配置初始登陆密码</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Install] Linkis-2421  支持安装部署时，配置 kerberos 相关认证信息</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[EC] Linkis-2159 EC 的 log 日志支持按大小和时间切割滚动</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Common-Scheduler] Linkis-2272 优化代码格式增加 LoopArray 单元测试</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[PS-ContextService] Linkis-2234 在 contextservice 添加了批量清理 context 值的方法</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#0080ff"><strong><span style="background-color:#ffffff; color:#0080ff">修复功能</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[EC] Linkis-2275 修复 EC 引擎心跳上报在异常场景下日志字段过长导致存储失败问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Web] Linkis-2239  修复 yarm 队列资源空闲 / 繁忙状态使用率的环形占比图显示不正确问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[PS-ContextService] Linkis-2226 修复 FileReader 和 BufferedReader 资源在 final 中未释放的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Install] Linkis-2203  不同系统编译出现 shell 脚本授权 + x 权限失败问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance] Linkis-2237 重构 JobQueueLabel 和 JobRunningLabel, 修复任务排队标签和任务运行标签 bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Build] Linkis-2354  修复 WIN 系统下 编译打包项目存在的 ERROR 级别的警告问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Gateway] Linkis-2329 修复 LDAP 接入存在的配置问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance] Linkis-2238 优化结果集路径以日期分隔，解决单个文件夹子目录过多问题 不同日期的 resustset 路径在同一个文件夹，如 “/tmp/linkis/hadoop/linkis/20220516_210525/IDE/40099”，可能会导致一个文件夹下文件太多</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance] Linkis-2162 优化结果集路径以日期分隔，解决单个文件夹子目录过多问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Common] Linkis-2332 关闭 SpringCloud 默认配置中心，减少不必要日志信息的干扰</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Web] Linkis-2295 移除 web 安装脚本中多余的代码</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#0080ff"><strong><span style="color:#0080ff">安全相关</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[PS-Jobhistory] Linkis-2248 任务查询列表接口增加参数校验，防止 sql 注入的安全问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[PS-PublicService] Linkis-1949  /api/rest_j/v1/datasource/columns 接口增加用户权限检查</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#0080ff"><strong><span style="color:#0080ff">依赖变更</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Common] Linkis-2188 升级 poi 5.2.1 至 poi 5.2.2，修复可能出现的内存分配问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Common] Linkis-2182 升级 gson:2.8.5 至 gson:2.8.9 版本</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#0080ff"><strong><span style="color:#0080ff">详细指引</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><span>本版本总览: </span><u>https://linkis.apache.org/zh-CN/docs/latest/release</u></p> </li> 
 <li> <p style="color:#24292e; margin-left:0; margin-right:0; text-align:left"><span>详细安装部署见指引：</span><u>https://linkis.apache.org/zh-CN/docs/latest/deployment/quick-deploy</u></p> </li> 
 <li> <p style="color:#24292e; margin-left:0px; margin-right:0px; text-align:left"><span>官方下载链接：</span><u>https://linkis.apache.org/zh-CN/download/main</u></p> </li> 
</ul> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><strong style="color:#0080ff">贡献者寄语</strong></p> 
<p style="color:#333333; margin-left:8px; margin-right:.75em; text-align:left"><span>Apache Linkis (incubating) 1.1.3 的发布离不开 Linkis 社区的贡献者，感谢所有的社区贡献者，包括但不仅限于以下 Contributors（排名不分先后）:</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img src="https://oscimg.oschina.net/oscnet/923e56ac-d115-40a3-879b-88a17f11f5c5.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:8px; margin-right:.75em; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img src="https://oscimg.oschina.net/oscnet/62e05cec-6f04-4cdd-bc5e-10d2d58c3f0a.jpg" width="620" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><span><strong style="color:#525151">— END —</strong></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#0080ff"><strong><span style="background-color:rgba(0, 0, 0, 0); color:#0080ff">如何成为社区贡献者</span></strong></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span style="color:#0080ff"><span><strong>1 </strong></span>►</span> <span style="color:#000000">官方文档贡献。发现文档的不足、优化文档，持续更新文档等方式参与社区贡献。通过文档贡献，让开发者熟悉如何提交 PR 和真正参与到社区的建设。参考攻略：</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4MDkxNzUxMg%3D%3D%26mid%3D2247488838%26idx%3D1%26sn%3D3599cbb009751af44ba46720b0b60cf7%26chksm%3Debb07621dcc7ff37405c5c7ab36193c44ba543d4854b01a23cbc66a12440472a3a0adbc85c5b%26scene%3D21%23wechat_redirect" target="_blank"><span style="color:#0080ff">保姆级教程：如何成为 Apache Linkis 文档贡献者</span></a></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span style="color:#0080ff"><span><strong>2 </strong></span><span>►</span></span><span style="color:#5f9cef"> </span><span><span style="color:#000000">代码贡献。我们梳理了社区中简单并且容易入门的的任务，非常适合新人做代码贡献。请查阅新手任务列表：</span><u>https://github.com/apache/incubator-linkis/issues/1161</u></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span style="color:#0080ff"><span><strong>3 </strong></span>►</span><span style="color:#5f9cef"> </span><span style="color:#000000">内容贡献：发布 WeDataSphere 开源组件相关的内容，<span style="background-color:#ffffff; color:#333333">包括但不限于安装部署教程、使用经验、案例实践等，形式不限，请投稿给小助手。例如：</span></span></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4MDkxNzUxMg%3D%3D%26mid%3D2247488722%26idx%3D1%26sn%3D6069ac14a2e0ec6f09acb8c8a471914f%26chksm%3Debb077b5dcc7fea3fcb2df95de0b3a99ecf1f73a86b8c036f1c36c17cce30c1d36b38866fec0%26scene%3D21%23wechat_redirect" target="_blank"><span style="color:#0080ff">技术干货 | Linkis 实践：新引擎实现流程解析</span></a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4MDkxNzUxMg%3D%3D%26mid%3D2247488695%26idx%3D1%26sn%3D4020e1bccb565d518c0731b26b9a76ac%26chksm%3Debb077d0dcc7fec65c3052051f3a7d6d51b160fa82b5b89c06e1e0180080bb85949683f31a32%26scene%3D21%23wechat_redirect" target="_blank"><span style="color:#0080ff">技术干货 | Prophecis 保姆级部署教程</span></a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4MDkxNzUxMg%3D%3D%26mid%3D2247488005%26idx%3D1%26sn%3Ddf78dfb77f475c2d1ef7ee69568db5c7%26chksm%3Debb07162dcc7f8749a421038dd51abd7befb08aba8354846d87c61982db6a1ba520d99fd391b%26scene%3D21%23wechat_redirect" target="_blank"><span style="color:#0080ff">社区开发者专栏 | MariaCarrie：Linkis1.0.2 安装及使用指南</span></a></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span style="color:#0080ff"><span><strong>4 </strong></span>►</span><span style="color:#5f9cef"> </span><span style="color:#000000">社区答疑：积极在社区中进行答疑、分享技术、帮助开发者解决问题等；</span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span style="color:#0080ff"><span><strong>5 </strong></span>►</span><span style="color:#5f9cef"> </span><span style="color:#000000">其他：积极参与社区活动、成为社区志愿者、帮助社区宣传、为社区发展提供有效建议等；</span></span></p>
                                        </div>
                                      
</div>
            