
---
title: '如何从 Kubernetes 切换到 Containerd'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=613'
author: Dockone
comments: false
date: 2021-08-23 08:09:14
thumbnail: 'https://picsum.photos/400/300?random=613'
---

<div>   
<br><h3>一、环境准备</h3><ul><li>Ubuntu 20.04 x5</li><li>etcd 3.4.16</li><li>Kubernetes 1.21.1</li><li>Containerd 1.3.3</li></ul><br>
<br><h4>1.1、处理 IPVS</h4>由于 Kubernetes 新版本 Service 实现切换到 IPVS，所以需要确保内核加载了 IPVS modules；以下命令将设置系统启动自动加载 IPVS 相关模块，执行完成后需要重启。<br>
<pre class="prettyprint"># Kernel modules<br>
cat > /etc/modules-load.d/50-kubernetes.conf <<EOF<br>
# Load some kernel modules needed by kubernetes at boot<br>
nf_conntrack<br>
br_netfilter<br>
ip_vs<br>
ip_vs_lc<br>
ip_vs_wlc<br>
ip_vs_rr<br>
ip_vs_wrr<br>
ip_vs_lblc<br>
ip_vs_lblcr<br>
ip_vs_dh<br>
ip_vs_sh<br>
ip_vs_fo<br>
ip_vs_nq<br>
ip_vs_sed<br>
EOF<br>
<br>
# sysctl<br>
cat > /etc/sysctl.d/50-kubernetes.conf <<EOF<br>
net.ipv4.ip_forward=1<br>
net.bridge.bridge-nf-call-iptables=1<br>
net.bridge.bridge-nf-call-ip6tables=1<br>
fs.inotify.max_user_watches=525000<br>
EOF<br>
</pre><br>
重启完成后务必检查相关 module 加载以及内核参数设置：<br>
<pre class="prettyprint"># check ipvs modules<br>
➜ ~ lsmod | grep ip_vs<br>
ip_vs_sed              16384  0<br>
ip_vs_nq               16384  0<br>
ip_vs_fo               16384  0<br>
ip_vs_sh               16384  0<br>
ip_vs_dh               16384  0<br>
ip_vs_lblcr            16384  0<br>
ip_vs_lblc             16384  0<br>
ip_vs_wrr              16384  0<br>
ip_vs_rr               16384  0<br>
ip_vs_wlc              16384  0<br>
ip_vs_lc               16384  0<br>
ip_vs                 155648  22 ip_vs_wlc,ip_vs_rr,ip_vs_dh,ip_vs_lblcr,ip_vs_sh,ip_vs_fo,ip_vs_nq,ip_vs_lblc,ip_vs_wrr,ip_vs_lc,ip_vs_sed<br>
nf_conntrack          139264  1 ip_vs<br>
nf_defrag_ipv6         24576  2 nf_conntrack,ip_vs<br>
libcrc32c              16384  5 nf_conntrack,btrfs,xfs,raid456,ip_vs<br>
<br>
# check sysctl<br>
➜ ~ sysctl -a | grep ip_forward<br>
net.ipv4.ip_forward = 1<br>
net.ipv4.ip_forward_update_priority = 1<br>
net.ipv4.ip_forward_use_pmtu = 0<br>
<br>
➜ ~ sysctl -a | grep bridge-nf-call<br>
net.bridge.bridge-nf-call-arptables = 1<br>
net.bridge.bridge-nf-call-ip6tables = 1<br>
net.bridge.bridge-nf-call-iptables = 1<br>
</pre><br>
<h4>1.2、安装 Containerd</h4>Containerd 在 Ubuntu 20 中已经在默认官方仓库中包含，所以只需要 apt 安装即可：<br>
<pre class="prettyprint"># 其他软件包后面可能会用到，所以顺手装了<br>
apt install containerd bridge-utils nfs-common tree -y<br>
</pre><br>
安装成功后可以通过执行 <code class="prettyprint">ctr images ls</code> 命令验证，本章节不会对 Containerd 配置做说明，Containerd 配置文件将在 Kubernetes 安装时进行配置。<br>
<h3>二、安装 kubernetes</h3><h4>2.1、安装 etcd 集群</h4>etcd 对于 Kubernetes 来说是核心中的核心，所以个人还是比较喜欢在宿主机安装；宿主机安装情况下为了方便我打包了一些 <strong><code class="prettyprint">*-pack</code></strong> 的工具包，用于快速处理：<br>
<br>安装 Cfssl 和 etcd：<br>
<pre class="prettyprint"># 下载安装包<br>
wget https://github.com/mritd/etcd-pack/releases/download/v3.4.16/etcd_v3.4.16.run<br>
wget https://github.com/mritd/cfssl-pack/releases/download/v1.5.0/cfssl_v1.5.0.run<br>
<br>
# 安装 Cfssl 和 etcd<br>
chmod +x *.run<br>
./etcd_v3.4.16.run install<br>
./cfssl_v1.5.0.run install<br>
</pre><br>
安装完成后，自行调整 <code class="prettyprint">/etc/cfssl/etcd/etcd-csr.json</code> 相关 IP，然后执行同目录下 <code class="prettyprint">create.sh</code> 生成证书。<br>
<pre class="prettyprint">➜ ~ cat /etc/cfssl/etcd/etcd-csr.json<br>
&#123;<br>
"key": &#123;<br>
    "algo": "rsa",<br>
    "size": 2048<br>
