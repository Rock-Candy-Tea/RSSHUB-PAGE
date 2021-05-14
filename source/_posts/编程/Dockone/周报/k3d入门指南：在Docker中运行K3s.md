
---
title: 'k3d入门指南：在Docker中运行K3s'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210514103015645.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70#pic_center'
author: Dockone
comments: false
date: 2021-05-14 04:13:08
thumbnail: 'https://img-blog.csdnimg.cn/20210514103015645.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70#pic_center'
---

<div>   
<br><img src="https://img-blog.csdnimg.cn/20210514103015645.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
在本文中，我们将简单了解k3d，这是一款可让您在安装了Docker的任何地方运行一次性Kubernetes集群的工具，此外在本文中我们还将探讨在使用k3d中可能会出现的一切问题。 <br>
<h2>什么是k3d？</h2>k3d是一个小型程序，用于在Docker中运行K3s集群。 K3s是经过CNCF认证的轻量级Kubernetes发行和沙箱项目。它是为资源有限环境设计的，被打包为单个二进制文件，所需RAM小于512MB。 要了解有关K3s的更多信息，请查看我们之前的公众号文章及B站上的视频。<br>
<br>k3d借助从K3s仓库构建的Docker镜像在安装了Docker的任何机器上的Docker容器中启动多个K3s节点。 这样，一台物理（或虚拟）机（称为Docker Host）可以运行多个K3s集群，每个集群同时有多个server和agent节点。<br>
<h2>k3d能做什么？</h2>2021年1月，发布k3dv4.0.0，包含以下功能：<br>
<ul><li>创建/停止/启动/删除/扩大/缩小K3s集群（和单个节点）</li><li>通过命令行标志</li><li>通过配置文件</li><li>管理可与集群一起使用的容器镜像仓库并与之交互</li><li>管理集群的Kubeconfigs</li><li>将本地Docker daemon中的镜像导入集群中运行的容器运行时中</li></ul><br>
<br>显然，还有更多的方法，您可以用来对使用过程中的细节进行调整。<br>
<h2>k3d的用途是什么？</h2>k3d的主要应用场景是在Kubernetes上进行本地开发，因为k3d轻量、简单的特性，在这一场景下几乎不会遇到麻烦和资源使用问题。 开发k3d的初衷是为开发人员提供一个简单的工具，使他们能够在开发环境的机器上运行轻量级的Kubernetes集群，从而在类似于生产的环境中获得快速的迭代时间（相对于在本地运行docker-compose与生产中的Kubernetes要快得多）。<br>
<br>随着时间的推移，k3d还发展成为一种运维工具，用于在隔离的环境中测试某些Kubernetes（或特别是K3s）功能。 例如，使用k3d，您可以轻松地创建多节点集群，在其上部署一些应用程序，轻松停止一个节点并查看Kubernetes的反应，还能够将您的应用重新调度到其他节点上。<br>
<br>此外，您可以在持续集成系统中使用k3d来快速启动集群，在其上部署测试堆栈并运行集成测试。完成操作后，您就可以轻松地停用整个集群。无需担心适当的清理和可能的残留。<br>
<br>我们还提供了一个k3d-dind镜像（类似于电影《盗梦空间》中的梦中的梦，我们在容器内的容器中放置了容器。）通过此操作，您可以创建一个运行k3d的docker-in-docker环境，该环境会在Docker中生成一个K3s集群。这意味着您只有一个容器（k3d-dind）在您的Docker主机上运行，而该容器又在其中运行了整个K3s / Kubernetes集群。<br>
<h2>如何使用k3d？</h2>1、安装k3d（如需使用也可安装kubectl）<br>
<br><blockquote><br>注意：本文介绍内容对版本有要求，请至少使用k3d v4.1.1以上版本</blockquote>2、可以尝试以下其中一个示例，或使用文档或CLI帮助文本找到适合您自己的方式（k3d [command] --help）<br>
<br><strong>“简单”的方式</strong><br>
<br><strong>k3d cluster create</strong><br>
<br>该命令将创建一个带有两个容器的K3s集群：一个Kubernetes控制平面节点（server）和一个位于其前面的负载均衡器（serverlb）。 它将它们都放置在专用的Docker网络中，并在Docker主机上随机选择的免费端口上暴露Kubernetes API。 它还在后台创建了一个名为Docker的卷，作为镜像导入的准备。<br>
<br>默认情况下，如果不提供name参数，集群将被命名为k3s-default，并且容器将显示为k3d-<cluster-name>-<role>-<#>，因此在本例中，两个容器将显示为 k3d- k3s-default-serverlb和k3d-k3s-default-server-0<br>
<br>k3d等待一切准备就绪，从集群中拉取Kubeconfig并将其与默认的Kubeconfig合并（通常位于$ HOME / .kube / config或者KUBECONFIG环境变量指向的任何路径中）。<br>
不用担心，您也可以调整该行为。<br>
<br>使用kubectl查看您刚创建的用于显示节点的内容：. kubectl get nodes <br>
k3d还为您提供了一些命令来列出您所创建的东西：.k3d cluster | node | registry list<br>
<br><strong>“简单但精妙”的方式</strong><br>
<br><code class="prettyprint">k3d cluster create mycluster --api-port 127.0.0.1:6445 --servers 3 --agents 2 --volume '/home/me/mycode:/code@agent[*]' --port '8080:80@loadbalancer'</code><br>
<br>此命令生成带有六个容器的K3s集群：* 1个负载均衡器* 3个server（控制平面节点）* 2个agent（以前为worker节点）<br>
<br>通过--api-port 127.0.0.1:6445，您可以使用k3d将Kubernetes API端口（6443内部）映射到127.0.0.1 / localhost的端口6445。这意味着随后将在Kubeconfig中包含以下连接字符串：server: <a href="https://127.0.0.1:6445/" rel="nofollow" target="_blank">https://127.0.0.1:6445</a>以连接到此集群。<br>
该端口将从负载均衡器映射到您的主机系统。请求将从那里被代理到server节点，从而有效地模拟生产环境设置，在该环境中server节点也可能发生故障，并且希望故障转移到另一个server上。<br>
<br>--volume /home/me/mycode:/code@agent[<em>] 绑定将你的本地目录/home/me/mycode挂载到所有（[</em>] agent 节点）内部的路径/code。使用索引（0或1）替换*，以便只把它挂载到其中一个节点。<br>
告诉k3d应该将卷安装到哪个节点的规范称为“节点过滤器”，它也用于其他标志，例如端口映射的--port标志。<br>
<br>也就是说，--port '8080:80@loadbalancer'将本地主机的端口8080映射到负载均衡器（serverlb）上的端口80，该负载均衡器可用于将HTTP ingress流量转发到集群。 例如，可以将Web应用程序部署到集群（Deployment）中，该集群通过一个 Ingress（如myapp.k3d.localhost）在外部暴露（Service）。<br>
<br>然后（前提是一切都设置为将该域解析为本地主机IP），则可以将浏览器指向<a href="http://myapp.k3d.localhost:8080/" rel="nofollow" target="_blank">http://myapp.k3d.localhost:8080</a> 访问您的应用程序。 然后，流量从您的主机通过Docker桥接口流向负载均衡器。 从那里，它被代理到集群，并通过Ingress和Service传递到您的应用程序Pod。<br>
<br><blockquote><br>注意：你必须设置一些机制，将myapp.k3d.localhost路由到本地主机IP（127.0.0.1）。<br>
  最常见的方法是在你的/etc/hosts文件中使用127.0.0.1<br>
  myapp.k3d.localhost的条目（C:\Windows\System32\drivers\etc/hosts）。。<br>
  但是，这不允许使用通配符（<em>.localhost），因此一段时间后可能会变得有些麻烦，因此您可能需要了解dnsmasq（MacOS /<br>
  UNIX）或Acrylic（Windows）之类的工具来减轻负担。  提示：可以在某些系统（至少是Linux操作系统，包括SUSE<br>
  Linux和openSUSE）上安装libnss-myhostname软件包，以将</em>.localhost域自动解析为127.0.0.1，这意味着您不必再手动操作。例如<br>
  ，如果您希望通过Ingress进行测试，则需要在其中设置域。</blockquote>在此处，需要注意的事是：如果创建多个server节点，则K3s将被分配到--cluster-init标志，这意味着它将K3s的默认内部数据库（默认为SQLite）更改为etcd。<br>
