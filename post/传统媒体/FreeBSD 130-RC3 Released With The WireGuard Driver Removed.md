
---
title: FreeBSD 13.0-RC3 Released With The WireGuard Driver Removed
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Sat, 20 Mar 2021 17:13:48 GMT
thumbnail: https://www.phoronix.com/assets/categories/bsd.jpg
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="BSD -- " src="https://www.phoronix.com/assets/categories/bsd.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
A third and final release candidate of <a href="https://www.phoronix.com/scan.php?page=search&q=FreeBSD%2013.0">FreeBSD 13.0</a> was warranted ahead of its formal 13.0-RELEASE later this month.
<br>
<br>FreeBSD 13.0-RC3 is out this weekend as what was an "as-needed" milestone ahead of the FreeBSD 13.0 release set to take place around 30 March. Notable with this weeks FreeBSD 13.0-RC3 is the removal of the WireGuard kernel driver "if_wg" due to <a href="https://www.phoronix.com/scan.php?page=news_item&px=FreeBSD-New-WireGuard">the change in WireGuard implementations</a> amid concerns over code quality for this original WireGuard driver that was set to be introduced in FreeBSD 13.0. Now the existing WireGuard kernel code was removed but this new implementation won't land until at least FreeBSD 13.1 due to the timing of this significant change.
<br>
<br>FreeBSD 13.0-RC3 also takes care of a virtual memory list locking issue, a fix for systems running under VirtualBox, a fix in the service utility, and other small fixes.
<br>
<br>See the <a href="https://lists.freebsd.org/pipermail/freebsd-stable/2021-March/093340.html">release announcement</a> for more details on this final test release ahead of FreeBSD 13.0 stable.
<br>
<br>FreeBSD 13.0 brings improvements to its freebsd-update utility, a new Linux-compatible copy_file_range system call for efficient file copies, a much improved cryptographic framework within the kernel, AES-NI and armv8crypto are now included by default for the generic kernel builds to improve crypto performance, various new network drivers, efibootmgr EFI boot loader improvements, various ARM hardware support improvements, the default CPU support for the i386 architecture is now i686 rather than i486, and other hardware improvements. Intel users should also be able to find <a href="https://www.phoronix.com/vr.php?view=29920">much better performance</a> on recent hardware generations.
<br>
<br>Stay tuned for more FreeBSD 13.0 benchmarks following the official release.  
</div>
            