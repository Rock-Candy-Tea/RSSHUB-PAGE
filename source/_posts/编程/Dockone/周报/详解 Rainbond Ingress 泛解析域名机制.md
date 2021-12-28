
---
title: '详解 Rainbond Ingress 泛解析域名机制'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://tva1.sinaimg.cn/large/008i3skNly1gwzgzq8siij325i0dedhf.jpg'
author: Dockone
comments: false
date: 2021-12-28 12:12:46
thumbnail: 'https://tva1.sinaimg.cn/large/008i3skNly1gwzgzq8siij325i0dedhf.jpg'
---

<div>   
<br><blockquote><br><a href="https://www.rainbond.com/?channel=dockone">Rainbond</a> 作为一款云原生应用管理平台，天生带有引导南北向网络流量的分布式网关 rbd-gateway。区别于一般的 Ingress 配置中，用户需要自行定义域名的使用体验，Rainbond 的网关策略可以一键自动生成域名访问策略，用户通过这个域名可以立刻访问到部署在 Rainbond 上的业务系统。这个使用体验在开发测试场景下非常友好，这篇文章详解了这一机制到底是如何实现的。</blockquote><h3>Gateway 与 Ingress</h3>Rainbond 团队开发了高性能分布式网关组件 rbd-gateway，作为集群内部的 Ingress Controller 处理集群南北流量。它同时支持 L4 和 L7 层协议，以及一键开启 WebSocket 等高级功能。在使用它的时候，一个细节功能点非常好用，就是可以一键生成一个可以被访问的域名地址。<br>
<br><img src="https://tva1.sinaimg.cn/large/008i3skNly1gwzgzq8siij325i0dedhf.jpg" alt="image-20211202142555295" referrerpolicy="no-referrer"><br>
<br>这个域名的格式详解如下：<br>
<pre class="prettyprint">http://<servicePort>.<service_alias>.<tenant_name>.17a4cc.grapps.cn/<br>
- servicePort: 访问策略对应的目标端口名称<br>
- service_alias: 当前服务组件的别名<br>
- tenant_name: 当前团队的别名<br>
- .17a4cc.grapps.cn: 当前集群的泛解析域名<br>
</pre><br>
<br>实际上，这一条路由规则，是由 Kubernetes 中对应的 ingress 和 service 所定义的。整个访问链路可以归纳为下图：<br>
<br><img src="https://tva1.sinaimg.cn/large/008i3skNly1gwzkbrhzv2j31ie0u0q6w.jpg" alt referrerpolicy="no-referrer"><br>
<br>开启 <strong>对外服务</strong> 开关，相当于自动生成了以下资源：<br>
<br><pre class="prettyprint">apiVersion: v1<br>
kind: Service<br>
metadata:<br>
labels:<br>
creator: Rainbond<br>
event_id: ""<br>
name: gr49d848ServiceOUT<br>
port_protocol: http<br>
protocol: http<br>
rainbond.com/tolerate-unready-endpoints: "true"<br>
service_alias: gr49d848<br>
service_port: "5000"<br>
service_type: outer<br>
tenant_name: 2c9v614j<br>
name: service-8965-5000out<br>
namespace: 3be96e95700a480c9b37c6ef5daf3566<br>
spec:<br>
clusterIP: 172.21.7.172<br>
ports:<br>
- name: tcp-5000<br>
port: 5000<br>
protocol: TCP<br>
targetPort: 5000<br>
selector:<br>
name: gr49d848<br>
sessionAffinity: None<br>
type: ClusterIP<br>
status:<br>
loadBalancer: &#123;&#125;<br>
apiVersion: extensions/v1beta1<br>
kind: Ingress<br>
metadata:<br>
annotations:<br>
nginx.ingress.kubernetes.io/weight: "100"<br>
generation: 1<br>
labels:<br>
creator: Rainbond<br>
service_alias: gr49d848<br>
tenant_name: 2c9v614j<br>
name: 3cf8d6bd89250eda87ac127c49694a05<br>
namespace: 3be96e95700a480c9b37c6ef5daf3566<br>
spec:<br>
rules:<br>
- host: 5000.gr49d848.2c9v614j.17a4cc.grapps.cn<br>
http:<br>
  paths:<br>
  - backend:<br>
      serviceName: service-8965-5000out<br>
      servicePort: 5000<br>
    path: /<br>
