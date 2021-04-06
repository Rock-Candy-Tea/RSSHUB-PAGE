
---
title: 'OpenCV 4.5.2 发布，Intel 开源的计算机视觉库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2822'
author: 开源中国
comments: false
date: Tue, 06 Apr 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2822'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OpenCV 是 Intel 开源计算机视觉库，它实现了图像处理和计算机视觉方面的很多通用算法。</p> 
<h3>亮点：</h3> 
<ul> 
 <li>core：增加了对并行后端的支持。特殊的 OpenCV 构建允许选择并行后端和/或通过插件动态加载它；</li> 
 <li>imgproc：增加了 IntelligentScissors 的实现。该功能已集成到 CVAT 注释工具中，您可以在https://cvat.org 上在线试用；</li> 
 <li>videoio: 改进的硬件加速视频解码/编码任务。</li> 
</ul> 
<h3>DNN 模块：</h3> 
<ul> 
 <li>改进了 TensorFlow 解析错误的调试；</li> 
 <li>改进了图层/激活/支持更多模型； 
  <ul> 
   <li>优化了 NMS 处理、DetectionOutput；</li> 
   <li>修复了 Div with constant、MatMul、Reshape；</li> 
   <li>增加了支持：Mish ONNX 子图、NormalizeL2 (ONNX)、LeakyReLU (TensorFlow)、TanH (Darknet)、SAM (Darknet)、Exp；</li> 
  </ul> </li> 
 <li>增加了对OpenVINO 2021.3版本的支持。</li> 
</ul> 
<h3>G-API 模块：</h3> 
<ul> 
 <li>支持 Python： 
  <ul> 
   <li>引入了一个新的 Python 后端 —— 现在 G-API 可以运行用 Python 编写的自定义内核，作为管道的一部分；</li> 
   <li>扩展了 G-API Python 绑定中的推理支持；</li> 
   <li>在 G-API 的 Python 绑定中增加了更多的图形数据类型支持；</li> 
  </ul> </li> 
 <li>推理支持： 
  <ul> 
   <li>在 OpenVINO 推理后端中引入了动态输入/CNN 重塑功能；</li> 
   <li>在 OpenVINO 推理后端引入异步执行支持，现在推理可以在多个请求中并行运行，以增加流密度/吞吐量；</li> 
   <li>在 ONNX 推理后端中扩展了 INT64/INT32 支持的数据类型，在 OpenVINO 推理后端中扩展了 INT32 支持的数据类型；</li> 
   <li>在 ONNX 后端引入 cv::GFrame / cv::MediaFrame 和恒定支持；</li> 
  </ul> </li> 
 <li>媒体支持： 
  <ul> 
   <li>在绘图/渲染界面中引入了 cv::GFrame / cv::MediaFrame 支持；</li> 
   <li>在流媒体模式中引入了多流媒体输入支持和帧同步策略，以支持立体声等情况；</li> 
   <li>增加了 Y 和 UV 操作，以在图形级别访问 cv::GFrame 的 NV12 数据；</li> 
   <li>如果媒体格式不同，转换是即时完成的；</li> 
  </ul> </li> 
 <li>操作和内核： 
  <ul> 
   <li>增加了新操作的性能测试（MorphologyEx、BoundingRect、FitLine、FindContours、KMeans、Kalman、BackgroundSubtractor）；</li> 
   <li>修正了 PlaidML 后台的 RMat 输入支持；</li> 
   <li>为 Fluid AbsDiffC、AddWeighted 和 bitwise 操作添加了 ARM NEON 优化。</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fwiki%2FChangeLog%23version452" target="_blank">https://github.com/opencv/opencv/wiki/ChangeLog#version452</a></p>
                                        </div>
                                      
</div>
            