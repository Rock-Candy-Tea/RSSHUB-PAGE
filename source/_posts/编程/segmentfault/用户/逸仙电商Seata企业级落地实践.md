
---
title: '逸仙电商Seata企业级落地实践'
categories: 
 - 编程
 - segmentfault
 - 用户
headimg: 'https://segmentfault.com/img/bVcRhgz'
author: segmentfault
comments: false
date: 2021-04-15 12:10:39
thumbnail: 'https://segmentfault.com/img/bVcRhgz'
---

<div>   
<p>简介：本文将会以逸仙电商的业务作为背景， 先介绍一下seata的原理， 并给大家进行线上演示， 由浅入深去介绍这款中间件， 以便读者更加容易去理解 Seata 这个中间件。<br>作者 | 张嘉伟（GitHub ID：l81893521）<br>就职于逸仙电商交易中心；Seata Committer，加入 Seata 社区已有一年半，见证了从 Fescar 到 Seata 的变更，GA等。<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgz" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>你可能没有听说过逸仙电商，但是你的女朋友不可能没有听说过它。逸仙电商旗下有完美日记、小奥汀、完子心选等品牌。完美日记作为国货美妆界的黑马用了不到三年时间，达到了行业龙头企业通常需要十年以上才能达到的营收规模。2020 年正式登陆纽约证券交易所，成为第一家在美国上市的“国货美妆品牌”。在快速增长的业务下，系统流量增长速度越来越快，服务数量不断增多，调用链路错综复杂，数据不一致的问题日渐显现，为了降低人力成本和系统资源，我们选择了 Seata。<br>本文将会以逸仙电商的业务作为背景， 先介绍一下seata的原理， 并给大家进行线上演示， 由浅入深去介绍这款中间件， 以便读者更加容易去理解 Seata 这个中间件。<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgA" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><ol><li>问题背景<br>在微服务的架构下，数据不一致的产生原因</li><li>业务介绍<br>挑选了逸仙电商一些比较简单易懂的业务作为开展背景</li><li>原理分析<br>Seata的实现原理和故障解决以及部署方案</li><li>Demo演示<br>如何在线体验这款中间件，无需整合和下载任何代码<br>数据不一致的原因<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgC" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></li></ol><p>在微服务的环境下，由于调用链路跨越多个应用，甚至跨越多个数据源，数据的一致性在普通情况下难以保证，导致数据不一致的原因非常多，这里列举了三个最常见的原因</p><ol><li>业务异常一个服务链路调用中，如果调用的过程出现业务异常，产生异常的应用独立回滚，非异常的应用数据已经持久化到数据库。</li><li>网络异常调用的过程中，由于网络不稳定，导致链路中断，部分应用业务执行完成，部分应用业务未被执行。</li><li>服务不可用若服务不可用，无法被正常调用，也会导致问题的产生<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgE" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></li></ol><p>这里挑选了逸仙电商业务体系里面一个非常通俗容易理解的调用方式，并且去掉了多余复杂的链路，方便在阅读过程中更加关注重点。<br>在以往如果出现数据不一致的问题，相信大多数的解决方案是这样的<br>• 人工补偿数据<br>• 定时任务检查和补偿数据<br>但是这两种方式的缺点也是显然意见的，一种是浪费大量的人力成本和时间，另外一种是浪费大量的系统资源去检查数据是否一致和额外的人力成本。<br>接下来我会根据逸仙在生产上稳定运行将近一年总结的经验并且尽可能简单的去描述Seata是如何保证数据一致的。<br>原理<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgH" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>在接触一项新技术之前，我们应该先从宏观的角度去理解它大概包含些什么。在Seata中，它大概分为以下三个角色。<br>• 黄色，Transaction Manager（TM），client端<br>• 蓝色，Resource Manager（RM），client端<br>• 绿色，Transaction Coordinator（TC），server端<br>你可以根据颜色，名字，缩写甚至客户端/服务端去区分这三者的关系，同时简单去理解它们每一个自身的职责大概是要干些什么事情，后面的讲解我也会保持一样的颜色和名字来区分它们。<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgK" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>Seata其中只一个核心是数据源代理，意味着在你执行一句Sql语句时，Seata会帮你在执行之前和之后做一些额外的操作，从而保证数据的一致性，并且尽可能做到无感知，让你使用起来感觉非常方便和神奇。这里首先要去理解两个知识点。<br>• 前置镜像（Before Image）：保存数据变更前的样子<br>• 后置镜像（After Image）：保存数据变更后的样子<br>• Undo Log：保存镜像<br>有时候新项目接入的时候，有同事会问，为什么事务不生效，如果你也遇到过同样的问题，那首先要检查一下自己的数据源是否已经代理成功。<br>当执行一句Sql时，Seata会尝试去获取这条/批数据变更前的内容，并保存到前置镜像中（Insert语句没有前置镜像），然后执行业务Sql，执行完后会尝试去获取这条/批数据变更后的内容，并保存到后置镜像中（Delete语句没有后置镜像），之后会进行分支事务注册，TC在收到分支事务注册请求时，会持久化这些分支事务信息和根据操作数据的主键为维度作为全局锁并持久化，可选持久化方式有<br>• file<br>• db<br>• redis<br>在收到TC返回的分支注册成功响应后，会把镜像持久化到应用所在的数据源的Undo Log表中，最后提交本地事务。<br>以上所有操作都会保证在同一个本地事务中，保证业务操作和Undo Log操作的原子性<br>一阶段<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgL" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>理解了单个应用的处理流程，再从一个完全的调用链路，去看Seata的处理过程，相信理解起来会简单很多，</p><ol><li>首先一个使用了@GlobalTransactional的接口被调用，Seata会对其进行拦截，拦截的角色我们称之为TM，这个时候会访问TC开启一个新的全局事务，TC收到请求后会生成XID和全局事务信息并持久化，然后返回XID。</li><li>在每一层的调用链路中，XID都必须往下传递，然后每一层都经过之前说过的处理逻辑，直到执行完成/异常抛出。<br>直到目前，一阶段已经执行完成。<br>另外一个需要注意的问题是，如果发现事务不生效，需要检查XID是否成功往下传递<br>二阶段提交<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgN" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></li></ol><p>如果在整个调用链路的过程，没有发生任何异常，那么二阶段提交的过程是非常简单而且非常的高效，只有两步<br>• TC清理全局事务对应的信息<br>• RM清理对应Undo Log信息<br>二阶段回滚<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgP" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>若调用过程中出现异常，会自动触发反向回滚<br>反向回滚表示，如果调用链路顺序为 A -> B -> C，那么回滚顺序为 C -> B -> A。<br>例：A=Insert，B=Update，如果回滚时不按照反向的顺序进行回滚，则有可能出现回滚时先把A删除了，再更新A，引发错误<br>在回滚的过程中有可能会遇到一种非常极端的情况，回滚到对应的模块时，找不到对应的Undo Log，这种情况主要发生在<br>• 分支事务注册成功，但是由于网络原因收不到成功的响应，Undo Log未被持久化<br>• 同时全局事务超时(超时时间可自由配置)触发回滚<br>这时候RM会持久化一个特殊的Undo Log，状态为GlobalFinished。由于这个全局事务已经回滚，需要防止网络恢复时，未持久化Undo Log的应用收到了分支注册成功的响应和持久化Undo Log，并提交本地最终引发的数据不一致。<br>读已提交<br>由于在一阶段的时候，数据已经保存到数据库并提交，所以Seata默认的隔离级别为读未提交，如果需要把隔离级别提升至读已提交则需要使用@GlobalLock标签并且在查询语句上加上for update<br>@GlobalLock<br>@Transactional<br>public PayMoneyDto detail(ProcessOnEventRequestDto processOnEventRequestDto) &#123;</p><pre><code>return baseMapper.detail(processOnEventRequestDto.getProcessInfoDto().getBusinessKey())</code></pre><p>&#125;<br>@Mapper<br>public interface PayMoneyMapper extends BaseMapper<PayMoney> &#123;</p><pre><code>
@Select("select id, name, amount, account, has_repayment, pay_amount from pay_money m where m.business_key = #&#123;businessKey&#125; for update")
PayMoneyDto detail(@Param("businessKey") String businessKey);</code></pre><p>&#125;<br>这个时候Seata会对添加了for update的查询语句进行代理<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgR" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>如果一个全局事务1正在操作，并且未进行二阶段提交/回滚的时候，全局锁是被全局事务1锁持有的，同时另外一个全局事务2尝试去查询相同的数据，由于查询语句被代理，seata会尝试去获取这条数据的全局锁，直到获取成功/失败(重试次数达到配置值)为止。<br>问题<br>在生产上运行接近1年时间，总体来说遇到的问题不算多，解决起来也比较容易，比如以下这个问题<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgT" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>经过排查发现，由于Seata会使用jdbc标准接口尝试获取业务操作所对应的表结构，由于表结构改动频率较少，并且考虑到表结构变更后应用会进行重启，所以会对表结构进行缓存，如果表结构改动后不对应用进行重启，有可能引发构建镜像时出现NullPointerException。下面贴出关键代码<br>@Override<br>public TableMeta getTableMeta(final Connection connection, final String tableName, String resourceId) &#123;</p><pre><code>if (StringUtils.isNullOrEmpty(tableName)) &#123;
    throw new IllegalArgumentException("TableMeta cannot be fetched without tableName");
