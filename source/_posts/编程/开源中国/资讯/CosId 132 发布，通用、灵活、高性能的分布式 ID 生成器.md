
---
title: 'CosId 1.3.2 发布，通用、灵活、高性能的分布式 ID 生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/AhooWang/CosId/raw/main/docs/Snowflake-identifier.png'
author: 开源中国
comments: false
date: Sat, 17 Jul 2021 07:46:00 GMT
thumbnail: 'https://gitee.com/AhooWang/CosId/raw/main/docs/Snowflake-identifier.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId" target="_blank">CosId</a> 通用、灵活、高性能的分布式 ID 生成器</h1> 
<h2 style="text-align:left">更新内容（1.3.2） 🎉 🎉 🎉</h2> 
<ol> 
 <li>增强：新增 <code>MergedIdSegment</code> 合并 <code>IdSegment</code> 避免创建过多 <code>IdSegment</code> 对象。</li> 
 <li>增强：新增 亲和性预取线程池 <code>PrefetchWorkerExecutorService</code>(<code>PrefetchWorker</code> 1:n <code>PrefetchJob</code>)，提升 <code>PrefetchWorker</code> 利用率，防止因申明过多 <code>SegmentChainId</code> 导致的创建过多线程的问题(<code>PrefetchWorker</code> 1:1 <code>PrefetchJob</code>)。</li> 
 <li>增强：使用 <code>CacheClock</code> 替换 <code>System.currentTimeMillis</code>提升获取当前时钟性能。 
  <ol> 
   <li><code>System.currentTimeMillis</code>: 太慢了，TPS只有<code>7191W+/s</code>，低于 <code>SegmentChainId</code> 能达到的峰值<code>12743W+/s</code>，当开启<code>IdSegment</code>的<code>ttl</code>功能时会影响<code>SegmentChainId</code>峰值性能。</li> 
   <li><code>CacheClock</code>: TPS <code>41765W+/s</code> ，精度1秒，应用需要容忍潜在的1秒精度延迟可能性，在 <code>TTL</code> 检查的场景中完全适用。</li> 
  </ol> </li> 
 <li>增强：数值计算溢出检查。</li> 
 <li>增强：优化安全间隙（<code>safeGap</code>）计算逻辑。</li> 
</ol> 
<h2 style="text-align:left">介绍</h2> 
<p style="text-align:left"><em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId" target="_blank">CosId</a></em> 旨在提供通用、灵活、高性能的分布式 ID 生成器。 目前提供了俩类 ID 生成器：</p> 
<ul> 
 <li><code>SnowflakeId</code> : <em>单机 TPS 性能：409W/s</em> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%2Fblob%2Fmain%2FREADME.zh-CN.md%23jmh-benchmark" target="_blank">JMH 基准测试</a> , 主要解决 <em>时钟回拨问题</em> 、<em>机器号分配问题</em> 并且提供更加友好、灵活的使用体验。</li> 
 <li><code>SegmentId</code>: 每次获取一段 (<code>Step</code>) ID，来降低号段分发器的网络IO请求频次提升性能。 
  <ul> 
   <li><code>IdSegmentDistributor</code>: 号段分发器（号段存储器） 
    <ul> 
     <li><code>RedisIdSegmentDistributor</code>: 基于 <em>Redis</em> 的号段分发器。</li> 
     <li><code>JdbcIdSegmentDistributor</code>: 基于 <em>Jdbc</em> 的号段分发器，支持各种关系型数据库。</li> 
    </ul> </li> 
   <li><code>SegmentChainId</code>(<strong>推荐</strong>):<code>SegmentChainId</code> (<em>lock-free</em>) 是对 <code>SegmentId</code> 的增强。性能可达到近似 <code>AtomicLong</code> 的 <em>TPS 性能:12,743W+/s</em> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%2Fblob%2Fmain%2FREADME.zh-CN.md%23jmh-benchmark" target="_blank">JMH 基准测试</a> 。 
    <ul> 
     <li><code>PrefetchWorker</code> 维护安全距离(<code>safeDistance</code>), 并且支持基于饥饿状态的动态<code>safeDistance</code>扩容/收缩。</li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:left">SnowflakeId</h2> 
