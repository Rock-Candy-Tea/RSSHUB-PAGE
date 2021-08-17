
---
title: '数据库 EAV 模型'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1c9c49a29524cd59b6eccf36b4232d7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 19:08:39 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1c9c49a29524cd59b6eccf36b4232d7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">举个🌰</h1>
<p>假设要做一个电商的商品管理，我们先卖一些衣服，需要管理衣服的尺码、颜色、款式等信息，有一天需要卖电脑了，电脑需要 主板、CPU、显卡、内存、硬盘、散热 等信息，过几天又需要卖手机了，手机有 颜色、版本、存储容量、套餐类型等等信息，数据库如何设计。</p>
<h2 data-id="heading-1">1. 新增字段</h2>
<p>每次新增商品，需要支持不同的信息的话就不停的加字段。</p>

































































<table><thead><tr><th><strong>ID</strong></th><th><strong>Name</strong></th><th><strong>尺码</strong></th><th><strong>颜色</strong></th><th><strong>款式</strong></th><th><strong>主板</strong></th><th><strong>CPU</strong></th><th><strong>显卡</strong></th><th><strong>内存</strong></th><th><strong>存储</strong></th><th><strong>散热</strong></th><th><strong>版本</strong></th><th><strong>套餐类型</strong></th></tr></thead><tbody><tr><td>1</td><td>T恤</td><td>M</td><td>白色</td><td>字节九周年</td><td>NULL</td><td>NULL</td><td>NULL</td><td>NULL</td><td>NULL</td><td>NULL</td><td>NULL</td><td>NULL</td></tr><tr><td>2</td><td>外星人电脑</td><td>NULL</td><td>NULL</td><td>NULL</td><td>A</td><td>i99</td><td>RTX8090</td><td>32G</td><td>2T</td><td>水冷</td><td>NULL</td><td>键鼠套装</td></tr><tr><td>3</td><td>香蕉手机</td><td>NULL</td><td>五彩斑斓黑</td><td>NULL</td><td>NULL</td><td>骁龙999</td><td>NULL</td><td>12G</td><td>512G</td><td>风扇</td><td>8s Pro Plus MAX</td><td>碎屏险套餐</td></tr></tbody></table>
<p>这样会造成以下问题：</p>
<ol>
<li>实现成本高，每次添加商品都需要进行前后端开发、调试，浪费时间和人力。</li>
</ol>

<ol>
<li>数据库的字段可能会越来越多，而很多字段大部分商品都是不需要的，需要设置为<code>NULL</code>，导致内存大量浪费。</li>
</ol>

<h2 data-id="heading-2">2. 预留字段</h2>
<p>给对应的表定义几个预留字段，然后这些预留字段在不同的商品可以重复使用。这样的话可以解决一部分的开发问题，大部分情况不需要开发，直接复用现有字段就可以。</p>

















































<table><thead><tr><th><strong>ID</strong></th><th><strong>Name</strong></th><th><strong>Ext1</strong></th><th><strong>Ext2</strong></th><th><strong>Ext3</strong></th><th><strong>Ext4</strong></th><th><strong>Ext5</strong></th><th><strong>Ext6</strong></th><th><strong>Ext7</strong></th></tr></thead><tbody><tr><td>1</td><td>T恤</td><td>M</td><td>白色</td><td>字节九周年</td><td>NULL</td><td>NULL</td><td>NULL</td><td>NULL</td></tr><tr><td>2</td><td>外星人电脑</td><td>A</td><td>RTX8090</td><td>i99</td><td>32G</td><td>2T</td><td>水冷</td><td>键鼠套装</td></tr><tr><td>3</td><td>香蕉手机</td><td>8s Pro Plus MAX</td><td>五彩斑斓黑</td><td>骁龙999</td><td>12G</td><td>512G</td><td>风扇</td><td>碎屏险套餐</td></tr></tbody></table>
<p>但是这样也有很多问题：</p>
<ol>
<li>字段一样，但是含义不一样，需要前端做大量适配。</li>
</ol>

<ol start="2">
<li>字段的类型可能不一样，预留字段还得考虑不同的类型。</li>
</ol>

<ol start="3">
<li>预留字段太少了作用有限，太多了和新增字段一样会有存储和性能问题。</li>
</ol>

<ol start="4">
<li>扩展字段是公用的，不能根据字段名顾名思义，得在启用时维护对应关系，使用时查找对应关系。</li>
</ol>

