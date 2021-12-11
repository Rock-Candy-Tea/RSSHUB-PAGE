
---
title: 'CosId 1.4.5 发布，通用、灵活、高性能的分布式 ID 生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/1210/215357_d7f04332_384561.png'
author: 开源中国
comments: false
date: Sat, 11 Dec 2021 07:43:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/1210/215357_d7f04332_384561.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0px; margin-right:0px; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId">CosId</a><span> </span>通用、灵活、高性能的<strong>分布式ID</strong>生成器</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新内容（v1.4.5） 🎉 🎉 🎉</h2> 
<div style="text-align:start"> 
 <ul> 
  <li>新增<span> </span><code>CosIdIntervalShardingAlgorithm</code><span> 算法</span>实现<span> </span><code>org.apache.shardingsphere.sharding.spi.ShardingAlgorithm</code><span> </span>以提升<code>INTERVAL</code>性能与易用性。<br> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/1210/215357_d7f04332_384561.png" referrerpolicy="no-referrer"> 
   <ul> 
    <li>易用性: 原生支持多种数据类型 (<code>Long</code>、<code>LocalDateTime</code>、<code>Date</code>)，而官方实现是先转换成字符串再转换成<code>LocalDateTime</code>，转换成功率受时间格式化字符影响。</li> 
    <li>性能 : 相比于官方实现<code>org.apache.shardingsphere.sharding.algorithm.sharding.datetime.IntervalShardingAlgorithm</code><span> </span>性能至少高出<span> </span><em>1200~4000</em><span> </span>倍。<br> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/1210/222953_69c4910d_384561.png" referrerpolicy="no-referrer"></li> 
    <li>基于间隔的时间范围分片算法</li> 
    <li><code>DateIntervalShardingAlgorithm</code><span> </span>(COSID_INTERVAL_DATE)</li> 
    <li><code>LocalDateTimeIntervalShardingAlgorithm</code><span> </span>(COSID_INTERVAL_LDT)</li> 
    <li><code>SnowflakeIntervalShardingAlgorithm</code><span> </span>(COSID_INTERVAL_SNOWFLAKE)</li> 
    <li><code>TimestampIntervalShardingAlgorithm</code><span> </span>(COSID_INTERVAL_TS)</li> 
    <li><code>TimestampOfSecondIntervalShardingAlgorithm</code><span> </span>(COSID_INTERVAL_TS_SECOND)</li> 
   </ul> </li> 
 </ul> 
 <div> 
  <pre><code><span style="color:#dd1144">spring:</span>
<span>  shardingsphere:</span>
<span>    rules:</span>
<span>      sharding:</span>
        sharding-<span style="color:#dd1144">algorithms:</span>
          alg-<span style="color:#dd1144">name:</span>
<span>            type:</span> COSID_INTERVAL_&#123;type_suffix&#125;
<span>            props:</span>
              logic-<span style="color:#dd1144">name:</span> logic-name
              id-<span style="color:#dd1144">name:</span> cosid-name
              datetime-<span style="color:#dd1144">lower:</span> <span style="color:#008080">2021</span>-<span style="color:#008080">12</span>-<span style="color:#008080">08</span><span style="color:#dd1144">T22:</span><span style="color:#008080">00</span>:<span style="color:#008080">00</span>
              datetime-<span style="color:#dd1144">upper:</span> <span style="color:#008080">2022</span>-<span style="color:#008080">12</span>-<span style="color:#008080">01</span><span style="color:#dd1144">T00:</span><span style="color:#008080">00</span>:<span style="color:#008080">00</span>
              sharding-suffix-<span style="color:#dd1144">pattern:</span> _yyyyMM
              datetime-interval-<span style="color:#dd1144">unit:</span> MONTHS
              datetime-interval-<span style="color:#dd1144">amount:</span> <span style="color:#008080">1</span>
</code>
</pre> 
 </div> 
 <ul> 
  <li>新增基准测试:<code>CosIdIntervalShardingAlgorithm</code><span> </span>VS<span> </span><code>org.apache.shardingsphere.sharding.algorithm.sharding.datetime.IntervalShardingAlgorithm</code></li> 
 </ul> 
 <div> 
  <pre><code><span style="color:#55cde3">gradle</span> <span style="color:#55cde3">cosid-shardingsphere</span><span>:jmh</span></code></pre> 
 </div> 
 <div> 
  <pre><code><strong style="color:#999999"># JMH version: 1.29</strong>
