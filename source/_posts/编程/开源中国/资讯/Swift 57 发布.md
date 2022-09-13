
---
title: 'Swift 5.7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4993'
author: 开源中国
comments: false
date: Tue, 13 Sep 2022 07:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4993'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">Swift 5.7 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.swift.org%2Fblog%2Fswift-5.7-released%2F" target="_blank">发布</a>，该版本包括对语言和标准库的主要添加、对编译器的增强以提供更好的开发人员体验、对 Swift 生态系统中的工具（包括 SourceKit-LSP 和 Swift 包管理器）的改进、改进的 Windows 支持等等。</span></p> 
<h4><strong><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>语言和标准库</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Swift 5.7 语言和标准库具有多项改进：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>通用样板代码的新速记语法，包括<code class="language-plaintext">if let</code>语句和多语句 closure type annotations</li> 
 <li>解除长期存在的语言限制，使通用编程更加无缝</li> 
 <li>通过新的 annotations 和 opt-in diagnositcs 增强 data race 安全性</li> 
 <li>分布式环境中的 Actor 隔离</li> 
 <li>改进了一套现有指针 API 的可用性</li> 
 <li>全新的语言支持和字符串处理的 API</li> 
</ul> 
<h4><strong><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>开发者体验</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<p><strong><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的泛型实现</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>除了上述用于处理泛型的语言改进之外，类型检查器的泛型实现也从头开始重写，在正确性和性能方面都有所改进。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的实现修复了许多长期存在的错误，主要与处理复杂的同类型需求有关，例如对集合<code class="language-plaintext">SubSequence</code>关联类型的同类型需求，以及使用<code class="language-plaintext">CaseIterable</code>协议的代码，该协议定义了<code class="language-plaintext">Self.Element == Self</code>的要求。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的泛型实现也提高了性能。在某些协议和关联类型的配置下，类型检查时间在 Swift 5.6 中会呈指数增长，但现在在 Swift 5.7 中是线性的。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>自动引用计数改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在 Swift 5.7 中，通过指定新规则以在允许优化时缩短变量的生命周期，ARC 行为更具可预测性、用户友好性和执行性。为了强制执行这些规则，编译器采用了一种新的内部表示来跟踪每个变量的词法范围。这涉及更新现有的优化和实现几个新的优化。现在，依赖于扩展变量生命周期的最常见编程模式是安全的，无需程序员显式使用<code class="language-plaintext">withExtendedLifetime()</code>，这可以保护你免受仅在优化构建中运行时出现的难以诊断的生命周期错误。它还允许在不破坏现有资源的情况下引入更强大的优化。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Code Completion</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>函数调用参数、变量和全局函数的 Code Completion 现在紧密集成到 Swift 的类型检查器中。这允许 Code Completion 能够在模糊的代码或有错误的代码中提供更准确的结果。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>如果在以下示例中的<code class="language-plaintext">+</code>完成后，Code Completion 现在会报告 int 和 string 与周围的上下文相匹配，允许编辑器将这些结果排在</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>高于<code class="language-plaintext">array</code><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>的位置。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre style="text-align:start"><code><span style="color:var(--color-syntax-keywords)">func</span> <span>makeIntOrString</span><span>()</span> <strong>-></strong> <span>Int</span> <span>&#123;&#125;</span>
<span style="color:var(--color-syntax-keywords)">func</span> <span>makeIntOrString</span><span>()</span> <strong>-></strong> <span>String</span> <span>&#123;&#125;</span>

<span style="color:var(--color-syntax-keywords)">let</span> <span>array</span> <strong>=</strong> <span>[</span><span style="color:var(--color-syntax-numbers)">4</span><span>,</span> <span style="color:var(--color-syntax-numbers)">2</span><span>]</span>
<span style="color:var(--color-syntax-keywords)">let</span> <span>int</span> <strong>=</strong> <span style="color:var(--color-syntax-numbers)">42</span>
<span style="color:var(--color-syntax-keywords)">let</span> <span>string</span> <strong>=</strong> <span style="color:var(--color-syntax-strings)">"Hello World!"</span>
<span>makeIntOrString</span><span>()</span> <strong>+</strong></code></pre> 
<p style="margin-left:0; margin-right:0; text-align:start">如果补全<span style="background-color:#ffffff; color:#000000">以下示例中缺少的参数</span>，<span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Code Completion </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>现在只提示 secondInt 参数标签而省略 secondString。</p> 
<pre style="text-align:start"><code><span style="color:var(--color-syntax-keywords)">func</span> <span>add</span><span>(</span><span>_</span> <span>firstInt</span><span>:</span> <span>Int</span><span>,</span> <span>secondInt</span><span>:</span> <span>Int</span><span>)</span> <span>&#123;&#125;</span>
<span style="color:var(--color-syntax-keywords)">func</span> <span>add</span><span>(</span><span>_</span> <span>firstString</span><span>:</span> <span>String</span><span>,</span> <span>secondString</span><span>:</span> <span>String</span><span>)</span> <span>&#123;&#125;</span>
<span>add</span><span>(</span><span style="color:var(--color-syntax-numbers)">1</span><span>,</span> <span>)</span></code></pre> 
<p style="margin-left:0; margin-right:0; text-align:start">更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.swift.org%2Fblog%2Fswift-5.7-released%2F" target="_blank">查看官方博客</a>。</p>
                                        </div>
                                      
</div>
            