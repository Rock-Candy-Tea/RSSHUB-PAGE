
---
title: 'Govern Service - 0.9.2 发布 - 基于 Redis 的服务治理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f37615ab6907049d52efce7871a7ce82446.png'
author: 开源中国
comments: false
date: Fri, 14 May 2021 01:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f37615ab6907049d52efce7871a7ce82446.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:left">基于 Redis 的服务治理平台（服务注册/发现 & 配置中心）</h1> 
<p style="text-align:left"><em>Govern Service</em> 是一个轻量级、低成本的服务注册、服务发现、 配置服务 SDK，通过使用现有基础设施中的 Redis （相信你已经部署了Redis），不用给运维部署带来额外的成本与负担。 借助于 Redis 的高性能， * Govern Service* 提供了超高TPS&QPS。<em>Govern Service</em> 结合本地进程缓存策略 + <em>Redis PubSub</em>，实现实时进程缓存刷新，兼具无与伦比的QPS性能、进程缓存与 Redis 的实时一致性。</p> 
<h2 style="text-align:left">更新内容（0.9.2）</h2> 
<p style="text-align:left">1. 优化 Redis 集群模式的支持</p> 
<p style="text-align:left">2. 添加 对可视化管理平台的支持 Dashboard (beta)</p> 
<p style="text-align:left"><img alt height="912" src="https://oscimg.oschina.net/oscnet/up-f37615ab6907049d52efce7871a7ce82446.png" width="1130" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt height="397" src="https://oscimg.oschina.net/oscnet/up-4c9d83183f56fb83dada5da9c775efb8b63.png" width="1299" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">安装</h2> 
<h3 style="text-align:left">Gradle</h3> 
<div style="text-align:left"> 
 <div> 
  <pre>    <strong><span style="color:#d73a49"><span style="color:#d73a49">val</span></span></strong> <strong>governVersion</strong> <span style="color:#eeeeee">=</span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62"><span style="color:#032f62">"0.9.2"</span></span></span><span style="color:#eeeeee">;</span>
    <strong>implementation</strong><span style="color:#eeeeee">(</span><span style="background-color:transparent; color:#00aadd"><span style="color:#032f62"><span style="color:#032f62">"me.ahoo.govern:spring-cloud-starter-config:$&#123;governVersion&#125;"</span></span></span><span style="color:#eeeeee">)</span>
    <strong>implementation</strong><span style="color:#eeeeee">(</span><span style="background-color:transparent; color:#00aadd"><span style="color:#032f62"><span style="color:#032f62">"me.ahoo.govern:spring-cloud-starter-discovery:$&#123;governVersion&#125;"</span></span></span><span style="color:#eeeeee">)</span></pre> 
 </div> 
</div> 
<h3 style="text-align:left">Maven</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><strong><span style="color:#6a737d"><span style="color:#6a737d"><?xml version="1.0" encoding="UTF-8"?></span></span></strong>

<span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">project</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">xmlns</span></span></span><span style="color:#333333">=</span></span></span><span style="background-color:transparent; color:#00aadd"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"http://maven.apache.org/POM/4.0.0"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">
         </span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">xmlns:xsi</span></span></span><span style="color:#333333">=</span></span></span><span style="background-color:transparent; color:#00aadd"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"http://www.w3.org/2001/XMLSchema-instance"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">
         </span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">xsi:schemaLocation</span></span></span><span style="color:#333333">=</span></span></span><span style="background-color:transparent; color:#00aadd"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"</span></span></span></span></span><span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333">></span></span></span>

  <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">modelVersion</span></span></span><span style="color:#333333">></span></span></span>4.0.0<span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">modelVersion</span></span></span><span style="color:#333333">></span></span></span>
  <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span></span>demo<span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span></span>
  <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">properties</span></span></span><span style="color:#333333">></span></span></span>
    <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">govern.version</span></span></span><span style="color:#333333">></span></span></span>0.9.2<span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">govern.version</span></span></span><span style="color:#333333">></span></span></span>
  <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">properties</span></span></span><span style="color:#333333">></span></span></span>

  <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependencies</span></span></span><span style="color:#333333">></span></span></span>
    <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span></span></span>me.ahoo.govern<span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span></span>spring-cloud-starter-config<span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span></span></span>$&#123;govern.version&#125;<span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span></span></span>
    <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span></span></span>
    <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span></span></span>me.ahoo.govern<span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span></span>spring-cloud-starter-discovery<span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span></span></span>$&#123;govern.version&#125;<span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span></span></span>
    <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span></span></span>
  <span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependencies</span></span></span><span style="color:#333333">></span></span></span>

<span style="color:#ffcc55"><span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">project</span></span></span><span style="color:#333333">></span></span></span></pre> 
 </div> 