<strong style="color:#999999"># VM version: JDK 11.0.13, OpenJDK 64-Bit Server VM, 11.0.13+8-LTS</strong>
<strong style="color:#999999"># VM options: -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/work/CosId/cosid-shardingsphere/build/tmp/jmh -Duser.country=CN -Duser.language=zh -Duser.variant</strong>
<strong style="color:#999999"># Blackhole mode: full + dont-inline hint</strong>
<strong style="color:#999999"># Warmup: 1 iterations, 10 s each</strong>
<strong style="color:#999999"># Measurement: 1 iterations, 10 s each</strong>
<strong style="color:#999999"># Timeout: 10 min per iteration</strong>
<strong style="color:#999999"># Threads: 1 thread, will synchronize iterations</strong>
<strong style="color:#999999"># Benchmark mode: Throughput, ops/time</strong>
Benchmark                                                          Mode  Cnt         Score   Error  Units
IntervalShardingAlgorithmBenchmark.cosid_precise_local_date_time  thrpt       <span style="color:#008080">66276995.822</span>          ops/s
IntervalShardingAlgorithmBenchmark.cosid_precise_timestamp        thrpt       <span style="color:#008080">24841952.001</span>          ops/s
IntervalShardingAlgorithmBenchmark.cosid_range_local_date_time    thrpt        <span style="color:#008080">3344013.803</span>          ops/s
IntervalShardingAlgorithmBenchmark.cosid_range_timestamp          thrpt        <span style="color:#008080">2846453.298</span>          ops/s
IntervalShardingAlgorithmBenchmark.office_precise_timestamp       thrpt           <span style="color:#008080">6286.861</span>          ops/s
IntervalShardingAlgorithmBenchmark.office_range_timestamp         thrpt           <span style="color:#008080">2302.986</span>          ops/s
</code>
</pre> 
 </div> 
 <ul> 
  <li>API调整: 开放接口<span> </span><code>SnowflakeFriendlyId.getParser</code></li> 
  <li>修复： <code>JdbcIdSegmentInitializer</code>构造函数赋值错误问题<span> </span><a href="https://gitee.com/AhooWang/CosId/issues/I4LVBZ">#I4LVBZ:jdbc模式无法自动创建表</a><span> </span>(CosIdJdbcSegmentAutoConfiguration,jdbcIdSegmentInitializer)</li> 
 </ul> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">简介</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><em><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId">CosId</a></em><span> </span>旨在提供通用、灵活、高性能的分布式 ID 生成器。 目前提供了俩类 ID 生成器：</p> 
<ul> 
 <li><code>SnowflakeId</code><span> </span>:<span> </span><em>单机 TPS 性能：409W/s</em><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%2Fblob%2Fmain%2FREADME.zh-CN.md%23jmh-benchmark">JMH 基准测试</a><span> </span>, 主要解决<span> </span><em>时钟回拨问题</em><span> </span>、<em>机器号分配问题</em><span> </span>并且提供更加友好、灵活的使用体验。</li> 
 <li><code>SegmentId</code>: 每次获取一段 (<code>Step</code>) ID，来降低号段分发器的网络IO请求频次提升性能。 
  <ul> 
   <li><code>IdSegmentDistributor</code>: 号段分发器（号段存储器） 
    <ul> 
     <li><code>RedisIdSegmentDistributor</code>: 基于<span> </span><em>Redis</em><span> </span>的号段分发器。</li> 
     <li><code>JdbcIdSegmentDistributor</code>: 基于<span> </span><em>Jdbc</em><span> </span>的号段分发器，支持各种关系型数据库。</li> 
    </ul> </li> 
   <li><code>SegmentChainId</code>(<strong>推荐</strong>):<code>SegmentChainId</code><span> </span>(<em>lock-free</em>) 是对<span> </span><code>SegmentId</code><span> </span>的增强。性能可达到近似<span> </span><code>AtomicLong</code><span> </span>的<span> </span><em>TPS 性能:12743W+/s</em><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%2Fblob%2Fmain%2FREADME.zh-CN.md%23jmh-benchmark">JMH 基准测试</a><span> </span>。 
    <ul> 
     <li><code>PrefetchWorker</code><span> </span>维护安全距离(<code>safeDistance</code>), 并且支持基于饥饿状态的动态<code>safeDistance</code>扩容/收缩。</li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/AhooWang/CosId/blob/main/wiki/getting-started.md">快速开始</a></h2> 
