
---
title: 'SQLAlchemy 1.4.40 发布，Python ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4367'
author: 开源中国
comments: false
date: Wed, 10 Aug 2022 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4367'
---

<div>   
<div class="content">
                                                                                            <p>SQLAlchemy 是 Python SQL 工具箱和对象关系映射器，它为应用程序开发人员提供了 SQL 的全部功能和灵活性。它提供了一整套知名的企业级持久性模式，旨在高效、高性能地访问数据库，并被适配为一种简单的 Pythonic 域语言。</p> 
<p>SQLAlchemy 1.4.40 版本的更新内容如下：</p> 
<h3>orm</h3> 
<ul> 
 <li> <p><strong>[orm] [bug]</strong></p> <p>修正了在多态 SELECT 中多次引用 CTE 的问题，该问题可能导致同一 CTE 的多个 "克隆" 被构建，然后将这两个 CTE 触发为重复的。</p> </li> 
</ul> 
<h3>engine</h3> 
<ul> 
 <li> <p><strong>[engine] [usecase]</strong></p> <p>在 Core 中为 <code>Connection</code> 实现了新的 <code>Connection.execution_options.yield_per</code> 执行选项，以反映 ORM 中可用的相同 yield_per 选项。</p> </li> 
 <li> <p><strong>[engine] [bug]</strong></p> <p>修正了 <code>Result</code> 中的错误，在使用 <code>Connection.execution_options.stream_results</code> 时，如果使用的 dialect 不支持明确的 "server side cursor" 设置，则不会使用缓冲的结果策略。</p> </li> 
 <li> <p><strong>[engine] [bug]</strong></p> <p>添加了 <code>FilterResult.yield_per()</code>，以便 <code>MappingResult</code>、 <code>ScalarResult</code> 和 <code>AsyncResult</code> 等结果实现能够访问该方法。</p> </li> 
</ul> 
<h3>sql</h3> 
<ul> 
 <li> <p><strong>[sql] [bug]</strong></p> <p>调整了字符串包含函数 <code>.contains()</code>, <code>.startswith()</code>, <code>.endswith()</code> 的 SQL 编译，以强制使用字符串连接操作符，而不是依赖加法操作符的重载</p> </li> 
</ul> 
<h3>mypy</h3> 
<ul> 
 <li> <p><strong>[mypy] [bug]</strong></p> <p>修正了 mypy 插件在默认使用 lambda 作为 Column 时的崩溃问题</p> </li> 
</ul> 
<h3>asyncio</h3> 
<ul> 
 <li> <p><strong>[asyncio] [bug]</strong></p> <p>当使用 <code>AsyncConnection</code> 或 <code>AsyncSession</code> 作为上下文管理器时，特别是在 <code>__aexit()__</code> 上下文管理器退出时，为连接和会话释放过程添加了 <code>asyncio.shield()</code> ，在上下文管理器完成后释放对象。</p> </li> 
</ul> 
<h3>postgresql</h3> 
<ul> 
 <li> <p><strong>[postgresql] [bug]</strong></p> <p>修正了 psycopg2 dialect 中的问题，即为 #4392 实现的 "多主机" 功能，可以在查询字符串中以 <code>?host=host1:port1&host=host2:port2&host=host3:port3</code> 的形式传递多个 <code>host:port</code> 对，但没有正确实现。</p> </li> 
</ul> 
<h3>misc</h3> 
<ul> 
 <li> <p><strong>[bug] [types]</strong></p> <p>修正了在装饰 <code>ARRAY</code> 数据类型时， <code>TypeDecorator</code> 不能正确代理 <code>__getitem__()</code> 操作符的问题</p> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.sqlalchemy.org%2Fen%2F14%2Fchangelog%2Fchangelog_14.html%23change-1.4.40" target="_blank">https://docs.sqlalchemy.org/en/14/changelog/changelog_14.html#change-1.4.40</a></p>
                                        </div>
                                      
</div>
            