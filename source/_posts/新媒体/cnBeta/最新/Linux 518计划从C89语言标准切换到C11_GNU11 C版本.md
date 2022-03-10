
---
title: 'Linux 5.18计划从C89语言标准切换到C11_GNU11 C版本'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0310/3285fc8ab5dad25.jpg'
author: cnBeta
comments: false
date: Thu, 10 Mar 2022 13:14:02 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0310/3285fc8ab5dad25.jpg'
---

<div>   
在内核变化的背后，当Linus
Torvalds有了动力，新的变化往往发生得更快，最新的例子是从C89语言标准切换到C11（GNU11）。这一变化现在有望在Linux
5.18合并窗口的早期进行。最近有关于Linux内核从C89转向C11的讨论非常热烈。目前内核的C语言编程被限制在旧的C89标准上，而最新主线版本的目标是将其提升到更现代的C11。<br>
 <p>由于Linux 5.15已经将GCC编译器的版本要求提高到了GCC 5.1，他们可以安全地开始引入C11/GNU11语言特性，而不需要施加任何新的编译器要求。</p><p>在快速修订了用于将构建Linux内核的"-std=gnu89"目标改为"-std=gnu11"目标的补丁集之后，Linus Torvalds指出，他希望尽早将其拉入下一个合并窗口，以防其他拉动请求最终使用C11功能，等等。转换到C11将发生在即将到来的周期即Linux 5.18。</p><p><img src="https://static.cnbetacdn.com/article/2022/0310/3285fc8ab5dad25.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>现在有linux-kbuild的kbuild-gnu11分支，它将在早期被送入Linux 5.18的合并窗口。如果Linux 5.17在周日按时发布，该合并窗口将在下周启动。</p><p><strong>了解更多：</strong></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/masahiroy/linux-kbuild.git/log/?h=kbuild-gnu11" _src="https://git.kernel.org/pub/scm/linux/kernel/git/masahiroy/linux-kbuild.git/log/?h=kbuild-gnu11" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/masahiroy/linux-kbuild.git/log/?h=kbuild-gnu11</a><br></p>   
</div>
            