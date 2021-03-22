
---
title: 'D 语言_DLang 2.096.0 发布，增强跨平台能力！'
categories: 
    - 编程
    - 开源中国
    - 资讯

author: 开源中国
comments: false
date: Sun, 21 Mar 2021 14:20:00 GMT
thumbnail: ''
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>DMD 2.096.0 正式发布更新，DMD 是 D语言官方推出的编译器，此版本包含了 17 项主要变更，同时修复 81 个已知<code>bug</code>。相信过几天 LDC 也会跟进到本次大更新！这个版本有 54 个开发者进行参与，非常感谢他们为 DLang 的发展做出的贡献。</p> 
 <h2>编译器变更</h2> 
 <ul> 
  <li><code>x86_64 Posix</code> 平台下的 <code>D ABI</code> 有所更改</li> 
  <li>新增类型：<code>__c_complex_float</code>、<code>__c_complex_double</code> 和 <code>__c_complex_real</code></li> 
  <li>不再支持构造函数复制和块复制(postblit)</li> 
  <li><code>DMD</code> 的 <code>JSON</code> 输出现在会包含保护级成员</li> 
  <li><code>DMD</code> 的 <code>JSON</code> 输出现在会区分处理模块的构造方法和析构方法（包含有无<code>shared</code>的情形）</li> 
  <li>局部模板不再支持接收通过别名(<code>alias</code>)传入的局部符号</li> 
  <li>增强了 <code>C++</code> 头文件的生成功能</li> 
  <li>新增编译器开关：-gdwarf=<<code>version</code>></li> 
  <li>新增 <code>__traits(getVisibility, Sym)</code> 来替代 <code>getProtection</code></li> 
  <li>无参的 <code>synchronized</code> 语句现在会使用运行时分配的互斥量</li> 
  <li>允许使用更短形式的函数实现（单一表达式函数）</li> 
 </ul> 
 <h2>运行时变更</h2> 
 <ul> 
  <li>移除了 <code>druntime</code> 里的参数选项 <code>callStructDtorsDuringGC</code></li> 
  <li>在 <code>mount</code> 模块里，移除了与 <code>FreeBSD</code> 相关的 <code>statvfs</code> 声明</li> 
  <li>新增体验功能：基于 <code>backtrace</code> 输出的 <code>llvm-libunwind</code></li> 
 </ul> 
 <h2>库变更</h2> 
 <ul> 
  <li>弃用 <code>std.math</code> 模块里的 <code>approxEqual</code> 方法</li> 
 </ul> 
 <h2>Dub变更</h2> 
 <ul> 
  <li>支持更多 <code>DMD</code> 的连接器参数</li> 
  <li><code>VisualD</code> 的工程里允许使用 <code>copyFiles</code></li> 
 </ul> 
 <h2>更多参考</h2> 
 <ul> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.096.0.html" target="_blank">DMD 2.096.0 – Changelog</a></li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            