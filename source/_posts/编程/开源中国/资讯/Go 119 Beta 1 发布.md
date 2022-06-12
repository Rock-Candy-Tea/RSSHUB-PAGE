
---
title: 'Go 1.19 Beta 1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1005'
author: 开源中国
comments: false
date: Sun, 12 Jun 2022 08:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1005'
---

<div>   
<div class="content">
                                                                                            <p>Go 1.19 预计将于 2022 年 8 月发布，目前 Go 1.19 的 beta 版本发布了，下面介绍一下 GO 1.19 版本的主要变更：</p> 
<h2>语言的变化</h2> 
<p>语言只有一个很小的变化，对方法声明中类型参数的范围进行了很小的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgo%2Fissues%2F52038" target="_blank">修正</a>。现有程序不受影响。</p> 
<h2>记忆模型</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftip.golang.org%2Fref%2Fmem" target="_blank">Go 内存模型</a>已经过修改，以使 Go 与 C、C++、Java、JavaScript、Rust 和 Swift 使用的内存模型保持一致 。</p> 
<h2>端口</h2> 
<p>Go 1.19 支持 Linux 上的龙芯 64 位架构 LoongArch 。<span style="color:#202224">(</span><code>GOOS=linux</code><span style="color:#202224">, </span><code>GOARCH=loong64</code><span style="color:#202224">).</span></p> 
<h2>工具</h2> 
<h3>文档评论</h3> 
<p>Go 1.19 在文档注释中添加了对链接、列表和更清晰的标题的支持。作为此更改的一部分，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftip.golang.org%2Fcmd%2Fgofmt" target="_blank"><code>gofmt</code></a> 现在可用于重新格式化文档注释，以使其呈现的含义更清晰。</p> 
<h3>新的<code>unix</code>构建约束</h3> 
<p>现在可以在 //go:build 行中识别构建约束 unix。 如果目标操作系统（也称为 GOOS）是 Unix 或类 Unix 系统，则满足约束。</p> 
<h2>运行</h2> 
<p>运行时现在包括对软内存限制的支持。此内存限制包括 Go 堆和运行时管理的所有其他内存，不包括外部内存源，例如二进制文件本身的映射、以其他语言管理的内存以及操作系统代表 Go 程序持有的内存。</p> 
<p> </p> 
<h2>编译器</h2> 
<ul> 
 <li>编译器现在使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBranch_table" target="_blank">跳转表</a>来实现大整数和字符串 switch 语句。switch 语句的性能改进各不相同，可以快 20% 左右。</li> 
 <li><code>riscv64</code> 端口现在支持使用寄存器传递函数参数和结果，基准测试显示有 10% 或更多的性能改进。</li> 
 <li>Go 编译器现在需要该 <code>-p=importpath</code> 标志来构建可链接的目标文件。</li> 
</ul> 
<h2>汇编器</h2> 
<p>与编译器一样，汇编器现在需要该 <code>-p=importpath</code>标志来构建可链接的目标文件。</p> 
<h2>链接器</h2> 
<p>在 ELF 平台上，链接器现在以标准 gABI 格式而不是传统的 <code>.zdebug</code> 格 发出压缩的 DWARF 部分。</p> 
<p> </p> 
<p>其他内容可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftip.golang.org%2Fdoc%2Fgo1.19" target="_blank">go1.19 文档</a>中查看，其中一部分更改还未实现，或许在正式版本有所删减。</p>
                                        </div>
                                      
</div>
            