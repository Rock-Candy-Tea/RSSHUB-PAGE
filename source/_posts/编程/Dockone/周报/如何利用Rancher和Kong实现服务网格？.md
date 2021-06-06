
---
title: '如何利用Rancher和Kong实现服务网格？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210604001433105.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
author: Dockone
comments: false
date: 2021-06-06 00:39:15
thumbnail: 'https://img-blog.csdnimg.cn/20210604001433105.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
---

<div>   
<br>服务网格（Service mesh）是当前新兴的架构模式，越来越受到人们的青睐。与Kubernetes一起，服务网格可以形成一个强大的平台，它可以解决在微服务集群或服务基础设施上发现的高度分布式环境中出现的技术需求。服务网格是一个专门的基础设施层，用于促进微服务之间的服务到服务通信。<br>
<br>服务网格解决了基于微服务的应用中典型的通信需求，包括加密隧道、健康检查、断路器、负载均衡以及流量许可。如果离开微服务来解决这些需求，会导致开发过程中产生高昂的费用和耗时。<br>
<br>在本文中，我们将对服务网格架构模式解决的最常见的微服务通信需求进行概述。<br>
<br><h2>微服务动态和内在挑战</h2>当你意识到微服务实现了相当多的与最初分配给它们的业务逻辑无关的代码时，问题就出现了。此外，有可能你有多个微服务在非标准化的流程中实现了类似的功能。换句话说，微服务开发团队应该专注于业务逻辑，并将低级通信能力留给特定的层。<br>
<br>继续推进我们的方案，需要考虑微服务的内在动态。在给定的时间内，你可能由于以下几个原因而拥有一个微服务的多个实例：<br>
<ul><li>吞吐量（Throughput）：根据传入的请求，你可能拥有更多或更少的微服务实例</li><li>金丝雀发布</li><li>蓝绿部署</li><li>A/B测试</li></ul><br>
<br>简而言之，微服务到微服务的通信有特定的需求和问题需要解决。以下图片展示了这一方案：<br>
<br><img src="https://img-blog.csdnimg.cn/20210604001433105.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt referrerpolicy="no-referrer"><br>
<br>该图示描述了几个技术挑战。显然，Microservice 1的主要职责是均衡所有Microservice 2实例之间的负载。因此，Microservice 1必须弄清楚我们在请求时刻有多少个Microservice 2实例。换句话说，Microservice 1必须实现服务发现和负载均衡。<br>
<br>另一方面，Microservice 2必须实现一些服务注册功能以告知Microservice 1何时有全新的实例。<br>
<br>想要拥有一个完全动态的环境，以下这些功能应该是微服务开发的一部分：<br>
<ul><li>流量控制：负载均衡的自然演变。我们想指定应该发送到每个Microservice 2实例的请求数量。 在Microservice<br>
1和2之间加密通信</li><li>借助断路器和健康检查以解决和克服网络问题</li></ul><br>
<br>总而言之，主要问题是开发团队花费了大量资源编写十分复杂的代码，而这些代码与微服务预期交付的业务逻辑不直接相关。<br>
<br><h2>有潜力的解决方案</h2>如何将所有微服务都可以调用的外部标准化组件中的所有非功能和操作功能外部化？例如，下图编译了所有功能，这些功能不属于给定的微服务。因此，在确定所有功能之后，我们需要决定在哪里实现它们。<br>
<br><img src="https://img-blog.csdnimg.cn/20210604001554196.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br><strong>Solution #1 ：将所有功能封装在一个library中</strong><br>
<br>开发者将负责调用library提供的函数来解决微服务通信需求。<br>
<br>这个解决方案有几个缺点：<br>
<br>这是一个紧密耦合的解决方案，意味着微服务高度依赖于library<br>
这个模式对于分布和升级新版本的library来说并不容易<br>
这不符合微服务多语言的原则，因为这会将不同的编程语言应用于不同的上下文。<br>
<br><strong>Solution #2：透明代理（Transparent Proxy）</strong><br>
<br><img src="https://img-blog.csdnimg.cn/20210604001716992.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>这个解决方案实现了同样的功能集合。但是，采用了一种非常不同的方法：每个微服务都有一个特定的组件，扮演代理的角色，负责处理它的传入和传出流量。代理解决了我们之前描述的库的缺点，具体如下：<br>
<ul><li>代理是透明的，这意味着微服务不会意识到它正在附近运行并实现了与其他微服务进行通信所需的所有功能。</li><li>由于它是一个透明的代理，开发者不需要改变代码来引用代理。因此，从微服务开发的角度来看，升级代理将是一个并不会对开发流程造成太大影响。</li><li>代理可以使用微服务使用的不同技术和编程语言进行开发。</li></ul><br>
<br><strong>服务网格架构模式</strong><br>
<br>虽然透明代理的方法给微服务开发团队和微服务通信需求带来了一些好处，但仍有一些缺失的部分：<br>
<ul><li>代理只是执行策略来实现通信需求，例如负载均衡、金丝雀发布等。</li><li>由什么来负责定义这样的策略，并在所有运行的代理上发布呢？</li></ul><br>
<br>解决方案架构需要另一个组件，这些组件将被管理员用来定义策略，它将负责向代理传播策略。<br>
<br>以下图片展示了最终架构，也就是服务网格模式：<br>
<br><img src="https://img-blog.csdnimg.cn/20210604001856310.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>如你所见，该模式包含了我们所描述的两个主要组件。<br>
<ul><li>数据平面：也被称为sidecar，它扮演着透明代理的角色。同样，每个微服务都会有自己的数据平面，拦截所有的入站和出站流量，并应用之前描述的策略。</li><li>控制平面：由管理员用来定义策略并发布到数据平面。</li></ul><br>
<br>一些重要的事情需要注意：<br>
<ul><li>这是一个 "push-based "的架构。数据平面不做 "调用 "来获取策略——那将会消耗网络。</li><li>数据平面通常向控制平面或特定的基础设施报告使用指标。</li></ul><br>
<br><h2>手把手教你使用Rancher、Kong和Kong Mesh</h2>Kong提供了一个企业级的综合服务连接平台，其包括了API gateway、Kubernetes ingress controller以及服务网格实现。该平台允许用户部署多个环境，如本地、混合云、多区域以及多云环境。<br>
<br>让我们借助运行在独立于云架构（cloud-agnostic）的Kubernetes集群上的金丝雀发布来实现服务网格，该集群可能包括GKE集群或任何其他的Kubernetes发行版。服务网格将由Kong Mesh实现，并由Kong for Kubernetes作为Kubernetes Ingress Controller。一般而言，ingress controller负责定义进入你的Kubernetes集群的入口点，暴露部署在其内部的微服务，并对其实行消费策略。<br>
<br>首先，确保你已经安装Rancher以及正在运行一个由Rancher管理的Kubernetes集群。在登录到Rancher之后，选在我们将要使用的Kubernetes集群，在本例中为“kong-rancher”。点击Cluster Explorer。你将会重定向到以下页面：<br>
<br><img src="https://img-blog.csdnimg.cn/2021060400193837.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>现在，让我们从服务网格开始：<br>
<br><strong>1、 Kong Mesh Helm Chart</strong><br>
<br>回到Rancher Cluster Manger主页并再次选择你的集群。点击菜单栏的“Tools”选项然后点击Catalogs，以创建一个新的catalog。点击Add Catalog按钮，将Kong Mesh的Helm chart收录其中（<a href="https://kong.github.io/kong-mesh-charts/" rel="nofollow" target="_blank">https://kong.github.io/kong-mesh-charts/</a>）。<br>
<br>选择Global作为范围，Helm v3作为Helm版本。<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002012609.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>现在点击Apps和Launch来查看在Catalog中可用的Kong Mesh。请注意，Kong作为Rancher的合作伙伴默认提供了Kong for Kubernetes的Helm chart：<br>
<br><img src="https://img-blog.csdnimg.cn/2021060400205873.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>2、 安装Kong Mesh<br>
<br>点击顶部菜单栏Namespaces选项并创建一个“kong-mesh-system”命名空间。<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002047133.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>将鼠标移到kong-rancher顶部菜单选项上，点击kong-rancher活动集群。<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002110276.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>点击Launch kubetcl<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002118408.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>创建一个名为“license.json”的文件，用于存放你从Kong Mesh收到的license。格式如下：<br>
<br><pre class="prettyprint">&#123;“license”:<br>
&#123;“version”:1,“signature”:“6a7c81af4b0a42b380be25c2816a2bb1d761c0f906ae884f93eeca1fd16c8b5107cb6997c958f45d247078ca50a25399a5f87d546e59ea3be28284c3075a9769”,“payload”:<br>
&#123;“customer”:“Kong_SE_Demo_H1FY22”,“license_creation_date”:“2020-11-30”,“product_subscription”:“Kong Enterprise Edition”,“support_plan”:“None”,“admin_seats”:“5”,“dataplanes”:“5”,“license_expiration_date”:“2021-06-30”,“license_key”:“XXXXXXXXXXXXX”<br>
</pre>&#125;&#125;&#125;<br>
<br>现在使用以下命令创建一个Kubernetes通用密钥：<br>
<pre class="prettyprint">kubectl create secret generic kong-mesh-license -n kong-mesh-system --from-file=./license.json<br>
</pre><br>
<br>关闭kubectl会话，点击Default项目以及顶部菜单栏的Apps。点击Launch按钮并选择kong-mesh Helm chart。<br>
<br>点击Use an existing namespace并选择我们刚刚创建的那个。这有几个参数(<a href="https://artifacthub.io/packages/helm/kong-mesh/kong-mes" rel="nofollow" target="_blank">https://artifacthub.io/package ... g-mes</a>h)来配置Kong Mesh，但我们将保留所有默认值。点击Launch之后，你应该看到Kong Mesh应用程序部署完成。<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002200811.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>你可以再次使用Rancher Cluster Explorer来检查安装。点击左侧菜单的Pods并选择kong-mesh-system的命名空间。<br>
<br>你也可以像这样使用kubectl：<br>
<pre class="prettyprint">NAMESPACE          NAME                                                      READY   STATUS    RESTARTS   AGE<br>
cattle-system      cattle-cluster-agent-785fd5f54d-r7x8r                     1/1     Running   0          75m<br>
fleet-system       fleet-agent-77c78f9c74-f97tv                              1/1     Running   0          75m<br>
kong-mesh-system   kuma-control-plane-5b9c6f4598-nvq8q                       1/1     Running   0          16m<br>
kube-system        event-exporter-gke-666b7ffbf7-n9lfl                       2/2     Running   0          76m<br>
kube-system        fluentbit-gke-xqsdv                                       2/2     Running   0          76m<br>
kube-system        gke-metrics-agent-gjrqr                                   1/1     Running   0          76m<br>
kube-system        konnectivity-agent-4c4hf                                  1/1     Running   0          76m<br>
kube-system        kube-dns-66d6b7c877-tq877                                 4/4     Running   0          76m<br>
kube-system        kube-dns-autoscaler-5c78d65cd9-5hcxs                      1/1     Running   0          76m<br>
kube-system        kube-proxy-gke-c-kpwnf-default-0-be059c1c-49qp            1/1     Running   0          76m<br>
kube-system        l7-default-backend-5b76b455d-v6dvg                        1/1     Running   0          76m<br>
kube-system        metrics-server-v0.3.6-547dc87f5f-qntjf                    2/2     Running   0          75m<br>
kube-system        prometheus-to-sd-fdf9j                                    1/1     Running   0          76m<br>
kube-system        stackdriver-metadata-agent-cluster-level-68d94db6-64n4r   2/2     Running   1          75m<br>
</pre><br>
<br><strong>3、 微服务部署</strong><br>
<br>我们的Service Mesh部署是基于一个简单的微服务到微服务的通信场景。由于我们运行的是金丝雀发布，被调用的微服务有两个版本：<br>
<br>“magnanimo”：通过Kong暴露Kubernetes ingress controller。<br>
“benigno”：提供了一个 “hello” endpoint，在这个端点中，它呼应了当前的datetime。它有一个金丝雀发布，会发送一个稍微不同的响应。<br>
<br>下图展示了这一架构：<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002400918.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>创建一个带有sidecar注入注释的命名空间。你可以再次使用Rancher Cluster Manager：选择你的集群，然后单击Projects/Namespaces。点击Add Namespace。输入 “kong-mesh-app” 作为名称，并包含一个带有 “kuma.io/sidecar-injection” 键和 “enabled” 作为其值的注释。<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002416870.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>当然，你也可以选择使用kubectl<br>
<pre class="prettyprint">kubectl create namespace kong-mesh-app<br>
<br>
kubectl annotate namespace kong-mesh-app kuma.io/sidecar-injection=enabled<br>
<br>
Submit the following declaration to deploy Magnanimo injecting the Kong Mesh data plane<br>
<br>
cat <<EOF | kubectl apply -f -<br>
<br>
apiVersion: apps/v1<br>
<br>
kind: Deployment<br>
<br>
metadata:<br>
<br>
name: magnanimo<br>
<br>
namespace: kong-mesh-app<br>
<br>
spec:<br>
<br>
replicas: 1<br>
<br>
selector:<br>
<br>
matchLabels:<br>
<br>
app: magnanimo<br>
<br>
template:<br>
<br>
metadata:<br>
<br>
labels:<br>
<br>
app: magnanimo<br>
<br>
spec:<br>
<br>
containers:<br>
<ul><li>name: magnanimo</li></ul><br>
image: claudioacquaviva/magnanimo<br>
<br>
ports:<br>
<ul><li>containerPort: 4000</li></ul><br>
---<br>
<br>
apiVersion: v1<br>
<br>
kind: Service<br>
<br>
metadata:<br>
<br>
name: magnanimo<br>
<br>
namespace: kong-mesh-app<br>
<br>
labels:<br>
<br>
app: magnanimo<br>
<br>
spec:<br>
<br>
type: ClusterIP<br>
<br>
ports:<br>
<ul><li>port: 4000</li></ul><br>
name: http<br>
<br>
selector:<br>
<br>
app: magnanimo<br>
<br>
EOF<br>
</pre><br>
<br>使用Rancher Cluster Manager检查你的部署。将鼠标移动至kong-rancher菜单上，点击Default项目，可以看到当前的部署情况：<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002454885.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>点击magnanimo检查部署的细节，包括其pods：<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002507158.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>点击magnanimo pod，检查其内部运行的容器。<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002518266.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>我们可以看到，pod有两个运行的容器：<br>
<ul><li>magnanimo：微服务实际运行的地方。</li><li>kuma-sidecar：在部署的时候注入，作为Kong Mesh的数据平面。</li></ul><br>
<br>同理，部署Benigno的时候，也有自己的sidecar：<br>
<pre class="prettyprint">cat <<EOF | kubectl apply -f -<br>
<br>
apiVersion: apps/v1<br>
<br>
kind: Deployment<br>
<br>
metadata:<br>
<br>
name: benigno-v1<br>
<br>
namespace: kong-mesh-app<br>
<br>
spec:<br>
<br>
replicas: 1<br>
<br>
selector:<br>
<br>
matchLabels:<br>
<br>
app: benigno<br>
<br>
template:<br>
<br>
metadata:<br>
<br>
labels:<br>
<br>
app: benigno<br>
<br>
version: v1<br>
<br>
spec:<br>
<br>
containers:<br>
<ul><li>name: benigno</li></ul><br>
image: claudioacquaviva/benigno<br>
<br>
ports:<br>
<ul><li>containerPort: 5000</li></ul><br>
---<br>
<br>
apiVersion: v1<br>
<br>
kind: Service<br>
<br>
metadata:<br>
<br>
name: benigno<br>
<br>
namespace: kong-mesh-app<br>
<br>
labels:<br>
<br>
app: benigno<br>
<br>
spec:<br>
<br>
type: ClusterIP<br>
<br>
ports:<br>
<ul><li>port: 5000</li></ul><br>
name: http<br>
<br>
selector:<br>
<br>
app: benigno<br>
<br>
EOF<br>
<br>
And finally, deploy Benigno canary release. Notice that the canary release will be abstracted by the same Benigno Kubernetes Service created before:<br>
<br>
cat <<EOF | kubectl apply -f -<br>
<br>
apiVersion: apps/v1<br>
<br>
kind: Deployment<br>
<br>
metadata:<br>
<br>
name: benigno-v2<br>
<br>
namespace: kong-mesh-app<br>
<br>
spec:<br>
<br>
replicas: 1<br>
<br>
selector:<br>
<br>
matchLabels:<br>
<br>
app: benigno<br>
<br>
template:<br>
<br>
metadata:<br>
<br>
labels:<br>
<br>
app: benigno<br>
<br>
version: v2<br>
<br>
spec:<br>
<br>
containers:<br>
<ul><li>name: benigno</li></ul><br>
image: claudioacquaviva/benigno\_rc<br>
<br>
ports:<br>
<ul><li>containerPort: 5000</li></ul><br>
EOF<br>
</pre><br>
<br>使用以下命令检查部署和Pods：<br>
<br><pre class="prettyprint">&#123;&#123;&#123;$ kubectl get pod --all-namespaces<br>
NAMESPACE          NAME                                                      READY   STATUS    RESTARTS   AGE<br>
cattle-system      cattle-cluster-agent-785fd5f54d-r7x8r                     1/1     Running   0          75m<br>
fleet-system       fleet-agent-77c78f9c74-f97tv                              1/1     Running   0          75m<br>
kong-mesh-app      benigno-v1-fd4567d95-drnxq                                2/2     Running   0          110s<br>
kong-mesh-app      benigno-v2-b977c867b-lpjpw                                2/2     Running   0          30s<br>
kong-mesh-app      magnanimo-658b67fb9b-tzsjp                                2/2     Running   0          5m3s<br>
kong-mesh-system   kuma-control-plane-5b9c6f4598-nvq8q                       1/1     Running   0          16m<br>
kube-system        event-exporter-gke-666b7ffbf7-n9lfl                       2/2     Running   0          76m<br>
kube-system        fluentbit-gke-xqsdv                                       2/2     Running   0          76m<br>
kube-system        gke-metrics-agent-gjrqr                                   1/1     Running   0          76m<br>
kube-system        konnectivity-agent-4c4hf                                  1/1     Running   0          76m<br>
kube-system        kube-dns-66d6b7c877-tq877                                 4/4     Running   0          76m<br>
kube-system        kube-dns-autoscaler-5c78d65cd9-5hcxs                      1/1     Running   0          76m<br>
kube-system        kube-proxy-gke-c-kpwnf-default-0-be059c1c-49qp            1/1     Running   0          76m<br>
kube-system        l7-default-backend-5b76b455d-v6dvg                        1/1     Running   0          76m<br>
kube-system        metrics-server-v0.3.6-547dc87f5f-qntjf                    2/2     Running   0          75m<br>
kube-system        prometheus-to-sd-fdf9j                                    1/1     Running   0          76m<br>
kube-system        stackdriver-metadata-agent-cluster-level-68d94db6-64n4r   2/2     Running   1          75m<br>
<br>
<br>
$ kubectl get service --all-namespaces<br>
NAMESPACE          NAME                   TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)                                                AGE<br>
default            kubernetes             ClusterIP   10.0.16.1     <none>        443/TCP                                                79m<br>
kong-mesh-app      benigno                ClusterIP   10.0.20.52    <none>        5000/TCP                                               4m6s<br>
kong-mesh-app      magnanimo              ClusterIP   10.0.30.251   <none>        4000/TCP                                               7m18s<br>
kong-mesh-system   kuma-control-plane     ClusterIP   10.0.21.228   <none>        5681/TCP,5682/TCP,443/TCP,5676/TCP,5678/TCP,5653/UDP   18m<br>
kube-system        default-http-backend   NodePort    10.0.19.10    <none>        80:32296/TCP                                           79m<br>
kube-system        kube-dns               ClusterIP   10.0.16.10    <none>        53/UDP,53/TCP                                          79m<br>
kube-system        metrics-server         ClusterIP   10.0.20.174   <none>        443/TCP                                                79m<br>
</pre>&#125;&#125;&#125;<br>
<br>你也可以使用Kong Mesh控制台来检查微服务和数据平面。在Terminal上运行以下命令：<br>
<pre class="prettyprint">kubectl port-forward service/kuma-control-plane -n kong-mesh-system 5681<br>
</pre><br>
<br>重定向你的浏览器到<a href="http://localhost:5681/gui" rel="nofollow" target="_blank">http://localhost:5681/gui</a>。点击Skip to Dashboard和All Data Plane Proxies：<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002611722.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>启动一个循环，看看金丝雀发布的运行情况。注意服务已经被部署为ClusterIP类型，所以你需要用 “port-forward”直接暴露它们。下一步将展示如何用Ingress Controller暴露服务。<br>
<br>在本地terminal上运行：<br>
<pre class="prettyprint">kubectl port-forward service/magnanimo -n kong-mesh-app 4000<br>
</pre><br>
<br>打开另一个Terminal，开始循环。请求要到Magnanimo提供的4000端口。路径“/hw2 ”将请求路由到Benigno服务，它后面有两个endpoint，与Benigno两个版本有关：<br>
<pre class="prettyprint">while [1]; do curl http://localhost:4000/hw2; echo; done<br>
</pre><br>
<br>你应该看到类似下方的结果：<br>
<pre class="prettyprint">Hello World, Benigno: 2020-11-20 12:57:05.811667<br>
Hello World, Benigno: 2020-11-20 12:57:06.304731<br>
Hello World, Benigno, Canary Release: 2020-11-20 12:57:06.789208<br>
Hello World, Benigno: 2020-11-20 12:57:07.269674<br>
Hello World, Benigno, Canary Release: 2020-11-20 12:57:07.755884<br>
Hello World, Benigno, Canary Release: 2020-11-20 12:57:08.240453<br>
Hello World, Benigno: 2020-11-20 12:57:08.728465<br>
Hello World, Benigno: 2020-11-20 12:57:09.208588<br>
Hello World, Benigno, Canary Release: 2020-11-20 12:57:09.689478<br>
Hello World, Benigno, Canary Release: 2020-11-20 12:57:10.179551<br>
Hello World, Benigno: 2020-11-20 12:57:10.662465<br>
Hello World, Benigno: 2020-11-20 12:57:11.145237<br>
Hello World, Benigno, Canary Release: 2020-11-20 12:57:11.618557<br>
Hello World, Benigno: 2020-11-20 12:57:12.108586<br>
Hello World, Benigno, Canary Release: 2020-11-20 12:57:12.596296<br>
Hello World, Benigno, Canary Release: 2020-11-20 12:57:13.093329<br>
Hello World, Benigno: 2020-11-20 12:57:13.593487<br>
Hello World, Benigno, Canary Release: 2020-11-20 12:57:14.068870<br>
</pre><br>
<br><strong>4、 控制金丝雀发布的成本</strong><br>
<br>正如我们所见，两个Benigno微服务发布的请求使用了循环策略。也就是说，我们无法控制金丝雀发布的花销。Service Mesh允许我们定义何时以及如何将金丝雀发布暴露给我们的consumer（在本例中指Magnanimo微服务）。<br>
<br>要定义一个策略来控制流向两个版本的流量，需要使用下面这个声明。它说90%的流量应该流向当前版本，而只有10%的流量应该重定向到金丝雀发布。<br>
<pre class="prettyprint">cat <<EOF | kubectl apply -f -<br>
apiVersion: kuma.io/v1alpha1<br>
kind: TrafficRoute<br>
mesh: default<br>
metadata:<br>
namespace: default<br>
name: route-1<br>
spec:<br>
sources:<br>
- match:<br>
kuma.io/service: magnanimo\_kong-mesh-app\_svc\_4000<br>
destinations:<br>
- match:<br>
kuma.io/service: benigno\_kong-mesh-app\_svc\_5000<br>
conf:<br>
split:<br>
- weight: 90<br>
destination:<br>
kuma.io/service: benigno\_kong-mesh-app\_svc\_5000<br>
version: v1<br>
- weight: 10<br>
destination:<br>
kuma.io/service: benigno\_kong-mesh-app\_svc\_5000<br>
version: v2<br>
EOF<br>
</pre><br>
<br>应用声明之后，你应该看到如下结果：<br>
<pre class="prettyprint">Hello World, Benigno: 2020-11-20 13:05:02.553389<br>
Hello World, Benigno: 2020-11-20 13:05:03.041120<br>
Hello World, Benigno: 2020-11-20 13:05:03.532701<br>
Hello World, Benigno: 2020-11-20 13:05:04.021804<br>
Hello World, Benigno: 2020-11-20 13:05:04.515245<br>
Hello World, Benigno, Canary Release: 2020-11-20 13:05:05.000644<br>
Hello World, Benigno: 2020-11-20 13:05:05.482606<br>
Hello World, Benigno: 2020-11-20 13:05:05.963663<br>
Hello World, Benigno, Canary Release: 2020-11-20 13:05:06.446599<br>
Hello World, Benigno: 2020-11-20 13:05:06.926737<br>
Hello World, Benigno: 2020-11-20 13:05:07.410605<br>
Hello World, Benigno: 2020-11-20 13:05:07.890827<br>
Hello World, Benigno: 2020-11-20 13:05:08.374686<br>
Hello World, Benigno: 2020-11-20 13:05:08.857266<br>
Hello World, Benigno: 2020-11-20 13:05:09.337360<br>
Hello World, Benigno: 2020-11-20 13:05:09.816912<br>
Hello World, Benigno: 2020-11-20 13:05:10.301863<br>
Hello World, Benigno: 2020-11-20 13:05:10.782395<br>
Hello World, Benigno: 2020-11-20 13:05:11.262624<br>
Hello World, Benigno: 2020-11-20 13:05:11.743427<br>
Hello World, Benigno: 2020-11-20 13:05:12.221174<br>
Hello World, Benigno: 2020-11-20 13:05:12.705731<br>
Hello World, Benigno: 2020-11-20 13:05:13.196664<br>
Hello World, Benigno: 2020-11-20 13:05:13.680319<br>
</pre><br>
<br><strong>5、 安装Kong for Kubernetes</strong><br>
<br>让我们回到Rancher中安装我们的Kong for Kubernetes Ingress Controller，并控制服务网格的暴露。在Rancher Catalog页面中，点击Kong图标。接受默认值，然后点击Launch：<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002706837.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>你应该看到Kong和Kong Mesh这两个应用程序都已经部署完成：<br>
<br><img src="https://img-blog.csdnimg.cn/20210604002717317.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="图片" referrerpolicy="no-referrer"><br>
<br><img src="https://img-blog.csdnimg.cn/20210604002728634.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>再次使用kubectl检查安装：<br>
<pre class="prettyprint">$ kubectl get pod --all-namespaces<br>
NAMESPACE          NAME                                                      READY   STATUS    RESTARTS   AGE<br>
cattle-system      cattle-cluster-agent-785fd5f54d-r7x8r                     1/1     Running   0          84m<br>
fleet-system       fleet-agent-77c78f9c74-f97tv                              1/1     Running   0          83m<br>
kong-mesh-app      benigno-v1-fd4567d95-drnxq                                2/2     Running   0          10m<br>
kong-mesh-app      benigno-v2-b977c867b-lpjpw                                2/2     Running   0          8m47s<br>
kong-mesh-app      magnanimo-658b67fb9b-tzsjp                                2/2     Running   0          13m<br>
kong-mesh-system   kuma-control-plane-5b9c6f4598-nvq8q                       1/1     Running   0          24m<br>
kong               kong-kong-754cd6947-db2j9                                 2/2     Running   1          72s<br>
kube-system        event-exporter-gke-666b7ffbf7-n9lfl                       2/2     Running   0          85m<br>
kube-system        fluentbit-gke-xqsdv                                       2/2     Running   0          84m<br>
kube-system        gke-metrics-agent-gjrqr                                   1/1     Running   0          84m<br>
kube-system        konnectivity-agent-4c4hf                                  1/1     Running   0          84m<br>
kube-system        kube-dns-66d6b7c877-tq877                                 4/4     Running   0          84m<br>
kube-system        kube-dns-autoscaler-5c78d65cd9-5hcxs                      1/1     Running   0          84m<br>
kube-system        kube-proxy-gke-c-kpwnf-default-0-be059c1c-49qp            1/1     Running   0          84m<br>
kube-system        l7-default-backend-5b76b455d-v6dvg                        1/1     Running   0          85m<br>
kube-system        metrics-server-v0.3.6-547dc87f5f-qntjf                    2/2     Running   0          84m<br>
kube-system        prometheus-to-sd-fdf9j                                    1/1     Running   0          84m<br>
kube-system        stackdriver-metadata-agent-cluster-level-68d94db6-64n4r   2/2     Running   1          84m<br>
<br>
<br>
$ kubectl get service --all-namespaces<br>
NAMESPACE          NAME                   TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)                                                AGE<br>
default            kubernetes             ClusterIP      10.0.16.1     <none>          443/TCP                                                85m<br>
kong-mesh-app      benigno                ClusterIP      10.0.20.52    <none>          5000/TCP                                               10m<br>
kong-mesh-app      magnanimo              ClusterIP      10.0.30.251   <none>          4000/TCP                                               13m<br>
kong-mesh-system   kuma-control-plane     ClusterIP      10.0.21.228   <none>          5681/TCP,5682/TCP,443/TCP,5676/TCP,5678/TCP,5653/UDP   24m<br>
kong               kong-kong-proxy        LoadBalancer   10.0.26.38    35.222.91.194   80:31867/TCP,443:31039/TCP                             78s<br>
kube-system        default-http-backend   NodePort       10.0.19.10    <none>          80:32296/TCP                                           85m<br>
kube-system        kube-dns               ClusterIP      10.0.16.10    <none>          53/UDP,53/TCP                                          85m<br>
kube-system        metrics-server         ClusterIP      10.0.20.174   <none>          443/TCP                                                85m<br>
</pre><br>
<br><strong>6、 创建Ingress</strong><br>
<br>通过下面的声明，我们将通过一个Ingress和它的路由 “/route1” 来暴露Magnanimo微服务。<br>
<pre class="prettyprint">cat <<EOF | kubectl apply -f -<br>
apiVersion: extensions/v1beta1<br>
kind: Ingress<br>
metadata:<br>
name: route1<br>
namespace: kong-mesh-app<br>
annotations:<br>
konghq.com/strip-path: "true"<br>
spec:<br>
rules:<br>
- http:<br>
paths:<br>
- path: /route1<br>
backend:<br>
serviceName: magnanimo<br>
servicePort: 4000<br>
EOF<br>
</pre><br>
<br>现在，临时的 “port-forward” 暴露机制可以被正式的Ingress所取代。而我们的循环也可以开始消耗Ingress，结果如下：<br>
<pre class="prettyprint">&#123;while [1]; do curl http://35.222.91.194/route1/hw2; echo; done<br>
</pre>
                                
                                                              
</div>
            