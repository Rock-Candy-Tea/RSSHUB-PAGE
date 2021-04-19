
---
title: '数据同步工具 Elasticsearch-datatran v6.2.9 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://esdoc.bbossgroups.com/images/datasyn.png'
author: 开源中国
comments: false
date: Mon, 19 Apr 2021 12:44:00 GMT
thumbnail: 'https://esdoc.bbossgroups.com/images/datasyn.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">数据同步工具 Elasticsearch-datatran 6.2.9 发布，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">Elasticsearch-datatran</a> 由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FREADME" target="_blank">bboss </a>开源的数据同步迁移工具，支持在Elasticsearch、关系数据库(mysql,oracle,db2,sqlserver、达梦等)、Mongodb、HBase、Hive、Kafka、文本文件、SFTP/FTP多种数据源之间进行海量数据同步；支持日志文件实时增量采集</span>到kafka/elasticsearch/database<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="text-align:left"><strong>Elasticsearch版本兼容性：支持</strong>各种Elasticsearch版本（1.x,2.x,5.x,6.x,7.x,+）之间相互数据迁移</p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333"><img alt height="572" src="https://esdoc.bbossgroups.com/images/datasyn.png" width="781" referrerpolicy="no-referrer"></span></p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fchangelog%3Fid%3Dv629-%25e5%258a%259f%25e8%2583%25bd%25e6%2594%25b9%25e8%25bf%259b" target="_blank"><span style="color:#34495e">v6.2.9 功能改进</span></a></p> 
<ol> 
 <li> <p>数据同步改进：完善ip2region和geoip数据库热加载机制</p> </li> 
 <li> <p>Restclient改进：升级httpcliet组件版本到最新的官方版本4.5.13</p> </li> 
 <li> <p>Restclient改进：升级fastxml jackson databind版本2.9.10.8</p> </li> 
 <li> <p>Restclient改进：增加对elasticsearch pit机制的支持，参考用例：</p> <p>testPitId方法</p> <p><a href="https://gitee.com/bboss/eshelloword-spring-boot-starter/blob/master/src/test/java/org/bboss/elasticsearchtest/springboot/SimpleBBossESStarterTestCase.java" target="_blank">https://gitee.com/bboss/eshelloword-spring-boot-starter/blob/master/src/test/java/org/bboss/elasticsearchtest/springboot/SimpleBBossESStarterTestCase.java</a></p> </li> 
 <li> <p>数据同步工具扩展：增加日志文件采集插件，支持全量和增量采集两种模式，实时采集日志文件数据到kafka/elasticsearch/database</p> <p>使用文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Ffilelog-guide" target="_blank">https://esdoc.bbossgroups.com/#/filelog-guide</a></p> <p>日志文件采集插件使用案例：</p> 
  <ol> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbbossgroups%2Ffilelog-elasticsearch%2Fblob%2Fmain%2Fsrc%2Fmain%2Fjava%2Forg%2Fframeworkset%2Felasticsearch%2Fimp%2FFileLog2DBDemo.java" target="_blank">采集日志数据并写入数据库</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbbossgroups%2Ffilelog-elasticsearch%2Fblob%2Fmain%2Fsrc%2Fmain%2Fjava%2Forg%2Fframeworkset%2Felasticsearch%2Fimp%2FFileLog2ESDemo.java" target="_blank">采集日志数据并写入Elasticsearch</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbbossgroups%2Fkafka2x-elasticsearch%2Fblob%2Fmaster%2Fsrc%2Fmain%2Fjava%2Forg%2Fframeworkset%2Felasticsearch%2Fimp%2FFilelog2KafkaDemo.java" target="_blank">采集日志数据并发送到Kafka</a></li> 
  </ol> <p>之前版本升级6.2.9注意事项，需手动修改增量同步状态表结构，增加下面三个字段：</p> <pre><code>status number(1) ,  //数据采集完成状态：0-采集中（默认值）  1-完成  适用于文件日志采集 默认值 0
filePath varchar(500)  //日志文件路径，默认值""
fileId varchar(500)  //日志文件indoe标识，默认值""</code></pre> </li> 
 <li> <p>Restclient改进：设每个elasticsearch数据源默认版本兼容性为7，为了处理启动时无法连接es的情况，可以根据连接的es来配置和调整每个elasticsearch数据源的配置，示例如下： elasticsearch.version=7.12.0</p> </li> 
 <li> <p>调整gradle构建脚本语法，保持与gradle 7的兼容性</p> </li> 
 <li> <p>Restclient改进：elasticsearch节点自动发现和故障节点健康检查后台线程模型调整为daemon模式</p> </li> 
 <li> <p>http-proxy改进：http-proxy节点自动发现和故障节点健康检查后台线程模型调整为daemon模式</p> </li> 
</ol>
                                        </div>
                                      
</div>
            