<h2 style="margin-left:0; margin-right:0; text-align:left">背景（为什么需要<em>分布式ID</em>）</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">在软件系统演进过程中，随着业务规模的增长，我们需要进行集群化部署来分摊计算、存储压力，应用服务我们可以很轻松做到无状态、弹性伸缩。 但是仅仅增加服务副本数就够了吗？显然不够，因为性能瓶颈往往是在数据库层面，那么这个时候我们就需要考虑如何进行数据库的扩容、伸缩、集群化，通常使用分库、分表的方式来处理。 那么我如何分片(水平分片，当然还有垂直分片不过不是本文需要讨论的内容)呢，分片得前提是我们得先有一个ID，然后才能根据分片算法来分片。（比如比较简单常用的ID取模分片算法，这个跟Hash算法的概念类似，我们得先有key才能进行Hash取得插入槽位。）</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">当然还有很多分布式场景需要<em>分布式ID</em>，这里不再一一列举。</p> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:left">分布式ID方案的核心指标</h2> 
<ul> 
 <li><strong>全局（相同业务）唯一性</strong>：唯一性保证是<strong>ID</strong>的必要条件，假设ID不唯一就会产生主键冲突，这点很容易可以理解。 
  <ul> 
   <li>通常所说的全局唯一性并不是指所有业务服务都要唯一，而是相同业务服务不同部署副本唯一。 比如 Order 服务的多个部署副本在生成<code>t_order</code>这张表的<code>Id</code>时是要求全局唯一的。至于<code>t_order_item</code>生成的<code>ID</code>与<code>t_order</code>是否唯一，并不影响唯一性约束，也不会产生什么副作用。 不同业务模块间也是同理。即唯一性主要解决的是ID冲突问题。</li> 
  </ul> </li> 
 <li><strong>有序性</strong>：有序性保证是面向查询的数据结构算法（除了Hash算法）所必须的，是<strong>二分查找法</strong>(分而治之)的前提。 
  <ul> 
   <li>MySq-InnoDB B+树是使用最为广泛的，假设 Id 是无序的，B+ 树 为了维护 ID 的有序性，就会频繁的在索引的中间位置插入而挪动后面节点的位置，甚至导致频繁的页分裂，这对于性能的影响是极大的。那么如果我们能够保证ID的有序性这种情况就完全不同了，只需要进行追加写操作。所以 ID 的有序性是非常重要的，也是ID设计不可避免的特性。</li> 
  </ul> </li> 
 <li><strong>吞吐量/性能(ops/time)</strong>：即单位时间（每秒）能产生的ID数量。生成ID是非常高频的操作，也是最为基本的。假设ID生成的性能缓慢，那么不管怎么进行系统优化也无法获得更好的性能。 
  <ul> 
   <li>一般我们会首先生成ID，然后再执行写入操作，假设ID生成缓慢，那么整体性能上限就会受到限制，这一点应该不难理解。</li> 
  </ul> </li> 
 <li><strong>稳定性(time/op)</strong>：稳定性指标一般可以采用<strong>每个操作的时间进行百分位采样</strong>来分析，比如<span> </span><em><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId">CosId</a></em><span> </span>百分位采样<span> </span><strong>P9999=0.208 us/op</strong>，即<span> </span><strong>0% ~ 99.99%</strong><span> </span>的单位操作时间小于等于<span> </span><strong>0.208 us/op</strong>。 
  <ul> 
   <li><a href="https://gitee.com/link?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E7%2599%25BE%25E5%2588%2586%25E4%25BD%258D%25E6%2595%25B0">百分位数 WIKI</a><span> </span>：统计学术语，若将一组数据从小到大排序，并计算相应的累计百分点，则某百分点所对应数据的值，就称为这百分点的百分位数，以Pk表示第k百分位数。百分位数是用来比较个体在群体中的相对地位量数。</li> 
   <li>为什么不用平均<em>每个操作的时间</em>：马老师的身价跟你的身价能平均么？平均后的值有意义不？</li> 
   <li>可以使用最小<em>每个操作的时间</em>、最大<em>每个操作的时间</em>作为参考吗？因为最小、最大值只说明了零界点的情况，虽说可以作为稳定性的参考，但依然不够全面。而且<em>百分位数</em>已经覆盖了这俩个指标。</li> 
  </ul> </li> 
 <li><strong>自治性（依赖）</strong>：主要是指对外部环境有无依赖，比如<strong>号段模式</strong>会强依赖第三方存储中间件来获取<code>NexMaxId</code>。自治性还会对可用性造成影响。</li> 
 <li><strong>可用性</strong>：分布式ID的可用性主要会受到自治性影响，比如<strong>SnowflakeId</strong>会受到时钟回拨影响，导致处于短暂时间的不可用状态。而<strong>号段模式</strong>会受到第三方发号器（<code>NexMaxId</code>）的可用性影响。 
  <ul> 
   <li><a href="https://gitee.com/link?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%258F%25AF%25E7%2594%25A8%25E6%2580%25A7">可用性 WIKI</a><span> </span>：在一个给定的时间间隔内，对于一个功能个体来讲，总的可用时间所占的比例。</li> 
   <li>MTBF：平均故障间隔</li> 
   <li>MDT：平均修复/恢复时间</li> 
   <li>Availability=MTBF/(MTBF+MDT)</li> 
   <li>假设MTBF为1年，MDT为1小时，即<code>Availability=(365*24)/(365*24+1)=0.999885857778792≈99.99%</code>，也就是我们通常所说对可用性4个9。</li> 
  </ul> </li> 
 <li><strong>适应性</strong>：是指在面对外部环境变化的自适应能力，这里我们主要说的是面对流量突发时动态伸缩分布式ID的性能， 
  <ul> 
   <li><strong>SegmentChainId</strong>可以基于<strong>饥饿状态</strong>进行<strong>安全距离</strong>的动态伸缩。</li> 
   <li><strong>SnowflakeId</strong>常规位分配方案性能恒定409.6W，虽然可以通过调整位分配方案来获得不同的TPS性能，但是位分配方法的变更是破坏性的，一般根据业务场景确定位分配方案后不再变更。</li> 
  </ul> </li> 
 <li><strong>存储空间</strong>：还是用MySq-InnoDB B+树来举例，普通索引（二级索引）会存储主键值，主键越大占用的内存缓存、磁盘空间也会越大。Page页存储的数据越少，磁盘IO访问的次数会增加。总之在满足业务需求的情况下，尽可能小的存储空间占用在绝大多数场景下都是好的设计原则。</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">不同分布式ID方案核心指标对比</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>分布式ID</th> 
   <th>全局唯一性</th> 
   <th>有序性</th> 
   <th>吞吐量</th> 
   <th>稳定性（1s=1000,000us）</th> 
   <th>自治性</th> 
   <th>可用性</th> 
   <th>适应性</th> 
   <th>存储空间</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">UUID/GUID</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">是</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">完全无序</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3078638(ops/s)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">P9999=0.325(us/op)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">完全自治</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">100%</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">否</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">128-bit</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">SnowflakeId</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">是</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">本地单调递增，全局趋势递增(受全局时钟影响)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">4096000(ops/s)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">P9999=0.244(us/op)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">依赖时钟</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">时钟回拨会导致短暂不可用</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">否</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">64-bit</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">SegmentId</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">是</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">本地单调递增，全局趋势递增(受Step影响)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">29506073(ops/s)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">P9999=46.624(us/op)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">依赖第三方号段分发器</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">受号段分发器可用性影响</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">否</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">64-bit</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">SegmentChainId</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">是</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">本地单调递增，全局趋势递增(受Step、安全距离影响)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">127439148(ops/s)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">P9999=0.208(us/op)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">依赖第三方号段分发器</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">受号段分发器可用性影响，但因安全距离存在，预留ID段，所以高于SegmentId</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">是</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">64-bit</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="margin-left:0; margin-right:0; text-align:left">有序性(要想分而治之·二分查找法，必须要维护我)</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">刚刚我们已经讨论了ID有序性的重要性，所以我们设计ID算法时应该尽可能地让ID是单调递增的，比如像表的自增主键那样。但是很遗憾，因全局时钟、性能等分布式系统问题，我们通常只能选择局部单调递增、全局趋势递增的组合（就像我们在分布式系统中不得不的选择最终一致性那样）以获得多方面的权衡。下面我们来看一下什么是单调递增与趋势递增。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">有序性之单调递增</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="单调递增" src="https://gitee.com/AhooWang/CosId/raw/main/wiki/img/monotonically-increasing.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">单调递增：T表示全局绝对时点，假设有Tn+1>Tn（绝对时间总是往前进的，这里不考虑相对论、时间机器等），那么必然有F(Tn+1)>F(Tn)，数据库自增主键就属于这一类。 另外需要特别说明的是单调递增跟连续性递增是不同的概念。 连续性递增：<code>F(n+1)=(F(n)+step)</code>即下一次获取的ID一定等于当前<code>ID+Step</code>，当<code>Step=1</code>时类似于这样一个序列:<code>1->2->3->4->5</code>。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">扩展小知识：数据库的自增主键也不是连续性递增的，相信你一定遇到过这种情况，请思考一下数据库为什么这样设计？</p> 
