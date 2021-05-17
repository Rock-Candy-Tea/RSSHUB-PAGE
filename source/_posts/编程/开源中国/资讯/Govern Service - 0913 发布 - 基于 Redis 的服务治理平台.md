
---
title: 'Govern Service - 0.9.13 发布 - 基于 Redis 的服务治理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-dashboard.png'
author: 开源中国
comments: false
date: Mon, 17 May 2021 00:01:00 GMT
thumbnail: 'https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-dashboard.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:left">Govern Service 基于 Redis 的服务治理平台（服务注册/发现 & 配置中心）</h1> 
<p style="text-align:left"><em>Govern Service</em> 是一个轻量级、低成本的服务注册、服务发现、 配置服务 SDK，通过使用现有基础设施中的 Redis （相信你已经部署了Redis），不用给运维部署带来额外的成本与负担。 借助于 Redis 的高性能， <em>Govern Service</em> 提供了超高TPS&QPS (10W+/s <a href="https://gitee.com/AhooWang/govern-service#jmh-benchmark">JMH 基准测试</a>)。<em>Govern Service</em> 结合本地进程缓存策略 + <em>Redis PubSub</em> ，实现实时进程缓存刷新，兼具无与伦比的QPS性能、进程缓存与 Redis 的实时一致性。</p> 
<h2 style="text-align:left">更新内容（0.9.13）</h2> 
<ol> 
 <li>新增支持编辑服务实例元数据 (Dashboard-UI)</li> 
 <li>新增支持当监听的配置更新时发布 <em>RefreshEvent</em></li> 
 <li>优化 Rest-API-Server 的异步操作（性能优化）</li> 
 <li>新增  Rest-API-Server 的 K8S-deployment 模版</li> 
 <li>优化 使用 monaco Web代码编辑器 编辑配置数据/实例元数据</li> 
 <li>优化 回滚配置的对比当前配置文件的修改内容</li> 
 <li>更新 最新版本（0.9.13）的 JMH 基准测试报告</li> 
</ol> 
<h2 style="text-align:left">安装</h2> 
<h3 style="text-align:left">Gradle</h3> 
<blockquote> 
 <p>Kotlin DSL</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>    <strong>val</strong> <strong>governVersion</strong> <span style="color:#eeeeee">=</span> <span style="background-color:transparent; color:#00aadd">"0.9.13"</span><span style="color:#eeeeee">;</span>
    <strong>implementation</strong><span style="color:#eeeeee">(</span><span style="background-color:transparent; color:#00aadd">"me.ahoo.govern:spring-cloud-starter-config:$&#123;governVersion&#125;"</span><span style="color:#eeeeee">)</span>
    <strong>implementation</strong><span style="color:#eeeeee">(</span><span style="background-color:transparent; color:#00aadd">"me.ahoo.govern:spring-cloud-starter-discovery:$&#123;governVersion&#125;"</span><span style="color:#eeeeee">)</span></pre> 
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
    <span style="color:#ffcc55"><govern.version></span>0.9.13<span style="color:#ffcc55"></govern.version></span>
  <span style="color:#ffcc55"></properties></span>

  <span style="color:#ffcc55"><dependencies></span>
    <span style="color:#ffcc55"><dependency></span>
      <span style="color:#ffcc55"><groupId></span>me.ahoo.govern<span style="color:#ffcc55"></groupId></span>
      <span style="color:#ffcc55"><artifactId></span>spring-cloud-starter-config<span style="color:#ffcc55"></artifactId></span>
      <span style="color:#ffcc55"><version></span>$&#123;govern.version&#125;<span style="color:#ffcc55"></version></span>
    <span style="color:#ffcc55"></dependency></span>
    <span style="color:#ffcc55"><dependency></span>
      <span style="color:#ffcc55"><groupId></span>me.ahoo.govern<span style="color:#ffcc55"></groupId></span>
      <span style="color:#ffcc55"><artifactId></span>spring-cloud-starter-discovery<span style="color:#ffcc55"></artifactId></span>
      <span style="color:#ffcc55"><version></span>$&#123;govern.version&#125;<span style="color:#ffcc55"></version></span>
    <span style="color:#ffcc55"></dependency></span>
  <span style="color:#ffcc55"></dependencies></span>

