
---
title: '源码解析：Kubernetes 创建 Pod 时，背后发生了什么（二）'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=410'
author: Dockone
comments: false
date: 2021-06-07 05:22:11
thumbnail: 'https://picsum.photos/400/300?random=410'
---

<div>   
<br><h3>kubelet</h3>每个 Kubernetes Node 上都会运行一个名为 kubelet 的 agent，它负责：<br>
<ul><li><br>Pod 生命周期管理。<br>
<br>这意味着，它负责将 “Pod” 的逻辑抽象（etcd 中的元数据）转换成具体的容器（container）。</li><li><br>挂载目录</li><li>创建容器日志</li><li>垃圾回收等等</li></ul><br>
<br><h4>Pod sync（状态同步）</h4><strong>kubelet 也可以认为是一个 controller</strong>，它：<br>
<ol><li>通过 ListWatch 接口，从 kube-apiserver <strong>获取属于本节点的 Pod 列表</strong>（根据 <code class="prettyprint">spec.nodeName</code> <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/kubelet/config/apiserver.go#L32">过滤</a>），</li><li>然后<strong>与自己缓存的 Pod 列表对比</strong>，如果有 Pod 创建、删除、更新等操作，就开始同步状态。</li></ol><br>
<br>下面具体看一下同步过程。<br>
<br><strong>同步过程</strong><br>
<pre class="prettyprint">// pkg/kubelet/kubelet.go<br>
<br>
// syncPod is the transaction script for the sync of a single pod.<br>
func (kl *Kubelet) syncPod(o syncPodOptions) error &#123;<br>
pod := o.pod<br>
<br>
if updateType == SyncPodKill &#123; // kill pod 操作<br>
    kl.killPod(pod, nil, podStatus, PodTerminationGracePeriodSecondsOverride)<br>
    return nil<br>
&#125;<br>
<br>
firstSeenTime := pod.Annotations["kubernetes.io/config.seen"] // 测量 latency，从 apiserver 第一次看到 pod 算起<br>
<br>
if updateType == SyncPodCreate &#123; // create pod 操作<br>
    if !firstSeenTime.IsZero() &#123; // Record pod worker start latency if being created<br>
        metrics.PodWorkerStartDuration.Observe(metrics.SinceInSeconds(firstSeenTime))<br>
    &#125;<br>
&#125;<br>
<br>
// Generate final API pod status with pod and status manager status<br>
apiPodStatus := kl.generateAPIPodStatus(pod, podStatus)<br>
<br>
podStatus.IPs = []string&#123;&#125;<br>
if len(podStatus.IPs) == 0 && len(apiPodStatus.PodIP) > 0 &#123;<br>
    podStatus.IPs = []string&#123;apiPodStatus.PodIP&#125;<br>
&#125;<br>
<br>
runnable := kl.canRunPod(pod)<br>
if !runnable.Admit &#123; // Pod is not runnable; update the Pod and Container statuses to why.<br>
    apiPodStatus.Reason = runnable.Reason<br>
    ...<br>
&#125;<br>
<br>
kl.statusManager.SetPodStatus(pod, apiPodStatus)<br>
<br>
// Kill pod if it should not be running<br>
if !runnable.Admit || pod.DeletionTimestamp != nil || apiPodStatus.Phase == v1.PodFailed &#123;<br>
    return kl.killPod(pod, nil, podStatus, nil)<br>
&#125;<br>
<br>
// 如果 network plugin not ready，并且 pod 网络不是 host network 类型，返回相应错误<br>
if err := kl.runtimeState.networkErrors(); err != nil && !IsHostNetworkPod(pod) &#123;<br>
    return fmt.Errorf("%s: %v", NetworkNotReadyErrorMsg, err)<br>
&#125;<br>
<br>
// Create Cgroups for the pod and apply resource parameters if cgroups-per-qos flag is enabled.<br>
pcm := kl.containerManager.NewPodContainerManager()<br>
<br>
if kubetypes.IsStaticPod(pod) &#123; // Create Mirror Pod for Static Pod if it doesn't already exist<br>
    ...<br>
