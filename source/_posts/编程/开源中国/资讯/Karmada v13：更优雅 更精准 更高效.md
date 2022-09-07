
---
title: 'Karmada v1.3：更优雅 更精准 更高效'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic4.zhimg.com/80/v2-068c6ee48eadc9dcd831dd06df270337_720w.jpg'
author: 开源中国
comments: false
date: Wed, 07 Sep 2022 17:57:00 GMT
thumbnail: 'https://pic4.zhimg.com/80/v2-068c6ee48eadc9dcd831dd06df270337_720w.jpg'
---

<div>   
<div class="content">
                                                                                            <blockquote>
 <strong>摘要：</strong>最新发布的 1.3 版本中，Karmada 重新设计了应用跨集群故障迁移功能，实现了基于污点的故障驱逐机制，并提供平滑的故障迁移过程，可以有效保障服务迁移过程的连续性（不断服）。
</blockquote> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本文分享自华为云社区《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbbs.huaweicloud.com%2Fblogs%2F374327%3Futm_source%3Doschina%26utm_medium%3Dbbs-ex%26utm_campaign%3Dother%26utm_content%3Dcontent" target="_blank">Karmada v1.3：更优雅 更精准 更高效</a>》，作者：云容器大未来。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Karmada 是开放的多云多集群容器编排引擎，旨在帮助用户在多云环境下部署和运维业务应用。凭借兼容 Kubernetes 原生 API 的能力，Karmada 可以平滑迁移单集群工作负载，并且仍可保持与 Kubernetes 周边生态工具链协同。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://pic4.zhimg.com/80/v2-068c6ee48eadc9dcd831dd06df270337_720w.jpg" width="814" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在最新发布的 1.3 版本中，Karmada 重新设计了应用跨集群故障迁移功能，实现了基于污点的故障驱逐机制，并提供平滑的故障迁移过程，可以有效保障服务迁移过程的连续性（不断服）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://pic2.zhimg.com/80/v2-5d878abfce44956cbc2c5678bf583e81_720w.jpg" width="1723" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本版本新增加的特性：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>增加了面向多集群的资源代理新特性，通过该代理平台业务方可以在不感知多集群的情况下，以单集群访问姿势直接操纵部署在多集群的工作负载；</li> 
 <li>提供针对集群资源建模能力，通过自定义的集群资源模型，调度器可以更精准地进行资源调度；</li> 
 <li>提供基于 Bootstrap 令牌来注册 Pull 模式集群的能力，不仅可以简化集群注册过程，还可以方便地进行权限控制；</li> 
</ul> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">此外，基于生产环境的用户反馈，本版本还进行了诸多性能优化，系统运行过程中 CPU 和内存资源需求大大降低，详细的性能测试报告稍后发布。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">与之前版本一样，v1.3 与前面的版本仍然保持兼容，前面版本的用户仍可以平滑升级。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">新特性概览</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">基于污点的优雅驱逐</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">当集群被判定为故障，并且故障时间超过宽限期（默认 5 分钟）之后，Karmada 将为故障集群添加 “NoExecute” 污点，随后新引入的 taint-manager 控制器将开始驱逐该故障集群上的工作负载，接着调度器重新调度被驱逐的工作负载至新的可用集群，如果用户开启了 GracefulEviction 特性，被驱逐的工作负载并不会被立即删除，而是延迟到新的工作负载运行之后，可以保障驱逐过程中业务不中断。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">整体故障迁移过程可以表示成：” 集群故障判定” → “负载预驱逐” → “重新调度” → “清理冗余负载”。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">此处，无论故障判定还是驱逐，用户都可以参过参数来控制：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong>--failover-eviction-timeout</strong>，指定从调度结果中删除故障集群的宽限期，默认 5 分钟</li> 
 <li><strong>--default-not-ready-toleration-seconds</strong>，指定默认情况下添加到尚未具有 notReady:NoExecute 容忍的传播策略上的容忍时间，默认 600 秒</li> 
 <li><strong>--default-unreachable-toleration-seconds</strong>，指定默认情况下添加到尚未具有 unreachable:NoExecute 容忍的传播策略上的容忍时间，默认 600 秒</li> 
 <li><strong>--graceful-eviction-timeout</strong>，指定自工作负载已移动到优雅驱逐任务以来，等待优雅驱逐控制器执行最终删除的超时时间，默认时长 10 分钟</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">跨多群集资源的全局代理</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Karmada 在 1.2 版本中新增了一个 “karmada-search” 组件，该组件为选装组件，用于缓存集群中部署的资源对象和事件，并通过搜索 API 对外提供检索服务。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">1.3 版本中，我们在该组件中引入了一个新的代理功能，允许用户以访问单集群的方式访问多集群中的资源，无论资源是否由 Karmada 管理，利用代理功能，用户可以统一通过 Karmada 控制面来操作成员集群中的资源。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">用户可以使用 ResourceRegistry API 来指定缓存的资源类型以及数据源（目标集群），例如以下配置表示从 member1 和 member2 两个集群中缓存 Pod 与 Node 资源：</p> 
