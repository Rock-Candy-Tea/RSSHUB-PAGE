
---
title: '微软发布 Pyjion 1.0，用于 Python 的 JIT 编译器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1111/071844_z77h_2744687.png'
author: 开源中国
comments: false
date: Thu, 11 Nov 2021 07:18:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1111/071844_z77h_2744687.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">用于 Python 3.10 及以上版本的 的 JIT 编译器<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.trypyjion.com%2F" target="_blank">Pyjion</a><span> </span>已发布 1.0 版本。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Pyjion 是由 Python 软件基金会研究员和微软研究员 Anthony Shaw  合作开发的一种用于 Python 的即时 (JIT) 编译系统，它不是像 PyPy 那样的独立 runtime，而是在 CPython 3.10 下运行的可安装库。安装后，只需导入 Pyjion 库并启用，即可在程序中使用：导入后运行的所有内容都属于 JIT 编译。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img alt height="405" src="https://static.oschina.net/uploads/space/2021/1111/071844_z77h_2744687.png" width="720" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Pyjion 的工作原理是通过 .NET EE 编译器将 Python 虚拟机操作码编译成汇编语言，基准测试表明：在实际工作中，Pyjion 比常规 Python 快两到三倍，部分优化允许加速10倍，常规算术的速度可以快一个数量级。Pyjion 包含一个中间件层，允许 WSGI 应用程序在 Pyjion 下运行，因此像 web 应用这种长时间运行的应用程序非常适合 JIT 加速。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前，有一些 Python 特性还不能在 Pyjion 中实现，比如 block 和 async/await，不过这些特性都已经在 Pyjion 的路线图中。由于各种各样的原因，让 Python 变得更快非常困难。大多数提高 Python 速度的方法仍然依赖于 Python C API 来实现兼容性，性能也会受到限制。 Pyjion 也不例外，它仍然依赖 Python C API，但  Pyjion 的优化计划（例如，优化对数组类型的访问）表明，它的开发人员已经在思考如何处理这些问题。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Pyjion 1.0 依赖项：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.trypyjion.com%2Fpython.org%2Fdownload" target="_blank">CPython 3.10</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdotnet.microsoft.com%2Fdownload%2Fdotnet%2F6.0" target="_blank">.NET 6</a></li> 
</ul>
                                        </div>
                                      
</div>
            