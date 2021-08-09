
---
title: 'Apache ShenYu(incubating) 2.4.0_ 让 API 网关更简单'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://shenyu.apache.org/img/architecture/shenyu-framework.png'
author: 开源中国
comments: false
date: Mon, 09 Aug 2021 02:57:00 GMT
thumbnail: 'https://shenyu.apache.org/img/architecture/shenyu-framework.png'
---

<div>   
<div class="content">
                                                                                            <h2><span style="color:inherit">Apache ShenYu(incubating) 2.4.0: 让 API 网关更简单</span></h2> 
<blockquote> 
 <p>声明:本文中的<code>Apache ShenYu</code> 都指的是 <code>Apache ShenYu (incubating)</code><br> 本人作者：肖宇 Apache ShenYu(incubating) Founder && PPMC<br> 2.4.0 Release Manager ： 张永伦 Apache ShenYu(incubating) PPMC && Apache ShardingSphere PMC</p> 
</blockquote> 
<p>所有的朋友们：</p> 
<p><code>Apache ShenYu</code>网关是原 <code>Dromara/soul</code> 网关捐献给<code>Apache</code>基金会后改名而来，<br> 此次发布的 <code>2.4.0</code> 版本是 <code>Apache ShenYu</code> 网关进入<code>Apache孵化器</code>后的首个版本。这个版本涉及很多新功能的增加，<br> 项目名称,包名以及<code>maven</code>依赖坐标的变更。</p> 
<h2><span style="color:inherit">Apache ShenYu 是什么？</span></h2> 
<p><code>Apache ShenYu</code>是使用<code>Java reactor</code>编程方式开发的，具有<code>异步</code>，<code>高性能</code>，<code>跨语言</code>等特性的 <code>API 网关</code>。<br> 在流量控制方面，有精美的Admin控制台，能够<code>精准</code>，<code>动态</code>控制流量，满足复杂的业务场景。<br> 在功能方面，它使用插件化的设计思想，支持许多常见的协议：如 <code>http/https</code>， <code>Dubbo</code>、 <code>Spring Cloud</code>、 <code>GRPC</code>、 <code>Motan</code>、<code>Sofa</code>、 <code>Tars</code> 等。<br> 同时内置十分丰富的功能插件，如 <code>熔断</code>，<code>限流</code>，<code>鉴权</code>，<code>黑白名单</code>，<code>防火墙</code>，<code>监控</code>，<code>参数更改</code>等等插件。其架构图如下:</p> 
<p><img alt src="https://shenyu.apache.org/img/architecture/shenyu-framework.png" referrerpolicy="no-referrer"></p> 
<h2><span style="color:inherit">流量控制</span></h2> 
<p>对流量的控制是网关的灵魂，针对流量控制，<code>Apache ShenYu</code> 设计了<code>选择器</code>，<code>规则</code> 2个概念，来控制流量。</p> 
<p><code>选择器</code>和 <code>规则</code>是 <code>Apache ShenYu</code> 网关中最<code>灵魂</code>的东西。掌握好它，你可以对任何流量进行管理。</p> 
<p>一个插件有多个选择器，一个选择器对应多种规则。选择器相当于是对流量的一级筛选，规则就是最终的筛选。</p> 
<p>对一个插件而言，我们希望根据我们的配置，达到满足条件的流量，插件才会被执行。</p> 
<p>选择器和规则就是为了让流量在满足特定的条件下，才去执行我们想要的，这种规则首先要明白。</p> 
<p>插件、选择器和规则执行逻辑如下，当流量进入到Apache ShenYu网关之后，会先判断是否有对应的插件，该插件是否开启；然后判断流量是否匹配该插件的选择器。</p> 
<p>然后再判断流量是否匹配该选择器的规则。如果请求流量能满足匹配条件才会执行该插件，否则插件不会被执行，处理下一个。</p> 
<p>Apache ShenYu网关就是这样通过层层筛选完成流量控制。其流程图如下 :</p> 
<p><img alt src="https://shenyu.apache.org/img/shenyu/plugin/plugin-chain-execute.png" referrerpolicy="no-referrer"></p> 
<h2><span style="color:inherit">流量筛选</span></h2> 
<p>流量筛选，是<code>选择器</code>和<code>规则</code>的<code>灵魂</code>，对应为选择器与规则里面的匹配条件(conditions)，根据不同的流量筛选规则，我们可以处理各种复杂的场景。</p> 
<p>流量筛选可以从<code>Header</code>, <code>URI</code>, <code>Query</code>, <code>Cookie</code> 等等Http请求获取数据，</p> 
<p>然后可以采用 <code>Match</code>，<code>=</code>，<code>SpEL</code>，<code>Regex</code>，<code>Groovy</code>等匹配方式，匹配出你所预想的数据。</p> 
<p>多组匹配添加可以使用<code>And/Or</code>的匹配策略。上述都是采用<code>SPI的设计思想</code>，用户可以<code>自主进行扩展</code> :更多的请查看 : https://shenyu.apache.org/zh/projects/shenyu/selector-and-rule/</p> 
<p>其过程图如下 :</p> 
<p><img alt src="https://shenyu.apache.org/img/shenyu/design/flow-condition.png" referrerpolicy="no-referrer"></p> 
<h2><span style="color:inherit">数据同步与缓存</span></h2> 
<p>为了提升网关的<code>性能</code>，<code>Apache ShenYu</code> 网关会将所有的流量控制规则缓存在<code>JVM</code> 内存里面。在<code>集群部署/分布式</code>场景中，<code>Apache ShenYu</code> 自主研发了一套 <code>将 Admin 控制台的数据，远程同步到每一个 Apache ShenYu 网关节点 JVM内存 的方案</code>。</p> 
<p>每一种方案，采用 <code>SPI</code> 设计思想，以供用户<code>灵活</code>的选择。目前支持的方案有 <code>HttpLongPull</code>, <code>Websocket</code>, <code>Zookeeper</code>, <code>Nacos</code>, <code>Consul</code>, <code>ETCD</code>。 其整体流程如下 :</p> 
<p><img alt src="https://shenyu.apache.org/img/shenyu/dataSync/config-strategy-processor-zh.png" referrerpolicy="no-referrer"></p> 
<h2><span style="color:inherit">Admin控制台</span></h2> 
<p>为了方便用户快速便捷的控制流量以及网关的所有功能特性，<code>Apache ShenYu</code> 提供了 一个十分精美的<code>Admin控制台</code>，用户可以<code>中英文切换</code>,在这上面，可以随意的<code>控制流量</code>，<code>启停插件</code>，<code>配置不同的参数与策略</code>，这些操作更改通过上述的<code>数据同步原理</code>，同步到网关的 <code>JVM内存</code>。其后台示意图如下:</p> 
<p><img alt src="https://shenyu.apache.org/img/community/admin.png" referrerpolicy="no-referrer"></p> 
<p>##### 菜单/数据权限</p> 
<p>网关的后台管理是十分重要的，为了针对企业级的用户，跨部门应用代理，<code>Apache ShenYu</code>设计了一整套的<code>权限控制体系</code>，它包含<code>按钮级别的菜单权限</code>，以及<code>行数据级别的数据权限</code>。并且这些权限控制在 <code>Admin控制台</code> 自主自动可配。</p> 
<p><img alt src="https://shenyu.apache.org/img/community/admin-permission.png" referrerpolicy="no-referrer"></p> 
<h2><span style="color:inherit">协议代理</span></h2> 
<p>协议代理是网关最核心的功能，目前 <code>Apache ShenYu</code> 支持 <code>http</code> 转成 <code>http/https</code>， <code>Websocket</code>,<code>Dubbo</code>、 <code>Spring Cloud</code>、 <code>GRPC</code>、 <code>Motan</code>、<code>Sofa</code>、 <code>Tars</code> 等协议的转换，未来将支持 <code>TCP</code>, <code>MQTT</code>,<code>MQTT</code> 等协议。</p> 
<p>#### Divide插件</p> 
<p><code>Divide</code>插件,是用来专门代理 <code>http/https/websocket</code> 等方式请求 <code>Apache ShenYu</code> 网关的插件。 它具有 <code>负载均衡</code>，<code>流量预热</code>, <code>节点发现</code>，<code>超时重试</code>，<code>超时控制</code> 等功能。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --><code>Divide插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/http-proxy/</p> 
<p><code>xml <dependency> <groupId>org.apache.shenyu</groupId> <artifactId>shenyu-spring-boot-starter-plugin-divide</artifactId> <version>$&#123;project.version&#125;</version> </dependency> <dependency> <groupId>org.apache.shenyu</groupId> <artifactId>shenyu-spring-boot-starter-plugin-httpclient</artifactId> <version>$&#123;project.version&#125;</version> </dependency> </code></p> 
<p>#### Dubbo插件</p> 
<p><code>Dubbo</code>插件，是<code>Apache ShenYu</code>网关将 <code>http/https</code> 请求转换成 <code>dubbo</code>协议的插件 。 它采用了<code>Dubbo泛化</code>调用的机制，整合了 <code>Dubbo的客户端</code>，具有<code>服务发现</code>，<code>负载均衡</code> 等功能。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>dubbo插件</code>将其设置为 <code>开启</code>,并且配置上<code>注册中心</code>, 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/dubbo-proxy/</p> 
<p><code>xml ¨K16K <dependency> <groupId>org.apache.shenyu</groupId> <artifactId>shenyu-spring-boot-starter-plugin-alibaba-dubbo</artifactId> <version>$&#123;project.version&#125;</version> </dependency> ¨K17K <dependency> <groupId>org.apache.shenyu</groupId> <artifactId>shenyu-spring-boot-starter-plugin-apache-dubbo</artifactId> <version>$&#123;project.version&#125;</version> </dependency> </code></p> 
<p>#### SpringCloud插件</p> 
<p><code>SpringCloud</code>插件，是<code>Apache ShenYu</code>网关代理 <code>SpringCloud</code>微服务业务的插件 。 它整合了 <code>SpringCloud</code>的注册中心，以及负载均衡服务，实现了服务的代理。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>SpringCloud插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/spring-cloud-proxy/</p> 
<p><code>xml <dependency> <groupId>org.apache.shenyu</groupId> <artifactId>shenyu-spring-boot-starter-plugin-springcloud</artifactId> <version>$&#123;project.version&#125;</version> </dependency> </code></p> 
<p>#### GRPC插件</p> 
<p><code>GRPC</code>插件，是<code>Apache ShenYu</code>网关将 <code>http/https</code> 请求转换成 <code>GRPC</code>协议的插件 。 它整合了 <code>GRPC</code> 客户端，实现了 <code>GRPC</code>服务的代理。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>GRPC插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 :https://shenyu.apache.org/zh/projects/shenyu/grpc-proxy/</p> 
<p><code>xml <dependency> <groupId>org.apache.shenyu</groupId> <artifactId>shenyu-spring-boot-starter-plugin-grpc</artifactId> <version>$&#123;project.version&#125;</version> </dependency> </code></p> 
<p>#### Tars插件</p> 
<p><code>Tars</code>插件，是<code>Apache ShenYu</code>网关将 <code>http/https</code> 请求转换成 <code>Tars</code>协议的插件 。 <code>Tars</code>是腾讯开源的 RPC框架， 该插件整合了 <code>Tars-JAVA</code> 客户端，实现了 <code>Tars</code>服务的代理。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>Tars插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/tars-proxy/</p> 
<p><code>xml <dependency> <groupId>org.apache.shenyu</groupId> <artifactId>shenyu-spring-boot-starter-plugin-tars</artifactId> <version>$&#123;project.version&#125;</version> </dependency> </code></p> 
<p>#### Sofa插件</p> 
<p><code>Sofa</code>插件，是<code>Apache ShenYu</code>网关将 <code>http/https</code> 请求转换成 <code>Sofa-RPC</code>协议的插件 。 它采用了<code>Sofa泛化</code>调用的机制，整合了 <code>Sofa-RPC的客户端</code>，具有<code>服务发现</code>，<code>负载均衡</code> 等功能。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>sofa插件</code>将其设置为 <code>开启</code>，并且配置上<code>注册中心</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/sofa-proxy/</p> 
<p><code>xml <dependency> <groupId>org.apache.shenyu</groupId> <artifactId>shenyu-spring-boot-starter-plugin-sofa</artifactId> <version>$&#123;project.version&#125;</version> </dependency> </code></p> 
<h2><span style="color:inherit">熔断限流</span></h2> 
<h4><span style="color:inherit">Hystrix 插件</span></h4> 
<p><code>Hystrix</code>插件，是<code>Apache ShenYu</code>网关整合<code>Hystrix</code>框架，提供请求熔断的功能，<code>Hystrix</code>熔断参数可动态化配置。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>Hystrix插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/hystrix-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-hystrix<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">Sentinel 插件</span></h4> 
<p><code>Sentinel</code>插件，是<code>Apache ShenYu</code>网关整合<code>Sentinel</code>框架，提供请求熔断限流的功能，<code>Sentinel</code>熔断限流参数可动态化配置。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>Sentinel插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/sentinel-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-sentinel<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">Resilience4j 插件</span></h4> 
<p><code>Resilience4j</code>插件，是<code>Apache ShenYu</code>网关整合<code>Resilience4j</code>框架，提供请求熔断限流的功能，<code>Resilience4j</code>熔断限流参数可动态化配置。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>Resilience4j插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/resilience4j-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-resilience4j<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">RateLimiter 插件</span></h4> 
<p><code>RateLimiter</code>插件，是<code>Apache ShenYu</code>网关使用<code>redis</code>，提供请求集群限流的功能，限流算法策略有：<code>令牌桶算法</code>,<code>并发限流</code>，<code>漏桶算法</code>，<code>滑动窗口算法</code>。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>RateLimiter插件</code>将其设置为 <code>开启</code>，并且配置上<code>redis</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/rate-limiter-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-ratelimiter<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h2><span style="color:inherit">安全/权限认证</span></h2> 
<h4><span style="color:inherit">Waf插件</span></h4> 
<p><code>Waf</code>插件，是<code>Apache ShenYu</code>网关，用来对流量实现防火墙，主要用来拦截非法请求，或者异常请求，并且给与相关的拒绝策略，它提供了黑白名单配置的功能。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>Waf插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/waf-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-waf<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">Sign 插件</span></h4> 
<p><code>Sign</code>插件，是<code>Apache ShenYu</code>网关，用来对请求进行签名认证。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>Sign插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/sign-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-sign<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">JWT 插件</span></h4> 
<p><code>JWT</code>插件，是<code>Apache ShenYu</code>网关，是针对 <code>http</code> 请求头的 <code>token</code> 属性或者是 <code>authorization</code> 属性携带值进行鉴权判断，兼容 <code>OAuth2.0</code>。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>jwt插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/jwt-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-jwt<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">OAuth2 插件</span></h4> 
<p><code>OAuth2</code>插件，是<code>Apache ShenYu</code>网关，使用 <code>Webflux OAuth2</code>客户端实现，用于支持 <code>OAuth2</code> 协议。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>oauth2插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/oauth2-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-oauth2<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h2><span style="color:inherit">个性化处理</span></h2> 
<h4><span style="color:inherit">Rewrite 插件</span></h4> 
<p><code>Rewrite</code>插件，是<code>Apache ShenYu</code>网关，支持使用正则表达式来重写<code>URI</code>的插件。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>rewrite插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/rewrite-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-rewrite<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">Redirect 插件</span></h4> 
<p><code>Redirect</code>插件，是<code>Apache ShenYu</code>网关，将请求进行重定向的插件，支持网关内部接口与外部地址。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>redirect插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/redirect-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-redirect<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">Request 插件</span></h4> 
<p><code>Request</code>插件，是<code>Apache ShenYu</code>网关容许用户对<code>请求参数</code>、<code>请求头</code> 以及 <code>Cookie</code> 进行<code>添加</code>、<code>修改</code>、<code>删除</code>等功能。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>request插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/request-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-request<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">Context-Path 插件</span></h4> 
<p><code>Context-Path</code>插件，是<code>Apache ShenYu</code>网关，容许用户对请求路径上的 <code>Context-Path</code>,进行 <code>添加</code>、<code>修改</code>、<code>删除</code>等功能。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>context_path插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/context-path-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-context-path<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">Param-Mapping 插件</span></h4> 
<p><code>Param-Mapping</code>插件，是<code>Apache ShenYu</code>网关，容许用户对请求体中的 <code>Body</code>,进行 <code>添加</code>、<code>修改</code>、<code>删除</code>字段等功能。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>param_mapping插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/param-mapping-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-param-mapping<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">ModifyResponse 插件</span></h4> 
<p><code>ModifyResponse</code>插件，是<code>Apache ShenYu</code>网关，用来对请求响应体中的 <code>响应头</code>,<code>状态码</code>，<code>响应内容</code>,进行 <code>添加</code>、<code>修改</code>、<code>删除</code>等功能。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>modifyResponse插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/modify-response-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-modify-response<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h2><span style="color:inherit">可观测性</span></h2> 
<h4><span style="color:inherit">Monitor 插件</span></h4> 
<p><code>Monitor</code>插件，是<code>Apache ShenYu</code>网关，使用 <code>prometheus</code>来完成对<code>请求量</code>，<code>QPS</code>, <code>JVM</code>等相关<code>metrics</code>进行监控的插件。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>monitor插件</code>将其设置为 <code>开启</code>, 并且配置 <code>prometheus</code>相关参数。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/monitor-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-monitor<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h4><span style="color:inherit">Logging 插件</span></h4> 
<p><code>Monitor</code>插件，是<code>Apache ShenYu</code>网关，容许用户日志中打印本次<code>请求信息</code>，包含 <code>请求路径</code>、<code>请求方法</code>、<code>请求参数</code> 、<code>响应头</code>、<code>响应体</code>等信息。用户想要使用它，请在网关添加如下依赖， 然后在 <code>Admin控制台</code> --> <code>插件管理</code> --> <code>logging插件</code>将其设置为 <code>开启</code>。 更详细的介绍请看 : https://shenyu.apache.org/zh/projects/shenyu/logging-plugin/</p> 
<pre><code class="language-xml"><span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-logging<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
   <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<h2><span style="color:inherit">下一个版本规划</span></h2> 
