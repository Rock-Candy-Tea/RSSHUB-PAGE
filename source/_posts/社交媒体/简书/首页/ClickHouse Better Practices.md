
---
title: 'ClickHouse Better Practices'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/195230-40f8286e2ae4450c.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/195230-40f8286e2ae4450c.png'
---

<div>   
<h3>前言</h3>
<p>经过一个月的调研和快速试错，我们的ClickHouse集群已经正式投入生产环境，在此过程中总结出了部分有用的经验，现记录如下。看官可去粗取精，按照自己项目中的实际情况采纳之。（版本为19.16.14.65）</p>
<p>因为我们引入ClickHouse的时间并不算长，还有很多要探索的，因此不敢妄称“最佳实践”，还是叫做“更佳实践”比较好吧。</p>
<h3>表相关事项</h3>
<h5>数据类型</h5>
<ul>
<li>建表时能用数值型或日期时间型表示的字段，就不要用字符串——全String类型在以Hive为中心的数仓建设中常见，但CK环境不应受此影响。</li>
<li>直接用DateTime表示时间列，而不是用整形的时间戳。因为CK中DateTime的底层就是时间戳，效率高，可读性好，且转换函数丰富。</li>
<li>官方已经指出Nullable类型几乎总是会拖累性能，因为存储Nullable列时需要创建一个额外的文件来存储<code>NULL</code>的标记，并且Nullable列无法被索引。因此除非极特殊情况，应直接使用字段默认值表示空，或者自行指定一个在业务中无意义的值（例如用-1表示没有商品ID）。</li>
</ul>
<h5>分区和索引</h5>
<ul>
<li>事实表必须分区，分区粒度根据业务特点决定，不宜过粗或过细。我们当前都是按天分区，按小时、周、月分区也比较常见（系统表中的query_log、trace_log表默认就是按月分区的）。</li>
<li>必须指定索引列，在绝大多数查询的<code>WHERE</code>语句中都会用到的列适合作为索引。CK的索引非MySQL的B树索引，而是类似Kafka log风格的稀疏索引，故不用考虑最左原则，<del>但是建议日期列和区分度较低的列在前，区分度较高的列在后。</del>
</li>
</ul>
<p>订正：根据稀疏索引的规律，建议<strong>查询中更经常用做查询条件（WHERE谓词）的列在前，较不经常用做查询条件的列在后。</strong>如果有两列在WHERE谓词中出现的频率大致相同，则<strong>基数较大的列（即区分度较高的列）在前，基数较小的列（区分度较低的列）在后。</strong>另外，<strong>基数特别大的列（如订单ID等）不建议直接用作索引。</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1558" data-height="310"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-40f8286e2ae4450c.png" data-original-width="1558" data-original-height="310" data-original-format="image/png" data-original-filesize="49506" src="https://upload-images.jianshu.io/upload_images/195230-40f8286e2ae4450c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>表的索引粒度<code>index_granularity</code>不建议调整，保持默认值8192即可。</li>
</ul>
<h5>表参数</h5>
<ul>
<li>生产环境中提供线上服务的表均采用复制表与分布式表相结合，即Replicated*MergeTree+Distributed引擎。分布式表的表名为本地表名加上<code>_all</code>后缀。</li>
<li>如果表中不是必须保留全量历史数据，建议指定TTL，可以免去手动过期历史数据的麻烦。TTL也可以通过<code>ALTER TABLE</code>语句随时修改。</li>
<li>建议指定<code>use_minimalistic_part_header_in_zookeeper = 1</code>设置项，能够显著压缩表元数据在ZooKeeper中的存储。该项也可以写入config.xml中的<merge_tree>一节。</li>
</ul>
<h3>查询相关事项</h3>
<h5>单表查询</h5>
<ul>
<li>所有应用层查询禁止<code>SELECT *</code>。</li>
<li>查询分区表必须指定分区（所谓partition pruning），不能全表查询。</li>
<li>大规模数据集上的ORDER BY要加LIMIT限制。</li>
<li>结果集上的简单运算（例如<code>SELECT pv, uv, pv / uv as ratio...</code>中的ratio）可以在前端展示时再进行，减少SQL中不必要的虚拟列。</li>
<li>业务场景非强制要求100%准确的基数计量，应该用uniq()函数而不是uniqExact()函数或DISTINCT关键字。uniq()底层采用HyperLogLog实现，能够以低于1%的精度损失换来极大的性能提升。</li>
<li>能够重用的模式化查询（如固定刷新的BI报表、热力图等）一定要做成物化视图，并在物化视图上查询出结果，可以避免大量的重复计算。关于其用法，可参见之前写过的<a href="https://www.jianshu.com/p/3f385e4e7f95" target="_blank">《物化视图简介与ClickHouse中的应用示例》</a>。</li>
</ul>
<h5>多表查询</h5>
<ul>
<li>当两表关联查询只需要从左表出结果时，建议用IN而不是JOIN，即写成<code>SELECT ... FROM left_table WHERE join_key IN (SELECT ... FROM right_table)</code>的风格。</li>
<li>不管是LEFT、RIGHT还是INNER JOIN操作，小表都必须放在右侧。因为CK默认在大多数情况下都用hash join算法，左表固定为probe table，右表固定为build table且被广播。</li>
<li>CK的查询优化器比较弱，JOIN操作的谓词不会下推，因此一定要先做完过滤、聚合等操作，再在结果集上做JOIN。这点与我们写其他平台SQL语句的习惯很不同，初期尤其需要注意。</li>
<li>两张分布式表上的IN和JOIN之前必须加上GLOBAL关键字。如果不加GLOBAL关键字的话，每个节点都会单独发起一次对右表的查询，而右表又是分布式表，就导致右表一共会被查询N<sup>2</sup>次（N是该分布式表的shard数量），这就是所谓的查询放大，会带来不小的overhead。加上GLOBAL关键字之后，右表只会在接收查询请求的那个节点查询一次，并将其分发到其他节点上。</li>
</ul>
<h5>负载均衡</h5>
<p>对于循环复制拓扑的集群，查询分布式表的负载均衡策略（即<code>load_balancing</code>）设为first_or_random是最优的，能够充分利用机器page cache的同时，在有replica失败时也能尽量保证负载平均分配。详情可见<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FClickHouse%2FClickHouse%2Fissues%2F4820" target="_blank">这个issue</a>。</p>
<h3>写入相关事项</h3>
<ul>
<li>写入分布式表的底表，而不直接写分布式表。在之前的<a href="https://www.jianshu.com/p/ab811cceb856" target="_blank">《ClickHouse复制表、分布式表机制与使用方法》</a>一文中已有说明。</li>
<li>不要做小批量零碎的写入，每批次至少千条级别，避免给merge造成太大压力。</li>
<li>不要同时写入太多个分区，或者写入过快（官方给出的阈值为1秒1次），容易因为merge的速度跟不上parts生成的速度而报出"too many parts"的错误。如果正常情况下还会出现此错误，建议在CPU资源允许的情况下适当调大后台任务线程数<code>background_pool_size</code>，默认值为16。</li>
</ul>
<h3>运维相关事项</h3>
<h5>CPU</h5>
<p>CK的“快”与其对CPU的积极利用密不可分，所以CPU的单核性能和多核性能都要尽量好一点，16核32线程左右且带较高的睿频比较合适。CK设置中的<code>max_threads</code>参数控制单个查询所能利用的CPU线程数，默认与本机CPU的物理核心数相同，如果服务器是CK独占的，那么就不用改，否则就改小些。</p>
<p>在监控集群时，CPU指标也是最重要的。实测当单个CK Server节点的CPU使用率超过70%时，服务就不太稳定了。</p>
<h5>内存</h5>
<p>官方文档建议单机物理内存128G左右。实测CK在我们的应用场景下内存占用并不激进，每线程对应1G内存非常绰绰有余，即<code>max_threads</code>设为20的话，<code>max_memory_usage</code>参数设为20G（懒得打辣么多0了）。为了不干扰系统的正常运行，也应配置所有查询能利用的最大内存参数<code>max_memory_usage_for_all_queries</code>，取物理内存的80%左右即可。</p>
<p>另外，CK在执行GROUP BY聚合逻辑的过程中很有可能超出内存限制，因此也建议设置<code>max_bytes_before_external_group_by</code>参数。在内存占用超出此阈值之后，就会spill到磁盘继续操作，且性能没有降低特别多。官方建议将它设置为<code>max_memory_usage</code>的一半。</p>
<h5>存储</h5>
<p>CK不太挑存储介质，普通7200rpm SATA HDD都可以用，也可以配置磁盘阵列，建议RAID10或者RAID6。但是如果为了快速响应，或者多数查询的数据量都很大，还是建议上SSD（我们就是如此）。另外，CK还支持基于配置文件的多盘存储、冷热数据分离和存储策略（storage policy）设置，在特定场景下可能会很有用。我们未实操过，不多讲了。</p>
<h5>ZooKeeper</h5>
<p>千万要调教好ZooKeeper集群，一旦ZK不可用，复制表和分布式表就不可用了。ZK的数据量基本上与CK的数据量成正相关，所以一定要配置自动清理：</p>
<pre><code class="cpp">autopurge.purgeInterval = 1
autopurge.snapRetainCount = 5
</code></pre>
<p>另外，ZK的log文件和snapshot文件建议分不同的盘存储，尽量减少follower从leader同步的磁盘压力，且余量必须要留足，毕竟硬盘的成本不算高。</p>
<h3>The End</h3>
<p>上文中还涉及到一些比较重要的知识点，如MergeTree索引的结构，JOIN语句的执行过程，CK与ZK的交互等等，今后有时间会分别写文章详细讲解。</p>
<p>618之前事情一直都会比较多，希望一切顺利。今天先这样吧。</p>
<p>民那晚安晚安。</p>
  
</div>
            