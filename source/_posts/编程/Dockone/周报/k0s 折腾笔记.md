
---
title: 'k0s 折腾笔记'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210821/5fe16ac80fd6c7ab4e772e35d7301f78.png'
author: Dockone
comments: false
date: 2021-08-23 07:07:57
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210821/5fe16ac80fd6c7ab4e772e35d7301f78.png'
---

<div>   
<br>【编者的话】最近两年一直在使用 kubeadm 部署 Kubernetes 集群，总体来说配合一些自己小脚本还有一些自动化工具还算是方便；但是全容器化稳定性确实担忧，也遇到过莫名其妙的证书过期错误，最后重启大法解决这种问题；所以也在探索比较方便的二进制部署方式，比如这个 k0s。<br>
<h3>一、k0s 介绍</h3><em>The Simple, Solid & Certified Kubernetes Distribution.</em><br>
<br>k0s 可以认为是一个下游的 Kubernetes 发行版，与原生 Kubernetes 相比，k0s 并未阉割大量 Kubernetes 功能；k0s 主要阉割部分基本上只有<strong>树内 Cloud provider</strong>，其他的都与原生 Kubernetes 相同。<br>
<br>k0s 自行编译 Kubernetes 源码生成 Kubernetes 二进制文件，然后在安装后将二进制文件释放到宿主机再启动；这种情况下所有功能几乎与原生 Kubernetes 没有差异。<br>
<h3>二、k0sctl 使用</h3>k0sctl 是 k0s 为了方便快速部署集群所提供的工具，有点类似于 kubeadm，但是其扩展性要比 kubeadm 好得多。在多节点的情况下，k0sctl 通过 SSH 链接目标主机然后按照步骤释放文件并启动 Kubernetes 相关服务，从而完成集群初始化。<br>
<h4>2.1、k0sctl 安装集群</h4>安装过程中会自动下载相关镜像，需要保证所有节点可以扶墙，如何离线安装后面讲解。<strong>安装前保证目标机器的 hostname 为非域名形式，否则可能会出现一些问题。</strong>以下是一个简单的启动集群示例：<br>
<br>首先安装 k0sctl：<br>
<pre class="prettyprint"># 安装 k0sctl<br>
wget https://github.com/k0sproject/k0sctl/releases/download/v0.9.0/k0sctl-linux-x64<br>
chmod +x k0sctl-linux-x64<br>
mv k0sctl-linux-x64 /usr/local/bin/k0sctl<br>
</pre><br>
然后编写 k0sctl.yaml 配置文件：<br>
<pre class="prettyprint">apiVersion: k0sctl.k0sproject.io/v1beta1<br>
kind: Cluster<br>
metadata:<br>
name: k0s-cluster<br>
spec:<br>
hosts:<br>
- ssh:<br>
  address: 10.0.0.11<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: controller+worker<br>
- ssh:<br>
  address: 10.0.0.12<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: controller+worker<br>
- ssh:<br>
  address: 10.0.0.13<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: controller+worker<br>
- ssh:<br>
  address: 10.0.0.14<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: worker<br>
- ssh:<br>
  address: 10.0.0.15<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: worker<br>
k0s:<br>
version: 1.21.2+k0s.1<br>
config:<br>
  apiVersion: k0s.k0sproject.io/v1beta1<br>
  kind: Cluster<br>
  metadata:<br>
    name: k0s<br>
  spec:<br>
    api:<br>
      address: 10.0.0.11<br>
      port: 6443<br>
      k0sApiPort: 9443<br>
      sans:<br>
      - 10.0.0.11<br>
      - 10.0.0.12<br>
      - 10.0.0.13<br>
    storage:<br>
      type: etcd<br>
      etcd:<br>
        peerAddress: 10.0.0.11<br>
    network:<br>
      kubeProxy:<br>
        disabled: false<br>
        mode: ipvs<br>