<ol start="5">
<li>扩展字段的数量无法精确定义。</li>
</ol>
<h2 data-id="heading-3">3. JSON_OBJECT</h2>
<p>这种情况下有一种简单的解决方案，就是设计一个 <code>extra</code> 字段，类型为 JSON，然后把 尺码、颜色、款色、主板、CPU、显卡、内存等等都放到 JSON 里。</p>

























<table><thead><tr><th><strong>ID</strong></th><th><strong>Name</strong></th><th><strong>Extra</strong></th></tr></thead><tbody><tr><td>1</td><td>T恤</td><td><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1c9c49a29524cd59b6eccf36b4232d7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></td></tr><tr><td>2</td><td>外星人电脑</td><td><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac7d29cf38874e60b34f56d79f0a58f6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></td></tr><tr><td>3</td><td>香蕉手机</td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b74925f31ea4af2bcf60ad36a58c9d0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></td></tr></tbody></table>
<p>但是 JSON 有以下几个问题：</p>
<ol>
<li>JSON 数据仅仅只能用于展示，如果用于条件查询、数据更新其效率是很低的。查询时需要遍历表解析 JSON。</li>
</ol>

<ol start="2">
<li>虽然 MySQL 支持了 JSON 类型，但 MySQL 作为关系型数据库，对标准化的 column-per-value 支持更好，包括数据类型限制、长度限制，唯一索引限制，查询索引优化，外键关联，关联查询支持，运算支持等，这些都是 JSON 中 Key 无法达到的。</li>
</ol>

<ol start="3">
<li>将常用的查询字段从 JSON 数据中剥离出来形成单独的字段，虽然可以改善查询问题，但需要有先见之明，如果后期进行剥离就会涉及代码修改和数据迁移，遇到多版本的话，还可能出现数据冗余的问题，处理不好还会出现数据不一致问题，并不仅仅这么简单，一定慎用。</li>
</ol>

<ol start="4">
<li>大 JSON 的解析性能较差。</li>
</ol>

<ol start="5">
<li>每条数据都需要同时保存 Key 和 Value，对于中文数据，纯 JSON 太占空间了。</li>
</ol>
<p>基于以上几个原因，在一些复杂的情况下，不建议使用 JSON 存数据。</p>
<p>以上三种都不是理想的解决方案，后续经过不断的经验积累，有人提出来了 EAV 模型，可以在一定程度上解决以上问题。</p>
<h1 data-id="heading-4">什么是 EAV 模型</h1>
<p>Entity-Attribute-Value (<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FEntity%25E2%2580%2593attribute%25E2%2580%2593value_model" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model" ref="nofollow noopener noreferrer">wiki</a>)是一种数据库模型，用于以节省空间的方式对实体进行编码。</p>
<ul>
<li>Entity：实体，代表一个业务对象，比如上面的例子里的商品。</li>
</ul>

<ul>
<li>Attribute：对象的属性，属性并不是作为实体单独的一列来进行存放，而是存储在一组单独的数据库表中。</li>
</ul>

<ul>
<li>Value：指特定属性所关联的值。</li>
</ul>
<h2 data-id="heading-5">几个概念</h2>
<h3 data-id="heading-6"><strong>稀疏属性（Sparseness of Attributes）</strong></h3>
<p>在数学和计算机科学中，如果一个对象仅包含大量潜在属性中的几个属性，称之为“<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E7%25A8%2580%25E7%2596%258F%25E7%259F%25A9%25E9%2598%25B5" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E7%A8%80%E7%96%8F%E7%9F%A9%E9%98%B5" ref="nofollow noopener noreferrer">稀疏矩阵</a>”。在讨论EAV 时，采用“稀疏”来描述大多数无值的属性。如上文中的主板、CPU、显卡等属性。</p>
<h3 data-id="heading-7">行模型（Row Modeling）</h3>
<p>基于行模型的表，其描述实体的数据记录为多行，每组新的数据在数据库中存为额外的行而非额外的列。行模型是数据库设计的标准数据建模技术，它仅适用于满足如下两个条件的情况：</p>
<ul>
<li>特定实体的数据是稀疏的。</li>
</ul>

