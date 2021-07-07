
---
title: 'OpenCV 4.5.3 发布，Intel 开源的计算机视觉库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9311'
author: 开源中国
comments: false
date: Wed, 07 Jul 2021 06:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9311'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OpenCV 是 Intel 开源计算机视觉库，它实现了图像处理和计算机视觉方面的很多通用算法。OpenCV 4.5.3 版本的更新内容如下：</p> 
<p>highgui：增加了对 UI 后端的支持，特殊的 OpenCV 构建允许选择 UI 后端和/或通过插件动态加载它；</p> 
<p>videoio：通过 FFmpeg 后端支持 UMat/OpenCL 硬件加速的视频解码/编码；</p> 
<p>video：DaSiamRPN 追踪器以 OpenCV 算法实现；</p> 
<p>DNN 模块：</p> 
<ul> 
 <li>改进了层/激活/支持更多的模型： 
  <ul> 
   <li>优化：在 CUDA 后端支持 MatMul；</li> 
   <li>修复：BatchNorm 重新初始化；</li> 
  </ul> </li> 
 <li>英特尔推理引擎后端： 
  <ul> 
   <li>增加了对 OpenVINO 2021.4 LTS 版本的支持；</li> 
   <li>在 IE clDNN 插件中启用了 OpenCL 内核缓存；</li> 
  </ul> </li> 
</ul> 
<p>G-API 模块：</p> 
<ul> 
 <li>Python 支持： 
  <ul> 
   <li>引入了一个新的 Python 操作 API：现在 G-API 可以直接用 Python 中的新 graph 操作来扩展；</li> 
   <li>用更多的 G-API 配置选项扩展了 Python 绑定：为管道指定任意数量的 NN 模型，graph 编译参数；</li> 
   <li>在 Python 绑定中公开了更多 G-API 操作： <code>parseSSD</code>、 <code>parseYolo</code>、 <code>copy</code>、 <code>timestamp</code>、 <code>seq_id</code>；</li> 
  </ul> </li> 
 <li>Inference 支持： 
  <ul> 
   <li>在 OpenVINO 推理后端增加了 FP16 数据类型处理；</li> 
   <li>在 OpenVINO 推理后端引入了带有 remote context 的推理，还扩展了 <code>cv::MediaFrame</code> 数据结构，以便在可能的情况下携带关于远程内存的额外信息；</li> 
  </ul> </li> 
 <li>操作： 
  <ul> 
   <li>增加了转置操作；</li> 
   <li>修正了 <code>parseSSD</code> 操作中可能存在的模糊的过载问题；</li> 
  </ul> </li> 
 <li>演示： 
  <ul> 
   <li>引入了一个 MTCNN 对象检测演示，该演示强调了如何将深度学习与 G-API 中非简单的用户自定义预处理和后处理相结合；</li> 
  </ul> </li> 
 <li>其他变化： 
  <ul> 
   <li>增加了一个新的 graph 编译选项来指定 Streaming 模式下的内部队列容量——这个选项可以用来微调执行行为，从面向吞吐量（默认）到面向延迟的模式；</li> 
   <li>在 Streaming 执行器中添加了 ITT 工具——现在，管道执行的不同部分可以在英特尔® VTune Profiler 中得到突出显示；</li> 
   <li>修正了向 graph 传递空数据输入的问题；</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fwiki%2FChangeLog%23version453" target="_blank"><code>https://github.com/opencv/opencv/wiki/ChangeLog#version453</code></a></p>
                                        </div>
                                      
</div>
            