<p style="text-align:left"><img alt="Snowflake" src="https://gitee.com/AhooWang/CosId/raw/main/docs/Snowflake-identifier.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p><em>SnowflakeId</em> 使用 <code>Long</code> （64 bits） 位分区来生成 ID 的一种分布式 ID 算法。 通用的位分配方案为：<code>timestamp</code> (41 bits) + <code>machineId</code> (10 bits) + <code>sequence</code> (12 bits) = 63 bits 。</p> 
</blockquote> 
<ul> 
 <li>41 位 <code>timestamp</code> = (1L<<41)/(1000/3600/365) 约可以存储 69 年的时间戳，即可以使用的绝对时间为 <code>EPOCH</code> + 69 年，一般我们需要自定义 <code>EPOCH</code> 为产品开发时间，另外还可以通过压缩其他区域的分配位数，来增加时间戳位数来延长可用时间。</li> 
 <li>10 位 <code>machineId</code> = (1L<<10) = 1024 即相同业务可以部署 1024 个副本 (在 Kubernetes 概念里没有主从副本之分，这里直接沿用 Kubernetes 的定义) 实例，一般情况下没有必要使用这么多位，所以会根据部署规模需要重新定义。</li> 
 <li>12 位 <code>sequence</code> = (1L<<12) * 1000 = 4096000 即单机每秒可生成约 409W 的 ID，全局同业务集群可产生 4096000*1024=419430W=41.9亿(TPS)。</li> 
</ul> 
<p style="text-align:left">从 <em>SnowflakeId</em> 设计上可以看出:</p> 
<ul> 
 <li><img alt="👍" height="14" src="https://assets.gitee.com/assets/emoji/thumbsup-f866ad23f6584fa15376ddb4738e53cf.png" width="14" referrerpolicy="no-referrer"> <code>timestamp</code> 在高位，所以 <em>SnowflakeId</em> 是本机单调递增的，受全局时钟同步影响 <em>SnowflakeId</em> 是全局趋势递增的。</li> 
 <li><img alt="👍" height="14" src="https://assets.gitee.com/assets/emoji/thumbsup-f866ad23f6584fa15376ddb4738e53cf.png" width="14" referrerpolicy="no-referrer"> <em>SnowflakeId</em> 不对任何第三方中间件有强依赖关系，并且性能也非常高。</li> 
 <li><img alt="👍" height="14" src="https://assets.gitee.com/assets/emoji/thumbsup-f866ad23f6584fa15376ddb4738e53cf.png" width="14" referrerpolicy="no-referrer"> 位分配方案可以按照业务系统需要灵活配置，来达到最优使用效果。</li> 
 <li><img alt="👎" height="14" src="https://assets.gitee.com/assets/emoji/thumbsdown-da41668c7715a2e470f020d398f74f74.png" width="14" referrerpolicy="no-referrer"> 强依赖本机时钟，潜在的时钟回拨问题会导致 ID 重复。</li> 
 <li><img alt="👎" height="14" src="https://assets.gitee.com/assets/emoji/thumbsdown-da41668c7715a2e470f020d398f74f74.png" width="14" referrerpolicy="no-referrer"> <code>machineId</code> 需要手动设置，实际部署时如果采用手动分配 <code>machineId</code>，会非常低效。</li> 
</ul> 
<hr> 
<p style="text-align:left"><em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%2Ftree%2Fmain%2Fcosid-core%2Fsrc%2Fmain%2Fjava%2Fme%2Fahoo%2Fcosid%2Fsnowflake" target="_blank">CosId-SnowflakeId</a></em> 主要解决 <em>SnowflakeId</em> 俩大问题：机器号分配问题、时钟回拨问题。 并且提供更加友好、灵活的使用体验。</p> 
<h3 style="text-align:left">MachineIdDistributor (MachineId 分配器)</h3> 
<blockquote> 
 <p>目前 <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId" target="_blank">CosId</a></em> 提供了以下三种 <code>MachineId</code> 分配器。</p> 
</blockquote> 
<h4 style="text-align:left">ManualMachineIdDistributor</h4> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">cosid</span>:
  <span style="color:#008080">snowflake</span>:
    <span style="color:#008080">machine</span>:
      <span style="color:#008080">distributor</span>:
        <span style="color:#008080">type</span>: <span style="background-color:transparent; color:#00aadd">manual</span>
        <span style="color:#008080">manual</span>:
          <span style="color:#008080">machine-id</span>: <strong>0</strong></pre> 
 </div> 
</div> 
<blockquote> 
 <p>手动分配 <code>MachineId</code>。</p> 
</blockquote> 
<h4 style="text-align:left">StatefulSetMachineIdDistributor</h4> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">cosid</span>:
  <span style="color:#008080">snowflake</span>:
    <span style="color:#008080">machine</span>:
      <span style="color:#008080">distributor</span>:
        <span style="color:#008080">type</span>: <span style="background-color:transparent; color:#00aadd">stateful_set</span></pre> 
 </div> 
</div> 
<blockquote> 
 <p>使用 <code>Kubernetes</code> 的 <code>StatefulSet</code> 提供的稳定的标识 ID 作为机器号。</p> 
