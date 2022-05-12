
---
title: 'ORM 工具 HasorDB 经过 8 年迭代，正式更名为 dbVisitor 开始独立发展'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-50ec61959f0d3df1cb4ac72767728dbc70d.png'
author: 开源中国
comments: false
date: Thu, 12 May 2022 06:37:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-50ec61959f0d3df1cb4ac72767728dbc70d.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0; margin-right:0; text-align:left">介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">dbVisitor<span style="background-color:#ffffff"> 是一个全功能数据库访问工具，提供对象映射、丰富的类型处理、动态 SQL、存储过程、内置分页方言 20+、支持嵌套事务、多数据源、条件构造器、INSERT 策略、多语句 / 多结果。兼容 Spring 及 MyBatis 用法。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">它不依赖任何其它框架，因此可以很方便的和任意一个框架整合在一起使用。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能特性</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">熟悉的方式</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>JdbcTemplate 接口方式（高度兼容 Spring JDBC）</li> 
   <li>Mapper 文件方式（高度兼容 MyBatis）</li> 
   <li>LambdaTemplate （高度接近 MyBatis Plus、jOOQ 和 BeetlSQL）</li> 
   <li>@Insert、@Update、@Delete、@Query、@Callable 注解（类似 JPA）</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">事务支持</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>支持 5 个事务隔离级别、7 个事务传播行为（与 Spring tx 相同）</li> 
   <li>提供 TransactionTemplate、TransactionManager 接口方式声明式事务控制能力（用法与 Spring 相同）</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">特色优势</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>支持 分页查询 并且提供多种数据库方言（20+）</li> 
   <li>支持 INSERT 策略（INTO、UPDATE、IGNORE）</li> 
   <li>更加丰富的 TypeHandler（MyBatis 40+，HasorDB 60+）</li> 
   <li>Mapper XML 支持多语句、多结果</li> 
   <li>提供独特的 <code>@&#123;xxx, expr , xxxxx &#125;</code> 规则扩展机制，让动态 SQL 更加简单</li> 
   <li>支持 存储过程</li> 
   <li>支持 JDBC 4.2 和 Java8 中时间类型</li> 
   <li>支持多数据源</li> 
  </ul> </li> 
</ul> 
<h2>发展历史</h2> 
<p>最初是 Hasor 项目的一个小模块，主要提供数据库访问功能。当时名字为 hasor-db</p> 
<p>历经了 8年的发展，各版本可以在 mvnrepository 中找到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmvnrepository.com%2Fartifact%2Fnet.hasor%2Fhasor-db" target="_blank"><span>https://mvnrepository.com/artifact/net.hasor/hasor-db</span></a></p> 
<h2>为什么叫 dbVisitor</h2> 
<p>经过了 4.3.x 几个版本的准备阶段，hasor-db 已经和 Hasor 项目相关联的依赖全部理清。</p> 
<p>为什么叫 dbVisitor</p> 
<p>简单拆解为两个词： db  visitor，表示 dbVisitor 将会专注在数据库访问层的一个工具。</p> 
<h2>官网更新</h2> 
<p>当前整个官网已经完成更新，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hasordb.net%2F" target="_blank">https://www.hasordb.net/</a>、新域名<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.dbvisitor.net%2F" target="_blank">https://www.dbvisitor.net/</a> 将在近期启用。</p> 
<p><img height="1764" src="https://oscimg.oschina.net/oscnet/up-50ec61959f0d3df1cb4ac72767728dbc70d.png" width="3104" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">最后</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="background-color:#ffffff">在最后如果您觉得这个工具还不错可以给个 start 多多关注这个工具，地址为： </span><a href="https://gitee.com/zycgit/dbvisitor">https://gitee.com/zycgit/dbvisitor</a></li> 
 <li> <p style="margin-left:0; margin-right:0">此外如果你想更多了解它，也可以在官方网站上加入 dbVisitor 社区进行深入交流。</p> </li> 
</ul>
                                        </div>
                                      
</div>
            