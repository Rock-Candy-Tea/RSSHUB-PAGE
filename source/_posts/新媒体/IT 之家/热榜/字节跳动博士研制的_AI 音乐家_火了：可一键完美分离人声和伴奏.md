
---
title: '字节跳动博士研制的_AI 音乐家_火了：可一键完美分离人声和伴奏'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/9/a03d88b2-333a-46d3-9b68-8c0f2456e768.png'
author: IT 之家
comments: false
date: Sun, 19 Sep 2021 05:47:28 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/9/a03d88b2-333a-46d3-9b68-8c0f2456e768.png'
---

<div>   
<p data-vmark="95a5">AI 可以写歌、填词、改换风格、续写音乐。今天，<span class="accentTextColor">AI 又来做编曲人了</span>。</p><p data-vmark="0da7">上传一段《Stay》，一键按下，<span class="accentTextColor">伴奏和人声就轻松分离</span>。</p><p data-vmark="c09c"><img src="https://img.ithome.com/newsuploadfiles/2021/9/a03d88b2-333a-46d3-9b68-8c0f2456e768.png" w="1080" h="407" title="字节跳动博士研制的“AI 音乐家”火了：可一键完美分离人声和伴奏" width="1080" height="309" referrerpolicy="no-referrer"></p><p data-vmark="6098">人声颇有种在空旷地带清唱的清晰感，背景乐都能直接拿去做混剪了！</p><p data-vmark="b2c5">这样惊人的效果也引发了 Reddit 热议。</p><p data-vmark="20a7"><img src="https://img.ithome.com/newsuploadfiles/2021/9/f71be552-38ba-4449-8ed2-b2a334d747f1.png" w="1080" h="168" alt="图片" title="字节跳动博士研制的“AI 音乐家”火了：可一键完美分离人声和伴奏" width="1080" height="128" referrerpolicy="no-referrer"></p><p data-vmark="6cf1">这项研究的主要负责人孔秋强来自字节跳动，全球最大的古典钢琴数据集 GiantMIDI-Piano，也是由他在去年牵头发布的。</p><p data-vmark="6548">那么今天，他又带来了怎样的一个 AI 音乐家呢？</p><p data-vmark="0967">一起来看看。</p><h2>基于深度残差网络的音源分离</h2><p data-vmark="f328">这是一个包含了相位估计的音乐源分离（MSS）系统。</p><p data-vmark="3445">首先，将幅值（Magnitude）与相位（Phase）解耦，用以估计复数理想比例掩码（cIRM）。</p><p data-vmark="140f">其次，为了实现更灵活的幅值估计，将有界掩码估计和直接幅值预测结合起来。</p><p data-vmark="8ee4">最后，为 MSS 系统引入一个 143 层的深度残差网络（Deep Residual UNets），利用残差编码块（REB）和残差解码块（RDB）来增加其深度：</p><p data-vmark="dfbe"><img src="https://img.ithome.com/newsuploadfiles/2021/9/369e8eb6-605e-47c8-b4ec-1211b90f1369.png" w="590" h="1050" title="字节跳动博士研制的“AI 音乐家”火了：可一键完美分离人声和伴奏" width="590" height="1050" referrerpolicy="no-referrer"></p><p data-vmark="c46c">残差编码块和残差卷积块中间还引入了中间卷积块（ICB），以提高残差网络的表达能力。</p><p data-vmark="dcd5">其中每个残差编码块由 4 个残差卷积块（RCB）组成，残差卷积块又由两个核大小为 3×3 的卷积层组成。</p><p data-vmark="35c1">每个残差解码块由 8 个卷积层和 1 个反卷积层组成。</p><p data-vmark="aa3f"><img src="https://img.ithome.com/newsuploadfiles/2021/9/0267e5ea-efba-47d2-a772-8ac2d8659e8a.png" w="630" h="282" alt="图片" title="字节跳动博士研制的“AI 音乐家”火了：可一键完美分离人声和伴奏" width="630" height="282" referrerpolicy="no-referrer"></p><h2>实验结果</h2><p data-vmark="27dd">接下来，将这一系统在 MUSDB18 数据集上进行实验。</p><p data-vmark="4210">MUSDB18 中的训练/验证集分别包含 100/50 个完整的立体声音轨，包括独立的人声、伴奏、低音、鼓和其他乐器。</p><p data-vmark="90b6">在训练时，利用上述系统进行并行的混合音频数据增强，随机混合来自同一来源的两个 3 秒片段，然后作为一个新的 3 秒片段进行训练。</p><p data-vmark="f063">以信号失真率（SDR）作为评判标准，可以看到 <span class="accentTextColor">ResUNetDecouple 系统在分离人声、低音、其他和伴奏方面明显优于以前的方法</span>：</p><p data-vmark="5cc0">在消融实验中，143 层残差网络的表现也证实了，结合有界掩码估计和直接幅值预测确实能够改善声音源分离系统的性能。</p><p data-vmark="284a"><img src="https://img.ithome.com/newsuploadfiles/2021/9/d1474d6e-2171-4273-be6e-741bcbcbcb9f.png" w="634" h="368" title="字节跳动博士研制的“AI 音乐家”火了：可一键完美分离人声和伴奏" width="634" height="368" referrerpolicy="no-referrer"></p><h2>作者介绍</h2><p data-vmark="a2e8">这项研究的论文一作为孔秋强，本硕都毕业于华南理工大学，博士则毕业于英国萨里大学的电子信息工程专业。</p><p data-vmark="4f44">他在 2019 年加入字节跳动的 Speech, Audio and Music Intelligence 研究小组，<span class="accentTextColor">主要负责音频信号处理和声音事件检测等领域的研究</span>。</p><p data-vmark="d56e"><img src="https://img.ithome.com/newsuploadfiles/2021/9/26c263a8-415f-4000-b47a-2594858b88a4.png" w="400" h="400" title="字节跳动博士研制的“AI 音乐家”火了：可一键完美分离人声和伴奏" width="400" height="400" referrerpolicy="no-referrer"></p>
          
</div>
            