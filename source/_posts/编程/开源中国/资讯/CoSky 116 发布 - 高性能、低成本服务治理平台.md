
---
title: 'CoSky 1.1.6 发布 - 高性能、低成本服务治理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/AhooWang/CoSky/raw/main/docs/CoSky-Discovery.png'
author: 开源中国
comments: false
date: Fri, 11 Jun 2021 11:18:00 GMT
thumbnail: 'https://gitee.com/AhooWang/CoSky/raw/main/docs/CoSky-Discovery.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCoSky" target="_blank">CoSky</a> 基于 Redis 的服务治理平台（服务注册/发现 & 配置中心）</h1> 
<blockquote> 
 <p><strong>Co</strong>n<strong>s</strong>ul + S<strong>ky</strong> = <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCoSky" target="_blank">CoSky</a></strong></p> 
</blockquote> 
<p style="text-align:left"><em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCoSky" target="_blank">CoSky</a></em> 是一个轻量级、低成本的服务注册、服务发现、 配置服务 SDK，通过使用现有基础设施中的 Redis （相信你已经部署了Redis），不用给运维部署带来额外的成本与负担。 借助于 Redis 的高性能， <em>CoSky</em> 提供了超高TPS&QPS (10W+/s <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCoSky%23jmh-benchmark" target="_blank">JMH 基准测试</a>)。<em>CoSky</em> 结合本地进程缓存策略 + <em>Redis PubSub</em> ，实现实时进程缓存刷新，兼具无与伦比的QPS性能 (7000W+/s <a href="https://gitee.com/AhooWang/CoSky#jmh-benchmark">JMH 基准测试</a>)、进程缓存与 Redis 的实时一致性。</p> 
<h2 style="text-align:left">更新内容（1.1.6） 🎉 🎉 🎉</h2> 
<ol> 
 <li>增强：新增 CoskyReactiveDiscoveryClient 支持 ReactiveDiscoveryClient（Spring Cloud Commons）</li> 
 <li>优化：新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCoSky%2Ftree%2Fmain%2Fspring-cloud-starter-cosky-discovery-ribbon" target="_blank">spring-cloud-starter-cosky-discovery-ribbon</a> 支持旧版本 Spring-Cloud</li> 
</ol> 
<h3 style="text-align:left">服务注册与发现</h3> 
<p style="text-align:left"><img alt="CoSky-Discovery" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/CoSky-Discovery.png" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">配置中心</h3> 
<p style="text-align:left"><img alt="CoSky-Configuration" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/CoSky-Configuration.png" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">CoSky-Mirror （实时同步服务实例变更状态）</h3> 
<blockquote> 
 <p>CoSky-Mirror 就像一个镜子放在 Nacos、CoSky 中间，构建一个统一的服务发现平台。</p> 
</blockquote> 
<p style="text-align:left"><img alt="CoSky-Mirror" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/CoSky-Mirror.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt="CoSky-Mirror-Unified" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/CoSky-Mirror-Unified.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">Examples</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2FCoSky%2Ftree%2Fmain%2Fexamples" target="_blank">Service Consumer --RPC--> Service Provider Examples</a></p> 
<h2 style="text-align:left">安装</h2> 
<h3 style="text-align:left">Gradle</h3> 
<blockquote> 
 <p>Kotlin DSL</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>    <strong>val</strong> <strong>coskyVersion</strong> <span style="color:#eeeeee">=</span> <span style="background-color:transparent; color:#00aadd">"1.1.6"</span><span style="color:#eeeeee">;</span>
    <strong>implementation</strong><span style="color:#eeeeee">(</span><span style="background-color:transparent; color:#00aadd">"me.ahoo.cosky:spring-cloud-starter-cosky-config:$&#123;coskyVersion&#125;"</span><span style="color:#eeeeee">)</span>
    <strong>implementation</strong><span style="color:#eeeeee">(</span><span style="background-color:transparent; color:#00aadd">"me.ahoo.cosky:spring-cloud-starter-cosky-discovery:$&#123;coskyVersion&#125;"</span><span style="color:#eeeeee">)</span>
    <strong>implementation</strong><span style="color:#eeeeee">(</span><span style="background-color:transparent; color:#00aadd">"org.springframework.cloud:spring-cloud-starter-loadbalancer:3.0.3"</span><span style="color:#eeeeee">)</span></pre> 
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
    <span style="color:#ffcc55"><cosky.version></span>1.1.6<span style="color:#ffcc55"></cosky.version></span>
  <span style="color:#ffcc55"></properties></span>

  <span style="color:#ffcc55"><dependencies></span>
    <span style="color:#ffcc55"><dependency></span>
      <span style="color:#ffcc55"><groupId></span>me.ahoo.cosky<span style="color:#ffcc55"></groupId></span>
      <span style="color:#ffcc55"><artifactId></span>spring-cloud-starter-cosky-config<span style="color:#ffcc55"></artifactId></span>
      <span style="color:#ffcc55"><version></span>$&#123;cosky.version&#125;<span style="color:#ffcc55"></version></span>
    <span style="color:#ffcc55"></dependency></span>
    <span style="color:#ffcc55"><dependency></span>
      <span style="color:#ffcc55"><groupId></span>me.ahoo.cosky<span style="color:#ffcc55"></groupId></span>
      <span style="color:#ffcc55"><artifactId></span>spring-cloud-starter-cosky-discovery<span style="color:#ffcc55"></artifactId></span>
      <span style="color:#ffcc55"><version></span>$&#123;cosky.version&#125;<span style="color:#ffcc55"></version></span>
    <span style="color:#ffcc55"></dependency></span>
    <span style="color:#ffcc55"><dependency></span>
      <span style="color:#ffcc55"><groupId></span>org.springframework.cloud<span style="color:#ffcc55"></groupId></span>
      <span style="color:#ffcc55"><artifactId></span>spring-cloud-starter-loadbalancer<span style="color:#ffcc55"></artifactId></span>
      <span style="color:#ffcc55"><version></span>3.0.3<span style="color:#ffcc55"></version></span>
    <span style="color:#ffcc55"></dependency></span>
  <span style="color:#ffcc55"></dependencies></span>

