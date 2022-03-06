
---
title: 'MyBatis Dynamic SQL 1.4.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7812'
author: 开源中国
comments: false
date: Sun, 06 Mar 2022 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7812'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">MyBatis dynamic SQL 1.4.0 现已发布，此工具库是生成动态 SQL 语句的通用框架，可把它看作是一个类型安全的 SQL 模板库，它还支持 MyBatis3 和 Spring JDBC 模板。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">MyBatis dynamic SQL 可生成格式完整的 DELETE、INSERT、SELECT 和 UPDATE 语句供 MyBatis 或 Spring 使用。最常见的用例是生成可由 MyBatis 直接使用的语句和一组匹配的参数。该工具库还可生成与 Spring JDBC 模板兼容的语句和参数对象。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">1.4.0 版本包含<span style="background-color:#ffffff">以下增强功能</span>：</span></p> 
<ul> 
 <li><span style="color:#000000">增加对 where 子句中任意分组条件的支持，以及对"not" conditions 的支持。任何 where 子句都可以通过这个改变来实现。</span></li> 
 <li><span style="color:#000000">对表别名计算的改进，这将使 where 子句中的子查询更容易</span></li> 
 <li><span style="color:#000000">删除一些废弃的代码</span></li> 
 <li><span style="color:#000000">Kotlin DSL 的重大更新：</span> 
  <ul> 
   <li><span style="color:#000000">where 子句 DSL 被重写，更接近 native SQL</span></li> 
   <li><span style="color:#000000">Kotlin where 子句还支持任意分组和"not" conditions</span></li> 
   <li><span style="color:#000000">所有插入语句现在都有 native Kotlin 构建器</span></li> 
   <li><span style="color:#000000">使用 Kotlin DSL building functions 的许多其他小改进</span></li> 
  </ul> </li> 
</ul> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">在这个版本中，Kotlin DSL 非常接近 </span></span><span style="background-color:#ffffff; color:#24292f">native</span><span style="color:#000000"><span style="background-color:#ffffff"> SQL。</span></span></p> 
<p style="text-align:start"><strong><span style="background-color:#ffffff; color:#333333">Maven</span></strong></p> 
<pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
  <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>org.mybatis.dynamic-sql</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
  <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>mybatis-dynamic-sql</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
  <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>1.4.0</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
<p style="text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-dynamic-sql%2Freleases%2Ftag%2Fmybatis-dynamic-sql-1.4.0" target="_blank">https://github.com/mybatis/mybatis-dynamic-sql/releases/tag/mybatis-dynamic-sql-1.4.0</a></p>
                                        </div>
                                      
</div>
            