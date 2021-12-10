
---
title: '微软开发可高效揪出代码错误的BugLabs人工智能解决方案'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1210/111f04906cce62b.gif'
author: cnBeta
comments: false
date: Fri, 10 Dec 2021 06:08:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1210/111f04906cce62b.gif'
---

<div>   
<strong>微软研究院首席研究员 Miltos Alamanis 与高级首席研究主管 Marc Brockschmidt，刚刚在一篇博客文章中介绍了他们新开发的 BugLabs 人工智能。</strong>顾名思义。这是一套专门用于发现代码中的错误，帮助开发者更精准、高效地调试其应用程序的 AI 解决方案。而且它的开发过程，与创建生成对抗网络（GAN）的形式大致相同。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1210/111f04906cce62b.gif" alt="0.gif" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：Microsoft <a href="https://www.microsoft.com/en-us/research/blog/finding-and-fixing-bugs-with-deep-learning/" target="_self">Research Blog</a>）</p><p>在《借助深度学习查找并修复错误》一文中，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>研究员介绍了他们设置的两个相互对抗的网络。其中一个旨在将小错误引入代码，另一个则旨在发现这些 bug 。</p><p>随着深度学习训练的持续推进，AI 的能力也变得愈加完善，最终成为了我们看到的这个特别擅长识别“隐藏在真是代码中的 bug”的人工智能。</p><p><a href="https://static.cnbetacdn.com/article/2021/1210/02f90df13b1ab90.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1210/02f90df13b1ab90.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p>这种方法的优点，在于全程无需自我监督或标记数据。Miltos Allamanis 与 Marc Brockschmidt 在报告中提到：</p><blockquote><p>理论上，我们可以将之广泛地应用于‘捉迷藏’游戏 —— 教授机器去识别任务复杂的错误。遗憾的是，这些 bug 通常超出了现代人工智能方法的运用范围。</p><p>有鉴于此，研究团队决定更加专注于一组常见的错误 —— 包括不正确的比较（例如使用 <= 而不使用 < 或 > 符号、不适当的布尔运算符（与 / 或）、滥用变量（误用 i 而不是 j）等。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2021/1210/15cdc89993d8529.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1210/15cdc89993d8529.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>系统测试期间，微软研究员特别专注于 Python 代码。一旦检测器通过了训练，即可将它用于检测和修复实际代码中的 bug 。</p><p>不过为了均衡性能，他们还是手动注释了 Python Package Index 中包含的某些类型的小错误数据集。</p><p>最终与随机错误插入等其它替代方案相比，其“hide-and-seek”训练模型有高达三成的领先优势，前景很是光明。</p><p><a href="https://static.cnbetacdn.com/article/2021/1210/4bd4a6ad1322b47.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1210/4bd4a6ad1322b47.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p>具体说来是，hide-and-seek 能够自动找到并修复大约 26% 的错误，且其中包括了 19 个此前未知的真实开源 GitHub 代码中的 bug 。</p><p>与此同时，现阶段的 AI 模型仍存在许多误报。在投入实际运用之前，显然还需要开展更多的改进。</p><p>最后，鉴于微软已经成功地推动了 GitHub 上的 GPT-3 项目，预计 hide-and-seek 也将很快迎来商业化应用。</p>   
</div>
            