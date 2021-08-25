
---
title: '后Kubernetes时代的虚拟机管理技术之kubevirt篇'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/bc2a36cf2ec56937a9bcf638376f611b.png'
author: Dockone
comments: false
date: 2021-08-25 01:47:14
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/bc2a36cf2ec56937a9bcf638376f611b.png'
---

<div>   
<br>kubevirt是Red Hat开源的以容器方式运行虚拟机的项目，是基于kubernetes运行，利用k8s CRD为增加资源类型VirtualMachineInstance（VMI），使用CRD的方式是由于kubevirt对虚拟机的管理不局限于pod管理接口。通过CRD机制，kubevirt可以自定义额外的操作，来调整常规容器中不可用的行为。kubevirt可以使用容器的image registry去创建虚拟机并提供VM生命周期管理。<br>
Kubevirt的架构<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/bc2a36cf2ec56937a9bcf638376f611b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/bc2a36cf2ec56937a9bcf638376f611b.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>    kubevirt以CRD的形式将VM管理接口接入到kubernetes中，通过一个pod去使用libvirtd管理VM的方式，实现pod与VM的一一对应，做到如同容器一般去管理虚拟机，并且做到与容器一样的资源管理、调度规划、这一层整体与企业IAAS关系不大，也方便企业的接入，统一纳管。<br>
virt-api：kubevirt是以CRD形式去管理VM Pod，virt-api就是所有虚拟化操作的入口，这里面包括常规的CDR更新验证、以及console、vm start、stop等操作。<br>
    virt-controller：virt-controller会根据vmi CRD，生成对应的virt-launcher Pod，并且维护CRD的状态。与kubernetes api-server通讯监控VMI资源的创建删除等状态。<br>
    virt-handler：virt-handler会以deamonset形式部署在每一个节点上，负责监控节点上的每个虚拟机实例状态变化，一旦检测到状态的变化，会进行响应并且确保相应的操作能够达到所需（理想）的状态。virt-handler还会保持集群级别VMI Spec与相应libvirt域之间的同步；报告libvirt域状态和集群Spec的变化；调用以节点为中心的插件以满足VMI Spec定义的网络和存储要求。<br>
