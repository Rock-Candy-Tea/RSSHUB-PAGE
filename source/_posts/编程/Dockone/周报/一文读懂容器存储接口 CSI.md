
---
title: '一文读懂容器存储接口 CSI'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/e4f9702599c4417184c152865bdfaa97.png'
author: Dockone
comments: false
date: 2021-04-12 12:10:35
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/e4f9702599c4417184c152865bdfaa97.png'
---

<div>   
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/e4f9702599c4417184c152865bdfaa97.png" alt="头图.png" referrerpolicy="no-referrer"><br>
<br>作者 | 惠志<br>
来源 | <a href="https://mp.weixin.qq.com/s/A9xWKMmrxPyOEiCs_sicYQ">阿里巴巴云原生公众号</a><br>
<br><blockquote><br><strong>导读：</strong>在<a href="https://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247490043&idx=1&sn=c09ad4a9bc790f4b742abd8ca1301ffb&scene=21#wechat_redirect">《一文读懂 K8s 持久化存储流程》</a>一文我们重点介绍了 K8s 内部的存储流程，以及 PV、PVC、StorageClass、Kubelet 等之间的调用关系。接下来本文将将重点放在 CSI（Container Storage Interface）容器存储接口上，探究什么是 CSI 及其内部工作原理。</blockquote><h1>背景</h1>K8s 原生支持一些存储类型的 PV，如 iSCSI、NFS、CephFS 等等（详见<a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#types-of-persistent-volumes">链接</a>），这些 in-tree 类型的存储代码放在 Kubernetes 代码仓库中。这里带来的问题是 K8s 代码与三方存储厂商的代码<strong>强耦合</strong>：<br>
<ul><li>更改 in-tree 类型的存储代码，用户必须更新 K8s 组件，成本较高</li><li>in-tree 存储代码中的 bug 会引发 K8s 组件不稳定</li><li>K8s 社区需要负责维护及测试 in-tree 类型的存储功能</li><li>in-tree 存储插件享有与 K8s 核心组件同等的特权，存在安全隐患</li><li>三方存储开发者必须遵循 K8s 社区的规则开发 in-tree 类型存储代码</li></ul><br>
<br>CSI 容器存储接口标准的出现解决了上述问题，将三方存储代码与 K8s 代码解耦，使得三方存储厂商研发人员只需实现 CSI 接口（无需关注容器平台是 K8s 还是 Swarm 等）。<br>
<br><h1>CSI 核心流程介绍</h1>在详细介绍 CSI 组件及其接口之前，我们先对 K8s 中 CSI 存储流程进行一个介绍。《一文读懂 K8s 持久化存储流程》一文介绍了 K8s 中的 Pod 在挂载存储卷时需经历三个的阶段：Provision/Delete（创盘/删盘）、Attach/Detach（挂接/摘除）和 Mount/Unmount（挂载/卸载），下面以图文的方式讲解 K8s 在这三个阶段使用 CSI 的流程。<br>
<br><h2>1. Provisioning Volumes</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/116bec4216f3b7817c27e4b29adb170e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/116bec4216f3b7817c27e4b29adb170e.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>1.<strong>集群管理员</strong>创建 StorageClass 资源，该 StorageClass 中包含 CSI 插件名称（provisioner:pangu.csi.alibabacloud.com）以及存储类必须的参数（parameters: type=cloud_ssd）。sc.yaml 文件如下：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/c4f55094de55489e54cf8841d11cde73.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/c4f55094de55489e54cf8841d11cde73.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>2.<strong>用户</strong>创建 PersistentVolumeClaim 资源，PVC 指定存储大小及 StorageClass（如上）。pvc.yaml 文件如下：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/c3ec1cc153d46ad29d48f4e3cc11ccae.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/c3ec1cc153d46ad29d48f4e3cc11ccae.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>3.<strong>卷控制器（PersistentVolumeController）</strong>观察到集群中新创建的 PVC 没有与之匹配的 PV，且其使用的存储类型为 out-of-tree，于是为 PVC 打 annotation：volume.beta.kubernetes.io/storage-provisioner=[out-of-tree CSI 插件名称]（本例中即为 provisioner:pangu.csi.alibabacloud.com）。<br>
<br>4.<strong>External Provisioner 组件</strong>观察到 PVC 的 annotation 中包含 "volume.beta.kubernetes.io/storage-provisioner" 且其 value 是自己，于是开始创盘流程。<br>
<ul><li>获取相关 StorageClass 资源并从中获取参数（本例中 parameters 为  type=cloud_ssd），用于后面 CSI 函数调用。</li><li>通过 unix domain socket 调用<strong>外部 CSI 插件</strong>的<strong>CreateVolume 函数</strong>。</li></ul><br>
<br>5.<strong>外部 CSI 插件</strong>返回成功后表示盘创建完成，此时<strong>External Provisioner 组件</strong>会在集群创建一个 PersistentVolume 资源。<br>
<br>6.<strong>卷控制器</strong>会将 PV 与 PVC 进行绑定。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/1852521a16f49a4f71cda16bc66eba5a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/1852521a16f49a4f71cda16bc66eba5a.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>2. Attaching Volumes</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/dafe17ceaaf1b5ab6bb21b14c33b7724.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/dafe17ceaaf1b5ab6bb21b14c33b7724.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>1.<strong>AD 控制器（AttachDetachController）</strong>观察到使用 CSI 类型 PV 的 Pod 被调度到某一节点，此时<strong>AD 控制器</strong>会调用<strong>内部 in-tree CSI 插件（csiAttacher）</strong>的 Attach 函数。<br>
<br>2.<strong>内部 in-tree CSI 插件（csiAttacher）</strong>会创建一个 VolumeAttachment 对象到集群中。<br>
<br>3.<strong>External Attacher </strong>观察到该 VolumeAttachment 对象，并调用<strong>外部 CSI插件</strong>的<strong>ControllerPublish 函数</strong>以将卷挂接到对应节点上。<strong>外部 CSI 插件</strong>挂载成功后，<strong>External Attacher</strong>会更新相关 VolumeAttachment 对象的 .Status.Attached 为 true。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/60a0e2a42ac5164490e9a0f8acb0aef6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/60a0e2a42ac5164490e9a0f8acb0aef6.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>4.<strong>AD 控制器内部 in-tree CSI 插件（csiAttacher）</strong>观察到 VolumeAttachment 对象的 .Status.Attached 设置为 true，于是更新<strong>AD 控制器</strong>内部状态（ActualStateOfWorld），该状态会显示在 Node 资源的 .Status.VolumesAttached 上。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/9af1c6f738018ff185c3a42866d7767f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/9af1c6f738018ff185c3a42866d7767f.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>3. Mounting Volumes</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/e1d471302d8c707dc55f1f1b37ca0ec2.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/e1d471302d8c707dc55f1f1b37ca0ec2.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>1.<strong>Volume Manager（Kubelet 组件）</strong>观察到有新的使用 CSI 类型 PV 的 Pod 调度到本节点上，于是调用<strong>内部 in-tree CSI 插件（csiAttacher）</strong>的 WaitForAttach 函数。<br>
<br>2.<strong>内部 in-tree CSI 插件（csiAttacher）</strong>等待集群中 VolumeAttachment 对象状态 .Status.Attached 变为 true。<br>
<br>3.<strong>in-tree CSI 插件（csiAttacher）</strong>调用 MountDevice 函数，该函数内部通过 unix domain socket 调用<strong>外部 CSI 插件</strong>的<strong>NodeStageVolume 函数</strong>；之后<strong>插件（csiAttacher）</strong>调用<strong>内部 in-tree CSI 插件（csiMountMgr）</strong>的 SetUp 函数，该函数内部会通过 unix domain socket 调用<strong>外部 CSI 插件</strong>的<strong>NodePublishVolume 函数</strong>。<br>
<br><h2>4. Unmounting Volumes</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/a682506b8bdec0b8957434d9d46a8151.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/a682506b8bdec0b8957434d9d46a8151.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>1.<strong>用户</strong>删除相关 Pod。<br>
<br>2.<strong>Volume Manager（Kubelet 组件）</strong>观察到包含 CSI 存储卷的 Pod 被删除，于是调用<strong>内部 in-tree CSI 插件（csiMountMgr）</strong>的 TearDown 函数，该函数内部会通过 unix domain socket 调用<strong>外部 CSI 插件</strong>的 <strong>NodeUnpublishVolume 函数</strong>。<br>
<br>3.<strong>Volume Manager（Kubelet 组件）</strong>调用<strong>内部 in-tree CSI 插件（csiAttacher）</strong>的 UnmountDevice 函数，该函数内部会通过 unix domain socket 调用<strong>外部 CSI 插件</strong>的 <strong>NodeUnpublishVolume 函数</strong>。<br>
<br><h2>5. Detaching Volumes</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/8d59e88122679ab42bb755b8765eb67b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/8d59e88122679ab42bb755b8765eb67b.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>1.<strong>AD 控制器</strong>观察到包含 CSI 存储卷的 Pod 被删除，此时该控制器会调用<strong>内部 in-tree CSI 插件（csiAttacher）</strong>的 Detach 函数。<br>
<br>2.<strong>csiAttacher</strong>会删除集群中相关 VolumeAttachment 对象（但由于存在 finalizer，va 对象不会立即删除）。<br>
<br>3.<strong>External Attacher</strong>观察到集群中 VolumeAttachment 对象的 DeletionTimestamp 非空，于是调用<strong>外部 CSI 插件</strong>的<strong>ControllerUnpublish 函数</strong>以将卷从对应节点上摘除。<strong>外部 CSI 插件</strong>摘除成功后，<strong>External Attacher</strong>会移除相关 VolumeAttachment 对象的 finalizer 字段，此时 VolumeAttachment 对象被彻底删除。<br>
<br>4.<strong>AD 控制器</strong>中<strong>内部 in-tree CSI 插件（csiAttacher）</strong>观察到 VolumeAttachment 对象已删除，于是更新<strong>AD 控制器</strong>中的内部状态；同时<strong>AD 控制器</strong>更新 Node 资源，此时 Node 资源的 .Status.VolumesAttached 上已没有相关挂接信息。<br>
<br><h2>6. Deleting Volumes</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/ce4a43c41c6e0a1fed7682994baa3fc3.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/ce4a43c41c6e0a1fed7682994baa3fc3.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>1.<strong>用户</strong>删除相关 PVC。<br>
<br>2.<strong>External Provisioner 组件</strong>观察到 PVC 删除事件，根据 PVC 的回收策略（Reclaim）执行不同操作：<br>
<ul><li>Delete：调用<strong>外部 CSI 插件</strong>的<strong>DeleteVolume 函数</strong>以删除卷；一旦卷成功删除，<strong>Provisioner</strong>会删除集群中对应 PV 对象。</li><li>Retain：<strong>Provisioner</strong>不执行卷删除操作。</li></ul><br>
<br><h1>CSI Sidecar 组件介绍</h1>为使 K8s 适配 CSI 标准，社区将与 K8s 相关的存储流程逻辑放在了 CSI Sidecar 组件中。<br>
<br><h2>1. Node Driver Registrar</h2><h3>1）功能</h3><strong>Node-Driver-Registrar 组件</strong>会将<strong>外部 CSI 插件</strong>注册到<strong>Kubelet</strong>，从而使<strong>Kubelet</strong>通过特定的 Unix Domain Socket 来调用<strong>外部 CSI 插件函数</strong>（Kubelet 会调用外部 CSI 插件的 NodeGetInfo、NodeStageVolume、NodePublishVolume、NodeGetVolumeStats 等函数）。<br>
<br><h3><strong>2）原理</strong></h3><strong>Node-Driver-Registrar 组件</strong>通过Kubelet 外部插件注册机制实现注册，注册成功后：<br>
<ul><li><br><strong>Kubelet</strong>为本节点 Node 资源打 annotation：<strong>Kubelet</strong>调用<strong>外部 CSI 插件</strong>的<strong>NodeGetInfo 函数</strong>，其返回值 [nodeID]、[driverName] 将作为值用于 "csi.volume.kubernetes.io/nodeid" 键。</li><li><br><strong>Kubelet</strong>更新 Node Label：将<strong>NodeGetInfo 函数</strong>返回的 [AccessibleTopology] 值用于节点的 Label。</li><li><br><strong>Kubelet</strong>更新 Node Status：将<strong>NodeGetInfo 函数</strong>返回的 maxAttachLimit（节点最大可挂载卷数量）更新到 Node 资源的 Status.Allocatable：attachable-volumes-csi-[driverName]=[maxAttachLimit]。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/b6a313269bf62862a64f6cffa2f9acdf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/b6a313269bf62862a64f6cffa2f9acdf.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><strong>Kubelet</strong>更新 CSINode 资源（没有则创建）：将 [driverName]、[nodeID]、[maxAttachLimit]、[AccessibleTopology] 更新到 Spec 中（拓扑仅保留 Key 值）。</li></ul><br>
<br><h2>2. External Provisioner</h2><h3>1）功能</h3>创建/删除实际的存储卷，以及代表存储卷的 PV 资源。<br>
<br><h3><strong>2）原理</strong></h3><strong>External-Provisioner</strong>在启动时需指定参数 -- provisioner，该参数指定 Provisioner 名称，与 StorageClass 中的 provisioner 字段对应。<br>
<br><strong>External-Provisioner</strong>启动后会 watch 集群中的 PVC 和 PV 资源。<br>
<br>对于集群中的 PVC 资源：<br>
<ul><li><br>判断 PVC 是否需要动态创建存储卷，标准如下：<br>
<ul><li>PVC 的 annotation 中是否包含 "volume.beta.kubernetes.io/storage-provisioner" 键（由卷控制器创建），并且其值是否与 Provisioner 名称相等。</li><li>PVC 对应 StorageClass 的 VolumeBindingMode 字段若为 WaitForFirstConsumer，则 PVC 的 annotation 中必须包含 "volume.kubernetes.io/selected-node" 键（详见调度器如何处理 WaitForFirstConsumer），且其值不为空；若为 Immediate 则表示需要 Provisioner 立即提供动态存储卷。</li></ul></li><li><br>通过特定的 Unix Domain Socket 调用<strong>外部 CSI 插件</strong>的 <strong>CreateVolume 函数</strong>。</li><li><br>创建 PV 资源，PV 名称为 [Provisioner 指定的 PV 前缀] - [PVC uuid]。</li></ul><br>
<br>对于集群中的 PV 资源：<br>
<ul><li><br>判断 PV 是否需要删除，标准如下：<br>
<ul><li>判断其 .Status.Phase 是否为 Release。</li><li>判断其 .Spec.PersistentVolumeReclaimPolicy 是否为 Delete。</li><li>判断其是否包含 annotation（pv.kubernetes.io/provisioned-by），且其值是否为自己。</li></ul></li><li><br>通过特定的 Unix Domain Socket 调用<strong>外部 CSI 插件</strong>的 <strong>DeleteVolume 接口</strong>。</li><li><br>删除集群中的 PV 资源。<br>
<h2>3. External Attacher</h2><h3><strong>1）功能</strong></h3>挂接/摘除存储卷。</li></ul><br>
<br><h3><strong>2）原理</strong></h3><strong>External-Attacher </strong>内部会时刻 watch 集群中的 VolumeAttachment 资源和 PersistentVolume 资源。<br>
<br>对于 VolumeAttachment 资源：<br>
<ul><li><br>从 VolumeAttachment 资源中获得 PV 的所有信息，如 volume ID、node ID、挂载 Secret 等。</li><li><br>判断 VolumeAttachment 的 DeletionTimestamp 字段是否为空来判断其为卷挂接或卷摘除：若为卷挂接则通过特定的 Unix Domain Socket 调用<strong>外部 CSI 插件</strong>的<strong>ControllerPublishVolume 接口</strong>；若为卷摘除则通过特定的 Unix Domain Socket 调用<strong>外部 CSI 插件</strong>的<strong>ControllerUnpublishVolume 接口</strong>。</li></ul><br>
<br>对于 PersistentVolume 资源：<br>
<ul><li><br>在挂接时为相关 PV 打上 Finalizer：external-attacher/[driver 名称]。</li><li><br>当 PV 处于删除状态时（DeletionTimestamp 非空），删除 Finalizer：external-attacher/[driver 名称]。</li></ul><br>
<br><h2>4. External Resizer</h2><h3><strong>1）功能</strong></h3>扩容存储卷。<br>
<br><h3><strong>2）原理</strong></h3><strong>External-Resizer</strong>内部会 watch 集群中的 PersistentVolumeClaim 资源。<br>
<br>对于 PersistentVolumeClaim 资源：<br>
<ul><li><br>判断 PersistentVolumeClaim 资源是否需要扩容：PVC 状态需要是 Bound 且 .Status.Capacity 与 .Spec.Resources.Requests 不等。</li><li><br>更新 PVC 的 .Status.Conditions，表明此时处于 Resizing 状态。</li><li><br>通过特定的 Unix Domain Socket 调用<strong>外部 CSI 插件</strong>的 <strong>ControllerExpandVolume 接口</strong>。</li><li><br>更新 PV 的 .Spec.Capacity。</li><li><br>若 CSI 支持文件系统在线扩容，ControllerExpandVolume 接口返回值中 NodeExpansionRequired 字段为 true，<strong>External-Resizer</strong>更新 PVC 的 .Status.Conditions 为 FileSystemResizePending 状态；若不支持则扩容成功，<strong>External-Resizer</strong>更新 PVC 的 .Status.Conditions 为空，且更新 PVC 的 .Status.Capacity。</li></ul><br>
<br><strong>Volume Manager（Kubelet 组件）</strong>观察到存储卷需在线扩容，于是通过特定的 Unix Domain Socket 调用<strong>外部 CSI 插件</strong>的<strong>NodeExpandVolume 接口</strong>实现文件系统扩容。<br>
<br><h2>5. livenessprobe</h2><h3><strong>1）功能</strong></h3>检查 CSI 插件是否正常。<br>
<br><h3><strong>2）原理</strong></h3>通过对外暴露一个 / healthz HTTP 端口以服务 kubelet 的探针探测器，内部是通过特定的 Unix Domain Socket 调用<strong>外部 CSI 插件</strong>的 <strong>Probe 接口</strong>。<br>
<br><h1>CSI 接口介绍</h1>三方存储厂商需实现 CSI 插件的三大接口：<strong>IdentityServer、ControllerServer、NodeServer</strong>。<br>
<br><h2>1. IdentityServer</h2>IdentityServer 主要用于认证 CSI 插件的身份信息。<br>
<br><code class="prettyprint">// IdentityServer is the server API for Identity service.<br>
type IdentityServer interface &#123;<br>
    // 获取CSI插件的信息，比如名称、版本号<br>
    GetPluginInfo(context.Context, *GetPluginInfoRequest) (*GetPluginInfoResponse, error)<br>
    // 获取CSI插件提供的能力，比如是否提供ControllerService能力<br>
    GetPluginCapabilities(context.Context, *GetPluginCapabilitiesRequest) (*GetPluginCapabilitiesResponse, error)<br>
    // 获取CSI插件健康状况<br>
    Probe(context.Context, *ProbeRequest) (*ProbeResponse, error)<br>
