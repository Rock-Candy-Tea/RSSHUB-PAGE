
---
title: 'TensorFlow 2.10.0 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5696'
author: 开源中国
comments: false
date: Fri, 09 Sep 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5696'
---

<div>   
<div class="content">
                                                                                            <p>TensorFlow 2.10 已经发布，此版本的亮点包括 Keras 中的用户友好功能，可帮助开发转换器、确定性和无状态初始化程序、优化器 API 的更新以及帮助加载音频数据的新工具。</p> 
<p>此版本还通过 oneDNN 增强了性能，在 Windows 上扩展了 GPU 支持等等。此版本还标志着 TensorFlow 决策森林 1.0！</p> 
<h3 style="margin-left:0px">对 Keras 注意力层的扩展、统一掩码支持</h3> 
<p>从 TensorFlow 2.10 开始，对 Keras 注意力层的掩码处理，例如 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FAttention" target="_blank">tf.keras.layers.Attention</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FAdditiveAttention" target="_blank">tf.keras.layers.AdditiveAttention</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FMultiHeadAttention%3Fversion%3Dnightly" target="_blank">tf.keras.layers.MultiHeadAttention</a> 进行了扩展和统一。特别添加了两个功能：</p> 
<p>Causal attention <strong>：</strong>三个层现在都支持<span style="color:#444444">调用 use_causal_mask</span> 参数 （<span style="color:#444444">Attention</span>和 <span style="color:#444444">AdditiveAttention</span> 用于将 Causal 参数传递给 <span style="color:#444444"><strong>init</strong></span>）。</p> 
<p><strong>隐式屏蔽：</strong> Keras <span style="color:#444444">Attention</span>、 <span style="color:#444444">AdditiveAttention </span>和 <span style="color:#444444">MultiHeadAttention </span>层现在支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tensorflow.org%2Fguide%2Fkeras%2Fmasking_and_padding" target="_blank">隐式屏蔽</a> 。（ 需要在 <span style="color:#444444">tf.keras.layers.Embedding 中设置 mask_zero=True</span>）。</p> 
<p>结合起来简化了任何 Transformer 样式模型的实现。</p> 
<h3>新的 Keras Optimizer API</h3> 
<p>之前的 Tensorflow 2.9 版本在 tf.keras.optimizers.experimental 中发布了新版本的 Keras Optimizer API，它将替换 TensorFlow 2.11 中当前的 tf.keras.optimizers 命名空间。</p> 
<p>为了将优化器命名空间正式切换到新 API，TensorFlow 2.10 的 tf.keras.optimizers.legacy 导出了所有当前的 Keras 优化器。大多数用户不会受到此更改的影响，请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Foptimizers%2Fexperimental" target="_blank">API 文档</a>，以检查工作流中使用的API 是否已更改。</p> 
<h3 style="margin-left:0px">确定性和无状态 Keras 初始化器</h3> 
<p style="margin-left:0px">TensorFlow 2.10 使 Keras 初始化程序（ <span style="color:#444444">tf.keras.initializers</span> API）无状态和确定性，建立在无状态 TF 随机操作之上。从 TensorFlow 2.10 开始，种子和非种子 Keras 初始化程序在每次调用时（对于给定的变量形状）总是会生成相同的值。</p> 
<p style="margin-left:0px">无状态初始化器使 Keras 能够支持新功能，例如使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tensorflow.org%2Fguide%2Fdtensor_overview" target="_blank">DTensor</a> 进行多客户端模型训练。</p> 
<h3 style="margin-left:0px">具有步级粒度的 BackupAndRestore 检查点</h3> 
<p style="margin-left:0px">在之前的版本 Tensorflow 2.9 中，tf.keras.callbacks.BackupAndRestore Keras 回调将在 epoch 边界备份模型和训练状态。</p> 
<p style="margin-left:0px">在 Tensorflow 2.10 中，回调还可以每 N 个训练步骤备份一次模型。 但是，，当 BackupAndRestore 与 tf.distribute.MultiWorkerMirroredStrategy 一起使用时，分布式数据集迭代器状态将被重新初始化，并且在恢复模型时不会恢复。</p> 
<h3 style="margin-left:0px">从音频文件目录轻松生成音频分类数据集</h3> 
<p style="margin-left:0px">现在可以使用新程序 tf.keras.utils.audio_dataset_from_directory ，从 .wav 文件目录轻松生成音频分类数据集。</p> 
<p style="margin-left:0px">只需将音频文件分类到每个文件类的不同目录中，一行代码将提供一个标记 tf.data.Dataset，可以将其传递给 Keras 模型。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tensorflow.org%2Ftutorials%2Faudio%2Fsimple_audio" target="_blank">查看示例</a></p> 
<h3 style="margin-left:0px">EinsumDense 层转为稳定功能</h3> 
<p>einsum 函数是线性代数的瑞士军刀。 它可以有效而明确地描述各种各样的操作。 tf.keras.layers.EinsumDense 层为 Keras 带来了一些功能。</p> 
<p>einsum、einops.rearrange 和 EinsumDense 层等操作基于描述输入和输出轴的字符串“方程”进行操作。 对于 EinsumDense，方程列出了输入参数的轴、权重的轴和输出的轴。</p> 
<p>更多内容可以查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.tensorflow.org%2F2022%2F09%2Fwhats-new-in-tensorflow-210.html" target="_blank">Tensorflow 博客</a>。</p>
                                        </div>
                                      
</div>
            