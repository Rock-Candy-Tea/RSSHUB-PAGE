
---
title: 'GraalVM 21.3.0 社区版发布，高性能跨语言虚拟机'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2676'
author: 开源中国
comments: false
date: Fri, 22 Oct 2021 06:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2676'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">GraalVM 是 Oracle 打造的高性能跨语言虚拟机，支持运行 JavaScript、Python 3、Ruby、R、基于 JVM 的语言（如 Java、Scala 和 Kotlin），以及基于 LLVM 的语言，如 C 和 C++。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">GraalVM 21.3.0 更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新功能</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>现在默认使用 TRegex，这为正则表达式的匹配提供了很大的速度提升</li> 
 <li>添加 Polyglot.languages 以显示可用语言的列表。</li> 
 <li>外部对象现在有了一个基于其互操作特性的动态生成的类，如<span> </span><code>ForeignArray</code>，并能更好地与 Ruby 对象集成。</li> 
 <li>外部数组现在拥有 Ruby<span> </span><code>Enumerable</code><span> </span>的所有方法和<span> </span><code>Array</code><span> </span>的许多方法。</li> 
 <li>外部哈希现在拥有 Ruby<span> </span><code>Enumerable</code><span> </span>的所有方法和<span> </span><code>Hash</code><span> </span>的许多方法。</li> 
 <li>外部的迭代器 (<span> </span><code>InteropLibrary#hasIterator</code>) 现在拥有 Ruby<span> </span><code>Enumerable</code><span> </span>的所有方法。</li> 
 <li>外部对象现在实现了<span> </span><code>#instance_variables</code>和<span> </span><code>#methods</code>。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">错误修正</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复<span> </span><code>rb_str_modify_expand</code>，以保留现有的字节。</li> 
 <li>修复<span> </span><code>Dir.mkdir</code><span> </span>对<span> </span><code>Pathname</code><span> </span>路径的错误处理。</li> 
 <li>修复多次加载同一文件时的常量查找。</li> 
 <li>修正<span> </span><code>define_method(name, &block)</code><span> </span>方法中<span> </span><code>break</code>、<span> </span><code>next</code><span> </span>和<span> </span><code>redo</code><span> </span>的处理。</li> 
 <li>修复<span> </span><code>Float#<=></code>中不兼容类型的处理。</li> 
 <li>修正<span> </span><code>Dir.glob</code><span> </span>的大括号转义问题。</li> 
 <li>修复<span> </span><code>base64</code><span> </span>解码时输出丢失的问题。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">兼容性</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>实现<span> </span><code>Process::Status.wait</code>。</li> 
 <li>更新<span> </span><code>rb_str_modify</code><span> </span>和<span> </span><code>rb_str_modify_expand</code>，当给定一个冻结的字符串时引发<span> </span><code>FrozenError</code><span> </span>。</li> 
 <li>实现<span> </span><code>rb_fiber_*</code><span> </span>函数。</li> 
 <li>实现<span> </span><code>rb_str_vcatf</code>。</li> 
 <li>实现<span> </span><code>rb_str_catf</code>。</li> 
 <li>接受字符串作为<span> </span><code>StringScanner#scan</code>和<span> </span><code>StringScanner#check</code>的模式参数。</li> 
 <li>……</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Ftruffleruby%2Freleases%2Ftag%2Fvm-21.3.0" target="_blank">https://github.com/oracle/truffleruby/releases/tag/vm-21.3.0</a></p>
                                        </div>
                                      
</div>
            