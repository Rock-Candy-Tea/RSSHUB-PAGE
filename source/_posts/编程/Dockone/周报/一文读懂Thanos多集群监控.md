
---
title: '一文读懂Thanos多集群监控'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/ec2ce8ee0ae2dacdc46f755b0a245cb0.png'
author: Dockone
comments: false
date: 2021-04-13 04:11:29
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/ec2ce8ee0ae2dacdc46f755b0a245cb0.png'
---

<div>   
<br><h3>介绍</h3>在本文中，我们将看到Prometheus监控技术栈的局限性，以及为什么移动到基于Thanos的技术栈可以提高指标留存率并降低总体基础设施成本。<br>
<br>用于此演示的内容可以在这两个地方获得，<a href="https://github.com/particuleio/teks/tree/main/terragrunt/live/thanos">1</a>，<a href="https://github.com/particuleio/terraform-kubernetes-addons/tree/main/modules/aws">2</a>，并提交到他们各自的许可证。<br>
<h3>Kubernetes普罗米修斯技术栈</h3>在为我们的客户部署Kubernetes基础设施时，在每个集群上部署监控技术栈是标准做法。这个堆栈通常由几个组件组成：<br>
<ul><li>Prometheus：收集度量标准</li><li>告警管理器：根据指标查询向各种提供者发送警报</li><li>Grafana：可视化豪华仪表板</li></ul><br>
<br>简化架构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/ec2ce8ee0ae2dacdc46f755b0a245cb0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/ec2ce8ee0ae2dacdc46f755b0a245cb0.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>注意事项</h4>这种架构有一些注意事项，当你想从其中获取指标的集群数量增加时，它的伸缩性以及可扩展性不太好。<br>
<br><strong>多个Grafana</strong><br>
<br>在这种设置中，每个集群都有自己的Grafana和自己的一组仪表板，维护起来很麻烦。<br>
<br><strong>存储指标数据是昂贵的</strong><br>
<br>Prometheus将指标数据存储在磁盘上，你必须在存储空间和指标保留时间之间做出选择。如果你想长时间存储数据并在云提供商上运行，那么如果存储TB的数据，块存储的成本可能会很高。同样，在生产环境中，Prometheus经常使用复制或分片或两者同时运行，这可能会使存储需求增加两倍甚至四倍。<br><br>
<h3>解决方案</h3><strong>多个Grafana数据源</strong><br>
<br>可以在外部网络上公开Prometheus的端点，并将它们作为数据源添加到单个Grafana中。你只需要在Prometheus外部端点上使用TLS或TLS和基本认证来实现安全性。此解决方案的缺点是不能基于不同的数据源进行计算。<br>
<br><strong>Prometheus联邦</strong><br>
<br>Prometheus联邦允许从Prometheus中抓取Prometheus，当你不抓取很多指标数据时，这个解决方案可以很好地工作。在规模上，如果你所有的Prometheus目标的抓取持续时间都比抓取间隔长，可能会遇到一些严重的问题。<br>
<br><strong>Prometheus远程写</strong><br>
<br>虽然远程写入是一种解决方案（也由Thanos receiver实现），但我们将不在本文中讨论“推送指标”部分。你可以在<a href="https://docs.google.com/document/d/1H47v7WfyKkSLMrR8_iku6u9VB73WrVzBHb2SB6dL9_g/edit#heading=h.2v27snv0lsur">这里</a>阅读关于推送指标的利弊。建议在不信任多个集群或租户的情况下（例如在将Prometheus构建为服务提供时），将指标作为最后的手段。无论如何，这可能是以后文章的主题，但我们将在这里集中讨论抓取。<br>
<h3>Thanos，它来了</h3>Thanos是一个“开源的，高可用的Prometheus系统，具有长期存储能力”。很多知名公司都在使用Thanos，也是CNCF孵化项目的一部分。<br>
<br>Thanos的一个主要特点就是允许“无限”存储空间。通过使用对象存储（比如S3），几乎每个云提供商都提供对象存储。如果在前提环境下运行，对象存储可以通过rook或minio这样的解决方案提供。<br>
<h4>它是如何工作的？</h4>Thanos和Prometheus并肩作战，从Prometheus开始升级到Thanos是很常见的。<br>
<br>Thanos被分成几个组件，每个组件都有一个目标（每个服务都应该这样:)），组件之间通过gRPC进行通信。<br>
<br><strong>Thanos Sidecar</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/fc97b38331d572b8b5d720db5e46e056.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/fc97b38331d572b8b5d720db5e46e056.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Thanos和Prometheus一起运行（有一个边车），每2小时向一个对象存储库输出Prometheus指标。这使得Prometheus几乎是无状态的。Prometheus仍然在内存中保存着2个小时的度量值，所以在发生宕机的情况下，你可能仍然会丢失2个小时的度量值（这个问题应该由你的Prometheus设置来处理，使用HA/分片，而不是Thanos）。<br>
<br>Thanos sidecar与Prometheus运营者和Kube Prometheus栈一起，可以轻松部署。这个组件充当Thanos查询的存储。<br>
<br><strong>Thanos存储</strong><br>
<br>Thanos存储充当一个网关，将查询转换为远程对象存储。它还可以在本地存储上缓存一些信息。基本上，这个组件允许你查询对象存储以获取指标。这个组件充当Thanos查询的存储。<br>
<br><strong>Thanos Compactor</strong><br>
<br>Thanos Compactor是一个单例（它是不可扩展的），它负责压缩和降低存储在对象存储中的指标。下采样是随着时间的推移对指标粒度的宽松。例如，你可能想将你的指标保持2年或3年，但你不需要像昨天的指标那么多数据点。这就是压缩器的作用，它可以在对象存储上节省字节，从而节省成本。<br>
<br><strong>Thanos Query</strong><br>
<br>Thanos查询是Thanos的主要组件，它是向其发送PromQL查询的中心点。Thanos查询暴露了一个与Prometheus兼容的端点。然后它将查询分派给所有的“stores”。记住，Store可能是任何其他提供指标的Thanos组件。Thanos查询可以发送查询到另一个Thanos查询（他们可以堆叠）。<br>
<ul><li>Thanos Store</li><li>Thanos Sidecar</li><li>Thanos Query</li></ul><br>
<br>还负责对来自不同Store或Prometheus的相同指标进行重复数据删除。例如，如果你有一个度量值在Prometheus中，同时也在对象存储中，Thanos Query可以对该指标值进行重复数据删除。在Prometheus HA设置的情况下，重复数据删除也基于Prometheus副本和分片。<br>
<br><strong>Thanos Query Frontend</strong><br>
<br>正如它的名字所暗示的，Thanos查询前端是Thanos查询的前端，它的目标是将大型查询拆分为多个较小的查询，并缓存查询结果（在内存或memcached中）。<br>
<br>还有其他组件，比如在远程写的情况下接收Thanos，但这仍然不是本文的主题。<br>
<h3>多集群架构</h3>有多种方法可以将这些组件部署到多个Kubernetes集群中，根据用例的不同，有些方法比其他方法更好，在这里我们不能给出详细的介绍。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/e906b9149a1f4fea010612fe9687c16b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/e906b9149a1f4fea010612fe9687c16b.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们的例子是在AWS上运行，使用<a href="https://github.com/particuleio/teks">tEKS</a>部署了2个集群，我们的all in one解决方案将生产就绪的EKS集群部署在AWS上：<br>
<ul><li>一个<a href="https://github.com/particuleio/teks/tree/main/terragrunt/live/thanos/eu-west-1/clusters/observer">观察者集群</a></li><li>一个<a href="https://github.com/particuleio/teks/tree/main/terragrunt/live/thanos/eu-west-3/clusters/observee">被观察集群</a></li></ul><br>
<br>我们的部署使用了官方的kube-prometheus-stack和bitnami thanos图表。<br>
<br>一切都是在我们的terraform-kubernetes-addons存储库中策划的。<br>
<br>Thanos demo文件夹中的目录结构如下：<br>
<pre class="prettyprint">.<br>
├──  env_tags.yaml<br>
├──  eu-west-1<br>
│  ├──  clusters<br>
│  │  └──  observer<br>
│  │     ├──  eks<br>
│  │     │  ├──  kubeconfig<br>
│  │     │  └──  terragrunt.hcl<br>
│  │     ├──  eks-addons<br>
│  │     │  └──  terragrunt.hcl<br>
│  │     └──  vpc<br>
│  │        └──  terragrunt.hcl<br>
│  └──  region_values.yaml<br>
└──  eu-west-3<br>
├──  clusters<br>
│  └──  observee<br>
│     ├──  cluster_values.yaml<br>
│     ├──  eks<br>
│     │  ├──  kubeconfig<br>
│     │  └──  terragrunt.hcl<br>
│     ├──  eks-addons<br>
│     │  └──  terragrunt.hcl<br>
│     └──  vpc<br>
│        └──  terragrunt.hcl<br>
└──  region_values.yaml<br>
</pre><br>
这允许DRY（Don 't Repeat Yourself）基础设施，并可以轻松地扩展AWS帐户、区域和集群的数量。<br>
<h4>观察者集群</h4>观察者集群是我们的主集群，我们将从它查询其他集群：<br>
<br>Prometheus正在运行：<br>
<ul><li>Grafana启用</li><li>Thanos边车上传到特定的桶</li></ul><br>
<br><pre class="prettyprint">kube-prometheus-stack = &#123;<br>
enabled                     = true<br>
allowed_cidrs               = dependency.vpc.outputs.private_subnets_cidr_blocks<br>
thanos_sidecar_enabled      = true<br>
thanos_bucket_force_destroy = true<br>
extra_values                = <<-EXTRA_VALUES<br>
grafana:<br>
  deploymentStrategy:<br>
    type: Recreate<br>
  ingress:<br>
    enabled: true<br>
    annotations:<br>
      kubernetes.io/ingress.class: nginx<br>
      cert-manager.io/cluster-issuer: "letsencrypt"<br>
    hosts:<br>
      - grafana.$&#123;local.default_domain_suffix&#125;<br>
    tls:<br>
      - secretName: grafana.$&#123;local.default_domain_suffix&#125;<br>
        hosts:<br>
          - grafana.$&#123;local.default_domain_suffix&#125;<br>
  persistence:<br>
    enabled: true<br>
    storageClassName: ebs-sc<br>
    accessModes:<br>
      - ReadWriteOnce<br>
    size: 1Gi<br>