&#125;</code><br>
<h2>2. ControllerServer</h2>ControllerServer 主要负责存储卷及快照的创建/删除以及挂接/摘除操作。<br>
<br><code class="prettyprint">// ControllerServer is the server API for Controller service.<br>
type ControllerServer interface &#123;<br>
    // 创建存储卷<br>
    CreateVolume(context.Context, *CreateVolumeRequest) (*CreateVolumeResponse, error)<br>
    // 删除存储卷<br>
    DeleteVolume(context.Context, *DeleteVolumeRequest) (*DeleteVolumeResponse, error)<br>
    // 挂接存储卷到特定节点<br>
    ControllerPublishVolume(context.Context, *ControllerPublishVolumeRequest) (*ControllerPublishVolumeResponse, error)<br>
    // 从特定节点摘除存储卷<br>
    ControllerUnpublishVolume(context.Context, *ControllerUnpublishVolumeRequest) (*ControllerUnpublishVolumeResponse, error)<br>
    // 验证存储卷能力是否满足要求，比如是否支持跨节点多读多写<br>
    ValidateVolumeCapabilities(context.Context, *ValidateVolumeCapabilitiesRequest) (*ValidateVolumeCapabilitiesResponse, error)<br>
    // 列举全部存储卷信息<br>
    ListVolumes(context.Context, *ListVolumesRequest) (*ListVolumesResponse, error)<br>
    // 获取存储资源池可用空间大小<br>
    GetCapacity(context.Context, *GetCapacityRequest) (*GetCapacityResponse, error)<br>
    // 获取ControllerServer支持功能点，比如是否支持快照能力<br>
    ControllerGetCapabilities(context.Context, *ControllerGetCapabilitiesRequest) (*ControllerGetCapabilitiesResponse, error)<br>
    // 创建快照<br>
    CreateSnapshot(context.Context, *CreateSnapshotRequest) (*CreateSnapshotResponse, error)<br>
    // 删除快照<br>
    DeleteSnapshot(context.Context, *DeleteSnapshotRequest) (*DeleteSnapshotResponse, error)<br>
    // 获取所有快照信息<br>
    ListSnapshots(context.Context, *ListSnapshotsRequest) (*ListSnapshotsResponse, error)<br>
    // 扩容存储卷<br>
    ControllerExpandVolume(context.Context, *ControllerExpandVolumeRequest) (*ControllerExpandVolumeResponse, error)<br>
