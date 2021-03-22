
---
title: 'Linux Looks To Finally Remove Its Legacy IDE Driver Support'
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Sat, 20 Mar 2021 04:00:00 GMT
thumbnail: 'https://www.phoronix.com/assets/categories/linuxstorage.jpg'
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="LINUX STORAGE -- " src="https://www.phoronix.com/assets/categories/linuxstorage.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
It's 2021 and proposed patches by upstream developers would finally remove Linux's legacy IDE driver code.
<br>
<br>The proposed code is for removing the legacy IDE driver support from the mainline kernel tree, likely beginning with the 5.13 kernel assuming all goes as planned. It was two years ago that <a href="https://www.phoronix.com/scan.php?page=news_item&px=Linux-Legacy-IDE-Deprecated">the legacy IDE driver code was deprecated</a> and marked for removal in 2021... We are now well into 2021, so Christoph Hellwig is following through and looking to have that removed.
<br><p align="center"><a href="https://www.phoronix.com/image-viewer.php?id=251&image=abit_aw8_ide_lrg" target="_blank"><img src="https://www.phoronix.net/image.php?id=251&image=abit_aw8_ide_med" referrerpolicy="no-referrer"></a></p>
<br>It's important to note though this removal is just about the legacy IDE driver support. IDE support itself will still be available on modern Linux kernel versions through the libata layer, which nearly all users have already been relying upon for many years if still rocking out any IDE devices.
<br><p align="center"><a href="https://www.phoronix.com/image-viewer.php?id=251&image=abit_aw8_ideround_lrg" target="_blank"><img src="https://www.phoronix.net/image.php?id=251&image=abit_aw8_ideround_med" referrerpolicy="no-referrer"></a></p>
<br>The Linux kernel for a long time -- more than one decade, going towards two decades -- relied upon the libata path to much better support. The libata code will be sticking around while the prior IDE driver support is what's slated for removal.
<br>
<br>Hellwig noted in Thursday's <a href="https://lore.kernel.org/lkml/20210318045706.200458-1-hch@lst.de/">remove the legacy ide driver</a>:
<br><blockquote>we've been trying to get rid of the legacy ide driver for a while now, and finally scheduled a removal for 2021, which is three month old now.
<br>
<br>In general distros and most defconfigs have switched to libata long ago, but there are a few exceptions.  This series first switches over all remaining defconfigs to use libata and then removes the legacy ide driver.
<br>
<br>libata mostly covers all hardware supported by the legacy ide driver. There are three mips drivers that are not supported, but the linux-mips list could not identify any users of those.  There also are two m68k drivers that do not have libata equivalents, which might or might not have users, so we'll need some input and possibly help from the m68k
<br>community here.</blockquote>
<br>So while there still might be a few niche legacy hardware platforms still making use of the legacy IDE driver, removing it has clear benefits with lightening up the kernel by around 41k+ lines of code and allow for more clean-ups to come within the Linux kernel's block layer.  
</div>
            