<ul> 
 <li> <p>RPC框架灰度发布增强，包含 <code>SpringCloud</code>，<code>GRPC</code>，<code>Dubbo</code>，<code>Sofa-RPC</code>，<code>Tars</code>等。</p> </li> 
 <li> <p>新增<code>ShenYu-Agent</code>模块，打造网关<code>metrics</code>, <code>tracing</code>, <code>logging</code> 等可观测性体系。</p> </li> 
 <li> <p>自定义插件动态加载，方便用户快速，不停机扩展与更新。</p> </li> 
 <li> <p>集成测试 + 单元测试 全面覆盖。</p> </li> 
</ul> 
<h2><span style="color:inherit">如何加入我们</span></h2> 
<p><code>Apache ShenYu</code> 是完全由国人主导的社区性开源项目，处在高速发展时期，<code>功能开发</code>，<code>文档完善</code>，<code>BUG修复</code> 等大量的事情需要完成。<br> <code>Apache ShenYu</code> 社区遵循 <code>Apache Way</code>的社区理念，打造一个<code>完全开放</code>，<code>治理</code>的社区。</p> 
<h4><span style="color:inherit">邮件订阅</span></h4> 
<ul> 
 <li><span style="color:inherit">发送订阅邮件。</span></li> 
</ul> 
<blockquote> 
 <p>用自己的邮箱向dev-subscribe@shenyu.apache.org发送一封邮件，主题和内容任意。</p> 
