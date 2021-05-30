
---
title: 'KubeVirt在360的探索之路'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/9bece3ba2e6b65c83ac23989f5380500.png'
author: Dockone
comments: false
date: 2021-05-30 00:37:52
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/9bece3ba2e6b65c83ac23989f5380500.png'
---

<div>   
<br>KubeVirt是一个Kubernetes插件，在调度容器之余也可以调度传统的虚拟机。它通过使用自定义资源（CRD）和其它Kubernetes功能来无缝扩展现有的集群，以提供一组可用于管理虚拟机的虚拟化的API。本文作者经过长时间对KubeVirt的调研和实践，总结了kubevirt的一些关键技术和使用经验，现在就跟随作者一起探讨下吧。<br>
<h3>背景简介</h3>当前公司的虚拟化存在两套调度平台，裸金属和VM由OpenStack调度，容器肯定是Kubernetes调度。两套两班人马，人力和资源都存在着一定的重叠和浪费。当前VM和Pod的比例在1：1，同时随着业务的全面上云，大部分Web无状态业务都开始容器化，所以未来Kubernetes+容器肯定是业务发布的主流选择，业界也基本成型。<br>
<br>而VM的使用场景会被压缩，但是VM作为一个常用的运行时，未来也会长期存在较长时间，最后和容器达成一个三七开的比例。同时裸金属物理机，由于部分业务的特性独占需求，也会在未来长期存在。<br>
<h4>OpenStack转型Kubernetes</h4>所以未来可能会长期存在OpenStack+Kubernetes两种虚拟化运行时调度系统，这个增加了团队的维护和学习成本，再加上现在OpenStack社区整体趋于平稳和下滑，外加上OpenStack本身复杂和臃肿的调度架构，和Python在大项目管理和维护方面天生的劣势，造成了相关的人员招聘难度较大，大家的学习和维护热情也降低。<br>
<br>于此相对的是Kubernetes调度系统的全面优越，简洁和更好的可扩展性，Go语言的大项目和易部署维护的天然优势，业界不少公司都在考虑是否可以由Kubernetes来接管VM和裸金属等，因为本质上VM底层干活的是libvirt，qemu-kvm等，裸金属底层是物理机的ipmi，我们是否可以利用Kubernetes的可扩展性，实现一些新的Operator来接管VM和裸金属。<br>
<br>基于上述考虑，最终的目标是用Kubernetes来管一切虚拟化运行时，包含裸金属，VM，Kata，容器，一套调度，多种运行时，用户按需选择。<br>
<h4>技术选型</h4>有了以上想法以后，就开始调研，发现业界在从OpenStack转型Kubernetes的过程中涌现了这么一部分比较好的项目，例如，KubeVirt，Virtlet，Rancher/VM等，但是社区活跃度最高，设计最好的还是KubeVirt。<br>
<br><a href="https://kubevirt.io/2017/technology-comparison.html" rel="nofollow" target="_blank">https://kubevirt.io/2017/techn ... .html</a><br>
<br>文章核心谈了几个点：<br>
<br>KubeVirt是不是一个VM管理平台的替代品，和OpenStack还有ovirt等虚拟化管理平台的区别。<br>
<br>简单来说：KubeVirt只是用Kubernetes管VM，其中会复用Kubernetes的CNI和CSI，所以只是用Operator的方式来操作VM，他不去管网络和存储等。所以和OpenStack中包含Nova，Neutron，Cinder等不一样，可以理解成KubeVirt是一个Kubernetes框架下的，用Go写的Nova VM管理组件。<br>
<br>KubeVirt和Kata的区别。<br>
<br>简单来说：Kata是有着VM的安全性和隔离性，以容器的方式运行，有着容器的速度和特点，但不是一个真正的VM，而Kubevirt是借用Kubernetes的扩展性来管VM，你用到的是一个真正的VM。<br>
<br>KubeVirt和Virtlet的区别。<br>
<br>简单来说：Virtlet是把VM当成一个CRI来跑了，是按Pod API来定义一个VM，所以VM的很多功能比如热迁移等，Virtlet是没法满足VM的全部特性的，算是一个70%功能的VM。<br>
<br>为啥要用Kubernetes管VM，而不是用OpenStack管容器。<br>
<br>简单来说：Kubernetes+容器是未来的主流方向，但是由于历史和业务需要，VM也会存在很长时间，所以我们一套支持VM的容器管理平台Kubernetes，而不是需要一套支持容器的VM管理平台例如OpenStack管容器Magnum这种类似项目。<br>
<h4>选型插曲</h4>有个插曲：在验证Kubevirt的这段时间，正好看到Rancher也发布了基于Kubevirt和Kubernetes的超融合基础架构软件Harvester，从侧面说明，这个方向是有共性的。所有上了年纪的公司，都有OpenStack和Kubernetes的包袱，而Rancher的老总也是CloudStack的创始人，以前和OpenStack竞争的时候落于下风，现在基于Kubernetes和Kubevirt又回到了IaaS的地带，所有技术圈好多也是轮回啊。<br>
<br>所以Kubevirt这种项目也是在很多从IaaS OpenStack转型PaaS Kubernetes的人群中有更多共鸣，年轻Kubernetes原住民可能对这个项目没有太多感知。因为Kubevirt的发起方RedHat，和核心开发者以前也是OpenStack社区的项目Owner等。所以Kubevirt的一些测试公司和用户也都是有此类共同转型背景的人和公司。<br>
<br>基于如上考虑，最终技术选型确定了Kubevirt，接下来对Kubevirt的一些概念和逻辑架构，还有在360的测试和验证之路做一个简单介绍。<br>
<h3>KubeVirt 是什么</h3>KubeVirt是RedHat开源一套以容器方式运行虚拟机的项目，通过Kubernetes云原生来管理虚拟机生命周期。<br>
<h3>KubeVirt CRD</h3>在介绍KubeVirt前我们先了解一下CRD，在Kubernetes里面有一个核心思想既一切都是资源，如同Puppet里面一切都是资源思想。CRD是Kubernetes 1.7之后添加的自定义资源二次开发来扩展Kubernetes API，通过CRD可以向API中添加资源类型，该功能提升了Kubernetes的扩展能力，那么KubeVirt有哪些需要我们理解的CRD资源，这些资源会在我们的学习和理解过程中都是需要注意的，大概简介绍如下几种：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/9bece3ba2e6b65c83ac23989f5380500.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/9bece3ba2e6b65c83ac23989f5380500.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>KubeVirt组件介绍</h3>与OpenStack 类似， KubeVirt每个组件负责不同的功能，不同点是资源调度策略由Kubernetes去管理，其中主要组件如下：virt-api，virt-controller，virt-handler，virt-launcher。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/4dd1d67e0611e5348d203b4e3669a6f1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/4dd1d67e0611e5348d203b4e3669a6f1.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Kubevirt常见操作</h3><pre class="prettyprint">type DomainManager interface &#123;<br>
//SyncVMI 为创建虚拟机<br>
SyncVMI(*v1.VirtualMachineInstance, bool, *cmdv1.VirtualMachineOptions) (*api.DomainSpec, error)<br>
//暂停VMI<br>
PauseVMI(*v1.VirtualMachineInstance) error<br>
//恢复暂停的VMI<br>
UnpauseVMI(*v1.VirtualMachineInstance) error<br>
KillVMI(*v1.VirtualMachineInstance) error<br>
//删除VMI<br>
DeleteVMI(*v1.VirtualMachineInstance) error<br>
SignalShutdownVMI(*v1.VirtualMachineInstance) error<br>
MarkGracefulShutdownVMI(*v1.VirtualMachineInstance) error<br>
ListAllDomains() ([]*api.Domain, error)<br>
//迁移VMI<br>
MigrateVMI(*v1.VirtualMachineInstance, *cmdclient.MigrationOptions) error<br>
PrepareMigrationTarget(*v1.VirtualMachineInstance, bool) error<br>
GetDomainStats() ([]*stats.DomainStats, error)<br>
//取消迁移<br>
CancelVMIMigration(*v1.VirtualMachineInstance) error<br>
//如下需要启用Qemu guest agent，没启用会包VMI does not have guest agent connected<br>
GetGuestInfo() (v1.VirtualMachineInstanceGuestAgentInfo, error)<br>
GetUsers() ([]v1.VirtualMachineInstanceGuestOSUser, error)<br>
GetFilesystems() ([]v1.VirtualMachineInstanceFileSystem, error)<br>
SetGuestTime(*v1.VirtualMachineInstance) error<br>
&#125; <br>
</pre><br>
<h3>KubeVirt虚机VMI</h3><pre class="prettyprint">[root@openstack825 ~]# kubectl get vmi -o wide<br>
NAME                          AGE     PHASE     IP             NODENAME        LIVE-MIGRATABLE<br>
test100.foo.demo.example.com     8d   Running   192.168.10.30  10.10.67.244   True<br>
test200.foo.demo.example.com     8d   Running   192.168.10.31  10.10.67.245   True<br>
</pre><br>
<pre class="prettyprint">获取已安装的kubevirt pod<br>
[root@openstack825 ~]# kubectl  -n kubevirt get pod<br>
NAME                               READY   STATUS    RESTARTS   AGE<br>
virt-api-68c958dd-6sx4n            1/1     Running   0          14d<br>
virt-api-68c958dd-sldgr            1/1     Running   0          14d<br>
virt-controller-647d666bd5-gsnzf   1/1     Running   1          14d<br>
virt-controller-647d666bd5-hshnz   1/1     Running   1          14d<br>
virt-handler-4g7ck                 1/1     Running   3          14d<br>
virt-handler-kzv86                 1/1     Running   0          14d<br>
virt-handler-m2ppb                 1/1     Running   0          14d<br>
virt-handler-v6fgt                 1/1     Running   0          14d<br>
virt-operator-65ccf74f56-b82kz     1/1     Running   0          14d<br>
virt-operator-65ccf74f56-zs2xq     1/1     Running   0          14d<br>
virtvnc-947874d99-hn7k5            1/1     Running   0          6d19h<br>
</pre><br>
总结：同时我们在调研过程遇到一些问题，比如重启数据丢失、VMI重启和热迁移后IP改变、镜像导入数据缓慢、VMI启动调度缓慢、热迁移网络与存储支持等等。KubeVirt通过CRD方式将VM管理接口接入到Kubernetes集群，而Pod使用libvirtd管理VMI，如容器一样去管理VMI，最后通过标准化插件方式管理调度网络和存储资源对象，将其整合在一起形成一套 具有Kubernetes管理虚拟化的技术栈。<br>
<h3>KubeVirt存储</h3>虚拟机镜像（磁盘）是启动虚拟机必不可少的部分，目前KubeVirt中提供多种方式的虚拟机磁盘。<br>
<br>cloudInitNoCloud/cloudInitConfigDrive：用于提供cloud-init初始化所需要的user-data，使用ConfigMap作为数据源，此时VMI内部将出现第二块大约为356KB的第二块硬盘。<br>
<pre class="prettyprint">devices:<br>
     disks:<br>
     - disk:<br>
         bus: virtio<br>
       name: cloudinit<br>
