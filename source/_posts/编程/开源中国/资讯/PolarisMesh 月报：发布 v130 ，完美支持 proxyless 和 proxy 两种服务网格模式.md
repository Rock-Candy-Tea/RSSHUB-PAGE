
---
title: 'PolarisMesh 月报：发布 v1.3.0 ，完美支持 proxyless 和 proxy 两种服务网格模式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1202/141022_Bh8O_5430600.png'
author: 开源中国
comments: false
date: Thu, 02 Dec 2021 14:18:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1202/141022_Bh8O_5430600.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#060605; margin-left:0; margin-right:0; text-align:justify">北极星（PolarisMesh ）是腾讯开源的百万级服务发现和治理中心，积累了腾讯从虚拟机到容器时代的分布式服务治理经验。作为分布式和微服务架构中的核心组件，PolarisMesh 提供服务寻址、流量调度、故障容错和访问控制等一系列能力，在K8s 和虚拟机环境中可以无差别使用，支持主流的开发模式，兼容grpc、spring cloud和servicemesh等开源生态，帮助用户快速构建扩展性强、可用性高的业务架构，实现从传统架构到云原生架构的转型。</p> 
<p style="color:#060605; margin-left:0; margin-right:0; text-align:justify">Github地址：https://github.com/polarismesh/polaris</p> 
<h1 style="margin-left:0px; margin-right:0px; text-align:justify">背景</h1> 
<h2 style="margin-left:0px; margin-right:0px"><strong>1. Proxy 网格</strong></h2> 
<p style="margin-left:0; margin-right:0"><img alt height="298" src="https://static.oschina.net/uploads/space/2021/1202/141022_Bh8O_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">对于proxy网格，这种模式能有效得将应用与治理组件解耦，便于应用以极低侵入的代价接入微服务体系。但是它却有一个难以规避的问题——性能以及资源消耗，proxy网格为了将应用与治理组件解耦，采取运行独立的proxy容器来接管业务容器的东西流量；为了达到治理能力，proxy需要能够解析业务之间的通信协议并根据其内容作出不同的治理动作，因此proxy实际上大部分的工作都是在频繁的消耗CPU进行序列化相关操作以及网络请求转发，降低整体业务的响应时长以及QPS。</p> 
<h2 style="margin-left:0px; margin-right:0px"><strong>2.proxyless 网格</strong></h2> 
<p style="margin-left:0; margin-right:0"><img alt height="259" src="https://static.oschina.net/uploads/space/2021/1202/141328_stnn_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">因为proxy网格难以规避的性能以及资源消耗问题，proxyless网格被重新提了起来，即proxy做的事情，再次回到了业务容器中——即通过引入一个轻量的SDK来负责原先proxy的任务。由于整个网格架构中没有了proxy这一环，性能降低以及资源消耗的问题得到了较好的解决。由于北极星诞生之初，就一并开发了多语言的轻量级的SDK作为北极星在proxyless的方案，并且也是腾讯内部分布式服务长期使用的开发方式。</p> 
<p style="margin-left:0; margin-right:0">在之前的版本中，北极星提供了多语言的轻量级高性能SDK，实现注册发现、流量调度、熔断降级和访问控制等服务治理功能。从v1.3.0 版本开始，北极星在通信协议层完成了对xDS协议的支持，可以直接作为envoy或者gRPC的proxyless形式的控制面，北极星对于两种网格模式的互联互通和统一治理能力的正式开放。</p> 
<h1 style="margin-left:0px; margin-right:0px"><strong>实现方案</strong></h1> 
<p><span>为了实现proxyless服务与proxy服务的互联互通和统一治理，必须解决以下2个关键点：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span>服务数据之间可互通</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>治理规则的互通</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>由于通过istio默认使用了kubernetes crd作为服务注册中心，因此为了实现服务数据之间的互通，必须打通polaris与kubernetes crd这2个注册中心。polaris扩展kubernetes的controller的方式，开发了polaris-controller组件，通过监听service和endpoint事件，实现kubernetes的服务数据与polaris进行实时同步。从而解决服务数据互通问题。</span></p> 
<p><span>为了解决治理规则互通的问题，可以通过2个方式来打通：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p><span>polaris规则数据转换成istio的规则数据格式，并且与kubernetes的crd进行打通</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>polaris规则数据转换成XDS数据，直接下发给envoy，不经过istio</span></p> </li> 
</ol> 
<p><span>为解决全量加载性能问题有两种方案：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p><span>修改Istio，让它支持按需加载服务数据</span></p> </li> 
 <li> <p><span>直接支持envoy的VHDS协议，envoy直接对接polaris按需加载服务数据</span></p> </li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>因为Istio社区已经全面转向MCP-OVER-XDS，将原来MCP改成MCP-OVER-XDS存在较大的协议调整工作量。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>结合以上问题的可选解决方案，权衡各方面的考虑，我们最终决定采用envoy直接对接polaris的方案来解决一开始提出的3个问题，系统架构如下图：</span></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0"><img alt height="441" src="https://static.oschina.net/uploads/space/2021/1202/141239_53wn_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0px; margin-right:0px"><strong>北极星网格优势</strong></h1> 
