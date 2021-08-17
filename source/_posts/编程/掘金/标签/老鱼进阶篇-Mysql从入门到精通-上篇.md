
---
title: '老鱼进阶篇-Mysql从入门到精通-上篇'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://www.pianshen.com/images/675/89f7ef8d94ade21729c0661d35efa81b.JPEG'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 03:05:43 GMT
thumbnail: 'https://www.pianshen.com/images/675/89f7ef8d94ade21729c0661d35efa81b.JPEG'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6996982426086047781" title="https://juejin.cn/post/6996982426086047781" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">1、Mysql 体系架构图</h1>
<p><img src="https://www.pianshen.com/images/675/89f7ef8d94ade21729c0661d35efa81b.JPEG" alt="mysql架构体系" loading="lazy" referrerpolicy="no-referrer"></p>

























<table><thead><tr><th>中文名称</th><th>英文概述</th><th>功能描述</th></tr></thead><tbody><tr><td>连接层</td><td>Connectors</td><td>客户端连接到mysql，都需要经过连接器连接到默认mysql的3306端口，连接器一直处于监听状态，主要用于接收用户的请求。max_connections 代表设置的最大连接数，生产环境一般设置为1000-2000</td></tr><tr><td>服务层</td><td>Server</td><td>主要分为Sql接口、解析器Parser、Optimizer优化器、Cache和Buffer查询缓存、以及系统管理和控制工具</td></tr><tr><td>存储引擎层</td><td>Storage Engin</td><td>主要分为MyISAM、InnoDB等，存储引擎具有可插拔的特点，因为存储引擎不是针对于数据的，而是针对于具体的数据库表的</td></tr></tbody></table>
<h1 data-id="heading-1">2、Mysql 查询执行流程</h1>
<h2 data-id="heading-2">2.1 流程图</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bc46abac6d04e9c95c2456a00c8227f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210811201602234.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">2.2 连接器建立连接</h2>
<p>第一步，先连接到这个数据库上，这时候接待的就是连接器。连接器负责跟客户端建立连接、获取权限、维持和管理连接。</p>
<h2 data-id="heading-4">2.3 查询缓存</h2>
<p>第二步，如果查询sql和上次完全相同（多一个空格等都会认为不相同），则通缓存进行数据获取数据，但是缓存一般失效非常频繁，表结构变动、数据更新都会导致缓存失效。</p>
<p>因此，mysql不建议使用查询缓存，原因是利大于弊。</p>
<h2 data-id="heading-5">2.4 解析器进行sql解析</h2>
<p>第三步，解析器进行词法分析，把一个完成的sql语句分割成一个个的字符串；然后进行语法分析，判定语法是否合法有效；然后会根据mysql定义的语法规则，根据sql生成一个解析树，如下所示：</p>
<p><img alt="image-20210811202531618" src="https://juejin.cn/post/6996982426086047781" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">2.5 预处理器进行解析树合法检查</h2>
<p>第四步，预处理器则会进一步去检查解析树是否合法，比如表名是否存在，语句中表的列是否存在等，在这一步MySQL会检验用户是否有表的操作权限。预处理之后会得到一个新的解析树。</p>
<h2 data-id="heading-7">2.6 优化器执行sql优化处理</h2>
<p>第五步，查询优化器根据生成的解析树最终生成不同的执行计划，然后选择最优的执行计划，mysql内部使用的基于成本模型的优化器，执行计划所需成本越少则越优先。优化器所做的处理功能部分如下：多个索引存在时决定使用那个索引；存在多表关联时，决定表的连接顺序，确定基准表。</p>
<h2 data-id="heading-8">2.7 根据执行计划执行sql语句</h2>
<p>第六步，执行器根据执行计划，进行sql语句的执行，主要是根据存储引擎定义的接口，去获取数据。在获取数据之前会检查用户的权限。</p>
<h1 data-id="heading-9">3、Mysql 存储引擎</h1>





















































