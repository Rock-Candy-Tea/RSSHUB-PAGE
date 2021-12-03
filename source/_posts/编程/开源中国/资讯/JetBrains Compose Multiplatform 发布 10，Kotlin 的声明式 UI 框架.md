
---
title: 'JetBrains Compose Multiplatform 发布 1.0，Kotlin 的声明式 UI 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-34eb3bb85daf81f9399723ece00dd22e31a.png'
author: 开源中国
comments: false
date: Fri, 03 Dec 2021 08:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-34eb3bb85daf81f9399723ece00dd22e31a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#000000"><span style="background-color:#ffffff">JetBrains 宣布 Compose Multiplatform（Kotlin 的声明式 UI 框架）已经达到 1.0 版本，现在可以在生产中使用了。</span></span><span style="background-color:#ffffff; color:#27282c">此版本主要解决质量和稳定性问题，同时修复关键问题和错误。</span></p> 
<p><span style="color:#000000"><span style="background-color:#ffffff">一些亮点内容如下：</span></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fkotlin%2F2021%2F12%2Fcompose-multiplatform-1-0-is-going-live%2F%23desktop" target="_blank">On desktop</a>，你现在可以快速高效地创建具有漂亮用户界面的 Kotlin 应用程序。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fkotlin%2F2021%2F12%2Fcompose-multiplatform-1-0-is-going-live%2F%23web" target="_blank">On the web</a>，你现在可以使用 Compose for Web 的稳定 DOM API 构建生产质量的动态 Web 体验，并与所有浏览器 API 完全互通。未来版本中将提供对 Material UI 小部件的支持。</li> 
 <li>总体而言，现在在各种平台（包括 Android，使用与 Google Jetpack Compose 的兼容性）之间<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fkotlin%2F2021%2F12%2Fcompose-multiplatform-1-0-is-going-live%2F%23sharing" target="_blank">共享专业知识和代码</a>要容易得多。</li> 
</ul> 
<p><strong>Kotlin UI for Desktop</strong></p> 
<ul> 
 <li style="text-align:start"><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>采用声明式方法构建用户界面</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>通过硬件加速实现出色的运行时性能</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>通过预览工具缩短迭代周期</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>通过自动应用程序打包，自信地交付桌面应用程序</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>与 Android 上的 Jetpack Compose 和 Java UI 框架的互操作性</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>使用 Compose Multiplatform </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>wizards <span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>快速启动并运行</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="278" src="https://oscimg.oschina.net/oscnet/up-34eb3bb85daf81f9399723ece00dd22e31a.png" width="500" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><strong>Compose for Web</strong></p> 
<p>Compose Multiplatform 还提供了一个强大的、声明性的 Kotlin/JS API 来处理 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocument_Object_Model%2FIntroduction" target="_blank">DOM</a>。</p> 
<p>它拥有你在现代 Web 框架中想要和需要的所有功能，包括全面的 DOM API、内置 CSS-in-JS 支持、对 SVG 的支持、typed inputs 等。Compose Multiplatform的 Web target 是用纯 Kotlin 编写的，并充分利用了该语言所提供的类型系统和习语。这使你可以使用你可能已经习惯的其他 Kotlin targets 的开发工作流程。</p> 
<p><strong><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>多平台支持</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p><span style="background-color:#ffffff; color:#27282c">要使用 Compose 快速开始构建面向多个平台的应用程序，您可以使用 IntelliJ IDEA 2021.1+ 中的 Kotlin Project Wizard。</span></p> 
<p><span style="background-color:#ffffff; color:#27282c">更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fkotlin%2F2021%2F12%2Fcompose-multiplatform-1-0-is-going-live%2F" target="_blank">查看官方博客</a>。</span></p>
                                        </div>
                                      
</div>
            