</div> 
<h3 style="text-align:left">bootstrap.yml (Spring-Cloud-Config)</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1">spring</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1">:</span></span>
  <span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1">application</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1">:</span></span>
    <span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1">name</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1">:</span></span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62"><span style="color:#032f62">govern-rest-api</span></span></span>
  <span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1">cloud</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1">:</span></span>
    <span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1">govern</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1">:</span></span>
      <span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1">namespace</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1">:</span></span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62"><span style="color:#032f62">dev</span></span></span>
      <span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1">config</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1">:</span></span>
        <span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1">config-id</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1">:</span></span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62"><span style="color:#032f62">$&#123;spring.application.name&#125;.yml</span></span></span>
      <span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1">redis</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1">:</span></span>
        <span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1">mode</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1">:</span></span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62"><span style="color:#032f62">standalone</span></span></span>
        <span style="color:#008080"><span style="color:#6f42c1"><span style="color:#6f42c1">url</span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1">:</span></span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62"><span style="color:#032f62">redis://localhost:6379</span></span></span></pre> 
 </div> 
</div> 
<h2 style="text-align:left">REST-API Server (<code>Optional</code>)</h2> 
<div style="text-align:left"> 
 <div> 
  <pre>bin/rest-api</pre> 
 </div> 
</div> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Fswagger-ui%2Findex.html%23%2F" target="_blank">http://localhost:8080/swagger-ui/index.html#/</a></p> 
</blockquote> 
<h3 style="text-align:left">Namespace</h3> 
<p style="text-align:left"><img alt="rest-api-namespace" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/rest-api-namespace.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>/v1/namespaces 
  <ul> 
   <li>GET</li> 
  </ul> </li> 
 <li>/v1/namespaces/&#123;namespace&#125; 
  <ul> 
   <li>PUT</li> 
   <li>GET</li> 
  </ul> </li> 
 <li>/v1/namespaces/current 
  <ul> 
   <li>GET</li> 
  </ul> </li> 
 <li>/v1/namespaces/current/&#123;namespace&#125; 
  <ul> 
   <li>PUT</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:left">Config</h3> 
<p style="text-align:left"><img alt="rest-api-config" src="https://oscimg.oschina.net/oscnet/up-d2476cf9f4c2585b00293c7ca7a9a7390a7.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>/v1/namespaces/&#123;namespace&#125;/configs 
  <ul> 
   <li>GET</li> 
  </ul> </li> 
 <li>/v1/namespaces/&#123;namespace&#125;/configs/&#123;configId&#125; 
  <ul> 
   <li>GET</li> 
   <li>PUT 
    <ul> 
     <li>DELETE</li> 
    </ul> </li> 
  </ul> </li> 
 <li>/v1/namespaces/&#123;namespace&#125;/configs/&#123;configId&#125;/versions 
  <ul> 
   <li>GET</li> 
  </ul> </li> 
 <li>/v1/namespaces/&#123;namespace&#125;/configs/&#123;configId&#125;/versions/&#123;version&#125; 
  <ul> 
   <li>GET</li> 
  </ul> </li> 
 <li>/v1/namespaces/&#123;namespace&#125;/configs/&#123;configId&#125;/to/&#123;targetVersion&#125; 
  <ul> 
   <li>PUT</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:left">Service</h3> 
<p style="text-align:left"><img alt="rest-api-service" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/rest-api-service.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>/v1/namespaces/&#123;namespace&#125;/services/ 
  <ul> 
   <li>GET</li> 
  </ul> </li> 
 <li>/v1/namespaces/&#123;namespace&#125;/services/&#123;serviceId&#125;/instances 
  <ul> 
   <li>GET</li> 
   <li>PUT</li> 
  </ul> </li> 
 <li>/v1/namespaces/&#123;namespace&#125;/services/&#123;serviceId&#125;/instances/&#123;instanceId&#125; 
  <ul> 
   <li>DELETE</li> 
  </ul> </li> 
 <li>/v1/namespaces/&#123;namespace&#125;/services/&#123;serviceId&#125;/instances/&#123;instanceId&#125;/metadata 
  <ul> 
   <li>PUT</li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:left">JMH 基准测试</h2> 
<ul> 
 <li>The development notebook : MacBook Pro (M1)</li> 
 <li>All benchmark tests are carried out on the development notebook.</li> 
 <li>Deploying Redis with docker on the development notebook.</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#6f42c1"><span style="color:#6f42c1">gradle</span></span> <span style="color:#032f62"><span style="color:#032f62">jmh</span></span></pre> 
 </div> 
</div> 
<h3 style="text-align:left">ConfigService</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#6a737d"><span style="color:#6a737d"># JMH version: 1.28</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># VM version: JDK 11.0.11, OpenJDK 64-Bit Server VM, 11.0.11+9-LTS</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># VM invoker: /Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home/bin/java</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># VM options: -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/Users/ahoo/govern-service/config/build/tmp/jmh -Duser.country=CN -Duser.language=zh -Duser.variant</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Blackhole mode: full + dont-inline hint</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Warmup: 1 iterations, 10 s each</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Measurement: 1 iterations, 10 s each</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Timeout: 10 min per iteration</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Threads: 50 threads, will synchronize iterations</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Benchmark mode: Throughput, ops/time</span></span>

