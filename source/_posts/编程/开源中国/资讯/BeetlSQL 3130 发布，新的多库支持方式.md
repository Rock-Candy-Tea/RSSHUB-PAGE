
---
title: 'BeetlSQL 3.13.0 发布，新的多库支持方式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6932'
author: 开源中国
comments: false
date: Mon, 14 Mar 2022 16:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6932'
---

<div>   
<div class="content">
                                                                                            <p>新增 ThreadLocalSQLManager 类，让开发者指定使用哪个SQLManager, 一个使用例子</p> 
<pre><code>beetlsql.sqlManagers = proxySqlManager
beetlsql.proxySqlManager.threadlocal=sqlManager1,sqlManager2
beetlsql.proxySqlManager.basePackage=org.beetl.sql.springboot.threadlocal
beetlsql.sqlManager1.ds=ds1
beetlsql.sqlManager1.
beetlsql.sqlManager2.ds=ds2,ds2-slave
</code></pre> 
<p>如上配置了ds1和ds2，ds2还有一个从库ds2-slave. 所有这些配置都使用proxyManager代理，设定了</p> 
<p>threadlocal=sqlManger1,sqManager2, 第一个为默认数据库，那么如下代码根据Use注解来确定使用哪个库</p> 
<p> </p> 
<pre><code class="language-java">@Autowired
@Qualifier("proxySqlManager")
SQLManager sqlManager;

@Autowired
    UserInfoMapper mapper;


    @Use("sqlManager2")
public long test2()&#123;
return mapper.allCount();

&#125;


@Use("sqlManager1")
public long test1()&#123;
return mapper.allCount();
&#125;

    //默认sqlmanager1
public long test1()&#123;
return mapper.allCount();
&#125;</code></pre> 
<p><a href="https://gitee.com/xiandafu/beetlsql/tree/master/sql-integration/sql-springboot-starter/src/test/java/org/beetl/sql/springboot">SpringBoot例子 </a></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span></span>
    <span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span></span>com.ibeetl<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span></span>
    <span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span>beetlsql<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span>
    <span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span></span>3.13.0-RELEASE<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span></span>
<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span></span></code></pre> 
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
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            