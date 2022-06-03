
---
title: 'NTFS3内核驱动迎来久违更新 作者向Linux 5.19发送修复程序'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg'
author: cnBeta
comments: false
date: Fri, 03 Jun 2022 12:28:34 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg'
---

<div>   
在最近关于NTFS3内核驱动的维护问题和其他开发者组织起来加紧维护Paragon软件公司提供的"NTFS3"内核驱动之后，现在已经有一批修复程序准备在Linux 5.19上使用。<br>
 <p><a href="https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg" referrerpolicy="no-referrer"></a></p><p>Paragon软件公司的Konstantin Komarov在因休息和其他事务而离开后，又重新活跃在内核邮件列表中。Komarov今天早上为Linux 5.19的合并窗口提交了一批NTFS3的修正。</p><p>在Linux 5.19的NTFS3驱动修复中，包括解决各种内存泄漏和涉及到内核的问题，包括一些xfstests测试案例的修复以及修复各种内核错误、随机的错别字修正、无用代码删除和其他维护任务。</p><p>关于Linux 5.19的NTFS3修复的完整列表，请参见此拉动请求：</p><p><a href="https://lore.kernel.org/lkml/c5c16f3d-c8a7-96b0-4fd6-056c4159fcef@paragon-software.com/" _src="https://lore.kernel.org/lkml/c5c16f3d-c8a7-96b0-4fd6-056c4159fcef@paragon-software.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="6201570153540451064f015a03554f5b5400524f560406544f525754015653575b040107042212031003050d0c4f110d0416150310074c010d0f">[email protected]</span>/</a><br></p><p>这是自去年Paragon的NTFS3驱动在Linux 5.15中被精简后的第一次范围修复。</p><p>关于当前NTFS3内核驱动功能的细节可以通过kernel.org找到：</p><p><a href="https://www.kernel.org/doc/html/latest/filesystems/ntfs3.html" _src="https://www.kernel.org/doc/html/latest/filesystems/ntfs3.html" target="_blank">https://www.kernel.org/doc/html/latest/filesystems/ntfs3.html</a><br></p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1197145.htm" target="_blank">Linux 5.15版发布 含DG2/Alchemist+Xe HPG初步支持及新NTFS驱动</a></p><p><a href="https://www.cnbeta.com/articles/tech/1262763.htm" target="_blank">去年合并的"新"NTFS Linux驱动因缺乏维护再度引起关注</a></p><p><a href="https://www.cnbeta.com/articles/tech/1263645.htm" target="_blank">Linus Torvalds对NTFS3 Linux驱动无人维护的情况发表评论</a></p></div>   
</div>
            