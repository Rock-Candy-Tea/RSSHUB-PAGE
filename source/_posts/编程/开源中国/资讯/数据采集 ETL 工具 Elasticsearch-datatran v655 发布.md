
---
title: '数据采集 ETL 工具 Elasticsearch-datatran v6.5.5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://esdoc.bbossgroups.com/images/datasyn.png'
author: 开源中国
comments: false
date: Wed, 06 Apr 2022 01:53:00 GMT
thumbnail: 'https://esdoc.bbossgroups.com/images/datasyn.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据采集 ETL 工具 Elasticsearch-datatran v6.5.5发布，</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fchangelog%3Fid%3Dv650-%25e5%258a%259f%25e8%2583%25bd%25e6%2594%25b9%25e8%25bf%259b" target="_blank"><span style="color:#34495e">v6.5.5 功能改进</span></a></h1> 
<ol> 
 <li> <p style="margin-left:0; margin-right:0">带来全新改版的bboss官网,欢迎大家体验：https://www.bbossgroups.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">数据同步机制优化：各插件tran逻辑复用优化</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">ftp/sftp文件下载锁优化，大幅提升文件采集插件性能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">增加ftp/sftp文件并行下载机制，通过setDownloadWorkThreads实现并行下载线程数，默认为3个，如果设置为0代表串行下载</p> <pre style="margin-left:0; margin-right:0"><code>FtpConfig ftpConfig <span>=</span> <span style="color:#e96900">new</span> <span>FtpConfig</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">.</span><span style="color:#e96900">setFtpIP</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"10.13.6.127"</span><span style="color:#525252">)</span><span style="color:#525252">.</span><span style="color:#e96900">setFtpPort</span><span style="color:#525252">(</span><span style="color:#c76b29">21</span><span style="color:#525252">)</span>
             <span style="color:#525252">.</span><span style="color:#e96900">setFtpUser</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"ecsftp"</span><span style="color:#525252">)</span><span style="color:#525252">.</span><span style="color:#e96900">setFtpPassword</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"ecsftp"</span><span style="color:#525252">)</span><span style="color:#525252">.</span><span style="color:#e96900">setDownloadWorkThreads</span><span style="color:#525252">(</span><span style="color:#c76b29">4</span><span style="color:#525252">)</span><span style="color:#8e908c">//设置4个线程并行下载文件，可以允许最多4个文件同时下载</span>
             <span style="color:#525252">.</span><span style="color:#e96900">setRemoteFileDir</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"xcm"</span><span style="color:#525252">)</span><span style="color:#525252">.</span><span style="color:#e96900">setRemoteFileValidate</span><span style="color:#525252">(</span><span style="color:#e96900">new</span> <span>RemoteFileValidate</span><span style="color:#525252">(</span><span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
                 <span style="color:#8e908c">/**
                  * 校验数据文件合法性和完整性接口

                  * @param validateContext 封装校验数据文件信息
                  *     dataFile 待校验零时数据文件，可以根据文件名称获取对应文件的md5签名文件名、数据量稽核文件名称等信息，
                  *     remoteFile 通过数据文件对应的ftp/sftp文件路径，计算对应的目录获取md5签名文件、数据量稽核文件所在的目录地址
                  *     ftpContext ftp配置上下文对象
                  *     然后通过remoteFileAction下载md5签名文件、数据量稽核文件，再对数据文件进行校验即可
                  *     redownload 标记校验来源是否是因校验失败重新下载文件导致的校验操作，true 为重下后 文件校验，false为第一次下载校验
                  * @return int
                  * 文件内容校验成功
                  *     RemoteFileValidate.FILE_VALIDATE_OK = 1;
                  *     校验失败不处理文件
                  *     RemoteFileValidate.FILE_VALIDATE_FAILED = 2;
                  *     文件内容校验失败并备份已下载文件
                  *     RemoteFileValidate.FILE_VALIDATE_FAILED_BACKUP = 3;
                  *     文件内容校验失败并删除已下载文件
                  *     RemoteFileValidate.FILE_VALIDATE_FAILED_DELETE = 5;
                  */</span>
                 <span style="color:#e96900">public</span> Result <span style="color:#e96900">validateFile</span><span style="color:#525252">(</span>ValidateContext validateContext<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
<span style="color:#8e908c">//                        if(redownload)</span>
<span style="color:#8e908c">//                            return Result.default_ok;</span>
<span style="color:#8e908c">////                        return Result.default_ok;</span>
<span style="color:#8e908c">//                        Result result = new Result();</span>
<span style="color:#8e908c">//                        result.setValidateResult(RemoteFileValidate.FILE_VALIDATE_FAILED_REDOWNLOAD);</span>
<span style="color:#8e908c">//                        result.setRedownloadCounts(3);</span>
<span style="color:#8e908c">//                        result.setMessage("MD5校验"+remoteFile+"失败，重试3次");//设置校验失败原因信息</span>
<span style="color:#8e908c">//                        //根据remoteFile的信息计算md5文件路径地址，并下载，下载务必后进行签名校验</span>
<span style="color:#8e908c">//                        //remoteFileAction.downloadFile("remoteFile.md5","dataFile.md5");</span>
<span style="color:#8e908c">//                        return result;</span>
                     <span style="color:#e96900">return</span> Result<span style="color:#525252">.</span>default_ok<span style="color:#525252">;</span>
                 <span style="color:#525252">&#125;</span>
             <span style="color:#525252">&#125;</span><span style="color:#525252">)</span></code></pre> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool%3Fid%3D_2317-%25e6%2595%25b0%25e6%258d%25ae%25e5%2590%258c%25e6%25ad%25a5%25e4%25bb%25bb%25e5%258a%25a1%25e6%2589%25a7%25e8%25a1%258c%25e7%25bb%259f%25e8%25ae%25a1%25e4%25bf%25a1%25e6%2581%25af%25e8%258e%25b7%25e5%258f%2596" target="_blank">完善数据同步作业任务监控指标统计信息</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">增加数据批量/串行同步写入<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo%3Fid%3D_11-%25e4%25bb%258esftp%25e6%259c%258d%25e5%258a%25a1%25e5%2599%25a8%25e9%2587%2587%25e9%259b%2586excel%25e6%2596%2587%25e4%25bb%25b6%25e5%2586%2599%25e5%2585%25a5redis%25e6%25a1%2588%25e4%25be%258b" target="_blank">redis案例</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">增加<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo%3Fid%3D_11-%25e4%25bb%258esftp%25e6%259c%258d%25e5%258a%25a1%25e5%2599%25a8%25e9%2587%2587%25e9%259b%2586excel%25e6%2596%2587%25e4%25bb%25b6%25e5%2586%2599%25e5%2585%25a5redis%25e6%25a1%2588%25e4%25be%258b" target="_blank">远程数据文件校验机制</a>，以实现对数据文件md5签名校验、记录数校验、校验失败重试下载（支持设置重试下载次数）等功能，</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">数据加工处理改进：Context 接口getValue方法支持获取解析后的日志文件记录字段值</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">对作业启动日志中的数据源口令进行脱敏处理</p> </li> 
</ol> 
<h1 style="margin-left:0px; margin-right:0px"><strong>Elasticsearch-datatran特色</strong></h1> 
<p><span style="background-color:#ffffff; color:#333333"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">Elasticsearch-datatran</a> 由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FREADME" target="_blank">bboss </a>开源的数据采集同步ETL工具，提供数据采集、数据清洗转换处理和数据入库功能。支持在Elasticsearch、关系数据库(mysql,oracle,db2,sqlserver、达梦等)、Mongodb、HBase、Hive、Kafka、文本文件、excel文件、SFTP/FTP多种数据源之间进行海量数据采集同步；支持数据实时增量采集</span>和全量采集；支持根据字段进行数据记录切割；支持多级文件路径信息将不同文件数据写入不同的数据库表<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#34495e">提供自定义处理采集数据功能，可以按照自己的要求将采集的数据</span><span style="background-color:#ffffff; color:#34495e">处理到目的地，如需定制化将数据保存到特定的地方，可自行实现CustomOutPut接口处理即可。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">Elasticsearch-datatran</a> 的独特之处，其数据同步作业采用java语言开发，小巧而精致，可以用采用java提供的所有功能和现有组件框架，随心所欲地处理和加工海量存量数据、实时增量数据；可以根据数据规模及同步性能要求，按需配置和调整数据采集同步作业所需内存、工作线程、线程队列大小；可以将作业独立运行，亦可以将作业嵌入基于java开发的各种应用汇总运行；提供了作业任务监控api、作业启动和停止api，可轻松定制一款属于自己的ETL管理工具。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">如果您还在苦于logstash、flume、filebeat之类的开源工具无法满足复杂的、海量的数据处理加工场景，那么<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">Elasticsearch-datatran</a>将</span>是一个不错的选择。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Elasticsearch版本兼容性：支持</strong>各种Elasticsearch版本（1.x,2.x,5.x,6.x,7.x,8.x+）之间相互数据迁移</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="736" src="https://esdoc.bbossgroups.com/images/datasyn.png" width="1274" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">功能完备的文件数据采集插件：支持从ftp/sftp并行下载各种文件，并行采集和处理各种文件数据</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><img src="https://esdoc.bbossgroups.com/images/filelog-es.jpg" referrerpolicy="no-referrer"></h1> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fchangelog%3Fid%3D%25e5%25af%25bc%25e5%2585%25a5bboss" target="_blank"><span style="color:#34495e">导入bboss</span></a></h1> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">一般项目导入下面的maven坐标即可：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>com.bbossgroups.plugins<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>bboss-elasticsearch-rest-jdbc<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>6.5.5<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">如果是spring boot项目还需要导入下面的maven坐标：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>com.bbossgroups.plugins<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>bboss-elasticsearch-spring-boot-starter<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>6.5.5<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#525252"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></code></pre>
                                        </div>
                                      
</div>
            