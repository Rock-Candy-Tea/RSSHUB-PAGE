
---
title: 'virtlet是什么？virtlet如何管理虚拟机？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/deb10858cfee05efa64d7497f76a37e4.png'
author: Dockone
comments: false
date: 2021-08-11 01:48:34
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/deb10858cfee05efa64d7497f76a37e4.png'
---

<div>   
<br>随着Docker和Kubernetes生态圈的发展，云计算领域对容器的兴趣达到了狂热的程度。容器技术为应用程序提供了隔离的运行空间，每个容器内都包含一个独享的完整用户环境空间，容器内的变动不会影响其他容器的运行环境。因为容器之间共享同一个系统内核，当同一个库被多个容器使用时，内存的使用效率会得到提升。基于物理主机操作系统内核的，那就意味着对于不同内核或者操作系统需求的应用是不可能部署在一起的。<br>
虚拟化技术则是提供了一个完整的虚拟机，为用户提供了不依赖于宿主机内核的运行环境。对于从物理服务器过渡到虚拟服务器是一个很自然的过程，从用户使用上并没有什么区别。<br>
目前Redhat开源的kubevirt和Mirantis开源的virtlet都提供了以容器方式运行虚拟机的方案。<br>
kubevirt 是 Redhat 开源的以容器方式运行虚拟机的项目，以 k8s add-on方式，利用 k8s CRD 为增加资源类型Virtual Machine Instance（VMI）， 使用容器的image registry去创建虚拟机并提供VM生命周期管理。 用pod管理能力，要自主去实现，目前kubevirt实现了类似RS的功能。<br>
那Virtlet是什么呢？<br>
Virtlet 来自于 Mirantis，跟 kubevirt 的不同之处在于它使用 POD 来描述一个 VM（Virtual Machine,虚拟机)。Virtlet 是 Kubernetes 一个运行时服务，能够根据 QCOW2 映像运行 VM 工作负载。Virtlet是是K8S的一个插件，CRI接口兼容的插件，能够在 Kubernetes 集群上运行基于虚拟机的 Pods。<br>
<strong>Virtlet的架构</strong><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/deb10858cfee05efa64d7497f76a37e4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/deb10858cfee05efa64d7497f76a37e4.png" class="img-polaroid" title="图片1.png" alt="图片1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>CRIProxy作为代理，可以实现在一个节点上支持多种CRI。<br>
kubelet会去调用CRIProxy，由CRIProxy根据pod image前缀（默认virtlet.cloud）决定将请求发给virtlet process 还是dockershim server，从而去创建虚拟机或者容器。<br>
每个节点上会由daemonset负责启动virtlet pod，该virtlet pod包括三个容器：<br>
virtlet：接收 CRI 调用，管理VM<br>
libvirt：接收 virtlet 的请求创建、停止或销毁VM<br>
VMs：所有 virtlet 管理的VM 都会在这个容器的命名空间里<br>
vm的确在vms container下，可以看到对应/proc/&#123;id&#125;/ns/下都是一致的，其实其他container ns只有mnt ns是不一样的。<br>
<strong>Virtlet如何管理虚拟机</strong><br>
虚拟机生命周期管理流程<br>
virtlet使用原生的workload（deployment，statefulset）去管理vm pod，vm的生命周期与pod一致。vm随着pod的创建而创建，随着pod的销毁而销毁。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/db48d85705b3fa0a0a8d7f44026c6c82.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/db48d85705b3fa0a0a8d7f44026c6c82.png" class="img-polaroid" title="图片2.png" alt="图片2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>整体流程：<br>
1.deploy、statefulset等workload创建出对应的pod；<br>
2.kubelet list-watch发现了调度到该节点的pod，根据cri调用criproxy；<br>
3.criproxy会根据pod image前缀判断是将请求发给virtlet还是docker，比如pod image为virtlet.cloud/library/cirrors, 根据前缀匹配到virtlet.cloud,则将请求转给virtlet；<br>
4.virtlet process会根据请求去调用libvirt api通过qemu-kvm去创建/输出虚拟机<br>
<strong>虚拟机存储</strong><br>
virtlet支持原生存储范畴：<br>
emptydir<br>
hostpath<br>
pvc， 需要mode类型是block<br>
flexvolumes<br>
secret，configmap<br>
可以通过annotation字段去配置磁盘驱动以及系统磁盘大小：<br>
<pre class="prettyprint">metadata:<br>
name: my-vm<br>
annotations:<br>
kubernetes.io/target-runtime: virtlet.cloud<br>
VirtletRootVolumeSize: 4Gi<br>
VirtletDiskDriver: virtio<br>
....<br>
</pre><br>
<br>VirtletRootVolumeSize定义了根卷的磁盘大小，VirtletDiskDriver定义了磁盘驱动，常规磁盘驱动默认为virtio-scsi。<br>
其中virtlet也支持cloud-init进行初始化配置，定义ssh密码以及相关用户、网络等初始化：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Pod<br>
metadata:<br>
name: ubuntu-vm<br>
annotations:<br>
kubernetes.io/target-runtime: virtlet.cloud<br>
<br>
# override some fields in cloud-init meta-data<br>
VirtletCloudInitMetaData: |<br>
  instance-id: foobar<br>
