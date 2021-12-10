
---
title: '微软发布新工具协助开发者在Edge中检测内存泄漏情况'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/12/ab23be9e3f2d759.webp'
author: cnBeta
comments: false
date: Fri, 10 Dec 2021 07:30:20 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/12/ab23be9e3f2d759.webp'
---

<div>   
内存泄漏是编程中的一个常见问题，即一段代码在停止运行后没有正确地回收和取消分配内存。这在长期运行的应用程序中尤其不可取，大量的未释放内存随着时间的推移而累积，拖累系统整体性能显著下降。<strong>为了解决这个问题，微软在其Edge浏览器中公布了一个新工具，为开发者提供调试功能。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/12/ab23be9e3f2d759.webp" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/12/ab23be9e3f2d759.webp" referrerpolicy="no-referrer"></a></p><p>在一篇博客文章中，微软透露，其Edge DevTools套件中的Detached Elements工具可以让开发者调查文档对象模型（DOM）的泄漏。顾名思义，它将向程序员展示一个分离元素的列表以方便以进一步调查。<br></p><p>例如一些应用程序如Twitter在加载信息时故意附加和分离元素，一个分离元素的列表可以确保开发人员可以深入到他们自己的应用程序的细节部位，并修复有问题的DOM泄漏。</p><p><a href="https://static.cnbetacdn.com/article/2021/12/daec95716b97d28.webp" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/12/daec95716b97d28.webp" referrerpolicy="no-referrer"></a></p><p><a href="https://static.cnbetacdn.com/article/2021/12/530950c98ad28df.webp" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/12/530950c98ad28df.webp" referrerpolicy="no-referrer"></a></p><p>微软在这里发布了一个演示用聊天程序，展示如何通过Edge测试分离元素：</p><p><a href="https://microsoftedge.github.io/Demos/detached-elements/" _src="https://microsoftedge.github.io/Demos/detached-elements/" target="_blank">https://microsoftedge.github.io/Demos/detached-elements/</a><br></p><p>该公司的博文还包含了关于如何在这个应用程序以及真实世界的应用程序中进一步调查DOM泄漏的广泛信息，请在这里查看：</p><p><a href="https://blogs.windows.com/msedgedev/2021/12/09/debug-memory-leaks-detached-elements-tool-devtools/" _src="https://blogs.windows.com/msedgedev/2021/12/09/debug-memory-leaks-detached-elements-tool-devtools/" target="_blank">https://blogs.</a><a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>.com/msedgedev/2021/12/09/debug-memory-leaks-detached-elements-tool-devtools/<br></p><p>分离元素面板从Edge 97开始提供，你可以通过Edge DevTools右上方的反馈图标向微软提交关于它的反馈。</p>   
</div>
            