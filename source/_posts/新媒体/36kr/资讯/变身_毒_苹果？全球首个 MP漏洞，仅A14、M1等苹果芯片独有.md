
---
title: '变身_毒_苹果？全球首个 MP漏洞，仅A14、M1等苹果芯片独有'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220507/v2_aee34a14d1b040e59ce2183c70dc5afe_img_png'
author: 36kr
comments: false
date: Sat, 07 May 2022 11:35:50 GMT
thumbnail: 'https://img.36krcdn.com/20220507/v2_aee34a14d1b040e59ce2183c70dc5afe_img_png'
---

<div>   
<p>近来的苹果，可以说是很好地诠释了一个词：树大招风。</p> 
<p>前有各大监管机构查它垄断、命其开放，后有竞争公司不断挖角、窃取机密，甚至就在日前，还有研究人员在 Apple Silicon 中发现了世界首个数据内存依赖预取器（Data Memory-Dependent Prefetcher，简称为 DMP）安全漏洞——该漏洞被称为“Augury”（意为“占卜”），目前只存在于 Apple Silicon。</p> 
<h2>1 一直对 DMP 存有疑虑</h2> 
<p>发现 Augury 的研究团队成员来自不同高校，其中包括伊利诺伊大学厄巴纳-香槟分校、特拉维夫大学和<a class="project-link" data-id="1678323706115076" data-name="华盛" data-logo="https://img.36krcdn.com/20220331/v2_dcfe33d40d024a8caa06ef7375c295c1_img_000" data-refer-type="1" href="https://36kr.com/project/1678323706115076" target="_blank">华盛</a>顿大学，而该团队一直以来对 DMP 都存有疑虑。</p> 
<p>DMP，即数据内存依赖预取器，可通过了解整个内存内容，预取数据来提高系统性能。一般来说，为了确保系统安全，内存访问会受到限制和划分，而著名科技评测网站 Anandtech 在苹果推出 M1 后，对 A14 测评的一段措辞引起了该研究团队的注意：</p> 
<p>在微架构调查中，我们在苹果的芯片设计中看到了“记忆魔法”的迹象，我们推测苹果正在使用某种指针追踪预取机制。</p> 
<p>对此，研究团队猜测：苹果芯片的 DMP 预取可能会超出内存指针集，即可以访问并尝试对不相关的内存地址进行预取，甚至深度预取。</p> 
<p>出于这种担忧，该团队开始研究 M1 和 A14，也果然发现了眉目：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>“我们发现苹果处理器有一个 DMP。”</p></li> 
 <li><p>“我们发现这个 DMP 预取了一个指针数组解引用模式。”</p></li> 
 <li><p>“我们发现可以通过此预取器来泄漏任何指令都不会读取的数据（指针），即使只是推测性的！”</p></li> 
</ul> 
<p>进一步解释：Apple Silicon 的 DMP 功能存在漏洞“Augury”，如该漏洞被攻击者成功利用，系统将会被暴露于静态数据攻击，即被泄露的数据由于是静态的，不会以推测或非推测的方式被核心读取，因此难以被发现。</p> 
<h2>2 Apple Silicon 独有的漏洞</h2> 
<p>具体来说，该研究团队发现 Apple Silicon 的确使用了 DMP 预取指针数组 (AoP)：</p> 
<p><img src="https://img.36krcdn.com/20220507/v2_aee34a14d1b040e59ce2183c70dc5afe_img_png" data-img-size-val="1746,226" referrerpolicy="no-referrer"></p> 
<p><span style="letter-spacing: 0px;">研究人员对此解释道：“一旦代码看到 *arr[0]……arr[2] 发生（甚至只是推测性的！），它就将开始预取 arr[3]。也就是说，它是先预取 arr 的内容，然后才取消引用。但一般传统的预取器不会执行第二步/取消引用的操作。”</span></p> 
<p>在 AoP 中，系统寻址、读取和缓存尚未访问过的内存，且这些数据可能永远不会被访问——也就是说，目前 Apple Silicon 的 DMP 功能使系统过度读取和暴露数据，也就更容易受到攻击。</p> 
<p>说到这里，可能会有人会由这次的 Augury，联想到曾经在全球引起巨大轰动的 Spectre 和 Meltdown 漏洞（这两个漏洞可使攻击者通过利用并行运行进程的方式来破坏处理器的特权内存，窃取敏感数据），但该研究团队指出，Augury 和 Spectre/Meltdown 并不相同：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>Augury 只利用 DMP 功能，并非瞬态执行；</p></li> 
 <li><p>Spectre 可被完全禁用，而 Augury 将仍然存在；</p></li> 
 <li><p>适用于 Augury 的防御类型与其他微架构攻击也不同。任何依赖于跟踪被核心访问的数据防御都不能阻止 Augury 泄露数据，因为通过 Augury 泄露的数据永远不会被核心读取。</p></li> 
</ul> 
<p>因此我们也可以理解为，Spectre 和 Meltdown 漏洞泄漏的是正在使用的数据，而利用苹果的 DMP，Augury 可能会泄漏整个内存内容，即使这些数据没有被主动访问。</p> 
<h2>3 苹果已知情，但尚未打补丁</h2> 
<p>据研究团队公开的漏洞资料表明，Augury 目前仅存于 Apple Silicon，已确认受影响的芯片包括 A14、M1 和 M1 Max（都具有 DMP 功能）。他们也对最新几款英特尔和 AMD 处理器进行了测试，但均没有发现 Augury 漏洞的迹象。</p> 
<p>此外，研究人员补充道：“我们认为一些较旧的 A 系列芯片和最新的 M1 系列（M1 Pro 等）芯片也会受到影响，但目前只在 M1 Max 上得到了证实。”</p> 
<p>值得庆幸的是，该研究团队指出，尽管听起来 Augury 存在不小的隐患，但他们还未“展示任何借助 Augury 进行端到端的漏洞利用”，因此至少现阶段，“只有指针会被泄露”。</p> 
<p>至于该漏洞的补丁，研究团队表示已与苹果方面讨论过这个问题，苹果也已知晓漏洞的全部细节，但目前据他们的了解，苹果尚未推出相关补丁。</p> 
<p>参考链接：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>https://www.prefetchers.info/</p></li> 
 <li><p>https://www.tomshardware.com/news/apple-silicon-exclusively-hit-with-world-first-augury-dmp-vulnerability</p></li> 
</ul> 
<p>本文来自微信公众号<a href="https://mp.weixin.qq.com/s/M79k_hGZVUwj-cYdGakAIQ" rel="noopener noreferrer nofollow">“CSDN”（ID:CSDNnews）</a>，整理：郑丽媛，36氪经授权发布。</p>  
</div>
            