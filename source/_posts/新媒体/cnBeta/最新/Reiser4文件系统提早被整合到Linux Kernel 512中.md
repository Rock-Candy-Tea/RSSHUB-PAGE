
---
title: 'Reiser4文件系统提早被整合到Linux Kernel 5.12中'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0408/cd0960b76f7a35a.jpg'
author: cnBeta
comments: false
date: Thu, 08 Apr 2021 07:51:05 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0408/cd0960b76f7a35a.jpg'
---

<div>   
树外（out-of-tree）的 Reiser4 文件系统通常情况下只有在首发稳定版发布之后，才会移植到 Linux Kernel 新版中。<strong>不过这次 Reiser4 已经提前移植到即将发布的 Linux Kernel 5.12 中。</strong><br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0408/cd0960b76f7a35a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0408/cd0960b76f7a35a.jpg" alt="n7wh8epj.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">这主要是因为在 Linux 5.11 版本中并没有完成合适的 Reiser4 补丁，而现在为了继承其 Linux 5.10 的移植，现在的代码已经针对当前的 Linux 5.12 Git 状态进行了重新编译。</p><p style="text-align: left;">这个更新后的文件系统驱动不得不围绕着一个被废弃的读文件操作修改代码，放弃使用一个被移除的上游宏，并对现有的 Reiser4 函数进行了一些修改。假设没有在最后一刻对 Linux 5.12 的接口进行修改，这个 Reiser4 的移植应该能够在本月晚些时候的Linux 5.12稳定版中继续工作。</p><p style="text-align: left;">截至写稿时，实验性的 "Reiser5 "代码还没有针对Linux 5.12的源码树进行重新编译。</p>   
</div>
            