&#125;,<br>
"names": [<br>
    &#123;<br>
        "O": "etcd",<br>
        "OU": "etcd Security",<br>
        "L": "Beijing",<br>
        "ST": "Beijing",<br>
        "C": "CN"<br>
    &#125;<br>
],<br>
"CN": "etcd",<br>
"hosts": [<br>
    "127.0.0.1",<br>
    "localhost",<br>
    "*.etcd.node",<br>
    "*.kubernetes.node",<br>
    "10.0.0.11",<br>
    "10.0.0.12",<br>
    "10.0.0.13"<br>
]<br>
&#125;<br>
<br>
# 复制到 3 台 master<br>
➜ ~ for ip in `seq 1 3`; do scp /etc/cfssl/etcd/*.pem root@10.0.0.1$ip:/etc/etcd/ssl; done<br>
</pre><br>
证书生成完成后调整每台机器的 etcd 配置文件，然后修复权限启动。<br>
<pre class="prettyprint"># 复制配置<br>
for ip in `seq 1 3`; do scp /etc/etcd/etcd.cluster.yaml root@10.0.0.1$ip:/etc/etcd/etcd.yaml; done<br>
<br>
# 修复权限<br>
for ip in `seq 1 3`; do ssh root@10.0.0.1$ip chown -R etcd:etcd /etc/etcd; done<br>
<br>
# 每台机器启动<br>
systemctl start etcd<br>
</pre><br>
启动完成后通过 <code class="prettyprint">etcdctl</code> 验证集群状态：<br>
<pre class="prettyprint"># 稳妥点应该执行 etcdctl endpoint health<br>
➜ ~ etcdctl member list<br>
55fcbe0adaa45350, started, etcd3, https://10.0.0.13:2380, https://10.0.0.13:2379, false<br>
cebdf10928a06f3c, started, etcd1, https://10.0.0.11:2380, https://10.0.0.11:2379, false<br>
f7a9c20602b8532e, started, etcd2, https://10.0.0.12:2380, https://10.0.0.12:2379, false<br>
</pre><br>
<h4>2.2、安装 kubeadm</h4>kubeadm 国内用户建议使用 aliyun 的安装源：<br>
<pre class="prettyprint"># kubeadm<br>
apt-get install -y apt-transport-https<br>
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add -<br>
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list<br>
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main<br>
EOF<br>
apt update<br>
<br>
# ebtables、ethtool kubelet 可能会用，具体忘了，反正从官方文档上看到的<br>
apt install kubelet kubeadm kubectl ebtables ethtool -y<br>
</pre><br>
<h4>2.3、安装 kube-apiserver-proxy</h4>kube-apiserver-proxy 是我自己编译的一个仅开启四层代理的 Nginx，其主要负责监听 <code class="prettyprint">127.0.0.1:6443</code> 并负载到所有的 Api Server 地址（<code class="prettyprint">0.0.0.0:5443</code>）：<br>
<pre class="prettyprint">wget https://github.com/mritd/kube-apiserver-proxy-pack/releases/download/v1.20.0/kube-apiserver-proxy_v1.20.0.run<br>
chmod +x *.run<br>
./kube-apiserver-proxy_v1.20.0.run install<br>
</pre><br>
安装完成后根据 IP 地址不同自行调整 Nginx 配置文件，然后启动：<br>
<pre class="prettyprint">➜ ~ cat /etc/kubernetes/apiserver-proxy.conf<br>
error_log syslog:server=unix:/dev/log notice;<br>
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
    server 10.0.0.11:5443;<br>
    server 10.0.0.12:5443;<br>
    server 10.0.0.13:5443;<br>
&#125;<br>
<br>
server &#123;<br>
    listen        0.0.0.0:6443;<br>
    proxy_pass    kube_apiserver;<br>
    proxy_timeout 10m;<br>
    proxy_connect_timeout 1s;<br>
&#125;<br>
&#125;<br>
<br>
systemctl start kube-apiserver-proxy<br>
</pre><br>
<h4>2.4、安装 kubeadm-config</h4>kubeadm-config 是一系列配置文件的组合以及 kubeadm 安装所需的必要镜像文件的打包，安装完成后将会自动配置 Containerd、ctrictl 等：<br>
<pre class="prettyprint">wget https://github.com/mritd/kubeadm-config-pack/releases/download/v1.21.1/kubeadm-config_v1.21.1.run<br>
chmod +x *.run<br>
<br>
# --load 选项用于将 kubeadm 所需镜像 load 到 containerd 中<br>
./kubeadm-config_v1.21.1.run install --load<br>
</pre><br>
<strong>2.4.1、containerd 配置</strong><br>
<br>Containerd 配置位于 <code class="prettyprint">/etc/containerd/config.toml</code>，其配置如下：<br>
<pre class="prettyprint">version = 2<br>
# 指定存储根目录<br>
root = "/data/containerd"<br>
state = "/run/containerd"<br>
# OOM 评分<br>
oom_score = -999<br>
<br>
[grpc]<br>
address = "/run/containerd/containerd.sock"<br>
<br>
[metrics]<br>
address = "127.0.0.1:1234"<br>
<br>
[plugins]<br>
[plugins."io.containerd.grpc.v1.cri"]<br>
# sandbox 镜像<br>
sandbox_image = "k8s.gcr.io/pause:3.4.1"<br>
[plugins."io.containerd.grpc.v1.cri".containerd]<br>
  snapshotter = "overlayfs"<br>
  default_runtime_name = "runc"<br>
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes]<br>
    [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]<br>
      runtime_type = "io.containerd.runc.v2"<br>
      # 开启 systemd cgroup<br>
      [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]<br>
        SystemdCgroup = true<br>
</pre><br>
<strong>2.4.2、crictl 配置</strong><br>
<br>在切换到 Containerd 以后意味着以前的 <code class="prettyprint">Docker</code> 命令将不再可用，containerd 默认自带了一个 <code class="prettyprint">ctr</code> 命令，同时 CRI 规范会自带一个 <code class="prettyprint">crictl</code> 命令；<code class="prettyprint">crictl</code> 命令配置文件存放在 <code class="prettyprint">/etc/crictl.yaml</code> 中：<br>
<pre class="prettyprint">runtime-endpoint: unix:///run/containerd/containerd.sock<br>
image-endpoint: unix:///run/containerd/containerd.sock<br>
pull-image-on-create: true<br>
</pre><br>
<strong>2.4.3、kubeadm 配置</strong><br>
<br>kubeadm 配置目前分为 2 个，一个是用于首次引导启动的 init 配置，另一个是用于其他节点 join 到 master 的配置；其中比较重要的 init 配置如下：<br>
<pre class="prettyprint"># /etc/kubernetes/kubeadm.yaml<br>
apiVersion: kubeadm.k8s.io/v1beta2<br>
kind: InitConfiguration<br>
# kubeadm token create<br>
bootstrapTokens:<br>
- token: "c2t0rj.cofbfnwwrb387890"<br>
nodeRegistration:<br>
# CRI 地址(Containerd)<br>
criSocket: unix:///run/containerd/containerd.sock<br>
kubeletExtraArgs:<br>
runtime-cgroups: "/system.slice/containerd.service"<br>
rotate-server-certificates: "true"<br>
localAPIEndpoint:<br>
advertiseAddress: "10.0.0.11"<br>
bindPort: 5443<br>
# kubeadm certs certificate-key<br>
certificateKey: 31f1e534733a1607e5ba67b2834edd3a7debba41babb1fac1bee47072a98d88b<br>
---<br>
apiVersion: kubeadm.k8s.io/v1beta2<br>
kind: ClusterConfiguration<br>
clusterName: "kuberentes"<br>
kubernetesVersion: "v1.21.1"<br>
certificatesDir: "/etc/kubernetes/pki"<br>
# Other components of the current control plane only connect to the apiserver on the current host.<br>
# This is the expected behavior, see: https://github.com/kubernetes/kubeadm/issues/2271<br>
controlPlaneEndpoint: "127.0.0.1:6443"<br>
etcd:<br>
external:<br>
endpoints:<br>
- "https://10.0.0.11:2379"<br>
- "https://10.0.0.12:2379"<br>
- "https://10.0.0.13:2379"<br>
caFile: "/etc/etcd/ssl/etcd-ca.pem"<br>
certFile: "/etc/etcd/ssl/etcd.pem"<br>
keyFile: "/etc/etcd/ssl/etcd-key.pem"<br>
networking:<br>
serviceSubnet: "10.66.0.0/16"<br>
podSubnet: "10.88.0.1/16"<br>
dnsDomain: "cluster.local"<br>
apiServer:<br>
extraArgs:<br>
v: "4"<br>
alsologtostderr: "true"<br>
#    audit-log-maxage: "21"<br>
#    audit-log-maxbackup: "10"<br>
#    audit-log-maxsize: "100"<br>
#    audit-log-path: "/var/log/kube-audit/audit.log"<br>
#    audit-policy-file: "/etc/kubernetes/audit-policy.yaml"<br>
authorization-mode: "Node,RBAC"<br>
event-ttl: "720h"<br>
runtime-config: "api/all=true"<br>
service-node-port-range: "30000-50000"<br>
service-cluster-ip-range: "10.66.0.0/16"<br>
#    insecure-bind-address: "0.0.0.0"<br>
#    insecure-port: "8080"<br>
# The fraction of requests that will be closed gracefully(GOAWAY) to prevent<br>
# HTTP/2 clients from getting stuck on a single apiserver.<br>
goaway-chance: "0.001"<br>
#  extraVolumes:<br>
#  - name: "audit-config"<br>
#    hostPath: "/etc/kubernetes/audit-policy.yaml"<br>
#    mountPath: "/etc/kubernetes/audit-policy.yaml"<br>
#    readOnly: true<br>
#    pathType: "File"<br>
#  - name: "audit-log"<br>
#    hostPath: "/var/log/kube-audit"<br>
#    mountPath: "/var/log/kube-audit"<br>
#    pathType: "DirectoryOrCreate"<br>
certSANs:<br>
- "*.kubernetes.node"<br>
- "10.0.0.11"<br>
- "10.0.0.12"<br>
- "10.0.0.13"<br>
timeoutForControlPlane: 1m<br>
controllerManager:<br>
extraArgs:<br>
v: "4"<br>
node-cidr-mask-size: "19"<br>
deployment-controller-sync-period: "10s"<br>
experimental-cluster-signing-duration: "8670h"<br>
node-monitor-grace-period: "20s"<br>
pod-eviction-timeout: "2m"<br>
terminated-pod-gc-threshold: "30"<br>
scheduler:<br>
extraArgs:<br>
v: "4"<br>
---<br>
apiVersion: kubelet.config.k8s.io/v1beta1<br>
kind: KubeletConfiguration<br>
failSwapOn: false<br>
oomScoreAdj: -900<br>
cgroupDriver: "systemd"<br>
kubeletCgroups: "/system.slice/kubelet.service"<br>
nodeStatusUpdateFrequency: 5s<br>
rotateCertificates: true<br>
evictionSoft:<br>
"imagefs.available": "15%"<br>
"memory.available": "512Mi"<br>
"nodefs.available": "15%"<br>
"nodefs.inodesFree": "10%"<br>
evictionSoftGracePeriod:<br>
"imagefs.available": "3m"<br>
"memory.available": "1m"<br>
"nodefs.available": "3m"<br>
"nodefs.inodesFree": "1m"<br>
evictionHard:<br>
"imagefs.available": "10%"<br>
"memory.available": "256Mi"<br>
"nodefs.available": "10%"<br>
"nodefs.inodesFree": "5%"<br>
evictionMaxPodGracePeriod: 30<br>
imageGCLowThresholdPercent: 70<br>
imageGCHighThresholdPercent: 80<br>
kubeReserved:<br>
"cpu": "500m"<br>
"memory": "512Mi"<br>
"ephemeral-storage": "1Gi"<br>
---<br>
apiVersion: kubeproxy.config.k8s.io/v1alpha1<br>
kind: KubeProxyConfiguration<br>
# kube-proxy specific options here<br>
clusterCIDR: "10.88.0.1/16"<br>
mode: "ipvs"<br>
oomScoreAdj: -900<br>
ipvs:<br>
minSyncPeriod: 5s<br>
syncPeriod: 5s<br>
scheduler: "wrr"<br>
</pre><br>
init 配置具体含义请自行参考官方文档，相对于 init 配置，join 配置比较简单，不过需要注意的是如果需要 join 为 master 则需要 <code class="prettyprint">controlPlane</code> 这部分，否则请注释掉 <code class="prettyprint">controlPlane</code>。<br>
<pre class="prettyprint"># /etc/kubernetes/kubeadm-join.yaml<br>
apiVersion: kubeadm.k8s.io/v1beta2<br>
kind: JoinConfiguration<br>
controlPlane:<br>
localAPIEndpoint:<br>
advertiseAddress: "10.0.0.12"<br>
bindPort: 5443<br>
certificateKey: 31f1e534733a1607e5ba67b2834edd3a7debba41babb1fac1bee47072a98d88b<br>
discovery:<br>
bootstrapToken:<br>
apiServerEndpoint: "127.0.0.1:6443"<br>
token: "c2t0rj.cofbfnwwrb387890"<br>
# Please replace with the "--discovery-token-ca-cert-hash" value printed<br>
# after the kubeadm init command is executed successfully<br>
caCertHashes:<br>
- "sha256:97590810ae34a82501717e33acfca76f16044f1a365c5ad9a1c66433c386c75c"<br>
nodeRegistration:<br>
criSocket: unix:///run/containerd/containerd.sock<br>
kubeletExtraArgs:<br>
runtime-cgroups: "/system.slice/containerd.service"<br>
rotate-server-certificates: "true"<br>
</pre><br>
<h4>2.5、拉起 Master</h4>在调整好配置后，拉起 Master 节点只需要一条命令：<br>
<pre class="prettyprint">kubeadm init --config /etc/kubernetes/kubeadm.yaml --upload-certs --ignore-preflight-errors=Swap<br>
</pre><br>
拉起完成后记得保存相关 Token 以便于后续使用。<br>
<h4>2.6、拉起其他 Master</h4>在第一个 Master 启动完成后，使用 <code class="prettyprint">join</code> 命令让其他 Master 加入即可；需要注意的是 <code class="prettyprint">kubeadm-join.yaml</code> 配置中需要替换 <code class="prettyprint">caCertHashes</code> 为第一个 Master 拉起后的 <code class="prettyprint">discovery-token-ca-cert-hash</code> 的值。<br>
<pre class="prettyprint">kubeadm join 127.0.0.1:6443 --config /etc/kubernetes/kubeadm-join.yaml --ignore-preflight-errors=Swap<br>
</pre><br>
<h4>2.7、拉起其他 Node</h4>Node 节点拉起与拉起其他 Master 节点一样，唯一不同的是需要注释掉配置中的 <code class="prettyprint">controlPlane</code> 部分。<br>
<pre class="prettyprint"># /etc/kubernetes/kubeadm-join.yaml<br>
apiVersion: kubeadm.k8s.io/v1beta2<br>
kind: JoinConfiguration<br>
<h1>controlPlane:</h1> #  localAPIEndpoint:<br>
#    advertiseAddress: "10.0.0.12"<br>
#    bindPort: 5443<br>
#  certificateKey: 31f1e534733a1607e5ba67b2834edd3a7debba41babb1fac1bee47072a98d88b<br>
discovery:<br>
bootstrapToken:<br>
apiServerEndpoint: "127.0.0.1:6443"<br>
token: "c2t0rj.cofbfnwwrb387890"<br>
# Please replace with the "--discovery-token-ca-cert-hash" value printed<br>
# after the kubeadm init command is executed successfully<br>
caCertHashes:<br>
- "sha256:97590810ae34a82501717e33acfca76f16044f1a365c5ad9a1c66433c386c75c"<br>
nodeRegistration:<br>
criSocket: unix:///run/containerd/containerd.sock<br>
kubeletExtraArgs:<br>
runtime-cgroups: "/system.slice/containerd.service"<br>
rotate-server-certificates: "true"<br>
</pre><br>
<pre class="prettyprint">kubeadm join 127.0.0.1:6443 --config /etc/kubernetes/kubeadm-join.yaml --ignore-preflight-errors=Swap<br>
</pre><br>
<h4>2.8、其他处理</h4>由于 kubelet 开启了证书轮转，所以新集群会有大量 csr 请求，批量允许即可：<br>
<pre class="prettyprint">kubectl get csr | grep Pending | awk '&#123;print $1&#125;' | xargs kubectl certificate approve<br>
</pre><br>
同时为了 Master 节点也能负载 Pod，需要调整污点：<br>
<pre class="prettyprint">kubectl taint nodes --all node-role.kubernetes.io/master-<br>
</pre><br>
后续 CNI 等不在本文内容范围内。<br>
<h3>三、Containerd 常用操作</h3><pre class="prettyprint"># 列出镜像<br>
ctr images ls<br>
<br>
# 列出 k8s 镜像<br>
ctr -n k8s.io images ls<br>
<br>
# 导入镜像<br>
ctr -n k8s.io images import xxxx.tar<br>
<br>
# 导出镜像<br>
ctr -n k8s.io images export kube-scheduler.tar k8s.gcr.io/kube-scheduler:v1.21.1<br>
</pre><br>
<h3>四、资源仓库</h3>本文中所有 <code class="prettyprint">*-pack</code> 仓库地址如下：<br>
<ul><li><a href="https://github.com/mritd/cfssl-pack"></a><a href="https://github.com/mritd/cfssl-pack" rel="nofollow" target="_blank">https://github.com/mritd/cfssl-pack</a></li><li><a href="https://github.com/mritd/etcd-pack"></a><a href="https://github.com/mritd/etcd-pack" rel="nofollow" target="_blank">https://github.com/mritd/etcd-pack</a></li><li><a href="https://github.com/mritd/kube-apiserver-proxy-pack"></a><a href="https://github.com/mritd/kube-apiserver-proxy-pack" rel="nofollow" target="_blank">https://github.com/mritd/kube-apiserver-proxy-pack</a></li><li><a href="https://github.com/mritd/kubeadm-config-pack"></a><a href="https://github.com/mritd/kubeadm-config-pack" rel="nofollow" target="_blank">https://github.com/mritd/kubeadm-config-pack</a></li></ul><br>
<br>原文链接：<a href="https://mritd.com/2021/05/29/use-containerd-with-kubernetes/" rel="nofollow" target="_blank">https://mritd.com/2021/05/29/u ... etes/</a>，作者：bleem
                                
                                                              
</div>
            