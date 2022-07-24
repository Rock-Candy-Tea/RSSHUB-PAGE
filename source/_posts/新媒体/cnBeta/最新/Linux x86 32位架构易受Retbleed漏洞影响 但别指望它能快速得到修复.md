
---
title: 'Linux x86 32位架构易受Retbleed漏洞影响 但别指望它能快速得到修复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0724/f4ab8abb5009cbf.webp'
author: cnBeta
comments: false
date: Sun, 24 Jul 2022 00:00:47 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0724/f4ab8abb5009cbf.webp'
---

<div>   
<strong>虽然相关的英特尔和AMD处理器已经对最近影响老一代处理器的Retbleed安全漏洞提供了缓解措施，但这些缓解措施目前只适用于x86_64内核，如果在受影响的硬件上运用传统的x86内核，则这些安全措施无法发挥作用。</strong>除非有热情的个人站出来，否则它不可能得到修复，因为上游的开发者和供应商早已转向只关心x86_64的问题。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0724/f4ab8abb5009cbf.webp" title alt="image.webp" referrerpolicy="no-referrer"></p><p>上周，在为缓解这种最新的投机执行攻击而进行的一系列Linux补丁之后，有人指出，Linux x86 32位内核仍然容易受到Retbleed的攻击。事实证明，32位的Debian即使打了补丁的内核，i386部分仍然容易受到Retbleed攻击。</p><p>AMD Zen 1/2和英特尔Skylake时代的CPU已经收到Retbleed缓解措施，它们都能够运行x86_64软件，所以现在能做的就是期望生产环境下的用户避免使用32位内核。</p><p>Linux内核开发者第二把手Greg Kroah-Hartman回应说："这很有趣。我不认为这是一个应该关心的有效组合，但是如果这是一个需要关心的"真实"的部分，我会让Pawan[来自英特尔]来评论。"</p><p>Pawan Gupta回应说："英特尔不认为在Skylake那一代以及以后的CPU上会有人使用32位模式的生产环境，所以这不应该是一个问题。"</p><p>英特尔的Peter Zijlstra补充说："是的，到目前为止没有人关心修复32位架构。但如果有人真正关心并想投入精力，我想我会审查这些补丁，但说真的，没人会也不应该在基于Skylake/Zen的系统上运行32位内核，这太傻了。"</p><p>首先这是因为它是相当旧的英特尔和AMD x86_64原生CPU，如果你在Skylake和Zen 1/2时代的硬件上运行32位Linux发行版，遇到的问题远不仅仅是漏洞，例如因为使用x86_64软件而错失很多可能的性能。</p><p>今天在TIP的x86/speculation分支排队的是一个补丁，它只使Retbleed缓解措施现在可配置于x86_64。</p><blockquote><p>对RETBleed的缓解措施目前在x86_32上是无效的，因为 entry_32.S 没有使用所需的宏。然而，对于 x86_32 目标，它们的 kconfig 符号仍然是默认启用的，并且 /sys/devices/system/cpu/vulnerabilities/retbleed 会错误地报告说缓解措施已经完成了。所有这些都依赖于 x86_64，并且只在 x86_64 上默认启用 RETHUNK。</p></blockquote><p>未来有可能有人会站出来改编Retbleed缓解代码，使其适用于x86 32位架构，但这意义不大，因为真正存在的绝大多数用户用户在2022年的今天会运行x86_64 CPU和x86_64操作系统。</p><p><strong>了解更多：</strong></p><p><a href="https://lore.kernel.org/lkml/CA+G9fYv0N0FcYRp5irO_7TpheLcUY8LRMQbcZqwEmiRTEccEjA@mail.gmail.com/" _src="https://lore.kernel.org/lkml/CA+G9fYv0N0FcYRp5irO_7TpheLcUY8LRMQbcZqwEmiRTEccEjA@mail.gmail.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="b8fbf993ff81dee1ce88f688fedbe1eac88dd1caf7e78fecc8d0ddf4dbede180f4eaf5e9dadbe2c9cffdd5d1eaecfddbdbfdd2f9f8d5d9d1d496dfd5d9d1d496db">[email protected]</span>om/</a><br></p>   
</div>
            