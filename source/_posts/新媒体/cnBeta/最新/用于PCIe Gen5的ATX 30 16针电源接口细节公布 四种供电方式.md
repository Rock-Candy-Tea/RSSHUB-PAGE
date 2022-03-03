
---
title: '用于PCIe Gen5的ATX 3.0 16针电源接口细节公布 四种供电方式'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0303/7808e7522599553.png'
author: cnBeta
comments: false
date: Thu, 03 Mar 2022 10:33:49 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0303/7808e7522599553.png'
---

<div>   
有关下一代PCIe 5.0显卡将引入全新16针(或者说12+4针)，我们已经讲了不少次，华硕、酷冷、技嘉、微星也都陆续发布了配备新接口、新电源线(转接线)的电源产品。现在，PCIe 5.0显卡供电的官方标准规范，终于泄露了一部分出来。<br>
 <p>新标准的官方名为“<strong>12VHPWR</strong>”，非常拗口，也是导致产品命名混乱不规范的根源。</p><p>我们知道，PCIe x16插槽的供电能力是75W，从未变过，PCIe 6针、8针辅助供电最高分别是75W、150W。</p><p>到了PCIe 5.0的时代，根据新标准，<strong>12VHPWR 16针的供电电压为12V，单个针脚电流最大9.2A，整体最大55A，最高稳定功率则有四个档次，从低到高分别是150W、300W、450W、600W，具体会在接头上明确标注，方便识别。</strong></p><p>当然，16个针脚中<strong>只有12个是负责供电的</strong>，另外4个负责信号监视传输，属于可选，但没有它们就上不到600W，最多只能到450W。</p><p><strong>如果再加上PCIe x16插槽本身的75W，PCIe 5.0显卡可以获得最高675W的供电支撑。</strong></p><p><img src="https://static.cnbetacdn.com/article/2022/0303/7808e7522599553.png" referrerpolicy="no-referrer"></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0303/b79f00661beb96b.png"><img data-original="https://static.cnbetacdn.com/article/2022/0303/b79f00661beb96b.png" src="https://static.cnbetacdn.com/thumb/article/2022/0303/b79f00661beb96b.png" referrerpolicy="no-referrer"></a></p><p>同时，<strong>标准还定义了两个边带信号(sideband signal)，分别叫Sense0、Sense1，全部接地的时候，才能达到600W的持续供电能力，系统启动时供电为375W。</strong></p><p>如果有任何一个非接地，持续和启动供电功率就会逐级下降，450W、300W、225W峰值分别对应225W、150W、100W起步。</p><p>如果显卡不监控此边带信号，则必须以最低的100W来启动。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0303/4bceb8e4191264d.png"><img data-original="https://static.cnbetacdn.com/article/2022/0303/4bceb8e4191264d.png" src="https://static.cnbetacdn.com/thumb/article/2022/0303/4bceb8e4191264d.png" referrerpolicy="no-referrer"></a></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0303/cef09594b5f835e.png"><img data-original="https://static.cnbetacdn.com/article/2022/0303/cef09594b5f835e.png" src="https://static.cnbetacdn.com/thumb/article/2022/0303/cef09594b5f835e.png" referrerpolicy="no-referrer"></a></p><p>另外根据ATX 3.0电源标准，<strong>16针供电不兼容现在的6/8针</strong>，因为无论是接口尺寸还是电流电压，都不完全一样，必须使用转接。</p><p><strong>消息称，NVIDIA RTX 40系列会标配16针供电接口</strong>，但不知道像RTX 30 FE系列那样仅限公版，还是非公版也会支持。</p><p>还有说法称RTX 3090 Ti会首发新接口，但这个卡皇命运多舛，已经推迟到不知道什么时候。</p><p><img src="https://static.cnbetacdn.com/article/2022/0303/edbaa1fe18b43e8.png" referrerpolicy="no-referrer"></p>   
</div>
            