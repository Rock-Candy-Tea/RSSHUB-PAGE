
---
title: '再见Docker Desktop，你好 Minikube！'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211007/eb4c4757cfaf55de60bf549b237c0018.png'
author: Dockone
comments: false
date: 2021-10-10 11:06:15
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211007/eb4c4757cfaf55de60bf549b237c0018.png'
---

<div>   
<br>我使用Docker Desktop在Mac中启用Docker和Kubernetes已经有一段时间了。尽管它疯狂地吞噬着CPU和内存，让粉丝们疯狂。但随着“当面”弹出强制升级Docker的弹窗和软件许可的变更，是时候为本地Kubernetes开发寻找其他替代品了。<br>
<br>这篇文章只会专注于Mac平台。如果你在Linux上尝试过，请告诉我情况如何。<br>
<h3>卸载Docker Desktop</h3>让我们先从删除Docker Desktop开始。<br>
<pre class="prettyprint">brew uninstall docker<br>
</pre><br>
这不仅会摆脱Docker，还会摆脱Hyperkit以及Docker守护进程。Docker守护进程允许我们构建镜像并适用交互式的Docker CLI与之对话。当然还包括Kubernetes集群和kubectl二进制（除非你有单独部署）。如果你没有使用Homebrew，那么就需要相应地卸载这些工具。<br>
<br>然后，让我们把这些工具逐一找回来。<br>
<h3>安装Hyperkit</h3>Hyperkit仍然是在Mac上本地运行Kubernetes集群的一个可行的选择，我们先来安装它。<br>
<pre class="prettyprint">brew install hyperkit<br>
</pre><br>
确认安装正确。<br>
<pre class="prettyprint">$ hyperkit -v<br>
hyperkit: 0.20200908Homepage:https://github.com/docker/hyperkit<br>
License: BSD<br>
</pre><br>
<h3>安装Docker CLI</h3>我们是想摆脱Docker Desktop，但并不是Docker本身。Docker仍然是一个很有用的、开源的容器管理工具，如果你有一堆Dockerfiles需要处理，Docker CLI会很有用。<br>
<pre class="prettyprint">brew install docker<br>
</pre><br>
<br><blockquote><br>注意：千万不要运行brew install --cask docker。这会安装Docker Desktop集成版本，我们又要重头来过。</blockquote>这仅仅会安装Docker CLI，但不会安装Docker守护程序<code class="prettyprint">dockerd</code>。你可以通过运行<code class="prettyprint">docker info</code>看到这一点。<br>
<pre class="prettyprint">$ docker info<br>
Client:<br>
Context:    default<br>
Debug Mode: falseServer:<br>
ERROR: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?<br>
</pre><br>
<h3>安装Kubectl</h3><pre class="prettyprint">brew install kubectl<br>
</pre><br>
这一点没什么可说的。<br>
<h3>安装Minikube（和Docker守护进程）</h3>随着Hyperkit的部署，我们已经准备好部署Kubernetes集群了。并且，在这个过程中启动了一个Docker守护程序。<br>
<pre class="prettyprint">brew install minikube<br>
</pre><br>
在我们开始使用Kubernetes集群之前，这里有一些小知识需要了解。<br>
<h4>使用哪一种驱动？</h4>换句话说，我们是将Kubernetes部署在虚拟机、容器还是直接部署在裸金属服务器上？根据操作系统的不同，这里有<a href="https://minikube.sigs.k8s.io/docs/drivers/">多种选择</a>。我们将使用Mac的Hyperkit驱动。<br>
<h4>使用哪一种容器运行时？</h4>可用的选项：Docker、containerd和cri-o。鉴于Kubernetes本身正在远离Docker而转向Containerd，Containerd是一个不错的选择。但由于我们希望Docker守护程序能够构建Docker镜像，所以我们还是使用Docker吧。<br>
<h4>设定CPU和内存限制</h4>和Docker Desktop一样，设置正确的CPU和内存限制总是明智，特别是如果你打算运行许多Pod。<br>
<pre class="prettyprint">minikube config set cpus 6<br>
minikube config set memory 12g<br>
</pre><br>
最后，启动Kubernetes集群。<br>
<pre class="prettyprint">$ minikube start --kubernetes-version=v1.19.14 --driver=hyperkit --container-runtime=docker<br>
</pre><br>
使用命令行选项<code class="prettyprint">-kubernetes-version</code>来部署特定版本的Kubernetes。不用这个标志的话，默认部署最新的版本。我需要部署一个较早的版本来满足我的需要。<br>
<br>以下是上述命令的输出。<br>
<pre class="prettyprint">minikube v1.23.0 on Darwin 11.5.2<br>
▪ MINIKUBE_ACTIVE_DOCKERD=minikube<br>
  Using the hyperkit driver based on user configuration<br>
  Starting control plane node minikube in cluster minikube<br>
  Downloading Kubernetes v1.19.14 preload ...<br>
