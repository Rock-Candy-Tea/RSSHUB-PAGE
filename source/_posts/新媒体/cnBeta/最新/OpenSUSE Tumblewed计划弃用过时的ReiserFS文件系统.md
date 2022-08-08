
---
title: 'OpenSUSE Tumblewed计划弃用过时的ReiserFS文件系统'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0808/b3b54fd3ead0f9f.webp'
author: cnBeta
comments: false
date: Mon, 08 Aug 2022 03:23:56 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0808/b3b54fd3ead0f9f.webp'
---

<div>   
在 20 年前，SUSE 曾是 ReiserFS 的主要支持者之一。在 2006 年之前，SUSE 还默认使用 ReiserFS 文件系统。在 2006 年之后 ReiserFS 虽然不再是 SUSE/openSUSE 的默认文件系统，但依然为挂载 ReiserFS 文件系统保留了 install-time 选项和相关支持，但这种做法可能很快就会结束。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0808/b3b54fd3ead0f9f.webp" alt="z21sajia.webp" referrerpolicy="no-referrer"></p><p>由于 Linux Kernel 5.18 正逐渐弃用 ReiserFS 并计划在 2025 年完全删除该内核代码，<strong>SUSE 终于开始讨论删除对这个过时文件系统的支持。</strong>自从 ReiserFS 与 SUSE/openSUSE 或其他 Linux 发行版相关以来，已经有很长时间了。</p><p>SUSE Labs Data & Performance 主管 Jeff Mahoney 周五制定了逐步淘汰 ReiserFS 的计划。他的建议是立即从 openSUSE Tumbleweed 中删除 ReiserFS 软件包，并立即禁用 ReiserFS 内核支持。</p><p>立即行动是针对滚动发布的 openSUSE Tumbleweed，而在 openSUSE Leap / SUSE Linux Enterprise 方面，显然在下一个主要版本发布之前不太可能看到任何变化。在 openSUSE Tumbleweed 上删除 ReiserFS 的计划可以在 opensuse-factory 上找到。</p>   
</div>
            