- cloudInitNoCloud:<br>
     userData: |<br>
       #cloud-config<br>
       password: kubevirt<br>
[centos@xxxv ~]$ lsblk<br>
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT<br>
vda    253:0    0   47G  0 disk<br>
└─vda1 253:1    0   47G  0 part /<br>
vdb    253:16   0  366K  0 disk<br>
</pre><br>
dataVolume：虚拟机启动流程中自动将虚拟机磁盘导入PVC的功能，在不使用DataVolume的情况下，用户必须先准备带有磁盘映像的PVC，然后再将其分配给VM或VMI。dataVolume拉取镜像的来源可以是HTTP、PVC。<br>
<pre class="prettyprint">spec:<br>
 pvc:<br>
   accessModes:<br>
   - ReadWriteMany<br>
   volumeMode: Block<br>
   resources:<br>
     requests:<br>
       storage: 55G<br>
   storageClassName:  csi-rbd-sc<br>
 source:<br>
   http:<br>
     url: http://127.0.0.1:8081/CentOS7.4_AMD64_2.1<br>
</pre><br>
PersistentVolumeClaim：PVC做为后端存储，适用于数据持久化，即在虚拟机重启或关机后数据依然存在。PV类型可以是block和filesystem，为filesystem时，将使用PVC上的disk.img，格式为RAW格式的文件作为硬盘。block模式时，使用block volume直接作为原始块设备提供给虚拟机。缺点在于仅支持RAW格式镜像，若镜像较大CDI导入镜像会比较慢（如果是QCW2 CDI内部机制qemu.go会将其进行格式转换为RAW并导入PVC中），因此降低快速创建VMI体验感。当然社区目前支持一种较smart-clone方式导入，目前笔者还没进行测试。<br>
<pre class="prettyprint">spec:<br>
 pvc:<br>
   accessModes:<br>
   - ReadWriteMany<br>
   volumeMode: Block<br>
   resources:<br>
     requests:<br>
       storage: 55G<br>
   storageClassName:  csi-rbd-sc<br>
 source:<br>
   http:<br>
     url: http://127.0.0.1:8081/CentOS7.4_AMD64_2.1<br>