</blockquote> 
<h4 style="margin-left:0; margin-right:0; text-align:left">有序性之趋势递增</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="趋势递增" src="https://gitee.com/AhooWang/CosId/raw/main/wiki/img/trend-increasing.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">趋势递增：Tn>Tn-s，那么大概率有F(Tn)>F(Tn-s)。虽然在一段时间间隔内有乱序，但是整体趋势是递增。从上图上看，是有上升趋势的（趋势线）。</p> 
<ul> 
 <li>在<strong>SnowflakeId</strong>中n-s受到全局时钟同步影响。</li> 
 <li>在号段模式(<strong>SegmentId</strong>)中n-s受到号段可用区间(<code>Step</code>)影响。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">分布式ID分配方案</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">UUID/GUID</h3> 
<ul> 
 <li><img alt="👍" height="14" src="https://assets.gitee.com/assets/emoji/thumbsup-f866ad23f6584fa15376ddb4738e53cf.png" width="14" referrerpolicy="no-referrer">不依赖任何第三方中间件</li> 
 <li><img alt="👍" height="14" src="https://assets.gitee.com/assets/emoji/thumbsup-f866ad23f6584fa15376ddb4738e53cf.png" width="14" referrerpolicy="no-referrer">性能高</li> 
 <li><img alt="👎" height="14" src="https://assets.gitee.com/assets/emoji/thumbsdown-da41668c7715a2e470f020d398f74f74.png" width="14" referrerpolicy="no-referrer">完全无序</li> 
 <li><img alt="👎" height="14" src="https://assets.gitee.com/assets/emoji/thumbsdown-da41668c7715a2e470f020d398f74f74.png" width="14" referrerpolicy="no-referrer">空间占用大，需要占用128位存储空间。</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">UUID最大的缺陷是随机的、无序的，当用于主键时会导致数据库的主键索引效率低下（为了维护索引树，频繁的索引中间位置插入数据，而不是追加写）。这也是UUID不适用于数据库主键的最为重要的原因。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">SnowflakeId</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="Snowflake" src="https://gitee.com/AhooWang/CosId/raw/main/docs/Snowflake-identifier.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><em>SnowflakeId</em>使用<code>Long</code>（64-bit）位分区来生成ID的一种分布式ID算法。 通用的位分配方案为：<code>timestamp</code>(41-bit)+<code>machineId</code>(10-bit)+<code>sequence</code>(12-bit)=63-bit。</p> 
</blockquote> 
<ul> 
 <li>41-bit<code>timestamp</code>=(1L<<41)/(1000/3600/365)，约可以存储69年的时间戳，即可以使用的绝对时间为<code>EPOCH</code>+69年，一般我们需要自定义<code>EPOCH</code>为产品开发时间，另外还可以通过压缩其他区域的分配位数，来增加时间戳位数来延长可用时间。</li> 
 <li>10-bit<code>machineId</code>=(1L<<10)=1024，即相同业务可以部署1024个副本(在Kubernetes概念里没有主从副本之分，这里直接沿用Kubernetes的定义)。一般情况下没有必要使用这么多位，所以会根据部署规模需要重新定义。</li> 
 <li>12-bit<code>sequence</code>=(1L<<12)*1000=4096000，即单机每秒可生成约409W的ID，全局同业务集群可产生<code>4096000*1024=419430W=41.9亿(TPS)</code>。</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">从<span> </span><em>SnowflakeId</em><span> </span>设计上可以看出:</p> 
