
---
title: 'Windows 11 Edge Ink API：手写输入延迟最高改善240%'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0819/6b47753c79956c0.gif'
author: cnBeta
comments: false
date: Wed, 18 Aug 2021 23:52:07 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0819/6b47753c79956c0.gif'
---

<div>   
在 Microsoft Edge 的最新 Dev 频道版本中，微软放出了增强手写输入的预览版。在 Build 2021 开发者大会上，微软首次介绍了这些增强功能，展示了这个全新网络 API（已在 Chromium 开源项目的上游实现）是如何大大减少物理手写笔的笔尖和手写在屏幕上绘制时的延迟。<br>
 <p style="text-align: left;">在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 最新预览版中，微软表示手写延迟改善了 240%，下面动图中绿色部分为增强手写输入，可以看到延迟得到了明显改进，让屏幕响应更快更跟手写笔输入。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0819/6b47753c79956c0.gif" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0819/6b47753c79956c0.gif" width="750" height="480/" referrerpolicy="no-referrer"></a></p><p style="text-align: left;"><strong>技术细节</strong></p><p style="text-align: left;">微软解释道目前基于 Chromium 的浏览器中，手写笔事件首先发送到浏览器进程，而浏览器进程又将这些事件转发到 Web 应用程序的 JavaScript 事件循环。浏览器进程收到这些事件和它们到达应用程序之间的时间延迟有时会很明显，这取决于主线程的其他部分，从而导致在手写时出现延迟。</p><p style="text-align: left;">为了改善这一点，在 Windows 11 上的 InkPresenter 实现的基础上，Microsoft Edge 正在使用一个新的 Windows API，它将直接与操作系统的合成器合作，在 Microsoft Edge 的应用程序循环之外绘制额外的笔触。由于这个API，我们不用等待通过JavaScript将事件传递给网络应用，而是可以在收到这些点后立即将其提供给操作系统的合成器。然后，合成器可以用墨水笔画将这些点连接起来，并在要呈现在屏幕上的下一帧中绘制这些笔画，大大减少了延迟。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0819/3945de24527e778.gif" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0819/3945de24527e778.gif" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">对于像 Windows 10 和 Linux 这样没有这个 API 的操作系统，在 Microsoft Edge 中直接实现的 polyfill 将接管并为最后一个已知的可信任的PointerEvent之外的墨水笔触提供预测性渲染。这个实现的目的是与Windows 11的API类似--它利用浏览器所知道的点，以及一些预测的点，在最后一刻为应用程序的笔迹画出一个扩展。虽然效果没有Windows 11 API那么强大，但它仍然可以为用户提供更多的体验!</p>   
</div>
            