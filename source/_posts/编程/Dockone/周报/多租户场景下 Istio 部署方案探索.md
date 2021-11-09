
---
title: '多租户场景下 Istio 部署方案探索'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/3083a8c7eec18cef6cafcfcee9fae524.jpg'
author: Dockone
comments: false
date: 2021-11-09 08:09:29
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/3083a8c7eec18cef6cafcfcee9fae524.jpg'
---

<div>   
<br>Istio 作为服务治理的主流技术，应用的越来越多。在将 Istio 落地部署的时候，需要考虑公司组织结构、产品、网络、人员等多种场景因素，确定合适的部署方案。我们需要在一个 Kubernetes 集群中通过 Istio 纳管多款产品，针对该需求，对 Istio 部署模型进行了一些调研探索，确定了适合的的部署模式，记录下来，为有相同需要的伙伴提供参考。<br>
<h3>背景</h3>随着云原生概念的普及，服务网格技术的流行以及 Istio 的成熟，使用Istio 进行服务治理的实践也越来越多，正成为服务治理的趋势。<br>
<br>在这样的背景下，我们也加入到 Istio 的研究中，希望初期通过 Istio 实现公司产品迭代版本的灰度发布，后续基于 Istio 为业务产品提供更多的流量管理及观测追踪能力。<br>
<br>一开始设计 Istio 部署方案时，基于当时对公司产品部署方式的了解，每款产品独占一套 Kubernetes 集群，另外考虑到当时我们对 Istio 的熟悉程度，设计的是最基础的方案：一套 Kubernetes 集群中部署一套 Istio，将该 Kubernetes 集群内唯一的产品纳管到 Istio 服务网格中，即 Kubernetes 集群、产品、Istio 是1:1:1的关系。<br>
<br>随着对公司产品部署方式调研的深入，我们了解到有几款产品部署在一套 Kubernetes 集群中，按照 namespace 进行分割，并且公司开始推行统一 Kubernetes 集群，已经在落地实施。<br>
<br>如果我们继续使用初始的部署方案，在初期 Kubernetes 集群中产品数量不多，规模不大的情况，也是可以支撑的，但存在潜在问题(主要是性能问题以及故障隔离性的问题)，所以需要调研实现在一套 Kubernetes 集群内，为每一个产品提供一套 Istio 服务网格的方案。<br>
<h3>初始方案问题</h3>初始方案存在以下两个问题：<br>
<h4>性能问题</h4>集群规模较大时，多产品共用同一套 Istio，会存在性能问题。在默认情况下，服务网格中的每个 Sidecar 都会收到整个集群所有服务信息。在较大规模的规模中，尤其是由于流量规则批量变更，控制面向数据面短时间内大量下发服务信息的情况下，Sidecar 的 CPU 及内存消耗、XDS 的下发及时性等问题，会变得非常突出。<br>
<h4>故障隔离性问题</h4>多款产品共用一套 Istio，可能 Istio 本身会出现问题，也可能由于某款产品的配置导致 Istio 出现问题，进而可能导致纳管的所有产品灰度甚至正常访问都出现问题，无法实现故障的隔离。<br>
<h3>新方案调研</h3>我们需要调研实现在一套 Kubernetes 集群内，为每一个产品提供一套 Istio 服务网格的方案，解决潜在的问题。总结下来，有以下几种方案：<br>
<h4>官方方案</h4>Istio 官方网站有一篇2018年的博文：<a href="https://istio.io/latest/zh/blog/2018/soft-multitenancy/">Istio 的软性多租户支持</a>给出了方案，可以实现为每个产品提供一套 Istio 网格的目标，每套 Istio 的控制面可以安装到指定的 namespace 中，数据面可以设置为产品部署的 namespace。官方方案是符合我们期望的方案，但 Istio 版本升级太快，博文内容比较陈旧，没办法按文档操作，并且有人反馈实操时有问题（提出问题的 <a href="https://github.com/istio/istio/issues/7608">issue</a>）。<br>
<br>每个 namespace 装一套 Istio 网格，也是存在一定问题的，但结合目前我们的实际情况，认为下面的两个问题我们是可以接受的。<br>
<ul><li>资源消耗问题：每套 Istio 网格都是需要消耗一定量的资源的</li><li>namespace 之间网络请求问题：如果 namespace 之间存在服务互访，按照 Istio 的规范，通过在 namespace 中部署 Ingress Gateway 和 Egress Gateway，控制进入和流出的流量，但这样增加了部署复杂度。</li></ul><br>
<br><h4>单控制面多 Gateway 方案</h4>Service Mesh (Istio) patterns for Multitenancy 提供了另外一种方案，该方案为部署一套 Istio 控制面，纳管多个产品数据面，每个产品以及 Istio 控制面的 namespace 部署一套 Ingress Gateway，相当于产品共用 Istio 控制面，但不共用 Ingress Gateway，一定程度上减少产品的耦合。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/3083a8c7eec18cef6cafcfcee9fae524.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/3083a8c7eec18cef6cafcfcee9fae524.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>单控制面多 Gateway 方案</em><br>
<h4>大厂方案</h4>一些大厂，在开源 Istio 的基础上，增加了多租户的支持，比如 <a href="https://www.redhat.com/en/topics/microservices/why-choose-openshift-service-mesh">Red Hat OpenShift Service Mesh</a>、<a href="https://www.infoq.cn/article/id2w4pefjqbusjhmd8jt">腾讯云 TFS Mesh</a> 及<a href="https://www.qbitai.com/2020/06/15846.html">蚂蚁金服 SOFAMesh</a>，在这三篇文章中，都各自提到了对多租户的支持。<br>
<h3>我们的探索</h3>目前我们进行了前两个方案的探索，即上文中官方方案及单控制面多 Gateway 的方案，通过实践和对源码研究，在不修改调研版本（V1.8.1）Istio 源码的情况下，前者是行不通的，而后者是可以顺利实现的(PS：通过对最新版本 V1.11.4 的 Istio 进行实践，本文对 V1.11.4 版本 Istio 仍然适用)。<br>
<br>两个方案各有优缺点：<br>
<ul><li>前者可以实现租户对 Istio 的独占，是在一套 Kubernetes 集群中彻底的分租户方案，比较完美的解决性能问题及故障隔离性问题，但缺点是需要修改源代码，开发成本较高，后期每次 Istio 版本升级，需要将 patch 重新打入，维护成本也较高，另外考虑对 Istio 的熟悉程度，修改源码带来的风险也较大。</li><li>后者是在不修改源代码的情况下实现多租户的折中方案，租户间虽然共享控制面，但独享数据面，在数据面范围内实现租户隔离，解决用户访问租户产品时的性能问题和故障隔离性问题，保障了产品的正常访问，这也是最重要、最需要保障的部分，缺点是租户共享控制面，控制面出现问题时，影响多产品控制面对数据面的管理，比如流量管理配置变更下发，但考虑一般在周期性上线时，才涉及到控制面对数据面的管理变更，解决问题的紧急程度，比数据面业务访问出问题时的紧急程度低很多，并且我们会通过控制面高可用等方案，降低这种情况的影响。</li></ul><br>
<br>下面详细介绍下对两个方案的探索：<br>
<h4>官方方案</h4>前面已经提到，官方方案内容比较陈旧，没办法按照文档操作，并且有人反馈存在问题，按照博文方案，通过 istioctl 方式多次尝试，没有成功。阅读了更多的其他官方文档，考虑 Istio Operator 方式安装 Istio，可以更方便进行 Istio 部署设置，所以进行了通过 Istio Operator 安装 Istio 的很多尝试，并且深入阅读了 Istio 相关代码，发现在不修改 Istio 源代码的情况下，是行不通的。<br>
<br>以下是通过 Istio Operator 安装 Istio，实现官方方案的一些尝试，并包含一些源代码的分析。<br>
<br>试验 Demo 部署模型如下，在一套 Kubernetes 集群上部署两套服务网格及两套产品（Foo 和 Bar），每套服务网格完全隔离，每个产品独占对应的服务网格。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/7839426c0627f8fcecdbbcfc8fe53b17.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/7839426c0627f8fcecdbbcfc8fe53b17.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>官方方案验证 demo 部署模型</em><br>
<br>1、为 Foo 产品部署独占的 Istio 组件<br>
<pre class="prettyprint">kubectl create namespace istio-system-foo<br>
istioctl operator init --istioNamespace istio-system-foo --watchedNamespaces istio-system-foo --namespace istio-system-foo --operatorNamespace istio-operator-foo<br>
kubectl apply -f istio-operator-foo.yaml<br>
</pre><br>
istio-operator-foo.yaml 的内容如下：<br>
<pre class="prettyprint">apiVersion: install.istio.io/v1alpha1<br>
kind: IstioOperator<br>
metadata:<br>
namespace: istio-system-foo<br>
name: istio-control-plane<br>
spec:<br>
namespace: istio-system-foo<br>
profile: default<br>
values:<br>
global:<br>
  istioNamespace: istio-system-foo<br>