<span style="color:#ffcc55"></project></span></pre> 
 </div> 
</div> 
<h3 style="text-align:left">bootstrap.yml (Spring-Cloud-Config)</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">spring</span>:
  <span style="color:#008080">application</span>:
    <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">$&#123;service.name:govern-rest-api&#125;</span>
  <span style="color:#008080">cloud</span>:
    <span style="color:#008080">govern</span>:
      <span style="color:#008080">namespace</span>: <span style="background-color:transparent; color:#00aadd">$&#123;govern.namespace:govern-&#123;system&#125;&#125;</span>
      <span style="color:#008080">config</span>:
        <span style="color:#008080">config-id</span>: <span style="background-color:transparent; color:#00aadd">$&#123;spring.application.name&#125;.yml</span>
      <span style="color:#008080">redis</span>:
        <span style="color:#008080">mode</span>: <span style="background-color:transparent; color:#00aadd">$&#123;govern.mode:standalone&#125;</span>
        <span style="color:#008080">url</span>: <span style="background-color:transparent; color:#00aadd">$&#123;govern.redis.uri:redis://localhost:6379&#125;</span>
<span style="color:#008080">logging</span>:
  <span style="color:#008080">file</span>:
    <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">logs/$&#123;spring.application.name&#125;.log</span>
</pre> 
 </div> 
</div> 
<h2 style="text-align:left">REST-API Server (<code>Optional</code>)</h2> 
<h3 style="text-align:left">安装 REST-API Server</h3> 
<h4 style="text-align:left">方式一：下载可执行文件</h4> 
<blockquote> 
 <p>下载 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2Fgovern-service%2Freleases%2Fdownload%2F0.9.13%2Frest-api-0.9.13.tar" target="_blank">rest-api-server</a></p> 
</blockquote> 
<blockquote> 
 <p>解压 <em>rest-api-0.9.13.tar</em></p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#0086b3">cd </span>rest-api-0.9.13
<em># 工作目录: rest-api-0.9.13</em>
bin/rest-api <span style="color:#ffcc55">--server</span>.port=8080 <span style="color:#ffcc55">--govern</span>.redis.uri=redis://localhost:6379</pre> 
 </div> 
</div> 
<h4 style="text-align:left">方式二：Docker run</h4> 
<div style="text-align:left"> 
 <div> 
  <pre>docker pull ahoowang/govern-service:0.9.13
docker run <span style="color:#ffcc55">--name</span> govern-service <span style="color:#ffcc55">-d</span> <span style="color:#ffcc55">-p</span> 8080:8080 <span style="color:#ffcc55">--link</span> redis <span style="color:#ffcc55">-e</span> <span style="color:#ffaa44">GOVERN_REDIS_URI</span>=redis://redis:6379  ahoowang/govern-service:0.9.13</pre> 
 </div> 
</div> 
<hr> 
<blockquote> 
 <p>MacBook Pro (M1)</p> 
 <p>请使用 <em>ahoowang/govern-service:0.9.13-armv7</em></p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>docker pull ahoowang/govern-service:0.9.13-armv7
docker run <span style="color:#ffcc55">--name</span> govern-service <span style="color:#ffcc55">-d</span> <span style="color:#ffcc55">-p</span> 8080:8080 <span style="color:#ffcc55">--link</span> redis <span style="color:#ffcc55">-e</span> <span style="color:#ffaa44">GOVERN_REDIS_URI</span>=redis://redis:6379  ahoowang/govern-service:0.9.13-armv7</pre> 
 </div> 
