
---
title: '保姆级教程：用 Go 轻松完成一个分布式事务 TCC'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210927/476ef3a4d6a28e69101a88168740f501.jpg'
author: Dockone
comments: false
date: 2021-10-02 12:11:02
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210927/476ef3a4d6a28e69101a88168740f501.jpg'
---

<div>   
<br>什么是分布式事务？银行跨行转账业务是一个典型分布式事务场景，假设A需要跨行转账给 B，那么就涉及两个银行的数据，无法通过一个数据库的本地事务保证转账的 ACID，只能够通过分布式事务来解决。<br>
<br>分布式事务就是指事务的发起者、资源及资源管理器和事务协调者分别位于分布式系统的不同节点之上。在上述转账的业务中，用户 A - 100 操作和用户 B + 100 操作不是位于同一个节点上。本质上来说，分布式事务就是为了保证在分布式场景下，数据操作的正确执行。<br>
<br>什么是 TCC，TCC 是 Try、Confirm、Cancel 三个词语的缩写，最早是由 Pat Helland 于 2007 年发表的一篇名为《Life beyond Distributed Transactions:an Apostate’s Opinion》的论文提出。<br>
<h3>TCC 组成</h3>TCC 分为3个阶段：<br>
<ul><li>Try 阶段：尝试执行，完成所有业务检查（一致性）, 预留必须业务资源（准隔离性）</li><li>Confirm 阶段：如果所有分支的Try都成功了，则走到 Confirm 阶段。Confirm 真正执行业务，不作任何业务检查，只使用 Try 阶段预留的业务资源</li><li>Cancel 阶段：如果所有分支的 Try 有一个失败了，则走到 Cancel 阶段。Cancel 释放 Try 阶段预留的业务资源。</li></ul><br>
<br>TCC 分布式事务里，有 3 个角色，与经典的 XA 分布式事务一样：<br>
<ul><li>AP/ 应用程序，发起全局事务，定义全局事务包含哪些事务分支</li><li>RM/ 资源管理器，负责分支事务各项资源的管理</li><li>TM/ 事务管理器，负责协调全局事务的正确执行，包括 Confirm，Cancel 的执行，并处理网络异常</li></ul><br>
<br>如果我们要进行一个类似于银行跨行转账的业务，转出（TransOut）和转入（TransIn）分别在不同的微服务里，一个成功完成的TCC事务典型的时序图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210927/476ef3a4d6a28e69101a88168740f501.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210927/476ef3a4d6a28e69101a88168740f501.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>TCC 网络异常</h3>TCC 在整个全局事务的过程中，可能发生各类网络异常情况，典型的是空回滚、幂等、悬挂，由于 TCC 的异常情况，和 SAGA、可靠消息等事务模式有相近的地方，因此我们把所有异常的解决方案统统放在这篇文章<a href="https://zhuanlan.zhihu.com/p/388444465">《还被分布式事务的网络异常困扰吗？一个函数调用帮你搞定它》</a>进行讲解。<br>
<h3>TCC 实践</h3>对于前面的跨行转账操作，最简单的做法是，在 Try 阶段调整余额，在 Cancel 阶段反向调整余额，Confirm 阶段则空操作。这么做带来的问题是，如果 A 扣款成功，金额转入 B 失败，最后回滚，把 A 的余额调整为初始值。在这个过程中如果 A 发现自己的余额被扣减了，但是收款方 B 迟迟没有收到余额，那么会对 A 造成困扰。<br>
<br>更好的做法是，Try 阶段冻结A转账的金额，Confirm 进行实际的扣款，Cancel 进行资金解冻，这样用户在任何一个阶段，看到的数据都是清晰明了的。<br>
<br>下面我们进行一个 TCC 事务的具体开发。<br>
<br>目前可用于 TCC 的开源框架，主要为 Java 语言，其中以 seata 为代表。我们的例子采用 Go 语言，使用的分布式事务框架为 <a href="https://github.com/yedf/dtm">dtm</a>，它对分布式事务的支持非常优雅。下面来详细讲解 TCC 的组成。<br>
<br>我们首先创建两张表，一张是用户余额表，一张是冻结资金表，建表语句如下：<br>
<pre class="prettyprint">CREATE TABLE dtm_busi.`user_account` (<br>
`id` int(11) AUTO_INCREMENT PRIMARY KEY,<br>
`user_id` int(11) not NULL UNIQUE ,<br>
`balance` decimal(10,2) NOT NULL DEFAULT '0.00',<br>
`create_time` datetime DEFAULT now(),<br>
`update_time` datetime DEFAULT now()<br>
);<br>
<br>
CREATE TABLE dtm_busi.`user_account_trading` (<br>
`id` int(11) AUTO_INCREMENT PRIMARY KEY,<br>
`user_id` int(11) not NULL UNIQUE ,<br>
`trading_balance` decimal(10,2) NOT NULL DEFAULT '0.00',<br>
`create_time` datetime DEFAULT now(),<br>
`update_time` datetime DEFAULT now()<br>
); <br>
</pre><br>
trading 表中，trading_balance 记录正在交易的金额。<br>
<br>我们先编写核心代码，冻结/解冻资金操作，会检查约束 balance + trading_balance >= 0，如果约束不成立，执行失败。<br>
<pre class="prettyprint">func adjustTrading(uid int, amount int) (interface&#123;&#125;, error) &#123;<br>
幂等、悬挂处理<br>
dbr := sdb.Exec("update dtm_busi.user_account_trading t join dtm_busi.user_account a on t.user_id=a.user_id and t.user_id=? set t.trading_balance=t.trading_balance + ? where a.balance + t.trading_balance + ? >= 0", uid, amount, amount)<br>
if dbr.Error == nil && dbr.RowsAffected == 0 &#123; // 如果余额不足，返回错误<br>
return nil, fmt.Errorf("update error, balance not enough")<br>
&#125;<br>
其他情况检查及处理<br>
&#125; <br>
</pre><br>
然后是调整余额。<br>
<pre class="prettyprint">func adjustBalance(uid int, amount int) (ret interface&#123;&#125;, rerr error) &#123;<br>
幂等、悬挂处理<br>
这里略去进行相关的事务处理，包括开启事务，以及在 defer 中处理提交或回滚<br>
// 将原先冻结的资金记录解冻<br>
dbr := db.Exec("update dtm_busi.user_account_trading t join dtm_busi.user_account a on t.user_id=a.user_id and t.user_id=? set t.trading_balance=t.trading_balance + ?", uid, -amount)<br>
if dbr.Error == nil && dbr.RowsAffected == 1 &#123; // 解冻成功<br>
// 调整金额<br>
dbr = db.Exec("update dtm_busi.user_account set balance=balance+? where user_id=?", amount, uid)<br>
&#125;<br>
其他情况检查及处理<br>
&#125; <br>
</pre><br>
下面我们来编写具体的 Try/Confirm/Cancel 的处理函数。<br>
<pre class="prettyprint">RegisterPost(app, "/api/TransInTry", func (c *gin.Context) (interface&#123;&#125;, error) &#123;<br>
return adjustTrading(1, reqFrom(c).Amount)<br>
&#125;)<br>
RegisterPost(app, "/api/TransInConfirm", func TransInConfirm(c *gin.Context) (interface&#123;&#125;, error) &#123;<br>
return adjustBalance(1, reqFrom(c).Amount)<br>
&#125;)<br>
RegisterPost(app, "/api/TransInCancel", func TransInCancel(c *gin.Context) (interface&#123;&#125;, error) &#123;<br>
return adjustTrading(1, -reqFrom(c).Amount)<br>
&#125;)<br>
<br>
RegisterPost(app, "/api/TransOutTry", func TransOutTry(c *gin.Context) (interface&#123;&#125;, error) &#123;<br>
return adjustTrading(2, -reqFrom(c).Amount)<br>
&#125;)<br>
RegisterPost(app, "/api/TransOutConfirm", func TransInConfirm(c *gin.Context) (interface&#123;&#125;, error) &#123;<br>
return adjustBalance(2, -reqFrom(c).Amount)<br>
&#125;)<br>
RegisterPost(app, "/api/TransOutCancel", func TransInCancel(c *gin.Context) (interface&#123;&#125;, error) &#123;<br>
return adjustTrading(2, reqFrom(c).Amount)<br>
&#125;) <br>
</pre><br>
到此各个子事务的处理函数已经 OK 了，然后是开启 TCC 事务，进行分支调用。<br>
<pre class="prettyprint">// TccGlobalTransaction 会开启一个全局事务<br>
_, err := dtmcli.TccGlobalTransaction(DtmServer, func(tcc *dtmcli.Tcc) (rerr error) &#123;<br>
// CallBranch 会将事务分支的 Confirm/Cancel 注册到全局事务上，然后直接调用 Try<br>
res1, rerr := tcc.CallBranch(&TransReq&#123;Amount: 30&#125;, host+"/api/TransOutTry", host+"/api/TransOutConfirm", host+"/api/TransOutRevert"<br>
进行错误检查，以及其他逻辑<br>
res2, rerr := tcc.CallBranch(&TransReq&#123;Amount: 30&#125;, host+"/api/TransInTry", host+"/api/TransInConfirm", host+"/api/TransInRevert")<br>
进行错误检查，有任何错误，返回错误，回滚交易<br>
// 如果没有错误，函数正常返回后，全局事务会提交，TM 会调用各个事务分支的 Confirm，完成整个事务<br>
&#125;) <br>
</pre><br>
至此，一个完整的TCC分布式事务编写完成。<br>
<br>如果您想要完整运行一个成功的示例，那么按照 <a href="https://github.com/yedf/dtm">dtm</a> 项目的说明搭建好环境之后，运行下面命令运行 TCC 的例子即可。<br>
<pre class="prettyprint">go run app/main.go tcc_barrier<br>
</pre><br>
<h3>TCC 的回滚</h3>假如银行将金额准备转入用户 2 时，发现用户 2 的账户异常，返回失败，会怎么样？我们给出事务失败交互的时序图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210927/4635ac6817b2b6e7512d5debd22e71c0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210927/4635ac6817b2b6e7512d5debd22e71c0.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这个跟成功的 TCC 差别就在于，当某个子事务返回失败后，后续就回滚全局事务，调用各个子事务的 Cancel 操作，保证全局事务全部回滚。<br>
<h3>小结</h3>在这篇文章里，我们介绍了 TCC 的理论知识，也通过一个例子，完整给出了编写一个 TCC 事务的过程，涵盖了正常成功完成，以及成功回滚的情况。相信读者通过这边文章，对 TCC 已经有了深入的理解。<br>
<br>原文链接：<a href="https://zhuanlan.zhihu.com/p/388357329" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/388357329</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            