
---
title: 'SQLAlchemy 1.4.7 发布，Python ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4423'
author: 开源中国
comments: false
date: Mon, 12 Apr 2021 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4423'
---

<div>   
<div class="content">
                                                                                            <p>SQLAlchemy 是 Python SQL 工具箱和对象关系映射器，它为应用程序开发人员提供了 SQL 的全部功能和灵活性。它提供了一整套知名的企业级持久性模式，旨在高效、高性能地访问数据库，并被适配为一种简单的 Pythonic 域语言。</p> 
<p>SQLAlchemy 1.4.7 版本的更新内容如下：</p> 
<h3>orm</h3> 
<ul> 
 <li> <p><strong>[bug] [regression]</strong></p> <p>修正了 subqueryload() 加载器策略在 subqueryload 的 "路径"超过一级深度时，无法正确容纳子选项的问题，例如列上的 defer() 选项；</p> </li> 
 <li> <p><strong>[bug] [regression]</strong></p> <p>修正了 dogpile.caching 示例所依赖的 merge_frozen_result() 函数未被包含在测试中，并且由于内部参数不正确而开始失败的回归问题；</p> </li> 
 <li> <p><strong>[bug] [regression]</strong></p> <p>修正了一个关键的回归问题，即当刷新发生时，在没有现有事务的情况下，Session 可能无法 "自动开始"一个新的事务，从而隐含地将 Session 置于传统的自动提交模式，从而提交事务。现在，Session 除了修复刷新问题外，还有一个检查，可以防止这种情况发生；</p> </li> 
 <li> <p><strong>[bug] [regression]</strong></p> <p>修正了 ORM 编译方案假设混合属性的函数名与属性名相同的回归问题，当它试图确定结果元组中每个元素的正确名称时，会引发 AttributeError。类似的问题在 1.3 中也存在，但只影响元组行的名称。这里的修复增加了一项检查，即在分配这个名称之前，检查混合体的函数名是否确实存在于类或其超类的 <strong>dict</strong> 中；否则，混合体被认为是 "未命名的"，ORM 结果元组将使用底层表达式的命名方案。</p> </li> 
 <li> <p><strong>[bug] [regression]</strong></p> <p>修正了作为 #1763 的一部分添加的新特性引起的关键回归，eager loaders 在未到期操作上被调用。新特性利用 "immediateload" eager loaders 策略来替代集合加载策略，与其他"后加载"策略不同的是，该策略不适应相互依赖关系之间的递归调用，导致递归溢出错误。</p> </li> 
</ul> 
<h3>sql</h3> 
<ul> 
 <li> <p><strong>[bug] [regression]</strong></p> <p>增强了用于 ColumnOperators.in_() 操作的"扩展"功能，如果左侧没有设置任何显式类型，则从右侧元素列表中推断表达式的类型。这使得表达式可以支持字符串化等功能。在 1.3 中，ColumnOperators.in_() 表达式并没有自动使用 "expansion"，所以从这个意义上来说，这个变化修复了一个行为上的回归。</p> </li> 
 <li> <p><strong>[bug]</strong></p> <p>修正了"stringify"编译器，以支持"多行" INSERT 语句的基本字符串化，即在 VALUES 关键字后有多个元组的语句。</p> </li> 
</ul> 
<h3>schema</h3> 
<ul> 
 <li> <p><strong>[bug] [regression]</strong></p> <p>修正了在 Connection.execute_options.schema_translate_map 字典中使用包含特殊字符（如大括号）的标记时无法正确替换的问题。方括号字符 [] 的使用现在被明确禁止，因为在当前的实现中，这些字符被用作定界符。</p> </li> 
</ul> 
<h3>mypy</h3> 
<ul> 
 <li> <p><strong>[bug]</strong></p> <p>修正了 Mypy 插件中的问题，即插件没有为不直接从 TypeEngine 下传的子类的列推断正确的类型，特别是 TypeDecorator 和 UserDefinedType 的类型。</p> </li> 
</ul> 
<h3>misc</h3> 
<ul> 
 <li> <p><strong>[change] [tests]</strong></p> <p>在 DefaultDialect 中添加了一个名为 supports_schema 的新标志；当为第三方 dialects 运行测试套件时，第三方 dialects 可以将该标志设置为 True，以启用 SQLAlchemy 的模式级测试。</p> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.sqlalchemy.org%2Fen%2F14%2Fchangelog%2Fchangelog_14.html%23change-1.4.7" target="_blank">https://docs.sqlalchemy.org/en/14/changelog/changelog_14.html#change-1.4.7</a></p>
                                        </div>
                                      
</div>
            