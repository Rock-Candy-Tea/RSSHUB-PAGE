
---
title: 'SQLAlchemy 1.4.13 发布，Python ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3095'
author: 开源中国
comments: false
date: Tue, 04 May 2021 23:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3095'
---

<div>   
<div class="content">
                                                                                            <p>SQLAlchemy 是 Python SQL 工具箱和对象关系映射器，它为应用程序开发人员提供了 SQL 的全部功能和灵活性。它提供了一整套知名的企业级持久性模式，旨在高效、高性能地访问数据库，并被适配为一种简单的 Pythonic 域语言。</p> 
<p>SQLAlchemy 1.4.13 版本的更新内容如下：</p> 
<h3>orm</h3> 
<ul> 
 <li> <p><strong>[orm] [bug] [regression]</strong></p> <p>修正了 <code>selectinload</code> 加载器策略的回归，当处理跨多列连接的关系时，例如使用复合外键时，会导致它不正确地缓存其内部状态。无效的缓存会导致其他无关的加载器操作失败；</p> </li> 
 <li> <p><strong>[orm] [bug] [regression]</strong></p> <p>修正了回归，即如果主导实体是一个 SQL 函数或其他从相关主实体派生的表达式，而不是一个简单的实体或该实体的列， <code>Query.filter_by()</code> 将无法工作。此外，改进了 <code>Select.filter_by()</code> 的行为，使其即使在非 ORM 环境下也能与列表达式一起工作。</p> </li> 
 <li> <p><strong>[orm] [bug] [regression]</strong></p> <p>修正了使用 <code>selectinload()</code> 和 <code>subqueryload()</code> 加载一个两级深度的路径会导致属性错误的问题。</p> </li> 
 <li> <p><strong>[orm] [bug] [regression]</strong></p> <p>修正了在使用 <code>noload()</code> 加载器策略和 "动态"关系时，会导致属性错误的问题，因为 noload 策略会试图将自己应用到动态加载器上。</p> </li> 
</ul> 
<h3>asyncio</h3> 
<ul> 
 <li> <p><strong>[asyncio] [bug] [regression]</strong></p> <p>修正了 #6337 引入的一个回归，即在任何 asyncio 循环启动之前实例化 asyncio 引擎时，会创建一个 asyncio.Lock，它可能被附加到错误的循环中，导致在某些情况下试图使用该引擎时出现 asyncio 错误信息。</p> </li> 
</ul> 
<h3>postgresql</h3> 
<ul> 
 <li> <p><strong>[postgresql] [usecase]</strong></p> <p>在 PostgreSQL 的 pg8000 dialect 中增加对服务器端游标的支持。这允许使用 <code>Connection.execution_options.stream_results</code> 选项。</p> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.sqlalchemy.org%2Fen%2F14%2Fchangelog%2Fchangelog_14.html%23change-1.4.13" target="_blank">https://docs.sqlalchemy.org/en/14/changelog/changelog_14.html#change-1.4.13</a></p>
                                        </div>
                                      
</div>
            