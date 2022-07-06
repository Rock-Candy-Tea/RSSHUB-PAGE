
---
title: 'V（Vlang）0.3 正式发布，改进泛型'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1830d499f9dd4a10c79ca6910afe6bfa681.png'
author: 开源中国
comments: false
date: Wed, 06 Jul 2022 07:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1830d499f9dd4a10c79ca6910afe6bfa681.png'
---

<div>   
<div class="content">
                                                                                            <p>自 0.2 版以来（2020 年 12 月），有 5769 个提交被推送到 master 分支，有 1697 个 bug 被修复。从现在开始，Vlang 将每隔 4 个月做一次重大更新。</p> 
<p><img alt height="408" src="https://oscimg.oschina.net/oscnet/up-1830d499f9dd4a10c79ca6910afe6bfa681.png" width="700" referrerpolicy="no-referrer"></p> 
<p>V 0.3 部分更新内容如下：</p> 
<ul> 
 <li>通过 C2V 进行 C 到 V 的转译： <code>v translate file.c</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D6oXrz3oRoEg" target="_blank">演示视频</a>，YouTube）</li> 
 <li>在 V、cgen 和 C 互操作中进行了大量的错误修正，以允许运行转译好的 DOOM.v</li> 
 <li>用 V 编译器构建的程序不再默认泄漏内存</li> 
 <li>Vlang Closures 支持所有的操作系统</li> 
 <li><code>Option</code> 和 <code>Result</code> 现在是独立的类型，旧的代码将在未来 1 年内可以继续正常使用</li> 
 <li>在类型检查器中增加了数百个新的检查</li> 
 <li>所有 V 的后端都被分割成独立的进程，因此构建 V 的速度提高了 26%。</li> 
 <li><code>ustring</code> 已被 <code>[]rune</code> 所取代</li> 
 <li>Maps 现在可以有非字符串的键</li> 
 <li>C 后端现在是并行的（目前只有 cgen 部分）</li> 
 <li>大量的编译器源代码的清理和优化。根据 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ffast.vlang.io" target="_blank">fast.vlang.io</a> 的数据，编译器的速度提高了 ~30%</li> 
 <li>更好的编译器源代码组织</li> 
 <li>V 的整数类型的命名现在更加一致了： <code>byte</code> 已被改名为 <code>u8</code>，旧的代码将在未来 1 年内可以继续正常使用</li> 
 <li>错别字检测器现在高亮显示了建议的名称，从而使其更加明显</li> 
 <li><code>datatypes</code> 模块现在有 <code>Heap</code>, <code>Queue</code>, <code>Stack</code>, <code>BSTree</code>, <code>LinkedList</code></li> 
 <li>vlib 现在有一个 TOML 解析器，与 TOML 1.0 完全兼容。</li> 
 <li>在 V.js 后端做了很多工作，包括图形库，它已被移植到 V.js</li> 
 <li>现在可以通过使用数组中的每个单独元素来进行更复杂的数组初始化 (<code>[]int&#123;init: it&#125;</code>)</li> 
 <li>V 中加入了移位运算符 <code>>>></code> 和 <code>>>>=</code>（它们的工作原理与 Java 中的完全一样）</li> 
 <li><code>nofloat</code> 选项，这对编写内核和没有 FPU 的嵌入式系统很有用</li> 
 <li>TCC 现在与语言捆绑在一起，这允许在不依赖外部 C 编译器的情况下构建 V 程序</li> 
 <li>Null 可以只在 <code>unsafe</code> 的情况下使用</li> 
 <li>新模块 <code>compress.gzip</code></li> 
 <li>大量的 <code>net</code>/ <code>net.http</code>/ <code>vweb</code> 修正</li> 
 <li>支持 IPv6</li> 
 <li>Go2V 转译器已经由社区启动，并且已经可以转译简单的程序</li> 
 <li>Go 后端的早期版本（ <code>v -b go -o file.go file.v</code>）</li> 
 <li>引入 <code>isize</code> 和 <code>usize</code> 类型，弃用 <code>size_t</code>，改用 <code>usize</code>。</li> 
 <li>添加 <code>datatypes</code> 和 <code>datatypes.fsm</code> 模块。</li> 
 <li>泛型接口</li> 
 <li>修复泛型中的更多错误</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvlang%2Fv" target="_blank">https://github.com/vlang/v</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            