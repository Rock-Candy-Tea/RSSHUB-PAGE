
---
title: 'Lux 0.7 发布，函数式 Lisp'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=92'
author: 开源中国
comments: false
date: Fri, 19 Aug 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=92'
---

<div>   
<div class="content">
                                                                                            <p>Lux 0.7 已发布，这是一门函数式、具备静态类型的 Lisp 编程语言，支持在 Java 虚拟机、JavaScript、Python、Lua 和 Ruby 解释器上运行。</p> 
<p><strong>Lux 0.7 主要变化</strong></p> 
<p><strong>新增</strong></p> 
<ul> 
 <li>内联函数</li> 
 <li>支持<span style="color:#24292f">将配置参数从构建描述 (</span>build description<span style="color:#24292f">) 传递给编译器</span></li> 
 <li>基于配置参数的代码选择</li> 
 <li>基于编译器版本的代码选择</li> 
 <li>实验性阶段的可扩展元编译器 (meta-compiler) 架构</li> 
 <li>导出 machinery 以使用来自宿主语言程序的 Lux 代码</li> 
 <li>Generalized/type-agnostic arithmetic</li> 
 <li><span style="color:#24292f">【可选】更快（但不安全）的数组处理机制</span></li> 
 <li><span style="color:#24292f">【可选】更快（但不安全）的文本处理机制</span></li> 
 <li><span style="color:#24292f">【可选】</span>更快（但不安全）的二进制处理机制</li> 
 <li>使用 Aedifex 部署版本</li> 
 <li>可扩展的 import 语法</li> 
 <li>上下文感知的宏</li> 
 <li><span style="color:#24292f">用于更可控的宏扩展的宏词汇表</span></li> 
</ul> 
<p><strong>变更</strong></p> 
<ul> 
 <li><span style="color:#24292f">JVM 编译不再依赖 ASM 库</span></li> 
 <li>更友好的语法</li> 
 <li>在 JVM FFI 中不再自动转换基本类型</li> 
 <li><span style="color:#24292f">现在要求使用强制性的 </span>loop name，<span style="color:#24292f">而不是使用默认的 </span>"again" name</li> 
 <li>改进 JVM 互操作语法</li> 
 <li>宏作为一等公民的值</li> 
 <li>模式匹配现在支持匹配全局定义的常量</li> 
 <li>模式中的所有（正常）宏现在都会自动展开</li> 
</ul> 
<p><strong>Bugfix</strong></p> 
<ul> 
 <li>修复支持原语冗余的模式匹配错误</li> 
 <li>修复与编译器扩展相关的各种错误</li> 
 <li>修复多项 JVM 互操作错误</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLuxLang%2Flux%2Freleases%2Ftag%2F0.7.0" target="_blank">详情查看 release note</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            