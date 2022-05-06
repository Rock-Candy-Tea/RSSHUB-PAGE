
---
title: 'Racket v8.5 发布，Lisp 语言分支'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4657'
author: 开源中国
comments: false
date: Fri, 06 May 2022 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4657'
---

<div>   
<div class="content">
                                                                                            <p>Racket v8.5 已发布，Racket（原名 PLT Scheme）是一门通用、多范型，属于 Lisp 家族的函数式程序设计语言，它的设计目之一是为了提供一种用于创造设计与实现其它编程语言的平台，Racket 被用于脚本程序设计、通用程序设计、计算机科学教育和学术研究等不同领域。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Racket 有一个实现平台，包含了运行环境、函数库、即时编译器 (JIT compiler) 等等，还有提供一个以 Racket 本身写成的开发环境 DrRacket（原名 DrScheme）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新版本主要变化</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;"><span><span><span style="color:inherit"><span>Racket 的新<code>-y</code>flag 会自动使编译后的文件保持最新状态，从而减少后续加载时间。</span></span></span></span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span><span><span style="color:inherit"><span>错误消息领域允许 Racket 托管的语言适应和重写错误消息以在特定上下文中有意义。</span></span></span></span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span><span><span style="color:inherit"><span>非特权用户可以使用插件目录中的“其他版本”目录来控制软件包安装范围。</span></span></span></span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span><span><span style="color:inherit"><span>Racket CS 可在当前不支持本地代码生成的平台上运行（例如，s390x 或 ppc64）。有关要配置的 </span></span></span></span><span style="color:#000000">—enable-pb flag<span> </span></span><span><span><span style="color:inherit"><span>的更多信息，参阅源分发中的“README.txt”。</span></span></span></span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span><span><span style="color:inherit"><span>DrRacket 引入了新的“重新打开关闭的选项卡”文件菜单项</span></span></span></span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span><span><span style="color:inherit"><span>Typed Racket 支持<code>xml</code>库；使用<code>typed/xml</code></span></span></span></span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span><span><span style="color:inherit"><span>Rackunit 以 Typed Racket 语言报告失败测试用例的源位置。</span></span></span></span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span><span><span style="color:inherit"><span>对于手动配置 Racket CS 使用 Zlib 压缩编译代码的用户，已修复 CVE-2018-25032 漏洞；下一个版本和当前的快照版本使用更新、更安全的 zlib 版本。</span></span></span></span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span><span><span style="color:inherit"><span>许多其他修复和更改</span></span></span></span></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.racket-lang.org%2F2022%2F04%2Fracket-v8-5.html" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            