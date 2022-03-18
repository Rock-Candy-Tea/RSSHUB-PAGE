
---
title: 'Linus Torvalds计划将Linux内核迁移至现代C语言'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=7678'
author: Dockone
comments: false
date: 2022-03-18 03:13:10
thumbnail: 'https://picsum.photos/400/300?random=7678'
---

<div>   
<br>在此之前，Linux的内核基础为古老的C89标准；如今，Torvalds决定升级至2011年发布的、更为现代的C11标准。<br>
<br>大家都知道，Linux是由C语言编写而成。但各位可能不太了解，这里使用的是一种早已过时的C方言：C语言标准的1989年版本，即C89，也称ANSI X3.159-1989或ANSI C。Linus Torvalds当然知晓这一切，并决定将Linux的官方C版本更新至2011年发布的C11标准。<br>
<br>这次调整其实并不像听起来那么夸张，毕竟C89时至今日仍然拥有普遍支持。由于一切C编译器都能向下兼容早期版本，所以C89程序在编译或者运行上不会出现任何问题。换句话说，任何兼容C11的编译器都能顺利兼容C89遗留代码。<br>
<br>既然如此，干嘛还要费这个劲呢？理由也很简单，旧版本无法提供新版本中的很多实用功能。<br>
<br>这种情况当然引起了Torvalds的注意。当时有人打算修复内核链表primitive中预测执行函数的潜在安全问题，却发现补丁中存在另一个问题。在尝试修复时，Torvalds意识到在C89当中，传递给链表遍历宏的迭代器必须在循环本体之外的范围进行声明。<br>
<br>Torvalds随后写信给Linux内核邮件列表（LKML），认为“之所以会引发这种非预测性bug，原因就是C89当中根本不存在「循环声明变量」这种东西。正是因为无法在循环之内声明迭代器变量，list_for_each_entry() -这类宏在本质上总会把最后一个HEAD条目泄漏到循环以外。”<br>
<br>如何解决？把C89迁移至更新的C语言标准就能彻底消灭这类问题。所以，“是时候考虑转向C99标准了——虽然这项标准也已有20多年历史，但至少比C88更新、能够支持块级变量声明。”<br>
<br>Linux内核开发人员Arnd Bergmann认可这项计划的可行性，并补充称不如直接升级到2011年的C11标准。这主要是考虑到C99的流行度并不太高，而C11引入了标准化多线程支持并增强了安全性，所以最好能一步到位。<br>
<br>直上C11并不困难。就连Linux内核中的最小C编译器GCC 5.1都能够支持C11。这个理由说服了Torvalds，“这个问题已经酝酿了很多年，我真的很希望能迈出这一步。”<br>
<br>随后，在确保新的C标准能够在内核中正常工作之后，Torvalds决定按下“发射按钮”，表示“让我们在5.18合并窗口的早期尝试一下。”考虑到5.18合并窗口即将到来，所以最早可能在3月份就可能在内核中见到C11的身影。<br>
<br>但事情真能这么顺利吗？Linux内核开发人员兼记者Jonathan Corbet警告称，“千万要注意，在合并窗口与5.18发布之间可能会出现很多问题。语言标准版本的升级有可能在内核中某些不为人知的角落引发bug，所以必须尽早发现问题才能保证及时进行版本还原。但如果一切真的进展顺利，下一个Linux内核版本将正式转向C11。”<br>
<br><strong>原文链接：<a href="https://www.zdnet.com/article/linus-torvalds-prepares-to-move-the-linux-kernel-to-modern-c/">Linus Torvalds prepares to move the Linux kernel to modern C</a></strong>
                                
                                                              
</div>
            