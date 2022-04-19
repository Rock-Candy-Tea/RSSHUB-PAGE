
---
title: 'Apache ShenYu(incubating) 发布 2.4.3，异步高性能跨语言响应式 API 网关'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ea97dc74b6edfbaecd17eedcdb7632568b6.png'
author: 开源中国
comments: false
date: Tue, 19 Apr 2022 09:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ea97dc74b6edfbaecd17eedcdb7632568b6.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:black"><span>Apache ShenYu(incubating) </span><span>发布2.4.3</span></span></span></span></span></span></h1> 
<p style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span><span><span style="color:black">刘艺，肖宇 </span></span></span><span><span><span style="color:#576b95">Apache ShenYu</span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><strong><span><span style="background-color:#3e3e3e"><span><span style="color:white">Release Manager</span></span></span></span></strong></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><strong><span><span>刘艺 </span></span></strong><span><span> /  Apache ShenYu PPMC</span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><span><span>时隔3个月，Apache ShenYu再次发布2.4.3版本，本次版本内容，有200+的pull Request，30+的贡献者参与，新增了非常多的功能，修复了很多bug，以及优化了很多内容</span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><span><span style="background-color:#3e3e3e"><span><span style="color:white">Vol .1  </span></span></span></span><span><span style="background-color:#3e3e3e"><span><span style="color:white">新增功能</span></span></span></span></span></span></span></p> 
<ul> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">增加 Http 注册客户端的重试机制。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">支持 Content-Type 类型为 octet-stream。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">支持 Bootstrap 的URIs 的重定向。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">增加本地 API 授权。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">支持配置 Dubbo消费者线程池大小。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">支持 Divide 插件的失败重试机制。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">支持 Webscoket 的客户端配置。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">支持 MemoryLimitedLinkedBlockingQueue。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">支持 Alibaba Dubbo 插件共享线程池。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">支持 gRPC 插件共享线程池。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">增加 Metrics 插件。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">增加 Cache 插件。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">增加 Logging RocketMQ 插件。</span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><span><span style="background-color:#3e3e3e"><span><span style="color:white">Vol .2 </span></span></span></span><span><span style="background-color:#3e3e3e"><span><span style="color:white">优化项</span></span></span></span></span></span></span></p> 
<ul> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">更新 JUnit4 为 JUnit5。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">优化 password encryption。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">优化和校验 shenyu-admin 模块的接口参数。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">优化同步数据时，初始化数据的代码。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">增加 LoggingRocketMQ 插件的集成测试。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">在 ScheduledExecutorService 类中使用定时轮算法。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">重构admin 中注册 URI 的 buildHandle 方法。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">优化 Spring Cloud 客户端自动设置端口。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">重构 JWT 插件支持多等级 Tokens。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">优化网关netty参数自定义可配置</span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><span><span style="background-color:#3e3e3e"><span><span style="color:white">Vol .3 Fix Bug</span></span></span></span></span></span></span></p> 
<ul> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复 CommonUpstreamUtils 类初始化时的空指针异常。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复 Nacos 注册失败时进行判断。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复登录未注册用户时的空指针异常。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复重复打印启动日志的问题。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复重试次数，超时时间不生效的问题。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复 Token 解析报错的问题。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复 Websocket 传输大数据异常的问题。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复 NettyHttpClient 插件在失败时未重试的问题。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复 CVE-2021-41303 漏洞。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复判断所有插件包含条件不生效的问题。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复 Http Headers 丢失数据的问题。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复 Rewrite 插件不支持 URL 占位符的问题。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复 Nacos 同步数据异常的问题。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复当 ContextPath 插件打开时，Websocket 代理失败或者空指针异常的问题。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">修复 Http 注册客户端的端口占用检查。</span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><span><span style="background-color:#3e3e3e"><span><span style="color:white">Vol .4  </span></span></span></span><span><span style="background-color:#3e3e3e"><span><span style="color:white">移除项</span></span></span></span></span></span></span></p> 
<ul> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">移除 Monitor 插件。</span></span></span></span></span></span></span></li> 
 <li style="text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">移除 shenyu-agent 模块。</span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><span><span style="background-color:#3e3e3e"><span><span style="color:white">Vol .5  Metrics </span></span></span></span><span><span style="background-color:#3e3e3e"><span><span style="color:white">插件使用说明</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">Metrics </span></span></span></span><span><span style="background-color:white"><span><span style="color:black">插件 插件是网关用来监控自身运行状态（JVM 相关），请求的响应迟延，QPS、TPS等相关 metrics。</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span><span><span><span><span style="background-color:white"><span><span style="color:black">插件的使用</span></span></span></span></span></span></span></strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在网关的 pom.xml 文件中添加 metrics 的依赖。</p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0"><code><span><dependency></span></code><code><span>    <groupId>org.apache.shenyugroupId></span></code><code><span>    <artifactId>shenyu-spring-boot-starter-plugin-metricsartifactId></span></code><code><span>    <version>$&#123;project.version&#125;version></span></code><code><span><dependency></span></code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在网关的配置 yaml 文件中编辑如下内容</p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0"><code><span>shenyu:</span></code><code><span>  metrics:</span></code><code><span>    enabled: <span style="color:#0e9ce5">false</span>  #设置为 <span style="color:#0e9ce5">true</span> 表示开启</span></code><code><span>    name : prometheus </span></code><code><span>    host: <span style="color:#0e9ce5">127.0</span><span style="color:#0e9ce5">.0</span><span style="color:#0e9ce5">.1</span> #暴露的ip</span></code><code><span>    port: <span style="color:#0e9ce5">8090</span> #暴露的端口</span></code><code><span>    jmxConfig: <span style="color:#afafaf">#jmx配置</span></span></code><code><span>    props:</span></code><code><span>      jvm_enabled: <span style="color:#0e9ce5">true</span> #开启jvm的监控指标</span></code></pre> 
