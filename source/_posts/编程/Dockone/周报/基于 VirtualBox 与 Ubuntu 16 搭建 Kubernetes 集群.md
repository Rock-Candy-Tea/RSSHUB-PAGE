
---
title: '基于 VirtualBox 与 Ubuntu 16 搭建 Kubernetes 集群'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=902'
author: Dockone
comments: false
date: 2021-07-06 08:08:13
thumbnail: 'https://picsum.photos/400/300?random=902'
---

<div>   
<br>【编者的话】这篇文章记录了我在一台机器使用 VirtualBox + Ubuntu 16 搭建 Kubernetes 的整个过程，包括其中遇到的一些问题以及解决办法。<br>
<br><h3>关于 Kubernetes</h3>下面是一段来自维基百科的关于 Kubernetes 的解释：<br>
<br><blockquote><br>Kubernetes（常简称为 K8s）是用于自动部署、扩展和管理「容器化（containerized）应用程序」的开源系统。该系统由 Google 设计并捐赠给 Cloud Native Computing Foundation（今属 Linux 基金会）来使用。<br>
  它旨在提供“跨主机集群的自动部署、扩展以及运行应用程序容器的平台”。它支持一系列容器工具，包括 Docker 等。</blockquote>Kubernetes 可以为我们提供 <code class="prettyprint">服务发现和负载均衡</code>、<code class="prettyprint">存储编排</code>、<code class="prettyprint">自动部署和回滚</code>、<code class="prettyprint">自动完成装箱计算</code>、<code class="prettyprint">自我修复</code>和<code class="prettyprint">密钥与配置管理</code>的能力。<br>
<h3>基础环境准备</h3><h3>安装 VirtualBox</h3>VirtualBox 是一种功能强大的虚拟机软件，而且是开源免费的，下载地址：<a href="https://www.virtualbox.org/wiki/Downloads" rel="nofollow" target="_blank">https://www.virtualbox.org/wiki/Downloads</a>，安装 VirtualBox 非常简单，这里我就不赘述了。<br>
<h4>下载 Ubuntu 16 系统镜像</h4>这里我选择了 Ubuntu 16 作为系统镜像，当然你也可以使用其他系统，比如 CentOS 等，Ubuntu 16 的下载地址：<a href="https://releases.ubuntu.com/16.04/" rel="nofollow" target="_blank">https://releases.ubuntu.com/16.04/</a>。<br>
<h4>虚拟机 x3</h4>安装好了 VirtualBox，下载了 Ubuntu 16 的镜像后，我们首先需要搭建三台 Ubuntu 16 的虚拟机。这个新建虚拟机的过程也是比较简单的，一步一步往下走就可以了。新建完成后，我们需要对每台虚拟机进行相应的配置，配置时使用的用户应该是 <code class="prettyprint">root</code> 用户。<br>
<br><strong>虚拟机 IP</strong><br>
<br>由于我们使用的是虚拟机，我们会给每台虚拟机配置网卡，让每台虚拟机都可以上网的，这里有两种方式：<br>
<ol><li>使用<code class="prettyprint">桥接网卡</code>，每台虚拟机的 IP 将会是宿主机网段的，支持虚拟机上网</li><li>使用<code class="prettyprint">NAT 网络</code> + 端口转发，网段自行设置，支持虚拟机上网</li></ol><br>
<br>大家可以使用其中任意一种方式给虚拟机配置网卡，从而让虚拟机可以上网。<br>
<br>需要注意的是，<strong>在集群搭建完成后，集群中的每个节点的 IP 要求保持不变，否则节点需要重新加入。</strong><br>
<br>简单的方式就是让虚拟机不关机，而是进入睡眠状态，下次只需唤醒即可。<br>
<br>在集群中，我们使用的是内网地址，可以通过  <code class="prettyprint">ifconfig</code>  或者  <code class="prettyprint">ip addr</code>  找到每台虚拟机对应的内网地址：<br>
<pre class="prettyprint">> ifconfig<br>
<br>
enp0s3    Link encap:Ethernet  HWaddr 08:00:27:6f:23:2a  <br>
      inet addr:10.0.2.4  Bcast:10.0.2.255  Mask:255.255.255.0<br>
      inet6 addr: fe80::a00:27ff:fe6f:232a/64 Scope:Link<br>
      UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1<br>
      RX packets:3277016 errors:0 dropped:0 overruns:0 frame:0<br>
      TX packets:3385793 errors:0 dropped:0 overruns:0 carrier:0<br>
      collisions:0 txqueuelen:1000 <br>
      RX bytes:1084480916 (1.0 GB)  TX bytes:2079122979 (2.0 GB)<br>
