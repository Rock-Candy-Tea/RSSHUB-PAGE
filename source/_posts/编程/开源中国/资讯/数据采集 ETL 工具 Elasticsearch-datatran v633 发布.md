
---
title: '数据采集 ETL 工具 Elasticsearch-datatran v6.3.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-15e5da3306591cbfb9237eb3a1f7616379c.png'
author: 开源中国
comments: false
date: Fri, 13 Aug 2021 01:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-15e5da3306591cbfb9237eb3a1f7616379c.png'
---

<div>   
<div class="content">
                                                                                            <p>数据采集ETL工具 Elasticsearch-datatran v6.3.3 发布， <span style="background-color:#ffffff; color:#333333">v6.3.3修复了v6.3.2,v6.3.1版本引入的一系列问题，建议升级。</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">Elasticsearch-datatran</a> 由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FREADME" target="_blank">bboss </a>开源的数据采集同步ETL工具，提供数据采集、数据处理清洗和数据入库功能。支持在Elasticsearch、关系数据库(mysql,oracle,db2,sqlserver、达梦等)、Mongodb、HBase、Hive、Kafka、文本文件、SFTP/FTP多种数据源之间进行海量数据同步；支持日志文件实时增量采集</span>到kafka/elasticsearch/database<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="text-align:left"><strong>Elasticsearch版本兼容性：支持</strong>各种Elasticsearch版本（1.x,2.x,5.x,6.x,7.x,+）之间相互数据迁移</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-15e5da3306591cbfb9237eb3a1f7616379c.png" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:start"><span style="color:#34495e">v6.3.3 功能改进</span></h1> 
<ol> 
 <li> <p>数据同步改进：处理异步更新状态可能导致的死锁问题</p> </li> 
 <li> <p>数据同步改进：处理在closeEOF为true情况下filelog插件重启后不采集数据问题和filelog插件不采集新增文件数据问题</p> </li> 
 <li> <p>数据同步改进：优化作业停止资源处理机制</p> </li> 
 <li> <p>数据同步改进：优化作业状态管理机制</p> </li> 
 <li> <p>数据同步改进：filelog插件增加FileFilter机制，自定义筛选需要采集日志的文件</p> </li> 
</ol> 
<h1 style="text-align:start"><span style="color:#34495e">v6.3.2 功能改进</span></h1> 
<ol> 
 <li> <p>数据同步改进：启用日志文件采集探针closeOlderTime配置，允许文件内容静默最大时间，单位毫秒，如果在idleMaxTime访问内一直没有数据更新，认为文件是静默文件，将不再采集静默文件数据，关闭文件对应的采集线程，作业重启后也不会采集</p> </li> 
 <li> <p>数据同步改进：日志文件采集插件增加对CallInterceptor的支持，采集文件任务新增/结束时会调用拦截器方法，可以在refactor方法中获取拦截器设置的数据，文件采集完毕后释放</p> </li> 
 <li> <p>数据同步工具完善：修复同步数据到kafka productor初始化问题</p> </li> 
 <li> <p>数据同步工具完善：修复停止filelog作业报错问题</p> </li> 
 <li> <p>数据同步工具改进：发送kafka控件改进，设置发送多少条消息后打印发送统计信息</p> </li> 
</ol> 
<h1 style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo%3Fid%3Dbboss%25e6%2595%25b0%25e6%258d%25ae%25e9%2587%2587%25e9%259b%2586etl%25e6%25a1%2588%25e4%25be%258b%25e5%25a4%25a7%25e5%2585%25a8" target="_blank"><span style="color:#34495e">bboss数据采集ETL案例大全</span></a></h1> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo" target="_blank">https://esdoc.bbossgroups.com/#/bboss-datasyn-demo</a></p>
                                        </div>
                                      
</div>
            