
---
title: 'Linux Kernel 5.15 发布首个 RC 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0913/191609_ALuW_2720166.png'
author: 开源中国
comments: false
date: Tue, 14 Sep 2021 07:01:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0913/191609_ALuW_2720166.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Linus 在内核邮件列表宣布推出 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flkml.org%2Flkml%2F2021%2F9%2F12%2F310" target="_blank">Linux 5.15-rc1</a>。</p> 
 <p><img src="https://static.oschina.net/uploads/space/2021/0913/191609_ALuW_2720166.png" referrerpolicy="no-referrer"></p> 
 <p>Linus 在公告中称 5.15 并不是一个特别大的版本，因为这是 5.x 系列中 commit 数量最少的一次。</p> 
 <p>新版本主要变化：</p> 
 <ul> 
  <li>引入 Paragon Software 开发的 NTFS3 内核驱动</li> 
 </ul> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-e58cc97d611a8376aee9a5521877f869fac.png" referrerpolicy="no-referrer"></p> 
 <ul> 
  <li>支持使用 <span style="color:#000000">KSMBD 作为内核空间 SMB3 文件服务器</span></li> 
  <li>改进对微软 NTFS 文件系统的支持</li> 
  <li>支持<span style="color:#000000">在上下文切换时选择进入 L1d 缓存刷新</span></li> 
  <li>继续改进对 Apple M1 的支持</li> 
  <li>增加 PassThru DMA 引擎驱动</li> 
  <li><span style="color:#000000">对</span>英特尔<span style="color:#000000"> DG2/Alchemist 和 XeHP 独立显卡的初步支持</span></li> 
  <li><span style="color:#000000">以及新增对许多其他新硬件的支持</span></li> 
 </ul> 
 <p>此外，Linus 还提到了在构建内核时<a href="https://www.oschina.net/news/158833/linux-5-15-use-werror">启用"-Werror"</a>的问题，称此次发布的更新由于这条规则导致了更多的混乱。</p> 
</div>
                                        </div>
                                      
</div>
            