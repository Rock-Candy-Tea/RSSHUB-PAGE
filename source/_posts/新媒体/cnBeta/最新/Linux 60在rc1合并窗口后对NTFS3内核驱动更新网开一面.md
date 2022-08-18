
---
title: 'Linux 6.0在rc1合并窗口后对NTFS3内核驱动更新网开一面'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg'
author: cnBeta
comments: false
date: Thu, 18 Aug 2022 04:31:17 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg'
---

<div>   
<strong>由 Paragon Software 开源的 NTFS3，是现代 Linux 内核中的 NFTS 文件系统的读 / 写驱动程序。</strong>随着上一个 Linux 合并窗口在 6.0-rc1 版本发布时结束，我们也看到了一些针对 Linux 6.0 的后期代码重构和修复。但在常规的两周时间里，Paragon Software 并未带来新功能代码和其它非严格 bug 的修复。<br>
 <p><a href="https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg" referrerpolicy="no-referrer"></a></p><p>与今年早些时候的少量 NTFS3 维护相比，这次它晚了好几天。</p><p>即便如此，Paragon Software 的 NTFS3 维护者 Konstantin Komarov，还是在 rc-1 合并窗口关闭几天后，提交了一批 NTFS3 代码重构和 bug 修复。</p><p>由查询请求（<a href="https://lore.kernel.org/lkml/db8cb5d9-56d6-a00a-9cf0-4deec9056433@paragon-software.com/" target="_self">pull request</a>）可知，其修复了 NTFS3 的几个逻辑错误、解决了与 xfstests 有关的部分问题、以及删除 / 重构了一些代码。</p><p><img src="https://static.cnbetacdn.com/article/2022/0818/ddf8dca628cfbb4.png" referrerpolicy="no-referrer"></p><p>虽然迟早的更新算不上是严格意义上的 bug 修复，Linus Torvalds 还是对 Paragon Software 的工作给予了<a href="https://lore.kernel.org/lkml/CAHk-=wg53xW_ppC5w_tDvWKn3Q7i-hWmd09KM-O1npQHWoBBGw@mail.gmail.com/" target="_self">如下评价</a>：</p><blockquote><p>是的，这里本该有几个正经的修复。但至少，我们有看到新开发的 FALLOC_FL_INSERT_RANGE 。</p><p>至于其余部分，似乎大多仅为重构和清理 —— 这些内容本该在上一个合并窗口期内出现。</p><p>不过鉴于这些事情只涉及 NTFS3 本身，我们认为相关实验还是相当可靠的。</p><p>但愿到下一轮的时候 —— 无论是清理还是实际的新代码 —— 还请记得准时靠谱一点。</p></blockquote><p>综上所述，至少在 Linux 6.0 中，针对 NTFS3 的这些微小变更仍会被吸纳，以改进<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>主导的 NFTS 文件系统的开源读 / 写内核驱动。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1174749.htm" target="_blank">Linux Kernel 5.15将整合NTFS3驱动 更好支持NTFS文件系统</a></p><p><a href="https://www.cnbeta.com/articles/tech/1263645.htm" target="_blank">Linus Torvalds对NTFS3 Linux驱动无人维护的情况发表评论</a></p><p><a href="https://www.cnbeta.com/articles/tech/1276877.htm" target="_blank">NTFS3内核驱动迎来久违更新 作者向Linux 5.19发送修复程序</a></p></div>   
</div>
            