
---
title: 'Swift 5.6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7833'
author: 开源中国
comments: false
date: Tue, 15 Mar 2022 07:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7833'
---

<div>   
<div class="content">
                                                                                            <p><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Swift 5.6 现已正式发布。此版本</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>包括了对类型系统的许多增强、改进了与指针的交互，并增加了使用包管理器运行新插件命令的能力。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution" target="_blank">Swift Evolution</a> <span style="background-color:#ffffff; color:#333333">流程中的一些提案也在 Swift 5.6 中得以实现：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0290-negative-availability.md" target="_blank">SE-0290</a> - Unavailability Condition</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0302-concurrent-value-and-concurrent-closures.md" target="_blank">SE-0302</a> - <code class="language-plaintext">Sendable</code>和<code class="language-plaintext">@Sendable</code>closures</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0315-placeholder-types.md" target="_blank">SE-0315</a> - <span style="background-color:#ffffff; color:#000000">Type placeholders</span>（以前称为“<span style="background-color:#ffffff; color:#000000">Placeholder types</span>”）</li> 
</ul> 
<pre style="text-align:start"><code><span style="color:var(--color-syntax-keywords)">enum</span> <span>Either</span><strong><</strong><span>Left</span><span>,</span> <span>Right</span><strong>></strong> <span>&#123;</span>
  <span style="color:var(--color-syntax-keywords)">case</span> <span>left</span><span>(</span><span>Left</span><span>)</span>
  <span style="color:var(--color-syntax-keywords)">case</span> <span>right</span><span>(</span><span>Right</span><span>)</span>
<span>&#125;</span>

<span style="color:var(--color-syntax-comments)">// Inferred as 'Either<ClosedRange<Int>, Range<Int>>'</span>
<span style="color:var(--color-syntax-keywords)">let</span> <span>either</span><span>:</span> <span>Either</span><strong><</strong><span>_</span><span>,</span> <span>Range</span><strong><</strong><span>Int</span><strong>>></strong> <strong>=</strong> <strong>.</strong><span>left</span><span>(</span><span style="color:var(--color-syntax-numbers)">0</span><strong>...</strong><span style="color:var(--color-syntax-numbers)">10</span><span>)</span></code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0320-codingkeyrepresentable.md" target="_blank">SE-0320</a> - 允许在<code class="language-plaintext">KeyedContainer</code>中对非<code class="language-plaintext">String</code><span style="background-color:#ffffff; color:#000000"><span> </span>/<span> </span></span><code class="language-plaintext">Int</code>键入的 Dictionary 进行编码</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0322-temporary-buffers.md" target="_blank">SE-0322</a> - 临时未初始化的缓冲区。这<span style="background-color:#ffffff; color:#000000">引入了一种创建临时未初始化内存空间的新方法，这在与需要提供用于存储计算结果的内存的 C API 交互时特别有用。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0324-c-lang-pointer-arg-conversion.md" target="_blank">SE-0324</a> - 放宽 C 函数指针参数的诊断。此更改允许将不安全指针的可<span style="color:#000000">变体（例如</span><code class="language-plaintext">UnsafeMutablePointer</code><span style="color:#000000">）传递给采用不可变体（例如</span><code class="language-plaintext">UnsafePointer</code><span style="color:#000000">）的API，而无需显式转换。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0331-remove-sendable-from-unsafepointer.md" target="_blank">SE-0331</a> - 从不安全的指针类型中删除 Sendable 一致性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0335-existential-any.md" target="_blank">SE-0335</a> - 引入了 existential any</li> 
</ul> 
<pre style="text-align:start"><code><span style="color:var(--color-syntax-keywords)">protocol</span> <span>DataSourceObserver</span> <span>&#123;</span> <strong>...</strong> <span>&#125;</span>

<span style="color:var(--color-syntax-keywords)">struct</span> <span>DataSource</span> <span>&#123;</span>
  <span style="color:var(--color-syntax-keywords)">var</span> <span>observers</span><span>:</span> <span>[</span><span>any</span> <span>DataSourceObserver</span><span>]</span> <span>&#123;</span> <strong>...</strong> <span>&#125;</span>
<span>&#125;</span></code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0337-support-incremental-migration-to-concurrency-checking.md" target="_blank">SE-0337</a> - 增量迁移到并发检查。在 Swift 5.6 中，关于 Sendable 的诊断默认是被抑制的，但可以通过明确定义对 Sendable 的符合性或使用 -warn-concurrency 编译器标志来启用，从而实现并发检查的增量迁移路径。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.swift.org%2Fblog%2Fswift-5.6-released%2F" target="_blank">https://www.swift.org/blog/swift-5.6-released/</a></p>
                                        </div>
                                      
</div>
            