<ul>
<li>数据是经常变动的。</li>
</ul>
<p>行模型是不适用于稀疏且数据非波动的情形，此时，应采用传统的列模型。</p>
<h2 data-id="heading-8">EAV 与行模型</h2>
<p>EAV 模型是行模型的泛化。行模型的表的数据是均匀的，这意味着整个数据库所有类型的数据存储在一张表中；此外，行模型表中值列的数据类型是预先确定的。而在 EAV表中，特定行其值的数据类型由对应的属性确定。</p>
<p>选择数据模型的最佳方法是很难的，但作为一个准则，如满足如下条件时使用EAV模型而非行模型：</p>
<ul>
<li>数据记录中的单个属性的数据类型不同；采用行模型时一张表中很难存储不同类型的值。</li>
</ul>

<ul>
<li>需要表示多种类型的数据，其数量可能出现波动。与此同时，即使不稀疏的属性，然每类数据都非常少。这种情况下，传统的数据模型将使成百的表却只有几行数据。</li>
</ul>

<ul>
<li>在一定的环境中，其属性必须动态创建，某些类在原型随后的周期中常常会被省略。</li>
</ul>

<ul>
<li>某些实体有混合型的属性，这意味着一些属性是非稀疏的，而其他属性则是高度稀疏的。在这种情况下，非稀疏属性存储在传统表中，而稀疏的属性存储在EAV或行建模的格式。</li>
</ul>
<h1 data-id="heading-9">表结构设计</h1>
<h2 data-id="heading-10">方案一：行模型</h2>
<p>先来一个简单的方案，使用行建模的方式。商品作为实体存入 Goods 表中，其余的属性和值存入商品属性表 Attribute 中。</p>
<p><strong>商品表（Goods）</strong></p>





















<table><thead><tr><th><strong>GoodsID</strong></th><th><strong>Name</strong></th></tr></thead><tbody><tr><td>1</td><td>T恤</td></tr><tr><td>2</td><td>外星人电脑</td></tr><tr><td>3</td><td>香蕉手机</td></tr></tbody></table>
<p><strong>商品属性表（Attribute）</strong></p>































































































<table><thead><tr><th><strong>GoodsID</strong></th><th><strong>Attribute</strong></th><th><strong>Value</strong></th></tr></thead><tbody><tr><td>1</td><td>尺码</td><td>M</td></tr><tr><td>1</td><td>颜色</td><td>白色</td></tr><tr><td>1</td><td>款式</td><td>字节九周年</td></tr><tr><td>2</td><td>主板</td><td>A</td></tr><tr><td>2</td><td>CPU</td><td>i99</td></tr><tr><td>2</td><td>显卡</td><td>RTX8090</td></tr><tr><td>2</td><td>内存</td><td>32G</td></tr><tr><td>2</td><td>存储</td><td>2T</td></tr><tr><td>2</td><td>散热</td><td>水冷</td></tr><tr><td>2</td><td>套餐类型</td><td>键鼠套装</td></tr><tr><td>3</td><td>颜色</td><td>五彩斑斓黑</td></tr><tr><td>3</td><td>CPU</td><td>骁龙999</td></tr><tr><td>3</td><td>内存</td><td>12G</td></tr><tr><td>3</td><td>存储</td><td>512G</td></tr><tr><td>3</td><td>散热</td><td>风扇</td></tr><tr><td>3</td><td>版本</td><td>8s Pro Plus MAX</td></tr><tr><td>3</td><td>套餐类型</td><td>碎屏险套餐</td></tr></tbody></table>
<p>上面这个方案是行模型的方案，通过这种方式我们可以无限的扩展商品的属性。这种方案比较适用于每个实体的属性都不固定的情况。</p>
<p>但是这种方案有以下几个问题：</p>
<ol>
<li>每条数据都需要同时保存 Key 和 Value，对于中文数据，Key 有限，行无限的情况下，会浪费大量空间，性能也比较差。</li>
</ol>

<ol>
<li>Value 没有类型限制，都是 VARCHAR 的，对数据库不友好，会导致内存浪费，而且存取都需要进行数据格式转换。对存储为字符串的值创建的索引不允许针对数值型和日期型的搜索范围优化，这是采用混合数据类型的键-值对描述数据的公共问题。</li>
</ol>
<h2 data-id="heading-11">方案二：简单 EAV</h2>
<p>针对方案一的第一个问题进行优化。</p>
<p>商品表保持不变。商品属性表拆分为属性表和值表。</p>
<p><strong>属性表（Attribute）</strong></p>





















































