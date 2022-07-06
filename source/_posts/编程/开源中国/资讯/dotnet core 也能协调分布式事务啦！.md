
---
title: 'dotnet core 也能协调分布式事务啦！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=622'
author: 开源中国
comments: false
date: Wed, 06 Jul 2022 09:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=622'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p>2022 年 5 月 24 日，我们发布了 DBPack <a href="https://www.oschina.net/news/release-v0.1.0.md">v0.1.0</a> 版本，该版本主要 release 了分布式事务功能。在我们的规划里，DBPack 是要支持所有微服务开发语言协调分布式事务的，但经过社区反馈，dotnet core 并不支持。于是，我们在 v0.1.1 对 dotnet core 进行了支持。下面就如何支持 dotnet core 做一个说明。</p> 
</blockquote> 
<h2>MySql 协议</h2> 
<p>先请允许我对 MySql 的通信协议做一个简单的介绍。MySql 支持两种协议，一种是文本（Text）协议，一种是二进制（Binary）协议。MySql 客户端使用 COM_QUERY 发出的请求，MySql 服务端会以文本协议响应结果；使用 COM_STMT_EXECUTE 命令发出的请求，会以二进制协议响应结果。</p> 
<p>在我们用程序调用 MySql Client SDK 发起请求的时候，不同的 MySql Client SDK 会默认使用不同的协议发送请求，但大部分 MySql Client SDK 都支持文本协议和二进制协议，我们可以通过修改属性配置改变 MySql Client SDK 的默认行为。比如：</p> 
<ul> 
 <li>JAVA</li> 
</ul> 
<pre><code class="language-java">@Mapper
public interface ProductMapper &#123;
    @Update("UPDATE /*+ XID('$&#123;xid&#125;') */ `product`.`inventory` SET `available_qty` = `available_qty` - #&#123;qty&#125;, allocated_qty = allocated_qty + #&#123;qty&#125; WHERE product_sysno = #&#123;productSysNo&#125; AND available_qty >= #&#123;qty&#125;")
    boolean allocateInventory(@Param("xid") String xid, @Param("productSysNo") long productSysNo, @Param("qty") int qty);
&#125;
</code></pre> 
<p>在 java 语言编写的微服务中，我们写了一个方法去修改商品的库存，当我们传入参数提交执行的时候，默认该 SQL 请求会被编码成</p> 
<pre><code class="language-sql">update /*+ XID('gs/aggregationSvc/81336085455405058') */ product.inventory set available_qty = available_qty - 2, allocated_qty = allocated_qty + 2 where product_sysno = 1 and available_qty >= 2;
</code></pre> 
<p>通过 COM_QUERY 命令发出。</p> 
<p>我们可以通过修改连接字符串，在原来的 <code>jdbc:mysql://dbpack2:13307/product</code> 上加上 <code>useServerPrepStmts=true</code>，改为 <code>jdbc:mysql://dbpack2:13307/product?useServerPrepStmts=true</code>，再次执行时，会首先发出 COM_STMT_PREPARE 请求：</p> 
<pre><code class="language-sql">UPDATE /*+ XID('gs/aggregationSvc/2612341069705662465') */ product.inventory set available_qty = available_qty - ?, allocated_qty = allocated_qty + ? WHERE product_sysno = ? and available_qty >= ?
</code></pre> 
<p>获取到 statement id 后，再将 statement id 和请求参数编码后通过 COM_STMT_EXECUTE 命令发出。</p> 
<ul> 
 <li>Golang</li> 
</ul> 
<p>Golang MySql driver 默认是以二进制协议发送带参数的 DML 请求的，通过在 dsn 上加上参数 <code>interpolateParams=true</code>，才会以文本协议发送。例如：</p> 
<pre><code>dksl:123456@tcp(127.0.0.1:13306)/employees?interpolateParams=true&timeout=10s&readTimeout=10s&writeTimeout=10s&parseTime=true&loc=Local&charset=utf8mb4,utf8
</code></pre> 
<h2>Dotnet Core</h2> 
<p>Dotnet core 如果使用 EntityFrameworkCore 或者 Dapper 来访问数据库，目前还不支持使用 Prepared Statement，下面这两个 issue 有相关说明：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fefcore%2Fissues%2F5459" target="_blank">https://github.com/dotnet/efcore/issues/5459</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDapperLib%2FDapper%2Fissues%2F474" target="_blank">https://github.com/DapperLib/Dapper/issues/474</a></p> 
<p>在 v0.1.0 版本，我们只对 COM_STMT_EXECUTE 请求做了拦截处理，来协调分布式事务问题。dotnet core 使用 COM_QUERY 提交请求自然无法协调分布式事务，在 v0.1.1 我们增加了 COM_QUERY 请求协调分布式事务的支持，这样真正做到了支持所有微服务语言协调分布式事务。</p> 
<p>dotnet core sample 见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack-samples%2Ftree%2Fmain%2Fdotnet%25E3%2580%2582" target="_blank">https://github.com/CECTC/dbpack-samples/tree/main/dotnet。</a></p> 
<h2>其他特性</h2> 
<p>本次发版，还修复了一些 bug，增加了 status api 用于查询 dbpack 的运行状态：</p> 
<pre><code>$ curl http://localhost:9999/status
$ &#123;
    "listeners": [&#123;
        "protocol_type": "mysql",
        "socket_address": &#123;
            "address": "0.0.0.0",
            "port": 13306
        &#125;,
        "active": true
    &#125;],
    "distributed_transaction_enabled": true,
    "is_master": true
&#125;
</code></pre> 
<p>至此，我们有了</p> 
<ul> 
 <li>/live</li> 
 <li>/ready</li> 
 <li>/status</li> 
 <li>/metrics</li> 
</ul> 
<p>这些 api 辅助我们查看 dbpack 的运行状态。</p> 
<p>完整的版本变更日志请看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack%2Freleases%25E3%2580%2582" target="_blank">https://github.com/CECTC/dbpack/releases。</a></p> 
<p>在下一个版本，我们会增加 tracing 和审计日志的功能。</p> 
<h2>一些链接</h2> 
<p>DBPack 项目地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack" target="_blank">https://github.com/cectc/dbpack</a></p> 
<p>DBPack 文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcectc.github.io%2Fdbpack-doc%2F%23%2F" target="_blank">https://cectc.github.io/dbpack-doc/#/</a></p> 
<p>DBPack-samples：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcectc%2Fdbpack-samples" target="_blank">https://github.com/cectc/dbpack-samples</a></p> 
<p>DBPack 介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FDmXfk5bAcVYdnOwvp8ocHA" target="_blank">https://mp.weixin.qq.com/s/DmXfk5bAcVYdnOwvp8ocHA</a></p> 
<p>事件驱动的分布式事务架构设计：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fr43JvRY3LCETMoZjrdNxXA" target="_blank">https://mp.weixin.qq.com/s/r43JvRY3LCETMoZjrdNxXA</a></p>
                                        </div>
                                      
</div>
            