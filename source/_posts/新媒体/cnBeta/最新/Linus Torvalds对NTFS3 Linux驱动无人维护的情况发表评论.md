
---
title: 'Linus Torvalds对NTFS3 Linux驱动无人维护的情况发表评论'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0428/d372a669b6796f5.png'
author: cnBeta
comments: false
date: Thu, 28 Apr 2022 12:41:54 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0428/d372a669b6796f5.png'
---

<div>   
正如本周早些时候所写的，人们对"新的"NTFS Linux驱动程序提出了担忧，因为它在被纳入主流不到一年的时间里实际上就没有得到维护。<strong>此后，Linus Torvalds对此事发表了评论，并为其他开发者维护它的想法加油鼓劲。</strong><br>
<p><a href="https://static.cnbetacdn.com/article/2022/0428/d372a669b6796f5.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0428/d372a669b6796f5.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p>自从该驱动去年在Linux 5.15中最终被主线化以来，还没有任何重大的错误修复被送入驱动。该驱动最初是由Paragon软件公司开发的专有驱动，去年在Paragon的Git树上看到了一些修复，但从未提交给主线。其他开发者试图联系NTFS3的维护者，但都没有成功。因此引发了本周关于这个NTFS开源Linux驱动的公开讨论，该驱动提供了读/写支持和其他现有NTFS Linux驱动所不具备的功能，而且比基于FUSE的替代方案更好。</p><p>一些人假设缺乏NTFS3驱动的维护可能是俄罗斯-乌克兰战争的后果，俄罗斯的开发者参与其中。然而，这种缺乏上游错误修复提交和对其他开发者询问的回应可以追溯到去年第四季度，远在冲突开始之前。</p><p><a href="https://static.cnbetacdn.com/article/2022/0426/836a4e0244c8ae1.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/0426/836a4e0244c8ae1.jpg" referrerpolicy="no-referrer"></a></p><p>Linus Torvalds昨天对这个话题发表了评论。Kari Argillander在内核邮件列表中发起了关于这种情况的帖子，他在NTFS3驱动被精简的时候为其提供了补丁，甚至在他试图与Paragon开发者接触的时候提出成为共同维护者。Linus Torvalds为Kari敞开了大门，让他和其他感兴趣的内核开发者一起接管驱动的维护工作。基本上，如果原来的维护者Konstantin Komarov不能或没有兴趣继续维护上游内核的驱动程序，他将愿意接受其他开发者的拉取请求。</p><p><strong>Linus Torvalds的发言原文如下：</strong></p><blockquote><p>如果你愿意维护它（也许还能找到其他志同道合的人帮助你），我想这肯定是一件值得尝试的事情。</p><p>如果我们能找到*没有人*来关心和维护它，那么我想我们应该删除它，而不是最后有两个*有效的未维护的NTFS驱动副本。</p><p>并不是说两个未维护的文件系统比一个差得多 :-P</p></blockquote><p>那位正在寻求改进以前的NTFS Linux驱动的开发者Namjae Jeon随后回应，"我目前正在研究对只读NTFS(fs/ntfs)的写支持，目标是在几个月内发布。而在那之后，我正计划在ntfs-3g的ntfsprogs中开始工作fsck，以解决目前缺乏实用性的问题。"</p><p>接下来，我们将看到NTFS Linux的情况在今年如何发展。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1262763.htm" target="_blank">去年合并的"新"NTFS Linux驱动因缺乏维护再度引起关注</a></p></div>   
</div>
            