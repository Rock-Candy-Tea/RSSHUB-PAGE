
---
title: '数据采集 ETL 工具 bboss-datatran v6.7.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a05dc48949c3cec2bdcc08a85184383a4f8.png'
author: 开源中国
comments: false
date: Mon, 15 Aug 2022 09:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a05dc48949c3cec2bdcc08a85184383a4f8.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#333333">数据采集 ETL 工具 bboss-datatran v6.7.2 发布，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">bboss-datatran</a> 是一款基于 java 语言开发的数据采集同步工具，提供数据采集、数据清洗转换处理和数据入库功能，支持在 Elasticsearch、关系数据库 (mysql,oracle,db2,sqlserver、达梦等)、Mongodb、HBase、Hive、Kafka、文本文件 / 日志文件、excel 文件、csv 文件、SFTP/FTP、http/https 等多种数据源之间进行海量数据采集同步；支持数据实时增量和全量数据采集；提供了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-control" target="_blank">作业任务控制 API</a>、作业监控 api，支持作业启动、暂停 (pause)、继续（resume）、停止控制机制；支持http jwt服务认证和数据签名。基于 bboss 可轻松定制一款属于自己的 ETL 管理工具。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:center"><img alt height="736" src="https://oscimg.oschina.net/oscnet/up-a05dc48949c3cec2bdcc08a85184383a4f8.png" width="1283" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><span style="color:#34495e">v6.7.2 功能改进</span></h1> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">数据同步bug修复：执行destroy方法销毁作业时空指针异常问题修复</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">数据同步改进：优化作业销毁机制</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">数据同步改进：优化filelog插件日志采集多行识别处理增量采集机制和未结束多行记录回滚机制</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">数据同步改进：优化kafka输入插件并行消息处理机制</p> </li> 
</ol> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">数据同步作业开发视频教程：</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1xf4y1Z7xu" target="_blank">https://www.bilibili.com/video/BV1xf4y1Z7xu</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>bboss 案例大全</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo" target="_blank">https://esdoc.bbossgroups.com/#/bboss-datasyn-demo</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Quick Start</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fquickstart" target="_blank">https://esdoc.bbossgroups.com/#/quickstart</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>开发交流</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bbossgroups.com%2Fforum.html" target="_blank">https://www.bbossgroups.com/forum.html</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><span style="color:#34495e">bboss插件清单</span></h1> 
<h2 style="margin-left:.8rem; margin-right:0; text-align:start"><span style="color:#34495e">输入插件</span></h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; box-sizing:border-box !important; color:#222222; display:table; font-family:system-ui,-apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif; font-size:17px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:0.544px; margin:0px 0px 10px; max-width:100%; orphans:2; outline:0px; overflow-wrap:break-word !important; padding:0px; text-align:justify; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:677px; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>插件</th> 
   <th>插码名称</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">DBInputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">DB数据库输入插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">配置DB数据源、查询sql、查询sql文件路径及文件名称,支持各种关系数据库，hive</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">ElasticsearchInputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">elasticsearch输出插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">配置elasticsearch数据源、queryDsl、queryDsl配置文件路径等</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">HttpInputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Http输入插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">配置http服务参数、服务地址、服务查询参数、ssl证书等</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">FileInputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">文件输入插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">对应文本类数据文件数据采集配置，源文件目录、Ftp/sftp配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">ExcelFileInputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">excel文件输入插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">excel文件采集映射配置（忽略行数、excel列号与目标字段名称映射、列默认值配置），包括excel源文件目录、Ftp/sftp配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">HBaseInputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">hbase输入插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">hbase连接配置、查询表配置、查询条件配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">MongoDBInputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">mongodb输入插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">mongodb连接配置、查询表配置、查询条件配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Kafka2InputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">kafka输入插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">kafka消费端参数配置、主题配置、客户端消费组配置等</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Kafka1InputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">低版本kafka输入插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">低版本kafka消费端参数配置、主题配置、客户端消费组配置等</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:.8rem; margin-right:0; text-align:start"><span style="color:#34495e">输出插件</span></h2> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"> </p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; box-sizing:border-box !important; color:#222222; display:table; font-family:system-ui,-apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif; font-size:17px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:0.544px; margin:0px 0px 10px; max-width:100%; orphans:2; outline:0px; overflow-wrap:break-word !important; padding:0px; text-align:justify; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:677px; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>插件</th> 
   <th>插码名称</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">DBOutputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">数据库输出插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">数据库地址配置、连接池配置、输出sql、更新sql、deletesql配置、sql文件路径配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">ElasticsearchOutputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Elasticsearch输出插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">elasticsearch地址配置、http连接池配置、账号口令配置、elasticsearch连接参数配置、Elasticsearch输出表配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">HttpOutputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">http/https输出插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">http输出服务参数配置、连接参数配置、监控检查机制配置、ssl证书配置、输出服务地址配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">FileOutputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">文本文件输出插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">文本文件输出配置、文件切割记录数配置、文件行分隔符配置、文件名称生成规则配置、记录标题行配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">ExcelFileOutputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">excel文件输出插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Excel文件输出配置、列号与字段映射配置、标题配置、sheet配置、列标题配置、文件切割记录数配置、文件行分隔符配置、文件名称生成规则配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Kafka2OutputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">kafka输出插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">kafka输出参数配置、主题配置、记录序列化机制配置、记录生成器配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Kafka1OutputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">低版本kafka输出插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">低版本kafka输出参数配置、主题配置、记录序列化机制配置、记录生成器配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">CustomOupputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">自定义输出插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">提供自定义处理采集数据功能，可以按照自己的要求将采集的数据处理到目的地，如需定制化将数据保存到特定的地方，可自行实现CustomOutPut接口处理即可</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">DummyOutputConfig</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">dummy插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">调试作业使用，将采集的数据直接输出到控制台</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">bboss具备良好的扩展性，可以非常方便地扩展bboss数据采集插件。</p> 
<p> </p>
                                        </div>
                                      
</div>
            