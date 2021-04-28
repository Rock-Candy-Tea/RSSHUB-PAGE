
---
title: '6 张图带你彻底搞懂分布式事务 XA 模式'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/5b549b99586dcfae979d311479e89055.png'
author: Dockone
comments: false
date: 2021-04-28 08:08:43
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/5b549b99586dcfae979d311479e89055.png'
---

<div>   
<br>作者 | 朱晋君<br>
来源 |<a href="https://mp.weixin.qq.com/s/Rp8paKc2bQhERBGDKtpMcA"> 阿里巴巴云原生公众号</a><br>
<br>XA 协议是由 X/Open 组织提出的分布式事务处理规范，主要定义了事务管理器 TM 和局部资源管理器 RM 之间的接口。目前主流的数据库，比如 oracle、DB2 都是支持 XA 协议的。<br>
<br>mysql 从 5.0 版本开始，innoDB 存储引擎已经支持 XA 协议，今天的源码介绍实验环境使用的是 mysql 数据库。<br>
<br><h1>两阶段提交</h1>分布式事务的两阶段提交是把整个事务提交分为 prepare 和 commit 两个阶段。以电商系统为例，分布式系统中有订单、账户和库存三个服务，如下图：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210426/5b549b99586dcfae979d311479e89055.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/5b549b99586dcfae979d311479e89055.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>第一阶段，事务协调者向事务参与者发送 prepare 请求，事务参与者收到请求后，如果可以提交事务，回复 yes，否则回复 no。<br>
<br>第二阶段，如果所有事务参与者都回复了 yes，事务协调者向所有事务参与者发送 commit 请求，否则发送 rollback 请求。<br>
<br>两阶段提交存在三个问题：<br>
<ul><li>同步阻塞，本地事务在 prepare 阶段锁定资源，如果有其他事务也要修改 xiaoming 这个账户，就必须等待前面的事务完成。这样就造成了系统性能下降。</li><li>协调节点单点故障，如果第一个阶段 prepare 成功了，但是第二个阶段协调节点发出 commit 指令之前宕机了，所有服务的数据资源处于锁定状态，事务将无限期地等待。</li><li>数据不一致，如果第一阶段 prepare 成功了，但是第二阶段协调节点向某个节点发送 commit 命令时失败，就会导致数据不一致。</li></ul><br>
<br><h1>三阶段提交</h1>为了解决两阶段提交的问题，三阶段提交做了改进：<br>
<ul><li>在协调节点和事务参与者都引入了超时机制。</li><li>第一阶段的 prepare 阶段分成了两步，canCommi 和 preCommit。</li></ul><br>
<br>如下图：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210426/9c7a4da33f1e61f51c04018be467c8ef.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/9c7a4da33f1e61f51c04018be467c8ef.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>引入 preCommit 阶段后，协调节点会在 commit 之前再次检查各个事务参与者的状态，保证它们的状态是一致的。但是也存在问题，那就是如果第三阶段发出 rollback 请求，有的节点没有收到，那没有收到的节点会在超时之后进行提交，造成数据不一致。<br>
<br><h1>XA 事务语法介绍</h1>xa 事务的语法如下：<br>
1. 三阶段的第一阶段：开启 xa 事务，这里 xid 为全局事务 id：<br>
<br><code class="prettyprint">XA &#123;START|BEGIN&#125; xid [JOIN|RESUME]</code><br>
<br>结束 xa 事务：<br>
<br><code class="prettyprint">XA END xid [SUSPEND [FOR MIGRATE]]</code><br>
<ol><li>三阶段的第二阶段，即 prepare：</li></ol><br>
<br><code class="prettyprint">XA PREPARE xid</code><br>
<ol><li>三阶段的第三阶段，即 commit/rollback：</li></ol><br>
<br><code class="prettyprint">XA COMMIT xid [ONE PHASE]<br>
XA ROLLBACK xid</code><br>
<ol><li>查看处于 PREPARE 阶段的所有事务：</li></ol><br>
<br><code class="prettyprint">XA RECOVER XA RECOVER [CONVERT XID]</code><br>
<br><h1>seata XA 简介</h1>seata 是阿里推出的一款开源分布式事务解决方案，目前有 AT、TCC、SAGA、XA 四种模式。<br>
<br>seata 的 XA 模式是利用分支事务中数据库对 XA 协议的支持来实现的。我们看一下 seata 官网的介绍：[1]<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210426/6e4974b0547ce412f47288b33ae56ef4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/6e4974b0547ce412f47288b33ae56ef4.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>从上面的图可以看到，seata XA 模式的流程跟其他模式一样：<br>
<ol><li>TM 开启全局事务</li><li>RM 向 TC 注册分支事务</li><li>RM 向 TC 报告分支事务状态</li><li>TC 向 RM 发送 commit/rollback 请求</li><li>TM 结束全局事务</li></ol><br>
<br>这里介绍一下 RM 客户端初始化关联的 UML 类图：[2]<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210426/10dee4f5176bf941090d34b652ef2db3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/10dee4f5176bf941090d34b652ef2db3.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>这个图中有一个类是 AbstractNettyRemotingClient，这个类的内部类 ClientHandler 来处理 TC 发来的请求并委托给父类 AbstractNettyRemoting 的 processMessage 方法来处理。processMessage 方法调用 RmBranchCommitProcessor 类的 process 方法。<br>
<br>需要注意的是，<strong>「seata 的 xa 模式对传统的三阶段提交做了优化，改成了两阶段提交」</strong>:<br>
<ul><li>第一阶段首执行 XA 开启、执行 sql、XA 结束三个步骤，之后直接执行 XA prepare。</li><li>第二阶段执行 XA commit/rollback。</li></ul><br>
<br>mysql 目前是支持 seata xa 模式的两阶段优化的。<br>
<br><strong>「但是这个优化对 oracle 不支持，因为 oracle 实现的是标准的 xa 协议，即 xa end 后，协调节点向事务参与者统一发送 prepare，最后再发送 commit/rollback。这也导致了 seata 的 xa 模式对 oracle 支持不太好。」</strong><br>
<br><h1>seata XA 源码</h1>seata 中的 XA 模式是使用数据源代理来实现的，需要手动配置数据源代理，代码如下：<br>
<br>```<br>
@Bean<br>
@ConfigurationProperties(prefix = "spring.datasource")<br>
public DruidDataSource druidDataSource() &#123;<br>
    return new DruidDataSource();<br>
&#125;<br>
<br>@Bean("dataSourceProxy")<br>
public DataSource dataSource(DruidDataSource druidDataSource) &#123;<br>
    return new DataSourceProxyXA(druidDataSource);<br>
&#125;<br>
```<br>
<ul><li>也可以根据普通 DataSource 来创建 XAConnection，但是这种方式有兼容性问题（比如 oracle），所以 seata 使用了开发者自己配置 XADataSource。</li><li>seata 提供的 XA 数据源代理，要求代码框架中必须使用 druid 连接池。</li></ul><br>
<br><h2>1. XA 第一阶段</h2>当 RM 收到 DML 请求后，seata 会使用 ExecuteTemplateXA来执行，执行方法 execute 中有一个地方很关键，就是把 autocommit 属性改为了 false，而 mysql 默认 autocommit 是 true。事务提交之后，还要把 autocommit 改回默认。<br>
<br>下面我们看一下 XA 第一阶段提交的主要代码。<br>
<br><h3><strong>1）开启 XA</strong></h3>上面代码标注[1]处，调用了 ConnectionProxyXA 类的 setAutoCommit 方法，这个方法的源代码中，XA start 主要做了三件事：<br>
<ul><li>向 TC 注册分支事务</li><li>调用数据源的 XA Start</li></ul><br>
<br><code class="prettyprint">xaResource.start(this.xaBranchXid, XAResource.TMNOFLAGS);</code><br>
<ul><li>把 xaActive 设置为 true</li></ul><br>
<br>RM 并没有直接使用 TC 返回的 branchId 作为 xa 数据源的 branchId，而是使用全局事务 id(xid) 和 branchId 重新构建了一个。<br>
<br><h3><strong>2）执行 sql</strong></h3>调用 PreparedStatementProxyXA 的 execute 执行 sql。<br>
<br><h3><strong>3）XA end/prepare</strong></h3><code class="prettyprint">public void commit() throws SQLException &#123;<br>
    //省略部分源代码<br>
    try &#123;<br>
        // XA End: Success<br>
        xaResource.end(xaBranchXid, XAResource.TMSUCCESS);<br>
        // XA Prepare<br>
        xaResource.prepare(xaBranchXid);<br>
        // Keep the Connection if necessary<br>
        keepIfNecessary();<br>
    &#125; catch (XAException xe) &#123;<br>
        try &#123;<br>
            // Branch Report to TC: Failed<br>
            DefaultResourceManager.get().branchReport(BranchType.XA, xid, xaBranchXid.getBranchId(),<br>
                BranchStatus.PhaseOne_Failed, null);<br>
        &#125; catch (TransactionException te) &#123;<br>
            //这儿只打印了一个warn级别的日志<br>
        &#125;<br>
        throw new SQLException(<br>
            &quot;Failed to end(TMSUCCESS)/prepare xa branch on &quot; + xid + &quot;-&quot; + xaBranchXid.getBranchId() + &quot; since &quot; + xe<br>
                .getMessage(), xe);<br>
    &#125; finally &#123;<br>
        cleanXABranchContext();<br>
    &#125;<br>