<span style="color:#ffcc55"></project></span></pre> 
 </div> 
</div> 
<h3 style="text-align:left">bootstrap.yaml (Spring-Cloud-Config)</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">spring</span>:
  <span style="color:#008080">application</span>:
    <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">$&#123;service.name:cosky-rest-api&#125;</span>
  <span style="color:#008080">cloud</span>:
    <span style="color:#008080">cosky</span>:
      <span style="color:#008080">namespace</span>: <span style="background-color:transparent; color:#00aadd">$&#123;cosky.namespace:cosky-&#123;system&#125;&#125;</span>
      <span style="color:#008080">config</span>:
        <span style="color:#008080">config-id</span>: <span style="background-color:transparent; color:#00aadd">$&#123;spring.application.name&#125;.yaml</span>
      <span style="color:#008080">redis</span>:
        <span style="color:#008080">mode</span>: <span style="background-color:transparent; color:#00aadd">$&#123;cosky.redis.mode:standalone&#125;</span>
        <span style="color:#008080">url</span>: <span style="background-color:transparent; color:#00aadd">$&#123;cosky.redis.uri:redis://localhost:6379&#125;</span>
<span style="color:#008080">logging</span>:
  <span style="color:#008080">file</span>:
    <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">logs/$&#123;spring.application.name&#125;.log</span></pre> 
 </div> 
</div> 
<h2 style="text-align:left">REST-API Server (<code>Optional</code>)</h2> 
<h3 style="text-align:left">安装 REST-API Server</h3> 
<h4 style="text-align:left">方式一：下载可执行文件</h4> 
<blockquote> 
 <p>下载 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAhoo-Wang%2Fcosky%2Freleases%2Fdownload%2F1.1.6%2Fcosky-rest-api-1.1.6.tar" target="_blank">rest-api-server</a></p> 
</blockquote> 
<blockquote> 
 <p>解压 <em>cosky-rest-api-1.1.6.tar</em></p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#0086b3">cd </span>cosky-rest-api-1.1.6
<em># 工作目录: cosky-rest-api-1.1.6</em>
bin/cosky-rest-api <span style="color:#ffcc55">--server</span>.port=8080 <span style="color:#ffcc55">--cosky</span>.redis.uri=redis://localhost:6379</pre> 
 </div> 
</div> 
<h4 style="text-align:left">方式二：在 Docker 中运行</h4> 
<div style="text-align:left"> 
 <div> 
  <pre>docker pull ahoowang/cosky-rest-api:1.1.6
docker run <span style="color:#ffcc55">--name</span> cosky-rest-api <span style="color:#ffcc55">-d</span> <span style="color:#ffcc55">-p</span> 8080:8080 <span style="color:#ffcc55">--link</span> redis <span style="color:#ffcc55">-e</span> <span style="color:#ffaa44">COSKY_REDIS_URI</span>=redis://redis:6379  ahoowang/cosky-rest-api:1.1.6</pre> 
 </div> 
</div> 
<p>MacBook Pro (M1)</p> 
<blockquote> 
 <p>请使用 <em>ahoowang/cosky-rest-api:1.1.6-armv7</em></p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>docker pull ahoowang/cosky-rest-api:1.1.6-armv7
