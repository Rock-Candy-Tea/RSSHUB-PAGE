
---
title: '英特尔并不惧怕新的Spectre漏洞 但研究人员称不应该把工作推给程序员'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0501/9b04f214d9845ec.jpg'
author: cnBeta
comments: false
date: Tue, 04 May 2021 11:37:42 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0501/9b04f214d9845ec.jpg'
---

<div>   
几天前，一份报告公布了三个新的Spectre漏洞，这些漏洞存在于所有现代处理器的微操作缓存中。在媒体TechSpot写完这篇报道后不久，英特尔联系到了他们，称官方并不认为新的漏洞是一个大问题。他们的官方声明是这样写的：<br>
<p>"<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>审查了该报告，并告知研究人员，现有的缓解措施没有被绕过，这种情况在我们的安全编码指南中得到了解决。遵循我们的指导的软件已经有针对附带通道的保护措施，包括uop缓存附带通道。不需要新的缓解措施或指导。"</p><p>简单地说，在更新的硬件上运行的更新软件应该不受新漏洞的影响。随后媒体询问了发现这些漏洞和利用的团队的助理教授Ashish Venkat对英特尔的声明的看法。他承认，英特尔一些现有对策的是有效的。英特尔的安全编码指南推荐了三条原则来防止侧通道攻击。它们是由程序员来实施的。如果它们都被正确采用，那么它们可以保护软件免受所有传统的侧信道攻击和大多数投机执行的侧信道攻击，包括微操作缓存攻击。</p><p><a href="https://static.cnbetacdn.com/thumb/article/2021/0501/9b04f214d9845ec.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0501/9b04f214d9845ec.jpg" referrerpolicy="no-referrer"></a></p><p><strong>三原则如下：</strong><br></p><p>确保运行时间与秘密值无关。</p><p>确保代码访问模式与秘密值无关。</p><p>确保数据访问模式与秘密值无关。</p><p>从理论上讲，这些原则很简单，但英特尔承认，它们在实践中可能很难实现。带有优化器的编译器有时会打破这些原则，使代码更有效率的同时从而重新引入漏洞。Venkat和他的团队不喜欢英特尔依靠程序员来更新他们的软件，因为他们所发现的漏洞最终是一个硬件问题。</p><p>Venkat说："恒定时间编程不仅在实际的程序员工作方面很难，而且还需要性能的开销和与修补所有敏感软件有关的重大部署挑战。使用恒定时间原则编写的代码的比例实际上是相当小的。依靠这一点将是危险的。这就是为什么我们仍然需要确保硬件的安全"。</p><p>政府部门、银行和大公司不愿意更新他们的底层软件是臭名昭著的，而这些漏洞给这些组织带来的风险最大，因为他们的服务器同时运行着很多不同的软件，而且他们要处理大量的机密。</p><p>对于普通用户，Venkat表示他们 "应该继续关注他们最脆弱的地方，包括互联网上的病毒和恶意软件"。但是，为了确保每个人使用的数字服务的安全，硬件供应商需要重新强调硬件安全的前进方向。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1110567.htm" target="_blank">AMD承认Zen 3 CPU易受新型类Spectre攻击影响 但暂时问题不大</a></p><p><a href="https://www.cnbeta.com/articles/tech/1122539.htm" target="_blank">新的Spectre变种被发现可利用CPU微操作缓存来窃取数据</a></p></div>   
</div>
            