
---
title: 'OpenMLDB Weekly Update：提升性能稳定性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bb5c72664a7ff038056a0218e498181a854.png'
author: 开源中国
comments: false
date: Fri, 10 Sep 2021 14:10:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bb5c72664a7ff038056a0218e498181a854.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p><strong>Summary</strong></p> 
 <p>本周合并 Pull requests 18个，新增Pull requests 9个，关闭 Issues 10个，新增 Issues 26个。总计94个文件修改，新增1502行代码，删除7764行代码。发布Release版本v0.2.3。了解<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourl.cn%2FTPhQcf" target="_blank">OpenMLDB</a></p> 
 <p><img alt height="462" src="https://oscimg.oschina.net/oscnet/up-bb5c72664a7ff038056a0218e498181a854.png" width="900" referrerpolicy="no-referrer"></p> 
 <p><strong>Merged Pull Requests</strong></p> 
 <ul> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F305" target="_blank">docs: add the demo link in readme</a>#305 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F364" target="_blank">docs: add a new logo</a>#364 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F327" target="_blank">refactor: refact AppendEntries in log replicator</a>#327 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F341" target="_blank">fix: sql and ns client desc result</a>#341 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F346" target="_blank">docs: add compile doc</a>#346 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F355" target="_blank">docs: new shilds</a>#355 merged </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F348" target="_blank">docs: added new shields</a>#348 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F328" target="_blank">fix: importer fix and doc</a>#328 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F307" target="_blank">build(deps): bump hive-exec from 3.0.0 to 3.1.1 in /java/openmldb-import</a>#307 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F299" target="_blank">update the blog link</a>#299 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F343" target="_blank">refactor: remove unused scripts</a>#343 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F344" target="_blank">fix: revert spark and hadoop version</a>#344 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F308" target="_blank">build(deps-dev): bump junit from 4.11 to 4.13.1 in /java/openmldb-import</a>#308 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F332" target="_blank">feat: update spark and hadoop version</a>#332 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F310" target="_blank">feat: update openmldb version</a>#310 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F326" target="_blank">feat: add offline update for changelog</a>#326 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F325" target="_blank">build(hybridse): prepare version to 0.2.3</a>#325 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F246" target="_blank">feat: build nearline tablet framework</a>#246 </li> 
 </ul> 
 <p><strong>Open Pull Requests</strong></p> 
 <ul> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F347" target="_blank">feat: add java common lib</a>#347 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F349" target="_blank">feat: support column query with the same name in window skew optimization</a>#349</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F350" target="_blank">feat: enhance plan optimization for group and filter</a>#350 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F359" target="_blank">feat: add batchjob module</a>#359 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F361" target="_blank">feat: add task manager module</a>#361 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F366" target="_blank">ci: openmldb java deploy workflow</a>#366 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F367" target="_blank">feat: add openmldb jmh</a>#367 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F368" target="_blank">test: modify test case</a>#368 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F370" target="_blank">update readme_add ai pipeline</a>#370 </li> 
 </ul> 
 <p><strong>Close Issues</strong></p> 
 <ul> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F363" target="_blank">docs: Add a new OpenMLDB logo</a>#363 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F331" target="_blank">bug: sql client `desc` result</a>#331 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F345" target="_blank">Add compile doc</a>#345 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F298" target="_blank">在readme里添加知乎、oschina等媒体链接</a>#298 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F202" target="_blank">Support reading and write tables in hive metastore catalog</a>#202 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F337" target="_blank">Remove unused scripts</a>#337 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F333" target="_blank">Update Spark version to 3.1.2</a>#333 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F122" target="_blank">TestWindowUnion failed: 20 did not equal 10 (TestWindowUnion.scala:58)</a>#122 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F324" target="_blank">Update the verison of openmldb-jdbc, openmldb-native and openmldb-import before auto release</a>#324 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F218" target="_blank">Build NearLineTablet framework</a>#218 </li> 
 </ul> 
 <p><strong>Open Issues</strong></p> 
 <ul> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F365" target="_blank">feat: support and validate query table with multiple-levels path</a>#365 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F362" target="_blank">feat: refactor of sql query router</a>#362 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F360" target="_blank">Add TaskManager service to submit OpenMLDB Batch jobs</a>#360 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F358" target="_blank">ut: so many unit test have memory leak, we should use sanitizer to check</a>#358 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F357" target="_blank">bug: cicd build failed but report ok</a>#357 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F356" target="_blank">Multiple columns with the same name can't execute when last join and over window</a>#356 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F354" target="_blank">bug: cicd python test</a>#354 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F353" target="_blank">bug: create index can't set ttl with no units</a>#353 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F352" target="_blank">Add OpenMLDB docs</a>#352 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F351" target="_blank">Add module for OpenMLDB Batch to run custom SQL and submit by TaskManager</a>#351 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F342" target="_blank">Add java common lib</a>#342 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F340" target="_blank">Replace `rtidb` to `openmldb` in some files</a>#340 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F339" target="_blank">Enable the unit test of TestWindowUnion</a>#339 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F338" target="_blank">Test and register the iceberg tables without using default Spark catalog</a>#338 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F336" target="_blank">Enable UnsafeRowOpt by default and resolve the related issues</a>#336 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F335" target="_blank">Enable WindowSkewOpt by default and resolve the running issues</a>#335 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F334" target="_blank">Add the unit test for physical nodes like GroupByAgg for offline</a>#334 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F330" target="_blank">Add deployment script</a>#330 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F329" target="_blank">Reduce the size of docker image</a>#329 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F323" target="_blank">Automatic packaging openmldb-import after tag creation</a>#323 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F322" target="_blank">Add `exit` command for sql_client</a>#322 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F321" target="_blank">Not able to find out SQL syntax docs from readme.</a>#321 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F318" target="_blank">feat: support distributed query on BatchMode under some restrictions</a>#318 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F317" target="_blank">feat: engine plan optimization for where and group with the same partition</a>#317 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F316" target="_blank">feat: support integration test for java/python sdk and offline batch</a>#316 </li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F315" target="_blank">enable python style check via pylint</a>#315 </li> 
 </ul> 
 <p><strong>Contributors</strong></p> 
 <ul> 
  <li>aceforeverd(<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ateapot%40aceforeverd.com" target="_blank">teapot@aceforeverd.com</a>)</li> 
  <li>dependabot[bot](49699333+dependabot[bot]@<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fusers.noreply.github.com" target="_blank">http://users.noreply.github.com</a>)</li> 
  <li>dl239(<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Adl239%40126.com" target="_blank">dl239@126.com</a>)</li> 
  <li>HuangWei(<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ahuangwei%40apache.org" target="_blank">huangwei@apache.org</a>)</li> 
  <li>imotai(<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Acodego.me%40gmail.com" target="_blank">codego.me@gmail.com</a>)</li> 
  <li>Lucifer(<a href="https://www.oschina.net/action/GoToLink?url=mailto%3A63491234%2Bashish-patwal%40users.noreply.github.com" target="_blank">63491234+ashish-patwal@users.noreply.github.com</a>)</li> 
  <li>luyuxiao211(<a href="https://www.oschina.net/action/GoToLink?url=mailto%3A79981940%2Bluyuxiao211%40users.noreply.github.com" target="_blank">79981940+luyuxiao211@users.noreply.github.com</a>)</li> 
  <li>Rohan Sharma(<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Arhnsharma5113%40gmail.com" target="_blank">rhnsharma5113@gmail.com</a>)</li> 
  <li>tobe(<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Atobeg3oogle%40gmail.com" target="_blank">tobeg3oogle@gmail.com</a>)</li> 
  <li>Wang ZeKai(<a href="https://www.oschina.net/action/GoToLink?url=mailto%3A1290561498%40qq.com" target="_blank">1290561498@qq.com</a>)</li> 
  <li>wuyou10206(<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Azw1020688%40163.com" target="_blank">zw1020688@163.com</a>)</li> 
  <li>xuman2019(<a href="https://www.oschina.net/action/GoToLink?url=mailto%3A52193163%2Bxuman2019%40users.noreply.github.com" target="_blank">52193163+xuman2019@users.noreply.github.com</a>)</li> 
 </ul> 
 <p><strong>Highlights</strong></p> 
 <p>本周发布Release v0.2.3版本，在功能特性、性能稳定性上都在稳步提升。在线存储引擎数据导入工具支持批量导出（Bulk load），在线计算引擎批处理模式（Batch mode）支持带参数的SQL查询，离线存储引擎支持数仓元数据服务（Hive metastore）以及数据湖存储格式（Apache Iceberg），数据分析能力支持Trino计算集群，离线计算引擎支持全局排序节点（SortByNode）。修复大量性能和功能相关的Bug，如端到端离线计算引擎测试时使用相同SQL导致的错误，在线存储引擎添加索引使用desc来展示TTL值有误等等。SQL语法也有拓展支持nvl、nvl2等函数，支持”&”、“|”、“^”、“~“等位操作函数，支持Between谓词逻辑等。详细Release日志请参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Freleases%2Ftag%2Fv0.2.3" target="_blank">Release OpenMLDB v0.2.3 · 4paradigm/OpenMLDB</a> 。</p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourl.cn%2FTPhQcf" target="_blank">OpenMLDB</a>整体架构也在升级重构中，全新的近实时存储服务Nearline Tablet和批处理任务管理服务TaskManager也在初步设计和实现中，新增模块在OpenMLDB的易用性和可拓展性上有进一步增强，相信在不久的v0.3.0正式版中可以与开发者见面。</p> 
 <p>欢迎更多开发者关注和参与<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourl.cn%2FTPhQcf" target="_blank">OpenMLDB</a>开源项目。</p> 
</div>
                                        </div>
                                      
</div>
            