
---
title: '数据交换平台 Exchangis 1.0.0-RC1 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=672'
author: 开源中国
comments: false
date: Fri, 17 Jun 2022 19:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=672'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#57aaff"><strong>Exchangis简介</strong></span></p> 
<p>Exchangis是一个轻量级、高度可扩展的数据交换平台，支持结构化和非结构化异构数据源之间的数据传输。在应用层，具有数据权限管理与控制、节点服务高可用、多租户资源隔离等业务特性。在数据层，还具有传输架构多样、模块插件、组件耦合低等架构特点。</p> 
<p><strong><span>Exchangis1.0.0-RC1 是微众银行联合中国电信天翼云和仙翁科技共建的全新数据交换工具，支持异构数据源之间的结构化和非结构化数据传输同步。</span></strong></p> 
<p><span>Exchangis1.0.0 还抽象了一套统一的数据源和同步作业定义插件，允许用户快速接入新的数据源，允许用户快速集成对接 Apache Linkis 新的数据同步引擎，用户只需在数据库中简单配置即可在页面中使用新的数据源和数据同步引擎。</span></p> 
<p> </p> 
<p><span>借助于Linkis计算中间件的连接、复用和简化能力，Exchangis天生具备了高并发、高可用、多租户隔离和资源管控的金融级数据同步能力。</span></p> 
<p> </p> 
<p><span><span style="color:#333333">GitHub：</span><u>https://github.com/WeBankFinTech/Exchangis</u></span></p> 
<p> </p> 
<p><span><strong><span style="color:#57aaff">新版本内容</span></strong></span></p> 
<p><span>相比于 Exchangis0.5.0，Exchangis1.0.0-RC1 最大的特点就是已与 DataSphereStudio1.0.1 集成对接，可作为 DSS工作流的数据交换节点，进一步丰富了数据应用开发全流程的用户使用场景需求。</span></p> 
<p> </p> 
<p><span>由于架构的重大调整，Exchangis1.0.0 目前只支持使用 Linkis Sqoop 引擎进行数据同步，我们将在接下来的版本中逐步对接 Exchangis0.X 已支持的数据同步引擎，如：DataX，同时规划对接新的数据同步引擎，如：Distcp，FlinkX等。</span></p> 
<p> </p> 
<p><strong><span>该版本主要包含了以下内容：</span></strong></p> 
<p><span>1、【数据同步作业模块】数据同步作业执行重构</span></p> 
<p><span>2、【任务运行模块】对正在运行或者已完成的子作业查看他们的各项指标信息，以便对任务进行实时监控。</span></p> 
<p><span>3、【日志模块】数据同步进行中/结束能展示job和task的实时日志，准确快速的排查问题</span></p> 
<p><span>4、【数据源管理模块】对数据同步数据源进行一系列的管理操作</span></p> 
<p><span>5、【同步历史模块】对已完成或正在执行的同步数据任务进行历史信息管理</span></p> 
<p><span>6、【项目管理模块】对数据同步项目、任务进行配置管理</span></p> 
<p><span>7、【数据同步作业构建模块】对数据同步作业配置的信息进行构建，形成能够提交给linkis的形式</span></p> 
<p><span>8、 【Appconn模块】支持工作流形式执行数据同步任务</span></p> 
<p> </p> 
<p><span>缩写：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span>EJS: Exchangis Job Server</span></p> </li> 
 <li> <p><span>EJB: Exchangis Job Builder</span></p> </li> 
 <li> <p><span>EP: Exchangis Project</span></p> </li> 
 <li> <p><span>EDS: Exchangis Datasource Server</span></p> </li> 
 <li> <p><span>EXAPP: Exchangis Appconn</span></p> </li> 
