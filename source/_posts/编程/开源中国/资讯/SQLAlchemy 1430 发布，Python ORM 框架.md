
---
title: 'SQLAlchemy 1.4.30 发布，Python ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9666'
author: 开源中国
comments: false
date: Fri, 21 Jan 2022 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9666'
---

<div>   
<div class="content">
                                                                                            <p>SQLAlchemy 是 Python SQL 工具箱和对象关系映射器，它为应用程序开发人员提供了 SQL 的全部功能和灵活性。它提供了一整套知名的企业级持久性模式，旨在高效、高性能地访问数据库，并被适配为一种简单的 Pythonic 域语言。</p> 
<p>SQLAlchemy 1.4.30 版本的更新内容如下：</p> 
<h3>orm</h3> 
<ul> 
 <li> <p><strong>[orm] [bug]</strong></p> <p>修正了这样一个问题：对于同一个类，多次调用 <code>registry.map_imperatively()</code> 会产生一个意外的错误，而不是目标类已被映射的信息性错误。</p> </li> 
 <li> <p><strong>[orm] [bug] [asyncio]</strong></p> <p>在 <code>AsyncSession</code> 类中增加了缺失的 <code>AsyncSession.invalidate()</code> 方法。</p> </li> 
 <li> <p><strong>[orm] [bug] [regression]</strong></p> <p>修正了 1.4.23 中出现的回归问题，该回归在某些情况下会导致加载器选项被错误处理，从而会导致 <code>TypeError</code>。</p> </li> 
 <li> <p><strong>[orm] [bug] [regression]</strong></p> <p>修复了 ORM 回归问题，其中，如果现有构造针对固定表，则针对现有 <code>aliased()</code> 构造调用<code>aliased()</code>函数将无法生成正确的 SQL。</p> </li> 
 <li> <p><strong>[orm] [bug]</strong></p> <p>修复了<code>Select.correlate_except()</code>方法在传递<code>None</code>值或无参数时，在 ORM 上下文中使用时不会关联任何元素。</p> </li> 
 <li> <p><strong>[orm] [bug] [regression]</strong></p> <p>修复了 1.3 版本中的回归问题，其中"子查询加载"加载程序策略如果用于使用<code>Query.from_statement()</code>或<code>Select.from_statement()</code>的查询，则会失败并带有堆栈跟踪的问题</p> </li> 
</ul> 
<h3>sql</h3> 
<ul> 
 <li> <p><strong>[sql] [bug] [postgresql]</strong></p> <p>在系统中增加了额外的规则，即从 Python 字面意义上确定 TypeEngine 的实现，以便对类型进行第二层调整</p> </li> 
 <li> <p><strong>[sql] [bug]</strong></p> <p>在将方法对象传递到 SQL 构造时添加了信息性错误消息</p> </li> 
</ul> 
<h3>mypy</h3> 
<ul> 
 <li> <p><strong>[mypy] [bug]</strong></p> <p>修复了运行 id 守护程序模式时 Mypy 崩溃的问题，该模式是由内部 mypy <code>Var</code>实例上的缺少属性引起的。</p> </li> 
</ul> 
<h3>asyncio</h3> 
<ul> 
 <li> <p><strong>[asyncio] [usecase]</strong></p> <p>向 asyncio 驱动程序使用的 DBAPI 连接接口添加了新的方法<code>AdaptedConnection.run_async()</code>这允许在无法使用<code>await</code>关键字的同步式函数中直接针对基础"驱动程序"连接调用方法。</p> </li> 
</ul> 
<h3>postgresql</h3> 
<ul> 
 <li> <p><strong>[postgresql] [usecase]</strong></p> <p>为 <code>UUID</code> 数据类型添加了字符串渲染，因此用 "literal_binds" 对使用该类型的语句进行字符串化，将为 PostgreSQL 后端渲染一个合适的字符串值。</p> </li> 
 <li> <p><strong>[postgresql] [bug] [asyncpg]</strong></p> <p>改进了对 asyncpg 处理 TIME WITH TIMEZONE 的支持，这一点并没有完全实现。</p> </li> 
 <li> <p><strong>[postgresql] [bug]</strong></p> <p>修正了对需要转义字符的枚举值数组的处理。</p> </li> 
</ul> 
<h3>mysql</h3> 
<ul> 
 <li> <p><strong>[mysql] [change]</strong></p> <p>在 MySQL 和 MariaDB dialect 初始化中，用等价的 <code>SELECT @@variable</code> 替换 <code>SHOW VARIABLES LIKE</code> 语句。这应该可以避免 <code>SHOW VARIABLES</code> 引起的互斥，提高初始化性能。</p> </li> 
 <li> <p><strong>[mysql] [bug]</strong></p> <p>从 asyncmy dialect 中删除了对 PyMySQL 的不必要依赖。</p> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.sqlalchemy.org%2Fen%2F14%2Fchangelog%2Fchangelog_14.html%23change-1.4.30" target="_blank">https://docs.sqlalchemy.org/en/14/changelog/changelog_14.html#change-1.4.30</a></p>
                                        </div>
                                      
</div>
            