&#125;</code><br>
<br><h2>3. NodeServer</h2>NodeServer 主要负责存储卷挂载/卸载操作。<br>
<br><code class="prettyprint">// NodeServer is the server API for Node service.<br>
type NodeServer interface &#123;<br>
    // 将存储卷格式化并挂载至临时全局目录<br>
    NodeStageVolume(context.Context, *NodeStageVolumeRequest) (*NodeStageVolumeResponse, error)<br>
    // 将存储卷从临时全局目录卸载<br>
    NodeUnstageVolume(context.Context, *NodeUnstageVolumeRequest) (*NodeUnstageVolumeResponse, error)<br>
    // 将存储卷从临时目录bind-mount到目标目录<br>
    NodePublishVolume(context.Context, *NodePublishVolumeRequest) (*NodePublishVolumeResponse, error)<br>
    // 将存储卷从目标目录卸载<br>
    NodeUnpublishVolume(context.Context, *NodeUnpublishVolumeRequest) (*NodeUnpublishVolumeResponse, error)<br>
    // 获取存储卷的容量信息<br>
    NodeGetVolumeStats(context.Context, *NodeGetVolumeStatsRequest) (*NodeGetVolumeStatsResponse, error)<br>
    // 存储卷扩容<br>
    NodeExpandVolume(context.Context, *NodeExpandVolumeRequest) (*NodeExpandVolumeResponse, error)<br>
    // 获取NodeServer支持功能点，比如是否支持获取存储卷容量信息<br>
    NodeGetCapabilities(context.Context, *NodeGetCapabilitiesRequest) (*NodeGetCapabilitiesResponse, error)<br>
    // 获取CSI节点信息，比如最大支持卷个数<br>
    NodeGetInfo(context.Context, *NodeGetInfoRequest) (*NodeGetInfoResponse, error)<br>
