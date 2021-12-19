
---
title: 'HasorDB 4.3.0 发布，这一次可能是史上功能最完备的 ORM 框架了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-43d245081855d600af6313dd9d07df61159.png'
author: 开源中国
comments: false
date: Sun, 19 Dec 2021 00:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-43d245081855d600af6313dd9d07df61159.png'
---

<div>   
<div class="content">
                                                                                            <h2>介绍</h2> 
<p><span style="background-color:#ffffff; color:#40485b">HasorDB 是一个全功能数据库访问工具，提供对象映射、丰富的类型处理、动态SQL、存储过程、内置分页方言20+、支持嵌套事务、多数据源、条件构造器、INSERT 策略、多语句/多结果。并兼容 Spring 及 MyBatis 用法。它不依赖任何其它框架，因此可以很方便的和任意一个框架整合在一起使用。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能特性</h2> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">熟悉的方式</p> 
  <ul> 
   <li>JdbcTemplate 接口方式（高度兼容 Spring JDBC）</li> 
   <li>Mapper 文件方式（高度兼容 MyBatis）</li> 
   <li>LambdaTemplate （高度接近 MyBatis Plus、jOOQ 和 BeetlSQL）</li> 
   <li>@Insert、@Update、@Delete、@Query、@Callable 注解（类似 JPA）</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">事务支持</p> 
  <ul> 
   <li>支持 5 个事务隔离级别、7 个事务传播行为（与 Spring tx 相同）</li> 
   <li>提供 TransactionTemplate、TransactionManager 接口方式声明式事务控制能力（用法与 Spring 相同）</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">特色优势</p> 
  <ul> 
   <li>支持 分页查询 并且提供多种数据库方言（20+）</li> 
   <li>支持 INSERT 策略（INTO、UPDATE、IGNORE）</li> 
   <li>更加丰富的 TypeHandler（MyBatis 40+，HasorDB 60+）</li> 
   <li>Mapper XML 支持多语句、多结果</li> 
   <li>提供独特的<span> </span><code>@&#123;xxx, expr , xxxxx &#125;</code><span> </span>规则扩展机制，让动态 SQL 更加简单</li> 
   <li>支持 存储过程</li> 
   <li>支持 JDBC 4.2 和 Java8 中时间类型</li> 
   <li>支持多数据源</li> 
  </ul> </li> 
</ul> 
<h1>全新的文档首页</h1> 
<p><img height="1548" src="https://oscimg.oschina.net/oscnet/up-43d245081855d600af6313dd9d07df61159.png" width="2894" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><a href="https://my.oschina.net/ta8210/blog/5374205">https://my.oschina.net/ta8210/blog/5374205《推荐一款绝对不能错过的 ORM 框架 HasorDB》</a></p> 
<p>官方文档站：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.hasor.cn" target="_blank">http://www.hasor.cn</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hasordb.net" target="_blank">https://www.hasordb.net</a></p>
                                        </div>
                                      
</div>
            