virt-launcher：每个virt-launcher pod对应着一个VMI，kubelet只负责virt-launcher pod运行状态，不会去关心VMI创建情况。virt-handler会根据CRD参数配置去通知virt-launcher去使用本地的libvirtd实例来启动VMI，随着Pod的生命周期结束，virt-lanuncher也会去通知VMI去执行终止操作；其次在每个virt-launcher pod中还对应着一个libvirtd，virt-launcher通过libvirtd去管理VM的生命周期，这样做到去中心化，不再是以前的虚拟机那套做法，一个libvirtd去管理多个VM。<br>
virtctl：virtctl是kubevirt自带类似kubectl的命令行工具，它是越过virt-launcher pod这一层去直接管理VM虚拟机，可以控制VM的start、stop、restart。<br>
Kubevirt如何管理虚拟机？<br>
虚拟机镜像制作与管理<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/ec5d9c086f01209ee6b1e403d0a6537f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/ec5d9c086f01209ee6b1e403d0a6537f.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>    虚拟机镜像采用容器镜像形式存放在镜像仓库中。创建原理如上图所示，将Linux发行版本的镜像文件存放到基础镜像的/disk目录内，镜像格式支持qcow2、raw、img。通过Dockerfile文件将虚拟机镜像制作成容器镜像，然后分别推送到不同的registry镜像仓库中。客户在创建虚拟机时，根据配置的优先级策略拉取registry中的虚拟机容器镜像，如果其中一台registry故障，会另一台健康的registry拉取镜像。<br>
虚拟机生命周期管理<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/6d53696c69281711eeb8a69c9f7f4045.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/6d53696c69281711eeb8a69c9f7f4045.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>    KubeVirt虚拟机生命周期管理主要分为以下几种状态：<br>
虚拟机创建：创建VM对象，并同步创建DataVolume/PVC，从Harbor镜像仓库中拉取系统模板镜像拷贝至目标调度主机，通过调度、IP分配后生成VMI以及管理VM的Launcher Pod从而启动供业务使用的VM。<br>
虚拟机运行：运行状态下的VM 可以进行控制台管理、快照备份/恢复、热迁移、磁盘热挂载/热删除等操作，此外还可以进行重启、下电操作，提高VM安全的同时解决业务存储空间需求和主机异常Hung等问题。<br>
虚拟机关机：关机状态下的VM可以进行快照备份/恢复、冷迁移、CPU/MEM规格变更、重命名以及磁盘挂载等操作，同时可通过重新启动进入运行状态，也可删除进行资源回收。<br>
虚拟机删除：对虚机资源进行回收，但VM所属的磁盘数据仍将保留、具备恢复条件。<br>
虚拟机创建流程<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/e33a7f296827604ff66783a270d40050.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/e33a7f296827604ff66783a270d40050.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>虚拟机创建分为创建DataVolume和VMI两个流程：<br>
1.创建DataVolume后，CDI组件创建对应的PVC并且关联到合适的PV，然后通过临时Importer Pod拉取虚拟机容器镜像绑定到DataVolume生成的PV中，并且将镜像转换成disk.img文件存储在PV中供虚拟机使用。<br>
2.创建VMI后，等待disk.img转换成功，然后在对应的Node上启动Launcher Pod，并将CDI流程生成的PV挂载到Pod内，当做虚拟机启动的系统盘。Launcher根据VMI的定义生成定义虚拟机的XML文件，然后调用libvirt进程调用Qemu命令创建并且启动虚拟机。VMI会对Launcher Pod状态进行同步，反应VM运行的状态。<br>
Kubevirt如何实现容器与虚拟机交互TBD<br>
容器和虚拟机互通<br>
Virtual-Kubelet对应的Node会上报节点上Pod的Endpoint，假定Kubernetes集群和IaaS层平台部署在同一个二层网络下，则集群内容器Pod可以访问VM-Pod，但容器Pod对于VM-Pod不可见；<br>
针对上一点可以通过Macvlan等网络插件，将容器-Pod，降维至二层网络上，实现容器-Pod和虚拟机互通，有一定硬件要求。<br>
如何实现⼀套集群下虚拟机与容器的混合调度与资源隔离<br>
Virtual-Kubelet提供的是一个虚拟节点用来向Kubernetes上报Node对象和Pod的状态和资源情况，虚拟机资源和集群内节点资源完全隔离；<br>
在引入Virtual-Kubelet的情况下，需要对Virtual-Kubelet节点配置Taint和Tolerations，保证容器-Pod和VM-Pod调度分离。<br>
服务发现<br>
Virtual-Kubelet，通过Provider实现的API将IaaS层VM信息抽象成对应Pod对象的信息的方式来上报Endpoints，可以通过给CR添加no selector Service，待VM-Pod拉起后补充address至对应的Service<br>
Kubevirt适用场景<br>
由于Kubervirt提供的成熟的虚拟化能力和性能，并且可以直接通过Kubernetes进行统一管理。所以Kubevirt适合在有PaaS层管理平台和Kubernetes集群环境的情况下，通过kubevirt中的单一控制平面简化了对虚拟机的管理，让用户无需关心IaaS层，即可轻松在集群内构建、部署出一台虚拟机进行使用。<br>
如何搭建Kubevirt<br>
Kubevirt安装<br>
1.前置条件<br>
查看硬件是否支持虚拟化<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/7ad36203b0839916a702c2bffe6c2544.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/7ad36203b0839916a702c2bffe6c2544.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>如果虚拟化不可用，则需要手动开启软件仿真<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/2b2147f98db0a9c4a0df6e713bae23be.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/2b2147f98db0a9c4a0df6e713bae23be.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>2.安装Kubevirt组件<br>
直接操作以下命令进行安装<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/07bcc4e0824de0c07aafc5fbd92dd303.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/07bcc4e0824de0c07aafc5fbd92dd303.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>3.检查实例是否正常运行<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/f1eaffb2966781c998b504843fd722a3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/f1eaffb2966781c998b504843fd722a3.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>4.启动相关特性<br>
修改kubevirt-config configmap内的数据<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/b493f6e762737f0ff85a932c9ee2d3d0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/b493f6e762737f0ff85a932c9ee2d3d0.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>5.安装virtctl<br>
安装kubevirt命令行工具<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/303c2339aa2957dd6485ef91e4c2e2a5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/303c2339aa2957dd6485ef91e4c2e2a5.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>6.安装CDI<br>
CDI(containerized-data-importer) 是kubernetes的持久存储管理插件，帮助kubevirt构建磁盘镜像，可以将不同来源的数据源（url、container image、upload....）来填充pvc的能力。<br>
获取最新版，进行安装<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/7392e274c0a07d24d14624df4204fc63.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/7392e274c0a07d24d14624df4204fc63.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>安装完毕后，会在cdi namespace下，启动cdi相关组件<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/557b10edb3484c1d7a1af10e4a9d452f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/557b10edb3484c1d7a1af10e4a9d452f.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>    至此，kubevirt安装完毕<br>
创建虚拟机<br>
1.准备一个虚拟机镜像<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/e5dc7518d117a1dabf4b42edabdeb98d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/e5dc7518d117a1dabf4b42edabdeb98d.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>    通过dockerfile构建出一个虚拟机镜像<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/dbfd21e00f9281c78d31d97db66da973.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/dbfd21e00f9281c78d31d97db66da973.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>2.创建一台VM<br>
编辑好yaml文件，通过kubectl命令拉起一台vm<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/ebcb1088627ac04fbdd1b66bde2b873d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/ebcb1088627ac04fbdd1b66bde2b873d.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/8cb13761c96ce8c3e477a6b767ba0092.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/8cb13761c96ce8c3e477a6b767ba0092.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>加粗文字</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            