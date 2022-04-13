
---
title: 'Spring Native 0.11.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9266'
author: 开源中国
comments: false
date: Wed, 13 Apr 2022 07:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9266'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Spring Native 0.11.4 现已发布。<span style="color:#252525">Spring Native（前身为 Spring GraalVM Native，Spring 社区试验性项目）通过使用 GraalVM 原生镜像编译器将 Spring 应用程序编译为独立的系统原生可执行文件（无需安装 JVM），提供了一种在轻量级容器中原生部署 Spring 应用程序的新方法，支持 Java 和 Kotlin，并提供有趣的特性，包括几乎即时启动（通常<100ms），即时峰值性能和较低的内存消耗，但所需的构建时间和运行时优化次数少于 JVM。目标是在此新平台上几乎不做修改就能支持 Spring Boot 应用程序。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#252525">具体更新内容如下：</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>兼容性</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><span style="color:#252525">支持 native tests 的应用程序类的 native hints</span></li> 
 <li><span style="color:#252525">Native-tests 在 GraalVM 22.1 中被破坏</span></li> 
 <li><span style="color:#252525">webmvc-kotlin 在 GraalVM 22.1 中 fail</span></li> 
 <li><span style="color:#252525">webflux-kotlin 在 GraalVM 22.1 中 fail</span></li> 
 <li><span style="color:#252525">session-redis-webflux 在 GraalVM 22.1 中 fail</span></li> 
 <li><span style="color:#252525">events 在 GraalVM 22.1 中 fail</span></li> 
 <li><span style="color:#252525">data-r2dbc-kotlin 在 GraalVM 22.1 中 fail</span></li> 
 <li><span style="color:#252525">commandlinerunner-log4j2 在 GraalVM 22.1 中 fail</span></li> 
 <li><span style="color:#252525">cloud-function-netty 在 GraalVM 22.1 中 fail</span></li> 
 <li><span style="color:#252525">grpc sample 在 GraalVM 22.1 中 fail</span></li> 
 <li><span style="color:#252525">GraalVM for Apple Silicon：management.metrics.distribution 错误</span></li> 
 <li><span style="color:#252525">添加 Jackson PropertyNamingStrategies 的提示</span></li> 
 <li><span style="color:#252525">Spring Native 0.11.3 + 最新的 Spring Data JPA 和 Sleuth Zipkin 在 Bootstrap 期间出现故障</span></li> 
 <li><span style="color:#252525">Spring Security - AuthenticationFailureBadCredentialsEvent 没有合适的构造函数</span></li> 
 <li><span style="color:#252525">Spring 安全方法缺少提示</span></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>Spring Aot Maven 插件在 Maven Compiler Plugin > 3.8.1 时无法工作</li> 
 <li>在 IntelliJ 中重新加载 Gradle 项目会导致生成的 AOT 源被删除</li> 
 <li>模糊检查仅适用于构造函数</li> 
 <li>如果参数值具有未解析的泛型，则无法检测到工厂方法的可执行文件</li> 
 <li>Record 上的 @ConfigurationProperties 与 @Validated - 即使在 0.11.3 中，本机构建仍然失败</li> 
 <li>ASM visitors 应该使用 SpringAsmInfo.ASM_VERSION 而不是硬编码的 ASM 版本</li> 
 <li>com.ecwid.consul.v1.kv.model.GetValue 类被反射实例化但从未注册</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>文档</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>删除程序化的 Logback 配置文档</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>依赖升级</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>升级到 Native Build Tools 0.9.11</li> 
 <li>升级到 Spring Boot 2.6.6</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Freleases%2Ftag%2F0.11.4" target="_blank">https://github.com/spring-projects-experimental/spring-native/releases/tag/0.11.4</a></p>
                                        </div>
                                      
</div>
            