<br><strong>“配置即编码”方式</strong><br>
<br>从k3d v4.0.0（发布于2021年1月）开始，我们支持使用配置文件，来配置一切您以前通过命令行标志所做的代码（不久之后甚至可能支持更多）。在撰写本文时，您可以在repo中找到用于验证配置文件的JSON模式：<br>
<a href="https://github.com/rancher/k3d/blob/092f26a4e27eaf9d3a5bc32b249f897f448bc1ce/pkg/config/v1alpha2/schema.json"></a><a href="https://github.com/rancher/k3d/blob/092f26a4e27eaf9d3a5bc32b249f897f448bc1ce/pkg/config/v1alpha2/schema.json" rel="nofollow" target="_blank">https://github.com/rancher/k3d ... .json</a><br>
<br>示例配置文件：<br>
<br><code class="prettyprint"><h1>k3d configuration file, saved as e.g. /home/me/myk3dcluster.yaml</h1>apiVersion: k3d.io/v1alpha2  # this will change in the future as we make everything more stable<br>
kind: Simple  # internally, we also have a Cluster config, which is not yet available externally<br>
name: mycluster  # name that you want to give to your cluster (will still be prefixed with `k3d-`)<br>
servers: 1  # same as `--servers 1`<br>
agents: 2  # same as `--agents 2`<br>
kubeAPI:  # same as `--api-port 127.0.0.1:6445`<br>
  hostIP: &quot;127.0.0.1&quot;<br>
  hostPort: &quot;6445&quot;<br>