&#125;</code><br>
<br><h1>K8s CSI API 对象</h1>K8s 为支持 CSI 标准，包含如下 API 对象：<br>
<ul><li>CSINode</li><li>CSIDriver</li><li>VolumeAttachment</li></ul><br>
<br><h2>1. CSINode</h2><code class="prettyprint">apiVersion: storage.k8s.io/v1beta1<br>
kind: CSINode<br>
metadata:<br>
  name: node-10.212.101.210<br>
spec:<br>
  drivers:<br>
  - name: yodaplugin.csi.alibabacloud.com<br>
    nodeID: node-10.212.101.210<br>
    topologyKeys:<br>
    - kubernetes.io/hostname<br>
  - name: pangu.csi.alibabacloud.com<br>
    nodeID: a5441fd9013042ee8104a674e4a9666a<br>
    topologyKeys:<br>
    - topology.pangu.csi.alibabacloud.com/zone</code><br>
<br>作用：<br>
<ol><li><br>判断<strong>外部 CSI 插件</strong>是否注册成功。在 Node Driver Registrar 组件向 Kubelet 注册完毕后，Kubelet 会创建该资源，故不需要显式创建 CSINode 资源。</li><li><br>将 Kubernetes 中 Node 资源名称与三方存储系统中节点名称（nodeID）一一对应。此处<strong>Kubelet</strong>会调用<strong>外部 CSI 插件</strong>NodeServer 的 <strong>GetNodeInfo 函数</strong>获取 nodeID。</li><li><br>显示卷拓扑信息。CSINode 中 topologyKeys 用来表示存储节点的拓扑信息，卷拓扑信息会使得<strong>Scheduler</strong>在 Pod 调度时选择合适的存储节点。</li></ol><br>
<br><h2>2. CSIDriver</h2><code class="prettyprint">apiVersion: storage.k8s.io/v1beta1<br>
kind: CSIDriver<br>
metadata:<br>
  name: pangu.csi.alibabacloud.com<br>
