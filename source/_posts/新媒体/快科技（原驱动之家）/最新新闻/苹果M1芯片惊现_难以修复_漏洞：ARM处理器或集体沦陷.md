
---
title: '苹果M1芯片惊现_难以修复_漏洞：ARM处理器或集体沦陷'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220612/s_bef2d0bf30a94f389c784c4ab256744f.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sun, 12 Jun 2022 18:22:37 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220612/s_bef2d0bf30a94f389c784c4ab256744f.jpg'
---

<div>   
<p>6月11日消息，据媒体报道，近日，麻省理工学院（MIT）的研究人员发现，苹果的M1芯片存在一个“无法修补”的硬件漏洞，攻击者可以利用该漏洞突破其最后一道安全防御。</p>
<p>报道称，该漏洞存在于苹果M1芯片中使用的硬件级安全机制中，被称为“指针身份验证”（PAC）——这是Arm处理器当中广泛存在的一项硬件安全机制，它通过使用加密哈希保护指针来保护内存中的指针完整性，该加密哈希验证指针无法被修改，系统使用它来验证程序对受保护指针的使用。当使用错误的PAC时，程序会崩溃。</p>
<p>根据此前Arm公布的信息显示，PAC最小化了攻击面，使得面向返回编程(ROP)漏洞减少了60%以上、面向跳转编程(JOP)漏洞减少了40%以上。</p>
<p>如果是同时使用PAC和分支目标标识符（BTI）这两个硬件安全机制的Arm CPU则能够进一步提升安全性，Glibc 中攻击者可用的小工具数量减少了约 98%，而代码大小仅增加了 2% 左右。</p>
<p>不过，麻省理工学院计算机科学和人工智能实验室（CSAIL）的研究人员Joseph Ravichandran、Weon Taek Na、Jay Lang 和 Mengjia Yan 创造了一种新颖的硬件攻击方式，它结合了内存损坏和推测执行攻击来回避安全功能。</p>
<p><strong>该攻击表明，指针身份验证可以不留痕迹地被攻破，并且由于它是一种硬件安全机制，因此苹果将无法通过更新M1芯片的软件补丁来修复它。</strong></p>
<p>MIT CSAIL研究团队将其攻击方式称之为“Pacman”，它通过硬件侧信道攻击来暴力破解PAC值（由于PAC值只有一定数量，研究人员可以尝试所有值以找到正确的值），并抑制崩溃，从而启动连锁攻击，最终构建控制流劫持攻击。</p>
<p>“PAC的大小相对较小，直接的暴力攻击会导致足够多的崩溃来检测恶意行为——更不用说程序重新启动会导致 PAC 被刷新。但Pacman攻击的关键在于，使用推测执行攻击，通过微架构侧通道秘密泄露PAC验证结果，而不会导致崩溃。”该论文解释道。</p>
<p>在概念验证中，研究人员证明该攻击甚至可以针对内核（设备操作系统的软件核心）起作用，这“对所有启用指针身份验证的 Arm 系统的未来安全工作具有重大影响。”MIT CSAIL的博士生和该研究论文的共同主要作者Joseph Ravichandran说道。</p>
<p>“指针身份验证背后的想法是，如果所有其他防御方法都失败了，你仍然可以依靠它来防止攻击者控制你的系统。” Joseph Ravichandran补充道：“但是，我们已经证明，作为最后一道防线的指针身份验证并不像我们曾经认为的那样的安全。”</p>
<p>到目前为止，苹果已经在其所有基于Arm架构的定制芯片上内置了PAC功能，包括 M1、M1 Pro 和 M1 Max等。此外，包括高通和三星在内的许多其他芯片厂商已经宣布或预计将推出新处理器都将支持该硬件级安全功能。</p>
<p>虽然，MIT CSAIL的研究人员表示，尚未对苹果刚刚发布的 M2 芯片的进行测试攻击，但该芯片也支持PAC功能。</p>
<p>根据此前Arm公布的信息显示，不仅基于Armv8.3/8.6指令集的CPU内置了PAC功能，最新的Armv9指令集的CPU同样也内置了PAC功能。</p>
<p>MIT CSAIL的研究人员在研究论文中说：“<strong>如果不解决这个问题，我们发现的这项攻击方式将在未来几年影响大多数移动设备，甚至可能影响桌面设备。</strong>”</p>
<p>据介绍，研究人员已经向苹果公司展示了他们的研究结果。不过，他们也指出，Pacman攻击并不能绕过 M1 芯片上的所有安全机制，它只是针对PAC可以防止的现有的漏洞。</p>
<p>Joseph Ravichandran表示：“到目前为止，还没有使用Pacman创建端到端攻击，因此没有直接的担忧。Pacman需要一个现有的软件漏洞才能发挥作用——攻击者需要能够写入溢出内存。攻击者可以使用现有的漏洞与我们的谓的‘Pacman Gadget’相结合——受攻击中的一个代码序列，允许推测性地使用签名指针。”</p>
<p>目前，该研究团队已将该问题通知苹果，并将在 6 月 18 日的计算机架构国际研讨会上披露更多细节。</p>
<p>在该消息被曝光之后，苹果公司发言人 Scott Radcliffe 对外回应称：“我们要感谢研究人员的合作，因为这个概念证明促进了我们对这些技术的理解。根据我们的分析以及研究人员与我们分享的详细信息，我们得出的结论是，此问题不会对我们的用户构成直接风险，并且不足以自行绕过操作系统安全保护。”</p>
<p>值得一提的是，Pacman是在苹果M1芯片中被发现的第三个漏洞。去年5月，安全研究员赫克托马丁 (Hector Martin) 发现了一个名为M1RACLES的漏洞，该漏洞允许两个应用程序秘密交换数据。</p>
<p>上个月，多个大学组成的团队又发现了一个名为 Augury 的漏洞，可导致芯片泄漏静态数据，不过目前还没有展示出任何可行的漏洞利用方法。</p>
<p>但是与前两个漏洞不同的是，Pacman漏洞利用的是M1本身的存在的硬件安全机制PAC，而且该机制还广泛存在于其他Arm架构的处理器当中，这也使得该漏洞可能将会带来更大的影响。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220612/bef2d0bf30a94f389c784c4ab256744f.jpg" target="_blank"><img alt="苹果M1芯片惊现“难以修复”漏洞：ARM处理器或集体沦陷" h="354" src="https://img1.mydrivers.com/img/20220612/s_bef2d0bf30a94f389c784c4ab256744f.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：万南</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/pingguom1.htm">苹果M1</a><a href="https://news.mydrivers.com/tag/loudong.htm">漏洞</a><a href="https://news.mydrivers.com/tag/arm.htm">ARM</a>  </p>
        
</div>
            