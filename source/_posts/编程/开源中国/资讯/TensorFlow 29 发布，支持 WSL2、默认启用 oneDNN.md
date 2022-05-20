
---
title: 'TensorFlow 2.9 发布，支持 WSL2、默认启用 oneDNN'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0520/072124_u8iu_4937141.png'
author: 开源中国
comments: false
date: Fri, 20 May 2022 07:22:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0520/072124_u8iu_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TensorFlow 是一个用于机器学习的端到端开源平台。它有一个全面灵活的工具、库和社区资源所组成的生态，让开发人员轻松建立和部署由 ML 驱动的应用程序。TensorFlow 最初用于进行机器学习和深度神经网络研究。但该系统具有足够的通用性，也适用于其他广泛的领域。</p> 
<p><img alt height="394" src="https://static.oschina.net/uploads/space/2022/0520/072124_u8iu_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>TensorFlow 2.9 近日正式发布，更新内容包括 oneDNN 的性能改进，以及 DTensor 的发布，其中后者是一个用于模型分布的 API，可以用来无缝地从数据并行迁移到模型并行。</p> 
<p>TensorFlow 还对核心库进行了改进，包括 Eigen 和 <code>tf.function</code> 的统一，以及对 Windows 的 WSL2 的支持。最后，新版本还为 <code>tf.function retracing</code> 和 <code>Keras Optimizers</code> 发布了新的实验性 API。</p> 
<h3>改进 CPU 性能：默认启用 oneDNN</h3> 
<p>TensorFlow 与英特尔合作，将 oneDNN 性能库与 TensorFlow 整合在一起，以便在英特尔 CPU 上实现更好的性能。自 TensorFlow 2.5 以来，TensorFlow 对 oneDNN 有实验性的支持，它可以提供高达 4 倍的性能改进。在 TensorFlow 2.9 中，在 Linux x86 上默认开启了 oneDNN 优化，并为具有神经网络硬件功能的 CPU 开启了优化，这些功能在英特尔 Cascade Lake 以及更新的 CPU 上都具备。</p> 
<h3>使用 DTensor 的模型并行</h3> 
<p>DTensor 是一个用于分布式模型处理的新的 TensorFlow API，它允许模型可以无缝地从数据并行迁移到基于单程序多数据（SPMD）的模型并行。</p> 
<p>DTensor 的设计以下列原则为核心。</p> 
<ul> 
 <li>一个与设备无关的 API：这允许在 CPU、GPU 或 TPU 上使用相同的模型代码，包括跨设备类型划分的模型。</li> 
 <li>多客户端执行：移除协调器，让每个任务驱动其本地连接的设备，允许在不影响启动时间的情况下扩展一个模型。</li> 
 <li>传统上，TensorFlow 的分布式模型代码是围绕副本编写的，但在 DTensor 中，模型代码是从全局角度编写的，每个副本的代码由 DTensor 运行时生成和运行。</li> 
</ul> 
<h3>tf.function 的 TraceType</h3> 
<p>新版本修改了 tf.function 回溯的方式，使其更加简单、可预测和可配置。</p> 
<p><code>tf.function</code> 的所有参数都被分配了一个 <code>tf.type.experimental.TraceType</code>。自定义用户类可以使用跟踪协议（ <code>tf.types.experimental.SuppersTracingProtocol</code> ）声明一个 TraceType。</p> 
<h3>对 WSL2 的支持</h3> 
<p>Windows Subsystem for Linux 让开发者直接在 Windows 上运行 Linux 环境，而不需要传统的虚拟机或双启动设置。TensorFlow 现在支持 WSL2，包括 GPU 加速。</p> 
<h3>确定性的行为</h3> 
<p>API <code>tf.config.experimental.enable_op_determinism</code> 使 TensorFlow 操作具有确定性。</p> 
<p>确定性意味着，如果你用相同的输入多次运行一个操作，该操作每次都会返回完全相同的输出。这对于调试模型很有用，如果你用确定性从头开始训练你的模型几次，你的模型权重每次都是一样的。通常情况下，由于在操作中使用线程，可以以非确定性的顺序添加浮点数，所以许多操作是非确定性的。</p> 
<h3>用 Keras 优化训练</h3> 
<p>在 TensorFlow 2.9 中，发布一个新的实验版本的 Keras Optimizer API， <code>tf.keras.optimizers.experimental</code>。该 API 让开发者可以更容易地定制和扩展。</p> 
<p>在未来的版本中， <code>tf.keras.optimizers.experimental.Optimizer</code>（和子类）将取代 <code>tf.keras.optimizers.Optimizer</code>（和子类），这意味着使用传统的 Keras 优化器的工作流将自动切换到新的优化器。当前的 <code>tf.keras.optimizers.*</code> API 仍将可以通过 <code>tf.keras.optimizers.legacy.*</code> 访问。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftensorflow%2Ftensorflow%2Freleases%2Ftag%2Fv2.9.0" target="_blank">https://github.com/tensorflow/tensorflow/releases/tag/v2.9.0</a></p>
                                        </div>
                                      
</div>
            