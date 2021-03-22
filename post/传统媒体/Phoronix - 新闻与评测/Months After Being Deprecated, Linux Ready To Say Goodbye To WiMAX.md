
---
title: Months After Being Deprecated, Linux Ready To Say Goodbye To WiMAX
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Sun, 21 Mar 2021 13:15:00 GMT
thumbnail: 'https://www.phoronix.com/assets/categories/linuxnetworking.jpg'
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="LINUX NETWORKING -- " src="https://www.phoronix.com/assets/categories/linuxnetworking.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
In addition to <a href="https://www.phoronix.com/scan.php?page=news_item&px=Linux-Drop-Legacy-IDE-2021">the legacy IDE driver code ready to go</a> from the mainline Linux kernel, receiving its final death sentence now is also the <a href="https://www.phoronix.com/scan.php?page=search&q=WiMAX">WiMAX</a> support.
<br>
<br>With Linux 5.11 the kernel <a href="https://www.phoronix.com/scan.php?page=news_item&px=Linux-5.11-WiMAX-Demoted">demoted the WiMAX networking code</a> down to the "staging" area of the kernel with a plan to remove it should no one step up to maintain the code. Well, no one cares enough about WiMAX support to maintain it, so the kernel support is set to be removed with Linux 5.13.
<br><p align="center"><img src="https://www.phoronix.net/image.php?id=962&image=ces_2008d0_03" referrerpolicy="no-referrer"><br><em>Riding around in some Intel vehicles back at CES 2008 was the only time we ever got to make use of WiMAX... Under Windows.</em></p>
<br>IEEE 802.16 / WiMAX was promising more than one decade ago for expanding Internet access especially in remote areas and other interesting use-cases. But these days outside of the AeroMACS wireless solution employed by some airports and some niche deployments of WiMAX in remote regions, there isn't much left going for its adoption. Even the WiMAX Forum's own product registry of certified products has been down for some time.
<br><p align="center"><img src="https://www.phoronix.net/image.php?id=962&image=ces_2008d0_04" referrerpolicy="no-referrer"><br><em>Thirteen years after Intel was heavily promoting WiMAX, the Linux kernel support is being removed. This follows the Linux kernel also <a href="https://www.phoronix.com/scan.php?page=news_item&px=Intel-Phasing-Out-MID-Linux">recently phasing out the Intel MID support</a>.</em></p>
<br>The WiMAX infrastructure and Intel i2400m driver have been in the mainline Linux kernel for years albeit unmaintained with Intel not being involved like they once were with the effort. After several months being in the staging area of the kernel and no interested parties stepping up, it's been decided to just delete the code. Especially as this WiMAX code doesn't work with AeroMACS or other more recent efforts.
<br>
<br>Linux staging maintainer Greg Kroah-Hartman has queued up the WiMAX removal in staging-next for Linux 5.13. He wrote in the commit, "<em>the wimax code is dead with no known users.  It has stayed in staging for 5 months, with no one willing to take up the codebase for maintance and support, so let's just remove it entirely for now. If someone comes along and wants to revive it, a simple revert of this patch is a good place to start.</em>"<br><br>
Dropping this unmaintained code lightens up the Linux kernel by some fifteen thousand lines of code.  
</div>
            