<p><strong><img alt height="236" src="https://static.oschina.net/uploads/space/2021/1202/141609_CPva_5430600.png" width="700" referrerpolicy="no-referrer"></strong></p> 
<p>这个方案有<strong>三大优势</strong>：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p>多种微服务体系完美打通</p> </li> 
 <li> <p>K8s和虚拟机环境无差别使用</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持多K8s集群之间的服务发现</p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px"><span style="color:#000000"><strong>1. 多种微服务体系完美打通</strong></span></h2> 
<p style="margin-left:0; margin-right:0">在分布式和微服务架构的演进过程中，从部署环境以及应用+治理的结合模式，分别经历了不同的发展阶段。</p> 
<p style="margin-left:0; margin-right:0">对于部署环境</p> 
<p><img alt height="196" src="https://static.oschina.net/uploads/space/2021/1202/141708_37IJ_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">而对于应用和治理结合模式</p> 
<p style="margin-left:0; margin-right:0"><img alt height="483" src="https://static.oschina.net/uploads/space/2021/1202/141731_gRWB_5430600.png" width="700" referrerpolicy="no-referrer"><br> 可以看到，无论是部署环境，还是应用+治理结合模式，其发展都不是一蹴而就的，大部分情况下都存在过度阶段，因此这里就引入了不同的微服务体系：</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p>sdk+discovery（无kubernetes）</p> </li> 
 <li> <p><span>sdk+discovery 以及 proxy网格（vm + kubernetes 混合部署）</span></p> </li> 
 <li> <p><span>proxy网格 （kubernetes）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>proxyless网格（kubernetes）</span></p> </li> 
</ol> 
<p style="margin-left:0; margin-right:0">对于上述<strong>不同的微服务技术体系，如何做到统一的治理</strong>？</p> 
<p style="margin-left:0; margin-right:0">北极星不仅仅通过xDS协议的支持以及多语言客户端来解决1、3、4情况，同时还提供了polaris-controller组件，用于同步kubernetes中的service到polaris，使得polaris既有通过kubernetes注册服务，也有通过polaris注册的服务，解决了vm + kubernetes 混合部署模式下的应用之间互通互联的问题。</p> 
<h2 style="margin-left:0px; margin-right:0px"><span style="color:#000000"><strong>2. Kubernetes 和虚拟机环境无差别使用</strong></span></h2> 
<p style="margin-left:0; margin-right:0"><span>对于polaris来说，无论是在Kubernetes上的运行的服务还是运行在VM上的运行服务，统一转换为polaris的数据模型，由polaris充当控制面的角色，提供统一的服务操作入口以及服务治理规则定义，用户无需在关心自己的服务运行在何种环境下，也无需关心该如何统一管理多种运行环境下的服务实例。</span></p> 
<p style="margin-left:0; margin-right:0"><span>无论在kubernetes环境还是在VM环境，通过提供polaris-agent组件，直接代理业务的DNS请求，通过对DNS的解析，返回被调服务的一个实例给主调方用于完成业务请求，让业务在代码无侵入前提下使得业务能够享受polaris的服务发现功能。</span></p> 
<h2 style="margin-left:0px; margin-right:0px"><span style="color:#000000"><strong>3. 支持多 Kubernetes 集群之间的服务发现</strong></span></h2> 
<p style="margin-left:0; margin-right:0"><span>随着业务规模的增加，可能出现不同业务不同kubernetes集群，如果出现不同业务之间需要相互服务调用，那么就需要解决跨kubernetes集群间服务发现的问题，当前istio要支持跨kubernetes集群的服务发现的话，两两kubernetes集群间都需要进行配置，那么随着kubernetes集群数变多，那么就需要不断的执行istio配置操作，相比之下，polaris支持多kubernetes集群服务发现，只需要用户在每个kubernetes集群部署一个polaris-controller，每个controller都指向同一个polaris-server集群即可。</span></p> 
<h1 style="margin-left:0px; margin-right:0px"><strong>1.3.0 Release Notes</strong></h1> 
<p style="margin-left:0; margin-right:0"><strong>Feature：</strong></p> 
<ul> 
 <li>【polaris】接入层支持可观测性指标暴露给prometheus</li> 
 <li>【polaris】优化部署脚本使用体验问题</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>Bugfix：</strong></p> 
<ul> 
 <li>【polaris】优化心跳处理方案，解决polaris重启可能导致实例健康状态不正确的问题</li> 
 <li>【polaris】修复部分单元测试用例</li> 
</ul> 
<h1 style="margin-left:0px; margin-right:0px"><strong>后续规划</strong></h1> 
<ul> 
 <li><span>【polaris-console】支持命名空间管理</span></li> 
 <li><span>【polaris-php】支持最好的语言PHP（7.x）接入</span></li> 
 <li><span>【spring-cloud-tencent】支持spring cloud 2020接入</span></li> 
 <li><span>【spring-boot-polaris】支持spring boot</span></li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span>更多详细的生态规划任务可以查看 issue：https://github.com/polarismesh/polaris/issues/163</span></p>
                                        </div>
                                      
</div>
            