spec:<br>
    # 插件是否支持卷挂接（VolumeAttach）<br>
  attachRequired: true<br>
  # Mount阶段是否CSI插件需要Pod信息<br>
  podInfoOnMount: true<br>
  # 指定CSI支持的卷模式<br>
  volumeLifecycleModes:<br>
  - Persistent</code><br>
<br>作用：<br>
<ol><li><br>简化<strong>外部 CSI 插件</strong>的发现。由集群管理员创建，通过 kubectl get csidriver 即可得知环境上有哪些 CSI 插件。</li><li><br>自定 义Kubernetes 行为，如一些外部 CSI 插件不需要执行卷挂接（VolumeAttach）操作，则可以设置 .spec.attachRequired 为 false。</li></ol><br>
<br><h2>3. VolumeAttachment</h2><code class="prettyprint">apiVersion: storage.k8s.io/v1<br>
kind: VolumeAttachment<br>
metadata:<br>
  annotations:<br>
    csi.alpha.kubernetes.io/node-id: 21481ae252a2457f9abcb86a3d02ba05<br>
  finalizers:<br>
  - external-attacher/pangu-csi-alibabacloud-com<br>
  name: csi-0996e5e9459e1ccc1b3a7aba07df4ef7301c8e283d99eabc1b69626b119ce750<br>