<div style="text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><code class="language-text"><span style="color:#005cc5">apiVersion</span>: search.karmada.io/v1alpha1
<span style="color:#005cc5">kind</span>: ResourceRegistry
<span style="color:#005cc5">metadata</span>:
     <span style="color:#005cc5">name</span>: proxy-sample
     <span style="color:#005cc5">spec</span>:
         <span style="color:#005cc5">targetCluster</span>:
        <span style="color:#005cc5">clusterNames</span>:
        - member1
        - member2
        <span style="color:#005cc5">resourceSelectors</span>:
        - <span style="color:#005cc5">apiVersion</span>: v1
         <span style="color:#005cc5">kind</span>: Pod
        - <span style="color:#005cc5">apiVersion</span>: v1
         <span style="color:#005cc5">kind</span>: Node</code></pre> 
</div> 
<p style="color:#252b3a; margin-left:0; margin-right:0; text-align:start">将该配置提交给 karmada-apiserver 之后，便可使用 URL：/apis/search.karmada.io/v1alpha1/proxying/karmada/proxy/api/v1/namespaces/default/pods 来进行集群资源访问。该 URL 中 /apis/search.karmada.io/v1alpha1/proxying/karmada/proxy 为固定前缀，后面部分与 Kubernetes 原生 API 路径完全一致。</p> 
<p style="color:#252b3a; margin-left:0; margin-right:0; text-align:start">关于该特性的更多信息可以参考：<u>https://karmada.io/docs/userguide/globalview/proxy-global-resource/</u></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"> </p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">基于自定义集群资源模型的调度</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在集群调度的过程中，karmada-scheduler 会基于一系列的因素来做调度决策，其中一个不可或缺的因素就是集群的可用资源。之前的版本中，Karmada 采用了一种通用的资源模型 ResourceSummary 来抽象集群的可用情况，如下所示：</p> 
<div style="text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><code class="language-text"><span style="color:#005cc5">resourceSummary</span>:
   <span style="color:#005cc5">allocatable</span>:
      <span style="color:#005cc5">cpu</span>: <span style="color:#032f62">"1024"</span>
      <span style="color:#005cc5">memory</span>: <span>4096</span>Mi
      <span style="color:#005cc5">pods</span>: <span style="color:#032f62">"110"</span>
   <span style="color:#005cc5">allocated</span>:
      <span style="color:#005cc5">cpu</span>: <span style="color:#032f62">"512"</span>
      <span style="color:#005cc5">memory</span>: <span>2048</span>Mi
      <span style="color:#005cc5">pods</span>: <span style="color:#032f62">"64"</span></code></pre> 
