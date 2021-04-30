
---
title: 'Kubernetes 的 Hello World 及其工作原理'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=7792'
author: Dockone
comments: false
date: 2021-04-30 00:14:00
thumbnail: 'https://picsum.photos/400/300?random=7792'
---

<div>   
<br>在《<a href="https://zhuanlan.zhihu.com/p/259692468">Kubernetes 配置文件描述的基本概念</a>》里介绍了一说到集群管理脑海中就会出现的几个概念。如果大家跃跃欲试，想用 kubectl 命令提交几个 Kubernetes 作业试试，则需要看看本文中涉及的几个概念。<br>
<h4>API Server</h4>每一个 Kubernetes 机群可以有一台或者多台机器。比如，用 minikube start 命令可以在一台 Linux 或者 macOS 机器上创建一个只有一台 VM 构成的微型 Kubernetes 机群。麻雀虽小，五脏俱全。其中一脏，就是在这台 VM 上运行的一个 RESTful API server —— Kubernetes 的 API server。<br>
<h4>kubectl</h4>用户用命令行工具 kubectl 和 Kubernetes API server 打交道，包括提交作业，运行分布式程序。不过既然 API server 是一个 RESTful API server，那么任何 HTTP 客户端工具，包括 wget 和 curl 其实都可以用。<br>
<h4>etcd</h4>用户不管是用 kubectl 还是 curl 发给 API server 的 RESTful calls 大致都是要写、读、或者修改某个 URI 的值。这些 URI 和值存在哪里呢？存在一个叫 etcd 的“不死”的存储系统里。比如，如果用户想要创建一个 Pod，则在本地写一个 YAML 文件描述这个 Pod（要执行哪个 Docker image 等），然后用 kubectl 或者 curl 把这个 YAML 文件发给 API server；而 API server 会把这个文件里的信息（用户的意图）写入到 etcd 里。<br>
<h4>Kubernetes Controllers</h4>把用户的意图（启动一个什么样的pod）写入 etcd 之后呢？这些意图是如何被 Kubernetes 注意到并且变为现实的呢？<br>
<br>在沈凋墨《<a href="https://zhuanlan.zhihu.com/p/148782297">Kubernetes: 微内核的分布式操作系统</a>》一文里，把 Kubernetes 类比成一个为内核的操作系统，比如 CMU Mach。微内核操作系统的系统核心功能由多个 system services 共同协作实现。在 Kubernetes 里，也是如此，只是 system services 对应 Kubernetes Controllers。<br>
<br>一个 controller 就是一个 Pod，和 Kubernetes 用户提交的其他 Pod 一样，运行在 Kubernetes 机群上。一个 controller 调用 etcd API 监视 etcd 里的内容变化。通常每一个 controller 会监控一类内容的变化。比如，Kubernetes 官方发布的一个 controller，名叫 Kubernetes scheduler 的，会监控和 Pod 相关的内容的变化。当发现有人往 etcd 里写了一个 Pod 描述，而系统中并不存在这个 Pod 的时候，scheduler 就会作如下工作来实现用户的意图：<br>
<ol><li>根据 scheduler 对机群各个节点（Node）的负载以及其他情况的了解，找到一个适合的 Node 来启动这个 Pod。</li><li>给这个 Node 上运行的一个程序 kubelet 发消息，命令它启动一个 Pod。</li></ol><br>
<br>因此，我们说，scheduler 是一个特殊的 controller。<br>
<h4>Kubernetes Operators</h4>既然是一个为内核的分布式操作系统，Kubernetes 就允许用户开发和部署各种各样的 controllers。第三方开发的，专门用来把一类现有的程序跑在 Kubernetes 上的 controller，在社区俗话里叫 operator。<br>
<br>比如，TensorFlow 项目提供一个 tf-operator，就是负责把分布式 TensorFlow 程序启动在 Kubernetes 机群上。TensorFlow API 和 TensorFlow runtime 允许用户开发和启动分布式作业；启动的时候，要手工启动每一个进程，并且通过设置环境变量的方式，让每个进程都知道其他进程的 IP 和端口，这样它们启动之后才能协作执行分布式训练。<br>
<br>TensorFlow 提供的这个 tf-operator 就是监控 etcd 里是否被人写入了一个类型是 tfjobs 的内容；如果是，它会调用 Kubernetes API（和 API server 通信）要求启动几个 Pod；同时要求把这几个 Pod 的 IP 地址写入 TensorFlow API 期待的一个环境变量里。这样一来，这些 Pod 启动后就执行对应的 Docker image 里的 TensorFlow 分布式训练程序，而这个分布式训练程序通过环境变量得知作业里所有进程的 IP 和端口。<br>
<br>社区贡献的类似的 operators 还有很多。有些把 Spark 作业启动在 Kubernetes 上，也有的负责启动 MySQL 等。<br>
<h4>Resource</h4>上文提及的 Pods 和 tf-job 都是 Kubernetes Resource。在 Kubernetes 里，resource 的名字会出现在 RESTful API 的 URL 的最末端（endpoint）。比如，下面命令列出用户可以查看的所有 Pods。<br>
<pre class="prettyprint">curl http://localhost:8001/api/v1/namespaces/default/pods<br>
</pre><br>
请注意，上面 URL 中的 endpoint 就是 resource name pods 了。<br>
<br>认真的读者会问，这个 locahost:8001 是怎么来的呢？这其实是 API sever 的一个 Web proxy server 的地址。是我运行 kubectl proxy 命令创建的。<br>
<br>那么为什么要创建这个 Proxy 呢？直接访问 API server 的地址不行吗？当然是可以的。只是那样的话，我的 curl 命令会很冗长，因为要提供验证用户身份必要的命令行参数。而这个 Proxy 是 kubectl 命令利用 $HOME/.kube/config 里的内容（包括身份验证信息）创建的，省去了我们通过 curl 附上身份验证信息的麻烦。<br>
<h4>Object</h4>上面命令会列出 Pods 这个 resource 里所有的实例（instances）。其中每个 instance 在 Kubernetes 的术语里叫一个 object。类似的，tfjob 这个 resource 也可以有多个 object，每个 object 对应一个分布式 TensorFlow 训练作业。<br>
<h4>Custom Resource</h4>上面提到的 Pods 这个 resource 是 Kubernetes 开发者定义的，所以就叫 resource 了。而 tfjobs 这个 resource 不是 Kubernetes 开发者定义的，而是 KubeFlow 项目的开发者定义的 —— 这种外人定义的 resource 叫做 custom resource。<br>
<br>一个 Pods 类型的 object 里要包含 Pod 执行的 Docker image name。一个 tfjobs 类型的 object 里要包含启动几个 worker pods。这些用户要填写的内容，就是 resource definition（或者理解成一个 C struct 类型定义）。Custom resource 的定义就叫 custom resource definition，简称 CRD。很多时候，社区里把 CRD 和 custom resource 混用。<br>
<br>我们可以运行命令 kubectl api-resources 来列出机群上的所有 resources。比如我的 minikube 机群包括如下 resources：<br>
<pre class="prettyprint">...<br>
pods                              po                   apps           <br>
deployments                       deploy               apps<br>
workflows                         wf                   argoproj.io<br>
...<br>
</pre><br>
其中 Pods 是 scheduler 定义的 resource；po 是其简写。deployment 也是 scheduler 定义的。workflows 是我安装的 Argo 项目提供的 resource；wf 是其简写。<a href="https://argoproj.github.io/">argoproj.io</a> 是什么呢？是 API Group。<br>
<h4>API Group 和 Version</h4>一个 Kubernetes Controller 通常关心一个 CRD。也就是说，它会监控 etcd 里符合它关注的 CRD 的 objects。而每个 R（Resource）又对应 API server URL 的 endpoint，那么给人的感觉是，用户访问 API server 的 URL 被根据 endpoint 分发给了不同的 controllers 去处理 —— 实际上不是直接分发，而是通过 API server 写 etcd 和 controllers 监控 etcd 实现的间接分发。总之是分发，也就是说一个 controller 实现了一部分 Kubernetes API —— 这一部分被称为一个 API group。<br>
<br>每个API group 有一个 version。格式是 vx，vxalpha，vxbeta，其中 x 是一个数字编号。要看看机群中有哪些 API groups 以及他们的 versions，可以用 kubectl api-versions 命令。在我的 minikube 机群里，输出包括：<br>
<pre class="prettyprint">...<br>
apps/v1<br>
argoproj.io/v1alpha1<br>
...<br>
</pre><br>
其中 apps/v1 是 scheduler 提供的 API group；v1 是其 version。<a href="https://argoproj.io/v1alpha1">argoproj.io/v1alpha1</a> 是因为我安装了 Argo 项目提供的 Kubernetes operator；v1lapha1 是其 version。<br>
<h3>实操一下</h3>在很多 Kubernetes 教程里，第一个实操的例子是启动一个 Pod。大概需要用户敲如下命令：<br>
<pre class="prettyprint">cat <<EOF | kubectl apply -f -<br>
apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
name: my-pod<br>
spec:<br>
replicas: 1<br>
template:<br>
metadata:<br>
  labels:<br>
    app: whatever<br>
spec:<br>
  containers:<br>
    - name: shell<br>
      image: centos:7<br>
      command:<br>
        - sh<br>
        - '-c'<br>
        - echo "I will just print something here and then exit"<br>
EOF<br>
</pre><br>
一般教程不会详解上述命令里 YAML 的内容，而是留待日后再说哦。不过我们的顺序是反过来的 —— 先介绍 Kubernetes 的原理，再举例，所以大家应该已经可以看懂了：<br>
<ul><li>apiVersion: apps/v1 是一个 API group 和 version。其背后是 Kubernetes scheduler。也就是说，这个创建操作会通过 etcd 被导向 Kubernetes 的 scheduler。</li><li>kind: Deployment 是 resource 的名字。</li><li>metadata.name: my-pod 是 object 的名字。</li><li>spec 里指定的就是 resource 要求大家填写的内容了。</li></ul><br>
<br>原文链接：<a href="https://zhuanlan.zhihu.com/p/259698755" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/259698755</a>，作者：王益
                                
                                                              
</div>
            