spec:<br>
  attacher: pangu.csi.alibabacloud.com<br>
  nodeName: node-10.212.101.241<br>
  source:<br>
    persistentVolumeName: pangu-39aa24e7-8877-11eb-b02f-021234350de1<br>
status:<br>
  attached: true</code><br>
<br>作用：VolumeAttachment 记录了存储卷的挂接/摘除信息以及节点信息。<br>
<br><h1>支持特性</h1><h2>1. 拓扑支持</h2>在 StorageClass 中有 AllowedTopologies 字段：<br>
<br><code class="prettyprint">apiVersion: storage.k8s.io/v1<br>
kind: StorageClass<br>
metadata:<br>
  name: csi-pangu<br>
provisioner: pangu.csi.alibabacloud.com<br>
parameters:<br>
  type: cloud_ssd<br>
volumeBindingMode: Immediate<br>
allowedTopologies:<br>
- matchLabelExpressions:<br>
  - key: topology.pangu.csi.alibabacloud.com/zone<br>
    values:<br>
    - zone-1<br>
    - zone-2</code><br>
<br><strong>外部 CSI 插件</strong>部署后会为每个节点打标，打标内容<strong>NodeGetInfo 函数</strong>返回的 [AccessibleTopology] 值（详见 Node Driver Registrar 部分）。<br>
<br><strong>External Provisioner</strong>在调用 CSI 插件的 CreateVolume 接口之前，会在请求参数设置 AccessibilityRequirements：<br>
<ul><li><br>对于 WaitForFirstConsumer<br>
<ul><li>当 PVC 的 anno 中包含 "volume.kubernetes.io/selected-node" 且不为空，则先获取对应节点 CSINode 的 TopologyKeys，然后根据该 TopologyKeys 键从 Node 资源的 Label 获取 Values 值，最后拿该 Values 值与 StorageClass 的 AllowedTopologies 比对，判断其是否包含于其中；若不包含则报错。</li></ul></li><li><br>对于 Immediately<br>
<ul><li>将 StorageClass 的 AllowedTopologies 的值填进来，若 StorageClass 没有设置 AllowedTopologies 则将所有包含 TopologyKeys 键的节点 Value 添进来。</li></ul></li></ul><br>
<br><h3><strong>Scheduler 如何处理使用存储卷调度</strong></h3>> 基于社区 1.18 版本调度器<br>
<br>调度器的调度过程主要有如下三步：<br>
<ul><li><strong>预选（Filter）</strong>：筛选满足 Pod 调度要求的节点列表。</li><li><strong>优选（Score）</strong>：通过内部的优选算法为节点打分，获得最高分数的节点即为选中的节点。</li><li><strong>绑定（Bind）</strong>：调度器将调度结果通知给 kube-apiserver，更新 Pod 的 .spec.nodeName 字段。</li></ul><br>
<br>调度器预选阶段：处理 Pod 的 PVC/PV 绑定关系以及动态供应 PV（Dynamic Provisioning），同时使调度器调度时考虑 Pod 所使用 PV 的节点亲和性。详细调度过程如下：<br>
<ol><li><br>Pod 不包含 PVC 直接跳过。</li><li><br>FindPodVolumes<br>
<ul><li><br> 获取 Pod 的 boundClaims、claimsToBind 以及 unboundClaimsImmediate。<br>
<ul><li>boundClaims：已 Bound 的 PVC</li><li>claimsToBind：PVC 对应 StorageClass 的 VolumeBindingMode 为 VolumeBindingWaitForFirstConsumer</li><li>unboundClaimsImmediate：PVC 对应 StorageClass 的 VolumeBindingMode 为 VolumeBindingImmediate</li></ul></li><li><br> 若 len(unboundClaimsImmediate) 不为空，表示这种 PVC 需要立即绑定 PV（即存 PVC 创建后，立刻动态创建 PV 并将其绑定到 PVC，该过程不走调度），若 PVC 处于 unbound 阶段则报错。</li><li><br> 若 len(boundClaims) 不为空，则检查 PVC 对应 PV 的节点亲和性与当前节点的 Label 是否冲突，若冲突则报错（可检查 Immediate 类型的 PV 拓扑）。</li><li><br> 若 len(claimsToBind) 不为空<br>
<ul><li>先检查环境中已有的 PV 能否与该 PVC 匹配（findMatchingVolumes），将能够匹配 PVC 的 PV 记录在调度器的 cache 中。</li><li>未匹配到 PV 的 PVC 走动态调度流程，动态调度主要通过 StorageClass 的 AllowedTopologies 字段判断当前调度节点是否满足拓扑要求（针对 WaitForFirstConsumer 类型的 PVC）。</li></ul></li></ul></li></ol><br>
<br>调度器优选阶段不讨论。<br>
<br>调度器 Assume 阶段<br>
<br><blockquote><br>调度器会先 Assume PV/PVC，再 Assume Pod。<br>
  <ol><li><br>将当前待调度的 Pod 进行深拷贝。</li><li><br>AssumePodVolumes（针对 WaitForFirstConsumer 类型的 PVC）<br>
  <ul><li>更改调度器 cache 中已经 Match 的 PV 信息：设置 annotation：pv.kubernetes.io/bound-by-controller="yes"。</li><li>更改调度器 cache 中未匹配到 PV 的 PVC，设置 annotation：volume.kubernetes.io/selected-node=【所选节点】。</li></ul></li><li><br>Assume Pod 完毕<br>
  <ul><li>更改调度器 cache 中 Pod 的 .Spec.NodeName 为【所选节点】。</li></ul></li></ol></blockquote>调度器 Bind 阶段<br>