<table><thead><tr><th><strong>AttributeID</strong></th><th><strong>Name</strong></th></tr></thead><tbody><tr><td>1</td><td>颜色</td></tr><tr><td>2</td><td>尺码</td></tr><tr><td>3</td><td>款式</td></tr><tr><td>4</td><td>主板</td></tr><tr><td>5</td><td>CPU</td></tr><tr><td>6</td><td>显卡</td></tr><tr><td>7</td><td>内存</td></tr><tr><td>8</td><td>存储</td></tr><tr><td>9</td><td>散热</td></tr><tr><td>10</td><td>版本</td></tr><tr><td>11</td><td>套餐类型</td></tr></tbody></table>
<p><strong>值表（Value）</strong></p>































































































<table><thead><tr><th><strong>GoodsID</strong></th><th><strong>AttributeID</strong></th><th><strong>Value</strong></th></tr></thead><tbody><tr><td>1</td><td>2</td><td>M</td></tr><tr><td>1</td><td>1</td><td>白色</td></tr><tr><td>1</td><td>3</td><td>字节九周年</td></tr><tr><td>2</td><td>4</td><td>A</td></tr><tr><td>2</td><td>5</td><td>i99</td></tr><tr><td>2</td><td>6</td><td>RTX8090</td></tr><tr><td>2</td><td>7</td><td>32G</td></tr><tr><td>2</td><td>8</td><td>2T</td></tr><tr><td>2</td><td>9</td><td>水冷</td></tr><tr><td>2</td><td>11</td><td>键鼠套装</td></tr><tr><td>3</td><td>1</td><td>五彩斑斓黑</td></tr><tr><td>3</td><td>5</td><td>骁龙999</td></tr><tr><td>3</td><td>7</td><td>12G</td></tr><tr><td>3</td><td>8</td><td>512G</td></tr><tr><td>3</td><td>9</td><td>风扇</td></tr><tr><td>3</td><td>10</td><td>8s Pro Plus MAX</td></tr><tr><td>3</td><td>11</td><td>碎屏险套餐</td></tr></tbody></table>
<p>这样属性都保存在属性表里，每个属性值都保存在值表里，同时与商品表和属性表做关联，这样就可以大大节省内存。</p>
<h2 data-id="heading-12">方案三：优化 EAV</h2>
<p>为了解决方案一的第二个问题，则需要对值表基于数据类型进行分割，每个不同的数据类型拆为一个单独的表，同时通过 属性表（Attribute） 添加 类型决定去哪里存取数据。</p>
<p><strong>属性表（Attribute）</strong></p>

































































<table><thead><tr><th><strong>AttributeID</strong></th><th><strong>Name</strong></th><th><strong>Type</strong></th></tr></thead><tbody><tr><td>1</td><td>颜色</td><td>VARCHAR</td></tr><tr><td>2</td><td>尺码</td><td>INT</td></tr><tr><td>3</td><td>款式</td><td>INT</td></tr><tr><td>4</td><td>主板</td><td>VARCHAR</td></tr><tr><td>5</td><td>CPU</td><td>INT</td></tr><tr><td>6</td><td>显卡</td><td>INT</td></tr><tr><td>7</td><td>内存</td><td>INT</td></tr><tr><td>8</td><td>存储</td><td>INT</td></tr><tr><td>9</td><td>散热</td><td>VARCHAR</td></tr><tr><td>10</td><td>版本</td><td>TEXT</td></tr><tr><td>11</td><td>套餐类型</td><td>VARCHAR</td></tr></tbody></table>
<p><strong>值表</strong></p>
<p>eav_int</p>























































<table><thead><tr><th><strong>GoodsID</strong></th><th><strong>AttributeID</strong></th><th><strong>Value(INT)</strong></th></tr></thead><tbody><tr><td>1</td><td>2</td><td>2(M)</td></tr><tr><td>1</td><td>3</td><td>1(字节九周年)</td></tr><tr><td>2</td><td>5</td><td>99(i99)</td></tr><tr><td>2</td><td>6</td><td>8090(RTX8090)</td></tr><tr><td>2</td><td>7</td><td>32(32G)</td></tr><tr><td>2</td><td>8</td><td>2048(2T)</td></tr><tr><td>3</td><td>5</td><td>999(骁龙999)</td></tr><tr><td>3</td><td>7</td><td>12(12G)</td></tr><tr><td>3</td><td>8</td><td>512(512G)</td></tr></tbody></table>
<p>eav_varchar</p>








































