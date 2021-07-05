
---
title: 'Linux 5.14解决了​某些数码相机exFAT文件系统的兼容性问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Mon, 05 Jul 2021 11:49:09 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
早在2019年底的Linux 5.4版本中合并了exFAT文件系统驱动，在微软的协助下，由三星主导的工作在这个阶段已经被证明是相当成熟的。鉴于exFAT文件系统的成熟度，在最近的内核版本中没有太多的exFAT文件系统驱动变化。<br>
<p>即使在Linux 5.14中，也只有两个exFAT补丁，但至少对一些用户来说是值得注意的，因为它修复了文件系统与一些数码相机的兼容性。</p><p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>Linux 5.14的exFAT带来了与一些数码相机的exFAT文件系统的兼容性改进。特别是当在Linux下挂载某些数码相机的exFAT文件系统时，在某些情况下，并非所有的文件都能在Linux下显示出来。</p><p>这个问题似乎最终与数码相机的固件有关，而不是与Linux有关，这是因为在某些情况下，目录的流条目中的数据长度没有得到更新。这意味着问题出现时，Linux不会显示出特定目录中的所有文件。</p><p>现在，在Linux 5.14的exFAT驱动补丁中，有一个补丁可以处理exFAT读取目录功能中错误的流条目大小，这个修复/解决方法也将被回传到稳定版内核。</p><p>这个 "丢失文件"的问题似乎至少发生在一些富士数码相机上，而供应商是否会更新他们的exFAT文件系统还有待观察，因为在这种情况下，他们才是不符合规范的一方。</p><p><strong>了解更多：</strong></p><p><a href="https://lore.kernel.org/lkml/002c01d7714d$a8699070$f93cb150$@samsung.com/" _src="https://lore.kernel.org/lkml/002c01d7714d$a8699070$f93cb150$@samsung.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="6959595b0a59580d5e5e585d0d4d08515f5050595e594d0f505a0a0b585c594d291a08041a1c070e470a0604">[email protected]</span>/</a><br></p>   
</div>
            