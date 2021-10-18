
---
title: 'BFE Ingress Controller 正式发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3686'
author: 开源中国
comments: false
date: Mon, 18 Oct 2021 17:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3686'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">大家期待已久的BFE IngressController终于在近日正式发布！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">BFE Ingress Controller是基于 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjY0NDQxMw%3D%3D%26mid%3D2247483658%26idx%3D1%26sn%3D35de005cad4f1e59df22c276badb854f%26chksm%3Dc03bbc58f74c354e9030df6b255bb79b03ab2315174b70a6808033ce841dffbdce23b1cfb588%26scene%3D21%23wechat_redirect" target="_blank">BFE</a> 实现的Kubernetes Ingress Controller，用于支持在 Kubernetes 中使用 Ingress来暴露服务并进行负载均衡、SSL终结等，现已正式发布并可以下载使用。BFE Ingress Controller 采用Apache-2.0 License，项目地址：https://github.com/bfenetworks/ingress-bfe 。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>背景</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">随着云原生、容器化的不断推进，以及用户对BFE强大能力的使用和了解，我们不断收到社区的反馈，希望能够为在Kubernetes环境中部署的服务，使用BFE进行流量接入和转发。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在Kubernetes中，对外暴露服务有Ingress、LoadBalancer、NodePort等多种方式。Ingress是对服务的外部HTTP/HTTPS访问进行管理的 API 对象。采用Ingress暴露服务时，需要部署Ingress Controller，以根据 Ingress 资源上定义的规则对流量进行控制和路由。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">今年2月，BFE开源社区的开发者们发起了基于BFE的Ingress Controller的项目，目的是提供一款Ingress Controller，使用户能够在使用Ingress进行流量接入时，享受到BFE的众多优秀特点和强大能力。经过大半年的开发和测试，BFE Ingress Controller终于在本月发布了。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>主要</strong><strong>功能</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">BFE Ingress Controller实现了Kubernetes原生Ingress的功能，并基于BFE的能力，扩展了路由规则描述能力和服务间的流量调度能力。<span>主要功能包括：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">HTTP/HTTPS流量路由</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:0; margin-right:0; text-align:left">支持根据Host、Path、Header、Cookie对请求进行路由</p> </li> 
   <li> <p style="margin-left:0; margin-right:0; text-align:left">支持Path的精确匹配、前缀匹配</p> </li> 
   <li> <p style="margin-left:0; margin-right:0; text-align:left">支持Host的精确匹配、通配符匹配</p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">多Service之间负载均衡</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:0; margin-right:0; text-align:left">支持在提供相同服务的多个Service之间按权重进行负载均衡</p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">TLS终结</p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">灰度发布</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:0; margin-right:0; text-align:left">支持基于HTTP Header/Cookie的服务灰度发布</p> </li> 
  </ul> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更多信息，见BFE Ingress Controller的文档：https://github.com/bfenetworks/ingress-bfe。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>如何</strong><strong>部署</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">我们提供了BFE Ingress Controller的Docker镜像、所需的yaml配置文件、完善的手册，您可以根据文档中的“部署指南”，快速上手部署BFE Ingress Controller。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>Ingress配置</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">通过配置Ingress资源，可以定义 Kubernetes 集群内服务对外提供服务时的流量路由规则。BFE Ingress Controller支持Kubernetes原生定义的Host规则、Path规则，并利用注解(Annotation)支持了Header规则、Cookie规则，以及多服务之间的负载均衡。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在文档中的“配置指南”部分，我们提供了详细的说明和多个示例。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>后续计划</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">接下来，我们会将更多的BFE的成熟能力，加入到BFE Ingress Controller当中，并提供对Gateway API的支持。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">期待您的使用反馈，并希望有更多人加入BFE开源社区一起建设。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.baidu.com%2F%3Ffrom%3D101503" target="_blank">点击进入获得更多技术信息~~</a></p>
                                        </div>
                                      
</div>
            