
---
title: 'BeetlSQL 3.6.1 发布，流行的 Java DAO 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
author: 开源中国
comments: false
date: Mon, 12 Jul 2021 13:33:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>本次改动引入了sqlParser工具，用来解析sql，代替之前自己写的解析工具</p> 
<ul> 
 <li>修复upsert方法复合主键不支持的错误</li> 
 <li>合并来自社区的PR，增强BeetlSQL代码可读性</li> 
 <li>按照社区建议，采用sqlParser，解决execute方法解析sql导致的问题</li> 
</ul> 
<p style="text-align:left">Maven</p> 
<pre style="text-align:left"><code class="language-xml"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>com.ibeetl<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>beetlsql<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>3.6.1-RELEASE<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
</code></pre> 
<p style="text-align:left">BeetlSQL 研发自2015年，目标是提供开发高效，维护高效，运行高效的数据访问框架，它适用范围广，定制性强，写起数据库访问代码特别顺滑,不亚于MyBatis. 你不想写SQL也好，或者想更好的写SQL也好，BeetlSQL都能满足这要求，目前支持的数据库如下</p> 
<ul> 
 <li>传统数据库：MySQL,MariaDB,Oralce,Postgres,DB2,SQL Server，H2,SQLite,Derby，神通，达梦，华为高斯，人大金仓，PolarDB 等</li> 
 <li>大数据：HBase，ClickHouse，Cassandar，Hive</li> 
 <li>物联网时序数据库：Machbase，TD-Engine，IotDB</li> 
 <li>SQL查询引擎:Drill,Presto，Druid</li> 
 <li>内存数据库:ignite，CouchBase</li> 
</ul> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide" target="_blank">阅读文档</a><span style="background-color:#ffffff; color:#333333"> </span><a href="https://gitee.com/xiandafu/beetlsql">源码和例子</a> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F121.42.237.11%3A8080%2Fbeetlsql_online%2F" target="_blank">在线体验</a></p> 
<p style="text-align:left">BeetlSQL也支持IDEA插件，提供向导和自动提示</p> 
<p style="text-align:left"><img alt height="288" src="https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png" width="600" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            