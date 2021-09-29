
---
title: '分布式事务实战：用Go轻松完成一个 TCC'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210929/06deb3d9ec8ef7324361475e42d012e3.png'
author: Dockone
comments: false
date: 2021-09-29 14:07:41
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210929/06deb3d9ec8ef7324361475e42d012e3.png'
---

<div>   
<br>TCC 分布式事务来源于 2007 年 Pat Helland 发表的一篇名为《Life beyond Distributed Transactions:an Apostate’s Opinion》的论文，TCC 分别是 Try、Confirm、Cancel 的手写字母。<br><br>
<h3>组成</h3>TCC 有三个分支：<br>
<ul><li>Try 分支：预留锁定业务相关资源，如果资源不够，则返回失败</li><li>Confirm 分支：如果前面的 Try 全部成功，则进入 Confirm，进行数据变更，这个阶段不会返回失败</li><li>Cancel 分支：如果前面的 Try 没有全部成功，有返回失败的，则进入 Cancel。Cancel 解冻 Try 锁定的资源，也类似 Confirm 是不会返回失败的。</li></ul><br>
<br>假设有一个银行跨行转账的业务，因为不同银行，数据不在同一个数据库，而更可能在不同微服务下的数据库里。这是一个典型的分布式事务场景，我们看看一个成功的 TCC 时序图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210929/06deb3d9ec8ef7324361475e42d012e3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210929/06deb3d9ec8ef7324361475e42d012e3.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>实践</h3>A 转账给 B 的跨行转账操作，如果转账不成功，我们不想让用户看到自己账上的余额变动过，因此我们在 Try 阶段冻结相关的余额，Confirm 阶段进行转账，Cancel 阶段进行余额解冻。这样可以避免 A 看到自己的存款减少了，但是最后转账又失败的情况。<br>
<br>下面是具体的开发详情：<br>
<br>我们采用Go语言，使用 <a href="https://github.com/yedf/dtm" rel="nofollow" target="_blank">https://github.com/yedf/dtm</a> 这个功能强大又简单易用的分布式事务框架。<br>
<br>创建两张表，一个用户余额表，另一个是冻结资金表，语句如下：<br>
<pre class="prettyprint">CREATE TABLE dtm_busi.`user_account` (  <br>
`id` int(11) AUTO_INCREMENT PRIMARY KEY,  <br>
`user_id` int(11) not NULL UNIQUE ,  <br>
`balance` decimal(10,2) NOT NULL DEFAULT '0.00',  <br>
`create_time` datetime DEFAULT now(),  <br>
`update_time` datetime DEFAULT now()  <br>
);  <br>
<br>
CREATE TABLE dtm_busi.`user_account_trading` (  <br>
`id` int(11) AUTO_INCREMENT PRIMARY KEY,  <br>
`user_id` int(11) not NULL UNIQUE ,  <br>
`trading_balance` decimal(10,2) NOT NULL DEFAULT '0.00',  <br>
`create_time` datetime DEFAULT now(),  <br>
`update_time` datetime DEFAULT now()  <br>
); <br>
</pre><br>
trading 表中 trading_balance 记录的是交易中的金额。<br>
<br>最重要的业务代码包括冻结/解冻资金和调整余额，代码如下：<br>
<pre class="prettyprint">func adjustTrading(uid int, amount int) (interface&#123;&#125;, error) &#123;<br>
幂等、悬挂处理<br>
dbr := sdb.Exec("update dtm_busi.user_account_trading t join dtm_busi.user_account a on t.user_id=a.user_id and t.user_id=? set t.trading_balance=t.trading_balance + ? where a.balance + t.trading_balance + ? >= 0", uid, amount, amount)<br>
if dbr.Error == nil && dbr.RowsAffected == 0 &#123; // 如果余额不足，返回错误<br>
return nil, fmt.Errorf("update error, balance not enough")<br>
&#125;<br>
其他情况检查及处理<br>
&#125;<br>
<br>
func adjustBalance(uid int, amount int) (ret interface&#123;&#125;, rerr error) &#123;<br>
幂等、悬挂处理<br>
这里略去进行相关的事务处理，包括开启事务，以及在defer中处理提交或回滚<br>
// 将原先冻结的资金记录解冻<br>
dbr := db.Exec("update dtm_busi.user_account_trading t join dtm_busi.user_account a on t.user_id=a.user_id and t.user_id=? set t.trading_balance=t.trading_balance + ?", uid, -amount)<br>
if dbr.Error == nil && dbr.RowsAffected == 1 &#123; // 解冻成功<br>
// 调整金额<br>
dbr = db.Exec("update dtm_busi.user_account set balance=balance+? where user_id=?", amount, uid)<br>
&#125;<br>
其他情况检查及处理<br>
&#125; <br>
</pre><br>
业务有个重要约束 balance+trading_balance >= 0，表示用户最终的余额不能为负。如果约束不成立，返回失败。<br>
<br>然后是 Try/Confirm/Cancel 的处理函数，他们比较简单。<br>
<pre class="prettyprint">RegisterPost(app, "/api/TransInTry", func (c *gin.Context) (interface&#123;&#125;, error) &#123;  <br>
return adjustTrading(1, reqFrom(c).Amount)  <br>
&#125;)  <br>
RegisterPost(app, "/api/TransInConfirm", func TransInConfirm(c *gin.Context) (interface&#123;&#125;, error) &#123;  <br>
return adjustBalance(1, reqFrom(c).Amount)  <br>
&#125;)  <br>
RegisterPost(app, "/api/TransInCancel", func TransInCancel(c *gin.Context) (interface&#123;&#125;, error) &#123;  <br>
return adjustTrading(1, -reqFrom(c).Amount)  <br>
&#125;)  <br>
<br>
RegisterPost(app, "/api/TransOutTry", func TransOutTry(c *gin.Context) (interface&#123;&#125;, error) &#123;  <br>
return adjustTrading(2, -reqFrom(c).Amount)  <br>
&#125;)  <br>
RegisterPost(app, "/api/TransOutConfirm", func TransInConfirm(c *gin.Context) (interface&#123;&#125;, error) &#123;  <br>
return adjustBalance(2, -reqFrom(c).Amount)  <br>
&#125;)  <br>
RegisterPost(app, "/api/TransOutCancel", func TransInCancel(c *gin.Context) (interface&#123;&#125;, error) &#123;  <br>
return adjustTrading(2, reqFrom(c).Amount)  <br>
&#125;)  <br>
</pre><br>
到此各个子事务的处理函数已经 OK 了，然后是开启 TCC 事务，进行分支调用：<br>
<pre class="prettyprint">err := dtmcli.TccGlobalTransaction(DtmServer, gid, func(tcc *dtmcli.Tcc) (*resty.Response, error) &#123;<br>
resp, err := tcc.CallBranch(&TransReq&#123;Amount: 30&#125;, Busi+"/TccBTransOutTry", Busi+"/TccBTransOutConfirm", Busi+"/TccBTransOutCancel")<br>
if err != nil &#123;<br>
  return resp, err<br>
&#125;<br>
return tcc.CallBranch(&TransReq&#123;Amount: 30&#125;, Busi+"/TccBTransInTry", Busi+"/TccBTransInConfirm", Busi+"/TccBTransInCancel")<br>
&#125;) <br>
</pre><br>
至此，一个 TCC 分布式事务全部完成。<br>
<br>yedf/dtm 项目中有完整的示例，你可以访问该项目，通过下面命令运行上述的示例。<br>
<pre class="prettyprint">go run app/main.go tcc_barrier<br>
</pre><br>
<h3>回滚</h3>跨行转账有可能出现失败，例如 A 转账给 B，但是 B 的账户由于各类原因异常，返回无法转入，这种情况会怎么样？我们可以修改代码，让我们的示例处理这种情况：<br><br>
<pre class="prettyprint">RegisterPost(app, "/api/TransInTry", func (c *gin.Context) (interface&#123;&#125;, error) &#123;  <br>
return gin.H&#123;"dtm_result":"FAILURE"&#125;, nil  <br>
&#125;)<br>
</pre><br>
因为 B 账户的异常，会导致整个全局事务的回滚，时序图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210929/a3c9f69b8bc2121ee50d68b6bc0816b6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210929/a3c9f69b8bc2121ee50d68b6bc0816b6.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这个时序图与成功的时序图非常相近，主要差别在于 TransIn 返回了失败，后续的操作由 Confirm 变成了 Cancel。<br>
<h3>小结</h3>这篇文章完整的介绍了 TCC 事务的全过程，包括 TCC 事务的业务设计要点、一个成功完成的例子、一个成功回滚的例子。相信读者到这里，已经对 TCC 有了很清晰的理解。<br>
<br>全局事务进行过程中，可能出现各类网络异常，例如收到重复的 Cancel 或者未收到 Try 却收到 Cancel 等。这类难题的处理技巧，以及其他分布式事务模式如 SAGA、XA 等，可以参考我的另一篇文章《<a href="http://dockone.io/article/2434504">分布式事务最经典的七种解决方案</a>》，里面有全面的讲解。 <br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/lCOfgGp19NdoQz1-aaAmHg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/lCOfgGp19NdoQz1-aaAmHg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            