</pre><br>
最后执行 <code class="prettyprint">apply</code> 命令安装即可，安装前确保你的操作机器可以 SSH 免密登陆所有目标机器：<br>
<pre class="prettyprint">➜  tmp k0sctl apply -c bak.yaml<br>
<br>
⠀⣿⣿⡇⠀⠀⢀⣴⣾⣿⠟⠁⢸⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀█████████ █████████ ███<br>
⠀⣿⣿⡇⣠⣶⣿⡿⠋⠀⠀⠀⢸⣿⡇⠀⠀⠀⣠⠀⠀⢀⣠⡆⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀███          ███    ███<br>
⠀⣿⣿⣿⣿⣟⠋⠀⠀⠀⠀⠀⢸⣿⡇⠀⢰⣾⣿⠀⠀⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀███          ███    ███<br>
⠀⣿⣿⡏⠻⣿⣷⣤⡀⠀⠀⠀⠸⠛⠁⠀⠸⠋⠁⠀⠀⣿⣿⡇⠈⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⣿⠀███          ███    ███<br>
⠀⣿⣿⡇⠀⠀⠙⢿⣿⣦⣀⠀⠀⠀⣠⣶⣶⣶⣶⣶⣶⣿⣿⡇⢰⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⠀█████████    ███    ██████████<br>
<br>
k0sctl 0.0.0 Copyright 2021, k0sctl authors.<br>
Anonymized telemetry of usage will be sent to the authors.<br>
By continuing to use k0sctl you agree to these terms:<br>
https://k0sproject.io/licenses/eula<br>
INFO ==> Running phase: Connect to hosts<br>
INFO [ssh] 10.0.0.15:22: connected<br>
INFO [ssh] 10.0.0.11:22: connected<br>
INFO [ssh] 10.0.0.12:22: connected<br>
INFO [ssh] 10.0.0.14:22: connected<br>
INFO [ssh] 10.0.0.13:22: connected<br>
INFO ==> Running phase: Detect host operating systems<br>
INFO [ssh] 10.0.0.11:22: is running Ubuntu 20.04.2 LTS<br>
INFO [ssh] 10.0.0.12:22: is running Ubuntu 20.04.2 LTS<br>
INFO [ssh] 10.0.0.14:22: is running Ubuntu 20.04.2 LTS<br>
INFO [ssh] 10.0.0.13:22: is running Ubuntu 20.04.2 LTS<br>
INFO [ssh] 10.0.0.15:22: is running Ubuntu 20.04.2 LTS<br>
INFO ==> Running phase: Prepare hosts<br>
INFO ==> Running phase: Gather host facts<br>
INFO [ssh] 10.0.0.11:22: discovered ens33 as private interface<br>
INFO [ssh] 10.0.0.13:22: discovered ens33 as private interface<br>
INFO [ssh] 10.0.0.12:22: discovered ens33 as private interface<br>
INFO ==> Running phase: Download k0s on hosts<br>
INFO [ssh] 10.0.0.11:22: downloading k0s 1.21.2+k0s.1<br>
INFO [ssh] 10.0.0.13:22: downloading k0s 1.21.2+k0s.1<br>
INFO [ssh] 10.0.0.12:22: downloading k0s 1.21.2+k0s.1<br>
INFO [ssh] 10.0.0.15:22: downloading k0s 1.21.2+k0s.1<br>
INFO [ssh] 10.0.0.14:22: downloading k0s 1.21.2+k0s.1<br>
......<br>
</pre><br>
稍等片刻后带有三个 Master 和两个 Node 的集群将安装完成：<br>
<pre class="prettyprint"># 注意：目标机器 hostname 不应当为域名形式，这里的样例是已经修复了这个问题<br>
k1.node ➜ ~ k0s kubectl get node -o wide<br>
NAME      STATUS   ROLES    AGE   VERSION       INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     CONTAINER-RUNTIME<br>
k1.node   Ready    <none>   10m   v1.21.2+k0s   10.0.0.11     <none>        Ubuntu 20.04.2 LTS   5.4.0-77-generic   containerd://1.4.6<br>
k2.node   Ready    <none>   10m   v1.21.2+k0s   10.0.0.12     <none>        Ubuntu 20.04.2 LTS   5.4.0-77-generic   containerd://1.4.6<br>
k3.node   Ready    <none>   10m   v1.21.2+k0s   10.0.0.13     <none>        Ubuntu 20.04.2 LTS   5.4.0-77-generic   containerd://1.4.6<br>
k4.node   Ready    <none>   10m   v1.21.2+k0s   10.0.0.14     <none>        Ubuntu 20.04.2 LTS   5.4.0-77-generic   containerd://1.4.6<br>
k5.node   Ready    <none>   10m   v1.21.2+k0s   10.0.0.15     <none>        Ubuntu 20.04.2 LTS   5.4.0-77-generic   containerd://1.4.6<br>
</pre><br>
<h4>2.2、k0sctl 的扩展方式</h4>与 kubeadm 不同，k0sctl 几乎提供了所有安装细节的可定制化选项，其通过三种行为来完成扩展：<br>
<ul><li><strong>文件上传</strong>：k0sctl 允许定义在安装前的文件上传，在安装之前 k0sctl 会把已经定义的相关文件全部上传到目标主机，包括不限于 k0s 本身二进制文件、离线镜像包、其他安装文件、其他辅助脚本等。</li><li><strong>Manifests 与 Helm</strong>：当将特定的文件上传到 Master 节点的 <code class="prettyprint">/var/lib/k0s/manifests</code> 目录时，k0s 在安装过程中会自动应用这些配置，类似 kubelet 的 static pod 一样，只不过 k0s 允许全部资源（包括不限于 Deployment、DaemonSet、namespace 等）；同样也可以直接在 <code class="prettyprint">k0sctl.yaml</code> 添加 Helm 配置，k0s 也会以同样的方式帮你管理。</li><li><strong>辅助脚本</strong>：可以在每个主机下配置 <code class="prettyprint">hooks</code> 选项来实现执行一些特定的脚本（文档里没有，需要看源码），以便在特定情况下做点骚操作。</li></ul><br>
<br><h4>2.3、k0sctl 使用离线镜像包</h4>基于上面的扩展，k0s 还方便的帮我们集成了离线镜像包的自动导入，我们只需要定义一个文件上传，将镜像包上传到 <code class="prettyprint">/var/lib/k0s/images/</code> 目录后，k0s 会自定将其倒入到 containerd 中而无需我们手动干预：<br>
<pre class="prettyprint">apiVersion: k0sctl.k0sproject.io/v1beta1<br>
kind: Cluster<br>
metadata:<br>
name: k0s-cluster<br>
spec:<br>
hosts:<br>
- ssh:<br>
  address: 10.0.0.11<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: controller+worker<br>
