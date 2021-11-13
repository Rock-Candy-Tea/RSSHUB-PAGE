
---
title: 'Ruby 3.1.0 Preview 1 发布，合并 YJIT'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9935'
author: 开源中国
comments: false
date: Sat, 13 Nov 2021 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9935'
---

<div>   
<div class="content">
                                                                                            <p>Ruby 3.1.0 Preview 1 现已发布。Ruby 3.1 合并了 YJIT，一个由 Shopify 开发的新的进程内 JIT 编译器。根据介绍，YJIT 既实现了快速的 <span style="background-color:#ffffff; color:#111111">warmup time</span>，又在大多数软件上实现了性能改进；在 railsbench 上可达 22%，在 liquid-render 上可达 39%。</p> 
<p>目前，YJIT 仍然是一个实验性的功能，因此它默认是禁用的；需要通过<code class="language-plaintext">--yjit</code>命令行选项来进行启用。它目前也只限于 x86-64 平台的 macOS 和 Linux。</p> 
<p>其他的一些版本更新内容包括有：</p> 
<ul> 
 <li>一个新的 <span style="background-color:#ffffff; color:#4e4242">debug.gem 调试器取代了 lib/debug.rb 标准库。</span><span style="background-color:#ffffff; color:#111111">debug.gem 是快速调试器实现，它提供了许多功能，如远程调试、colorful REPL、IDE (VSCode) 集成等。</span></li> 
 <li><span style="background-color:#ffffff; color:#111111">引入了一个内置的 gem，error_highlight。它包括在回溯中 fine-grained error location。默认启用的，可通过使用命令行选项 --disable-error_highlight 来禁用。</span></li> 
</ul> 
<pre><code>$ ruby test.rb
test.rb:1:in `<main>': undefined method `time' for 1:Integer (NoMethodError)

1.time &#123;&#125;
 ^^^^^
Did you mean?  times</code></pre> 
<ul> 
 <li>Irb 改进</li> 
 <li>语言方面：Hash literals 和关键字参数中的值可以省略，<span style="background-color:#ffffff; color:#111111">模式匹配中的 Pin 运算符现在采用表达式。</span></li> 
 <li><span style="background-color:#ffffff; color:#4e4242">用于描述 Ruby 程序结构的 RBS 语言也进行了更新：</span> 
  <ul> 
   <li><span style="background-color:#ffffff; color:#4e4242">引入了 rbs collection 来管理 gems 的 RBS</span></li> 
   <li><span style="background-color:#ffffff; color:#4e4242">对内置和标准库的签名的更新和添加</span></li> 
   <li><span style="background-color:#ffffff; color:#4e4242">许多错误修复和性能改进</span></li> 
  </ul> </li> 
 <li><span style="background-color:#ffffff; color:#111111">Ruby 的静态类型分析器 TypeProf 更新：</span> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fruby%2Ftypeprof%2Fblob%2Fmaster%2Fdoc%2Fide.md" target="_blank">实验性 IDE 支持</a>已实现。</li> 
   <li>许多错误修复和性能改进。</li> 
  </ul> </li> 
 <li><span style="background-color:#ffffff; color:#111111">MJIT 性能改进</span> 
  <ul> 
   <li><span style="background-color:#ffffff; color:#111111">对于 Rails 这样的工作负载，默认的 --jit-max-cache 从 100 改为 10000。JIT 编译器不再跳过超过 1000 条指令的方法的编译。</span></li> 
   <li><span style="background-color:#ffffff; color:#111111">为了支持 Rails 的 Zeitwerk，当启用 class events 的 TracePoint 时，JIT-ed code 不再被取消。</span></li> 
  </ul> </li> 
 <li><span style="background-color:#ffffff; color:#111111">One-line pattern matching，例如，</span><code class="language-plaintext">ary => [x, y, z]</code><span style="background-color:#ffffff; color:#111111">，不再是试验性的。</span></li> 
 <li><span style="background-color:#ffffff; color:#111111">多重分配评估顺序略有变化。</span></li> 
 <li><span style="background-color:#ffffff; color:#111111">可变宽度分配：字符串（实验性）</span></li> 
</ul> 
<p><span style="color:#111111">更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ruby-lang.org%2Fen%2Fnews%2F2021%2F11%2F09%2Fruby-3-1-0-preview1-released%2F" target="_blank">查看官方公告</a>。</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            