meshConfig:<br>
  rootNamespace: istio-system-foo<br>
components:<br>
ingressGateways:<br>
  - name: istio-ingressgateway<br>
    k8s:<br>
      service:<br>
        type: NodePort<br>
</pre><br>
执行以上操作后，过一段时间，查看 istio-system-foo namespace，可以看到 Foo 独占的 Istio 组件部署成功。<br>
<br>2、类似的方式，为 Bar 应用部署独占的 Istio 组件<br>
<pre class="prettyprint">kubectl create namespace istio-system-bar<br>
istioctl operator init --istioNamespace istio-system-bar --watchedNamespaces istio-system-bar --namespace istio-system-bar --operatorNamespace istio-operator-bar<br>
kubectl apply -f istio-operator-bar.yaml<br>
</pre><br>
istio-operator-bar.yaml 的内容如下：<br>
<pre class="prettyprint">apiVersion: install.istio.io/v1alpha1<br>
kind: IstioOperator<br>
metadata:<br>
namespace: istio-system-bar<br>
name: istio-control-plane<br>
spec:<br>
namespace: istio-system-bar<br>
profile: default<br>
values:<br>
global:<br>
  istioNamespace: istio-system-bar<br>
meshConfig:<br>
  rootNamespace: istio-system-bar<br>
