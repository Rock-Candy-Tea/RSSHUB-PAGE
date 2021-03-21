
---
title: Ubuntu 21.04 Moves Ahead With Enabling LTO Optimizations For Greater Performance
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Sat, 20 Mar 2021 12:46:46 GMT
thumbnail: https://www.phoronix.com/assets/categories/ubuntu.jpg
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="UBUNTU -- " src="https://www.phoronix.com/assets/categories/ubuntu.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
Ubuntu 21.04 is moving ahead with plans to enable compiler <a href="https://www.phoronix.com/scan.php?page=search&q=Link-time%20optimization">link-time optimizations</a> (LTO) by default for package builds in the name of greater performance.
<br>
<br>Back in January the plans were discussed for <a href="https://www.phoronix.com/scan.php?page=news_item&px=Ubuntu-21.04-LTO-Packages">Ubuntu enabling LTO optimizations for packages</a> with Ubuntu 21.04 to yield greater performance by allowing additional compiler optimizations at link-time on the entire binary. This follows the likes of Fedora and openSUSE already employing LTO by default as part of their package builds.
<br>
<br>While into the Ubuntu 21.04 feature freeze and just one month out from release, this LTO enablement is finally happening for the Hirsute Hippo.
<br>
<br><a href="https://launchpad.net/ubuntu/+source/dpkg/1.20.7.1ubuntu4">Uploaded</a> this week was the latest dpkg package that now turns on LTO optimizations. Link-time optimizations are enabled by default for x86_64 (AMD64), ARM64, PPC64EL, and s390x architectures where GCC LTO support is reliable and generally a worthwhile performance improvement.
<br>
<br>Matthias Klose  further commented on the <a href="https://lists.ubuntu.com/archives/ubuntu-devel/2021-March/041421.html">mailing list</a> for the current state and the plan on black-listing packages that have build issues or other problems with LTO:
<br><blockquote>This is now turned on by default, a bit later than expected (discussed and approved by Lukasz). The package lto-disabled-list is now seeded with all packages not in main, which regressed with LTO optimizations for some reason.
<br>
<br>For the ~80 regressing packages in main, I'll do uploads after the next test rebuild planned for next week, either fixing the regression, or turning off LTO optimizations directly in the package.</blockquote>
<br>Great to see this happening and should help the default GCC 10 compiler on Ubuntu 21.04 help squeeze some extra performance out of the system. Ubuntu 21.04 benchmarks will be heating up on Phoronix in the weeks ahead.  
</div>
            