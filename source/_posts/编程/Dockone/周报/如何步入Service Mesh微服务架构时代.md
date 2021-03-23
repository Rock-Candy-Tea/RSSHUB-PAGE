
---
title: '如何步入Service Mesh微服务架构时代'
categories: 
 - 编程
 - Dockone
 - — 周报
headimg: 'http://dockone.io/uploads/article/20210319/8a04d3df804dd1c8ef66863324906b4d.png'
author: Dockone
comments: false
date: 2021-03-23 12:52:19
thumbnail: 'http://dockone.io/uploads/article/20210319/8a04d3df804dd1c8ef66863324906b4d.png'
---

<div>   
<br>今天要和大家分享的是关于新一代微服务架构——Service Mesh的具体玩法！在微服务架构盛行的今天，作为一名互联网技术从业人员，对于微服务的概念相信大家都已经耳熟能详了！而至于像Spring Cloud这样的微服务框架，因为大部分互联网公司都在此基础上构建过第一代微服务体系，所以对于做Java的同学来说，Spring Cloud微服务体系应该是非常熟悉了！几年前我也写过一篇介绍我当时所在公司——摩拜单车基于Spring Cloud框架构建微服务体系的文章，感兴趣的可以戳下看看《<a href="http://dockone.io/article/8606">基于Spring Cloud的微服务架构演变史</a>》。<br>
<br>这里并不是说其他语言栈就没有构建微服务体系的框架，例如Go语言也有像Go-Micro这样的微服务框架，只不过目前除了像头条这样重度使用Go语言的公司外，其他绝大多数互联网公司的服务端语言依然还是Java的天下！所以对于目前大部分已经或打算采用微服务架构的公司来说，Spring Cloud框架依然是它们的首选！但如果我说，这套体系发展到今天已经快过时了，你会不会觉得我是在瞎掰呢？因为毕竟咱们现在天天玩的微服务还都是Spring Cloud这一套啊！<br>
<br>难道像Spring Cloud GateWay、Zuul、Eureka、Consul、Nacos、Feign/Ribbon、Hystrix、Sentinel、Spring Cloud Config、Apollo...，这些涵盖了微服务体系——服务注册与发现、限流、熔断降级、负载均衡、服务配置等服务治理各个方面的牛逼开发框架或服务组件们都快要过时了吗？<br>
<br>虽然这很难让人接受，毕竟这些技术才刚刚捂热！但在下一代微服务架构Service Mesh 面前，它们中的绝大部分组件确实是快要过时了，倒不是说这些开源组件在技术上不牛逼或者没有深入学习研究的价值了，而是它们所面向的微服务体系结构在设计理念上与Service Mesh已经存在代差，这种差距夸张点说就像歼-20与歼-10的差别。这听起来可能有点耸人听闻，但从目前微服务技术发展趋势和实践上看，这就是历史潮流！接下来我将从理论和实践层面对此进行分析和演示！<br>
<h3>为什么要进入Service Mesh时代</h3>前面我略微夸张的说到，以Spring Cloud为代表的微服务体系相比Service Mesh而言已经存在技术代差，那凭什么这么说呢？接下来，我们回顾下使用Spring Cloud构建微服务体系的大致技术流程！<br>
<br>要构建微服务体系，首先我们需要独立部署一款实现服务注册/发现功能的组件服务，目前可供选择的主流方案一般有Eureka、Consul、Nacos等，搞定服务注册/发现后，我们编写一个Java微服务，此时为了将该服务注册到服务注册中心，一般会引入Spring Cloud提供的支持对应注册中心接入的SDK，并在应用入口类中通过@EnableDiscoveryClient注解的方式标注，之后SDK中的逻辑就会在应用启动时执行服务注册动作，并提供给注册中心相应地探测接口，以此实现微服务与服务注册中心之间的连接。以此类推，我们可以通过这种方式将一组微服务都注册到服务注册中心！<br>
<br>而如果服务之间要互相调用怎么办呢？一般我们会通过编写FeignClient接口来实现微服务之间的调用，而其底层的逻辑则是通过Feign所集成的Ribbon组件去注册中心中获取目标服务的服务地址列表，之后Ribbon根据服务地址列表进行负载均衡调用。至于服务与注册中心之间如何保证连接有效性，则依赖于服务注册中心与其SDK之间的协作机制。<br>
<br>而高级一点，服务之间的调用除了实现负载均衡，还要实现熔断限流、那么此时可以通过部署服务网关组件（例如Zuul/Spring Cloud GateWay）来实现微服务入口的熔断限流、内部服务之间的限流熔断则通过集成Hystrix或Sentinel组件，以客户端本地配置或远程配置中心的方式来实现。<br>
<br>上述过程基本就是我们使用Spring Cloud构建微服务体系的大致过程了！如果仔细思考下这个过程，我们会发现在该微服务体系的构造过程中，与服务治理相关的大部分逻辑都是以SDK的方式耦合在具体的微服务应用之中！服务注册需要引入SDK、服务调用需要引入SDK、服务熔断限流也需要SDK；除此之外，为了保证这套体系的正常运行，我们还需要额外维护服务注册中心、服务网关这样的基础服务。这样的结构会导致什么弊端呢？具体有以下几点：<br>
<h4>框架/SDK太多，后续升级维护困难</h4>在这套体系中，与服务治理相关的逻辑都是以SDK代码依赖的方式嵌入在微服务之中，如果某天我们想升级下服务注册中心的SDK版本，或者熔断限流组件Hystrix或Sentinel的版本，那么需要升级改造的微服务可能会是成百上千，且由于这些组件都与业务应用绑定在一起，在升级的过程中会不会影响业务稳定，这都是需要谨慎对待的事情，所以对SDK的升级难度可想而知的！<br>
<h4>多语言微服务SDK维护成本高</h4>试想下如果构建的微服务体系，也要支持像Go、Python或者其他语言编写的微服务的话，那么上述这些微服务治理相关的SDK是不是得单独再维护几套呢？所以在这种体系结构中，对多语言微服务的支持就成了一个问题！<br>
<h4>服务治理策略难以统一控制</h4>基于该套体系构建的微服务体系，在对像熔断、限流、负载均衡等服务治理相关的策略管理上，都是比较分散的，可能有人会写到自己的本地配置文件，有人会硬编码到代码逻辑中，也可能有人会将其配置到远程配置中心，总之对于服务治理策略逻辑都是由对应的开发人员自己控制，这样就很难形成统一的控制体系！<br>
<h4>服务治理逻辑嵌入业务应用，占有业务服务资源</h4>在这套微服务体系中，服务治理相关的逻辑都是在微服务应用进程中寄生运行的，这多少会占有宝贵的业务服务器资源，影响应用性能的发挥！<br>
<h4>额外的服务治理组件的维护成本</h4>无论是服务注册中心、还是服务网关，这些除了微服务应用本身之外服务治理组件，都需要我们以中间件基础服务的方式进行维护，需要额外的人力、额外的服务器成本！<br>
<br>以上就是以Spring Cloud为代表的传统微服务体系的弊端，如果我说在Service Mesh体系下，以上几点都不再是问题，甚至都不需要研发人员再进行任何关注！我们只需要写一个普通的Spring Boot服务，也不需要引入服务注册SDK、熔断限流SDK组件，总之你写一个普普通通的服务，就能实现像之前Spring Cloud微服务体系所能支持的大部分服务治理功能，你会相信吗？你会不会觉得这跟之前写单体应用没啥差别了呢？<br>
<br>不管你怎么想，这些就是Service Mesh要干的事情！Service Mesh的目标就是要将微服务治理体系下沉为一套与业务无关的基础设施。从这个角度看，如果咱们不认真学习下Service Mesh，那么以后将变得越来越低智，因为Spring Cloud好歹还能让我们感知下微服务的存在，而在Service Mesh中，微服务治理体系作为基础设施的一部分，对普通研发人员将越来越透明！<br>
<h4>Service Mesh的解决方案是什么</h4>在前面我们说到，Service Mesh的目标是要将微服务治理体系下沉为与业务无关的基础设施。这句话怎么理解呢？实际上Service Mesh微服务治理技术的诞生也不是凭空产生的，而是在以Kubernetes为代表的容器编排技术逐步成为软件运行主流基础环境的背景下，以及以Spring Cloud框架为代表的传统微服务技术体系弊端逐步显现的情况下技术自然迭代发展的结果。总之，就是有点万事具备，只欠东风的感觉！<br>
<br>所以，我们看到目前落地的Service Mesh方案中大多都是与Kubernetes深度结合的方案，例如最受瞩目的Istio！接下来我们具体看看在Service Mesh中微服务治理的核心逻辑是怎么实现的（以Istio+Envoy为例）！<br>
<br>要理解在Service Mesh中的微服务治理逻辑的具体实现，就不得不上一张关于服务网格概念很经典但刚开始看着又很难理解的图，如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/8a04d3df804dd1c8ef66863324906b4d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/8a04d3df804dd1c8ef66863324906b4d.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果你之前大致了解过Service Mesh的概念，那么这张图相信你一定见过。其中绿色的正方形表示正常部署的微服务，而蓝色的正方形表示一个网络代理，也就是大家通常所说的SideCar。在Service Mesh架构下，每部署一个微服务，都需要部署一个与之相对应的代理服务，所有与微服务本身的交互都通过SideCar代理，而SideCar之间会形成一张形似网格的交互链路，这就是服务网格名称的来由！<br>
<br>在Service Mesh中，当我们将一个服务部署在Kubernetes之后，安装在Kubernetes中的Service Mesh组件（例如Istio）就会自动在该微服务的同一个Pod之中启动一个与之对应的代理进程（例如istio-proxy），这个保姆式的代理进程会代替微服务本身去实现原先在Spring Cloud体系中需要微服务自身完成的服务注册、负载均衡、熔断限流等微服务治理功能。并且，这些代理进程并不是孤军奋战，而是会通过像xDS协议（Service Mesh中数据面与控制面通信的通用协议）与Service Mesh控制组件保持连接。<br>
<br>这也就引出了Service Mesh架构中关键的两个概念：控制面与数据面。前面我们所示的Sidecar（例如istio-proxy，实际上是envoy）就是数据面，与微服务治理逻辑相关的信息都存储在数据面中，而控制面则是Service Mesh的中心控制组件（例如Istio中的Pilot组件），控制面可以通过xDS协议（具体又分为LDS、CDS……）向数据面下发各种服务治理相关的规则，例如限流规则、路由规则、服务节点更新信息等等。<br>
<br>这种设计方式就是Service Mesh最核心的设计逻辑——通过Sidecar的方式代理微服务进行服务治理逻辑（数据面），通过控制面感知外界环境的变化并通过xDS协议支持各种微服务治理策略规则的集中管理和下发，而这里的控制面和数据面都会被融合进像Kubernetes这样的基础架构环境中，对于普通微服务的开发，研发人员要做的只是将一个应用以编排的方式部署进k8s集群即可！而所有与微服务治理相关的逻辑都由代理数据面与控制面协作完成。<br>
<br>这里我们以Service Mesh最著名的开源方案Istio的架构图来解释上面所说的逻辑，具体如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/d8e34b9afed2a15c0e79f989942e914d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/d8e34b9afed2a15c0e79f989942e914d.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
其中服务注册发现可以直接利用Kubernetes的内部发现机制，通过监听Kubernetes Pod的变化来实现，具体示意图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/be1193a810c1f90203106eb27996971e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/be1193a810c1f90203106eb27996971e.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
而微服务治理相关的逻辑，以Istio为例，流程大致是这样的：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/f8074568faf5071b8857223b3a197497.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/f8074568faf5071b8857223b3a197497.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
管理员通过Pilot配置治理规则，并通过xDS协议向Envoy下发治理规则，而Envoy从Pilot获取微服务治理规则后，就可以在流量访问的时候按照规则执行相应的限流、路由等微服务治理逻辑了！<br>
<h3>Istio+Envoy的Service Mesh架构玩法</h3>前面我们从原理层面大致介绍了Service Mesh微服务架构的核心概念及流程逻辑，如果你玩过Service Mesh架构，那么理解起来是很容易的！但是如果没有具体实践过，特别是如果对Kubernetes没有基本的了解，那么上面的概念可能也并不好理解，例如你可能会竭力地想象"我到底应该怎么部署那个所谓的Sidecar代理？"，"在Service Mesh架构下怎么去开发服务？"等这样的问题！<br>
<br>而如果我写到这里不写了，那么这篇文章也只是与大部分介绍过Service Mesh的文章一样，要么就是各种高大上不接地气的原理介绍，要么就是翻过来覆过去的概念介绍，或者好不容易找到一篇带有示例的文章，但大多数也是基于Istio官方Demo的演示！<br>
<br>而对于开发过Spring Cloud微服务应用的同学来说，其实并不是很好理解！所以接下来的玩法实践，我将以最接近实际开发场景的方式、站在一个曾经使用Spring Cloud框架开发过微服务的研发人员角度，来整体介绍如何用平常工作中所使用的Java流行框架(如Spring Boot)来开发基于Service Mesh体系的微服务应用！<br>
<br>具体过程及步骤如下：<br>
<h4>Kubernetes环境准备及Istio安装</h4>要玩转Service Mesh微服务架构，基本的前提是需要一个功能完整的Kubernetes环境，这里我所使用的Kubernetes环境是在开发本上安装一个Linux虚拟机并在其之上部署一个只有Master节点的Kubernetes单节点集群，另外由于Istio对Kubernetes的版本是有要求的，这里所使用的Kubernetes版本是v1.18.6。<br>
<br>这里我先假设你已经搞定了Kubernetes环境，接下来开始安装Istio，选择的版本是istio-1.8.4，具体步骤如下：<br>
<br>1)、下载Istio发布包<br>
<br>由于官方提供的下载脚本执行速度比较慢，可以直接在GitHub找到相应的Istio发布版本后通过wget命令将其下载至主机指定目录（能正常连接Kubernetes集群）：<br>
<pre class="prettyprint">wget https://github.com/istio/istio/releases/download/1.8.4/istio-1.8.4-linux-amd64.tar.gz<br>
</pre><br>
下载成功后，解压安装包：<br>
<pre class="prettyprint">tar -zxvf istio-1.8.4-linux-amd64.tar.gz<br>
</pre><br>
进入解压安装包目录：<br>
<pre class="prettyprint">cd istio-1.8.4/<br>
</pre><br>
2)、将istioctl客户端添加到系统可执行路径<br>
<br>在具体安装Istio时需要使用istioctl命令，因此需要先将该命令加入系统可执行路径，命令如下：<br>
<pre class="prettyprint">export PATH=$PWD/bin:$PATH<br>
</pre><br>
3)、执行安装istio命令<br>
<br>这里使用istioctl命令执行安装命令，具体如下：<br>
<pre class="prettyprint">istioctl install --set profile=demo<br>
</pre><br>
这里“--set profile=demo”表示安装一个istio测试环境！成功安装后的信息输出如下：<br>
<pre class="prettyprint">Detected that your cluster does not support third party JWT authentication. Falling back to less secure first party JWT. See https://istio.io/v1.8/docs/ops/best-practices/security/#configure-third-party-service-account-tokens for details.<br>
This will install the Istio 1.8.4 demo profile with ["Istio core" "Istiod" "Ingress gateways" "Egress gateways"] components into the cluster. Proceed? (y/N) Y<br>
✔ Istio core installed                                                                                                                                                                                      <br>
✔ Istiod installed                                                                                                                                                                                          <br>
✔ Ingress gateways installed                                                                                                                                                                                <br>
✔ Egress gateways installed                                                                                                                                                                                 <br>
✔ Installation complete  <br>
</pre><br>
如果安装成功，则可以通过kubectl命令查看Istio相关组件是否已经安装在Kubernetes环境之中，命令如下：<br>
<pre class="prettyprint">kubectl get svc -n istio-system<br>
NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                                                                      AGE<br>
istio-egressgateway    ClusterIP      10.101.134.226   <none>        80/TCP,443/TCP,15443/TCP                                                     8m12s<br>
istio-ingressgateway   LoadBalancer   10.96.167.106    <pending>     15021:31076/TCP,80:31032/TCP,443:31438/TCP,31400:32751/TCP,15443:31411/TCP   8m11s<br>
istiod                 ClusterIP      10.102.112.111   <none>        15010/TCP,15012/TCP,443/TCP,15014/TCP  <br>
</pre><br>
此时可以看到Istio的核心组件istiod，以及入口网关Ingress Gateway、出口网关Egress Gateway已经成功以Service资源的方式运行在了Kubernetes集群之中！<br>
<br>4)、Kubernetes默认命名空间开启自动注入Envoy Sidecar<br>
<br>这是一个关键的步骤，如果我们的微服务应用未来是默认部署在Kubernetes的default命名空间，那么在安装Istio是需要开启该空间的Sidecar自动注入功能。这是我们前面提到每启动一个微服务应用，Kubernetes就会默认在相同的Pod中自动启动一个代理进程的关键设置！<br>
<br>具体命令如下：<br>
<pre class="prettyprint">$ kubectl label namespace default istio-injection=enabled<br>
namespace/default labeled<br>
</pre><br>
5)、Istio可观测性部署<br>
<br>Kiali是一个基于服务网格的Istio管理控制台，它提供了一些数据仪表盘和可观测能力，同时也可以让我们去操作网格的配置。使用如下方式快速部署一个用于演示的Kiali，命令如下：<br>
<pre class="prettyprint">$ kubectl apply -f samples/addons<br>
serviceaccount/grafana created<br>
configmap/grafana created<br>
service/grafana created<br>
deployment.apps/grafana created<br>
configmap/istio-grafana-dashboards created<br>
configmap/istio-services-grafana-dashboards created<br>
deployment.apps/jaeger created<br>
service/tracing created<br>
service/zipkin created<br>
service/jaeger-collector created<br>
Warning: apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition<br>
customresourcedefinition.apiextensions.k8s.io/monitoringdashboards.monitoring.kiali.io created<br>
serviceaccount/kiali created<br>
configmap/kiali created<br>
clusterrole.rbac.authorization.k8s.io/kiali-viewer created<br>
clusterrole.rbac.authorization.k8s.io/kiali created<br>
clusterrolebinding.rbac.authorization.k8s.io/kiali created<br>
role.rbac.authorization.k8s.io/kiali-controlplane created<br>
rolebinding.rbac.authorization.k8s.io/kiali-controlplane created<br>
service/kiali created<br>
deployment.apps/kiali created<br>
serviceaccount/prometheus created<br>
configmap/prometheus created<br>
clusterrole.rbac.authorization.k8s.io/prometheus created<br>
clusterrolebinding.rbac.authorization.k8s.io/prometheus created<br>
service/prometheus created<br>
deployment.apps/prometheus created<br>
....<br>
</pre><br>
其中具体会安装部署Promethues、Grafana、Zipkin等指标及链路采集服务！因为安装的组件比较多，也比较耗费资源，如果集群资源不是很充足，可能会出现启动比较慢的情况。如果正常部署成功，可以查看Pod状态，命令如下：<br>
<pre class="prettyprint"># kubectl get pod -n istio-system -o wide<br>
NAME                                    READY   STATUS    RESTARTS   AGE   IP           NODE         NOMINATED NODE   READINESS GATES<br>
grafana-94f5bf75b-4mkcn                 1/1     Running   1          30h   10.32.0.11   kubernetes   <none>           <none><br>
istio-egressgateway-7f79bc776-w6rqn     1/1     Running   3          30h   10.32.0.3    kubernetes   <none>           <none><br>
istio-ingressgateway-74ccb8977c-gnhbb   1/1     Running   2          30h   10.32.0.8    kubernetes   <none>           <none><br>
istiod-5d4dbbb8fc-lhgsj                 1/1     Running   2          30h   10.32.0.5    kubernetes   <none>           <none><br>
jaeger-5c7675974-4ch8v                  1/1     Running   3          30h   10.32.0.13   kubernetes   <none>           <none><br>
kiali-667b888c56-8xm6r                  1/1     Running   3          30h   10.32.0.6    kubernetes   <none>           <none><br>
prometheus-7d76687994-bhsmj             2/2     Running   7          30h   10.32.0.14   kubernetes   <none>           <none><br>
</pre><br>
由于前面安装Istio时，我们并没有在istio-system空间开启自动注入Sidecar（其label istio-injection=disabled），这里为了在Kubernetes集群之外正常访问Kiali、Prometheus、Granfana、Tracing的控制面板（它们共同组成了Service Mesh的可观测体系），可以通过nodePort的方式对外暴露端口。<br>
<br>Kiali的NodePort访问操作方式：<br>
<br>将部署的Kiali的Service文件导出到主机的某个目录，例如：<br>
<pre class="prettyprint">kubectl get svc -n istio-system kiali -o yaml > kiali-nodeport.yaml<br>
</pre><br>
之后编辑导出的文件，删除metadata下的annotation、resourceVersion、selfFlink、uid等信息；并修改下spec下的type类型值，将ClusterIP修改为NodePort，并指定nodePort端口信息；同时删除status状态字段即可。具体如下：<br>
<pre class="prettyprint">spec:<br>
...<br>
ports:<br>
- name: http<br>
nodePort: 31001<br>
...<br>
type: NodePort<br>
</pre><br>
编辑完成后执行执行命令：<br>
<pre class="prettyprint">kubectl apply -f kiali-nodeport.yaml<br>
</pre><br>
之后查看服务端口，命令如下：<br>
<pre class="prettyprint">kubectl get svc -n istio-system kiali<br>
NAME    TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)                          AGE<br>
kiali   NodePort   10.100.214.196   <none>        20001:31001/TCP,9090:30995/TCP   41h<br>
</pre><br>
此时通过Kubernetes的集群外部IP+31001端口就能访问Kiali控制面板了，效果如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/9e227fffa71f1c2c88a05af9c5452d91.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/9e227fffa71f1c2c88a05af9c5452d91.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
与Kiali的操作方式类似，我们也可以通过获取修改部署的Promethues、Granfana、Tracing、Zipkin等服务的发布文件，通过设置NodePort端口，从而在Kubernetes集群外部进行可观测界面的访问！例如：<br>
<pre class="prettyprint">#Prometheus<br>
kubectl get svc -n istio-system prometheus -o  yaml > prometheus-nodeport.yaml<br>
kubectl apply -f prometheus-nodeport.yaml <br>
<br>
#Granfana<br>
kubectl get svc -n istio-system grafana -o yaml > grafana-nodeport.yaml<br>
kubectl apply -f grafana-nodeport.yaml<br>
<br>
#Jaeger(分布式链路)<br>
kubectl get svc -n istio-system tracing -o yaml > tracing-nodeport.yaml<br>
kubectl apply -f tracing-nodeport.yaml<br>
...<br>
</pre><br>
其中Granfana的访问效果示意图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/41f4e5aea685b9f480a017dd517fa8b4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/41f4e5aea685b9f480a017dd517fa8b4.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Spring Boot微服务开发</h4>经过前面的步骤，我们已经从基础架构环境的角度完成了基于Istio的Service Mesh微服务体系的构建！如果类比之前基于Spring Cloud框架的微服务开发体验，那么在Istio体系下应该如何进行微服务应用的开发呢？<br>
<br>接下来我们通过一个实际的应用示例来演示，如何开发基于Istio的Service Mesh微服务应用，服务链路如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/6363d4ec409a81608aa0bbc041f4b41a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/6363d4ec409a81608aa0bbc041f4b41a.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如上所示链路，具体说明如下：<br>
<ol><li>为了完整演示在Service Mesh架构下微服务的研发过程，这里我们定义3个微服务，其中micro-api服务是面向外部客户端接入的Api服务提供Http协议访问；</li><li>而micro-api与micro-order之间则基于微服务的注册发现机制进行内部服务调用，具体采用Http协议；</li><li>而micro-order与micro-pay之间也基于微服务注册发现机制进行内部微服务调用，为了演示更多的研发场景，这两个微服务之间的通信我们采用Grpc协议。</li></ol><br>
<br>规划好了微服务应用架构，接下来就可以具体开发了！具体的服务代码层面的构建，这里并不需要做任何微服务框架的引入，你只需要通过Spring Boot构建几个基本的Spring Boot应用即可，不需要引入任何服务治理相关的组件，只是一个简单且单纯的Spring Boot应用，不需要连接注册中心，也不需要引入什么OpenFeign、Hystrix、Sentinel之类的组件。<br>
<br>具体的代码结构如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/fd476603e5f26d16cce7e5987047dbae.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/fd476603e5f26d16cce7e5987047dbae.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到应用的入口类中已经没有服务发现之类的注解！接下来我们讲重点：<br>
<br>首先，在之前基于Spring Cloud的微服务调用中，如果通过Http协议进行服务调用，一般我们是通过引入OpenFeign来实行，服务方提供一个FeignClient接口定义，调用方代码直接引入即可，而具体的运行逻辑，则是OpenFeign中集成的Ribbon组件会从注册中心获取目标服务地址列表，然后进行负载均衡调用。<br>
<br>但在Service Mesh架构下负载均衡及服务发现的逻辑已经由Istio中的Sidecar帮我们干了，所以在这里就不能还像以前一样引入OpenFeign了！那么怎么办呢？为了延续之前的编程风格及服务通信代码的简易性，这里我们需要自己定制一个类似于OpenFeign的框架，可以基于OpenFeign的源码进行改造，但是要去掉其中关于服务负载均衡、熔断限流等服务治理相关的逻辑，让它变成一个只是简单进行Http服务调用的框架。<br>
<br>目前市面上并没有这样一个官方的适配框架，所以一些落地Service Mesh架构的公司为了兼容Spring Cloud微服务体系的迁移，也是自己单独改造和封装的，这里我从github上找了一个个人改造的代码并进行了适配修改，测试是可以的！其具备的能力说明如下：<br>
<br>1、支持在istio服务网格体系下，完成服务间的快速调用（体验和原先Spring Cloud Feign类似）；<br>
<br>2、支持多环境配置，例如本地环境微服务的调用地址可配置为本地，其他环境默认为Kubernetes集群中的服务；<br>
<br>3、支持链路追踪，默认透传如下Header，可以自动支持jaeger、zipkin链路追踪等，如下：<br>
<pre class="prettyprint">`"x-request-id", "x-b3-traceid", "x-b3-spanid", "x-b3-sampled", "x-b3-flags", "x-b3-parentspanid","x-ot-span-context", "x-datadog-trace-id", "x-datadog-parent-id", "x-datadog-sampled", "end-user", "user-agent"`<br>
</pre><br>
最后的实际编程风格是这样的：<br>
<pre class="prettyprint">@FakeClient(name = "micro-order")<br>
@RequestMapping("/order")<br>
public interface OrderServiceClient &#123;<br>
/**<br>
 * 订单创建<br>
 */<br>
