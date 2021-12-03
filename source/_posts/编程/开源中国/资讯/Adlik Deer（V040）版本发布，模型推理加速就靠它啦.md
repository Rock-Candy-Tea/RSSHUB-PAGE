
---
title: 'Adlik Deer（V0.4.0）版本发布，模型推理加速就靠它啦'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1203/125502_LluC_4937141.jpeg'
author: 开源中国
comments: false
date: Fri, 03 Dec 2021 13:03:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1203/125502_LluC_4937141.jpeg'
---

<div>   
<div class="content">
                                                                    
                                                        <p>今天，Adlik Deer 版本 (V0.4.0) 发布啦！</p> 
<p><img alt src="https://static.oschina.net/uploads/space/2021/1203/125502_LluC_4937141.jpeg" width="700" referrerpolicy="no-referrer"></p> 
<p>本次的新版本中，可以看到 Adlik 最近一段时间的许多技术探索，对优化器来说有集成蒸馏、Zen-NAS 优化等；推理引擎也更易用、支持更多硬件和推理运行时。针对 Bert 的模型推理优化，Adlik 使用 Ansor 来搜索全局最优的张量调度方案，为动态输入的推理提供了专用调度器，在 x86 CPU 上能达到比 OpenVINO 更高的吞吐量。</p> 
<p>欢迎大家体验试用新版本哦，用 Adlik 实现模型推理性能的飞跃。</p> 
<h2>Compiler</h2> 
<ol> 
 <li>Adlik 编译器支持 OpenVINO INT8 量化</li> 
 <li>Adlik 编译器支持 TensorRT INT8 量化，支持扩展量化校准器，降低引入量化带来的精度下降</li> 
</ol> 
<h2>Optimizer</h2> 
<ol> 
 <li>支持集成蒸馏方式，使用多教师网络进行蒸馏优化</li> 
 <li>支持 ZEN-NAS 搜索增强特性，包括并行训练，搜索加速优化，修复原有实现 bug 等，在搜索时间下降 15% 左右情况下，搜索 Score 略有提升，搜索到的模型训练精度提升 0.2%~1%</li> 
</ol> 
<h2>Inference Engine</h2> 
<ol> 
 <li>支持 Paddle Inference Runtime，使用 Paddle 模型时无需再通过 Onnx 组件转换，直接可以在 Adlik 环境上运行推理。</li> 
 <li>支持 Intel TGL-U i5 设备推理，完成多模型支持验证，提交 Benchmark</li> 
 <li>云原生镜像发布 0.4 版本，支持引擎各组件最新版本： 
  <ol> 
   <li>OpenVINO：2021.4.582 版本</li> 
   <li>TensorFlow：2.6.2</li> 
   <li>TensorRT：7.2.1.6</li> 
   <li>Tf-lite：2.4.0</li> 
   <li>TVM：0.7</li> 
   <li>Paddle Inference：2.1.2</li> 
  </ol> </li> 
 <li>新增 C++ 版本 Client API，支持 cmake 和 bazel 方式编译，方便用户在 C/C++ 场景应用部署。</li> 
</ol> 
<h2>Benchmark Test</h2> 
<p>在 Intel TGL-U i5 设备完成 Resnet-50，Yolo v3/v4，FastRCNN，MaskRCNN 等模型 Benchmark 测试，包括时延，吞吐量，以及 GPU/CPU 视频解码下的各种性能指标。</p>
                                        </div>
                                      
</div>
            