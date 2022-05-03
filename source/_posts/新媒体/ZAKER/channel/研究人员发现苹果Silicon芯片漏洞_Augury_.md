
---
title: '研究人员发现苹果Silicon芯片漏洞_Augury_'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/62707d818e9f094979544fbd_1024.jpg'
author: ZAKER
comments: false
date: Mon, 02 May 2022 20:14:04 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/62707d818e9f094979544fbd_1024.jpg'
---

<div>   
<p>IT 之家 5 月 3 日消息，据 9to5 Mac 报道，在深入研究 Apple Silicon 之后，研究人员发现了一个影响苹果最新 M1 和 A14 芯片的新漏洞。"Augury" Apple Silicon 微架构缺陷已被证明会泄漏静态数据，但目前似乎还没有 " 那么糟糕 "。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202205/62707d818e9f094979544fbd_1024.jpg" data-height="720" data-width="1440" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/62707d818e9f094979544fbd_1024.jpg" referrerpolicy="no-referrer"></div></div>伊利诺伊大学厄巴纳香槟分校的 Jose Rodrigo Sanchez Vicarte 和华盛顿大学的 Michael Flanders 领导的一组研究人员，他们公布了发现新颖的 Augury 微架构 Apple Silicon 缺陷的详细信息（所有细节在发布前与苹果共享）。<p></p><p>该小组发现，苹果芯片使用所谓的数据内存依赖预取器 ( DMP ) ，它通过查看内存内容来决定预取什么。</p><p>Augury Apple Silicon 漏洞的工作原理</p><p>具体来说，苹果的 M1、M1 Max 和 A14 经过测试，发现使用指针数组解引用模式进行预取。研究人员发现，该过程可能会泄漏 " 任何指令都不会读取的数据，即使是推测性的！" 他们还认为 M1 Pro 和可能较旧的 A 系列芯片容易受到相同缺陷的影响。</p><p>以下是研究人员所说的苹果的 DMP 与传统 DMP 的不同之处：</p><p>" 一旦它看到 *arr [ 0 ] … *arr [ 2 ] 发生（甚至是推测性的！）它将开始预取 *arr [ 3 ] 。也就是说，它将首先预取 arr 的内容，然后取消引用这些内容。相反，传统的预取器不会执行第二步 / 取消引用操作。"</p><p>至于为什么像这样的静态数据攻击很麻烦，该论文说，大多数防止 " 微架构攻击 " 的硬件或软件防御策略都假设有一些指令可以访问机密。但静态数据漏洞并非如此。研究进一步解释说：</p><p>" 任何依赖于跟踪内核访问的数据（推测性或非推测性）的防御措施都无法防止 Augury，因为内核永远不会读取泄漏的数据！"</p><p>但华盛顿大学助理教授兼研究小组首席研究员 David Kohlbrenner 指出，这种 DMP" 是攻击者可以获得的最弱的 DMP"。</p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres2.myzaker.com/202205/62707d818e9f094979544fbe_1024.jpg" data-height="531" data-width="553" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/62707d818e9f094979544fbe_1024.jpg" referrerpolicy="no-referrer"></div></div>研究人员强调，目前该漏洞看起来并没有 " 那么糟糕 "，而且他们目前还没有展示任何 " 使用 Augury 技术的端到端漏洞利用 "。目前，只有指针可以泄露，而且很可能只在沙盒威胁模型中。"<p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            