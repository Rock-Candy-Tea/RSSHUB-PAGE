
---
title: '数据采集 ETL 工具 bboss-datatran v6.7.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9bc6507d06ae01c4e8420c5a221970a32d6.png'
author: 开源中国
comments: false
date: Mon, 18 Jul 2022 10:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9bc6507d06ae01c4e8420c5a221970a32d6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>数据采集 ETL 工具 bboss-datatran v6.7.0 发布</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fchangelog%3Fid%3Dv670-%25e5%258a%259f%25e8%2583%25bd%25e6%2594%25b9%25e8%25bf%259b" target="_blank"><span style="color:#34495e">v6.7.0 功能改进</span></a></h1> 
<ol> 
 <li>数据同步DB导出插件改进:支持为sql语句额外指定同步条件进行全量或者定时增量导入</li> 
</ol> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">定时按特定条件导入数据</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>importBuilder<span style="color:#525252">.</span><span style="color:#e96900">setSql</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"select * from batchtest1 where optime >= #[start_optime] and optime < #[end_optime]"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>

        importBuilder<span style="color:#525252">.</span><span style="color:#e96900">addParam</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"start_optime"</span><span style="color:#525252">,</span> TimeUtil<span style="color:#525252">.</span><span style="color:#e96900">parserDate</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"yyyy-MM-dd HH🇲🇲ss"</span><span style="color:#525252">,</span><span style="color:var(--theme-color,#42b983)">"2018-03-21 00:27:21"</span><span style="color:#525252">)</span><span style="color:#525252">)</span>
                <span style="color:#525252">.</span><span style="color:#e96900">addParam</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"end_optime"</span><span style="color:#525252">,</span>TimeUtil<span style="color:#525252">.</span><span style="color:#e96900">parserDate</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"yyyy-MM-dd HH🇲🇲ss"</span><span style="color:#525252">,</span><span style="color:var(--theme-color,#42b983)">"2019-12-30 00:27:21"</span><span style="color:#525252">)</span><span style="color:#525252">)</span><span style="color:#525252">;</span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">定时按特定条件增量导入数据</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>importBuilder<span style="color:#525252">.</span><span style="color:#e96900">setSql</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"select * from batchtest1 where optime >= #[start_optime] and optime < #[end_optime] and collecttime > #[collecttime]"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        importBuilder<span style="color:#525252">.</span><span style="color:#e96900">setLastValueColumn</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"collecttime"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        importBuilder<span style="color:#525252">.</span><span style="color:#e96900">setLastValueType</span><span style="color:#525252">(</span>ImportIncreamentConfig<span style="color:#525252">.</span>TIMESTAMP_TYPE<span style="color:#525252">)</span><span style="color:#525252">;</span>

        importBuilder<span style="color:#525252">.</span><span style="color:#e96900">addParam</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"start_optime"</span><span style="color:#525252">,</span> TimeUtil<span style="color:#525252">.</span><span style="color:#e96900">parserDate</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"yyyy-MM-dd HH🇲🇲ss"</span><span style="color:#525252">,</span><span style="color:var(--theme-color,#42b983)">"2018-03-21 00:27:21"</span><span style="color:#525252">)</span><span style="color:#525252">)</span>
                <span style="color:#525252">.</span><span style="color:#e96900">addParam</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"end_optime"</span><span style="color:#525252">,</span>TimeUtil<span style="color:#525252">.</span><span style="color:#e96900">parserDate</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"yyyy-MM-dd HH🇲🇲ss"</span><span style="color:#525252">,</span><span style="color:var(--theme-color,#42b983)">"2019-12-30 00:27:21"</span><span style="color:#525252">)</span><span style="color:#525252">)</span><span style="color:#525252">;</span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">使用参考文档：</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdb-es-datasyn" target="_blank">https://esdoc.bbossgroups.com/#/db-es-datasyn</a></p> 
<ol start="2"> 
 <li>数据同步改进：完善作业监控输出日志信息，改造es 数据采集dsl扩展参数管理机制，其他插件亦可以使用这些扩展参数</li> 
 <li>数据同步架构重构：去掉所有源到目标builder，统一使用“ImportBuilder构建器+InputConfig+OutputConfig“来构建数据同步作业</li> 
</ol> 
<p>    <img alt height="693" src="https://oscimg.oschina.net/oscnet/up-9bc6507d06ae01c4e8420c5a221970a32d6.png" width="1474" referrerpolicy="no-referrer"></p> 
<ol start="2"> 
 <li>数据同步改进：一次性作业支持延时时间配置和开始时间配置</li> 
 <li>数据同步改进：jdk timer作业支持设置作业运行截止时间，截止时间对quartz和xxl-job调度作业不起作用,对kafka作业、文件采集探针不起作用</li> 
 <li>数据同步改进：增加http输入和输出插件，使用参考文档：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fdatatran-http" target="_blank">https://esdoc.bbossgroups.com/#/datatran-http</a></li> 
 <li>增加数据同步作业开发gradle模板工程<span> </span><a href="https://gitee.com/bboss/bboss-datatran-demo" target="_blank">https://gitee.com/bboss/bboss-datatran-demo</a></li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>bboss 案例大全</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fbboss-datasyn-demo" target="_blank">https://esdoc.bbossgroups.com/#/bboss-datasyn-demo</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Quick Start</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fquickstart" target="_blank">https://esdoc.bbossgroups.com/#/quickstart</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>开发交流</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bbossgroups.com%2Fforum.html" target="_blank">https://www.bbossgroups.com/forum.html</a></p> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p> </p>
                                        </div>
                                      
</div>
            