&#125;<br>
<br>
kl.makePodDataDirs(pod)                     // Make data directories for the pod<br>
kl.volumeManager.WaitForAttachAndMount(pod) // Wait for volumes to attach/mount<br>
pullSecrets := kl.getPullSecretsForPod(pod) // Fetch the pull secrets for the pod<br>
<br>
// Call the container runtime's SyncPod callback<br>
result := kl.containerRuntime.SyncPod(pod, podStatus, pullSecrets, kl.backOff)<br>
kl.reasonCache.Update(pod.UID, result)<br>
&#125; <br>
</pre><br>
<ol><li>如果是 Pod 创建事件，会记录一些 pod latency 相关的 metrics；</li><li><br>然后调用 <code class="prettyprint">generateAPIPodStatus()</code> <strong>生成一个 v1.PodStatus 对象</strong>，代表 Pod 当前阶段（Phase）的状态。<br>
<br>Pod 的 Phase 是对其生命周期中不同阶段的高层抽象，非常复杂，后面会介绍。</li><li><br>PodStatus 生成之后，将发送给 Pod status manager，后者的任务是<strong>异步地通过 apiserver 更新 etcd 记录</strong>。</li><li><br>接下来会<strong>运行一系列 admission handlers</strong>，确保 pod 有正确的安全权限（security permissions）。<br>
<br>其中包括 enforcing  <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/kubelet/kubelet.go#L883-L884">AppArmor profiles and <code class="prettyprint">NO_NEW_PRIVS</code></a>。在这个阶段<strong>被 deny 的 Pods 将无限期处于 Pending 状态</strong>。</li><li><br>如果指定了 <code class="prettyprint">cgroups-per-qos</code>，kubelet 将为这个 Pod 创建 cgroups。可以实现更好的 QoS。</li><li><br><strong>为容器创建一些目录</strong>。包括<br>
<ul><li>Pod 目录 （一般是  <code class="prettyprint">/var/run/kubelet/pods/&lt;podID></code>）</li><li>Volume 目录 (<code class="prettyprint">&lt;podDir>/volumes</code>)</li><li>Plugin 目录 (<code class="prettyprint">&lt;podDir>/plugins</code>).</li></ul></li><li><br>volume manager 将 <a href="https://github.com/kubernetes/kubernetes/blob/2723e06a251a4ec3ef241397217e73fa782b0b98/pkg/kubelet/volumemanager/volume_manager.go#L330">等待</a>  <code class="prettyprint">Spec.Volumes</code> 中定义的 volumes attach 完成。取决于 volume 类型，Pod 可能会等待很长时间（例如 cloud 或 NFS volumes）。</li><li>从 apiserver 获取  <code class="prettyprint">Spec.ImagePullSecrets</code>  中指定的  <strong>secrets，注入容器</strong>。</li><li><strong>容器运行时（runtime）创建容器</strong>（后面详细描述）。</li></ol><br>
<br><strong>Pod 状态</strong><br>
<br>前面提到，<code class="prettyprint">generateAPIPodStatus()</code> <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/kubelet/kubelet_pods.go#L1287">生成一个 v1.PodStatus</a> 对象，代表 Pod 当前阶段（Phase）的状态。<br>
<br>Pod 的 Phase 是对其生命周期中不同阶段的高层抽象，包括：<br>
<ul><li><code class="prettyprint">Pending</code></li><li><code class="prettyprint">Running</code></li><li><code class="prettyprint">Succeeded</code></li><li><code class="prettyprint">Failed</code></li><li><code class="prettyprint">Unknown</code></li></ul><br>
<br>生成这个状态的过程非常复杂，一些细节如下：<br>
<ol><li><br>首先，顺序执行一系列 <code class="prettyprint">PodSyncHandlers</code>。每个 handler <strong>判断这个 Pod 是否还应该留在这个 Node 上</strong>。 如果其中任何一个判断结果是否，那 Pod 的 phase  <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/kubelet/kubelet_pods.go#L1293-L1297">将变为</a>  <code class="prettyprint">PodFailed</code>  并最终会被<strong>从这个 node 驱逐</strong>。<br>
<br>一个例子是 Pod 的 <code class="prettyprint">activeDeadlineSeconds</code>（Jobs 中会用到）超时之后，就会被驱逐。</li><li><br>接下来决定 Pod Phase 的将是其 init 和 real containers。由于此时容器还未启动，因此 将<strong>处于</strong>  <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/kubelet/kubelet_pods.go#L1244">waiting</a>  <strong>状态</strong>。<strong>有 waiting 状态 container 的 Pod，将处于 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/kubelet/kubelet_pods.go#L1258-L1261"><code class="prettyprint">Pending</code></a>  Phase</strong>。</li><li>由于此时容器运行时还未创建我们的容器 ，因此它将把 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/kubelet/status/generate.go#L70-L81"><code class="prettyprint">PodReady</code>  字段置为 False</a>。</li></ol><br>
<br><h4>CRI 及创建 pause 容器</h4>至此，大部分准备工作都已完成，接下来即将创建容器了。<strong>创建容器是通过 Container Runtime （例如 <code class="prettyprint">docker</code> 或 <code class="prettyprint">rkt</code>）完成的</strong>。<br>
<br>为实现可扩展，kubelet 从 v1.5.0 开始，<strong>使用 CRI（Container Runtime Interface）与具体的容器运行时交互</strong>。 简单来说，CRI 提供了 kubelet 和具体 runtime implementation 之间的抽象接口， 用 <a href="https://github.com/google/protobuf">protocol buffers</a> 和 gRPC 通信。<br>
<br><strong>CRI SyncPod</strong><br>
<pre class="prettyprint">// pkg/kubelet/kuberuntime/kuberuntime_manager.go<br>
<br>
// SyncPod syncs the running pod into the desired pod by executing following steps:<br>
//  1. Compute sandbox and container changes.<br>
//  2. Kill pod sandbox if necessary.<br>
//  3. Kill any containers that should not be running.<br>
//  4. Create sandbox if necessary.<br>
//  5. Create ephemeral containers.<br>
//  6. Create init containers.<br>
//  7. Create normal containers.<br>
//<br>
func (m *kubeGenericRuntimeManager) SyncPod(pod *v1.Pod, podStatus *kubecontainer.PodStatus,<br>
pullSecrets []v1.Secret, backOff *flowcontrol.Backoff) (result kubecontainer.PodSyncResult) &#123;<br>
<br>
// Step 1: Compute sandbox and container changes.<br>
podContainerChanges := m.computePodActions(pod, podStatus)<br>
if podContainerChanges.CreateSandbox &#123;<br>
    ref := ref.GetReference(legacyscheme.Scheme, pod)<br>
    if podContainerChanges.SandboxID != "" &#123;<br>
        m.recorder.Eventf("Pod sandbox changed, it will be killed and re-created.")<br>
    &#125; else &#123;<br>
        InfoS("SyncPod received new pod, will create a sandbox for it")<br>
    &#125;<br>
