
---
title: 'NGINX Ingress Controller for Kubernetes 版本 1.8.0更新及介绍'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic4.zhimg.com/v2-bf2ad7d899dafcf301b0b272c3678ae3_r.jpg'
author: 开源中国
comments: false
date: Mon, 04 Oct 2021 06:17:00 GMT
thumbnail: 'https://pic4.zhimg.com/v2-bf2ad7d899dafcf301b0b272c3678ae3_r.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">NGINX Ingress Controller for Kubernetes 版本 1.8.0建立在 Kubernetes 平台（包括 Red Hat OpenShift、Amazon Elastic Container Service for Kubernetes (EKS)、Azure Kubernetes Service (AKS)、Google Kubernetes Engine (GKE)、IBM Cloud Private、Diamanti 等）Ingress 负载均衡解决方案的持续开发基础之上。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><img alt="preview" src="https://pic4.zhimg.com/v2-bf2ad7d899dafcf301b0b272c3678ae3_r.jpg" referrerpolicy="no-referrer"></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">版本 1.8.0 的充分彰显了我们致力于提供灵活、强大且易用的 Ingress Controller的承诺。Ingress Controller可以使用 Kubernetes Ingress 资源和 NGINX Ingress 资源进行配置：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• Kubernetes Ingress 资源充分兼容不同的 Ingress Controller实现，并且可使用annotations和自定义模板进行扩展，以生成复杂配置。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• NGINX Ingress 资源提供 了NGINX 特定的配置模式，与自定义通用 Kubernetes Ingress 资源的方式相比更为丰富和安全。</p> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">即版本1.7.0的基础上，版本 1.8.0 的主要增强和改进包括：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 集成 NGINX App Protect – NGINX App Protect 是领先的 NGINX 应用安全解决方案，能够为 Web 应用提供深度签名和结构化保护。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 面向 NGINX Ingress 资源的可扩展性 – 对于想要使用 NGINX Ingress 资源但需要对 VirtualServer 和 VirtualServerRoute 资源中尚未实施的 NGINX 特性进行自定义的用户，目前支持两种互补机制：配置snippets和自定义模板。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• URI 重写以及修改请求和响应头 – 这些特性可支持您精细控制（添加、删除和忽略）传递给上游以及传递回客户端的请求和响应头。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 策略和 IP 地址访问控制列表 – 通过将策略以及流量管理功能抽象成独立的K8S对象，不同团队可以在多个地方进行定义并部署。访问控制列表 (ACL) 可用于过滤流经 NGINX Ingress Controller的出入站网络流量。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="preview" src="https://pic2.zhimg.com/v2-185d1d097272c87758e12a0c590daee9_r.jpg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 其他新增特性 –</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>readiness 探测</li> 
 <li>在 VirtualServer 和 VirtualServerRoute 资源及 Helm 图表中支持多个 Ingress Controller</li> 
 <li>关于 VirtualServer 和 VirtualServerRoute 资源的状态信息</li> 
 <li>NGINX Ingress Operator for Red Hat OpenShift 更新</li> 
