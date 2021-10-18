
---
title: 'Elasticsearch Rest Client bboss v6.3.6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=77'
author: 开源中国
comments: false
date: Mon, 18 Oct 2021 13:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=77'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><em>The best Elasticsearch Highlevel Rest  Client API-----<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FREADME" target="_blank">bboss   </a></em></strong> v6.3.6 发布。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">bboss elasticsearch 是一套基 于query dsl 语法操作和访问分布式搜索引擎 elasticsearch 的 o/r mapping 高性能java开发库，底层基于 es restful api。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>主要功能特色</strong></h4> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">ORM和DSL二者兼顾，类mybatis方式操作ElasticSearch,提供丰富的开发<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdocument-crud" target="_blank">API</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FElasticsearch-demo" target="_blank">开发Demo</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">采用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdevelopment%3Fid%3D_53-dsl%25e9%2585%258d%25e7%25bd%25ae%25e8%25a7%2584%25e8%258c%2583" target="_blank">XML文件配置和管理检索dsl脚本</a>，简洁而直观；只需编写好dsl，放入xml配置文件，通过bboss api完成相应的检索查询操作即可；提供丰富的逻辑判断语法,在dsl脚本中可以使用变量、脚本片段、foreach循环、逻辑判断、注释；基于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-dsl" target="_blank">可扩展DSL配置管理机制</a>可以非常方便地实现数据库、redis等方式管理dsl;配置管理的dsl语句支持在线修改、自动热加载，支持在线控制将运行时dsl打印到日志文件功能，开发和调试非常方便</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提供Elasticsearch集群节点自动负载均衡和容灾恢复机制，Elasticsearch节点断连恢复后可自动重连，高效可靠</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提供Elasticsearch集群节点<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdevelopment%3Fid%3D_23-%25e9%259b%2586%25e7%25be%25a4%25e8%258a%2582%25e7%2582%25b9%25e8%2587%25aa%25e5%258a%25a8%25e5%258f%2591%25e7%258e%25b0discover%25e6%258e%25a7%25e5%2588%25b6%25e5%25bc%2580%25e5%2585%25b3" target="_blank">自动发现机制</a>：自动发现Elasticsearch服务端节点增加和下线操作并变更客户端集群可用节点地址清单;提供api自定义发现Elasticsearch节点发现机制</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提供<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdevelopment%3Fid%3D_26-http%25e5%258d%258f%25e8%25ae%25ae%25e9%2585%258d%25e7%25bd%25ae" target="_blank">http 连接池管理</a>功能，提供精细化的http连接池参数配置管理</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持在应用中<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdevelopment%3Fid%3D_52-%25e5%25a4%259aelasticsearch%25e6%259c%258d%25e5%258a%25a1%25e5%2599%25a8%25e9%259b%2586%25e7%25be%25a4%25e6%2594%25af%25e6%258c%2581" target="_blank">访问和操作多个Elasticsearch集群</a>，每个Elasticsearch集群的版本可以不同</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持基于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fcn%2Fproducts%2Fx-pack" target="_blank">X-Pack</a>和searchguard两种<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdevelopment%3Fid%3D_21-es%25e6%259c%258d%25e5%258a%25a1%25e5%2599%25a8%25e8%25b4%25a6%25e5%258f%25b7%25e5%2592%258c%25e5%258f%25a3%25e4%25bb%25a4%25e9%2585%258d%25e7%25bd%25ae" target="_blank">安全认证机制</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FElasticsearch-SQL-ORM" target="_blank">Elasticsearch-SQL-ORM</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FElasticsearch-JDBC" target="_blank">Elasticsearch-JDBC</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提供高效的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FbulkProcessor" target="_blank">BulkProcessor处理机制</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提供快速而高效的数据同步导入ES工具，<strong>支持增、删、改数据同步</strong>：支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">DB到Elasticsearch</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool%3Fid%3D_3-elasticsearch-db%25e6%2595%25b0%25e6%258d%25ae%25e5%2590%258c%25e6%25ad%25a5%25e4%25bd%25bf%25e7%2594%25a8%25e6%2596%25b9%25e6%25b3%2595" target="_blank">Elasticsearch到DB</a>,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fmongodb-elasticsearch" target="_blank">MongoDB到Elastisearch数据同步</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fhbase-elasticsearch" target="_blank">HBase到Elasticsearch数据同步</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool%3Fid%3D_7-kafka2x-elasticsearch%25e6%2595%25b0%25e6%258d%25ae%25e5%2590%258c%25e6%25ad%25a5%25e4%25bd%25bf%25e7%2594%25a8%25e6%2596%25b9%25e6%25b3%2595" target="_blank">Kafka到Elasticsearch数据同步</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool%3Fid%3D_5-database-database%25E6%2595%25B0%25E6%258D%25AE%25E5%2590%258C%25E6%25AD%25A5%25E4%25BD%25BF%25E7%2594%25A8%25E6%2596%25B9%25E6%25B3%2595" target="_blank">DB到DB之间数据同步</a>，后续将支持更多的数据源</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提供按时间日期<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Felasticsearch-indexclean-task" target="_blank">ES历史数据清理工具</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">APM开源产品pinpoint官方Elasticsearch bboss 客户端性能监控插件，插件地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnaver%2Fpinpoint%2Ftree%2Fmaster%2Fplugins%2Felasticsearch-bboss" target="_blank">https://github.com/naver/pinpoint/tree/master/plugins/elasticsearch-bboss</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:start">与Elasticsearch、Spring boot、jdk兼容性</p> 
  <table cellspacing="0" style="border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-size:14px; line-height:inherit; margin:0px 0px 20px; max-width:100%; overflow:auto; width:1320px; word-break:keep-all"> 
   <tbody> 
    <tr> 
     <th>bboss</th> 
     <th>Elasticsearch</th> 
     <th>spring boot</th> 
    </tr> 
   </tbody> 
   <tbody> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">2.x</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">3.x</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">5.x</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">6.x</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">7.x</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
    </tr> 
   </tbody> 
  </table> <p style="margin-left:0; margin-right:0; text-align:start">jdk兼容性：jdk 1.7+</p> </li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>v6.3.6 功能改进</strong></p> 
<p>ClientInterface增加一组指定elasticsearch datasource名称的方法，可以在方法级指定需要操作的elasticsearch数据源名称，详情接口api定义如下：</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><a href="https://gitee.com/bboss/bboss-elastic/blob/v6.3.6/bboss-elasticsearch-rest/src/main/java/org/frameworkset/elasticsearch/client/ClientInterfaceWithESDatasource.java" target="_blank">https://gitee.com/bboss/bboss-elastic/blob/v6.3.6/bboss-elasticsearch-rest/src/main/java/org/frameworkset/elasticsearch/client/ClientInterfaceWithESDatasource.java</a></p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">使用参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdevelopment%3Fid%3D_523-%25e5%259c%25a8%25e6%258e%25a5%25e5%258f%25a3%25e6%2596%25b9%25e6%25b3%2595%25e4%25b8%258a%25e6%258c%2587%25e5%25ae%259adatasourcename" target="_blank">5.2.3 在接口方法上指定datasourceName</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更多版本变更记录访问</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fchangelog" target="_blank">https://esdoc.bbossgroups.com/#/changelog</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Elasticsearch bboss使用文档</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fquickstart" target="_blank">https://esdoc.bbossgroups.com/#/quickstart</a></li> 
</ul>
                                        </div>
                                      
</div>
            