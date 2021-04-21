
---
title: '因故意插入实验性漏洞 明尼苏达大学开发者被禁止向Linux内核供应代码'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0421/a0b37319bda789a.png'
author: cnBeta
comments: false
date: Wed, 21 Apr 2021 12:00:26 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0421/a0b37319bda789a.png'
---

<div>   
Greg
Kroah-Hartman禁止美国一所大学尝试主线Linux内核补丁，因为它故意提交有安全影响的可疑代码和其他以研究为名的"实验"。源于一篇研究论文，明尼苏达大学的研究人员故意在Linux内核主线中隐秘地引入漏洞。他们为了研究论文，故意在内核中隐蔽地引入用户之后的漏洞。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0421/a0b37319bda789a.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0421/a0b37319bda789a.png" title alt="WR0FCZ7)M05J[6GO]I3FO05.png" referrerpolicy="no-referrer"></a></p><p>但即使在这篇论文之后，明尼苏达大学的研究人员又有了新一轮的补丁，他们声称这来自"一个新的静态分析器"，但没有任何真正的价值。这些新的、有问题的补丁实际上似乎没有任何真正的价值，至少只是在浪费上游开发者的时间。内核维护者Greg揭露了这一伎俩，并禁止这些开发者在未来尝试为Linux内核做贡献。</p><p>Greg今天早上在内核邮件列表中写道："[这些新的补丁]显然不是由一个有智慧的静态分析工具创造的，因为它们都是完全不同的模式的结果，而且所有这些补丁显然根本没有修复任何东西。那么，除了你和你的团队继续通过发送这种无稽之谈的补丁来对内核社区的开发者进行试验之外，我还能想到什么呢？......任何对C语言有一定了解的人都可以看到你提交的补丁根本没有任何作用，所以认为一个工具创造了它们，然后你认为它们是一个有效的 "修复"，这完全是你的疏忽，不是我们的。你才是有错的人，我们的工作不是成为你创造的工具的测试对象......因为这个，我现在不得不禁止你的大学今后的所有贡献，并撤销以前的贡献，因为这显然是以恶意的方式提交的，本身是为了造成问题。</p><p><a href="https://static.cnbetacdn.com/article/2021/0421/aa19b4908adef2d.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0421/aa19b4908adef2d.png" title alt="THY2N9B0UTXJO_P$FUB&#123;W&#125;Y.png" referrerpolicy="no-referrer"></a></p><p>因此，内核维护团队不再欢迎来自明尼苏达大学的贡献者对上游的Linux内核开发提交变动，而明尼苏达大学之前对Linux内核的补丁将被恢复。</p>   
</div>
            