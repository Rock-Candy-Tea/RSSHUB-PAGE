
---
title: 'Meta开源MemLab JavaScript内存泄露检测器'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0915/2f2ac0e824da982.png'
author: cnBeta
comments: false
date: Thu, 15 Sep 2022 07:20:39 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0915/2f2ac0e824da982.png'
---

<div>   
<strong>Facebook 母公司 Meta 刚刚宣布了开源 MemLab，该工具可在 Chromium 内核浏览器上，查找 JavaScript 应用程序中的内存泄露。</strong>Facebook 工程团队指出：“使用我公司网络应用程序的人们，通常会立即留意到性能与功能正确性问题。但对于内存泄露，其隐蔽性就远不在同一水平线上了。取而代之的是，用户会得到一个响应性逐渐降低的会话”。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0915/2f2ac0e824da982.png" referrerpolicy="no-referrer"></p><p>内存泄漏的后果在单页应用程序（SPA）中更为严重，因为用户可能会在较长时间内继续与页面交互，而 MemLab 就是专为这种场景而设计的。</p><p><strong>如上图所示，MemLab 的工作原理如下：</strong></p><blockquote><p>（1）导航到页面并返回；</p><p>（2）查找未释放的对象；</p><p>（3）显示泄露追踪结果。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0915/fe01c1a8f1d5ee8.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">创建场景，并将文件保存到 ~/memlab/scenarios/detached-dom.js 路径。</p><p>据悉，MemLab 使用了一个名为“<a href="https://pptr.dev/" target="_self">Puppeteer</a>”的 Node.js 库。它可以控制 Google Chrome 或其它基于 Chromium 内核打造的浏览器，且默认情况下以 headless 模式运行（方便命令行交互）。</p><blockquote><p>Facebook 工程师解释称，MemLab 的工作方式就是导航到一个页面、然后离开。</p><p>正常情况下，可预计该页面分配的大部分内存也将被释放。但若没有，则意味其存在极高的内存泄露可能性。</p><p>MemLab 拥有一些特定于框架的知识（尤其是 React），这是由 Facebook 团队打造的框架、现也主导着 JavaScript 的开发。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0915/f8c94624cb1152e.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">运行 MemLab（或需几分钟）</p><p>React 使用存储在树结构中、被称作 Fibers 的对象，来表示内存中的浏览器文档对象模型（DOM）。</p><p>据该团队所述，这可能是存在“巨大内存泄露”的一个主要原因。拥有强连接图的缺点很是显著，若有任何外部引用指向图的任何部分，就无法对整个图开展垃圾回收。</p><p>MemLab 的另一特性，就是提供了 JavaScript 堆的图形视图、启用了用于检查堆快照的 API 。这意味着开发者能够编写开展内存断言的测试，例如声明某个对象将不再存在于内存中。</p><p>此外有一个用于查找重复字符串实例的工具，在某个案例中，团队发现字符串占用了 70% 的堆、且其中半数至少有一个重复的实例。</p><p><img src="https://static.cnbetacdn.com/article/2022/0915/abb6c9990146384.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">3 - 调试泄露追踪</p><p>包括 Chrome、Edge、Firefox 在内的浏览器，都有附带内存检查工具。但正如以为开发者在 Hacker News 上吐槽的那样 —— 这些开发工具难以在调试过程中揪出内存泄露的问题。</p><p>安装方面，MemLab 不仅可以通过 npm 包管理器、还可从 <a href="https://github.com/facebookincubator/memlab" target="_self">git 存储库</a>进行构建。不过 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 平台必须使用 Git Bash，否则会在构建时遭遇失败。然后开发者可以运行 MemLab，将其传递给 JavaScript 文件中定义的场景。</p><p>最后，MemLab 的另一项强大功能，就是可以在测试期间作为命令过程的一部分而运行。这意味着如果代码中引入了严重的泄露，开发者们也能够在投入生产环境前加以捕获。</p>   
</div>
            