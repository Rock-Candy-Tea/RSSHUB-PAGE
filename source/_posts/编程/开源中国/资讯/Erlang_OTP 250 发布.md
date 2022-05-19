
---
title: 'Erlang_OTP 25.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4190'
author: 开源中国
comments: false
date: Thu, 19 May 2022 07:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4190'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ferlang.org%2Fpipermail%2Ferlang-announce%2F2022-May%2F000208.html" target="_blank">Erlang/OTP 25.0 已发布</a>，这是一个新的重要版本，带来了新特性、改进和修复，当然也包含一些不兼容的改动。</p> 
<blockquote> 
 <p>Erlang 是一种通用的并发函数式程序设计语言。Erlang 也可以指 Erlang/OTP 的通称，开源电信平台 (OTP) 是 Erlang 的常用执行环境及一系列标准组件。</p> 
</blockquote> 
<p>主要变化</p> 
<h3 style="text-align:start">stdlib</h3> 
<ul> 
 <li><code><font face="-apple-system, BlinkMacSystemFont, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Segoe UI, PingFang SC, Hiragino Sans GB, Microsoft YaHei, Helvetica Neue, Helvetica, Arial, sans-serif"><span style="background-color:#ffffff; font-size:16px">引入新函数</span></font>filelib:ensure_path/1</code><span>，用于</span><span style="background-color:#ffffff; color:#424242">确保给定路径的所有目录都存在</span></li> 
 <li>为<code>maps</code>模块引入新函数<code>groups_from_list/2</code>和<code>groups_from_list/3</code></li> 
 <li>为<code>lists</code>module模块引入新函数<code>uniq/1</code><span> </span><code>uniq/2</code></li> 
 <li>将新的 PRNG 添加到<code>rand</code>模块，用于快速生成伪随机数</li> 
</ul> 
<h3 style="text-align:start">compiler, kernel, stdlib, syntax_tools</h3> 
<ul> 
 <li>增加了对<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erlang.org%2Feeps%2Feep-0060" target="_blank"><code>EEP-60</code></a>中描述的可选择特性的支持。在编译过程中可以用<code>erlc</code>的选项 (ordinary and +term) 以及文件中的指令来启用/禁用特性。类似的选项可以用在<code>erl</code>中，用于启用/禁用运行时允许的特性。新的<code>maybe</code>表达式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erlang.org%2Feeps%2Feep-0049" target="_blank"><code>EEP-49</code></a>作为 may_expr 特性被完全支持。</li> 
</ul> 
<h3 style="text-align:start">erts & JIT</h3> 
<ul> 
 <li><span style="background-color:#ffffff; color:#424242">JIT 现在适用于 64 位 ARM 处理器</span></li> 
 <li>JIT 现在根据 BEAM 文件中的类型信息进行基于类型的优化。</li> 
 <li>改进了 JIT 对<code>perf</code>和<code>gdb</code>等外部工具的支持，允许它们显示行号，甚至可以找到原始的 Erlang 源代码。</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erlang.org%2Fnews%2F157" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            