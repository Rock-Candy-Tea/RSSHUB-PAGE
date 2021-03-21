
---
title: Initial Support For The Rust Language Lands In Linux-Next
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Fri, 19 Mar 2021 16:40:59 GMT
thumbnail: https://www.phoronix.com/assets/categories/linuxkernel.jpg
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="LINUX KERNEL -- " src="https://www.phoronix.com/assets/categories/linuxkernel.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
For a long while now Linux kernel developers have discusses the prospects of <a href="https://www.phoronix.com/scan.php?page=news_item&px=Linux-Plumbers-2020-Rust">optionally allowing the Rust language to be used for new device drivers</a> within the Linux kernel areas and other areas within the kernel for this language that prides itself on safety and performance. As the first baby step towards that dream, initial Rust support appeared this week in the Linux-Next tree.
<br>
<br>Announced yesterday on <a href="https://lore.kernel.org/rust-for-linux/CANiq72nbNxpps+p4wYp03ncrbGH9FFoTfHQZwg_vGdPO41eGmQ@mail.gmail.com/t/">rust-for-linux</a> was word of initial Rust support hitting Linux-Next. Miguel Ojeda who has been involved with this effort was quick to note in the announcement, "<em>This does not mean we will make it into mainline, of course, but it is a nice step to make things as smooth as possible. Stephen has kindly agreed to give me a bit of leeway the first few days until the RFC to rebase things as needed, which is very much appreciated.</em>"
<br>
<br>The code <a href="https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/commit/?id=c7c4c9b88eecb28d3b48ba855cd6f9f7391a33b2">merged</a> lays the foundation for building Rust kernel features moving forward. The initial infrastructure is in place and all of the new code residing under <em>rust/</em>. 
<br>
<br>This support is obviously conditional upon a Rust compiler (rustc) being present on the system. As such the current architectures focused on are ARM64 and x86_64. Currently the kernel support needs a recent nightly Rust toolchain for building.
<br>
<br>While no fully-baked Rust kernel driver is ready yet, the initial merge to Linux-Next does include an example kernel module written in Rust. See the merge link above for more details.
<br>
<br>Particularly over the past year excitement around possibly introducing optional Rust support in the kernel heated up. There's been <a href="https://www.phoronix.com/scan.php?page=news_item&px=Linux-Kernel-Rust-Path-LPC2020">much to figure out about allowing Rust in the kernel</a> but last summer at least <a href="https://www.phoronix.com/scan.php?page=news_item&px=Torvalds-Rust-Kernel-K-Build">Linus Torvalds indicated he would be open to Rust in the kernel</a>.
<br>
<br>While Rust is now in Linux-Next, it's not yet clear if/when it will be mainlined. Generally work in Linux-Next bakes until the next cycle but sometimes can stay in Linux-Next longer if it's still a work-in-progress. The code still needs to go through all the merge window pull request formalities and we haven't seen Linus Torvalds provide any fresh take on these Rust efforts. In any case, the effort is moving along and will be interesting to see if this initial Rust infrastructure for the Linux kernel does manage to make it mainline for 5.13 or another kernel release this year.  
</div>
            