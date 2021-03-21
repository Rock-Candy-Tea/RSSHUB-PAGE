
---
title: AMD Sends In Aldebaran, FreeSync HDMI, Other Graphics Changes For Linux 5.13
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Sat, 20 Mar 2021 11:22:30 GMT
thumbnail: https://www.phoronix.com/assets/categories/radeon.jpg
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="RADEON -- " src="https://www.phoronix.com/assets/categories/radeon.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
AMD on Friday submitted a big batch of AMDGPU driver changes to DRM-Next ahead of next month's Linux 5.13 merge window.
<br>
<br>This was a big set of feature changes in the works for Linux 5.13 and with this pull request some of the user noteworthy items include:
<br>
<br>- Initial support for Aldebaran, the next-gen CDNA GPU. At the end of February, AMD began posting the open-source Linux driver patches around <a href="https://www.phoronix.com/scan.php?page=news_item&px=AMD-Aldebaran-Linux-Posted">Aldebaran as a new CDNA GPU</a> following LLVM code appearing for <a href="https://www.phoronix.com/scan.php?page=news_item&px=AMDGPU-LLVM-GFX90A">GFX90A</a>. Linux 5.13 will have initial support for Aldebaran.
<br>
<br>- Initial AMD FreeSync HDMI is now fully wired up and working. This didn't end up being part of Linux 5.12 but just the FreeSync HDMI code wired up for the DMCU. With this pull request, FreeSync HDMI should now be fully working for Linux 5.13 at least with pre-HDMI 2.1. The modern HDMI FreeSync/VRR support is still a mess due to <a href="https://www.phoronix.com/scan.php?page=news_item&px=HDMI-Closed-Spec-Hurts-Open">closed spec access by the HDMI Forum</a>.
<br>
<br>- Display ASSR support is now enabled. ASSR is is Alternate Scrambler Seed Reset and is a display authentication feature with eDP as part of the contention protection offerings. ASSR support began <a href="https://www.phoronix.com/scan.php?page=news_item&px=AMDGPU-Linux-5.9-Round-1">landing</a> last year and presumably was added as part of the Google Chromebook push, just like HDCP and other features.
<br>
<br>- 10bpc dithering improvements.
<br>
<br>- Various clean-ups and fixes, including display fixes, S0iX power savings fixes, PCIe DPM fixes, and other work.
<br>
<br>The full list of AMDGPU changes as part of this DRM-Next pull request ahead of Linux 5.13 can be found via <a href="https://lists.freedesktop.org/archives/dri-devel/2021-March/300278.html">this mailing list post</a>. Expect additional AMDGPU feature work over the next few weeks.  
</div>
            