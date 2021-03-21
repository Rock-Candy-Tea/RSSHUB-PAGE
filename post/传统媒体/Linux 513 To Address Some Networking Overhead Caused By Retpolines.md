
---
title: Linux 5.13 To Address Some Networking Overhead Caused By Retpolines
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Sun, 21 Mar 2021 12:47:08 GMT
thumbnail: https://www.phoronix.com/assets/categories/linuxnetworking.jpg
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="LINUX NETWORKING -- " src="https://www.phoronix.com/assets/categories/linuxnetworking.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
It's been three years that <a href="https://www.phoronix.com/scan.php?page=search&q=Retpolines">Retpolines</a> (return trampolines) have been around as part of the Spectre defenses on Linux and kernel developers in particular are still working to better optimize different areas of their code to deal with the performance overhead incurred.
<br>
<br>With the current Linux 5.12 cycle there is <a href="https://www.phoronix.com/scan.php?page=news_item&px=AES-NI-XTS-Retpolines-Regress">an important change to the AES-NI crypto code</a> to overcome the overhead introduced by enabling Retpolines on older Intel systems and old through current AMD hardware where this is needed as part of Spectre V2 mitigations. Those AES-NI code changes in Linux 5.12 for avoiding indirect calls makes <a href="https://www.phoronix.com/scan.php?page=news_item&px=AES-NI-CTS-Linux-5.12-AMD">a big performance improvement for cryptsetup</a> on Retpolines-enabled hardware. Now with Linux 5.13, the networking subsystem is seeing some tuning to also avoid Retpoline costs.
<br>
<br>Patches by Alexander Lobakin have been queued into net-next ahead of Linux 5.13 to work on avoiding Retpoline overhead. The area of focus with these initially queued patches are for VLAN and TEB GRO (Transparent Ethernet Bridging). There are just over two dozen lines of code changed for dealing with indirect calls there in aiming to lower the performance hit on Retpoline-enabled kernels.
<br><blockquote>The two most popular headers going after Ethernet are IPv4 and IPv6. Retpoline overhead for them is addressed only in dev_gro_receive(), when they lie right after the outermost Ethernet header. Use the indirect call wrappers in TEB (Transparent Ethernet Bridging, such as GENEVE, NvGRE, VxLAN etc.) GRO receive code to reduce the penalty when processing the inner headers.
<br>...
<br>Use the indirect call wrappers in VLAN GRO receive code to reduce the penalty on receiving tagged frames (when hardware stripping is off or not available).</blockquote>
<br>The real interesting matter is how much more kernel code is left to be optimized in trying to lower the overhead impact from Retpolines. Of course though, Retpolines are just one of several software mitigations out there for the growing number of speculative execution vulnerabilities affecting modern processors.  
</div>
            