# files 配置将会在安装前将相关文件上传到目标主机<br>
files:<br>
- name: image-bundle<br>
  src: /Users/bleem/tmp/bundle_file<br>
  # 在该目录下的 image 压缩包将会被自动导入到 containerd 中<br>
  dstDir: /var/lib/k0s/images/<br>
  perm: 0755<br>
......<br>
</pre><br>
关于 image 压缩包（bundle_file）如何下载以及自己自定义问题请参考官方 <a href="https://docs.k0sproject.io/v1.21.2+k0s.1/airgap-install/">Airgap install</a> 文档。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210821/5fe16ac80fd6c7ab4e772e35d7301f78.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210821/5fe16ac80fd6c7ab4e772e35d7301f78.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>2.4、切换 CNI 插件</h4>默认情况下 k0s 内部集成了两个 CNI 插件：Calico 和 kube-router；如果我们使用其他的 CNI 插件例如 Flannel，我们只需要将默认的 CNI 插件设置为 <code class="prettyprint">custom</code>，然后将 Flannel 的部署 yaml 上传到一台 Master 的 <code class="prettyprint">/var/lib/k0s/manifests</code> 目录即可，k0s 会自动帮我门执行 <code class="prettyprint">apply -f xxxx.yaml</code> 这种操作。<br>
<br>下面是切换到 Flannel 的样例，需要注意的是 Flannel 官方镜像不会帮你安装 CNI 的二进制文件，我们需要借助文件上传自己安装（<a href="https://github.com/containernetworking/plugins/releases">CNI GitHub 插件下载地址</a>）：<br>
<pre class="prettyprint">apiVersion: k0sctl.k0sproject.io/v1beta1<br>
kind: Cluster<br>
metadata:<br>
name: k0s-cluster<br>
spec:<br>
hosts:<br>
- ssh:<br>
  address: 10.0.0.11<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: controller+worker<br>