<ul> 
 <li><img alt="👍" height="14" src="https://assets.gitee.com/assets/emoji/thumbsup-f866ad23f6584fa15376ddb4738e53cf.png" width="14" referrerpolicy="no-referrer"><code>timestamp</code>在高位，单实例<em>SnowflakeId</em>是会保证时钟总是向前的（校验本机时钟回拨），所以是本机单调递增的。受全局时钟同步/时钟回拨影响<em>SnowflakeId</em>是全局趋势递增的。</li> 
 <li><img alt="👍" height="14" src="https://assets.gitee.com/assets/emoji/thumbsup-f866ad23f6584fa15376ddb4738e53cf.png" width="14" referrerpolicy="no-referrer"><em>SnowflakeId</em>不对任何第三方中间件有强依赖关系，并且性能也非常高。</li> 
 <li><img alt="👍" height="14" src="https://assets.gitee.com/assets/emoji/thumbsup-f866ad23f6584fa15376ddb4738e53cf.png" width="14" referrerpolicy="no-referrer">位分配方案可以按照业务系统需要灵活配置，来达到最优使用效果。</li> 
 <li><img alt="👎" height="14" src="https://assets.gitee.com/assets/emoji/thumbsdown-da41668c7715a2e470f020d398f74f74.png" width="14" referrerpolicy="no-referrer">强依赖本机时钟，潜在的时钟回拨问题会导致ID重复、处于短暂的不可用状态。</li> 
 <li><img alt="👎" height="14" src="https://assets.gitee.com/assets/emoji/thumbsdown-da41668c7715a2e470f020d398f74f74.png" width="14" referrerpolicy="no-referrer"><code>machineId</code>需要手动设置，实际部署时如果采用手动分配<code>machineId</code>，会非常低效。</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">SnowflakeId之机器号分配问题</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">在<strong>SnowflakeId</strong>中根据业务设计的位分配方案确定了基本上就不再有变更了，也很少需要维护。但是<code>machineId</code>总是需要配置的，而且集群中是不能重复的，否则分区原则就会被破坏而导致ID唯一性原则破坏，当集群规模较大时<code>machineId</code>的维护工作是非常繁琐，低效的。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">有一点需要特别说明的，<strong>SnowflakeId</strong>的<strong>MachineId</strong>是逻辑上的概念，而不是物理概念。 想象一下假设<strong>MachineId</strong>是物理上的，那么意味着一台机器拥有只能拥有一个<strong>MachineId</strong>，那会产生什么问题呢？</p> 
</blockquote> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">目前<span> </span><em><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId">CosId</a></em><span> </span>提供了以下三种<span> </span><code>MachineId</code><span> </span>分配器。</p> 
</blockquote> 
<ul> 
 <li>ManualMachineIdDistributor: 手动配置<code>machineId</code>，一般只有在集群规模非常小的时候才有可能使用，不推荐。</li> 
 <li>StatefulSetMachineIdDistributor: 使用<code>Kubernetes</code>的<code>StatefulSet</code>提供的稳定的标识ID（HOSTNAME=service-01）作为机器号。</li> 
 <li>RedisMachineIdDistributor: 使用<strong>Redis</strong>作为机器号的分发存储，同时还会存储<code>MachineId</code>的上一次时间戳，用于<strong>启动时时钟回拨</strong>的检查。</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="RedisMachineIdDistributor" src="https://gitee.com/AhooWang/CosId/raw/main/docs/RedisMachineIdDistributor.png" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">SnowflakeId之时钟回拨问题</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">时钟回拨的致命问题是会导致ID重复、冲突（这一点不难理解），ID重复显然是不能被容忍的。 在<strong>SnowflakeId</strong>算法中，按照<strong>MachineId</strong>分区ID，我们不难理解的是不同<strong>MachineId</strong>是不可能产生相同ID的。所以我们解决的时钟回拨问题是指当前<strong>MachineId</strong>的时钟回拨问题，而不是所有集群节点的时钟回拨问题。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>MachineId</strong>时钟回拨问题大体可以分为俩种情况：</p> 
<ul> 
 <li>运行时时钟回拨：即在运行时获取的当前时间戳比上一次获取的时间戳小。这个场景的时钟回拨是很容易处理的，一般<strong>SnowflakeId</strong>代码实现时都会存储<code>lastTimestamp</code>用于运行时时钟回拨的检查，并抛出时钟回拨异常。 
  <ul> 
   <li>时钟回拨时直接抛出异常是不太好地实践，因为下游使用方几乎没有其他处理方案（噢，我还能怎么办呢，等吧），时钟同步是唯一的选择，当只有一种选择时就不要再让用户选择了。</li> 
   <li><code>ClockSyncSnowflakeId</code>是<code>SnowflakeId</code>的包装器，当发生时钟回拨时会使用<code>ClockBackwardsSynchronizer</code>主动等待时钟同步来重新生成ID，提供更加友好的使用体验。</li> 
  </ul> </li> 
 <li>启动时时钟回拨：即在启动服务实例时获取的当前时钟比上次关闭服务时小。此时的<code>lastTimestamp</code>是无法存储在进程内存中的。当获取的外部存储的<strong>机器状态</strong>大于当前时钟时钟时，会使用<code>ClockBackwardsSynchronizer</code>主动同步时钟。 
  <ul> 
   <li>LocalMachineStateStorage：使用本地文件存储<code>MachineState</code>(机器号、最近一次时间戳)。因为使用的是本地文件所以只有当实例的部署环境是稳定的，<code>LocalMachineStateStorage</code>才适用。</li> 
   <li>RedisMachineIdDistributor：将<code>MachineState</code>存储在<strong>Redis</strong>分布式缓存中，这样可以保证总是可以获取到上次服务实例停机时<strong>机器状态</strong>。</li> 
  </ul> </li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">SnowflakeId之JavaScript数值溢出问题</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><code>JavaScript</code>的<code>Number.MAX_SAFE_INTEGER</code>只有53-bit，如果直接将63位的<code>SnowflakeId</code>返回给前端，那么会产生值溢出的情况（所以这里我们应该知道后端传给前端的<code>long</code>值溢出问题，<strong>迟早</strong>会出现，只不过SnowflakeId出现得更快而已）。 很显然溢出是不能被接受的，一般可以使用以下俩种处理方案：</p> 
