
---
title: 'TensorFlow 2.7.0 正式版发布，机器学习平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1107/074848_JgT2_4252687.png'
author: 开源中国
comments: false
date: Sat, 06 Nov 2021 23:56:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1107/074848_JgT2_4252687.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">TensorFlow 是一个用于机器学习的端到端开源平台。它有一个全面灵活的工具、库和社区资源所组成的生态，让开发人员轻松建立和部署由 ML 驱动的应用程序。TensorFlow 最初用于进行机器学习和深度神经网络研究。但该系统具有足够的通用性，也适用于其他广泛的领域。</span></p> 
<p><span style="color:#333333"><strong>2.7.0 主要更新内容：</strong></span></p> 
<h3 style="margin-left:0px"><strong>改进 TensorFlow 调试体验</strong></h3> 
<p style="margin-left:0px">之前版本 TensorFlow 错误堆栈跟踪涉及很多内部帧，通读所有帧很麻烦，而且有一些帧用户是不可操作的。2.7 版本中，TensorFlow 会过滤内部帧，让堆栈跟踪保持简短、可读，只保留用户能操作的帧。 </p> 
<ul> 
 <li>可以通过输入<strong>tf.debugging.disable_traceback_filtering() </strong>禁用此行为，</li> 
 <li>可以通过<strong>tf.debugging.enable_traceback_filtering() </strong>重新启用<strong>。</strong></li> 
 <li>如果您正在调试 TensorFlow 内部问题，请确保禁用回溯过滤。</li> 
</ul> 
<p style="margin-left:0px">此外，新版本还改进了 Keras <span style="color:#24292f"><code>Layer.__call__()</code></span> 引发的错误信息量。 </p> 
<p style="margin-left:0px">注意：新功能只适用于 Python 3.7 和以上版本。 </p> 
<p style="margin-left:0px"><strong>数据处理优化 （TensorFlow Data）</strong></p> 
<p style="margin-left:0px"><span style="color:#0a0a0a">TF data service 新增了自动切分功能，如，</span>可以使用 <strong>tf.data.experimental.service.ShardingPolicy </strong>枚举指定分片策略。<span style="color:#2e3033">自动切分(静态切分) 需要在 TensorFlow.data.experimental.DispatcherConfig 中指定 worker 地址。</span></p> 
<p style="margin-left:0px"><span style="color:#2e3033">TensorFlow 数据集 (<code>tf.data.experimental.service.register_dataset</code>) 接受可选的压缩参数。</span></p> 
<h3 style="margin-left:0px"><strong>Keras（深度学习）</strong></h3> 
<p><span style="color:#2e3033">Keras 层 </span><span style="color:#24292f"><code>tf.keras.layers.Conv</code></span><span style="color:#2e3033"> 包含一个公共的 </span><code><strong>convolution_op</strong></code><span style="color:#2e3033"> 方法，用于简化 Convo 子类的实现，使用新技术有两种方法。</span></p> 
<p><img height="143" src="https://static.oschina.net/uploads/space/2021/1107/074848_JgT2_4252687.png" width="1065" referrerpolicy="no-referrer"></p> 
<p>或者覆盖 <code><strong>convolution_op</strong></code>：</p> 
<p><img height="180" src="https://static.oschina.net/uploads/space/2021/1107/074906_HoU3_4252687.png" width="1000" referrerpolicy="no-referrer"></p> 
<p>另外，新版本将 <span style="color:#2e3033"><code>merge_state() </code>方法加入 <code>tf.keras.metrics</code> ，用于分布式计算。</span></p> 
<p><span style="color:#2e3033">还在 </span><code><strong>tf.keras.layers.TextVectorization</strong></code> 中加入 <span style="color:#24292f"><code>sparse</code> 和 <code>ragged</code> 选项，用于从 </span><strong>Keras </strong><span style="color:#24292f">层输出 </span><code>SparseTensor</code><span style="color:#24292f"> 和 </span><code>RaggedTensor</code>。</p> 
<h3 style="margin-left:0px"><strong>RPC API </strong></h3> 
<p style="margin-left:0px"><strong>2.7 版本引入了  </strong><span style="color:#24292f"><code>distribute.experimental.rpc</code></span> 包，这个包主要用来创建基于 <span style="color:#24292f">GRPC 的服务器和客户端，用于</span><span style="color:#2e3033">注册 tf 函数和调用远程注册（GRPC 是谷歌的现代轻量级通信协议），RPC api 可用于多客户端设置，即服务器和客户端都在独立的应用启动。</span></p> 
<h2 style="margin-left:0px"><span style="color:#2e3033">BUG 修复</span></h2> 
<h3 style="margin-left:0px"><span style="color:#2e3033">TF CORE</span></h3> 
<ul> 
 <li>随机数生成 (RNG) 系统现在带有新功能，可以显式选择 RNG 算法、无状态版本的 dropout，且可以在参数服务器策略的范围内创建生成器。</li> 
 <li>现在可以添加实验会话 <code><strong>tf.experimental.disable_functional_ops_lowering</strong></code><strong> </strong>，用于禁止功能控制流的操作优化。在可移植运行时中执行时这个函数很有用，因为选择性注册可能无法加载控制流的操作内核。</li> 
 <li>可以向静态哈希表添加新的实验参数，用于在匿名模式下创建表。这样一来，表资源只能通过资源句柄（而不是资源名称）访问，且指向它的所有资源句柄都消失时，表资源将自动删除。</li> 
</ul> 
<p>除以上更新项，TensorFlow 2.7 版本还包含大量细节性的 bug 修复和功能优化，详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftensorflow%2Ftensorflow%2Freleases%2Ftag%2Fv2.7.0" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            