</ul> 
<p> </p> 
<p><span><strong><span style="color:#57aaff">新特性</span></strong></span></p> 
<p><span>- [EJS][Exchangis-102] 增加新的exchangis-job-server模块，新增对数据同步任务调度类、执行类、提交任务类，新政任务增删改查功能、日志监控功能、同步历史管理功能   https://github.com/WeBankFinTech/Exchangis/pull/102</span></p> 
<p><span>- [EJB][Exchangis-110] 增加新的exchangis-job-builder模块，新增对数据同步作业的构建管理类，将数据同步作业转换为能够提交给linkis的形式.  https://github.com/WeBankFinTech/Exchangis/pull/110</span></p> 
<p><span>- [EP][Exchangis-88] 增加新的exchangis-project模块，提供数据同步项目管理服务，通过restful接口提供了数据同步项目的增删查改等功能。https://github.com/WeBankFinTech/Exchangis/issues/86</span></p> 
<p><span>- [EDS][Exchangis-88] 增加新的exchangis-datasource-server模块，提供对linkis-datasouce的数据源管理服务，通过restful接口提供了对数据源的增删改查、连接测试、版本管理等功能。https://github.com/WeBankFinTech/Exchangis/pull/95</span></p> 
<p><span>- [EJS][Exchangis-] 新增加对已提交数据同步任务的的管理服务，通过restful接口提供了历史任务的日志监控，指标信息查看，中止已提交任务等功能。https://github.com/WeBankFinTech/Exchangis/pull/160</span></p> 
<p><span>- [EJS][Exchangis-131] 对数据同步作业的执行过程进行了重构，提供异步执行、多租户功能和任务的高可用性 https://github.com/WeBankFinTech/Exchangis/pull/131</span></p> 
<p><span>- [EXAPP][Exchangis-179] 增加新的exchangis-appconn模块，通过appconn以第三方组件的方式与DSS对接，实现工作流形式执行数据同步任务，同步增删改查任务等功能。https://github.com/WeBankFinTech/Exchangis/pull/179</span></p> 
<p> </p> 
<p><span style="color:#57aaff"><strong>功能增强</strong></span></p> 
<p><span>- [EJS][Exchangis-140] 对于正在运行/已完成的某个子作业，能够展示各项指标信息。https://github.com/WeBankFinTech/Exchangis/pull/140</span></p> 
<p><span>- [Exchangis][Exchangis-284] 安装部署脚本优化。https://github.com/WeBankFinTech/Exchangis/pull/284</span></p> 
<p><span>- [Exchangis][Exchangis-284] 完善exchangis ddl，dml，配置文件。https://github.com/WeBankFinTech/Exchangis/pull/284</span></p> 
<p><span>- [Exchangis][Exchangis-281] 添加对ISSUE模板、Pull request模板和github CI action的支持。https://github.com/WeBankFinTech/Exchangis/pull/281</span></p> 
<p><span>- [Exchangis][Exchangis-224] 升级exchangis对linkis的依赖版本由1.0.3到1.1.0。https://github.com/WeBankFinTech/Exchangis/pull/224</span></p> 
<p><span>- [EJS][Exchangis-222] 重构job-server模块以适配新的数据库表。https://github.com/WeBankFinTech/Exchangis/pull/222</span></p> 
<p><span>- [EP][Exchangis-189] 重构数据同步项目管理模块。https://github.com/WeBankFinTech/Exchangis/pull/189</span></p> 
<p><span>- [EJB][Exchangis-188] 增强sqoop引擎数据同步作业构建功能。https://github.com/WeBankFinTech/Exchangis/pull/188</span></p> 
<p><span>- [EXAPP][Exchangis-179] 重构exchangis appconn模块https://github.com/WeBankFinTech/Exchangis/pull/179</span></p> 
<p><span>- [EJS][Exchangis-140] 数据同步进行中/结束能展示job/和task的实时日志。https://github.com/WeBankFinTech/Exchangis/pull/140</span></p> 
<p><span>- [EJS,EP][Exchangis-167] 添加作业更新接口，添加作业及项目的分页功能，优化restful层 https://github.com/WeBankFinTech/Exchangis/pull/167</span></p> 
<p><span>- [Exchangis][Exchangis-141] 添加对数据同步任务日志的前端异常处理 https://github.com/WeBankFinTech/Exchangis/pull/141</span></p> 
<p><span>- [EJS][Exchangis-143] 添加获取任务日志、获取所有所有历史任务和杀死任务的接口 https://github.com/WeBankFinTech/Exchangis/pull/143</span></p> 
<p><span>- [EJS][Exchangis-147] 调整日志组件的获取逻辑 https://github.com/WeBankFinTech/Exchangis/pull/147</span></p> 
<p><span>- [EJS][Exchangis-150] 增加对hive分区信息获取的功能 https://github.com/WeBankFinTech/Exchangis/pull/150</span></p> 
<p><span>- [EDS][Exchangis-165] 客户端RPC的实现和restful类的命名空间的修改 https://github.com/WeBankFinTech/Exchangis/pull/165</span></p> 
<p> </p> 
<p><span><strong><span style="color:#57aaff">Bug修复</span></strong></span></p> 
<p><span>- [Exchangis-227] [EJS] 解决job info服务因库表变动而造成的不适配问题 https://github.com/WeBankFinTech/Exchangis/pull/227</span></p> 
<p><span>- [Exchangis-185] [EJS-Execution] 避免map计算方法中netscape调用过程中的死锁:调整调度任务选择规则 https://github.com/WeBankFinTech/Exchangis/pull/185</span></p> 
<p><span>- [Exchangis-158] [EJS-Execution] 修复更新进度、状态和指标的错误。https://github.com/WeBankFinTech/Exchangis/pull/158</span></p> 
<p><span>- [Exchangis-165] [EDS] 客户端RPC的实现和restful类的命名空间的修改。https://github.com/WeBankFinTech/Exchangis/pull/165</span></p> 
<p><span>- [Exchangis-140] [EJS] 修复hive的run_date时间分区系统变量获取失败的问题 https://github.com/WeBankFinTech/Exchangis/issues/292</span></p> 
<p><span>- [Exchangis-140] [EJS-Execution] 修复sqoop工作流节点在取消任务后依旧在后台执行的问题 https://github.com/WeBankFinTech/Exchangis/issues/293</span></p> 
<p><span>- [Exchangis-282] [EJS-Execution] 修复复制子任务后更改数据源库表，导致原子任务的字段映射被覆盖的问题 https://github.com/WeBankFinTech/Exchangis/pull/282</span></p> 
<p><span>- [Exchangis-140] [EJS-Execution] 修复将任务提交到wtss进行调度代理用户失效的问题 https://github.com/WeBankFinTech/Exchangis/issues/294</span></p> 
<p><span>- [Exchangis-241] [EJS] 修复子任务日志缺失问题https://github.com/WeBankFinTech/Exchangis/issues/241</span></p> 
<p><span>- [Exchangis-221] [EJS] 修复查看子任务时候的重复请求问题 https://github.com/WeBankFinTech/Exchangis/issues/221</span></p> 
<p><span>- [Exchangis-204] [EJB] 在任务配置选择数据源库表时候，增加搜索框进行快速搜索 https://github.com/WeBankFinTech/Exchangis/issues/204</span></p> 
<p><span>- [Exchangis-210] [EJS] 修复点击执行ID查看任务进度后关闭，及时切换到别的页面，依旧在不停的拉取任务进度的问题 https://github.com/WeBankFinTech/Exchangis/issues/210</span></p> 
<p> </p> 
<p><span><strong><span style="color:#57aaff">贡献者</span></strong></span></p> 
<p><span><span style="color:#333333">Exchangis</span><span> </span>1.0.0-RC发布离不开<span style="color:#333333">Exchangis</span>社区的贡献者，感谢所有的社区贡献者！包括但不仅限于以下Contributors：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span>wushengyeyouya、Dlimeng、Davidhua1996、mingfengwang</span></p> </li> 
 <li> <p><span>peacewong、Casion、xiaojie19852006、yuxin-No1</span></p> </li> 
 <li> <p><span>ryanqin01、lucaszhu2zgf、FinalTarget、Liveipool、gjy1043</span></p> </li> 
</ul> 
<p> </p> 
<p><span>欢迎社区伙伴们安装和试用 Exchangis1.0.0-RC1，欢迎社区伙伴们参与共建全新的Exchangis1.0！</span></p>
                                        </div>
                                      
</div>
            