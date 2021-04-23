
---
title: 'SQLAlchemy 1.4.11 发布，Python ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1395'
author: 开源中国
comments: false
date: Fri, 23 Apr 2021 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1395'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SQLAlchemy 是 Python SQL 工具箱和对象关系映射器，它为应用程序开发人员提供了 SQL 的全部功能和灵活性。它提供了一整套知名的企业级持久性模式，旨在高效、高性能地访问数据库，并被适配为一种简单的 Pythonic 域语言。</p> 
<p>SQLAlchemy 1.4.11 版本的更新内容如下：</p> 
<h4>orm declarative：</h4> 
<ul> 
 <li> <p>[orm] [declarative] [bug] [regression]：</p> <p>修正了最近支持 Python 数据类的变化所带来的回归问题，即 ORM 映射的类无法成功覆盖 <code>__new__()</code> 方法；</p> </li> 
</ul> 
<h4>引擎：</h4> 
<ul> 
 <li> <p>[engine] [bug] [regression]：</p> <p>修正了 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.sqlalchemy.org%2Ftrac%2Fticket%2F5497" target="_blank">#5497</a> 中的变化所导致的关键性回归，即连接池的 "init" 阶段不再发生在互斥隔离中，这使得其他线程可以在 dialect 未初始化的情况下继续进行，这可能会影响 SQL 语句的编译。</p> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.sqlalchemy.org%2Fen%2F14%2Fchangelog%2Fchangelog_14.html%23change-1.4.11" target="_blank">https://docs.sqlalchemy.org/en/14/changelog/changelog_14.html#change-1.4.11</a></p>
                                        </div>
                                      
</div>
            