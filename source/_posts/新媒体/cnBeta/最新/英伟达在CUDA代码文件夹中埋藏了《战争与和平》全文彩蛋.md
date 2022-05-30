
---
title: '英伟达在CUDA代码文件夹中埋藏了《战争与和平》全文彩蛋'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0530/4849f31b768967e.png'
author: cnBeta
comments: false
date: Mon, 30 May 2022 06:47:12 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0530/4849f31b768967e.png'
---

<div>   
<strong>Reddit 网友 CHDuckie 在 NVIDIA 子版块上发帖称，其在硬盘上的英伟达 CUDA 文件夹中发现了一个不同寻常的“大文件”。</strong>与其它一众 10 KB 不到的代码相比，该文档的体积竟然高达 3212 KB 。当时 CHDuckie 正在检索自己的硬盘驱动器，结果意外发现了这个包含《战争与和平》全文的 txt 文档“彩蛋”。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0530/4849f31b768967e.png" alt="0.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图 via <a href="https://wccftech.com/famous-tolstoy-literature-finds-use-in-nvidia-cuda-and-not-just-as-an-easter-egg/" target="_self">WCCFTech</a>）</p><p>出于好奇，他用 VS Code 打开了该文件。毕竟对于常规的记事本（notepad.exe）应用程序来说，该 txt 文档的体型着实大得有些离谱。</p><p>结果在这个包含 65340 行的文档中，首先映入眼帘的就是 —— 列夫·托尔斯泰的古腾堡计划，《战争与和平》电子书。</p><p><img src="https://static.cnbetacdn.com/article/2022/0530/6f24db3c868ede1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>尽管让人感到有些疑惑，还是有网友给出了相对合理的解释。据悉，作为计算平台和编程模型的 NVIDIA CUDA，开发者可在该公司的 GPU 上开展一系列通用加速计算。</p><p>然后 Jlouis8 在评论中贴出了 GitHub 上的一个代码示例（<a href="https://github.com/NVIDIA/cuda-samples/blob/master/Samples/0_Introduction/c%2B%2B11_cuda/c%2B%2B11_cuda.cu#L97" target="_self">传送门</a>），演示了如何通过创建一个小型的 CUDA 内核，以计算某些数据（比如《战争与和平》电子书）中，w、x、y 和 z 的字母数量。</p><p><img src="https://static.cnbetacdn.com/article/2022/0530/aba90f413df4e69.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>之所以选择这本电子书，其原因也不难理解。首先，NVIDIA 可在不侵犯版权的情况下自由包含；其次，原始文本量足够庞大、但又足够在 CUDA（GPU）硬件上快速完成。</p>   
</div>
            