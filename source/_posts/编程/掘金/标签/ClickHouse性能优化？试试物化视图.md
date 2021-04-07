
---
title: 'ClickHouse性能优化？试试物化视图'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbd869f52842411d8d928946f9be611d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 16:55:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbd869f52842411d8d928946f9be611d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="mark" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbd869f52842411d8d928946f9be611d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、前言</h2>
<p>ClickHouse是一个用于联机分析(OLAP)的列式数据库管理系统(DBMS)；目前我们使用CH作为实时数仓用于统计分析，在做性能优化的时候使用了 <code>物化视图</code> 这一特性作为优化手段，本文主要分享物化视图的特性与如何使用它来优化ClickHouse的查询性能。</p>
<p> </p>
<h2 data-id="heading-1">二、概念</h2>
<p>数据库中的 <code>视图(View)</code> 指的是通过一张或多张表查询出来的 <strong>逻辑表</strong> ，本身只是一段 <strong>SQL</strong> 的封装并 <strong>不存储数据</strong>。</p>
<p>而 <code>物化视图(Materialized View)</code> 与普通视图不同的地方在于它是一个查询结果的数据库对象(持久化存储)，非常趋近于表；物化视图是数据库中的预计算逻辑+显式缓存，典型的空间换时间思路，所以用得好的话，它可以避免对基础表的频繁查询并复用结果，从而显著提升查询的性能。</p>
<p>在传统关系型数据库中，Oracle、PostgreSQL、SQL Server等都支持物化视图，而作为MPP数据库的ClickHouse也支持该特性。</p>
<p><img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98b22b6021144e02afcad722dfed6917~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h2 data-id="heading-2">三、ClickHouse物化视图</h2>
<p>ClickHouse中的物化视图可以挂接在任意引擎的基础表上，而且会自动更新数据，它可以借助 MergeTree 家族引擎(SummingMergeTree、Aggregatingmergetree等)，得到一个实时的预聚合，满足快速查询；但是对 <strong>更新</strong> 与 <strong>删除</strong> 操作支持并不好，更像是个插入触发器。</p>
<p>创建语法：</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">CREATE</span> [MATERIALIZED] <span class="hljs-keyword">VIEW</span> [IF <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">EXISTS</span>] [db.]table_name [<span class="hljs-keyword">TO</span>[db.]name] [ENGINE <span class="hljs-operator">=</span> engine] [POPULATE] <span class="hljs-keyword">AS</span> <span class="hljs-keyword">SELECT</span> ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>POPULATE 关键字决定了物化视图的更新策略：</p>
<ul>
<li>若有POPULATE 则在创建视图的过程会将源表已经存在的数据一并导入，类似于 create table ... as</li>
<li>若无POPULATE 则物化视图在创建之后没有数据</li>
</ul>
<blockquote>
<p>ClickHouse 官方并不推荐使用populated，因为在创建视图过程中插入表中的数据并不会写入视图，会造成数据的丢失。</p>
</blockquote>
<p> </p>
<h2 data-id="heading-3">四、案例</h2>
<h3 data-id="heading-4">4.1. 场景</h3>
<p>假设有一个日志表 <code>login_user_log</code> 来记录每次登录的用户信息，现在需要按用户所属地为维度来统计每天的登录次数。</p>
<blockquote>
<p><strong>PS</strong>：这种 <strong>只有新增记录</strong>，没有更新删除的记录表就非常适合使用 <code>物化视图</code> 来优化统计性能</p>
</blockquote>
<p> </p>
<p>正常的聚合SQL如下：city为用户所属地，login_date为登录时间</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">select</span> city, login_date, <span class="hljs-built_in">count</span>(<span class="hljs-number">1</span>) login_cnt
<span class="hljs-keyword">from</span> login_user_log
<span class="hljs-keyword">group</span> <span class="hljs-keyword">by</span> city, login_date
<span class="copy-code-btn">复制代码</span></code></pre>
<p>增加 <code>物化视图</code> 后的架构如下图所示：</p>
<p><img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e97aae74b7a40c08388464ee541fc8a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h3 data-id="heading-5">4.2. 建表</h3>
<p><strong>创建基础表</strong>：基础表使用 <code>SummingMergeTree</code> 引擎，进行预聚合处理</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">TABLE</span> login_user_log_base
(
    city String,
login_date <span class="hljs-type">Date</span>,
    login_cnt UInt32
)
ENGINE <span class="hljs-operator">=</span> SummingMergeTree()
<span class="hljs-keyword">ORDER</span> <span class="hljs-keyword">BY</span> (city, login_date)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>SummingMergeTree表引擎主要用于只关心聚合后的数据，而不关心明细数据的场景，它能够在合并分区的时候按照预先定义的条件聚合汇总数据，将同一分组下的多行数据汇总到一行，可以显著的 <strong>减少存储空间并加快数据查询的速度</strong>。</p>
</blockquote>
<p> </p>
<p><strong>创建物化视图</strong>：用户在创建物化视图时，通过 <code>AS SELECT ...</code> 子句从源表中查询需要的列，十分灵活</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">CREATE</span> MATERIALIZED <span class="hljs-keyword">VIEW</span> if <span class="hljs-keyword">not</span> <span class="hljs-keyword">exists</span> login_user_log_mv 
<span class="hljs-keyword">TO</span> login_user_log_base 
<span class="hljs-keyword">AS</span> 
<span class="hljs-keyword">SELECT</span> city, login_date, <span class="hljs-built_in">count</span>(<span class="hljs-number">1</span>) login_cnt
<span class="hljs-keyword">from</span> login_user_log
<span class="hljs-keyword">group</span> <span class="hljs-keyword">by</span> city, login_date
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>使用 <strong>TO</strong> 关键字关联 <code>物化视图</code> 与 <code>基础表</code>，需要自己初始化历史数据。</p>
</blockquote>
<p> </p>
<h3 data-id="heading-6">4.3. 查询统计结果</h3>
<p>使用物化视图查询</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">SELECT</span> city, login_date, <span class="hljs-built_in">sum</span>(login_cnt) cnt
<span class="hljs-keyword">from</span> login_user_log_mv
<span class="hljs-keyword">group</span> <span class="hljs-keyword">by</span> city, login_date
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>注意</strong>：在使用物化视图（SummingMergeTree引擎）的时候，也需要按照聚合查询来写sql，因为虽然 <code>SummingMergeTree</code> 会自己预聚合，但是并不是实时的，具体执行聚合的时机并 <strong>不可控</strong>。</p>
</blockquote>
<p> </p>
<h2 data-id="heading-7">总结</h2>
<ol>
<li>在创建 MV 表时，一定要使用 TO 关键字为 MV 表指定存储位置，否则不支持 <strong>嵌套视图</strong>(多个物化视图继续聚合一个新的视图)</li>
<li>在创建 MV 表时如果用到了多表联查，不能为连接表指定别名，如果多个连接表中存在同名字段，在连接表的查询语句中使用 AS 将字段名区分开</li>
<li>在创建 MV 表时如果用到了多表联查，只有当第一个查询的表有数据插入时，这个 MV 才会被触发</li>
<li>在创建 MV 表时不要使用 POPULATE 关键字，而是在 MV 表建好之后将数据手动导入 MV 表</li>
<li>在使用 MV 的聚合引擎时，也需要按照聚合查询来写sql，因为聚合时机不可控</li>
</ol>
<p> </p>
<p><strong>扫码关注有惊喜！</strong></p>
<p><img alt="陶陶技术笔记公众号二维码.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b50d99e30f3c4a0fb43e3336b5568078~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            