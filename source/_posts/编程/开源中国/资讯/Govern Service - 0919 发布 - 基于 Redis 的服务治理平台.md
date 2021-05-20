
---
title: 'Govern Service - 0.9.19 发布 - 基于 Redis 的服务治理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-dashboard.png'
author: 开源中国
comments: false
date: Wed, 19 May 2021 23:19:00 GMT
thumbnail: 'https://gitee.com/AhooWang/govern-service/raw/main/docs/dashboard-dashboard.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align: left;">Govern Service 基于 Redis 的服务治理平台（服务注册/发现 & 配置中心）</p> 
<p style="text-align:left"><em>Govern Service</em> 是一个轻量级、低成本的服务注册、服务发现、 配置服务 SDK，通过使用现有基础设施中的 Redis （相信你已经部署了Redis），不用给运维部署带来额外的成本与负担。 借助于 Redis 的高性能， <em>Govern Service</em> 提供了超高TPS&QPS (10W+/s <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2Fgovern-service%2Fblob%2Fmain%2FREADME.zh-CN.md%23jmh-benchmark" target="_blank">JMH 基准测试</a>)。<em>Govern Service</em> 结合本地进程缓存策略 + <em>Redis PubSub</em> ，实现实时进程缓存刷新，兼具无与伦比的QPS性能、进程缓存与 Redis 的实时一致性。</p> 
<h2 style="text-align:left">更新内容（0.9.19）</h2> 
<ol> 
 <li>优化服务实例续期日志</li> 
 <li>增强搜索体验（Dashboard - UI）</li> 
 <li>更新 K8S-Deployment(REST-API) 镜像版本</li> 
 <li>优化 Rest-API-Server 的异步操作（性能优化）</li> 
 <li>优化 时间戳/日期显示（Dashboard - UI）</li> 
 <li>修复 编辑实例信息的 BUG（Dashboard - UI）</li> 
</ol> 
<h2 style="text-align:left">安装</h2> 
<h3 style="text-align:left">Gradle</h3> 
<blockquote> 
 <p>Kotlin DSL</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre style="text-align:start">    <span style="color:var(--color-prettylights-syntax-keyword)">val</span> governVersion <span style="color:var(--color-prettylights-syntax-keyword)">=</span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>0.9.19<span style="color:var(--color-prettylights-syntax-string)">"</span></span>;
    implementation(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>me.ahoo.govern:spring-cloud-starter-govern-config:<span style="color:var(--color-prettylights-syntax-entity)">$&#123;governVersion&#125;</span><span style="color:var(--color-prettylights-syntax-string)">"</span></span>)
    implementation(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>me.ahoo.govern:spring-cloud-starter-govern-discovery:<span style="color:var(--color-prettylights-syntax-entity)">$&#123;governVersion&#125;</span><span style="color:var(--color-prettylights-syntax-string)">"</span></span>)</pre> 
 </div> 
</div> 
<h3 style="text-align:left">Maven</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><strong><span style="color:#6a737d"><?xml version="1.0" encoding="UTF-8"?></span></strong>

<span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">project</span></span></span><span style="color:#333333"> </span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1">xmlns</span>=</span></span><span style="background-color:transparent; color:#00aadd"><span style="color:#333333"><span style="color:#032f62">"http://maven.apache.org/POM/4.0.0"</span></span></span><span style="color:#333333">
         </span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1">xmlns:xsi</span>=</span></span><span style="background-color:transparent; color:#00aadd"><span style="color:#333333"><span style="color:#032f62">"http://www.w3.org/2001/XMLSchema-instance"</span></span></span><span style="color:#333333">
         </span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1">xsi:schemaLocation</span>=</span></span><span style="background-color:transparent; color:#00aadd"><span style="color:#333333"><span style="color:#032f62">"http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"</span></span></span><span style="color:#ffcc55"><span style="color:#333333">></span></span>

  <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">modelVersion</span>></span></span>4.0.0<span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">modelVersion</span>></span></span>
  <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span></span>demo<span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span></span>
  <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">properties</span>></span></span>
    <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">govern.version</span>></span></span>0.9.19<span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">govern.version</span>></span></span>
  <span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">properties</span>></span></span>

  <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">dependencies</span>></span></span>
    <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">groupId</span>></span></span>me.ahoo.govern<span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">groupId</span>></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span></span>spring-cloud-starter-govern-config<span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">version</span>></span></span>$&#123;govern.version&#125;<span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">version</span>></span></span>
    <span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></span>
    <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">groupId</span>></span></span>me.ahoo.govern<span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">groupId</span>></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span></span>spring-cloud-starter-govern-discovery<span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span></span>
      <span style="color:#ffcc55"><span style="color:#333333"><<span style="color:#22863a">version</span>></span></span>$&#123;govern.version&#125;<span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">version</span>></span></span>
    <span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></span>
  <span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">dependencies</span>></span></span>

<span style="color:#ffcc55"><span style="color:#333333"></<span style="color:#22863a">project</span>></span></span></pre> 
 </div> 
</div> 
<h3 style="text-align:left">bootstrap.yml (Spring-Cloud-Config)</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080"><span style="color:#6f42c1">spring</span></span><span style="color:#6f42c1">:</span>
  <span style="color:#008080"><span style="color:#6f42c1">application</span></span><span style="color:#6f42c1">:</span>
    <span style="color:#008080"><span style="color:#6f42c1">name</span></span><span style="color:#6f42c1">:</span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62">$&#123;service.name:govern-rest-api&#125;</span></span>
  <span style="color:#008080"><span style="color:#6f42c1">cloud</span></span><span style="color:#6f42c1">:</span>
    <span style="color:#008080"><span style="color:#6f42c1">govern</span></span><span style="color:#6f42c1">:</span>
      <span style="color:#008080"><span style="color:#6f42c1">namespace</span></span><span style="color:#6f42c1">:</span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62">$&#123;govern.namespace:govern-&#123;system&#125;&#125;</span></span>
      <span style="color:#008080"><span style="color:#6f42c1">config</span></span><span style="color:#6f42c1">:</span>
        <span style="color:#008080"><span style="color:#6f42c1">config-id</span></span><span style="color:#6f42c1">:</span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62">$&#123;spring.application.name&#125;.yaml</span></span>
      <span style="color:#008080"><span style="color:#6f42c1">redis</span></span><span style="color:#6f42c1">:</span>
        <span style="color:#008080"><span style="color:#6f42c1">mode</span></span><span style="color:#6f42c1">:</span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62">$&#123;govern.mode:standalone&#125;</span></span>
        <span style="color:#008080"><span style="color:#6f42c1">url</span></span><span style="color:#6f42c1">:</span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62">$&#123;govern.redis.uri:redis://localhost:6379&#125;</span></span>
<span style="color:#008080"><span style="color:#6f42c1">logging</span></span><span style="color:#6f42c1">:</span>
  <span style="color:#008080"><span style="color:#6f42c1">file</span></span><span style="color:#6f42c1">:</span>
    <span style="color:#008080"><span style="color:#6f42c1">name</span></span><span style="color:#6f42c1">:</span> <span style="background-color:transparent; color:#00aadd"><span style="color:#032f62">logs/$&#123;spring.application.name&#125;.log</span></span>
</pre> 
 </div> 
</div> 
<h2 style="text-align:left">REST-API Server (<code>Optional</code>)</h2> 
<h3 style="text-align:left">安装 REST-API Server</h3> 
<h4 style="text-align:left">方式一：下载可执行文件</h4> 
<blockquote> 
 <p>下载 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2Fgovern-service%2Freleases%2Fdownload%2F0.9.19%2Fgovern-rest-api-0.9.19.tar" target="_blank">rest-api-server</a></p> 
</blockquote> 
<blockquote> 
 <p>解压 <em>rest-api-0.9.19.tar</em></p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#0086b3"><span style="color:#6f42c1">cd</span> </span><span style="color:#032f62">rest-api-0.9.19</span>
<em><span style="color:#6a737d"># 工作目录: rest-api-0.9.19</span></em>
<span style="color:#6a737d">bin/rest-api</span> <span style="color:#ffcc55"><span style="color:#032f62">--server</span></span><span style="color:#032f62">.port=8080 </span><span style="color:#ffcc55"><span style="color:#032f62">--govern</span></span><span style="color:#032f62">.redis.uri=redis://localhost:6379</span></pre> 
 </div> 
</div> 
<h4 style="text-align:left">方式二：在 Docker 中运行</h4> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#6f42c1">docker</span> <span style="color:#032f62">pull ahoowang/govern-service:0.9.19</span>
<span style="color:#6f42c1">docker</span> <span style="color:#032f62">run </span><span style="color:#ffcc55"><span style="color:#032f62">--name</span></span><span style="color:#032f62"> govern-service </span><span style="color:#ffcc55"><span style="color:#032f62">-d</span></span><span style="color:#032f62"> </span><span style="color:#ffcc55"><span style="color:#032f62">-p</span></span><span style="color:#032f62"> 8080:8080 </span><span style="color:#ffcc55"><span style="color:#032f62">--link</span></span><span style="color:#032f62"> redis </span><span style="color:#ffcc55"><span style="color:#032f62">-e</span></span><span style="color:#032f62"> </span><span style="color:#ffaa44"><span style="color:#032f62">GOVERN_REDIS_URI</span></span><span style="color:#032f62">=redis://redis:6379  ahoowang/govern-service:0.9.19</span></pre> 
 </div> 
</div> 
<hr> 
<blockquote> 
 <p>MacBook Pro (M1)</p> 
 <p>请使用 <em>ahoowang/govern-service:0.9.19-armv7</em></p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#6f42c1">docker</span> <span style="color:#032f62">pull ahoowang/govern-service:0.9.19-armv7</span>
<span style="color:#6f42c1">docker</span> <span style="color:#032f62">run </span><span style="color:#ffcc55"><span style="color:#032f62">--name</span></span><span style="color:#032f62"> govern-service </span><span style="color:#ffcc55"><span style="color:#032f62">-d</span></span><span style="color:#032f62"> </span><span style="color:#ffcc55"><span style="color:#032f62">-p</span></span><span style="color:#032f62"> 8080:8080 </span><span style="color:#ffcc55"><span style="color:#032f62">--link</span></span><span style="color:#032f62"> redis </span><span style="color:#ffcc55"><span style="color:#032f62">-e</span></span><span style="color:#032f62"> </span><span style="color:#ffaa44"><span style="color:#032f62">GOVERN_REDIS_URI</span></span><span style="color:#032f62">=redis://redis:6379  ahoowang/govern-service:0.9.19-armv7</span>
</pre> 
 </div> 
</div> 
<h4 style="text-align:left">方式三：在 Kubernetes 中运行</h4> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">apiVersion</span>: <span style="background-color:transparent; color:#00aadd">apps/v1</span>
<span style="color:#008080">kind</span>: <span style="background-color:transparent; color:#00aadd">Deployment</span>
<span style="color:#008080">metadata</span>:
  <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">govern-service-rest-api</span>
<span style="color:#008080">spec</span>:
  <span style="color:#008080">replicas</span>: <strong>1</strong>
  <span style="color:#008080">selector</span>:
    <span style="color:#008080">matchLabels</span>:
      <span style="color:#008080">app</span>: <span style="background-color:transparent; color:#00aadd">govern-service-rest-api</span>
  <span style="color:#008080">template</span>:
    <span style="color:#008080">metadata</span>:
      <span style="color:#008080">labels</span>:
        <span style="color:#008080">app</span>: <span style="background-color:transparent; color:#00aadd">govern-service-rest-api</span>
    <span style="color:#008080">spec</span>:
      <span style="color:#008080">containers</span>:
        - <span style="color:#008080">env</span>:
            - <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">GOVERN_REDIS_MODE</span>
              <span style="color:#008080">value</span>: <span style="background-color:transparent; color:#00aadd">standalone</span>
            - <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">GOVERN_REDIS_URI</span>
              <span style="color:#008080">value</span>: <span style="background-color:transparent; color:#00aadd">redis://redis-uri:6379</span>
          <span style="color:#008080">image</span>: <span style="background-color:transparent; color:#00aadd">ahoowang/govern-service:0.9.19</span>
          <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">govern-service</span>
          <span style="color:#008080">resources</span>:
            <span style="color:#008080">limits</span>:
              <span style="color:#008080">cpu</span>: <span style="color:orange">"</span><span style="background-color:transparent; color:#00aadd">1"</span>
              <span style="color:#008080">memory</span>: <span style="background-color:transparent; color:#00aadd">640Mi</span>
            <span style="color:#008080">requests</span>:
              <span style="color:#008080">cpu</span>: <span style="background-color:transparent; color:#00aadd">250m</span>
              <span style="color:#008080">memory</span>: <span style="background-color:transparent; color:#00aadd">512Mi</span>
          <span style="color:#008080">volumeMounts</span>:
            - <span style="color:#008080">mountPath</span>: <span style="background-color:transparent; color:#00aadd">/etc/localtime</span>
              <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">volume-localtime</span>
      <span style="color:#008080">volumes</span>:
        - <span style="color:#008080">hostPath</span>:
            <span style="color:#008080">path</span>: <span style="background-color:transparent; color:#00aadd">/etc/localtime</span>
            <span style="color:#008080">type</span>: <span style="color:orange">"</span><span style="background-color:transparent; color:#00aadd">"</span>
          <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">volume-localtime</span></pre> 
  <p> </p> 
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
<p style="text-align:left">Namespace</p> 
<p style="text-align:left"><img alt="rest-api-namespace" src="https://gitee.com/AhooWang/govern-service/raw/main/docs/rest-api-namespace.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong>Config</strong></p> 
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
  <pre><span style="color:#6f42c1">gradle</span> <span style="color:#032f62">config:jmh</span></pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#6a737d"># JMH version: 1.29</span>
<span style="color:#6a737d"># VM version: JDK 11.0.11, OpenJDK 64-Bit Server VM, 11.0.11+9-LTS</span>
<span style="color:#6a737d"># VM invoker: /Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home/bin/java</span>
<span style="color:#6a737d"># VM options: -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/Users/ahoo/govern-service/config/build/tmp/jmh -Duser.country=CN -Duser.language=zh -Duser.variant</span>
<span style="color:#6a737d"># Blackhole mode: full + dont-inline hint</span>
<span style="color:#6a737d"># Warmup: 1 iterations, 10 s each</span>
<span style="color:#6a737d"># Measurement: 1 iterations, 10 s each</span>
<span style="color:#6a737d"># Timeout: 10 min per iteration</span>
<span style="color:#6a737d"># Threads: 50 threads, will synchronize iterations</span>
<span style="color:#6a737d"># Benchmark mode: Throughput, ops/time</span>

<span style="color:#032f62">Benchmark</span>                                          <span style="color:#032f62">Mode</span>  <span style="color:#032f62">Cnt</span>          <span style="color:#032f62">Score</span>   <span style="color:#032f62">Error</span>  <span style="color:#032f62">Units</span>
<span style="color:#032f62">ConsistencyRedisConfigServiceBenchmark.getConfig</span>  <span style="color:#032f62">thrpt</span>       265321650.148          <span style="color:#032f62">ops/s</span>
<span style="color:#032f62">RedisConfigServiceBenchmark.getConfig</span>             <span style="color:#032f62">thrpt</span>          106991.476          <span style="color:#032f62">ops/s</span>
<span style="color:#032f62">RedisConfigServiceBenchmark.setConfig</span>             <span style="color:#032f62">thrpt</span>          103659.132          <span style="color:#032f62">ops/s</span></pre> 
 </div> 
</div> 
<h3 style="text-align:left">ServiceDiscovery</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#6f42c1">gradle</span> <span style="color:#032f62">discovery:jmh</span></pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#6a737d"># JMH version: 1.29</span>
<span style="color:#6a737d"># VM version: JDK 11.0.11, OpenJDK 64-Bit Server VM, 11.0.11+9-LTS</span>
<span style="color:#6a737d"># VM invoker: /Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home/bin/java</span>
<span style="color:#6a737d"># VM options: -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/Users/ahoo/govern-service/discovery/build/tmp/jmh -Duser.country=CN -Duser.language=zh -Duser.variant</span>
<span style="color:#6a737d"># Blackhole mode: full + dont-inline hint</span>
<span style="color:#6a737d"># Warmup: 1 iterations, 10 s each</span>
<span style="color:#6a737d"># Measurement: 1 iterations, 10 s each</span>
<span style="color:#6a737d"># Timeout: 10 min per iteration</span>
<span style="color:#6a737d"># Threads: 50 threads, will synchronize iterations</span>
<span style="color:#6a737d"># Benchmark mode: Throughput, ops/time</span>

<span style="color:#032f62">Benchmark</span>                                                <span style="color:#032f62">Mode</span>  <span style="color:#032f62">Cnt</span>          <span style="color:#032f62">Score</span>   <span style="color:#032f62">Error</span>  <span style="color:#032f62">Units</span>
<span style="color:#032f62">ConsistencyRedisServiceDiscoveryBenchmark.getInstances</span>  <span style="color:#032f62">thrpt</span>        76894658.867          <span style="color:#032f62">ops/s</span>
<span style="color:#032f62">ConsistencyRedisServiceDiscoveryBenchmark.getServices</span>   <span style="color:#032f62">thrpt</span>       466036317.472          <span style="color:#032f62">ops/s</span>
<span style="color:#032f62">RedisServiceDiscoveryBenchmark.getInstances</span>             <span style="color:#032f62">thrpt</span>          107778.244          <span style="color:#032f62">ops/s</span>
<span style="color:#032f62">RedisServiceDiscoveryBenchmark.getServices</span>              <span style="color:#032f62">thrpt</span>          106920.412          <span style="color:#032f62">ops/s</span>
<span style="color:#032f62">RedisServiceRegistryBenchmark.deregister</span>                <span style="color:#032f62">thrpt</span>          114094.513          <span style="color:#032f62">ops/s</span>
<span style="color:#032f62">RedisServiceRegistryBenchmark.register</span>                  <span style="color:#032f62">thrpt</span>          109085.694          <span style="color:#032f62">ops/s</span>
<span style="color:#032f62">RedisServiceRegistryBenchmark.renew</span>                     <span style="color:#032f62">thrpt</span>          127003.104          <span style="color:#032f62">ops/s</span></pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            