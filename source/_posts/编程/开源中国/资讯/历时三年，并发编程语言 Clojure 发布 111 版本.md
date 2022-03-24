
---
title: '历时三年，并发编程语言 Clojure 发布 1.11 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=562'
author: 开源中国
comments: false
date: Thu, 24 Mar 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=562'
---

<div>   
<div class="content">
                                                                                            <p>并发编程语言 Clojure 是一种 LISP 风格的语言，运行在JVM上。自 <a href="https://www.oschina.net/news/102867/clojure-1-10-released"><strong>Clojure 1.10 发布</strong></a><strong> </strong>三年半后，Clojure 1.11 版本发布了，Clojure 1.11 提供了用于关键字参数调用的新语法、无需加载的命名空间别名、新的 clojure.math 命名空间以及许多其他错误修复和增强功能。</p> 
<p>关键字参数是可选的尾随变量参数，形式为<em>(f akey aval bkey bval ...​)</em>。使用关键字参数调用函数写起来很方便，但是关键字参数不是集合，所以它们很难在函数之间流动。在 Clojure 1.11 中，采用关键字参数的函数现在可以传递一个尾随映射，而不是键/值对，或者除了键/值对之外也可以在键/值对之后传递。当一个单独的映射被传递时，它用于解构，否则尾映射被 conj 添加到键/值对映射中，此更改使关键字 arg 函数更便于编程。</p> 
<p>Spec（和其他库）依赖限定关键字作为规范名称。 ns 中的命名空间别名使长名称更短，但需要命名空间才能存在和加载。 在 Clojure 1.11 中，require 添加了一个新选项 <code>:as-alias</code>，它类似于 :as，但不需要命名空间存在或加载。</p> 
<p>JDK 包 java.lang.Math 提供了对许多有用的数学函数的访问。Clojure 以前依赖于通过互操作使用这些函数，但在可发现性、原始性能、高阶应用程序和可移植性方面存在问题。新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fclojure.github.io%2Fclojure%2F%23clojure.math" target="_blank">clojure.math</a> 命名空间为 java.lang.Math 中可用的方法提供了包装函数，用于快速原语调用的<code>long</code> 和 <code>double</code> 重载。</p> 
<p>有关 Clojure 1.11.0 中所有更改的完整列表，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fclojure%2Fclojure%2Fblob%2Fmaster%2Fchanges.md%23changes-to-clojure-in-version-1110" target="_blank">更改日志</a>。</p>
                                        </div>
                                      
</div>
            