</ol> 
<hr> 
<h2 style="margin-left:0; margin-right:0; text-align:left">什么是 NGINX Ingress Controller for Kubernetes？</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">NGINX Ingress Controller for Kubernetes 是一个在 Kubernetes 环境中与 NGINX Open Source 或 NGINX Plus 实例一起运行的守护进程。该守护进程负责监视 Kubernetes Ingress 资源和 NGINX Ingress 资源，以识别部署了Ingress的services。一旦发现此类请求，它将自动配置 NGINX 或 NGINX Plus，从而将流量路由到这些services并进行负载均衡。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">现已推出多种 NGINX Ingress Controller实现。官方的 NGINX 实现拥有高性能，可随时投入生产，并且适合长期部署的特性。我们旨在为各个版本提供出色的稳定性，以及可在全企业范围内部署的丰富特性。我们免费为 NGINX Plus 用户提供全方位支持，并致力于为 NGINX Open Source 用户提供出色的稳定性和可支持性。</p> 
<hr> 
<h2 style="margin-left:0; margin-right:0; text-align:left">与1.7.0 版本比，NGINX Ingress Controller 1.8.0 有哪些新增特性？</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>集成 NGINX App Protect</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">随着更多企业竭力加速数字化转型，针对应用的攻击日益增加。更为复杂的新型漏洞攻击每天都在上演。与网络防火墙和杀毒解决方案不同，NGINX App Protect 作为一种智能 Web 应用防火墙 (WAF)，可以快速有效地缓解恶意攻击。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">NGINX Ingress Controller版本 1.8.0 嵌入了 NGINX App Protect，可支持您使用熟悉的 Kubernetes API 管理 App Protect 安全策略和配置。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">这款集成解决方案具有三大独特优势：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 保护应用边界 – 在架构设计合理的 Kubernetes 部署中，Ingress Controller是数据平面流量流向 Kubernetes 内所有运行服务的唯一入口点，这使其成为部署安全代理的理想位置。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 整合数据平面 – 将 WAF 嵌入到 Ingress Controller中消除了对独立 WAF 设备的需求。这可以降低复杂性、成本和故障点的数量。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 整合控制平面 – 使用 Kubernetes API 管理 WAF 配置有助于更轻松地实现 CI/CD 流程的自动化。NGINX Ingress Controller配置符合 Kubernetes 基于角色的访问控制 (RBAC) ，因此 WAF 配置可安全地委派给专门的 DevSecOps团队。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如欲了解详细概述，请查看相关博客使用 NGINX App Protect 保护 Kubernetes 中的应用。如欲了解在 NGINX Ingress Controller中如何对 NGINX App Protect 进行配置和故障排除的完整说明，请查看 Ingress Controller文档。如欲了解有关其他 App Protect 用例的信息，请查看 NGINX App Protect 文档。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">您必须同时订阅 NGINX Plus 和 NGINX App Protect 服务才能将 App Protect 内置到 NGINX Ingress Controller镜像中。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>使用Snippets和自定义模板扩展 NGINX Ingress 资源</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在此前的的版本中，您可以使用snippets和自定义模板将 NGINX 配置插入到标准 Kubernetes Ingress 资源中。snippets支持您将 NGINX以原生配置的方式部署到NGINX的大多数 配置上下文中。自定义模板支持您生成其他配置块（例如default server），并将其应用于 ConfigMaps。版本 1.8.0 将snippets和自定义模板的使用扩展到了 NGINX Ingress 资源、VirtualServer 和 VirtualServerRoute。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">snippets和自定义模板支持管理员为标准 Kubernetes Ingress 资源或 NGINX Ingress 资源中尚未发布的用例和功能实施配置。一个特别重要的用例便是当将 NGINX 代理的非 Kubernetes 应用迁移到 Kubernetes时，借助snippets和自定义模板，您可以继续使用 NGINX Ingress 资源中尚未发布的 NGINX 特性，例如高速缓存和速率限制。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此示例配置显示了如何在不同 NGINX 配置上下文中，通过采用不同设置的snippets配置高速缓存和速率限制：</p> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:#6f42c1">apiVersion:</span> <span style="color:#032f62">k8s.nginx.org/v1</span>
<span style="color:#6f42c1">kind:</span> <span style="color:#032f62">VirtualServer</span>
<span style="color:#6f42c1">metadata:</span>
  <span style="color:#6f42c1">name:</span> <span style="color:#032f62">cafe</span>
  <span style="color:#6f42c1">namespace:</span> <span style="color:#032f62">cafe</span>
<span style="color:#6f42c1">spec:</span>
  <span style="color:#6f42c1">http-snippets:</span> <span style="color:#032f62">|
    limit_req_zone $binary_remote_addr zone=mylimit:10m rate=1r/s;
    proxy_cache_path /tmp keys_zone=one:10m;
</span>  <span style="color:#6f42c1">host:</span> <span style="color:#032f62">cafe.example.com</span>
  <span style="color:#6f42c1">tls:</span>
    <span style="color:#6f42c1">secret:</span> <span style="color:#032f62">cafe-secret</span>
  <span style="color:#6f42c1">server-snippets:</span> <span style="color:#032f62">|
    limit_req zone=mylimit burst=20;
