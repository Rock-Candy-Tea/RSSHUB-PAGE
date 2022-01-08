
---
title: 'Canonical正重构Snap应用安装包：更细、更模块化'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0108/cefba5b1891e5bd.webp'
author: cnBeta
comments: false
date: Sat, 08 Jan 2022 03:03:09 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0108/cefba5b1891e5bd.webp'
---

<div>   
Snap 是由 Canonical 创建的 Linux 软件包打包和分发平台。相比较传统 Linux 安装包，Snap 更具可移植性，而且它们中的大多数都被容器化，以防止一些常见的安全问题。<strong>然而，Snap 也有很多问题，这可能是 Canonical 正在试验新架构的原因。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0108/cefba5b1891e5bd.webp" alt="9p9dhrbr.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在一篇名为《<a href="https://ubuntu.com//blog/the-future-of-snapcraft" target="_blank">the future of Snapcraft</a>》的博文中，Canonical 详细介绍了将 Snap 框架分解成更小的模块化组件。关于最终结果会是什么样子，或者对于安装和使用 Sna p应用程序的普通人来说是否会更好，目前还没有任何确定的细节。然而，它应该使应用程序开发人员和 Canonical 更容易创建和维护 Snap 应用程序，这有可能使 Canonical 腾出时间来专注于 Snap 框架的其他方面。</p><p style="text-align: left;">Canonical说：“基本概念是围绕着把 Snapcraft 拆开--拆成更小、更模块化和可重复使用的组件，可以在一系列不同的产品中利用。这项工作的共同基础是一套 Craft Libraries，正如我们在‘Craft Parts’博文中已经讨论过的。该理论要求使用基于工艺提供者和工艺部件的通用部件构建器，并将添加的 Snapcraft 功能作为一个单独的层”。</p><p style="text-align: left;">Snap 安装包无疑是应用程序在 Linux 上发布的一种更容易的方式，因为它们不必依赖系统自己的包管理器，而包管理器在不同的桌面 Linux 发行版中并不总是相同。例如，如果你想为 Ubuntu、Fedora 和 Arch Linux 制作一个应用程序，你将不得不维护三种完全不同的发行方式（PPA、RPM 和 Pacman）。相比之下，Snap 应用程序几乎可以在所有基于 Linux 的现代操作系统上运行，包括 Ubuntu, Arch, Debian, Fedora, Majaro, Pop!_OS 等。</p><p style="text-align: left;">多年来，Snapcraft因各种问题而受到批评。不支持自定义软件库或应用服务器，所以所有的软件都必须通过Canonical自己的Snap商店分发，而且Canonical也没有发布Snap商店服务器的源代码。这种集中式的模式并不受所有人的欢迎，尤其是Canonical已经慢慢用Snap版本取代了Ubuntu中的核心应用程序（如Chromium）。Linux Mint完全阻止了Snap应用程序的安装，其他一些发行版也认可Flatpak作为一种替代。Canonical的博客文章没有提到任何关于支持第三方商店和存储库的内容。</p>   
</div>
            