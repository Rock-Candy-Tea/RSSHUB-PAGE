
---
title: 'OpenMLDB Weekly：修复集成测试中 SQL 优化过程重复优化子节点的问题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic2.zhimg.com/80/v2-1be9d2f10111161f279f400c548c6f71_1440w.jpg'
author: 开源中国
comments: false
date: Fri, 08 Oct 2021 04:16:00 GMT
thumbnail: 'https://pic2.zhimg.com/80/v2-1be9d2f10111161f279f400c548c6f71_1440w.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourl.cn%2Frf5R6R" target="_blank">OpenMLDB</a></h2> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Summary</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本周合并 Pull requests 5个，新增Pull requests 6个，关闭 Issues 1个，新增 Issues 5个。总计150个文件修改，新增531行代码，删除432行代码。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://pic2.zhimg.com/80/v2-1be9d2f10111161f279f400c548c6f71_1440w.jpg" width="1890" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Merged Pull Requests</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F453" target="_blank">fix: remove dup apply pass on the same physical op</a>#453 merged 5 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F482" target="_blank">feat: revert hadoop common version to 2.7.1 for batch</a>#482 merged 6 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F481" target="_blank">feat: add taskmanager as java submodule</a>#481 merged 6 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F470" target="_blank">style: update hybridse header guard style</a>#470 merged 6 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F479" target="_blank">fix: fix bug in integration-test-src</a>#479 merged 7 days ago<span> </span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Open Pull Requests</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F480" target="_blank">fix: create index parse and desc</a>#480 opened 7 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F483" target="_blank">feat: java sdk add api getTableSchema</a>#483 opened 7 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F486" target="_blank">feat: rm zk dependency in standalone mode</a>#486 opened 6 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F489" target="_blank">fix: fix concat join fail</a>#489 opened 6 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F490" target="_blank">fix: fix can't use broadcast join when open window skew optimization</a>#490 opened 5 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fpull%2F491" target="_blank">feat: support plan explain</a>#491 opened 5 days ago</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Close Issues</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F437" target="_blank">Bug: fail to compile and run some SQL statements with OpenMLDB-batch when enable batch_window_parallelization</a>#437 closed 5 days ago<span> </span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Open Issues</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F488" target="_blank">Feat: Support explain for dataframe in openmldb-batch</a>#488 opened 6 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F487" target="_blank">Bug: Can't use broadcast join automatically when genAddColumnsDf</a>#487 opened 6 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F485" target="_blank">Bug: Cannot resolve column name "__CONCATJOIN_INDEX__"</a>#485 opened 6 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F484" target="_blank">Bug: Failed to merge incompatible data types string and int</a>#484 opened 6 days ago</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2F4paradigm%2FOpenMLDB%2Fissues%2F478" target="_blank">`create table` and `create index` should use the same logic to avoid more mistakes.</a>#478 opened 7 days ago<span> </span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Contributors</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Chen22 (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ajingchen2222%40gmail.com" target="_blank">jingchen2222@gmail.com</a>)</li> 
 <li>HuangWei (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ahuangwei%40apache.org" target="_blank">huangwei@apache.org</a>)</li> 
 <li>Kanekanekane (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3A1290561498%40qq.com" target="_blank">1290561498@qq.com</a>)</li> 
 <li>tobe (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Atobeg3oogle%40gmail.com" target="_blank">tobeg3oogle@gmail.com</a>)</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Highlights</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本周恰逢中国国庆节，预祝大家国庆快乐，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourl.cn%2Frf5R6R" target="_blank">OpenMLDB</a>相关的代码修改和Pull-request比同期较少，但仍有重要的bugfix。包括OpenMLDB Batch模块现在可以同时开启窗口并行优化和窗口倾斜优化，同时修复集成测试中发现的SQL优化过程重复优化子节点的情况。本周新增外部开发者参与，在Gitee悬赏Issue中修复了C++ header style重构问题，更多悬赏任务请参考<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fpin%2F1417945812144390144" target="_blank">【 悬赏】第四范式悬赏计划第一期来啦…</a><span> </span>。<span> </span></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">欢迎更多开发者关注和参与<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourl.cn%2Frf5R6R" target="_blank">OpenMLDB</a>开源项目。</p>
                                        </div>
                                      
</div>
            