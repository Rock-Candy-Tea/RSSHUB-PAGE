
---
title: 'iOS底层学习——LLVM编译流程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8f426632c394ab4ba1aee82104a8697~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 08:00:53 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8f426632c394ab4ba1aee82104a8697~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1.LLVM概念</h1>
<h3 data-id="heading-1">1.编译器</h3>
<p>在学习<code>LLVM</code>之前我们先了解一下什么是编译器？</p>
<p>简单讲，编译器就是将<code>一种语言（通常为高级语言）</code>翻译为<code>另一种语言（通常为低级[语言]</code>的程序。一个现代编译器的主要工作流程：源代码(<code>source code</code>) → 预处理器<code>(preprocessor</code>) → 编译器(<code>compiler</code>) →  目标代码(<code>object code</code>) → 链接器(<code>Linker</code>) → 可执行程序(<code>executables</code>)</p>
<p>源代码一般为高级语言(<code>High-level language</code>)， 如<code>C</code>、<code>C++</code>、<code>Java</code>、<code>Objective-C</code>等或汇编语言，而目标则是机器语言的目标代码(<code>Object copy</code>)，有时也称作机器代码(<code>Machine code</code>)。</p>
<p>我们用两种语言来做个对比：解释型语言和编译型语言。</p>
<ul>
<li>
<p>解释型语言</p>
<p>下面引入一个<code>Python</code>代码，见下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8f426632c394ab4ba1aee82104a8697~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建一个<code>FirstDemo.py</code>文件，里面只有一行代码，<code>print('Hello world for first time')</code>。通过解释器指令<code>pythop</code>，解释这段代码：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/453199f8110549ad9a400184024f6ca2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上面的流程可以发现解释型语言的运行流程：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c11e72793726499b986ed8a86bc06a9c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解释型语言特点：<code>边解释，边执行，运行速度慢，部分改动无需整体重新编译，不可脱离解释器环境运行。</code></p>
</li>
<li>
<p>编译型语言</p>
<p>下面引入一个<code>C</code>代码，见下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90866200ed2449e0bc414a8f43e7d0e1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建一个<code>firstDemoForC.c</code>文件，里面添加了一个<code>main</code>函数。首先通过<code>clang</code>去读取这个代码:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9246075fd94881b69e12513d2e21fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>读取之后发现代码并没有立刻执行，而是生成了一个<code>a.out</code>文件。这个文件就是可执行文件。通过<code>./a.out</code>执行这段代码：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/105f59c4a3e54dfd9f10eb58d8523885~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上面的流程可以发现编译型语言的运行流程：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac36891c5be44e63a4ac766801094577~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编译型语言特点：<code>先整体编译，再执行，运行速度快，任意改动需重新编译，可脱离编译环境运行。</code></p>
</li>
</ul>
<p>解释型语言：读到相应代码就直接执行</p>
<p>编译型语言：先将代码编译成<code>cpu</code>可读的懂的二进制才能执行</p>
<h3 data-id="heading-2">2.LLVM概述</h3>
<p><code>LLVM</code>是构架编译器(<code>compiler</code>)的框架系统，以<code>C++</code>编写而成，用于优化以任意程序语言编写的程序的编译时间(<code>compile-time</code>)、链接时间(<code>link-time</code>)、运行时间<code>(run-time</code>)以及空闲时间(<code>idle-time</code>)，对开发者保持开放，并兼容已有脚本。</p>
<p><code>LLVM</code>计划启动于<code>2000</code>年，最初由美国<code>UIUC</code>大学的<code>Chris Lattner</code>博士主持开展。<code>2006</code>年<code>Chris Lattner</code>加盟<code>Apple Inc.</code>并致力于<code>LLVM</code>在<code>Apple</code>开发体系中的应用。<code>Apple</code>也是<code>LLVM</code>计划的主要资助者。</p>
<p>目前<code>LLVM</code>已经被<code>Apple</code>、<code>Microsoft</code>、<code>Google</code>、<code>Facebook</code>等各大公司采用。</p>
<ul>
<li>
<p>传统编译器的设计</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7d3f88ff3c14eb18bc3ce945973e206~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>编译器前端(<code>Frontend</code>)</p>
<p>编译器前端的任务是解析源代码。它会进行：词法分析、语法分析、语义分析，检查源代码是否存在错误，然后构建抽象语法树，<code>LLVM</code>的前端会生成中间代码<code>IR</code>。</p>
</li>
<li>
<p>优化器(<code>Optimizer</code>)</p>
<p>优化器负责进行各种优化。改善运行时间，例如消除冗余计算等。</p>
</li>
<li>
<p>后端(<code>Backend</code>)</p>
<p>也可以叫代码生成器(<code>CodeGenerator</code>)，将代码映射到目标指令集。生成机器语言，并且进行机器相关的代码优化。</p>
</li>
</ol>
</li>
</ul>
<p>随着高级语言越来越多，终端类型种类的增加，所使用的的<code>CPU</code>架构等也不尽相同，所以为了适配多种环境，不得不设计不同的编译器，而这些编译器前端和后端往往是捆绑在一起的。</p>
<ul>
<li>
<p><code>LLVM</code>设计思路</p>
<p><code> LLVM</code>的设计之初，即将编译器前端(<code>Frontend</code>)和后端(<code>Backend</code>)进行了分离。将前端和后端针对不同的架构，按照独立的项目进行研发，而它们均采用通用的代码形式<code>IR</code>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d94fba5086d40ea8e7170cfb3ae9e87~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当编译器决定支持多种语言或多种硬件架构时，<code>LLVM</code>最重要的地方就体现出来了，使用通用的代码表示形式(<code>IR</code>)，它是用来在编译器中表示代码的形式。所以<code>LLVM</code>可以为任何编程语言独立编写前端，并且可以为任意硬件架构独立编写后端。</p>
</li>
<li>
<p><code>iOS</code>编译架构</p>
<p><code>Objective C</code>/<code>C</code>/<code>C++</code>使用的编译器前端是<code>Clang</code>，<code>Swift</code>是<code>Swift</code>，后端都是<code>LLVM</code>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f36f7b8954eb4421be51ccfd01e97fac~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-3">3.Clang</h3>
<p><code>Clang</code>是<code>LLVM</code>项目中的一个子项目。它是基于<code>LLVM</code>架构的轻量级编译器，诞生之初是为了替代<code>GCC</code>，提供更快的编译速度。它是负责编译<code>C</code>、<code>C++</code>、<code>Objective-C</code>语言的编译器，它属于整个<code>LLVM</code>架构中，编译器前端。对于开发者来说，研究<code>Clang</code>可以给我们带来很多好处。</p>
<h1 data-id="heading-4">2.编译流程</h1>
<p>通过命令可以打印源码的编译阶段。引入下面一个案例，<code>main.m</code>中添加代码</p>
<pre><code class="copyable">int main(int argc, const char * argv[]) &#123;
    return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过指令<code>clang -ccc-print-phases main.m</code>，查看编译流程：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee911637becd4b989d0bd35ce28b2ebb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>流程说明：</strong></p>
