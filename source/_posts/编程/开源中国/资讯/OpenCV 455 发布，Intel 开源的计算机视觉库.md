
---
title: 'OpenCV 4.5.5 发布，Intel 开源的计算机视觉库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=533'
author: 开源中国
comments: false
date: Mon, 27 Dec 2021 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=533'
---

<div>   
<div class="content">
                                                                                            <p>OpenCV 是 Intel 开源计算机视觉库，它实现了图像处理和计算机视觉方面的很多通用算法。OpenCV 4.5.5 版本的更新内容如下：</p> 
<ul> 
 <li>作为 VideoCapture API 的一部分，新增音频支持：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F19721" target="_blank">MSMF #19721</a> + <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F21264" target="_blank">GStreamer #21264</a></li> 
 <li>更新了 SOVERSION 处理规则: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F21178" target="_blank">#21178</a></li> 
 <li>DNN 模块补丁： 
  <ul> 
   <li>增加了测试，以涵盖 ONNX 一致性测试套件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fpull%2F21088" target="_blank">#21088</a></li> 
   <li>将内置的 protobuf 从 3.5.2 升级到 3.19.1</li> 
   <li>对 RISC-V 平台进行了更多优化</li> 
   <li>英特尔 OpenVINO 
    <ul> 
     <li>增加了对 OpenVINO 2021.4.2 LTS 版本的支持</li> 
    </ul> </li> 
  </ul> </li> 
 <li>G-API 模块 
  <ul> 
   <li>G-API 框架： 
    <ul> 
     <li>修正了从 <code>cv::Rmat</code> 访问 1D 数据的问题</li> 
     <li>限制将 G-API 类型传递给图形输入/输出以供执行</li> 
     <li>重新命名各种内部结构以保持一致性</li> 
    </ul> </li> 
   <li>Fluid backend: 
    <ul> 
     <li>引入了一个更好的 Resize 矢量版本</li> 
     <li>增加了矢量版的 Multiply 内核</li> 
     <li>添加矢量版的 Divide 内核</li> 
     <li>添加了矢量版的 AddC 内核</li> 
     <li>添加了矢量版的 SubC 内核</li> 
     <li>添加了矢量版的 MulC 内核</li> 
     <li>添加了矢量版的 SubRC 内核</li> 
     <li>启用了 AbsDiffC 的 SIMD 调度功能</li> 
    </ul> </li> 
   <li>其他变化和修正： 
    <ul> 
     <li>为 OpenVINO 2021.4 版本修正了各种静态分析问题</li> 
     <li>修正了 OpenVINO 更新后引入的各种构建警告</li> 
     <li>在 G-API 测试套件中继续清理了 GTest 宏和测试数据</li> 
     <li>为 Fluid 性能测试添加了自定义精度比较函数</li> 
    </ul> </li> 
   <li>……</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fwiki%2FChangeLog%23version455" target="_blank">https://github.com/opencv/opencv/wiki/ChangeLog#version455</a></p>
                                        </div>
                                      
</div>
            