
---
title: 'Khronos Group 已发布 OpenCL 3.0.12'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1998'
author: 开源中国
comments: false
date: Sat, 17 Sep 2022 08:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1998'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Khronos Group 发布了 OpenCL </span>3.0.12<span style="background-color:#ffffff; color:#333333">，这是最新的</span><span style="background-color:#ffffff; color:#121212">跨异构平台计算</span>标准，<span style="background-color:#ffffff; color:#333333">OpenCL 让显示芯片（GPL）也能为通用软件提供计算能力的标准，简单来说就是 GPU 可以帮忙干 CPU 的活儿。</span></p> 
<blockquote>
 OpenCL 全称 Open Computing Language，是第一个面向异构系统通用目的并行编程的开放式、免费标准，也是一个统一的编程环境，便于软件开发人员为高性能计算服务器、桌面计算系统、手持设备编写高效轻便的代码，而且广泛适用于多核心处理器 (CPU)、图形处理器 (GPU)、Cell 类型架构以及数字信号处理器 (DSP) 等其他并行处理器，在游戏、娱乐、科研、医疗等各种领域都有广阔的发展前景。
</blockquote> 
<p>OpenCL 3.0.12 中的更改为：</p> 
<ul> 
 <li>添加了有效对象的定义和测试有效对象的要求。</li> 
 <li>添加了内核支持的参数数量的最大限制。</li> 
 <li>明确了对象句柄的可比性和唯一性要求。</li> 
 <li>澄清了无效设备端入队“clk_event_t”句柄的行为。</li> 
 <li>澄清了 `cl_khr_command_buffer` 与其他扩展的交互。</li> 
 <li>指定命令缓冲区多次完成时的错误行为。</li> 
</ul> 
<p>值得注意的是引入了一个新的扩展“cl_khr_command_buffer_mutable_dispatch”，用于使用命令缓冲区进行可变调度。这是 OpenCL 3.0.12 中的新功能，以临时形式引入。该扩展允许在命令缓冲区队列之间修改内核执行命令的配置。</p> 
<p><span style="background-color:#ffffff; color:#121212">该扩展由 Codeplay、Qualcomm、Arm、英特尔、坦佩雷大学、NVIDIA 和 Google 的工程师开发，以克服 cl_khr_command_buffer 的限制：命令缓冲区中记录的命令在队列间不可变。</span></p> 
<blockquote>
 cl_khr_command_buffer 扩展通过提供一种记录一组命令的机制将命令构造与入队分开，然后这些命令可以重复入队。但是，记录到命令缓冲区的命令在队列之间是不可变的。 cl_khr_command_buffer_mutable_dispatch 消除了这个限制，尤其是，这个扩展允许修改命令缓冲区中的内核执行命令的配置，称为 mutable-dispatch。这允许内核的输入和输出，以及工作项的大小和偏移量，而无需在新的命令缓冲区中重新记录整个命令序列。
</blockquote> 
<p><span style="background-color:#ffffff; color:#121212">更多 OpenCL 3.0.12 文档</span>可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FOpenCL-Docs%2Freleases%2Ftag%2Fv3.0.12" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            