</div> 
<hr> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Fdashboard" target="_blank">http://localhost:8080/dashboard</a></p> 
</blockquote> 
<h3 style="text-align:left">Dashboard</h3> 
<p style="text-align:left"><img alt="dashboard-dashboard" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-dashboard.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">命名空间管理</h4> 
<p style="text-align:left"><img alt="dashboard-namespace" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-namespace.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">配置管理</h4> 
<h2 style="text-align:left"><img alt="dashboard-config" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-config.png" referrerpolicy="no-referrer"></h2> 
<h2 style="text-align:left"><img alt="dashboard-config-edit" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-config-edit.png" referrerpolicy="no-referrer"></h2> 
<h2 style="text-align:left"><img alt="dashboard-config-rollback" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-config-rollback.png" referrerpolicy="no-referrer"></h2> 
<p style="text-align:left"><img alt="dashboard-config-import" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-config-import.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">服务管理</h4> 
<h2 style="text-align:left"><img alt="dashboard-service" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-service.png" referrerpolicy="no-referrer"></h2> 
<p style="text-align:left"><img alt="dashboard-service-edit" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-service-edit.png" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">REST-API</h3> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Fswagger-ui%2Findex.html%23%2F" target="_blank">http://localhost:8080/swagger-ui/index.html#/</a></p> 
</blockquote> 
<p>Namespace</p> 
<p style="text-align:left"><img alt="rest-api-namespace" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/rest-api-namespace.png" referrerpolicy="no-referrer"></p> 
<p><strong>Config</strong></p> 
<p style="text-align:left"><img height="476" src="https://oscimg.oschina.net/oscnet/up-ad9940ec94f1123d872682adfcad73e7e46.png" width="1453" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><span style="color:#333333">Service</span></p> 
<p style="text-align:left"><img alt="rest-api-service" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/rest-api-service.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">JMH-Benchmark</h2> 
<ul> 
 <li>基准测试运行环境：笔记本开发机 ( MacBook Pro (M1) )</li> 
 <li>所有基准测试都在开发笔记本上执行。</li> 
 <li>Redis 部署环境也在该笔记本开发机上。</li> 
</ul> 
<h3 style="text-align:left">ConfigService</h3> 
<div style="text-align:left"> 
 <div> 
  <pre>gradle config:jmh</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre># JMH version: 1.29
# VM version: JDK 11.0.11, OpenJDK 64-Bit Server VM, 11.0.11+9-LTS
# VM invoker: /Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home/bin/java
# VM options: -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/Users/ahoo/govern-service/config/build/tmp/jmh -Duser.country=CN -Duser.language=zh -Duser.variant
# Blackhole mode: full + dont-inline hint
# Warmup: 1 iterations, 10 s each
# Measurement: 1 iterations, 10 s each
# Timeout: 10 min per iteration
# Threads: 50 threads, will synchronize iterations
# Benchmark mode: Throughput, ops/time

Benchmark                                          Mode  Cnt          Score   Error  Units
ConsistencyRedisConfigServiceBenchmark.getConfig  thrpt       265321650.148          ops/s
RedisConfigServiceBenchmark.getConfig             thrpt          106991.476          ops/s
RedisConfigServiceBenchmark.setConfig             thrpt          103659.132          ops/s</pre> 
 </div> 
</div> 
<h3 style="text-align:left">ServiceDiscovery</h3> 
<div style="text-align:left"> 
 <div> 
  <pre>gradle discovery:jmh</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre># JMH version: 1.29
# VM version: JDK 11.0.11, OpenJDK 64-Bit Server VM, 11.0.11+9-LTS
# VM invoker: /Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home/bin/java
# VM options: -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/Users/ahoo/govern-service/discovery/build/tmp/jmh -Duser.country=CN -Duser.language=zh -Duser.variant
# Blackhole mode: full + dont-inline hint
# Warmup: 1 iterations, 10 s each
# Measurement: 1 iterations, 10 s each
# Timeout: 10 min per iteration
# Threads: 50 threads, will synchronize iterations
# Benchmark mode: Throughput, ops/time

Benchmark                                                Mode  Cnt          Score   Error  Units
ConsistencyRedisServiceDiscoveryBenchmark.getInstances  thrpt        76894658.867          ops/s
ConsistencyRedisServiceDiscoveryBenchmark.getServices   thrpt       466036317.472          ops/s
RedisServiceDiscoveryBenchmark.getInstances             thrpt          107778.244          ops/s
RedisServiceDiscoveryBenchmark.getServices              thrpt          106920.412          ops/s
RedisServiceRegistryBenchmark.deregister                thrpt          114094.513          ops/s
RedisServiceRegistryBenchmark.register                  thrpt          109085.694          ops/s
RedisServiceRegistryBenchmark.renew                     thrpt          127003.104          ops/s</pre> 
 </div> 
</div> 
<h2 style="text-align:left"> </h2>
                                        </div>
                                      
</div>
            