
---
title: 'Intel 60核心至强官方曝照：天生残血'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0221/12f8b802511ed47.jpg'
author: cnBeta
comments: false
date: Mon, 21 Feb 2022 10:19:53 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0221/12f8b802511ed47.jpg'
---

<div>   
日前，Intel公布了至强处理器路线图，今年第一季度交付Sapphire Rapids，工艺、架构都与12代酷睿同款(当然只有大核)，支持八通道DDR4、PCIe
5.0，可选集成最多64GB HBM2e内存。ISSCC 2022国际固态电路大会上，Intel又大方地公布了Sapphire
Rapids的内核照、结构简图，芯片大神Locuza则据此进行分析，对每个模块都做了标注。<br>
<p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0221/12f8b802511ed47.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0221/12f8b802511ed47.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0221/12f8b802511ed47.jpg" referrerpolicy="no-referrer"></a></p><p>原始内核照</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0221/756124ebc762cb3.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0221/756124ebc762cb3.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0221/756124ebc762cb3.jpg" referrerpolicy="no-referrer"></a></p><p>内核标注图</p><p><img src="https://static.cnbetacdn.com/article/2022/0221/859a381edb87ab9.jpg" referrerpolicy="no-referrer"></p><p>每个核心与EMIB桥接通道的互连</p><p>首先，<strong>这次终于明确了Sapphire Rapids的核心数量，实际开启的确实是56个，但原生并非64个，而是60个。</strong></p><p>Sapphire Rapids采用小芯片封装，内部集成四个Die，彼此通过EMIB桥接互连。</p><p><strong>之前的拆解打磨图上，像极了每个Die 16个核心，四行四列布局，但是根据官方内核照，其中一块并非CPU核心，而是内存控制器单元</strong>，和旁边的内存PHY物理层相连，实际上每个Die是15个核心(开启14个)。</p><p><img src="https://static.cnbetacdn.com/article/2022/0221/0465aca9d4bf04a.jpg" referrerpolicy="no-referrer"></p><p><img src="https://static.cnbetacdn.com/article/2022/0221/713d531af121bbb.jpg" referrerpolicy="no-referrer"><br>太有迷惑性了</p><p>同样是小芯片，Intel、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>走的是不同路线。AMD单独将I/O部分做成了一个Die芯片，<strong>Intel则是每个Die芯片都是完整的</strong>，包括所有必要模块，甚至单独拿出来都可以做一颗处理器，这样划分不同型号更为简单。</p><p><strong>每个CPU核心有1.875MB三级缓存，整个处理器共计112.5MB，实际开启105MB。</strong></p><p><strong>PCIe 5.0与新的CXL 1.1标准高速总线打通，基本彼此对等，共有128条</strong>，另外，UPI互连总线共计96条，但不知道是否全部开启。</p><p>内存通道，每个Die 128-bit，如果加上ECC纠错就是160-bit。</p><p>Sapphire Rapids还集成了<strong>多种加速器</strong>，已经可以找到的有DSA(数据流加速器)、QAT(快速助手技术)、DLBoost 2.0。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0221/9be2b60088409c1.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0221/9be2b60088409c1.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0221/9be2b60088409c1.jpg" referrerpolicy="no-referrer"></a></p><p>原始结构简图</p>   
</div>
            