
---
title: 'SpringBoot 2.6.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://minio.pigx.vip/oss/1637199358.png'
author: 开源中国
comments: false
date: Fri, 19 Nov 2021 15:58:00 GMT
thumbnail: 'https://minio.pigx.vip/oss/1637199358.png'
---

<div>   
<div class="content">
                                                                                            <h1><span>新特性</span></h1> 
<h2><span>1. 支持配置 Cookie SameSite</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p>Strict 严格模式，必须同站请求才能发送 cookie</p> </li> 
 <li> <p>Lax 宽松模式，安全的跨站请求可以发送 cookie</p> </li> 
 <li> <p>None 禁止 SameSite 限制，必须配合 Secure 一起使用（浏览器最后的坚持）</p> </li> 
</ul> 
<p><img alt src="https://minio.pigx.vip/oss/1637199358.png" referrerpolicy="no-referrer"></p> 
<h2><span>2. Reactive Session 个性化</span></h2> 
<p style="color:#595959; margin-left:0; margin-right:0">当前版本可以动态配置 reactive session 的有效期</p> 
<pre><code>server.reactive.session.timeout=30
</code></pre> 
<h2><span>3. 支持自定义脱敏规则</span></h2> 
<p style="color:#595959; margin-left:0; margin-right:0">关于 SpringBoot 端点敏感数据脱敏，之前在文章 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMjM5MzEwODY4Mw%3D%3D%26mid%3D2257484664%26idx%3D1%26sn%3Dc86ceb6c1a947e85b1f699abe573c0a8%26chksm%3Da5e6dcdc929155cab89c974c4f847ec6559904ccbe01ea47f6e092e104844bfa4616dccd9076%26token%3D711727790%26lang%3Dzh_CN%23rd" target="_blank">Spring Boot 2.3 新特配置文件属性跟踪</a> ，简单讲是敏感的一些字段予以脱敏输出。</p> 
<p><img alt src="https://minio.pigx.vip/oss/1637199772.jpg" referrerpolicy="no-referrer"></p> 
<h2><span>4. Redis 链接自动配置链接池</span></h2> 
<p style="color:#595959; margin-left:0; margin-right:0">当应用依赖中包含 commons-pool2.jar 会自动配置 redis 链接池 （Jedis Lettuce 都支持）</p> 
<p style="color:#595959; margin-left:0; margin-right:0">如果你想关闭则通过如下属性</p> 
<pre><code>spring.redis.jedis.pool.enabled=<span style="color:#0184bb">false</span>

spring.redis.lettuce.pool.enabled=<span style="color:#0184bb">false</span>
</code></pre> 
<h2><span>5. 端点新增运行时 Java 信息</span></h2> 
<pre><code>management.info.java.enabled=<span style="color:#0184bb">true</span>
</code></pre> 
<ul style="list-style-type:disc"> 
 <li> <p>输出如下</p> </li> 
</ul> 
<pre><code>&#123;
  <span style="color:#50a14f">"java"</span>: &#123;
    <span style="color:#50a14f">"vendor"</span>: <span style="color:#50a14f">"BellSoft"</span>,
    <span style="color:#50a14f">"version"</span>: <span style="color:#50a14f">"17"</span>,
    <span style="color:#50a14f">"runtime"</span>: &#123;
      <span style="color:#50a14f">"name"</span>: <span style="color:#50a14f">"OpenJDK Runtime Environment"</span>,
      <span style="color:#50a14f">"version"</span>: <span style="color:#50a14f">"17+35-LTS"</span>
    &#125;,
    <span style="color:#50a14f">"jvm"</span>: &#123;
      <span style="color:#50a14f">"name"</span>: <span style="color:#50a14f">"OpenJDK 64-Bit Server VM"</span>,
      <span style="color:#50a14f">"vendor"</span>: <span style="color:#50a14f">"BellSoft"</span>,
      <span style="color:#50a14f">"version"</span>: <span style="color:#50a14f">"17+35-LTS"</span>
    &#125;
  &#125;
&#125;
</code></pre> 
<h2><span>6. 构建信息个性化</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p>通过 spring-boot-maven-plugin 支持自动生成此次构建信息的 <strong style="color:#47c1a8">build-info.properties</strong></p> </li> 
</ul> 
<pre><code>    <span><<span style="color:#e45649">plugin</span>></span>
      <span><<span style="color:#e45649">groupId</span>></span>org.springframework.boot<span></<span style="color:#e45649">groupId</span>></span>
      <span><<span style="color:#e45649">artifactId</span>></span>spring-boot-maven-plugin<span></<span style="color:#e45649">artifactId</span>></span>
      <span><<span style="color:#e45649">configuration</span>></span>
           <span><<span style="color:#e45649">excludeInfoProperties</span>></span>
            <span><<span style="color:#e45649">excludeInfoProperty</span>></span>version<span></<span style="color:#e45649">excludeInfoProperty</span>></span>
         <span></<span style="color:#e45649">excludeInfoProperties</span>></span>
      <span></<span style="color:#e45649">configuration</span>></span>
    <span></<span style="color:#e45649">plugin</span>></span>
</code></pre> 
<h2><span>7. 启动信息新增指标</span></h2> 
<pre><code>application.started.time: 启动应用程序所需的时间

application.ready.time:  启动应用到对外提供服务所需时间
</code></pre> 
<h2><span>8. 磁盘空间指标</span></h2> 
<pre><code>disk.free  磁盘空闲