</span>  <span style="color:#6f42c1">upstreams:</span>
  <span style="color:#005cc5">-</span> <span style="color:#6f42c1">name:</span> <span style="color:#032f62">tea</span>
    <span style="color:#6f42c1">service:</span> <span style="color:#032f62">tea-svc</span>
    <span style="color:#6f42c1">port:</span> <span>80</span>
  <span style="color:#005cc5">-</span> <span style="color:#6f42c1">name:</span> <span style="color:#032f62">coffee</span>
    <span style="color:#6f42c1">service:</span> <span style="color:#032f62">coffee-svc</span>
    <span style="color:#6f42c1">port:</span> <span>80</span>
  <span style="color:#6f42c1">routes:</span>
  <span style="color:#005cc5">-</span> <span style="color:#6f42c1">path:</span> <span style="color:#032f62">/tea</span>
    <span style="color:#6f42c1">location-snippets:</span> <span style="color:#032f62">|
      proxy_cache one;
      proxy_cache_valid 200 10m;
</span>    <span style="color:#6f42c1">action:</span>
      <span style="color:#6f42c1">pass:</span> <span style="color:#032f62">tea</span>
  <span style="color:#005cc5">-</span> <span style="color:#6f42c1">path:</span> <span style="color:#032f62">/coffee</span>
    <span style="color:#6f42c1">action:</span>
      <span style="color:#6f42c1">pass:</span> <span style="color:#032f62">coffee</span></pre> 
  </div> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">对snippets和自定义模板进行慎重检查非常重要，因为无效的snippets或模板会阻止 NGINX 重新加载其配置。虽然在这种情况下，流量处理并不会中断（NGINX 继续在现有有效配置下运行），但是您还可以使用其他机制来提高稳定性：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 一个全局启用/禁用snippets的设置。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 通常只有管理员才能应用 ConfigMap，这是配置自定义模板的唯一机制。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>URI 重写以及修改请求和响应头</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">版本 1.8.0 在上游和下游连接中新增了 URI 重写以及修改请求和响应头的特性。这实质上通过添加一个过滤和修改层将终端用户与后端服务器实现解耦。现在，我们可以直接在 VirtualServer 和 VirtualServerRoute 资源中使用此功能，并且可以针对特定路径对其进行配置。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">URI 重写以及修改请求和响应头特性可支持您快速解决生产环境中无法预料的可靠性问题，而无需后端开发人员排除故障或重写代码。这反过来提高了 Kubernetes 中应用的可用性、安全性和弹性。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">典型用例包括：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• URI 重写 – 管理员可能希望在一个非应用代码所在的路径上发布应用。例如，您可以将应用向外定向到 /coffee URI，并通过 Ingress Controller将请求重定向到应用后端正在监听的根 (/) URI。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 高速缓存 – 应用开发人员并不能总是正确设置高速缓存header，或者根本不设置高速缓存header。管理员可以使用header修改来修补已部署应用中的header。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">您可以通过 proxy 操作将请求传递到上游，从而在配置 VirtualServer 或 VirtualServerRoute 中配置header修改和 URI 重写。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在此示例配置中，当 Ingress Controller代理对 /tea 路径的客户端请求时，它会在将请求转发到上游之前修改 Content-Type（内容-类型）请求头。它还将按reteaPath 字段中所指定的，把 /tea URI 重写为 /。在将服务器响应传递回客户端之前，Ingress Controller会添加一个新的 Access-Control-Allow-Origin header字段，并隐藏、忽略和传递其他几个header字段。</p> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:#6f42c1">apiVersion:</span> <span style="color:#032f62">k8s.nginx.org/v1</span> 
<span style="color:#6f42c1">kind:</span> <span style="color:#032f62">VirtualServer</span> 
<span style="color:#6f42c1">metadata:</span> 
  <span style="color:#6f42c1">name:</span> <span style="color:#032f62">cafe</span> 