@PostMapping("/create")<br>
ResponseResult<CreateOrderBO> create(@RequestBody CreateOrderDTO createOrderDTO);<br>
&#125; <br>
</pre><br>
这里是micro-order微服务给micro-api所提供的接口调用代码，micro-api服务引入调用即可，从编程风格上与之前Spring Cloud微服务的开发方式十分类似。只不过到这里为止，你并没有能看到任何与服务注册发现相关的逻辑！<br>
<br>其次，服务治理的核心逻辑都是由Istio及Sidecar代理完成的，完成应用开发后，只需要编写Kubernetes部署文件将服务部署进安装了Istio环境的Kubernetes集群即可，而将编写的Java服务部署到Kubernetes集群的流程，涉及"Docker镜像打包->镜像仓库发布->Kubernetes部署拉取镜像"这一套CI/CD操作流程。<br>
<br>接下来重点演示micro-api及micro-order的Kubernetes发布文件，看看它们有什么特别之处：<br>
<br>micro-order服务Kubernetes发布文件（micro-order.yaml）：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: micro-order<br>
labels:<br>
app: micro-order<br>
service: micro-order<br>
spec:<br>
type: ClusterIP<br>
ports:<br>
- name: http<br>
  port: 80<br>
  targetPort: 9091<br>
selector:<br>
app: micro-order<br>
<br>
---<br>
apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
name: micro-order-v1<br>
labels:<br>
app: micro-order<br>
version: v1<br>
spec:<br>
replicas: 2<br>
selector:<br>
matchLabels:<br>
  app: micro-order<br>
  version: v1<br>