</blockquote> 
<h4 style="text-align:left">RedisMachineIdDistributor</h4> 
<p style="text-align:left"><img alt="RedisMachineIdDistributor" src="https://gitee.com/AhooWang/CosId/raw/main/docs/RedisMachineIdDistributor.png" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">cosid</span>:
  <span style="color:#008080">snowflake</span>:
    <span style="color:#008080">machine</span>:
      <span style="color:#008080">distributor</span>:
        <span style="color:#008080">type</span>: <span style="background-color:transparent; color:#00aadd">redis</span></pre> 
 </div> 
</div> 
<blockquote> 
 <p>使用 <code>Redis</code> 作为机器号的分发存储。</p> 
</blockquote> 
<h3 style="text-align:left">ClockBackwardsSynchronizer (时钟回拨同步器)</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">cosid</span>:
  <span style="color:#008080">snowflake</span>:
    <span style="color:#008080">clock-backwards</span>:
      <span style="color:#008080">spin-threshold</span>: <strong>10</strong>
      <span style="color:#008080">broken-threshold</span>: <strong>2000</strong></pre> 
 </div> 
</div> 
<p style="text-align:left">默认提供的 <code>DefaultClockBackwardsSynchronizer</code> 时钟回拨同步器使用主动等待同步策略，<code>spinThreshold</code>(默认值 10 毫秒) 用于设置自旋等待阈值， 当大于<code>spinThreshold</code> 时使用线程休眠等待时钟同步，如果超过<code>brokenThreshold</code>(默认值 2 秒)时会直接抛出<code>ClockTooManyBackwardsException</code>异常。</p> 
<h3 style="text-align:left">MachineStateStorage (机器状态存储)</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>public</strong> <strong>class</strong> <strong>MachineState</strong> &#123;
    <strong>public</strong> <strong>static</strong> <strong>final</strong> <strong>MachineState</strong> <span style="color:turquoise">NOT_FOUND</span> = of(-<span style="color:#009999">1</span>, -<span style="color:#009999">1</span>);
    <strong>private</strong> <strong>final</strong> <strong>int</strong> machineId;
    <strong>private</strong> <strong>final</strong> <strong>long</strong> lastTimeStamp;

    <strong>public</strong> <strong>MachineState</strong>(<strong>int</strong> machineId, <strong>long</strong> lastTimeStamp) &#123;
        <strong>this</strong>.<span style="color:#008080">machineId</span> = machineId;
        <strong>this</strong>.<span style="color:#008080">lastTimeStamp</span> = lastTimeStamp;
    &#125;

    <strong>public</strong> <strong>int</strong> <strong>getMachineId</strong>() &#123;
        <strong>return</strong> machineId;
    &#125;

    <strong>public</strong> <strong>long</strong> <strong>getLastTimeStamp</strong>() &#123;
        <strong>return</strong> lastTimeStamp;
    &#125;

    <strong>public</strong> <strong>static</strong> <strong>MachineState</strong> <strong>of</strong>(<strong>int</strong> machineId, <strong>long</strong> lastStamp) &#123;
        <strong>return</strong> <strong>new</strong> <strong>MachineState</strong>(machineId, lastStamp);
    &#125;
&#125;</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">cosid</span>:
  <span style="color:#008080">snowflake</span>:
    <span style="color:#008080">machine</span>:
      <span style="color:#008080">state-storage</span>:
        <span style="color:#008080">local</span>:
          <span style="color:#008080">state-location</span>: <span style="background-color:transparent; color:#00aadd">./cosid-machine-state/</span></pre> 
 </div> 
</div> 
<p style="text-align:left">默认提供的 <code>LocalMachineStateStorage</code> 本地机器状态存储，使用本地文件存储机器号、最近一次时间戳，用作 <code>MachineState</code> 缓存。</p> 
<h3 style="text-align:left">ClockSyncSnowflakeId (主动时钟同步 <code>SnowflakeId</code>)</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">cosid</span>:
  <span style="color:#008080">snowflake</span>:
    <span style="color:#008080">share</span>:
      <span style="color:#008080">clock-sync</span>: <span style="color:turquoise">true</span></pre> 
 </div> 
</div> 
<p style="text-align:left">默认 <code>SnowflakeId</code> 当发生时钟回拨时会直接抛出 <code>ClockBackwardsException</code> 异常，而使用 <code>ClockSyncSnowflakeId</code> 会使用 <code>ClockBackwardsSynchronizer</code> 主动等待时钟同步来重新生成 ID，提供更加友好的使用体验。</p> 
<h3 style="text-align:left">SafeJavaScriptSnowflakeId (<code>JavaScript</code> 安全的 <code>SnowflakeId</code>)</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>SnowflakeId</strong> snowflakeId=<strong>SafeJavaScriptSnowflakeId</strong>.<span style="color:#008080">ofMillisecond</span>(<span style="color:#009999">1</span>);</pre> 
 </div> 