<ul> 
 <li>将生成的63-bit<code>SnowflakeId</code>转换为<code>String</code>类型。 
  <ul> 
   <li>直接将<code>long</code>转换成<code>String</code>。</li> 
   <li>使用<code>SnowflakeFriendlyId</code>将<code>SnowflakeId</code>转换成比较友好的字符串表示：<code>&#123;timestamp&#125;-&#123;machineId&#125;-&#123;sequence&#125; -> 20210623131730192-1-0</code></li> 
  </ul> </li> 
 <li>自定义<code>SnowflakeId</code>位分配来缩短<code>SnowflakeId</code>的位数（53-bit）使<span> </span><code>ID</code><span> </span>提供给前端时不溢出 
  <ul> 
   <li>使用<code>SafeJavaScriptSnowflakeId</code>(<code>JavaScript</code><span> </span>安全的<span> </span><code>SnowflakeId</code>)</li> 
  </ul> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">号段模式（SegmentId）</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="SegmentId" src="https://gitee.com/AhooWang/CosId/raw/main/docs/SegmentId.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">从上面的设计图中，不难看出<strong>号段模式</strong>基本设计思路是通过每次获取一定长度（Step）的可用ID（Id段/号段），来降低网络IO请求次数，提升性能。</p> 
<ul> 
 <li><img alt="👎" height="14" src="https://assets.gitee.com/assets/emoji/thumbsdown-da41668c7715a2e470f020d398f74f74.png" width="14" referrerpolicy="no-referrer">强依赖第三方号段分发器，可用性受到第三方分发器影响。</li> 
 <li><img alt="👎" height="14" src="https://assets.gitee.com/assets/emoji/thumbsdown-da41668c7715a2e470f020d398f74f74.png" width="14" referrerpolicy="no-referrer">每次号段用完时获取<code>NextMaxId</code>需要进行网络IO请求，此时的性能会比较低。</li> 
 <li>单实例ID单调递增，全局趋势递增。 
  <ul> 
   <li>从设计图中不难看出<strong>Instance 1</strong>每次获取的<code>NextMaxId</code>，一定比上一次大，意味着下一次的号段一定比上一次大，所以从单实例上来看是单调递增的。</li> 
   <li>多实例各自持有的不同的号段，意味着同一时刻不同实例生成的ID是乱序的，但是整体趋势的递增的，所以全局趋势递增。</li> 
  </ul> </li> 
 <li>ID乱序程度受到Step长度以及集群规模影响（从趋势递增图中不难看出）。 
  <ul> 
   <li>假设集群中只有一个实例时<strong>号段模式</strong>就是单调递增的。</li> 
   <li><code>Step</code>越小，乱序程度越小。当<code>Step=1</code>时，将无限接近单调递增。需要注意的是这里是无限接近而非等于单调递增，具体原因你可以思考一下这样一个场景： 
    <ul> 
     <li>号段分发器T1时刻给<strong>Instance 1</strong>分发了<code>ID=1</code>,T2时刻给<strong>Instance 2</strong>分发了<code>ID=2</code>。因为机器性能、网络等原因，<code>Instance 2</code>网络IO写请求先于<code>Instance 1</code>到达。那么这个时候对于数据库来说，ID依然是乱序的。</li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">号段链模式（SegmentChainId）</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/AhooWang/CosId/blob/main/wiki/SegmentChainId.zh-CN.md">分布式ID(CosId)之号段链模式性能(1.2亿/s)解析</a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="SegmentChainId" src="https://gitee.com/AhooWang/CosId/raw/main/docs/SegmentChainId.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>SegmentChainId</strong>是<strong>SegmentId</strong>增强版，相比于<strong>SegmentId</strong>有以下优势：</p> 
