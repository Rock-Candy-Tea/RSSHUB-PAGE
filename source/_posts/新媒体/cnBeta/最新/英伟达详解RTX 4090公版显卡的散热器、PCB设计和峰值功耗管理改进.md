
---
title: '英伟达详解RTX 4090公版显卡的散热器、PCB设计和峰值功耗管理改进'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0921/5b20dce578c7376.jpg'
author: cnBeta
comments: false
date: Thu, 22 Sep 2022 07:42:45 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0921/5b20dce578c7376.jpg'
---

<div>   
<strong>在今日的简报中，英伟达分享了 GeForce RTX 4090 公版（Founders Edition）显卡的一些设计细节，包括 PCB、散热器、以及峰值功耗控制。</strong>尽管从产品外形上来看，RTX 4090 和 RTX 3090 Ti 很相似，但官方还是指出了多处变更。比如金属外框的青铜色更明显，且下方散热器的阵列有重新排布、以改善两个风扇之间的风道。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0921/5b20dce578c7376.jpg" referrerpolicy="no-referrer"></p><p>早前 VideoCardz 有爆料 RTX 4090 拥有更大的轴流<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C738%2C751" target="_blank">风扇</a>，现英伟达也证实，该公司测试了多达 50 种新风扇设计，最终让气流较 RTX 3090 Ti 高出了 20% 。</p><p>除了散热器和风扇，该公司还重新设计了覆盖 GPU 主芯片、附近显存、以及 VRM 供电组件的散热器底板，让热管更加迎合显卡的热分布。</p><p>此外在 PCB 外形上，RTX 4090 沿用了上一代的紧凑型设计，以便于气流更顺畅地穿过散热鳍片。供电接口上，该卡用上了 12+4 pin 的 PCIe 5.0 12VHPWR 连接器。</p><p><img src="https://static.cnbetacdn.com/article/2022/0922/9733ca35f570b60.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自 @<a href="https://space.bilibili.com/95192698/dynamic" target="_self">大魔王FCP</a>）</p><p>尽管距离 ATX 3.0 电源的陆续上市仍有些时日，但不少厂商有提供三 8-pin 转接线、或者开放了符合新标准的 16-pin 模组线申请链接。</p><p>理论上，一条 12VHPWR 线缆能够承受高达 600W 的功率。所以即便 RTX 4090 的默认功耗为 450W，20 相 GPU + 3 相显存的 VRM 供电设计，还是给人们留下了相当大的遐想空间。</p><p>不过最让人关注的，还是 RTX 4090 对显卡峰值功耗 / 瞬态电压的管理改进有多上心。毕竟上一代 RTX 30 高端显卡的问题，曾给不少电源厂商打了个猝不及防（大幅超出了额定功率的上限）。</p><p><a href="https://static.cnbetacdn.com/article/2022/0922/2ffbfcb3b185eb2.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0922/2ffbfcb3b185eb2.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图自：<a href="https://www.techpowerup.com/299096/nvidia-details-geforce-rtx-4090-founders-edition-cooler-pcb-design-new-power-spike-management" target="_self">TechPowerUp</a>）</p><p>如上图所示，英伟达展示了全新 VRM 设计（PID 控制反馈回路的响应速度提升了十倍）是如何缓解电流尖峰的。</p><p>可知在 RTX 3090 出现较大波动的同时，RTX 4090 仍能保持相对稳定 —— 即便 RTX 3090 的额定功率要低 100W，但峰值却大幅超出了 RTX 4090 。</p><p>对于不想立即更换 ATX 3.0 电源的老 PC DIY 升级玩家们来说，这显然是个重大利好 —— 当然这并不意味着非公显卡也可满足相同的瞬态响应标准。</p><p><a href="https://static.cnbetacdn.com/article/2022/0921/ee8e5073283d6a0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0921/ee8e5073283d6a0.jpg" referrerpolicy="no-referrer"></a></p><p>显存方面，英伟达继续选择了与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://mall.jd.com/index-1000098521.html" target="_blank">美光</a>合作，单颗容量达到了 16 Gbit，因而无需像 RTX 3090 那样贴满双面 24 颗粒。通过将 12 颗 GDDR6X 显存放在 PCB 的同一侧，RTX 4090 可更有效地降温（-10℃）。</p><p>有趣的是，尽管定位掠地一阶，但 RTX 4080 16GB 公版显卡，还是用上了与 RTX 4090 同款的散热器。最后，GeForce RTX 4090 显卡将于 10 月 12 日上架，官方指导价为 1600 美元（国行 12999 RMB）。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1318325.htm" target="_blank">VideoCardz称RTX 4090沿用三槽设计 辅以更大的双轴流风扇</a></p><p><a href="https://www.cnbeta.com/articles/tech/1318725.htm" target="_blank">英伟达宣称RTX 4090等Ada Lovelace GPU可超频至3GHz以上</a></p></div>   
</div>
            