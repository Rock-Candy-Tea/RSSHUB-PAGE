
---
title: 'CosId 1.0.0 发布，通用、灵活、高性能的分布式 ID 生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-efcfba09103434c12ff0c40af9c62343907.png'
author: 开源中国
comments: false
date: Wed, 30 Jun 2021 07:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-efcfba09103434c12ff0c40af9c62343907.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId" target="_blank">CosId</a> 通用、灵活、高性能的分布式 ID 生成器</h1> 
<h2 style="text-align:left">介绍</h2> 
<p style="text-align:left"><em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId" target="_blank">CosId</a></em> 旨在提供通用、灵活、高性能的分布式系统 ID 生成器。 目前提供了俩大类 ID 生成器：<em>SnowflakeId</em> （单机 TPS 性能：409W/s <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%23jmh-benchmark" target="_blank">JMH 基准测试</a>）、<em>RedisIdGenerator</em> (单机 TPS 性能(步长 1000)：3687W+/s <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%23jmh-benchmark" target="_blank">JMH 基准测试</a>)。</p> 
<h2 style="text-align:left">更新内容（1.0.0） 🎉 🎉 🎉</h2> 
<ol> 
 <li>增强：支持自定义配置 <strong>ClockBackwardsSynchronizer</strong>（spring-boot-starter-cosid）。</li> 
 <li>增强：优化 SnowflakeIdProperties 配置体验 （spring-boot-starter-cosid）。</li> 
 <li>变更：重命名 LocalMachineState 为 <strong>MachineStateStorage</strong>。</li> 
 <li>增强：支持自定义 IdDefinition 来开启 <strong>ClockSyncSnowflakeId</strong>。</li> 
 <li>增强：优化自定义配置 epoch 。</li> 
 <li>增强：支持配置 RedisIdGenerator#offset ，来设置分布式ID起始值。</li> 
 <li>新增：新增 <strong>SnowflakeFriendlyId</strong>，生成更具可读性的 SnowflakeIdState。</li> 
 <li>增强：自定义配置 Redis#timeout。</li> 
</ol> 
<h2 style="text-align:left">SnowflakeId</h2> 
<p style="text-align:left"><img alt="Snowflake" height="407" src="https://oscimg.oschina.net/oscnet/up-efcfba09103434c12ff0c40af9c62343907.png" width="1417" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p><em>SnowflakeId</em> 使用 <code>Long</code> （64 bits） 位分区来生成 ID 的一种分布式 ID 算法。<br> 通用的位分配方案为：<code>timestamp</code> (41 bits) + <code>machineId</code> (10 bits) + <code>sequence</code> (12 bits) = 63 bits 。</p> 
</blockquote> 
<ul> 
 <li>41 位 <code>timestamp</code> = (1L<<41)/(1000/3600/365) 约可以存储 69 年的时间戳，即可以使用的绝对时间为 <code>EPOCH</code> + 69 年，一般我们需要自定义 <code>EPOCH</code>为产品开发时间，另外还可以通过压缩其他区域的分配位数，来增加时间戳位数来延长可用时间。</li> 
 <li>10 位 <code>machineId</code> = (1L<<10) = 1024 即相同业务可以部署 1024 个副本 (在 Kubernetes 概念里没有主从副本之分，这里直接沿用 Kubernetes 的定义) 实例，一般情况下没有必要使用这么多位，所以会根据部署规模需要重新定义。</li> 
 <li>12 位 <code>sequence</code> = (1L<<12) * 1000 = 4096000 即单机每秒可生成约 409W 的 ID，全局同业务集群可产生 4096000*1024=419430W=41.9亿(TPS)。</li> 
</ul> 
<p style="text-align:left">从 <em>SnowflakeId</em> 设计上可以看出:</p> 
<ul> 
 <li> <code>timestamp</code> 在高位，所以 <em>SnowflakeId</em> 是本机单调递增的，受全局时钟同步影响 <em>SnowflakeId</em> 是全局趋势递增的。</li> 
 <li> <em>SnowflakeId</em> 不对任何第三方中间件有强依赖关系，并且性能也非常高。</li> 
 <li> 位分配方案可以按照业务系统需要灵活配置，来达到最优使用效果。</li> 
 <li> 强依赖本机时钟，潜在的<strong>时钟回拨</strong>问题会导致 ID 重复。</li> 
 <li> <code>machineId</code> 需要手动设置，实际部署时如果采用手动分配 <code>machineId</code>，会非常低效。</li> 
</ul> 
<hr> 
<p style="text-align:left"><em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%2Ftree%2Fmain%2Fcosid-core%2Fsrc%2Fmain%2Fjava%2Fme%2Fahoo%2Fcosid%2Fsnowflake" target="_blank">CosId-SnowflakeId</a> </em>主要解决 <em>SnowflakeId</em> 俩大问题：机器号分配问题、时钟回拨问题。 并且提供更加友好、灵活的使用体验。</p> 
<h3 style="text-align:left">MachineIdDistributor (MachineId 分配器)</h3> 
<blockquote> 
 <p>目前 <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId" target="_blank">CosId</a></em> 提供了以下三种 <code>MachineId</code> 分配器。</p> 
</blockquote> 
<h4 style="text-align:left">ManualMachineIdDistributor</h4> 
<pre style="text-align:left"><code>cosid:
  snowflake:
    machine:
      distributor:
        type: manual
        manual:
          machine-id: 0
</code></pre> 
<blockquote> 
 <p>手动分配 <code>MachineId</code></p> 
</blockquote> 
<h4 style="text-align:left">StatefulSetMachineIdDistributor</h4> 
<pre style="text-align:left"><code>cosid:
  snowflake:
    machine:
      distributor:
        type: stateful_set
</code></pre> 
<blockquote> 
 <p>使用 <code>Kubernetes</code> 的 <code>StatefulSet</code> 提供的稳定的标识 ID 作为机器号。</p> 
</blockquote> 
<h4 style="text-align:left">RedisMachineIdDistributor</h4> 
<pre style="text-align:left"><code>cosid:
  snowflake:
    machine:
      distributor:
        type: redis
</code></pre> 
<blockquote> 
 <p>使用 <code>Redis</code> 作为机器号的分发存储。</p> 
</blockquote> 
<h3 style="text-align:left">ClockBackwardsSynchronizer (时钟回拨同步器)</h3> 
<pre style="text-align:left"><code>cosid:
  snowflake:
    clock-backwards:
      spin-threshold: 10
      broken-threshold: 2000
</code></pre> 
<p style="text-align:left">默认提供的 <code>DefaultClockBackwardsSynchronizer</code> 时钟回拨同步器使用主动等待同步策略，<code>spinThreshold</code>(默认值 10 毫秒) 用于设置自旋等待阈值， 当大于<code>spinThreshold</code>时使用线程休眠等待时钟同步，如果超过<code>brokenThreshold</code>(默认值 2 秒)时会直接抛出<code>ClockTooManyBackwardsException</code>异常。</p> 
<h3 style="text-align:left">MachineStateStorage (机器状态存储)</h3> 
<pre style="text-align:left"><code><strong>public</strong> <strong>class</strong> <strong>MachineState</strong> &#123;
    <strong>public</strong> <strong>static</strong> <strong>final</strong> MachineState NOT_FOUND = of(-<span style="color:#008080">1</span>, -<span style="color:#008080">1</span>);
    <strong>private</strong> <strong>final</strong> <strong>int</strong> machineId;
    <strong>private</strong> <strong>final</strong> <strong>long</strong> lastTimeStamp;

    <strong>public</strong> <strong>MachineState</strong>(<strong>int</strong> machineId, <strong>long</strong> lastTimeStamp) &#123;
        <strong>this</strong>.machineId = machineId;
        <strong>this</strong>.lastTimeStamp = lastTimeStamp;
    &#125;

    <strong>public</strong> <strong>int</strong> <strong>getMachineId</strong>() &#123;
        <strong>return</strong> machineId;
    &#125;

    <strong>public</strong> <strong>long</strong> <strong>getLastTimeStamp</strong>() &#123;
        <strong>return</strong> lastTimeStamp;
    &#125;

    <strong>public</strong> <strong>static</strong> MachineState <strong>of</strong>(<strong>int</strong> machineId, <strong>long</strong> lastStamp) &#123;
        <strong>return</strong> <strong>new</strong> MachineState(machineId, lastStamp);
    &#125;
&#125;
</code></pre> 
<pre style="text-align:left"><code>cosid:
  snowflake:
    machine:
      state-storage:
        local:
          state-location: ./cosid-machine-state/
</code></pre> 
<p style="text-align:left">默认提供的 <code>LocalMachineStateStorage</code> 本地机器状态存储，使用本地文件存储机器号、最近一次时间戳，用作 <code>MachineState</code> 缓存。</p> 
<h3 style="text-align:left">ClockSyncSnowflakeId (主动时钟同步 <code>SnowflakeId</code>)</h3> 
<pre style="text-align:left"><code>cosid:
  snowflake:
    share:
      clock-sync: true
</code></pre> 
<p style="text-align:left">默认 <code>SnowflakeId</code> 当发生时钟回拨时会直接抛出 <code>ClockBackwardsException</code> 异常，而使用 <code>ClockSyncSnowflakeId</code> 会使用 <code>ClockBackwardsSynchronizer</code>主动等待时钟同步来重新生成 ID，提供更加友好的使用体验。</p> 
<h3 style="text-align:left">SafeJavaScriptSnowflakeId (<code>JavaScript</code> 安全的 <code>SnowflakeId</code>)</h3> 
<pre style="text-align:left"><code>SnowflakeId snowflakeId=SafeJavaScriptSnowflakeId.ofMillisecond(<span style="color:#008080">1</span>);
</code></pre> 
<p style="text-align:left"><code>JavaScript</code> 的 <code>Number.MAX_SAFE_INTEGER</code> 只有 53 位，如果直接将 63 位的 <code>SnowflakeId</code> 返回给前端，那么会值溢出的情况，通常我们可以将<code>SnowflakeId</code>转换为 String 类型或者自定义 <code>SnowflakeId</code> 位分配来缩短 <code>SnowflakeId</code> 的位数 使 <code>ID</code> 提供给前端时不溢出。</p> 
<h3 style="text-align:left">SnowflakeFriendlyId (可以将 <code>SnowflakeId</code> 解析成可读性更好的 <code>SnowflakeIdState</code> )</h3> 
<pre style="text-align:left"><code>cosid:
  snowflake:
    share:
      friendly: true
</code></pre> 
<pre style="text-align:left"><code><strong>public</strong> <strong>class</strong> <strong>SnowflakeIdState</strong> &#123;

    <strong>private</strong> <strong>final</strong> <strong>long</strong> id;

    <strong>private</strong> <strong>final</strong> <strong>int</strong> machineId;

    <strong>private</strong> <strong>final</strong> <strong>long</strong> sequence;

    <strong>private</strong> <strong>final</strong> LocalDateTime timestamp;
    /**
     * &#123;@link #timestamp&#125;-&#123;@link #machineId&#125;-&#123;@link #sequence&#125;
     */
    <strong>private</strong> <strong>final</strong> String friendlyId;
&#125;
</code></pre> 
<pre style="text-align:left"><code><strong>public</strong> <strong>interface</strong> <strong>SnowflakeFriendlyId</strong> <strong>extends</strong> <strong>SnowflakeId</strong> &#123;

  SnowflakeIdState <strong>friendlyId</strong>(<strong>long</strong> id);

  SnowflakeIdState <strong>ofFriendlyId</strong>(String friendlyId);

  <strong>default</strong> SnowflakeIdState <strong>friendlyId</strong>() &#123;
    <strong>long</strong> id = generate();
    <strong>return</strong> friendlyId(id);
  &#125;
&#125;
</code></pre> 
<pre style="text-align:left"><code>        SnowflakeFriendlyId snowflakeFriendlyId = <strong>new</strong> DefaultSnowflakeFriendlyId(snowflakeId);
        SnowflakeIdState idState = snowflakeFriendlyId.friendlyId();
        idState.getFriendlyId(); <em>//20210623131730192-1-0</em>
</code></pre> 
<h2 style="text-align:left">RedisIdGenerator</h2> 
<pre style="text-align:left"><code>cosid:
  redis:
    enabled: true
    share:
      offset: 0
      step: 100
    provider:
      bizA:
        offset: 10000
        step: 100
      bizB:
        offset: 10000
        step: 100
</code></pre> 
<p style="text-align:left"><code>RedisIdGenerator</code> 步长设置为 1 时（每次生成<code>ID</code>都需要执行一次 <em>Redis</em> 网络 IO 请求）<em>TPS</em> 性能约为 21W/s (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%23jmh-benchmark" target="_blank">JMH 基准测试</a>)，如果在部分场景下我们对 ID 生成的 <em>TPS</em> 性能有更高的要求，那么可以选择使用增加每次<code>ID</code>分发步长来降低网络 IO 请求频次，提高 <code>IdGenerator</code>性能（比如增加步长为 1000，性能可提升到 3545W+/s <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%23jmh-benchmark" target="_blank">JMH 基准测试</a>）。</p> 
<h2 style="text-align:left">IdGeneratorProvider</h2> 
<pre style="text-align:left"><code>cosid:
  snowflake:
    provider:
      bizA:
        #      epoch:
        #      timestamp-bit:
        sequence-bit: 12
      bizB:
        #      epoch:
        #      timestamp-bit:
        sequence-bit: 12
</code></pre> 
<pre style="text-align:left"><code>IdGenerator idGenerator = idGeneratorProvider.get(<span style="color:#dd1144">"bizA"</span>);
</code></pre> 
<p style="text-align:left">在实际使用中我们一般不会所有业务服务使用同一个 <code>IdGenerator</code> ，而是不同的业务使用不同的 <code>IdGenerator</code>，那么 <code>IdGeneratorProvider</code>就是为了解决这个问题而存在的，他是 <code>IdGenerator</code> 的容器，可以通过业务名来获取相应的 <code>IdGenerator</code>。</p> 
<h2 style="text-align:left">Examples</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%2Ftree%2Fmain%2Fcosid-example" target="_blank">CosId-Examples</a></p> 
<h2 style="text-align:left">安装</h2> 
<h3 style="text-align:left">Gradle</h3> 
<blockquote> 
 <p>Kotlin DSL</p> 
</blockquote> 
<pre style="text-align:left"><code>    val cosidVersion = "1.0.0";
    implementation("me.ahoo.cosid:spring-boot-starter-cosid:$&#123;cosidVersion&#125;")
</code></pre> 
<h3 style="text-align:left">Maven</h3> 
<pre style="text-align:left"><code><strong><?xml version="1.0" encoding="UTF-8"?></strong>

<span style="color:#55cde3"><<span style="color:#55cde3">project</span> <span style="color:#008080">xmlns</span>=<span style="color:#dd1144">"http://maven.apache.org/POM/4.0.0"</span>
         <span style="color:#008080">xmlns:xsi</span>=<span style="color:#dd1144">"http://www.w3.org/2001/XMLSchema-instance"</span>
         <span style="color:#008080">xsi:schemaLocation</span>=<span style="color:#dd1144">"http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"</span>></span>

    <span style="color:#55cde3"><<span style="color:#55cde3">modelVersion</span>></span>4.0.0<span style="color:#55cde3"></<span style="color:#55cde3">modelVersion</span>></span>
    <span style="color:#55cde3"><<span style="color:#55cde3">artifactId</span>></span>demo<span style="color:#55cde3"></<span style="color:#55cde3">artifactId</span>></span>
    <span style="color:#55cde3"><<span style="color:#55cde3">properties</span>></span>
        <span style="color:#55cde3"><<span style="color:#55cde3">cosid.version</span>></span>1.0.0<span style="color:#55cde3"></<span style="color:#55cde3">cosid.version</span>></span>
    <span style="color:#55cde3"></<span style="color:#55cde3">properties</span>></span>

    <span style="color:#55cde3"><<span style="color:#55cde3">dependencies</span>></span>
        <span style="color:#55cde3"><<span style="color:#55cde3">dependency</span>></span>
            <span style="color:#55cde3"><<span style="color:#55cde3">groupId</span>></span>me.ahoo.cosid<span style="color:#55cde3"></<span style="color:#55cde3">groupId</span>></span>
            <span style="color:#55cde3"><<span style="color:#55cde3">artifactId</span>></span>spring-boot-starter-cosid<span style="color:#55cde3"></<span style="color:#55cde3">artifactId</span>></span>
            <span style="color:#55cde3"><<span style="color:#55cde3">version</span>></span>$&#123;cosid.version&#125;<span style="color:#55cde3"></<span style="color:#55cde3">version</span>></span>
        <span style="color:#55cde3"></<span style="color:#55cde3">dependency</span>></span>
    <span style="color:#55cde3"></<span style="color:#55cde3">dependencies</span>></span>

<span style="color:#55cde3"></<span style="color:#55cde3">project</span>></span>
</code></pre> 
<h3 style="text-align:left">application.yaml</h3> 
<pre style="text-align:left"><code>cosid:
  namespace: $&#123;spring.application.name&#125;
  snowflake:
    enabled: true
    #    epoch: 1577203200000
    clock-backwards:
      spin-threshold: 10
      broken-threshold: 2000
    machine:
      #      stable: true
      #      machine-bit: 10
      #      instance-id: $&#123;HOSTNAME&#125;
      distributor:
        type: redis
      #        manual:
      #          machine-id: 0
      state-storage:
        local:
          state-location: ./cosid-machine-state/
    share:
      clock-sync: true
      friendly: true
    provider:
      bizA:
        #        timestamp-bit:
        sequence-bit: 12
      bizB:
        #        timestamp-bit:
        sequence-bit: 12

#  redis:
#    enabled: false
#    share:
#      offset: 0
#      step: 100
#    provider:
#      bizA:
#        offset: 10000
#        step: 100
#      bizB:
#        offset: 10000
#        step: 100
</code></pre> 
<h2 style="text-align:left">JMH-Benchmark</h2> 
<h3 style="text-align:left">SnowflakeId</h3> 
<pre style="text-align:left"><code>Benchmark                                                    Mode  Cnt        Score   Error  Units
SnowflakeIdBenchmark.millisecondSnowflakeId_generate        thrpt       <span style="color:#008080">4093924.313</span>          ops/s
SnowflakeIdBenchmark.safeJsMillisecondSnowflakeId_generate  thrpt        <span style="color:#008080">511542.292</span>          ops/s
SnowflakeIdBenchmark.safeJsSecondSnowflakeId_generate       thrpt        <span style="color:#008080">511939.629</span>          ops/s
SnowflakeIdBenchmark.secondSnowflakeId_generate             thrpt       <span style="color:#008080">4204761.870</span>          ops/s
</code></pre> 
<h3 style="text-align:left">RedisIdGenerator</h3> 
<pre style="text-align:left"><code>gradle cosid-redis:jmh
</code></pre> 
<pre style="text-align:left"><code>Benchmark                             Mode  Cnt         Score        Error  Units
RedisIdGeneratorBenchmark.step_1     thrpt   <span style="color:#008080">25</span>    <span style="color:#008080">220218.848</span> ±   <span style="color:#008080">2070.786</span>  ops/s
RedisIdGeneratorBenchmark.step_100   thrpt   <span style="color:#008080">25</span>   <span style="color:#008080">3605422.967</span> ±  <span style="color:#008080">13479.405</span>  ops/s
RedisIdGeneratorBenchmark.step_1000  thrpt   <span style="color:#008080">25</span>  <span style="color:#008080">36874696.252</span> ± <span style="color:#008080">357214.292</span>  ops/s</code></pre>
                                        </div>
                                      
</div>
            