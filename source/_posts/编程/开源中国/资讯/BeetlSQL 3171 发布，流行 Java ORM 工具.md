
---
title: 'BeetlSQL 3.17.1 发布，流行 Java ORM 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8586'
author: 开源中国
comments: false
date: Mon, 01 Aug 2022 10:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8586'
---

<div>   
<div class="content">
                                                                                            <p>由于仓库上传失败，版本跳到3.17.1了</p> 
<ul> 
 <li><a href="https://gitee.com/xiandafu/beetlsql/issues/I5HAK5#note_11984386">允许@Table(name="",assignId=true</a>) , 指定数据库主键以POJO注解为准而不是数据库，这样可以在视图，或者特殊表中使用自定义注解</li> 
 <li><a href="https://gitee.com/xiandafu/beetlsql/issues/I5J7OB">主键大小写忽略以适应跨数据库</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide%2F3033051" target="_blank">文档进行了更新</a></li> 
</ul> 
<pre><code class="language-xml"><dependency>
    <groupId>com.ibeetl</groupId>
    <artifactId>beetlsql</artifactId>
    <version>3.17.1-RELEASE</version>
</dependency></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span> </span>BeetlSQL 自主研发自 2015 年，目标是提供开发高效，维护高效，运行高效的数据访问框架，它适用范围广，定制性强，写起数据库访问代码特别顺滑，不亚于 MyBatis。你不想写 SQL 也好，或者想更好地写 SQL 也好，BeetlSQL 都能满足这要求，目前支持的数据库如下</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>传统数据库：MySQL (包括支持 MySQL 协议的各种数据库), MariaDB ,Oralce ,Postgres (包括支持 Postgres 协议的各种数据库), DB2 , SQL Server ，H2 , SQLite , Derby ，神通，达梦，华为高斯，人大金仓，PolarDB，GBase8s，GreatSQL 等</li> 
 <li>大数据：HBase，ClickHouse，Cassandar，Hive,GreenPlum</li> 
 <li>物联网时序数据库：Machbase，TD-Engine，IotDB</li> 
 <li>SQL 查询引擎：Drill,Presto，Druid</li> 
 <li>内存数据库：ignite，CouchBase</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide" target="_blank">阅读文档</a><span style="background-color:#ffffff; color:#333333"><span> </span></span><a href="https://gitee.com/xiandafu/beetlsql">源码和例子</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F121.42.237.11%3A8080%2Fbeetlsql_online%2F" target="_blank">在线体验</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide%2F1958115" target="_blank">多库使用</a> <a href="https://gitee.com/xiandafu/dao-benchmark">性能测试</a></p>
                                        </div>
                                      
</div>
            