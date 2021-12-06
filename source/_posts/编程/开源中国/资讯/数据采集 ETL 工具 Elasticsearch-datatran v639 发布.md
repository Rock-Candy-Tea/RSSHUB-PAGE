
---
title: '数据采集 ETL 工具 Elasticsearch-datatran v6.3.9 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6a76b2f36cfa35d9bd8f617abc3636b7ee8.png'
author: 开源中国
comments: false
date: Mon, 06 Dec 2021 12:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6a76b2f36cfa35d9bd8f617abc3636b7ee8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据采集ETL工具 Elasticsearch-datatran v6.3.9 发布<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">Elasticsearch-datatran</a> 由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FREADME" target="_blank">bboss </a>开源的数据采集同步ETL工具，提供数据采集、数据清洗转换处理和数据入库功能。支持在Elasticsearch、关系数据库(mysql,oracle,db2,sqlserver、达梦等)、Mongodb、HBase、Hive、Kafka、文本文件、SFTP/FTP多种数据源之间进行海量数据采集同步；支持本地/ftp日志文件实时增量采集</span>到kafka/elasticsearch/database；支持根据字段进行数据记录切割；支持根据文件路径信息将不同文件数据写入不同的数据库表<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#34495e">提供自定义处理采集数据功能，可以按照自己的要求将采集的数据</span><span style="background-color:#ffffff; color:#34495e">处理到目的地，支持数据来源包括：database，elasticsearch，kafka，mongodb，hbase，file，ftp等，想把采集的数据保存到什么地方，由自己实现CustomOutPut接口处理即可。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Elasticsearch版本兼容性：支持</strong>各种Elasticsearch版本（1.x,2.x,5.x,6.x,7.x,+）之间相互数据迁移</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="736" src="https://oscimg.oschina.net/oscnet/up-6a76b2f36cfa35d9bd8f617abc3636b7ee8.png" width="1232" referrerpolicy="no-referrer"></p> 
<p><strong>v6.3.9 功能改进</strong></p> 
<ol> 
 <li>修复db-es数据同步时，指定了任务拦截器，但是处理任务上下文中没有指定任务级别的sql语句时空指针问题</li> 
 <li>bboss安全过滤器改造：增加xss攻击和敏感词攻击策略配置</li> 
 <li>数据采集作业运行工具改进：完善运行容器工具，增加启动bootrap类，负责运行、停止、重启mainclass，并将mainclass运行、停止、重启过程中的日志、异常输出到log日志文件</li> 
</ol> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">导入微服务容器组件包：由bboss-rt调整为bboss-bootstrap-rt</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><strong style="color:#2c3e50">gradle坐标</strong></p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><code>group<span>:</span> <span style="color:var(--theme-color,#42b983)">'com.bbossgroups'</span><span style="color:#525252">,</span> name<span>:</span> <span style="color:var(--theme-color,#42b983)">'bboss-bootstrap-rt'</span><span style="color:#525252">,</span> version<span>:</span> <span style="color:var(--theme-color,#42b983)">"5.8.5"</span><span style="color:#525252">,</span>transitive<span>:</span> <span style="color:#c76b29">true</span> </code></p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><strong style="color:#2c3e50">maven坐标</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>  <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>  
      <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.bbossgroups<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>  
      <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>bboss-bootstrap-rt<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>  
      <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>5.8.5<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>  
  <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>  </code></pre> 
<ol start="4"> 
 <li>运行容器工具改进：停止进程时需等待进程停止完毕再退出</li> 
 <li>敏感信息处理：对httpproxy和elasticsearch客户端输出日志中的用户口令信息进行脱敏处理</li> 
 <li>兼容老版本升级到最新的数据同步框架：自动创建增量状态表和增量状态历史表中新增的字段</li> 
 <li>修复httpproxy问题：停止默认连接池时，没有清空默认配置对象</li> 
 <li>完善数据同步异常处理机制：捕获插件初始化异常并输出到日志文件</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo%3Fid%3Dbboss%25e6%2595%25b0%25e6%258d%25ae%25e9%2587%2587%25e9%259b%2586etl%25e6%25a1%2588%25e4%25be%258b%25e5%25a4%25a7%25e5%2585%25a8" target="_blank"><span style="color:#34495e">bboss数据采集ETL案例大全</span></a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo" target="_blank">https://esdoc.bbossgroups.com/#/bboss-datasyn-demo</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            