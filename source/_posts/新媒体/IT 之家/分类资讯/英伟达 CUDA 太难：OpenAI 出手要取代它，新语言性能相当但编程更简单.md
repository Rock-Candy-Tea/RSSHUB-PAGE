
---
title: '英伟达 CUDA 太难：OpenAI 出手要取代它，新语言性能相当但编程更简单'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/7/61d2bfb9-3234-4bae-8549-e725b793cc4f.png'
author: IT 之家
comments: false
date: Thu, 29 Jul 2021 07:58:11 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/7/61d2bfb9-3234-4bae-8549-e725b793cc4f.png'
---

<div>   
<p>用 CUDA 为 GPU 编程实在太难了。</p><p>为了让没有 CUDA 编程经验的人写出和专家效率相当的 GPU 代码，现在 OpenAI 推出了一种新的语言和编译器 ——Triton。</p><p>它的难度比 CUDA 低，但是性能却可与之相媲美。</p><p>OpenAI 声称：</p><blockquote><p>Triton 只要 25 行代码，就能在 FP16 矩阵乘法 shang 上达到与 cuBLAS 相当的性能。</p></blockquote><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/61d2bfb9-3234-4bae-8549-e725b793cc4f.png" w="640" h="728" title="英伟达 CUDA 太难：OpenAI 出手要取代它，新语言性能相当但编程更简单" width="640" height="728" referrerpolicy="no-referrer"></p><p>OpenAI 的研究人员已经使用 Triton，来生成比同等 Torch 效率高出 1 倍的内核。</p><p>Triton 项目的负责人 Philippe Tillet 说：“我们的目标是使 Triton 成为深度学习 CUDA 的可行替代方案。”</p><h2>25 行代码实现最佳性能</h2><p>Triton 起源于 Tillet 在 2019 年学术会议 MLPF 上的一篇论文，当时他还是哈佛大学的一名研究生。</p><p>Tillet 解决的问题是如何开发一种 cuDNN 更具表现力的语言，既能够处理神经网络中涉及的矩阵的各种操作，同时兼具可移植性且以及和 cuDNN 相媲美的性能。</p><p>现代 GPU 大致分为三个主要组件 ——DRAM、SRAM、ALU，对这些资源进行调度管理十分复杂，即便是熟悉 CUDA 的程序员。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/a17d1293-a36b-4e5f-a3f7-9178734f1a0d.png" w="796" h="254" title="英伟达 CUDA 太难：OpenAI 出手要取代它，新语言性能相当但编程更简单" width="796" height="254" referrerpolicy="no-referrer"></p><p>Triton 可以将这些优化过程完全自动化，让开发者可以更好地专注于并行代码的高级逻辑。</p><p>以矩阵乘法为例，能够为逐元素运算和归约编写融合内核很重要，但考虑到神经网络中矩阵乘法任务的重要性，这还不够。</p><p>Triton 非常适合这些应用，只需约 25 行 Python 代码即可实现最佳性能。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/299eed38-af1e-4b61-843a-f838dbe44cf2.png" w="661" h="742" title="英伟达 CUDA 太难：OpenAI 出手要取代它，新语言性能相当但编程更简单" width="661" height="742" referrerpolicy="no-referrer"></p><p>而另一方面，在 CUDA 中实现类似的过程需要花费更多的精力，甚至可能会降低性能。</p><p>手写矩阵乘法内核的一个重要优点是它们可以根据需要进行定制，以适应其输入和输出的融合变换。</p><p>如果没有 Triton，对于没有特殊 GPU 编程经验的开发者来说，矩阵乘法内核的修改是非常困难的。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/7d71087e-8af1-455a-8f1e-8c16dcbcdb9a.png" w="1080" h="659" title="英伟达 CUDA 太难：OpenAI 出手要取代它，新语言性能相当但编程更简单" width="1080" height="500" referrerpolicy="no-referrer"></p><h2>Triton 背后的原理</h2><p>Triton 的良好性能，来自于以 Triton-IR 为中心的模块化系统架构，这是一种基于 LLVM 的中间表示。</p><p>@triton.jit decorator 通过遍历提供 Python 函数的抽象语法树（AST），产生的 Triton-IR 使用通用 SSA 构建算法上的动态。</p><p>生成的 IR 代码随后由编译器后端进行简化、优化和自动并行化，然后转换为高质量的 LLVM-IR（最终转换为 PTX）。</p><p>研究人员发现，数据可以通过查看计算密集型块级操作（例如 tl.dot）的操作数自动存储到共享内存中，并使用标准活性分析技术进行分配/同步。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/90af2da8-0485-4d96-989a-d7a87ba6e7ed.png" w="1080" h="373" title="英伟达 CUDA 太难：OpenAI 出手要取代它，新语言性能相当但编程更简单" width="1080" height="283" referrerpolicy="no-referrer"></p><p>另一方面，Triton 程序可以通过同时执行不同的内核实例跨 SM 进行高效和自动并行化，以及通过分析每个块级操作的迭代空间，并在不同的 SIMD 中进行充分分区将 SM 内单元并行化。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/26f432b4-88d4-47c8-86a3-7ae3d662a4cd.png" w="1080" h="441" title="英伟达 CUDA 太难：OpenAI 出手要取代它，新语言性能相当但编程更简单" width="1080" height="335" referrerpolicy="no-referrer"></p><p>目前 Triton 仅适用于英伟达 GPU，但官方表示 AMD GPU 以及 CPU 的版本正在开发中。</p><p>开源地址：</p><p>https://github.com/openai/triton</p><p>论文：</p><p>https://dl.acm.org/doi/abs/10.1145/3315508.3329973</p>
          
</div>
            