
---
title: 'BeetlSQL 3.3.8 发布，Java 的 DAO 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
author: 开源中国
comments: false
date: Sun, 28 Mar 2021 21:07:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
---

<div>   
<div class="content">
                                                                                            <p>本次发布修复了若干Bug</p> 
<ul> 
 <li>TD-Engine中使用内置SQL中，使用where标签代替 1=1，目前版本的TD-Engine不支持sql中1=1的表达式</li> 
 <li>在一些不支持JDBC metadata的某些NOSql上，屏蔽对POJO的类型检测以避免报错。更好的支持NoSQL</li> 
 <li>修复在Mapper方法中，使用枚举类，没有经过BeetlSQL对枚举的预处理</li> 
 <li>代码生成，允许指定数据库日期对应的Java类型</li> 
 <li>修复加载Markdown文件时候，并发导致加载错误的问题，建议升级</li> 
</ul> 
<pre><code class="language-xml"><dependency>
  <groupId>com.ibeetl</groupId>
  <artifactId>beetlsql</artifactId>
  <version>3.3.8-RELEASE</version>
</dependency></code></pre> 
<p style="text-align:left"> </p> 
<p style="text-align:left">BeetlSQL 研发自2015年，目标是提供开发高效，维护高效，运行高效的数据库访问框架，以我多年天天CRUD的经验总结得来的框架，适用范围广，性能高，维护性好。目前支持的数据库如下</p> 
<ul> 
 <li>传统数据库：MySQL,MariaDB,Oralce,Postgres,DB2,SQL Server，H2,SQLite,Derby，神通，达梦，华为高斯，人大金仓，PolarDB 等</li> 
 <li>大数据：HBase，ClickHouse，Cassandar，Hive</li> 
 <li>物联网时序数据库：Machbase，TD-Engine，IotDB</li> 
 <li>SQL查询引擎:Drill,Presto，Druid</li> 
 <li>内存数据库:ignite，CouchBase</li> 
</ul> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide" target="_blank">阅读文档</a><span style="background-color:#ffffff; color:#333333"> </span><a href="https://gitee.com/xiandafu/beetlsql">源码和例子</a></p> 
<p style="text-align:left">BeetlSQL也支持IDEA插件，提供向导和自动提示</p> 
<p style="text-align:left"><img alt height="355" src="https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png" width="740" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            