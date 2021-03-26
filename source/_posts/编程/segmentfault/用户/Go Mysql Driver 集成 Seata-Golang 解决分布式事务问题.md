
---
title: 'Go Mysql Driver 集成 Seata-Golang 解决分布式事务问题'
categories: 
 - 编程
 - segmentfault
 - 用户
headimg: 'https://segmentfault.com/img/remote/1460000039712299'
author: segmentfault
comments: false
date: 2021-03-26 08:09:10
thumbnail: 'https://segmentfault.com/img/remote/1460000039712299'
---

<div>   
<p><strong>简介：</strong> 2020 年 4 月，我们开始尝试实现 go 语言的分布式事务框架 Seata-Golang。众所周知，Seata AT 模式以无业务代码侵入的特点，被广大开发者推崇。Java 版 Seata AT 模式通过对 DataSource 数据源进行代理，在 sql 语句执行时，对 sql 拦截解析，获取数据库对应数据在 sql 语句执行前后的副本，序列化后保存起来，在 TC 协调回滚时用来回滚对应数据。实现 go 版本 client 的 AT 模式时，怎样对业务开发者更友好，入侵更少，成了首要考虑的目标。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039712299" alt="头图.png" title="头图.png" referrerpolicy="no-referrer"></span></p><p>作者 | 刘晓敏  GitHub ID：dk-lockdown<br>来源 | <a href="https://mp.weixin.qq.com/s/CB6BCai1k2tCJBOWJ9o1_g" rel="nofollow">阿里巴巴云原生公众号</a></p><h1>背景</h1><p>2020 年 4 月，我们开始尝试实现 go 语言的分布式事务框架 <a href="https://github.com/opentrx/seata-golang" rel="nofollow">Seata-Golang</a>。众所周知，Seata AT 模式以无业务代码侵入的特点，被广大开发者推崇。Java 版 Seata AT 模式通过对 DataSource 数据源进行代理，在 sql 语句执行时，对 sql 拦截解析，获取数据库对应数据在 sql 语句执行前后的副本，序列化后保存起来，在 TC 协调回滚时用来回滚对应数据。实现 go 版本 client 的 AT 模式时，怎样对业务开发者更友好，入侵更少，成了首要考虑的目标。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039712300" alt="1.png" title="1.png" referrerpolicy="no-referrer"></span></p><p>使用 go 操作数据库时，我们会使用到 go 语言的官方库 <code>database/sql</code>，通过 <code>sql.Open("mysql", $&#123;dsn&#125;)</code> 获取一个数据源操作对象 db。开启事务时，使用 <code>db.Begin()</code> 或 <code>db.BeginTx(ctx, &sql.TxOptions&#123;&#125;)</code> 获得事务操作对象 tx，执行 sql 查询使用 <code>tx.Query</code>；执行 sql 新增、修改、删除，使用 <code>tx.Exec</code>；最后使用 <code>tx.Commit()</code> 提交或使用 <code>tx.Rollback()</code> 回滚。</p><p>go 语言官方库 <code>database/sql</code> 提供了一个标准抽象层，通过实现不同的 driver 一套标准的抽象 API 可以操作不同的数据库。开发 Go 版本的 AT 模式，必然要兼容 <code>database/sql</code>。通过研究 <code>database/sql</code> 的 api，创建数据源操作对象，数据库有关的配置必须通过 Data Source Name (DSN) 抽象传递进去，下面是 DSN 的定义：</p><p><code>[username[:password]@][protocol[(address)]]/dbname[?param1=value1&...&paramN=valueN]</code></p><p>实现 AT 模式对数据源代理是需要和事务协调器 TC 进行交互的，如果将 AT 模式实现在 driver 层，那么和 TC 交互的一些参数必须要通过 DSN 传递到 driver，这样有些破坏它的设计。所以，最后采取了一种折中方案，在 <code>database/sql</code> 层之上实现 AT 模式，代理 <code>database/sql</code> 创建出来的数据源操作对象。数据源代理对象实现 <code>database/sql</code> 库定义的 Tx 接口，另外再提供一个开启事务的方法：<code>Begin()</code>，虽然没有完全兼容 <code>database/sql</code> 的 api，但是关键接口和它的定义成一样，勉强还能接受。到此，Seata-Golang 项目核心功能的开发已完成。</p><pre><code>type Tx interface &#123;
    Commit() error
    Rollback() error
