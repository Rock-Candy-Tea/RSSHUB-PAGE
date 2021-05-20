
---
title: 'Flutter 2.2 发布：针对各平台的性能优化、完善生态支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5d44f1571e8a33397b1a21a83a1f8b0746f.png'
author: 开源中国
comments: false
date: Thu, 20 May 2021 08:29:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5d44f1571e8a33397b1a21a83a1f8b0746f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>谷歌在昨日举办的 Google I/O 2021 大会上宣布了 Flutter 2.2，其开发团队称此版本是迄今为止 Flutter 最好的版本。</p> 
<p>Flutter 2.2 的更新亮点包括：针对开发者优化通过应用内购买、付款和广告的变现流程；更新工具包和语言特性以帮助开发者消除大部分错误；提升应用程序性能并减小程序包体积。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5d44f1571e8a33397b1a21a83a1f8b0746f.png" referrerpolicy="no-referrer"></p> 
<p>下面简要介绍 Flutter 2.2 主要变化。</p> 
<p>新创建项目默认启用空类型安全 (null safety)</p> 
<p>从 Flutter 2.2 起，新创建的项目会默认启用健全的空类型安全 (null safety)。null safety 增强了针对空引用异常的保护，为开发者提供了在其代码中表达非空类型的方法。由于 Dart 的实现是健全的，编译器可以在运行时消除空值检查，为应用程序提供更高的性能。此外，Flutter 生态也已经迅速做出反应，大约有 5000 个软件包已经更新以支持 null safety。</p> 
<h1>针对各平台的优化</h1> 
<p>此版本还包含许多性能改进：对于 Web 应用，提供了使用 service workers 的后台缓存；对于 Android 应用，增加对延迟组件的支持；对于 iOS 应用，着色器的预编译现在已经集成至开发工具中，可以消除或减少首次运行的卡顿。此外还为 DevTools 套件增加了许多新功能，可帮助开发者了解应用程序中的内存分配情况，以及支持第三方工具扩展。</p> 
<h1>Dart 2.13</h1> 
<p>Dart 也在 Flutter 2.2 中进行了更新。Dart 2.13 扩展了对原生应用互操作性的支持，支持在 FFI 中使用数组和封装好的数据结构。此外还包括对类型别名 (type aliases) 的支持，该项特性增加了可读性，并为某些重构方案提供了途径。</p> 
<h1>完善生态支持</h1> 
<p>谷歌认为，虽然自己仍然是 Flutter 的主要贡献者，但它不仅仅是一个“谷歌项目”。因为 Flutter 周围更广泛的生态正在逐渐增长，越来越多的企业参与了进来。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-32e6c273ae6416b9c0cbb2a3c8a7e768943.png" referrerpolicy="no-referrer"></p> 
<p>最近几个月特别增长的领域之一是 Flutter 扩展了到越来越多的平台和操作系统。例如：</p> 
<ul> 
 <li>丰田宣布会在下一代车载信息娱乐系统应用 Flutter</li> 
 <li>Canonical 上个月发布的新版 Ubuntu 是首个集成 Flutter 支持的版本</li> 
 <li>三星正在将 Flutter 移植到 Tizen，并提供其他人也可以参与的开源仓库</li> 
 <li>索尼正在主导一个让 Flutter 嵌入到 Linux 的方案</li> 
 <li>微软 Surface 团队除了构建 Flutter 的可折叠体验之外，还包括 Flutter 对面向 Windows 10 构建的 UWP 应用的支持</li> 
</ul> 
<p>Flutter 团队也提到越来越多主流应用也开始使用 Flutter 构建部分模块，例如微信和 Tik Tok，据说 Tik Tok 背后的公司——字节跳动已使用 Flutter 构建了 70 多个不同的应用程序。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fflutter%2Fannouncing-flutter-2-2-at-google-i-o-2021-92f0fcbd7ef9" target="_blank">详细内容查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            