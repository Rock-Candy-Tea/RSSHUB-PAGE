
---
title: 'Ubuntu将Firefox Snap启动速度缩短了近半'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0709/f68be977bd50fb3.jpg'
author: cnBeta
comments: false
date: Sat, 09 Jul 2022 02:17:03 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0709/f68be977bd50fb3.jpg'
---

<div>   
Canonical 工程师一直在努力改善 Snap 版本的 Mozilla Firefox 应用程序的启动时间，此前该问题引发了相当多的吐槽。<strong>好消息是，作为 Ubuntu 22.04 LTS 长期支持版本上的默认浏览器，最新推送的 Firefox Snap 已将启动时间缩减了近半。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0709/f68be977bd50fb3.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0709/f68be977bd50fb3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">Firefox Snap 资料图</p><p>在周五的一篇 <a href="https://ubuntu.com//blog/improving-firefox-snap-performance-part-3" target="_self">Ubuntu Blog</a> 文章中，产品经理 Oliver Smith 解释称：</p><blockquote><p>与 Firefox 101 相比，全新安装后的启动时间，平均减少了 50% 。</p><p>此外在一系列平台和发行版上，其测试结果都保持一致。</p></blockquote><p>据悉，由于 Mozilla 改成了在启动时一次只复制一个环境 / 语言包（而不是在初始启动时尝试复制所有语言包），此外区域设置将遵循系统设置，因而大幅缩减了启动等待时间。</p><blockquote><p>其它改动包括将 GNOME 和 GTK 主题快照从 XZ 切换到 LZO，除了缩短启动时间、这么做还有助于提升性能体验。</p><p>Canonical 已经为 Firefox Snap 转移到 LZO 压缩，现其所依赖的 GNOME 和 GTK 主题 Snap 也使用了相同的压缩技术、以更快地解压缩 / 启动。</p></blockquote><p>目前 Canonical 正在研究解压缩时的多线程支持、解决 Firefox 在树莓派上使用的软件渲染问题，以及探索预缓存（pre-caching）等技术。</p>   
</div>
            