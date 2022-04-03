
---
title: 'SQLAlchemy 1.4.34 发布，Python ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0403/073944_PTPZ_5430600.png'
author: 开源中国
comments: false
date: Sun, 03 Apr 2022 07:40:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0403/073944_PTPZ_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">SQLAlchemy 1.4.34 是紧随 1.4.33 发布的版本，主要是修复了一个回归错误，即如果语句中包含 ORM 实体，通过 Session.execute() 方法运行 insert() 构造函数会失败。此外还对 psycopg2 的"executemany mode"进行了额外的改进。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">被取消的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlalchemy.org%2Fblog%2F2022%2F03%2F31%2Fsqlalchemy-1.4.33-released%2F" target="_blank">1.4.33</a><span> </span>包含了大量的修复和改进，包括大幅减少 ORM 映射的内存使用，以及对 Engine.dispose() 功能的改进，这使得在多进程环境中可以更好地整合。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlalchemy.org%2Fblog%2F2022%2F03%2F31%2Fsqlalchemy-1.4.34-released%2F" target="_blank">详情查看发布公告</a>。</p> 
<hr> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">SQLAlchemy 是一个 Python 的 SQL 工具包以及数据库对象映射 (ORM) 框架。它包含整套企业级持久化模式，专门用于高效和高性能的数据库访问。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="376" src="https://static.oschina.net/uploads/space/2022/0403/073944_PTPZ_5430600.png" width="500" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">最后，SQLAlchemy 2.0 的开发工作仍在继续，最近的工作重点是提供新的面向类型的映射样式 (mapping styles)，以及面向整个库中的整体 pep-484 支持。</span></p>
                                        </div>
                                      
</div>
            