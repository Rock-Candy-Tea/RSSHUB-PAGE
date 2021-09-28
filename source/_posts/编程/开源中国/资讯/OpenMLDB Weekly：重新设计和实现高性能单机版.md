
---
title: 'OpenMLDB Weekly：重新设计和实现高性能单机版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic4.zhimg.com/80/v2-35bd89bd891c0f2104ec4f8ff6189727_1440w.jpg'
author: 开源中国
comments: false
date: Tue, 28 Sep 2021 08:07:00 GMT
thumbnail: 'https://pic4.zhimg.com/80/v2-35bd89bd891c0f2104ec4f8ff6189727_1440w.jpg'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourl.cn%2FzrncAA" target="_blank">OpenMLDB</a></h2> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Summary</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本周合并 Pull requests 8个，新增Pull requests 5个，关闭 Issues 11个，新增 Issues 20个。总计84个文件修改，新增6677行代码，删除511行代码。<span> </span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://pic4.zhimg.com/80/v2-35bd89bd891c0f2104ec4f8ff6189727_1440w.jpg" width="947" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Merged Pull Requests</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F466" target="_blank">feat: support spark.master config to run job in yarn or local</a>#466<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F464" target="_blank">feat: read openmldb git properties and set in return string</a>#464</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F467" target="_blank">feat: enable `TestWindowUnion` test</a>#467</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F416" target="_blank">feat: bump snakeyaml from 1.17 to 1.26 in /test/batch-test/openmldb-batch-test</a>#416<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F367" target="_blank">feat: add openmldb jmh</a>#367<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F465" target="_blank">test: modify cicd</a>#465<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F452" target="_blank">feat: add src test cicd</a>#452<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F438" target="_blank">fix: fix a bug when turn on window parallelization and skew optimization</a>#438<span> </span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Open Pull Requests</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F439" target="_blank">Fix import error of OpenMLDB Python lib when installed as zip format</a>#439<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F453" target="_blank">fix: remove dup apply pass on the same physical op.</a>#453<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F457" target="_blank">feat: ddlparser extracts indexes from sql</a>#457<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F469" target="_blank">build: add deployment script</a>#469<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F470" target="_blank">style: update hybridse header guard style</a>#470<span> </span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Close Issues</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F456" target="_blank">Support Spark local jobs in TaskManager for local OpenMLDB setup</a>#456<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F463" target="_blank">Return the openmldb version string for Batch</a>#463<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F339" target="_blank">Enable the unit test of TestWindowUnion</a>#339<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F162" target="_blank">创建索引，ttl_type=test，创建成功，期望返回错误信息</a>#162<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F84" target="_blank">Deploy all-in-one java package</a>#84<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F120" target="_blank">move demo to main repo</a>#120<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F163" target="_blank">创建absorlat类型的索引，desc展示不出来</a>#163<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F371" target="_blank">scripts: package java sdk set cmake type to release</a>#371<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F398" target="_blank">feat: support insert multiple rows into a table using a single SQL insert statement.</a>#398</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F444" target="_blank">Fix enable WindowSkewOpt and WindowComputeParallelOpt at the same time</a>#444<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F313" target="_blank">add more status badges to README</a>#313<span> </span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Open Issues</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F468" target="_blank">Support passing multiple databases for parsing each SQL statement</a>#468<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F462" target="_blank">Set index if there is no index info in create statement</a>#462<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F461" target="_blank">Update catalog in stand alone mode</a>#461<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F460" target="_blank">Add `SHOW DEPLOYMENT` and `DROP DEPLOYMENT` command</a>#460<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F459" target="_blank">Recover metadata when nameserver restart in stand alone mode</a>#459<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F458" target="_blank">Store metadata in system table</a>#458<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F455" target="_blank">Support `SELECT INTO OUTFILE` syntax</a>#455<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F454" target="_blank">ci: pre-build macos pkg needs to select sdk</a>#454<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F451" target="_blank">Support querying data from Trino in oenmldb CLI</a>#451<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F450" target="_blank">Add SHOW JOBS command for CLI and TaskManager</a>#450<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F449" target="_blank">Support generating and storing job id for TaskManager</a>#449<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F448" target="_blank">Integrate the ability of SQL analysis by trino in CLI</a>#448<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F447" target="_blank">Add `DEPLOY` command</a>#447<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F446" target="_blank">Write the result of select sql into file</a>#446<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F445" target="_blank">Support `SET` syntax</a>#445<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F443" target="_blank">Add `import` command</a>#443<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F442" target="_blank">Support `engine` option in `create` statement</a>#442<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F441" target="_blank">Use nameserver ip and port to connect openmldb</a>#441<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F440" target="_blank">Support stand-alone mode</a>#440<span> </span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F437" target="_blank">Fail query window+lastjoin when turn on `enable_batch_window_parallelization`</a>#437<span> </span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Contributors</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>aceforeverd (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ateapot%40aceforeverd.com" target="_blank">teapot@aceforeverd.com</a>)</li> 
 <li>Chen22 (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ajingchen2222%40gmail.com" target="_blank">jingchen2222@gmail.com</a>)</li> 
 <li>Kanekanekane (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3A1290561498%40qq.com" target="_blank">1290561498@qq.com</a>)</li> 
 <li>Stark (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ahujinlei1999%40qq.com" target="_blank">hujinlei1999@qq.com</a>)</li> 
 <li>tobe (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Atobeg3oogle%40gmail.com" target="_blank">tobeg3oogle@gmail.com</a>)</li> 
 <li>wuyou10206 (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Azw1020688%40163.com" target="_blank">zw1020688@163.com</a>)<span> </span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Highlights</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本周在特性开发、缺陷修复、性能测试、CICD集成方案都有进一步完善。功能上在TaskManager上支持了单机批处理模式，Bug方案修复Git版本信息展示、批模式同时运行窗口倾斜优化以及窗口并行优化的问题，性能测试方面集成了openmldb-jmh模块加强对Java模块的性能回归测试，CICD集成方面加入了基于源码分支的SRC测试和基于特定版本的PKG测试，包含数千个case的大规模集成测试也可以在Github中手动出发运行。本周新增Issue较多，侧重于高性能单机版的重新设计和实现，对高性能数据库优化感兴趣的也可以关注一下。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">欢迎更多开发者关注和参与<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourl.cn%2FzrncAA" target="_blank">OpenMLDB</a>开源项目。</p>
                                        </div>
                                      
</div>
            