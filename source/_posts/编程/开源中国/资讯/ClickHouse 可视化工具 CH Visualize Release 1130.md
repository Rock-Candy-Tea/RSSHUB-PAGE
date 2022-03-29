
---
title: 'ClickHouse 可视化工具 CH Visualize Release 1.13.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://dbm.incubator.edurt.io/assets/images/1.13.0/quickly_enter.jpg'
author: 开源中国
comments: false
date: Tue, 29 Mar 2022 11:07:00 GMT
thumbnail: 'https://dbm.incubator.edurt.io/assets/images/1.13.0/quickly_enter.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:rgba(0, 0, 0, 0.87); text-align:start">DBM<span> </span><code>1.13.0</code><span> </span>版本发布!</p> 
<p style="color:rgba(0, 0, 0, 0.87); text-align:start">发布时间:<span> </span><code>2022-03-29</code></p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">功能 (增强)<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Fzh%2Frelease%2F1.13.0-20220329.html%23_1" target="_blank">¶</a></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>元数据管理删除数据库支持快速输入数据库名称<span> </span><img alt="Quickly enter" src="https://dbm.incubator.edurt.io/assets/images/1.13.0/quickly_enter.jpg" referrerpolicy="no-referrer"></li> 
 <li>添加<span> </span><code>EXPLAIN AST</code>,<span> </span><code>EXPLAIN SYNTAX</code>,<span> </span><code>EXPLAIN PLAN</code>,<span> </span><code>EXPLAIN PIPELINE</code>,<span> </span><code>EXPLAIN ESTIMATE</code>,<span> </span><code>EXPLAIN TABLE OVERRIDE</code><span> </span><img alt="EXPLAIN ..." src="https://dbm.incubator.edurt.io/assets/images/1.13.0/explain.jpg" referrerpolicy="no-referrer"></li> 
 <li>查询结果可导出为 CSV 文件<span> </span><img alt="Export" src="https://dbm.incubator.edurt.io/assets/images/1.13.0/export.png" referrerpolicy="no-referrer"></li> 
 <li>支持删除数据库时删除表<span> </span><img alt="img.png" src="https://dbm.incubator.edurt.io/assets/images/1.13.0/delete_table_on_database.png" referrerpolicy="no-referrer"></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">UI<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Fzh%2Frelease%2F1.13.0-20220329.html%23ui" target="_blank">¶</a></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>元数据管理服务请求失败状态为红色<span> </span><img alt="Service failure" src="https://dbm.incubator.edurt.io/assets/images/1.13.0/service_failure.png" referrerpolicy="no-referrer"></li> 
 <li>元数据管理菜单添加了要显示的子菜单数量<span> </span><img alt="Submenus count" src="https://dbm.incubator.edurt.io/assets/images/1.13.0/submenus_count.png" referrerpolicy="no-referrer"></li> 
 <li>添加查询结果返回的总行数<span> </span><img alt="Query result" src="https://dbm.incubator.edurt.io/assets/images/1.13.0/query_result.png" referrerpolicy="no-referrer"></li> 
 <li>支持查询历史执行中异常数据的高亮显示<span> </span><img alt="img.png" src="https://dbm.incubator.edurt.io/assets/images/query/query_history.png" referrerpolicy="no-referrer"></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">优化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Fzh%2Frelease%2F1.13.0-20220329.html%23_2" target="_blank">¶</a></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>优化元数据管理删除数据列<span> </span><img alt="img.png" src="https://dbm.incubator.edurt.io/assets/images/1.13.0/delete_column.png" referrerpolicy="no-referrer"></li> 
 <li>优化查询结果展示表<span> </span><img alt="Table" src="https://dbm.incubator.edurt.io/assets/images/1.13.0/table.png" referrerpolicy="no-referrer"></li> 
 <li>删除数据分区的优化数据排列<span> </span><img alt="img.png" src="https://dbm.incubator.edurt.io/assets/images/1.13.0/clean_partitions.png" referrerpolicy="no-referrer"></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Fzh%2Frelease%2F1.13.0-20220329.html%23_3" target="_blank">¶</a></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>添加安装文档</li> 
 <li>添加查询历史文档</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">Bug<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Fzh%2Frelease%2F1.13.0-20220329.html%23bug" target="_blank">¶</a></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>修复清除多分区数据的问题</li> 
 <li>修复 run dev Last few GCs</li> 
 <li>修复了取消执行后编辑器状态不重置的问题</li> 
 <li>修复 README.md 文件脚本指向错误</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">贡献者（排名不分先后）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Fzh%2Frelease%2F1.13.0-20220329.html%23_4" target="_blank">¶</a></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FqianmoQ" target="_blank">@qianmoQ</a></li> 
</ul> 
<p>下载地址</p> 
<p><strong style="color:#c0392b">https://github.com/EdurtIO/dbm/releases/tag/1.13.0</strong></p>
                                        </div>
                                      
</div>
            