<ol start="0">
<li>输入文件：找到源文件</li>
<li>预处理阶段：这个过程处理包括宏的替换，头文件的导入</li>
<li>编译阶段：进行词法分析、语法分析、检测语法是否正确，最终生成<code>IR</code></li>
<li>后端：这里<code>LLVM</code>会通过一个一个的<code>Pass（节点）</code>去优化，每个<code>Pass</code>做一些事情，最终生成汇编代码</li>
<li>生成目标文件</li>
<li>链接：链接需要的动态库和静态库，生成可执行文件</li>
<li>通过不同的架构，生成对应的可行文件</li>
</ol>
<h3 data-id="heading-5">1.预处理</h3>
<p>执行如下指令：<code>clang -E main.m</code>，对源代码进行预处理。见下面流程:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4767dfe0787f42fb9e4503cb778127fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在预处理之后，输出<code>mainE.m</code>文件，查看<code>mainE.m</code>文件：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1b4301fac804bfaaa0cb5170ac816ea~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开<code>mainE.m</code>源文件会发现，其进行了宏的替换，如上面案例中宏<code>c</code>直接替换成了<code>30</code>；进行头文件的导入。</p>
<h3 data-id="heading-6">2.编译阶段</h3>
<ul>
<li>
<p>词法分析</p>
<p>预处理完成后就会进行词法分析，这里会把代码切成一个个<code>Token</code>，比如大小括号，等于号以及字符串等。词法分析指令为：</p>
<pre><code class="copyable">clang -fmodules -fsyntax-only -Xclang -dump-tokens main.m
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考下面的案例：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04b9e4d01a914c83ad044364b152a8e5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过指令的输出可以看到，语法分析会将源码进行切割并检测。比如分号，逗号，<code>int</code>等。</p>
</li>
<li>
<p>语法分析</p>
<p>词法分析完成之后就是语法分析，它的任务是验证语法是否正确。在词法分析的基础上将单词序列组合成各类语法短语，如:<code>程序</code>，<code>语句</code>，<code>表达式</code>等等，然后将所有节点组成<code>抽象语法树（Abstract Syntax Tree，AST）</code>。语法分析程序判断源程序在结构上是否正确。语法分析指令：</p>
<pre><code class="copyable">clang -fmodules -fsyntax-only -Xclang -ast-dump main.m
<span class="copy-code-btn">复制代码</span></code></pre>
<p>语法分析输出结果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/550d68b0019a4027a32446314e6f318d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上面的输出可以发现，其是一个树结构，比如下面的<code>FunctionDecl</code>，表示一个<code>方法</code>，在源码的<code>第五行</code>，名称为<code>main</code>，返回值为<code>int</code>，传入两个参数一个是<code>int</code>，一个是<code>const char **</code>。见下图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3beceb62ac5442eeb2ad1de8dfc05820~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong><code>这里需要注意的是，一旦生成抽象语法树，如果源码中存在语法错误，就会报错，而上面的预处理和词法分析不会报错。</code></strong></p>
<p>如在源码中设置一个语法错误，通过语法分析指令进行进行编译，就会报错，见下面案例：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ba0182be2864085bb0ad599809f9fe7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>生成中间代码<code>IR(intermediate representation)</code></p>
<p>完成以上步骤后，就开始生成中间代码<code>IR</code>了，代码生成器<code>（Code Generation）</code>会将语法树自顶向下遍历逐步翻译成<code>LLVM IR</code>。通过下面指令可以生成<code>.ll</code>的文本文件，查看<code>IR</code>代码。</p>
<pre><code class="copyable">clang -S -fobjc-arc -emit-llvm main.m
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的指令获取<code>main.ll</code>文件，其结构见下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9939340cbb9497aaf1560d0c22131a8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>IR的基本语法
<ul>
<li><code>@</code> 全局标识</li>
<li><code>%</code> 局部标识</li>
<li><code>alloca</code> 开辟空间</li>
<li><code>align</code> 内存对齐</li>
<li><code>i32</code> <code>32</code>个<code>bit</code>，<code>4</code>个字节</li>
<li><code>store</code> 写入内存</li>
<li><code>load</code> 读取数据</li>
<li><code>call</code> 调用函数</li>
<li><code>ret</code> 返回</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>IR</code>优化</p>
<p>上面生成的<code>IR</code>代码是没有经过优化的，其实我们在平时阅读代码时，经常会看下面的一些定义：</p>
<pre><code class="copyable">#define fastpath(x) (__builtin_expect(bool(x), 1))
#define slowpath(x) (__builtin_expect(bool(x), 0))
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>fastpath</code>：可以理解为快速流程，对更有可能执行的流程进行优化，调高运行速度；</li>
<li><code>slowpath</code>：基本流程，不被优化的。</li>
</ul>
<p>在<code>XCode</code>中也有相应的优化设置入口：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7b9bf9d84de4734a5b593644102e3f5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>LLVM</code>的优化级别分别是<code>-O0</code> <code>-O1</code> <code>-O2</code> <code>-O3</code> <code>-Os</code>(第一个是大写英文字母<code>O</code>)。可以通过下面的指令获取优化后的<code>IR</code>代码，也就是<code>.ll</code>文件：</p>
<pre><code class="copyable">clang -Os -S -fobjc-arc -emit-llvm main.m -o main.ll
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的指令，进行优化后获取的<code>IR</code>代码见下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbadb22ec43c49ad88dfb1ee1312561e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>相较于优化前，代码精简了很多。</p>
<p>这里需要注意的是，通常<code>debug模式</code>下，优化模式选择<code>None -O0</code>，也就是不优化，避免一些保留代码被屏蔽，从而影响调试。而<code>release模式</code>设置为<code>Fastest,Smallest -Os</code>。</p>
</li>
<li>
<p><code>bitCode</code></p>
<p><code>Xcode7</code>以后开启<code>bitCode</code>苹果会做进一步的优化，生成<code>.bc</code>的中间代码。我们通过优化后的<code>IR</code>代码生成<code>.bc</code>代码。对应指令为：</p>
<pre><code class="copyable">clang -emit-llvm -c main.ll -o main.bc
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-7">3.后端生成汇编代码</h3>
<p>我们通过最终的<code>.bc</code>或者<code>.ll</code>代码生成汇编代码：</p>
<pre><code class="copyable">    clang -S -fobjc-arc main.bc -o main.s
    clang -S -fobjc-arc main.ll -o main.s
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成汇编代码也可以进行优化：</p>
<pre><code class="copyable">    clang -Os -S -fobjc-arc main.m -o main.s
<span class="copy-code-btn">复制代码</span></code></pre>
<p>采用相同的案例，分别三种方式生成汇编代码，可以看到其优化效果。在进行<code>IR</code>优化后生成的<code>.ll</code>文件，依然可以进行优化生成回应的汇编代码。在不同的节点上都可以进行优化。见下图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8c8002d78c84c41a03f6a38d0320242~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">4.生成目标文件(汇编器)</h3>
<p>目标文件的生成，是汇编器以汇编代码作为输入，将汇编代码转换为机器代码，最后输出目标文件（<code>object file</code>）。指令为：</p>
<pre><code class="copyable">clang -fmodules -c main.s -o main.o
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成目标文件，见下图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a67b357ffd547cab93a4e7fe9032c1a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中<code>main.o</code>文件即为目标文件，但是此时生成的目标文件是不可执行的。通过<code>nm</code>命令，查看下<code>main.o</code>中的符号：</p>
<pre><code class="copyable">    $xcrun nm -nm main.o
            (undefined) external _printf
    0000000000000000 (__TEXT,__text) external _test
    000000000000000a (__TEXT,__text) external _main
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>_printf</code>是一个<code>undefifined external</code>的</li>
<li><code>undefifined</code>表示在当前文件暂时找不到符号<code>_printf</code></li>
<li><code>external</code>表示这个符号是外部可以访问的</li>
</ul>
<p>此时就需要链接，链接器把编译生成的<code>.o</code>文件和（<code>.dylib</code> <code>.a</code>）文件链接生成一个<code>mach-o</code>文件。</p>
<pre><code class="copyable">    clang main.o -o main
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成对应的可执行文件，见下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56b8df7ad4e548f39ca8c2f2966794f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查看链接之后的符号：</p>
<pre><code class="copyable">$xcrun nm -nm main
        (undefined) external _printf (from libSystem)
        (undefined) external dyld_stub_binder (from libSystem)
0000000100000000 (__TEXT,__text) [referenced dynamically] external __mh_execute_header
000000100000f6d (__TEXT,__text) external _test
000000100000f77 (__TEXT,__text) external _main
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以发现此时的外部函数有<code>2</code>个，<code>_printf</code>和<code>dyld_stub_binder</code>，它们都来自<code>libSystem</code>库。<code>dyld_stub_binder</code>这个函数的作用是进行运行时绑定流程。<strong><code>链接是在编译时，用来确定外部函数来自哪个动态库；绑定是在运行时，将对应方法的实现地址与符号进行绑定。</code></strong></p>
<p>可执行文件运行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1b9b6b33eca4655a66879ffb1b24cef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            