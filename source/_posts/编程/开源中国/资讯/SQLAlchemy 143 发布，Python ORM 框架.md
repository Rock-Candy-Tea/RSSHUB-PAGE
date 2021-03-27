
---
title: 'SQLAlchemy 1.4.3 发布，Python ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2853'
author: 开源中国
comments: false
date: Sat, 27 Mar 2021 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2853'
---

<div>   
<div class="content">
                                                                                            <p>SQLAlchemy 是 Python SQL 工具箱和对象关系映射器，它为应用程序开发人员提供了 SQL 的全部功能和灵活性。它提供了一整套知名的企业级持久性模式，旨在高效、高性能地访问数据库，并被适配为一种简单的 Pythonic 域语言。</p> 
<p>SQLAlchemy 1.4.3 版本的更新内容如下：</p> 
<h3>orm</h3> 
<ul> 
 <li>修正了一个 python 2.7.5（CentOS 7 上的默认版本）无法导入 sqlalchemy 的 bug，因为在这个版本的 Python 上， <code>exec "statement"</code> 和 <code>exec("statement")</code> 的行为方式并不相同。我们使用了兼容性的 <code>exec_()</code> 函数来代替。</li> 
 <li>修正了一个当在属性中使用 <code>Select.correlate_except()</code> 来控制相关性时，使用相关子查询和 <code>column_property()</code> 的 ORM 查询将无法正确地关联包围子查询或 CTE 的错误。</li> 
 <li>修正了新的“relationship with criteria”功能与使用新的“lambda SQL”功能（包括 selectinload 和 lazyload 等加载器策略）的结合可能会失败的 bug，以应对多态加载等更复杂的情况。</li> 
 <li>修复了对 <code>ClauseElement.params()</code> 方法的支持，使 <code>ClauseElement.params()</code> 方法能够正确地与 <code>Select</code> 对象一起工作，该对象包括跨 ORM 关系结构的连接，这是 1.4 中的一个新特性。</li> 
 <li>修正了关系加载器机制内部产生"在 2.0 中删除"警告的问题。</li> 
</ul> 
<h3>orm declarative</h3> 
<ul> 
 <li>修正了每类级别上的 <code>.metadata</code> 属性不会被遵循的回归问题.</li> 
</ul> 
<h3>engine</h3> 
<ul> 
 <li>将 <code>ResultProxy</code> 名称恢复到 <code>sqlalchemy.engine</code> 命名空间。这个名字指的是 <code>LegacyCursorResult</code> 对象。</li> 
</ul> 
<h3>mypy</h3> 
<ul> 
 <li>添加了对 Mypy 扩展的支持，以正确解释使用 <code>as_declarative()</code> 函数以及 <code>registry.as_declarative_base()</code> 方法生成的声明式基类。</li> 
 <li>修正了 Mypy 插件中 Python 类型检测 <code>Boolean</code> 列类型会产生异常的错误；另外实现了对 <code>Enum</code> 的支持，包括检测基于字符串的枚举与使用Python <code>enum.Enum</code>。</li> 
</ul> 
<h3>postgresql</h3> 
<ul> 
 <li>修正了在 PostgreSQL 中，表的身份列在混合大小写名称中的反映。</li> 
</ul> 
<h3>sqlite</h3> 
<ul> 
 <li>增加了对与 SQLAlchemy asyncio 扩展一起使用的 aiosqlite 数据库驱动程序的支持。</li> 
 <li>修复了在 1.4 版本中退步的 <code>pysqlcipher</code> dialect，使其正确连接，并增加了测试 + CI 支持，使驱动保持在工作状态。现在 dialect 默认导入 Python 3 的 <code>sqlcipher3</code> 模块。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.sqlalchemy.org%2Fen%2F14%2Fchangelog%2Fchangelog_14.html%23change-1.4.3" target="_blank">https://docs.sqlalchemy.org/en/14/changelog/changelog_14.html#change-1.4.3</a></p>
                                        </div>
                                      
</div>
            