
---
title: '深度学习框架 PyTorch 发布 1.11  版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6308'
author: 开源中国
comments: false
date: Thu, 17 Mar 2022 07:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6308'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Python 著名 AI 框架 PyTorch 1.11 已发布。此版本由自 1.10 以来的 3300 多个提交组成， TorchData 和 functorch 的 beta 版本亦伴随发布。</p> 
<p>版本概括：</p> 
<ul> 
 <li><strong>TorchData </strong>是一个用于通用模块化数据加载原语的新库，用于轻松构建灵活和高性能的数据管道。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fdata" target="_blank">在 GitHub 上查看</a>。</li> 
 <li><strong>functorch </strong>是一个将可组合函数转换添加到 PyTorch 的库，现已推出 beta 版。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Ffunctorch" target="_blank">在 GitHub 上查看</a>。</li> 
 <li>分布式数据并行 (DDP) 静态图优化稳定可用。</li> 
</ul> 
<h3><strong>TorchData</strong> 介绍 </h3> 
<p><strong>TorchData </strong>是一个通用模块化数据加载原语库，用于轻松构建灵活且高性能的数据管道。现有的 DataLoader 将太多的功能捆绑在一起，难以扩展,此外，不同的用例通常必须一遍又一遍地重写相同的数据加载实用程序。<strong>TorchData </strong>的目标是通过称为“ DataPipes ”的 Iterable 样式和 Map 样式的构建块启用可组合的数据加载，这些构建块与 PyTorch 的 DataLoader 开箱即用。</p> 
<p>目前已经实现了 50 多个提供不同核心功能的 DataPipes，例如打开文件、解析文本、转换样本、缓存、混洗和批处理。在此版本中，一些 PyTorch 域库已迁移其数据集以使用 DataPipes。在 TorchText 中，库提供的流行数据集是使用 DataPipes 实现的，其 SST-2 二进制文本分类教程的一部分演示了如何使用 DataPipes 为模型预处理数据。</p> 
<p>TorchData 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Fdata" target="_blank">文档</a>现已上线，包含介绍<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Fdata%2F0.3.0%2Ftutorial.html%23using-datapipes" target="_blank">如何使用 DataPipes</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Fdata%2F0.3.0%2Ftutorial.html%23working-with-dataloader" target="_blank">将它们与 DataLoader 一起使用</a>以及<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Fdata%2F0.3.0%2Ftutorial.html%23implementing-a-custom-datapipe" target="_blank">实现自定义</a>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fdata%23readme" target="_blank">项目的 README 文件</a>中描述了与 DataLoader 相关的常见问题解答和未来计划。</p> 
<h3><strong>functorch </strong>介绍 </h3> 
<p>受Google JAX 的极大启发，functorch 是一个向 PyTorch 添加可组合函数转换的库。它旨在提供可组合的 vmap（矢量化）和 autodiff 转换，可与 PyTorch 模块和 PyTorch autograd 一起使用，并具有良好的渴望模式性能。</p> 
<p>可组合的函数转换可以帮助解决当今在 PyTorch 中难以实现的许多用例：</p> 
<ul> 
 <li>计算每样本梯度（或其他每样本数量）</li> 
 <li>在单台机器上运行模型集合</li> 
 <li>在 MAML 的内循环中有效地将任务批处理在一起</li> 
 <li>有效地计算雅可比矩阵和黑森矩阵以及批量矩阵</li> 
</ul> 
<p>组合 vmap（矢量化）、vjp（反向模式 AD）和 jvp（正向模式 AD）转换能够轻松地表达上述内容，而无需为每个转换设计单独的库。有关 functorch 的详细信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Ffunctorch%2F" target="_blank">文档</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Ffunctorch" target="_blank">教程</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Ffunctorch%2Fstable%2Finstall.html" target="_blank">安装说明</a>。</p> 
<h2>分布式训练</h2> 
<h3>（稳定）DDP 静态图</h3> 
<p>DDP 静态图假设您的模型在每次迭代中都使用相同的一组已使用/未使用的参数，因此它可以确定性地了解状态，例如哪些 hooks 将触发、hooks 将触发多少次以及第一次迭代后的梯度计算就绪顺序。</p> 
<p>静态图在第一次迭代中缓存了这些状态，因此它可以支持 DDP 在以前的版本中无法支持的功能，例如，支持在相同参数上的多个激活检查点，无论是否有未使用的参数。当存在未使用的参数时，静态图功能还应用性能优化，例如，它避免遍历图以在每次迭代中搜索未使用的参数，并启用动态分桶顺序。</p> 
<p>DDP 静态图中的这些优化为一些推荐模型带来了 10% 的 QPS 增益。</p> 
<p>要启用静态图，只需在 DDP API 中设置 <code>static_graph=True</code> ，如下所示：</p> 
<pre>ddp_model = DistributedDataParallel(model, static_graph=True)</pre> 
<p>有关更多详细信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Fdocs%2Fmaster%2Fgenerated%2Ftorch.nn.parallel.DistributedDataParallel.html" target="_blank">文档</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Ftutorials%2Fintermediate%2Fddp_tutorial.html" target="_blank">教程</a>。</p> 
<p> </p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Fblog%2Fpytorch-1.11-released%2F" target="_blank">https://pytorch.org/blog/pytorch-1.11-released/</a></p>
                                        </div>
                                      
</div>
            