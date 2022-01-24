
---
title: '数据采集 ETL 工具 Elasticsearch-datatran v6.5.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6a76b2f36cfa35d9bd8f617abc3636b7ee8.png'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 12:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6a76b2f36cfa35d9bd8f617abc3636b7ee8.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据采集ETL工具 Elasticsearch-datatran v6.5.0 发布<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-tool" target="_blank">Elasticsearch-datatran</a> 由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FREADME" target="_blank">bboss </a>开源的数据采集同步ETL工具，提供数据采集、数据清洗转换处理和数据入库功能。支持在Elasticsearch、关系数据库(mysql,oracle,db2,sqlserver、达梦等)、Mongodb、HBase、Hive、Kafka、文本文件、SFTP/FTP多种数据源之间进行海量数据采集同步；支持本地/ftp日志文件实时增量采集</span>到kafka/elasticsearch/database；支持根据字段进行数据记录切割；支持根据文件路径信息将不同文件数据写入不同的数据库表<span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#34495e">提供自定义处理采集数据功能，可以按照自己的要求将采集的数据</span><span style="background-color:#ffffff; color:#34495e">处理到目的地，支持数据来源包括：database，elasticsearch，kafka，mongodb，hbase，file，ftp等，想把采集的数据保存到什么地方，由自己实现CustomOutPut接口处理即可。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Elasticsearch版本兼容性：支持</strong>各种Elasticsearch版本（1.x,2.x,5.x,6.x,7.x,+）之间相互数据迁移</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="736" src="https://oscimg.oschina.net/oscnet/up-6a76b2f36cfa35d9bd8f617abc3636b7ee8.png" width="1232" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fchangelog%3Fid%3D%25e5%25af%25bc%25e5%2585%25a5bboss" target="_blank"><span style="color:#34495e">导入bboss</span></a></h1> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">一般项目导入下面的maven坐标即可：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.bbossgroups.plugins<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>bboss-elasticsearch-rest-jdbc<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>6.5.0<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">如果是spring boot项目还需要导入下面的maven坐标：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.bbossgroups.plugins<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>bboss-elasticsearch-spring-boot-starter<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
            <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>6.5.0<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span></code></pre> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fchangelog%3Fid%3Dv650-%25e5%258a%259f%25e8%2583%25bd%25e6%2594%25b9%25e8%25bf%259b" target="_blank"><span style="color:#34495e">v6.5.0 功能改进</span></a></h1> 