components:<br>
ingressGateways:<br>
  - name: istio-ingressgateway<br>
    k8s:<br>
      service:<br>
        type: NodePort<br>
</pre><br>
执行以上的操作，稍等一会，查看 istio-system-bar namespace 下的 Istio 组件部署情况，会发现 Istio Ingress Gateway 的 pod 无法成功启动，查看日志，日志中报如下错误：<br>
<pre class="prettyprint">error   xdsproxy        failed to create upstream grpc client: rpc error: code = Unavailable desc = connection error: desc = "transport: authentication handshake failed: x509: certificate signed by unknown authority (possibly because of \"crypto/rsa: verification error\" while trying to verify candidate authority certificate \"cluster.local\")"<br>
</pre><br>
更多日志见下面截图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/8edab9a4129288fd235104e90da9fbe0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/8edab9a4129288fd235104e90da9fbe0.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Ingress Gateway 启动错误日志</em><br>
<br>要解释截图中的错误日志原因，需要先介绍下数据面（Envoy）和控制面（Istiod）的网络交互。下面是网络交互图（ADS 请求部分）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/54d97ea2e33c84960b5d80f324c7176a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/54d97ea2e33c84960b5d80f324c7176a.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Envoy 和 Istiod 的网络交互图</em><br>
<br>在数据面 Istio Ingress Gateway 容器中或者业务产品 pod 注入的 Sidecar 容器中，启动着两个进程，Envoy 进程及 Pilot Agent 进程（即图中的 Istio Agent），后者扮演着 Istiod 和 Envoy 之间（即控制面和数据面之间）进行网络交互的中间代理角色。Envoy 向Istio Agent 发送 ADS（Aggregated Discovery Services，即聚合的发现服务，通过一个 gRPC 流来同步所有的配置更新）请求，后者将请求转发给控制面的配置发现服务（一般为 Istiod），然后配置发现服务将全部的配置更新返回给数据面。<br>
<br>数据面和控制面之间的网络请求，默认基于双向 TLS 认证，即两者进行通信时，双方都需要验证对方的身份，通过阅读源代码及参考赵化冰大佬的文章：《<a href="https://zhaohuabing.com/post/2020-05-25-istio-certificate/">一文带你彻底厘清 Isito 中的证书工作机制</a>》，了解数据面对控制面的身份认证过程如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/de815543b50730fe615a9f9f4d5a1f04.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/de815543b50730fe615a9f9f4d5a1f04.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>身份认证</em><br>
<ol><li>Istiod 采用内置的 CA 服务为自身签发一个服务器证书，并采用该服务器证书对外提供基于 TLS 的 gPRC 服务；</li><li>Istiod 调用 kube-apiserver 生成 configmap：istio-ca-root-cert，在该 configmap 中放入了 Istiod 的 CA 根证书；</li><li>数据面 Ingress Gateway 容器或 Sidecar 容器将istio-ca-root-cert configmap mount 为容器内 /var/run/secrets/istio/root-cert.pem 文件；</li><li>在Pilot Agent 和 Istiod 建立 gRPC 连接时，Pilot Agent 采用 root-cert.pem 文件证书对 Istiod 的身份进行认证。</li></ol><br>
<br>问题出现：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/bf497e5e5946ce43f9942c68e8805319.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/bf497e5e5946ce43f9942c68e8805319.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Istio 多租户认证过程</em><br>
<ol><li>Istio 通过 Kubernetes Informer 机制，将步骤2 Foo 控制面生成的 Configmap 同步到 Kubernetes 集群里所有的 namespace 下，包括 Bar 网格相关的 Namespace；</li><li>Bar 数据面 Ingress Gateway 容器或 Sidecar 容器，采用步骤3相同的方式，将步骤5同步到的 Configmap mount 到容器内；</li><li>Bar 的 Ingress Gateway 或 Sidecar 使用 Foo 控制面生成的 CA 根证书，对 Bar 的控制面进行身份认证，认证失败。</li></ol><br>
<br>可以从 Istio 源代码：<a href="https://github.com/istio/istio/blob/1.8.1/pilot/pkg/bootstrap/server.go" rel="nofollow" target="_blank">https://github.com/istio/istio ... er.go</a> 和 <a href="https://github.com/istio/istio/blob/1.8.1/pilot/pkg/serviceregistry/kube/controller/namespacecontroller.go" rel="nofollow" target="_blank">https://github.com/istio/istio ... er.go</a> 中看到相关的分析内容，Istiod 中 pilot 模块 server 服务时，会进行一系列的初始化工作，包括初始化 namespaceController，而该namespaceController 会创建 configmapInformer，通过 informer 机制，接受 Kubernetes 集群中的 istio-ca-root-cert configmap 的更新，而该 informer 是一个SharedIndexInformer，也就是共享的 informer，监听同一个 Kubernetes 集群中所有 namespace 下 configmap 的变化，所以从代码中可以看出，目前的 Istio 不支持在同一个 Kubernetes 集群中存在多套 Istio 控制面，这个变化应该是来自 Istio 2020 年 7 月的一次代码修改，可以查看：<a href="https://github.com/istio/istio/commit/9fdec2a68d443b9f9aac85530ac01491b0d24bf2" rel="nofollow" target="_blank">https://github.com/istio/istio ... 24bf2</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/3a0b61397286f3713bd1e68252b3e4c9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/3a0b61397286f3713bd1e68252b3e4c9.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>namespace controller: use shared informer</em><br>
<br>所以得出结论，在不修改 Istio 源码的情况下，想要实现官方方案，是行不通的。<br>
<h4>单控制面多 Gateway 方案</h4>参照《<a href="https://medium.com/@sudeep.batra/service-mesh-istio-patterns-for-multitenancy-2462568636f7">Service Mesh (Istio) patterns for Multitenancy</a>》，进行了实践验证，实践过程很顺利，以下是试验 Demo 部署模型及实践步骤，一套 Kubernetes 集群上部署两款产品（Foo 和 Bar），两款产品共享控制面，独享数据面，数据面范围内实现租户隔离。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211104/da4bb03e6834e9be802987fae42b85fa.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211104/da4bb03e6834e9be802987fae42b85fa.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>单控制面多 Gateway 方案 Demo 部署模型</em><br>
<br>1、部署 Istio Operator<br>
<pre class="prettyprint">istioctl operator init<br>
</pre><br>
2、创建 istio-system namespace<br>
<pre class="prettyprint">kubectl create namespace istio-system<br>
</pre><br>
3、创建部署控制面的 Istio Operator 自定义资源<br>
<pre class="prettyprint">kubectl apply -f istio-operator.yaml<br>
</pre><br>
istio-operator.yaml 的内容如下：<br>
<pre class="prettyprint">apiVersion: install.istio.io/v1alpha1<br>
kind: IstioOperator<br>
metadata:<br>
namespace: istio-system<br>
name: istio-control-plane<br>
spec:<br>
namespace: istio-system<br>
profile: default<br>
components:<br>
pilot:<br>
  k8s:<br>
    hpaSpec:<br>
      minReplicas: 2<br>
    env:<br>
      - name: PILOT_SCOPE_GATEWAY_TO_NAMESPACE<br>
        value: "true"<br>
