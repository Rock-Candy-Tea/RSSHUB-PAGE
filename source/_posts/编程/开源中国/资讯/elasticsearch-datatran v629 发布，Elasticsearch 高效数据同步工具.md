
---
title: 'elasticsearch-datatran v6.2.9 发布，Elasticsearch 高效数据同步工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4890'
author: 开源中国
comments: false
date: Mon, 19 Apr 2021 11:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4890'
---

<div>   
<div class="content">
                                                                    
                                                        <p>elasticsearch-datatran v6.2.9 已经发布，这是一个 Elasticsearch 高效数据同步工具。Elasticsearch-datatran 由 bboss 开源的数据同步迁移工具，支持在Elasticsearch、关系数据库(mysql,oracle,db2,sqlserver、达梦等)、Mongodb、HBase、Hive、Kafka、文本文件、SFTP/FTP多种数据源之间进行海量数据同步；支持日志文件实时增量采集到kafka/elasticsearch/database。</p> 
<p>Elasticsearch版本兼容性：支持各种Elasticsearch版本（1.x,2.x,5.x,6.x,7.x,+）之间相互数据迁移。</p> 
<p>v6.2.9 功能改进</p> 
<p>数据同步改进：完善ip2region和geoip数据库热加载机制</p> 
<p>Restclient改进：升级httpcliet组件版本到最新的官方版本4.5.13</p> 
<p>Restclient改进：升级fastxml jackson databind版本2.9.10.8</p> 
<p>Restclient改进：增加对elasticsearch pit机制的支持，参考用例：</p> 
<p>testPitId方法</p> 
<p><a href="https://gitee.com/bboss/eshelloword-spring-boot-starter/blob/master/src/test/java/org/bboss/elasticsearchtest/springboot/SimpleBBossESStarterTestCase.java" target="_blank">https://gitee.com/bboss/eshelloword-spring-boot-starter/blob/master/src/test/java/org/bboss/elasticsearchtest/springboot/SimpleBBossESStarterTestCase.java</a></p> 
<p>数据同步工具扩展：增加日志文件采集插件，支持全量和增量采集两种模式，实时采集日志文件数据到kafka/elasticsearch/database</p> 
<p>使用文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Ffilelog-guide" target="_blank">https://esdoc.bbossgroups.com/#/filelog-guide</a></p> 
<p>日志文件采集插件使用案例：</p> 
<p>采集日志数据并写入数据库 采集日志数据并写入Elasticsearch 采集日志数据并发送到Kafka 之前版本升级6.2.9注意事项，需手动修改增量同步状态表结构，增加下面三个字段：</p> 
<p>status number(1) , //数据采集完成状态：0-采集中（默认值） 1-完成 适用于文件日志采集 默认值 0 filePath varchar(500) //日志文件路径，默认值"" fileId varchar(500) //日志文件indoe标识，默认值"" Restclient改进：设每个elasticsearch数据源默认版本兼容性为7，为了处理启动时无法连接es的情况，可以根据连接的es来配置和调整每个elasticsearch数据源的配置，示例如下： elasticsearch.version=7.12.0</p> 
<p>调整gradle构建脚本语法，保持与gradle 7的兼容性</p> 
<p>Restclient改进：elasticsearch节点自动发现和故障节点健康检查后台线程模型调整为daemon模式</p> 
<p>http-proxy改进：http-proxy节点自动发现和故障节点健康检查后台线程模型调整为daemon模式</p> 
<p>详情查看：<a href="https://gitee.com/bboss/bboss-elastic-tran/releases/v6.2.9">https://gitee.com/bboss/bboss-elastic-tran/releases/v6.2.9</a></p>
                                        </div>
                                      
</div>
            