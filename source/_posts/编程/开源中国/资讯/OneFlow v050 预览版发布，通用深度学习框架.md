
---
title: 'OneFlow v0.5.0 预览版发布，通用深度学习框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202109/22160418_os4t.png'
author: 开源中国
comments: false
date: Wed, 22 Sep 2021 16:36:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202109/22160418_os4t.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img src="https://static.oschina.net/uploads/img/202109/22160418_os4t.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left">今天是 OneFlow 开源的第 410 天，OneFlow 0.5.0 预览版发布。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:left">本次版本更新包含以下重点：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><strong>新增动态图特性</strong>：OneFlow 默认以动态图模式（eager）运行，与静态图模式（graph）相比，更容易搭建网络、调试和验证算法。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>面向对象式的动态图接口</strong><strong> </strong><strong>nn.Module</strong>，熟悉 PyTorch 的用户可以轻松上手。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>“一行代码转换 OneFlow 与 PyTorch 网络</strong>”：与 PyTorch 对齐的算子数目增加至200+。在 ResNet50、AlexNet 等常用网络上已通过 import oneflow as torch 和 import torch as flow 验证。注意：此特性是为方便用户由 PyTorch 迁移至 OneFlow 而设计，并不是承诺完全兼容 PyTorch。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><strong>面向对象式的静态图接口</strong>：新增面向对象的静态图接口 nn.Graph。保留了 OneFlow 静态图性能优势的同时，让静态图的编程门槛与动态图接近，期待更多的算法工程师把 OneFlow 的高性能优势玩起来。附一个用 nn.Graph 搭建的ResNet50示例：<em>https://github.com/Oneflow-Inc/models/tree/main/resnet50)</em></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>易用高效的分布式训练</strong>：分布式训练是大势所趋，此版本新增的 Consistent Tensor，让用户可以像操作单机单卡一样操作整个集群，并立即看到效果。新增的 launch 模块、DDP 模块配合 OneFlow 的一致性视角让用户轻松启动分布式训练，无论是数据并行、模型并行、还是流水并行，OneFlow 均原生支持，易用高效。</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>1、新增动态图功能</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新增与 PyTorch 兼容的动态图模式，原 PyTorch 用户可直接上手体验，无额外的学习成本和迁移成本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>https://docs.oneflow.org/master/basics/01_quickstart.html</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2、nn.Module 接口</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">提供面向对象式的接口 nn.Module，使得搭建神经网络更简单。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>https://docs.oneflow.org/master/basics/04_build_network.html</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>3、nn.Graph</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">长时间以来，动态图的性能、部署短板让人遗憾；静态图的编程门槛让人望而生畏。OneFlow 推出 nn.Graph 方案。 </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">nn.Graph 和 nn.Module 一样，也是面向对象式的接口，并且可以大量复用 nn.Module 中的功能。同时 nn.Graph 保留了 OneFlow 一贯的静态图的高效性能。用户只做少量的改动，就可以将 nn.Module 转为高性能的静态图。如以下示例。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-php"><span><span style="color:#d73a49">class</span> <span style="color:#6f42c1">NeuralGraph</span>(<span style="color:#6f42c1">flow</span>.<span style="color:#6f42c1">nn</span>.<span style="color:#6f42c1">Graph</span>):</span>
    <span><span style="color:#d73a49">def</span> <span style="color:#6f42c1">__init__</span><span>(<span style="color:#d73a49">self</span>)</span></span>:
        <span style="color:#d73a49">super</span>().__init_<span>_</span>()
        <span style="color:#d73a49">self</span>.model = model <span style="color:#6a737d"># model是 nn.Module 对象</span>

    <span><span style="color:#d73a49">def</span> <span style="color:#6f42c1">build</span><span>(<span style="color:#d73a49">self</span>, x)</span></span>:
        y_pred = <span style="color:#d73a49">self</span>.model(x)
        <span style="color:#d73a49">return</span> y_pred