ingressGateways:<br>
  - name: istio-ingressgateway<br>
    enabled: false<br>
</pre><br>
需要注意一点，部署 pilot 组件时，为 pilot 组件设置了 <code class="prettyprint">PILOT_SCOPE_GATEWAY_TO_NAMESPACE</code> 环境变量，值为 true，会限制 gateway 规则只会应用到 gateway 所在 namespace 下 Istio Ingress Gateway 上，这样设置实现租户之间的隔离。<br>
<br>operator controller 会监测到 istio-control-plane 这个 IstioOperator 资源，并按照配置部署相关组件，稍等一段时间，可以看懂 istio-system namespace 下共享的控制面组件已经部署完成。<br>
<pre class="prettyprint">kubectl get all -n istio-system<br>
NAME                          READY   STATUS    RESTARTS   AGE<br>
pod/istiod-6fc49c7d5c-2ljdl   1/1     Running   0          19h<br>
pod/istiod-6fc49c7d5c-mjp5h   1/1     Running   0          19h<br>
NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                                 AGE<br>
service/istiod   ClusterIP   10.109.247.96   <none>        15010/TCP,15012/TCP,443/TCP,15014/TCP   5d5h<br>
NAME                     READY   UP-TO-DATE   AVAILABLE   AGE<br>
deployment.apps/istiod   2/2     2            2           19h<br>
NAME                                DESIRED   CURRENT   READY   AGE<br>
replicaset.apps/istiod-6fc49c7d5c   2         2         2       19h<br>
replicaset.apps/istiod-f77f59479    0         0         0       19h<br>
NAME                                         REFERENCE           TARGETS         MINPODS   MAXPODS   REPLICAS   AGE<br>
horizontalpodautoscaler.autoscaling/istiod   Deployment/istiod   <unknown>/80%   2         5         2          19h<br>
</pre><br>
4、创建 foo namespace，并为该 namespace 打上标签，支持 istio sidecar 自动注入<br>
<pre class="prettyprint">kubectl create namespace foo<br>
kubectl label namespace foo istio-injection=enabled<br>
</pre><br>
5、创建部署 Foo 应用独占的 Istio Ingress Gateway 需要的 Istio Operator 自定义资源<br>
<pre class="prettyprint">kubectl apply -f istio-operator-foo.yaml<br>
</pre><br>
istio-operator-foo.yaml 的内容如下：<br>
<pre class="prettyprint">apiVersion: install.istio.io/v1alpha1<br>
kind: IstioOperator<br>
metadata:<br>
namespace: istio-system<br>
name: foo-ingress-gateway<br>
spec:<br>
profile: empty<br>
components:<br>
ingressGateways:<br>
  - name: istio-ingress-gateway<br>
    namespace: foo <br>
    enabled: true<br>
    k8s:<br>
      hpaSpec:<br>
        minReplicas: 2<br>
      service:<br>
        type: NodePort<br>
        ports:<br>
          - name: http2<br>
            nodePort: 32180<br>
            port: 80<br>
            protocol: TCP<br>
            targetPort: 8080<br>