<br>
# override some fields in cloud-init user-data<br>
VirtletCloudInitUserData: |<br>
  users:<br>
  - name: cloudy<br>
    gecos: Magic Cloud App Daemon User<br>
    inactive: true<br>
    system: true<br>
</pre><br>
<br><strong>virtlet管理的虚拟机与容器如何实现整体交互</strong><br>
virtlet与常规CRI一样，也是使用CNI管理虚拟机的网络。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/d3ec09faa874fb023e03e43fed41f92e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/d3ec09faa874fb023e03e43fed41f92e.png" class="img-polaroid" title="图片3.png" alt="图片3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>virtlet去调用cni之前，会创建出新的network namespace，通过tap设备连接虚拟机，veth pair连接主机网络与cni 网络模型。<br>
当前连通virtlet管理的虚拟机方式：<br>
根据virtlet pod IP地址，直接ssh形式<br>
kubectl attach命令， virtlet提供attach接口，能够以类似console形式访问<br>
virtletctl 命令，提供ssh，vps形式<br>
虚拟机镜像<br>
virtlet支持qcow格式的镜像文件，但需要在pod image定义中指定virtlet.cloud前缀。virtlet会将对镜像进行名称转换, 将名称转换成虚拟机镜像下载地址。<br>
当前virtlet支持两种镜像名称转换的方式：<br>
静态配置：默认kube-system会创建名为virtlet-image-translations的configmap<br>
<pre class="prettyprint">translations:<br>
- name: cirros<br>
url: https://github.com/mirantis/virtlet/releases/download/v0.9.3/cirros.img<br>
- name: fedora<br>
url: https://dl.fedoraproject.org/pub/fedora/linux/releases/29/Cloud/x86_64/images/Fedora-Cloud-Base-29-1.2.x86_64.qcow2<br>
</pre><br>
<br>举个例子：<br>
当你将image配置成virtlet.cloud/cirrors, virtlet会将该镜像转换成<br>
<a href="https://github.com/mirantis/virtlet/releases/download/v0.9.3/cirros.img" rel="nofollow" target="_blank">https://github.com/mirantis/vi ... s.img</a>，virtlet根据该地址去下载，下载完毕后从而去创建虚拟机。<br>
自定义对象配置：virtlet提供VirtletImageMapping资源对象，相对来说，优先级会高于静态配置<br>
<pre class="prettyprint">apiVersion: "virtlet.k8s/v1"<br>
kind: VirtletImageMapping<br>
metadata:<br>
name: primary<br>
namespace: kube-system<br>
spec:<br>
prefix: ""<br>
translations:<br>
- ...<br>
- ...<br>
</pre><br>
<br>默认的是，virtlet是基于文件系统进行存储虚拟机镜像，镜像存储地址如下：<br>
<br><pre class="prettyprint">/var/lib/virtlet/images<br>
links/<br>
example.com%whatever%etc -> ../data/2d711642b726b04401627ca9fbac32f5c8530fb1903cc4db02258717921a4881<br>
example.com%same%image   -> ../data/2d711642b726b04401627ca9fbac32f5c8530fb1903cc4db02258717921a4881<br>
anotherimg               -> ../data/a1fce4363854ff888cff4b8e7875d600c2682390412a8cf79b37d0b11148b0fa<br>
data/<br>
2d711642b726b04401627ca9fbac32f5c8530fb1903cc4db02258717921a4881<br>
a1fce4363854ff888cff4b8e7875d600c2682390412a8cf79b37d0b11148b0fa<br>
</pre><br>
    镜像名称中/字段转换成%，并软连接到匹配的数据文件。<br>
Virtlet优缺点<br>
优点<br>
沿用原生workload，virtlet可无缝接入已有平台<br>
复用CRI能力，侵入性小<br>
缺点<br>
引入CRIPROXY链路风险<br>
限于CRI的整体框架内，无法灵活扩展<br>
不支持CSI，仅支持flexvolume存储驱动<br>
不支持备份与迁移等能力<br>
社区活跃度低，已不再继续维护<br>
整体来说，virtlet是一种接入成本低，能够快速融入已有云平台的方式，但由于社区已不维护且本身CRI方式对接的局限性，对后续的可扩展性以及迭代开发来说，其可扩展方式不够优雅且低，迭代开发难度相对来说大。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            