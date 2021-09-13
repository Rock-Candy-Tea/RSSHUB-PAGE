
---
title: 'BeetlSQL 3.8.0 发布，流行的 Java DAO 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
author: 开源中国
comments: false
date: Mon, 13 Sep 2021 13:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
---

<div>   
<div class="content">
                                                                                            <p>本次发布合并了BeetlSQL使用者的若干PR</p> 
<ul> 
 <li>PageRequest 新增 listRequeired属性，如果设置位false，则只查询总数，不会查询列表</li> 
 <li>SpringBoot集成增强，如果已经使用了Spring Boot内置的数据源，则默认采用</li> 
 <li>自定义事务管理器,优化了事务关闭链接</li> 
 <li>新增updateRowById, 此方法将忽略POJO的@Version @InsertIgnore等注解，直接按照属性来保存数据</li> 
 <li>在Saga回滚中，使用updateRowById代替updateById</li> 
 <li>对GreenPlum 支持</li> 
</ul> 
<pre><code class="language-xml"><dependency>
    <groupId>com.ibeetl</groupId>
    <artifactId>beetlsql</artifactId>
    <version>3.8.0-RELEASE</version>
</dependency></code></pre> 
<div> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">BeetlSQL 自主研发自2015年，目标是提供开发高效，维护高效，运行高效的数据访问框架，它适用范围广，定制性强，写起数据库访问代码特别顺滑,不亚于MyBatis. 你不想写SQL也好，或者想更好的写SQL也好，BeetlSQL都能满足这要求，目前支持的数据库如下</p> 
 <ul style="box-sizing: inherit; margin: 0px 0px 20px; list-style-type: disc; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"> 
  <li style="box-sizing: inherit; line-height: 1.875em; margin-top: 0px;">传统数据库：MySQL,MariaDB,Oralce,Postgres,DB2,SQL Server，H2,SQLite,Derby，神通，达梦，华为高斯，人大金仓，PolarDB 等</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">大数据：HBase，ClickHouse，Cassandar，Hive,GreenPlum</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">物联网时序数据库：Machbase，TD-Engine，IotDB</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">SQL查询引擎:Drill,Presto，Druid</li> 
  <li style="box-sizing: inherit; line-height: 1.875em; margin-bottom: 0px;">内存数据库:ignite，CouchBase</li> 
 </ul> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide" style="box-sizing: inherit; background-color: transparent; color: rgb(52, 111, 182); text-decoration: none;" target="_blank">阅读文档</a><span style="box-sizing: inherit; background-color: rgb(255, 255, 255); color: rgb(51, 51, 51);"> </span><a href="https://gitee.com/xiandafu/beetlsql" style="box-sizing: inherit; background-color: transparent; color: rgb(52, 111, 182); text-decoration: none;">源码和例子</a> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F121.42.237.11%3A8080%2Fbeetlsql_online%2F" style="box-sizing: inherit; background-color: transparent; color: rgb(52, 111, 182); text-decoration: none;" target="_blank">在线体验</a> <a href="https://gitee.com/xiandafu/dao-benchmark" style="box-sizing: inherit; background-color: transparent; color: rgb(52, 111, 182); text-decoration: none;">性能测试</a></p> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">BeetlSQL也支持IDEA插件，提供向导和自动提示</p> 
 <p style="box-sizing: inherit; margin: 0px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"><img alt class="zoom-in-cursor" height="288" src="https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" width="600" referrerpolicy="no-referrer"></p> 
</div>
                                        </div>
                                      
</div>
            