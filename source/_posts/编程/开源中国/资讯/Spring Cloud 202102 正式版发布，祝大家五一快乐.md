
---
title: 'Spring Cloud 2021.0.2 正式版发布，祝大家五一快乐'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6914'
author: 开源中国
comments: false
date: Fri, 29 Apr 2022 15:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6914'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">一、发布说明</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcloud.spring.io%2F" target="_blank">Spring Cloud 2021.0</a> Release Train 的 Service Release 2 现已推出。这主要是一个错误修复版本。该版本可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Forg%2Fspringframework%2Fcloud%2Fspring-cloud-dependencies%2F2021.0.2%2F" target="_blank">Maven Central</a>中找到。您可以查看 2021.0.2<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-release%2Fwiki%2FSpring-Cloud-2021.0-Release-Notes%23202102" target="_blank">发行说明以获取更多信息</a>。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">二、更新内容</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.1 <span style="color:#191e1e"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Spring Cloud Commons</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li>在阻塞 LoadBalancer 客户端中传递请求数据上下文 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fissues%2F1090" target="_blank">1090</a> )</li> 
 <li>支持 LoadBalancer 生命周期中的自定义 HTTP 状态码 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fissues%2F1066" target="_blank">1066</a> )</li> 
 <li>默认支持不带端口的URI <code>ServiceInstance</code>（[1054] <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fpull%2F1054%29" target="_blank">https://github.com/spring-cloud/spring-cloud-commons/pull/1054</a>）</li> 
 <li>改进了计算循环负载平衡器位置 ([1078 ] <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fpull%2F1078%29%2Ffiles" target="_blank">https://github.com/spring-cloud/spring-cloud-commons/pull/1078)/files</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.2 Spring Cloud Sleuth</h3> 
<ul> 
 <li>修复文档中指向 Sleuth 样本的链接 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F2148" target="_blank">2148</a> )</li> 
 <li>重新定位 SleuthSpanContextSupplier ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fpull%2F2147" target="_blank">2147</a> )</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F2132" target="_blank">Reactor Netty ( 2132</a> )的文档访问日志</li> 
 <li>修复 Zipkin WebClientSender 的 Content-Type ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F2139" target="_blank">2139</a> , <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F2126" target="_blank">2126</a> )</li> 
 <li>修复 RSocket 的 Netty LEAK 报告 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F2102" target="_blank">2102</a> )</li> 
 <li>停止包装 AbstractPlatformTransactionManager 实现 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F2114" target="_blank">2114</a> )</li> 
 <li>在创建 SkipPatternProvider ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F2136" target="_blank">2136</a> )时发生 BeanCreationException 时添加日志消息</li> 
 <li>Prometheus 示例的自动配置 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fpull%2F2143" target="_blank">2143</a> )</li> 
 <li>修复 Rabbit、Kafka 和 Zipkin 的自动配置顺序 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F2134" target="_blank">2134</a> )</li> 
 <li>修复使用 WebClient 的线程无效阻塞 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F2127" target="_blank">2127</a> )</li> 
 <li>修复无效的 ThreadLocalSpan 堆栈和跟踪上下文泄漏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F2064" target="_blank">2064</a> )</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.3 Spring Cloud Contract</h3> 
<h3 style="margin-left:0; margin-right:0; text-align:left"> </h3> 
<ul> 
 <li>Bumped WireMock to 2.33.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-contract%2Fissues%2F1771" target="_blank">1771</a>)</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.4 Spring Cloud OpenFeign</h3> 
<ul> 
 <li>为 CircuitBreaker id 提供和替代命名约定（[687] <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-openfeign%2Fpull%2F687%29" target="_blank">https://github.com/spring-cloud/spring-cloud-openfeign/pull/687）</a>）</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.5 Spring Cloud Netflix</h3> 
<ul> 
 <li>减少由<code>EurekaRenewedEvent</code>([4052] <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-netflix%2Fpull%2F4052%29" target="_blank">https://github.com/spring-cloud/spring-cloud-netflix/pull/4052)</a>引起的高负载</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.6 Spring Cloud CircuitBreaker</h3> 
<ul> 
 <li>允许配置默认舱壁策略 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-circuitbreaker%2Fissues%2F119" target="_blank">119</a> )</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.7 Spring Cloud Kubernetes</h3> 
<ul> 
 <li>更新到 Fabric8 5.10.2</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.8 2021.0.2版本相关依赖更新内容如下：</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; border-collapse:collapse; border-spacing:0px; color:#191e1e; font-family:"Open Sans",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; orphans:2; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>模块</th> 
   <th>版本</th> 
   <th>Issues</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ffffff">Spring Cloud Config</td> 
   <td style="border-top:1px solid #ffffff">3.1.2</td> 
   <td style="border-top:1px solid #ffffff">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-config%2Fmilestone%2F99%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Circuitbreaker</td> 
   <td style="border-top:1px solid #ebf2f2">2.1.2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-circuitbreaker%2Fmilestone%2F14%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Kubernetes</td> 
   <td style="border-top:1px solid #ebf2f2">2.1.2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-kubernetes%2Fmilestone%2F43%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Commons</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fmilestone%2F100%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Sleuth</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fmilestone%2F100%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Contract</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-contract%2Fmilestone%2F86%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Task</td> 
   <td style="border-top:1px solid #ebf2f2">2.4.2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-task%2Fmilestone%2F59" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Gateway</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-gateway%2Fmilestone%2F65%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud OpenFeign</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-openfeign%2Fmilestone%2F50%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Starter Build</td> 
   <td style="border-top:1px solid #ebf2f2">2021.0.2</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Netflix</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-netflix%2Fmilestone%2F109%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Function</td> 
   <td style="border-top:1px solid #ebf2f2">3.2.4</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Stream</td> 
   <td style="border-top:1px solid #ebf2f2">3.2.3</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">三、项目引入</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">3.1 <span style="color:#191e1e"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>maven方式引入</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<pre><code class="language-xml"><dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>2021.0.2</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-config</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
    </dependency>
    ...
</dependencies></code></pre> 
<h3 style="margin-left:0; margin-right:0; text-align:left">3.2 Gradle引入</h3> 
<pre><code class="language-xml">plugins &#123;
  id 'org.springframework.boot' version '2.6.7'
  id 'io.spring.dependency-management' version '1.0.11.RELEASE'
  id 'java'
&#125;

repositories &#123;
  mavenCentral()
&#125;

ext &#123;
  set('springCloudVersion', "2021.0.2")
&#125;

dependencies &#123;
  implementation 'org.springframework.cloud:spring-cloud-starter-config'
  implementation 'org.springframework.cloud:spring-cloud-starter-netflix-eureka-client'
  //...
&#125;

dependencyManagement &#123;
  imports &#123;
    mavenBom "org.springframework.cloud:spring-cloud-dependencies:$&#123;springCloudVersion&#125;"
  &#125;
&#125;</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">三、项目案例</h2> 
<p>基于Spring Cloud 2021.0.2的项目样例：<a href="https://gitee.com/matevip/matecloud">https://gitee.com/matevip/matecloud</a></p>
                                        </div>
                                      
</div>
            