docker run <span style="color:#ffcc55">--name</span> cosky-rest-api <span style="color:#ffcc55">-d</span> <span style="color:#ffcc55">-p</span> 8080:8080 <span style="color:#ffcc55">--link</span> redis <span style="color:#ffcc55">-e</span> <span style="color:#ffaa44">COSKY_REDIS_URI</span>=redis://redis:6379  ahoowang/cosky-rest-api:1.1.6-armv7</pre> 
 </div> 
</div> 
<h4 style="text-align:left">方式三：在 Kubernetes 中运行</h4> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080">apiVersion</span>: <span style="background-color:transparent; color:#00aadd">apps/v1</span>
<span style="color:#008080">kind</span>: <span style="background-color:transparent; color:#00aadd">Deployment</span>
<span style="color:#008080">metadata</span>:
  <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">cosky-rest-api</span>
  <span style="color:#008080">labels</span>:
    <span style="color:#008080">app</span>: <span style="background-color:transparent; color:#00aadd">cosky-rest-api</span>
<span style="color:#008080">spec</span>:
  <span style="color:#008080">replicas</span>: <strong>1</strong>
  <span style="color:#008080">selector</span>:
    <span style="color:#008080">matchLabels</span>:
      <span style="color:#008080">app</span>: <span style="background-color:transparent; color:#00aadd">cosky-rest-api</span>
  <span style="color:#008080">template</span>:
    <span style="color:#008080">metadata</span>:
      <span style="color:#008080">labels</span>:
        <span style="color:#008080">app</span>: <span style="background-color:transparent; color:#00aadd">cosky-rest-api</span>
    <span style="color:#008080">spec</span>:
      <span style="color:#008080">containers</span>:
        - <span style="color:#008080">env</span>:
            - <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">COSKY_REDIS_MODE</span>
              <span style="color:#008080">value</span>: <span style="background-color:transparent; color:#00aadd">standalone</span>
            - <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">COSKY_REDIS_URI</span>
              <span style="color:#008080">value</span>: <span style="background-color:transparent; color:#00aadd">redis://redis-uri:6379</span>
          <span style="color:#008080">image</span>: <span style="background-color:transparent; color:#00aadd">ahoowang/cosky-rest-api:1.1.6</span>
          <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">cosky-rest-api</span>
          <span style="color:#008080">ports</span>:
            - <span style="color:#008080">containerPort</span>: <strong>8080</strong>
              <span style="color:#008080">protocol</span>: <span style="background-color:transparent; color:#00aadd">TCP</span>
          <span style="color:#008080">resources</span>:
            <span style="color:#008080">limits</span>:
              <span style="color:#008080">cpu</span>: <span style="color:orange">"</span><span style="background-color:transparent; color:#00aadd">1"</span>
              <span style="color:#008080">memory</span>: <span style="background-color:transparent; color:#00aadd">1280Mi</span>
            <span style="color:#008080">requests</span>:
              <span style="color:#008080">cpu</span>: <span style="background-color:transparent; color:#00aadd">250m</span>
              <span style="color:#008080">memory</span>: <span style="background-color:transparent; color:#00aadd">1024Mi</span>
          <span style="color:#008080">volumeMounts</span>:
            - <span style="color:#008080">mountPath</span>: <span style="background-color:transparent; color:#00aadd">/etc/localtime</span>
              <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">volume-localtime</span>
      <span style="color:#008080">volumes</span>:
        - <span style="color:#008080">hostPath</span>:
            <span style="color:#008080">path</span>: <span style="background-color:transparent; color:#00aadd">/etc/localtime</span>
            <span style="color:#008080">type</span>: <span style="color:orange">"</span><span style="background-color:transparent; color:#00aadd">"</span>
          <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">volume-localtime</span>

<strong>---</strong>
<span style="color:#008080">apiVersion</span>: <span style="background-color:transparent; color:#00aadd">v1</span>
<span style="color:#008080">kind</span>: <span style="background-color:transparent; color:#00aadd">Service</span>
<span style="color:#008080">metadata</span>:
  <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">cosky-rest-api</span>
  <span style="color:#008080">labels</span>:
    <span style="color:#008080">app</span>: <span style="background-color:transparent; color:#00aadd">cosky-rest-api</span>
<span style="color:#008080">spec</span>:
  <span style="color:#008080">selector</span>:
    <span style="color:#008080">app</span>: <span style="background-color:transparent; color:#00aadd">cosky-rest-api</span>
  <span style="color:#008080">ports</span>:
    - <span style="color:#008080">name</span>: <span style="background-color:transparent; color:#00aadd">rest</span>
      <span style="color:#008080">port</span>: <strong>80</strong>
      <span style="color:#008080">protocol</span>: <span style="background-color:transparent; color:#00aadd">TCP</span>
      <span style="color:#008080">targetPort</span>: <strong>8080</strong></pre> 
 </div> 
