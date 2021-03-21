
---
title: Intel Tweaking Ice Lake Xeon Linux Power Management Code For Higher C6 Latency
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Fri, 19 Mar 2021 12:16:03 GMT
thumbnail: https://www.phoronix.com/assets/categories/intel.jpg
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="INTEL -- " src="https://www.phoronix.com/assets/categories/intel.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
While Intel upstreamed their forthcoming "Ice Lake" Xeon processor support long ago and has been focused on next-gen Sapphire Rapids enablement now for the better part of the past year, there still are some Ice Lake Xeon tweaks taking place here and there. This week a new bleeding-edge patch is in testing for tweaking the power/performance behavior of Ice Lake Xeon with Intel's idle driver.
<br>
<br>For hitting the C6 low-power state with Intel's Ice Lake Xeon there are higher costs involved than existing Xeon processors. The C6 exit latency as the maximum time it takes the CPU from entering an idle state to executing the first instruction after a wake-up from that state has been increased. The Ice Lake Xeon C6 exit latency within the Intel Idle driver was at 128 micro-seconds but now has been bumped up to 170 microseconds. The exit latency change was attributed to using the median latency previously rather than worst-case latency,  Meanwhile Xeon Scalable Skylake / Cascade Lake has a exit latency of 133 microseconds with this "intel_idle" driver.
<br>
<br>The C6 target residency has also been increased from 384 microseconds to 600 microseconds. The target residency is the least amount of time the hardware should spend in a particular idle state in order for the energy savings to pay off over using a shallower idle state.
<br>
<br>With the bump from 384 to 600 microseconds, the Intel Idle driver will likely end up using C6 less often. The Intel developers with this change did acknowledge it may lead to less C6 residency for some workloads while was tested as a reasonable level of power/performance and a better value than going all the way up to 1000 microseconds that they were also evaluating.
<br>
<br>With the increase to the C6 exit latency it puts the Ice Lake Xeon behind that of existing Xeon processors while the target residency now matches that of current Xeon processors rather than being an improvement. <a href="https://git.kernel.org/pub/scm/linux/kernel/git/rafael/linux-pm.git/commit/?h=bleeding-edge&id=d484b8bfc6fa71a088e4ac85d9ce11aa0385867e">The patch</a> from Intel engineers entered the Linux power management's "bleeding-edge" Git branch yesterday for testing.  Barring any other tweaks this in turn should work its way into the PM linux-next code ahead of the Linux 5.13 cycle unless it's sent in as a "fix" for the current 5.12 kernel. In either case, we'll see if this change gets back-ported to existing stable series ahead of Ice Lake Xeon's public arrival so that the intel_idle behavior is the same across kernels with these forthcoming server processors.
<br>
<br>Aside from the occasional tweaks like this, the Intel Ice Lake Xeon Linux kernel code should be in good shape for launch and has already worked its way out to all the major Linux distributions for quite some time. The GCC compiler support has also been out for two years now as "icelake-server" along with other toolchain components. It's expected everything should be in good shape while we'll see for ourselves once getting our hands on the new server processors.  
</div>
            