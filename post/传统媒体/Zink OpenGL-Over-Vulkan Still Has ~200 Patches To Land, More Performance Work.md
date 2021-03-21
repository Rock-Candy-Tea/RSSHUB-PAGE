
---
title: Zink OpenGL-Over-Vulkan Still Has ~200 Patches To Land, More Performance Work
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Fri, 19 Mar 2021 05:00:00 GMT
thumbnail: https://www.phoronix.com/assets/categories/mesa.jpg
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="MESA -- " src="https://www.phoronix.com/assets/categories/mesa.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
Mike Blumenkrantz who has been working under contract for Valve as part of their Linux graphics driver initiatives has provided a fresh status report on Zink as the Mesa Gallium3D effort for implementing OpenGL APIs atop Vulkan.
<br>
<br>With supporting OpenGL 4 already and continuing to squeeze out more performance, Zink is on a solid footing but there still is even more work to land to further enhance this OpenGL-on-Vulkan implementation. Mike noted in the latest post that his work-in-progress "zink-wip" branch is down to around 200 patches left to clean-up and see through the review process for merging. Two hundred or so patches isn't bad at all when considering a month or so ago they were around 600 patches.
<br>
<br>With working through the zink-wip queue for mainlining, one recent addition that was merged for Mesa 21.1 is descriptor caching support. Mike noted that this should yield a 80~100% performance improvement nearly across the board for CPU bound scenarios. As another performance win to happen on mainline, there is less than 100 patches to go before seeing threaded context support with Mesa Git.
<br>
<br>Zink has also expanded its continuous integration (CI) work to help fend off future regressions. The Lavapipe software-based Vulkan implementation nearing Vulkan 1.1 support will also allow Zink CI testing through OpenGL 4.5.
<br>
<br>The latest Zink status details can be found over on <a href="https://www.supergoodcode.com/a-more-accurate-update/">Mike's blog</a>.  
</div>
            