> preloaded-images-k8s-v12-v1...: 470.78 MiB / 470.78 MiB  100.00% 6.17 MiB<br>
  Creating hyperkit VM (CPUs=6, Memory=12288MB, Disk=20000MB) ...<br>
  This VM is having trouble accessinghttps://k8s.gcr.io<br>
  To pull new external images, you may need to configure a proxy:https://minikube.sigs.k8s.io/docs/reference/networking/proxy/<br>
  Preparing Kubernetes v1.19.14 on Docker 20.10.8 ...<br>
▪ Generating certificates and keys ...<br>
▪ Booting up control plane ...<br>
▪ Configuring RBAC rules ...<br>
  Verifying Kubernetes components...<br>
▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5<br>
  Enabled addons: storage-provisioner, default-storageclass❗  /usr/local/bin/kubectl is version 1.22.1, which may have incompatibilites with Kubernetes 1.19.14.<br>
▪ Want kubectl v1.19.14? Try 'minikube kubectl -- get pods -A'<br>
  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default<br>
</pre><br>
<br><blockquote><br>如果你在本地运行dnsmasq，在集群中可能会出现DNS解析失败。你可以卸载它或者在dnsmasq.conf中添加listen-address=192.168.64.1。更多信息可以在<a href="https://minikube.sigs.k8s.io/docs/drivers/hyperkit/">这里</a>找到。</blockquote>Kube Config的上下文已经设置好了。我们可以用 <code class="prettyprint">kubectl</code>来检查集群，如下所示。<br>
<pre class="prettyprint">$ minikube kubectl get nodes<br>
NAME       STATUS   ROLES    AGE    VERSION<br>
minikube   Ready    master   7m6s   v1.19.14<br>
</pre><br>
由于我们已经安装了kubectl二进制程序，我们可以直接使用它。<br>
<br>此时，我们已经有了一个Kubernetes集群，由于我们使用了Docker驱动，Docker守护程序也在运行。所以在我们使用守护进程之前，让我们先设置环境变量。<br>
<pre class="prettyprint">eval $(minikube docker-env)<br>
</pre><br>
确认Docker守护进程是正常工作的。<br>
<pre class="prettyprint">$ docker info<br>
Client:<br>
Context:    default<br>
Debug Mode: falseServer:<br>
Containers: 14<br>
Running: 14<br>
Paused: 0<br>
Stopped: 0<br>
Images: 10<br>
Server Version: 20.10.8<br>
Storage Driver: overlay2<br>
Backing Filesystem: extfs<br>
...<br>
</pre><br>
下面是我们的Minikube集群在K9S中的样子。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211007/eb4c4757cfaf55de60bf549b237c0018.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211007/eb4c4757cfaf55de60bf549b237c0018.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>新安装的Minikube集群的K9S截图</em><br>
<h3>需要Docker Compose？</h3>用以下命令安装Docker-Compose。<br>
<pre class="prettyprint">brew install docker-compose<br>
</pre><br>
<h3>暴露Services到Minikube外部</h3>对于本地开发，通常是通过浏览器或CLI从电脑访问服务。端口转发总是一个选择，但有时Ingress或负载均衡器也是有用的。让我们看看它们是如何与Minikube一起工作的。<br>
<h4>处理Ingress资源</h4>我们现在有了一个Kubernetes集群，也可以在上面部署应用程序。但我们如何访问Ingress资源呢？Minikube有一个答案，就是addons（附加组件）。<br>
<pre class="prettyprint">$ minikube addons enable ingress<br>
▪ Using image k8s.gcr.io/ingress-nginx/controller:v1.0.0-beta.3<br>
▪ Using image k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.0<br>
▪ Using image k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.0<br>
Verifying ingress addon...<br>
</pre><br>
这会部署Nginx Ingress控制器。更重要的是，它会把Nginx服务部署以 <code class="prettyprint">NodePort</code>的形式部署，并将Minikube的IP直接指向Ingress。让我们先找到这个IP。<br>
<pre class="prettyprint">$ minikube ip<br>
192.168.64.12<br>
</pre><br>
我们在80端口调用上述IP，我们应该可以从Nginx得到响应。<br>
<pre class="prettyprint">$ curl http://192.168.64.12<br>
<html><br>
<head><title>404 Not Found</title></head><br>
<body><br>
<center><h1>404 Not Found</h1></center><br>
<hr><center>nginx</center><br>
</body><br>
</html><br>
</pre><br>
记住，Ingress依赖于DNS工作，它应该被解析到Minikube的IP上。如果后端服务之一调用该DNS，除非明确配置了，否则会解析失败。这个时候，另一个附加组件可以来拯救你！<br>
<pre class="prettyprint">$ minikube addons enable ingress-dns<br>
▪ Using image cryptexlabs/minikube-ingress-dns:0.3.0<br>
</pre><br>
这将在Kubernetes集群内启动一个DNS服务器，监听在Minikube的IP上。此外，还需要一个自定义的解析器，以强制自定义顶级域名（如.test，不要使用.local）的DNS解析被重定向到上面启动的DNS服务器。<a href="https://minikube.sigs.k8s.io/docs/handbook/addons/ingress-dns/">Minikube Ingress DNS文档</a>很好地解释了这一点。按照文档里描述的步骤操作，你将会部署成功一个带有自定义DNS的Ingress。<br>
<h4>负载均衡类型的Service</h4>部署负载均衡器类型的服务，并从主机上访问它，就像你在云端部署时一样，这不是很好吗？多亏了<code class="prettyprint">metalb</code>插件，让这变得很简单。<br>
<pre class="prettyprint">minikube addons enable metallb<br>
</pre><br>
这将部署另外两个Pod，负责为负载均衡器类型的Service分配一个外部IP。如果不这样做，这些服务的外部IP将始终处于“pending”状态。<br>
<br>在使用<code class="prettyprint">metallb</code>之前，还有一个步骤。默认情况下，<code class="prettyprint">metallb</code>没有办法知道哪个范围的IP可以分配给负载均衡器的服务。运行下面的命令来提供一个范围。<br>
<pre class="prettyprint">$ minikube addons configure metallb<br>
-- Enter Load Balancer Start IP: 192.168.64.5<br>
-- Enter Load Balancer End IP: 192.168.64.15<br>
▪ Using image metallb/speaker:v0.9.6<br>
▪ Using image metallb/controller:v0.9.6<br>
metallb was successfully configured<br>
</pre><br>
基于你的Minikube IP，分配一个小范围的IP，包括Minikube IP。现在，每当你部署一个负载均衡器服务时，这个范围内的一个IP将被分配。<br>
<h3>其他问题</h3><h4>登录到远程镜像仓库</h4>你可能仍然有旧的<code class="prettyprint">~/.docker/config.json</code>，其中<code class="prettyprint">credsStore</code>设置为<code class="prettyprint">osxkeychain</code>或<code class="prettyprint">desktop</code>。这在新的配置中不会起作用。为了解决这个问题，我们来安装<code class="prettyprint">Docker Credential Helper</code>。<br>
<pre class="prettyprint">brew install docker-credential-helper<br>
</pre><br>
密钥凭证还是会像以前一样存储在MacOS Keychain中。如果这不起作用，一个快速的解决方法是删除<code class="prettyprint">~/.docker/config.json</code>文件，然后再次登录到镜像仓库。<br>
<h4>保留Docker镜像和持久化存储卷声明</h4><em>Added 7th Sept 2021</em><br>
<br>Docker Desktop的一个好处是，你可以关闭Kubernetes集群，以后再启动它，用相同的Docker镜像和持久化卷运行你的Pod。例如，在Kubernetes中运行本地数据库时，这就很有用。能够在多次重启中仍然保持有效的持久化卷是很方便的。<br>
<br>在Minikube中，如果我用<code class="prettyprint">minikube stop</code>关闭集群（和Hyperkit虚拟机），它会删除Docker镜像和所有持久化卷，这很麻烦。但幸运的是，Minikube提供了一种防止删除的方法。我们可以暂停Kubernetes集群和Hyperkit VM，而不是停止它。<br>
<pre class="prettyprint">minikube pause<br>
</pre><br>
该命令会终止Kubernetes集群，但不会删除Hyperkit虚拟机。这就释放了更多的CPU，同时仍然保留了所有的Docker镜像和持久化卷。但是，等一下，它变得更好！它不会停止dockerd守护进程。所以你可以继续使用Docker CLI，只是别忘了用<code class="prettyprint">eval $(minikube docker-env)</code>设置一下docker环境。<br>
<br>当你想恢复在Kubernetes集群上的工作时，可以运行以下命令。<br>
<pre class="prettyprint">minikube unpause<br>
</pre><br>
而你将拥有所有的系统Pod，包括附加组件Addons。这甚至在笔记本电脑重新启动后，也能正常工作！<br>
<h4>在Docker容器中绑定挂载</h4><em>Added 7th Sept 2021</em><br>
<br>一些在<a href="https://www.reddit.com/r/kubernetes/comments/pjlt52/goodbye_docker_desktop_hello_minikube/hbyi4m5?utm_source=share&utm_medium=web2x&context=3">Reddit</a>上的好心人指出，Docker容器中的绑定挂载<code class="prettyprint">(-v)</code>在Minikube和Docker的配置中并不能工作。这是Docker容器的一个常见操作，他理论上应该可以正常工作。<br>
<br>由于存在Hyperkit作为中间层，挂载一个卷其实是分成两步操作的。首先，让我们把笔记本上的磁盘挂载到Hyperkit VM上。<br>
<pre class="prettyprint">minikube mount /myvolume:/test<br>
</pre><br>
这将把本地文件夹<code class="prettyprint">/myvolume</code>挂载到Hyperkit VM的<code class="prettyprint">/test</code>路径下。这个进程仍然是活跃的，所以你不应该关闭这个终端。<br>
<br>在另一个终端上，运行Docker容器，并将<code class="prettyprint">/test</code>卷绑定到容器内的一个路径上。<br>
<pre class="prettyprint">docker run --rm -it -v /test:/inside busybox /bin/sh<br>
</pre><br>
这将在容器内的Hyperkit VM上挂载<code class="prettyprint">/test</code>卷，路径为<code class="prettyprint">/inside</code>。实际上，这会使得笔记本电脑上<code class="prettyprint">/myvolume</code>下的所有处在容器内的文件和文件夹处于读写模式。很好！<br>
<h3>总结</h3>在周日下午花了几个小时后，我对这个新的配置相当满意。我们摆脱了Docker Desktop，用Hyperkit和Minikube取代了它。我们仍然可以使用Docker API来管理Docker文件，并在本地Kubernetes集群中部署应用程序。最重要的是，我的笔记本可以愉快地运行，额外的资源可以用来运行Slack、Notion和其他Electron应用程序;-)<br>
<br><strong>原文链接：<a href="https://itnext.io/goodbye-docker-desktop-hello-minikube-3649f2a1c469">Goodbye Docker Desktop, Hello Minikube!</a>（翻译：小灰灰）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            