
---
title: 'Apache Linkis(incubating) 1.1.1 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2111d591221b0d9fd73b1f2ece3ce31e085.png'
author: 开源中国
comments: false
date: Wed, 01 Jun 2022 14:33:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2111d591221b0d9fd73b1f2ece3ce31e085.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#0080ff"><strong><span style="background-color:#ffffff">Linkis 1.1.1 版本简介</span></strong></span></p> 
<p><span style="background-color:#ffffff; color:#24292f">本次发布的1.1.1版本，主要支持UDF多版本控制；支持将UDF函数的jar包/脚本物料上传至BML管理的hdfs文件系统；提交任务支持Yarn队列资源使用统计采集和查看；管理台的ECM管理页面能支持运行中的引擎日志文件的查看；新增对数据虚拟化引擎OpenLooKeng的支持。</span></p> 
<p><span style="background-color:#ffffff; color:#24292f"><span style="background-color:#ffffff; color:#24292f">GitHub：</span><u>https://github.com/apache/incubator-linkis</u></span></p> 
<p><span>缩写：</span></p> 
<ul style="margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0"><span>EC: Engineconn</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>ECM: EngineConnManager</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>ECP: EngineConnPlugin</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>EC: EngineConn</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>DMS: Data Source Manager Service</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>MDS: MetaData Manager Service</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>LM: Linkis Manager</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>BML: BigData Material Library</span></p> </li> 
</ul> 
<p><span style="color:#0080ff"><strong><span>版本新特性</span></strong></span></p> 
<p><span><strong>新特性1：支持代理用户模式</strong></span></p> 
<p><span>linkis在执行用户提交的任务时，linkis的主进程会通过 sudo -u 切换到对应用户下，然后执行对应的引擎启动命令，这就需要为每个&#123;submit user&#125; 提前创建对应的系统用户，并且配置好相关的环境变量。对于新用户，需要一系列的环境的初始化准备工作，如果频繁的用户变化，会增大运维成本，而且用户过多，没法针对单个用户配置资源，资源之间无法很好的管控。代理用户模式的支持，能够实现用户A的任务代理给指定的代理用户执行，可以将执行入口统一收敛。后续DSS计划集成Linkis的代码用户模式（暂未发布），能够通过DSS管理台页面，对当前登陆用户的代理用户选择。</span></p> 
<p><strong><span>新特性2：UDF支持多版本控制</span></strong></p> 
<p><span>1.1.1版本之前无法支持UDF多版本的控制，无法对某个UDF函数的历史版本进行查看和回退，并且UDF函数jar包/脚本物料是存储在服务器的主机上，如果更换服务器的话，需要做UDF函数jar包/脚本物料的同步迁移。新增linkis_ps_udf_version表 ，以支持UDF函数的多版本存储，依赖于目前linkis已有的BML物料管理功能，将udf函数的jar/脚本物料上传至BML管理的hdfs文件系统中。</span></p> 
<p><span>具体使用方式见：</span><u>https://linkis.apache.org/zh-CN/docs/latest/user_guide/udf</u></p> 
<p><strong><span>新特性3：新增数据虚拟化openLooKeng引擎插件</span></strong></p> 
<p><span>openLooKeng用于支持数据探索、即席查询和批处理，具有100+毫秒至分钟级的近实时时延，而无需移动数据。openLooKeng还支持层次化部署，使地理上远程的openLooKeng集群能够参与相同的查询。利用其跨区域查询计划优化能力，涉及远程数据的查询可以达到接近“本地”的性能。新增的openLooKeng引擎插件可以让Linkis拥有数据虚拟化的能力，支持提交跨源异构查询、跨域跨DC查询型任务。</span></p> 
<p><span>具体使用方式见：</span><u>https://linkis.apache.org/zh-CN/docs/latest/engine_usage/openlookeng</u></p> 
<p><strong><span>新特性4：引擎进程日志文件页面查看</span></strong></p> 
<p><span>对于启动的引擎进程，能够在管理台>ECM管理>某ECM具体引擎列表页面，直接查看进程的运行日志文件内容。方便某些异常问题的排查，以及引擎运行时，关键日志信息的查看。</span></p> 
<p><span style="color:#0080ff"><strong><span>功能增强</span></strong></span></p> 
<ul style="margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Gateway][Linkis-1430] 针对Token认证方式，Token的获取由配置文件调整为数据库表</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance][Linkis-1642] 优化excel导出接口resultsetToExcel:支持传递下载数据的行数</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance][Linkis-1733] 添加支持更多与run_date相关的默认时间变量</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance][Linkis-1794] 添加写入限制结果集单行的数据大小，优化大结果集会导致的OOM问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[DMS-Common][Linkis-1757] 支持配置Hive的元数据管理员，管理员通过接口可以获取hive的所有库表的元数据信息</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Common][Linkis-1799] 优化服务日志的分割:将日志历史切分时间从一天调整为一小时</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Common][Linkis-1921] 优化Jackson的依赖管理方式:通过jackson-bom统一管理jackson依赖，并升级至2.11.4版本</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[ECM][Linkis-1779] 优化ECM实例的状态监控逻辑，增加心跳上报时间的判断，修复可能因为Eureka的性能问题导致错误判断问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[ECM][Linkis-1930] 优化资源检查时未检查ECM资源的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Web][Linkis-1596] 优化管理台任务日志查看的接口使用，修复对于运行中的job，日志无法及时刷新显示的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Web][Linkis-1650] linkis管理台-全局历史页面,支持通过创建者信息搜索过滤历史任务数据</span></p> </li> 
</ul> 
<p><span style="color:#0080ff"><strong><span>修复功能</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance][Linkis-1623] 修复LogPath和ResultSetPath错误的将submitUser使用为executeUser</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance][Linkis-1640] 修复LogReader使用单例InputStream，存在日志丢失，无法读取最新的持久化日志的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance][Linkis-2009] 修复Entrance 服务存在的线程资源未关闭导致的内存泄漏的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance][Linkis-1901] 将EntranceFactory中的缓存替换为Guava Cache，修复用户修改了并发参数后无法生效的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance][Linkis-1986] 修复Entrance实时日志获取行数异常，导致获取的日志重复问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[ECM][Linkis-1714] 通过减少EC Java默认内存大小以及添加EC应用程序的重试日志，优化EC出现的"Cannot allocate memory"的异常问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[ECM][Linkis-1806] 优化EC的生命周期处理逻辑，当ECM 启动EC因为队列资源不足超时等原因导致状态为Failed时候，将EC进程kill掉</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Common][Linkis-1721] 修复Kerberos认证失败时, hdfsFileSystem未进行刷新的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[UDF][Linkis-1728] 优化/api/rest_j/v1/udf/all的API接口偶发的查询耗时高的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Config][Linkis-1859] 修复管理台参数配置saveFullTree接口，主键重复异常问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[<span>Client</span>][Linkis-1739] 修复ujes-client的请求中，存在的参数拼写错误导致参数传递失败问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Client][Linkis-1783] 修复任务创建人creator参数默认配置不生效的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Client][Linkis-1821] 修复ujes-client 请求实体类GetTableStatisticInfoAction参数缺失问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[EC][Linkis-1765] 修复EC 在任务运行时触发tryShutdown存在的阻塞卡住问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[LM-AppManager][Linkis-1814] 修复EngineRestfulApi的createEngineConn接口返回response信息有误，导致客户端调用出现NPE的问题。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Web][Linkis-1972] 移除管理台历史原因遗留但未使用的dss相关接口代码</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[EC-Spark][Linkis-1729] 添加SparkPreExecutionHook函数，兼容Linkis之前的老包名（com.webank.wedatasphere.linkis）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[EC-JDBC][Linkis-1851] 修复jdbc引擎，一次任务执行中存在多条sql语句时无法正常执行的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[EC-JDBC][Linkis-1961] 修复jdbc引擎启动因SLF4J依赖问题导致日志无法正常打印的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Gateway][Linkis-1898] 修复GatewaySSOUtils用户成功登录生成cookie时，无法设置初始域名的问题</span></p> </li> 
</ul> 
<p><strong style="color:#0080ff">其他</strong></p> 
<ul style="margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[License][Linkis-2110] 移除了源码中的二进制文件.mvn/wrapper/maven-wrapper.jar，调整.mvn/*相关的LICENSE说明</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[License][Linkis-2113] 升级 py4j-0.10.7-src.zip 至 py4j-0.10.9.5-src.zip，解决0.10.7版本中部分文件license协议不明确问题，更新py4j-*.src的license文件</span></p> </li> 
</ul> 
<p><strong style="color:#0080ff">详细指引</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:#333333">本版本总览:<span> </span></span><u>https://linkis.apache.org/zh-CN/docs/latest/release</u></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span>详细安装部署见指引：</span><u>https://linkis.apache.org/zh-CN/docs/latest/deployment/quick_deploy</u></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span>官方下载链接：</span><u>https://linkis.apache.org/zh-CN/download/main</u></p> </li> 
</ul> 
<p><strong style="color:#0080ff">贡献者寄语</strong></p> 
<p><span>Apache Linkis(incubating) 1.1.1的发布离不开Linkis社区的贡献者,感谢所有的社区贡献者，包括但不仅限于以下Contributors：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>AbnerHung、Alexkun、CCweixiao</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Davidhua1996、</span><span>Fuu3214、Liveipool</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>barry8023、casionon</span><span>e、</span><span>demonray</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>husofskyzy、jackxu2011、legendtkl</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>lizheng920625、</span><span>maidangdang4</span><span>4</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>peacewong、</span><span>s</span><span>eedscoder</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"> </p> 
<p><img height="2000" src="https://oscimg.oschina.net/oscnet/up-2111d591221b0d9fd73b1f2ece3ce31e085.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#0080ff"><strong>如何参与贡献</strong></span></p> 
<p style="color:#24292f; margin-left:8px; margin-right:8px; text-align:left"><span><span style="color:#333333">（1）新手任务：认领入门任务，详见 </span><u>https://github.com/apache/incubator-linkis/issues/1161</u><span style="color:#333333">； <span> </span></span></span></p> 
<p style="color:#24292f; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#333333">（2）作品沉淀：发布WeDataSphere开源组建相关内容，包括但不限于安装部署教程、使用经验、案例实践等，形式不限，请投稿给小助手。如：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4MDkxNzUxMg%3D%3D%26mid%3D2247488005%26idx%3D1%26sn%3Ddf78dfb77f475c2d1ef7ee69568db5c7%26chksm%3Debb07162dcc7f8749a421038dd51abd7befb08aba8354846d87c61982db6a1ba520d99fd391b%26scene%3D21%23wechat_redirect" target="_blank"><span style="color:#0080ff">社区开发者专栏 | MariaCarrie：Linkis1.0.2安装及使用指南</span></a></p> 
<p style="color:#24292f; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#333333">（3）贡献代码：PR和Issue；</span></p> 
<p style="color:#24292f; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#333333">（4）答疑：热心为开发者答疑，如社区群回答开发者问题、issue答疑等；</span></p> 
<p style="color:#24292f; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#333333">（5）其他：沙箱体验、参与活动、成为社区志愿者等。</span></p>
                                        </div>
                                      
</div>
            