graph = NeuralGraph() <span style="color:#6a737d"># Graph 对象</span>
y_pred = graph(x) <span style="color:#6a737d"># 首次调用会编译计算图并运行，后续调用都是直接运行</span>

</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">用户使用 nn.Module，可以快速验证想法，解决正确性、模型效果的问题。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">需要优化性能时，再花很少的精力转为 nn.Graph。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>https://docs.oneflow.org/master/basics/08_nn_graph.html</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>4、易用高效的分布式训练</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">对不少工程师而言，可能还不熟悉分布式训练，为此我们整理了分布式训练专题，它既可以作为用 OneFlow 做分布式训练的用户手册，也可以作为深度学习分布式入门的一手资料。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>https://docs.oneflow.org/master/parallelism/01_introduction.html</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>5、Consistent Tensor</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新增动态图模式下的 Consistent Tensor，用户第一次可以简单直观地看到张量在集群中如何被自动分发、组合。OneFlow 提供的一致性视角，让 OneFlow 不借助插件，就能轻松配置各种并行策略。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>https://docs.oneflow.org/master/parallelism/03_consistent_tensor.html</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>6、DDP 模块</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新增 DDP模块用于做分布式数据并行。它使得用户只需要改动极少的代码，就能将单机训练脚本扩充为分布式脚本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>https://docs.oneflow.org/master/parallelism/05_ddp.html</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>7、易用、原生的流水并行支持</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用 nn.Graph，通过设置 Consistent Tensor 的 placement 和 sbp 属性，用户只需要关注流水并行的逻辑。支持高效流水所需的 micro batch、张量缓存分配等问题都由 OneFlow 自动解决。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">查看流水并行示例代码:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>https://docs.oneflow.org/master/parallelism/06_pipeline.html</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">其他人都在看</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%253D%253D%26chksm%3Dfe41866fc9360f796889e7fd34469ec23289e8224c1168f70d50675d0e2d96a6d46edd5222cd%26idx%3D1%26mid%3D2247485529%26scene%3D21%26sn%3Dd220a69422273762f5691ddaefcc79f1%23wechat_redirect" target="_blank">“我们决定去登月”| OneFlow开源这一年</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%253D%253D%26chksm%3Dfe4186a7c9360fb187c0bdc59876165058bba18d760a7675ab61f6ca47a9cd3419b199cd1a99%26idx%3D1%26mid%3D2247485585%26scene%3D21%26sn%3D5348f1801ecb4f782fd70e1af9c37402%23wechat_redirect" target="_blank">并行机缔造者希利斯和思维机器的浮沉十年</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%253D%253D%26chksm%3Dfe4186b6c9360fa0fd66c979af18d8e7afa2e7dd4de4561638294d11856bd7ea9501bb2cfb17%26idx%3D1%26mid%3D2247485568%26scene%3D21%26sn%3D22dc2fdec7d30bcc9d50b8ed0d49acec%23wechat_redirect" target="_blank">对抗软件系统复杂性③：恰当分层，不多不少</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%253D%253D%26chksm%3Dfe4189cdc93600db9d68622dbce73986f2bf2ca8591743d345e0ea8678d9ffa5ea774d8d1ad8%26idx%3D1%26mid%3D2247485435%26scene%3D21%26sn%3D1d98da18492f648248021f1162ce48ec%23wechat_redirect" target="_blank">动态调度的“诅咒”| 原有深度学习框架的缺陷③</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODY2MTk3Nw%253D%253D%26chksm%3Dfe4186ecc9360ffae5312d7c684d562632df65c709fc50ba6b4f6701317eb3ac4c937ff9b1b9%26idx%3D1%26mid%3D2247485658%26scene%3D21%26sn%3Da44f876130227449edfd6aaf328abb83%23wechat_redirect" target="_blank">为OneFlow添加新的前端语言</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            