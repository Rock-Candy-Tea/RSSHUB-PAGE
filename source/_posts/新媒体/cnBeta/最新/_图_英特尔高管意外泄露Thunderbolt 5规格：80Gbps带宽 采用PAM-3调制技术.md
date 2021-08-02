
---
title: '_图_英特尔高管意外泄露Thunderbolt 5规格：80Gbps带宽 采用PAM-3调制技术'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0802/b5bf8d2bbdc416e.jpg'
author: cnBeta
comments: false
date: Mon, 02 Aug 2021 00:00:35 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0802/b5bf8d2bbdc416e.jpg'
---

<div>   
英特尔执行副总裁兼计算部总经理格雷戈里·布莱恩特（Gregory Bryant）本周访问了公司的以色列研发机构，这是他今年首次访问海外英特尔机构。在本周日早上他发布的推文中，意外展示了关于下一代 ThunderBolt 技术的相关信息。随后这条推文被立即删除。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0802/b5bf8d2bbdc416e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0802/b5bf8d2bbdc416e.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在这张图片中，我们可以看到墙上的海报展示了“80G PHY 技术”，这意味着<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>正在研究 80Gbps 连接的物理层（PHY）。这是 Thunderbolt 4 带宽的两倍，Thunderbolt 4 的带宽是 40Gbps。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0802/d9e66b3ffd2d8d2.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0802/d9e66b3ffd2d8d2.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">第二行写道：“USB 80G的目标是支持现有的USB-C生态系统”，这表明英特尔的目标是保持 USB-C 连接器，但将有效带宽提高一倍。</p><p style="text-align: left;">第三行实际上是它在技术上变得有趣的地方。PHY 将基于新颖的 PAM-3 调制技术。这是关于 0 和 1 的传输方式--传统上我们谈论的是 NRZ 编码，它只允许传输 0 或 1，或一个单一的比特。自然的发展是一个允许传输两个比特的方案，这被称为 PAM-4（脉冲振幅调制），4 是两个比特可以被看到的不同变体的分界线（可以是00，01，10，或11）。在相同的频率下，PAM-4 的带宽是 NRZ 连接的两倍。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0802/35dba80fe1c287b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0802/35dba80fe1c287b.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">那么 PAM-3 技术是什么？数据线可以携带-1、0或+1。该系统所做的实际上是将两个PAM-3传输合并为一个3位数据信号，例如000是一个-1，后面是一个-1。这变得很复杂，所以这里有一个表格。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0802/1936aee3b03356a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0802/1936aee3b03356a.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">当我们将 NRZ 与 PAM-3 和 PAM-4 进行比较时，我们可以看到 PAM-3 的数据传输率处于NRZ和PAM-4的中间。在这种情况下使用 PAM-3 的原因是为了实现更高的带宽，而没有 PAM-4 需要启用的额外限制。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0802/7e437abdcc669f0.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0802/7e437abdcc669f0.png" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">这张图片的最后一行是“专注于新PHY技术的N6测试芯片正在[实验室]工作，并显示出令人鼓舞的结果”。第一个词我认为是台积电，但它必须与上面一行的 "The "宽度相同。所以看起来我没有说对，但 N6 是台积电的节点。</p>   
</div>
            