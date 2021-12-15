
---
title: 'Go 1.18 Beta 1 可用，带有泛型'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7660'
author: 开源中国
comments: false
date: Wed, 15 Dec 2021 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7660'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Go 1.18 Beta 1 现已可用，这是 Go 1.18 的第一个预览版；Go 1.18 的正式版发布还需要几个月的时间。</p> 
<p>感兴趣的用户可以访问<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgo.dev%2Fdl%2F%23go1.18beta1" target="_blank">下载页面获取 Go 1.18 Beta 1</a>。</p> 
<p style="text-align:start"><span><span><span style="color:#202224"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Go 1.18 Beta 1 是第一个包含 Go 对<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgo.dev%2Fblog%2Fwhy-generics" target="_blank">使用参数化类型的泛型代码</a>的新支持的预览版本。官方表示，泛型是自 Go 1 发布以来 Go 最重要的变化，也是他们所做过的最大的单一语言变化。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<blockquote> 
 <p style="text-align:start"><span><span><span style="color:#202224"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>对于任何大型的新功能，新用户发现新错误是很常见的，我们不希望泛型成为这个规则的例外；一定要以适当的谨慎态度对待它们。此外，某些微妙的情况，例如特定类型的递归泛型类型，已推迟到未来版本。也就是说，我们知道一些早期采用者已经相当满意，如果你有你认为特别适合泛型的用例，我们希望你能尝试一下。我们发布了一个 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgo.dev%2Fdoc%2Ftutorial%2Fgenerics" target="_blank">关于如何开始使用泛型的简短教程，</a> 并<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D35eIxI_n5ZM%26t%3D1755s" target="_blank">在上周的 GopherCon 上做了一个</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D35eIxI_n5ZM%26t%3D1755s" target="_blank">演讲</a>。你甚至可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgo.dev%2Fplay%2F%3Fv%3Dgotip" target="_blank">Go playground 的 Go dev 分支模式下</a>试用 。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
</blockquote> 
<p>此外，<span style="color:#202224">Go 1.18 Beta 1<span> </span></span>还包含：</p> 
<ul> 
 <li>添加了对编写<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgo.dev%2Fblog%2Ffuzz-beta" target="_blank">基于模糊测试的</a>内置支持 ，以自动查找导致程序崩溃或返回无效答案的输入。</li> 
 <li>添加了一个新的“<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgo.dev%2Fdesign%2F45713-workspace" target="_blank">Go workspace mode</a>”，它允许用户同时使用多个 Go 模块，这对大型项目来说是一个重要的用例。</li> 
 <li>包含一个扩展<code>go version -m</code>命令，它现在可以记录 compiler flags 等构建细节 。程序可以使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkg.go.dev%2Fruntime%2Fdebug%40master%23BuildInfo" target="_blank">debug.ReadBuildInfo</a> 查询自己的构建细节 ，现在可以使用新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkg.go.dev%2Fdebug%2Fbuildinfo%40master" target="_blank">debug/buildinfo</a> 包从其他二进制文件中读取构建细节 。此功能旨在成为任何需要为 Go 二进制文件生成软件物料清单 (SBOM) 的工具的基础。</li> 
 <li>Go 1.17 曾添加了一个新的基于寄存器的调用约定，以加速 x86-64 系统上的 Go 代码。Go 1.18 Beta 1 将该功能扩展到 ARM64 和 PPC64，从而提高了 20% 的速度。</li> 
</ul> 
<p>更多详情可查看官方博客：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgo.dev%2Fblog%2Fgo1.18beta1" target="_blank">https://go.dev/blog/go1.18beta1</a></p>
                                        </div>
                                      
</div>
            