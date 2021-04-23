
---
title: 'BeetlSQL 3.3.12 发布，Java 的 DAO 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
author: 开源中国
comments: false
date: Fri, 23 Apr 2021 12:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>本次发布了修改了一个严重的Bug,强烈建议升级</p> 
<ul> 
 <li>Spring框架下，修复读取metadata时候占用数据库链接而没有释放，导致链接资源池耗光</li> 
 <li>修复了对boolean 原始类型的的映射支持</li> 
 <li>增强MySql的KeyHandler</li> 
 <li>使用新的方式判断系统版本是否是JDK8以上</li> 
 <li>对所有单元测试中数据库连接池的配置个数设置为1，以方便以后查找链接池泄露问题</li> 
</ul> 
<p>感谢使用者的迅速反馈以及指出问题所在，BeetlSQL的用户越来越多，越来越强</p> 
<pre><code class="language-xml"><dependency>
  <groupId>com.ibeetl</groupId>
  <artifactId>beetlsql</artifactId>
  <version>3.3.12-RELEASE</version>
</dependency></code></pre> 
<p> </p> 
<p style="text-align:left">BeetlSQL 研发自2015年，目标是提供开发高效，维护高效，运行高效的数据库访问框架，它适用范围广，性能高，维护性好，写起数据库访问代码特别顺滑。目前支持的数据库如下</p> 
<ul> 
 <li>传统数据库：MySQL,MariaDB,Oralce,Postgres,DB2,SQL Server，H2,SQLite,Derby，神通，达梦，华为高斯，人大金仓，PolarDB 等</li> 
 <li>大数据：HBase，ClickHouse，Cassandar，Hive</li> 
 <li>物联网时序数据库：Machbase，TD-Engine，IotDB</li> 
 <li>SQL查询引擎:Drill,Presto，Druid</li> 
 <li>内存数据库:ignite，CouchBase</li> 
</ul> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide" target="_blank">阅读文档</a><span style="background-color:#ffffff; color:#333333"> </span><a href="https://gitee.com/xiandafu/beetlsql">源码和例子</a> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F121.42.237.11%3A8080%2Fbeetlsql_online%2F" target="_blank">在线体验</a></p> 
<p style="text-align:left">BeetlSQL也支持IDEA插件，提供向导和自动提示</p> 
<p style="text-align:left"><img alt height="355" src="https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png" width="740" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            