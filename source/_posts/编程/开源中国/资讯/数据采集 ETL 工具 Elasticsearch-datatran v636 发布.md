
---
title: '数据采集 ETL 工具 Elasticsearch-datatran v6.3.6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://esdoc.bbossgroups.com/images/datasyn.png'
author: 开源中国
comments: false
date: Mon, 18 Oct 2021 12:40:00 GMT
thumbnail: 'https://esdoc.bbossgroups.com/images/datasyn.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据采集ETL工具 Elasticsearch-datatran v6.3.6 发布，本版本提供大家期待已久的<strong>记录切割功能</strong>和<strong>ftp文件下载采集</strong>功能<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">Elasticsearch-datatran</a> 由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FREADME" target="_blank">bboss </a>开源的数据采集同步ETL工具，提供数据采集、数据处理清洗和数据入库功能。支持在Elasticsearch、关系数据库(mysql,oracle,db2,sqlserver、达梦等)、Mongodb、HBase、Hive、Kafka、文本文件、SFTP/FTP多种数据源之间进行海量数据同步；支持本地/ftp日志文件实时增量采集</span>到kafka/elasticsearch/database<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Elasticsearch版本兼容性：支持</strong>各种Elasticsearch版本（1.x,2.x,5.x,6.x,7.x,+）之间相互数据迁移</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="736" src="https://esdoc.bbossgroups.com/images/datasyn.png" width="1232" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>v6.3.6 变更记录</strong></p> 
<ol> 
 <li>数据同步改进：增加<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool%3Fid%3D_2322-%25e8%25ae%25b0%25e5%25bd%2595%25e5%2588%2587%25e5%2589%25b2" target="_blank">记录切割</a>功能，可以将指定的字段拆分为多条新记录，新产生的记录会自动继承原记录其他字段数据，亦可以指定覆盖原记录字段值</li> 
 <li> <p style="margin-left:0; margin-right:0">数据同步功能：扩展filelog插件，增加对<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Ffilelog-guide%3Fid%3D_7ftp%25e9%2587%2587%25e9%259b%2586%25e9%2585%258d%25e7%25bd%25ae" target="_blank">ftp日志文件下载采集</a>支持，支持实时监听下载ftp目录下生成的日志文件，将ftp文件中的数据采集写入elasticsearch、数据库、推送kafka、写入新的日志文件，参考案例：<span> </span><a href="https://gitee.com/bboss/filelog-elasticsearch/blob/v6.3.6/src/main/java/org/frameworkset/elasticsearch/imp/FtpLog2ESETLScheduleDemo.java" target="_blank">FtpLog2ESETLScheduleDemo.java</a><span> </span><a href="https://gitee.com/bboss/filelog-elasticsearch/blob/v6.3.6/src/main/java/org/frameworkset/elasticsearch/imp/FtpLog2ESDemo.java" target="_blank">FtpLog2ESDemo</a></p> </li> 
</ol> 
<p style="margin-left:0; margin-right:0"><img alt src="https://esdoc.bbossgroups.com/images/filelog-es.jpg" referrerpolicy="no-referrer"></p> 
<ol start="2"> 
 <li> <p style="margin-left:0; margin-right:0">数据同步功能：支持备份采集完毕日志文件功能，可以指定备份文件保存时长，定期清理超过时长文件</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">数据同步功能：提供自定义处理采集数据功能，可以自行将采集的数据按照自己的要求进行处理到目的地，支持数据来源包括：database，elasticsearch，kafka，mongodb，hbase，file，ftp等，想把采集的数据保存到什么地方，有自己实现CustomOutPut接口处理即可</p> </li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>FileLog2DummyExportBuilder importBuilder <span>=</span> <span style="color:#e96900">new</span> <span>FileLog2DummyExportBuilder</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
<span style="color:#8e908c">//自己处理数据</span>
importBuilder<span style="color:#525252">.</span><span style="color:#e96900">setCustomOutPut</span><span style="color:#525252">(</span><span style="color:#e96900">new</span> <span>CustomOutPut</span><span style="color:#525252">(</span><span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
   <span style="color:#525252">@Override</span>
   <span style="color:#e96900">public</span> <span style="color:#e96900">void</span> <span style="color:#e96900">handleData</span><span style="color:#525252">(</span>TaskContext taskContext<span style="color:#525252">,</span> List<span style="color:#e96900"><span style="color:#525252"><</span>CommonRecord<span style="color:#525252">></span></span> datas<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>

      <span style="color:#8e908c">//You can do any thing here for datas</span>
      <span style="color:#e96900">for</span><span style="color:#525252">(</span>CommonRecord record<span>:</span>datas<span style="color:#525252">)</span><span style="color:#525252">&#123;</span>
         Map<span style="color:#e96900"><span style="color:#525252"><</span>String<span style="color:#525252">,</span>Object<span style="color:#525252">></span></span> data <span>=</span> record<span style="color:#525252">.</span><span style="color:#e96900">getDatas</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
         logger<span style="color:#525252">.</span><span style="color:#e96900">info</span><span style="color:#525252">(</span>SimpleStringUtil<span style="color:#525252">.</span><span style="color:#e96900">object2json</span><span style="color:#525252">(</span>data<span style="color:#525252">)</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
      <span style="color:#525252">&#125;</span>
   <span style="color:#525252">&#125;</span>
<span style="color:#525252">&#125;</span><span style="color:#525252">)</span><span style="color:#525252">;</span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">自定义处理采集数据功能典型的应用场景就是对接大数据流处理，直接将采集的数据交给一些流处理框架，譬如与我们内部自己开发的大数据流处理框架对接，效果简直不要不要的，哈哈。</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><a href="https://gitee.com/bboss/filelog-elasticsearch/blob/v6.3.6/src/main/java/org/frameworkset/elasticsearch/imp/FileLog2CustomDemo.java" target="_blank">采集日志文件自定义处理案例</a></p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo%3Fid%3Dbboss%25e6%2595%25b0%25e6%258d%25ae%25e9%2587%2587%25e9%259b%2586etl%25e6%25a1%2588%25e4%25be%258b%25e5%25a4%25a7%25e5%2585%25a8" target="_blank"><span style="color:#34495e">bboss数据采集ETL案例大全</span></a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo" target="_blank">https://esdoc.bbossgroups.com/#/bboss-datasyn-demo</a></p>
                                        </div>
                                      
</div>
            