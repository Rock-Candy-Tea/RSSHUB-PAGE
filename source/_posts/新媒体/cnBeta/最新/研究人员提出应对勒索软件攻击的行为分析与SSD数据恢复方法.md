
---
title: '研究人员提出应对勒索软件攻击的行为分析与SSD数据恢复方法'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0910/94656ab9d5ff577.png'
author: cnBeta
comments: false
date: Fri, 10 Sep 2021 03:25:52 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0910/94656ab9d5ff577.png'
---

<div>   
来自韩国仁荷大学（Inha University）、大邱庆北科技学院（DGIST）、中佛罗里达大学（UCF）、以及梨花女子大学（EWU）网络安全系的一支研究团队，刚刚介绍了一套应对勒索软件攻击的 SSD 数据检测与恢复方法。<strong>据说这套名为“SSD-Insider”的方案可实现几乎 100% 的准确性，且已通过现实世界中勒索软件的测试考验。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0910/94656ab9d5ff577.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0910/94656ab9d5ff577.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">研究配图（来自：UCF | <a href="http://cs.ucf.edu/~mohaisen/doc/icdcs18b.pdf" target="_self">PDF</a>）</p><p>据悉，SSD-Insider 的工作原理，是识别 SSD 活动中某些已知可辨别的勒索软件行为模式。</p><p>为了仅通过 IO 请求标头的分布来识别勒索软件活动，研究团队留意到 WannaCry、Mole 和 CryptoShield 等勒索软件，都具有相当独特的覆盖行为。</p><p>仁荷大学研究员 DaeHun Nyang 在接受 The Register 采访时称：“当 SSD-Insider 检测到勒索软件活动时，存储器的输入 / 输出（IO）将被暂停，以便用户能够对勒索软件进程进行剔除”。</p><p><a href="https://static.cnbetacdn.com/article/2021/0910/ebde901792a4102.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0910/ebde901792a4102.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">勒索软件行为模式分析</p><p>在勒索软件被中止时，SSD-Insider 还可通过 SSD 的独特属性，来恢复已丢失的文件。</p><p>文章指出：在被新数据覆盖之前，固态存储器将始终保留此前被删除的数据，直到后续被主控和固件的垃圾回收机制给清理。</p><p>通过利用 SSD 的这一内置备份功能，SSD-Insider 也得以追踪驱动器内的旧版本数据。然后在勒索软件检测算法确认新版本数据未受到勒索软件影响之前，这些数据都将不被彻底删除。</p><p><a href="https://static.cnbetacdn.com/article/2021/0910/e86c422ec52b28a.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0910/e86c422ec52b28a.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">SSD-Insider 测试表现</p><p>SSD-Insider 的真正独特之处，在于它甚至能够以固件级别运行。那样即使系统上没有安装相应的安全软件，用户也可获得抵御勒索软件攻击的益处。</p><p>此外，论文中提到了传统软件防御方法的缺点，比如反勒索软件的 CPU 开销较高、且某些勒索软件可能逃脱反病毒软件的检测。相比之下，SSD-Insider 的时间开销仅在 147~254 ns 左右。</p><p>以 WannaCry 等勒索软件展开测试时，SSD-Insider 为放过任何勒索软件活动，且极少触发误报。在所有测试场景下，其错误拒绝率（FRR）为零、错误接受率（FAR）也几乎为零。</p><p><img src="https://static.cnbetacdn.com/article/2021/0910/2322be7c9fd1294.png" alt="4.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">测试训练用的勒索软件 / 应用程序</p><p>研究人员指出：就 FRR 而言，最糟糕的“背景噪声”，来源于 IO / CPU 密集型的工作环境。至于 FAR，最糟糕的情况也是 DataWiping 和数据库等重覆盖类型的工作场景。</p><p>当然，对于防病毒研究人员来说，SSD-Insider 的这样的方法也并不是万无一失的。</p><p>毕竟在勒索软件开发者知晓了该方案的存在之后，后续仍可开发出对应的绕过方法，所以大家还是要养成定期备份数据的好习惯。</p>   
</div>
            