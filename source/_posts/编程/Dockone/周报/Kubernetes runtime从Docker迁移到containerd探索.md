
---
title: 'Kubernetes runtime从Docker迁移到containerd探索'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/4a054b984df614836f315fb80ec0469f.png'
author: Dockone
comments: false
date: 2021-05-20 04:11:25
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/4a054b984df614836f315fb80ec0469f.png'
---

<div>   
<br>Kubernetes宣布在1.20版本之后将弃用Docker作为容器运行时，在2021年末发布的1.23版本中将彻底移除dockershim组件。Dockershim是kubelet内置的一个组件，功能是使Kubernetes能够通过CRI（Container Runtime Interface）操作Docker。一旦Docker有任何的功能特性变更，dockershim 代码必须加以改动来保证能够继续和Docker通信。另外，Docker的底层运行时是containerd，而containerd自身是可以支持CRI的，也就是说Kubernetes可以绕过Docker通过CRI直接与containerd通信，这也是Kubernetes社区希望弃用dockershim的原因。<br>
<br>Containerd在1.0版本中虽然考虑了CRI，但是它将CRI-Containerd作为一个独立组件存在的，即：Kubernetes需要先通过CRI接口调用CRI-Containerd，再由这个组件去调用containerd。在Containerd 1.1版本之后对该特性做了重新的设计，它将CRI-plugin内嵌在containerd中，以此来达到与containerd通信的目的，调用链路更短了。Containerd 1.1支持Kubernetes 1.10及以上版本作为容器运行时，并且支持Kubernetes的全部特性。<br>
<br>下图说明了Docker和containerd作为容器运行时的工作原理。由此可以看出，如果之前使用Docker作为容器运行时，那么迁移到containerd是一个相对容易的选择，而且containerd具有更好的性能和更低的成本。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210518/4a054b984df614836f315fb80ec0469f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/4a054b984df614836f315fb80ec0469f.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
接下来，主要介绍如何将Kubernetes的运行时从Docker迁移到containerd，并且迁移之后使用上的一些变化。<br>
<h3>Kubernetes运行时从Docker迁移到containerd</h3><h4>环境准备</h4>操作系统：SUSE 12 SP5<br>
<br>Kernel版本：4.12.14-120<br>
<br>Kubernetes版本：v1.14.0<br>
<br>Docker版本：docker-ee-18.09.9<br>
<br>Containerd版本：1.4.4<br>
<h4>查看当前节点运行时信息</h4><pre class="prettyprint">kubectl get node -o wide<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210518/c3ce604dd0a0ffc6cae826e90eed9e39.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/c3ce604dd0a0ffc6cae826e90eed9e39.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到，当前所有节点使用的运行时都是Docker，通过systemctl status containerd可以看到containerd服务默认也是启动的。使用如下命令列出containerd的命名空间。<br>
<pre class="prettyprint">ctr namespaces list<br>
</pre><br>
可以看到有一个moby命名空间，这也是Docker服务默认使用的命名空间。<br>
<pre class="prettyprint">ctr -namespace moby container list<br>
</pre><br>
使用如上命令列出Moby命名空间下运行的所有容器，结果如下图，可以看到跟docker ps输出的容器个数相同。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210518/d109b5237cc603ef7ff61a859924633c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/d109b5237cc603ef7ff61a859924633c.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>驱逐节点并停止节点上的Docker和kubelet服务</h4>下面以节点spk8mgr03为例说明Docker到containerd的迁移流程。<br>
<pre class="prettyprint">kubectl drain spk8mgr03 --ignore-daemonsets --delete-local-data --force<br>
<br>
systemctl stop kubelet<br>
<br>
systemctl stop docker<br>
</pre><br>
卸载Docker（该步骤是可选的，为了排除测试过程中Docker的干扰，这里选择卸载）：<br>
<pre class="prettyprint">zypper rm -y docker-ee docker-ee-cli containerd.io<br>
</pre><br>
<h4>安装配置containerd</h4>下载containerd并解压安装：<br>
<pre class="prettyprint">wget https://github.com/containerd/containerd/releases/download/v1.4.4/cri-containerd-cni-1.4.4-linux-amd64.tar.gz<br>
<br>
tar -C / -xzvf cri-containerd-cni-1.4.4-linux-amd64.tar.gz<br>
</pre><br>
解压后的文件包括如下内容：<br>
<pre class="prettyprint">/<br>
<br>
/etc/<br>
<br>
/etc/systemd/<br>
<br>
/etc/systemd/system/<br>
<br>
/etc/systemd/system/containerd.service<br>
<br>
/etc/crictl.yaml<br>
<br>
/etc/cni/<br>
<br>
/etc/cni/net.d/<br>
<br>
/etc/cni/net.d/10-containerd-net.conflist<br>
<br>
/usr/<br>
<br>
/usr/local/<br>
<br>
/usr/local/bin/<br>
<br>
/usr/local/bin/containerd<br>
<br>
/usr/local/bin/containerd-shim<br>
<br>
/usr/local/bin/crictl<br>
<br>
/usr/local/bin/containerd-shim-runc-v2<br>
<br>
/usr/local/bin/critest<br>
<br>
/usr/local/bin/containerd-shim-runc-v1<br>
<br>
/usr/local/bin/ctr<br>
<br>
/usr/local/sbin/<br>
<br>
/usr/local/sbin/runc<br>
<br>
/opt/<br>
<br>
/opt/containerd/<br>
<br>
/opt/containerd/cluster/<br>
<br>
/opt/containerd/cluster/gce/<br>
<br>
/opt/containerd/cluster/gce/env<br>
<br>
/opt/containerd/cluster/gce/cni.template<br>
<br>
/opt/containerd/cluster/gce/configure.sh<br>
<br>
/opt/containerd/cluster/gce/cloud-init/<br>
<br>
/opt/containerd/cluster/gce/cloud-init/node.yaml<br>
<br>
/opt/containerd/cluster/gce/cloud-init/master.yaml<br>
<br>
/opt/containerd/cluster/version<br>
<br>
/opt/cni/<br>
<br>
/opt/cni/bin/<br>
<br>
/opt/cni/bin/bandwidth<br>
<br>
/opt/cni/bin/host-device<br>
<br>
/opt/cni/bin/flannel<br>
<br>
/opt/cni/bin/static<br>
<br>
/opt/cni/bin/loopback<br>
<br>
/opt/cni/bin/dhcp<br>
<br>
/opt/cni/bin/ptp<br>
<br>
/opt/cni/bin/ipvlan<br>
<br>
/opt/cni/bin/vlan<br>
<br>
/opt/cni/bin/host-local<br>
<br>
/opt/cni/bin/firewall<br>
<br>
/opt/cni/bin/tuning<br>
<br>
/opt/cni/bin/sbr<br>
<br>
/opt/cni/bin/bridge<br>
<br>
/opt/cni/bin/portmap<br>
<br>
/opt/cni/bin/macvlan<br>
</pre><br>
启动并配置containerd：<br>
<pre class="prettyprint">systemctl start containerd<br>
<br>
systemctl enable containerd<br>
<br>
mkdir -p /etc/containerd<br>
<br>
containerd config default > /etc/containerd/config.toml<br>
</pre><br>
config.toml文件内容如下，注意修改sandbox_image参数：<br>
<pre class="prettyprint">version = 2<br>
<br>
root = "/var/lib/containerd"<br>
<br>
state = "/run/containerd"<br>
<br>
plugin_dir = ""<br>
<br>
disabled_plugins = []<br>
<br>
required_plugins = []<br>
<br>
oom_score = 0<br>
<br>
<br>
<br>
[grpc]<br>
<br>
address = "/run/containerd/containerd.sock"<br>
<br>
tcp_address = ""<br>
<br>
tcp_tls_cert = ""<br>
<br>
tcp_tls_key = ""<br>
<br>
uid = 0<br>
<br>
gid = 0<br>
<br>
max_recv_message_size = 16777216<br>
<br>
max_send_message_size = 16777216<br>
<br>
<br>
<br>
[ttrpc]<br>
<br>
address = ""<br>
<br>
uid = 0<br>
<br>
gid = 0<br>
<br>
<br>
<br>
[debug]<br>
<br>
address = ""<br>
<br>
uid = 0<br>
<br>
gid = 0<br>
<br>
level = ""<br>
<br>
<br>
<br>
[metrics]<br>
<br>
address = ""<br>
<br>
grpc_histogram = false<br>
<br>
<br>
<br>
[cgroup]<br>
<br>
path = ""<br>
<br>
<br>
<br>
[timeouts]<br>
<br>
"io.containerd.timeout.shim.cleanup" = "5s"<br>
<br>
"io.containerd.timeout.shim.load" = "5s"<br>
<br>
"io.containerd.timeout.shim.shutdown" = "3s"<br>
<br>
"io.containerd.timeout.task.state" = "2s"<br>
<br>
<br>
<br>
[plugins]<br>
<br>
[plugins."io.containerd.gc.v1.scheduler"]<br>
<br>
pause_threshold = 0.02<br>
<br>
deletion_threshold = 0<br>
<br>
mutation_threshold = 100<br>
<br>
schedule_delay = "0s"<br>
<br>
startup_delay = "100ms"<br>
<br>
[plugins."io.containerd.grpc.v1.cri"]<br>
<br>
disable_tcp_service = true<br>
<br>
stream_server_address = "127.0.0.1"<br>
<br>
stream_server_port = "0"<br>
<br>
stream_idle_timeout = "4h0m0s"<br>
<br>
enable_selinux = false<br>
<br>
selinux_category_range = 1024<br>
<br>
sandbox_image = "k8s.gc.io/pause:3.1"<br>
<br>
stats_collect_period = 10<br>
<br>
systemd_cgroup = false<br>
<br>
enable_tls_streaming = false<br>
<br>
max_container_log_line_size = 16384<br>
<br>
disable_cgroup = false<br>
<br>
disable_apparmor = false<br>
<br>
restrict_oom_score_adj = false<br>
<br>
max_concurrent_downloads = 3<br>
<br>
disable_proc_mount = false<br>
<br>
unset_seccomp_profile = ""<br>
<br>
tolerate_missing_hugetlb_controller = true<br>
<br>
disable_hugetlb_controller = true<br>
<br>
ignore_image_defined_volumes = false<br>
<br>
[plugins."io.containerd.grpc.v1.cri".containerd]<br>
<br>
snapshotter = "overlayfs"<br>
<br>
default_runtime_name = "runc"<br>
<br>
no_pivot = false<br>
<br>
disable_snapshot_annotations = true<br>
<br>
discard_unpacked_layers = false<br>
<br>
[plugins."io.containerd.grpc.v1.cri".containerd.default_runtime]<br>
<br>
runtime_type = ""<br>
<br>
runtime_engine = ""<br>
<br>
runtime_root = ""<br>
<br>
privileged_without_host_devices = false<br>
<br>
base_runtime_spec = ""<br>
<br>
[plugins."io.containerd.grpc.v1.cri".containerd.untrusted_workload_runtime]<br>
<br>
runtime_type = ""<br>
<br>
runtime_engine = ""<br>
<br>
runtime_root = ""<br>
<br>
privileged_without_host_devices = false<br>
<br>
base_runtime_spec = ""<br>
<br>
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes]<br>
<br>
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]<br>
<br>
runtime_type = "io.containerd.runc.v2"<br>
<br>
runtime_engine = ""<br>
<br>
runtime_root = ""<br>
<br>
privileged_without_host_devices = false<br>
<br>
base_runtime_spec = ""<br>
<br>
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]<br>
<br>
[plugins."io.containerd.grpc.v1.cri".cni]<br>
<br>
bin_dir = "/opt/cni/bin"<br>
<br>
conf_dir = "/etc/cni/net.d"<br>
<br>
max_conf_num = 1<br>
<br>
conf_template = ""<br>
<br>
[plugins."io.containerd.grpc.v1.cri".registry]<br>
<br>
[plugins."io.containerd.grpc.v1.cri".registry.mirrors]<br>
<br>
[plugins."io.containerd.grpc.v1.cri".registry.mirrors."docker.io"]<br>
<br>
endpoint = ["https://registry-1.docker.io"]<br>
<br>
[plugins."io.containerd.grpc.v1.cri".image_decryption]<br>
<br>
key_model = ""<br>
<br>
[plugins."io.containerd.grpc.v1.cri".x509_key_pair_streaming]<br>
<br>
tls_cert_file = ""<br>
<br>
tls_key_file = ""<br>
<br>
[plugins."io.containerd.internal.v1.opt"]<br>
<br>
path = "/opt/containerd"<br>
<br>
[plugins."io.containerd.internal.v1.restart"]<br>
<br>
interval = "10s"<br>
<br>
[plugins."io.containerd.metadata.v1.bolt"]<br>
<br>
content_sharing_policy = "shared"<br>
<br>
[plugins."io.containerd.monitor.v1.cgroups"]<br>
<br>
no_prometheus = false<br>
<br>
[plugins."io.containerd.runtime.v1.linux"]<br>
<br>
shim = "containerd-shim"<br>
<br>
runtime = "runc"<br>
<br>
runtime_root = ""<br>
<br>
no_shim = false<br>
<br>
shim_debug = false<br>
<br>
[plugins."io.containerd.runtime.v2.task"]<br>
<br>
platforms = ["linux/amd64"]<br>
<br>
[plugins."io.containerd.service.v1.diff-service"]<br>
<br>
default = ["walking"]<br>
<br>
[plugins."io.containerd.snapshotter.v1.devmapper"]<br>
<br>
root_path = ""<br>
<br>
pool_name = ""<br>
<br>
base_image_size = ""<br>
<br>
async_remove = false<br>
</pre><br>
修改完配置后，重启containerd服务：<br>
<pre class="prettyprint">systemctl restart containerd<br>
</pre><br>
测试containerd：<br>
<pre class="prettyprint">ctr images pull docker.io/library/nginx:alpine<br>
</pre><br>
看到输出done，说明containerd运行正常。<br>
<h3>配置crictl</h3>crictl默认与Docker进行通信，如果希望crictl直接与containerd通信，需要修改crictl的配置文件，在/etc/crictl.yaml加入如下内容：<br>
<pre class="prettyprint">runtime-endpoint: unix:///run/containerd/containerd.sock<br>
</pre><br>
注：安装containerd时解压好的文件默认已经添加了该配置。<br>
<br>测试一下cri插件是否可用：<br>
<pre class="prettyprint">crictl pull docker.io/library/nginx:alpine<br>
<br>
crictl images<br>
</pre><br>
<h4>配置kubelet</h4>kubelet默认使用docker作为容器运行时，如果希望使用containerd，需要修改kubelet的配置文件。编辑/etc/systemd/system/kubelet.service.d/10-kubeadm.conf文件，添加如下内容：<br>
<pre class="prettyprint">[Service]<br>
<br>
Environment="KUBELET_EXTRA_ARGS=--container-runtime=remote --runtime-request-timeout=15m --container-runtime-endpoint=unix:///run/containerd/containerd.sock"<br>
</pre><br>
重启kubelet服务：<br>
<pre class="prettyprint">systemctl daemon-reload<br>
<br>
systemctl restart kubelet<br>
</pre><br>
<h4>验证</h4><pre class="prettyprint">kubectl get node -o wide<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210518/d0aa172e207c20cb9b1d491f176159a4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/d0aa172e207c20cb9b1d491f176159a4.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到spk8mgr03节点的容器运行时已经变成了containerd，这时节点还是不可调度状态，执行如下命令将其改为可调度状态。<br>
<pre class="prettyprint">kubectl uncordon spk8mgr03<br>
</pre><br>
此时再查看containerd的命名空间，会发现多了一个k8s.io的命名空间，而且所有的容器都会运行在该命名空间中，而Moby命名空间中没有任何容器运行了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210518/e4a345a0e5b355bdf6d6f54368e2e152.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/e4a345a0e5b355bdf6d6f54368e2e152.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
至此，我们成功完成了容器运行时从Docker到containerd的迁移，集群中的其他节点可以重复上述步骤完成全部迁移。<br>
<h3>Containerd和Docker使用对比</h3>当使用Docker作为容器运行时，系统管理员有时会登录Kubernetes节点执行Docker命令来收集系统或者应用信息，这些命令都是通过docker CLI实现的。而迁移到containerd之后，可以通过containerd CLI工具ctr来实现与containerd的交互，但是从使用便捷性和功能性上考虑，更推荐使用crictl作为troubleshooting的工具。Crictl是类似于docker CLI的客户端调试工具，并且适用于所有与CRI兼容的容器运行时，包括Docker。下面将围绕镜像、容器、Pod方面比较一下Docker、ctr、crictl常用命令的使用区别。<br>
<h4>镜像相关功能</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210518/a9b95c0834150020eeee4d0e4dceae87.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/a9b95c0834150020eeee4d0e4dceae87.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>容器相关功能</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210518/efd8a5f89ceac77391566c88b5c2811c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/efd8a5f89ceac77391566c88b5c2811c.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这里要特别说明一下，通过ctr containers create创建容器后，只是一个静态的容器，容器中的用户进程并没有启动，所以还需要通过ctr task start来启动容器进程。当然，也可以用ctr run的命令直接创建并运行容器。在进入容器操作时，与docker不同的是，必须在ctr task exec命令后指定--exec-id参数，这个id可以随便写，只要唯一就行。另外，ctr没有stop容器的功能，只能暂停（ctr task pause）或者杀死（ctr task kill）容器。<br>
<h4>Pod相关功能</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210518/0fc1ccfa98a39b6fc811ecff51e27b99.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/0fc1ccfa98a39b6fc811ecff51e27b99.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这里要说明的是：crictl pods列出的是pod的信息，包括pod所在的命名空间以及状态。crictl ps列出的是应用容器的信息，而docker ps列出的是初始化容器（pause容器）和应用容器的信息，初始化容器在每个pod启动时都会创建，通常不会关注，从这一点上来说，crictl使用起来更简洁明了一些。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210518/c3ee0ba0fccfe4e4e3fb94bb702613d1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/c3ee0ba0fccfe4e4e3fb94bb702613d1.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Docker和containerd除了上述常用命令有些区别外，在容器日志及相关参数配置方面也存在一些差异，详见下表。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210518/9e8087e27c6d3bfd8ca5bd4675a0ea40.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210518/9e8087e27c6d3bfd8ca5bd4675a0ea40.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>Kubernetes弃用Docker这一决定可能对从事相关工作的人员来说有些措手不及，但其实无需特别担心。对于Kubernetes的终端用户来说，这仅仅是一个后端容器运行时的更改，从使用方面来说几乎感觉不到任何区别；对于应用开发/运维人员来说，依旧可以继续使用Docker来构建镜像，以相同的方式将镜像推送到registry，并将这些镜像部署到Kubernetes环境中；对于Kubernetes集群管理员来说，只需要将Docker切换成其它的容器运行时（比如containerd），并将节点troubleshooting工具从docker CLI切换到crictl即可。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/0F-Gj0pAGqXinr-sg0vKYg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/0F-Gj0pAGqXinr-sg0vKYg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            