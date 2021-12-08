
---
title: 'Windows 系统关于用户和权限的逻辑是怎样的？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic2.zhimg.com/v2-99b4577d42061dc5a4cfc498f22a2481_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2021-12-08 00:29:22
thumbnail: 'https://pic2.zhimg.com/v2-99b4577d42061dc5a4cfc498f22a2481_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">


<div class="answer">

<strong>
<img class="avatar" src="https://pic2.zhimg.com/v2-99b4577d42061dc5a4cfc498f22a2481_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">Serendipity，</span><span class="bio">星星还是要还给宇宙的</span>
<a href="https://www.zhihu.com/question/66229405/answer/2257838074" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>1983 年，微软开始研发 Windows 系统，第一个版本的 Windows 1.0<sup>[1]</sup>于 1985 年问世，1987 年，微软推出了 Windows 2.0，此后，直到 1990 年 5 月 22 日，微软迎来了第一个具有时代意义的作品——Windows 3.0。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-ddf2372de92dc2e9d50fc4464b61ffdd_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>Windows 1.0</figcaption></figure>
<p>而在此之前，微软早已开始研究基于 NT 内核的 Windows NT 系统了<sup>[2]</sup>，并在 1988 年 11 月开始了对于“WinNT”（即第一代的 Windows NT 3.1）的产品研发。</p>
<p>Windows NT 是基于 OS/2 NT 的基础编制的，体系结构是一种分层设计，由两个主要组件组成，用户模式和内核模式。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-52fb5df54f5fe3d5d27d61d90db31609_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>https://zh.wikipedia.org/wiki/File:Windows_2000_architecture.svg</figcaption></figure>
<p>可以看到，上图用户模式（User mode）和内核模式（Kernel Mode）有明显的分隔，上方用户模式的进程都运行在受保护的进程地址空间，通过 ntdll.dll 将 Win32 函数的调用转换为非文档化的系统内部函数调用，经过 SSDT（系统服务描述表）后从 ring3 层进入 ring0 层执行<sup>[3]</sup>。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-fde56d8249a87ba73696acbb6c913601_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>（ring 是用户模式和系统模式在硬件上的实现）。</figcaption></figure>
<p>用户模式下，对对象的访问都要经过系统的安全审核，内核模式的权限则提高了很多<sup>[4]</sup>。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-13c4ab899abdfff5c15884e257cea6c5_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>Microsoft Windows 2000 是沿袭微软公司 Windows NT 系列的 32 位视窗操作系统，是 Windows 操作系统发展的一个新里程碑，Windows 2000 起初称为 Windows NT 5.0。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-d5152130e01d55872304fec34fda6c0e_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>Windows 2000 引入了 NTFS 3.0、加密文件系统、动态逻辑磁盘管理等机制，但就安全性而言，还是太弱，正因如此，其成为许多高危电脑病毒的攻击目标，像是知名的红色代码（Code Red）和 Nimda 病毒等。</p>
<p>2001 年发布的 Windows XP，在 Windows 2000 的基础上进行了更多的安全性改进。如果以受限账户登陆，那么在 ACL 的限制下，病毒程序将不能修改系统的关键数据。然而，受限账户限制太多，比如无法安装应用程序，无法修改系统设置等，因此，XP 用户在大多数情况下，其实都是以管理员账户的身份来进行日常操作的。</p>
<p>2003 年 8 月，冲击波（Worm.Blaster）病毒<sup>[5]</sup>利用 RPC 服务漏洞全球爆发，感染该病毒后，将出现系统无故重启、无法正常上网等现象。2004 年 5 月，震荡波（Worm.Sasser）病毒利用 LSASS 服务漏洞全球爆发，感染该病毒后将出现系统反复重启、电脑运行缓慢等现象<sup>[6]</sup>。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-ff2729d157882b9f2f235a9673a4ee40_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>那个时候，Windows XP 逐渐普及起来。然而，由于 Windows XP 经常出现安全漏洞以及易受恶意软件、电脑病毒、缓存溢出等问题的影响，接连出现全球安全风暴，微软陷入严重信任危机。</p>
<p>这件事带来两个影响，首先是微软检讨后开始提出“可信计算”的概念，而关于这项技术的讨论，到现在也没有停止。</p>
<p>这项技术的拥护者，称它将会使计算机更加安全、更加不易被病毒和恶意软件侵害，因此从最终用户角度来看也更加可靠。</p>
<p>而反对者则认为，可信计算背后的那些公司并不那么值得信任，这项技术给系统和软件设计者过多的权利和控制。他们还认为可信计算会潜在地迫使用户的在线交互过程失去匿名性，并强制推行一些不必要的技术。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-229ecf298078f128861bbbf7fd10fca6_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>第二个影响在于，Windows XP SP2 最终于 2004 年 8 月推出，包含了加强版的 Windows 防火墙、Internet Explorer 6（新增弹窗拦截），且新增了数据执行保护（DEP）、Windows 安全中心等功能，支持蓝牙技术和改良对 Wi-Fi 的支持。</p>
<p>此时，Windows 的安全机制主要靠定期向病毒木马样本库中添加 signature 来查杀，辅之 hook 关键的系统函数，以方便在用户 down 文件或者打开 exe 时查杀木马。</p>
<p><strong>但是，由于系统本身缺乏在管理员模式下对应用程序的行为限制，导致木马、病毒仍然层出不穷，盗号和损害系统的行为依然到处可见。</strong></p>
<p>例如，许多 RAT 可以很直接地通过调用 NtUserGetAsyncKeyState 或者 NtUserGetRawInputData 来获取用户输入，亦或者通过调用 NtUserSetWindowsHookEx 来注册消息回调函数，作为应对手段，许多软件都必须加载键盘过滤驱动来避免木马窃取账号信息。<sup>[7]</sup></p>
<p>前文说到，Windows XP SP2 引入了数据执行保护（DEP）机制，可以防止应用运行用于暂存指令的那部分内存中的数据，从而保护电脑。</p>
<p>而在此之前，分给某一进程的全部内存空间都是可读写并且可执行的，但 DEP 允许系统将一页或多页内存标记为不可执行文件。 将内存区域标记为不可执行意味着不能从该内存区域运行代码，这会使对缓冲区溢出的利用变得更困难。当然，攻击者们也有新的入侵手段，例如通过调用系统内部的函数，将注入的恶意代码标记为可执行的，这样便可绕过 XP SP2 引入的数据执行保护（DEP）机制了。</p>
<p><strong>Windows XP 之后的下一代操作系统是 Windows Vista，这是用户权限变化最为明显的一次。</strong></p>
<p>较之 XP，Vista 增加了用户管理机制（UAC）以及内置的恶意软件查杀工具（Windows Defender），以便实现——即便用户以管理员账户的身份登陆操作系统，系统也能在有效程度上防止病毒程序获得高权限并以此来对系统造成严重破坏——高权限必然带来高破坏。直到现在，提权也是入侵之后必不可少的手段。</p>
<p>此外，微软还在 Vista 系统中引入了名为 ASLR（Address Space Layout Randomization，地址空间布局随机化）的技术，随机化地打乱地址空间，来防止黑客的入侵。</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-4321cad8161981bd3053a62931f06fd3_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>当然，ASLR 也并非无懈可击，在出现了某些漏洞，比如内存信息泄露的情况下，攻击者会得到部分内存信息，比如某些代码指针。传统的 ASLR 只随机化整个 segment，比如栈，堆，或者代码区。这时候攻击者可以通过泄露的地址信息来推导别的信息，比如另外一个函数的地址，等等。这样整个 segment 的地址都可以推导出来，进而得到更多信息，大大增加了攻击利用的成功率<sup>[8]</sup>。</p>
<p>Flash 应用，还有过时的 Java 等，都可以绕过 ASLR 的限制，进而突破数据执行保护。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-1d84502db8dd33a116b64d9dc14a9673_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>而且，在 32 位系统中，由于随机的熵值不高，攻击者也容易通过穷举猜出地址</p>
<p>接着，为了兼容性考虑，对一部分文件的加载位置并未做随机化，而这也为 ASLR 的被攻克留下了机会<sup>[9]</sup>。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-8a1070f49d28c1f6273bbd610b48a49a_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>此外，2005 年，在 Windows XP 与 Windows Server 2003 Service Pack 1 的 64 位版本中，首次推出内核补丁保护（Kernel Patch Protection）机制，防止对内核的修补<sup>[10]</sup>。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-b180796e8c781d82e471a5fb48789d39_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>话接上文，Windows XP 默认提供给用户管理员账号，但从 Vista 开始，默认情况下标准用户和管理员都会在标准用户安全上下文中访问资源和运行程序。用户登录系统之后，不仅会分配到一个 session，还会创建一个访问令牌（token），这个令牌中包含授权给该用户的访问权限信息，比如对应的 Windows 权限和安全标识符（SID）等。</p>
<p>如果登陆账户是 Administrators 组的成员，系传统会为之创建两个单独的令牌：标准用户访问令牌和管理员访问令牌。标准用户访问令牌包含的用户特定信息与管理员访问令牌包含的信息相同，但是已经删除管理 Windows 权限和 SID，标准用户访问令牌用于启动不执行管理任务的应用程序。</p>
<p>默认情况下，将用户的权限控制在标准用户访问令牌之内，当需要写入文件，或者运行特定程序时，便需要管理员权限，这时只有申请到管理员令牌，才能进行相应的高权限操作如运行 or 写入文件。</p>
<p><strong>Windows Vista 企图赋予用户两方面的好处，一方面是允许管理员在标准用户的上下文环境下执行大部分的进程，仅通过用户准许来提升他们的用户令牌的特权，另外，允许标准用户通过选择提升一个进程，使用管理员级别的身份来执行管理员的任务。</strong></p>
<p>此外，除了 ASLR 和 UAC，ACL、MIC 和 UIPI 等机制对用户和进程权限进行限制。例如，即使遵守 ACL 机制，进程的行为也需要进行检查，主要查看进程和资源对象的完整性级别，完整性级别低的进程，不能写入到完整性级别比之高的资源对象中去。</p>
<p>但是，过多且繁琐的管理员权限申请，使得大多数用户十分不耐烦，也正因如此，很多杂志把禁用 UAC 视作是对于 Vista 的一大优化，正如现如今，禁用 WIN10 的自动更新被指为是对于 WIN10 系统的优化，但我建议你不要那么做，详见下面的回答：</p>
<p><a class="internal" href="https://www.zhihu.com/question/26443384/answer/2233580548">为什么这两年没再听说有什么大规模的电脑病毒爆发？</a></p>
<p>接着，Windows 8 中引入了 AppContainer 的机制，主推运行在 AppContainer 中的 Metro 应用，这一项机制直到 WIN 10 还在使用，例如下图就是我在自己的 WIN 10 虚拟机上用 Process monitor<sup>[11]</sup>查看得到的信息，你可以看到 integrity 一栏明显的 AppContainer。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-e26cd23fa4e51378bb42739930700811_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>我的 WIN 10 虚拟机</figcaption></figure>
<p>从 Windows 8 引入 Metro(Morden) App 开始，Windows 出现了一个新的进程隔离机制，即 AppContainer。Windows Store 应用运行在 AppContainer 的容器当中权限被极大的限制，很多危险的操作无法进行，微软通过 Windows Store 进行应用分发，能够控制来源，这样能够极大的降低恶意软件的困扰，而 AppContainer 同样能够支持传统的 Desktop 应用<sup>[12]</sup>。</p>
<blockquote>隔离是 AppContainer 执行环境的主要目标。通过将应用程序与不需要的资源和其他应用程序隔离，可以最大限度地减少恶意操作的机会。基于最低权限授予访问权限可防止应用程序和用户访问超出其权限的资源。控制对资源的访问可以保护进程、设备和网络。<br><br>Windows 中的大多数漏洞都始于应用程序。一些常见示例包括应用程序脱离其浏览器或向 Internet Explorer 发送错误文档以及利用插件（如 Flash）。这些应用程序在 AppContainer 中隔离的越多，设备和资源就越安全。即使应用程序中的漏洞被利用，该应用程序也无法访问超出授予 AppContainer 的资源。恶意应用程序无法接管机器的其余部分。<br><br></blockquote>
<p><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//docs.microsoft.com/en-us/windows/win32/secauthz/appcontainer-isolation" target="_blank" rel="nofollow noreferrer">AppContainer Isolation - Win32 apps</a></p>
<p>Windows 8 中，大量加入了 ASLR 机制，强制所有 DLL 进行 ASLR 方式的内存载入方式，硬件 ASLR 和 HEASLR 等......</p>
<p>Windows 10 中，加入了以下内置的安全特性：</p>
<ul>
<li>In-place 升级</li>
<li>Stay Current 保持最新</li>
<li>UPAO (User Protection Always On)</li>
<li>Secure ETW Channel（安全 ETW 通道）</li>
<li>Lockdown Mode 和虚拟化安全</li>
<li>AMSI (Antimalware Scan Interface)</li>
<li>WinRE Offline 扫描</li>
<li>CFG（控制流保护）</li>
</ul>
<p>总结一下：Windows XP 以后，也就是自 Windows Vista 起，乃至之后的 Windows 7、Windows 8 、Windows 10，登陆账户是管理员，不代表用户默认使用管理员权限来执行所有操作，在普通用户权限下执行的操作不在少数，仍有很多运行和修改操作需要申请“管理员权限”，例如写入只读文件，运行某些特定<sup>[13]</sup>进程。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-7e48a1e9eedff7abee673924846d4022_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p><strong>参考</strong></p>
<ol>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">https://en.wikipedia.org/wiki/Windows_1.0x</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">https://zh.wikipedia.org/wiki/Windows_NT</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">https://blog.csdn.net/qq_35191331/article/details/75557567</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">https://www.cnblogs.com/william-dai/p/10897905.html</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">https://baike.baidu.com/item/%E5%86%B2%E5%87%BB%E6%B3%A2%E7%97%85%E6%AF%92/11036738?fr=aladdin</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">https://www.williamlong.info/archives/3362.html</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">https://en.wikipedia.org/wiki/Windows_1.0x</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">https://zhuanlan.zhihu.com/p/25292204</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">http://www.inforsec.org/wp/?p=1009</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">https://docs.microsoft.com/zh-cn/windows/win32/memory/data-execution-prevention</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">https://docs.microsoft.com/en-us/sysinternals/downloads/procmon</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">https://docs.microsoft.com/en-us/windows/win32/secauthz/appcontainer-isolation</a></li>
<li> <a href="https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F66229405%2Fanswer%2F2257838074" target="_blank" rel="noopener noreferrer">http://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/Architecture_of_Windows_NT</a></li>
</ol>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/66229405">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            