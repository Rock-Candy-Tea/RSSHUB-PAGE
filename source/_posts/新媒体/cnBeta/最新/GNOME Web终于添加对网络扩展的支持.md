
---
title: 'GNOME Web终于添加对网络扩展的支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0704/b71a827d792998b.webp'
author: cnBeta
comments: false
date: Mon, 04 Jul 2022 03:02:42 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0704/b71a827d792998b.webp'
---

<div>   
GNOME Web（Epiphany）是面向 Linux 用户的优秀浏览器之一，提供了精简且独特的用户体验。但遗憾的是，这种独特性并没有激励用户将其用作他们的主要网络浏览器。<strong>不过这种情况有望在近期发生改变....开发人员 Patrick（TingPing）透露，GNOME Web 终于添加了对 WebExtensions 的支持。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0704/b71a827d792998b.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0704/d9198ae2a26c03d.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在最新的 Epiphany 43.alpha 版本中添加了实验支持，因此现阶段目前仅在 GNOME Web 的 Beta 和 Alpha 版本中进行测试。开发者表示</p><p style="text-align: left;">Epiphany 43.alpha 支持上述基本结构。我们目前正在根据 Firefox 的 ManifestV2 API 对我们的行为进行建模，其中包括尽可能与 Chrome 扩展程序的兼容性。未来计划与 V2 一起支持 ManifestV3。</p><p style="text-align: left;">用户需要使用终端来启用扩展程序支持，然后通过下载 + 添加扩展的 .xpi 文件来安装扩展。您可以安装 Epiphany (GNOME Web) 的最新开发版本并使用以下命令启用扩展：</p><p style="text-align: left;">● flatpak remote-add --if-not-exists gnome-nightly <a href="https://nightly.gnome.org/gnome-nightly.flatpakrepo" _src="https://nightly.gnome.org/gnome-nightly.flatpakrepo" target="_blank">https://nightly.gnome.org/gnome-nightly.flatpakrepo</a><br style="text-align: left;"></p><p style="text-align: left;">● flatpak install gnome-nightly org.gnome.Epiphany.Devel</p><p style="text-align: left;">● flatpak run --command=gsettings org.gnome.Epiphany.Devel set org.gnome.Epiphany.web:/org/gnome/epiphany/web/ enable-webextensions true</p>   
</div>
            