<span style="color:#6f42c1">spec:</span> 
  <span style="color:#6f42c1">host:</span> <span style="color:#032f62">cafe.example.com</span> 
  <span style="color:#6f42c1">upstreams:</span> 
  <span style="color:#005cc5">-</span> <span style="color:#6f42c1">name:</span> <span style="color:#032f62">tea</span> 
    <span style="color:#6f42c1">service:</span> <span style="color:#032f62">tea-svc</span> 
    <span style="color:#6f42c1">port:</span> <span>80</span> 
  <span style="color:#005cc5">-</span> <span style="color:#6f42c1">name:</span> <span style="color:#032f62">coffee</span> 
    <span style="color:#6f42c1">service:</span> <span style="color:#032f62">coffee-svc</span> 
    <span style="color:#6f42c1">port:</span> <span>80</span> 
  <span style="color:#6f42c1">routes:</span> 
  <span style="color:#005cc5">-</span> <span style="color:#6f42c1">path:</span> <span style="color:#032f62">/tea</span> 
    <span style="color:#6f42c1">action:</span> 
      <span style="color:#6f42c1">proxy:</span> 
        <span style="color:#6f42c1">upstream:</span> <span style="color:#032f62">tea</span> 
        <span style="color:#6f42c1">requestHeaders:</span> 
          <span style="color:#6f42c1">pass:</span> <span style="color:#005cc5">true</span> 
          <span style="color:#6f42c1">set:</span>
          <span style="color:#005cc5">-</span> <span style="color:#6f42c1">name:</span> <span style="color:#032f62">Content-Type</span> 
            <span style="color:#6f42c1">value:</span> <span style="color:#032f62">application/json</span> 
        <span style="color:#6f42c1">responseHeaders:</span> 
          <span style="color:#6f42c1">add:</span> 
          <span style="color:#005cc5">-</span> <span style="color:#6f42c1">name:</span> <span style="color:#032f62">Access-Control-Allow-Origin</span>
            <span style="color:#6f42c1">value:</span> <span style="color:#032f62">"*"</span> 
            <span style="color:#6f42c1">always:</span> <span style="color:#005cc5">true</span> 
          <span style="color:#6f42c1">hide:</span> 
          <span style="color:#005cc5">-</span> <span style="color:#032f62">x-internal-version</span> 
          <span style="color:#6f42c1">ignore:</span> 
          <span style="color:#005cc5">-</span> <span style="color:#032f62">Expires</span> 
          <span style="color:#005cc5">-</span> <span style="color:#032f62">Set-Cookie</span> 
          <span style="color:#6f42c1">pass:</span> 
          <span style="color:#005cc5">-</span> <span style="color:#032f62">Server</span> 
        <span style="color:#6f42c1">rewritePath:</span> <span style="color:#032f62">/</span>
  <span style="color:#005cc5">-</span> <span style="color:#6f42c1">path:</span> <span style="color:#032f62">/coffee</span>
    <span style="color:#6f42c1">action:</span>
      <span style="color:#6f42c1">pass:</span> <span style="color:#032f62">coffee</span></pre> 
  </div> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此示例配置说明了如何在条件匹配时将header操作和 URI 重写嵌入到 action 块中，从而实现更复杂的流量处理：</p> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:#6f42c1">apiVersion:</span> <span style="color:#032f62">k8s.nginx.org/v1</span> 
<span style="color:#6f42c1">kind:</span> <span style="color:#032f62">VirtualServer</span> 
<span style="color:#6f42c1">metadata:</span> 
  <span style="color:#6f42c1">name:</span> <span style="color:#032f62">cafe</span> 
