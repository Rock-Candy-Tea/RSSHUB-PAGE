
---
title: '一种简易但设计全面的ID生成器思考'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38e050ec695b46c9abbd4d2fc4d9a20a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 17:01:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38e050ec695b46c9abbd4d2fc4d9a20a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第22天</p>
<p>分布式系统中，全局唯一 ID 的生成是一个老生常谈但是非常重要的话题。随着技术的不断成熟，大家的分布式全局唯一 ID 设计与生成方案趋向于趋势递增的 ID，这篇文章将结合我们系统中的 ID 针对实际业务场景以及性能存储和可读性的考量以及优缺点取舍，进行深入分析。本文并不是为了分析出最好的 ID 生成器，而是分析设计 ID 生成器的时候需要考虑哪些，如何设计出最适合自己业务的 ID 生成器。</p>
<blockquote>
<p>项目地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FJoJoTec%2Fid-generator" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/JoJoTec/id-generator" ref="nofollow noopener noreferrer">github.com/JoJoTec/id-…</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38e050ec695b46c9abbd4d2fc4d9a20a~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先，先放出我们的全局唯一 ID 结构：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8f1fd2bf8ec4d61a963c6f1693f68b6~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个唯一 ID 生成器是放在每个微服务进程里面的插件这种架构，不是有那种唯一 ID 生成中心的架构：</p>
<ul>
<li>开头是时间戳格式化之后的字符串，可以直接看出年月日时分秒以及毫秒。由于分散在不同进程里面，需要考虑不同微服务时间戳不同是否会产生相同 ID 的问题。</li>
<li>中间业务字段，最多 4 个字符。</li>
<li>最后是自增序列。这个自增序列通过 Redis 获取，同时做了分散压力优化以及集群 fallback 优化，后面会详细分析。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1547d9f9c8704fc18ebf663b160a6fcb~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>序列号的开头是时间戳格式化之后的字符串，由于分散在不同进程里面，不同进程当前时间可能会有差异，这个差异可能是毫秒或者秒级别的。所以，<strong>要考虑 ID 中剩下的部分是否会产生相同的序列</strong>。</p>
<p>自增序列由两部分组成，第一部分是 Bucket，后面是从 Redis 中获取的对应 Bucket 自增序列，获取自增序列的伪代码是：</p>
<pre><code class="copyable">1. 获取当前线程 ThreadLocal 的 position，position 初始值为一个随机数。
2. position += 1，之后对最大 Bucket 大小（即 2^8）取余，即对 2^8 - 1 取与运算，获取当前 Bucket。
   如果当前 Bucket 没有被断路，则执行做下一步，否则重复 2。
   如果所有 Bucket 都失败，则抛异常退出
3. redis 执行： incr sequence_num_key:当前Bucket值，拿到返回值 sequence
4. 如果 sequence 大于最大 Sequence 值，即 2^18， 对这个 Bucket 加锁（sequence_num_lock:当前Bucket值），
   更新 sequence_num_key:当前Bucket值 为 0，之后重复第 3 步。否则，返回这个 sequence
   