&#125;<br>
<br>
// Step 2: Kill the pod if the sandbox has changed.<br>
if podContainerChanges.KillPod &#123;<br>
    if podContainerChanges.CreateSandbox &#123;<br>
        InfoS("Stopping PodSandbox for pod, will start new one")<br>
    &#125; else &#123;<br>
        InfoS("Stopping PodSandbox for pod, because all other containers are dead")<br>
    &#125;<br>
<br>
    killResult := m.killPodWithSyncResult(pod, ConvertPodStatusToRunningPod(m.runtimeName, podStatus), nil)<br>
    result.AddPodSyncResult(killResult)<br>
<br>
    if podContainerChanges.CreateSandbox &#123;<br>
        m.purgeInitContainers(pod, podStatus)<br>
    &#125;<br>
&#125; else &#123;<br>
    // Step 3: kill any running containers in this pod which are not to keep.<br>
    for containerID, containerInfo := range podContainerChanges.ContainersToKill &#123;<br>
        killContainerResult := NewSyncResult(kubecontainer.KillContainer, containerInfo.name)<br>
        result.AddSyncResult(killContainerResult)<br>
        m.killContainer(pod, containerID, containerInfo)<br>
    &#125;<br>
&#125;<br>
<br>
// Keep terminated init containers fairly aggressively controlled<br>
// This is an optimization because container removals are typically handled by container GC.<br>
m.pruneInitContainersBeforeStart(pod, podStatus)<br>
<br>
// Step 4: Create a sandbox for the pod if necessary.<br>
podSandboxID := podContainerChanges.SandboxID<br>
if podContainerChanges.CreateSandbox &#123;<br>
    createSandboxResult := kubecontainer.NewSyncResult(kubecontainer.CreatePodSandbox, format.Pod(pod))<br>
    result.AddSyncResult(createSandboxResult)<br>
    podSandboxID, msg = m.createPodSandbox(pod, podContainerChanges.Attempt)<br>
    podSandboxStatus := m.runtimeService.PodSandboxStatus(podSandboxID)<br>
&#125;<br>
<br>
// the start containers routines depend on pod ip(as in primary pod ip)<br>
// instead of trying to figure out if we have 0 < len(podIPs) everytime, we short circuit it here<br>
podIP := ""<br>
if len(podIPs) != 0 &#123;<br>
    podIP = podIPs[0]<br>
&#125;<br>
<br>
// Get podSandboxConfig for containers to start.<br>
configPodSandboxResult := kubecontainer.NewSyncResult(ConfigPodSandbox, podSandboxID)<br>
result.AddSyncResult(configPodSandboxResult)<br>
podSandboxConfig := m.generatePodSandboxConfig(pod, podContainerChanges.Attempt)<br>
<br>
// Helper containing boilerplate common to starting all types of containers.<br>
// typeName is a label used to describe this type of container in log messages,<br>
// currently: "container", "init container" or "ephemeral container"<br>
start := func(typeName string, spec *startSpec) error &#123;<br>
    startContainerResult := kubecontainer.NewSyncResult(kubecontainer.StartContainer, spec.container.Name)<br>
    result.AddSyncResult(startContainerResult)<br>
<br>
    isInBackOff, msg := m.doBackOff(pod, spec.container, podStatus, backOff)<br>
    if isInBackOff &#123;<br>
        startContainerResult.Fail(err, msg)<br>
        return err<br>
    &#125;<br>
<br>
    m.startContainer(podSandboxID, podSandboxConfig, spec, pod, podStatus, pullSecrets, podIP, podIPs)<br>
    return nil<br>