</div> 
<p style="text-align:left"><code>JavaScript</code> 的 <code>Number.MAX_SAFE_INTEGER</code> 只有 53 位，如果直接将 63 位的 <code>SnowflakeId</code> 返回给前端，那么会值溢出的情况，通常我们可以将<code>SnowflakeId</code> 转换为 <code>String</code> 类型或者自定义 <code>SnowflakeId</code> 位分配来缩短 <code>SnowflakeId</code> 的位数 使 <code>ID</code> 提供给前端时不溢出。</p> 
<h3 style="text-align:left">SnowflakeFriendlyId (可以将 <code>SnowflakeId</code> 解析成可读性更好的 <code>SnowflakeIdState</code> )</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">cosid</span>:
  <span style="color:#008080">snowflake</span>:
    <span style="color:#008080">share</span>:
      <span style="color:#008080">friendly</span>: <span style="color:turquoise">true</span></pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>public</strong> <strong>class</strong> <strong>SnowflakeIdState</strong> &#123;

    <strong>private</strong> <strong>final</strong> <strong>long</strong> id;

    <strong>private</strong> <strong>final</strong> <strong>int</strong> machineId;

    <strong>private</strong> <strong>final</strong> <strong>long</strong> sequence;

    <strong>private</strong> <strong>final</strong> <strong>LocalDateTime</strong> timestamp;
    <span style="color:#888888">/**</span>
<span style="color:#888888">     * &#123;@link #timestamp&#125;-&#123;@link #machineId&#125;-&#123;@link #sequence&#125;</span>
<span style="color:#888888">     */</span>
    <strong>private</strong> <strong>final</strong> <strong>String</strong> friendlyId;
&#125;</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>public</strong> <strong>interface</strong> <strong>SnowflakeFriendlyId</strong> <strong>extends</strong> <strong>SnowflakeId</strong> &#123;

    <strong>SnowflakeIdState</strong> <strong>friendlyId</strong>(<strong>long</strong> id);

    <strong>SnowflakeIdState</strong> <strong>ofFriendlyId</strong>(<strong>String</strong> friendlyId);

    <strong>default</strong> <strong>SnowflakeIdState</strong> <strong>friendlyId</strong>() &#123;
        <strong>long</strong> id = generate();
        <strong>return</strong> <strong>friendlyId</strong>(id);
    &#125;
&#125;</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre>        <strong>SnowflakeFriendlyId</strong> snowflakeFriendlyId=<strong>new</strong> <strong>DefaultSnowflakeFriendlyId</strong>(snowflakeId);
        <strong>SnowflakeIdState</strong> idState=snowflakeFriendlyId.<span style="color:#008080">friendlyId</span>();
        idState.<span style="color:#008080">getFriendlyId</span>(); <span style="color:#888888">//20210623131730192-1-0</span></pre> 
 </div> 
</div> 
<h2 style="text-align:left">SegmentId (号段模式)</h2> 
<p style="text-align:left"><img alt="SegmentId" src="https://gitee.com/AhooWang/CosId/raw/main/docs/SegmentId.png" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">RedisIdSegmentDistributor (使用<code>Redis</code>作为号段分发后端存储)</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">cosid</span>:
  <span style="color:#008080">segment</span>:
    <span style="color:#008080">enabled</span>: <span style="color:turquoise">true</span>
    <span style="color:#008080">distributor</span>:
      <span style="color:#008080">type</span>: <span style="background-color:transparent; color:#00aadd">redis</span></pre> 
 </div> 
</div> 
<h3 style="text-align:left">JdbcIdSegmentDistributor (使用关系型数据库<code>Db</code>作为号段分发后端存储)</h3> 
<blockquote> 
 <p>初始化 <code>cosid</code> table</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>create table if not exists cosid
(
    name            varchar(100) not null comment '&#123;namespace&#125;.&#123;name&#125;',
    last_max_id     bigint       not null default 0,
    last_fetch_time bigint       not null,
    constraint cosid_pk
        primary key (name)
) engine = InnoDB;
</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">spring</span>:
  <span style="color:#008080">datasource</span>:
    <span style="color:#008080">url</span>: <span style="background-color:transparent; color:#00aadd">jdbc:mysql://localhost:3306/test_db</span>
    <span style="color:#008080">username</span>: <span style="background-color:transparent; color:#00aadd">root</span>
    <span style="color:#008080">password</span>: <span style="background-color:transparent; color:#00aadd">root</span>