</div> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">但是 ResourceSummary 机械地累加了集群中所有节点的资源，忽视了节点上的碎片资源，这会导致资源需求较大的 Pod 无法准确地调度到合适的集群。同时它也忽视了不同用户的集群中节点可分配的资源不完全相同的特点。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">1.3 版本中 Karmada 引入了一种新的方式 —— 自定义集群资源模型，来抽象集群的可用资源情况，旨在使调度器调度集群的结果更精确。用户可以启用 --CustomizedClusterResourceModeling 的特性开关来启用这一特性，开启后，在集群被 Karmada 所纳管后，Karmada 会自动地为集群设置默认的资源模型，这一资源模型将集群中的各个节点分为不同等级的模型，默认的资源模型将根据 CPU 和内存这两项资源指标把节点分为 9 个不同的等级，如下所示：</p> 
<div style="text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><code class="language-text"><span style="color:#005cc5">resourceModels</span>:
- <span style="color:#005cc5">grade</span>: <span>0</span>
<span style="color:#005cc5">ranges</span>:
- <span style="color:#005cc5">max</span>: <span style="color:#032f62">"1"</span>
<span style="color:#005cc5">min</span>: <span style="color:#032f62">"0"</span>
<span style="color:#005cc5">name</span>: cpu
- <span style="color:#005cc5">max</span>: <span>4</span>Gi
<span style="color:#005cc5">min</span>: <span style="color:#032f62">"0"</span>
<span style="color:#005cc5">name</span>: memory
- <span style="color:#005cc5">grade</span>: <span>1</span>
<span style="color:#005cc5">ranges</span>:
- <span style="color:#005cc5">max</span>: <span style="color:#032f62">"2"</span>
<span style="color:#005cc5">min</span>: <span style="color:#032f62">"1"</span>
<span style="color:#005cc5">name</span>: cpu
- <span style="color:#005cc5">max</span>: <span>16</span>Gi
<span style="color:#005cc5">min</span>: <span>4</span>Gi
<span style="color:#005cc5">name</span>: memory
.....
- <span style="color:#005cc5">grade</span>: <span>8</span>
<span style="color:#005cc5">ranges</span>:
- <span style="color:#005cc5">max</span>: <span style="color:#032f62">"9223372036854775807"</span>
<span style="color:#005cc5">min</span>: <span style="color:#032f62">"128"</span>
<span style="color:#005cc5">name</span>: cpu
- <span style="color:#005cc5">max</span>: <span style="color:#032f62">"9223372036854775807"</span>
<span style="color:#005cc5">min</span>: <span>1</span>Ti
<span style="color:#005cc5">name</span>: memory</code></pre> 
</div> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Cluster-status-controller 将会收集集群内的节点、Pod 信息计算对应模型节点的数量，与此同时，karmada-scheduler 根据将要调度的实例资源请求比较不同集群中满足要求的节点数，并将实例调度到满足要求的节点更多的集群。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">同时，在一些场景下，默认的集群资源模型不能满足用户特定集群的需求，现在用户可以通过 kubectl edit cluster 命令自定义地设置集群的资源模型，使资源模型能够更好地拟合集群的资源拓扑。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">基于 Bootstrap 令牌的集群注册</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">1.3 版本中，对于 Pull 模式下的集群，我们提供了一种通过命令行向 Karmada 控制面注册的方式。现在通过 karmadactl token 命令我们可以轻松的创建 Bootstrap 启动令牌的 token，token 的默认有效时长是 24 小时。</p> 
<div style="text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><code class="language-text"><span style="color:#6a737d">$</span><span> karmadactl token create --<span>print</span>-register-command --kubeconfig /etc/karmada/karmada-apiserver.config</span></code></pre> 
</div> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"> </p> 
<div style="text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><code class="language-text"># <span style="color:#d73a49">The</span> <span style="color:#d73a49">example</span> <span style="color:#d73a49">output</span> <span style="color:#d73a49">is</span> <span style="color:#d73a49">shown</span> <span style="color:#d73a49">below</span>
<span style="color:#d73a49">karmadactl</span> <span style="color:#d73a49">register</span> 10<span style="color:#6f42c1">.10</span><span style="color:#6f42c1">.x</span><span style="color:#6f42c1">.x</span><span style="color:#6f42c1">:32443</span> <span style="color:#d73a49">--token</span> <span style="color:#d73a49">t2jgtm</span><span style="color:#6f42c1">.9nybj0526mjw1jbf</span> <span style="color:#d73a49">--discovery-token-ca-cert-hash</span> <span style="color:#d73a49">sha256</span><span style="color:#6f42c1">:f5a5a43869bb44577dba582e794c3e3750f2050d62f1b1dc80fd3d6a371b6ed4</span></code></pre> 
</div> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">通过 karmadactl register 命令可以在不复制成员集群 kubeconfig 的情况下非常轻松地完成包括部署 karmada-agent 在内的注册过程，增强了控制面以 Pull 模式纳管成员集群的易用性和安全性。</p> 
<div style="text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><code class="language-text">$ karmadactl register 10.10.x.x:32443 <span style="color:#6a737d">--token t2jgtm.9nybj0526mjw1jbf --discovery-token-ca-cert-hash sha256:f5a5a43869bb44577dba582e794c3e3750f2050d62f1b1dc80fd3d6a371b6ed4</span>