<table><thead><tr><th><strong>GoodsID</strong></th><th><strong>AttributeID</strong></th><th><strong>Value(VARCHAR)</strong></th></tr></thead><tbody><tr><td>1</td><td>1</td><td>白色</td></tr><tr><td>2</td><td>4</td><td>A</td></tr><tr><td>3</td><td>1</td><td>五彩斑斓黑</td></tr><tr><td>3</td><td>9</td><td>风扇</td></tr><tr><td>3</td><td>11</td><td>碎屏险套餐</td></tr><tr><td>2</td><td>11</td><td>键鼠套装</td></tr></tbody></table>
<p>eav_text</p>















<table><thead><tr><th><strong>GoodsID</strong></th><th><strong>AttributeID</strong></th><th><strong>Value(TEXT)</strong></th></tr></thead><tbody><tr><td>3</td><td>10</td><td>8s Pro Plus MAX</td></tr></tbody></table>
<p>这种就是比较标准的 EAV 模型。解决了方案一的两个问题。</p>
<h1 data-id="heading-13"><strong>EAV 的优/缺点</strong></h1>
<h2 data-id="heading-14">优点</h2>
<p>EAV模型的主要优点是其灵活性。属性描述表不限制数量，这意味着每次新增属性不需要重新设计数据结构；扩展数据库时，属性的数量可以垂直增加，而无需改变数据结构。</p>
<p>EAV只处理非空属性，不需要为空值保留额外的存储空间。这使得EAV模型相当节省空间。</p>
<p>物理数据格式是非常干净，类似于JSON/XML，很容易将数据映射为JSON/XML格式。</p>
<p>EAV模型可以极好地迅速扩展应用，因为它可以防止(属性)不断变化的后果。可以简单地记录任何结构的新数据，而不需要修改任何数据结构。</p>
<h2 data-id="heading-15">缺点</h2>
<p>当考虑EAV时，确定数据是否稀疏和数据量非常重要，因为采用不恰当的数据集时，EAV设计的复杂性超过了其优势所在。相对静态或简单数据选用传统的表结构更为合适。</p>
<p>相较于传统的数据结构，EAV的一个主要缺点是它在检索大容量数据时效率较低。在EAV模型中，数据更加分散，所以查询一个完整实体的记录需要多个表JOIN查询。更重要的是，当EAV模型应用于大数据量时，对于同一组EAV建模的数据描述，需要短暂或永久地在进行矩阵转积处理(Pivoting)(行列转换)。该操作易于出错且是CPU密集型的任务。</p>
<p>EAV模型的另一个局限性，需要制定额外的逻辑来完成传统数据结构下自动进行的事务。但是，利用现有的EAV工具可以降低此类工作的成本。</p>
<p>最后，理解EAV模型确实需要时间。它有一个明确的学习曲线，使的初级开发人员在真正理解其概念前，需要为此付出更多的精力。</p>
<h1 data-id="heading-16">结论</h1>
<p>应用 EAV 模型时，应考虑以下条件：</p>
<ul>
<li>数据是稀疏的、异构的，一个实体的属性范围较广，且常引入新的属性。</li>
</ul>

<ul>
<li>数据量非常大，有许多不同类型的数据，即使属性是非稀疏的。</li>
</ul>

<ul>
<li>有许多混合属性，既具有稀疏也具有非稀疏属性。通常情况下，并不是所有的数据类满足EAV建模的要求。</li>
</ul>
<p>在实际在生产环境中，往往采用混合模式（mixed schema），包括传统的关系、EAV或合适的混合方法。</p>
<h1 data-id="heading-17">参考</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Finviqa.com%2Fblog%2Funderstanding-eav-data-model-and-when-use-it" target="_blank" rel="nofollow noopener noreferrer" title="https://inviqa.com/blog/understanding-eav-data-model-and-when-use-it" ref="nofollow noopener noreferrer">Understanding the EAV data model and when to use it</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Falanhou.org%2Fentity-attribute-value-model%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://alanhou.org/entity-attribute-value-model/" ref="nofollow noopener noreferrer">实体-属性-值(EAV)模型 | Alan Hou的个人博客</a></p></div>  
</div>
            