&#125;</code><br>
<br>从这个源码我们看到，commit 主要做了三件事：<br>
<ul><li>调用数据源的 XA end</li><li>调用数据源的 XA prepare</li><li>向 TC 报告分支事务状态</li></ul><br>
<br>到这里我们就可以看到，seata 把 xa 协议的前两个阶段合成了一个阶段。<br>
<br><h2>2. XA commit</h2>这里的调用关系用一个时序图来表示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210426/c68fae4461646520f47024d37e36b875.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/c68fae4461646520f47024d37e36b875.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>看一下 RmBranchCommitProcessor 类的 process 方法，代码如下：<br>
<br><code class="prettyprint">@Override<br>
public void process(ChannelHandlerContext ctx, RpcMessage rpcMessage) throws Exception &#123;<br>
    String remoteAddress = NetUtil.toStringAddress(ctx.channel().remoteAddress());<br>
    Object msg = rpcMessage.getBody();<br>
    if (LOGGER.isInfoEnabled()) &#123;<br>
        LOGGER.info(&quot;rm client handle branch commit process:&quot; + msg);<br>
    &#125;<br>
    handleBranchCommit(rpcMessage, remoteAddress, (BranchCommitRequest) msg);<br>
&#125;</code><br>
<br>从调用关系时序图可以看出，上面的 handleBranchCommit 方法最终调用了 AbstractRMHandler 的 handle 方法，最后通过 branchCommit 方法调用了 ResourceManagerXA 类的 finishBranch 方法。<br>
ResourceManagerXA 类是 XA 模式的资源管理器，看下面这个类图，也就是 seata 中资源管理器（RM）的 UML 类图：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210426/c85543be438a93c9d8332b6d5a5ed049.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/c85543be438a93c9d8332b6d5a5ed049.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>上面的 finishBranch 方法调用了 connectionProxyXA.xaCommit 方法，我们最后看一下 xaCommit 方法：<br>
<br><code class="prettyprint">public void xaCommit(String xid, long branchId, String applicationData) throws XAException &#123;<br>
    XAXid xaXid = XAXidBuilder.build(xid, branchId);<br>
 //因为使用mysql，这里xaResource是MysqlXAConnection<br>
    xaResource.commit(xaXid, false);<br>
    releaseIfNecessary();<br>