</blockquote> 
<ul> 
 <li><span style="color:inherit">接收确认邮件并回复。</span></li> 
</ul> 
<blockquote> 
 <p>完成步骤1后，您将收到一封来自dev-help@shenyu.apache.org的确认邮件（如未收到，请确认该邮件是否已被拦截，或已经被自动归入订阅邮件、垃圾邮件、推广邮件等文件夹）。直接回复该邮件，或点击邮件里的链接快捷回复即可，主题和内容任意。</p> 
</blockquote> 
<ul> 
 <li><span style="color:inherit">接收欢迎邮件。</span></li> 
</ul> 
<blockquote> 
 <p>完成以上步骤后，您会收到一封主题为WELCOME to dev@shenyu.apache.org的欢迎邮件，至此您已成功订阅Apache ShenYu的邮件列表。</p> 
</blockquote> 
<h4><span style="color:inherit">GitHub</span></h4> 
<ul> 
 <li><span style="color:inherit">网关 ： https://github.com/apache/incubator-shenyu</span></li> 
 <li><span style="color:inherit">前端 ： https://github.com/apache/incubator-shenyu-dashboard</span></li> 
 <li><span style="color:inherit">官网 ： https://github.com/apache/incubator-shenyu-websit</span></li> 
</ul> 
<h4><span style="color:inherit">Gitee</span></h4> 
<ul> 
 <li><span style="color:inherit">网关 ： https://gitee.com/Apache-ShenYu/incubator-shenyu</span></li> 
 <li><span style="color:inherit">前端 ： https://gitee.com/Apache-ShenYu/incubator-shenyu-dashboard</span></li> 
 <li><span style="color:inherit">官网 ： https://gitee.com/Apache-ShenYu/incubator-shenyu-websit</span></li> 
</ul>
                                        </div>
                                      
</div>
            