prometheus:<br>
  prometheusSpec:<br>
    replicas: 1<br>
    retention: 2d<br>
    retentionSize: "10GB"<br>
    ruleSelectorNilUsesHelmValues: false<br>
    serviceMonitorSelectorNilUsesHelmValues: false<br>
    podMonitorSelectorNilUsesHelmValues: false<br>
    storageSpec:<br>
      volumeClaimTemplate:<br>
        spec:<br>
          storageClassName: ebs-sc<br>
          accessModes: ["ReadWriteOnce"]<br>
          resources:<br>
            requests:<br>
              storage: 10Gi<br>
EXTRA_VALUES<br>
</pre><br>
为观察者集群生成一个CA证书：<br>
<ul><li>这个CA将被进入sidecar的被观察集群所信任</li><li>为Thanos querier组件生成TLS证书，这些组件将查询被观察集群</li></ul><br>
<br>Thanos组件部署：<br>
<ul><li>Thanos组件全部部署完成</li><li>查询前端，作为Grafana的数据源端点</li><li>存储网关用于查询观察者桶</li><li>Query将对存储网关和其他查询器执行查询</li></ul><br>
<br>部署的额外Thanos组件：<br>
<ul><li>配置了TLS的Thanos查询器对每个被观察集群进行查询</li></ul><br>
<br><pre class="prettyprint">thanos-tls-querier = &#123;<br>
"observee" = &#123;<br>
enabled                 = true<br>
default_global_requests = true<br>
default_global_limits   = false<br>
stores = [<br>
  "thanos-sidecar.$&#123;local.default_domain_suffix&#125;:443"<br>
]<br>
&#125;<br>
&#125;<br>
<br>
thanos-storegateway = &#123;<br>
"observee" = &#123;<br>
enabled                 = true<br>
default_global_requests = true<br>
default_global_limits   = false<br>
bucket                  = "thanos-store-pio-thanos-observee"<br>
region                  = "eu-west-3"<br>
&#125; <br>
</pre><br>
<h4>被观测集群</h4>被观测集群是Kubernetes集群，具有最小的Prometheus/Thanos安装，将被观测集群查询。<br>
<br>Prometheus operator正在运行：<br>
<ul><li>Thanos这边就是上传给观察者特定的桶</li><li>Thanos边车与TLS客户端认证的入口对象一起发布，并信任观察者集群CA</li></ul><br>
<br><pre class="prettyprint">kube-prometheus-stack = &#123;<br>
enabled                     = true<br>
allowed_cidrs               = dependency.vpc.outputs.private_subnets_cidr_blocks<br>
thanos_sidecar_enabled      = true<br>
thanos_bucket_force_destroy = true<br>
extra_values                = <<-EXTRA_VALUES<br>
grafana:<br>
  enabled: false<br>