<span style="color:#6a737d"># The example output is shown below</span>
[preflight] Running pre-flight checks
[prefligt] All pre-flight checks were passed
[karmada-agent-<span style="color:#d73a49">start</span>] Waiting <span style="color:#d73a49">to</span> perform the TLS Bootstrap
[karmada-<span style="color:#d73a49">agent</span>-<span style="color:#d73a49">start</span>] Waiting <span style="color:#d73a49">to</span> construct karmada-<span style="color:#d73a49">agent</span> kubeconfig
[karmada-<span style="color:#d73a49">agent</span>-<span style="color:#d73a49">start</span>] Waiting the necessary secret <span style="color:#d73a49">and</span> RBAC
[karmada-<span style="color:#d73a49">agent</span>-<span style="color:#d73a49">start</span>] Waiting karmada-<span style="color:#d73a49">agent</span> Deployment
W0825 <span>11</span>:<span>03</span>:<span>12.167027</span> <span>29336</span> check.go:<span>52</span>] pod: karmada-<span style="color:#d73a49">agent</span><span>-5</span>d659b4746-wn754 <span style="color:#d73a49">not</span> ready. <span style="color:#d73a49">status</span>: ContainerCreating
......
I0825 <span>11</span>:<span>04</span>:<span>06.174110</span> <span>29336</span> check.go:<span>49</span>] pod: karmada-<span style="color:#d73a49">agent</span><span>-5</span>d659b4746-wn754 <span style="color:#d73a49">is</span> ready. <span style="color:#d73a49">status</span>: Running

cluster(member3) <span style="color:#d73a49">is</span> joined successfully</code></pre> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">版本升级</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">我们验证了从 karmada 1.2 版本到 1.3 版本的升级路径，升级过程平滑，<span style="background-color:#ffffff; color:#252b3a">可参考升级文档：https://karmada.io/docs/administrator/upgrading/v1.2-v1.3</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">致谢贡献者</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Karmada v1.3 版本包含了来自 51 位贡献者的数百次代码提交，在此对各位贡献者表示由衷的感谢：</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">贡献者 GitHub ID：</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@AllenZMC</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@calvin0327</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@carlory</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@CharlesQQ</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@Charlie17Li</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@chaunceyjiang</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@cutezhangq</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@dapengJacky</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@dddddai</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@duanmengkk</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@Fish-pro</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@Garrybest</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@gy95</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@halfrost</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@hanweisen</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@huntsman-li</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@ikaven1024</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@joengjyu</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@JoshuaAndrew</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@kerthcet</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@kevin-wangzefeng</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@kinzhi</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@likakuli</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@lonelyCZ</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@luoMonkeyKing</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@maoyangLiu</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@mathlsj</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@mikeshng</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@Momeaking</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@mrlihanbo</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@my-git9</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@nuclearwu</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@Poor12</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@prodanlabs</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@RainbowMango</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@suwliang3</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@TheStylite</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@wawa0210</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@weilaaa</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@windsonsea</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@wlp1153468871</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@wuyingjun-lucky</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@XiShanYongYe-Chang</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@xuqianjins</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@xyz2277</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@yusank</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@yy158775</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@zgfh</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@zhixian82</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@zhuwint</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">@zirain</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">参考链接</h2> 
<p style="color:#252b3a; margin-left:0; margin-right:0; text-align:start">● Release Notes:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarmada-io%2Fkarmada%2Freleases%2Ftag%2Fv1.3.0" target="_blank"><u>https://github.com/karmada-io/karmada/releases/tag/v1.3.0</u></a></p> 
<p style="color:#252b3a; margin-left:0; margin-right:0; text-align:start">● 集群故障迁移使用指导：https://karmada.io/docs/userguide/failover/#concept</p> 
<p style="color:#252b3a; margin-left:0; margin-right:0; text-align:start">● 多集群资源全局代理使用指导：<u>https://karmada.io/docs/userguide/globalview/proxy-global-resource/</u></p> 
<p style="color:#252b3a; margin-left:0; margin-right:0; text-align:start">● 集群资源模型使用指导：<u>https://karmada.io/docs/userguide/scheduling/cluster-resources</u></p> 
<p style="color:#252b3a; margin-left:0; margin-right:0; text-align:start">● 基于 Bootstrap 令牌的集群注册使用指导：https://karmada.io/docs/userguide/clustermanager/cluster-registration</p>
                                        </div>
                                      
</div>
            