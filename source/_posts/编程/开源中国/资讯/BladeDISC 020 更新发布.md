
---
title: 'BladeDISC 0.2.0 更新发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic1.zhimg.com/80/v2-ad100d0307dd45a1b944adb663a34bfc_720w.jpg'
author: 开源中国
comments: false
date: Tue, 13 Sep 2022 16:52:00 GMT
thumbnail: 'https://pic1.zhimg.com/80/v2-ad100d0307dd45a1b944adb663a34bfc_720w.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在BladeDISC正式开源三个月后，我们发布了0.2.0版本，该更新包含了大量的性能优化与功能增强。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Falibaba%2FBladeDISC" target="_blank">BladeDISC</a>是目前业界领先的支持动态shape的深度学习优化编译器。深度学习优化编译器负责将上层的神经网络计算图转换为底层硬件可执行的程序，当前流行的深度学习优化编译器（TVM[1]、XLA[2]、TensorRT[3]等）对静态shape的支持力度较大，对动态shape的支持则有所欠缺。其中，XLA目前只支持静态shape，TensorRT可以支持ranged shape（即指定尺寸范围内的动态shape）。BladeDISC编译器提供了对动态shape的完整支持，可以将包含动态shape语义的上层模型描述转换为高效的底层可执行程序。更多关于BladeDISC的介绍内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F462641670" target="_blank">此处</a>[5]。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本文描述BladeDISC v0.2.0版本相对于最初开源版本（即v0.1.0版本）的主要更新内容。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">性能优化</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">当前的神经网络计算图主要由访存密集型算子（主要包括element-wise/elemental算子及reduce算子）和计算密集型算子（主要包括GEMM和Convolution算子）组成。BladeDISC v0.2.0版本相对v0.1.0版本在这两方面都做了大量优化。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">访存密集算子的优化</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本章重点描述v0.2.0新增的GPU stitch优化（以及附带的shape constraint功能增强）。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">GPU上的stitch优化方法来源于我们发表在ASPLOS 2022上的论文<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fdl.acm.org%2Fdoi%2Fabs%2F10.1145%2F3503222.3507723" target="_blank">AStitch</a>[6]，我们正在逐步地将AStitch中的技术迁移到BladeDISC中，目前已完成部分迁移工作。Stitch的方法旨在解决当前深度学习模型在GPU上执行时遇到的大量的kernel调度（scheduling）和发射（launch）开销以及片外访存开销，以及不同shape之下memory-intensive算子的高效schedule问题，其基本方法是通过GPU上多层次的中间结果访存管理（以寄存器，shared memory及global memory作为中间数据的buffer）、层次化的数据同步控制以及自动适配的parallelism-aware的codegen schedule生成，将原先多个不同的fusion kernel给stitch在一起，并生成高效的计算代码。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本次BladeDISC release实现了通过shared memory将原先被reduce算子分割开的多个fusion进行stitch融合的功能，达到计算融合加速效果（跨CUDA thread block的global memory的stitch以及自动适配的parallelism-aware的codegen在本次release中暂未实现）。我们提供了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Falibaba%2FBladeDISC%2Ftree%2Fmain%2Fexamples%2FPyTorch%2FInference%2FCUDA" target="_blank">一组示例</a>来展示如何开启stitch优化。</p> 
<p style="text-align:center"><img src="https://pic1.zhimg.com/80/v2-ad100d0307dd45a1b944adb663a34bfc_720w.jpg" width="432" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><img src="https://pic4.zhimg.com/80/v2-639d63e6013185c877c43ac42c018a2b_720w.jpg" width="432" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">动态shape给stitch优化带来了新的挑战，其最重要的挑战在于，在不知道确切shape的情况下，正确地判断被stitch在一起的op之间的数据局部性，从而正确得为其中的数据传输分配片上存储（即GPU shared memory）。本次更新包含了一系列的shape constraint功能增强，作为GPU stitch功能的基础支撑。其基本思想是挖掘与传播producer op和consumer op之间以及sibling op之间的shape constraint，通过symbolic的方式构建全局的shape等价关系；在此基础上，进一步构建shape dimension之间的乘法关系，用以解析reshape等算子的shape等价性关系。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">值得说明的是，在前一个版本中（即BladeDISC开源版本v0.1.0），我们针对CPU上的模型，对部分访存密集型计算子图实现了CPU端的stitch优化，从而更好地增强数据局部性，提升访存效率。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">计算密集算子的优化</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本章主要介绍本次更新中包含的GEMM合并优化及CPU上计算密集型算子的pre-packing和layout优化。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">GEMM 合并优化</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本次release实现了以下两种GEMM合并优化：</p> 
<ol style="margin-left:0; margin-right:0"> 
 <li>两个GEMM算子有公共的操作数，将其合并为一个算子，比如 A x B 和 A x C 可以合并为 A x concat(B, C)，真实模型中的典型场景是Attention中的QKV合并；</li> 
 <li>两个GEMM有相同的计算形状，将其合并为一个batched GEMM，比如对于 A x B 和 C x D，如果A和C以及B和D的形状相同，那么就可以合并为一个batched GEMM。</li> 
