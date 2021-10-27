
---
title: 'TensorFlow 2.7.0 rc1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=608'
author: 开源中国
comments: false
date: Wed, 27 Oct 2021 07:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=608'
---

<div>   
<div class="content">
                                                                                            <p>TensorFlow 是一个用于机器学习的端到端开源平台。它有一个全面灵活的工具、库和社区资源所组成的生态，让开发人员轻松建立和部署由 ML 驱动的应用程序。</p> 
<p>TensorFlow 最初用于进行机器学习和深度神经网络研究。但该系统具有足够的通用性，也适用于其他广泛的领域。</p> 
<h3>主要变化</h3> 
<ul> 
 <li><code>tf.keras</code>: 
  <ul> 
   <li><code>Model.fit()</code>、 <code>Model.predict()</code> 和 <code>Model.evaluate()</code>方法将不再把 <code>(batch_size,)</code>的输入数据上升为 <code>(batch_size, 1)</code>。这使得 <code>Model</code>子类能够在其 <code>train_step()</code>/ <code>test_step()</code>/ <code>predict_step()</code>方法中处理标量数据。</li> 
   <li><code>Model.to_yaml()</code>和 <code>keras.models.model_from_yaml</code>方法已被替换为引发 <code>RuntimeError</code>，因为它们可能被滥用以导致任意代码执行。</li> 
   <li><code>LinearModel</code>和 <code>WideDeepModel</code>被移至 <code>tf.compat.v1.keras.models.</code>命名空间（ <code>tf.compat.v1.keras.models.LinearModel</code>和 <code>tf.compat.v1.keras.models.WideDeepModel</code>），其 <code>experimental</code> 端点（ <code>tf.keras.experimental.models.LinearModel</code>和 <code>tf.keras.experimental.models.WideDeepModel</code>）被弃用。</li> 
   <li>所有 <code>tf.keras.initializers</code> 类的 RNG 行为改变。这一变化将使初始化行为在 v1 和 v2 之间保持一致。</li> 
  </ul> </li> 
 <li><code>tf.lite</code>: 
  <ul> 
   <li>弃用 Makefile 构建：Makefile 用户需要将他们的构建迁移到 CMake 或 Bazel。</li> 
   <li>弃用 <code>tflite::OpResolver::GetDelegates</code>。TfLite 的 <code>BuiltinOpResolver::GetDelegates</code> 所返回的列表现在总是空的。相反，建议使用新方法 <code>tflite::OpResolver::GetDelegateCreators</code>。</li> 
  </ul> </li> 
 <li>TF Core: 
  <ul> 
   <li><code>tf.Graph.get_name_scope()</code> 现在总是返回一个字符串。以前，当在 <code>name_scope("")</code> 或 <code>name_scope(None)</code> 背景下调用时，它返回 <code>None</code>；现在它返回空字符串。</li> 
   <li><code>tensorflow/core/ir/</code> 包含了一个新的基于 MLIR 的 Graph dialect，与 GraphDef 同构，并将用于取代基于 GraphDef（例如 Grappler）的优化。</li> 
   <li>弃用并删除了形状推理中的 <code>attrs()</code> 函数。现在所有的属性都应该通过名字来查询。</li> 
   <li>以下 Python 符号是在 TensorFlow 的早期版本中被意外添加，现在已被删除。每个符号都有一个应该使用的替换，但注意替换的参数名称是不同的： 
    <ul> 
     <li><code>tf.quantize_and_dequantize_v4</code>（在 TensorFlow 2.4 中引入），使用 <code>tf.quantization.quantize_and_dequantize_v2</code> 代替；</li> 
     <li><code>tf.batch_mat_mul_v3</code>（在 TensorFlow 2.6 中引入），使用 <code>tf.linalg.matmul</code> 代替。</li> 
     <li><code>tf.sparse_segment_sum_grad</code>（在 TensorFlow 2.6 中引入），使用 <code>tf.raw_ops.SparseSegmentSumGrad</code>代替。</li> 
    </ul> </li> 
   <li>将 tensorflow::int64 重命名为 int_64_t（前者是后者的别名）。</li> 
  </ul> </li> 
 <li>模块化文件系统的迁移： 
  <ul> 
   <li>对 S3 和 HDFS 文件系统的支持已经迁移到了一个模块化文件系统，应该为 S3 和 HDFS 安装 <code>tensorflow-io</code> python 包，以便用获得 tensorflow 支持。</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftensorflow%2Ftensorflow%2Freleases%2Ftag%2Fv2.7.0-rc1" target="_blank">https://github.com/tensorflow/tensorflow/releases/tag/v2.7.0-rc1</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            