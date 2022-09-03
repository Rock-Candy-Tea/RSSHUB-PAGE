
---
title: 'Diesel 2.0.0 正式发布，Rust ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8855'
author: 开源中国
comments: false
date: Sat, 03 Sep 2022 07:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8855'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#24292f">Diesel 2.0.0 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdiesel.rs%2Fnews%2F2_0_0_release.html" target="_blank">发布</a>。据称此版本开发周期长达 3 年，包含了超过 1700 次 commit。</span></p> 
<blockquote>
 Diesel 是一个安全可扩展的
 <span> </span>
 <a href="http://www.oschina.net/p/rust" target="_blank">Rust</a> ORM 框架和查询构建工具。Diesel 可避免运行时错误，提供最好的性能。
</blockquote> 
<p>2.0 添加了许多新功能，并重写了大部分内部结构。由于这是新的大版本，它还包含许多破坏性变化，具体处理方案可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdiesel.rs%2Fguides%2Fmigration_guide.html" target="_blank">迁移指南</a>。</p> 
<p><strong>更新亮点</strong></p> 
<ul> 
 <li>支持完全类型检查的<code>GROUP BY</code></li> 
 <li>支持表别名</li> 
 <li>支持通过相应类型定义 select 子句</li> 
 <li>支持<code>UNION</code>/<code>INTERSECT</code>查询</li> 
</ul> 
<p>此外，Diesel 2.0.0 还修复了类级别(type level) SQL 表示中的几个问题，它现在可以正确处理以下情况：</p> 
<ul> 
 <li>混合嵌套<code>LEFT JOINS</code>和<code>INNER JOINS</code></li> 
 <li>通过<code>AND</code>,<code>OR</code>和类似的运算符链接混合的可空表达式 (nullable expressions)</li> 
</ul> 
<hr> 
<p><strong>支持<code>GROUP BY</code>子句</strong></p> 
<p>Diesel 2.0 添加了对<code>GROUP BY</code>子句的支持，用于 select 查询。</p> 
<p>示例</p> 
<pre><code class="language-sql"> users::table.inner_join(posts::table)
    .group_by(users::id)
    .select((users::name, count(posts::id)))</code></pre> 
<p><strong>支持表别名</strong></p> 
<p>以下查询展示了此功能：</p> 
<pre><code class="language-sql">// Define new table alias for the existing `users` table
let users1 = diesel::alias!(schema::users as user1);

// Use the corresponding alias inside any existing query
users::table
    .inner_join(users1.on(users::id).eq(users1.field(users::id))))
    .select((users::id, users::name, users1.field(users::name)))
    .order_by(users1.field(users::id))</code></pre> 
<p><strong>支持<code>UNION</code>/<code>INTERSECT</code>查询</strong></p> 
<p>此功能轻松地将多个查询链接在一起，只要它们返回相同类型的字段。</p> 
<pre><code class="language-sql"> users.select(user_name.nullable())
    .union(animals.select(animal_name).filter(animal_name.is_not_null()))</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdiesel-rs%2Fdiesel%2Freleases%2Ftag%2Fv2.0.0" target="_blank">Release Note</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdiesel.rs%2Fchangelog.html" target="_blank">Changelog</a></p>
                                        </div>
                                      
</div>
            