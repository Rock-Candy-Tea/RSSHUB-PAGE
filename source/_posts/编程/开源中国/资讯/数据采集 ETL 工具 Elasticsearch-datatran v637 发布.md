
---
title: '数据采集 ETL 工具 Elasticsearch-datatran v6.3.7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6a76b2f36cfa35d9bd8f617abc3636b7ee8.png'
author: 开源中国
comments: false
date: Thu, 04 Nov 2021 09:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6a76b2f36cfa35d9bd8f617abc3636b7ee8.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据采集ETL工具 Elasticsearch-datatran v6.3.7 发布<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">Elasticsearch-datatran</a> 由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FREADME" target="_blank">bboss </a>开源的数据采集同步ETL工具，提供数据采集、数据处理和数据入库功能。支持在Elasticsearch、关系数据库(mysql,oracle,db2,sqlserver、达梦等)、Mongodb、HBase、Hive、Kafka、文本文件、SFTP/FTP多种数据源之间进行海量数据采集同步；支持本地/ftp日志文件实时增量采集</span>到kafka/elasticsearch/database；支持根据字段进行数据记录切割；支持根据文件路径信息将不同文件数据写入不同的数据库表<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#34495e">提供自定义处理采集数据功能，可以按照自己的要求将采集的数据</span><span style="background-color:#ffffff; color:#34495e">处理到目的地，支持数据来源包括：database，elasticsearch，kafka，mongodb，hbase，file，ftp等，想把采集的数据保存到什么地方，由自己实现CustomOutPut接口处理即可。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Elasticsearch版本兼容性：支持</strong>各种Elasticsearch版本（1.x,2.x,5.x,6.x,7.x,+）之间相互数据迁移</p> 
<p><img height="736" src="https://oscimg.oschina.net/oscnet/up-6a76b2f36cfa35d9bd8f617abc3636b7ee8.png" width="1232" referrerpolicy="no-referrer"></p> 
<p><strong style="color:#333333">v6.3.7 变更记录</strong></p> 
<ol> 
 <li>elasticsearch客户端改进：多数据源支持数据源引用功能，如果两个数据源都指向同一个数据源，则可以将第二个数据源指向第一个数据源，配置示例：</li> 
</ol> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">普通项目</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#2973b7">elasticsearch.referExternal</span><span style="color:#525252">=</span><span style="color:var(--theme-color,#42b983)">default</span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">spring boot项目</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#2973b7">spring.elasticsearch.bboss.elasticsearch.referExternal</span><span style="color:#525252">=</span><span style="color:var(--theme-color,#42b983)">default</span></code></pre> 
<ol start="2"> 
 <li>数据源同步改进：增加自定义定时同步调度机制，可以指定作业执行的时间段（支持指定多个时间段）和忽略执行时间段（支持指定多个时间段），使用案例：</li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>        <span style="color:#8e908c">//定时任务配置，</span>
        importBuilder<span style="color:#525252">.</span><span style="color:#e96900">setScheduleSelf</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#8e908c">//使用bboss自带的定时器,bboss timer</span>
                <span style="color:#525252">.</span><span style="color:#e96900">setDeyLay</span><span style="color:#525252">(</span><span style="color:#c76b29">1000</span>L<span style="color:#525252">)</span> <span style="color:#8e908c">// 任务延迟执行deylay毫秒后执行</span>
                <span style="color:#525252">.</span><span style="color:#e96900">setPeriod</span><span style="color:#525252">(</span><span style="color:#c76b29">1</span><span>*</span><span style="color:#c76b29">60</span><span>*</span><span style="color:#c76b29">1000</span>l<span style="color:#525252">)</span><span style="color:#8e908c">//每隔period毫秒执行，如果不设置，只执行一次</span>
                <span style="color:#525252">.</span><span style="color:#e96900">addScanNewFileTimeRange</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"12:37-23:59"</span><span style="color:#525252">)</span><span style="color:#525252">;</span><span style="color:#8e908c">//添加每天调度执行的时间段，可以调用多次addScanNewFileTimeRange方法添加多个时间段</span>
                <span style="color:#8e908c">//添加每天排除的时间段（不调度执行作业），可以调用多次addSkipScanNewFileTimeRange方法添加多个时间段,设置addScanNewFileTimeRange，则SkipScanNewFileTimeRange不起作用</span>
<span style="color:#8e908c">//                .addSkipScanNewFileTimeRange("11:30-13:00");</span>
        <span style="color:#8e908c">//定时任务配置结束</span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">如果是Filelog插件，还需要额外指定：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>        FileImportConfig config <span>=</span> <span style="color:#e96900">new</span> <span>FileImportConfig</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span style="color:#8e908c">/**
        * 设置是否采用外部新文件扫描调度机制：bboss timer,jdk timer,quartz,xxl-job
        * true 采用，false 不采用，默认false
        */</span>
        config<span style="color:#525252">.</span><span style="color:#e96900">setUseETLScheduleForScanNewFile</span><span style="color:#525252">(</span><span style="color:#c76b29">true</span><span style="color:#525252">)</span><span style="color:#525252">;</span>        </code></pre> 
