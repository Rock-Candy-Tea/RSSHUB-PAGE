
---
title: 'Windows同样无条件保留了前1MB的内存 Linux只是晚了一步'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Wed, 09 Jun 2021 08:05:06 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
上周末，Linux 5.13内核进行了修改，使Linux
x86/x86_64内核开始强制保留最初的1MB内存，以避免一些BIOS和帧缓冲器有时对系统内存的最低部分进行破坏的问题。<strong>虽然人们认为无条件地保留前1MB有点麻烦，而且也许Windows有某种方法来决定保留多少低内存区域，但事实证明，Windows多年来一直采用这种做法。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>虽然Linus Torvalds确认在Linux 5.13中进行了修改，在Linux x86/x86_64系统上保留了第一个1MB的内存，但他评论说："这似乎有点荒谬，这在<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>下是如何运作的？一定有一些我们不知道的关于BIOS影响方面的Windows方面的做法，我已经把它找出来了，看起来确实有一些奇怪的事情正在发生。"</p><p>在人们对这一变化产生兴趣之后，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>一位工程师与Windows团队进行了核实，并在社区评论说，事实上，Windows一直无条件地在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>和<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>系统上保留前1MB的内存，在这一点上他们已经这样做了很多年。"我向Windows团队核实过。Peter Anvin11年前的说法是真的。在英特尔和AMD处理器上，Windows无条件地保留了前一百万字节的内存，减去用于实模式启动的内存页面。这样做是为了解决BIOS带来的错误。"</p><p>因此，看起来Linux将坚持这种新的行为，在x86/x86_64系统中保留第一个1MB的内存，与Windows一同应对BIOS实现过程中的错误。</p><p><a href="https://static.cnbetacdn.com/article/2021/0609/f09201d9e5168ed.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0609/f09201d9e5168ed.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1137347.htm" target="_blank">Linux x86/x86_64现在将始终保留前1MB的内存</a></p></div>   
</div>
            