</ol> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">GEMM合并带来了两个好处。其一是，GEMM合并可以增加计算尺寸，从而更好地打满硬件的计算峰值，提升计算效率；其二是，GEMM合并可以减少GPU kernel数量，从而降低kernel调度和发射的开销。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">CPU上计算密集算子的pre-packing和layout优化</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在CPU上，对于GEMM及Convolution计算，BladeDISC支持对GEMM的操作数进行pre-packing优化，通过packing的数据layout转换，使得矩阵乘操作对操作数的访问能够更好地利用数据局部性（比如使得数据访问更好地适配cache line）。具体来说，BladeDISC封装了CPU上的计算库，通过对其提供的packing函数的封装与调用来实现pre-packing功能。我们提供了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Falibaba%2FBladeDISC%2Fblob%2Fmain%2Fexamples%2FPyTorch%2FInference%2FCPU%2Falbert%2Fmain.py%2523L27" target="_blank">基于Albert的示例</a>以展示如何开启pre-packing优化。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">对于Convolution函数，不同硬件vendor的不同计算库可能需要不同的数据layout以得到最佳性能，不同的数据类型在不同layout下的性能表现也会不同（比如，NVIDIA GPU上的FP16在TensorCore上和FP32在SIMT core上对layout的要求有所不同）。本次release针对CPU和GPU上的计算库，结合数据类型的考虑，为Convolution计算自动适配最佳的数据layout。数据layout的转换通过transpose操作来进行，我们实现了前后的transpose的抵消，最大限度减少额外带来的transpose的影响。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">性能验证</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="text-align:center"><img src="https://pic3.zhimg.com/80/v2-7365fe1a970ac652e48993dc7fb99272_720w.jpg" width="2880" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">上图展示了BladeDISC在四个当下流行的模型上的性能效果（在T4 GPU上进行验证，更多模型还在验证中）。图中的Framework表示原始的深度学习框架（FastSpeech2使用了TensorFlow 2.4框架，其他模型使用了PyTorch 1.7.1框架），Static Compiler表示该框架下接入静态优化编译器后的性能（TensorFlow使用XLA，PyTorch通过转onnx来利用TensorRT 8.2进行优化，TensorRT 8.2在优化T5和S2T的过程中失败，因此没有性能数据）。可以看到，BladeDISC相对于基本的深度学习框架可以取得最高达到8倍的性能加速效果，在BERT和FastSpeech2上，BladeDISC取得了与业界先进的静态优化编译器相近的优化效果。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">重要功能支持</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本次release也包括一系列的重要功能更新，包括：</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">X86和AArch64 CPU硬件的支持</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本次release在X86和AArch64架构的CPU平台上都做了大量更新和支持。<br> X86平台方面，在已有的访存密集算子codegen支持的基础上（v0.1.0包含的功能），本次release增加了计算密集算子的支持。具体来说，BladeDISC同时支持了MKL和oneDNN两种不同的计算库后端，并支持运行时按需选择。在功能支持之外，本次releaes也包括对计算密集算子的性能优化（如前面章节提到的layout优化和weight pre-packing优化）。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">AArch64平台方面，本次release完成了访存密集算子codegen对于AArch64平台的适配，以及计算密集算子库ACL的支持（通过oneDNN的形式）。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在上述功能的支持下，BladeDISC在X86平台以及AArch64平台上都已经端到端可用。具体使用方式及性能效果参见BaldeDISC提供的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Falibaba%2FBladeDISC%2Ftree%2Fmain%2Fexamples%2FTensorFlow%2FInference%2FX86%2FBERT" target="_blank">TF示例</a>及<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Falibaba%2FBladeDISC%2Ftree%2Fmain%2Fexamples%2FPyTorch%2FInference%2FCPU%2Falbert" target="_blank">PyTorch示例</a>。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">Blade推理加速器TensorRT的圈图支持</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本次release开源了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fhelp.aliyun.com%2Fdocument_detail%2F205128.html" target="_blank">Blade推理加速器</a>[7]两个重要的功能：TorchBlade和TensorFlowBlade。这两部分是Blade推理加速器面向两个最为广泛使用的深度学习框架所做的接入层，旨在提升模型优化的体验和完整度。Blade推理加速器在接入BladeDISC之外，也接入了TensorRT。具体来说，对于PyTorch和TensorFlow的模型，Blade推理加速器会自动识别出可以被TensorRT优化的计算子图，并送给TensorRT优化引擎进行优化。一定程度上提升了使用TensorRT的转换成功率，并且提供了与BladeDISC发挥联合优化作用的可能性。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">PyTorch Training的Proof-of-Concept跑通</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">BladeDISC正在逐步支持PyTorch模型的训练优化，目前已经成功跑通mnist的简单模型。在实现层面，BladeDISC利用PyTorch的Lazy Tensor Core机制，将TorchScript子图优化为高效的可执行程序。详细的设计文档见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Falibaba%2FBladeDISC%2Fblob%2Fmain%2Fdocs%2Fdesign%2Fltc_disc.md" target="_blank">此处</a>。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">以上为本次release的部分内容，更多关于本次版本更新的内容，请查看完整的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Falibaba%2FBladeDISC%2Freleases%2Ftag%2Fv0.2.0" target="_blank">release note</a>。<strong>欢迎加入BladeDISC用户交流群。</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>项目开源地址</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2FBladeDISC" target="_blank">https://github.com/alibaba/BladeDISC</a></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"> </p> 
<h2><span><span>参考文献</span></span></h2> 
<ol style="margin-left:0; margin-right:0"> 
 <li> 
  <div>
   <span><span>"TVM: An Automated End-to-End Optimizing Compiler for Deep Learning", Tianqi Chen, Thierry Moreau, Ziheng Jiang, Lianmin Zheng, Eddie Yan, Meghan Cowan, Haichen Shen, Leyuan Wang, Yuwei Hu, Luis Ceze, Carlos Guestrin, Arvind Krishnamurthy. OSDI 2018</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>"XLA: Optimizing Compiler for Machine Learning", </span></span>
   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tensorflow.org%2Fxla" target="_blank"><span><span>https://www.tensorflow.org/xla</span></span></a>
  </div> </li> 
 <li> 
  <div>
   <span><span>"NVIDIA TensorRT", </span></span>
   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.nvidia.com%2Ftensorrt" target="_blank"><span><span>https://developer.nvidia.com/tensorrt</span></span></a>
  </div> </li> 
 <li> 
  <div>
   <span><span>"Putting the VM in TVM: The Relay Virtual Machine", </span></span>
   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftvm.apache.org%2Fdocs%2F%2Farch%2Fvirtual_machine.html" target="_blank"><span><span>https://tvm.apache.org/docs//arch/virtual_machine.html</span></span></a>
  </div> </li> 
 <li> 
  <div>
   <span><span>"阿里 BladeDISC 深度学习编译器正式开源", </span></span>
   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F462641670" target="_blank"><span><span>https://zhuanlan.zhihu.com/p/462641670</span></span></a>
  </div> </li> 
 <li> 
  <div>
   <span><span>"AStitch: Enabling A New Multi-Dimensional Optimization Space for Memory-Intensive ML Training and Inference on Modern SIMT Architectures", Zhen Zheng, Xuanda Yang, Pengzhan Zhao, Guoping Long, Kai Zhu, Feiwen Zhu, Wenyi Zhao, Xiaoyong Liu, Jun Yang, Jidong Zhai, Shuaiwen Leon Song, and Wei Lin. ASPLOS 2022</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>Blade推理加速器, </span></span>
   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhelp.aliyun.com%2Fdocument_detail%2F205128.html" target="_blank"><span><span>https://help.aliyun.com/document_detail/205128.html</span></span></a>
  </div> </li> 
</ol>
                                        </div>
                                      
</div>
            