</pre><br>
稍等一段时间，可以看到 foo namespace 下，Foo 应用独占的 Istio Ingress Gateway 部署完成。<br>
<pre class="prettyprint">kubectl get all -n foo<br>
NAME                                         READY   STATUS    RESTARTS   AGE<br>
pod/istio-ingress-gateway-78447867cf-gh4l8   1/1     Running   0          23h<br>
pod/istio-ingress-gateway-78447867cf-nqcb4   1/1     Running   0          23h<br>
NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                                                                      AGE<br>
service/istio-ingress-gateway   NodePort    10.233.21.151   <none>        80:32180/TCP   23h<br>
NAME                                    READY   UP-TO-DATE   AVAILABLE   AGE<br>
deployment.apps/istio-ingress-gateway   2/2     2            2           23h<br>
NAME                                               DESIRED   CURRENT   READY   AGE<br>
replicaset.apps/istio-ingress-gateway-78447867cf   2         2         2       23h<br>
NAME                                                        REFERENCE                          TARGETS   MINPODS   MAXPODS   REPLICAS   AGE<br>
horizontalpodautoscaler.autoscaling/istio-ingress-gateway   Deployment/istio-ingress-gateway   8%/80%    2         5         2          23h<br>
</pre><br>
6、参照步骤4、5，在 bar namespace 中部署产品 Bar 独占的 Istio Ingress Gateway。<br>
<pre class="prettyprint">kubectl create namespace bar<br>
kubectl label namespace bar istio-injection=enabled<br>
kubectl apply -f istio-operator-bar.yaml<br>
</pre><br>
istio-operator-bar.yaml 内容如下：<br>
<pre class="prettyprint">apiVersion: install.istio.io/v1alpha1<br>
kind: IstioOperator<br>
metadata:<br>
namespace: istio-system<br>
name: bar-ingress-gateway<br>
spec:<br>
profile: empty<br>
components:<br>
ingressGateways:<br>
  - name: istio-ingress-gateway<br>
    namespace: bar<br>
    enabled: true<br>
    k8s:<br>
      hpaSpec:<br>
        minReplicas: 2<br>
      service:<br>
        type: NodePort<br>
        ports:<br>
          - name: http2<br>
            nodePort: 32280<br>
            port: 80<br>
            protocol: TCP<br>
            targetPort: 8080<br>