<span style="color:#008080">cosid</span>:
  <span style="color:#008080">segment</span>:
    <span style="color:#008080">enabled</span>: <span style="color:turquoise">true</span>
    <span style="color:#008080">distributor</span>:
      <span style="color:#008080">type</span>: <span style="background-color:transparent; color:#00aadd">jdbc</span>
      <span style="color:#008080">jdbc</span>:
        <span style="color:#008080">enable-auto-init-cosid-table</span>: <span style="color:turquoise">false</span>
        <span style="color:#008080">enable-auto-init-id-segment</span>: <span style="color:turquoise">true</span></pre> 
 </div> 
</div> 
<p style="text-align:left">开启 <code>enable-auto-init-id-segment:true</code> 之后，应用启动时会尝试创建 <code>idSegment</code> 记录，避免手动创建。类似执行了以下初始化sql脚本，不用担心误操作，因为 <code>name</code> 是主键。</p> 
<div style="text-align:left"> 
 <div> 
  <pre>insert into cosid
    (name, last_max_id, last_fetch_time)
    value
    ('namespace.name', 0, unix_timestamp());</pre> 
 </div> 
</div> 
<h3 style="text-align:left">SegmentChainId (号段链模式)</h3> 
<p style="text-align:left"><img alt="SegmentChainId" src="https://gitee.com/AhooWang/CosId/raw/main/docs/SegmentChainId.png" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">cosid</span>:
  <span style="color:#008080">segment</span>:
    <span style="color:#008080">enabled</span>: <span style="color:turquoise">true</span>
    <span style="color:#008080">mode</span>: <span style="background-color:transparent; color:#00aadd">chain</span>
    <span style="color:#008080">chain</span>:
      <span style="color:#008080">safe-distance</span>: <strong>5</strong>
      <span style="color:#008080">prefetch-worker</span>:
        <span style="color:#008080">core-pool-size</span>: <strong>2</strong>
        <span style="color:#008080">prefetch-period</span>: <span style="background-color:transparent; color:#00aadd">1s</span></pre> 
 </div> 
</div> 
<h2 style="text-align:left">IdGeneratorProvider</h2> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">cosid</span>:
  <span style="color:#008080">snowflake</span>:
    <span style="color:#008080">provider</span>:
      <span style="color:#008080">bizA</span>:
        <span style="color:#888888">#      epoch:</span>
        <span style="color:#888888">#      timestamp-bit:</span>
        <span style="color:#008080">sequence-bit</span>: <strong>12</strong>
      <span style="color:#008080">bizB</span>:
        <span style="color:#888888">#      epoch:</span>
        <span style="color:#888888">#      timestamp-bit:</span>
        <span style="color:#008080">sequence-bit</span>: <strong>12</strong></pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>IdGenerator</strong> idGenerator=idGeneratorProvider.<span style="color:#008080">get</span>(<span style="background-color:transparent; color:#00aadd">"bizA"</span>);</pre> 
 </div> 
</div> 
<p style="text-align:left">在实际使用中我们一般不会所有业务服务使用同一个 <code>IdGenerator</code> ，而是不同的业务使用不同的 <code>IdGenerator</code>，那么 <code>IdGeneratorProvider</code>就是为了解决这个问题而存在的，他是 <code>IdGenerator</code> 的容器，可以通过业务名来获取相应的 <code>IdGenerator</code>。</p> 
<h2 style="text-align:left">Examples</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%2Ftree%2Fmain%2Fcosid-rest-api" target="_blank">CosId-Examples</a></p> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Fswagger-ui%2Findex.html%23%2F" target="_blank">http://localhost:8080/swagger-ui/index.html#/</a></p> 
</blockquote> 
<h2 style="text-align:left">安装</h2> 
<h3 style="text-align:left">Gradle</h3> 
<blockquote> 
 <p>Kotlin DSL</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>    <strong>val</strong> <strong>cosidVersion</strong> <span style="color:#eeeeee">=</span> <span style="background-color:transparent; color:#00aadd">"1.3.2"</span><span style="color:#eeeeee">;</span>
    <strong>implementation</strong><span style="color:#eeeeee">(</span><span style="background-color:transparent; color:#00aadd">"me.ahoo.cosid:spring-boot-starter-cosid:$&#123;cosidVersion&#125;"</span><span style="color:#eeeeee">)</span></pre> 
 </div> 
</div> 
<h3 style="text-align:left">Maven</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><strong><?xml version="1.0" encoding="UTF-8"?></strong>

