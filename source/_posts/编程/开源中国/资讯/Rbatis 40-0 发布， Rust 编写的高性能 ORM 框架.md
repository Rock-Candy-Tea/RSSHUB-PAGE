
---
title: 'Rbatis 4.0-0 发布， Rust 编写的高性能 ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8861'
author: 开源中国
comments: false
date: Sun, 07 Aug 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8861'
---

<div>   
<div class="content">
                                                                                            <p>Rbatis 是一个用 Rust 编写的高性能、安全、动态 SQL（编译时）ORM 框架，受 Mybatis 和 MybatisPlus 的启发。它提供高性能，基于 Future，带有 async_std/tokio，单线程基准测试可以轻松达到 200,000 QPS。</p> 
<p>目前 Rbatis 4.0.0 发布了，带来如下变更：</p> 
<ul> 
 <li>删除了 sqlx-core</li> 
 <li>添加 rbdc 驱动程序（mysql、sqlite、mssql、pg....等等）。重写的数据库驱动类似于 JDBC，实现 Box Dyn 依赖分离</li> 
 <li>添加 mobc 连接池</li> 
 <li>删除了 <span style="color:#24292f">Wrapper</span></li> 
 <li>pysql/htmlsql 宏添加了关键字 <code>``</code>支持</li> 
 <li>所有驱动程序支持关键字 <code>?</code> 占位符</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frbatis%2Frbatis%2Freleases%2Ftag%2Fv4.0" target="_blank">https://github.com/rbatis/rbatis/releases/tag/v4.0</a></p>
                                        </div>
                                      
</div>
            