</pre><br>
这台虚拟机（master）的地址就是 <code class="prettyprint">10.0.2.4</code>。<br>
<br><strong>配置主机名</strong><br>
<br>Kubernetes 的节点名称是由主机名决定的，所以我们可以分别设置三台虚拟机的主机名为 <code class="prettyprint">master</code>、<code class="prettyprint">node1</code> 和 <code class="prettyprint">node2</code>，通过修改 <code class="prettyprint">/etc/hosts</code> 文件来修改主机名，需要重启虚拟机：<br>
<pre class="prettyprint"># /etc/hosts<br>
10.0.2.4 master<br>
10.0.2.5 node1<br>
10.0.2.6 node2<br>
</pre><br>
<br><strong>SSH 无密连接</strong><br>
<br>在虚拟机运行起来后，我们要做的第一件事就是要连通这三台虚拟机，即配置 SSH 无密连接。<br>
<br>首先在其中的一台虚拟机上生成 SSH 的公私钥：<br>
<pre class="prettyprint">ssh-keygen -t rsa -C 'k8scat@gmail.com' -f ~/.ssh/id_rsa -q -N ''<br>
</pre><br>
<br>关于 <code class="prettyprint">ssh-keygen</code> 的参数说明：<br>
<ul><li><code class="prettyprint">-t rsa</code> 指定加密算法为 <code class="prettyprint">RSA</code>  </li><li><code class="prettyprint">-C 'k8scat@gmail.com'</code> 用于提供一个备注，表明私钥的生成者  </li><li><code class="prettyprint">-f ~/.ssh/id_rsa</code> 指定私钥生成的位置  </li><li><code class="prettyprint">-q -N ''</code> 表示不对私钥加密码，以及使用静默的方式</li></ul><br>
<br>将公私钥分发给另外两台虚拟机，并在三台虚拟机上都将公钥（<code class="prettyprint">~/.ssh/id_rsa.pub</code>）的内容写进 <code class="prettyprint">~/.ssh/authorized_keys</code> 文件中，同时设置 <code class="prettyprint">~/.ssh/authorized_keys</code> 文件的权限为 <code class="prettyprint">400</code>：<br>
<pre class="prettyprint">cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys<br>
chmod 400 ~/.ssh/authorized_keys<br>
</pre><br>
配置完成后，我们将可以通过以下方式在其中一个虚拟机上连接另一台虚拟机了：<br>
<pre class="prettyprint"># 在 master 节点上<br>
ssh root@node1<br>
</pre><br>
<h3>Kubernetes 集群搭建</h3>在弄好三台虚拟机后，我们便可以开始搭建一个拥有三个节点的 Kubernetes 的集群了。<br>
<h4>安装 Docker</h4><pre class="prettyprint">apt-get update -y<br>
apt-get install -y \<br>
apt-transport-https \<br>
ca-certificates \<br>
curl \<br>
gnupg \<br>
lsb-release<br>
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg<br>
echo \<br>
"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \<br>
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null<br>
<br>
# INSTALL DOCKER ENGINE<br>
apt-get update -y<br>
apt-get install -y docker-ce docker-ce-cli containerd.io<br>
<br>
# Configure Docker to start on boot<br>
systemctl enable docker.service<br>
systemctl enable containerd.service<br>
<br>
# Start Docker<br>
systemctl start docker<br>
</pre><br>
<h4>安装 kubeadm、kubelet 和 kubectl</h4>这里使用的是阿里云的镜像源：<br>
<pre class="prettyprint"># 更新 apt 包索引并安装使用 Kubernetes apt 仓库所需要的包<br>
apt-get update -y<br>
apt-get install -y apt-transport-https ca-certificates curl<br>
<br>
# 下载 Google Cloud 公开签名秘钥<br>
# curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg<br>
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add -<br>
<br>
# 添加 Kubernetes apt 仓库<br>
# echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list<br>
echo "deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list<br>
<br>
# 更新 apt 包索引，安装 kubelet、kubeadm 和 kubectl，并锁定其版本<br>
apt-get update -y<br>
apt-get install -y kubelet kubeadm kubectl<br>
apt-mark hold kubelet kubeadm kubectl<br>
</pre><br>
<h4>关闭 SWAP</h4>编辑 <code class="prettyprint">/etc/fstab</code> 文件并注释掉 <code class="prettyprint">swap</code> 分区的配置：<br>
<pre class="prettyprint">#/dev/mapper/master--vg-swap_1 none            swap    sw              0       0<br>
</pre><br>
<h4>预先下载镜像</h4>获取 <code class="prettyprint">kubeadm init</code> 需要使用到的镜像列表：<br>
<pre class="prettyprint">> kubeadm config images list<br>
<br>
k8s.gcr.io/kube-apiserver:v1.21.1<br>
k8s.gcr.io/kube-controller-manager:v1.21.1<br>
k8s.gcr.io/kube-scheduler:v1.21.1<br>
k8s.gcr.io/kube-proxy:v1.21.1<br>
k8s.gcr.io/pause:3.4.1<br>
k8s.gcr.io/etcd:3.4.13-0<br>
k8s.gcr.io/coredns/coredns:v1.8.0<br>
</pre><br>
Kubernetes 的镜像源对于国内用户是可望而不可即的，但我们可以先拉到国内的镜像仓或者可以使用的镜像仓，比如阿里云的容器镜像服务 ACR 和 Docker 的官方镜像仓 DockerHub。<br>
<br>我们可以新建一个 GitHub 代码仓，里面只有一个 Dockerfile，其内容如下：<br>
<pre class="prettyprint">FROM k8s.gcr.io/kube-apiserver:v1.21.0<br>
</pre><br>
然后在阿里云的容器镜像服务 ACR 中新建一个镜像，并关联这个 GitHub 代码仓，构建出来的镜像就是我们要的 Kubernetes 镜像，比如上面的  <code class="prettyprint">k8s.gcr.io/kube-apiserver:v1.21.1</code>，但在使用的时候需要重新给镜像打标签。<br>
<br>在 ACR 中构建好了所有需要的镜像后，使用下面这个脚本可以快速处理给镜像打标签的任务：<br>
<pre class="prettyprint"># Pull images from aliyun registry<br>
kubeadm config images list | sed -e 's/^/docker pull /g' -e 's#k8s.gcr.io#registry.cn-shenzhen.aliyuncs.com/k8scat#g' -e 's#/coredns/coredns#/coredns#g' | sh -x<br>
<br>
# Tag images<br>
docker images | grep k8scat | awk '&#123;print "docker tag",$1":"$2,$1":"$2&#125;' | sed -e 's#registry.cn-shenzhen.aliyuncs.com/k8scat#k8s.gcr.io#2' | sh -x<br>
docker tag k8s.gcr.io/coredns:v1.8.0 k8s.gcr.io/coredns/coredns:v1.8.0<br>
<br>
# Remove images<br>
docker images | grep k8scat | awk '&#123;print "docker rmi",$1":"$2&#125;' | sh -x<br>
</pre><br>
<h4>初始化 master 节点</h4><code class="prettyprint">10.0.2.4</code>  是 master 节点的 IP 地址，设置 Pod 网段为 <code class="prettyprint">192.168.16.0/20</code>：<br>
<pre class="prettyprint">> kubeadm init --apiserver-advertise-address=10.0.2.4 --pod-network-cidr=192.168.16.0/20<br>
<br>
kubeadm join 10.0.2.4:6443 --token ioshf8.40n8i0rjsehpigcl \<br>
--discovery-token-ca-cert-hash sha256:085d36848b2ee8ae9032d27a444795bc0e459f54ba043500d19d2c6fb044b065<br>
</pre><br>
<h4>加入 node 节点</h4><pre class="prettyprint">kubeadm join 10.0.2.4:6443 --token ioshf8.40n8i0rjsehpigcl \<br>
--discovery-token-ca-cert-hash sha256:085d36848b2ee8ae9032d27a444795bc0e459f54ba043500d19d2c6fb044b065<br>
</pre><br>
<h4>分发 kubectl 配置文件</h4><pre class="prettyprint">scp master:/etc/kubernetes/admin.conf /etc/kubernetes/admin.conf<br>
echo 'export KUBECONFIG="/etc/kubernetes/admin.conf"' >> /etc/profile<br>
source /etc/profile<br>
</pre><br>
<h4>安装网络插件</h4>这里我们使用的是 <code class="prettyprint">Weave Net</code>：<br>
<pre class="prettyprint"># curl -L "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')" > weave-net.yaml<br>
<br>
# With IPALLOC_RANGE<br>
kubectl apply -f https://gist.githubusercontent.com/k8scat/c6a1aa5a1bdcb8c220368dd2db69bedf/raw/da1410eea6771c56e93f191df82206be8e722112/k8s-weave-net.yaml<br>
</pre><br>
<br>原文链接：<a href="https://juejin.cn/post/6970710333027516423" rel="nofollow" target="_blank">https://juejin.cn/post/6970710333027516423</a>
                                
                                                              
</div>
            