template:<br>
metadata:<br>
  labels:<br>
    app: micro-order<br>
    version: v1<br>
spec:<br>
  containers:<br>
    - name: micro-order<br>
      image: 10.211.55.2:8080/micro-service/micro-order:1.0-SNAPSHOT<br>
      imagePullPolicy: Always<br>
      tty: true<br>
      ports:<br>
        - name: http<br>
          protocol: TCP<br>
          containerPort: 19091<br>
</pre><br>
如上所示，这是micro-order服务的Kubernetes部署文件，就是正常定义了该应用的Service资源及Deployment编排资源；为了后面演示服务的负载均衡调用，这里我特地将该应用部署成了2个副本！<br>
<br>接下来继续看看调用方micro-api服务的Kubernetes发布文件（micro-api.yaml）：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: micro-api<br>
spec:<br>
type: ClusterIP<br>
ports:<br>
- name: http<br>
  port: 19090<br>
  targetPort: 9090<br>
selector:<br>
app: micro-api<br>
<br>
---<br>
apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
name: micro-api<br>
spec:<br>
replicas: 1<br>
selector:<br>
matchLabels:<br>
  app: micro-api<br>
template:<br>
metadata:<br>
  labels:<br>
    app: micro-api<br>
spec:<br>
  containers:<br>
    - name: micro-api<br>
      image: 10.211.55.2:8080/micro-service/micro-api:1.0-SNAPSHOT<br>
      imagePullPolicy: Always<br>
      tty: true<br>
      ports:<br>
        - name: http<br>
          protocol: TCP<br>
          containerPort: 19090<br>
