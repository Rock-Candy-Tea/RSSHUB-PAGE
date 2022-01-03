
---
title: '谷歌推出全能扒谱AI：只要听一遍歌曲 钢琴小提琴的乐谱全有了'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0103/86a17f283f09fa9.png'
author: cnBeta
comments: false
date: Mon, 03 Jan 2022 06:13:27 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0103/86a17f283f09fa9.png'
---

<div>   
听一遍曲子，就能知道乐谱，还能马上演奏，而且还掌握“十八般乐器”，钢琴、小提琴、吉他等都不在话下。这就不是人类音乐大师，而是谷歌推出的“多任务多音轨”音乐转音符模型 MT3。<br>
 <p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0103/86a17f283f09fa9.png"><img data-original="https://static.cnbetacdn.com/article/2022/0103/86a17f283f09fa9.png" src="https://static.cnbetacdn.com/thumb/article/2022/0103/86a17f283f09fa9.png" referrerpolicy="no-referrer"></a></p><p>首先需要解释一下什么是多任务多音轨。通常一首曲子是有多种乐器合奏而来，每个乐曲就是一个音轨，而多任务就是同时将不同音轨的乐谱同时还原出来。</p><p>事实上，谷歌 MT3 在还原多音轨乐谱这件事上，达到了 SOTA 的结果。谷歌已将该论文投给 ICLR 2022。</p><p>还原多音轨乐谱</p><p>相比与自动语音识别 (ASR) ，自动音乐转录 (AMT) 的难度要大得多，因为后者既要同时转录多个乐器，还要保留精细的音高和时间信息。</p><p>多音轨的自动音乐转录数据集更是“低资源”的。现有的开源音乐转录数据集一般只包含一到几百小时的音频，相比语音数据集动辄几千上万小时的市场，算是很少了。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0103/5f61321a539dee3.png"><img data-original="https://static.cnbetacdn.com/article/2022/0103/5f61321a539dee3.png" src="https://static.cnbetacdn.com/thumb/article/2022/0103/5f61321a539dee3.png" referrerpolicy="no-referrer"></a></p><p>先前的音乐转录主要集中在特定于任务的架构上，针对每个任务的各种乐器量身定制。因此，作者受到低资源 NLP 任务迁移学习的启发，证明了通用 Transformer 模型可以执行多任务 AMT，并显著提高了低资源乐器的性能。作者使用单一的通用 Transformer 架构 T5，而且是 T5“小”模型，其中包含大约 6000 万个参数。</p><p>该模型在编码器和解码器中使用了一系列标准的 Transformer 自注意力“块”。为了产生输出标记序列，该模型使用贪婪自回归解码：输入一个输入序列，将预测出下一个出现概率最高的输出标记附加到该序列中，并重复该过程直到结束。</p><p>MT3 使用梅尔频谱图作为输入。对于输出，作者构建了一个受 MIDI 规范启发的 token 词汇，称为“类 MIDI”。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0103/da17730880f4ac4.png"><img data-original="https://static.cnbetacdn.com/article/2022/0103/da17730880f4ac4.png" src="https://static.cnbetacdn.com/thumb/article/2022/0103/da17730880f4ac4.png" referrerpolicy="no-referrer"></a></p><p>生成的乐谱通过开源软件 FluidSynth 渲染成音频。此外，还要解决不同乐曲数据集不平衡和架构不同问题。</p><p>作者定义的通用输出 token 还允许模型同时在多个数据集的混合上进行训练，类似于用多语言翻译模型同时训练几种语言。这种方法不仅简化了模型设计和训练，而且增加了模型可用训练数据的数量和多样性。</p><p>实际效果</p><p>在所有指标和所有数据集上，MT3 始终优于基线。训练期间的数据集混合，相比单个数据集训练有很大的性能提升，特别是对于 GuitarSet、MusicNet 和 URMP 等“低资源”数据集。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0103/7c3f5e0aa14e85f.png"><img data-original="https://static.cnbetacdn.com/article/2022/0103/7c3f5e0aa14e85f.png" src="https://static.cnbetacdn.com/thumb/article/2022/0103/7c3f5e0aa14e85f.png" referrerpolicy="no-referrer"></a></p><p>最近，谷歌团队也放出了 MT3 的源代码，并在 Hugging Face 上放出了试玩 Demo。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0103/c1896007cc2a840.png"><img data-original="https://static.cnbetacdn.com/article/2022/0103/c1896007cc2a840.png" src="https://static.cnbetacdn.com/thumb/article/2022/0103/c1896007cc2a840.png" referrerpolicy="no-referrer"></a></p><p>不过由于转换音频需要 GPU 资源，在 Hugging Face 上，建议各位将在 Colab 上运行 Jupyter Notebook。</p><p>论文地址：</p><p>https://arxiv.org/abs/2111.03017</p><p>源代码：</p><p>https://github.com/magenta/mt3</p><p>Demo 地址：</p><p>https://huggingface.co/spaces/akhaliq/MT3</p>   
</div>
            