
---
title: '开发者正探讨于GTK5大版本更新时抛弃对X11的支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0704/3d7fbece0578ca3.png'
author: cnBeta
comments: false
date: Mon, 04 Jul 2022 06:50:45 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0704/3d7fbece0578ca3.png'
---

<div>   
尽管 GTK4 仍处于早期阶段、且距离 GTK5 的问世还有几年时间，<strong>但 GNOME 开发者们已经在积极讨论 —— 是否要在下一个 GTK 大版本上抛弃对 X11 的支持。</strong>若真如此，它将在 Linux 平台上成为“仅限于 Wayland”的存在。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0704/3d7fbece0578ca3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：GTK.org）</p><p><a href="https://www.phoronix.com/scan.php?page=news_item&px=GTK5-Might-Drop-X11" target="_self">Phoronix</a> 指出，GNOME 于上周开始考虑在下一个 GTK 里程碑上剔除对 X11 的后端支持。</p><p>红帽开发者 Matthias Clasen 在 GTK 社区开设了这个新议题（via <a href="https://gitlab.gnome.org/GNOME/gtk/-/issues/5004" target="_self">GitLab</a>），并解释称 X11 迟迟没有变得更好。与此同时，Wayland 却已经变得可广泛使用。</p><p>Matthias Clasen 指出，这项讨论仅针对 GTK5（无关乎 GTK4 的更新）。此外上游开发者补充道，X11 的代码活动，已几乎陷入沉寂。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0704/f2334ab1790df02.png" referrerpolicy="no-referrer"></p><p>Emmanuele Bassi 评论道，哪怕有“少数环境”覆盖了 90% 的用户群，他们也不至于在这里商议重新分配这个由志愿者所推动的项目的人力。</p><blockquote><p>嘴皮子动起来总是很简单，但代码并不会凭空出现 —— 那些失去了维护的代码，必然会随着时间的推移而退化。</p><p>对于 X11 来说，它最大的问题是长期没有迎来任何改进，而 GTK 早已开始转向以 Wayland 功能为主的 API 设计。</p><p>这意味着 X11 后端将难以获得应用程序开发者非常依赖的任何新特性，甚至会成为横亘在 GTK 上实现相关功能设计的一大障碍。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0704/b983c3e020803af.jpg" alt="GTK.jpg" referrerpolicy="no-referrer"></p><p>综上所述，除非有大量开发者切实投入 X11 的代码改进，否则它很可能在 GTK5 正式问世时被彻底打入冷宫。</p><p>最后，Red Hat 团队一直侧重于未来的 Wayland 支持准备工作（例如 XWayland rootfull），以增强在 XWayland 下运行完整的桌面的 Linux 系统生态和上游的其它现代化事务。</p>   
</div>
            