disk.total  磁盘总空间
</code></pre> 
<h2><span>9. Docker 镜像构建</span></h2> 
<p style="color:#595959; margin-left:0; margin-right:0">之前版本有分享 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMjM5MzEwODY4Mw%3D%3D%26mid%3D2257485430%26idx%3D1%26sn%3Dbc6865168c787d69b041a3867fea6082%26chksm%3Da5e6d9d2929150c4aef67c6427b07a6768d5a9142dcb835c92e08e7f8b99ab781e3eee154444%26token%3D711727790%26lang%3Dzh_CN%23rd" target="_blank">「Spring Boot 2.4 新特性」一键构建 Docker 镜像</a>, Spring Boot 内置 docker-maven-plugin 插件就是为了帮助我们在 Maven 工程中，通过简单的配置，自动生成镜像并推送到仓库中。</p> 
<p style="color:#595959; margin-left:0; margin-right:0">spring boot 2.6 进行功能增强：</p> 
<ul style="list-style-type:disc"> 
 <li> <p>支持自定义镜像 TAG</p> </li> 
 <li> <p>网络配置</p> </li> 
 <li> <p>构建缓存配置</p> </li> 
</ul> 
<hr> 
<h1><span>重要变更</span></h1> 
<h2><span>1. 完全移除 2.4 版本中的过期属性</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p>Spring MVC 和 servlet 部分属性已被删除，</p> </li> 
</ul> 
<table style="display:table; text-align:left"> 
 <thead> 
  <tr> 
   <th style="background-color:#f0f0f0; text-align:left">旧属性（已删除）</th> 
   <th style="background-color:#f0f0f0; text-align:left">新属性</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">spring.web.locale</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">spring.mvc.locale</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">spring.web.locale-resolver</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">spring.mvc.locale-resolver</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">spring.web.resources.*</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">spring.resources.*</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">management.server.base-path</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">management.server.servlet.context-path</td> 
  </tr> 
 </tbody> 
</table> 
<ul style="list-style-type:disc"> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0">Logback 常量 LoggingSystemProperties 完全删除，取而代之的是 LogbackLoggingSystemProperties</p> </li> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0">ConfigFileApplicationListener 完全删除，使用 ConfigDataEnvironmentPostProcessor 替代</p> </li> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0">Undertow 容器的个性化参数 isEagerInitFilters/setEagerInitFilters 完全删除，已被 isEagerFilterInit/替换 setEagerFilterInit</p> </li> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0">SpringApplication.contextClass() 完全删除，使用 contextFactory() 代替</p> </li> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0">CloudFoundryVcapEnvironmentPostProcessor 的大部分方法被移除，所以 CloudFoundry PaaS <strong style="color:#47c1a8">初期慎用</strong></p> </li> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0">ApplicationEnvironmentPreparedEvent，ApplicationStartingEvent 的部分方法以及 SpringApplicationRunListener 已被删除以支持 BootstrapContext</p> </li> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0">Spring Data Cassandra 健康指标端点已被删除</p> </li> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0"><strong style="color:#47c1a8">点击查看: 详细的属性变更说明</strong>[1]</p> </li> 
</ul> 
<h2><span>默认情况完全禁止 bean 循环引用</span></h2> 
<p><img alt="1637197849" src="https://minio.pigx.vip/oss/1637197849.png" referrerpolicy="no-referrer"></p> 
<p>1637197849</p> 
<pre><code>┌─────┐
|  a (field private com.example.demo.B com.example.demo.A.b)
↑     ↓
|  b (field private com.example.demo.A com.example.demo.B.a)
└─────┘


Action:

Relying upon circular references is discouraged and they are prohibited by default. Update your application to remove the dependency cycle between beans. As a last resort, it may be possible to <span style="color:#c18401">break</span> the cycle automatically by setting spring.main.allow-circular-references to <span style="color:#0184bb">true</span>.

</code></pre> 
<ul style="list-style-type:disc"> 
 <li> <p>如果对应 bean 循环引用的代码不好修改，可以通过如下配置允许使用</p> </li> 
</ul> 
<pre><code>spring.main.allow-circular-references=<span style="color:#0184bb">true</span>
</code></pre> 
<h2><span>2. SpringMVC 默认路径匹配策略</span></h2> 
<p style="color:#595959; margin-left:0; margin-right:0">Spring MVC 处理程序映射匹配请求路径的默认策略已从 AntPathMatcher 更改为<strong style="color:#47c1a8">PathPatternParser</strong>。</p> 
<ul style="list-style-type:disc"> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0">PathPattern 性能比 AntPathMatcher 好。理论上 pattern 越复杂，PathPattern 的优势越明显</p> </li> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0">如果需要将默认值切换回 AntPathMatcher，可设置如下属性</p> </li> 
</ul> 
<pre><code>spring.mvc.pathmatch.matching-strategy=ant-path-matcher
</code></pre> 
<h2><span>3. 默认禁用执行器环境信息</span></h2> 
<pre><code>management.info.env.enabled=<span style="color:#0184bb">true</span>
</code></pre> 
<h2><span>4. 应用启动信息记录变更</span></h2> 
<p style="color:#595959; margin-left:0; margin-right:0">记录到 SpringBoot 启动日志的 spring.boot.application.running 的属性，已重命名为 <code>spring.boot.application.read</code></p> 
<h3><span>参考资料</span></h3> 
<p><span><span>[1] </span>点击查看: 详细的属性变更说明: <em>https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.6.0-Configuration-Changelog</em></span></p>
                                        </div>
                                      
</div>
            