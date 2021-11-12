
---
title: '云原生环境下的API业务安全思考'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/e31757bbc30bc2b3de77043a5a23d5ac.png'
author: Dockone
comments: false
date: 2021-11-12 12:11:28
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/e31757bbc30bc2b3de77043a5a23d5ac.png'
---

<div>   
<br><h3>概述</h3>针对单体架构的应用，安全防护往往在边界网关设备处。随着业务需求的不断变化以及技术的持续更新，企业应用开始从单体架构向微服务架构转变。不同应用模块可以根据业务规模进行动态扩缩容，与此同时，微服务应用也为API安全防护带来了新的挑战。<br>
<br>笔者认为，微服务应用API安全防护相比传统API安全防护主要增加了以下几类挑战：<br>
<ol><li>随着服务更细颗粒度的划分，API接口的数量激增及调用关系的复杂，API管理将变得更加困难；</li><li>服务间调用的不断增多使得利用API漏洞进行横向攻击的风险也不断增加，从而增加了防御难度；</li><li>传统防御方式往往是在网络边界对南北向的流量进行检测，微服务间产生的东西向流量无法通过传统边界防御的方式检测。</li></ol><br>
<br>如上所述，我们需要一种更细粒度的适用于微服务环境下的全流量的API防护方法。本文将首先介绍传统应用API安全防护方法，进而引出云原生环境下微服务应用API安全防护方法，最后通过实际案例对微服务应用API安全防护方法进行剖析解读，希望可以引发大家更多的思考。<br>
<h3>API安全防护</h3>API（ApplicationProgramming Interface）作为程序之间交互的桥梁，承担着数据传输的重大作用。越来越多的安全问题都来自于API泄露，API设计缺陷等问题。微服务环境下，API数量的激增为系统的安全风险带来新的挑战。OWASP组织总结的API安全风险Top 10如表1所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211110/e31757bbc30bc2b3de77043a5a23d5ac.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/e31757bbc30bc2b3de77043a5a23d5ac.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>表1</em><br>
<br>对于API防护也主要集中在以下几个方面：<br>
<ol><li>身份认证：可靠的身份认证及权限控制机制</li><li>访问控制：对发起请求的对象，请求的速率进行准确的访问控制</li><li>安全防护：传统Web安全风险的防护，SQL注入，XSS，CSRF等</li><li>日志记录：对请求的链路进行完善的日志记录</li><li>配置管理：对API参数、调用链路、版本等进行有效管理</li></ol><br>
<br><h3>传统API防护方案</h3>在传统的网络架构中，内外网一般有明确的网络边界。常见的安全防护设备，例如WAF，防火墙，API网关等，都会在网络边界搭建来实现安全防护。主要防护进出内网的南北向流量，对于集群内部的API调用行为无法做到有效的防护。因此，一旦网络内部的一台机器的沦陷，会导致整个边界类型的API防护机制的失效。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211110/b4fcde026940c53c6cc13ab90fafdb0d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/b4fcde026940c53c6cc13ab90fafdb0d.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1</em><br>
<h3>微服务应用API治理与安全防护</h3>在微服务环境下，存在着大量的服务之间的调用。这时，内部服务的API调用的安全风险就不得不考虑进去。同时，在云原生环境中，内外网边界逐渐模糊，更多的API会暴露在云上。随着API暴露面的增加，API被攻击的风险也大大增加，传统的南北向的边界流量的防护体系在云原生环境下的防护将会显得力不从心。因此我们需要一种更细粒度的适用于微服务环境下的全流量的API防护的方案。<br>
<h4>微服务治理</h4>在微服务环境下，面对众多数据的微服务API，我们首先要解决的就是服务发现以及负载均衡的问题。<br>
<br>即如何发现服务的提供者、如何转发服务调用方发起的请求。目前业界主要有三种服务发现的模式。<br>
<ul><li>集中代理，提供统一代理入口，一般通过域名解析的方式由集中代理实现服务的负载均衡转发</li><li>客户端代理，该模式通过独立中心的服务注册组件实现服务发现，负载均衡是在客户端自己独自实现</li><li>Service Mesh模式，该模式和客户端代理模式有点相似，也是通过独立中心的服务注册组件实现服务发现，但是负载均衡是使用单独的进程，通常被称为Sidecar，统一实现。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211110/ce4a5bb0c8e5f4767eb116d0d1cf7152.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/ce4a5bb0c8e5f4767eb116d0d1cf7152.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>表2</em><br>
<br>集中代理模式，对业务变动较小，实现较为简单，但是存在集中单点的风险，且对集中代理的要求较高。客户端代理模式可以有效解决集中代理的单点的问题，同时直接调用服务提供者，可以降低网络开销，但是负载均衡需要自己实现，提升了实现复杂度，客户端比较复杂，不易于管理。Service Mesh弥补了两者的不足，通过Sidecar的模式做到负载均衡的统一。<br>
<h4>Service Mesh</h4>Service Mesh这个词的创始人William Morgan对Service Mesh定义是：<br>
<br>“服务网格是一个基础设施层，用于处理服务间通信。云原生应用有着复杂的服务拓扑，服务网格保证请求在这些拓扑中可靠地穿梭。在实际应用当中，服务网格通常是由一系列轻量级的网络代理组成的，它们与应用程序部署在一起，但对应用程序透明。”<br>
<br>Service Mesh在微服务的基础上加上了一个网络代理，所有的流量都在Sidecar上完成，Sidecar完成服务发现，负载均衡，智能路由，故障注入，熔断等动能，从而微服务只需要注重业务实现。<br>
<br>Service Mesh的架构如下图2所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211110/88aaa6a9477fbc22e8f29244332397a0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/88aaa6a9477fbc22e8f29244332397a0.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图2</em><br>
<br>从该架构可以看出，Service Mesh架构的设计为安全防护提供了很好的入口，在Sidecar中，我们可以完成上文提到的身份认证、访问控制、访问控制、日志记录、配置管理等API防护功能。目前比较知名的项目有Linkerd，Envoy，Istio，HashiCorp Consul等。<br>
<h4>Istio</h4>Istio就是目前受Google/IBM等大厂支持和推进的一个Service Mesh开源框架组合。Istio提供一种简单的方式来为已部署的服务建立网络，该网络具有负载均衡、服务间认证、监控等功能，而不需要对服务的代码做任何改动。Istio官方对Istio的架构描述如下图3：<br>
<br>Istio在逻辑上分为数据平面和控制平面，控制平面主要实现微服务管理需要的服务发现的功能，数据平面的Envoy以Sidecar的模式提供负载均衡的功能。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211110/6e40c38c3d808bd03bc950dd86c18950.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/6e40c38c3d808bd03bc950dd86c18950.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图3</em><br>
<h4>Envoy</h4>其中Envoy是Istio的核心组件之一，以Sidecar的方式与服务运行在一起，对服务的流量进行拦截转发。具有路由，流量控制等强大特性。Envoy主要面向SOA（面向服务的架构）的网络代理，所以非常适用于微服务，其主要是用来调解Service Mesh中所有服务的入站和出站流量。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211110/736ca813fdc40aee47ce012d077c9bf0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/736ca813fdc40aee47ce012d077c9bf0.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图4</em><br>
<br>Envoy流量走向，从上图4可以看出，所有流经后端业务容器的流量都会被Envoy劫持，流经各种Envoy的过滤器（EnvoyFilter），最终流量再转发到业务容器。Envoy的流量处理都是通过各种过滤器来实现。<br>
<br>过滤器分为两个类别：<br>
<ol><li>网络过滤器（L3/L4），是Envoy网络连接处理的核心</li><li>HTTP过滤器（L7），由特殊的网络过滤器HttpConnectionManager管理，专门处理HTTP1/HTTP2/gRPC请求</li></ol><br>
<br><h4>安全防护</h4>虽然Service Mesh架构的出现，有效解决了微服务治理的问题，但是还是缺失API安全风险防护所需的访问控制、安全防护等功能。得益于Envoy接管了进出微服务的所有的流量以及Envoy的过滤器的机制，只需要在Envoy的过滤器中实现API安全防护的能力，我们就得到了一个微服务环境下的全流量的安全防护体系。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211110/f93447e2fabe88f4bd939348f2580574.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/f93447e2fabe88f4bd939348f2580574.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图5</em><br>
<br>数据平面数据流走向如图5所示：<br>
<ol><li>请求发送至Pod,Envoy截获此请求</li><li>请求经过Envoy事先定义的Filter，Envoyfilter官方提供了多种实现方式，常用的有Lua，Wasm等</li><li>Filter对请求流量进行检测，判断是否是恶意流量，对非法行为直接阻拦，合法行为放行转发到业务容器</li><li>业务容器接受到正常请求处理完，返回响应报文</li><li>Filter对响应流量进行检测，判断是否是恶意流量，对非法行为直接阻拦，合法行为放行响应给请求方</li></ol><br>
<br><h3>案例</h3><h4>内置过滤器</h4>通过内置过滤器，我们可以在不编写代码的前提下，只需要通过配置项，就可以对流经Envoy的API请求进行防护。<br>
<br>假设为了解决数据安全风险，某请求接口需要添加Token，利用Envoy的过滤器就可以对特定请求添加Token。<br>
<br>具体EnvoyFilter配置如下：<br>
<pre class="prettyprint">apiVersion:networking.istio.io/v1alpha3<br>
kind:EnvoyFilter<br>
metadata:<br>
name: add-header<br>
namespace: <user-namespace><br>
spec:<br>
configPatches:<br>
- applyTo: VIRTUAL_HOST<br>
match:<br>
  context: SIDECAR_OUTBOUND<br>
  routeConfiguration:<br>
    vhost:<br>
      name: www.test.com:8080<br>
      route:<br>
        name: default<br>
