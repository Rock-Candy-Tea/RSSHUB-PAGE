
---
title: 'OpenMLDB Weekly：增加 IntegrationTest 集成测试模块'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic3.zhimg.com/80/v2-7bcca076791aa8e24f5872b3453e341a_1440w.jpg'
author: 开源中国
comments: false
date: Wed, 22 Sep 2021 06:44:00 GMT
thumbnail: 'https://pic3.zhimg.com/80/v2-7bcca076791aa8e24f5872b3453e341a_1440w.jpg'
---

<div>   
<div class="content">
                                                                                            <div> 
 <h2 style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F4paradigm%2Fopenmldb" target="_blank">OpenMLDB</a></h2> 
 <h2 style="margin-left:0; margin-right:0; text-align:left">Summary</h2> 
 <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本周合并 Pull requests 12个，新增Pull requests 4个，关闭 Issues 6个，新增 Issues 18个。总计353个文件修改，新增36056行代码，删除879行代码。</p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://pic3.zhimg.com/80/v2-7bcca076791aa8e24f5872b3453e341a_1440w.jpg" width="1898" referrerpolicy="no-referrer"></p> 
 <h2 style="margin-left:0; margin-right:0; text-align:left">Merged Pull Requests</h2> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F434" target="_blank">feat: add integration test cicd</a>#434</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F386" target="_blank">feat: add batchjob as java submodules</a>#386</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F400" target="_blank">feat: add kubernetes java dependencies for taskmanager</a>#400</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F436" target="_blank">fix: fix count in some yaml cases</a>#436</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F424" target="_blank">feat: add a new optimization for expanding data in window skew optimization</a>#424</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F399" target="_blank">feat: support insert multiple rows into a table using a single SQL insert statement</a>#399</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F393" target="_blank">feat: support aggregation over the whole table</a>#393</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F366" target="_blank">ci: openmldb java deploy workflow</a>#366</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F415" target="_blank">test: rm DataSyncReplicaCluster test</a>#415</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F414" target="_blank">feat: reconfiguration window skew optimization</a>#414</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F395" target="_blank">feat: add integration test</a>#395</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F382" target="_blank">feat: bump junit from 4.11 to 4.13.1 in /java/openmldb-batchjob</a>#382</li> 
 </ul> 
 <h2 style="margin-left:0; margin-right:0; text-align:left">Open Pull Requests</h2> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F416" target="_blank">build(deps): bump snakeyaml from 1.17 to 1.26 in /test/batch-test/openmldb-batch-test</a>#416</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F417" target="_blank">build(deps): bump httpclient from 4.5.2 to 4.5.13 in /test/integration-test/openmldb-test-java/openmldb-test-common</a>#417</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F423" target="_blank">feat: support in predicate</a>#423</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F435" target="_blank">feat: reorganize error code and use check_status and check_true</a>#435</li> 
 </ul> 
 <h2 style="margin-left:0; margin-right:0; text-align:left">Close Issues</h2> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F385" target="_blank">Make openmldb-batchjob and openmldb-taskmanager as submodules of openmldb-parent</a>#385</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F375" target="_blank">Support submit and manage Kubernetes jobs for TaskManager</a>#375</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F391" target="_blank">Bug: SQL INSERT Statement with multi rows does not work as expected</a>#391</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F278" target="_blank">studio.4.2.0安装的rtidb启动coredump</a>#278</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F219" target="_blank">Support General aggegrate function over table `COUNT`, `MAX`, `MIN`, `SUM`</a>#219</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F316" target="_blank">feat: support integration test for java/python sdk and offline batch</a>#316</li> 
 </ul> 
 <h2 style="margin-left:0; margin-right:0; text-align:left">Open Issues</h2> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F433" target="_blank">Add feature extraction tools like detecting data skew</a>#433</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F432" target="_blank">feat: try run benchmark on GitHub workflow, compare & upload test results</a>#432</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F430" target="_blank">feat: refactor error/warning log in hybridse</a>#430</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F427" target="_blank">refactor yaml sql test case</a>#427</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F426" target="_blank">feat: improve cli and make the console output more clean and clear</a>#426</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F425" target="_blank">RFC: Redesign some interfaces of SQLClusterRouter</a>#425</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F422" target="_blank">Create memtable when creating procedure</a>#422</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F421" target="_blank">Sync metadata to hive metastore when creating iceberg table</a>#421</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F420" target="_blank">Load data from iceberg to memtable</a>#420</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F419" target="_blank">Get index from sql&procdure</a>#419</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F418" target="_blank">Create message table and sync data to nearline tablet</a>#418</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F413" target="_blank">Add optimization passes for native LastJoin</a>#413</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F412" target="_blank">Enable optimization fo window parallel computation by default</a>#412</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F411" target="_blank">Package OpenMLDB Spark distribution for release</a>#411</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F410" target="_blank">Support table aggregation functions for Batch mode</a>#410</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F409" target="_blank">Support passing Spark parameters for TaskManager</a>#409</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F408" target="_blank">Refine the parameters from TaskManager API to support more job status</a>#408</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F407" target="_blank">Integrated TaskManager API with OpenMLDB CLI tool</a>#407</li> 
 </ul> 
 <h2 style="margin-left:0; margin-right:0; text-align:left">Contributors</h2> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>aceforeverd (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ateapot%40aceforeverd.com" target="_blank">teapot@aceforeverd.com</a>)</li> 
  <li>Chen22 (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ajingchen2222%40gmail.com" target="_blank">jingchen2222@gmail.com</a>)</li> 
  <li>dl239 (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Adl239%40126.com" target="_blank">dl239@126.com</a>)</li> 
  <li>Kanekanekane (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3A1290561498%40qq.com" target="_blank">1290561498@qq.com</a>)</li> 
  <li>Kanekanekane (kane@KanedeMacBook-Pro.local)</li> 
  <li>tobe (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Atobeg3oogle%40gmail.com" target="_blank">tobeg3oogle@gmail.com</a>)</li> 
  <li>Wang ZeKai (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3A1290561498%40qq.com" target="_blank">1290561498@qq.com</a>)</li> 
  <li>wuyou10206 (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Azw1020688%40163.com" target="_blank">zw1020688@163.com</a>)</li> 
 </ul> 
 <h2 style="margin-left:0; margin-right:0; text-align:left">Highlights</h2> 
 <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本周新增加了IntegrationTest集成测试模块，并集成到CICD流程，整体代码修改较多，主要是新增了大量SQL测试用例。TaskManager模块新增Kubernetes依赖，支持多种计算集群后端的任务管理。BatchJob模块加入Java项目子模块中，纳入完整的CICD集成流程。本周项目正式通过2021年信通院可信开源项目评审，并在代码上升级Hadoop-common依赖版本解决潜在风险问题，修复项目License依赖风险问题。</p> 
 <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">欢迎更多开发者关注和参与OpenMLDB开源项目。</p> 
</div>
                                        </div>
                                      
</div>
            