<br>BindPodVolumes：<br>
<ul><li><br>调用 Kubernetes 的 API 更新集群中 PV/PVC 资源，使其与调度器 Cache 中的 PV/PVC 一致。</li><li><br>检查 PV/PVC 状态：<br>
<ul><li>检查所有 PVC 是否已处于 Bound 状态。</li><li>检查所有 PV 的 NodeAffinity 是否与节点 Label 冲突。</li></ul></li><li><br>调度器执行 Bind 操作：调用 Kubernetes 的 API 更新 Pod 的 .Spec.NodeName 字段。</li></ul><br>
<br><h2>2. 存储卷扩容</h2>存储卷扩容部分在 External Resizer 部分已提到，故不再赘述。用户只需要编辑 PVC 的 .Spec.Resources.Requests.Storage 字段即可，注意只可扩容不可缩容。<br>
<br>若 PV 扩容失败，此时 PVC 无法重新编辑 spec 字段的 storage 为原来的值（只可扩容不可缩容）。参考 K8s 官网提供的 PVC 还原方法：<br>
_<a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#recovering-from-failure-when-expanding-volumes_" rel="nofollow" target="_blank">https://kubernetes.io/docs/con ... umes_</a><br>
<br><h2>3. 单节点卷数量限制</h2>卷数量限制在 Node Driver Registrar 部分已提到，故不再赘述。<br>
<br><h2>4. 存储卷监控</h2>存储商需实现 CSI 插件的 NodeGetVolumeStats 接口，Kubelet 会调用该函数，并反映在其 metrics上：<br>
<ul><li>kubelet_volume_stats_capacity_bytes：存储卷容量</li><li>kubelet_volume_stats_used_bytes：存储卷已使用容量</li><li>kubelet_volume_stats_available_bytes：存储卷可使用容量</li><li>kubelet_volume_stats_inodes：存储卷 inode 总量</li><li>kubelet_volume_stats_inodes_used：存储卷 inode 使用量</li><li>kubelet_volume_stats_inodes_free：存储卷 inode 剩余量</li></ul><br>
<br><h2>5. Secret</h2>CSI 存储卷支持传入 Secret 来处理不同流程中所需要的私密数据，目前 StorageClass 支持如下 Parameter：<br>
<ul><li>csi.storage.k8s.io/provisioner-secret-name</li><li>csi.storage.k8s.io/provisioner-secret-namespace</li><li>csi.storage.k8s.io/controller-publish-secret-name</li><li>csi.storage.k8s.io/controller-publish-secret-namespace</li><li>csi.storage.k8s.io/node-stage-secret-name</li><li>csi.storage.k8s.io/node-stage-secret-namespace</li><li>csi.storage.k8s.io/node-publish-secret-name</li><li>csi.storage.k8s.io/node-publish-secret-namespace</li><li>csi.storage.k8s.io/controller-expand-secret-name</li><li>csi.storage.k8s.io/controller-expand-secret-namespace</li></ul><br>
<br>Secret 会包含在对应 CSI 接口的参数中，如对于 CreateVolume 接口而言则包含在 CreateVolumeRequest.Secrets 中。<br>
<br><h2>6. 块设备</h2><code class="prettyprint">apiVersion: apps/v1<br>
kind: StatefulSet<br>
metadata:<br>
  name: nginx-example<br>
