
---
title: 'Seata 1.4.2 正式发布，向打工人致敬'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6083fa5f2f35eb3426580f42379fae85a95.png'
author: 开源中国
comments: false
date: Sat, 01 May 2021 08:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6083fa5f2f35eb3426580f42379fae85a95.png'
---

<div>   
<div class="content">
                                                                                            <p>Seata 1.4.2 正式发布。Seata 社区向所有打工人致敬，祝大家有一个愉快的假期。</p> 
<p><img alt="up-6083fa5f2f35eb3426580f42379fae85a95.png" src="https://oscimg.oschina.net/oscnet/up-6083fa5f2f35eb3426580f42379fae85a95.png" referrerpolicy="no-referrer"></p> 
<h3>用户登记</h3> 
<p>欢迎已使用用户在此链接登记，便于我们更好的针对业务场景优化：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fissues%2F1246" target="_blank">https://github.com/seata/seata/issues/1246</a></p> 
<h3>发布概览</h3> 
<p>此版本梳理了大部分用户反馈的 bug，对沉积的大部分问题进行了修复。同时增加了mysql antlr sqlparser、undo log压缩、redis-sentinel存储模式、自定义序列化插件、db/redis 密码加解密等特性支持。</p> 
<p>此次 release  修改文件数：361，最终代码变动：+116584，-1862 ，参与代码 commit 人数：40+，合并pr数：93，其中：feature：15，bugfix：29，优化重构测试及其他：49。</p> 
<p>此版本是目前参与代码提交人数最多和贡献代码最多的版本，感谢大家的贡献。</p> 
<h3>此版本的详细更新如下</h3> 
<h3>feature：</h3> 
<ul> 
 <li> <p>[#2933] 支持mysql antlr sqlparser</p> </li> 
 <li> <p>[#3228] 支持自定义序列化插件</p> </li> 
 <li> <p>[#3172] 支持 AT 模式 undo_log 压缩模式</p> </li> 
 <li> <p>[#3372] 支持saga模式下用户自定义是否更新最后一次重试日志</p> </li> 
 <li> <p>[#3411] 支持seata-server 线程池参数可配置</p> </li> 
 <li> <p>[#3348] 支持 TC 存储模式使用 redis-sentinel</p> </li> 
 <li> <p>[#2667] 支持使用db和redis存储模式时密码的加解密</p> </li> 
 <li> <p>[#3427] 支持分布式锁接口</p> </li> 
 <li> <p>[#3443] 支持将seata-server的日志发送到logstash或kafka中</p> </li> 
 <li> <p>[#3486] 支持Metrics增加事务分组属性</p> </li> 
 <li> <p>[#3317] 支持当zookeeper作为配置中心时从单node获取全部配置</p> </li> 
 <li> <p>[#3516] 支持 consul 作为注册中心和配置中心时的 acl-token</p> </li> 
 <li> <p>[#3116] 支持配置 apollo 配置中心配置 configService 和 cluster</p> </li> 
 <li> <p>[#3468] 支持saga模式下任务循环执行</p> </li> 
 <li> <p>[#3447] 支持日志框架中事务上下文的打印</p> </li> 
</ul> 
<h3>bugfix：</h3> 
<ul> 
 <li> <p>[#3258] 修复AsyncWorker潜在的OOM问题</p> </li> 
 <li> <p>[#3293] 修复配置缓存获取值类型不匹配的问题</p> </li> 
 <li> <p>[#3241] 禁止在多SQL的情况下使用 limit 和 order by 语法</p> </li> 
 <li> <p>[#3406] 修复当config.txt中包含特殊字符时无法推送至 nacos 的问题</p> </li> 
 <li> <p>[#3367] 修复最后一个XA分支二阶段时偶发无法回滚的异常</p> </li> 
 <li> <p>[#3418] 修复 getGeneratedKeys 可能会取到历史的主键的问题</p> </li> 
 <li> <p>[#3448] 修复多个锁竞争失败时，仅删除单个锁，并优化锁竞争逻辑提升处理性能</p> </li> 
 <li> <p>[#3408] 修复jar运行模式第三方依赖分离打包时的NPE问题</p> </li> 
 <li> <p>[#3431] 修复在读取配置时Property Bean可能未初始化的问题</p> </li> 
 <li> <p>[#3413] 修复回滚到savepoint以及releaseSavepoint的逻辑</p> </li> 
 <li> <p>[#3451] 修复autoCommit=true，全局锁竞争失败时的脏写问题</p> </li> 
 <li> <p>[#3481] 修复当 consul client 抛出异常时导致刷新任务中断的问题</p> </li> 
 <li> <p>[#3491] 修复README.md文件中的拼写错误</p> </li> 
 <li> <p>[#3531] 修复RedisTransactionStoreManager 获取 brachTransaction 可能的 NPE 问题</p> </li> 
 <li> <p>[#3500] 修复 oracle 和 postgreSql 无法获取 column info 的问题</p> </li> 
 <li> <p>[#3560] 修复 Committing 状态的事务异步任务没有时间阈值和无法进行事务恢复的问题</p> </li> 
 <li> <p>[#3555] 通过setBytes代替setBlob，避免高版本jdbc驱动工作异常</p> </li> 
 <li> <p>[#3540] 修复server发布打包时缺失文件的问题</p> </li> 
 <li> <p>[#3597] 修复可能的 NPE问题</p> </li> 
 <li> <p>[#3568] 修复自动数据源代理因 ConcurrentHashMap.computeIfAbsent 导致的死锁问题</p> </li> 
 <li> <p>[#3402] 修复更新SQL中字段名含有库名无法解析更新列的问题</p> </li> 
 <li> <p>[#3464] 修复测试用例空指针异常和StackTraceLogger中错误的日志格式.</p> </li> 
 <li> <p>[#3522] 修复当 DML 影响行数为0时注册分支和插入undo_log的问题</p> </li> 
 <li> <p>[#3635] 修复zookeeper 配置变更无法推送通知的问题</p> </li> 
 <li> <p>[#3133] 修复某些场景下无法重试全局锁的问题</p> </li> 
 <li> <p>[#3156] 修复嵌套代理类无法 获取target的问题</p> </li> 
</ul> 
<h3>optimize：</h3> 
<ul> 
 <li> <p>[#3341] 优化获取指定配置文件的路径格式问题</p> </li> 
 <li> <p>[#3385] 优化 GitHub Actions 配置,修复单测失败问题</p> </li> 
 <li> <p>[#3175] 支持雪花算法时钟回拨</p> </li> 
 <li> <p>[#3291] 优化mysql连接参数</p> </li> 
 <li> <p>[#3336] 支持使用System.getProperty获取Netty配置参数</p> </li> 
 <li> <p>[#3369] 添加github action的dockerHub秘钥</p> </li> 
 <li> <p>[#3343] 将CI程序从Travis CI迁移到Github Actions</p> </li> 
 <li> <p>[#3397] 增加代码变更记录</p> </li> 
 <li> <p>[#3303] 支持从nacos单一dataId中读取所有配置</p> </li> 
 <li> <p>[#3380] 优化 globalTransactionScanner 中的 DISABLE_GLOBAL_TRANSACTION listener</p> </li> 
 <li> <p>[#3123] 优化 seata-server 打包策略</p> </li> 
 <li> <p>[#3415] 优化 maven 打包时清除 distribution 目录</p> </li> 
 <li> <p>[#3316] 优化读取配置值时属性bean未初始化的问题</p> </li> 
 <li> <p>[#3420] 优化枚举类的使用并添加单元测试</p> </li> 
 <li> <p>[#3533] 支持获取当前事务角色</p> </li> 
 <li> <p>[#3436] 优化SQLType类中的错别字</p> </li> 
 <li> <p>[#3439] 调整springApplicationContextProvider order以使其可以在xml bean之前被调用</p> </li> 
 <li> <p>[#3248] 优化负载均衡配置迁移到client节点下</p> </li> 
 <li> <p>[#3441] 优化starter的自动配置处理</p> </li> 
 <li> <p>[#3466] 优化使用equalsIgnoreCase() 进行字符串比较</p> </li> 
 <li> <p>[#3476] 支持 server 参数传入hostname时自动将其转换为 ip</p> </li> 
 <li> <p>[#3236] 优化执行解锁操作的条件，减少不必要的 unlock 操作</p> </li> 
 <li> <p>[#3485] 删除 ConfigurationFactory 中无用的代码</p> </li> 
 <li> <p>[#3505] 删除 GlobalTransactionScanner 中无用的 if 判断</p> </li> 
 <li> <p>[#3544] 优化无法通过Statement#getGeneratedKeys时，只能获取到批量插入的第一个主键的问题</p> </li> 
 <li> <p>[#3549] 统一DB存储模式下不同表中的xid字段的长度</p> </li> 
 <li> <p>[#3551] 调大RETRY_DEAD_THRESHOLD的值以及设置成可配置</p> </li> 
 <li> <p>[#3589] 使用JUnit API做异常检查</p> </li> 
 <li> <p>[#3601] 使<code>LoadBalanceProperties</code>与<code>spring-boot:2.x</code>及以上版本兼容</p> </li> 
 <li> <p>[#3513] Saga SpringBeanService调用器支持切换 json 解析器</p> </li> 
 <li> <p>[#3318] 支持 CLIENT_TABLE_META_CHECKER_INTERVAL 可配置化</p> </li> 
 <li> <p>[#3371] 支持 metric 按 applicationId 分组</p> </li> 
 <li> <p>[#3459] 删除重复的ValidadAddress代码</p> </li> 
 <li> <p>[#3215] 优化seata-server 在file模式下启动时的reload逻辑</p> </li> 
 <li> <p>[#3631] 优化 nacos-config.py 脚本的入参问题</p> </li> 
 <li> <p>[#3638] 优化 update 和 delete 的 SQL 不支持 join 的错误提示</p> </li> 
 <li> <p>[#3523] 优化当使用oracle时调用releaseSavepoint()方法报异常的问题</p> </li> 
 <li> <p>[#3458] 还原已删除的md</p> </li> 
 <li> <p>[#3574] 修复EventBus.java文件中注释拼写错误</p> </li> 
 <li> <p>[#3573] 修复 README.md 文件中设计器路径错误</p> </li> 
 <li> <p>[#3662] 更新gpg密钥对</p> </li> 
 <li> <p>[#3664] 优化 javadoc</p> </li> 
 <li> <p>[#3637] 登记使用seata的公司和1.4.2版本包含的新增pr信息</p> </li> 
</ul> 
<h3>test</h3> 
<ul> 
 <li> <p>[#3381] 添加 TmClient 的测试用例</p> </li> 
 <li> <p>[#3607] 修复 EventBus 的单元测试问题</p> </li> 
 <li> <p>[#3579] 添加 StringFormatUtils 测试用例</p> </li> 
 <li> <p>[#3365] 修复ParameterParserTest测试用例</p> </li> 
 <li> <p>[#3359] 删除未使用的测试用例</p> </li> 
 <li> <p>[#3383] 优化StatementProxyTest单元测试</p> </li> 
 <li> <p>[#3578] 修复单元测试case里的UnfinishedStubbing异常</p> </li> 
</ul> 
<p>英文版：https://github.com/seata/seata/releases/tag/v1.4.2</p> 
<h3>致谢</h3> 
<p>非常感谢以下 contributors 的代码贡献。若有无意遗漏，请报告。</p> 
<ul> 
 <li> <p>slievrly</p> </li> 
 <li> <p>caohdgege</p> </li> 
 <li> <p>a364176773</p> </li> 
 <li> <p>wangliang181230</p> </li> 
 <li> <p>xingfudeshi</p> </li> 
 <li> <p>jsbxyyx</p> </li> 
 <li> <p>selfishlover</p> </li> 
 <li> <p>l8189352</p> </li> 
 <li> <p>Rubbernecker</p> </li> 
 <li> <p>lj2018110133</p> </li> 
 <li> <p>github-ganyu</p> </li> 
 <li> <p>dmego</p> </li> 
 <li> <p>spilledyear</p> </li> 
 <li> <p>hoverruan</p> </li> 
 <li> <p>anselleeyy</p> </li> 
 <li> <p>Ifdevil</p> </li> 
 <li> <p>lvxianzheng</p> </li> 
 <li> <p>MentosL</p> </li> 
 <li> <p>lian88jian</p> </li> 
 <li> <p>litianyu1992</p> </li> 
 <li> <p>xyz327</p> </li> 
 <li> <p>13414850431</p> </li> 
 <li> <p>xuande</p> </li> 
 <li> <p>tanggen</p> </li> 
 <li> <p>eas5</p> </li> 
 <li> <p>nature80</p> </li> 
 <li> <p>ls9527</p> </li> 
 <li> <p>drgnchan</p> </li> 
 <li> <p>imyangyong</p> </li> 
 <li> <p>sunlggggg</p> </li> 
 <li> <p>long187</p> </li> 
 <li> <p>h-zhi</p> </li> 
 <li> <p>StellaiYang</p> </li> 
 <li> <p>slinpq</p> </li> 
 <li> <p>sustly</p> </li> 
 <li> <p>cznc</p> </li> 
 <li> <p>squallliu</p> </li> 
 <li> <p>81519434</p> </li> 
 <li> <p>luoxn28</p> </li> 
</ul> 
<p>同时，我们收到了社区反馈的很多有价值的issue和建议，非常感谢大家。</p> 
<h3>社区讨论群</h3> 
<h3><strong><img alt height="354" src="https://oscimg.oschina.net/oscnet/up-dcf8bf137fa970b150f82983ff3722501b6.png" width="1080" referrerpolicy="no-referrer"></strong></h3> 
<h3>常用链接</h3> 
<ul> 
 <li> <p><strong>Seata:</strong> https://github.com/seata/seata</p> </li> 
 <li> <p><strong>Samples:</strong> https://github.com/seata/seata-samples</p> </li> 
 <li> <p><strong>Release:</strong> https://github.com/seata/seata/releases</p> </li> 
 <li> <p><strong>官网:</strong> https://seata.io</p> </li> 
</ul> 
<h3>投稿和招聘</h3> 
<p>欢迎大家将 Seata 相关的实践文章投稿至：slievrly@gmail.com</p> 
<p>阿里云-云原生应用平台-中间件招聘：https://github.com/slievrly</p>
                                        </div>
                                      
</div>
            