&#125;
TableMeta tmeta;
final String key = getCacheKey(connection, tableName, resourceId);
//错误关键处，尝试从缓存获取表结构
tmeta = TABLE_META_CACHE.get(key, mappingFunction -> &#123;
    try &#123;
        return fetchSchema(connection, tableName);
    &#125; catch (SQLException e) &#123;
        LOGGER.error("get table meta of the table `&#123;&#125;` error: &#123;&#125;", tableName, e.getMessage(), e);
        return null;
    &#125;
&#125;);
if (tmeta == null) &#123;
    throw new ShouldNeverHappenException(String.format("[xid:%s]get table meta failed," +
                                                       " please check whether the table `%s` exists.", RootContext.getXID(), tableName));
&#125;
return tmeta;</code></pre><p>&#125;<br>修改表结构，需要对应用进行重启，即可解决此问题，非常简单<br>第二个遇到的问题就是在生产运行一段时间后，发现branch_table和lock_table存在数据残留，并且根据xid查询global_table没有对应的数据，导致后续操作相同的数据行会出现获取全局锁失败，并且会每隔一段时间小量出现。这个异常隐藏的比较深，而且在开发环境和测试环境无法复现，通过跟踪源码和总结原因发现，是由于开启了Mysql主从，导致提交/回滚时，Seata通过xid查询分支事务时，数据未同步到从库，导致遗漏了一部分分支事务数据。<br>源码部分<br>@Override<br>public GlobalStatus commit(String xid) throws TransactionException &#123;</p><pre><code>//根据xid查询信息，如果开启主从，会有可能导致查询信息不完整
GlobalSession globalSession = SessionHolder.findGlobalSession(xid);
if (globalSession == null) &#123;
    return GlobalStatus.Finished;
&#125;
globalSession.addSessionLifecycleListener(SessionHolder.getRootSessionManager());
// just lock changeStatus
boolean shouldCommit = SessionHolder.lockAndExecute(globalSession, () -> &#123;
    // Highlight: Firstly, close the session, then no more branch can be registered.
    globalSession.closeAndClean();
    if (globalSession.getStatus() == GlobalStatus.Begin) &#123;
        if (globalSession.canBeCommittedAsync()) &#123;
            globalSession.asyncCommit();
            return false;
        &#125; else &#123;
            globalSession.changeStatus(GlobalStatus.Committing);
            return true;
        &#125;
    &#125;
    return false;
&#125;);
if (shouldCommit) &#123;
    boolean success = doGlobalCommit(globalSession, false);
    //If successful and all remaining branches can be committed asynchronously, do async commit.
    if (success && globalSession.hasBranch() && globalSession.canBeCommittedAsync()) &#123;
        globalSession.asyncCommit();
        return GlobalStatus.Committed;
    &#125; else &#123;
        return globalSession.getStatus();
    &#125;
&#125; else &#123;
    return globalSession.getStatus() == GlobalStatus.AsyncCommitting ? GlobalStatus.Committed : globalSession.getStatus();
&#125;</code></pre><p>&#125;<br>@Override<br>public GlobalStatus rollback(String xid) throws TransactionException &#123;</p><pre><code>//根据xid查询信息，如果开启主从，会有可能导致查询信息不完整
GlobalSession globalSession = SessionHolder.findGlobalSession(xid);
if (globalSession == null) &#123;
    return GlobalStatus.Finished;
&#125;
globalSession.addSessionLifecycleListener(SessionHolder.getRootSessionManager());
// just lock changeStatus
boolean shouldRollBack = SessionHolder.lockAndExecute(globalSession, () -> &#123;
    globalSession.close(); // Highlight: Firstly, close the session, then no more branch can be registered.
    if (globalSession.getStatus() == GlobalStatus.Begin) &#123;
        globalSession.changeStatus(GlobalStatus.Rollbacking);
        return true;
    &#125;
    return false;
&#125;);
if (!shouldRollBack) &#123;
    return globalSession.getStatus();
&#125;
doGlobalRollback(globalSession, false);
return globalSession.getStatus();</code></pre><p>&#125;<br>相信此问题会在支持Raft之后得到完美的解决<br>pr: <a href="https://github.com/seata/seata/pull/3086" rel="nofollow">https://github.com/seata/seat...</a><br>有兴趣的朋友也可以尝试去review一下代码<br>部署-高可用<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgU" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>Seata和其他中间件的高可用部署方式差别不大，如图片所示，确保应用服务和TC访问相同的注册中心和配置中心，同时只需要启动多台TC，并将store.mode改为db模式即可完成高可用部署，并选择合适的注册中心和配置中心即可，目前支持的配置中心有<br>• nacos<br>• consul<br>• etcd3<br>• eureka<br>• redis<br>• sofa<br>• zookeeper<br>可选的配置中心有<br>• nacos<br>• etcd3<br>• consul<br>• apollo<br>• zk<br>部署-单节点多应用<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhgW" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>当然也有更加灵活的部署方式，通过vgoup-mapping（事务集群），可以做到单节点多应用的隔离，比如A应用和B应用访问A-Group的两个TC，C应用和D应用访问B-Group的两个TC，E应用和F应用访问C-Group的两个TC。<br>部署-异地容灾<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhg0" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span><br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRhg1" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>通过vgoup-mapping也可以做到异地容灾，当原有集群出现不可用时，可以通过变更配置立刻转移到备用的集群上。此处以Nacos作为注册中心举例，TC配置方式如下：</p><h1>广州机房</h1><p>registry &#123;<br>  # file 、nacos 、eureka、redis、zk、consul、etcd3、sofa<br>  type = "nacos"<br>  loadBalance = "RandomLoadBalance"<br>  loadBalanceVirtualNodes = 10<br>  nacos &#123;</p><pre><code>application = "seata-server"
serverAddr = "127.0.0.1:8848"
group = "SEATA_GROUP"
namespace = ""
cluster = "Guangzhou"
username = ""
password = ""</code></pre><p>&#125;<br>&#125;</p><h1>上海机房</h1><p>registry &#123;<br>  # file 、nacos 、eureka、redis、zk、consul、etcd3、sofa<br>  type = "nacos"<br>  loadBalance = "RandomLoadBalance"<br>  loadBalanceVirtualNodes = 10<br>  nacos &#123;</p><pre><code>application = "seata-server"
serverAddr = "127.0.0.1:8848"
group = "SEATA_GROUP"
namespace = ""
cluster = "Shanghai"
username = ""
password = ""</code></pre><p>&#125;<br>&#125;<br><a href="https://developer.aliyun.com/article/783527?utm_content=g_1000263028" rel="nofollow">原文链接</a><br>本文为阿里云原创内容，未经允许不得转载。</p>  
</div>
            