</pre><br>
与micro-order一样也只是定义了该应用的Kubernetes正常发布资源，到这里也并没有体现出micro-api是怎么调用micro-order服务的！接下来我们通过这个文件将服务发布至Kubernetes集群中（注意，是开启了Sidecar自动注入的默认命名空间）！<br>
<br>部署成功后，查看Pods信息，具体如下：<br>
<pre class="prettyprint"># kubectl get pods <br>
NAME                                      READY   STATUS    RESTARTS   AGE<br>
micro-api-6455654996-57t4z                2/2     Running   4          28h<br>
micro-order-v1-84ddc57444-dng2k           2/2     Running   3          23h<br>
micro-order-v1-84ddc57444-zpmjl           2/2     Running   4          28h<br>
</pre><br>
如上所示，可以看到一个micro-api Pod两个micro-order Pod都已经正常运行起来了！但不知你发现没有，每个Pod中READY字段显示的都是2/2，这意味着每个Pod中都启动了两个容器，一个是微服务应用本身，另外一个就是自动注入启动的Sidecar代理进程。为了更深理解这个逻辑，我们可以通过命令查看下Pod的描述信息：<br>
<pre class="prettyprint"># kubectl describe pod micro-api-6455654996-57t4z<br>
<br>
Name:         micro-api-6455654996-57t4z<br>
...<br>
<br>
IP:           10.32.0.10<br>
IPs:<br>
IP:           10.32.0.10<br>
Controlled By:  ReplicaSet/micro-api-6455654996<br>
Init Containers:<br>
istio-init:<br>
Container ID:  docker://eb0298bc8456f5f1336dfe2e8baab6035fccce898955469353da445aceab15cb<br>
Image:         docker.io/istio/proxyv2:1.8.4<br>
Image ID:      docker-pullable://istio/proxyv2@sha256:6a4ac67c1a74f95d3b307a77ad87e3abb4fcd64ddffe707f99a4458f39d9ce85<br>
....<br>
<br>
Containers:<br>
micro-api:<br>
Container ID:   docker://ebb45c5fa826f78c354877fc0a4c07d6b2fae4c6304e15729268b1cc6a69abca<br>
Image:          10.211.55.2:8080/micro-service/micro-api:1.0-SNAPSHOT<br>
Image ID:       docker-pullable://10.211.55.2:8080/micro-service/micro-api@sha256:f303016a604f30b99df738cbb61f89ffc166ba96d59785172c7b769c1c75a18d<br>
<br>
此处省略……<br>
<br>
istio-proxy:<br>
Container ID:  docker://bba9dc648b9e1a058e9c14b0635e0872079ed3fe7d55e34ac90ae03c5e5f3a66<br>
Image:         docker.io/istio/proxyv2:1.8.4<br>
Image ID:      docker-pullable://istio/proxyv2@sha256:6a4ac67c1a74f95d3b307a77ad87e3abb4fcd64ddffe707f99a4458f39d9ce85<br>
<br>
此处省略……<br>
</pre><br>
可以看到在开启了Sidecar自动注入的命名空间中，每启动一个Pod，Istio都会将Sidecar代理以初始化容器（Init Containers）的方式，自动启动一个对应地istio-proxy代理进程（Envoy），到这里你应该真实感到到Sidecar到底是一个什么样的存在了吧！<br>
<h4>部署Istio微服务网关</h4>前面的步骤中我们已经完成了微服务应用的开发，并且也已经将其部署到了Kubernetes集群，Sidecar代理也正常启动了，那么怎么访问呢？<br>
<br>一般来说如果要访问Kubernetes集群中的Service，可以通过NodePort端口映射及Ingress的方式向Kubernetes集群外暴露访问端口。但在Istio中采用了一种新的模型——Istio Gateway来代替Kubernetes中的Ingress资源类型。在Istio微服务体系中，所有外部流量的访问都应该通过Gateway进来，并由Gateway转发到对应的内部微服务！<br>
<br>而基于统一的控制面配置，Istio也可以集中管理Gateway网关的流量访问规则，实现对外部流量访问的整体管控！在前面部署Istio时，“istio-ingressgateway”入口流量网关已经作为Istio体系的一部分运行在k8s集群中了，如下：<br>
<pre class="prettyprint"># kubectl get svc -n istio-system|grep istio-ingressgateway<br>
istio-ingressgateway   LoadBalancer   10.100.69.24     <pending>     15021:31158/TCP,80:32277/TCP,443:30508/TCP,31400:30905/TCP,15443:30595/TCP   46h<br>
</pre><br>
接下来我们需要设置通过该网关访问micro-api微服务的逻辑，编写网关部署文件（micro-gateway.yaml）：<br>
<pre class="prettyprint">apiVersion: networking.istio.io/v1alpha3<br>
kind: Gateway<br>
metadata:<br>
name: micro-gateway<br>
spec:<br>
selector:<br>
istio: ingressgateway<br>
servers:<br>
- port:<br>
    number: 80<br>
    name: http<br>
    protocol: HTTP<br>
  hosts:<br>
    - "*"<br>
