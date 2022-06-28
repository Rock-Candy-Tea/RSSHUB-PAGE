
---
title: 'Linux Kernel 5.19-rc4 发布，补丁规模较大、修复性能回归问题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0628/071239_aQWX_2720166.png'
author: 开源中国
comments: false
date: Tue, 28 Jun 2022 07:20:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0628/071239_aQWX_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>Linux Kernel 5.19 发布了第 4 个 RC 版本。</p> 
<p>Linus Torvalds 在邮件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flore.kernel.org%2Flkml%2FCAHk-%3DwjRt2bxDDT9-Uq337dAg6jipZfetgSsHejggU%3DJHmyK6A%40mail.gmail.com%2FT%2F%23u" target="_blank">写道</a>：“<span style="background-color:rgba(255, 255, 255, 0.65); color:#000000">在经历了几个相当小的 rc 版本之后，rc4 的 commit 数量量终于增加了。我当然不希望这种情况发生在发布周期中间时段，但考虑到目前的平静情况，这好像并没有什么好惊讶。虽然相比较此前的 rc 版本，5.19-rc4 有点大，也比此前 Linux 版本稍大一点，但并没有接近记录。所以 rc4 只是比平时稍大一点，而不是‘Oh my God, this thing is huge’。</span>”</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0628/071239_aQWX_2720166.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:rgba(255, 255, 255, 0.65); color:#000000">Linux 5.19-rc4 中另一个值得关注的变化是修复了性能回归问题。早在 3 月份的 Linux 5.19 合并窗口期间，</span>Linux 5.18 Stress-NG 中出现了一个很大的 NUMA 回归问题。目前针对该问题的<span style="background-color:rgba(255, 255, 255, 0.65); color:#000000">补丁被合并到了 Linux 5.19-rc4 中，估计也会被回传到 Linux 5.18。这个补丁是"mm: lru_cache_disable: use synchronize_rcu_expedited"的修改。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-10cfb4304399bff31c3c9f23983bcf4e599.png" referrerpolicy="no-referrer"></p> 
<p>最后，按照计划，Linux 5.19 稳定版内核将在七月底发布。</p>
                                        </div>
                                      
</div>
            