<span style="color:#ffcc55"><project</span> <span style="color:#008080">xmlns=</span><span style="background-color:transparent; color:#00aadd">"http://maven.apache.org/POM/4.0.0"</span>
         <span style="color:#008080">xmlns:xsi=</span><span style="background-color:transparent; color:#00aadd">"http://www.w3.org/2001/XMLSchema-instance"</span>
         <span style="color:#008080">xsi:schemaLocation=</span><span style="background-color:transparent; color:#00aadd">"http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"</span><span style="color:#ffcc55">></span>

    <span style="color:#ffcc55"><modelVersion></span>4.0.0<span style="color:#ffcc55"></modelVersion></span>
    <span style="color:#ffcc55"><artifactId></span>demo<span style="color:#ffcc55"></artifactId></span>
    <span style="color:#ffcc55"><properties></span>
        <span style="color:#ffcc55"><cosid.version></span>1.3.2<span style="color:#ffcc55"></cosid.version></span>
    <span style="color:#ffcc55"></properties></span>

    <span style="color:#ffcc55"><dependencies></span>
        <span style="color:#ffcc55"><dependency></span>
            <span style="color:#ffcc55"><groupId></span>me.ahoo.cosid<span style="color:#ffcc55"></groupId></span>
            <span style="color:#ffcc55"><artifactId></span>spring-boot-starter-cosid<span style="color:#ffcc55"></artifactId></span>
            <span style="color:#ffcc55"><version></span>$&#123;cosid.version&#125;<span style="color:#ffcc55"></version></span>
        <span style="color:#ffcc55"></dependency></span>
    <span style="color:#ffcc55"></dependencies></span>

<span style="color:#ffcc55"></project></span></pre> 
 </div> 
</div> 
<h3 style="text-align:left">application.yaml</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">spring</span>:
  <span style="color:#008080">application</span>:
    <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">$&#123;service.name:cosid-example&#125;</span>
  <span style="color:#008080">datasource</span>:
    <span style="color:#008080">url</span>: <span style="background-color:transparent; color:#00aadd">jdbc:mysql://localhost:3306/test_db</span>
    <span style="color:#008080">username</span>: <span style="background-color:transparent; color:#00aadd">root</span>
    <span style="color:#008080">password</span>: <span style="background-color:transparent; color:#00aadd">root</span>
  <span style="color:#008080">redis</span>:
    <span style="color:#008080">url</span>: <span style="background-color:transparent; color:#00aadd">redis://localhost:6379</span>
<span style="color:#008080">cosid</span>:
  <span style="color:#008080">namespace</span>: <span style="background-color:transparent; color:#00aadd">$&#123;spring.application.name&#125;</span>
  <span style="color:#008080">snowflake</span>:
    <span style="color:#008080">enabled</span>: <span style="color:turquoise">true</span>
    <span style="color:#888888">#    epoch: 1577203200000</span>
    <span style="color:#008080">clock-backwards</span>:
      <span style="color:#008080">spin-threshold</span>: <strong>10</strong>
      <span style="color:#008080">broken-threshold</span>: <strong>2000</strong>
    <span style="color:#008080">machine</span>:
      <span style="color:#888888">#      stable: true</span>
      <span style="color:#888888">#      machine-bit: 10</span>
      <span style="color:#888888">#      instance-id: $&#123;HOSTNAME&#125;</span>
      <span style="color:#008080">distributor</span>:
        <span style="color:#008080">type</span>: <span style="background-color:transparent; color:#00aadd">redis</span>
      <span style="color:#888888">#        manual:</span>
      <span style="color:#888888">#          machine-id: 0</span>
      <span style="color:#008080">state-storage</span>:
        <span style="color:#008080">local</span>:
          <span style="color:#008080">state-location</span>: <span style="background-color:transparent; color:#00aadd">./cosid-machine-state/</span>
    <span style="color:#008080">share</span>:
      <span style="color:#008080">clock-sync</span>: <span style="color:turquoise">true</span>
      <span style="color:#008080">friendly</span>: <span style="color:turquoise">true</span>
    <span style="color:#008080">provider</span>:
      <span style="color:#008080">bizA</span>:
        <span style="color:#888888">#        timestamp-bit:</span>
        <span style="color:#008080">sequence-bit</span>: <strong>12</strong>
      <span style="color:#008080">bizB</span>:
        <span style="color:#888888">#        timestamp-bit:</span>
        <span style="color:#008080">sequence-bit</span>: <strong>12</strong>
  <span style="color:#008080">segment</span>:
    <span style="color:#008080">enabled</span>: <span style="color:turquoise">true</span>
    <span style="color:#008080">mode</span>: <span style="background-color:transparent; color:#00aadd">chain</span>
    <span style="color:#008080">chain</span>:
      <span style="color:#008080">safe-distance</span>: <strong>5</strong>
      <span style="color:#008080">prefetch-worker</span>:
        <span style="color:#008080">core-pool-size</span>: <strong>2</strong>
        <span style="color:#008080">prefetch-period</span>: <span style="background-color:transparent; color:#00aadd">1s</span>
    <span style="color:#008080">distributor</span>:
      <span style="color:#008080">type</span>: <span style="background-color:transparent; color:#00aadd">redis</span>
    <span style="color:#008080">share</span>:
      <span style="color:#008080">offset</span>: <strong>0</strong>
      <span style="color:#008080">step</span>: <strong>100</strong>
    <span style="color:#008080">provider</span>:
      <span style="color:#008080">bizC</span>:
        <span style="color:#008080">offset</span>: <strong>10000</strong>
        <span style="color:#008080">step</span>: <strong>100</strong>
      <span style="color:#008080">bizD</span>:
        <span style="color:#008080">offset</span>: <strong>10000</strong>
        <span style="color:#008080">step</span>: <strong>100</strong></pre> 
 </div> 