&#125;<br>
<br>
// Step 5: start ephemeral containers<br>
// These are started "prior" to init containers to allow running ephemeral containers even when there<br>
// are errors starting an init container. In practice init containers will start first since ephemeral<br>
// containers cannot be specified on pod creation.<br>
for _, idx := range podContainerChanges.EphemeralContainersToStart &#123;<br>
    start("ephemeral container", ephemeralContainerStartSpec(&pod.Spec.EphemeralContainers[idx]))<br>
&#125;<br>
<br>
// Step 6: start the init container.<br>
if container := podContainerChanges.NextInitContainerToStart; container != nil &#123;<br>
    start("init container", containerStartSpec(container))<br>
&#125;<br>
<br>
// Step 7: start containers in podContainerChanges.ContainersToStart.<br>
for _, idx := range podContainerChanges.ContainersToStart &#123;<br>
    start("container", containerStartSpec(&pod.Spec.Containers[idx]))<br>
&#125;<br>
&#125; <br>
</pre><br>
<strong>CRI create sandbox</strong><br>
<br>kubelet <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/kubelet/kuberuntime/kuberuntime_sandbox.go#L51">发起 <code class="prettyprint">RunPodSandbox</code></a> RPC 调用。<br>
<br><strong>“Sandbox” 是一个 CRI 术语，它表示一组容器，在 Kubernetes 里就是一个 Pod</strong>。 这个词是有意用作比较宽泛的描述，这样对其他运行时的描述也是适用的（例如，在基于 hypervisor 的运行时中，Sandbox 可能是一个虚拟机）。<br>
<pre class="prettyprint">// pkg/kubelet/kuberuntime/kuberuntime_sandbox.go<br>
<br>
// createPodSandbox creates a pod sandbox and returns (podSandBoxID, message, error).<br>
func (m *kubeGenericRuntimeManager) createPodSandbox(pod *v1.Pod, attempt uint32) (string, string, error) &#123;<br>
podSandboxConfig := m.generatePodSandboxConfig(pod, attempt)<br>
<br>
// 创建 pod log 目录<br>
m.osInterface.MkdirAll(podSandboxConfig.LogDirectory, 0755)<br>
<br>
runtimeHandler := ""<br>
if m.runtimeClassManager != nil &#123;<br>
    runtimeHandler = m.runtimeClassManager.LookupRuntimeHandler(pod.Spec.RuntimeClassName)<br>
    if runtimeHandler != "" &#123;<br>
        InfoS("Running pod with runtime handler", runtimeHandler)<br>
    &#125;<br>
