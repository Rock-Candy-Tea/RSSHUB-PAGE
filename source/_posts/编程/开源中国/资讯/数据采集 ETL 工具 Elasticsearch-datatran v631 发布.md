
---
title: '数据采集 ETL 工具 Elasticsearch-datatran v6.3.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a4de01eaf0de04d13c4de23c9e4f61f6791.png'
author: 开源中国
comments: false
date: Mon, 02 Aug 2021 07:35:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a4de01eaf0de04d13c4de23c9e4f61f6791.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">数据采集ETL工具 Elasticsearch-datatran v6.3.1 发布，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">Elasticsearch-datatran</a> 由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FREADME" target="_blank">bboss </a>开源的数据采集同步ETL工具，提供数据采集、数据处理清洗和数据入库功能。支持在Elasticsearch、关系数据库(mysql,oracle,db2,sqlserver、达梦等)、Mongodb、HBase、Hive、Kafka、文本文件、SFTP/FTP多种数据源之间进行海量数据同步；支持日志文件实时增量采集</span>到kafka/elasticsearch/database<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="text-align:left"><strong>Elasticsearch版本兼容性：支持</strong>各种Elasticsearch版本（1.x,2.x,5.x,6.x,7.x,+）之间相互数据迁移</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-a4de01eaf0de04d13c4de23c9e4f61f6791.png" referrerpolicy="no-referrer"></p> 
<h1><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fchangelog%3Fid%3Dv630-%25e5%258a%259f%25e8%2583%25bd%25e6%2594%25b9%25e8%25bf%259b" target="_blank"><span style="color:#34495e">6.3.1 功能改进</span></a></h1> 
<ol> 
 <li> <p>日志采集探针，属性maxBytes为0或者负数时忽略记录长度截取</p> </li> 
 <li> <p>日志采集探针，增加忽略条件匹配类型文件记录包含与排除条件匹配类型： REGEX_MATCH,REGEX_CONTAIN,STRING_CONTAIN, STRING_EQUALS,STRING_PREFIX,STRING_END; 使用案例：</p> </li> 
</ol> 
<pre><code>               config<span style="color:#525252">.</span><span style="color:#e96900">addConfig</span><span style="color:#525252">(</span><span style="color:#e96900">new</span> FileConfig<span style="color:#525252">(</span>logPath<span style="color:#525252">,</span><span style="color:#8e908c">//指定目录</span>
                             fileName+<span style="color:var(--theme-color,#42b983)">".log"</span><span style="color:#525252">,</span><span style="color:#8e908c">//指定文件名称，可以是正则表达式</span>
                             startLabel<span style="color:#525252">)</span><span style="color:#8e908c">//指定多行记录的开头识别标记，正则表达式</span>
                             <span style="color:#525252">.</span><span style="color:#e96900">setCloseEOF</span><span style="color:#525252">(</span><span style="color:#c76b29">false</span><span style="color:#525252">)</span><span style="color:#8e908c">//已经结束的文件内容采集完毕后关闭文件对应的采集通道，后续不再监听对应文件的内容变化</span>
                             <span style="color:#525252">.</span><span style="color:#e96900">addField</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"tag"</span><span style="color:#525252">,</span>fileName<span style="color:#525252">.</span><span style="color:#e96900">toLowerCase</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">)</span><span style="color:#8e908c">//添加字段tag到记录中</span>
                             <span style="color:#525252">.</span><span style="color:#e96900">setEnableInode</span><span style="color:#525252">(</span><span style="color:#c76b29">true</span><span style="color:#525252">)</span>
                             <span style="color:#525252">.</span><span style="color:#e96900">setIncludeLines</span><span style="color:#525252">(</span>levelArr<span style="color:#525252">,</span> LineMatchType<span style="color:#525252">.</span>STRING_CONTAIN<span style="color:#525252">)</span></code></pre> 
<p>3.默认采用异步机制保存增量同步数据状态，大幅提升数据同步效率，降低同步功耗，可以通过以下机制关闭异步机制：</p> 
<p>importBuilder.setAsynFlushStatus(false);</p> 
<h1><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo%3Fid%3Dbboss%25e6%2595%25b0%25e6%258d%25ae%25e9%2587%2587%25e9%259b%2586etl%25e6%25a1%2588%25e4%25be%258b%25e5%25a4%25a7%25e5%2585%25a8" target="_blank"><span style="color:#34495e">bboss数据采集ETL案例大全</span></a></h1> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo" target="_blank">https://esdoc.bbossgroups.com/#/bboss-datasyn-demo</a></p>
                                        </div>
                                      
</div>
            