
---
title: 'eBay基于Istio的应用网关的探索和实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/0b643cc92bbee2e6fe66c109d426cd2f.png'
author: Dockone
comments: false
date: 2021-08-12 06:09:17
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/0b643cc92bbee2e6fe66c109d426cd2f.png'
---

<div>   
<br><h3>数据中心流量管理现状</h3>我们是有三个数据中心，每个数据中心有多个可用区，每个可用区有多个Kubernetes集群。现在流量接入数据中心主要是通过硬件负载均衡设备，也就是图中Web层的LB和APP层的LB，这些其实都是硬件负载均衡的设备对。目前，三个数据中心大概有2000多对这样的硬件负载均衡设备。我们内部应用相互间的调用主要是以南北向的流量为主，Web层会做流量的分发，将99%的流量转发到本地数据中心，1%的流量转发到远端的数据中心。数据中心的特征因我们是微服务的架构，所以它的VIP数量很多，同时会有公网和内网的VIP,并且在VIP上配置有少量L7规则，也就是应用间互相调用的防护规则。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/0b643cc92bbee2e6fe66c109d426cd2f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/0b643cc92bbee2e6fe66c109d426cd2f.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们期望实现的目标是可以基于Istio将这2000多对硬件负载均衡设备对全部替换掉。这种两层的架构其实我们已经用了很多年了，它最大的好处是假设某一个服务的应用在某一个数据中心全部宕机，这种情况下流量会自动切换到远端的数据中心，因为这边的健康检查会将这条链路断掉，如此客户端就不会因为缓存了这个VIP地址，造成客户端数据面的影响。因此在应用部署时，在每一个数据中心是有容量冗余的，就是我们可以端掉一个数据中心，其他两个数据中心的容量可足够支撑这个服务。<br>
<h4>规模化带来的挑战</h4><ul><li><br>异构应用  <br>
<ul><li>云业务，大数据，搜索服务</li><li>多种应用协议</li><li>灰度发布</li></ul></li><li><br>日益增长的安全需求：全链路TLS</li><li><br>可见性需求<br>
<ul><li>访问日志</li><li>Tracing</li></ul></li><li><br>数据中心规模：3主数据中心，20边缘数据中心，100+ Kubernetes集群</li><li><br>规模化运营Kubernetes集群<br>
<ul><li>总计100,000物理节点</li><li>单集群物理机节点规模高达 5,000</li></ul></li><li><br>业务服务全面容器化，单集群<br>
<ul><li>Pod实例可达 100,000</li><li>发布服务 5,000-10000</li></ul></li><li><br>单集群多环境支持<br>
<ul><li>功能测试、集成测试、压力测试共用单集群</li><li>不同环境需要彼此隔离</li></ul></li></ul><br>
<br>目前我们采用的是基于IPVS和Istio的网络云原生架构：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/feda8789401e6b247a60b8d84921669a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/feda8789401e6b247a60b8d84921669a.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
基于IPVS的L4 Service控制器：<br>
<ul><li>四层网关调度</li><li>VIP地址分配</li><li>不同应用配置独立网关VIP</li><li>配置IPIP Tunnel模式的IPVS规则</li><li>基于BGP VIP子网路由宣告</li><li>配置IngressGateway Tunnel接口</li><li>支持Direct Server Return（DSR）</li></ul><br>
<br>Istio作为应用网关控制器：<br>
<ul><li>管理应用L7规则</li><li>自动化生成eBay证书</li><li>管理和注入sidecar</li><li>网格内部请求mTLS</li></ul><br>
<br><h3>基于Istio的应用网关实践</h3><h4>Istio单集群多环境部署</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/1d4508fa7ed3db944c581b54e84909df.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/1d4508fa7ed3db944c581b54e84909df.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>非生产环境：Feature/LnP/Staging/StagingPCI</li><li>生产环境：Pre-Prod/Prod/PCI(Payment Card Industry)</li><li>单个Kubernetes集群部署多套Istiod，IngressGateway和L4集群</li><li>Cheery-pick 社区Pilot scoped namespaces PR</li><li>不同环境控制面数据面隔离</li></ul><br>
<br><h4>Istio集群证书管理</h4><strong>网关证书</strong><br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/3c59af15048c816c1e12d1022cb408d9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/3c59af15048c816c1e12d1022cb408d9.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>集成eBay CA，secret保存证书Ref</li><li>Istiod集成cert agent</li><li>SDS通过cert agent GRPC获取证书和key推送到IngressGateway</li></ul><br>
<br><strong>集群证书</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/9486d304c6ce17a5170b4b53f1e8383f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/9486d304c6ce17a5170b4b53f1e8383f.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>利用自签根证书为每个Istio集群签发中间证书</li><li>因安全方面的需求，需保证中间证书更新期间新旧证书同时可用</li></ul><br>
<br><h4>单网关全链路加密模式</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/f11486342ecfd04e94dc88d073b1c6a2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/f11486342ecfd04e94dc88d073b1c6a2.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>单网关全链路加密模式的架构图</em><br>
<ul><li><br>应用场景<br>
<ul><li>Feature/LnP/Staging Secure测试环境</li><li>全链路加密（E2E TLS）</li><li>可用性要求不高</li></ul></li><li><br>同时支持API Gateway和Mesh<br>
<ul><li>应用配置独立Gateway VIP</li><li>External访问API Gateway为Simple TLS</li><li>Mesh内部访问为mTLS</li><li>不同环境配置专有L4/L7集群</li></ul></li><li><br>软件防火墙集成（Sentinel）<br>
<ul><li>默认阻止所有访问</li><li>保护Ingress/Egress流量</li><li>保护进入Pod的流量</li></ul></li><li><br>模拟生产环境</li></ul><br>
<br><h4>多网关多集群部署</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/3ba5cba8346eda01a3cbd1909ab084c0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/3ba5cba8346eda01a3cbd1909ab084c0.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>Kubernetes集群联邦<br>
<ul><li>集群联邦APIServer作为用户访问kubernetes集群入口</li><li>所有Kubernetes集群注册至集群联邦</li></ul></li><li><br>可用区<br>
<ul><li>数据中心中具有独立供电制冷设备的故障域</li><li>同一可用区有较小网络延迟</li><li>同一可用区部署了多个Kubernetes集群</li></ul></li><li><br>多集群部署<br>
<ul><li>同一可用区设定一个网关集群</li><li>网关集群中部署Istio Primary</li><li>同一可用区的其他集群中部署Istio Remote</li><li>所有集群采用相同RootCA签发的中间证书</li></ul></li><li><br>东西南北流量统一管控<br>
<ul><li>同一可用区的服务调用基于Sidecar</li><li>跨可用区的服务调用基于Istio Gateway</li></ul></li></ul><br>
<br><h4>Istio Primary-Remote压力测试</h4>Istio控制面主要考虑两个配置推送到mesh的收敛时间（convergence time）：<br><br>
<ul><li>Gateway XDS</li><li>Sidecar EDS</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/c5924f1451e71155656063cb393d53e7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/c5924f1451e71155656063cb393d53e7.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/7c7b5df5b3262a836021f351b3b8accc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/7c7b5df5b3262a836021f351b3b8accc.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
结论：<br>
<ul><li><br>单个Istiod 32 CPU/10G内存可以支持：<br>
<ul><li>32个Ingress Pods</li><li>2000个sidecar</li></ul></li><li><br>收敛时间小于5秒能够支持的规模：<br>
<ul><li>2000 Kubernetes Service（5个端口）</li><li>其中同时有100个Endpoint地址发生变更</li></ul></li><li><br>如果Kubernetes Service数量少于2000，为了实现收敛时间小于5s，Istiod Pod的数量可以通过如下公式计算：<br>
<br>Istio Number = gateway number / 32 + sidecar number / 2000  </li></ul><br>
<br><h4>应用高可用接入方案-多集群1层</h4>这里的一层是指 VIP的数量：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/7211232627628c983ccdbe380e670420.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/7211232627628c983ccdbe380e670420.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
流量管理：<br>
<ul><li>GTM（智能DNS）配置多个VIP，负责健康检查</li><li>GTM（智能DNS）配置不同数据中心流量权重</li><li>L4 IPVS 为流量入口</li><li>没有跨数据中心流量</li><li>应用数据面为网关Envoy到Sidecar Envoy</li></ul><br>
<br>故障容灾：<br>
<ul><li>GTM监控VIP状态，自动mark down故障VIP</li><li>Istio网关宕机会影响客户端DNS缓存</li><li>单集群应用后端Pod整体宕机会造成数据面影响</li></ul><br>
<br><h4>应用高可用接入方案-多集群2层</h4>方案一：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/639aad998d737eef7b08d79dbc3ba0f3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/639aad998d737eef7b08d79dbc3ba0f3.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
流量管理：<br>
<ul><li>L4 IPVS为流量入口</li><li>本集群流量从Gateway直连后端服务器</li><li>跨集群流量经过远端IPVS VIP转发</li><li>ServiceEntry同时选择Pod和VIP</li><li>定义基于Locality的流量转发规则</li><li>同一数据中心流量权重99%，跨数据中心1%</li></ul><br>
<br>故障容灾：<br>
<ul><li>单集群应用后端Pod整体宕机不会造成数据面影响</li><li>Istio网关宕机，智能DNS停止返回该VIP</li></ul><br>
<br>因此我们又提出了另外一种两层的架构，这种两层的架构是我们现在比较倾向于选择的架构，它虽然也有两层VIP，但实际上它只有一个IP，只是我们开了两个端口。<br>
<br>方案二：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/cec170330b751476293d734568872a29.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/cec170330b751476293d734568872a29.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
流量管理：<br>
<ul><li>两层VIP，适配现有模型</li><li>ServiceEntry实现跨数据中心流量</li><li>利用Weighted HTTPRouteDestination,本数据中心98%，远端各1%</li><li>所有流量都经过Istio</li></ul><br>
<br>故障容灾：<br>
<ul><li>单集群应用后端Pod整体宕机不会造成数据面影响</li><li>Istio网关宕机会受客户端DNS缓存影响</li></ul><br>
<br><h4>应用高可用接入方案-数据面</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/dd2ff6aa204cf41592e3fdba8e39560f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/dd2ff6aa204cf41592e3fdba8e39560f.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>用户请求通过L4(IPVS)转发到IngressGateway</li><li>TLS PAASTHROUGH将请求路由至weighted cluster</li><li>Weighted cluster的Endpoints为本地和远端的网关地址</li><li>请求转发至本集群:TLS握手发生在client和gateway pod</li><li>请求需经过2次TLS</li><li>IngressGateway将请求响应通过Direct Server Return返回客户端</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/f26a1e3f3beec308a22e33618450660b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/f26a1e3f3beec308a22e33618450660b.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>TLS握手发生在local gateway和gateway pod</li><li>Ingress Gateway Pod需配置eBay Root CA</li><li>请求需经过2次TLS</li><li>正常接收1%流量，本集群后端服务整体宕机接收100%流量</li></ul><br>
<br>适配服务间调用（L7转发规则）：<br>
<ul><li>99%请求走Mesh东西向流量</li><li>1%请求经Gateway跨Mesh</li><li>VirtualService配置weighted Destination</li></ul><br>
<br><h4>统一流量模型 - AccessPoint</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/bfb44ef32c60bc70cb183ba14058a995.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/bfb44ef32c60bc70cb183ba14058a995.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>基于Istio网关的feature测试开发环境</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/8cd4e491227fca637e928182bef5764d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/8cd4e491227fca637e928182bef5764d.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Feature测试环境规模：<br>
<ul><li>单个测试环境包含一个Pod和若干个CNAME</li><li>Feature测试环境共享一个网关VIP</li><li>4000+个Pod/VS/GW/Service以及5k个CNAME</li><li>网关配置Wildcard证书</li></ul><br>
<br>VirtualService指定转发规则：<br>
<ul><li>Host: foo.example.com</li><li>Destination：foo-service</li></ul><br>
<br>Lesson Learn：<br>
<ul><li>Istio 1.3，1.7k个Pod, Pilot OOM</li><li>集群整体discover，配置过多</li><li>Listener缺失，CDS推送太慢</li><li>Gateway merge耗时，3k GW耗时近3k秒</li></ul><br>
<br>因此这套方案后来我们没有使用，用另外一套方案去替换了。但是也有一个很大的教训，就是说一个merge的scalability不可能无限大，因此我们一是要做基于环境的隔离，二是要对merge的规模进行控制，这样才能保证整个merge的稳定性和可用性。<br>
<h4>基于Istio网关的集中日志系统CAL</h4><strong>CAL日志系统集成Mesh</strong><br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/d48eb5e2bdf9698fb91b50eec3266877.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/d48eb5e2bdf9698fb91b50eec3266877.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>不同网格同时部署应用以及日志服务器</li><li>同时注入sidecar到应用端以及日志系统服务端</li><li>网格内部mTLS实现日志脱敏</li><li>南北流量转成东西流量</li></ul><br>
<br><h4>全链路加密存储服务-NuObject</h4>NuObject是我们目前做的一个新项目，用来替换Swift, 前期我们也做了很多压力测试，下图为压力测试环境与结果：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/7e7e6a5730ed2905ced886db39d20485.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/7e7e6a5730ed2905ced886db39d20485.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>压力测试环境</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/f8868f825fbc3a8197b89fcfc05135e6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/f8868f825fbc3a8197b89fcfc05135e6.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
高吞吐压力测试：<br>
<ul><li>Gateway达到30Gb/s</li><li>Backend BM达到40Gb/s</li><li>Jumbo frame，9000 bytes MTU</li><li>Sidecar内存增加到3GB</li><li>Envoy worker增加到20</li></ul><br>
<br>高安全性存储服务：<br>
<ul><li>注入Sidecar到后端服务</li><li>网关配置Simple TLS</li><li>网格内部mTLS</li><li>集成软件防火墙</li></ul><br>
<br><h4>Managed Stack全面集成Mesh</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210811/894740410e2339670a8aa41569929fda.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210811/894740410e2339670a8aa41569929fda.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Managed Stack是使用eBay框架的应用，包括Java，Java Web，Batch以及NodeJS应用。<br>
<ul><li>生产环境应用数量超过4000</li><li>个别应用部署后端服务器超过3000</li><li>生产环境Pod总数超180000</li><li>TLS/限速/授权与框架解耦</li><li>Fat container全面转向Native以及Mesh</li></ul><br>
<br><h3>Istio社区未解决的问题</h3><ul><li><br>端口协议冲突  <br>
<ul><li>不支持privilege端口<1024</li><li>同一网关端口不能同时支持TCP/HTTPS</li><li>解决方案：分配不通gateway service target port</li></ul></li><li><br>单点从外部访问mTLS Mesh机器<br>
<ul><li>解决方案：利用Subset Load Balancing，EnvoyFilter从URL解析Pod IP并转发</li></ul></li><li><br>Envoy readiness probe<br>
<ul><li>无法确保数据面通、证书配置好</li><li>解决方案：Readiness gate/Envoy active healthcheck</li></ul></li><li><br>Init Container inbound/outbound被block，社区issue<br>
<ul><li>解决方案：添加anntation traffic.sidecar.istio.io/excludeInboundPorts/用1337运行Init Container</li></ul></li><li><br>控制面性能问题<br>
<ul><li>解决方案：sharding，将mesh切片，限制单个Mesh Gateway/Service/Pod数量</li></ul></li></ul><br>
<br><h3>未来展望</h3><ul><li>全面替换硬件负载均衡设备  </li><li>南北流量接入软件应用网关</li><li>构建基于Mesh流量管理</li><li>全站应用全面转向Cloud Native/Service Mesh</li><li>数据中心内部南北流量转成东西流量</li><li>数据平面加速Cilium</li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/IA5gQFzRQDMnDsXl_5tg0w" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/IA5gQFzRQDMnDsXl_5tg0w</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            