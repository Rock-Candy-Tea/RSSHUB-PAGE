
---
title: 'ClickHouse 可视化工具 CH Visualize Release 1.14.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/table_type.png'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 09:17:00 GMT
thumbnail: 'https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/table_type.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start"><span><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>DBM 版本<code>1.14.0</code>发布！</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>推出日期：<code>2022-04-10</code></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><strong><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>增强<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Frelease%2F1.14.0-20220410.html%23enhancement" target="_blank">¶</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>支持可视化构建 MongoDB 表 <img alt="表类型" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/table_type.png" referrerpolicy="no-referrer"></li> 
 <li>支持可视化添加表的 TTL <img alt="TTL修改" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/ttl_modify.png" referrerpolicy="no-referrer"> <img alt="TTL修改配置" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/ttl_modify_configuration.png" referrerpolicy="no-referrer"></li> 
 <li>支持数据源拷贝 <img alt="数据源复制.png" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/datasource_copy.png" referrerpolicy="no-referrer"></li> 
 <li>支持可视化移除表的 TTL <img alt="TTL 移除" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/ttl_remove.png" referrerpolicy="no-referrer"> <img alt="TTL 移除配置" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/ttl_remove_configuration.png" referrerpolicy="no-referrer"></li> 
 <li>支持元数据管理以更改数据库名称 <img alt="重命名数据库" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/rename_database.png" referrerpolicy="no-referrer"> <img alt="数据库支持" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/support.png" referrerpolicy="no-referrer"> <img alt="数据库不支持" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/not_support.png" referrerpolicy="no-referrer"></li> 
 <li>查询历史支持 IndexDB 存储</li> 
 <li>支持删除单个查询历史 <img alt="删除简单查询历史" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/delete_simple_query_history.png" referrerpolicy="no-referrer"></li> 
 <li>支持元数据管理添加列 <img alt="图片.png" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/img.png" referrerpolicy="no-referrer"> <img alt="img_1.png" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/img_1.png" referrerpolicy="no-referrer"></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><strong><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>用户界面<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Frelease%2F1.14.0-20220410.html%23ui" target="_blank">¶</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>不可用的数据源不允许点击操作 <img alt="不可用数据" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/unavailable.png" referrerpolicy="no-referrer"></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><strong><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>优化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Frelease%2F1.14.0-20220410.html%23optimize" target="_blank">¶</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>优化数据表中只删除一列时的提示信息 <img alt="图片.png" src="https://dbm.incubator.edurt.io/assets/images/versions/1.14.0/img_2.png" referrerpolicy="no-referrer"></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><strong><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Frelease%2F1.14.0-20220410.html%23docs" target="_blank">¶</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>优化数据源管理文档</li> 
 <li>添加监视器 → 连接文档</li> 
 <li>添加监视器→突变文档</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><strong><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>漏洞<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Frelease%2F1.14.0-20220410.html%23bug" target="_blank">¶</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li>修复删除已有列的错误情况</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><strong><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>贡献者（排名不分先后）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbm.incubator.edurt.io%2Frelease%2F1.14.0-20220410.html%23contributors-in-no-particular-order" target="_blank">¶</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></h4> 
<hr> 
<ul style="list-style-type:disc"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FqianmoQ" target="_blank">@qianmoQ</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下载地址</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#c0392b">https://github.com/EdurtIO/dbm/releases/tag/1.14.0</strong></p>
                                        </div>
                                      
</div>
            