
---
title: '哥伦比亚大学提出可阻止间谍麦克风监听的神经语音伪装AI算法'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0420/48d4b55ffb644c9.jpg'
author: cnBeta
comments: false
date: Wed, 20 Apr 2022 08:00:04 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0420/48d4b55ffb644c9.jpg'
---

<div>   
早在 2013 年，就有报道称 FBI 有利用特殊的技术手段来监听麦克风。<strong>几周前，威斯康星大学麦迪逊分校又在一份调查报告中，揭示了静音麦克风是如何在视频会议期间被清楚收听到的。</strong>虽然结果有点让人感到惊讶，但其实耳机也可在特定情况下被当做麦克风来监听。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0420/48d4b55ffb644c9.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0420/48d4b55ffb644c9.jpg" alt="0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">资料图（来自：<a href="https://news.wisc.edu/youre-muted-or-are-you-videoconferencing-apps-may-listen-even-when-mic-is-off/" target="_self">University of Wisconsin-Madison</a>）</p><p>出于对隐私安全的关注，我们已见到一些突破性的技术。比如得益于新开发的一种算法，哥伦比亚大学研究人员声称可部分解决这方面的问题。</p><p>据悉，新算法主要聚焦两个方面。首先，它会将一个人的语音模糊和安静到接近耳语可听的水平，以避免被自动语音识别（ASR）AI 给破译。</p><p>其次，新算法还可预测即将说出的单词、并始终较 ASR 领先一步，所以新方法又被称作“预测性攻击”（Predicitive Attacks）。</p><p><a href="https://static.cnbetacdn.com/article/2022/0420/03e74f13820de5e.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0420/03e74f13820de5e.png" alt="639de4f7fccf4f4fe148b875e5a7305f1Y21TORf9xOKFP2D-0.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">研究配图 - 1：“神经语音伪装”可对 ASR 造成干扰</p><p>该校计算机科学助理教授 Carl Vondrick 简要解释了该技术的<a href="https://www.engineering.columbia.edu/news/block-smartphone-microphone-speech-recognition-spying" target="_self">工作原理</a>：</p><blockquote><p>在阻止麦克风恶意监听这件事上，我们的算法有 80% 的成效，同时也是测试平台上最快、最准确的算法。</p><p>即使我们对流氓麦克风一无所知 —— 比如它的位置、甚至背后运行的计算机软件 —— 该方法依然能够奏效。</p><p>本质上，我们可以通过无线的方式来伪装一个人的声音，将其隐藏在这些监听系统之外、且不会对在室内会话的人们造成不便。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0420/f278d9b32e274a2.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0420/f278d9b32e274a2.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">研究配图 - 2：预测攻击演示</p><p>研究的主要作者、Vondrick 的博士生 Mia Chiquier 进一步补充道：</p><blockquote><p>我们的算法能够通过预测一个人接下来会说什么的特征来跟上进度，给它足够的时间来生成正确的耳语。</p><p>到目前为止，该方法已被证明适用于大多数英语词汇。后续我们计划将该算法推广到覆盖更多语种，最终让耳语听起来完全不可察觉。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0420/96dbe0e5162c68e.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0420/96dbe0e5162c68e.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">研究配图 - 3：三个攻击实例</p><p>通过与其它用于攻击语音样本的方法进行比较 —— 包括统一噪声、离线投影梯度下降（PGD）和在线 PGD（实时）—— 可知该算法在预测未来 0.5 秒的讲述内容时表现最佳。</p><p>此外该算法针对标准 ASR 及其强大的对手展开了实测，虽然不见得很快就能派上实际用场，但感兴趣的朋友还是可以翻阅《实时神经语音伪装》这项基础研究的全文（<a href="https://arxiv.org/pdf/2112.07076.pdf" target="_self">PDF</a>）。</p>   
</div>
            