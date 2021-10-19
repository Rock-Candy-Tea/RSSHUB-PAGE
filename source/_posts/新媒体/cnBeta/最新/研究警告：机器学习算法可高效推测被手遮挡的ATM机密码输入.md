
---
title: '研究警告：机器学习算法可高效推测被手遮挡的ATM机密码输入'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1019/5c68da0dde4fe03.jpg'
author: cnBeta
comments: false
date: Tue, 19 Oct 2021 10:43:52 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1019/5c68da0dde4fe03.jpg'
---

<div>   
对于经常光顾 ATM 自助存取款的人们来说，确保密码输入的隐私安全，几乎已经成为了一项普遍共识。<strong>然而近日的一项研究表明，只要通过特殊的训练，即可利用深度学习算法，来高效破解被另一只手遮挡住的 PIN 码输入。</strong>最终结果是，通过模拟训练，算法可在 41% 的几率下猜出四位 PIN 码。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1019/5c68da0dde4fe03.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">完整攻击链（来自：Arxiv.org）</p><p>实验期间，研究人员收集了来自 58 名多样化人群的 5800 段视频，其中涉及输入 4 位 / 5 位 PIN 码。</p><p>运行预测模拟的机器配置，包括一台 Intel 志强 E5-2670 处理器 + 128GB 内存、以及三套英伟达 Tesla K20m（平均 5GB RAM）计算卡的计算机。</p><p>虽然与普通 PC 大不相同，但这套系统的整体经济性，还是在相当合理的范围呢。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1019/467b4e17f05d49f.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">三种攻击场景的预测热图</p><p>通过设置最大 3 次尝试次数（不然容易被 ATM 吞卡），研究人员在 30% 的时间内重建了 5 位 PIN 码的正确序列，并在 4 位 PIN 码中达成了更高的成功率（41%）。</p><p>预测模型可根据非输入（在上遮挡）手的覆盖范围来排除按键，并通过评估两个按键之间的拓扑距离，从而推断另一只手按下了哪个数字。</p><p>与此同时，拍摄画面用的相机位置，也起到了至关重要的作用 —— 尤其针对左撇子或右撇子参与者时。综合之下，隐藏于 ATM 顶部的针孔摄像头，对用户的安全威胁时最大的。</p><p><a href="https://static.cnbetacdn.com/article/2021/1019/8ea658899a69a1a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1019/8ea658899a69a1a.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">每位数字的猜测与概率</p><p>如果录制设备同时能够收音，则预测模型还可根据每个数字略有不同的按压声音反馈，来进一步提升预测的准确性。</p><p>综上所述，该实验证明了用一只手来遮挡密码键盘的方法，不足以抵御基于深度学习的 PIN 码猜测攻击。庆幸的是，研究团队也提供了一些反向应对策略。</p><blockquote><p>· 首先，如果银行允许设施较长的 PIN 码，就不要图省事用太短的，即便记起来也更累一些。</p><p>· 其次，尽量把手遮挡得严实一些。在 75% 覆盖率下，算法每次猜测的准确率为 0.55；而在 100% 遮挡的情况下，准确率会大幅降低至 0.33 。</p><p>· 第三，灵活运用随机 / 虚拟键盘，而不是标准化的机械键盘。虽然实用性不佳，但它确实是一种相当不错的安全措施。</p></blockquote><p>有趣的是，研究团队还邀请了 78 位参与者，看他们能够凭直觉达成多高的隐藏 PIN 码猜测准确率。结果发现，人类的回答准确率仅为 7.92% 。</p>   
</div>
            