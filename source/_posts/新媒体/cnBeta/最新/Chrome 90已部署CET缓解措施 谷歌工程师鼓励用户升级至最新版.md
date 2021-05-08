
---
title: 'Chrome 90已部署CET缓解措施 谷歌工程师鼓励用户升级至最新版'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0508/fae48a81fdd683c.png'
author: cnBeta
comments: false
date: Sat, 08 May 2021 07:28:28 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0508/fae48a81fdd683c.png'
---

<div>   
<strong>Chrome 平台安全团队工程师 Alex Gough 在周二的一篇博客文章中透露，面向 Windows 平台的 Chrome 90 已经部署了硬件增强型堆栈保护功能。</strong>据悉，微软在今年 3 月宣布了这项 Windows 安全特性。其旨在通过支持“控制流强执技术”（CET）的硬件平台上引入这项技术缓解手段，让黑客更加难以利用 Windows 10 20H1（12 月更新及更高版本系统）上的安全漏洞。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0508/fae48a81fdd683c.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0508/fae48a81fdd683c.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p>支持 CET 技术的处理器，涵盖了<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> 11 代酷睿和 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Zen 3 家族。谷歌推荐 Chrome 浏览器用户立即更新到最新版本，以获得这项至关重要的安全特性。</p><blockquote><p>谷歌解释称：通过部署这项技术缓解措施，处理器将维护一个受新措施保护的有效返回地址堆栈（又称 Shadow Stack / 影子堆栈）。</p><p>在提升了编程的复杂性之后，攻击者利用相关漏洞的难度也将大幅提升。但若将自身加载到 Chrome 中的软件与缓解措施不兼容，则可能影响稳定性。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/0508/8a862fe0957d095.gif" alt="2.gif" referrerpolicy="no-referrer"></p><p style="text-align: center;">返回导向编程（ROP）示意</p><p>对 CET 技术细节感兴趣的朋友，可移步至 <a href="https://security.googleblog.com/2021/05/enabling-hardware-enforced-stack.html" target="_self">Google Security Blog</a> 阅读全文。不过硬件级的堆栈防护，主要还是为了应对在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>推出了“数据执行保护”（DEP）之后、新发明的所谓“返回导向编程”（简称 ROP）攻击。</p><blockquote><p>Alex Gough 表示：。除了现有的堆栈，CPU 还维护着一个影子堆栈。普通程序代码并不能直接操纵该堆栈，而是只能存储返回地址、修改了 CALL 指令，以将返回地址推入普通堆栈和影子堆栈。</p><p>而后返回指令（RET）仍将从普通堆栈获取其返回地址，但会验证它与影子堆栈区域中存储的地址是否相同。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/0508/d9b3151cca55294.gif" alt="3.gif" referrerpolicy="no-referrer"></p><p>若一致，程序将保持不变，且能够像以往那样正常工作。但地址不匹配，则会触发一个可被操作系统（而不是 Chrome 浏览器本体）拦截的异常。</p><p>如此一来，操作系统便有机会修改影子堆栈区域，并允许程序继续运行。虽然这项技术仍有某些局限性，但它至少可以保护用户免受危害更大的恶意攻击。</p><p>如果不确定当前 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 计算机上是否已经更新到了最新版本的 Chrome 浏览器，还请移步至“设置 -> 帮助 -> 关于 Google Chrome”页面查看。</p>   
</div>
            