
---
title: '本周，Kubernetes Gateway API迎来重大更新'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220716/59ca7d43e1643a90ab471a93fd7d493d.png'
author: Dockone
comments: false
date: 2022-08-18 07:09:04
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220716/59ca7d43e1643a90ab471a93fd7d493d.png'
---

<div>   
<br>多年以来，Kubernetes用户一直希望能在Kubernetes API中配置更多高级路由功能。在谷歌的领导下，Gateway API的可用功能数量已经大幅增加。Gateway API能够支持Kubernetes中的多项新功能，包括流量拆分、标头修改，以及将流量转发至不同命名空间中的后端等等。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220716/59ca7d43e1643a90ab471a93fd7d493d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220716/59ca7d43e1643a90ab471a93fd7d493d.png" class="img-polaroid" title="image1_copy_4.png" alt="image1_copy_4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>自Gateway API项目提出以来，谷歌员工就一直在协助领导开源工作。该项目的两位主要贡献者均来自谷歌，另有10余名谷歌工程师也一直在为Gateway API贡献力量。<br>
<br>本周，Gateway API已经由alpha升级至beta阶段。作为该API的一大重要发展里程碑，beta阶段代表着其稳定性已经再上一个台阶。目前Gateway API中包含十余个API实现，且大多通过了全面的一致性测试，能够确保用户在任意环境或底层实现之上，获得一致的API使用体验。<br><br>
<h3>简单示例</h3>在这里，我们将通过一个简单示例向大家展示Gateway API的几项新功能。下面先从Gateway 开始：<br>
<pre class="prettyprint">apiVersion: gateway.networking.k8s.io/v1beta1<br>
kind: Gateway<br>
metadata:<br>
name: store-xlb<br>
spec:<br>
gatewayClassName: gke-l7-gxlb<br>
listeners:  <br>
- name: http<br>
protocol: HTTP<br>
port: 80 <br>
</pre><br>
此Gateway使用gke-I7-gxlb Gateway Class，也就是配置一个新的外部负载均衡器以支持此网关。当然，我们仍然需要告知负载均衡器应该将流量发送至哪里。为此，我们需要使用HTTPRoute：<br>
<pre class="prettyprint">apiVersion: gateway.networking.k8s.io/v1beta1<br>
kind: HTTPRoute<br>
metadata:<br>
name: store<br>
spec:<br>
parentRefs:<br>
- name: store-xlb<br>
rules:<br>
- matches:<br>
- path:<br>
    type: PathPrefix<br>
    value: /<br>
backendRefs:<br>
- name: store-svc<br>
  port: 3080<br>
  weight: 9<br>
- name: store-canary-svc<br>
  port: 3080<br>
  weight: 1 <br>
</pre><br>
这个简单的HTTPRoute将引导负载均衡器将流量路由至端口3080上的“store-svc” 或者 “store-canary-svc”，二选其一。在这里，我们使用权重执行一些基本的流量拆分，也就是将约10%的请求路由至canary（金丝雀测试）服务。<br>
<br>现在，假定我们希望为用户提供一种能够加入或退出金丝雀测试服务的方式，那么可以再额外添加一个带有部分标头匹配配置的HTTPRoute：<br>
<pre class="prettyprint">apiVersion: gateway.networking.k8s.io/v1beta1<br>
kind: HTTPRoute<br>
metadata:<br>
name: store-canary-option<br>
spec:<br>
parentRefs:<br>
- name: store-xlb<br>
rules:<br>
- matches:<br>
- header:<br>
    name: env<br>
    value: stable<br>
backendRefs:<br>
- name: store-svc<br>
  port: 3080<br>
- matches:<br>
- header:<br>
    name: env<br>
    value: canary<br>
backendRefs:<br>
- name: store-canary-svc<br>
  port: 3080 <br>
</pre><br>
这个HTTPRoute能够与我们之前创建的第一个路由协同工作。如果有任何请求将env标头设置为“stable”或者“canary”，则会被直接路由至相应的首选后端。<br>
<h3>立即使用</h3>与之前的Kubernetes API不同，大家无需升级至最新版本Kubernetes即可使用Gateway API。Gateway API是使用定制化资源定义（CRD）构建的，可被安装在任意1.16或更高版本（发布于约3年之前）的Kubernetes集群当中。<br>
<br>要在GKE上试用此API，请参阅GKE安装说明（<a href="https://cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#install_gateway_api_crds" rel="nofollow" target="_blank">https://cloud.google.com/kuber ... _crds</a>）。如果你希望将此AIP与其他实现一同使用，请参阅OSS入门页面（<a href="https://gateway-api.sigs.k8s.io/guides/getting-started/" rel="nofollow" target="_blank">https://gateway-api.sigs.k8s.i ... rted/</a>）。<br>
<h3>Gateway API的下一步计划</h3>随着Gateway API的核心功能趋于稳定，我们也开始积极探索新的特性与概念。目前，路由委托以及新的GPRCRoute等开发，都已经处于深度设计与验证当中。我们还建立起新的服务网格工作流，专门用于在各网格实现之间建立共识，指导它们将Gateway API用于服务到服务流量。与很多开源项目一样，我们也努力希望在开发新用例和实现API良好稳定性之间，找到最佳平衡点。我们的Gateway API已经取得一系列成果，也敬请大家期待它的未来发展与更多拓展。<br>
<br><strong>原文链接：<a href="https://opensource.googleblog.com/2022/07/gateway-api-graduates-to-beta.html">Gateway API Graduates to Beta</a></strong>
                                
                                                              
</div>
            