
---
title: 'CosId 1.0.4 发布，通用、灵活、高性能的分布式 ID 生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/AhooWang/CosId/raw/main/docs/Snowflake-identifier.png'
author: 开源中国
comments: false
date: Thu, 01 Jul 2021 23:49:00 GMT
thumbnail: 'https://gitee.com/AhooWang/CosId/raw/main/docs/Snowflake-identifier.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId" target="_blank">CosId</a> 通用、灵活、高性能的分布式 ID 生成器</h1> 
<h2 style="text-align:left">介绍</h2> 
<p style="text-align:left"><em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId" target="_blank">CosId</a></em> 旨在提供通用、灵活、高性能的分布式系统 ID 生成器。 目前提供了俩大类 ID 生成器：<em>SnowflakeId</em> （单机 TPS 性能：409W/s <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%23jmh-benchmark" target="_blank">JMH 基准测试</a>）、<em>RedisIdGenerator</em> (单机 TPS 性能(步长 1000)：3687W+/s <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%23jmh-benchmark" target="_blank">JMH 基准测试</a>)。</p> 
<h2 style="text-align:left">更新内容（1.0.4） 🎉 🎉 🎉</h2> 
<ol> 
 <li>增强：支持同时启用 RedisIdGenerator / SnowflakeId 模式的分布式ID生成器（spring-boot-starter-cosid）。</li> 
</ol> 
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
<p style="text-align:left"><code>JavaScript</code> 的 <code>Number.MAX_SAFE_INTEGER</code> 只有 53 位，如果直接将 63 位的 <code>SnowflakeId</code> 返回给前端，那么会值溢出的情况，通常我们可以将<code>SnowflakeId</code>转换为 <code>String</code> 类型或者自定义 <code>SnowflakeId</code> 位分配来缩短 <code>SnowflakeId</code> 的位数 使 <code>ID</code> 提供给前端时不溢出。</p> 
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
  <pre>        <strong>SnowflakeFriendlyId</strong> snowflakeFriendlyId = <strong>new</strong> <strong>DefaultSnowflakeFriendlyId</strong>(snowflakeId);
        <strong>SnowflakeIdState</strong> idState = snowflakeFriendlyId.<span style="color:#008080">friendlyId</span>();
        idState.<span style="color:#008080">getFriendlyId</span>(); <span style="color:#888888">//20210623131730192-1-0</span></pre> 
 </div> 
</div> 
<h2 style="text-align:left">RedisIdGenerator</h2> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">cosid</span>:
  <span style="color:#008080">redis</span>:
    <span style="color:#008080">enabled</span>: <span style="color:turquoise">true</span>
    <span style="color:#008080">share</span>:
      <span style="color:#008080">offset</span>: <strong>0</strong>
      <span style="color:#008080">step</span>: <strong>100</strong>
    <span style="color:#008080">provider</span>:
      <span style="color:#008080">bizA</span>:
        <span style="color:#008080">offset</span>: <strong>10000</strong>
        <span style="color:#008080">step</span>: <strong>100</strong>
      <span style="color:#008080">bizB</span>:
        <span style="color:#008080">offset</span>: <strong>10000</strong>
        <span style="color:#008080">step</span>: <strong>100</strong></pre> 
 </div> 
</div> 
<p style="text-align:left"><code>RedisIdGenerator</code> 步长设置为 1 时（每次生成<code>ID</code>都需要执行一次 <em>Redis</em> 网络 IO 请求）<em>TPS</em> 性能约为 21W/s (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%23jmh-benchmark" target="_blank">JMH 基准测试</a>)，如果在部分场景下我们对 ID 生成的 <em>TPS</em> 性能有更高的要求，那么可以选择使用增加每次<code>ID</code>分发步长来降低网络 IO 请求频次，提高 <code>IdGenerator</code> 性能（比如增加步长为 1000，性能可提升到 3545W+/s <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%23jmh-benchmark" target="_blank">JMH 基准测试</a>）。</p> 
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
  <pre><strong>IdGenerator</strong> idGenerator = idGeneratorProvider.<span style="color:#008080">get</span>(<span style="background-color:transparent; color:#00aadd">"bizA"</span>);</pre> 
 </div> 
</div> 
<p style="text-align:left">在实际使用中我们一般不会所有业务服务使用同一个 <code>IdGenerator</code> ，而是不同的业务使用不同的 <code>IdGenerator</code>，那么 <code>IdGeneratorProvider</code> 就是为了解决这个问题而存在的，他是 <code>IdGenerator</code> 的容器，可以通过业务名来获取相应的 <code>IdGenerator</code>。</p> 
<h2 style="text-align:left">Examples</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCosId%2Ftree%2Fmain%2Fcosid-example" target="_blank">CosId-Examples</a></p> 
<h2 style="text-align:left">安装</h2> 
<h3 style="text-align:left">Gradle</h3> 
<blockquote> 
 <p>Kotlin DSL</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>    <strong>val</strong> <strong>cosidVersion</strong> <span style="color:#eeeeee">=</span> <span style="background-color:transparent; color:#00aadd">"1.0.4"</span><span style="color:#eeeeee">;</span>
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
        <span style="color:#ffcc55"><cosid.version></span>1.0.4<span style="color:#ffcc55"></cosid.version></span>
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
  <pre><span style="color:#008080">cosid</span>:
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

<span style="color:#888888">#  redis:</span>
<span style="color:#888888">#    enabled: false</span>
<span style="color:#888888">#    share:</span>
<span style="color:#888888">#      offset: 0</span>
<span style="color:#888888">#      step: 100</span>
<span style="color:#888888">#    provider:</span>
<span style="color:#888888">#      bizA:</span>
<span style="color:#888888">#        offset: 10000</span>
<span style="color:#888888">#        step: 100</span>
<span style="color:#888888">#      bizB:</span>
<span style="color:#888888">#        offset: 10000</span>
<span style="color:#888888">#        step: 100</span></pre> 
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
  <pre>Benchmark                                                    Mode  Cnt        Score   Error  Units
SnowflakeIdBenchmark.millisecondSnowflakeId_generate        thrpt       4093924.313          ops/s
SnowflakeIdBenchmark.safeJsMillisecondSnowflakeId_generate  thrpt        511542.292          ops/s
SnowflakeIdBenchmark.safeJsSecondSnowflakeId_generate       thrpt        511939.629          ops/s
SnowflakeIdBenchmark.secondSnowflakeId_generate             thrpt       4204761.870          ops/s</pre> 
 </div> 
</div> 
<h3 style="text-align:left">RedisIdGenerator</h3> 
<div style="text-align:left"> 
 <div> 
  <pre>gradle cosid-redis:jmh</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre>Benchmark                             Mode  Cnt         Score        Error  Units
RedisIdGeneratorBenchmark.step_1     thrpt   25    220218.848 ±   2070.786  ops/s
RedisIdGeneratorBenchmark.step_100   thrpt   25   3605422.967 ±  13479.405  ops/s
RedisIdGeneratorBenchmark.step_1000  thrpt   25  36874696.252 ± 357214.292  ops/s</pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            