<ol> 
 <li> <p style="margin-left:0; margin-right:0">filelog插件添加子目录/ftp子目录/sftp子目录下日志文件采集功能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">对filelog插件文件选择过滤器FileFilter接口方法accept进行了重构，增加目录和文件区分标识对象FilterFileInfo，以适配本地目录、ftp和sftp三种场景，调整如下</p> <p style="margin-left:0; margin-right:0">重构前</p> </li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code> <span style="color:#e96900">public</span> <span style="color:#e96900">boolean</span> <span style="color:#e96900">accept</span><span style="color:#525252">(</span>String parentDir<span style="color:#525252">,</span>String fileName<span style="color:#525252">,</span> FileConfig fileConfig<span style="color:#525252">)</span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">重构后</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code> <span style="color:#e96900">public</span> <span style="color:#e96900">boolean</span> <span style="color:#e96900">accept</span><span style="color:#525252">(</span>FilterFileInfo filterFileInfo<span style="color:#525252">,</span> <span style="color:#8e908c">//包含Ftp文件名称，文件父路径、是否为目录标识</span>
                                            FileConfig fileConfig<span style="color:#525252">)</span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">使用案例</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>fileConfit<span style="color:#525252">.</span><span style="color:#e96900">setFileFilter</span><span style="color:#525252">(</span><span style="color:#e96900">new</span> <span>FileFilter</span><span style="color:#525252">(</span><span style="color:#525252">)</span> <span style="color:#525252">&#123;</span><span style="color:#8e908c">//指定ftp文件筛选规则</span>
                           <span style="color:#525252">@Override</span>
                           <span style="color:#e96900">public</span> <span style="color:#e96900">boolean</span> <span style="color:#e96900">accept</span><span style="color:#525252">(</span>FilterFileInfo filterFileInfo<span style="color:#525252">,</span> <span style="color:#8e908c">//包含Ftp文件名称，文件父路径、是否为目录标识</span>
                                            FileConfig fileConfig<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
                              <span style="color:#e96900">if</span><span style="color:#525252">(</span>filterFileInfo<span style="color:#525252">.</span><span style="color:#e96900">isDirectory</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">)</span><span style="color:#8e908c">//由于要采集子目录下的文件，所以如果是目录则直接返回true，当然也可以根据目录名称决定哪些子目录要采集</span>
                                 <span style="color:#e96900">return</span> <span style="color:#c76b29">true</span><span style="color:#525252">;</span>
                              String name <span>=</span> filterFileInfo<span style="color:#525252">.</span><span style="color:#e96900">getFileName</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
                              <span style="color:#8e908c">//判断是否采集文件数据，返回true标识采集，false 不采集</span>
                              <span style="color:#e96900">boolean</span> nameMatch <span>=</span> name<span style="color:#525252">.</span><span style="color:#e96900">startsWith</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"731_tmrt_user_login_day_"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
                              <span style="color:#e96900">if</span><span style="color:#525252">(</span>nameMatch<span style="color:#525252">)</span><span style="color:#525252">&#123;</span>
                                 String day <span>=</span> name<span style="color:#525252">.</span><span style="color:#e96900">substring</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"731_tmrt_user_login_day_"</span><span style="color:#525252">.</span><span style="color:#e96900">length</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
                                 SimpleDateFormat format <span>=</span> <span style="color:#e96900">new</span> <span>SimpleDateFormat</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"yyyyMMdd"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
                                 <span style="color:#e96900">try</span> <span style="color:#525252">&#123;</span>
                                    Date fileDate <span>=</span> format<span style="color:#525252">.</span><span style="color:#e96900">parse</span><span style="color:#525252">(</span>day<span style="color:#525252">)</span><span style="color:#525252">;</span>
                                    <span style="color:#e96900">if</span><span style="color:#525252">(</span>fileDate<span style="color:#525252">.</span><span style="color:#e96900">after</span><span style="color:#525252">(</span>startDate<span style="color:#525252">)</span><span style="color:#525252">)</span><span style="color:#8e908c">//下载和采集2020年12月11日以后的数据文件</span>
                                       <span style="color:#e96900">return</span> <span style="color:#c76b29">true</span><span style="color:#525252">;</span>
                                 <span style="color:#525252">&#125;</span> <span style="color:#e96900">catch</span> <span style="color:#525252">(</span><span>ParseException</span> e<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
                                    logger<span style="color:#525252">.</span><span style="color:#e96900">error</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">""</span><span style="color:#525252">,</span>e<span style="color:#525252">)</span><span style="color:#525252">;</span>
                                 <span style="color:#525252">&#125;</span>


                              <span style="color:#525252">&#125;</span>
                              <span style="color:#e96900">return</span> <span style="color:#c76b29">false</span><span style="color:#525252">;</span>
                           <span style="color:#525252">&#125;</span>
                        <span style="color:#525252">&#125;</span><span style="color:#525252">)</span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><strong style="color:#2c3e50">因此升级到6.5.0时需要对采集作业的FileFilter接口方法accept进行相应调整</strong></p> 
<ol start="3"> 
 <li>db管理dsl mysql无法创建加载dsl问题处理</li> 
 <li>log4j2版本升级2.17.1、slfj版本升级1.7.32</li> 
 <li>修复空行处理器Record问题：关闭key大写机制后，根据字段名称获取数据失效</li> 
 <li>忽略mysql stream机制情况下获取rowid失败异常</li> 
 <li>增加excel csv文件采集案例</li> 
</ol> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbbossgroups%2Fcsv-dbhandle" target="_blank">https://github.com/bbossgroups/csv-dbhandle</a></p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><a href="https://gitee.com/bboss/csv-dbhandle" target="_blank">https://gitee.com/bboss/csv-dbhandle</a></p> 
<ol start="8"> 
 <li> <p style="margin-left:0; margin-right:0">优化运行容器工具，增加从环境变量、jvm属性配置检索mainclass功能</p> <p style="margin-left:0; margin-right:0">默认使用org.frameworkset.elasticsearch.imp.DB2CSVFile作为作业主程序，</p> <p style="margin-left:0; margin-right:0">如果设置了环境变量mainclassevn，则使用mainclassevn作为作业主程序</p> <p style="margin-left:0; margin-right:0">环境变量名称不能和属性名称一致，否则报循环引用异常，并将原始值返回</p> <p style="margin-left:0; margin-right:0">mainclass=#[mainclassevn:org.frameworkset.elasticsearch.imp.DB2CSVFile]</p> </li> 
</ol> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">使用参考文档：</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><a href="https://my.oschina.net/bboss/blog/469411" target="_blank">https://my.oschina.net/bboss/blog/469411</a></p> 
<ol start="9"> 
 <li> <p style="margin-left:0; margin-right:0">升级mysql驱动版本号为8.0.28</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">增加通用异步批处理组件</p> </li> 
</ol> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">使用案例：</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><a href="https://gitee.com/bboss/eshelloword-booter/blob/master/src/test/java/org/bboss/elasticsearchtest/bulkprocessor/PersistentBulkProcessor.java" target="_blank">https://gitee.com/bboss/eshelloword-booter/blob/master/src/test/java/org/bboss/elasticsearchtest/bulkprocessor/PersistentBulkProcessor.java</a></p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">使用文档</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2FbulkProcessor-common" target="_blank">https://esdoc.bbossgroups.com/#/bulkProcessor-common</a></p>
                                        </div>
                                      
</div>
            