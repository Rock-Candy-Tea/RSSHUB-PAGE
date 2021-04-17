
---
title: 'SQLAlchemy 1.4.8 发布，Python ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4985'
author: 开源中国
comments: false
date: Sat, 17 Apr 2021 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4985'
---

<div>   
<div class="content">
                                                                                            <p>SQLAlchemy 是 Python SQL 工具箱和对象关系映射器，它为应用程序开发人员提供了 SQL 的全部功能和灵活性。它提供了一整套知名的企业级持久性模式，旨在高效、高性能地访问数据库，并被适配为一种简单的 Pythonic 域语言。</p> 
<p>SQLAlchemy 1.4.8 版本的更新内容如下：</p> 
<h3>orm：</h3> 
<ul> 
 <li>[bug] 修复了涉及 <code>with_expression()</code> 加载程序选项的缓存泄漏，该泄漏不会正确地将给定的 SQL 表达式视为缓存键的一部分。此外，修复了涉及相应 <code>query_expression()</code> 特征的回归 。虽然从技术上讲该 bug 也存在于 1.3 中，但直到 1.4 才暴露出来。当不需要时，null()的"default expr"值会被呈现出来。另外，当 ORM 重写语句时，如使用 jianed eager loading 时，也不能正确适应。该修复确保了像 null 和 true 这样的表达式不会被"适配"为 ORM 语句中的列引用，另外确保了如果没有使用 with_expression()，没有默认表达式的 query_expression() 不会在语句中呈现。</li> 
 <li>[bug] 修正了#1763引入的 Session.refresh() 新特性中的问题，急于加载的关系也会被刷新，其中 lazy="raise" 和 lazy="raise_on_sql" 加载器策略会干扰 immediateload() 加载器策略，因此对于用 selectinload()、subqueryload() 加载的关系也会破坏该特性。</li> 
</ul> 
<h3>引擎：</h3> 
<ul> 
 <li>[bug] Dialect.has_table() 方法现在会在传递一个 non-Connection 时引发一个信息异常，因为这种不正确的行为似乎很常见。这个方法不打算用于 dialect 之外的外部使用。请使用 Inspector.has_table() 方法，或者为了与旧版本的 SQLAlchemy 交叉兼容，使用 Engine.has_table() 方法。</li> 
</ul> 
<h3>sql：</h3> 
<ul> 
 <li>[feature] CursorResult.inserted_primary_key 返回的元组现在是一个 Row 对象，在现有的元组接口之上有一个命名的元组接口。</li> 
 <li>[bug] 修正了一个回归问题，即如果 BindParameter 对象是从内部克隆操作或从 pickle 操作中复制过来的，并且参数名中包含空格或其他特殊字符，则 BindParameter 对象不能正确地渲染 IN 表达式（即使用1.4中的 "post compile "功能）。</li> 
 <li>[bug] 修正了引入 INSERT 语法 "INSERT......VALUES (DEFAULT) "在一些支持 "INSERT......DEFAULT VALUES "的后台不支持的问题，包括 SQLite。现在，这两种语法在每个 dialect 中都被单独支持或不支持，例如，MySQL 支持 "VALUES (DEFAULT)"，但不支持 "DEFAULT VALUES"。</li> 
</ul> 
<h3>mypy：</h3> 
<ul> 
 <li>[change] 更新了Mypy插件，使其仅使用语义分析器的公共插件接口。</li> 
 <li>[bug] 修改了 1.4.7 版本的 OrderList 的修正，因为它是针对不正确的 API 测试。</li> 
</ul> 
<h3>asyncio：</h3> 
<ul> 
 <li>[bug] 修正了防止将AsyncSession的绑定属性设置为正确值的排印错误。</li> 
</ul> 
<h3>mssql：</h3> 
<ul> 
 <li>[bug] [regression] 修正了一个与 #6173、#6184 相同领域的额外回归，即在 SQL Server 中使用 OFFSET 的值为 0 与 LIMIT 结合，会创建一个使用 "TOP" 的语句，就像 1.3 中的行为一样，然而由于缓存的原因，会导致无法对 OFFSET 的其他值做出相应的响应。如果不是 "0" 在先，那么就可以了。对于修复，现在只有在完全省略 OFFSET 值的情况下才会发出 "TOP" 语法，即不使用 Select.offset()。需要注意的是，现在这个变化要求，如果使用了 "with_ties" 或 "percent" 修饰符，语句不能指定 OFFSET 为 0，现在需要完全省略。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.sqlalchemy.org%2Fen%2F14%2Fchangelog%2Fchangelog_14.html%23change-1.4.8" target="_blank">https://docs.sqlalchemy.org/en/14/changelog/changelog_14.html#change-1.4.8</a></p>
                                        </div>
                                      
</div>
            