</div> 
<h2 style="text-align:left">JMH-Benchmark</h2> 
<ul> 
 <li>基准测试运行环境：笔记本开发机 ( MacBook Pro (M1) )</li> 
 <li>所有基准测试都在开发笔记本上执行。</li> 
 <li>Redis 部署环境也在该笔记本开发机上。</li> 
</ul> 
<h3 style="text-align:left">SnowflakeId</h3> 
<div style="text-align:left"> 
 <div> 
  <pre>gradle cosid-core:jmh
<em># or</em>
java <span style="color:#ffcc55">-jar</span> cosid-core/build/libs/cosid-core-1.3.2-jmh.jar <span style="color:#ffcc55">-bm</span> thrpt <span style="color:#ffcc55">-wi</span> 1 <span style="color:#ffcc55">-rf</span> json <span style="color:#ffcc55">-f</span> 1</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre>Benchmark                                                    Mode  Cnt        Score   Error  Units
SnowflakeIdBenchmark.millisecondSnowflakeId_friendlyId      thrpt       4020311.665          ops/s
SnowflakeIdBenchmark.millisecondSnowflakeId_generate        thrpt       4095403.859          ops/s
SnowflakeIdBenchmark.safeJsMillisecondSnowflakeId_generate  thrpt        511654.048          ops/s
SnowflakeIdBenchmark.safeJsSecondSnowflakeId_generate       thrpt        539818.563          ops/s
SnowflakeIdBenchmark.secondSnowflakeId_generate             thrpt       4206843.941          ops/s</pre> 
 </div> 
</div> 
<h3 style="text-align:left">RedisChainIdBenchmark</h3> 
<h4 style="text-align:left">Throughput (ops/s)</h4> 
<p style="text-align:left"><img alt="RedisChainIdBenchmark-Throughput" src="https://gitee.com/AhooWang/CosId/raw/main/docs/jmh/RedisChainIdBenchmark-Throughput.png" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <div> 
  <pre>gradle cosid-redis:jmh
<em># or</em>
java <span style="color:#ffcc55">-jar</span> cosid-redis/build/libs/cosid-redis-1.3.2-jmh.jar <span style="color:#ffcc55">-bm</span> thrpt <span style="color:#ffcc55">-wi</span> 1 <span style="color:#ffcc55">-rf</span> json <span style="color:#ffcc55">-f</span> 1 RedisChainIdBenchmark</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre>Benchmark                                   Mode  Cnt          Score          Error  Units
RedisChainIdBenchmark.atomicLong_baseline  thrpt    5  144541334.198 ±  5578137.471  ops/s
RedisChainIdBenchmark.step_1               thrpt    5    1874168.687 ±   310274.706  ops/s
RedisChainIdBenchmark.step_100             thrpt    5  114226113.524 ± 15789563.078  ops/s
RedisChainIdBenchmark.step_1000            thrpt    5  127439148.104 ±  1833743.699  ops/s</pre> 
 </div> 
</div> 
<h4 style="text-align:left">Percentile-Sample (<em>P9999=0.208微秒</em>)</h4> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E7%2599%25BE%25E5%2588%2586%25E4%25BD%258D%25E6%2595%25B0" target="_blank">百分位数</a> ，统计学术语，若将一组数据从小到大排序，并计算相应的累计百分点，则某百分点所对应数据的值，就称为这百分点的百分位数，以Pk表示第k百分位数。百分位数是用来比较个体在群体中的相对地位量数。</p> 
</blockquote> 
<p style="text-align:left"><img alt="RedisChainIdBenchmark-Sample" src="https://gitee.com/AhooWang/CosId/raw/main/docs/jmh/RedisChainIdBenchmark-Sample.png" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <div> 
  <pre>java <span style="color:#ffcc55">-jar</span> cosid-redis/build/libs/cosid-redis-1.3.2-jmh.jar <span style="color:#ffcc55">-bm</span> sample <span style="color:#ffcc55">-wi</span> 1 <span style="color:#ffcc55">-rf</span> json <span style="color:#ffcc55">-f</span> 1 <span style="color:#ffcc55">-tu</span> us step_1000</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre>Benchmark                                            Mode      Cnt   Score    Error  Units
