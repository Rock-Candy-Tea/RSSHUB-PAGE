
---
title: 'Chrome_Chromium的Ozone X11代码现已全面启用 旧代码将被删除'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0829/112aaa5ed625c45.png'
author: cnBeta
comments: false
date: Sun, 29 Aug 2021 07:46:11 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0829/112aaa5ed625c45.png'
---

<div>   
Chrome/Chromium网络浏览器现在已经完全启用了对Ozone/X11平台的支持，包括测试版和稳定版渠道。通过Chrome的Ozone平台抽象代码，相当长一段时间以来，开发人员一直在努力从同一个构建中提供良好的Wayland和X11支持。<br>
 <p>在X11/X.Org上使用Ozone以前是一个实验性的选择，现在在今年夏天成功地通过了一个极早期试验。</p><p><img src="https://static.cnbetacdn.com/article/2021/0829/112aaa5ed625c45.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>Igalia开发者Maksim Sisov本周末通报了Ozone/X11平台的支持现在"在STABLE和BETA通道上100%启用"的消息。随着现在这种开始全面支持的形势渐入佳境，他们将致力于废除非Ozone/X11的路径，并在不久的将来删除那个传统的X11路径。</p><p>随着这个Ozone/X11使用的里程碑的完成和默认的前进，Igalia和其他参与的开发者将致力于运送Ozone/Wayland后端。在那之后，同样的Chrome/Chromium浏览器构建应该在X11和Wayland上都能很好地工作。</p><p><a href="https://static.cnbetacdn.com/article/2021/08/faa517e5e439ba6.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/08/faa517e5e439ba6.jpg" referrerpolicy="no-referrer"></a></p><p><a href="https://static.cnbetacdn.com/article/2021/08/f0193f2800f66e1.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/08/f0193f2800f66e1.jpg" referrerpolicy="no-referrer"></a></p><p>对Ozone平台层感兴趣的人可以通过<a href="https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/ozone_overview.md">googlesource.com</a>了解更多细节。谈论Chrome Ozone代码的工作已经有近十年了，这已经算得上是一个非常漫长的过程。<br></p>   
</div>
            