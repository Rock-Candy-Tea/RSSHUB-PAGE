
---
title: 'Qt 6.2 WebAssembly 新变化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cce6dc211ea03bb9a9e2c2c55437c073be8.png'
author: 开源中国
comments: false
date: Wed, 05 Jan 2022 07:32:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cce6dc211ea03bb9a9e2c2c55437c073be8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>去年发布的<a href="https://www.oschina.net/news/162575/qt-6-2-released"> Qt 6.2 LTS </a>正式版已提供了技术预览版的 WebAssembly 支持。最近 Qt 官方表示，它们会逐步发表关于 Qt WebAssembly 最新发展的一系列文章。</p> 
<p>Qt for WebAssembly 使用 Emscripten 将 Qt 编译成二进制格式，然后在 Web 浏览器中运行。Qt 团队认为，与其为多个平台编译和部署，不如在 Web 服务器上为任何支持 WebAssembly 的浏览器的平台进行编译和部署。因此，从本质上讲，开发者可以把自己的 C++ 应用程序针对 WebAssembly 重新编译，然后在兼容的浏览器中运行。如果是企业用户，有多个客户在使用不同的平台，则可以使用 Qt for WebAssembly 来编译 Qt 或 Quick 应用程序，只需部署一次，而不需要通过应用程序商店。</p> 
<p>有关 Qt for WebAssembly 的构建说明查看 <span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-dev%2Fwasm.html" target="_blank">Qt for WebAssembly 文档</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>。</p> 
<p><strong>Qt WebAssembly 截图</strong></p> 
<ul> 
 <li>Qt 6 WebAssembly QtQuick3d</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cce6dc211ea03bb9a9e2c2c55437c073be8.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>工业面板</li> 
</ul> 
<p>最初用于展示在低功耗嵌入式硬件上运行的 Qt 的各种用例。下图演示了如何通过 Web 浏览器访问相同的 UI，而无需对代码进行任何更改。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-02a59417993523dfc39d3ff96bd2d39e4a2.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-6e06858c724ba5b89125e75965fe80d42e5.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>Slate，精灵绘图应用程序</li> 
</ul> 
<p>它展示了一个完整的“主窗口”风格的应用程序，带有菜单和工具栏以及保存和加载功能。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-3274110717b7f283a14864fc2a589a33e14.png" referrerpolicy="no-referrer"></p> 
<p>更多例子查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fqt-examples-for-webassembly%3FhsLang%3Den" target="_blank">https://www.qt.io/qt-examples-for-webassembly?hsLang=en</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fs3.eu-west-2.amazonaws.com%2Fwasm-qt-examples%2Flast%2Findex.html" target="_blank">https://s3.eu-west-2.amazonaws.com/wasm-qt-examples/last/index.html</a>。</p> 
<p><strong>Qt 6.2 WebAssembly 正在进行的开发工作</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>改进的多线程支持：Qt 5 支持启动辅助线程，其通过 Emscripten 提供的 <span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Femscripten.org%2Fdocs%2Fporting%2Fpthreads.html" target="_blank">pthreads 实现</a></span></span></span>。Qt 6.3 对此进行了改进，并添加了对调用 exec() 和在辅助线程上运行事件循环的支持。</li> 
 <li>对 Emscripten 的 Asyncify 的实验性支持，它可以在主线程上调用阻塞 API，如 QEventLoop::exec() 和 QDialog::exec()。</li> 
 <li>改进的网络支持。Qt 5 支持网络套接字和 QNetworkAccessmanager http(s) 请求。Qt 6 添加了对 TCP 和 UDP 套接字的支持，使用了 Emscripten 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Femscripten.org%2Fdocs%2Fporting%2Fnetworking.html%3Fhighlight%3Dsockets%23emulated-posix-tcp-sockets-over-websockets" target="_blank">socket tunneling</a>。</li> 
 <li>改进的剪贴板支持。Qt 5 支持文本复制粘贴，Qt 6.3 对此进行了改进并增加了对复制和粘贴图像的支持。</li> 
</ul> 
<p>详情查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-6.2-web-assembly-whats-new" target="_blank">公告</a>。</p>
                                        </div>
                                      
</div>
            