patch:<br>
  operation: MERGE<br>
  value:<br>
    request_headers_to_add:<br>
    - append: true<br>
      header:<br>
        key: "X-AUTH-TOKEN"<br>
        value: token<br>
</pre><br>
<h4>自定义过滤器</h4>在更复杂的场景下，通过Envoy默认的Filter无法达到我们的需求，这时候我们希望能通过自定义的代码来实现更定制化的业务逻辑。<br>
<br>通过Envoy提供的Lua或者Wasm的过滤器。我们可以直接编写Lua代码，或者将C++、Resty代码编译成WebAssembly代码，实现自定义的过滤器。<br>
<br>假设发现特定接口有信息泄露的风险，在服务修复前，需要对调用该接口的所有请求进行拦截处理。利用Envoy的http_filter的Lua扩展，我们可以很容易的对包含特定特征的请求进行拦截。<br>
<br>具体EnvoyFilter配置如下：<br><br>
<pre class="prettyprint">apiVersion:networking.istio.io/v1alpha3<br>
kind:EnvoyFilter<br>
metadata:<br>
name: test-envoyfilter<br>
namespace: test-filter<br>
spec:<br>
configPatches:<br>
# The first patch adds the lua filter tothe listener/http connection manager<br>
- applyTo: HTTP_FILTER<br>
match:<br>
  context: GATEWAY<br>
  listener:<br>
   filterChain:<br>
     filter:<br>
       name: envoy.filters.network.http_connection_manager<br>
       subFilter:<br>
          name: envoy.filters.http.router<br>
patch:<br>
  operation: INSERT_BEFORE<br>
  value:<br>
    name: envoy.filters.http.lua<br>
    typed_config:<br>
      "@type":type.googleapis.com/envoy.extensions.filters.http.lua.v3.Lua<br>
      inline_code: |<br>
        functionenvoy_on_request(request_handle)<br>
          ifrequest_handle:headers():get(":path") == "/xss" then<br>
           request_handle:respond(&#123;[":status"] ="403"&#125;,"ok")<br>
          end<br>
        end<br>
        functionenvoy_on_response(response_handle)<br>
        end<br>
</pre><br>
更为完整的采用Lua过滤器完成API防护的可以参考开源项目curiefense的实现。<br>
<h3>总结</h3>在云原生环境下，利用Service Mesh的架构，在Sidecar提供负载均衡，路由的同时，同时提供API安全防护的能力，可以不仅防护南北向的流量，也可以提供东西向的全流量的安全防护，有效保证的云原生应用的安全性。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/KVBBmM_1q6VNs0hD3HYjMw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/KVBBmM_1q6VNs0hD3HYjMw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            