<ul> 
 <li>稳定性：<strong>SegmentId</strong>的稳定性问题（P9999=46.624(us/op)）主要是因为号段用完之后同步进行<code>NextMaxId</code>的获取导致的（会产生网络IO）。 
  <ul> 
   <li><strong>SegmentChainId</strong><span> </span>（P9999=0.208(us/op)）引入了新的角色<strong>PrefetchWorker</strong>用以维护和保证<strong>安全距离</strong>，理想情况下使得获取ID的线程几乎完全不需要进行同步的等待<code>NextMaxId</code>获取，性能可达到近似<span> </span><code>AtomicLong</code><span> </span>的<span> </span><em>TPS 性能:12743W+/s</em><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%2Fblob%2Fmain%2FREADME.zh-CN.md%23jmh-benchmark">JMH 基准测试</a><span> </span>。</li> 
  </ul> </li> 
 <li>适应性：从<strong>SegmentId</strong>介绍中我们知道了影响<strong>ID乱序</strong>的因素有俩个：集群规模、<code>Step</code>大小。集群规模是我们不能控制的，但是<code>Step</code>是可以调节的。 
  <ul> 
   <li><code>Step</code>应该近可能小才能使得<strong>ID单调递增</strong>的可能性增大。</li> 
   <li><code>Step</code>太小会影响吞吐量，那么我们如何合理设置<code>Step</code>呢？答案是我们无法准确预估所有时点的吞吐量需求，那么最好的办法是吞吐量需求高时，Step自动增大，吞吐量低时Step自动收缩。</li> 
   <li><strong>SegmentChainId</strong>引入了<strong>饥饿状态</strong>的概念，<strong>PrefetchWorker</strong>会根据<strong>饥饿状态</strong>检测当前<strong>安全距离</strong>是否需要膨胀或者收缩，以便获得吞吐量与有序性之间的权衡，这便是<strong>SegmentChainId</strong>的自适应性。</li> 
  </ul> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">集成</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">CosIdPlugin（MyBatis 插件）</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Kotlin DSL</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre><span>    <strong style="color:#cccccc">implementation</strong><span style="color:#eeeeee">(</span><span style="background-color:transparent; color:#00aadd">"me.ahoo.cosid:cosid-mybatis:$&#123;cosidVersion&#125;"</span><span style="color:#eeeeee">)</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong>public</strong> <strong>class</strong> <strong style="color:#cccccc">Order</strong> <span>&#123;</span></span>

<span>    <span>@CosId</span><span>(</span><span>value</span> <span>=</span> <span style="background-color:transparent; color:#00aadd">"order"</span><span>)</span></span>
<span>    <strong>private</strong> <strong style="color:#cccccc">Long</strong> <span>orderId</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#cccccc">Long</strong> <span>userId</span><span>;</span></span>

<span>    <strong>public</strong> <strong style="color:#cccccc">Long</strong> <strong style="color:#cccccc">getOrderId</strong><span>()</span> <span>&#123;</span></span>
<span>        <strong style="color:#cda869">return</strong> <span>orderId</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <strong>public</strong> <strong style="color:#445588">void</strong> <strong style="color:#cccccc">setOrderId</strong><span>(</span><strong style="color:#cccccc">Long</strong> <span>orderId</span><span>)</span> <span>&#123;</span></span>
<span>        <strong style="color:#cda869">this</strong><span>.</span><span style="color:#008080">orderId</span> <span>=</span> <span>orderId</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <strong>public</strong> <strong style="color:#cccccc">Long</strong> <strong style="color:#cccccc">getUserId</strong><span>()</span> <span>&#123;</span></span>
<span>        <strong style="color:#cda869">return</strong> <span>userId</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <strong>public</strong> <strong style="color:#445588">void</strong> <strong style="color:#cccccc">setUserId</strong><span>(</span><strong style="color:#cccccc">Long</strong> <span>userId</span><span>)</span> <span>&#123;</span></span>
<span>        <strong style="color:#cda869">this</strong><span>.</span><span style="color:#008080">userId</span> <span>=</span> <span>userId</span><span>;</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span>
</pre> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">ShardingSphere 插件</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Kotlin DSL</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre><span>    <strong style="color:#cccccc">implementation</strong><span style="color:#eeeeee">(</span><span style="background-color:transparent; color:#00aadd">"me.ahoo.cosid:cosid-shardingsphere:$&#123;cosidVersion&#125;"</span><span style="color:#eeeeee">)</span></span>
</pre> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">CosIdKeyGenerateAlgorithm (分布式主键)</h4> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#008080">spring</span><span>:</span></span>
<span>  <span style="color:#008080">shardingsphere</span><span>:</span></span>
<span>    <span style="color:#008080">rules</span><span>:</span></span>
<span>      <span style="color:#008080">sharding</span><span>:</span></span>
<span>        <span style="color:#008080">key-generators</span><span>:</span></span>
<span>          <span style="color:#008080">cosid</span><span>:</span></span>
<span>            <span style="color:#008080">type</span><span>:</span> <span style="background-color:transparent; color:#00aadd">COSID</span></span>
<span>            <span style="color:#008080">props</span><span>:</span></span>
<span>              <span style="color:#008080">id-name</span><span>:</span> <span style="background-color:transparent; color:#00aadd">__share__</span></span>
</pre> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">基于间隔的时间范围分片算法</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="CosIdIntervalShardingAlgorithm" src="https://gitee.com/AhooWang/CosId/raw/main/docs/CosIdIntervalShardingAlgorithm.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>易用性: 支持多种数据类型 (<code>Long</code>、<code>LocalDateTime</code>、<code>DATE</code>)，而官方实现是先转换成字符串再转换成<code>LocalDateTime</code>，转换成功率受时间格式化字符影响。</li> 
 <li>性能 : 相比于<span> </span><code>org.apache.shardingsphere.sharding.algorithm.sharding.datetime.IntervalShardingAlgorithm</code><span> </span>性能高出<span> </span><em>1200~4000</em><span> </span>倍。</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="Interval-based-sharding-algorithm" src="https://gitee.com/AhooWang/CosId/raw/main/docs/Interval-based-sharding-algorithm-jmh.png" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>gradle cosid-shardingsphere:jmh</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><span># JMH version: 1.29</span>
