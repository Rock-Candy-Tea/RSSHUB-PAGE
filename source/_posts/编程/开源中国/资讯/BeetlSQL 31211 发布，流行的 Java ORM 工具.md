
---
title: 'BeetlSQL 3.12.11 发布，流行的 Java ORM 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6222'
author: 开源中国
comments: false
date: Mon, 07 Feb 2022 09:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6222'
---

<div>   
<div class="content">
                                                                                            <ul> 
 <li> lombok的依赖方式调整为provided</li> 
 <li>增加注解@Date2Long,用于把日期类型自动转为Long <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhttps%3A%2F%2Fb23.tv%2FsArcMkx" target="_blank">视频直播功能调整</a></li> 
</ul> 
<pre><code class="language-java">@Data
@Table(name="order_log")
public class OrderLog &#123;
@AssignID
Integer orderId;
Integer age;

@Date2Long
Date createTime;

&#125;
</code></pre> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>com.ibeetl<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>beetlsql<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>3.12.11-RELEASE<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">BeetlSQL 自主研发自 2015 年，目标是提供开发高效，维护高效，运行高效的数据访问框架，它适用范围广，定制性强，写起数据库访问代码特别顺滑，不亚于 MyBatis。你不想写 SQL 也好，或者想更好地写 SQL 也好，BeetlSQL 都能满足这要求，目前支持的数据库如下</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>传统数据库：MySQL (包括支持MySQL协议的各种数据库), MariaDB ,Oralce ,Postgres (包括支持 Postgres 协议的各种数据库), DB2 , SQL Server ，H2 , SQLite , Derby ，神通，达梦，华为高斯，人大金仓，PolarDB，GBase8s，GreatSQL 等</li> 
 <li>大数据：HBase，ClickHouse，Cassandar，Hive,GreenPlum</li> 
 <li>物联网时序数据库：Machbase，TD-Engine，IotDB</li> 
 <li>SQL查询引擎：Drill,Presto，Druid</li> 
 <li>内存数据库：ignite，CouchBase</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide" target="_blank">阅读文档</a><span style="background-color:#ffffff; color:#333333"><span> </span></span><a href="https://gitee.com/xiandafu/beetlsql">源码和例子</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F121.42.237.11%3A8080%2Fbeetlsql_online%2F" target="_blank">在线体验</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide%2F1958115" target="_blank">多库使用</a> <a href="https://gitee.com/xiandafu/dao-benchmark">性能测试</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            