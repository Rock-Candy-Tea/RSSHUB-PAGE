
---
title: 'NVIDIA首款自出矿卡CMP 170HX曝光：超级大核心算力高达164MH_s'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://img1.mydrivers.com/img/20210902/7aa960d5f67e46e99909509e37488215.jpg'
author: cnBeta
comments: false
date: Thu, 02 Sep 2021 07:43:03 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210902/7aa960d5f67e46e99909509e37488215.jpg'
---

<div>   
今年3月份，曾有消息说，NVIDIA计划将安培家族的顶级大核心A100也做成矿卡，命名为CMP 220HX，以太坊算力高达210MH/s，价格也要3000美元。现在，它出现了，但不是完全体。知乎网友<a class="f14_link" href="https://zhuanlan.zhihu.com/p/393778558" target="_blank">@Codefordl</a>拿到了一块“<strong>CMP 170HX</strong>”，第一次听说这个名字，应该是CMP 220HX的小兄弟。<br>
 <p><img alt="超级大核心！NVIDIA首款自出矿卡CMP 170HX曝光：算力高达164MH/s" h="800" src="https://img1.mydrivers.com/img/20210902/7aa960d5f67e46e99909509e37488215.jpg" w="600" referrerpolicy="no-referrer"></p><p><img alt="超级大核心！NVIDIA首款自出矿卡CMP 170HX曝光：算力高达164MH/s" h="450" src="https://img1.mydrivers.com/img/20210902/9070983ac58840d28ff72369a7d64b49.jpg" w="600" referrerpolicy="no-referrer"></p><p><img alt="超级大核心！NVIDIA首款自出矿卡CMP 170HX曝光：算力高达164MH/s" h="800" src="https://img1.mydrivers.com/img/20210902/a98ae81b469a45728fd4b8a50f9c92bf.jpg" w="600" referrerpolicy="no-referrer"></p><p><img alt="超级大核心！NVIDIA首款自出矿卡CMP 170HX曝光：算力高达164MH/s" h="800" src="https://img1.mydrivers.com/img/20210902/75b78f36815a4c0aa9a058780990d592.jpg" w="600" referrerpolicy="no-referrer"></p><p>该卡造型和A100加速计算卡基本一致，也是被动散热、双插槽厚度，无视频接口，辅助供电很奇怪不是两个PCIe 8针，而是两个CPU ES 8针，因此需要转接线(附赠)。</p><p><strong>这应该是第一款NVIDIA自己打造的专用矿卡</strong>——之前的30HX、40HX、50HX、90HX都是只交付核心，矿卡由AIC厂商来做。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0902/c1aab8352f9dfda.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0902/c1aab8352f9dfda.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0902/c1aab8352f9dfda.jpg" referrerpolicy="no-referrer"></a></p><p>GPU-Z已经可以识别出基本规格，还有人挖出了一份官方规格表，大致能对应起来。</p><p>GPU核心认不出来，只有一个20C2的编号。<strong>流处理器(CUDA核心)只有4480个，对比RTX 3060还要少了384个</strong>，而完整的A100核心拥有8196个流处理器，也就是只开启了大约55％，或者相当于A100加速卡的84％，后者开启了6192个。</p><p>显然，<strong>NVIDIA这是拿瑕疵严重的A100核心重新利用</strong>，毕竟这样的大核心成本不菲，做成矿卡纯属白赚，不知道更高端的CMP 220HX会开启多少个。</p><p>HBM2e显存也大幅阉割，本来有40/80GB，而<strong>这里只配备了8GB，不过位宽依然有4096-bit，带宽也仍旧高达1.5TB/s</strong>，只是无法超频。</p><p><strong>核心基础频率仅为1140MHz，最高加速1410MHz</strong>(GPU-Z检测错误)，倒是和A100保持一致。</p><p>特别值得一提的是，<strong>该卡的系统带宽被锁定在PCIe 1.1 x4，只能用来挖矿，想拿它省钱做计算是不可能的</strong>——老黄果然心思缜密。</p><p>从频率上计算，CMP 170HX的以太坊算力理论上最高为186.625MB/s，当然实际运行时肯定要低一些。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0902/58a2581473d23d6.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0902/58a2581473d23d6.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0902/58a2581473d23d6.jpg" referrerpolicy="no-referrer"></a></p><p>实测使用ETHASH算法测试，<strong>默认状态下算力为164MH/s，此时功耗250W</strong>，但核心频率对温度非常敏感，超过70度就降频。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0902/5404a41e8c3abac.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0902/5404a41e8c3abac.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0902/5404a41e8c3abac.jpg" referrerpolicy="no-referrer"></a></p><p><strong>功耗限制到190W，算力降为158MH/s</strong>，损失不多，但能效提高了将近27％。</p><p>相比之下，RTX 3080以太坊算力一般在88MH/s，RTX 3060满血状态约为42MH/s，目前在售基本都是阉割版只有约21MH/s。</p><p><img src="https://static.cnbetacdn.com/article/2021/0902/a7ce3337641c479.png" referrerpolicy="no-referrer"><br>A100计算卡</p>   
</div>
            