<table><thead><tr><th>存储引擎</th><th>描述</th></tr></thead><tbody><tr><td>MyISAM</td><td>5.5版本之前MySQL的默认数据库，高速引擎，拥有较高的插入，查询速度，但不支持事务，行锁，外键</td></tr><tr><td>InnoDB</td><td>5.5版本后MySQL的默认数据库，支持事务和行级锁定，比MyISAM处理速度稍慢</td></tr><tr><td>ISAM</td><td>Indexed Sequential Access Method。MyISAM的前身，MySQL5.0以后不再默认安装</td></tr><tr><td>Memory</td><td>内存存储引擎，拥有极高的插入，更新和查询效率。但是会占用和数据量成正比的内存空间。只在内存上保存数据，意味着数据可能会丢失</td></tr><tr><td>CSV</td><td>CSV 存储引擎是基于 CSV 格式文件存储数据(应用于跨平台的数据交换)</td></tr><tr><td>Falcon</td><td>一种新的存储引擎，支持事物处理，传言可能是InnoDB的替代者</td></tr><tr><td>Archive</td><td>用于数据存档。将数据压缩后进行存储，非常适合存储大量的独立的，作为历史记录的数据，但是只能进行插入和查询操作</td></tr><tr><td>MRG_MyISAM（MERGE）</td><td>将多个表联合成一个表使用，在超大规模数据存储时很有用</td></tr><tr><td>BLACKHOLE</td><td>丢弃写操作，读操作会返回空内容</td></tr><tr><td>FEDERATED</td><td>用来访问远程表</td></tr><tr><td>NDB</td><td>MySQL集群专用存储引擎</td></tr></tbody></table>
<h1 data-id="heading-10">4、Mysql 索引</h1>
<h2 data-id="heading-11">4.1 索引分类</h2>
<h3 data-id="heading-12">4.1.1 按照使用类型划分</h3>
<ul>
<li><strong>主键索引</strong>：索引列的值必须是唯一的，不允许为空值，常使用主键字段</li>
<li><strong>普通索引</strong>：索引列的值没有任何限制，可以重复也可以为空</li>
<li><strong>唯一索引</strong>：索引列的值是唯一的，但是可以允许空值</li>
<li><strong>全文索引</strong>：文本类型字段CHAR、VARCHAR、TEXT才可以使用，推荐在数据量少或者并发度低的时候使用，否则可以选型es、lucene等</li>
</ul>
<h3 data-id="heading-13">4.1.2 按照索引列数量划分</h3>
<ul>
<li><strong>单列索引</strong>: 建立的索引只有一个列</li>
<li><strong>组合索引</strong>: 建立的索引使用2个以上的字段，组合索引的使用时需要遵从最左前缀原则，一般情况下建议使用组合索引代替单列索引（主键索引除外），因为更省空间</li>
</ul>
<h2 data-id="heading-14">4.2 索引存储及特点</h2>
<p>表中的数据是存储在磁盘文件上的，MySQL在处理数据时，需要先把数据从磁盘上读取到内存中。一个硬盘一般由多个盘片组成，盘片的数量一般都在5片以内。</p>
<p>磁盘的工作机制，决定了它读取数据的速度。读写一次磁盘信息所需的时间可分解为：<strong>寻道时间、延迟时间、传输时间</strong>。磁盘读取数据花费的时间，是这三个操作步骤所需时间之和。</p>
<p>MySQL本质上是一个软件，MySQL需要读取数据时，MySQL会调用操作系统的接口，操作系统会调用磁盘的驱动程序将数据读取到内核空间，然后将数据从内核空间copy到用户空间，随后MySQL就能从用户空间中读取到数据。<strong>操作系统读取磁盘时，Linux读取的最小单位一般为4K</strong>。最小单位由操作系统决定，不同的操作系统可能会有所不同。</p>
<p><strong>MySQL的InnoDB存储引擎的数据读取以页为单位，也大小由参数innodb_page_size控制，默认值是16k。</strong></p>
<h2 data-id="heading-15">4.3 索引的数据结构</h2>
<h3 data-id="heading-16">4.3.1 Hash表</h3>
<p>Hash表，Java中的HashMap，TreeMap就是Hash表结构，以键值对的方式存储数据。我们使用Hash表存储表数据Key可以存储索引列，Value可以存储行记录或者行磁盘地址。</p>
<p>Hash表在等值查询时效率很高，时间复杂度为O(1)；但是不支持范围快速查找，范围查找时还是只能通过扫描全表方式。</p>
<h3 data-id="heading-17">4.3.2 二叉树</h3>
<p>二叉树特点：每个节点最多有2个分叉，左子树和右子树数据顺序左小右大，二叉树的检索复杂度和树高相关，而且主键索引会存在单向链表结构的特殊情况。</p>
<h3 data-id="heading-18">4.3.3 平衡二叉树</h3>
<p>树的左右两个子树的层级最多相差1。在插入删除数据时通过左旋/右旋操作保持二叉树的平衡，不会出现左子树很高、右子树很矮的情况。使用平衡二叉查找树查询的性能接近于二分查找法，时间复杂度是 O(log2n)。</p>
<p>存在问题：</p>
<ul>
<li>时间复杂度和树高相关。树有多高就需要检索多少次</li>
<li>平衡二叉树不支持范围查询快速查找，范围查询时需要从根节点多次遍历，查询效率不高</li>
</ul>
<h3 data-id="heading-19">4.3.4 B树</h3>
<p>假如key为bigint=8字节，每个节点有两个指针，每个指针为4个字节，一个节点占用的空间16个字节（8+4*2=16）。</p>
<p>在每个节点存储多个元素，在每个节点尽可能多的存储数据。每个节点可以存储1000个索引（16k/16=1000），这样就将二叉树改造成了多叉树，通过增加树的叉树，将树从高瘦变为矮胖。构建1百万条数据，树的高度只需要2层就可以（1000*1000=1百万）。</p>
<p><strong>B树是一种多叉平衡查找树，主要特点是：</strong></p>
<ul>
<li>B树的节点中存储着多个元素，每个内节点有多个分叉</li>
<li>节点中的元素包含键值和数据，节点中的键值从大到小排列。也就是说，在所有的节点都储存数据。</li>
<li>父节点当中的元素不会出现在子节点中</li>
<li>所有的叶子结点都位于同一层，叶节点具有相同的深度，叶节点之间没有指针</li>
</ul>
<p><strong>B树的缺点：</strong></p>
<ul>
<li>B树不支持范围查询的快速查找，如果我们想要查找区间的数据，查找到起始值之后，需要回到根节点重新遍历查找，需要从根节点进行多次遍历，查询效率有待提高。</li>
<li>如果data存储的是行记录，行的大小随着列数的增多，所占空间会变大。这时，一个页中可存储的数据量就会变少，树相应就会变高，磁盘IO次数就会变大。</li>
</ul>
<h3 data-id="heading-20">4.3.5 B+树</h3>
<p><strong>只有叶子节点才会存储数据，非叶子节点只存储键值</strong>。叶子节点之间使用双向指针连接，最底层 的叶子节点形成了一个双向有序链表。</p>
<p><strong>B+树可以保证等值和范围查询的快速查找</strong>。</p>
<h2 data-id="heading-21">4.4 索引条件下推ICP</h2>
<p>Index Condition Pushdown, 简称ICP, 主要是mysql一种优化手段，主要用于使用索引从表中检索行的情况。可以通过参数optimizer_switch控制ICP的开始和关闭。</p>
<p>ICP的主要目的是为了减少回表查询的次数，可用于InnoDB和MyISAM引擎，对于前者仅用于辅助索引。</p>
<p><strong>总结</strong>：</p>
<p>1、不实用ICP时，满足最左前缀的索引条件是在存储引擎层进行比较的，非索引条件是在Server层进行过滤的。</p>
<p>2、使用ICP时，所有的索引条件的比较都是在存储引擎层比较的，非索引条件的比较是在Server层进行过滤的。</p>
<p><strong>对比使用ICP和不使用ICP，可以看到使用ICP可以有效减少回表查询次数和返回给服务层的记录数，从而减少了磁盘IO次数和服务层与存储引擎的交互次数。</strong></p>
<h2 data-id="heading-22">4.5 覆盖索引</h2>
<p>主要是通过查询时查询列都在索引列中，保证从索引查询时都是执行的数据获取，不再进行单独的回表查询，减少回表次数和IO次数，加快查询速度。</p>
<h2 data-id="heading-23">4.6 索引失效分析</h2>
<ul>
<li>不满足索引的最左前缀原则，或者在索引条件上使用<>, != 等判定，从第一个判定条件开始不走索引</li>
<li>在索引列上使用操作函数</li>
<li>使用is null, is not null查询条件无法走索引</li>
<li>字符串查询时不添加引号</li>
<li>like 模糊匹配时使用'%xxxx%'时无法走索引</li>
<li>尽量使用覆盖索引，减少select *</li>
<li>少用or进行条件查询连接，会导致索引失效</li>
<li>多使用全值匹配索引查询</li>
</ul>
<h1 data-id="heading-24">5、explain查询执行计划说明</h1>
<h3 data-id="heading-25">5.1 select_type</h3>
<ul>
<li>
<p><strong>simple</strong></p>
<p>表示不需要union操作或者不包含子查询的简单select查询。有连接查询时，外层的查询为simple，且只有一个。</p>
</li>
<li>
<p><strong>primary</strong></p>
<p>一个需要union操作或者含有子查询的select，位于最外层的单位查询的select_type即为primary，且只有一个。</p>
</li>
<li>
<p><strong>union</strong></p>
<p>union连接的两个select查询，第一个查询是dervied派生表，除了第一个表外，第二个以后的表select_type都是union。</p>
</li>
<li>
<p><strong>dependent union</strong></p>
<p>与union一样，出现在union 或union all语句中，但是这个查询要受到外部查询的影响</p>
</li>
<li>
<p><strong>union result</strong></p>
<p>包含union的结果集，在union和union all语句中,因为它不需要参与查询，所以id字段为null</p>
</li>
<li>
<p><strong>subquery</strong></p>
<p>除了from字句中包含的子查询外，其他地方出现的子查询都可能是subquery</p>
</li>
<li>
<p><strong>dependent subquery</strong></p>
<p>与dependent union类似，表示这个subquery的查询要受到外部表查询的影响</p>
</li>
<li>
<p><strong>derived</strong></p>
<p>from字句中出现的子查询，也叫做派生表，其他数据库中可能叫做内联视图或嵌套select</p>
</li>
</ul>
<h3 data-id="heading-26">5.2 type</h3>
<ul>
<li>
<p><strong>system</strong></p>
<p>表中只有一行数据或者是空表。</p>
</li>
<li>
<p><strong>const</strong></p>
<p>使用唯一索引或者主键，返回记录一定是1行记录的等值where条件时，通常type是const。其他数据库也叫做唯一索引扫描。</p>
</li>
<li>
<p><strong>eq_ref</strong></p>
<p>用于多表关联的等值连接情况下，并且等值连接的两个是主键或者唯一索引。此类型通常出现在多表的 join 查询, 表示对于前表的每一个结果, 都只能匹配到后表的一行结果. 并且查询的比较操作通常是 = , 查询效率较高。</p>
</li>
<li>
<p><strong>ref</strong></p>
<p>用于多表关联的等值连接情况下，并且等值连接的是非唯一索引，或者使用的是最左前缀规则的索引查询。</p>
</li>
<li>
<p><strong>fulltext</strong></p>
<p>全文索引检索，要注意，全文索引的优先级很高，若全文索引和普通索引同时存在时，mysql不管代价，优先选择使用全文索引</p>
</li>
<li>
<p><strong>ref_or_null</strong></p>
<p>与ref方法类似，只是增加了null值的比较。实际用的不多。</p>
</li>
<li>
<p><strong>unique_subquery</strong></p>
<p>用于where中的in形式子查询，子查询返回不重复值唯一值</p>
</li>
<li>
<p><strong>index_subquery</strong></p>
<p>用于in形式子查询使用到了辅助索引或者in常数列表，子查询可能返回重复值，可以使用索引将子查询去重。</p>
</li>
<li>
<p><strong>range</strong></p>
<p>索引范围扫描，常见于使用>,<,is null,between ,in ,like等运算符的查询中。</p>
</li>
<li>
<p><strong>index_merge</strong></p>
<p>表示查询使用了两个以上的索引，最后取交集或者并集，常见and ，or的条件使用了不同的索引，官方排序这个在ref_or_null之后，但是实际上由于要读取多个索引，性能可能大部分时间都不如range。</p>
</li>
<li>
<p><strong>index</strong></p>
<p>select结果列中使用到了索引，type会显示为index。全部索引扫描，把索引从头到尾扫一遍，常见于使用索引列就可以处理不需要读取数据文件的查询、可以使用索引排序或者分组的查询。</p>
</li>
<li>
<p><strong>all</strong></p>
<p>这个就是全表扫描数据文件，然后再在server层进行过滤返回符合要求的记录。</p>
</li>
</ul>
<h3 data-id="heading-27">5.3 extra</h3>
<ul>
<li>
<p><strong>using index</strong></p>
<p>查询时不需要回表查询，直接通过索引就可以获取查询的结果数据。表示相应的SELECT查询中使用到了覆盖索引（Covering Index），避免访问表的数据行，效率不错！</p>
<p>如果同时出现Using Where ，说明索引被用来执行查找索引键值。如果没有同时出现则代表索引用来读取数据而非执行查找动作。</p>
</li>
<li>
<p><strong>using where</strong></p>
<p>表示mysql将对storage engine提取的结果进行过滤，过滤条件字段无索引。</p>
</li>
<li>
<p><strong>using index condition</strong></p>
<p>表明使用了ICP索引条件下推。</p>
</li>
<li>
<p><strong>using filesort</strong></p>
<p>排序时无法使用到索引时，就会出现这个。常见于order by和group by语句中。说明mysql会使用一个外部的索引排序，而不是按照索引顺序进行读取，mysql中无法利用索引完成的排序操作称为“文件排序”。</p>
</li>
<li>
<p><strong>using temporary</strong></p>
<p>表示mysql在对查询结果order by和group by时表使用了临时表存储中间结果。</p>
</li>
<li>
<p><strong>distinct</strong></p>
<p>在select部分使用了distinct关键字 （索引字段）</p>
</li>
<li>
<p><strong>no tables used</strong></p>
<p>不带from字句的查询或者from dual查询。</p>
<p>使用not in()形式子查询或not exists运算符的连接查询，这种叫做反连接。即一般连接查询是先查询内表，再查询外表，反连接就是先查询外表，再查询内表。</p>
</li>
</ul>
<h1 data-id="heading-28">6、Mysql 锁简介</h1>
<h2 data-id="heading-29">6.1 锁的划分</h2>
<h3 data-id="heading-30">6.1.1 按粒度划分</h3>
<ul>
<li>
<p>全局锁：锁的是整个database。由MySQL的SQL layer层实现的</p>
</li>
<li>
<p>表级锁：锁的是某个table。由MySQL的SQL layer层实现的，主要有表锁和元数据锁。</p>
</li>
<li>
<p>行级锁：锁的是某行数据，也可能锁定行之间的间隙。由某些存储引擎实现，比如InnoDB。行锁锁定的是某行数据，也可能锁定行之间的间隙。InnoDB行锁是通过给索引树上的叶子节点中索引项加锁来实现的。</p>
<p>InnoDB的行级锁，按照锁定范围来说，分为三种：</p>
<p><strong>记录锁（Record Locks）</strong>: 锁定索引中一条记录。</p>
<p><strong>间隙锁（Gap Locks）</strong>: 锁住的是两个索引之间的区间（缝隙），是一个左开右开区间。</p>
<p><strong>Next-Key Locks</strong>: 间隙锁+紧邻间隙锁的下一个记录锁，左开右闭区间。</p>
<p><strong>而且在无索引的情况下，行锁会升级为表级锁。</strong></p>
</li>
</ul>
<h3 data-id="heading-31">6.1.2 按功能划分</h3>
<ul>
<li>共享读锁：允许一个事务去读一行，阻止其他事务获得相同数据集的<strong>排他锁</strong></li>
<li>排他写锁：允许获得排他写锁的事务更新数据，阻止其他事务取得相同数据集的<strong>共享读锁（不是读）和排他写锁</strong>。</li>
</ul>
<h3 data-id="heading-32">6.1.3 按实现方式</h3>
<ul>
<li>悲观锁</li>
<li>乐观锁</li>
</ul>
<h1 data-id="heading-33">7、Mysql 事物和MVCC底层原理</h1>
<h2 data-id="heading-34">7.1 事物四大特性（ACID）</h2>
<ul>
<li>
<p><strong>原子性</strong></p>
<p>事务是可以提交或回滚的工作的原子单位。当一个事务对数据库进行多次更改时，要么所有更改 在事务提交时成功，要么所有更改在事务回滚时撤消。它的意思就是在事务中发生的一系列操作是一个不可分割单元，事务里面的一系列更新操作，它们要么在事务提交全部是成功执行，要么在事务回滚时全部撤销。我们在程序中使用事务如果发生了异常的话，一定要进行事务回滚，如果进行了回滚的话，那么我们前面进行的数据库更新操作就像都没有执行过。</p>
</li>
<li>
<p><strong>一致性</strong></p>
<p>数据库在任何时候都保持一致的状态——在每次提交或回滚之后，以及在事务进行期间。如果是跨多个表更新相关数据，在事务外查询时将看到所有旧值或所有新值，而不是新旧值的混合。事务开始和结束之间的数据的中间状态不会被其他事务看到，事务的原子性保证了数据的一致性。</p>
</li>
<li>
<p><strong>隔离性</strong></p>
<p>事务在进行过程中相互隔离，它们不能相互干扰或查看彼此未提交的数据。事务的隔离性是通过锁定机制实现的，有经验的开发人员可以通过调整隔离级别，提高性能和并发性，这样他们就可以确保事务之间不会相互干扰。</p>
<p>由锁机制和MVCC机制来实现的；MVCC(多版本并发控制)：优化读写性能（读不加锁、读写不冲突）</p>
</li>
<li>
<p><strong>持久性</strong></p>
<p>事务的结果是持久的，事务执行成功后必须全部写入磁盘：一旦提交操作成功，该事务所做的更改就不会受到电源故障、系统崩溃等其他潜在危险的影响。数据库的数据通常是保存在磁盘上的，对数据的修改涉及对磁盘存储的写操作，其中包含一定数量的冗余，以防止在写操作期间出现电源故障或软件崩溃。</p>
</li>
</ul>
<h2 data-id="heading-35">7.2 InnoDB内存和磁盘结构</h2>
<h3 data-id="heading-36">7.2.1 内存结构</h3>
<h4 data-id="heading-37">Buffer Pool 缓冲池</h4>
<p>Buffer Pool是主内存的一块区域，在InnoDB访问表时会将数据页和索引页缓存到缓冲池中。在MySQL专用服务器上，通常将75％以     上的物理内存分配给缓冲池，可以通过参数<strong>innodb_buffer_pool_size</strong>控制缓冲池的大小。</p>
<p>InnoDB表中数据不管是主键索引还是辅助索引都是以页为单位存储在磁盘空间中的。当InnoDB访问某个页中的数据时，会先把这个页整体加载到缓冲池中然后在进行读写操作。在完成操作后，InnoDB并不会立即将这个页从缓冲池中删除，而是将它缓存起来，这样当下次再有操作需要访问这个页时，会直接从缓冲池中获取，这样就省去了磁盘IO开销，加快了数据访问速度。</p>
<p>Buffer Pool中页的大小和数据文件上页大小是一样的，都是16K。当Buffer Pool空间不够用时，Buffer Pool会使用<strong>LRU算法</strong>淘汰最近最少使用的页。</p>
<p>在MySQL初始化时会将Buffer Pool划分为若干个缓存页：</p>
<ul>
<li><strong>空闲页链表</strong>：未使用的缓存页</li>
<li><strong>脏页链表</strong>：发生修改的缓存页，InnoDB存储引擎对数据做修改的时候，会先把数据页从磁盘中读到内存中(buffer pool)中，然后在buffer pool中进行修改，那么这个时候buffer pool中的数据页就与磁盘上的数据页内容不一致，称这个页为dirty page 脏页</li>
<li><strong>LRU链表</strong>：LRU链表中保存着所有加载到Buffer Pool的数据页和索引页。按照最近最少使用的原则，最近使用的排在链表的头部，最近最少使用排在链表尾部。</li>
</ul>
<p>当Buffer Pool空间没有空闲页可用时，就从LRU链表尾部淘汰一些缓存页，经过淘汰之后，LRU头部就保存的是热点数据。LRU链表不是传统的LRU链表，InnoDB对LRU做了优化，<strong>将LRU链表分成了yong区（5/8）和old区（3/8）</strong>。这个比例可以通过参数<strong>innodb_old_blocks_pct</strong>调节，默认值37，代表old区占比37%。</p>
<p><strong>young区</strong>：存储使用频率非常高的缓存页，这一部分链表也叫做热数据。</p>
<p><strong>old区</strong>：存储使用频率不是很高的缓存页，所以这一部分链表也叫做冷数据。</p>
<p>当InnoDB将页面读入缓冲池时，<strong>它首先将其插入old列表的头部，当下次访问这个页面满足一定条件时在将这个页面插入到yong区的头部</strong>。<strong>满足一定条件是指</strong>：最近一次访问页面时间减去首次访问的时间<某个时间间隔。这个时间间隔可以通过innodb_old_blocks_time 参数控制，<strong>默认值1s</strong>。即第一次和最后一次访问该页面的时间间隔小于1s时，才会将这个页面插入到yong区的头部。</p>
<p>对于缓冲池中的一些<strong>热点索引页</strong>，InnoDB为了提高这些页的访问速度，会自动在缓冲池中建立一个<strong>自适应Hash索引</strong>。自适应哈希索引功能可以使用参数innodb_adaptive_hash_index是否开启，默认开启。</p>
<h4 data-id="heading-38">Change Buffer</h4>
<p>Change Buffer是一种特殊的数据结构，是针对二级索引（辅助索引）页的更新优化措施。当二级索引页不在Buffer Pool中，InnoDB会将对二级索引的数据更改操作先暂时缓存在Change Buffer中，稍后当索引页面因为其他读取操作加载到Buffer Pool的时候，会将这些更改操作合并更新到索引页中。Change Buffer缓存的更改可能由 Insert 、Delete 和 Update操作导致，这样通过合并操作可以减少二级索引的随机IO。Change Buffer的使用可以有效的提升insert，updte，delete的执行速度。</p>
<pre><code class="hljs language-xml copyable" lang="xml">步骤： 
1.二级索引页的DML操作，并且这个索引页页没有在Buffer Pool内，那么把这个操作存入Change Buffer。 
2.那么下一次需要加载这个页面的时候，索引页被加载到Buffer Pool中。Change Buffer内的更改 合并到Buffer Pool。 
3.随后当服务器在空闲的时候，这个更改会刷到磁盘上。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>什么时候将change buffer更新到buffer pool的索引页？</strong></p>
<p><strong>答</strong>：索引页加载到缓存池中时在内存中合并更新。</p>
<p><strong>什么时候将buffer pool的脏页更新到磁盘文件中？</strong></p>
<p><strong>答</strong>：redo log写满时；数据库空闲时，由后台线程；数据库正常关闭时。同样change buffer也会在这三种情况同时被更新到磁盘中。</p>
<h4 data-id="heading-39">Log Buffer（Redo Log）</h4>
<p>MySQL会<strong>将更新先缓存在内存</strong>中，当<strong>服务器空闲时</strong>才会选择将脏页刷新到磁盘中。但是这就会有个问题，如果在脏页落盘之前服务器异常关机或者MySQL崩溃宕机，就会造成脏页这些数据的丢失。为了避免这个问题，InnoDB把对页面的修改操作会同时写入一个日志文件持久化到磁盘上，这样当MySQL崩溃重启后，MySQL就会使用这个日志文件执行恢复操作，将更改重新应用到数据文件，实现了更新操作的持久化。这个日志文件就是Redo Log。</p>
<p>默认情况下，redo log对应的物理文件位于<strong>数据库的数据目录下的ib_logfile1和ib_logfile2</strong>。可以通过参数控制日志文件的存储文职，数量和大小，设置如下所示：</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-comment">#指定日志文件所在的路径，默认./，表示在数据库的数据目录下。 </span>
<span class="hljs-attr">innodb_log_group_home_dir</span>=<span class="hljs-string">./ </span>
<span class="hljs-comment">#指定重做日志文件组中文件的数量，默认2，表示有两个重做日志文件。 </span>
<span class="hljs-comment">#两个文件循环写入，一个写满之后才能开始使用另外一个，一般保持2就可以。 </span>
<span class="hljs-attr">innodb_log_files_in_group</span>=<span class="hljs-string">2 </span>
<span class="hljs-comment">#每个重做日志文件的大小，默认48M。 </span>
<span class="hljs-attr">innodb_log_file_size</span>=<span class="hljs-string">16777216</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种日志和磁盘配合的过程 ， 其实就是MySQL里经常说到的WAL 技术（Write-Ahead Logging），它的关键点就是在<strong>写磁盘前，先写日志</strong>。MySQL在内存中专门开辟了一块区域Log Buffer专门<strong>保存将要写入redo log</strong>的数据，它的大小可以通过数<strong>innodb_log_buffer_size</strong>控制，默认16M。</p>
<p><strong>落盘时机</strong>：Log Buffer写入磁盘的时机，由参数 <strong>innodb_flush_log_at_trx_commit</strong> 控制，<strong>默认是1</strong>，表示<strong>事务提交后立即落盘</strong>。</p>
<p><strong>落盘规则</strong>：</p>
<ul>
<li><strong>0</strong>:   MySQL每秒一次将数据从log buffer写入日志文件并同时fsync刷新到磁盘中。每次事务提交时，不会立即把 log buffer 里的数据写入到redo log日志文件的。如果MySQL崩溃或者服务器宕机，此时内存里的数据会全部丢失，最多会丢失1秒的事务。</li>
<li><strong>1</strong>：每次事务提交时，MySQL将数据从log buffer写入日志文件并同时fsync刷新到磁盘中。该模式为系统默认，MySQL崩溃已经提交的事务不会丢失，<strong>要完全符合ACID，必须使用默认设置1</strong>。</li>
<li><strong>2</strong>：每次事务提交时，MySQL将数据从log buffer写入日志文件，MySQL每秒执行一次fsync操作将数据同步到磁盘中。每次事务提交时，都会将数据刷新到操作系统缓冲区，可以认为已经持久化磁盘，如果MySQL崩溃已经提交的事务不会丢失。但是如果服务器宕机或者意外断电，操作系统缓存内的数据会丢失，所以最多丢失1秒的事务。</li>
</ul>
<p><strong>总结</strong>：</p>
<p>综合安全性和性能的考虑，<strong>在业务中经常使用2这种模式</strong>，在MySQL异常重启时不会丢失数据，只有在服务器意外宕机时才会丢失1秒的数据，这种情况几率是很低的，相对于性能来说，这时可以容忍的。</p>
<p><strong>日志文件也是磁盘文件，为什么不直接更新到数据文件中，而是要先更新到redo log中呢？</strong></p>
<p><strong>答</strong>：如果事务提交时，我们需要更新的数据是分散在不同页不同扇区中的，更新数据时需要根据磁盘地址找到对应的磁道，然后再找到对应的扇区，才能写入数据，这个时间一般需要10ms。<strong>一次事务提交的数据需要多次的磁盘IO交互才能完成，这个是随机IO，读取和写入速度比较慢</strong>。</p>
<p>而redo log文件是在磁盘中<strong>一块连续的区域</strong>，事务提交时，写入redo log时，我们只要找到找到第一块扇区，只需要依次向后写入就行，也就是说<strong>只需要执行一次磁盘IO操作，这就是顺序IO</strong>。<strong>脏页落盘是随机IO，记录日志是顺序IO，通过使用WAL技术，先将更改操作记录在日志文件中，延迟落盘，可以提高系统性能</strong>。需要注意的是，<strong>redo log主要用于崩溃恢复。磁盘中数据文件的数据的更新，仍旧来自于 buffer pool中的脏页落盘。</strong></p>
<p><strong>redo log的特点</strong>：</p>
<ol>
<li>
<p>redo log 是InnoDB存储引擎层产生的，其他存储引擎没有。</p>
</li>
<li>
<p>redo log是物理日志，记录的是“某个数据页上的数据做了什么修改”。</p>
</li>
<li>
<p>redo log的文件数和大小是固定的，redo一个文件写满后会切换到下一个文件。从第一个文件开始写，写到最后一个文件就又会回到第一个文件开始循环写。当系统空闲时或者redolog写满时，MySQL会将redo log前面的数据擦除，对应的数据修改会被同步到数据文件中。</p>
</li>
</ol>
<h4 data-id="heading-40">bin log</h4>
<p>binlog记录了数据库执行更改的操作（所有的ddl语句和dml语句），但不包括select和show这类操作。<strong>事务未提交前，所有未提交的二进制日志会被记录到一个缓存中去，等该事务提交时直接将缓冲中的二进制日志写入二进制日志文件</strong>，<strong>主要用于实现mysql主从复制、数据恢复</strong>。</p>
<p>binlog默认是关闭的，建议开启，需要通过以下配置进行开启。</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-comment">#默认关闭 </span>
<span class="hljs-meta">log-bin</span>=<span class="hljs-string">OFF </span>
<span class="hljs-comment">#开启，mysql-bin是binlog日志文件的文件名前缀，binlog日志文件的完整名称：mysql-bin-000001.log </span>
<span class="hljs-meta">log-bin</span>=<span class="hljs-string">mysql-bin</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>max_binlog_size</strong>指定了单个二进制日志文件的最大值。如果超过该值，则产生新的二进制日志文件，后缀名+1，如mysql-bin-000002.log。</p>
<p>二进制缓冲区是基于会话（session）的，其大小由binlog_cache_size 决定，默认大小为32K。当一个线程开始一个事务时，MySQL 自动分配一个大小为binlog cache_ size 的缓存。</p>
<p><strong>落盘时机</strong>：</p>
<p>写入磁盘的时机，由参数<strong>sync_binlog</strong>控制，默认是 1，<strong>在事务提交（Commit）前</strong>将二进制日志刷新到磁盘。</p>
<ul>
<li>
<p><strong>0</strong>：禁用MySQL服务器将二进制日志同步到磁盘的功能。依赖于操作系统不时地将二进制日志刷新到磁盘上，就像处理其他任何文件一样。此设置性能最佳，但是因为二进文件缓存在binlog_cache中，所以在电源故障或者操作系统崩溃时，会存在已提交的事务未同步到磁盘的可能性（在binlog_cache中的所有binlog信息都会被丢失）。</p>
</li>
<li>
<p><strong>1</strong>：在事务提交前将二进制日志同步到磁盘。这是最安全的设置，但是由于磁盘写入次数增加，会对性能产生影响。在电源故障或者操作系统崩溃时，可以保证所有已经提交的事务肯定已经刷新到磁盘中，未刷新到磁盘的事务仅仅是处于准备阶段（未提交），不会丢失事务。</p>
<blockquote>
<p>sync_binlog=1，一个事务发出COMMIT动作之前，会将二进制日志立即写入磁盘。如果这时已经写入了二进制日志，但是提交还没有发生，如果此时发生了宕机，那么在MySQL数据库下次启动时，由于COMMIT操作并没有发生，这个事务会被回滚掉。但是二进制日志已经记录了该事务信息，如果在主从复制环境下（或者使用这个binlog来来进行恢复）就会造成主从数据不一致。这个问题可以通过将参数<strong>innodb_support_xa=1来解决，它同时确保了二进制日志和InnoDB存储引擎数据文件的同步</strong>。</p>
</blockquote>
</li>
<li>
<p>N（N>1）：每N次事务，Mysql会同步二进制日志同步到磁盘。在电源故障或者操作系统崩溃时，会存在已提交的事务未同步到磁盘的可能性。</p>
</li>
</ul>
<p><strong>redo log和bin log区别</strong></p>
<ol>
<li>
<p>redo log 是InnoDB存储引擎层产生的，而bin log是数据服务层产生的。</p>
</li>
<li>
<p>redo log 空间固定，用完后循环写；binlog 采用“追加写”的方式，一个文件达到一定大小后会切换到下一个。</p>
</li>
<li>
<p>redo log主要用于崩溃恢复；binlog主要用于主从复制和数据恢复。</p>
</li>
</ol>
<h4 data-id="heading-41">Double Write双写缓冲区</h4>
<p><strong>为什么需要双写缓冲区？</strong></p>
<p><strong>答</strong>：数据库数据页大小是16K，操作系统IO的最小单位一般是4K，也就是说Buffer Pool中一个脏页写入数据文件时需要分4次写入。如果数据页在写入的过程中，服务器断电或者宕机，数据页就有可能只写入了一部分（比如只写入了8k），还有一半的数据没有写入，这种现象称为“部分写失效”（partial page write）。就会导致数据文件中的数据页被损坏，在MySQL重启后，就无法使用redo log恢复这个损坏的数据页，所以这个页的数据就丢失了，可能会造成数据不一致。<strong>InnoDB为了提高的可靠性，引入了Double Write机制，用来解决部分写失效</strong>。</p>
<p>双写缓冲是InnoDB的一个关键特性，可以<strong>使用参数innodb_doublewrite控制是否启用双写缓冲区，默认开启，建议开启</strong>。如果开启了双写缓冲，在 InnoDB将脏页写入数据文件之前，会先从缓冲池中刷新页面到双写缓冲区 ，然后再将脏页从双写缓冲刷新到数据文件中。如果脏页在写入数据文件过程中MySQL服务崩溃，MySQL重启后InnoDB就可以从系统表空间的Double Write中找到该页最近的一个副本，将其复制到表空间文件，然后再应用redo log，就可以完成了恢复。</p>
<h4 data-id="heading-42">undo log</h4>
<p>事务的原子性和隔离性都是由undo log来实现的。实现了原子性，其实也就是实现了一致性。事务的持久性是由redo log来实现的。</p>
<p>undolog（撤销日志或回滚日志）记录了事务中更改操作之前的数据状态，如果用户执行了回滚操作，数据库就可以<strong>利用undo log 将数据恢复至事务之前的状态</strong>。<strong>redo Log 和 undo Log ，统称为事务日志</strong>。undo Log 默认存储在系统表空间中，也可以将undoLog存储在独立表空间，可以通过以下参数设置。</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">show</span> <span class="hljs-string">global variables like '%undo%';</span>
<span class="hljs-comment">#undo存储目录，默认在数据目录下 </span>
<span class="hljs-attr">innodb_undo_directory</span>=<span class="hljs-string">./ </span>
<span class="hljs-comment">#默认0，表示关闭。undo文件的数量，格式为undo001，undo002等 </span>
<span class="hljs-attr">innodb_undo_tablespaces</span>=<span class="hljs-string">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了用于回滚操作，<strong>undo log的另一个作用是MVCC</strong>，在InnoDB存储引擎中MVCC的实现是通过undolog来完成。当用户读取一行记录时，若该记录已经被其他事务占用，当前事务可以通过undo log读取之前的行版本信息，以此实现非锁定读取。</p>
<h3 data-id="heading-43">7.2.2 InnoDB事物分析</h3>
<h4 data-id="heading-44">原子性、持久性和一致性</h4>
<p><strong>原子性，持久性和一致性主要是通过redo log、undo log、Force Log at Commit和Double Write机制来完成的。redo log用于在崩溃时恢复数据，undo log用于对事务回滚时进行撤销，也会用于隔离性的多版本控制。Force Log at Commit机制保证事务提交后redo log日志都已经持久化。Double Write机制用来提高数据库的可靠性，用来解决脏页落盘时部分写失效问题</strong>。</p>
<p>原子性：redo log、undo log、Force Log at Commit和Double Write机制。</p>
<p>持久性：redo log，Double Write。</p>
<p>redo log主要用于崩溃恢复。数据库崩溃重启后需要从redo log中把未落盘的脏页数据恢复出来，重新写入磁盘，保证用户的数据不丢失。</p>
<p>崩溃恢复时除了需要使用redo log对已经提交的事务。在崩溃恢复中还需要回滚没有提交的事务。回滚操作需要undo日志的支持，undo日志的完整性和可靠性需要redo日志来保证，<strong>所以崩溃恢复先做redo恢复数据，然后做undo回滚</strong>。</p>
<blockquote>
<p>事务进行过程中，每次sql语句执行，都会记录undo log和redo log，然后更新数据形成脏页，然后redo log按照时间或者空间等条件进行落盘，undo log和脏页按照checkpoint进行落盘，落盘后相应的redo log就可以删除了。此时，事务还未COMMIT，如果发生崩溃，则首先检查checkpoint记录，使用相应的redo log进行数据和undo log的恢复，然后查看undo log的状态发现事务尚未提交，然后就使用undo log进行事务回滚。事务执行COMMIT操作时，会将本事务相关的所有redo log都进行落盘，只有所有redo log落盘成功，才算COMMIT成功。然后内存中的数据脏页继续按照checkpoint进行落盘。如果此时发生了崩溃，则只使用redo log恢复数据。</p>
</blockquote>
<h4 data-id="heading-45">隔离性</h4>
<ul>
<li>
<p>Read uncommitted (读未提交)：最低级别，任何情况都无法保证。</p>
</li>
<li>
<p>Read committed (RC，读已提交)：可避免脏读的发生。</p>
</li>
<li>
<p>Repeatable read (RR，可重复读)：可避免脏读、不可重复读的发生。</p>
<p><strong>（注意事项：InnoDB的RR还可以解决幻读，主要原因是Next-Key（Gap）锁，只有RR才能使用 Next-Key锁）</strong></p>
</li>
<li>
<p>Serializable (串行化)：可避免脏读、不可重复读、幻读的发生。</p>
<p><strong>（由MVCC降级为Locking-Base CC）</strong></p>
</li>
</ul>
<p><strong>MVCC使得数据库读不会对数据加锁，普通的SELECT请求不会加锁，提高了数据库的并发处理能力</strong>。借助MVCC，数据库可以实现READ COMMITTED，REPEATABLE READ等隔离级别，用户可以查看当前数据的前一个或者前几个历史版本，保证了ACID中的I特性（隔离性)。</p>
<p>在MVCC并发控制中，读操作可以分成两类：<strong>快照读 (snapshot read)与当前读 (current read)。</strong></p>
<ul>
<li>快照读，读取的是记录的可见版本 (有可能是历史版本)，不用加锁。(select)</li>
<li>当前读，读取的是记录的最新版本，并且当前读返回的记录，都会加上锁，保证其他事务不会再并发修改这条记录。</li>
</ul>
<p>**一致性非锁定读(consistent nonlocking read)**是指InnoDB存储引擎通过多版本控制(MVCC)读取当前数据库中行数据的方式。</p>
<p>如果读取的行正在执行DELETE或UPDATE操作，这时读取操作不会因此去等待行上锁的释放。相反地，InnoDB会去读取行的一个最新可见快照。</p>
<h4 data-id="heading-46">事务链表</h4>
<p>MySQL中的事务在开始到提交这段过程中，都会被保存到一个叫trx_sys的事务链表中，这是一个基本的链表结构：</p>
<p>ct-trx --> trx11 --> trx9 --> trx6 --> trx5 --> trx3;</p>
<p>事务链表中保存的都是还未提交的事务，事务一旦被提交，则会被从事务链表中摘除。</p>
<p><strong>RR隔离级别下，在每个事务开始的时候</strong>，会将当前系统中的所有的活跃事务拷贝到一个列表中(readview)</p>
<p><strong>RC隔离级别下，在每个语句开始的时候</strong>，会将当前系统中的所有的活跃事务拷贝到一个列表中(readview)</p>
<p>show engine innodb status ,就能够看到事务列表。</p>
<h4 data-id="heading-47">ReadView</h4>
<p>Read View是事务开启时当前所有事务的一个集合，这个类中存储了当前Read View中最大事务ID及最小事务ID。</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-comment">#假设这就是当前活跃的事务列表。如下所示：</span>
<span class="hljs-meta">ct-trx</span> <span class="hljs-string">--> trx11 --> trx9 --> trx6 --> trx5 --> trx3;</span>
<span class="hljs-comment">#ct-trx 表示当前事务的id，对应上面的read_view数据结构如下</span>
<span class="hljs-meta">read_view->creator_trx_id</span> = <span class="hljs-string">ct-trx; </span>
<span class="hljs-meta">read_view->up_limit_id</span> = <span class="hljs-string">trx3; 低水位 </span>
<span class="hljs-meta">read_view->low_limit_id</span> = <span class="hljs-string">trx11; 高水位 </span>
<span class="hljs-meta">read_view->trx_ids</span> = <span class="hljs-string">[trx11, trx9, trx6, trx5, trx3];</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**low_limit水位”，即当时活跃事务的最大id，如果读到row的db_trx_id>=low_limit_id，说明这些id在此之前的数据都没有提交，如注释中的描述，这些数据都不可见。</p>
<p><strong>up_limit_id</strong>是“低水位”，即当时活跃事务列表的最小事务id，如果row的db_trx_id<up_limit_id,说明这些数据在事务创建的id时都已经提交，如注释中的描述，这些数据均可见。</p>
<p>row的<strong>db_trx_id</strong>在low_limit_id和up_limit_id之间，则<strong>查找该记录的db_trx_id是否在自己事务的read_view->trx_ids列表中，如果在则该记录的当前版本不可见，否则该记录的当前版本可见</strong>。</p>
<p>在<strong>repeatable read</strong>的隔离级别下，创建事务trx结构的时候，就生成了当前的global readview。使用trx_assign_read_view函数创建，一直维持到事务结束。<strong>在事务结束这段时间内 每一次查询都不会重新重建Read View ， 从而实现了可重复读。</strong></p>
<p>在 <strong>read-commited</strong>的隔离级别下，在每次语句执行的过程中，都关闭read_view, 重新在row_search_for_mysql函数中创建当前的一份read_view。这样就会产生不可重复读现象发生。</p></div>  
</div>
            