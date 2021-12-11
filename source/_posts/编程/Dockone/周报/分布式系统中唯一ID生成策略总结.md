
---
title: '分布式系统中唯一ID生成策略总结'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/f7d992ee11b708684d32979dbd84cb36.png'
author: Dockone
comments: false
date: 2021-12-11 00:26:23
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/f7d992ee11b708684d32979dbd84cb36.png'
---

<div>   
<br><h3>全局唯一ID介绍</h3>系统唯一ID是我们在设计阶段常常遇到的问题。在复杂的分布式系统中，几乎都需要对大量的数据和消息进行唯一标识。在设计初期，我们需要考虑日后数据量的级别，如果可能会对数据进行分库分表，那么就需要有一个全局唯一ID来标识一条数据或记录。生成唯一id的策略有多种，但是每种策略都有它的适用场景、优点以及局限性。<br>
<h4>全局唯一id特点</h4><ul><li>全局唯一性：不能出现重复的ID号，既然是唯一标识，这是最基本的要求；</li><li>趋势递增：在MySQL InnoDB引擎中使用的是聚集索引，由于多数RDBMS使用B-tree的数据结构来存储索引数据，在主键的选择上面我们应该尽量使用有序的主键保证写入性能；</li><li>单调递增：保证下一个ID一定大于上一个ID，例如事务版本号、IM增量消息、排序等特殊需求；</li><li>信息安全：如果ID是连续的，恶意用户的扒取工作就非常容易做了，直接按照顺序下载指定URL即可；如果是订单号就更危险了，竞对可以直接知道我们一天的单量。所以在一些应用场景下，会需要ID无规则、不规则；</li><li>高可用性：同时除了对ID号码自身的要求，业务还对ID号生成系统的可用性要求极高，想象一下，如果ID生成系统瘫痪，这就会带来一场灾难。所以不能有单点故障；</li><li>分片支持：可以控制ShardingId。比如某一个用户的文章要放在同一个分片内，这样查询效率高，修改也容易；</li><li>长度适中。</li></ul><br>
<br><h3>常见全局唯一ID生成策略</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211207/f7d992ee11b708684d32979dbd84cb36.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/f7d992ee11b708684d32979dbd84cb36.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>数据库自增长序列或字段生成ID</h4>最常见的一种生成ID方式。利用数据库本身来进行设置，在全数据库内保持唯一。<br>
<br>优点：<br>
<ul><li>非常简单。利用现有数据库系统的功能实现，成本小，代码简单，性能可以接受。</li><li>ID号单调递增。可以实现一些对ID有特殊要求的业务，比如对分页或者排序结果这类需求有帮助。</li></ul><br>
<br>缺点：<br>
<ul><li>强依赖DB。不同数据库语法和实现不同，数据库迁移的时候、多数据库版本支持的时候、或分表分库的时候需要处理，会比较麻烦。当DB异常时整个系统不可用，属于致命问题。</li><li>单点故障。在单个数据库或读写分离或一主多从的情况下，只有一个主库可以生成。有单点故障的风险。</li><li>数据一致性问题。配置主从复制可以尽可能的增加可用性，但是数据一致性在特殊情况下难以保证。主从切换时的不一致可能会导致重复发号。</li><li>难于扩展。在性能达不到要求的情况下，比较难于扩展。ID发号性能瓶颈限制在单台MySQL的读写性能。</li></ul><br>
<br>部分优化方案：<br>
<br>针对主库单点， 如果有多个Master库，则每个Master库设置的起始数字不一样，步长一样，可以是Master的个数。比如：Master1生成的是1，4，7，10，Master2生成的是2，5，8，11，Master3生成的是3，6，9，12。这样就可以有效生成集群中的唯一ID，也可以大大降低ID生成数据库操作的负载。<br>
<h4>UUID</h4>常见的生成ID方式，利用程序生成。<br>
<br>UUID（Universally Unique Identifier）的目的，是让分布式系统中的所有元素，都能有唯一的辨识资讯，而不需要透过中央控制端来做辨识资讯的指定。如此一来，每个人都可以建立不与其它人冲突的UUID。在这样的情况下，就不需考虑数据库建立时的名称重复问题。<br>
<br>UUID的标准形式包含32个16进制数字，以连字号分为五段，形式为8-4-4-4-12的36个字符，示例：550e8400-e29b-41d4-a716-446655440000，到目前为止业界一共有5种方式生成UUID，详情见IETF发布的UUID规范：<a href="https://www.omgwiki.org/dido/doku.php?id=dido:public:ra:xapend:xapend.b_stds:tech:ietf:uuid" rel="nofollow" target="_blank">https://www.omgwiki.org/dido/d ... :uuid</a><br>
<br>在Java中我们可以直接使用下面的API生成UUID：<br>
<pre class="prettyprint">UUID uuid  =  UUID.randomUUID(); String s = UUID.randomUUID().toString();<br>
</pre><br>
优点：<br>
<ul><li>非常简单，本地生成，代码方便，API调用方便。</li><li>性能非高。生成的ID性能非常好，没有网络消耗，基本不会有性能问题。</li><li>全球唯一。在数据库迁移、系统数据合并、或者数据库变更的情况下，可以 从容应对。</li></ul><br>
<br>缺点：<br>
<ul><li>存储成本高。UUID太长，16字节128位，通常以36长度的字符串表示，很多场景不适用。如果是海量数据库，就需要考虑存储量的问题。</li><li>信息不安全。基于MAC地址生成UUID的算法可能会造成MAC地址泄露，这个漏洞曾被用于寻找梅丽莎病毒的制作者位置。</li><li>不适用作为主键，ID作为主键时在特定的环境会存在一些问题，比如做DB主键的场景下，UUID就非常不适用。UUID往往是使用字符串存储，查询的效率比较低。</li><li>UUID是无序的。不是单调递增的，而现阶段主流的数据库主键索引都是选用的B+树索引，对于无序长度过长的主键插入效率比较低。<br>
传输数据量大。</li><li><br>不可读。<br>
<br>部分优化方案：</li><li><br>为了解决UUID不可读， 可以使用UUID to Int64的方法。</li><li>为了解决UUID无序的问题， NHibernate在其主键生成方式中提供了Comb算法（combined guid/timestamp）。保留GUID的10个字节，用另6个字节表示GUID生成的时间（DateTime）。</li></ul><br>
<br><h4>Redis生成ID</h4>当使用数据库来生成ID性能不够要求的时候，我们可以尝试使用Redis来生成ID。这主要依赖于Redis是单线程的，所以也可以用生成全局唯一的ID。可以用Redis的原子操作 INCR和INCRBY来实现。<br>
<br>可以使用Redis集群来获取更高的吞吐量。假如一个集群中有5台Redis。可以初始化每台Redis的值分别是1，2，3，4，5，然后步长都是5。各个Redis生成的ID为：<br>
<br>A：1，6，11，16，21<br>
<br>B：2，7，12，17，22<br>
<br>C：3，8，13，18，23<br>
<br>D：4，9，14，19，24<br>
<br>E：5，10，15，20，25<br>
<br>这个负载到哪台机器上需要提前设定好，未来很难做修改。但是3-5台服务器基本能够满足，都可以获得不同的ID。步长和初始值一定需要事先设定好。使用Redis集群也可以防止单点故障的问题。<br>
<br>比较适合使用Redis来生成日切流水号。比如订单号=日期+当日自增长号。可以每天在Redis中生成一个Key，使用INCR进行累加。<br>
<br>优点：<br>
<ul><li>不依赖于数据库，灵活方便，且性能优于数据库。</li><li>数字ID天然排序，对分页或者需要排序的结果很有帮助。</li></ul><br>
<br>缺点：<br>
<ul><li>如果系统中没有Redis，还需要引入新的组件，增加系统复杂度。</li><li>需要编码和配置的工作量比较大。</li><li>Redis单点故障，影响序列服务的可用性。</li></ul><br>
<br><h4>ZooKeeper生成ID</h4>ZooKeeper主要通过其znode数据版本来生成序列号，可以生成32位和64位的数据版本号，客户端可以使用这个版本号来作为唯一的序列号。<br>
<br>很少会使用ZooKeeper来生成唯一ID。主要是由于需要依赖ZooKeeper，并且是多步调用API，如果在竞争较大的情况下，需要考虑使用分布式锁。因此，性能在高并发的分布式环境下，也不甚理想。<br>
<h4>Twitter的Snowflake算法</h4>Snowflake（雪花算法）是Twitter开源的分布式ID生成算法，结果是一个long型的ID。这种方案把64-bit分别划分成多段，分开来标示机器、时间等。如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211207/71d9270baa220efa4a48f9db349d3277.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/71d9270baa220efa4a48f9db349d3277.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
其核心思想是：使用41bit作为毫秒数，10bit作为机器的ID（5个bit是数据中心，5个bit的机器ID），12bit作为毫秒内的流水号（意味着每个节点在每毫秒可以产生 4096 个 ID），最后还有一个符号位，永远是0。具体实现的代码可以参看：<a href="https://github.com/twitter/snowflake" rel="nofollow" target="_blank">https://github.com/twitter/snowflake</a><br>
<br>Snowflake算法可以根据自身项目的需要进行一定的修改。比如估算未来的数据中心个数，每个数据中心的机器数以及统一毫秒可以能的并发数来调整在算法中所需要的bit数。<br>
<br>优点：<br>
<ul><li>稳定性高，不依赖于数据库等第三方系统，以服务的方式部署，稳定性更高，生成ID的性能也是非常高的。</li><li>灵活方便，可以根据自身业务特性分配bit位。</li><li>单机上ID单调自增，毫秒数在高位，自增序列在低位，整个ID都是趋势递增的。</li></ul><br>
<br>缺点*：<br>
<ul><li>强依赖机器时钟，如果机器上时钟回拨，会导致发号重复或者服务会处于不可用状态。</li><li>ID可能不是全局递增。在单机上是递增的，但是由于涉及到分布式环境，每台机器上的时钟不可能完全同步，也许有时候也会出现不是全局递增的情况。</li></ul><br>
<br>原文链接：<a href="https://blog.csdn.net/LZ15932161597/article/details/113397226" rel="nofollow" target="_blank">https://blog.csdn.net/LZ159321 ... 97226</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            