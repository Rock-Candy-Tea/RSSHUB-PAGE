
---
title: 'SQLAlchemy 1.4.32 发布，Python ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/201703/10211112_UW9j.jpg'
author: 开源中国
comments: false
date: Tue, 08 Mar 2022 07:05:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/201703/10211112_UW9j.jpg'
---

<div>   
<div class="content">
                                                                                            <p>SQLAlchemy 1.4.32 已发布。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">SQLAlchemy 是一个 Python 的 SQL 工具包以及数据库对象映射 (ORM) 框架。它包含整套企业级持久化模式，专门用于高效和高性能的数据库访问。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="386" src="https://static.oschina.net/uploads/img/201703/10211112_UW9j.jpg" width="500" referrerpolicy="no-referrer"></p> 
<p>1.4.32 版本修复了一系列问题，其中大部分是是针对各种错误条件下的错误报告方面。此外还包括更新以适应最近版本的 cx_Oracle 和 mariadbconnector 变化，以及改进测试套件以纠正在第三方打包和集成环境中遇到的问题。</p> 
<ul> 
 <li>修复当 INSERT 未能静默实际插入行（例如来自触发器）时引发的 ORM 异常回归 (<span style="background-color:#ffffff; color:#212529">References:<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlalchemy.org%2Ftrac%2Fticket%2F7594" target="_blank">#7594</a>)</li> 
 <li>修复使用<strong>完全限定路径 </strong>(fully qualified path) 作为类名的问题，因为该路径<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.sqlalchemy.org%2Fen%2F14%2Form%2Frelationship_api.html%23sqlalchemy.orm.relationship" target="_blank"><code>relationship()</code></a>包含不是第一个标记的路径标记的错误名称，将无法引发信息性错误，而是在后续步骤中随机失败 (<span style="background-color:#ffffff; color:#212529">References:<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlalchemy.org%2Ftrac%2Fticket%2F7697" target="_blank">#7697</a>)</li> 
</ul> 
<p>SQLAlchemy 2.0 的开发工作仍在继续，最近的工作重点是提供新的面向类型的映射样式 (mapping styles)，以及面向整个库中的整体 pep-484 支持。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlalchemy.org%2Fchangelog%2FCHANGES_1_4_32" target="_blank">详情查看 Changelog</a>。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlalchemy.org%2Fdownload.html" target="_blank">https://www.sqlalchemy.org/download.html</a></p>
                                        </div>
                                      
</div>
            