
---
title: '研究人员发现苹果 Silicon 芯片漏洞_Augury_，影响 A14 和 M1 _ Max _ Pro'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/5/8b329004-fa75-427d-a811-89e118f7e1b6.jpg@s_2,w_820,h_410'
author: IT 之家
comments: false
date: Tue, 03 May 2022 00:34:51 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/5/8b329004-fa75-427d-a811-89e118f7e1b6.jpg@s_2,w_820,h_410'
---

<div>   
<p data-vmark="5f61"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 5 月 3 日消息，据 9to5 Mac 报道，在深入研究 Apple Silicon 之后，研究人员发现了一个影响苹果最新 M1 和 A14 芯片的新漏洞。“Augury” Apple Silicon 微架构缺陷已被证明会泄漏静态数据，但目前似乎还没有“那么糟糕”。</p><p style="text-align: center;" data-vmark="17e1"><img src="https://img.ithome.com/newsuploadfiles/2022/5/8b329004-fa75-427d-a811-89e118f7e1b6.jpg@s_2,w_820,h_410" w="1440" h="720" title="研究人员发现苹果 Silicon 芯片漏洞“Augury”，影响 A14 和 M1 / Max / Pro" srcset="https://img.ithome.com/newsuploadfiles/2022/5/8b329004-fa75-427d-a811-89e118f7e1b6.jpg 2x" width="1440" height="410" referrerpolicy="no-referrer"></p><p data-vmark="4daf">伊利诺伊大学厄巴纳香槟分校的 Jose Rodrigo Sanchez Vicarte 和华盛顿大学的 Michael Flanders 领导的一组研究人员，他们公布了发现新颖的 Augury 微架构 Apple Silicon 缺陷的详细信息（所有细节在发布前与苹果共享）。</p><p data-vmark="e5d2">该小组发现，苹果芯片使用所谓的数据内存依赖预取器 (DMP)，它通过查看内存内容来决定预取什么。</p><p data-vmark="48d5">Augury Apple Silicon 漏洞的工作原理</p><p data-vmark="68c5">具体来说，苹果的 M1、M1 Max 和 A14 经过测试，发现使用指针数组解引用模式进行预取。研究人员发现，该过程可能会泄漏“任何指令都不会读取的数据，即使是推测性的！”<span class="accentTextColor">他们还认为 M1 Pro 和可能较旧的 A 系列芯片容易受到相同缺陷的影响</span>。</p><p data-vmark="cc2d">以下是研究人员所说的苹果的 DMP 与传统 DMP 的不同之处：</p><blockquote><p data-vmark="8480">“一旦它看到 *arr [0] … *arr [2] 发生（甚至是推测性的！）它将开始预取 *arr [3] 。也就是说，它将首先预取 arr 的内容，然后取消引用这些内容。相反，传统的预取器不会执行第二步 / 取消引用操作。”</p></blockquote><p data-vmark="55ae">至于为什么像这样的静态数据攻击很麻烦，该论文说，大多数防止“微架构攻击”的硬件或软件防御策略都假设有一些指令可以访问机密。但静态数据漏洞并非如此。研究进一步解释说：</p><blockquote><p data-vmark="375d">“任何依赖于跟踪内核访问的数据（推测性或非推测性）的防御措施都无法防止 Augury，因为内核永远不会读取泄漏的数据！”</p></blockquote><p data-vmark="898f">但华盛顿大学助理教授兼研究小组首席研究员 David Kohlbrenner 指出，这种 DMP“是攻击者可以获得的最弱的 DMP”。</p><p style="text-align: center;" data-vmark="709e"><img src="https://img.ithome.com/newsuploadfiles/2022/5/46dd70da-1a78-4fa6-b68f-03c99b224ece.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xZC9xZDg1LnBuZw==,g_7,x_9,y_9,a_0,t_100" w="553" h="531" title="研究人员发现苹果 Silicon 芯片漏洞“Augury”，影响 A14 和 M1 / Max / Pro" width="553" height="531" referrerpolicy="no-referrer"></p><p data-vmark="5b11">研究人员强调，目前该漏洞看起来并没有“那么糟糕”，而且他们目前还没有展示任何“使用 Augury 技术的端到端漏洞利用”。目前，只有指针可以泄露，而且很可能只在沙盒威胁模型中。”</p>
          
</div>
            