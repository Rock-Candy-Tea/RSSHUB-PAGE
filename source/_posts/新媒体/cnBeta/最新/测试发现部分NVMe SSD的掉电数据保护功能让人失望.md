
---
title: '测试发现部分NVMe SSD的掉电数据保护功能让人失望'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0224/46a013fe5db5e13.jpg'
author: cnBeta
comments: false
date: Thu, 24 Feb 2022 11:15:29 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0224/46a013fe5db5e13.jpg'
---

<div>   
苹果开发者 Russ Bishop 在一份测试报告中指出：<strong>即使掉电保护已经是个绕不开的话题，不少 NVMe 驱动器还是容易遭遇数据丢失问题。</strong>所谓掉电保护（PLP），特指让留存在易失性存储（此处为 DRAM）中的缓冲区数据，有足够的时间和机会将之写入到非易失性存储上（此处为 NAND）。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0224/46a013fe5db5e13.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0224/46a013fe5db5e13.jpg" referrerpolicy="no-referrer"></a></p><p>通过预设的保护电路和主控 / 固件算法，理论上是可以让 NVMe <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a> 保住这部分数据的，一些硬件制造商也热衷于宣传该卖点。</p><p><img src="https://static.cnbetacdn.com/article/2022/0224/42e218c9ac3724f.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">2/4 的 NVMe SSD 掉电保护不佳</p><p>然而 Russ Bishop 遗憾地发现，部分 NVMe SSD 并未能让人如愿 —— 其中一些缺失了该功能，另一些则没有如预期般发挥作用。</p><p><img src="https://static.cnbetacdn.com/article/2022/0224/8df2099e39b42d6.png" referrerpolicy="no-referrer"></p><p>在其经手的四款 SKU 中，三星 970 EVO Plus（2TB）和西数 WD RED SN700（1TB）都没有问题。</p><p><img src="https://static.cnbetacdn.com/article/2022/0224/2615ae36cd6a05a.png" referrerpolicy="no-referrer"></p><p>尴尬的是，SK 海力士 Gold P31（2TB）和 Sabrent Rocket（512GB）却辜负了大家的信任。</p><p><img src="https://static.cnbetacdn.com/article/2022/0224/f9ea24a727ce1b4.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">网页截图（来自：<a href="https://www.computerbase.de/2022-02/ssd-cache-problem-trotz-flush-droht-datenverlust-bei-stromausfall/" target="_self">ComputerBase.de</a>）</p><p>作为大规模 NVMe SSD 评测的前菜，接下来我们还会看到更多厂牌 / 型号的掉电保护测试结果。</p><p><img src="https://static.cnbetacdn.com/article/2022/0224/5f088ab30029910.png" referrerpolicy="no-referrer"></p><p>即使许多评测网站都没有考虑到掉电数据保护这一项、且不少消费者都已经习惯了计算机在断电 / 崩溃时发生数据丢失，Russ Bishop 还是对此感到颇为失望，毕竟主控制造商 / SSD 厂家工程师手头肯定有专门的测试用具。</p><p><img src="https://static.cnbetacdn.com/article/2022/0224/0a874ca75023fd9.png" referrerpolicy="no-referrer"></p><p>三星、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>、西数、镁光这几家都有原厂方案，但<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://kingston.jd.com/" target="_blank">金士顿</a> NV1 的过测还是让 Russ Bishop 小小惊喜了一下。即使它和关键时刻掉链子的 Sabrent 采用了同款群联主控，但两者的固件策略还是大不相同。</p><p><img src="https://static.cnbetacdn.com/article/2022/0224/e0ec666c345cba5.png" referrerpolicy="no-referrer"></p><p>为排除偶发 / 兼容性因素，Russ Bishop 尝试互换了下机箱，结果发现掉电保护不佳的 NVMe SSD 依然拉胯、能过测的厂牌型号则依然稳健。下一步，他希望找到具有 8-10 个 M.2 盘位的板子来组建 NAS 测试平台。</p>   
</div>
            