
---
title: 'Acorn：用于Kubernetes的轻量级且可移植的PaaS'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/e4d006cc93aacde112553a2fc8b5d423.png'
author: Dockone
comments: false
date: 2022-09-09 03:31:21
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/e4d006cc93aacde112553a2fc8b5d423.png'
---

<div>   
<br><a href="https://acorn.io/">Acorn</a>是Rancher创始人推出的一个新的应用程序部署框架，它非常接近我对运行在Kubernetes上的开发环境的期望。<br>
<br>长期以来，我一直主张一种简化的方法来开发和部署以Kubernetes为目标的应用程序。我之前<a href="https://thenewstack.io/azure-container-apps-do-we-need-yet-another-managed-container-service/">强调</a>需要一个可移植的、透明的、开源的应用程序层，该应用程序层将始终部署在开发人员笔记本电脑中的Minikube集群或在公共云中配置的大型多节点集群内运行。<br>
<br>作为高人气Kubernetes发行版K3s缔造者Darren Shepherd及其团队的开发成果，Acorn从Rancher身上继承了不少颇受云原生社区好评的设计原则。这是一套开源、简单、轻量化且可移植的框架，用于在Kubernetes上部署和扩展微服务。<br>
<br>使用Acorn的开发人员和运维人员无需了解Kubernetes的具体细节。如果他们了解Volumes、Secrets、ConfigMaps和Ingress等内部结构，那将非常棒。Acorn用自己的类JSON领域特定语言（DSL）抽象了Kubernetes的复杂性，以描述基于微服务设计模式的现代应用程序。<br>
<br>像Cloud Foundry这样的PaaS的目标是将代码推送到运行时并使用URL。Acorn正是专注于接受源代码或容器镜像并发布端点的工作流程。在后台，它完成了与Kubernetes API协商以创建资源和连接它们所需的管道的繁重工作。<br>
<br>尽管Amazon Web Services的<a href="https://aws.amazon.com/apprunner/">App Runner</a>、<a href="https://azure.microsoft.com/en-us/services/container-apps/">Azure Container Apps</a>和<a href="https://cloud.google.com/run">Google Cloud Run</a>等努力为部署容器化工作负载带来类似PaaS的体验，但它们仅限于公有云环境并且不可移植。Acorn是少数几个可以从开发人员笔记本电脑上运行的<a href="https://kind.sigs.k8s.io/">Kind</a>集群无缝扩展到云中的多节点集群的框架之一。<br>
<br>本文分析了Acorn的架构，并深入了解Acorn部署如何转换为Kubernetes对象。<br>
<br>让我们详细了解一下。<br>
<br><h3>在Minikube中设置环境</h3>在Mac上安装<a href="https://minikube.sigs.k8s.io/docs/">Minikube</a>并在其上启用Nginx Ingress。Ingress是Acorn最重要的先决条件之一。<br>
<pre class="prettyprint">minikube addons enable ingress<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/e4d006cc93aacde112553a2fc8b5d423.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/e4d006cc93aacde112553a2fc8b5d423.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
使用Homebrew安装Acorn CLI，并检查其版本以确保已安装。<br>
<pre class="prettyprint">brew install acorn-io/cli/acorn<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/1ad6e9d7cd9878a3c8df1cc0056107ef.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/1ad6e9d7cd9878a3c8df1cc0056107ef.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们现在准备在Minikube中安装Acorn。运行<code class="prettyprint">acorn init</code>以配置Minikube。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/ab65bc787a6ccbff0a19c9cfde9e48df.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/ab65bc787a6ccbff0a19c9cfde9e48df.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在Kubernetes集群中安装Acorn会创建一组资源来处理应用程序的构建时间和运行时要求。让我们从namespaces开始。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/76cbcf285c62e84e257a1705a6685833.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/76cbcf285c62e84e257a1705a6685833.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<code class="prettyprint">acorn-system</code> namespaces包含API和控制器，它们是运行时环境的组件。在开发环境中运行时，相同的namespaces可以选择运行镜像构建器和镜像注册表。另一个namespaces <code class="prettyprint">acorn</code>是为应用程序保留的，我们将在下一节中探讨。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/a4b87282bc586661bd0b7ba33774bd86.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/a4b87282bc586661bd0b7ba33774bd86.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
安装程序仅在集群中创建一个自定义资源定义（CRD）。CRD <code class="prettyprint">AppInstance.internal.acorn.io</code>映射到集群内运行的Acorn应用程序上。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/23dbf24819f59e5beeda6e3169b7660d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/23dbf24819f59e5beeda6e3169b7660d.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Acorn API服务器通过聚合与Kubernetes API服务器关联。Acorn CLI与API服务器<code class="prettyprint">api.acorn.io</code>对话。由于Acorn利用Kubernetes API聚合，CLI只需要Acorn API组的RBAC权限。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/e2980911e900b8f87f76d583b2abea32.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/e2980911e900b8f87f76d583b2abea32.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
API服务器将入站请求传递给Acorn控制器，该控制器将应用程序定义转换为适当的Kubernetes资源，例如Deployments、ConfigMaps、Secrets和Volumes。控制器负责通过创建和终止下游Kubernetes资源来管理Acorn应用程序的生命周期。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/05942e01a4afc70c0fc78e89fc6d17c8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/05942e01a4afc70c0fc78e89fc6d17c8.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>部署Acorn应用程序</h3>让我们从基于Nginx镜像的单个Web服务器创建最简单的Acorn应用程序开始。<br>
<br>在一个空目录中创建一个<code class="prettyprint">Acornfile</code>包含以下内容的目录：<br>
<pre class="prettyprint">containers: &#123;<br>
web: &#123;<br>
image: "nginx"<br>
ports: &#123;<br>
publish: "80/http"<br>
&#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
该定义是不言自明的。我们基于Docker注册表中的Nginx镜像启动一个名为“web”的容器，并使其在端口80上可用。<br>
<br>使用以下命令运行Acornfile：<br>
<pre class="prettyprint">acorn run  .<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/6161637d4cd1b1f1c22a62e06662e100.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/6161637d4cd1b1f1c22a62e06662e100.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
由于我们没有为应用程序提供名称，因此Acorn为应用程序指定了一个随机名称，即proud-silence。<br>
<br>当我们调用run命令时，Acorn创建了一个OCI清单并将其推送到在namespace内运行的内部注册表服务<code class="prettyprint">acorn-system</code>上。也可以为这些OCI工件使用外部注册表。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/1db2abe22b3045af61dfa0e6bb9f19b2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/1db2abe22b3045af61dfa0e6bb9f19b2.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
让我们通过运行以下命令获取访问应用程序的URL：<br>
<pre class="prettyprint">acorn apps<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/4e843d6cd27eaa238e7b86481afd01d1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/4e843d6cd27eaa238e7b86481afd01d1.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
让我们访问Web服务器来测试应用程序。<br>
<pre class="prettyprint">curl  -H  "host: web.proud-silence.local.on-acorn.io"  `minikube ip`<br>
</pre><br>
现在，让我们看看这个简单的应用程序对我们的Kubernetes集群做了什么。<br>
<br>首先，我们注意到有一个新的namespace作为应用程序的边界。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/6eee1429d74cef39bf2437a3c10da809.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/6eee1429d74cef39bf2437a3c10da809.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
让我们检查一下这个namespace。正如预期的那样，app run命令已经创建了一个Kubernetes Deployment、ReplicaSet、Pod和一个集群IP服务。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/312e7f868a3a1475f804aa50edfe62cf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/312e7f868a3a1475f804aa50edfe62cf.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
集群IP服务通过一个Ingress资源暴露给外界，我们稍后会探讨。<br>
<br>当我们检查<code class="prettyprint">acorn</code> namespace时，我们会找到CRD的实例AppInstance。<br>
<pre class="prettyprint">kubectl get appinstances -n acorn<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/dc7d84da6637826a45d47308d695811f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/dc7d84da6637826a45d47308d695811f.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
重温Ingress的想法来暴露Web应用程序，让我们看看我们是否可以在应用程序namespace中找到一个Ingress资源。<br>
<pre class="prettyprint">kubectl get ingress  -n  proud-silence-f6db18f8-c38<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220829/154e1a039d3fa4794c19e67638b1ab9c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220829/154e1a039d3fa4794c19e67638b1ab9c.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
每个“发布”端口的Acorn应用程序都会在Kubernetes中创建一个关联的入口对象。<br>
<br>由于应用程序按预期运行，它现在可以被标记并推送到外部注册表。管理工作负载的运营团队可以将其部署到生产集群，而无需了解应用程序的内部结构。<br>
<br>Acorn让我着迷的是它的简单性和便携性。它将Kubernetes视为部署、扩展和运行应用程序的理想运行时环境，无需任何假设。它不会篡改集群并部署最少的资源集，足以运行微服务。从某种意义上说，它是真正可移植的，当我们从开发集群上下文切换到另一个并部署应用程序时，它会被推送到生产集群。<br>
<br>Acorn深受Docker的影响，并遵循一些通用的模式来运行多容器应用程序。与Cloud Foundry一样，它也支持绑定现有服务，例如部署在其他应用程序中的数据库和缓存。<br>
<br>一旦Acorn支持直接从包含Acornfile的Git存储库进行部署的能力，DevOps就可以非常轻松地管理基于微服务的应用程序。<br>
<br>在本系列的下一部分中，我将展示一个基于Acorn的微服务应用程序的真实示例，该应用程序在开发环境和生产集群中运行。敬请关注。<br>
<br><strong>原文链接：<a href="https://thenewstack.io/acorn-a-lightweight-portable-paas-for-kubernetes/">Acorn, a Lightweight, Portable PaaS for Kubernetes</a>（翻译：李鹏）</strong>
                                
                                                              
</div>
            