</pre><br>
ephemeral、containerDisk：数据是无法持久化，故在存储选型上，我们采用Ceph作为后端存储，通过调用Ceph CSI插件创建PVC卷方式管理虚机磁盘设备。Ceph CSI插件实现了容器存储编排与Ceph集群交互的接口，它可以为容器应用分配 存储集群中的存储空间，同时在选择Ceph-CSI版本需要考虑到当前Kubernetes版本、及Ceph版本号。<br>
<br>当前支持的版本列表：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/ffc170c42d6ff9b284099d7a1aeaadb6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/ffc170c42d6ff9b284099d7a1aeaadb6.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Dynamically provision , de-provision Block mode RWX volume</em><br>
<br>支持RBD块RWX的模式，使用此模式主要涉及到KubeVirt 热迁移场景，虚拟机调用VirtualMachineInstanceMigration CRD资源，热迁移时会检测Volume模式，此时块设备必须RWX模式，代码如下：<br>
<br>位置：pkg/vm-handler/vm.go<br>
<pre class="prettyprint">//主要通过调用磁盘、网络相关函数，来判断当前VMI 是否适合迁移<br>
func (d *VirtualMachineController) calculateLiveMigrationCondition(vmi *v1.VirtualMachineInstance, hasHotplug bool) (*v1.VirtualMachineInstanceCondition, bool) &#123;<br>
liveMigrationCondition := v1.VirtualMachineInstanceCondition&#123;<br>
Type:   v1.VirtualMachineInstanceIsMigratable,<br>
Status: k8sv1.ConditionTrue,<br>
&#125;<br>
//调用 checkvolume 方法<br>
isBlockMigration, err := d.checkVolumesForMigration(vmi)<br>
if err != nil &#123;<br>
//如果返回错误信息则会限制迁移<br>
liveMigrationCondition.Status = k8sv1.ConditionFalse<br>
liveMigrationCondition.Message = err.Error()<br>
liveMigrationCondition.Reason = v1.VirtualMachineInstanceReasonDisksNotMigratable<br>
return &liveMigrationCondition, isBlockMigration<br>
&#125;<br>
//调用网络模式检查方法<br>
err = d.checkNetworkInterfacesForMigration(vmi)<br>
if err != nil &#123;<br>
liveMigrationCondition = v1.VirtualMachineInstanceCondition&#123;<br>
Type:    v1.VirtualMachineInstanceIsMigratable,<br>
Status:  k8sv1.ConditionFalse,<br>
Message: err.Error(),<br>
Reason:  v1.VirtualMachineInstanceReasonInterfaceNotMigratable,<br>
&#125;<br>
return &liveMigrationCondition, isBlockMigration<br>
&#125;<br>
if hasHotplug &#123;<br>
liveMigrationCondition = v1.VirtualMachineInstanceCondition&#123;<br>
Type:    v1.VirtualMachineInstanceIsMigratable,<br>
Status:  k8sv1.ConditionFalse,<br>
Message: "VMI has hotplugged disks",<br>
Reason:  v1.VirtualMachineInstanceReasonHotplugNotMigratable,<br>
&#125;<br>
return &liveMigrationCondition, isBlockMigration<br>
&#125;<br>
return &liveMigrationCondition, isBlockMigration<br>
&#125; <br>
</pre><br>
<pre class="prettyprint">//checkvolume 定义<br>
/检查所有VMI卷共享可以在源和实时迁移的目的地之间热迁移<br>
//当所有卷均已共享且VMI没有本地磁盘时，blockMigrate才返回True<br>
//某些磁盘组合使VMI不适合实时迁移， 在这种情况下，将返回相关错误<br>
func (d *VirtualMachineController) checkVolumesForMigration(vmi *v1.VirtualMachineInstance) (blockMigrate bool, err error) &#123;<br>
for _, volume := range vmi.Spec.Volumes &#123;<br>
volSrc := volume.VolumeSource<br>
if volSrc.PersistentVolumeClaim != nil || volSrc.DataVolume != nil &#123;<br>
var volName string<br>
if volSrc.PersistentVolumeClaim != nil &#123;<br>
volName = volSrc.PersistentVolumeClaim.ClaimName<br>
&#125; else &#123;<br>
volName = volSrc.DataVolume.Name<br>
&#125;<br>
//pvcutils.IsSharedPVCFromClient<br>
_, shared, err := pvcutils.IsSharedPVCFromClient(d.clientset, vmi.Namespace, volName)<br>
if errors.IsNotFound(err) &#123;<br>
return blockMigrate, fmt.Errorf("persistentvolumeclaim %v not found", volName)<br>
&#125; else if err != nil &#123;<br>
return blockMigrate, err<br>
&#125;<br>
if !shared &#123;<br>
return true, fmt.Errorf("cannot migrate VMI with non-shared PVCs")<br>
&#125;<br>
&#125; else if volSrc.HostDisk != nil &#123;<br>
shared := volSrc.HostDisk.Shared != nil && *volSrc.HostDisk.Shared<br>
if !shared &#123;<br>
return true, fmt.Errorf("cannot migrate VMI with non-shared HostDisk")<br>
&#125;<br>
&#125; else &#123;<br>
blockMigrate = true<br>
&#125;<br>
&#125;<br>
return<br>
&#125;<br>
func IsSharedPVCFromClient(client kubecli.KubevirtClient, namespace string, claimName string) (pvc *k8sv1.PersistentVolumeClaim, isShared bool, err error) &#123;<br>
pvc, err = client.CoreV1().PersistentVolumeClaims(namespace).Get(claimName, v1.GetOptions&#123;&#125;)<br>
if err == nil &#123;<br>
//IsPVCShared<br>
isShared = IsPVCShared(pvc)<br>
&#125;<br>
return<br>
&#125;<br>
//IsPVCShared Shared 判断，函数返回bool 类型，成功则返回true<br>
func IsPVCShared(pvc *k8sv1.PersistentVolumeClaim) bool &#123;<br>
//循环PVC的accessModes<br>
for _, accessMode := range pvc.Spec.AccessModes &#123;<br>
if accessMode == k8sv1.ReadWriteMany &#123;<br>
return true<br>
&#125;<br>
&#125;<br>
return false<br>
&#125; <br>
</pre><br>
Ceph CSi启动的Pod进程：<br>
<pre class="prettyprint">[root@kubevirt01 ~]# kubectl get pod<br>
NAME                                               READY   STATUS    RESTARTS   AGE<br>
csi-rbdplugin-7bprd                                3/3     Running   0          14d<br>
csi-rbdplugin-fl5c9                                3/3     Running   0          14d<br>
csi-rbdplugin-ggj9q                                3/3     Running   0          14d<br>
csi-rbdplugin-provisioner-84bb9bdd56-7qtnh         6/6     Running   0          14d<br>
csi-rbdplugin-provisioner-84bb9bdd56-sdscf         6/6     Running   0          14d<br>
csi-rbdplugin-provisioner-84bb9bdd56-xjz2r         6/6     Running   0          14d<br>
csi-rbdplugin-svfv2<br>
</pre><br>
已创建的VMI对应的PVC卷：<br>
<pre class="prettyprint">---<br>
apiVersion: v1<br>
kind: PersistentVolumeClaim<br>
metadata:<br>
name: testzhangsanlisi<br>
spec:<br>
accessModes:<br>
- ReadWriteMany<br>
volumeMode: Block<br>
resources:<br>
requests:<br>
 storage: 10Gi<br>
storageClassName: csi-rbd-sc<br>
kubectl apply -f pvc-test.yaml<br>
[root@kubevirt01 ~]# kubectl get pvc<br>
NAME                           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE<br>
testzhangsanlisi   <br>
</pre><br>
Ceph架构相关，使用三副本策略，不同交换机下及高容量SATA盘作为OSD数据载体，保证数据的可用性。<br>
<pre class="prettyprint">(ceph-mon)[root@example100 /]# ceph -s<br>
cluster:<br>
id:     d8ab2087-f55c-4b8f-913d-fc60d6fc455d<br>
health: HEALTH_OK<br>
services:<br>
mon: 3 daemons, quorum 192.168.10.100 192.168.20.100 192.168.30.100 (age 4d)<br>
mgr: ceph100(active, since 4d), standbys: ceph200， ceph300<br>
osd: 27 osds: 27 up (since 2w), 27 in (since 2w)<br>
data:<br>
pools:   1 pools, 1024 pgs<br>
objects: 55.91k objects, 218 GiB<br>
usage:   682 GiB used, 98 TiB / 98 TiB avail<br>
pgs:     1024 active+clean<br>
io:<br>
client:   2.2 KiB/s wr, 0 op/s rd, 0 op/s wr<br>
(ceph-mon)[root@example100 /]# ceph df<br>
RAW STORAGE:<br>
CLASS     SIZE       AVAIL      USED        RAW USED     %RAW USED<br>
hdd       98 TiB     98 TiB     655 GiB      682 GiB          0.68<br>
TOTAL     98 TiB     98 TiB     655 GiB      682 GiB          0.68<br>
</pre><br>
<h3>KubeVirt 网络</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/f96db902784634646a7f7d9380c3ecf9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/f96db902784634646a7f7d9380c3ecf9.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>VMI通信流程</em><br>
<br>Kubernetes是KubeVirt底座，提供了管理容器和虚拟机的混合部署的方式，存储和网络也是通过集成到Kubernetes中， VMI使用了Pod进行通信。为了实现该目标，KubeVirt的对网络做了特殊实现。虚拟机具体的网络如图所示， virt-launcher Pod网络的网卡不再挂有Pod IP，而是作为虚拟机的虚拟网卡的与外部网络通信的交接物理网卡。<br>
<br>在当前的场景我们使用经典的大二层网络模型，用户在一个地址空间下，VM使用固定IP，在OpenStack社区，虚拟网络方案成熟，OVS基本已经成为网络虚拟化的标准。所以我门选择目前灵雀云（Alauda）开源的网络方案：Kube-OVN，它是基于OVN的Kubernetes网络组件，提供了大量目前Kubernetes不具备的网络功能，并在原有基础上进行增强。通过将OpenStack领域成熟的网络功能平移到Kubernetes，来应对更加复杂的基础环境和应用合规性要求。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/0a4c85bf5e0a55043e3341da367c8a6a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/0a4c85bf5e0a55043e3341da367c8a6a.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Kube-OVN是一款基于OVS/OVN的Kubernetes网络项目</em><br>
<h4>网络VLAN underlay</h4>在网络平面，管理网和VMI虚拟机流量分开，其中使用VLAN模式的underlay网络，容器网络可以直接通过VLAN接入物理交换机<br>
<pre class="prettyprint">//Demo Yaml<br>
//IP地址段来自源与网络物理设备分配时<br>
spec:<br>
cidrBlock: 192.168.10.0/23<br>
default: true<br>
excludeIps:<br>
- 192.168.10.1<br>
gateway: 192.168.10.1<br>
gatewayNode: ""<br>
gatewayType: distributed<br>
// 需要设置成false<br>
natOutgoing: false<br>
private: false<br>
protocol: IPv4<br>
provider: ovn<br>
//需要设置成true，若为false，会在主机侧加上route，导致net不通<br>
underlayGateway: true<br>
vlan: ovn-vlan<br>
</pre><br>
 <pre class="prettyprint">[root@kubevirt01 ~]# kubectl -n kube-system get pod<br>
NAME                                   READY   STATUS    RESTARTS   AGE<br>
coredns-65dbdb44db-8bxlr               1/1     Running   33         17d<br>
kube-ovn-cni-4v4xb                     1/1     Running   0          18d<br>
kube-ovn-cni-kvgrj                     1/1     Running   0          18d<br>
kube-ovn-cni-nj2pr                     1/1     Running   0          18d<br>
kube-ovn-cni-xv476                     1/1     Running   0          18d<br>
kube-ovn-controller-7f6db69b48-6c7w8   1/1     Running   0          18d<br>
kube-ovn-controller-7f6db69b48-82kjt   1/1     Running   0          18d<br>
kube-ovn-controller-7f6db69b48-mhkfc   1/1     Running   0          18d<br>
kube-ovn-pinger-n2rn4                  1/1     Running   0          18d<br>
kube-ovn-pinger-s4hrz                  1/1     Running   0          18d<br>
kube-ovn-pinger-tccz5                  1/1     Running   0          18d<br>
kube-ovn-pinger-x2tqq                  1/1     Running   0          18d<br>
ovn-central-775c4ff46d-4nqjw           1/1     Running   1          18d<br>
ovn-central-775c4ff46d-822v2           1/1     Running   0          18d<br>
ovn-central-775c4ff46d-txkn8           1/1     Running   0          18d<br>
ovs-ovn-mbpv2                          1/1     Running   0          18d<br>
ovs-ovn-r9mvc                          1/1     Running   0          18d<br>
ovs-ovn-wkxld                          1/1     Running   0          18d<br>
ovs-ovn-z89hw  <br>
</pre><br>
<h4>虚拟机固定IP</h4>Kubernetes的资源是在运行时才分配IP的，但是笔者希望能够对虚拟机的IP进行绑定从而实现固定IP的目的。为此，我们首先正常创建虚拟机，在虚拟机运行时Kubernetes会为之分配IP，当检测到虚拟机的IP后，我们通过替换VMI的配置文件的方式将IP绑定改虚拟机中。但是在实际操作时会报出如下错误：<br>
<pre class="prettyprint">Invalid value: 0x0: must be specified for an update<br>
</pre><br>
实际上Kubernetes API Server是支持乐观锁（Optimistic concurrency control）的机制来防止并发写造成的覆盖写问题，因此在修改的body中需要加入metadata.resourceVersion，笔者的做法是首选调用 read_namespaced_virtual_machine方法获取metadata.resourceVersion，其次再修改body。具体方案可参考：<br><br>
<a href="https://www.codeleading.com/article/27252474726/" rel="nofollow" target="_blank">https://www.codeleading.com/article/27252474726/</a><br>
<h3>KubeVirt SDK</h3>KubeVirt SDK现状：当前KubeVirt提供了Python版本以及Golang版本的SDK，具体的信息参考如下：<br>
<ul><li><a href="https://github.com/kubevirt/client-python" rel="nofollow" target="_blank">https://github.com/kubevirt/client-python</a></li><li><a href="https://github.com/kubevirt/client-go" rel="nofollow" target="_blank">https://github.com/kubevirt/client-go</a></li></ul><br>
<br>笔者实际使用的是Python的SDK，所以接下来重点叙述一下Python版本的SDK的使用心得，使用时发现了一些问题，并加以解决也将在下面的内容中记录。<br>
<br>SDK实现的功能本章笔者详细介绍一下使用到的一些sdk中的功能，在初体验的过程中笔者只是用了部分功能，完整的功能可以详见GitHub。<br>
<h4>创建使用实例</h4>SDK主要使用的是kubevirt.apis.default_api中的DefaultApi对象，进行接口调用个的。DefaultApi对象需要ApiClient对象，该对象实际上是连接Kubernetes的实例。因此在使用之前，需要在底层的Kubernetes中起一个Proxy。通过创建DefaultApi对象即可调用后续的接口了，具体的创建方法如下：<br>
<pre class="prettyprint">import kubevirt<br>
<br>
<br>
def get_api_client(host):<br>
api_client = kubevirt.ApiClient(host=host, header_name="Content-Type", header_value="application/json")<br>
return api_client<br>
<br>
<br>
api_client = get_api_client(host="http://127.0.0.1:8001")<br>
api_instance = kubevirt.DefaultApi(api_client)<br>
</pre><br>
<h4>KubVirt SDK的本质</h4>实际上我们知道，KubeVirt是在Kubernetes中定义了集中CRD，那么调用KubeVirt的SDK实际上也是调用Kubernetes中CRD相关接口，通过查看Kubernetes中CRD的接口我们知道，具体的url表示为：/apis/&#123;group&#125;/&#123;version&#125;/namespaces/&#123;namespace&#125;/&#123;plural&#125;/&#123;name&#125;因此重要的是找到group以及plural参数具体是什么。通过下图可以看出group都是kubevirt.io，plural根据需要的不同可以定义不同的类型：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/bc2f8716d6bac409bf2e5e03d2c10b1c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/bc2f8716d6bac409bf2e5e03d2c10b1c.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>SDK部分功能以及注意事项</h4>笔者主要使用了以下的功能。<br>
<pre class="prettyprint">创建虚拟机（create_namespaced_virtual_machine）注意：body是json格式，官方SDK的example有误<br>
删除虚拟机（delete_namespaced_virtual_machine）<br>
展示某个namespace下的VM资源（list_namespaced_virtual_machine）<br>
展示某个namespace下的VMI资源（list_namespaced_virtual_machine_instance）<br>
展示所有namespace下的VM资源（list_virtual_machine_for_all_namespaces）<br>
展示所有namespace下的VMI资源（list_virtual_machine_instance_for_all_namespaces）<br>
获取某个namespace某个name下的VM资源（read_namespaced_virtual_machine）<br>
获取某个namespace某个name下的VMI资源（read_namespaced_virtual_machine_instance）注意：在获取VM资源时无法获取到node_name，uuid，ip的数据，获取VMI资源时无法获取到disk以及image_url的数据，笔者认为VM是虚拟机资源，VMI是虚拟机实例资源，只有在running状态下的VM才是VMI，由于Kubernetes中IP是动态分配的，因此才会出现node_name，uuid，ip数据在VM中获取不到<br>
启动虚拟机（v1alpha3_start）<br>
停止虚拟机（v1alpha3_stop）<br>
重启虚拟机（v1alpha3_restart）注意：重启虚拟机只能在虚拟机状态是running是才能调用，否则会失败<br>
修改虚拟机名称（v1alpha3_rename）<br>
替换虚拟机的配置文件（replace_namespaced_virtual_machine_instance）<br>
</pre><br>
<h4>SDK使用注意事项</h4><strong>Kubernetes版本问题</strong><br>
<br>官方给出的KubeVirt SDK中对于创建删除以及替换配置文件等部分接口，Kubernetes版本是固定的稳定版v1版本，这显然不满足于SDK的灵活使用，因此笔者在使用时对API版本进行了兼容，保证用户可以通过传参的形式正确的使用。<br>
<br><strong>修改虚拟机名称缺乏参数</strong><br>
<br>诚如标题所述，修改虚拟机名称接口官方给出的参数有误，缺乏新名称参数。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/889c3085f8985366c531ffb7fede6fc3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/889c3085f8985366c531ffb7fede6fc3.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/0444b2150b6c8e966fff57030b674cfa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/0444b2150b6c8e966fff57030b674cfa.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
笔者通过查看virtclt源码找到了缺少的参数的具体名称并添加至SDK中，具体代码如下：<br>
<pre class="prettyprint">def v1alpha3_rename_with_http_info(self, name, newName, namespace, **kwargs):<br>
"""<br>
Rename a stopped VirtualMachine object.<br>
This method makes a synchronous HTTP request by default. To make an<br>
asynchronous HTTP request, please define a `callback` function<br>
to be invoked when receiving the response.<br>
>>> def callback_function(response):<br>
>>>     pprint(response)<br>
>>><br>
>>> thread = api.v1alpha3_rename_with_http_info(name, namespace, newName, callback=callback_function)<br>
:param callback function: The callback function<br>
   for asynchronous request. (optional)<br>
:param str name: Name of the resource (required)<br>
:param str namespace: Object name and auth scope, such as for teams and projects (required)<br>
:param str newName: NewName of the resource (required)<br>
:return: str<br>
        If the method is called asynchronously,<br>
        returns the request thread.<br>
"""<br>
all_params = ['name', 'namespace', 'newName']<br>
all_params.append('callback')<br>
all_params.append('_return_http_data_only')<br>
all_params.append('_preload_content')<br>
all_params.append('_request_timeout')<br>
params = locals()<br>
for key, val in iteritems(params['kwargs']):<br>
   if key not in all_params:<br>
       raise TypeError(<br>
           "Got an unexpected keyword argument '%s'"<br>
           " to method v1alpha3_rename" % key<br>
       )<br>
   params[key] = val<br>
del params['kwargs']<br>
# verify the required parameter 'name' is set<br>
if ('name' not in params) or (params['name'] is None):<br>
   raise ValueError("Missing the required parameter `name` when calling `v1alpha3_rename`")<br>
# verify the required parameter 'namespace' is set<br>
if ('namespace' not in params) or (params['namespace'] is None):<br>
   raise ValueError("Missing the required parameter `namespace` when calling `v1alpha3_rename`")<br>
collection_formats = &#123;&#125;<br>
path_params = &#123;&#125;<br>
# if 'name' in params:<br>
#     path_params['name'] = params['name']<br>
# if 'namespace' in params:<br>
#     path_params['namespace'] = params['namespace']<br>
query_params = []<br>
header_params = &#123;&#125;<br>
form_params = []<br>
local_var_files = &#123;&#125;<br>
body_params = &#123;"newName": params["newName"]&#125;<br>
# Authentication setting<br>
auth_settings = []<br>
api_route = "/apis/subresources.kubevirt.io/v1alpha3/namespaces/&#123;namespace&#125;/virtualmachines/&#123;name&#125;/rename".format(namespace=params["namespace"], name=params["name"])<br>
return self.api_client.call_api(api_route, 'PUT',<br>
                               path_params,<br>
                               query_params,<br>
                               header_params,<br>
                               body=body_params,<br>
                               post_params=form_params,<br>
                               files=local_var_files,<br>
                               response_type='str',<br>
                               auth_settings=auth_settings,<br>
                               callback=params.get('callback'),<br>
                               _return_http_data_only=params.get('_return_http_data_only'),<br>
                               _preload_content=params.get('_preload_content', True),<br>
                               _request_timeout=params.get('_request_timeout'),<br>
                               collection_formats=collection_formats)<br>
</pre><br>
<h3>Ultron平台创建基于KubeVirt 的虚拟机</h3>奥创平台是公司内的私有云管理平台（类似Horizon），可以通过其管理OpenStack VM，本次我们同时纳入到对KubeVirt 虚拟机的支持，创建方式和OpenStack方式一样。最后用户体验和功能特性也和OpenStack一致，用户本身也是不关注底层实现，性能特性方面后续文章会有对比。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/db9199ea844d47e7f17d8af8856fafd9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/db9199ea844d47e7f17d8af8856fafd9.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>KubeVirt作为一个兼容方案，当前在CNCF中孵化的也挺好，好像也要开始自己的KubeVirt Summit，主要是实际的解决了一些痛点，但目前看，KubeVirt还是适合在私有云，肯定满足不了公有云，因为Kubernetes在IaaS方面有先天劣势，所以KubeVirt应该是给大家在私有云领域落地虚拟化除了用OpenStack以外多了一种选择方案。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/RGYWwzi9Q9fBiGOqf19jIg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/RGYWwzi9Q9fBiGOqf19jIg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            