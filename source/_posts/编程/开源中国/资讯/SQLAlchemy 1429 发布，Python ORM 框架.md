
---
title: 'SQLAlchemy 1.4.29 发布，Python ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7971'
author: 开源中国
comments: false
date: Wed, 29 Dec 2021 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7971'
---

<div>   
<div class="content">
                                                                                            <p>SQLAlchemy 是 Python SQL 工具箱和对象关系映射器，它为应用程序开发人员提供了 SQL 的全部功能和灵活性。它提供了一整套知名的企业级持久性模式，旨在高效、高性能地访问数据库，并被适配为一种简单的 Pythonic 域语言。</p> 
<p>SQLAlchemy 1.4.29 版本的更新内容如下：</p> 
<h3>orm</h3> 
<ul> 
 <li> <p><strong>[orm] [usecase]</strong></p> <p>增加了 <code>Session.get.execution_options</code> 参数，该参数之前在 <code>Session.get()</code> 方法中缺失。</p> </li> 
 <li> <p><strong>[orm] [bug]</strong></p> <p>修正了新的方法 <code>PropComparator.and_()</code> 中的问题。</p> </li> 
 <li> <p><strong>[orm] [bug]</strong></p> <p>修正了当在加载器策略中使用 <code>with_loader_criteria()</code> 函数或 <code>PropComparator.and_()</code> 方法时，可能会在 ORM 语句编译中发生递归溢出</p> </li> 
 <li> <p><strong>[orm] [bug] [regression]</strong></p> <p>修正了与缓存相关的问题，即使用形式为 <code>lazyload(aliased(A).bs).joinload(B.cs)</code> 的加载器选项会导致 joinload 在查询被缓存后的运行中被调用。</p> </li> 
</ul> 
<h3>engine</h3> 
<ul> 
 <li> <p><strong>[engine] [bug]</strong></p> <p>纠正了当试图写入 <code>Row</code> 类上的属性时引发的 <code>AttributeError</code> 的错误信息，该属性是不可变的。</p> </li> 
 <li> <p><strong>[engine] [bug] [regression]</strong></p> <p>修正了用于解析 URL 字符串的 <code>make_url()</code> 函数的回归问题，如果使用 Python 2 <code>u''</code> 字符串，查询字符串的解析将进入递归溢出。</p> </li> 
</ul> 
<h3>mypy</h3> 
<ul> 
 <li> <p><strong>[mypy] [bug]</strong></p> <p>修正了 mypy 的回归问题，即 mypy 0.930 为 "命名类型" 的格式增加了额外的内部检查。这破坏了 SQLAlchemy 的 mypy 插件，引发了一个断言错误。</p> </li> 
</ul> 
<h3>asyncio</h3> 
<ul> 
 <li> <p><strong>[asyncio] [usecase]</strong></p> <p>增加了 <code>async_engine_config()</code> 函数，用于从配置 dict 中创建一个异步引擎。这与 <code>engine_from_config()</code> 的行为相同。</p> </li> 
</ul> 
<h3>tests</h3> 
<ul> 
 <li> <p><strong>[tests] [bug] [regression]</strong></p> <p>修正了测试套件中的一个回归问题，即由于检测到额外的测试工件，被称为 <code>CompareAndCopyTest::test_all_present</code> 的测试在某些平台上会失败。</p> </li> 
</ul> 
<p>……</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.sqlalchemy.org%2Fen%2F14%2Fchangelog%2Fchangelog_14.html%23change-1.4.29" target="_blank">https://docs.sqlalchemy.org/en/14/changelog/changelog_14.html#change-1.4.29</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            