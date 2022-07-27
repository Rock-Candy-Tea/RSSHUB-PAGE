
---
title: 'OneFlow v0.8.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/a433f1c0-37a3-4332-8e64-a627af117adf.png'
author: 开源中国
comments: false
date: Wed, 27 Jul 2022 06:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/a433f1c0-37a3-4332-8e64-a627af117adf.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p><span><img src="https://oscimg.oschina.net/oscnet/a433f1c0-37a3-4332-8e64-a627af117adf.png" referrerpolicy="no-referrer"></span></p> 
 <p><span>今天是 OneFlow 开源的 717 天，OneFlow v0.8.0 正式发布。本次更新包含523个commit，完整更新列表请<span style="color:#333333">查看</span>链接：</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOneflow-Inc%2Foneflow%2Freleases%2Ftag%2Fv0.8.0" target="_blank"><strong><span>https://github.com/Oneflow-Inc/oneflow/releases/tag/v0.8.0</span></strong></a> <span>，欢迎下载体验新版本，期待你的反馈。</span></p> 
 <p><span><span style="color:#333333">OneFlow v0.8.0 </span>主要包括以下新增亮点功能和优化：</span></p> 
 <p><span style="color:#1e2380"><strong><span style="color:#1e2380">1.兼容性</span></strong></span></p> 
 <p><strong><span>PyTorch compatible API 更加完善。</span></strong> <span>新增一系列与 PyTorch 1.10.0 兼容的功能和接口，包括新增与 PyTorch 对齐的 68 个 API， 修复了 84 个算子与接口兼容性 bug，支持用户将更多 PyTorch 模型一键迁移为 OneFlow。</span></p> 
 <p><span style="color:#1e2380"><strong><span style="color:#1e2380">2.Global 算子支持</span></strong></span></p> 
 <p><strong><span>所有算子对 Global Tensor 的支持更加完备且高效。</span></strong> <span>修复了 28 个 Global Tensor 相关的 bug，新增 180 个 Global 算子单测，用户可以更加简单且高效地用 Global Tensor 进行分布式模型开发。</span></p> 
 <p><span style="color:#1e2380"><strong><span style="color:#1e2380">3.性能</span></strong></span></p> 
 <p><strong><span>Graph 高级特性的性能更加成熟完善：</span></strong></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>除原本的 ZeRO-DP 以外，ZeRO 零冗余优化器可以与 MP，2-D，3-D 并行搭配使用，进一步节省显存开销。</span></p> </li> 
  <li> <p><span>Graph 提出了新的流水并行 API，在简化流水并行配置的同时加速流水并行与 3-D 并行的性能。</span></p> </li> 
  <li> <p><span>为了进一步提升 Graph.debug 调试效率，新增关于逻辑图、light plan 物理图、内存分析、Python 栈信息等多维度的调试功能。</span></p> </li> 
 </ul> 
 <p><img height="auto" src="https://oscimg.oschina.net/oscnet/04d32f57-4559-4d06-9802-c6a211ebf0ea.png" width="1280" referrerpolicy="no-referrer"></p> 
 <p><img height="376" src="https://oscimg.oschina.net/oscnet/up-3e6b4676ee0d1edfcfe69b902725b3a490c.png" width="762" referrerpolicy="no-referrer"></p> 
 <p><strong><span>基于 OneFlow v0.8.0 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%3D%3D%26mid%3D2247488517%26idx%3D1%26sn%3D21029ce1a98d5ee964bc173518eaeca1%26chksm%3Dfe419a33c93613252b08297338c8f6c1a5d06da2545764b8bb094b107cf616bc0c9d9026bdbd%26scene%3D21%23wechat_redirect" target="_blank">LiBai v0.2.0</a> ， GPT 和 BERT 3-D 并行下的速度优化明显</span></strong> <span>，在多个维度上的速度表现都超越相同配置下的 Megatron-LM（</span> <span style="color:#888888"><em><span>数据详见：</span></em></span> <span style="color:#888888"><em><span>https://libai.readthedocs.io/en/latest/tutorials/get_started/Benchmark.html</span></em></span> <span>）。</span></p> 
 <p><span style="color:#1e2380"><strong><span style="color:#1e2380">4.OneEmbedding组件</span></strong></span></p> 
 <p><strong><span>OneEmbedding 是一款专门为大规模推荐系统设计的拓展组件，具备高性能、可拓展、灵活度高等特点。</span></strong> <span>其具备以下特性：</span></p> 
 <ul style="list-style-type:disc"> 
  <li> <p><span>支持分层存储，动态扩容的 Embedding，用户可以以较低成本扩展 Embedding 容量</span></p> </li> 
  <li> <p><span>混合并行策略，能够轻松地将模型横向拓展到多机多卡的场景</span></p> </li> 
  <li> <p><span>通信量化压缩功能，在并行场景下，对通信的数据进行量化压缩，以减少通信量，提升训练速度</span></p> </li> 
  <li> <p><span>高效的数据流水线，将模型中没有数据依赖的部分提前执行，在时间上进行重叠</span></p> </li> 
  <li> <p><span>支持自动混合精度训练，模型训练过程中将部分计算转换为 FP16 数据类型计算，在减少显存占用的同时提升训练速度，并能保证模型收敛精度</span></p> </li> 
  <li> <p><span>针对推荐系统模型的常用操作提供一系列高性能 CUDA 算子</span></p> </li> 
  <li> <p><span>支持灵活的模型构建</span></p> </li> 
 </ul> 
 <p><span>API 文档：</span></p> 
 <p><span style="color:#888888"><em><span>https://</span></em></span> <span style="color:#888888"><em><span>docs.</span></em></span> <span style="color:#888888"><em><span>oneflow.o</span></em></span> <span style="color:#888888"><em><span>rg</span></em></span> <span style="color:#888888"><em><span>/master</span></em></span> <span style="color:#888888"><em><span>/cookies</span></em></span> <span style="color:#888888"><em><span style="color:#888888">/one_embedding.html</span></em></span></p> 
 <p><span style="color:#1e2380"><strong><span style="color:#1e2380">5.多设备适配</span></strong></span></p> 
 <p><strong><span>OneFlow 提供简洁高效易扩展的硬件抽象层 EP（Execution Provider），以应对适配不同硬件的复杂性。</span></strong> <span>引入硬件抽象层之后，用户无需关注底层硬件和框架的具体实现细节，框架的各个模块无需改动便可以适配新的硬件设备，同时，用户只需按照硬件抽象接口的约定和硬件设备的实际情况，实现一系列接口，便可以完成硬件的适配工作。</span></p> 
 <p><strong><span>EP 还定义了一组基础计算接口 Primitive，基于 Primitive 接口重新实现了 Kernel。</span></strong> <span>相比 EP 提供的运行时接口，Primitive 提供的接口更加灵活，不同接口之间相互独立，每一个接口表示了某种硬件设备可以提供的特定的计算能力。</span></p> 
 <p><span style="color:#1e2380"><strong><span style="color:#1e2380">6.调试工具栈</span></strong></span></p> 
 <p><strong><span>新增调试工具栈 OneFlow-Profiler 与 AutoProf。</span></strong></p> 
 <p><span>OneFlow-Profiler 用来在框架执行流程中收集各种性能相关信息的工具。该工具可以统计算子或系统组件的执行时间，内存显存的分配情况，同时可以记录算子对应的的输入和参数信息，这些信息可供开发者分析框架执行中开销最大的部分，以实现针对性优化（</span> <span style="color:#888888"><em><span>https://github.com/Oneflow-Inc/oneflow/pull/8047</span></em></span> <span>）。</span></p> 
 <p><img height="auto" src="https://oscimg.oschina.net/oscnet/758eb027-91d5-4d30-b9cb-323a56610e43.png" width="2614" referrerpolicy="no-referrer"></p> 
 <p><span>AutoProf 是一个测试 OneFlow 和 PyTorch 算子性能的框架，为 OneFlow 提供优雅、高效地检测 OneFlow API 与 PyTorch API 是否对齐的方法，让用户可以自动比较 OneFlow API 与 PyTorch API 的性能结果（</span> <em><span style="color:#888888">https://github.com/Oneflow-Inc/oneflow/pull/8207</span></em> <span>）。</span></p> 
 <p><span style="color:#1e2380"><strong><span style="color:#1e2380">7.异常报错处理</span></strong></span></p> 
 <p><span>大幅完善 OneFlow API 中的异常处理流程，完善 API 在异常情况下的报错提示信息。</span></p> 
 <p><span style="color:#1e2380"><strong><span style="color:#1e2380">8.API文档</span></strong></span></p> 
 <p><span>完善 OneFlow API 文档内容共20余处，按照功能对 API 文档进行模块重构。除通用的算子 API 外，详细说明 OneFlow </span> <span style="background-color:#d6d6d6">oneflow.nn.graph</span> <span>、</span> <span style="background-color:#d6d6d6">oneflow.embedding</span> <span>、</span> <span style="background-color:#d6d6d6">oneflow.autograd </span> <span>等模块及环境变量。</span></p> 
</div>
                                        </div>
                                      
</div>
            