prometheus:<br>
  thanosIngress:<br>
    enabled: true<br>
    ingressClassName: nginx<br>
    annotations:<br>
      cert-manager.io/cluster-issuer: "letsencrypt"<br>
      nginx.ingress.kubernetes.io/ssl-redirect: "true"<br>
      nginx.ingress.kubernetes.io/backend-protocol: "GRPC"<br>
      nginx.ingress.kubernetes.io/auth-tls-verify-client: "on"<br>
      nginx.ingress.kubernetes.io/auth-tls-secret: "monitoring/thanos-ca"<br>
    hosts:<br>
    - thanos-sidecar.$&#123;local.default_domain_suffix&#125;<br>
    paths:<br>
    - /<br>
    tls:<br>
    - secretName: thanos-sidecar.$&#123;local.default_domain_suffix&#125;<br>
      hosts:<br>
      - thanos-sidecar.$&#123;local.default_domain_suffix&#125;<br>
  prometheusSpec:<br>
    replicas: 1<br>
    retention: 2d<br>
    retentionSize: "6GB"<br>
    ruleSelectorNilUsesHelmValues: false<br>
    serviceMonitorSelectorNilUsesHelmValues: false<br>
    podMonitorSelectorNilUsesHelmValues: false<br>
    storageSpec:<br>
      volumeClaimTemplate:<br>
        spec:<br>
          storageClassName: ebs-sc<br>
          accessModes: ["ReadWriteOnce"]<br>
          resources:<br>
            requests:<br>
              storage: 10Gi<br>
