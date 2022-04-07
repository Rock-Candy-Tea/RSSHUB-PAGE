
---
title: '推出全新分布式计算接口！OneFlow v0.7.0 发布，LiBai 代码库、Serving 一应俱全'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/fd9ce558-a941-4c96-8c90-56948d25fa72.png'
author: 开源中国
comments: false
date: Thu, 07 Apr 2022 15:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/fd9ce558-a941-4c96-8c90-56948d25fa72.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p><img height="auto" src="https://oscimg.oschina.net/oscnet/fd9ce558-a941-4c96-8c90-56948d25fa72.png" width="720" referrerpolicy="no-referrer"></p> 
 <p><span>今天是 OneFlow 开源的 610 天，OneFlow v0.7.0 正式发布。<strong>欢迎下载体验最新版本：</strong></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOneflow-Inc%2Foneflow" target="_blank"><strong>https://github.com/Oneflow-Inc/oneflow</strong></a></p> 
 <p><span><strong><span>本次更新包含以下重点：</span></strong></span></p> 
 <ol style="list-style-type:decimal"> 
  <li> <p><strong><span>完善地提供了一种可以帮助用户轻松使用多机多卡执行的机制</span></strong><span> ：Global Tensor是 OneFlow 为社区带来的分布式执行的易用方案，用它可以方便地实现各种分布式并行策略，极大提高分布式实现的灵活性和易用性。基于 Global Tensor，OneFlow已支持 ResNet50、Wide and Deep、GPT、Bert、Swin-Transformer、InsightFace 等模型的并行化。</span></p> </li> 
  <li> <p style="text-align:left"><strong><span>持续完善 nn.Graph 功能，支持包括 ZeRO 、GradAcc、Checkpointing、Pipeline 相关的高级功能，丰富了 graph.debug 模式</span></strong><span>。新增支持任意 2D SBP 转换、支持 2D SBP 的半自动推导、支持断点续训等。 新增 OneFlow Feature Stages 标识，并给 nn.Graph 所提供的每一个功能都增加该标识。就 nn.Graph 整体而言， 基础功能进入 Beta Stage，可以支持对该功能的大部分需求；高级功能进入 Alpha Stage，可支持对该功能的标准需求。</span></p> </li> 
  <li> <p><span><strong>深度优化 Eager 性能， 在 V100 显卡上测试 Swin-Transformer 模型的单卡性能相比 v0.6.0 提升 3 倍。</strong></span></p> </li> 
  <li> <p><strong><span>算子相关进展</span></strong><span>：在单机单卡场景下，OneFlow 对 PyTorch 的兼容性进一步完善，OneFlow 已经支持的算子都保证和 PyTorch 的接口、语义、结果一致；另外设计了一套自动测试框架来验证一致性，常见网络可以做到<span style="background-color:#f6f6f6; color:#121212"><span><span>import oneflow as torch</span></span></span>  来完成迁移。相较于 v0.6.0， OneFlow 新增 16 个算子，优化 6 个算子的性能，修复 16 个算子存在的 bug。</span></p> </li> 
  <li> <p><span><strong>支持 Einsum 算子和 View 机制。</strong></span></p> </li> 
  <li> <p><span><strong>OneFlow 正式接入 MLIR 编译器生态。</strong></span></p> </li> 
  <li> <p><strong><span>发布 OneFlow-Serving v0.1.0，</span></strong><span>提供了开箱即用的 Triton OneFlow backend 镜像（</span><span style="color:#888888"><em>https://github.com/Oneflow-Inc/serving</em></span><span>）。</span></p> </li> 
  <li> <p style="text-align:left"><strong><span>发布 LiBai（李白） v0.1.0</span></strong><span>：这是一个针对 Transformer 的大规模分布式并行训练代码库，相比 Megatron-LM 等定制化代码库，基于模块化设计的 LiBai 为分布式训练提供了一系列模型和训练组件，让分布式下的模型训练像单卡一样方便（</span><span style="color:#888888"><em>https://github.com/Oneflow-Inc/libai</em></span><span>）。</span></p> </li> 
  <li> <p><strong><span>发布 Flow-Vision v0.1.0</span></strong><span>：新增 DeiT、ConvNeXt、ReXNet 等模型，完善了使用教程和文档（</span><em><span style="color:#888888">https://github.com/Oneflow-Inc/vision</span></em><span>）</span></p> </li> 
 </ol> 
 <p><strong><span style="color:#494949">以下为版本更新详情。</span></strong></p> 
 <p><span style="color:#f6ab00"><strong><span style="color:#f6ab00">1 </span></strong></span><span style="color:#1e2380"><strong><span style="color:#1e2380">分布式</span></strong></span></p> 
 <p><strong><span>Global Tenso</span></strong></p> 
 <p><span>Global Tensor 是OneFlow发布的一套全新的分布式计算接口，可以很方便地支持包括数据并行、模型并行和流水并行在内的任意并行方式。<strong>不同于普通 Tensor（下文叫 Local Tensor），Global Tensor 是一种全局视角下的 Tensor， 它的数据以特定方式分布在集群中的一组计算节点上，每个节点存储了该 Tensor 的部分或全部数据。</strong>placement 和 SBP 是每个 Global Tensor 的基本属性，描述了其数据在集群中的分布方式。</span></p> 
 <p><strong><span>Global Tensor 的数据分布方式</span></strong></p> 
 <p><span style="color:#333333">Global Tensor 支持三种不同的数据分布方式，我们将其统称为 SBP。</span></p> 
 <ul> 
  <li> <p><span>Split (dim)：数据以<span style="background-color:#f6f6f6; color:#121212"><span><span style="color:#494949">dim</span></span></span><span style="background-color:#ffffff; color:#121212"><span> </span></span>维度平均切分并分布到每一个计算节点上。</span></p> </li> 
  <li> <p><span>Broadcast：数据在每一个计算节点间进行复制。</span></p> </li> 
  <li> <p><span>PartialSum：数据为每一个计算节点的 element-wise 加和。</span></p> </li> 
 </ul> 
 <p><strong><span>统一的计算接口</span></strong></p> 
 <p><span>Global Tensor 具有和 Local Tensor 基本一致的计算接口，支持以很少的改动就可以将一个单卡的代码转换成分布式方式执行。</span></p> 
 <p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/08cd0378-a0aa-4ecb-8ad2-fd6f6fabfd1e.png" referrerpolicy="no-referrer"></p> 
 <p><strong><span>支持 Local Tensor 与 Global Tensor 的转换</span></strong></p> 
 <ul> 
  <li> <p><span>Local Tensor 可以使用 Tensor.to_global 接口创建一个 Global Tensor，并将该 Local Tensor 作为它在当前节点的本地分量。</span></p> </li> 
  <li> <p><span>Global Tensor 可以使用 Tensor.to_local 接口返回它在当前节点的本地分量。</span></p> </li> 
 </ul> 
 <p><img src="https://oscimg.oschina.net/oscnet/7e9fafa8-9e23-466a-8aa9-84a45d577a6e.png" referrerpolicy="no-referrer"></p> 
 <p><span><strong>支持 Global Tensor 在集群中重新分布</strong></span></p> 
 <p><span>Global Tensor 使用 Tensor.to_global 接口支持在集群中进行数据的重新分布，既可以选择分布到另外一组节点上，也可以改变它在这组节点上的分布方式（即改变 SBP ）。 重新分布通常会发生跨进程的数据通信，Tensor.to_global 这个接口很好地屏蔽了复杂的底层通信逻辑。</span></p> 
 <pre><code><span><span>>></span>> import oneflow as flow</span></code><code><span><span>>></span>> x = flow.tensor([<span>1.0</span>, <span>2.0</span>], placement=flow.placement(<span>"cuda"</span>, ranks=[<span>0</span>, <span>1</span>]), sbp=flow.sbp.split(<span>0</span>))</span></code><code><span><span>>></span>> y = x.to_global(placement=flow.placement(<span>"cuda"</span>, ranks=[<span>2</span>, <span>3</span>]), sbp=flow.sbp.broadcast)</span></code></pre> 
 <p><span>OneFlow 中每一种计算接口都定义了一套其所能支持的输入和输出的 SBP 组合，Global Tensor 支持自动重新分布，以满足执行某个计算接口对其 SBP 的要求。比如下面的代码：</span>  </p> 
 <pre><code><span><span>>></span>> import oneflow as flow</span></code><code><span><span>>></span>> x = flow.randn(<span>4</span>, <span>4</span>, </span></code><code><span>            placement=flow.placement(<span>"cuda"</span>, ranks=[<span>0</span>, <span>1</span>]), </span></code><code><span>            sbp=flow.sbp.split(<span>0</span>))</span></code><code><span><span>>></span>> y = flow.randn(<span>4</span>, <span>4</span>, </span></code><code><span>            placement=flow.placement(<span>"cuda"</span>, ranks=[<span>0</span>, <span>1</span>]), </span></code><code><span>            sbp=flow.sbp.split(<span>1</span>))</span></code><code><span><span>>></span>> z = x + y</span></code></pre> 
 <p><span>当执行 <span style="background-color:#ffffff; color:#121212"><span> </span></span><span style="background-color:#f6f6f6; color:#121212"><span><code><span>x + y</span></code></span></span><span style="background-color:#ffffff; color:#121212"><span> </span></span></span> <span> 时由于 x 是按第 0 维切分，y 是按第 1 维切分，它们在每个节点上的分量无法直接完成相加，那么它就会自动将 x 的 SBP 转换成<span style="background-color:#f6f6f6; color:#121212"><span><span style="color:#494949">flow</span><span style="color:#494949">.sbp.split(</span><span style="color:#494949">1)</span></span></span><span style="background-color:#ffffff; color:#121212"><span> </span></span> </span> <span> 或者将 y 自动转换成<span style="color:#494949"><span style="background-color:#f6f6f6; color:#121212"><span><span style="color:#494949">flow</span><span style="color:#494949">.sbp.split(0</span><span style="color:#494949">)</span></span></span><span style="background-color:#ffffff; color:#121212"><span> </span></span> </span><span style="color:#494949"> </span></span> <span>，计算得到的结果 z 的 SBP 为 </span> <span style="background-color:#f6f6f6; color:#121212"><span><span style="color:#494949">flow</span><span style="color:#494949">.sbp.split(</span><span style="color:#494949">1)</span></span></span> <span style="background-color:#ffffff; color:#121212"><span> </span></span> <span style="color:#494949"> </span> <span>或 </span> <code><span><span style="background-color:#f6f6f6; color:#121212"><span><span style="color:#494949">flow</span><span style="color:#494949">.sbp.split(0</span><span style="color:#494949">)</span></span></span><span style="background-color:#ffffff; color:#121212"><span> </span></span></span></code> <span>。</span></p> 
 <p><span>注意</span></p> 
 <ul> 
  <li> <p><span>Global Tensor 目前不支持和 DDP 接口混合使用；</span></p> </li> 
  <li> <p><span>Global Tensor 的代码要求所有节点一起执行，有分支的代码可能会因为执行路径分散而导致进程死锁，我们会持续改进这里的用户体验。</span></p> </li> 
 </ul> 
 <p><span style="color:#f6ab00"><strong><span style="color:#f6ab00">2 </span></strong></span><span style="color:#1e2380"><strong><span style="color:#1e2380">持续完善 nn.Graph 的功能</span></strong></span></p> 
 <p><strong><span>新增 OneFlow Feature Stages 标识</span></strong></p> 
 <p><span>OneFlow Feature Stages 标识 OneFlow 功能的成熟度等级依次为</span> <strong><span>Pre-alpha Stage、Alpah Stage、Beta Stage、Release candidate (RC) Stage、</span></strong> <strong><span>Stable Stage</span></strong> <span>。它给用户提供功能的状态说明，以了解该功能下所提供的保证，如功能完备性、API 稳定性、文档等；它还为开发者提供完善功能的标准，并据此推进对应功能走向成熟。</span></p> 
 <p><strong><span>nn.Graph v0.7.0 进展概述</span></strong></p> 
 <ul> 
  <li> <p><span>基础功能进入 Beta Stage，可以支持对该功能的大部分需求；</span></p> </li> 
  <li> <p><span>高级功能进入 Alpha Stage，可支持对该功能的标准需求；</span></p> </li> 
  <li> <p><span>已经支持了 ResNet50、Wide and Deep、GPT、Bert、Swin-Transformer、InsightFace 等模型。</span></p> </li> 
 </ul> 
 <p><strong><span>nn.Graph 静态图下 Feature</span></strong></p> 
 <ul> 
  <li> <p><span>Static Graph下的 Op 动静转换功能，从 Alpha Stage 到 Beta Stage</span></p> 
   <ul style="list-style-type:square"> 
    <li> <p><span>新增所有合法 Op 在 nn.Graph 做静态执行的单测，自动化单测功能完备；</span></p> </li> 
    <li> <p><span>新增支持更为灵活的输入输出，包括 List/Tuple/Dict 以及它们的嵌套，修复返回大小为 1 的 Tuple 问题；</span></p> </li> 
    <li> <p><span>新增后向的自动测试。</span></p> </li> 
   </ul> </li> 
  <li> <p><span>Static Graph 下的 Optimizer 和 LR Scheduler, 从 Alpha Stage 进步到 Beta Stage</span></p> 
   <ul style="list-style-type:square"> 
    <li> <p><span>添加更多的内置 LR scheduler，例如 WarmupLR, CosineAnnealingWarmRestarts 等常见的 scheduler ，同时提供 SequentialLR 和 ChainedScheduler 来为 scheduler 提供不同的组合能力；</span></p> </li> 
    <li> <p><span>重构了 scheduler 的 get_lr 函数，将其改造成纯函数的实现，目的是为了把 lr 的计算由迭代解切换到解析解，为 scheduler 的组合使用提供支撑；</span></p> </li> 
    <li> <p><code><span><span style="background-color:#f6f6f6; color:#121212"><span><span style="color:#494949">add_optimizer</span></span></span><span style="background-color:#ffffff; color:#121212"><span> </span></span></span></code> <span>接口新增参数 is_sparse。用以支持 graph 模式下的稀疏更新，支持稀疏更新的 optimizer 有 Adam 和 SGD。Eager 模式下的 optimizer 还未支持稀疏更新策略，后续版本会同稀疏张量一起支持。功能状态为 Pre-alpha Stage；</span></p> </li> 
    <li> <p><span>新增 LR 和 Step 的 Debug 打印功能，打开 LR Scheduler 的<span style="background-color:#f6f6f6; color:#494949"><span style="color:#494949">verbose</span></span> </span> <span>开关即可。</span></p> </li> 
   </ul> </li> 
  <li> <p><span>Static Graph 下新增<span style="background-color:#f6f6f6; color:#494949"><span style="color:#494949">state_dict</span></span></span> <span>和<span style="background-color:#f6f6f6; color:#494949">load_state_dict</span><span style="color:#494949"> </span></span> <span>，支持断点续训，功能状态为 Beta Stage</span></p> </li> 
  <li> <p><span>Static Graph 下的 Debug，从 Alpha Stage 进入 Beta Stage</span></p> 
   <ul style="list-style-type:square"> 
    <li> <p><span>新增 <span style="background-color:#f6f6f6; color:#494949"><span style="color:#494949">debug(2)</span></span></span> <span>、</span> <code><span><span style="color:#494949"> </span><span style="background-color:#f6f6f6; color:#494949">debug(3)</span></span></code> <span>，可以分 nn.Module 去定位问题，可定位 C++ 层 Op 对应的 Python 代码，可定位 Op 的前向图创建和推理；</span></p> </li> 
    <li> <p><span>新增显示内存开销。</span></p> </li> 
   </ul> </li> 
  <li> <p><span>Static Graph 下新增 ZeRO-DP 的支持，在数据并行下缩减和 Optimizer 关联的显存开销，功能状态为 Alpha Stage</span></p> </li> 
  <li> <p><span>Static Graph 下的 Global Tensor，多种并行执行，整体状态为 Alpha 和 Beta 之间</span></p> 
   <ul style="list-style-type:square"> 
    <li> <p><span>已在 LiBai 等多个模型库中使用；</span></p> </li> 
    <li> <p><span>已经在 OneFlow 模型库中广泛使用，单测的覆盖在进行中；</span></p> </li> 
    <li> <p><span>1D Global Tensor支持只定义 Source Tensor 的 SBP，下游可以自动推导，而且效果良好，Beta Stage；</span></p> </li> 
    <li> <p><span>新增 2D Global Tensor 支持只定义 Source Tensor 的 SBP ，下游可以自动推导，而且效果良好，Alpha Stage；</span></p> </li> 
    <li> <p><span>新增支持 1D to ND 与 ND to 1D 的转换, Alpha Stage；</span></p> </li> 
    <li> <p><span>新增支持任意 2D SBP 的转换, Alpha Stage；</span></p> </li> 
    <li> <p><span>1D&2D 单 Op 的测试在覆盖中，Pre-alpha Stage；</span></p> </li> 
    <li> <p><span>支持选择半自动推导 SBP的挑选策略，Pre-alpha Stage。</span></p> </li> 
   </ul> </li> 
  <li> <p><span>Static Graph 下的梯度累积(Gradient Accumulation)，重构和修复 Reshape 的支持，新增 API 文档，当前接口为<span style="background-color:#f6f6f6; color:#494949"><span style="color:#494949">mini-batch</span></span> </span> <span>的输入，下个版本将更新为体验更好的<span style="background-color:#f6f6f6; color:#494949">micro-batch</span><span style="color:#494949"> </span></span> <span>的输入，功能状态从 Pre-Alpha 到 Alpha；</span></p> </li> 
  <li> <p><span>Static Graph 下的流水并行，完善了教程，在 Libai 等多个模型库进入使用，功能状态为 Beta；</span></p> </li> 
  <li> <p><span>Static Graph 下的自动混合精度 AMP，新增 API 文档，功能状态 Pre-Alpha 到 Alpha；</span></p> </li> 
  <li> <p><span>Static Graph 下的 Activation Checkpointing，新增 API 文档，功能状态从 Pre-Alpha 到 Alpha；</span></p> </li> 
  <li> <p><span>Static Graph 下的多种 Op Fuse 优化，新增 API 文档，功能状态 Pre-Alpha 到 Alpha；</span></p> </li> 
  <li> <p><span>Static Graph 下的 XLA/TensorRT/OpenVINO 执行，新增 API 文档，功能状态 Pre-Alpha 到 Alpha。</span></p> </li> 
 </ul> 
 <p><span><strong><span>教程</span></strong></span></p> 
 <ul> 
  <li> <p><span>En </span> <span style="color:#888888"><em><span style="color:#888888">https://docs.oneflow.org/en/master/basics/08_nn_graph.html</span></em></span></p> </li> 
  <li> <p><span>中 </span> <em><span style="color:#888888">https://docs.oneflow.org/master/basics/08_nn_graph.html</span></em></p> </li> 
 </ul> 
 <p><strong><span>API文档</span></strong></p> 
 <ul> 
  <li> <p><span>En </span> <span style="color:#888888"><em><span style="color:#888888">https://oneflow.readthedocs.io/en/master/graph.html</span></em></span></p> </li> 
  <li> <p><span>中 </span> <em><span style="color:#888888">https://start.oneflow.org/oneflow-api-cn/graph.html</span></em></p> </li> 
 </ul> 
 <p><strong><span>流水并行的教程</span></strong></p> 
 <ul> 
  <li> <p><span>En </span> <span style="color:#888888"><em><span style="color:#888888">https://docs.oneflow.org/en/master/parallelism/06_pipeline.html</span></em></span></p> </li> 
  <li> <p><span>中 </span> <em><span style="color:#888888">https://docs.oneflow.org/master/parallelism/06_pipeline.html</span></em></p> </li> 
 </ul> 
 <p><strong><span>nn.Graph 静态图下的模型支持</span></strong></p> 
 <ul> 
  <li> <p><span>支持ResNet50单机单卡和单机多卡（</span> <span style="color:#888888"><em><span style="color:#888888">https://github.com/Oneflow-Inc/models/tree/main/Vision/classification/image/resnet50）</span></em></span></p> </li> 
  <li> <p><span>支持了Wide and Deep模型（</span> <em><span style="color:#888888">https://github.com/Oneflow-Inc/models/tree/main/RecommenderSystems/wide_and_deep）</span></em></p> </li> 
  <li> <p><span>支持了Libai中的GPT、Bert、Swin Transformer（</span> <span style="color:#888888"><em><span style="color:#888888">https://github.com/Oneflow-Inc/libai）</span></em></span></p> </li> 
  <li> <p><span>修复了以上多种模型的支持中遇到的功能问题</span></p> </li> 
 </ul> 
 <p><span style="color:#f6ab00"><strong><span style="color:#f6ab00">3 </span></strong></span><span style="color:#1e2380"><strong><span style="color:#1e2380">深度优化 Eager 性能</span></strong></span></p> 
 <ul> 
  <li> <p><span>深度优化 Eager 性能，OneFlow 在 V100 显卡上测试 Swin-Transformer 模型性能，单卡比 PyTorch 快25%， 8卡 DDP 比 PyTorch 快10%</span></p> </li> 
  <li> <p><span>优化 DDP 中的 NCCL 通信调度逻辑</span></p> </li> 
  <li> <p><span>DDP 支持 AllReduce fuse 优化，减少碎片化的 AllReduce 引起的额外开销，在 ResNet50 上测试有约 5% 的性能提升</span></p> </li> 
  <li> <p><span>VM 支持指令融合优化，大幅节省零碎小 Kernel 的调度开销</span></p> </li> 
  <li> <p><span>优化了 CPU 负载较高时的额外内存开销</span></p> </li> 
  <li> <p><span>Eager DataLoader 支持进程间内存共享优化</span></p> </li> 
  <li> <p><span>深度优化 Clip Grad 性能</span></p> </li> 
 </ul> 
 <p><span style="color:#f6ab00"><strong><span style="color:#f6ab00">4 </span></strong></span><span style="color:#1e2380"><strong><span style="color:#1e2380">算子相关进展</span></strong></span></p> 
 <ul> 
  <li> <p><span>OneFlow 成功适配 oneDNN 用于 CPU 算子加速，unary 和 binary element-wise 等 CPU 算子的性能提升 4 倍，Swin-Transformer 的 dataloader 速度提升 2.5 倍。</span></p> </li> 
  <li> <p><span>DataLoader 新增进程间内存共享功能，大幅提升 DataLoader 在 DDP 情况下的性能。</span></p> </li> 
  <li> <p><span>新增 Bool 类型 Tensor。</span></p> </li> 
  <li> <p><span>新增 To_contiguous 算子服务于 view 机制。</span></p> </li> 
  <li> <p><span>新增 Scalar div 算子。</span></p> </li> 
  <li> <p><span>新增 Lamb 优化器。</span></p> </li> 
  <li> <p><span>新增 Polynomial Learning Rate Scheduler。</span></p> </li> 
  <li> <p><span>新增 Tensor_split，As_strided 算子。</span></p> </li> 
  <li> <p><span>新增 Cumprod 算子。</span></p> </li> 
  <li> <p><span>新增 Tensor.T() 和 oneflow.t() 算子。</span></p> </li> 
  <li> <p><span>新增 Normalize 算子。</span></p> </li> 
  <li> <p><span>新增 div 和 sub 算子的 inplace 版本。</span></p> </li> 
  <li> <p><span>新增 Module.zero_grad 功能。</span></p> </li> 
  <li> <p><span>新增 Scalar Tensor 作为索引来做 list indexing 的功能。</span></p> </li> 
  <li> <p><span>新增 Leaky ReLU 算子的 half 类型支持。</span></p> </li> 
  <li> <p><span>新增 Mask Select 算子支持。</span></p> </li> 
  <li> <p><span>新增 Bool 类型的 Broadcast 及 Allgather 等非 reduce 通信操作。</span></p> </li> 
  <li> <p><span>基于自动测试框架开发支持 eager global 的自动测试。</span></p> </li> 
  <li> <p><span>优化 ReduceSum CUDA Kernel 的性能。</span></p> </li> 
  <li> <p><span>优化 Gather 算子的 CUDA Kernel 的性能。</span></p> </li> 
  <li> <p><span>优化 NCHW 情况下的 MaxPool 和 AvgPool 算子的 CUDA Kernel性能。</span></p> </li> 
  <li> <p><span>优化 PReLU 算子的后向计算部分，一般情况下可以节省较多显存。</span></p> </li> 
  <li> <p><span>优化 LayerNorm 后向 Kernel，进一步节省显存。</span></p> </li> 
  <li> <p><span>Conv1D/2D/3D 和 DeConv1D/2D/3D Kernel，stride 和 dilation 参数支持单个 int 传参，新增 Tensor.zero_() 接口，对齐 PyTorch tensor.norm，torch.max，torch.min 用法，flow.nn.functional.dropout 支持 inplace。</span></p> </li> 
  <li> <p><span>修复 BatchNorm 模块在 affine 参数为 False 运行报错的 bug。</span></p> </li> 
  <li> <p><span>修复 Maximum，Mimimum 反向的 bug。</span></p> </li> 
  <li> <p><span>修复 Var 算子 在某些情况下结果不符合预期的 bug。</span></p> </li> 
  <li> <p><span>修复 Tensor deepcopy 时行为不正确的 bug。</span></p> </li> 
  <li> <p><span>修复 Slice 算子输入 index 是 scalar tensor 时的 bug。</span></p> </li> 
  <li> <p><span>修复 BinaryCrossEntropy 在 half 情况下可能产生 nan 的 bug。</span></p> </li> 
  <li> <p><span>修复 Pow 算子底数和指数分别为实数和 Tensor 类型时报错的 bug。</span></p> </li> 
  <li> <p><span>修复 Stack 算子后向的 bug。</span></p> </li> 
  <li> <p><span>修复 Clip grad 在默认配置下并在 CUDA 上执行时 CPU 同步导致的效率过低问题。</span></p> </li> 
  <li> <p><span>修复 Batch Gather 和 Unsorted Batch Segment Sum 算子的 sbp 推导，global 单测通过。</span></p> </li> 
  <li> <p><span>修复 Affine Grid 算子的 Physical Shape 推导，并修复某些 SBP 情况下计算结果不符合预期的 bug ，global 单测通过。</span></p> </li> 
  <li> <p><span>修复 Arange 算子 不支持产生 0 size tensor 的问题，global 单测通过。</span></p> </li> 
  <li> <p><span>修复 Flip 算子 SBP 推导不正确的问题，global 单测通过。</span></p> </li> 
  <li> <p><span>修复 Advanced Indexing 和 ZerosLike 算子 SBP 的 bug。</span></p> </li> 
  <li> <p><span>修复 Eager global inplace 可能不成功的 bug。</span></p> </li> 
 </ul> 
 <p><span style="color:#f6ab00"><strong><span style="color:#f6ab00">5 </span></strong></span><span style="color:#1e2380"><strong><span style="color:#1e2380">支持 Einsum & View 机制</span></strong></span></p> 
 <p><span>新增 <span style="background-color:#f6f6f6; color:#494949"><span>einsum</span></span><span style="color:#494949"> </span>算子，<span style="background-color:#f6f6f6; color:#494949">einsum</span><span style="color:#494949"> </span>提供了一套既简洁又优雅的规则，可实现包括但不限于内积、外积、张量乘法、张量转置和张量收缩（tensor contraction）等张量操作，熟练运用 <span style="background-color:#f6f6f6; color:#494949">einsum</span><span style="color:#494949"> </span>可以很方便实现各种复杂的张量操作且不容易出错。</span></p> 
 <p><span>新增 <span style="background-color:#f6f6f6; color:#494949"><span>view</span></span> 机制 。通过 view 机制，一些常用算子可以实现 Tensor 的内存复用/共享，这样就能省去 Kernel Launch/Compute 的过程，并达到节省显存的效果。目前，新增了 reshape, view, squeeze, unsqueeze 等不会改变 tensor.is_contiguous() 属性的 view 算子， 后续会增加更多 view 算子（如 transpose, permute, narrow, expand, unfold 等）。</span></p> 
 <p><span style="color:#f6ab00"><strong><span style="color:#f6ab00">6 </span></strong></span><span style="color:#1e2380"><strong><span style="color:#1e2380">编译器相关进展</span></strong></span></p> 
 <p><span>OneFlow 正式接入 MLIR 生态，OneFlow Dialect 组件已经完备。成功完成了 OneFlow Job（OneFlow nn.Graph 的计算图）和 MLIR 的 RoundTrip，并对 OneFlow 所有的算子在 CI 流程中进行 RoundTrip 测试。</span></p> 
 <p><span>基于 MLIR DRR 实现了一系列自动 Fused 算子的静态图优化，加速 OneFlow 模型训练和推理。</span></p> 
 <p><span style="color:#f6ab00"><strong><span style="color:#f6ab00">7 </span></strong></span><span style="color:#1e2380"><strong><span style="color:#1e2380">OneFlow Serving</span></strong></span></p> 
 <p><span>OneFlow Serving 发布 v0.1.0 版本，特性如下：</span></p> 
 <ul> 
  <li> <p><span>提供用于推理的 OneFlow C++ API，支持加载模型和静态图推理。</span></p> </li> 
  <li> <p><span>模型训练者可以在 Python 中执行 <span style="background-color:#f6f6f6; color:#494949"><span style="color:#494949">flow.save(graph)</span></span><span style="color:#494949"> </span></span> <span>来同时保存模型权重和 MLIR 格式的计算图，用于在 C++ API 中加载并推理（暂不支持在 Python API 中加载计算图）。</span></p> </li> 
  <li> <p><span>支持自动使用 TensorRT 和 OpenVINO 推理 OneFlow 模型，无需模型转换（基于 OneFlow XRT 模块），在 NVIDIA GPU 和 Intel CPU 上可以取得更好的加速效果。</span></p> </li> 
  <li> <p><span>实现 Triton OneFlow backend</span></p> 
   <ul style="list-style-type:square"> 
    <li> <p><span>提供开箱即用的 Docker 镜像</span></p> </li> 
    <li> <p><span>支持 auto configuration，部署时只需要给出模型路径，不需要写 Triton 配置文件</span></p> </li> 
   </ul> </li> 
  <li> <p><span>在 OF 智能云上线了一个 使用 Triton OneFlow backend 进行部署的项目（</span> <span style="color:#888888"><em>https://oneflow.cloud/drill/#/project/public/code?id=7fc904d8dbe0069820da5d6d32a764fe</em></span> <span>），欢迎试玩。</span></p> </li> 
 </ul> 
 <p><span style="color:#f6ab00"><strong><span style="color:#f6ab00">8 </span></strong></span><span style="color:#1e2380"><strong><span style="color:#1e2380">LiBai（李白）</span></strong></span></p> 
 <p style="color:#494949"><span>LiBai是一个针对 Transformer 的大规模分布式并行训练代码库，相比于 Megatron-LM 等定制化代码库，基于模块化设计的LiBai为分布式训练提供了一系列模型和训练组件，旨在让分布式下的模型训练像单卡一样方便，v0.1.0 版本主要支持下面的特性和模型：</span></p> 
 <p><span>特性:</span></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>数据并行 (Data Parallelism)</span></p> </li> 
  <li> <p><span>1维张量并行 (1D Tensor Parallelism)</span></p> </li> 
  <li> <p><span>流水线并行 (Pipeline Parallelism)</span></p> </li> 
  <li> <p><span>单卡和多卡统一的分布式网络层 (Unified Distributed Layers)</span></p> </li> 
  <li> <p><span>可扩展新的并行方式 (Extensible for new parallelism)</span></p> </li> 
  <li> <p><span>混合精度训练 (Mixed Precision Training)</span></p> </li> 
  <li> <p><span>后向重计算 (Activation Checkpointing)</span></p> </li> 
  <li> <p><span>梯度累加 (Gradient Accumulation)</span></p> </li> 
  <li> <p><span>梯度裁剪 (Gradient Clip)</span></p> </li> 
  <li> <p><span>零冗余优化器 (ZeRO)</span></p> </li> 
  <li> <p><span>更灵活的 "LazyConfig" 配置系统</span></p> </li> 
  <li> <p><span>易于使用的<span style="color:#494949"> </span><span style="background-color:#f6f6f6; color:#494949"><span>Trainer</span></span> 和 <span style="background-color:#f6f6f6; color:#494949"><span>Evaluator</span></span></span></p> </li> 
  <li> <p><span>支持图像和文本的数据预处理</span></p> </li> 
 </ul> 
 <p><span>模型:</span></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span><span style="background-color:#f6f6f6; color:#494949"><span>Bert</span></span> (3D 并行)</span></p> </li> 
  <li> <p><span><span style="background-color:#f6f6f6; color:#494949"><span>GPT-2</span></span> (3D 并行)</span></p> </li> 
  <li> <p><span><span><span style="background-color:#f6f6f6; color:#494949"><span>ViT</span></span><span> </span></span>(3D 并行)</span></p> </li> 
  <li> <p><span><span style="background-color:#f6f6f6; color:#494949"><span>Swin-Transformer</span></span><span> </span>(数据并行)</span></p> </li> 
  <li> <p><span>在 <span style="background-color:#f6f6f6; color:#494949"><span>projects/</span></span>中支持微调任务</span></p> </li> 
  <li> <p><span>在 <span style="background-color:#f6f6f6; color:#494949">projects/</span>中支持文本分类任务</span></p> </li> 
 </ul> 
 <p><span style="color:#f6ab00"><strong><span style="color:#f6ab00">9 </span></strong></span><span style="color:#1e2380"><strong><span style="color:#1e2380">flow-vison</span></strong></span></p> 
 <p><span>flowvision 发布 v0.1.0 稳定版本，在之前的版本基础上作了以下改进：</span></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>新增</span> <span style="background-color:#f6f6f6; color:#494949">trunc_normal_</span> <span>初始化方法</span></p> </li> 
  <li> <p><span>新增</span> <span style="background-color:#f6f6f6; color:#494949">DeiT</span> <span><span style="background-color:#ffffff; color:#121212"><span> </span></span>模型，重构<span style="background-color:#ffffff; color:#121212"><span> </span></span></span> <span style="background-color:#f6f6f6; color:#494949">VisionTransformer</span> <span><span style="background-color:#ffffff; color:#121212"><span> </span></span>模型</span></p> </li> 
  <li> <p><span>新增<span style="background-color:#ffffff; color:#121212"><span> </span></span></span> <span><span style="background-color:#f6f6f6; color:#494949">ConvNeXt</span></span> <span><span style="background-color:#ffffff; color:#121212"><span> </span></span>模型</span></p> </li> 
  <li> <p><span>新增</span> <span><span style="background-color:#f6f6f6; color:#121212"><span style="color:#494949">ReXNet</span></span></span> <span><span style="background-color:#ffffff; color:#121212"><span> </span></span>模型</span></p> </li> 
  <li> <p><span>支持 </span> <span style="background-color:#f6f6f6; color:#494949">PolyLRScheduler</span> <span><span style="background-color:#ffffff; color:#121212"><span> </span></span>和</span> <span style="background-color:#f6f6f6; color:#494949">TanhLRScheduler</span> <span> 学习率调整策略</span></p> </li> 
  <li> <p><span>修复在 SSD 模型中</span> <span style="background-color:#f6f6f6; color:#494949">F.normalize</span> <span>的使用</span></p> </li> 
  <li> <p><span>修复</span> <span style="background-color:#f6f6f6; color:#494949">EfficientNet</span> <span><span style="background-color:#ffffff; color:#121212"><span> 和 </span></span></span> <span style="background-color:#f6f6f6; color:#494949">Res2Net</span> <span>中的 Bug</span></p> </li> 
  <li> <p><span>修复<span style="background-color:#ffffff; color:#121212"><span> </span></span></span> <span style="background-color:#f6f6f6; color:#494949">vit_small_patch32_384</span> <span><span style="background-color:#ffffff; color:#121212"><span> 模型与 </span></span></span> <span style="background-color:#f6f6f6; color:#494949">res2net50_48w_2s</span> <span>模型的权重问题</span></p> </li> 
  <li> <p><span>重构<span style="background-color:#ffffff; color:#121212"><span> </span></span></span> <span style="background-color:#f6f6f6; color:#494949">model zoo</span> <span>并对已有模型进行了更全面完整的测试</span></p> </li> 
  <li> <p><span>重构 </span> <span style="background-color:#f6f6f6; color:#494949">load_state_dict_from_url</span> <span>方法，自动保存下载的权重至 cache 文件夹</span></p> </li> 
  <li> <p><span>完善<span style="background-color:#ffffff; color:#121212"><span> </span></span></span> <span style="background-color:#f6f6f6; color:#494949">Getting Started</span> <span><span style="background-color:#ffffff; color:#121212"><span> 和 </span></span></span> <span style="background-color:#f6f6f6; color:#494949">flowvision.models</span> <span><span style="background-color:#ffffff; color:#121212"><span> </span></span>的相关文档</span></p> </li> 
 </ul> 
 <p><span>flowvision 的 v0.2.0 版本已经在推进, 将在 v0.1.0 版本上新增大量模型并完善文档，敬请期待。</span></p> 
 <p><span style="color:#888888">其他人都在看</span></p> 
 <ul style="list-style-type:circle; margin-left:8px; margin-right:8px"> 
  <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247485062%26idx%3D1%26sn%3D19587d2e78b9924e8b9599789bd23838%26chksm%3Dfe4188b0c93601a6a5960abdfd905a4ca57b708d7f29975f9af3019f7bc3d613544800b6ce2c%26scene%3D21%23wechat_redirect" target="_blank">颠覆式编程：软件2.0</a></p> </li> 
  <li> <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247487068%26idx%3D1%26sn%3D46d7b94a22b2079d5729b12bc07333df%26chksm%3Dfe41806ac936097cd8908890ed1af3e4ed036c1727ae759e5bbae2cb2cc32743a9d72cf09ddb%26scene%3D21%23wechat_redirect" target="_blank">“远见者”特斯拉AI主管Karpathy</a></p> </li> 
  <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247487015%26idx%3D1%26sn%3D04282e2d15eca05eb56062062b46e781%26chksm%3Dfe418011c9360907048966af43299fa55b570c9d634c4bcdb3702c6e4d8101a72ef07d5ec77f%26scene%3D21%23wechat_redirect" target="_blank">TVM：成为深度学习领域的“Linux”</a></p> </li> 
  <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247487005%26idx%3D1%26sn%3D1d6ea996356045206d9407f62840dcb8%26chksm%3Dfe41802bc936093d3ad43a320752769398ecfdc05f8fd151021e4ca489eade837d573b5647c9%26scene%3D21%23wechat_redirect" target="_blank">深度学习崛起十年：“开挂”的OpenAI革新者</a></p> </li> 
  <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247486978%26idx%3D1%26sn%3D19c313e90cdb078d7faf8da73094915f%26chksm%3Dfe418034c9360922bae804ce68cba51870eb827d79646d275a78de6dc033425d88772af7de50%26scene%3D21%23wechat_redirect" target="_blank">计算机架构新黄金时代，GPU能否继续保持辉煌</a></p> </li> 
  <li> <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247487045%26idx%3D1%26sn%3D270a5a066391b0e3fcd3bd95194d2014%26chksm%3Dfe418073c936096542f819835d788d86f48ea32dd2e0b07561af4035d71a66df0846a1fd8d7b%26scene%3D21%23wechat_redirect" target="_blank">芯片设计“花招”已耍完？无指令集架构颠覆旧套路</a></p> </li> 
 </ul> 
 <p><strong><span style="color:#888888">欢迎下载体验OneFlow新一代开源深度学习框架：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOneflow-Inc%2Foneflow" target="_blank">https://github.com/Oneflow-Inc/oneflow</a></strong></p> 
</div>
                                        </div>
                                      
</div>
            