<ol start="3"> 
 <li> <p style="margin-left:0; margin-right:0">在任务CallInterceptor.preCall中，可以根据taskContext中对应的不同的文件指定不同数据库添加、修改、删除sql,使用参考案例：</p> <pre style="margin-left:0; margin-right:0"><code><span style="color:#8e908c">//导出到数据源配置</span>
     DBConfigBuilder dbConfigBuilder <span>=</span> <span style="color:#e96900">new</span> <span>DBConfigBuilder</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
     dbConfigBuilder
             <span style="color:#525252">.</span><span style="color:#e96900">setSqlFilepath</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"sql-dbtran.xml"</span><span style="color:#525252">)</span><span style="color:#8e908c">//指定sql配置文件地址</span>
             <span style="color:#525252">.</span><span style="color:#e96900">setTargetDbName</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"test"</span><span style="color:#525252">)</span><span style="color:#525252">;</span><span style="color:#8e908c">//指定目标数据库，在application.properties文件中配置</span>

     importBuilder<span style="color:#525252">.</span><span style="color:#e96900">setOutputDBConfig</span><span style="color:#525252">(</span>dbConfigBuilder<span style="color:#525252">.</span><span style="color:#e96900">buildDBImportConfig</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
     importBuilder<span style="color:#525252">.</span><span style="color:#e96900">addCallInterceptor</span><span style="color:#525252">(</span><span style="color:#e96900">new</span> <span>CallInterceptor</span><span style="color:#525252">(</span><span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
         <span style="color:#525252">@Override</span>
         <span style="color:#e96900">public</span> <span style="color:#e96900">void</span> <span style="color:#e96900">preCall</span><span style="color:#525252">(</span>TaskContext taskContext<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
             FileTaskContext fileTaskContext <span>=</span> <span style="color:#525252">(</span>FileTaskContext<span style="color:#525252">)</span>taskContext<span style="color:#525252">;</span>
             String filePath <span>=</span> fileTaskContext<span style="color:#525252">.</span><span style="color:#e96900">getFileInfo</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">.</span><span style="color:#e96900">getOriginFilePath</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
             <span style="color:#8e908c">/**
              * 根据文件名称指定插入数据库的sql语句
              */</span>
             <span style="color:#e96900">if</span><span style="color:#525252">(</span>filePath<span style="color:#525252">.</span><span style="color:#e96900">endsWith</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"metrics-report.log"</span><span style="color:#525252">)</span><span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
                 DBConfigBuilder dbConfigBuilder <span>=</span> <span style="color:#e96900">new</span> <span>DBConfigBuilder</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
                 dbConfigBuilder<span style="color:#525252">.</span><span style="color:#e96900">setInsertSqlName</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"insertSql"</span><span style="color:#525252">)</span><span style="color:#525252">;</span><span style="color:#8e908c">//指定新增的sql语句名称，在配置文件中配置：sql-dbtran.xml</span>

                 taskContext<span style="color:#525252">.</span><span style="color:#e96900">setDbmportConfig</span><span style="color:#525252">(</span>dbConfigBuilder<span style="color:#525252">.</span><span style="color:#e96900">buildDBImportConfig</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
             <span style="color:#525252">&#125;</span>
         <span style="color:#525252">&#125;</span>

         <span style="color:#525252">@Override</span>
         <span style="color:#e96900">public</span> <span style="color:#e96900">void</span> <span style="color:#e96900">afterCall</span><span style="color:#525252">(</span>TaskContext taskContext<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>

         <span style="color:#525252">&#125;</span>

         <span style="color:#525252">@Override</span>
         <span style="color:#e96900">public</span> <span style="color:#e96900">void</span> <span style="color:#e96900">throwException</span><span style="color:#525252">(</span>TaskContext taskContext<span style="color:#525252">,</span> Exception e<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>

         <span style="color:#525252">&#125;</span>
     <span style="color:#525252">&#125;</span><span style="color:#525252">)</span><span style="color:#525252">;</span></code></pre> </li> 
</ol> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><a href="https://gitee.com/bboss/filelog-elasticsearch/blob/v6.3.6/src/main/java/org/frameworkset/elasticsearch/imp/FileLog2CustomDemo.java" target="_blank">采集日志文件自定义处理案例</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo%3Fid%3Dbboss%25e6%2595%25b0%25e6%258d%25ae%25e9%2587%2587%25e9%259b%2586etl%25e6%25a1%2588%25e4%25be%258b%25e5%25a4%25a7%25e5%2585%25a8" target="_blank"><span style="color:#34495e">bboss数据采集ETL案例大全</span></a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo" target="_blank">https://esdoc.bbossgroups.com/#/bboss-datasyn-demo</a></p>
                                        </div>
                                      
</div>
            