&#125;<br>
<br>
podSandBoxID := m.runtimeService.RunPodSandbox(podSandboxConfig, runtimeHandler)<br>
return podSandBoxID, "", nil<br>
&#125; <br>
</pre><br>
<pre class="prettyprint">// pkg/kubelet/cri/remote/remote_runtime.go<br>
<br>
// RunPodSandbox creates and starts a pod-level sandbox.<br>
func (r *remoteRuntimeService) RunPodSandbox(config *PodSandboxConfig, runtimeHandler string) (string, error) &#123;<br>
<br>
InfoS("[RemoteRuntimeService] RunPodSandbox", "config", config, "runtimeHandler", runtimeHandler)<br>
<br>
resp := r.runtimeClient.RunPodSandbox(ctx, &runtimeapi.RunPodSandboxRequest&#123;<br>
    Config:         config,<br>
    RuntimeHandler: runtimeHandler,<br>
&#125;)<br>
<br>
InfoS("[RemoteRuntimeService] RunPodSandbox Response", "podSandboxID", resp.PodSandboxId)<br>
return resp.PodSandboxId, nil<br>
&#125; <br>
</pre><br>
<strong>Create sandbox：docker 相关代码</strong><br>
<br>前面是 CRI 通用代码，如果我们的容器 runtime 是 docker，那接下来就会调用到 Docker 相关代码。<br>
<br>在这种 runtime 中，<strong>创建一个 sandbox 会转换成创建一个 “pause” 容器的操作</strong>。 Pause container 作为一个 pod 内其他所有容器的父角色，hold 了很多 pod-level 的资源， 具体说就是 Linux namespace，例如 IPC NS、Net NS、IPD NS。<br>
<br>“pause” container 提供了一种持有这些 ns、让所有子容器共享它们 的方式。 例如，共享 netns 的好处之一是，pod 内不同容器之间可以通过 localhost 方式访问彼此。 pause 容器的第二个用处是<strong>回收（reaping）dead processes</strong>。 更多信息，可参考  <a href="https://www.ianlewis.org/en/almighty-pause-container">这篇博客</a>。<br>
<br>Pause 容器创建之后，会被 checkpoint 到磁盘，然后启动。<br>
<pre class="prettyprint">// pkg/kubelet/dockershim/docker_sandbox.go<br>
<br>
// 对于 docker runtime，PodSandbox 实现为一个 holding 网络命名空间（netns）的容器<br>
func (ds *dockerService) RunPodSandbox(ctx context.Context, r *RunPodSandboxRequest) (*RunPodSandboxResponse) &#123;<br>
<br>
// Step 1: Pull the image for the sandbox.<br>
ensureSandboxImageExists(ds.client, image)<br>
<br>
// Step 2: Create the sandbox container.<br>
createConfig := ds.makeSandboxDockerConfig(config, image)<br>
createResp := ds.client.CreateContainer(*createConfig)<br>
resp := &runtimeapi.RunPodSandboxResponse&#123;PodSandboxId: createResp.ID&#125;<br>
<br>
ds.setNetworkReady(createResp.ID, false) // 容器 network 状态初始化为 false<br>
<br>
// Step 3: Create Sandbox Checkpoint.<br>
CreateCheckpoint(createResp.ID, constructPodSandboxCheckpoint(config))<br>
<br>
// Step 4: Start the sandbox container。 如果失败，kubelet 会 GC 掉 sandbox<br>
ds.client.StartContainer(createResp.ID)<br>
<br>
rewriteResolvFile()<br>
<br>
// 如果是 hostNetwork 类型，到这里就可以返回了，无需下面的 CNI 流程<br>
if GetNetwork() == NamespaceMode_NODE &#123;<br>
    return resp, nil<br>
&#125;<br>
<br>
// Step 5: Setup networking for the sandbox with CNI<br>
// 包括分配 IP、设置 sandbox 内的路由、创建虚拟网卡等。<br>
cID := kubecontainer.BuildContainerID(runtimeName, createResp.ID)<br>
ds.network.SetUpPod(Namespace, Name, cID, Annotations, networkOptions)<br>
<br>
return resp, nil<br>
&#125; <br>
</pre><br>
最后调用的  <code class="prettyprint">SetUpPod()</code>  为容器创建网络，它有会<strong>调用到 plugin manager 的同名方法</strong>：<br>
<pre class="prettyprint">// pkg/kubelet/dockershim/network/plugins.go<br>
<br>
func (pm *PluginManager) SetUpPod(podNamespace, podName, id ContainerID, annotations, options) error &#123;<br>
const operation = "set_up_pod"<br>
fullPodName := kubecontainer.BuildPodFullName(podName, podNamespace)<br>
<br>
// 调用 CNI 插件为容器设置网络<br>
pm.plugin.SetUpPod(podNamespace, podName, id, annotations, options)<br>
&#125; <br>
</pre><br>
<blockquote><br>Cgroup 也很重要，是 Linux 掌管资源分配的方式，Docker 利用它实现资源隔离。 更多信息，参考 <a href="https://jvns.ca/blog/2016/10/10/what-even-is-a-container/">What even is a Container?</a></blockquote><h4>CNI 前半部分：CNI plugin manager 处理</h4>现在我们的 Pod 已经有了一个占坑用的 pause 容器，它占住了 Pod 需要用到的所有 namespace。 接下来需要做的就是：<strong>调用底层的具体网络方案</strong>（Bridge/Flannel/Calico/Cilium 等等）提供的 CNI 插件，<strong>创建并打通容器的网络</strong>。<br>
<br>CNI 是 Container Network Interface 的缩写，工作机制与 Container Runtime Interface 类似。简单来说，CNI 是一个抽象接口，不同的网络提供商只要实现了 CNI 中的几个方法，就能接入 Kubernetes，为容器创建网络。kubelet 与CNI 插件之间通过 JSON 数据交互（配置文件放在  <code class="prettyprint">/etc/cni/net.d</code>），通过 stdin 将配置数据传递给 CNI binary（located in  <code class="prettyprint">/opt/cni/bin</code>）。<br>
<br>CNI 插件有自己的配置，例如，内置的 bridge 插件可能配置如下：<br>
<pre class="prettyprint">&#123;<br>
"cniVersion": "0.3.1",<br>
"name": "bridge",<br>
"type": "bridge",<br>
"bridge": "cnio0",<br>
"isGateway": true,<br>
"ipMasq": true,<br>
"ipam": &#123;<br>
    "type": "host-local",<br>
    "ranges": [<br>
      [&#123;"subnet": "$&#123;POD_CIDR&#125;"&#125;]<br>
    ],<br>
    "routes": [&#123;"dst": "0.0.0.0/0"&#125;]<br>
&#125;<br>
&#125; <br>
</pre><br>
还会通过 <code class="prettyprint">CNI_ARGS</code> 环境变量传递 pod metadata，例如 name 和 ns。<br>
<br><strong>调用栈概览</strong><br>
<br>下面的调用栈是 CNI 前半部分：<strong>CNI plugin manager 调用到具体的 CNI 插件</strong>（可执行文件），执行 shell 命令为容器创建网络：<br>
<pre class="prettyprint">SetUpPod                                                  // pkg/kubelet/dockershim/network/cni/cni.go<br>
|-ns = plugin.host.GetNetNS(id)<br>
|-plugin.addToNetwork(name, id, ns)                      // -> pkg/kubelet/dockershim/network/cni/cni.go<br>
|-plugin.buildCNIRuntimeConf<br>
|-cniNet.AddNetworkList(netConf)                      // -> github.com/containernetworking/cni/libcni/api.go<br>
   |-for net := range list.Plugins<br>
   |   result = c.addNetwork<br>
   |              |-pluginPath = FindInPath(c.Path)<br>
   |              |-ValidateContainerID(ContainerID)<br>
   |              |-ValidateNetworkName(name)<br>
   |              |-ValidateInterfaceName(IfName)<br>
   |              |-invoke.ExecPluginWithResult(pluginPath, c.args("ADD", rt))<br>
   |                        |-shell("/opt/cni/bin/xx <args>")<br>
   |<br>
   |-c.cacheAdd(result, list.Bytes, list.Name, rt) <br>
</pre><br>
最后一层调用 <code class="prettyprint">ExecPlugin()</code>：<br>
<pre class="prettyprint">// vendor/github.com/containernetworking/cni/pkg/invoke/raw_exec.go<br>
<br>
func (e *RawExec) ExecPlugin(ctx, pluginPath, stdinData []byte, environ []string) ([]byte, error) &#123;<br>
c := exec.CommandContext(ctx, pluginPath)<br>
c.Env = environ<br>
c.Stdin = bytes.NewBuffer(stdinData)<br>
c.Stdout = stdout<br>
c.Stderr = stderr<br>
<br>
for i := 0; i <= 5; i++ &#123; // Retry the command on "text file busy" errors<br>
    err := c.Run()<br>
    if err == nil &#123; // Command succeeded<br>
        break<br>
    &#125;<br>
<br>
    if strings.Contains(err.Error(), "text file busy") &#123;<br>
        time.Sleep(time.Second)<br>
        continue<br>
    &#125;<br>
<br>
    // All other errors except than the busy text file<br>
    return nil, e.pluginErr(err, stdout.Bytes(), stderr.Bytes())<br>
&#125;<br>
<br>
return stdout.Bytes(), nil<br>
&#125; <br>
</pre><br>
可以看到，经过上面的几层调用，最终是通过 shell 命令执行了宿主机上的 CNI 插件， 例如 <code class="prettyprint">/opt/cni/bin/cilium-cni</code>，并通过 stdin 传递了一些 JSON 参数。<br>
<h4>CNI 后半部分：CNI plugin 实现</h4>下面看 CNI 处理的后半部分：CNI 插件为容器创建网络，也就是可执行文件  <code class="prettyprint">/opt/cni/bin/xxx</code>  的实现。<br>
<br>CNI 相关的代码维护在一个<strong>单独的项目</strong> <a href="https://github.com/containernetworking/cni">github.com/containernetworking/cni</a>。 每个 CNI 插件只需要实现其中的几个方法，然后<strong>编译成独立的可执行文件</strong>，放在 <code class="prettyprint">/etc/cni/bin</code> 下面即可。 下面是一些具体的插件。<br>
<pre class="prettyprint">$ ls /opt/cni/bin/<br>
bridge  cilium-cni  cnitool  dhcp  host-local  ipvlan  loopback  macvlan  noop<br>
</pre><br>
<strong>调用栈概览</strong><br>
<br>CNI 插件（可执行文件）执行时会调用到 <code class="prettyprint">PluginMain()</code>，从这往后的调用栈（<strong>注意源文件都是 <code class="prettyprint">github.com/containernetworking/cni</code> 项目中的路径</strong>）：<br>
<pre class="prettyprint">PluginMain                                                     // pkg/skel/skel.go<br>
|-PluginMainWithError                                         // pkg/skel/skel.go<br>
|-pluginMain                                                // pkg/skel/skel.go<br>
  |-switch cmd &#123;<br>
      case "ADD":<br>
        checkVersionAndCall(cmdArgs, cmdAdd)               // pkg/skel/skel.go<br>
          |-configVersion = Decode(cmdArgs.StdinData)<br>
          |-Check(configVersion, pluginVersionInfo)<br>
          |-toCall(cmdArgs) // toCall == cmdAdd<br>
             |-cmdAdd(cmdArgs)<br>
               |-specific CNI plugin implementations<br>
<br>
      case "DEL":<br>
        checkVersionAndCall(cmdArgs, cmdDel)<br>
      case "VERSION":<br>
        versionInfo.Encode(t.Stdout)<br>
      default:<br>
        return createTypedError("unknown CNI_COMMAND: %v", cmd)<br>
    &#125; <br>
</pre><br>
可见<strong>对于 kubelet 传过来的 "ADD" 命令，最终会调用到 CNI 插件的 cmdAdd() 方法</strong>  —— 该方法默认是空的，需要由每种 CNI 插件自己实现。 同理，删除 Pod 时对应的是 <code class="prettyprint">&quot;DEL&quot;</code> 操作，调用到的 <code class="prettyprint">cmdDel()</code> 方法也是要由具体 CNI 插件实现的。<br>
<br><strong>CNI 插件实现举例：Bridge</strong><br>
<br><a href="https://github.com/containernetworking/plugins">github.com/containernetworking/plugins</a> 项目中包含了很多种 CNI plugin 的实现，例如 IPVLAN、Bridge、MACVLAN、VLAN 等等。<br>
<br><code class="prettyprint">bridge</code> CNI plugin 的实现见：<a href="https://github.com/containernetworking/plugins/blob/v0.9.1/plugins/main/bridge/bridge.go">plugins/main/bridge/bridge.go</a>。<br>
<br>执行逻辑如下：<br>
<ol><li>在默认 netns 创建一个 Linux bridge，这台宿主机上的所有容器都将连接到这个 bridge。</li><li>创建一个 veth pair，将容器和 bridge 连起来。</li><li><br>分配一个 IP 地址，配置到 pause 容器，设置路由。<br>
<br>IP 从配套的网络服务 IPAM（IP Address Management）中分配的。最场景的 IPAM plugin 是  <code class="prettyprint">host-local</code>，它从预先设置的一个网段里分配一个 IP，并将状态信息写到宿主机的本地文件系统，因此重启不会丢失。  <code class="prettyprint">host-local</code>  IPAM 的实现见  <a href="https://github.com/containernetworking/plugins/tree/v0.9.1/plugins/ipam/host-local">plugins/ipam/host-local</a>。</li><li><br>修改  <code class="prettyprint">resolv.conf</code>，为容器配置 DNS。这里的 DNS 信息是从传给 CNI plugin 的参数中解析的。</li></ol><br>
<br>以上过程完成之后，容器和宿主机（以及同宿主机的其他容器）之间的网络就通了， CNI 插件会将结果以 JSON 返回给 kubelet。<br>
<br><strong>CNI 插件实现举例：Noop</strong><br>
<br>再来看另一种<strong>比较有趣的 CNI 插件</strong>：<code class="prettyprint">noop</code>。这个插件是 CNI 项目自带的，代码见：<a href="https://github.com/containernetworking/cni/blob/v0.8.1/plugins/test/noop/main.go#L184">plugins/test/noop/main.go</a>。<br>
<pre class="prettyprint">func cmdAdd(args *skel.CmdArgs) error &#123;<br>
return debugBehavior(args, "ADD")<br>
&#125;<br>
<br>
func cmdDel(args *skel.CmdArgs) error &#123;<br>
return debugBehavior(args, "DEL")<br>
&#125; <br>
</pre><br>
从名字以及以上代码可以看出，这个 CNI 插件（几乎）什么事情都不做。用途：<br>
<ol><li><strong>测试或调试</strong>：它可以打印 debug 信息。</li><li>给<strong>只支持 hostNetwork 的节点</strong>使用。</li></ol><br>
<br>每个 Node 上必须有一个配置正确的 CNI 插件，kubelet 自检才能通过，否则 Node 会处于 NotReady 状态。<br>
<br>某些情况下，我们不想让一些 Node（例如 master node）承担正常的、创建带 IP Pod 的工作， 只要它能创建 hostNetwork 类型的 Pod 就行了（这样就无需给这些 Node 分配 PodCIDR， 也不需要在 Node 上启动 IPAM 服务）。<br>
<br>这种情况下，就可以用 noop 插件。参考配置：<br>
<pre class="prettyprint">$ cat /etc/cni/net.d/98-noop.conf<br>
 &#123;<br>
     "cniVersion": "0.3.1",<br>
     "type": "noop"<br>
 &#125; <br>
</pre><br>
<strong>CNI 插件实现举例：Cilium</strong><br>
<br>这个就很复杂了，做的事情非常多，可参考：<a href="http://arthurchiao.art/blog/cilium-code-cni-create-network/">Cilium Code Walk Through: CNI Create Network</a>。<br>
<h4>为容器配置跨节点通信网络（inter-host networking）</h4>这项工作<strong>不在 Kubernetes 及 CNI 插件的职责范围内</strong>，是由具体网络方案在节点上的 agent 完成的，例如 Flannel 网络的 Flanneld，Cilium 网络的 cilium-agent。<br>
<br>简单来说，跨节点通信有两种方式：<br>
<ol><li>隧道（tunnel or overlay）</li><li>直接路由</li></ol><br>
<br>这里赞不展开，可参考：<a href="http://arthurchiao.art/blog/trip-stepping-into-cloud-native-networking-era-zh/">迈入 Cilium+BGP 的云原生网络时代</a>。<br>
<h4>创建  <code class="prettyprint">init</code>  容器及业务容器</h4>至此，网络部分都配置好了。接下来就开始<strong>启动真正的业务容器</strong>。<br>
<br>Sandbox 容器初始化完成后，kubelet 就开始创建其他容器。首先会启动 <code class="prettyprint">PodSpec</code> 中指定的所有 init 容器，<a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/kubelet/kuberuntime/kuberuntime_manager.go#L690">代码</a> 然后才启动主容器（main containers）。<br>
<br><strong>调用栈概览</strong><br>
<pre class="prettyprint">startContainer<br>
|-m.runtimeService.CreateContainer                      // pkg/kubelet/cri/remote/remote_runtime.go<br>
|  |-r.runtimeClient.CreateContainer                    // -> pkg/kubelet/dockershim/docker_container.go<br>
|       |-new(CreateContainerResponse)                  // staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go<br>
|       |-Invoke("/runtime.v1.RuntimeService/CreateContainer")<br>
|<br>
|  CreateContainer // pkg/kubelet/dockershim/docker_container.go<br>
|      |-ds.client.CreateContainer                      // -> pkg/kubelet/dockershim/libdocker/instrumented_client.go<br>
|             |-d.client.ContainerCreate                // -> vendor/github.com/docker/docker/client/container_create.go<br>
|                |-cli.post("/containers/create")<br>
|                |-json.NewDecoder().Decode(&resp)<br>
|<br>
|-m.runtimeService.StartContainer(containerID)          // -> pkg/kubelet/cri/remote/remote_runtime.go<br>
|-r.runtimeClient.StartContainer<br>
     |-new(CreateContainerResponse)                  // staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go<br>
     |-Invoke("/runtime.v1.RuntimeService/StartContainer")<br>
</pre><br>
<strong>具体过程</strong><br>
<pre class="prettyprint">// pkg/kubelet/kuberuntime/kuberuntime_container.go<br>
<br>
func (m *kubeGenericRuntimeManager) startContainer(podSandboxID, podSandboxConfig, spec *startSpec, pod *v1.Pod,<br>
 podStatus *PodStatus, pullSecrets []v1.Secret, podIP string, podIPs []string) (string, error) &#123;<br>
<br>
container := spec.container<br>
<br>
// Step 1: 拉镜像<br>
m.imagePuller.EnsureImageExists(pod, container, pullSecrets, podSandboxConfig)<br>
<br>
// Step 2: 通过 CRI 创建容器<br>
containerConfig := m.generateContainerConfig(container, pod, restartCount, podIP, imageRef, podIPs, target)<br>
<br>
m.internalLifecycle.PreCreateContainer(pod, container, containerConfig)<br>
containerID := m.runtimeService.CreateContainer(podSandboxID, containerConfig, podSandboxConfig)<br>
m.internalLifecycle.PreStartContainer(pod, container, containerID)<br>
<br>
// Step 3: 启动容器<br>
m.runtimeService.StartContainer(containerID)<br>
<br>
legacySymlink := legacyLogSymlink(containerID, containerMeta.Name, sandboxMeta.Name, sandboxMeta.Namespace)<br>
m.osInterface.Symlink(containerLog, legacySymlink)<br>
<br>
// Step 4: 执行 post start hook<br>
m.runner.Run(kubeContainerID, pod, container, container.Lifecycle.PostStart)<br>
&#125; <br>
</pre><br>
过程：<br>
<ol><li><a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/kubelet/kuberuntime/kuberuntime_container.go#L140">拉镜像</a>。 如果是私有镜像仓库，就会从 PodSpec 中寻找访问仓库用的 secrets。</li><li><br>通过 CRI <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/kubelet/kuberuntime/kuberuntime_container.go#L179">创建 container</a>。<br>
<br>从 parent PodSpec 的  <code class="prettyprint">ContainerConfig</code>  struct 中解析参数（command, image, labels, mounts, devices, env variables 等等）， 然后通过 protobuf 发送给 CRI plugin。例如对于 docker，收到请求后会反序列化，从中提取自己需要的参数，然后发送给 Daemon API。 过程中它会给容器添加几个 metadata labels （例如 container type, log path, sandbox ID）。</li><li><br>然后通过  <code class="prettyprint">runtimeService.startContainer()</code>  启动容器；</li><li>如果注册了 post-start hooks，接下来就执行这些 hooks。<strong>post Hook 类型</strong>：<br>
<ul><li><code class="prettyprint">Exec</code>：在容器内执行具体的 shell 命令。</li><li><code class="prettyprint">HTTP</code>：对容器内的服务（endpoint）发起 HTTP 请求。</li></ul></li></ol><br>
<br>如果 PostStart hook 运行时间过长，或者 hang 住或失败了，容器就无法进入  <code class="prettyprint">running</code>  状态。<br>
<h3>结束</h3>至此，应该已经有 3 个 Pod 在运行了，取决于系统资源和调度策略，它们可能在一台 Node 上，也可能分散在多台。<br>
<br>原文链接：<a href="http://arthurchiao.art/blog/what-happens-when-k8s-creates-pods-5-zh/" rel="nofollow" target="_blank">http://arthurchiao.art/blog/wh ... 5-zh/</a>
                                
                                                              
</div>
            