</div> 
<h3 style="text-align:left">Dashboard</h3> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Fdashboard" target="_blank">http://localhost:8080/dashboard</a></p> 
</blockquote> 
<p style="text-align:left"><img alt="dashboard-dashboard" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/dashboard-dashboard.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">命名空间管理</h4> 
<p style="text-align:left"><img alt="dashboard-namespace" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/dashboard-namespace.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">配置管理</h4> 
<p style="text-align:left"><img alt="dashboard-config" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/dashboard-config.png" referrerpolicy="no-referrer"></p> 
<p>编辑配置</p> 
<p style="text-align:left"><img alt="dashboard-config-edit" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/dashboard-config-edit.png" referrerpolicy="no-referrer"></p> 
<p>回滚配置</p> 
<p style="text-align:left"><img alt="dashboard-config-rollback" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/dashboard-config-rollback.png" referrerpolicy="no-referrer"></p> 
<p>从 Nacos 导入配置</p> 
<p style="text-align:left"><img alt="dashboard-config-import" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/dashboard-config-import.gif" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">服务管理</h4> 
<p style="text-align:left"><img alt="dashboard-service" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/dashboard-service.png" referrerpolicy="no-referrer"></p> 
<p>编辑服务实例信息</p> 
<p style="text-align:left"><img alt="dashboard-service-edit" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/dashboard-service-edit.png" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">REST-API</h3> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Fswagger-ui%2Findex.html%23%2F" target="_blank">http://localhost:8080/swagger-ui/index.html#/</a></p> 
</blockquote> 
<p>Namespace</p> 
<p style="text-align:left"><img alt="rest-api-namespace" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/rest-api-namespace.png" referrerpolicy="no-referrer"></p> 
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
<p>Config</p> 
<p style="text-align:left"><img alt="rest-api-config" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/rest-api-config.png" referrerpolicy="no-referrer"></p> 
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
<h4 style="text-align:left">Service</h4> 
<p style="text-align:left"><img alt="rest-api-service" src="https://gitee.com/AhooWang/CoSky/raw/main/docs/rest-api-service.png" referrerpolicy="no-referrer"></p> 
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
 <li>/v1/namespaces/&#123;namespace&#125;/services/&#123;serviceId&#125;/lb 
  <ul> 
   <li>GET</li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:left">JMH-Benchmark</h2> 
<ul> 
 <li>基准测试运行环境：笔记本开发机 ( MacBook Pro (M1) )</li> 
 <li>所有基准测试都在开发笔记本上执行。</li> 
 <li>Redis 部署环境也在该笔记本开发机上。</li> 
</ul> 
<h3 style="text-align:left">ConfigService</h3> 
<div style="text-align:left"> 
 <div> 
  <pre>gradle cosky-config:jmh
<em># or</em>
java <span style="color:#ffcc55">-jar</span> cosky-config/build/libs/cosky-config-1.1.6-jmh.jar <span style="color:#ffcc55">-bm</span> thrpt <span style="color:#ffcc55">-t</span> 25 <span style="color:#ffcc55">-wi</span> 1 <span style="color:#ffcc55">-rf</span> json <span style="color:#ffcc55">-f</span> 1</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre># JMH version: 1.29
# VM version: JDK 11.1.61, OpenJDK 64-Bit Server VM, 11.1.61+9-LTS
# VM invoker: /Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home/bin/java
# VM options: -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/Users/ahoo/cosky/config/build/tmp/jmh -Duser.country=CN -Duser.language=zh -Duser.variant
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
  <pre>gradle cosky-discovery:jmh
<em># or</em>
java <span style="color:#ffcc55">-jar</span> cosky-discovery/build/libs/cosky-discovery-1.1.6-jmh.jar <span style="color:#ffcc55">-bm</span> thrpt <span style="color:#ffcc55">-t</span> 25 <span style="color:#ffcc55">-wi</span> 1 <span style="color:#ffcc55">-rf</span> json <span style="color:#ffcc55">-f</span> 1</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre># JMH version: 1.29
# VM version: JDK 11.1.61, OpenJDK 64-Bit Server VM, 11.1.61+9-LTS
# VM invoker: /Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home/bin/java
# VM options: -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/Users/ahoo/cosky/discovery/build/tmp/jmh -Duser.country=CN -Duser.language=zh -Duser.variant
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
                                        </div>
                                      
</div>
            