
---
title: 'ORM 工具 HasorDB 4.3.4 发布，支持 Spring_SpringBoot 集成'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9881'
author: 开源中国
comments: false
date: Sat, 30 Apr 2022 11:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9881'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">HasorDB 是一个全功能数据库访问工具，提供对象映射、丰富的类型处理、动态SQL、存储过程、内置分页方言20+、支持嵌套事务、多数据源、条件构造器、INSERT 策略、多语句/多结果。并兼容 Spring 及 MyBatis 用法。它不依赖任何其它框架，因此可以很方便的和任意一个框架整合在一起使用。</span></p> 
<h2 style="text-align:left">功能特性</h2> 
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
<h2 style="text-align:left">Release.Note</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持 Spring Xml 配置方式使用 HasorDB</li> 
 <li>支持 Spring Boot @MapperScan 方式配置。</li> 
 <li>DynamicConnection 增加 releaseConnection 方法用于外部数据源管理器的连接释放操作。</li> 
 <li> <p style="margin-left:0; margin-right:0">优化 Mapper 匹配逻辑，增加 mapper 匹配成功率。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">RefMapper 和 SimpleMapper 都标记了 DalMapper 注解</p> </li> 
</ul> 
<h2 style="text-align:start">最后</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="background-color:#ffffff">在最后如果您觉得这个工具还不错可以给个 start 多多关注这个工具，地址为： </span><a href="https://gitee.com/zycgit/hasordb">https://gitee.com/zycgit/hasordb</a></li> 
 <li> <p style="margin-left:0; margin-right:0">此外如果你想更多了解它，可以在它的官网上详细阅读使用技巧 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hasordb.net" target="_blank">https://www.hasordb.net</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            