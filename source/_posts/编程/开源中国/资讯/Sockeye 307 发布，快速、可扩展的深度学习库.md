
---
title: 'Sockeye 3.0.7 发布，快速、可扩展的深度学习库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1523'
author: 开源中国
comments: false
date: Tue, 21 Dec 2021 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1523'
---

<div>   
<div class="content">
                                                                                            <p data-darkreader-inline-color style="--darkreader-inline-color:#d8d4cf; color:#e8e6e3; margin-left:0px; margin-right:0px; text-align:start"><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333">Sockeye 是一个基于 </span><a href="https://www.oschina.net/p/mxnet">Apache MXNet</a><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333"> 的快速而可扩展的深度学习库。Sockeye 代码库具有来自 MXNet 的独特优势。例如，通过符号式和命令式 MXNet API，Sockeye 结合了陈述式和命令式编程风格；可以在多块 GPU 上并行训练模型。</span></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d8d4cf; color:#e8e6e3; margin-left:0px; margin-right:0px; text-align:start"><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333">目前 Sockeye 更新到 3.0.7 版本，改进了训练速度，内容如下：</span></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>[3.0.7]</strong></h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d8d4cf; color:#e8e6e3; margin-left:0px; margin-right:0px; text-align:start">在训练期间使用<span> </span><code>torch.nn.functional.multi_head_attention_forward</code><span> </span>的自注意力和编码器注意力来提高训练速度。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d8d4cf; color:#e8e6e3; margin-left:0px; margin-right:0px; text-align:start">需要重新组织键值输入投影的参数布局，因为当前的 Sockeye 注意力会交错以进行更快的推理。注意掩码（源掩码和自回归掩码都需要一些形状调整，因为对融合 MHA 操作的要求略有不同）。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>联合键值输入投影参数的非交错格式：<br> <code>in_features=hidden, out_features=2*hidden -> Shape: (2*hidden, hidden)</code></li> 
 <li>联合键值输入投影的交错格式存储键和值参数，按头部分组：<br> <code>Shape: ((num_heads * 2 * hidden_per_head), hidden)</code></li> 
 <li>模型以交错格式保存和加载键值投影参数。</li> 
 <li>当<span> </span><code>model.training == True</code><span> </span>键值投影参数被放入非交错格式时<code>torch.nn.functional.multi_head_attention_forward</code></li> 
 <li>当<span> </span><code>model.training == False</code>，即 model.eval() 被调用时，键值投影参数再次转换为交错格式。</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>[3.0.6]</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复了阻止使用<code>bleu</code>as<code>--optimized-metric</code>进行分布式训练的检查点解码器问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fawslabs%2Fsockeye%2Fissues%2F995" target="_blank">#995</a>）</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>[3.0.5]</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复了多语言教程中的数据下载。</li> 
</ul> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d8d4cf; color:#e8e6e3; margin-left:0px; margin-right:0px; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fawslabs%2Fsockeye%2Freleases%2Ftag%2F3.0.7" target="_blank">https://github.com/awslabs/sockeye/releases/tag/3.0.7</a></p>
                                        </div>
                                      
</div>
            