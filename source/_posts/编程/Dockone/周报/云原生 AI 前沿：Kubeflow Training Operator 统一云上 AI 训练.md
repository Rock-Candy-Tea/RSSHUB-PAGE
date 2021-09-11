
---
title: '云原生 AI 前沿：Kubeflow Training Operator 统一云上 AI 训练'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/6c3d619aa6a2b3ce47a85f0560bcafc3.jpg'
author: Dockone
comments: false
date: 2021-09-11 06:08:58
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/6c3d619aa6a2b3ce47a85f0560bcafc3.jpg'
---

<div>   
<br><h3>分布式训练与 Kubeflow</h3>当开发者想要将深度学习的分布式训练搬上 Kubernetes 集群时，首先想到的往往就是 Kubeflow 社区中形形色色的 Operators，如 tf-operator、mpi-operator。<br>
<br>这些服务于各种深度学习训练（TensorFlow、PyTorch、MXNet 等）的 Operators <strong>主要的工作包括</strong>：<br>
<ol><li>在 Kubernetes 集群上创建 Pod 以拉起各个训练进程</li><li>配置用作服务发现的信息（如 <code class="prettyprint">TF_CONFIG</code>）以及创建相关 Kubernetes 资源（如 Service）</li><li>监控并更新整个任务的状态</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/6c3d619aa6a2b3ce47a85f0560bcafc3.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/6c3d619aa6a2b3ce47a85f0560bcafc3.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
事实上，<strong>Kubeflow 的训练 Operators 已经成为在 Kubernetes 上运行分布式训练任务的实际标准</strong>。<br>
<br>不仅各大公有云厂商都已经基本收录或集成了 Kubeflow 的训练 Operators，社区上其他与深度学习训练相关的项目（如用以自动机器学习的 Katib，又如提供自动化编排功能的 Flyte）都<strong>对接了 Kubeflow 中的 Operators 作为下发创建分布式训练任务的工具。</strong><br>
<h3>Kubeflow Operators 的问题</h3>在 2019 年初，Kubeflow 社区启动了 kubeflow/common 项目用以维护 Operator 之间重复使用的部分代码。经过一年多的迭代和重构，在 2020 年中该项目<strong>逐渐稳定并开始接入训练 Operator</strong>。当前，<strong>tf-operator</strong>、<strong>mxnet-operator</strong> 和 <strong>xgboost-operator</strong> 即为构建在 kubeflow/common 项目之上的训练 Operators。<br>
<br>然而，整个 Kubeflow 训练 Operators 的项目维护依然存在许多挑战。<br>
<br><strong>主要包括</strong>：<br>
<ol><li>大量开发者的精力耗费在针对不同训练框架的功能增强和故障修复上</li><li>难以将测试和发布的基础功能与服务在不同 Operators 之间复用</li><li>第三方组件需要对接大量不同的 Operators</li><li>新的训练框架需要开发完整的对应的 Operator 才能使用，开发成本过高</li><li>众多的 Operators 对刚刚接触 Kubeflow 的新人开发者而言学习成本过高</li></ol><br>
<br>以上问题都是 Kubeflow 的开发者和维护者面对的。除此之外，<strong>这些 Operator 的使用者同样面临一些问题</strong>：<br>
<ol><li>用户需要安装多个 Operator 组件才能支持多种训练 APIs</li><li>各种 Kubeflow Jobs 的 JobSpec 看上去很类似，但是又有些许不同，并没有提供统一的使用体验</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/060d86f81d0d339205a894f3757aee12.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/060d86f81d0d339205a894f3757aee12.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
问题的原因主要在于<strong>每个深度学习框架都对应一个的 Operator 独立在一个 repository 中进行维护</strong>。这种分开维护的模式使得诸如构建环境、测试环境、部署方式以及代码逻辑都无法做到很好的整合。<br>
<br>尽管深度学习框架的数量处在收敛的过程中，但依然会有源源不断的新框架希望通过 Kubeflow 可以快速接入 Kubernetes 进行分布式训练，而这些新的增量使得问题变得更为严重。<br>
<h3>Proposal：All-in-One</h3>针对上面提到的各项问题，经过社区会议的多次讨论，决定尝试<strong>通过融合的方式将多个 Kubeflow 的训练 Operator 代码汇聚到一个仓库</strong>。<br>
<br>同时，参照 controller-runtime 中推荐的 One-Manager-Multi-Controller 的模式，让多个处理不同 API 的 controller 可以共享一个 Manager 及其 cache，在<strong>简化代码的同时也减少了在多个 Operator 同时部署时冗余的 APIServer 请求</strong>：<br>
<pre class="prettyprint">mgr, err := ctrl.NewManager(ctrl.GetConfigOrDie(), ctrl.Options&#123;...&#125;)  <br>
...  <br>
for _, s := range enabledSchemes &#123;  <br>
    setupFunc, supported := controller_v1.SupportedSchemeReconciler[s]  <br>
    if !supported &#123;os.Exit(1)&#125;  <br>
    if err = setupFunc(mgr, enableGangScheduling); err != nil &#123;  <br>
        setupLog.Error(err, "unable to create controller", "controller", s)  <br>
        os.Exit(1)  <br>
    &#125;  <br>
&#125; <br>
</pre> <br>
所有的 Controller（Reconciler）都需要向 <code class="prettyprint">SupportedSchemeReconciler</code> 提前完成注册：<br>
<pre class="prettyprint">var SupportedSchemeReconciler = map[string]ReconcilerSetupFunc&#123;  <br>
tensorflowv1.Kind: func(mgr manager.Manager, enableGangScheduling bool) error &#123;  <br>
    return tensorflowcontroller.NewReconciler(mgr, enableGangScheduling).SetupWithManager(mgr)  <br>
&#125;,  <br>
pytorchv1.Kind: func(mgr manager.Manager, enableGangScheduling bool) error &#123;  <br>
    return pytorchcontroller.NewReconciler(mgr, enableGangScheduling).SetupWithManager(mgr)  <br>
&#125;,  <br>
...,  <br>
&#125; <br>
</pre><br>
用户可以在启动 Operator 进程时通过 <code class="prettyprint">--enable-scheme</code> 来指定需要开启支持的 API。后续有新的 Controller 接入，按照这种“<strong>先注册后启动</strong>”的方式来选择性地开启对应的 Controllers。<br>
<h3>进展与近期规划</h3><strong>当前融合已经正式并入 tf-operator 的 Master 分支</strong>。用户很快可以在即将发布的 Kubeflow 1.4 Release 中体验到融合后的 tf-operator：部署单个 Operator 即可支持包括 TFJob、PyTorchJob、MXNetJob 和 XGBoostJob 在内的四种 API 支持。<br>
<br><strong>在代码仓库层面的融合是 Kubeflow Training Operator 迈向下一个阶段的第一步</strong>。这一步更多地解决了在项目运营层面，包括环境复用、整体代码管理上的一致性。而针对开发者的低代码开发，包括<strong>新功能增强、bug 修复和新 API 接入</strong>，将是我们规划的下一步目标。<br>
<br>根据这样的设计，开发者只需要修改非常有限的几个函数即可接入新的 API。<br>
<br><strong>主要包括</strong>：<br>
<pre class="prettyprint">// 根据 ctrl.Request 获取对应的自定义 Job  <br>
GetJob(ctx context.Context, req ctrl.Request) (client.Object, error)  <br>
// 从自定义 Job 中以 map[commonv1.ReplicaType]*commonv1.ReplicaSpec 的格式抽取 ReplicasSpecs  <br>
ExtractReplicasSpec(job client.Object) (map[commonv1.ReplicaType]*commonv1.ReplicaSpec, error)  <br>
// 从自定义 Job 中抽取 RunPolicy  <br>
ExtractRunPolicy(job client.Object) (*commonv1.RunPolicy, error)  <br>
// 从自定义 Job 中抽取 JobStatus  <br>
ExtractJobStatus(job client.Object) (*commonv1.JobStatus, error)<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/f06b4fe3603cf33ef639abb749a3596d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/f06b4fe3603cf33ef639abb749a3596d.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
开发者如果需要注入一些用以服务发现的环境变量，可以覆盖方法 <code class="prettyprint">DecoratePod(rtype commonv1.ReplicaType, podTemplate *corev1.PodTemplateSpec, job client.Object)</code> 在 client 向 APIServer 提交创建请求前修改 Pod。<br>
<br>以上低代码开发方式的基础已经以 <code class="prettyprint">pkg/reconciler.v1</code> 的形态合入 kubeflow/common 仓库。很快，我们也将在 tf-operator 上引入基于该 <code class="prettyprint">reconciler.v1</code> 包的基础 API，希望可以在验证 <code class="prettyprint">reconciler.v1</code> 的同时为更多通用的实用案例提供一种更为简便接入 Kubernetes 的方式。<br>
<br>如果开发者希望以更低层 API 的方式对 Controller 进行开发，<code class="prettyprint">pkg/controller.v1</code>包可以满足这一类开发者的需求。<br>
<h3>远景展望</h3>尽管针对 Kubeflow Training Operator 的优化改造还在进行中，我们并没有止步于此。对于 <strong>Training Operator 的未来的发展</strong>，我们认为存在以下几个领域值得持续投入：<br>
<ol><li><strong>首先</strong>是进一步提高 Kubeflow Training Operator 适配定制化需求 Job 时的灵活性。我们计划提出与深度学习训练框架解耦的一种 Job API 以支持更广泛的任务定义，并允许用户可以借助 kubeflow/common 中的 controller.v1 和 reconciler.v1 进行定制化开发，但其学习成本和开发成本依然过高。甚至在将来，初级开发者可以不修改 Operator 而仅仅添加/修改一些 webhook 或是 decorator server 来实现定制化修改。</li><li><strong>第二个方面</strong>是进一步增强 Kubeflow Training Operator 和其他第三方组件交互时的便利性。我们希望未来利用 Kubeflow Training Operator 来构建 AI 平台的开发者可以方便地将其与其他模块对接，实现诸如任务队列、流水线、超参数搜索等功能。</li><li><strong>最后也是最关键的</strong>，我们依然希望可以进一步提升 Kubeflow Training Operator 的稳定性。</li></ol><br>
<br>我们欢迎更多的同学能够尝试、体验 Kubeflow 并且投入到 Kubeflow 项目中来。<br>
<br>参考资料：<br>
<ol><li><a href="https://github.com/kubeflow/common/pull/141" rel="nofollow" target="_blank">https://github.com/kubeflow/common/pull/141</a></li><li><a href="https://github.com/kubeflow/common/tree/master/pkg/reconciler.v1/common" rel="nofollow" target="_blank">https://github.com/kubeflow/co ... ommon</a></li><li><a href="https://docs.google.com/document/d/1x1JPDQfDMIbnoQRftDH1IzGU0qvHGSU4W6Jl4rJLPhI/edit" rel="nofollow" target="_blank">https://docs.google.com/docume ... /edit</a></li></ol><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/20eFlnOmbydmklCM3K8lJw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/20eFlnOmbydmklCM3K8lJw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            