spec:<br>
  selector:<br>
    matchLabels:<br>
      app: nginx<br>
  serviceName: &quot;nginx&quot;<br>
  volumeClaimTemplates:<br>
  - metadata:<br>
      name: html<br>
    spec:<br>
      accessModes:<br>
        - ReadWriteOnce<br>
      volumeMode: Block<br>
      storageClassName: csi-pangu<br>
      resources:<br>
        requests:<br>
          storage: 40Gi<br>
  template:<br>
    metadata:<br>
      labels:<br>
        app: nginx<br>
    spec:<br>
      containers:<br>
      - name: nginx<br>
        image: nginx<br>
        volumeDevices:<br>
        - devicePath: &quot;/dev/vdb&quot;<br>
          name: html</code><br>
<br>三方存储厂商需实现 NodePublishVolume 接口。Kubernetes 提供了针对块设备的工具包（"k8s.io/kubernetes/pkg/util/mount"），在 NodePublishVolume 阶段可调用该工具的 EnsureBlock 和 MountBlock 函数。<br>
<br><h2>7. 卷快照/卷克隆能力</h2>鉴于本文篇幅，此处不做过多原理性介绍。读者感兴趣见官方介绍：<a href="https://kubernetes.io/zh/docs/concepts/storage/persistent-volumes/#%E5%AF%B9%E5%8D%B7%E5%BF%AB%E7%85%A7%E5%8F%8A%E4%BB%8E%E5%8D%B7%E5%BF%AB%E7%85%A7%E4%B8%AD%E6%81%A2%E5%A4%8D%E5%8D%B7%E7%9A%84%E6%94%AF%E6%8C%81">卷快照</a>、<a href="https://kubernetes.io/zh/docs/concepts/storage/persistent-volumes/#volume-cloning">卷克隆</a>。<br>
<br><h1>总结</h1>本文首先对 CSI 核心流程进行了大体介绍，并结合 CSI Sidecar 组件、CSI 接口、API 对象对 CSI 标准进行了深度解析。在 K8s 上，使用任何一种 CSI 存储卷都离不开上面的流程，环境上的容器存储问题也一定是其中某个环节出现了问题。本文对其流程进行梳理，以便于广大程序猿（媛）排查环境问题。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            