<p style="margin-left:0; margin-right:0">具体 Metrics 的指标信息可查看官网说明：https://shenyu.apache.org/zh/docs/plugin-center/observability/metrics-plugin</p> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><span><span style="background-color:#3e3e3e"><span><span style="color:white">Vol .5  Cache </span></span></span></span><span><span style="background-color:#3e3e3e"><span><span style="color:white">插件使用说明</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0">Cache 插件能够缓存目标服务的结果，还可以允许用户配置缓存结果失效时间</p> 
<p style="margin-left:0; margin-right:0">                                                                                                           <strong>插件的使用</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在网关的 pom.xml 文件中添加 Cache 的依赖。</p> </li> 
</ul> 
<pre style="margin-left:0px; margin-right:0px"><span><dependency>
    <groupId>org.apache.shenyu</groupId>
    <artifactId>shenyu-spring-boot-starter-plugin-cache</artifactId>
    <version>$&#123;project.version&#125;</version></span><code><span></dependency></span></code>
</pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">数据不会频繁更新，而且需要大量调用的场景。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">对于数据一致性要求不高的场景。</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><span><span style="background-color:#3e3e3e"><span><span style="color:white">Vol .5  Logging RocketMQ </span></span></span></span><span><span style="background-color:#3e3e3e"><span><span style="color:white">插件使用说明</span></span></span></span></span></span></span></p> 
<p style="margin-left:0px; margin-right:0px"><span><span><span><span><span style="background-color:white"><span><span style="color:black">Apache ShenYu </span></span></span></span><span><span style="background-color:white"><span><span style="color:black">网关接收客户端请求，向服务端转发请求，并将服务端结果返回给客户端.网关可以记录下每次请求对应的详细信息，  </span></span></span></span></span></span></span></p> 
<p style="margin-left:0px; margin-right:0px"><span><span><span><span><span style="background-color:white"><span><span style="color:black">列如：请求时间、请求参数、请求路径、响应结果、响应状态码、耗时、上游IP、异常信息等待.  </span></span></span></span></span></span></span></p> 
<p style="margin-left:0px; margin-right:0px"><span><span><span><span><span style="background-color:white"><span><span style="color:black">Logging-RocketMQ </span></span></span></span><span><span style="background-color:white"><span><span style="color:black">插件便是记录访问日志并将访问日志发送到 RocketMQ 集群的插件.</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span><span><span><span><span style="background-color:white"><span><span style="color:black">插件的使用</span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><span><span style="background-color:white"><span><span style="color:black">在网关的 pom.xml 文件中添加依赖。</span></span></span></span></span></span></span></p> 
<pre style="margin-left:0px; margin-right:0px"><span><dependency>
    <groupId>org.apache.shenyu</groupId>
    <artifactId>shenyu-spring-boot-starter-plugin-logging-rocketmq</artifactId>
    <version>$&#123;project.version&#125;</version></span><code><span></dependency></span></code>
</pre> 
<p style="margin-left:0px; margin-right:0px"><span><span><span> <span><span style="background-color:white"><span><span style="color:black">具体 配置以及各个参数的作用等信息可查看官网说明：https://shenyu.apache.org/zh/docs/plugin-center/observability/logging-rocketmq</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span><span><span><span><span>下个版本规划</span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"> </p> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span><span><span><span><span style="background-color:#3e3e3e"><span><span style="color:white">Features</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><span><span><strong><span><span style="background-color:white"><span><span style="color:#937a7a">新增集群方案</span></span></span></span></strong></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><span><span><span><span style="background-color:white"><span><span style="color:black">新增shenyu-proxy模块，支持ShenYu的集群模式，以及网关的动态扩缩容</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><span><span><span><span style="background-color:white"><span><span style="color:black">新增shenyu-nginx子项目，对接Nginx-upstream模块</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><span><span><strong><span><span style="background-color:white"><span><span style="color:#937a7a">新增多语言SDK</span></span></span></span></strong></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><span><span><span><span style="background-color:white"><span><span style="color:black">多语言的SDK主要是为了让其他类型的语言快速的接入shenyu网关</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><span><span><span><span style="background-color:white"><span><span style="color:black">https://github.com/apache/incubator-shenyu-client-donet</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><span><span><span><span style="background-color:white"><span><span style="color:black">https://github.com/apache/incubator-shenyu-client-golang</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><span><span><span><span style="background-color:white"><span><span style="color:black">https://github.com/apache/incubator-shenyu-client-python</span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><span><span><strong><span><span style="background-color:white"><span><span style="color:#937a7a">新增Helm的支持</span></span></span></span></strong></span></span></span></p> 
<p>                                 <img height="920" src="https://oscimg.oschina.net/oscnet/up-ea97dc74b6edfbaecd17eedcdb7632568b6.png" width="1166" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"> </p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><span><span><strong><span><span>加入我们</span></span></strong></span></span></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:center"><span><span><span><span><span><span style="color:black">  Apache ShenYu</span></span></span><span><span><span style="color:black">是一款多协议，插件化，高性能的API网关，于2021年5月加入Apache 孵化器</span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><span><span><strong><span><span><span style="color:#937a7a">如何贡献</span></span></span></strong></span></span></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:center"><span><span><span><span><span>https://shenyu.apache.org/zh/community/contributor-guide</span></span></span></span></span></p> 
<p>                            </p> 
<p style="margin-left:0; margin-right:0; text-align:justify"> </p>
                                        </div>
                                      
</div>
            