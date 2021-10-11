
---
title: 'OpenCV 4.5.4 发布，Intel 开源的计算机视觉库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3342'
author: 开源中国
comments: false
date: Mon, 11 Oct 2021 07:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3342'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">OpenCV 4.5.4 现已发布。OpenCV 是 Intel 开源计算机视觉库，它实现了图像处理和计算机视觉方面的很多通用算法。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">此版本更新亮点包括：</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fwiki%2FGSoC_2021" target="_blank">GSoC 2021</a> 已经结束。11 个项目成功，大部分结果已经合并到 OpenCV tree 中并在 4.5.4 中可用（在主存储库或在 opencv_contrib 中）：</p> 
<ul> 
 <li>DNN 模块中的 8-bit 量化：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20228" target="_blank">#20228</a> + onnx importer <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20535" target="_blank">#20535</a></li> 
 <li>改进了 Julia 的 OpenCV 绑定：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv_contrib%2Fpull%2F3009" target="_blank">opencv_contib#3009</a></li> 
 <li>语音识别示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20291" target="_blank">#20291</a></li> 
 <li>为 RISC-V 优化 OpenCV DNN：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20287" target="_blank">#20287</a> + <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20521" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20287" target="_blank">20521</a></li> 
 <li>Universal Intrinsics 和 parallel_for_ 高效跨平台算法实现教程：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20361" target="_blank">#20361</a></li> 
</ul> 
<p><strong><span style="background-color:#ffffff; color:#24292f">DNN module<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpulls%3Fq%3Dis%253Apr%2Blabel%253A%2522category%253A%2Bdnn%2522%2Bmerged%253A2021-07-06..2021-10-10" target="_blank">patches</a>：</strong></p> 
<ul> 
 <li> <p><span>改进 </span><span style="background-color:#ffffff; color:#24292f">layers </span><span>/ </span><span style="background-color:#ffffff; color:#24292f">activations </span><span>/支持更多模型：</span></p> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20442" target="_blank">GRU</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20483" target="_blank">CumSum</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20466" target="_blank">Max</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20682" target="_blank">Min</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20702" target="_blank">ExpandDims</a></li> 
   <li>修复了带有不对称填充的卷积法</li> 
   <li>修复 Unsqueeze (ONNX opset 13)</li> 
   <li>修复了 OpenCL 内核中的几个内存访问问题</li> 
  </ul> </li> 
 <li> <p><span>为 TextRecognitionModel 实现 CTC prefix beam 搜索解码：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20524" target="_blank">#20524</a></span></p> </li> 
 <li> <p><span>添加 SoftNMS 实现：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20813" target="_blank">#20813</a></span></p> </li> 
 <li> <p><span>英特尔 Inference Engine backend (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsoftware.intel.com%2Fen-us%2Fopenvino-toolkit" target="_blank">OpenVINO</a>)：</span></p> 
  <ul> 
   <li>添加了对 OpenVINO 2021.4.1 LTS 版本的支持</li> 
   <li>添加了对具有 non-FP32 输出的模型或具有 1D 布局的输出的支持</li> 
  </ul> </li> 
</ul> 
<p><span>以及许多其他贡献：</span></p> 
<ul> 
 <li> <p><span>将基于 DNN 的人脸检测和人脸识别添加到 modules/objdetect 中：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20422" target="_blank">#20422</a></span></p> </li> 
 <li> <p><span>恢复 LineSegmentDetector (LSD) 实现</span></p> </li> 
 <li> <p><span>Python：在 numpy.ndarray 上引入<code>cv.Mat</code>wrapper 以处理将 3D 数组传递给 C++ 算法的问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fissues%2F19091" target="_blank">#19091</a></span></p> </li> 
 <li> <p><span>Python：支持带有纯 Python 模块的 OpenCV 扩展：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20611" target="_blank">#20611</a></span></p> </li> 
 <li> <p><span style="background-color:#ffffff; color:#24292f">Debugging</span><span>：为 cv::Mat 添加 gdb </span><span style="background-color:#ffffff; color:#24292f">pretty printer</span><span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20547" target="_blank">#20547</a></span></p> </li> 
 <li> <p><span>在 iOS 和 macOS 上为 Mat 添加 Quicklook：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F20457" target="_blank">#20457</a></span></p> </li> 
 <li> <p><span>添加生成新型 </span><span style="background-color:#ffffff; color:#24292f">radon checkerboard</span><span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fissues%2F20364" target="_blank">#20735</a></span></p> </li> 
</ul> 
<p> 更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fwiki%2FChangeLog" target="_blank">https://github.com/opencv/opencv/wiki/ChangeLog</a></p>
                                        </div>
                                      
</div>
            