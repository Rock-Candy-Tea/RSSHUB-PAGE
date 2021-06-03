
---
title: '数据采集ETL工具 Elasticsearch-datatran v6.3.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a4de01eaf0de04d13c4de23c9e4f61f6791.png'
author: 开源中国
comments: false
date: Thu, 03 Jun 2021 10:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a4de01eaf0de04d13c4de23c9e4f61f6791.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">数据采集ETL工具 Elasticsearch-datatran 6.3.0 发布，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">Elasticsearch-datatran</a> 由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FREADME" target="_blank">bboss </a>开源的数据采集同步ETL工具，提供数据采集、数据处理清洗和数据入库功能。支持在Elasticsearch、关系数据库(mysql,oracle,db2,sqlserver、达梦等)、Mongodb、HBase、Hive、Kafka、文本文件、SFTP/FTP多种数据源之间进行海量数据同步；支持日志文件实时增量采集</span>到kafka/elasticsearch/database<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="text-align:left"><strong>Elasticsearch版本兼容性：支持</strong>各种Elasticsearch版本（1.x,2.x,5.x,6.x,7.x,+）之间相互数据迁移</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-a4de01eaf0de04d13c4de23c9e4f61f6791.png" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fchangelog%3Fid%3Dv630-%25e5%258a%259f%25e8%2583%25bd%25e6%2594%25b9%25e8%25bf%259b" target="_blank"><span style="color:#34495e">v6.3.0 功能改进</span></a></h1> 
<ol> 
 <li>elasticsearch rest client改进：优化批处理性能，执行批处理bulk操作后，默认只返回三个信息：took,errors,items.*.error，既耗时、错误标记、错误记录信息</li> 
 <li>数据同步功能改进：日志文件采集插件添加控制是否删除采集完的文件控制变量，默认false 不删除，true 删除</li> 
 <li>数据同步功能bug修复：修复hbase数据导出因columns信息为空导致的导出异常</li> 
 <li>数据同步功能bug修复：修改es2db导出时存在targetdb空指针问题</li> 
 <li>数据同步功能改进：增加采集日志文件数据，导出到文件并上传ftp/sftp服务器功能</li> 
 <li>数据同步功能改进：从kafka接收数据，处理后按照固定记录条数导出到文件并上传ftp/sftp服务器功能</li> 
 <li>数据同步功能改进：增加hbase数据导出到文件并上传ftp/sftp服务器功能</li> 
 <li>数据同步功能改进：增加mongodb数据导出到文件并上传ftp/sftp服务器功能</li> 
 <li>数据同步功能改进：增加hbase、mongodb到dummy/logger的输出功能</li> 
 <li>数据同步功能改进：增加日志文件数据采集到dummy/logger的输出功能</li> 
 <li>数据同步功能改进：增加kafka到dummy/logger输出功能</li> 
 <li>数据同步工具改进：增加kafka、hbase、mongodb到kafka的数据抽取同步功能</li> 
 <li>数据同步功能改进：增加hbase到database数据同步功能</li> 
 <li>数据同步功能改进：增加数据库/elasticsearch数据导出（增量/全量）到log4j日志文件dummy插件</li> 
</ol> 
<p style="text-align:start"><strong>说明：</strong>数据同步功能新增的dummy插件，便于调试采集数据作业，将采集的数据打印到控制台，观察数据的正确性</p> 
<h1 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo%3Fid%3Dbboss%25e6%2595%25b0%25e6%258d%25ae%25e9%2587%2587%25e9%259b%2586etl%25e6%25a1%2588%25e4%25be%258b%25e5%25a4%25a7%25e5%2585%25a8" target="_blank"><span style="color:#34495e">bboss数据采集ETL案例大全</span></a></h1> 
<h1 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo" target="_blank">https://esdoc.bbossgroups.com/#/bboss-datasyn-demo</a></h1>
                                        </div>
                                      
</div>
            