files:<br>
# 将 Flannel 的 yaml 放到 Manifests 里（需要单独创建一个目录）<br>
- name: flannel<br>
  src: /Users/bleem/tmp/kube-flannel.yaml<br>
  dstDir: /var/lib/k0s/manifests/flannel<br>
  perm: 0644<br>
# 自己安装一下 CNI 插件<br>
- name: cni-plugins<br>
  src: /Users/bleem/tmp/cni-plugins/*<br>
  dstDir: /opt/cni/bin/<br>
  perm: 0755<br>
k0s:<br>
version: v1.21.2+k0s.1<br>
config:<br>
  apiVersion: k0s.k0sproject.io/v1beta1<br>
  kind: Cluster<br>
  metadata:<br>
    name: k0s<br>
  spec:<br>
    api:<br>
      address: 10.0.0.11<br>
      port: 6443<br>
      k0sApiPort: 9443<br>
      sans:<br>
      - 10.0.0.11<br>
      - 10.0.0.12<br>
      - 10.0.0.13<br>
    storage:<br>
      type: etcd<br>
    network:<br>
      podCIDR: 10.244.0.0/16<br>
      serviceCIDR: 10.96.0.0/12<br>
      # 这里指定 CNI 为 custom 自定义类型，这样<br>
      # k0s 就不会安装 Calico/kube-router 了<br>
      provider: custom<br>
</pre><br>
<h4>2.5、上传 k0s 二进制文件</h4>除了普通文件、镜像压缩包等，默认情况下 k0sctl 在安装集群时还会在目标机器上下载 k0s 二进制文件；当然在离线环境下这一步也可以通过一个简单的配置来实现离线上传：<br>
<pre class="prettyprint">apiVersion: k0sctl.k0sproject.io/v1beta1<br>
kind: Cluster<br>
metadata:<br>
name: k0s-cluster<br>
spec:<br>
hosts:<br>
- ssh:<br>
  address: 10.0.0.11<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: controller+worker<br>
# 声明需要上传二进制文件<br>
uploadBinary: true<br>
# 指定二进制文件位置<br>
k0sBinaryPath: /Users/bleem/tmp/k0s<br>
files:<br>
- name: flannel<br>
  src: /Users/bleem/tmp/kube-flannel.yaml<br>
  dstDir: /var/lib/k0s/manifests/flannel<br>
  perm: 0644<br>
......<br>
</pre><br>
<h4>2.6、更换镜像版本</h4>默认情况下 k0s 版本号与 Kubernetes 保持一致，但是如果期望某个组件使用特定的版本，则可以直接配置这些内置组件的镜像名称：<br>
<pre class="prettyprint">apiVersion: k0sctl.k0sproject.io/v1beta1<br>
kind: Cluster<br>
metadata:<br>
name: k0s-cluster<br>
spec:<br>
hosts:<br>
- ssh:<br>
  address: 10.0.0.11<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: controller+worker<br>
uploadBinary: true<br>
k0sBinaryPath: /Users/bleem/tmp/k0s<br>
files:<br>
- name: flannel<br>
  src: /Users/bleem/tmp/kube-flannel.yaml<br>
  dstDir: /var/lib/k0s/manifests/flannel<br>
  perm: 0644<br>
......<br>
k0s:<br>
version: v1.21.2+k0s.1<br>
config:<br>
  apiVersion: k0s.k0sproject.io/v1beta1<br>
  kind: Cluster<br>
  metadata:<br>
    name: k0s<br>
  spec:<br>
    api:<br>
      address: 10.0.0.11<br>
      port: 6443<br>
      k0sApiPort: 9443<br>
      sans:<br>
      - 10.0.0.11<br>
      - 10.0.0.12<br>
      - 10.0.0.13<br>
    # 指定内部组件的镜像使用的版本<br>
    images:<br>
      #konnectivity:<br>
      #  image: us.gcr.io/k8s-artifacts-prod/kas-network-proxy/proxy-agent<br>
      #  version: v0.0.21<br>
      #metricsserver:<br>
      #  image: gcr.io/k8s-staging-metrics-server/metrics-server<br>
      #  version: v0.3.7<br>
      kubeproxy:<br>
        image: k8s.gcr.io/kube-proxy<br>
        version: v1.21.3<br>
      #coredns:<br>
      #  image: docker.io/coredns/coredns<br>
      #  version: 1.7.0<br>
      #calico:<br>
      #  cni:<br>
      #    image: docker.io/calico/cni<br>
      #    version: v3.18.1<br>
      #  node:<br>
      #    image: docker.io/calico/node<br>
      #    version: v3.18.1<br>
      #  kubecontrollers:<br>
      #    image: docker.io/calico/kube-controllers<br>
      #    version: v3.18.1<br>
      #kuberouter:<br>
      #  cni:<br>
      #    image: docker.io/cloudnativelabs/kube-router<br>
      #    version: v1.2.1<br>
      #  cniInstaller:<br>
      #    image: quay.io/k0sproject/cni-node<br>
      #    version: 0.1.0<br>
      default_pull_policy: IfNotPresent<br>
      #default_pull_policy: Never<br>
</pre><br>
<h4>2.7、调整 Master 组件参数</h4>熟悉 Kubernetes 的应该清楚，Master 上三大组件：apiserver、controller、scheduler 管控整个集群；在 k0sctl 安装集群的过程中也允许自定义这些组件的参数，这些调整通过修改使用的  <code class="prettyprint">k0sctl.yaml</code>  配置文件完成。<br>
<ul><li><code class="prettyprint">spec.api.extraArgs</code>：用于自定义 kube-apiserver 的自定义参数（KV map）</li><li><code class="prettyprint">spec.scheduler.extraArgs</code>：用于自定义 kube-scheduler 的自定义参数（KV map）</li><li><code class="prettyprint">spec.controllerManager.extraArgs</code>：用于自定义 kube-controller-manager 自定义参数（KV map）</li><li><code class="prettyprint">spec.workerProfiles</code>：用于覆盖 kubelet-config.yaml 中的配置，该配置最终将于默认的 kubelet-config.yaml 合并</li></ul><br>
<br>除此之外在 <code class="prettyprint">Host</code> 配置中还有一个 <code class="prettyprint">InstallFlags</code> 配置用于传递 k0s 安装时的其他配置选项。<br>
<h3>三、k0s HA 搭建</h3><em>其实上面的第二部分主要都是介绍 k0sctl 一些基础功能，为的就是给下面这部分 HA 生产级部署做铺垫。</em><br>
<br>就目前来说，k0s HA 仅支持独立负载均衡器的 HA 架构；<strong>即外部需要有一个高可用的 4 层负载均衡器，其他所有 Node 节点链接这个负载均衡器实现 Master 的高可用</strong>。在使用 k0sctl 命令搭建 HA 集群时很简单，只需要添加一个外部负载均衡器地址即可；<strong>以下是一个完整的，全离线状态下的 HA 集群搭建配置。</strong><br>
<h4>3.1、外部负载均衡器</h4>在搭建之前我们假设已经有一个外部的高可用的 4 层负载均衡器，且负载均衡器已经负载了以下端口：<br>
<ul><li><code class="prettyprint">6443（for Kubernetes API）</code>：负载均衡器 6443 负载所有 Master 节点的 6443</li><li><code class="prettyprint">9443（for controller join API）</code>：负载均衡器 9443 负载所有 Master 节点的 9443</li><li><code class="prettyprint">8132（for Konnectivity agent）</code>：负载均衡器 8132 负载所有 Master 节点的 8132</li><li><code class="prettyprint">8133（for Konnectivity server）</code>：负载均衡器 8133 负载所有 Master 节点的 8133</li></ul><br>
<br>以下为一个 Nginx 4 层代理的样例：<br>
<pre class="prettyprint">error_log syslog:server=unix:/dev/log notice;<br>
<br>
worker_processes auto;<br>
events &#123;<br>
multi_accept on;<br>
use epoll;<br>
worker_connections 1024;<br>
&#125;<br>
<br>
stream &#123;<br>
upstream kube_apiserver &#123;<br>
    least_conn;<br>
    server 10.0.0.11:6443;<br>
    server 10.0.0.12:6443;<br>
    server 10.0.0.13:6443;<br>
&#125;<br>
upstream konnectivity_agent &#123;<br>
    least_conn;<br>
    server 10.0.0.11:8132;<br>
    server 10.0.0.12:8132;<br>
    server 10.0.0.13:8132;<br>
&#125;<br>
upstream konnectivity_server &#123;<br>
    least_conn;<br>
    server 10.0.0.11:8133;<br>
    server 10.0.0.12:8133;<br>
    server 10.0.0.13:8133;<br>
&#125;<br>
upstream controller_join_api &#123;<br>
    least_conn;<br>
    server 10.0.0.11:9443;<br>
    server 10.0.0.12:9443;<br>
    server 10.0.0.13:9443;<br>
&#125;<br>
<br>
server &#123;<br>
    listen        0.0.0.0:6443;<br>
    proxy_pass    kube_apiserver;<br>
    proxy_timeout 10m;<br>
    proxy_connect_timeout 1s;<br>
&#125;<br>
server &#123;<br>
    listen        0.0.0.0:8132;<br>
    proxy_pass    konnectivity_agent;<br>
    proxy_timeout 10m;<br>
    proxy_connect_timeout 1s;<br>
&#125;<br>
server &#123;<br>
    listen        0.0.0.0:8133;<br>
    proxy_pass    konnectivity_server;<br>
    proxy_timeout 10m;<br>
    proxy_connect_timeout 1s;<br>
&#125;<br>
server &#123;<br>
    listen        0.0.0.0:9443;<br>
    proxy_pass    controller_join_api;<br>
    proxy_timeout 10m;<br>
    proxy_connect_timeout 1s;<br>
&#125;<br>
&#125; <br>
</pre><br>
<h4>3.2、搭建 HA 集群</h4>以下为 k0sctl 的 HA + 离线部署样例配置：<br>
<pre class="prettyprint">apiVersion: k0sctl.k0sproject.io/v1beta1<br>
kind: Cluster<br>
metadata:<br>
name: k0s-cluster<br>
spec:<br>
hosts:<br>
- ssh:<br>
  address: 10.0.0.11<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
# role 支持的值<br>
# 'controller' 单 Master<br>
# 'worker' 单 Worker<br>
# 'controller + worker' Master 和 Worker 都运行 <br>
role: controller+worker<br>
<br>
# 从本地 上传 k0s bin 文件，不要在目标机器下载<br>
uploadBinary: true<br>
k0sBinaryPath: /Users/bleem/tmp/k0s<br>
<br>
# 上传其他文件<br>
files:<br>
# 上传 Flannel 配置，使用自定的 Flannel 替换内置的 Calico<br>
- name: flannel<br>
  src: /Users/bleem/tmp/kube-flannel.yaml<br>
  dstDir: /var/lib/k0s/manifests/flannel<br>
  perm: 0644<br>
<br>
# 上传打包好的 image 镜像包，k0s 会自动导入到 containerd<br>
- name: image-bundle<br>
  src: /Users/bleem/tmp/bundle_file<br>
  dstDir: /var/lib/k0s/images/<br>
  perm: 0755<br>
<br>
# 使用 Flannel 后每个机器要上传对应的 CNI 插件<br>
- name: cni-plugins<br>
  src: /Users/bleem/tmp/cni-plugins/*<br>
  dstDir: /opt/cni/bin/<br>
  perm: 0755<br>
- ssh:<br>
  address: 10.0.0.12<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: controller+worker<br>
uploadBinary: true<br>
k0sBinaryPath: /Users/bleem/tmp/k0s<br>
files:<br>
- name: image-bundle<br>
  src: /Users/bleem/tmp/bundle_file<br>
  dstDir: /var/lib/k0s/images/<br>
  perm: 0755<br>
- name: cni-plugins<br>
  src: /Users/bleem/tmp/cni-plugins/*<br>
  dstDir: /opt/cni/bin/<br>
  perm: 0755<br>
- ssh:<br>
  address: 10.0.0.13<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: controller+worker<br>
uploadBinary: true<br>
k0sBinaryPath: /Users/bleem/tmp/k0s<br>
files:<br>
- name: image-bundle<br>
  src: /Users/bleem/tmp/bundle_file<br>
  dstDir: /var/lib/k0s/images/<br>
  perm: 0755<br>
- name: cni-plugins<br>
  src: /Users/bleem/tmp/cni-plugins/*<br>
  dstDir: /opt/cni/bin/<br>
  perm: 0755<br>
- ssh:<br>
  address: 10.0.0.14<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: worker<br>
uploadBinary: true<br>
k0sBinaryPath: /Users/bleem/tmp/k0s<br>
files:<br>
- name: image-bundle<br>
  src: /Users/bleem/tmp/bundle_file<br>
  dstDir: /var/lib/k0s/images/<br>
  perm: 0755<br>
- name: cni-plugins<br>
  src: /Users/bleem/tmp/cni-plugins/*<br>
  dstDir: /opt/cni/bin/<br>
  perm: 0755<br>
- ssh:<br>
  address: 10.0.0.15<br>
  user: root<br>
  port: 22<br>
  keyPath: /Users/bleem/.ssh/id_rsa<br>
role: worker<br>
uploadBinary: true<br>
k0sBinaryPath: /Users/bleem/tmp/k0s<br>
files:<br>
- name: image-bundle<br>
  src: /Users/bleem/tmp/bundle_file<br>
  dstDir: /var/lib/k0s/images/<br>
  perm: 0755<br>
- name: cni-plugins<br>
  src: /Users/bleem/tmp/cni-plugins/*<br>
  dstDir: /opt/cni/bin/<br>
  perm: 0755<br>
k0s:<br>
version: v1.21.2+k0s.1<br>
config:<br>
  apiVersion: k0s.k0sproject.io/v1beta1<br>
  kind: Cluster<br>
  metadata:<br>
    name: k0s<br>
  spec:<br>
    api:<br>
      # 此处填写外部的负载均衡器地址，所有 kubelet 会链接这个地址<br>
      externalAddress: 10.0.0.20<br>
      # 不要忘了为外部负载均衡器添加 API 证书的 SAN<br>
      sans:<br>
      - 10.0.0.11<br>
      - 10.0.0.12<br>
      - 10.0.0.13<br>
      - 10.0.0.20<br>
    # 存储类型使用 etcd，etcd 集群由 k0s 自动管理<br>
    storage:<br>
      type: etcd<br>
    network:<br>
      podCIDR: 10.244.0.0/16<br>
      serviceCIDR: 10.96.0.0/12<br>
      # 网络插件使用 custom，然后让 Flannel 接管<br>
      provider: custom<br>
      kubeProxy:<br>
        disabled: false<br>
        # 开启 kubelet 的 ipvs 模式<br>
        mode: ipvs<br>
    # 不发送任何匿名统计信息<br>
    telemetry:<br>
      enabled: false<br>
    images:<br>
      default_pull_policy: IfNotPresent<br>
</pre><br>
最后只需要执行 <code class="prettyprint">k0sctl apply -c k0sctl.yaml</code> 稍等几分钟集群就搭建好了，安装过程中可以看到相关文件的上传流程：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210821/9e403a39f653372982c0d975b726b2ab.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210821/9e403a39f653372982c0d975b726b2ab.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>3.3、证书续签和管理</h4>kubeadm 集群默认证书有效期是一年，到期要通过 kubeadm 重新签署；k0s 集群也差不多一样，但是不同的是 k0s 集群更加暴力；<strong>只要 CA（默认 10年）不丢，k0s 每次重启都强行重新生成一年有效期的证书，所以在 HA 的环境下，快到期时重启一下 k0s 服务就行。</strong><br>
<br>k0sctl 安装完的集群默认只有一个 <code class="prettyprint">k0scontroller.service</code> 服务，Master、Node 上所有服务都由这个服务启动，所以到期之前 <code class="prettyprint">systemctl restart k0scontroller.service</code> 一下就行。<br>
<h3>四、集群备份和恢复</h3>k0sctl 提供了集群备份和恢复功能，默认情况下只需要执行 <code class="prettyprint">k0sctl backup</code> 即可完成集群备份，该命令会在当前目录下生成一个 <code class="prettyprint">k0s_backup_TIMESTAMP.tar.gz</code> 备份文件。<br>
<br>需要恢复集群时使用 <code class="prettyprint">k0sctl apply --restore-from k0s_backup_TIMESTAMP.tar.gz</code> 命令进行恢复即可；需要注意的是恢复命令等同于在新机器重新安装集群，所以有一定风险。<br>
<br>经过连续两天的测试，感觉这个备份恢复功能并不算靠谱，还是推荐使用 Velero 备份集群。<br>
<h3>五、其他高级功能</h3><h4>5.1、etcd 替换</h4>在小规模集群场景下可能并不需要特别完善的 etcd 作为存储，k0s 借助于 kine 库可以实现使用 SQLite 或 MySQL 等传统数据库作为集群存储；如果想要切换存储只需要调整 <code class="prettyprint">k0sctl.yaml</code> 配置即可：<br>
<pre class="prettyprint">apiVersion: k0s.k0sproject.io/v1beta1<br>
kind: Cluster<br>
metadata:<br>
name: k0s<br>
spec:<br>
storage:<br>
type: kine<br>
kine:<br>
  dataSource: "sqlite:///var/lib/k0s/db/state.db?more=rwc&_journal=WAL&cache=shared"<br>
</pre><br>
<h4>5.2、集群用户管理</h4>使用 k0sctl 搭建的集群通过 <code class="prettyprint">k0s</code> 命令可以很方便的为集群添加用户，以下是添加样例：<br>
<pre class="prettyprint">k0s kubeconfig create --groups "system:masters" testUser > k0s.config<br>
</pre><br>
<h4>5.3、Containerd 配置</h4>在不做配置的情况下 k0s 集群使用默认的 Containerd 配置，如果需要自己定义特殊配置，可以在安装时通过文件上传方式将 Containerd 配置文件上传到 <code class="prettyprint">/etc/k0s/containerd.toml</code> 位置，该配置将会被 k0s 启动的 Containerd 读取并使用。<br>
<h3>六、总结</h3>k0s 是个不错的项目，对于二进制宿主机部署 Kubernetes 集群很方便，由于其直接采用 Kubernetes 二进制文件启动，所以基本没有功能阉割，而 k0sctl 又为自动化安装提供了良好的扩展性，所以值得一试。不过目前来说 k0s 在细节部分还有一定瑕疵，比如 <code class="prettyprint">konnectivity</code> 服务在安装时无法选择性关闭等；k0s 综合来说是个不错的工具，也推荐看看源码，里面很多设计很新颖也比较利于了解集群引导过程。<br>
<br>原文链接：<a href="https://mritd.com/2021/07/29/test-the-k0s-cluster/" rel="nofollow" target="_blank">https://mritd.com/2021/07/29/test-the-k0s-cluster/</a>，作者：bleem
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            