&#125;</code></pre><h1>转折</h1><p>Seata-Golang  开源后，逐渐被一些开发者了解和接触，社区也对 Seata-Golang 发出了一些反馈的声音，不少开发者并不习惯写原生 sql，他们希望将 Seata-Golang 集成到 ORM 框架，因为当时的设计没有完全兼容 <code>database/sql</code> 导致集成上遇到一些困难。随着社区的热切呼唤，且得益于前期对 driver 的一些研究，念念不忘必有回响，今年 3 月突然灵感迸发：为什么参数一定要通过 DSN 传递？Seata-Golang Client 初始化后，在需要时通过 Client 端的 API <code>config.GetATConfig()</code> 直接获取使用不就可以了。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039712301" alt="2.png" title="2.png" referrerpolicy="no-referrer"></span></p><p>于是工作之余，历时 2 周开发，第一个集成 Seata-Golang 的完全兼容 <code>database/sql</code> 的 mysql driver 被开发出来，项目开源在 <a href="https://github.com/opentrx/mysql" rel="nofollow">https://github.com/opentrx/mysql</a>，现处于 beta 状态，希望社区开发者使用后能有一些反馈，可通过例子：<a href="https://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247502784&idx=1&sn=6d2a90ba50b3bb025bf0f4f4fea7a848&chksm=fae6c00fcd91491924525f152ab388bf94a01c5e945292063ab218eec9419eff7443cfd0dde5&token=1233080785&lang=zh_CN" rel="nofollow">https://github.com/opentrx/seata-go-samples</a>，查看使用方式并进行测试。</p><h1>driver 的一些细节</h1><ul><li><strong>使用该 driver 进行分布式事务操作时，不能在 dsn 中设置 interpolateParams 参数为 true</strong>。</li></ul><p>这涉及到 mysql 的两个协议：Text 协议和 Binary 协议。有关两个协议的区别，可以在文末参考文档找到资料。实现该 driver 只对 binary 协议进行了处理，开启 interpolateParams 会使用 text 协议执行 sql。</p><ul><li><strong>使用该 driver 在需要加入全局事务组和 tc 进行交互时，需要使用 <code>db.BeginTx(ctx context.Context, opts driver.TxOptions)</code> 方法，并在 ctx 中加入 <code>XID</code> 全局事务 id 的值</strong>。</li></ul><pre><code>ctx := context.WithValue(context.Background(), mysql.XID, c.Request.Header.Get("XID"))
tx, err := dao.BeginTx(ctx, &sql.TxOptions&#123;
        Isolation: sql.LevelDefault,
        ReadOnly:  false,
    &#125;)</code></pre><p>XID 传递到 driver 层，会保存在 &mysqlConn 连接对象中，在和 TC 交互时用到。</p><ul><li><strong>使用该 driver 的分布式事务功能前需要先初始化 seata-golang client 和 mysql driver</strong>：</li></ul><pre><code> config.InitConf(configPath)
  client.NewRpcClient()
  mysql.InitDataResourceManager()
  mysql.RegisterResource(config.GetATConfig().DSN)</code></pre><p>具体可参考 <a href="https://github.com/opentrx/seata-go-samples" rel="nofollow">seata-go-samples</a>。</p><h2>寄语</h2><p>此项目开源到今年 4 月即满一年，通过本文中的 mysql driver，希望能降低使用门槛，让大家真正用起来，大家在选择微服务开发技术栈时也不用担心 go 语言没有分布式事务处理方案。</p><p><a href="https://developer.aliyun.com/article/783087?utm_content=g_1000256448" rel="nofollow">原文链接</a><br>本文为阿里云原创内容，未经允许不得转载。</p>  
</div>
            