
---
title: RISC-V XIP Support Queued Ahead Of Linux 5.13 To "eXecute In Place"
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Fri, 19 Mar 2021 10:28:53 GMT
thumbnail: https://www.phoronix.com/assets/categories/risc-v.jpg
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="RISC-V -- " src="https://www.phoronix.com/assets/categories/risc-v.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
It looks like the <a href="https://www.phoronix.com/scan.php?page=search&q=Linux+5.13">Linux 5.13</a> kernel will be supporting an interesting RISC-V feature this spring.
<br>
<br>Queued up now in RISC-V's "for-next" branch as of this week is support for XIP, or eXecute In Place. RISC-V XIP allows for code to be executed directly from non-volatile storage that is directly addressable by the CPU. RISC-V XIP allows for executing code directly off CPU-addressable storage like QSPI NOR flash memory without first having to load it into system RAM.
<br>
<br>A RISC-V XIP kernel can be run directly from flash but requires the kernel not to be compressed and MMU support must be present and enabled.
<br><blockquote><strong>"Kernel Execute-In-Place from ROM"</strong>
<br>
<br>Execute-In-Place allows the kernel to run from non-volatile storage directly addressable by the CPU, such as NOR flash. This saves RAM  space since the text section of the kernel is not loaded from flash to RAM.  Read-write sections, such as the data section and stack, are still copied to RAM.  The XIP kernel is not compressed since it has to run directly from flash, so it will take more space to store it.  The flash address used to link the kernel object files, and for storing it, is configuration dependent.</blockquote>
<br>More details via <a href="https://git.kernel.org/pub/scm/linux/kernel/git/riscv/linux.git/commit/?h=for-next&id=06c7c914de26c5a4f1418fd54e4dfd0be4215de6">this commit</a> in RISC-V for-next ahead of the Linux 5.13 cycle.  
</div>
            