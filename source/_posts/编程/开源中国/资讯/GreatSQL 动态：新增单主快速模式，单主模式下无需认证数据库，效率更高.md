
---
title: 'GreatSQL 动态：新增单主快速模式，单主模式下无需认证数据库，效率更高'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9430'
author: 开源中国
comments: false
date: Wed, 08 Sep 2021 10:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9430'
---

<div>   
<div class="content">
                                                                                            <h1>GreatSQL动态（2021.9.7）</h1> 
<hr> 
<p><strong>新特性</strong></p> 
<ul> 
 <li> <p>新增单主快速模式，单主模式下无需认证数据库，效率更高</p> </li> 
 <li> <p>新增投票节点，降低MGR部署成本开销</p> </li> 
</ul> 
<p><strong>BUG修复</strong></p> 
<ul> 
 <li> <p>解决recovering状态下关闭mgr导致丢数据或者gtid不一致的严重问题</p> </li> 
 <li> <p>解决外键约束导致MGR报错退出问题</p> </li> 
 <li> <p>解决rejoin过程中反复查询MGR MEMBER状态可能导致崩溃的问题</p> </li> 
 <li> <p>解决创建applier线程失败导致的死循环问题</p> </li> 
</ul> 
<p>Enjoy GreatSQL :)</p>
                                        </div>
                                      
</div>
            