
---
title: 'Seata 1.5.1 发布，支持用户控制台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-73372e23f9f09a75169a8f322e60015e1d9.png'
author: 开源中国
comments: false
date: Wed, 01 Jun 2022 07:20:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-73372e23f9f09a75169a8f322e60015e1d9.png'
---

<div>   
<div class="content">
                                                                                            <p>Seata 1.5.1 正式发布。</p> 
<p style="color:#048836; margin-left:0; margin-right:0"><span>发</span><span>布</span><span>概</span><span>览</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:start">主要新增特性：支持用户控制台，支持Skywalking tracing集成，支持bRPC、EDAS Hsf, 支持 kotlin 协程，支持 TCC幂等/空回滚/防悬挂，支持分布式任务调度，支持 Redis 存储lua模式，支持ON DUPLICATE KEY UPDATE 等语法解析。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:start">此次 release  修改文件数：872，最终代码变动：+60830，-9435 ，参与代码 commit 人数：60+，合并pr数：230，其中：feature：30+，bugfix：60+，优化重构测试及其他：100+。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:start">https://github.com/seata/seata/milestone/15</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:start"><span>此</span><span>版</span><span>本</span><span>是</span><span>目</span><span>前</span><span>参</span><span>与</span><span>代</span><span>码</span><span>提</span><span>交</span><span>人</span><span>数</span><span>最</span><span>多</span><span>和合并pr</span><span>最</span><span>多</span><span>的</span><span>版</span><span>本。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:start"><strong>控制台预览：</strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-73372e23f9f09a75169a8f322e60015e1d9.png" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:start"><strong>SkyWalking：</strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-bd06a7a4297bafc00c9f322199ea3573476.png" referrerpolicy="no-referrer"></p> 
<p style="color:#048836; margin-left:0; margin-right:0"><span>版</span><span>本</span><span>的主要</span><span>更</span><span>新</span><span>如</span><span>下</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#24292e">f</span><span style="color:#24292e">e</span><span style="color:#24292e">a</span><span style="color:#24292e">t</span><span style="color:#24292e">u</span><span style="color:#24292e">r</span><span style="color:#24292e">e</span><span style="color:#24292e">：</span></strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4115] 支持用户控制台</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3652] 支持 APM SkyWalking 集成</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3472] 添加 redisLocker 的 lua 模式</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3575] 支持对锁和会话不同存储的混合使用</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3009] 支持 server 端以 springboot  的方式的启动</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3374] 支持 MySQL INSERT ON DUPLICATE KEY UPDATE</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3642] TCC 模式支持使用 API 的形式进行二阶段参数传递</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3064] 支持可配置 GlobalTransactionInterceptor 和 TccActionInterceptor 的order值</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#2852] 支持自定义 GlobalTransactionScanner 的扫描对象。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3683] 支持 Redis 分布式锁来避免多TC竞争执行任务</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3545] TCC 模式支持幂等控制、防悬挂和空回滚</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3823] TCC 模式二阶段方法参数列表支持自定义</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3642] TCC 模式一阶段支持 BusinessActionContext 隐式传递</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3856] 支持 Edas-Hsf RPC 框架</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3869] 支持从环境 ENV 获取配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#2568] 支持 GlobalTransactionInterceptor 配置切面表达式</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3886] 支持注册中心注册 ip 的网络偏好设置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3906] 支持 SPI 卸载</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3668] 支持 kotlin 协程</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3968] 支持 bRPC-java RPC框架</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4268] 增加控制台 Global Session页面File模式实现</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4281] 增加控制台 Global Session页面和Global LockRedis模式实现</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4293] 增加控制台 Global Lock页面File模式实现</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4335] 实现配置中心上传配置交互脚本(nacos,etcd3)</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4360] 实现配置中心上传配置交互脚本(apollo,consul,zk)</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4320] 实现控制台db模式全局事务、锁查询接口</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4435] 控制台前端页面实现</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4480] 实现 DefaultAuthSigner 的默认签名加密方法</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3487] 增加分布式锁的 DB 实现</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3951] 支持 zstd 压缩</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#2838] Saga 支持 springboot 项目的自动配置</span></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#24292e">b</span><span style="color:#24292e">u</span><span style="color:#24292e">g</span><span style="color:#24292e">f</span><span style="color:#24292e">i</span><span style="color:#24292e">x</span><span style="color:#24292e">：</span></strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3497] 修复 TCC 模式并发量较大时线程池导致的超时问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3686] 修复 Apollo 集群配置项错误及NPE错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3716] 修复 findTargetClass 方法的错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3773] 修复 consul 注册中心在自定义集群名下无法获取 TC 集群</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3695] 修复 mariadb 无法创建XA连接的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3783] 修复 store mode 不生效问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3740] 修复在某些情况下，当Saga事务结束时 LocalThread 未被清除的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3792] 修复 Server 无法获取 Redis host的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3828] 修复 StringUtils 抛出 StackOverflowError 的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3817] 修复 TC 在SkyWalking拓扑图节点不汇聚的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3803] 修复 ReflectionUtil 抛出不预期异常问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3879] 修复 PosrgreSQL多schema无法找到channel问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3881] 修复不存在的相同 DataId 不同默认值返回相同值的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3897] 修复 FastjsonUndoLogParser 中 localdatatime类型不能回滚的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3901] 修复 seataio/seata-server 镜像中 servlet-api 冲突无法启动问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3931] 修复 线程池拒绝执行情况下,dump内存文件名和路径错误的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3949] 修复 nacos-config.py 空白选项的问题和内容丢失的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3988] 修复 nacos 的密码带有特殊字符导致用户名不存在问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3978] 修复 future timeout 引发的 NPE 问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3998] 修复 jedis multi.exec 的 NPE 问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4011] 修复 springboot下无法获取distributed-lock-table配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4023] 修复 dubbo部分场景存在xid未清除的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4032] 修复 server端的ShutdownHook在资源释放时，ApplicationContext已关闭的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4039] 修复本地事务抛出异常后 RM 没有清除xid问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4074] 修复 XA 模式资源悬挂问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4107] 修复项目构建时的死锁问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4158] 修复 logback 无法加载到 RPC_PORT 的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4162] 修复  Redis 注册中心内置配置名导致启动报错问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4165] 修复 StringUtils.toString(obj) 当obj是基本数据数组时，抛出ClassCastException的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4169] 修复 XA 模式originalConnection已关闭，导致二阶段无法执行</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4177] 修复当事务超时且TM发起commit决议时,意外造成全局锁释放的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4174] 修复删除 undolog 时连接关闭问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4189] 修复 kafka-appender.xml 和 logstash-appender.xml 配置文件表达式中的默认值问题。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4213] 修复部分"sessionMode"代码未执行导致启动失败问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4220] 修复 zstd-compressor 模块未合并到 seata-all 中的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4222] 修复字段列表为空时，插入语句无法回滚的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4253] 修复 UpdateExecutor只存储set 字段问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4233] 修复 lock 和 branch 数据残留问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4278] 修复 MySQL 的Blob/Clob/NClob数据类型无法反序列化的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4302] 修复 ORM 可能存在获取不到自增主键值的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4308] 修复PostgreSQL多个schema下存在相同表的TableMetaCache解析问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4326] 修复使用 MariaDB 驱动程序时无法构建 Executor 的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4355] 修复使用</span><span style="color:#24292e"><span> </span></span><span style="color:#24292e">MySQL</span><span style="color:#24292e"><span> </span></span><span style="color:#24292e">Loadbalance模式resourceId被误判为resourceIds的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4310] 修复通过 SELECT LAST_INSERT_ID 获取数据库自增id失败的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4331] 修复使用 ONLY_CARE_UPDATE_COLUMNS 配置可能出现的脏写校验异常</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4408] 修复容器环境中设置环境变量无效的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4441] 修复Redis 存储模式下查询时未关闭 Pipeline 和分支注册后添加分支session时branchSessions为null的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4438] 修复 file 模式下 GlobalSession 在延迟删除的情况下无法被正常删除的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4432] 修复 ServerApplicationListener无法读取配置中心配置的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4452] 修复 service.disableGlobalTransaction 配置的日志输出错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4449] 修复 Redis 分页查询 NPE 问题,优化readession限制查询条数后均衡返回结果</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4459] 修复 Oracle 和<span> </span></span><span style="color:#24292e">PostgreSQL<span> </span></span><span style="color:#24292e">数据库生成前后镜像失败的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4471] 修复运行时切换事务分组对应集群引起的错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4474] 修复<span> </span></span><span style="color:#24292e">MySQL<span> </span></span><span style="color:#24292e">多位Bit类型字段回滚错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4492] 修复 eureka 注册中心无法动态更新服务列表的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4228] 修复 TC 获取不同 ip 的 RM 连接导致的xa模式资源悬挂问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4561] 修复 allSessions/findGlobalSessions 某些情况下返回null 的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4505] 修复 time类型的fastjson序列化问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4579] 修复 MySQLInsertOrUpdateExecutor的prepareUndoLogAll</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4005] 修复 PK 约束名称与属于PK的唯一索引名称不同</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4062] 修复 Saga 复杂参数序列化问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4199] 修复 RPC TM 请求超时问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4352] 修复 SQL 解析器的一些问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3687] 修复某些场景下无法重试全局锁的问题</span></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#24292e">o</span><span style="color:#24292e">p</span><span style="color:#24292e">t</span><span style="color:#24292e">i</span><span style="color:#24292e">m</span><span style="color:#24292e">i</span><span style="color:#24292e">z</span><span style="color:#24292e">e/test</span><span style="color:#24292e">：</span></strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3700] 优化buildLockKey方法的效率</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3615] 优化二阶段同步提交时全局事务记录可异步删除</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3689] 修正script/server/config/file.properties中属性编写错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3588] 优化数据源自动代理的流程</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3528] 优化Redis存储模式内存占用</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3626] 移除重复的changeStatus代码</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3722] 添加分布式锁的代码</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3713] 统一enableClientBatchSendRequest的默认值</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3120] 优化Configuration的部分代码，并添加单元测试</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3735] 当TC只有单个节点时，不进行非必要的负载均衡操作</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3770] 关闭一些未关闭的对象</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3627] 使用TreeMap替换 TableMeta 中的 LinkedHashMap 以兼容高版本的MySQL</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3760] 优化seata-server的logback相关的配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3765] 将添加配置类的操作从AutoConfiguration转移到EnvironmentPostProcessor中并提升该操作的优先级</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3730] 重构TCC模式相关的代码</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3820] 在表tcc_fence_log中新增字段action_name</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3738] JacksonUndoLogParser支持解析LocalDateTime(支持微秒时间)</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3794] 优化seata-server的打包配置，修正Dockerfile的错误配置，并将Dockerfile也打包进去</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3795] 优化zkRegistrylookup方法性能</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3840] 优化apm-skwalking操作方法生成规则</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3834] 优化seata-distribution增加apm-seata-skywalking包</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3847] 优化ConcurrentHashMap.newKeySet替换ConcurrentSet</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3849] 优化字符串拼接</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3890] 优化insert后镜像仅查询插入字段</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3895] 优化解码异常</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3212] 优化解析OrderBy，Limit条件代码结构</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3898] 增加docker maven 插件</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3904] 增强 metrics 和修复 seata-server 单测不运行的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3905] 优化 nacos-config.sh 支持 ash</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3935] 优化以Redis为注册中心时,发送多条命令使用pipeline</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3916] 优化注册中心服务节点列表地址探活</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3918] 缓存Field和Method的反射结果</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3311] 支持从consul单一key中读取所有配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3907] 优化设置 Server 端口</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3912] 支持通过env配置JVM参数</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3939] 使用map优化大量的判断代码</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3955] 添加启动banner</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4266] 修改由于修改记录过多导致分支注册及lock释放失败的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3949] nacos-config.py 支持默认参数和选择性输入参数</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3954] 移除对druid依赖中过期方法的调用</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3981] 优化服务端口的优先级设置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4013] 优化可用TC地址检测</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3982] 优化 readme 文档和升级POM依赖</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3991] 关闭SpringBoot下无用的fileListener</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3994] 优化tcc_fence_log表定时删除任务的机制</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3327] 支持从etcd3单一key中读取所有配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4001] 支持从Nacos,Zookeeper,Consul,Etcd3 中读取 yml</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4017] 优化文件配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4018] 优化 Apollo 配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4021] 优化 Nacos、Consul、Zookeeper、Etcd3 配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4055] 优化NetUtil的getLocalAddress0方法</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4086] 分支事务支持懒加载并优化任务调度</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4056] 优化 DurationUtil</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4103] 减少分支事务注册无需竞争锁时的内存占用</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3733] 优化本地事务下的锁竞争机制</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4144] 支持默认的事务分组配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4157] 优化客户端批量发送请求</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4191] RPC 请求超时时间支持配置化</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4216] 非 AT 模式无须清理undolog表</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4176] 优化 Redis 注册中心存储，改用自动过期key替代hash.</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4196] TC 批量响应客户端</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4212] 控制台接口合并优化</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4237] 当所有的 before image均为空的时候，跳过 checkLock 的步骤</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4251] 优化部分代码处理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4262] 优化 TCC 模块代码处理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4235] 优化 eureka 注册中心保存实例信息</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4277] 优化 Redis-pipeline模式本地事务下的锁竞争机制</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4284] 支持 MSE-Nacos 的 ak/sk 鉴权方式</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4299] 优化异常提示</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4300] 优化NettyRemotingServer的close()</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4270] 提高全局提交和全局回滚的性能，分支事务清理异步化</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4307] 优化在 TCC 模式减少不必要的全局锁删除</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4303] tcc_fence_log表悬挂日志记录异步删除</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4328] 配置上传脚本支持注释</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4305] 优化 TC 端全局锁获取失败时的日志打印</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4336] 添加 AT 模式不支持的SQL语句异常提示</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4359] 支持配置元数据读取环境变量</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4353] seata-all.jar 瘦身。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4393] Redis & DB 模式下启动不需要reload</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4247] 在github actions上，添加基于 java17 和 springboot 各版本的测试</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4400] 异步二阶段任务支持并行处理提升效率</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4391] commit/rollback 重试超时事件</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4282] 优化回滚镜像构建逻辑</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4276] 修复 seata-test 单测不运行的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4407] file模式下无需延迟删除globasession</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4436] 优化file模式下的global session查询接口</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4431] 优化Redis模式查询globalSession限制查询条数</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4465] 优化TC 批量响应客户端模式客户端版本传输方式</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4469] 优化控制台db模式下获取配置的方式</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4478] 优化 Nacos 配置和注册元数据属性</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4522] 优化 GC 参数</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4517] 增强失败/超时状态的监控</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4451] fileSessionManager改为单例并优化任务线程池处理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4551] 优化 metrics rt 统计问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4574] 支持 accessKey/secretKey 配置自动注入</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4583] DefaultAuthSigner 的默认签名加密方法替换为HmacSHA256</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4591] 优化开关默认值</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3780] 升级 Druid 版本</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3797] 支持在Try 方法外由用户自己实例化BusinessActionContext</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3909] 优化collectRowLocks 方法</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3763] 优化 github actions</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4345] 修正包目录名</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4346] 优化服务器日志并移除lombok</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4348] 统一管理maven插件及其版本</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4354] 优化saga测试用例</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4227] 统一管理依赖的版本，并且升级spring-boot到2.4.13</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4453] 升级 eureka-clients 和 xstream 的版本</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4481] 优化nacos配置和命名属性</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4477] 优化调试级别日志并修复拼写错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4484] 优化TM/RM注册时TC的日志打印</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4458] 修复 metrices 模块 README.md 的配置遗漏问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4482]</span><span style="color:#24292e"><span> </span></span><span style="color:#24292e">[#3654]<span> </span></span><span style="color:#24292e">修复typos</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3880] 贡献文档增加中文版本</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4134] 初始化控制台基础代码</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3870] 让seata-bom成为真正的Bill-Of-Material</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3889] 支持</span><span style="color:#24292e">注册中心添</span><span style="color:#24292e">加心跳</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3702] 修改注释</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4608]</span><span style="color:#24292e"><span> </span></span><span style="color:#24292e">[#3110]</span><span style="color:#24292e">修复测试用例</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4163] 完善开发者奉献文档</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#3678] 补充遗漏的配置及新版本pr登记md文件</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4449] 优化 Redis limit 并修复 Redis 分页问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4535] 修复 FileSessionManagerTest单测错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#24292e">[#4025] 优化潜在的数据库资源泄露</span></p> </li> 
</ul> 
<p><strong><span>英</span><span>文</span><span>版</span><span>：</span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Freleases%2Ftag%2Fv1.5.1" target="_blank">https://github.com/seata/seata/releases/tag/v1.5.1</a></p>
                                        </div>
                                      
</div>
            