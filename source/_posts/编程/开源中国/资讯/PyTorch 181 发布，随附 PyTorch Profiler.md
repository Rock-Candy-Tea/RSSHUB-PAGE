
---
title: 'PyTorch 1.8.1 发布，随附 PyTorch Profiler'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4994'
author: 开源中国
comments: false
date: Tue, 30 Mar 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4994'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PyTorch 1.8.1 现已发布，这是一个小的错误修复版本。具体更新内容如下：</p> 
<p><strong>New Features</strong></p> 
<ul> 
 <li>改造 torch.profiler 中的 profiling tools。torch.profiler 子模块现在可用，它利用了新发布的 kineto 库进行性能分析。详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Fblog%2Fintroducing-pytorch-profiler-the-new-and-improved-performance-tool%2F" target="_blank">博客</a>。</li> 
 <li>为 pytorch xla 启用 autocast（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F48570" target="_blank">＃48570</a>）。该<code>torch.cuda.autocast</code>软件包现在可以与 torch xla 一起使用，以提供简单的混合精度训练。</li> 
</ul> 
<p><strong>Improvements</strong></p> 
<ul> 
 <li>使<code>torch.</code>子模块导入更易于自动完成（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F52339" target="_blank">＃52339</a>）</li> 
 <li>在 ONNX 中添加对<code>torch.&#123;isinf,any,all&#125;</code>的支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F53529" target="_blank">＃53529</a>）</li> 
 <li>在<code>torch.randperm</code>的 GPU 实现中将 thrust 替换为 cub，以高提性能（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F54537" target="_blank">＃54537</a>）</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<p>Misc</p> 
<ul> 
 <li>修复<code>torch.distributions</code>验证检查（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F53763" target="_blank">＃53763</a>）</li> 
 <li>允许更改<code>nn.Embedding</code>的 padding 向量（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F53447" target="_blank">＃53447</a>）</li> 
 <li>在 TorchScript 中正确 de-sugar Ellipsis（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F53766" target="_blank">＃53766</a>）</li> 
 <li>当组数为 24 的倍数时，停止使用 OneDNN 进行分组卷积（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F54015" target="_blank">＃54015</a>）</li> 
 <li>在 &#123;load,store&#125;_scalar 中使用 int8_t 代替 char（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F52616" target="_blank">＃52616</a>）</li> 
 <li>制作 ideep honor torch.set_num_thread（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F53871" target="_blank">＃53871</a>）</li> 
 <li>修复<code>pixel_&#123;un&#125;shuffle</code>中尺寸超出范围的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F54178" target="_blank">＃54178</a>）</li> 
 <li>更新 kineto 以修复 libtorch 构建（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F54205" target="_blank">＃54205</a>）</li> 
 <li>修复分布式 autograd CUDA 流同步的发送/接收操作（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F54358" target="_blank">＃54358</a>）</li> 
</ul> 
<p>ONNX</p> 
<ul> 
 <li>更新 ONNX 中的错误处理以避免<code>ValueError</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F53548" target="_blank">＃53548</a>）</li> 
 <li>更新嵌套结构和 dict 输出的 assign output shape（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F53311" target="_blank">＃53311</a>）</li> 
 <li>更新 embedding export wrt padding_idx（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F53931" target="_blank">＃53931</a>）</li> 
</ul> 
<p><strong>Documentation</strong></p> 
<ul> 
 <li><code>torch.fx</code>的文档更新（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F53674" target="_blank">＃53674</a>）</li> 
 <li>修复<code>distributed.rpc.options.TensorPipeRpcBackendOptions.set_device_map</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F53508" target="_blank">＃53508</a>）</li> 
 <li><code>nn.LSTMCell</code>的更新示例（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F51983" target="_blank">＃51983</a>）</li> 
 <li>更新<code>nn.Embedding</code>的<code>padding_idx</code>参数文档（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F53809" target="_blank">＃53809</a>）</li> 
 <li>更新通用文档模板（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fpull%2F54141" target="_blank">＃54141</a>）</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Freleases%2Ftag%2Fv1.8.1" target="_blank">https://github.com/pytorch/pytorch/releases/tag/v1.8.1</a></p>
                                        </div>
                                      
</div>
            