<span style="color:#6f42c1">spec:</span> 
  <span style="color:#6f42c1">host:</span> <span style="color:#032f62">cafe.example.com</span> 
  <span style="color:#6f42c1">upstreams:</span> 
  <span style="color:#005cc5">-</span> <span style="color:#6f42c1">name:</span> <span style="color:#032f62">tea</span> 
    <span style="color:#6f42c1">service:</span> <span style="color:#032f62">tea-svc</span> 
    <span style="color:#6f42c1">port:</span> <span>80</span> 
  <span style="color:#005cc5">-</span> <span style="color:#6f42c1">name:</span> <span style="color:#032f62">tea-post</span> 
    <span style="color:#6f42c1">service:</span> <span style="color:#032f62">tea-post-svc</span> 
    <span style="color:#6f42c1">port:</span> <span>80</span> 
  <span style="color:#6f42c1">routes:</span> 
  <span style="color:#005cc5">-</span> <span style="color:#6f42c1">path:</span> <span style="color:#032f62">/tea</span>
    <span style="color:#6f42c1">matches:</span> 
    <span style="color:#005cc5">-</span> <span style="color:#6f42c1">conditions:</span> 
      <span style="color:#005cc5">-</span> <span style="color:#6f42c1">variable:</span> <span style="color:#032f62">$request_method</span> 
        <span style="color:#6f42c1">value:</span> <span style="color:#032f62">POST</span>  
      <span style="color:#6f42c1">action:</span> 
        <span style="color:#6f42c1">proxy:</span> 
          <span style="color:#6f42c1">upstream:</span> <span style="color:#032f62">tea-post</span> 
          <span style="color:#6f42c1">requestHeaders:</span> 
            <span style="color:#6f42c1">pass:</span> <span style="color:#005cc5">true</span> 
            <span style="color:#6f42c1">set:</span> 
            <span style="color:#005cc5">-</span> <span style="color:#6f42c1">name:</span> <span style="color:#032f62">Content-Type</span> 
              <span style="color:#6f42c1">value:</span> <span style="color:#032f62">application/json</span> 
          <span style="color:#6f42c1">rewritePath:</span> <span style="color:#032f62">/</span>
    <span style="color:#6f42c1">action:</span>
      <span style="color:#6f42c1">pass:</span> <span style="color:#032f62">tea</span></pre> 
  </div> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>策略和 IP 地址访问控制列表</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">大多数组织都是多个团队合作交付应用。例如，NetOps 负责打开端口和过滤流量，SecOps 负责确保一致的安全状态，还有多个应用所有者为多个后端应用服务提供 Ingress 负载均衡策略。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">考虑到每个组织委派角色的方式不尽相同，NGINX Ingress 支持您以最大的灵活性定义各团队负责的特定配置部分，最后整合并执行。它还可支持多租户，同时最大程度地简化了管理员的委派工作。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">为了支持多租户，NGINX Ingress Controller版本 1.8.0 引入了policy策略，第一个受支持的策略类型是：基于 IP 地址的访问控制列表 (ACL)。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 通过将策略以及流量管理功能抽象成独立的K8S对象，不同团队可以在多个地方进行定义并部署。使用该方法配置 NGINX Ingress Controller更简单、更自然，并且带来了许多优势：类型安全、委派、多租户、封装以及简化的配置、可重用性和可靠性。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 借助基于 IP 地址的 ACL，您可以过滤网络流量并精确控制允许或拒绝访问特定 Ingress 资源的 IP 地址（或 IP 地址组，用 CIDR 表示法定义）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">注意：在版本 1.8.0 中，只能在 VirtualServer 资源中引用策略，其中策略应用于 server 上下文。在未来版本中，我们计划将策略支持扩展到 VirtualServerRoute 资源，其中策略应用于 location 上下文。我们还计划为速率限制等其他功能实施策略。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下图说明了策略的使用方式。左侧的 VirtualServer 资源引用了一个名为 webapp-policy 的策略，右侧的配置代码段分别使用这个名称定义了一个策略，用于过滤（允许或拒绝）来自 10.0.0.0/8 子网的连接。将该名称分配给两个策略意味着您可以使用 Kubernetes API 将对应策略应用于 VirtualServer，从而在不同策略之间进行切换。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>其他新增特性</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em><strong>Readiness探测</strong></em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在拥有较多 Ingress 资源（标准 Kubernetes、NGINX 或两者都有）的环境中，Pod 可能会在 NGINX 配置加载完之前上线，从而导致流量“走丢”（blackholed）。根据我们对生产级可靠性的承诺，版本 1.8.0 引入了 Kubernetes Readiness探测功能，旨在确保流量在 Ingress Controller准备好接受流量（即 NGINX 配置加载完成，且没有正在等待的重新加载）之前不会转发到特定 Pod。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><em>在 NGINX Ingress 资源和 Helm 图表中启用多种 Ingress Controller</em></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在以前的版本中，多种NGINX Ingress Controller实例可以共存于同一集群上，但只能通过使用标准 Kubernetes Ingress 资源中的 ​<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fkubernetes.io%2Fingress.class" target="_blank">​kubernetes.io/ingress.class​</a>​ 注释，指定目标 NGINX Ingress Controller部署。在版本 1.8.0 中，我们为 VirtualServer 和 VirtualServerRoute 资源添加了 ingressClassName 字段，以达到同样的目的。我们还更新了 Helm 图表，以支持部署多种 NGINX Ingress Controller。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em><strong>显示 VirtualServer 和 VirtualServerRoute 资源的状态</strong></em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">kubectl describe 命令的输出表示 Ingress Controller的配置是否已成功更新（在 Events 部分），并列出了其外部端点的 IP 地址和端口（在 Status 部分）。在版本 1.8.0 中，我们扩展了 VirtualServer 和 VirtualServerRoute 资源以返回此信息。对于 VirtualServerRoute 资源，status 部分还会命名父类 VirtualServer 资源。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">作为应用所有者，您可能会发现 VirtualServerRoute 资源的父类 VirtualServer 已被删除，从而导致应用无法访问。现在，您可以通过向相关的 VirtualServer 和 VirtualServerRoute 资源发出 kubectl describe 命令来解决该问题。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此示例命令显示已成功应用 cafe VirtualServer 的配置，在 Events 部分，Type 为 Normal，Reason 为AddedorUpdated。</p> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0">$ kubectl <span style="color:#d73a49">describe</span> vs cafe
