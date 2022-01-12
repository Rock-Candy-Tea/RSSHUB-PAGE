
---
title: 'OneFlow v0.6.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/5f2f2f33-d17b-4a46-9be3-ab343c59b835.jpg'
author: 开源中国
comments: false
date: Wed, 12 Jan 2022 13:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/5f2f2f33-d17b-4a46-9be3-ab343c59b835.jpg'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p><img src="https://oscimg.oschina.net/oscnet/5f2f2f33-d17b-4a46-9be3-ab343c59b835.jpg" referrerpolicy="no-referrer"></p> 
 <p><span>今天是 OneFlow 开源的 528 天，OneFlow v0.6.0 正式发布。</span> <span>点击“</span> <strong>阅读原文</strong> <span>”，欢迎下载体验最新版本。<span>本次版本更新包括框架</span><span>、模型和 OneFlow-ONNX 三大部分，主要有：</span></span></p> 
 <ul style="list-style-type:disc"> 
  <li> <p style="margin-left:8px; margin-right:8px"><span>性能提升，包括静态图、动态图、算子性能、显存占用等方面</span></p> </li> 
  <li> <p style="margin-left:8px; margin-right:8px"><span>新增大量常用算子</span></p> </li> 
  <li> <p style="margin-left:8px; margin-right:8px"><span>完善静态图和 ConsistentTensor 功能</span></p> </li> 
  <li> <p style="margin-left:8px; margin-right:8px"><span>支持 OneFlow 作为 Nvidia Triton 的后端提供 Serving 功能</span></p> </li> 
  <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>实现丰富的视觉预训练模型，与 torchvision、timm 对齐</span></p> </li> 
  <li> <p style="margin-left:8px; margin-right:8px"><span>实现更加完善的 OneFlow-ONNX 转换功能</span></p> </li> 
 </ul> 
 <p><span>以下为版本更新详情。</span></p> 
 <p><span style="color:#1e2380"><strong><span style="color:#1e2380">框架优化</span></strong></span></p> 
 <p><strong><span>1. 深度优化 nn.Graph 的性能</span></strong></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>与 v0.5.0 相比， v0.6.0 的 nn.Graph 在 ResNet AMP  和 WDL 等模型上的训练速度提升了 10%</span></p> 
   <ul style="list-style-type:square"> 
    <li> <p><span>新版的动静转换功能的性能还有可优化的空间，近期着重优化了 nn.Graph 在高频率迭代训练场景下的性能</span></p> </li> 
    <li> <p><span>重新设计实现了 nn.Graph 的调度指令， 重构了 Actor Graph 与 Eager VM 的交互逻辑，使得 Graph 的 runtime 执行与 Python input/output Tensor 尽可能异步流水并行</span></p> </li> 
   </ul> </li> 
 </ul> 
 <p><strong><span>2. 深度优化 Eager 性能</span></strong></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>与 v0.5.0 相比，v0.6.0 OneFlow Eager 在小 batch 场景下的训练速度大幅提升</span></p> 
   <ul style="list-style-type:square"> 
    <li> <p><span>深度优化虚拟机的调度逻辑</span></p> </li> 
    <li> <p><span>优化 get/set item</span></p> </li> 
    <li> <p><span>优化 tensor.numel()</span></p> </li> 
    <li> <p><span>优化 oneflow.Size()</span></p> </li> 
   </ul> </li> 
 </ul> 
 <p><strong><span>3. 深度优化算子性能</span></strong></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>着重优化了一些影响新模型性能瓶颈的算子，使得相关的模型训练速度有明显提升</span></p> 
   <ul style="list-style-type:square"> 
    <li> <p><span>新增 fused dropout系列算子</span></p> </li> 
    <li> <p><span>新增 CPU版 group deconv 并优化性能</span></p> </li> 
    <li> <p><span>给以下算子新增 inplace 版本实现：mul, hard_sigmoid<span style="color:#494949">,</span><span style="color:#494949"> </span>sin</span></p> </li> 
    <li> <p><span>对linalg.vector_norm在ord=2.0时进行了性能优化，相比之前提升了4倍</span></p> </li> 
    <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247486307%26idx%3D1%26sn%3D71ed328371124d59c69298b54725aa1f%26chksm%3Dfe418555c9360c4376d62799df3cfdbddfb62d020016056f3d366c427adef64ee8d2d17f9393%26scene%3D21%23wechat_redirect" target="_blank"><span>深度优化LayerNorm op，性能大幅度领先PyTorch和Apex实现</span></a></p> </li> 
    <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247485908%26idx%3D2%26sn%3Dd6504a6696eca8b5bb5112d776cc9cd4%26chksm%3Dfe4187e2c9360ef47768b030ec4d766cf0773870a30723cbc5727aab9839c89c53c08f4788db%26scene%3D21%23wechat_redirect" target="_blank"><span>实现op的数据类型自动提升</span></a></p> </li> 
   </ul> </li> 
 </ul> 
 <p><strong><span>4. 深度优化 Eager 显存占用</span></strong></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>优化了某些算子在网络训练中对显存占用，使得相同计算设备可以跑更大的模型或数据</span></p> 
   <ul style="list-style-type:square"> 
    <li> <p><span>优化 broadcast binary 一族算子的后向显存占用</span></p> </li> 
    <li> <p><span>优化 Slice 算子的后向显存占用</span></p> </li> 
    <li> <p><span>优化 LayerNorm 的显存占用  </span></p> </li> 
   </ul> </li> 
 </ul> 
 <p><strong><span>5. 给静态图 nn.Graph 新增众多实用功能</span></strong></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>静态图抽象 nn.Graph 增加了许多新功能，涉及静态图的效率、调试、完备性以及在更多场景下的易用性等方面：</span></p> 
   <ul style="list-style-type:circle"> 
    <li> <p><span>为了辅助静态图的调试，我们新增了：</span></p> </li> 
   </ul> 
   <ul style="list-style-type:square"> 
    <li> <p><span>debug 模式支持 graph.debug(1) 打印更多构图信息</span></p> </li> 
    <li> <p><span>提供环境变量：ONEFLOW_DEBUG_PASS 来显示编译期 图优化前后计算图的变化</span></p> </li> 
    <li> <p><span>给 Nsight Profile 增加用户可读的线程命名信息，方便定位和检索目标关键线程位置</span></p> </li> 
    <li> <p><span>丰富了大量静态图的测试用例：增加伴随Eager测试的自动nn.Graph测试</span></p> </li> 
   </ul> 
   <ul style="list-style-type:circle"> 
    <li> <p><span>为了支持使用 nn.Graph 做模型的部署（Serving），提供了 graph.save() 和 load() 接口</span></p> </li> 
    <li> <p><span>为了在使用 TensorCore 的 GPU 上做 AMP 的加速，提供了环境变量：ONEFLOW_ENABLE_NHWC 用于表示 CNN 相关算子进行 channels last 计算</span></p> </li> 
    <li> <p><span>使得 nn.Graph 支持更多的使用场景：</span></p> </li> 
   </ul> 
   <ul style="list-style-type:square"> 
    <li> <p><span>支持 稀疏更新 Optimizer，用于 WDL 场景下的参数稀疏更新</span></p> </li> 
    <li> <p style="text-align:left"><span>支持<span style="color:#494949">在nn.Graph下使用</span>Sequential<span style="color:#494949">, </span>ModuleList<span style="color:#494949">, </span>ModuleDict<span style="color:#494949">, </span>ParameterList<span style="color:#494949">, </span>ParameterDict这些nn.Module Container</span></p> </li> 
    <li> <p><span>支持在nn.Graph的init函数中创建Optimizer</span></p> </li> 
    <li> <p><span>支持nn.Graph下多个参数共用同一个Tensor</span></p> </li> 
    <li> <p><span>支持实际的进程数大于GPU设备数的使用场景</span></p> </li> 
    <li> <p><span>nn.Graph下Consistent的SBP推理时考虑Inplace，支持更多Inplace执行</span></p> </li> 
   </ul> </li> 
 </ul> 
 <p><strong><span>6. 新增了大量算子</span></strong></p> 
 <ul style="margin-left:8px; margin-right:8px"> 
  <li> <p style="text-align:left"><span>新增算子：cumsum<span style="color:#494949">, </span>meshgrid<span style="color:#494949">, </span>linspace<span style="color:#494949">, </span>diagonal<span style="color:#494949">, </span>movedim<span style="color:#494949">, </span>roialign<span style="color:#494949">, </span>nms<span style="color:#494949">, </span>arccos<span style="color:#494949">, </span>roll</span></p> </li> 
  <li> <p style="text-align:left"><span>新增算子：masked_fill<span style="color:#494949">, </span>floordiv<span style="color:#494949">, </span>glu<span style="color:#494949">, </span>pool1d<span style="color:#494949">, </span>pool2d<span style="color:#494949">, </span>pool3d</span></p> </li> 
  <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247485949%26idx%3D2%26sn%3D81026bab860f13691461047a89cc0042%26chksm%3Dfe4187cbc9360eddbd72514b81d1f0f98b5a91853c1c01dcf7b55804439049884f073650b7f2%26scene%3D21%23wechat_redirect" target="_blank"><span>新增unfold和fold op</span></a></p> </li> 
  <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247485908%26idx%3D2%26sn%3Dd6504a6696eca8b5bb5112d776cc9cd4%26chksm%3Dfe4187e2c9360ef47768b030ec4d766cf0773870a30723cbc5727aab9839c89c53c08f4788db%26scene%3D21%23wechat_redirect" target="_blank"><span>实现op的数据类型自动提升</span></a></p> </li> 
  <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247485835%26idx%3D2%26sn%3D58418d938a7c7dac1661704dd35da7a8%26chksm%3Dfe4187bdc9360eaba27f42d209968a029e263030961bdd59961f68ccefb8e6743a1431824058%26scene%3D21%23wechat_redirect" target="_blank"><span>实现expand和repeat op</span></a></p> </li> 
  <li> <p><span>目前 torchvision 库的模型可以通过import oneflow as torch实现一键切换</span></p> </li> 
 </ul> 
 <p><strong><span>7. 支持用户自定义 autograd.Function</span></strong></p> 
 <ul style="margin-left:8px; margin-right:8px"> 
  <li> <p style="text-align:left"><span>用户可以像 Torch 一样自定义 autograd.Function</span></p> </li> 
 </ul> 
 <p><strong><span>8. 提供基础的 Serving 功能</span></strong></p> 
 <ul style="margin-left:8px; margin-right:8px"> 
  <li> <p><span>支持 OneFlow 作为 Triton 的 backend 提供模型的 Serving 功能</span></p> </li> 
 </ul> 
 <p><strong><span>9. 新增 Tensor（ConsistentTensor） 的部分功能</span></strong></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>支持 Tensor 使用 2-D SBP 来表示任意的混合并行方式（如一个 Linear 运算在设备矩阵的行方向上数据并行，在列方向上模型并行）</span></p> </li> 
  <li> <p><span>支持 Tensor 从任意的 1-D SBP 到 2-D SBP 的转换（网络由 1-D 并行 和 2-D 并行混合组成）</span></p> </li> 
  <li> <p><span>支持从 numpy 构造 ConsistentTensor</span></p> </li> 
  <li> <p><span>新增 oneflow.from_numpy()</span></p> </li> 
  <li> <p><span>新增 oneflow.numel()</span></p> </li> 
  <li> <p><span>新增 tensor.expand_as()  ###  </span></p> </li> 
 </ul> 
 <p><span style="color:#1e2380"><strong><span style="color:#1e2380">模型实现</span></strong></span></p> 
 <p><span>发布 flowvison  0.0.54 </span></p> 
 <p><em><span style="color:#888888">（</span><span style="color:#888888">链接：htt</span></em><span style="color:#888888"><em>ps://github.com/Oneflow-Inc/vision）</em></span></p> 
 <p><strong><span>1. 实现了丰富的视觉预训练模型</span></strong></p> 
 <p><span><strong>图像分类</strong></span></p> 
 <ul style="margin-left:8px; margin-right:8px"> 
  <li> <p><span>CNN系列: </span><span style="background-color:#eff1f3">ResNet</span><span>, </span><span style="background-color:#eff1f3">DenseNet</span><span>, </span><span style="background-color:#eff1f3">VGG</span><span>, </span><span style="background-color:#eff1f3">ResNext</span><span>, </span><span style="background-color:#eff1f3">EfficientNet</span><span>等</span></p> </li> 
  <li> <p><span>Vis</span><span>ion Transformer系列: </span><span style="background-color:#eff1f3">ViT</span><span>, </span><span style="background-color:#eff1f3">PVT</span><span>, </span><span style="background-color:#eff1f3">Swin-Transformer</span><span>等</span></p> </li> 
  <li> <p><span>Vision MLP系列:</span><span style="background-color:#eff1f3">Mlp-Mixer</span><span>, </span><span style="background-color:#eff1f3">Res-MLP</span><span>, </span><span style="background-color:#eff1f3">g-MLP</span><span>等</span></p> </li> 
 </ul> 
 <p><span><strong>目标检测</strong></span></p> 
 <ul style="margin-left:8px; margin-right:8px"> 
  <li> <p><span>SSD, SSDLite</span></p> </li> 
  <li> <p><span>Faster R-CNN</span></p> </li> 
  <li> <p><span>RetinaNet</span></p> </li> 
 </ul> 
 <p><span><strong>图像分割</strong></span></p> 
 <ul style="margin-left:8px; margin-right:8px"> 
  <li> <p><span>FCN</span></p> </li> 
  <li> <p><span>DeepLabV3</span></p> </li> 
 </ul> 
 <p><span><strong>风格迁移</strong> </span></p> 
 <ul style="margin-left:8px; margin-right:8px"> 
  <li> <p><span>StyleNet: 支持风格</span><span style="background-color:#eff1f3">sketch</span><span>, </span><span style="background-color:#eff1f3">candy</span><span>, </span><span style="background-color:#eff1f3">mosaic</span><span>, </span><span style="background-color:#eff1f3">rain_princess</span><span>, </span><span style="background-color:#eff1f3">undie</span></p> </li> 
 </ul> 
 <p><strong><span>2. 实现了与torchvision对齐的数据增强操作</span></strong></p> 
 <p><span>包括</span> <span style="background-color:#eff1f3">CenterCrop</span> <span>, </span> <span style="background-color:#eff1f3">ColorJitter</span> <span>等与torchvision对齐的数据增强操作，在大多数场景下可以</span> <span style="background-color:#eff1f3">import flowvision as torchvision</span> <span>直接替换</span></p> 
 <p><strong><span>3. 对齐了timm中的高级的数据增强实现</span></strong></p> 
 <p><span><strong>flowvision.data中所实现的高级数据增强操作</strong></span></p> 
 <ul style="margin-left:8px; margin-right:8px"> 
  <li> <p><span>Mixup</span></p> </li> 
  <li> <p><span>CutMix</span></p> </li> 
  <li> <p><span>Random-Erasing</span></p> </li> 
  <li> <p><span>AutoAugment</span></p> </li> 
  <li> <p><span>RandAugment</span></p> </li> 
  <li> <p><span>AugMix</span></p> </li> 
 </ul> 
 <p><strong><span>4. 单独抽离出Layers模块，提供搭建模型时即插即用的Block</span></strong></p> 
 <p><span><strong>flowvision.layers.attention模块</strong></span></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>实现了</span><span style="background-color:#eff1f3">Non-Local</span><span>, </span><span style="background-color:#eff1f3">SELayer</span><span>, </span><span style="background-color:#eff1f3">CBAM</span><span>, </span><span style="background-color:#eff1f3">BAM</span><span>, </span><span style="background-color:#eff1f3">ECA</span><span>等即插即用的at</span><span>tention模块</span></p> </li> 
 </ul> 
 <p><span><strong>flowvision.layers.blocks模块</strong> </span></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>提供</span><span>了</span><span style="background-color:#eff1f3">PatchEmb</span><span>, </span><span style="background-color:#eff1f3">Pooler</span><span>, </span><span style="background-color:#eff1f3">ConvBnAct</span><span>等在搭</span><span>建模型时可能用到的模块</span></p> </li> 
 </ul> 
 <p><span><strong>flowvision.layers.regularization模块</strong> </span></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>提供了</span><span style="background-color:#eff1f3">drop-path</span><span>, </span><span style="background-color:#eff1f3">drop-block</span><span>, </span><span style="background-color:#eff1f3">stochastic depth</span><span>等正则化模块，用来提升模型泛化能力  此外还有</span><span style="background-color:#eff1f3">activation</span><span>, </span><span style="background-color:#eff1f3">weight_init</span><span>等单独的文件，用来提供</span><span style="background-color:#eff1f3">激活函数</span><span>，</span><span style="background-color:#eff1f3">初始化方法</span><span>等组件    </span></p> </li> 
 </ul> 
 <p><span style="color:#1e2380"><strong><span style="color:#1e2380">OneFlow-ONNX转换</span></strong></span></p> 
 <p><span>更新 OneFlow 转 ONNX 模型格式的工具包</span></p> 
 <ul style="margin-left:8px; margin-right:8px"> 
  <li> <p><span>支持CPU和GPU模式的OneFlow模型转onnx模型</span></p> </li> 
  <li> <p><span>新增算子和模型测试样例，对齐OneFlowVision库中的全部分类模型</span></p> </li> 
  <li> <p><span>修复PReLU转换时出现的onnx-runtime相关的bug</span></p> </li> 
  <li> <p><span>兼容1.9.0版本以上的onnx-runtime库</span></p> </li> 
  <li> <p><span>发布0.5.4版本oneflow-onnx包，pip install oneflow-onnx即可体验</span></p> </li> 
 </ul> 
 <p><span style="color:#888888">欢迎下载体验OneFlow新一代开源深度学习框架：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOneflow-Inc%2Foneflow%2F" target="_blank">https://github.com/Oneflow-Inc/oneflow/</a></p> 
 <hr>
</div>
                                        </div>
                                      
</div>
            