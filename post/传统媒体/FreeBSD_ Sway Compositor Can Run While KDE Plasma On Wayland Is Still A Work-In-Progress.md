
---
title: FreeBSD_ Sway Compositor Can Run While KDE Plasma On Wayland Is Still A Work-In-Progress
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Fri, 19 Mar 2021 09:48:19 GMT
thumbnail: https://www.phoronix.com/assets/categories/bsd.jpg
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="BSD -- " src="https://www.phoronix.com/assets/categories/bsd.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
It's been a while since hearing much about Wayland efforts on FreeBSD, but it turns out the Sway i3-inspired Wayland compositor can run on this BSD after a number of setup steps. However, the likes of KDE Plasma on Wayland still aren't working well outside of Linux.
<br>
<br>Free software developer Adriaan de Groot known for his work particularly around FreeBSD and KDE packaging recently set out to try out Wayland on FreeBSD. Following a number of steps to enable the Intel DRM kernel module, fetching Sway via pkg, and making a number of configuration changes, Adriaan was successful in getting Sway running on FreeBSD with Intel graphics. Under Sway he was able to get a number of applications running fine as well.
<br>
<br>In addition to Sway, he also tried the River dynamic tiling compositor for Wayland. River was also a success.
<br>
<br>But his attempts to get KDE Plasma on Wayland running under FreeBSD were so far thwarted. KDE Plasma Wayland just "sits there" when being launched without KWin properly initializing. So for now KDE on Wayland with FreeBSD still seems to be a work-in-progress. Given Adriaan's long history of KDE + FreeBSD wrangling, hopefully though it won't be long before Plasma is up and running nicely there.
<br>
<br>More details about Wayland on FreeBSD for early 2021 can be found via <a href="https://euroquis.nl//freebsd/2021/03/16/wayland">Adriaan's blog</a>.  
</div>
            