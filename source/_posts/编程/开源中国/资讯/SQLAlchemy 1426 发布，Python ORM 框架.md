
---
title: 'SQLAlchemy 1.4.26 发布，Python ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4828'
author: 开源中国
comments: false
date: Fri, 22 Oct 2021 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4828'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">SQLAlchemy 1.4.26 版本发布了，SQLAlchemy 是 Python SQL 工具箱和对象关系映射器，它为应用程序开发人员提供了 SQL 的全部功能和灵活性，旨在高效、高性能地访问数据库，被适配为一种简单的 Pythonic 域语言。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">SQLAlchemy 1.4.26<span> </span><strong>主要修复</strong>了 SQLAlchemy 1.4 版本大更新带来的一些 bug，主要内容如下：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#333333">修正了使用混合和复合属性时，</span><code>update()</code><span> </span><span style="color:#333333">语句在 ORM 上下文环境的用法。</span></li> 
 <li><span style="color:#333333">修复了<span> </span></span><code>with_loader_criteria()</code><span> </span>ORM 选项。</li> 
 <li>为新的 API 调整<span style="color:#333333"><span> </span>ORM 会话接口。</span></li> 
 <li><span style="color:#333333">给<span> </span><code>Query.join()<span> </span></code>不常用的模式加入遗留警告。</span></li> 
 <li>SQL / ORM 修复了从重复的、未标记的列表达式中进行选择的用例，通常是在 UNION 语句中用作占位符时的 null() 构造。</li> 
 <li><span style="color:#333333">针对 PostgreSQL ：</span><span style="color:#2e3033">跟<span> </span><code>PostgreSQL ARRAY</code><span> </span>数据类型一起使用时，改进了 “</span><span style="color:#333333">expanding IN"<span> </span></span><span style="color:#2e3033">SQL 特性，还修复了大多数<span> </span></span><span style="color:#333333">PostgreSQL 特有的</span><span style="color:#2e3033"><span> </span></span><code>any_()</code><span style="color:#333333"><span> </span>和<span> </span></span><code>all_()</code><span> </span> <span style="color:#333333">column  方法。</span></li> 
 <li><span style="color:#333333">针对 MySQL ，</span><span style="color:#2e3033">为适应 MariaDB 10.6 系列进行了修复。</span></li> 
 <li><span style="color:#2e3033">针对 SQL ，对外键约束和表单/视图检测的反射做了一些修复和改进。</span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlalchemy.org%2Fblog%2F2021%2F10%2F19%2Fsqlalchemy-1.4.26-released%2F" target="_blank">https://www.sqlalchemy.org/blog/2021/10/19/sqlalchemy-1.4.26-released/</a></p>
                                        </div>
                                      
</div>
            