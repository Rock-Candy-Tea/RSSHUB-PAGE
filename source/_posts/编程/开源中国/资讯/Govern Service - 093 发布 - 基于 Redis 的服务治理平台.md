
---
title: 'Govern Service - 0.9.3 发布 - 基于 Redis 的服务治理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-dashboard.png'
author: 开源中国
comments: false
date: Sat, 15 May 2021 00:54:00 GMT
thumbnail: 'https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-dashboard.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:left">Govern Service 基于 Redis 的服务治理平台（服务注册/发现 & 配置中心）</h1> 
<p style="text-align:left"><em>Govern Service</em> 是一个轻量级、低成本的服务注册、服务发现、 配置服务 SDK，通过使用现有基础设施中的 Redis （相信你已经部署了Redis），不用给运维部署带来额外的成本与负担。 借助于 Redis 的高性能， * Govern Service* 提供了超高TPS&QPS。<em>Govern Service</em> 结合本地进程缓存策略 + <em>Redis PubSub</em>，实现实时进程缓存刷新，兼具无与伦比的QPS性能、进程缓存与 Redis 的实时一致性。</p> 
<h2 style="text-align:left">更新内容（0.9.3）</h2> 
<p>1. 修复 Dashboard 刷新页面 404 的问题<br> 2. 新增 ServiceRegistry.setService api<br> 3. 新增 ServiceRegistry.removeService api<br> 4. 新增 ServiceStatistic.getInstanceCount api<br> 5. 新增 Dashboard-UI 管理 Config/Service/Namespace 的完整支持</p> 
<h2 style="text-align:left">安装</h2> 
<h3 style="text-align:left">Gradle</h3> 
<blockquote> 
 <p>Kotlin DSL</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>    <strong>val</strong> <strong>governVersion</strong> <span style="color:#eeeeee">=</span> <span style="background-color:transparent; color:#00aadd">"0.9.3"</span><span style="color:#eeeeee">;</span>
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
    <span style="color:#ffcc55"><govern.version></span>0.9.3<span style="color:#ffcc55"></govern.version></span>
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
    <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">govern-rest-api</span>
  <span style="color:#008080">cloud</span>:
    <span style="color:#008080">govern</span>:
      <span style="color:#008080">namespace</span>: <span style="background-color:transparent; color:#00aadd">dev</span>
      <span style="color:#008080">config</span>:
        <span style="color:#008080">config-id</span>: <span style="background-color:transparent; color:#00aadd">$&#123;spring.application.name&#125;.yml</span>
      <span style="color:#008080">redis</span>:
        <span style="color:#008080">mode</span>: <span style="background-color:transparent; color:#00aadd">standalone</span>
        <span style="color:#008080">url</span>: <span style="background-color:transparent; color:#00aadd">redis://localhost:6379</span></pre> 
 </div> 
</div> 
<h2 style="text-align:left">REST-API Server (<code>Optional</code>)</h2> 
<div style="text-align:left"> 
 <div> 
  <pre>bin/rest-api</pre> 
 </div> 
</div> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2F" target="_blank">http://localhost:8080/</a></p> 
</blockquote> 
<h3 style="text-align:left">Dashboard</h3> 
<p style="text-align:left"><img alt="dashboard-dashboard" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-dashboard.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">命名空间管理</h4> 
<p style="text-align:left"><img alt="dashboard-namespace" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-namespace.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">配置管理</h4> 
<h2 style="text-align:left"><img alt="dashboard-config" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-config.png" referrerpolicy="no-referrer"></h2> 
<h2 style="text-align:left"><img alt="dashboard-config-edit" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-config-edit.png" referrerpolicy="no-referrer"></h2> 
<p style="text-align:left"><img alt="dashboard-config-rollback" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-config-rollback.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">服务管理</h4> 
<h2 style="text-align:left"><img alt="dashboard-service" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-service.png" referrerpolicy="no-referrer"></h2> 
<p style="text-align:left"><img alt="dashboard-service-edit" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-service-edit.png" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">REST-API</h3> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Fswagger-ui%2Findex.html%23%2F" target="_blank">http://localhost:8080/swagger-ui/index.html#/</a></p> 
</blockquote> 
<p>Namespace</p> 
<p style="text-align:left"><img alt="rest-api-namespace" height="378" src="https://oscimg.oschina.net/oscnet/up-d3d0f734dd33a8e65426360a40ca7647c30.png" width="1456" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><span style="color:#333333">Config</span></p> 
<p style="text-align:left"><img height="476" src="https://oscimg.oschina.net/oscnet/up-b4b8f444522bf2073b3461acc8cc885e364.png" width="1453" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">Service</h4> 
<p style="text-align:left"><img alt="rest-api-service" height="593" src="https://oscimg.oschina.net/oscnet/up-34c7430781fd29cb6a3b58283fde3e58a50.png" width="1464" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><span style="color:#333333">JMH 基准测试</span></p> 
<ul> 
 <li>The development notebook : MacBook Pro (M1)</li> 
 <li>All benchmark tests are carried out on the development notebook.</li> 
 <li>Deploying Redis with docker on the development notebook.</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre>gradle jmh</pre> 
 </div> 
</div> 
<h3 style="text-align:left">ConfigService</h3> 
<div style="text-align:left"> 
 <div> 
  <pre># JMH version: 1.28
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
ConsistencyRedisConfigServiceBenchmark.getConfig  thrpt       555275866.836          ops/s
RedisConfigServiceBenchmark.getConfig             thrpt           57397.188          ops/s
RedisConfigServiceBenchmark.setConfig             thrpt           56882.673          ops/s</pre> 
 </div> 
</div> 
<h3 style="text-align:left">ServiceDiscovery</h3> 
<div style="text-align:left"> 
 <div> 
  <pre># JMH version: 1.29
# VM version: JDK 11.0.11, OpenJDK 64-Bit Server VM, 11.0.11+9-LTS
# VM invoker: /Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home/bin/java
# VM options: -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/Users/ahoo/work/ahoo-git/govern-service/discovery/build/tmp/jmh -Duser.country=CN -Duser.language=zh -Duser.variant
# Blackhole mode: full + dont-inline hint
# Warmup: 1 iterations, 10 s each
# Measurement: 1 iterations, 10 s each
# Timeout: 10 min per iteration
# Threads: 50 threads, will synchronize iterations
# Benchmark mode: Throughput, ops/time

Benchmark                                                Mode  Cnt           Score   Error  Units
ConsistencyRedisServiceDiscoveryBenchmark.getInstances  thrpt        567329996.255          ops/s
ConsistencyRedisServiceDiscoveryBenchmark.getServices   thrpt       1929377291.635          ops/s
RedisServiceDiscoveryBenchmark.getInstances             thrpt            43760.035          ops/s
RedisServiceDiscoveryBenchmark.getServices              thrpt            60953.971          ops/s
RedisServiceRegistryBenchmark.deregister                thrpt            63133.011          ops/s
RedisServiceRegistryBenchmark.register                  thrpt            53957.797          ops/s
RedisServiceRegistryBenchmark.renew                     thrpt            67116.116          ops/s</pre> 
 </div> 
</div> 
<h2 style="text-align:left">TODO</h2> 
<ol> 
 <li>Import/Export API</li> 
 <li>Grayscale Publishing</li> 
</ol>
                                        </div>
                                      
</div>
            