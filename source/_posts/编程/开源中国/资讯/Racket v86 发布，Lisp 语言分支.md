
---
title: 'Racket v8.6 发布，Lisp 语言分支'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3762'
author: 开源中国
comments: false
date: Thu, 18 Aug 2022 07:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3762'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Racket v8.6 已发布，Racket（原名 PLT Scheme）是一门通用、多范型，属于 Lisp 家族的函数式程序设计语言，它的设计目之一是为了提供一种用于创造设计与实现其它编程语言的平台，Racket 被用于脚本程序设计、通用程序设计、计算机科学教育和学术研究等不同领域。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Racket 有一个实现平台，包含了运行环境、函数库、即时编译器 (JIT compiler) 等等，还有提供一个以 Racket 本身写成的开发环境 DrRacket（原名 DrScheme）。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>新版本主要变化</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>此版本使用了新的构建系统 Zuo，根据面向语言编程 (Language Oriented Programming, LOP) 的思想，它被实现为一种小语言。此实现只有一个 C 文件（加上用 Zuo 实现的库），所以它很容易编译。zuo/build 库是以 make 和 Shake 为模型的，用于跟踪依赖关系和构建步骤</li> 
 <li>支持模板向量 (stencil vector)</li> 
 <li>支持运行 Windows 的 Arm64 设备</li> 
 <li>Redex 支持同步替换 (simultaneous substitutions)</li> 
 <li>Web 服务器通过其“safety limits”结构提供了对最大并发连接数的控制</li> 
 <li>Web 服务器改进了日志记录性能和请求解析性能，降低了尾部延迟 (tail latencies)</li> 
 <li>Web 服务器通过 web-server/dispatchers/dispatch-logresp 支持记录响应状态代码</li> 
 <li>db 库支持 PostgreSQL 连接的自定义类型</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.racket-lang.org%2F2022%2F08%2Fracket-v8-6.html" target="_blank">详情查看发布公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            