
---
title: 'Linux 5.18-rc3 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9014'
author: 开源中国
comments: false
date: Mon, 18 Apr 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9014'
---

<div>   
<div class="content">
                                                                                            <p>Linux 5.18-rc3 已作为每周候选版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flore.kernel.org%2Flkml%2FCAHk-%3DwgBR6P8EseYMjfMjxQ_oTpoQmL0qvKpAw04kP-HBgSGFg%40mail.gmail.com%2F" target="_blank">发布</a>了！这个候选版本没有特别明显的功能变化，都是一些底层的驱动更新和性能调优。对于 Linux 5.18-rc3 带来的改动，Linus Torvalds 评论道：</p> 
<blockquote> 
 <p>事情看起来仍然很正常，虽然 diffstat 可能看起来有点奇怪，因为一些电子邮件更新，导致了设备树文件中有很多展开的单行更新。</p> 
 <p>还有一系列声卡探测的 Bug 处理修复（“修复探测错误时丢失的 snd_card_free() 调用")  ，在许多声音驱动程序中显示为好几行。</p> 
</blockquote> 
<p>该版本还包含一些<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flore.kernel.org%2Flkml%2F165018953883.44773.12883227528447853271.tglx%40xen13%2FT%2F%23u" target="_blank">英特尔 TSX 修复程序</a>，这些补丁修复了一系列安全问题，比如系统可能容易受到 TSX 异步中止“TAA”漏洞的影响，这些 TSX 修复也将向后移植到稳定的内核。</p> 
<p>有关该候选版本的每个更新项，请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flore.kernel.org%2Flkml%2FCAHk-%3DwgBR6P8EseYMjfMjxQ_oTpoQmL0qvKpAw04kP-HBgSGFg%40mail.gmail.com%2F" target="_blank">5.18-rc3 公告</a> 。</p>
                                        </div>
                                      
</div>
            