RedisChainIdBenchmark.step_1000                    sample  1336271   0.024 ±  0.001  us/op
RedisChainIdBenchmark.step_1000:step_1000·p0.00    sample              ≈ 0           us/op
RedisChainIdBenchmark.step_1000:step_1000·p0.50    sample            0.041           us/op
RedisChainIdBenchmark.step_1000:step_1000·p0.90    sample            0.042           us/op
RedisChainIdBenchmark.step_1000:step_1000·p0.95    sample            0.042           us/op
RedisChainIdBenchmark.step_1000:step_1000·p0.99    sample            0.042           us/op
RedisChainIdBenchmark.step_1000:step_1000·p0.999   sample            0.042           us/op
RedisChainIdBenchmark.step_1000:step_1000·p0.9999  sample            0.208           us/op
RedisChainIdBenchmark.step_1000:step_1000·p1.00    sample           37.440           us/op</pre> 
 </div> 
</div> 
<h3 style="text-align:left">MySqlChainIdBenchmark</h3> 
<h4 style="text-align:left">Throughput (ops/s)</h4> 
<p style="text-align:left"><img alt="MySqlChainIdBenchmark-Throughput" src="https://gitee.com/AhooWang/CosId/raw/main/docs/jmh/MySqlChainIdBenchmark-Throughput.png" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <div> 
  <pre>gradle cosid-jdbc:jmh
<em># or</em>
java <span style="color:#ffcc55">-jar</span> cosid-jdbc/build/libs/cosid-jdbc-1.3.2-jmh.jar <span style="color:#ffcc55">-bm</span> thrpt <span style="color:#ffcc55">-wi</span> 1 <span style="color:#ffcc55">-rf</span> json <span style="color:#ffcc55">-f</span> 1 MySqlChainIdBenchmark</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre>Benchmark                                   Mode  Cnt          Score         Error  Units
MySqlChainIdBenchmark.atomicLong_baseline  thrpt    5  145294642.937 ±  224876.284  ops/s
MySqlChainIdBenchmark.step_1               thrpt    5      35058.790 ±   36226.041  ops/s
MySqlChainIdBenchmark.step_100             thrpt    5   74575876.804 ± 5590390.811  ops/s
MySqlChainIdBenchmark.step_1000            thrpt    5  123131804.260 ± 1488004.409  ops/s</pre> 
 </div> 
</div> 
<h4 style="text-align:left">Percentile-Sample (<em>P9999=0.208微秒</em>)</h4> 
<p style="text-align:left"><img alt="MySqlChainIdBenchmark-Sample" src="https://gitee.com/AhooWang/CosId/raw/main/docs/jmh/MySqlChainIdBenchmark-Sample.png" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <div> 
  <pre>java <span style="color:#ffcc55">-jar</span> cosid-jdbc/build/libs/cosid-jdbc-1.3.2-jmh.jar <span style="color:#ffcc55">-bm</span> sample <span style="color:#ffcc55">-wi</span> 1 <span style="color:#ffcc55">-rf</span> json <span style="color:#ffcc55">-f</span> 1 <span style="color:#ffcc55">-tu</span> us step_1000</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre>Benchmark                                            Mode      Cnt    Score   Error  Units
MySqlChainIdBenchmark.step_1000                    sample  1286774    0.024 ± 0.001  us/op
MySqlChainIdBenchmark.step_1000:step_1000·p0.00    sample               ≈ 0          us/op
MySqlChainIdBenchmark.step_1000:step_1000·p0.50    sample             0.041          us/op
MySqlChainIdBenchmark.step_1000:step_1000·p0.90    sample             0.042          us/op
MySqlChainIdBenchmark.step_1000:step_1000·p0.95    sample             0.042          us/op
MySqlChainIdBenchmark.step_1000:step_1000·p0.99    sample             0.042          us/op
MySqlChainIdBenchmark.step_1000:step_1000·p0.999   sample             0.083          us/op
MySqlChainIdBenchmark.step_1000:step_1000·p0.9999  sample             0.208          us/op
MySqlChainIdBenchmark.step_1000:step_1000·p1.00    sample           342.528          us/op</pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            