EXTRA_VALUES<br>
</pre><br>
Thanos组件部署：<br>
<ul><li>Thanos压缩器来管理这个特定集群的下采样</li></ul><br>
<br><pre class="prettyprint">thanos = &#123;<br>
enabled = true<br>
bucket_force_destroy = true<br>
trusted_ca_content      = dependency.thanos-ca.outputs.thanos_ca<br>
extra_values = <<-EXTRA_VALUES<br>
compactor:<br>
  retentionResolution5m: 90d<br>
query:<br>
  enabled: false<br>
queryFrontend:<br>
  enabled: false<br>
storegateway:<br>
  enabled: false<br>
EXTRA_VALUES<br>
&#125; <br>
</pre><br>
<h3>再深入一点</h3>让我们检查一下集群上正在运行什么。关于观察员，我们有:<br>
<pre class="prettyprint">kubectl -n monitoring get pods<br>
NAME                                                        READY   STATUS    RESTARTS   AGE<br>
alertmanager-kube-prometheus-stack-alertmanager-0           2/2     Running   0          120m<br>
kube-prometheus-stack-grafana-c8768466b-rd8wm               2/2     Running   0          120m<br>
kube-prometheus-stack-kube-state-metrics-5cf575d8f8-x59rd   1/1     Running   0          120m<br>
kube-prometheus-stack-operator-6856b9bb58-hdrb2             1/1     Running   0          119m<br>
kube-prometheus-stack-prometheus-node-exporter-8hvmv        1/1     Running   0          117m<br>
kube-prometheus-stack-prometheus-node-exporter-cwlfd        1/1     Running   0          120m<br>
kube-prometheus-stack-prometheus-node-exporter-rsss5        1/1     Running   0          120m<br>
kube-prometheus-stack-prometheus-node-exporter-rzgr9        1/1     Running   0          120m<br>
prometheus-kube-prometheus-stack-prometheus-0               3/3     Running   1          120m<br>
thanos-compactor-74784bd59d-vmvps                           1/1     Running   0          119m<br>
thanos-query-7c74db546c-d7bp8                               1/1     Running   0          12m<br>
thanos-query-7c74db546c-ndnx2                               1/1     Running   0          12m<br>
thanos-query-frontend-5cbcb65b57-5sx8z                      1/1     Running   0          119m<br>
thanos-query-frontend-5cbcb65b57-qjhxg                      1/1     Running   0          119m<br>
thanos-storegateway-0                                       1/1     Running   0          119m<br>
thanos-storegateway-1                                       1/1     Running   0          118m<br>
thanos-storegateway-observee-storegateway-0                 1/1     Running   0          12m<br>
thanos-storegateway-observee-storegateway-1                 1/1     Running   0          11m<br>
thanos-tls-querier-observee-query-dfb9f79f9-4str8           1/1     Running   0          29m<br>
thanos-tls-querier-observee-query-dfb9f79f9-xsq24           1/1     Running   0          29m<br>
<br>
kubectl -n monitoring get ingress<br>
NAME                            CLASS    HOSTS                                            ADDRESS                                                                         PORTS     AGE<br>
kube-prometheus-stack-grafana   <none>   grafana.thanos.teks-tg.clusterfrak-dynamics.io   k8s-ingressn-ingressn-afa0a48374-f507283b6cd101c5.elb.eu-west-1.amazonaws.com   80, 443   123m<br>
</pre><br>
被观察者：<br>
<pre class="prettyprint">kubectl -n monitoring get pods<br>
NAME                                                        READY   STATUS    RESTARTS   AGE<br>
alertmanager-kube-prometheus-stack-alertmanager-0           2/2     Running   0          39m<br>
kube-prometheus-stack-kube-state-metrics-5cf575d8f8-ct292   1/1     Running   0          39m<br>
kube-prometheus-stack-operator-6856b9bb58-4cngc             1/1     Running   0          39m<br>
kube-prometheus-stack-prometheus-node-exporter-bs4wp        1/1     Running   0          39m<br>
kube-prometheus-stack-prometheus-node-exporter-c57ss        1/1     Running   0          39m<br>
kube-prometheus-stack-prometheus-node-exporter-cp5ch        1/1     Running   0          39m<br>
kube-prometheus-stack-prometheus-node-exporter-tnqvq        1/1     Running   0          39m<br>
kube-prometheus-stack-prometheus-node-exporter-z2p49        1/1     Running   0          39m<br>
kube-prometheus-stack-prometheus-node-exporter-zzqp7        1/1     Running   0          39m<br>
prometheus-kube-prometheus-stack-prometheus-0               3/3     Running   1          39m<br>
thanos-compactor-7576dcbcfc-6pd4v                           1/1     Running   0          38m<br>
<br>
kubectl -n monitoring get ingress<br>
NAME                                   CLASS   HOSTS                                                   ADDRESS                                                                         PORTS     AGE<br>
kube-prometheus-stack-thanos-gateway   nginx   thanos-sidecar.thanos.teks-tg.clusterfrak-dynamics.io   k8s-ingressn-ingressn-95903f6102-d2ce9013ac068b9e.elb.eu-west-3.amazonaws.com   80, 443   40m<br>
</pre><br>
我们的TLS查询器应该能够查询被观测集群的度量标准。让我们来看看它们的行为：<br>
<pre class="prettyprint">k -n monitoring logs -f thanos-tls-querier-observee-query-687dd88ff5-nzpdh<br>
<br>
level=info ts=2021-02-23T15:37:35.692346206Z caller=storeset.go:387 component=storeset msg="adding new storeAPI to query storeset" address=thanos-sidecar.thanos.teks-tg.clusterfrak-dynamics.io:443 extLset="&#123;cluster=\"pio-thanos-observee\", prometheus=\"monitoring/kube-prometheus-stack-prometheus\", prometheus_replica=\"prometheus-kube-prometheus-stack-prometheus-0\"&#125;" <br>
</pre><br>
所以这个查询器pods可以查询我的其他集群，如果我们检查Web，我们可以看到存储：<br>
<pre class="prettyprint">kubectl -n monitoring port-forward thanos-tls-querier-observee-query-687dd88ff5-nzpdh 10902<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/8520cea8a4763433ddf74d3f97c39758.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/8520cea8a4763433ddf74d3f97c39758.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
太棒了，但是我只有一个存储，还记得我们说过查询器可以堆叠在一起吗？在我们的观察者集群中，我们有标准的http查询器，它可以查询架构图中的其他组件。<br>
<pre class="prettyprint">kubectl -n monitoring port-forward thanos-query-7c74db546c-d7bp8 10902<br>
</pre><br>
这里我们可以看到所有的存储已经被添加到我们的中心查询器：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/4bf2df6e2b01153ec40e46c61ad3165b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/4bf2df6e2b01153ec40e46c61ad3165b.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>观察者把本地Thanos聚集</li><li>我们的存储网关（一个用于远程观测者集群，一个用于本地观测者集群）</li><li>本地TLS查询器，它可以查询被观察的sidecar</li></ul><br>
<br><h3>在Grafana可视化</h3>最后，我们可以前往Grafana，看看默认的Kubernetes仪表板是如何与多集群兼容的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/8e9ecf3e24649fda97481343562fa477.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/8e9ecf3e24649fda97481343562fa477.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>Thanos是一个非常复杂的系统，有很多移动部件，我们没有深入研究具体的自定义配置，因为它会花费太多的时间。<br>
<br>我们在tEKS存储库中提供了一个相当完整的AWS实现，它抽象了很多复杂性（主要是mTLS部分），并允许进行很多定制。你也可以使用terraform-kubernetes-addons模块作为独立的组件。我们计划在未来支持其他云提供商。不要犹豫，通过Github上的任何一个项目的问题联系我们。<br>
<br>根据你的基础设施和需求，有许多可能适合你的Thanos实现。<br>
<br>如果你想深入研究Thanos，可以查看他们的官方kube-thanos存储库，以及他们<a href="https://thanos.io/tip/operating/cross-cluster-tls-communication.md/">关于跨集群通信的建议</a>。<br>
<br>当然，我们很乐意帮助你设置你的云原生监控堆栈，欢迎联系我们<a href="mailto:contact@particule.io">contact@particule.io</a>:)<br>
<br>你也可以每天通过CNCF/Kubernetes Slack频道联系我们。<br>
<br><strong>作者：</strong> Kevin Lefevre, CTO & 联合创始人<br>
<br><strong>原文链接：<a href="https://particule.io/en/blog/thanos-monitoring/">Multi-Cluster Monitoring with Thanos</a>（翻译：刘志超）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            