<span style="color:#032f62"><span style="color:#032f62">Benchmark</span></span>                                          <span style="color:#032f62"><span style="color:#032f62">Mode</span></span>  <span style="color:#032f62"><span style="color:#032f62">Cnt</span></span>          <span style="color:#032f62"><span style="color:#032f62">Score</span></span>   <span style="color:#032f62"><span style="color:#032f62">Error</span></span>  <span style="color:#032f62"><span style="color:#032f62">Units</span></span>
<span style="color:#032f62"><span style="color:#032f62">ConsistencyRedisConfigServiceBenchmark.getConfig</span></span>  <span style="color:#032f62"><span style="color:#032f62">thrpt</span></span>       555275866.836          <span style="color:#032f62"><span style="color:#032f62">ops/s</span></span>
<span style="color:#032f62"><span style="color:#032f62">RedisConfigServiceBenchmark.getConfig</span></span>             <span style="color:#032f62"><span style="color:#032f62">thrpt</span></span>           57397.188          <span style="color:#032f62"><span style="color:#032f62">ops/s</span></span>
<span style="color:#032f62"><span style="color:#032f62">RedisConfigServiceBenchmark.setConfig</span></span>             <span style="color:#032f62"><span style="color:#032f62">thrpt</span></span>           56882.673          <span style="color:#032f62"><span style="color:#032f62">ops/s</span></span></pre> 
 </div> 
</div> 
<h3 style="text-align:left">ServiceDiscovery</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#6a737d"><span style="color:#6a737d"># JMH version: 1.29</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># VM version: JDK 11.0.11, OpenJDK 64-Bit Server VM, 11.0.11+9-LTS</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># VM invoker: /Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home/bin/java</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># VM options: -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/Users/ahoo/work/ahoo-git/govern-service/discovery/build/tmp/jmh -Duser.country=CN -Duser.language=zh -Duser.variant</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Blackhole mode: full + dont-inline hint</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Warmup: 1 iterations, 10 s each</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Measurement: 1 iterations, 10 s each</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Timeout: 10 min per iteration</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Threads: 50 threads, will synchronize iterations</span></span>
<span style="color:#6a737d"><span style="color:#6a737d"># Benchmark mode: Throughput, ops/time</span></span>

<span style="color:#032f62"><span style="color:#032f62">Benchmark</span></span>                                                <span style="color:#032f62"><span style="color:#032f62">Mode</span></span>  <span style="color:#032f62"><span style="color:#032f62">Cnt</span></span>           <span style="color:#032f62"><span style="color:#032f62">Score</span></span>   <span style="color:#032f62"><span style="color:#032f62">Error</span></span>  <span style="color:#032f62"><span style="color:#032f62">Units</span></span>
<span style="color:#032f62"><span style="color:#032f62">ConsistencyRedisServiceDiscoveryBenchmark.getInstances</span></span>  <span style="color:#032f62"><span style="color:#032f62">thrpt</span></span>        567329996.255          <span style="color:#032f62"><span style="color:#032f62">ops/s</span></span>
<span style="color:#032f62"><span style="color:#032f62">ConsistencyRedisServiceDiscoveryBenchmark.getServices</span></span>   <span style="color:#032f62"><span style="color:#032f62">thrpt</span></span>       1929377291.635          <span style="color:#032f62"><span style="color:#032f62">ops/s</span></span>
<span style="color:#032f62"><span style="color:#032f62">RedisServiceDiscoveryBenchmark.getInstances</span></span>             <span style="color:#032f62"><span style="color:#032f62">thrpt</span></span>            43760.035          <span style="color:#032f62"><span style="color:#032f62">ops/s</span></span>
<span style="color:#032f62"><span style="color:#032f62">RedisServiceDiscoveryBenchmark.getServices</span></span>              <span style="color:#032f62"><span style="color:#032f62">thrpt</span></span>            60953.971          <span style="color:#032f62"><span style="color:#032f62">ops/s</span></span>
<span style="color:#032f62"><span style="color:#032f62">RedisServiceRegistryBenchmark.deregister</span></span>                <span style="color:#032f62"><span style="color:#032f62">thrpt</span></span>            63133.011          <span style="color:#032f62"><span style="color:#032f62">ops/s</span></span>
<span style="color:#032f62"><span style="color:#032f62">RedisServiceRegistryBenchmark.register</span></span>                  <span style="color:#032f62"><span style="color:#032f62">thrpt</span></span>            53957.797          <span style="color:#032f62"><span style="color:#032f62">ops/s</span></span>
<span style="color:#032f62"><span style="color:#032f62">RedisServiceRegistryBenchmark.renew</span></span>                     <span style="color:#032f62"><span style="color:#032f62">thrpt</span></span>            67116.116          <span style="color:#032f62"><span style="color:#032f62">ops/s</span></span></pre> 
 </div> 
</div> 
<h2 style="text-align:left">TODO</h2> 
<ol> 
 <li>Dashboard</li> 
 <li>Grayscale Publishing</li> 
</ol>
                                        </div>
                                      
</div>
            