</pre><br>
稍等一段时间，可以看到 bar namespace 下，Bar 应用独占的 Istio Ingress Gateway 部署完成。<br>
<pre class="prettyprint">kubectl get all -n bar<br>
NAME                                         READY   STATUS    RESTARTS   AGE<br>
pod/istio-ingress-gateway-8646b4964b-2q56j   1/1     Running   0          23h<br>
pod/istio-ingress-gateway-8646b4964b-xjvvp   1/1     Running   0          23h<br>
NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                                                                      AGE<br>
service/istio-ingress-gateway   NodePort    10.233.41.156   <none>        80:32280/TCP   23h<br>
NAME                                    READY   UP-TO-DATE   AVAILABLE   AGE<br>
deployment.apps/istio-ingress-gateway   2/2     2            2           23h<br>
NAME                                               DESIRED   CURRENT   READY   AGE<br>
replicaset.apps/istio-ingress-gateway-8646b4964b   2         2         2       23h<br>
NAME                                                        REFERENCE                          TARGETS   MINPODS   MAXPODS   REPLICAS   AGE<br>
horizontalpodautoscaler.autoscaling/istio-ingress-gateway   Deployment/istio-ingress-gateway   6%/80%    2         5         2          23h<br>
</pre><br>
通过步骤1-6，实现了单控制面多 Gateway 方案的部署，两款产品 Foo 及 Bar 共享 istio-system namespace 中的 Istiod 控制面，独占各自 namespace 中的 Istio Ingress Gateway。<br>
<br>部署Foo、Bar两款产品（很简单的 HelloWorld 类型的 Demo），并创建 Istio 流量管理相关的 CRD，可以实现 Foo、Bar 两款产品的灰度发布，下面是实现灰度发布后的效果，部署过程不再赘述。<br>
<pre class="prettyprint">curl http://10.154.0.165:32180/foo/hello<br>
Hello Foo 0.0.1<br>
curl -H 'version:v0-0-2' http://10.154.0.165:32180/foo/hello<br>
Hello Foo 0.0.2<br>
curl http://10.154.0.165:32280/bar/hello<br>
Hello Bar 0.0.1<br>
curl -H 'version:v0-0-2' http://10.154.0.165:32280/bar/hello<br>
Hello Bar 0.0.2<br>
</pre><br>
<h3>总结</h3>通过对 Istio 多租户方案的调研和探索，我们总结出同一个 Kubernetes 集群中分 namespace 部署多款产品场景下两种 Istio 部署方案的优缺点，结合我们目前的情况，更倾向采用单控制面多 Gateway 方案。以上的调研探索，可能存在错误或不准确的地方，欢迎大家交流指正。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/rmf7te7w9JVa2mrCHmdS4g" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/rmf7te7w9JVa2mrCHmdS4g</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            