...
<span style="color:#d73a49">Events</span>:
  <span style="color:#d73a49">Type</span>    Reason          Age   <span style="color:#d73a49">From</span>                      Message
  <span style="color:#6a737d">----    ------          ----  ----                      -------</span>
  <span style="color:#d73a49">Normal</span>  AddedOrUpdated  <span>16</span>s   nginx-ingress-controller  Configuration <span style="color:#d73a49">for</span> <span style="color:#d73a49">default</span>/cafe was added <span style="color:#d73a49">or</span> <span style="color:#d73a49">updated</span></pre> 
  </div> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此示例显示，cafe VirtualServer 的配置因无效而被拒绝，在 Events 部分，Type 为 warning，Reason 为 Rejected。原因是有两个都被命名为 tea 的上游。</p> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0">$ kubectl <span style="color:#d73a49">describe</span> vs cafe
...
<span style="color:#d73a49">Events</span>:
  <span style="color:#d73a49">Type</span>     Reason    Age   <span style="color:#d73a49">From</span>                      Message
  <span style="color:#6a737d">----     ------    ----  ----                      -------</span>
  <span style="color:#d73a49">Warning</span>  Rejected  <span>12</span>s   nginx-ingress-controller  VirtualServer <span style="color:#d73a49">default</span>/cafe 
<span style="color:#d73a49">is</span> invalid <span style="color:#d73a49">and</span> was rejected: spec.upstreams[<span>1</span>].name: <span style="color:#d73a49">Duplicate</span> <span style="color:#d73a49">value</span>: <span style="color:#032f62">"tea"</span></pre> 
  </div> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在输出的 Status 部分，Message 和 Reason 字段报告与 Events 部分相同的信息，以及每个外部端点的 IP 地址和端口。</p> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:#032f62">$</span> <span style="color:#032f62">kubectl</span> <span style="color:#032f62">describe</span> <span style="color:#032f62">vs</span> <span style="color:#032f62">cafe</span>
<span style="color:#032f62">...</span> 
<span style="color:#6f42c1">Status:</span>
  <span style="color:#6f42c1">External Endpoints:</span>
    <span style="color:#6f42c1">Ip:</span>        <span>12.13</span><span>.23</span><span>.123</span>
    <span style="color:#6f42c1">Ports:</span>     <span style="color:#032f62">[80,443]</span>
  <span style="color:#6f42c1">Message:  VirtualServer default/cafe is invalid and was rejected:</span> <span style="color:#032f62">spec.upstreams[1].name:</span> <span style="color:#6f42c1">Duplicate value:</span> <span style="color:#032f62">"tea"</span>
  <span style="color:#6f42c1">Reason:</span>   <span style="color:#032f62">Rejected</span></pre> 
  </div> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em><strong>更新NGINX Ingress Operator 用于Red Hat OpenShift</strong></em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• 策略 – 您现在可以利用 NGINX Ingress Controller Operator 按最终用户部署策略。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• App Protect 扩展 – 您可以使用Operator 来扩展NGINX Ingress Controller的App Protect 的能力，以便让所有NGINX ingress Controller实例都可以检查流量的安全性。</p> 
<hr> 
<h2 style="margin-left:0; margin-right:0; text-align:left">资源</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">有关版本 1.8.0 的完整变更日志，请查看版本说明。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如欲试用 NGINX Open Source NGINX Ingress Controller，您可以获取发布源代码，或从 DockerHub 下载预构建的容器。</p> 
<hr> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更多资源</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">想要更及时全面地获取NGINX相关的技术干货、互动问答、系列课程、活动资源？请前往​<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nginx.org.cn">​NGINX开源社区​</a>​官方网站 。</p>
                                        </div>
                                      
</div>
            