status:<br>
loadBalancer: &#123;<br>
</pre>&#125;<br>
<br><h3>自动生成域名</h3>对于大多数开发者而言，域名算是一种稀缺资源，如何为自己茫茫多的 Ingress rule 分配域名，是一件很令人头疼的事情。毕竟只有拥有了自己的域名时，才能够彻底掌控其解析的规则，避免无止境的修改 <code class="prettyprint">/etc/hosts</code> 文件。<br>
<br>市面上绝大多数 Kubernetes  管理工具都可以用半自动的方式生成 Service 与 Ingress资源。这种半自动的方式特指让用户在图形化 UI 界面上，输入必要的信息后，由管理工具自行生成对应的 yaml 配置文件，并加载到 Kubernetes 中去。但是对于所配置的域名，鲜有工具可以做到如 Rainbond 一样的使用体验。<br>
<br>达成这一优秀体验的关键在于泛解析域名的使用。<br>
<br>对泛解析域名最简单明了的解释就是：符合  <code class="prettyprint">*.mydomain.com</code> 这一规则的任意域名，都可以解析到同一个 IP 地址上去。在当下这一使用场景中，我们只需要将泛解析域名 <code class="prettyprint">*.17a4cc.grapps.cn</code> 解析到 rbd-gateway 所在的服务器 IP 地址，就可以随意为 <code class="prettyprint">Ingress rule</code> 配置符合规则的域名了。<br>
<br><img src="https://tva1.sinaimg.cn/large/008i3skNly1gwzmi07jcnj30b60cat91.jpg" alt referrerpolicy="no-referrer"><br>
<br>Rainbond 在产品设计层面将 <code class="prettyprint">Ingress rule</code> 和泛解析域名结合在了一起，自动为每个服务端口生成全局唯一的域名。并在集群安装时，自动向公网 DNS 服务器注册了解析记录，集群安装完毕之后，所生成的所有域名，都是可以被公网解析的，只要 PC 客户端可以使用公网 DNS 服务，就可以解析域名，并访问到指定的服务端口。<br>
<br>Rainbond 通过不同的三级域名 （比如当前场景中的 <code class="prettyprint">17a4cc</code>）来区分不同的集群。这里涉及到关于泛解析域名的一个特点，子级域名的解析记录，优先级高于父级域名的解析记录。<br>
<pre class="prettyprint">===========================================<br>
// 对两级泛解析域名注册解析记录<br>
*.grapps.cn           =解析记录注册=> 1.1.1.1<br>
<h1>*.17a4cc.grapps.cn    =解析记录注册=> 2.2.2.2</h1>===========================================<br>
// 客户端解析结果<br>
abc.grapps.cn         =解析 IP 地址=> 1.1.1.1<br>
abc.def.grapps.cn     =解析 IP 地址=> 1.1.1.1<br>
abc.17a4cc.grapps.cn  =解析 IP 地址=> 2.2.2.2     // 优先使用 *.17a4cc.grapps.cn 的解析记录<br>
</pre><br>
<br>---<br>
<br><a href="https://www.rainbond.com/?channel=dockone">Rainbond</a>是一个开源的云原生应用管理平台，使用简单，不需要懂容器和Kubernetes，支持管理多个Kubernetes集群，提供企业级应用的全生命周期管理，功能包括应用开发环境、应用市场、微服务架构、应用持续交付、应用运维、应用级多云管理等。<br>
<br>Github：<a href="https://github.com/goodrain/rainbond" rel="nofollow" target="_blank">https://github.com/goodrain/rainbond</a><br>
<br>官网：<a href="https://www.rainbond.com/?channel=dockone" rel="nofollow" target="_blank">https://www.rainbond.com?channel=dockone</a><br>
<br>微信群：请搜索添加群助手微信号 <code class="prettyprint">wylhzmyj</code><br>
<br>钉钉群：请搜索钉钉群号 <code class="prettyprint">31096419</code>
                                
                                                              
</div>
            