<span># VM version: JDK 11.0.13, OpenJDK 64-Bit Server VM, 11.0.13+8-LTS</span>
<span># VM options: -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/work/CosId/cosid-shardingsphere/build/tmp/jmh -Duser.country=CN -Duser.language=zh -Duser.variant</span>
<span># Blackhole mode: full + dont-inline hint</span>
<span># Warmup: 1 iterations, 10 s each</span>
<span># Measurement: 1 iterations, 10 s each</span>
<span># Timeout: 10 min per iteration</span>
<span># Threads: 1 thread, will synchronize iterations</span>
<span># Benchmark mode: Throughput, ops/time</span>
<span>Benchmark                                                          Mode  Cnt         Score   Error  Units</span>
<span>IntervalShardingAlgorithmBenchmark.cosid_precise_local_date_time  thrpt       66276995.822          ops/s</span>
<span>IntervalShardingAlgorithmBenchmark.cosid_precise_timestamp        thrpt       24841952.001          ops/s</span>
<span>IntervalShardingAlgorithmBenchmark.cosid_range_local_date_time    thrpt        3344013.803          ops/s</span>
<span>IntervalShardingAlgorithmBenchmark.cosid_range_timestamp          thrpt        2846453.298          ops/s</span>
<span>IntervalShardingAlgorithmBenchmark.office_precise_timestamp       thrpt           6286.861          ops/s</span>
<span>IntervalShardingAlgorithmBenchmark.office_range_timestamp         thrpt           2302.986          ops/s</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<ul> 
 <li>DateIntervalShardingAlgorithm 
  <ul> 
   <li>type: COSID_INTERVAL_DATE</li> 
  </ul> </li> 
 <li>LocalDateTimeIntervalShardingAlgorithm 
  <ul> 
   <li>type: COSID_INTERVAL_LDT</li> 
  </ul> </li> 
 <li>TimestampIntervalShardingAlgorithm 
  <ul> 
   <li>type: COSID_INTERVAL_TS</li> 
  </ul> </li> 
 <li>TimestampOfSecondIntervalShardingAlgorithm 
  <ul> 
   <li>type: COSID_INTERVAL_TS_SECOND</li> 
  </ul> </li> 
 <li>SnowflakeIntervalShardingAlgorithm 
  <ul> 
   <li>type: COSID_INTERVAL_SNOWFLAKE</li> 
  </ul> </li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#008080">spring</span><span>:</span></span>
<span>  <span style="color:#008080">shardingsphere</span><span>:</span></span>
<span>    <span style="color:#008080">rules</span><span>:</span></span>
<span>      <span style="color:#008080">sharding</span><span>:</span></span>
<span>        <span style="color:#008080">sharding-algorithms</span><span>:</span></span>
<span>          <span style="color:#008080">alg-name</span><span>:</span></span>
<span>            <span style="color:#008080">type</span><span>:</span> <span style="background-color:transparent; color:#00aadd">COSID_INTERVAL_&#123;type_suffix&#125;</span></span>
<span>            <span style="color:#008080">props</span><span>:</span></span>
<span>              <span style="color:#008080">logic-name</span><span>:</span> <span style="background-color:transparent; color:#00aadd">logic-name</span></span>
<span>              <span style="color:#008080">id-name</span><span>:</span> <span style="background-color:transparent; color:#00aadd">cosid-name</span></span>
<span>              <span style="color:#008080">datetime-lower</span><span>:</span> <span style="background-color:transparent; color:#00aadd">2021-12-08T22:00:00</span></span>
<span>              <span style="color:#008080">datetime-upper</span><span>:</span> <span style="background-color:transparent; color:#00aadd">2022-12-01T00:00:00</span></span>
<span>              <span style="color:#008080">sharding-suffix-pattern</span><span>:</span> <span style="background-color:transparent; color:#00aadd">_yyyyMM</span></span>
<span>              <span style="color:#008080">datetime-interval-unit</span><span>:</span> <span style="background-color:transparent; color:#00aadd">MONTHS</span></span>
<span>              <span style="color:#008080">datetime-interval-amount</span><span>:</span> <strong style="color:#0000dd">1</strong></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">性能测试报告</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">SegmentChainId-吞吐量 (ops/s)</h3> 
<h4 style="margin-left:0; margin-right:0; text-align:left">RedisChainIdBenchmark-Throughput</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="RedisChainIdBenchmark-Throughput" src="https://gitee.com/AhooWang/CosId/raw/main/docs/jmh/RedisChainIdBenchmark-Throughput.png" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">MySqlChainIdBenchmark-Throughput</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="MySqlChainIdBenchmark-Throughput" src="https://gitee.com/AhooWang/CosId/raw/main/docs/jmh/MySqlChainIdBenchmark-Throughput.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">SegmentChainId-每次操作耗时的百分位数(us/op)</h3> 
<h4 style="margin-left:0; margin-right:0; text-align:left">RedisChainIdBenchmark-Percentile</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="RedisChainIdBenchmark-Sample" src="https://gitee.com/AhooWang/CosId/raw/main/docs/jmh/RedisChainIdBenchmark-Sample.png" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">MySqlChainIdBenchmark-Percentile</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="MySqlChainIdBenchmark-Sample" src="https://gitee.com/AhooWang/CosId/raw/main/docs/jmh/MySqlChainIdBenchmark-Sample.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">基准测试报告运行环境说明</h2> 
<ul> 
 <li>基准测试运行环境：笔记本开发机(MacBook-Pro-(M1))</li> 
 <li>所有基准测试都在开发笔记本上执行。</li> 
</ul>
                                        </div>
                                      
</div>
            