
---
title: 'Kubernetes 配置文件描述的基本概念'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=7325'
author: Dockone
comments: false
date: 2021-05-06 00:03:05
thumbnail: 'https://picsum.photos/400/300?random=7325'
---

<div>   
<br>为了方便 <a href="https://github.com/sql-machine-learning/sqlflow">SQLFlow</a> 和 <a href="https://github.com/sql-machine-learning/elasticdl">ElasticDL</a> 的开发者了解 Kubernetes，本文梳理 Kubernetes 背后的复杂概念体系中最接近用户使用的几个。<br>
<br>为了理解方便，本文会用 Kubernetes 和 Linux 等单机操作系统对应，并称之为分布式操作系统。之前沈凋墨在《<a href="https://zhuanlan.zhihu.com/p/148782297">Kubernetes：微内核的分布式操作系统</a>》一文中用到这个类比，有读者较劲说 Kubernetes 不算分布式操作系统。追求字面和忽略内涵是我国文人的传统。为了方便大家理解，本文会无视传统继续用这个类比，以尝试简练清晰地表达内涵。<br>
<br>接下来，我们先解释这几个概念，然后看看在配置文件 $HOME/.kube/config 里这几个概念的具象化表示。<br>
<h3>基本概念</h3><h4>Cluster</h4>Kubernetes 是一套可定制的机群（cluster）管理软件。用户面对的首要概念就是这个cluster了。它可能是用户在某个公有云服务上购买的几个 VM 构成的，也可能是用户在个人电脑上用 minikube 这样的软件创建一个 VM 构成的。机群作为计算的硬件基础，对应个人电脑和手机。<br>
<h4>User</h4>和使用 Windows、macOS、Linux 这样的单机操作系统一样，用户要以某个身份去访问Kubernetes 这样的分布式操作系统管理的集群。在个人操作系统里，用户需要一个用户名（username）来标记自己，用一个密码（password）或者 TLS certificate 来验证自己（是自己）。在 Kubernetes 里，用户除了用密码，也可以用某种 token，或者 TLS certificate 来验明正身。<br>
<h4>Pod 和 Deployment</h4>我们习惯于在单机操作系统里启动一个“进程”（process）来执行一个“程序”（program），并且一个进程可以有多个线程，线程是操作系统调度的最小单位。<br>
<br>在 Kubernetes 上，对应进程的概念<strong>大致</strong>是 deployment，对应线程的概念<strong>大致</strong>是 Pod，对应程序的是 Docker image。Kubernetes 可以被定制使用各种 container engine，最常用的是 Docker。一个 deployment 里有一个或者多个 Pods。一个 Pod 通常对应一个 container，也可以对应多个 containers。<br>
<h4>Name</h4>当用户（user）在机群上运行 Pod 和 deployment 的时候，需要给每个 Pod 或者 deployment 取个名字。如果不取名字，Kubernetes 会给他们默认名字。就像一个线程有线程 ID，进程有进程 ID。<br>
<h4>Namespace</h4>既然有名字，名字就可以有“前缀”。Namespace 就像前缀。那么为什么需要给进程和线程 ID 加一个前缀呢？当然是为了方便分类。分类之后能做什么呢？可以对其实施群体操作，比如默认给予更高（低）的优先级和更多（少）的资源。<br>
<h4>Context</h4>当一个用户启动一个 Pod 或者 deployment 的时候，她需要说明是（1）什么身份（user）在（2）哪个机群（cluster）上启动，以及（3）默认的 namesapce。一个 Context 就是定义以上三点信息的。<br>
<h3>具象化表示</h3>对应 Kubernetes 初学者来说，可以下载执行 minikube 在本机创建一个由（一个）VM 构成的 Kubernetes 机群。minikube 程序会把自己创建的资源都放在 $HOME/.minikube 这个目录里。同时，为了让用户可以用 kubectl 这个标准 Kubernetes 客户端程序操作这个虚拟集群，minikube 还要修改 kubectl 使用的配置文件 $HOME/.kube/config，把自己创建的集群（cluster），这个集群上接受的用户（user），以及默认的 namespace 等信息写入默认 context 里。<br>
<br>以下是我的 iMac 上的 $HOME/.kube/config 的内容：<br>
<pre class="prettyprint">apiVersion: v1<br>
clusters:<br>
- cluster:<br>
certificate-authority: /Users/yi/.minikube/ca.crt<br>
server: https://192.168.64.6:8443<br>
name: minikube<br>
contexts:<br>
- context:<br>
cluster: minikube<br>
user: minikube<br>
name: minikube<br>
current-context: minikube<br>
kind: Config<br>
preferences: &#123;&#125;<br>
users:<br>
- name: minikube<br>
user:<br>
client-certificate: /Users/yi/.minikube/profiles/minikube/client.crt<br>
client-key: /Users/yi/.minikube/profiles/minikube/client.key<br>
</pre><br>
在 clusters 里定义了一个 cluster，name 是 minkube。在 users 里定义了一个用户，名字也是 minikube。这个 cluster 有一个 certificate 叫 ca.crt，这个用户也有一个 certificate 叫 client.crt。这些都是 minikube 程序在创建机群的时候创建的。关于 certificate 的原理，感兴趣的读者可以参考《<a href="https://zhuanlan.zhihu.com/p/26684020">TLS完全指南（零）</a>》。<br>
<br>这个 cluster 的 API server 监听虚拟机 192.168.64.6 上的 8443 端口。当我们运行 kubectl 命令创建和操作 Pods 以及 deployments 的时候，kubectl 就是访问这个 API server 的 RESTful 服务，与之交互的。<br>
<br>上述文件中定义了一个 context，把 minikube 集群和 minikube 用户联系起来。这里没有描述 namespace，所以用的是默认 namespace。这个 context 的名字也叫 minikube。而 current-context 的值就是这个 context 的名字。<br>
<br>此时，当我用 kubectl 命令创建一个 Pod 的时候，不需要指定以什么身份在哪个机群上创建 Pod，kubectl 通过 current-context 就知道这些默认信息了。<br>
<br>至于如何为一个 cluster 创建多个 namespace，以及如何用这些 namespace 来限制用户的操作权限，后面再谈。<br>
<br>原文链接：<a href="https://zhuanlan.zhihu.com/p/259692468" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/259692468</a>，作者：王益
                                
                                                              
</div>
            