-- 如果 3，4 出现 Redis 相关异常，则将当前 Bucket 加入断路器，重复步骤 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这种算法下，即使每个实例时间戳可能有差异，只要在<strong>最大差异时间内，同一业务不生成超过 Sequence 界限数量的实体，即可保证不会产生重复 ID</strong>。</p>
<p>同时，我们设计了 Bucket，<strong>这样在使用 Redis 集群的情况下，即使某些节点的 Redis 不可用，也不会影响我们生成 ID</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5fc76ac04174551bee239c214df4256~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当前 OLTP 业务离不开传统数据库，目前最流行的数据库是 MySQL，MySQL 中最流行的 OLTP 存储引擎是 InnoDB。考虑业务扩展与分布式数据库设计，InnoDB 的主键 ID 一般不采用自增 ID，而是通过全局 ID 生成器生成。这个 ID 对于 MySQL InnoDB 有哪些性能影响呢？我们通过将 BigInt 类型主键和我们这个字符串类型的主键进行对比分析。</p>
<p>首先，由于 B+ 树的索引特性，主键越是严格递增，插入性能越好。越是混乱无序，插入性能越差。这个原因，主要是 B+ 树设计中，如果值无序程度很高，数据被离散存储，造成 innodb 频繁的页分裂操作，严重降低插入性能。可以通过下面两个图的对比看出：</p>
<p><strong>插入有序</strong>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e69f63a41b5a458f8f8b2da771af9809~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>插入无序</strong>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a1f755551ca4b96bd89aca3b37b3705~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果插入的主键 ID 是离散无序的，那么每次插入都有可能对于之前的 B+ 树子节点进行裂变修改，<strong>那么在任一一段时间内，整个 B+ 树的每一个子分支都有可能被读取并修改，导致内存效率低下</strong>。<strong>如果主键是有序的（即新插入的 id 比之前的 id 要大），那么只有最新分支的子分支以及节点会被读取修改，这样从整体上提升了插入效率</strong>。</p>
<p>我们设计的 ID，由于是当前时间戳开头的，从<strong>趋势上是整体递增</strong>的。<strong>基本上能满足将插入要修改的 B+ 树节点控制在最新的 B+ 树分支上，防止树整体扫描以及修改</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adacf3ae141c4573b43b8dacce00fc26~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>和 SnowFlake 算法生成的 long 类型数字，在数据库中即 bigint 对比：bigint，在 InnoDB 引擎行记录存储中，无论是哪种行格式，都占用 <strong>8 字节</strong>。我们的 ID，char类型，字符编码采用 <strong>latin1</strong>（<strong>因为只有字母和数字</strong>），占用 27 字节，大概是 bigint 的 3 倍多。</p>
<ul>
<li>MySQL 的主键 B+ 树，如果主键越大，那么单行占用空间越多，即 B+ 树的分支以及叶子节点都会占用更多空间，造成的后果是：MySQL 是按页加载文件到内存的，也是按页处理的。这样一页内，可以读取与操作的数据将会变少。<strong>如果数据表字段只有一个主键，那么 MySQL 单页（不考虑各种头部，例如页头，行头，表头等等）能加载处理的行数， bigint 类型是我们这个主键的 3 倍多</strong>。但是数据表一般不会只有主键字段，还会有很多其他字段，<strong>其他字段占用空间越多，这个影响越小</strong>。</li>
<li>MySQL 的二级索引，叶子节点的值是主键，那么同样的，单页加载的叶子节点数量，bigint 类型是我们这个主键的 3 倍多。但是目前一般 MySQL 的配置，都是内存资源很大的，造成其实二级索引搜索主要的性能瓶颈并不在于此处，<strong>这个 3 倍影响对于大部分查询可能就是小于毫秒级别的优化提升。相对于我们设计的这个主键带来的可读性以及便利性来说，是微不足道的</strong>。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d09e0ceeee5648abac732eb63f55c853~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>业务上，其实有很多需要按创建时间排序的场景。比如说查询一个用户今天的订单，并且按照创建时间倒序，那么 SQL 一般是：</p>
<pre><code class="copyable">## 查询数量，为了分页
select count(1) from t_order where user_id = "userid" and create_time > date(now());
## 之后查询具体信息
select * from t_order where user_id = "userid" and create_time > date(now()) order by create_time limit 0, 10;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>订单表肯定会有 user_id 索引，但是随着业务增长，下单量越来越多导致这两个 SQL 越来越慢，这时我们就可以有两种选择：</p>
<ol>
<li>创建 user_id 和 create_time 的联合索引来减少扫描，但是大表额外增加索引会导致占用更多空间并且和现有索引重合有时候会导致 SQL 优化有误。</li>
<li>直接使用我们的主键索引进行筛选:</li>
</ol>
<pre><code class="copyable">select count(1) from t_order where user_id = "userid" and id > "210821";
select * from t_order where user_id = "userid" and id > "210821" order by id desc limit 0, 10;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是需要注意的是，第二个 SQL 执行会比创建 user_id 和 create_time 的联合索引执行原来的 SQL 多一步 <code>Creating sort index</code> 即将命中的数据在内存中排序，如果命中量比较小，即大部分用户在当天的订单量都是几十几百这个级别的，那么基本没问题，这一步不会消耗很大。否则还是需要创建 user_id 和 create_time 的联合索引来减少扫描。</p>
<p>如果不涉及排序，<strong>仅仅筛选的话</strong>，这样做基本是没问题的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda3d8fe25bb43f3a8b14d4e49a840e2~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们不希望用户通过 ID 得知我们的业务体量，例如我现在下一单拿到 ID，之后再过一段时间再下一单拿到 ID，对比这两个 ID 就能得出这段时间内有多少单。</p>
<p>我们设计的这个 ID 完全没有这个问题，因为最后的序列号：</p>
<ol>
<li>所有业务共用同一套序列号，每种业务有 ID 产生的时候，就会造成 Bucket 里面的序列递增。</li>
<li>序列号同一时刻可能不同线程使用的不同的 Bucket，并且结果是位操作，很难看出来那部分是序列号，那部分是 Bucket。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71f9ee069abe4a838379c3a6e0a33ab1~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从我们设计的 ID 上，可以直观的看出这个业务的实体，是在什么时刻创建出来的：</p>
<ul>
<li>一般客服受理问题的时候，拿到 ID 就能看出来时间，直接去后台系统对应时间段调取用户相关操作记录即可。简化操作。</li>
<li>一般的业务有报警系统，一般报警信息中会包含 ID，从我们设计的 ID 上就能看出来创建时间，以及属于哪个业务。</li>
<li>日志一般会被采集到一起，所有微服务系统的日志都会汇入例如 ELK 这样的系统中，从搜索引擎中搜索出来的信息，从 ID 就能直观看出业务以及创建时间。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16cd76e41f484249a7e59fb1a9ec7d6c~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在给出的项目源码地址中的单元测试中，我们测试了通过 embedded-redis 启动一个本地 redis 的单线程，200 线程获取 ID 的性能，并且对比了只操作 redis，只获取序列以及获取 ID 的性能，我的破电脑结果如下：</p>
<pre><code class="copyable">单线程
BaseLine(only redis): 200000 in: 28018ms
Sequence generate: 200000 in: 28459ms
ID generate: 200000 in: 29055ms

200线程
BaseLine(only redis): 200000 in: 3450ms
Sequence generate: 200000 in: 3562ms
ID generate: 200000 in: 3610ms
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            