&#125;</code><br>
<br>上面调用了数据源的 commit 方法，提交了 RM 分支事务。<br>
<br>到这里，整个 RM 分支事务就结束了。Rollback 的代码逻辑跟 commit 类似。<br>
<br>最后要说明的是，上面的 xaResource，是 mysql-connector-java.jar 包中的 MysqlXAConnection 类实例，它封装了 mysql 提供的 XA 协议接口。<br>
<br><h1>总结</h1>seata 中 XA 模式的实现是使用数据源代理完成的，底层使用了数据库对 XA 协议的原生支持。<br>
<br>mysql 的 java 驱动库中，MysqlXAConnection 类封装类 XA 协议的底层接口供外部调用。<br>
<br>跟 TCC 和 SAGA 模式需要在业务代码中实现 prepare/commit/rollback 逻辑相比，XA 模式对业务代码无侵入。<br>
<br><h2>Reference</h2>[1]：<a href="http://seata.io/zh-cn/docs/overview/what-is-seata.html">_</a><a href="http://seata.io/zh-cn/docs/overview/what-is-seata.html_" rel="nofollow" target="_blank">http://seata.io/zh-cn/docs/ove ... html_</a><br>
[2]：<a href="https://github.com/seata/seata">_</a><a href="https://github.com/seata/seata_" rel="nofollow" target="_blank">https://github.com/seata/seata_</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            