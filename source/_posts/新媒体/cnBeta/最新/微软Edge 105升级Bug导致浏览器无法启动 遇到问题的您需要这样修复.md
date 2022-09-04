
---
title: '微软Edge 105升级Bug导致浏览器无法启动 遇到问题的您需要这样修复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0904/36139425687ce90.png'
author: cnBeta
comments: false
date: Sun, 04 Sep 2022 09:31:07 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0904/36139425687ce90.png'
---

<div>   
几天前，微软发布了新版本的Edge浏览器，带来了各种改进和变化。但是，许多更新到微软Edge
105的人遇到了一个相当严重的问题--浏览器彻底罢工，无法启动。<strong>这是一个已经被广泛报道的问题，虽然微软对这个问题公开说了很多，但Edge开发团队的一名成员现在才站出来提出了解决方案。</strong><br>
 <p>因此，如果最新版本的Edge无法启动，你会很高兴地了解到，这个问题源于一个废弃的组策略，可以通过编辑注册表轻松解决。</p><p>微软Edge总经理Sean Lyndersay承认了这个问题，并认同已经分享的解决方案。他还说，这个错误将在Edge的下一个稳定版本推出时得到修复。</p><p><img src="https://static.cnbetacdn.com/article/2022/0904/36139425687ce90.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>在Twitter上，Lyndersay写道：</p><p>让Edge重新启动和运行的解决方案需要快速进入注册表编辑器：</p><p>1.按<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> + R，输入regedit并按回车键。</p><p>2.导航到HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Edge 并删除 MetricsReportingEnabled 键。</p><p>3.重复HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\ Edge的步骤，问题即可解决。</p>   
</div>
            