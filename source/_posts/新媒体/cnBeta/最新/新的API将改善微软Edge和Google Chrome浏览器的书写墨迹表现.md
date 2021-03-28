
---
title: '新的API将改善微软Edge和Google Chrome浏览器的书写墨迹表现'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0328/ed1c3bc3ba3b98a.png'
author: cnBeta
comments: false
date: Sun, 28 Mar 2021 11:39:40 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0328/ed1c3bc3ba3b98a.png'
---

<div>   
来自新的代码提交中发现，微软正在对基于Chromium的浏览器（如Edge和Chrome）中的墨迹功能进行一系列改进。<strong>这家软件巨头在收到用户的反馈后，决定对使用Chromium的墨迹功能中遇到的问题做一些改进，主要报告的问题是延迟问题，会导致书写并生成墨迹时感觉有点卡顿。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0328/ed1c3bc3ba3b98a.png" title alt="large.png" referrerpolicy="no-referrer"></p><p>微软方面收到了关于Edge无法区分笔和手指输入的投诉。作为一个名为 "Web Ink Enhancement "项目的一部分，微软一直在考虑使用新的API来解决使用钢笔或手写笔时的延迟问题。墨水预测"在目前的形式下相当糟糕"。例如有一个bug会令即使当鼠标左键被抬起时，墨水痕迹会短暂地继续，而原本这个时候墨水应该停止显现。当浏览器不知道任何关于书写墨迹的信号，无法停止转变点时，就会发生这种情况。</p><p>在Chromium Gerrit的一篇新文章中，微软已经证实，它计划使用即将到来的<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 API--StartNewTrail、AddTrailPoints、RemoveTrailPoints等来指示墨迹的起点，并在更多墨迹到达时添加额外的点。</p><p>"这允许浏览器进程直接向GPU主线程发送点，为这些点被操作系统API消耗做准备，减少延迟，"微软指出。</p><p>微软仍在研究这些新的Windows 10 API，它们将在未来的SDK中加入。除了墨迹之外，微软还在研究一些变化，以提高使用Chromium浏览器安装网络应用的质量。例如，未来的Chromium更新将允许用户通过浏览器会话还原系统恢复Web应用。</p>   
</div>
            