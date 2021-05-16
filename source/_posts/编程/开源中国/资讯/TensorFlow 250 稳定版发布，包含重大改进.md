
---
title: 'TensorFlow 2.5.0 稳定版发布，包含重大改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4721'
author: 开源中国
comments: false
date: Sat, 15 May 2021 23:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4721'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TensorFlow 2.5.0 稳定版<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftensorflow%2Ftensorflow%2Freleases%2Ftag%2Fv2.5.0" target="_blank">已发布</a>，此版本增加了许多重要的新特性和重大改进。</p> 
<h1><strong>新特性和改进</strong></h1> 
<p><strong>1. 增加了对 Python3.9 的支持。</strong></p> 
<p><strong>2. tf.data</strong></p> 
<ul> 
 <li> <p><code>tf.data</code> 服务现已支持严格的轮循读取，这对于示例大小不同的同步训练工作负载很有用。利用严格的轮循读取，用户可以保证消费者在同一步骤中获得相似大小的示例。</p> </li> 
 <li> <p><code>tf.data</code> 服务现已支持可选压缩。以前，数据总是经过压缩，但现在可以通过向 <code>tf.data.experimental.service.distribute(...)</code> 传递 <code>compression=None</code> 来禁用压缩。</p> </li> 
 <li> <p><code>tf.data.Dataset.batch()</code> 现已支持 <code>num_parallel_calls</code> 和 <code>deterministic</code> 参数。<code>num_parallel_calls</code> 用于表示应并行计算多个输入批次。设置 <code>num_parallel_calls</code> 后，<code>deterministic</code> 参数用于表示可以按非确定性顺序获得输出。</p> </li> 
 <li> <p>由 <code>tf.data.Dataset.options()</code> 返回的选项不再可变。</p> </li> 
 <li> <p><code>tf.data</code> 输入流水线现在可以在调试模式下执行，该模式禁用任何异步、并行或非确定性，并强制 Python 执行（而不是跟踪编译的计算图执行）传入转换（如 <code>map</code> ）中的用户定义的函数。调试模式可以通过 <code>tf.data.experimental.enable_debug_mode()</code> 启用。</p> </li> 
</ul> 
<p><strong>3. tf.lite</strong></p> 
<p>默认已启用基于 MLIR 的全新量化后端。</p> 
<ul> 
 <li> <p>全新后端用于 8 int 的训练后量化。</p> </li> 
 <li> <p>全新后端移除了多余的重缩放因子，并修复了一些错误（共享权重/偏置、极小缩放因子等）。</p> </li> 
 <li> <p>将 <code>tf.lite.TFLiteConverter</code> 中的 <code>experimental_new_quantizer</code> 设置为 False，以禁用此变更。</p> </li> 
</ul> 
<p><strong>4. tf.keras</strong></p> 
<ul> 
 <li> <p><code>tf.keras.metrics.AUC</code> 现已支持 logit 预测。</p> </li> 
 <li> <p>已在 <code>Model.fit</code> 中启用受支持的全新输入类型。<code>tf.keras.utils.experimental.DatasetCreator</code>，该类型需要可调用函数 <code>dataset_fn</code>。<code>DatasetCreator</code> 适用于所有 <code>tf.distribute</code> 策略，并且是参数服务器策略支持的唯一输入类型。</p> </li> 
</ul> 
<p><strong>5. tf.distribute</strong></p> 
<ul> 
 <li> <p>现可在 <code>tf.distribute.Strategy</code> 范围内（<code>tf.distribute.experimental.CentralStorageStrategy</code> 和 <code>tf.distribute.experimental.ParameterServerStrategy</code> 除外）创建 <code>tf.random.Generator</code>。不同的副本将得到不同随机数的工作流。</p> </li> 
 <li> <p><code>tf.distribute.experimental.ParameterServerStrategy</code> 现在与 <code>DatasetCreator</code> 一起使用时，可通过 Keras <code>Model.fit</code> 进行训练。</p> </li> 
</ul> 
<p><strong>6. TPU 嵌入支持</strong></p> 
<p>已将 <code>profile_data_directory</code> 添加到 <code>_tpu_estimator_embedding.py</code> 中的 <code>EmbeddingConfigSpec</code>。此功能允许将运行时收集的嵌入查找统计信息用于嵌入层分区决策。</p> 
<p><strong>7. PluggableDevice</strong></p> 
<p>第三方设备现可通过 StreamExecutor C API 和 PluggableDevice 接口以模块化方式连接至 TensorFlow。</p> 
<ul> 
 <li> <p>通过内核和算子注册 C API 添加自定义算子和内核。</p> </li> 
 <li> <p>使用计算图优化 C API 注册自定义计算图优化通道。</p> 
  <ul> 
   <li> <p>StreamExecutor C API</p> <p>https://github.com/tensorflow/community/blob/master/rfcs/20200612-stream-executor-c-api.md</p> </li> 
   <li> <p>PluggableDevice</p> <p>https://github.com/tensorflow/community/blob/master/rfcs/20200624-pluggable-device-for-tensorflow.md</p> </li> 
   <li> <p>以模块化方式</p> <p>https://github.com/tensorflow/community/blob/master/rfcs/20190305-modular-tensorflow.md</p> </li> 
   <li> <p>内核和算子注册 C API</p> <p>https://github.com/tensorflow/community/blob/master/rfcs/20190814-kernel-and-op-registration.md</p> </li> 
   <li> <p>计算图优化 C API</p> <p>https://github.com/tensorflow/community/blob/master/rfcs/20201027-modular-tensorflow-graph-c-api.md</p> </li> 
  </ul> </li> 
</ul> 
<p><strong>8. </strong>经过 Intel 优化的 TensorFlow <strong>的</strong> oneAPI 深度神经网络库(oneDNN)<strong>CPU 性能优化现已在官方 x86-64 Linux 和 Windows 版本中发布。</strong></p> 
<ul> 
 <li> <p>经过 Intel 优化的 TensorFlow</p> <p>https://software.intel.com/content/www/us/en/develop/articles/intel-optimization-for-tensorflow-installation-guide.html</p> </li> 
 <li> <p>oneAPI 深度神经网络库(oneDNN)</p> <p>https://github.com/oneapi-src/oneDNN</p> </li> 
</ul> 
<ul> 
 <li> <p>默认情况下，这些性能优化功能处于关闭状态。通过设置环境变量 <code>TF_ENABLE_ONEDNN_OPTS=1</code> 可启用这些功能。</p> </li> 
 <li> <p>不建议在 GPU 系统中使用这些功能，因为它们尚未经过 GPU 的充分测试。</p> </li> 
</ul> 
<p><strong>9. 利用 CUDA11.2 和 cuDNN 8.1.0 构建 TensorFlow pip 软件包。</strong></p> 
<h1><strong>重大变更</strong></h1> 
<ul> 
 <li>已将 <code>TF_CPP_MIN_VLOG_LEVEL</code> 环境变量重命名为 <code>TF_CPP_MAX_VLOG_LEVEL</code>，以正确描述其影响。</li> 
</ul> 
<hr> 
<p>稿源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FaIDrq4YkPbo8NLFMzGKElw" target="_blank">Tensorflow公众号</a></p>
                                        </div>
                                      
</div>
            