ports:<br>
  - port: 8080:80  # same as `--port 8080:80@loadbalancer<br>
    nodeFilters:<br>
      - loadbalancer<br>
options:<br>
  k3d:  # k3d runtime settings<br>
    wait: true  # wait for cluster to be usable before returining; same as `--wait` (default: true)<br>
    timeout: &quot;60s&quot;  # wait timeout before aborting; same as `--timeout 60s`<br>
  k3s:  # options passed on to K3s itself<br>
    extraServerArgs:  # additional arguments passed to the `k3s server` command<br>
      - --tls-san=my.host.domain<br>
    extraAgentArgs: []  # addditional arguments passed to the `k3s agent` command<br>
  kubeconfig:<br>
    updateDefaultKubeconfig: true  # add new cluster to your default Kubeconfig; same as `--kubeconfig-update-default` (default: true)<br>
switchCurrentContext: true  # also set current-context to the new cluster's context; same as `--kubeconfig-switch-context` (default: true)</code><br>
<br>假设我们将其另存为/home/me/myk3dcluster.yaml，我们可以使用它来配置新集群<br>
k3d cluster create --config /home/me/myk3dcluster.yaml<br>
<br>注意：您仍然可以设置额外的参数或标志，这些参数或标志将优先于（或将被合并）你在配置文件中定义的任何参数。<br>
<br><h2>k3d还能做什么？</h2>你可以在很多场景下使用k3d，例如：<br>
<ul><li>与k3d托管的容器仓库一起创建集群</li><li>使用集群通过热代码重载进行快速开发</li><li>将k3d与其他开发工具（例如Tilt或Skaffold）结合使用</li><li>两者都可以通过k3d image import利用镜像导入的功能</li><li>两者都可以利用k3d托管的仓库来加快开发周期</li><li>在您的CI系统中使用k3d（为此我们提供了PoC：<a href="https://github.com/iwilltry42/k3d-demo/blob/main/.drone.yml" rel="nofollow" target="_blank">https://github.com/iwilltry42/ ... e.yml</a>）</li><li>使用社区维护的vscode扩展程序（<a href="https://github.com/inercia/vscode-k3d" rel="nofollow" target="_blank">https://github.com/inercia/vscode-k3d</a>）将其集成到您的</li><li>vscode工作流程中 用它来设置K3s的高可用性</li></ul><br>
<br>您可以通过使用在此demo repo中准备好的脚本来自己尝试所有这些操作：<br>
<a href="https://github.com/iwilltry42/k3d-demo" rel="nofollow" target="_blank">https://github.com/iwilltry42/k3d-demo</a>。<br>
<blockquote><br>THORSTEN KLEIN<br>
   trivago的DevOps工程师，SUSE自由软件工程师，也是k3d的维护者。</blockquote>
                                
                                                              
</div>
            