---<br>
apiVersion: networking.istio.io/v1alpha3<br>
kind: VirtualService<br>
metadata:<br>
name: micro-gateway<br>
spec:<br>
hosts:<br>
- "*"<br>
gateways:<br>
- micro-gateway<br>
http:<br>
- match:<br>
    - uri:<br>
        exact: /api/order/create<br>
  route:<br>
    - destination:<br>
        host: micro-api<br>
        port:<br>
          number: 19090<br>
</pre><br>
如上所示，该部署文件中定义了路由匹配规则，凡事访问/api/order/create地址的请求都会被转发到micro-api服务的19090端口！<br>
<br>配置完上述网关路由转发规则后，我们尝试通过访问istio-ingressgateway来到达访问微服务接口的效果，具体链路是：“外部调用->istio-ingressgateway->micro-api->micro-order”。<br>
<br>但是对于istio-ingressgateway的访问，由于也是Kubernetes内部Pod，所以暂时先配置一个NodePort端口映射，具体可以通过以下命令进行操作：<br>
<pre class="prettyprint">export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='&#123;.spec.ports[?(@.name=="http2")].nodePort&#125;')<br>
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='&#123;.spec.ports[?(@.name=="https")].nodePort&#125;')<br>
export INGRESS_HOST=127.0.0.1<br>
export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT<br>
</pre><br>
以上分别设置了istio-ingressgateway的http/https的NodePort访问端口，设置完成后具体查看nodePort端口映射情况：<br>
<pre class="prettyprint"># kubectl get svc -n istio-system|grep istio-ingressgateway<br>
istio-ingressgateway   LoadBalancer   10.100.69.24     <pending>     15021:31158/TCP,80:32277/TCP,443:30508/TCP,31400:30905/TCP,15443:30595/TCP   46h<br>
</pre><br>
可以看到通过http的32277以及https的30508端口可以访问istio-ingressgateway。具体访问url是：http://&#123;k8s集群IP&#125;:32277/接口url。具体访问效果如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/5a48ac3c12a0fff6cf923494a87614da.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/5a48ac3c12a0fff6cf923494a87614da.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从调用效果上可以看到，基于Istio的Service Mesh微服务体系已经运行成功！而从编程体验上看，你似乎已经快感觉不出微服务的存在了！反正稀里糊涂的服务就调通了，服务发现怎么做到的？负载均衡怎么做到的？这些问题在不需要你关心的同时，可能也引起了你的疑惑！接下来我们通过调用日志简单感知下调用链路所经过的逻辑！<br>
<h4>链路调用日志原理分析</h4>通过Postman调用返回结果后，我们分别看下链路所经过的服务日志！先看看istio-ingressgateway的容器日志，具体如下：<br>
<pre class="prettyprint"># kubectl logs istio-ingressgateway-74ccb8977c-gnhbb -n istio-system<br>
<br>
...<br>
2021-03-18T08:02:30.863243Z    info    xdsproxy    Envoy ADS stream established<br>
2021-03-18T08:02:30.865335Z    info    xdsproxy    connecting to upstream XDS server: istiod.istio-system.svc:15012<br>
[2021-03-18T08:14:00.224Z] "POST /api/order/create HTTP/1.1" 200 - "-" 66 75 7551 6144 "10.32.0.1" "PostmanRuntime/7.26.8" "8e8bad1d-5dd9-954b-b218-15f8c9595a24" "10.211.55.12:32277" "10.32.0.10:9090" outbound|19090||micro-api.default.svc.cluster.local 10.32.0.8:57460 10.32.0.8:8080 10.32.0.1:33229 - -<br>
[2021-03-18T08:14:32.465Z] "POST /api/order/create HTTP/1.1" 200 - "-" 66 75 3608 3599 "10.32.0.1" "PostmanRuntime/7.26.8" "ccf56049-88e8-9170-a1f5-93affbf6e098" "10.211.55.12:32277" "10.32.0.10:9090" outbound|19090||micro-api.default.svc.cluster.local 10.32.0.8:57460 10.32.0.8:8080 10.32.0.1:33229 - -<br>
[2021-03-18T08:16:37.242Z] "POST /api/order/create HTTP/1.1" 200 - "-" 66 75 68 67 "10.32.0.1" "PostmanRuntime/7.26.8" "98ecbd52-91a0-97c6-9ce6-d8f6094560e0" "10.211.55.12:32277" "10.32.0.10:9090" outbound|19090||micro-api.default.svc.cluster.local 10.32.0.8:57460 10.32.0.8:8080 10.32.0.1:33229 - -<br>
</pre><br>
如上所示，从istio-ingressgateway的网关日志中，可以看到/api/order/create接口的访问情况，确实是被转发到了micro-api所在的Pod IP，符合前面配置的网关路由规则。<br>
<br>接下来我们查看micro-api的istio-proxy代理的日志：<br>
<pre class="prettyprint"># kubectl logs micro-api-6455654996-57t4z istio-proxy<br>
...<br>
[2021-03-18T08:41:10.750Z] "POST /order/create HTTP/1.1" 200 - "-" 49 75 19 18 "-" "PostmanRuntime/7.26.8" "886390ea-e881-9c45-b859-1e0fc4733680" "micro-order" "10.32.0.7:9091" outbound|80||micro-order.default.svc.cluster.local 10.32.0.10:54552 10.99.132.246:80 10.32.0.10:39452 - default<br>
[2021-03-18T08:41:10.695Z] "POST /api/order/create HTTP/1.1" 200 - "-" 66 75 104 103 "10.32.0.1" "PostmanRuntime/7.26.8" "886390ea-e881-9c45-b859-1e0fc4733680" "10.211.55.12:32277" "127.0.0.1:9090" inbound|9090|| 127.0.0.1:52782 10.32.0.10:9090 10.32.0.1:0 outbound_.19090_._.micro-api.default.svc.cluster.local default<br>
...<br>
[2021-03-18T08:47:22.215Z] "POST /order/create HTTP/1.1" 200 - "-" 49 75 78 70 "-" "PostmanRuntime/7.26.8" "9bbd3a3c-86c4-943f-999a-bc9a1dc02c35" "micro-order" "10.32.0.9:9091" outbound|80||micro-order.default.svc.cluster.local 10.32.0.10:54326 10.99.132.246:80 10.32.0.10:44338 - default<br>
[2021-03-18T08:47:22.173Z] "POST /api/order/create HTTP/1.1" 200 - "-" 66 75 134 129 "10.32.0.1" "PostmanRuntime/7.26.8" "9bbd3a3c-86c4-943f-999a-bc9a1dc02c35" "10.211.55.12:32277" "127.0.0.1:9090" inbound|9090|| 127.0.0.1:57672 10.32.0.10:9090 10.32.0.1:0 outbound_.19090_._.micro-api.default.svc.cluster.local default<br>
</pre><br>
这里我们访问了两次接口情况，可以看到micro-api的Sidecar代理以负载均衡的方式，分别调用了micro-order服务的两个不同实例（打下划线IP）！<br>
<br>而访问micro-order的istio-proxy代理日志：<br>
<pre class="prettyprint"># kubectl logs micro-order-v1-84ddc57444-dng2k istio-proxy<br>
...<br>
2021-03-18T08:33:06.146178Z    info    xdsproxy    Envoy ADS stream established<br>
2021-03-18T08:33:06.146458Z    info    xdsproxy    connecting to upstream XDS server: istiod.istio-system.svc:15012<br>
[2021-03-18T08:34:59.055Z] "POST /order/create HTTP/1.1" 200 - "-" 49 75 8621 6923 "-" "PostmanRuntime/7.26.8" "b1685670-9e54-9970-a915-5c5dd18debc8" "micro-order" "127.0.0.1:9091" inbound|9091|| 127.0.0.1:36420 10.32.0.7:9091 10.32.0.10:54552 outbound_.80_._.micro-order.default.svc.cluster.local default<br>
[2021-03-18T08:41:10.751Z] "POST /order/create HTTP/1.1" 200 - "-" 49 75 17 16 "-" "PostmanRuntime/7.26.8" "886390ea-e881-9c45-b859-1e0fc4733680" "micro-order" "127.0.0.1:9091" inbound|9091|| 127.0.0.1:41398 10.32.0.7:9091 10.32.0.10:54552 outbound_.80_._.micro-order.default.svc.cluster.local default<br>
....<br>
</pre><br>
可以看到，请求通过micro-order的istio-proxy代理被转到了具体的micro-order实例！<br>
<br>通过上面日志的分析，虽然很细节的原理可能还是有疑问，但至少可以得到一个结论，那就是在Istio的Service Mesh微服务架构中，服务的转发、路由逻辑的确都是由Sidecar代理来干的，而且从日志中可以看到Envoy代理时刻都在保持着同控制面服务istiod的连接，并随时通过xDS协议更新着服务治理规则！<br>
<h3>后记</h3>本文从Service Mesh的大致原理出发，以实际的开发案例演示了如何开发一套基于Service Mesh架构的微服务体系！应该算是能够让大家入门Service Mesh了！也多少弥补了一点目前网络上Service Mesh具体实践文章几近空白的情况！<br>
<br>但不得不说，虽然Service Mesh微服务架构体系，极大的简化了研发人员开发微服务应用的成本；但另一方面Service Mesh在将微服务治理体系下沉为基础设施一部分的同时，也增加了对DevOps工程师的要求！毕竟要玩好Service Mesh架构，不仅需要开发技能，还需要对Service Mesh的架构体系及其框架源码有深刻的理解。除此之外，还需要对Kubernetes基础设施特别熟悉！<br>
<br>总之，Service Mesh虽然先进，但是在团队技能知识储备尚不具备的情况下，贸然将这套体系引入生产环境，也是有风险的！所以这只是一个开始，在后面的时间里，我还会继续分享有关Service Mesh及Istio的实践及原理，感兴趣的朋友可以持续关注下！<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/L1LoiI9NZqwZWsuCzEJN1A" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/L1LoiI9NZqwZWsuCzEJN1A</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            