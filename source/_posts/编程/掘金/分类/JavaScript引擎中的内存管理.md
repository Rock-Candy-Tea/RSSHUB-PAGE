
---
title: 'JavaScript引擎中的内存管理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff61b5742d034f65ab0ae2af8f4a791b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 23:16:39 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff61b5742d034f65ab0ae2af8f4a791b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概述</h2>
<p>像 C 这样的编程语言，具有低级内存管理原语，如malloc()和free()。开发人员使用这些原语显式地对操作系统的内存进行分配和释放。</p>
<p>而JavaScript在创建对象(对象、字符串等)时会为它们分配内存，不再使用对时会“自动”释放内存，这个过程称为垃圾收集。这种看“自动”似释放资源的的特性是造成混乱的根源，因为这给JavaScript(和其他高级语言)开发人员带来一种错觉，以为他们可以不关心内存管理的错误印象，这是想法一个大错误。</p>
<p>即使在使用高级语言时，开发人员也应该了解内存管理(或者至少懂得一些基础知识)。有时候，自动内存管理存在一些问题(例如垃圾收集器中的bug或实现限制等)，开发人员必须理解这些问题，以便可以正确地处理它们(或者找到一个适当的解决方案，以最小代价来维护代码)。</p>
<h2 data-id="heading-1">内存是什么?</h2>
<p>我们现在常用的计算机都属于 <strong>冯·诺依曼体系计算机</strong>， 计算机硬件由 <strong>控制器、运算器、存储器、输入设备、输出设备</strong> 五大部分组成。</p>
<p>我们通常所说的内存就是 <strong>存储器</strong>（<strong>RAM</strong>随机存取存储器）。</p>
<p>常用的内存都是易失性存储器（需要通过不断加电刷新来保持数据，一旦断电就会导致数据丢失），所以需要一种容量大、低成本的非易失性存储器来进行数据的存储，这就是外存，例如磁带、软盘、硬盘、光盘、闪存卡、U盘等。可以将外存理解为输入输出设备，因为外存是需要通过I/O接口进行数据存取的，而内存是由CPU直接寻址的。外存中的程序需要通过I/O接口调入内存中才可以运行。</p>
<p>内存就是程序运行的地方，其实程序本质上就是指令和数据的集合。所以说内存是指令和数据的临时存储器，然后CPU对内存中的指令和数据进行处理。</p>
<h3 data-id="heading-2">它是如何工作的</h3>
<p>硬件层面上，计算机内存由大量的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFlip-flop_%2528electronics%2529" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Flip-flop_%28electronics%29" ref="nofollow noopener noreferrer">触发器</a><strong>组成的。每个触发器包含几个晶体管，能够存储一位，单个触发器都可以通过唯一标识符寻址，因此我们可以读取和覆盖它们。因此，从概念上讲，可以把的整个计算机内存看作是一个可以读写的巨大<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBit_array" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Bit_array" ref="nofollow noopener noreferrer">位数组</a></strong>。</p>
<p>作为人类，我们并不擅长用比特来思考和计算，所以我们把它们组织成更大的组，这些组一起可以用来表示数字。8位（比特）称为1字节（byte）。除了字节，还有字符（words）(有时是16位，有时是32位)。<strong>不同编码里，字符和字节的对应关系不同：</strong></p>
<p>很多东西都存储在内存中:</p>
<ol>
<li>程序使用的所有变量和其他数据。</li>
<li>程序的代码，包括操作系统的代码。</li>
</ol>
<p>编译器和操作系统一起为你处理大部分内存管理，但是你还是需要了解一下底层的情况，对内在管理概念会有更深入的了解。</p>
<p>在编译代码时，编译器可以检查基本数据类型，并提前计算它们需要多少内存。然后将所需的大小分配给调用堆栈空间中的程序，分配这些变量的空间称为堆栈空间。因为当调用函数时，它们的内存将被添加到现有内存之上，当它们终止时，它们按照后进先出（LIFO）顺序被移除。例如：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">int</span> n; <span class="hljs-comment">// 4字节</span>
<span class="hljs-keyword">int</span> x [<span class="hljs-number">4</span>]; <span class="hljs-comment">// 4个元素组成的数组，每个4个字节</span>
<span class="hljs-keyword">double</span> m；<span class="hljs-comment">// 8个字节</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译器能够立即知道所需的内存:4 + 4×4 + 8 = 28字节。</p>
<blockquote>
<p>这段代码展示了整型和双精度浮点型变量所占内存的大小。但是大约20年前,整型变量通常占2个字节,而双精度浮点型变量占4个字节。你的代码不应该依赖于当前基本数据类型的大小。</p>
</blockquote>
<p>编译器将插入与操作系统交互的代码，并申请存储变量所需的堆栈字节数。</p>
<p>在上面的例子中，编译器知道每个变量的确切内存地址。事实上，每当我们写入变量 <code>n</code> 时，它就会在内部被转换成类似<code>“内存地址4127963”</code>这样的信息。</p>
<p>注意，如果我们尝试访问 <code>x[4]</code>,将访问与m关联的数据。这是因为访问数组中一个不存在的元素（它比数组中最后一个实际分配的元素x[3]多4字节），可能最终读取(或覆盖)一些 m 位。这肯定会对程序的其余部分产生不可预知的结果。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff61b5742d034f65ab0ae2af8f4a791b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当函数调用其他函数时，每个函数在调用堆栈时获得自己的块。它保存所有的局部变量，但也会有一个程序计数器来记住它在执行过程中的位置。当函数完成时，它的内存块将再次用于其他地方。</p>
<h2 data-id="heading-3">内存的生命周期</h2>
<p>无论使用哪种编程语言,内存的生命周期都是一样的:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20b5acee3d5e42efb95055ac56b8b6ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这里简单介绍一下内存生命周期中的每一个阶段:</p>
<ul>
<li><strong>分配内存</strong> —  内存是由操作系统分配的，它允许您的程序使用它。在<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E4%25BD%258E%25E7%25BA%25A7%25E8%25AF%25AD%25E8%25A8%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E4%BD%8E%E7%BA%A7%E8%AF%AD%E8%A8%80" ref="nofollow noopener noreferrer">低级语言</a></strong>(例如C语言)中，这是一个开发人员需要自己处理的显式执行的操作。然而，在高级语言中，系统会自动为你分配内在。</li>
<li><strong>使用内存</strong> — 这是程序实际使用之前分配的内存，在代码中使用分配的变量时，就会发生读和写操作。</li>
<li><strong>释放内存</strong> — 释放所有不再使用的内存,使之成为自由内存,并可以被重利用。与分配内存操作一样,这一操作在低级语言中也是需要显式地执行。</li>
</ul>
<p>在JavaScript中，第一步和第三步由js引擎完成的。</p>
<h2 data-id="heading-4">JavaScript引擎的内存模型</h2>
<p>以V8引擎为例。</p>
<p>一个运行中的程序总是与内存中的一部分空间相对应。这部分空间叫做 Resident Set (驻留集)。说到这个就有个Resident set size的概念引出，此处不详细解释，大家可以去了解下内存耗用VSS/RSS/PSS/USS这些概念。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8477c0cd3c843aba157012e904d486e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>各部分作用如下：</p>
<ul>
<li><strong>Code Segment</strong> : 存放正在被执行的代码</li>
<li><strong>Stack</strong> : 栈内存，存放标识符、基本类型值及引用类型变量的堆地址</li>
<li><strong>Heap</strong> : 堆内存，存放引用类型值</li>
</ul>
<p>在多线程情况下，每个线程将拥有其自己的完全独立的stack，但它们将共享heap。stack是特定于线程的，而heap是特定于应用程序的。在异常处理和线程执行中，stack是重要的考虑因素。</p>
<p>JavaScript是一种单线程编程语言，这意味着它只有一个调用栈。</p>
<p>在 Node.js 中，我们可以通过调用process.memoryUsage() 方法来来查询内存使用情况。该函数返回值如下：
memory usage
&#123;
rss: 4935680,
heapTotal: 1826816,
heapUsed: 650472,
external: 49879
&#125;
以上数值以字节为单位
• rss：表示 Resident Set 的大小
• heapTotal：表示堆的总大小
• heapUsed：表示堆的实际使用大小
• external：表示 V8 管理的绑定到 JavaScript 对象的 C++ 对象的大小</p>
<h2 data-id="heading-5">堆栈</h2>
<h3 data-id="heading-6">什么是堆和栈？</h3>
<p>堆和栈本质上是两种数据结构。</p>
<p>栈（数据结构）：一种先进后出的数据结构。</p>
<p>堆（数据结构）：堆可以被看成是一棵树，如：堆排序。</p>
<h3 data-id="heading-7">栈（stack）</h3>
<p>用于<strong>静态内存分配</strong></p>
<p>栈是内存中一块用于存储局部变量和函数参数的线性结构，遵循着先进后出的原则。数据只能顺序的入栈，顺序的出栈。当然，栈只是内存中一片连续区域一种形式化的描述，数据入栈和出栈的操作仅仅是栈指针在内存地址上的上下移动而已。如下图所示（以 C 语言为例）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6352d0ecf7446be88be394856a04d4f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>栈中的变量在函数调用结束后，就会消失。</p>
<p>栈是由操作系统自动管理的，而不是由V8本身进行管理的</p>
<h3 data-id="heading-8">堆（heap）</h3>
<p>堆用于<strong>动态内存分配</strong>，与堆栈不同，程序需要使用<strong>指针</strong>在堆中查找数据（将其视为大型的多层库）。</p>
<p>堆是计算机内存中不会自动为您管理的区域，并且不受CPU严格管理。它是内存中更自由浮动的区域（并且更大）。要在堆上分配内存，必须使用<code>malloc()</code>或<code>calloc()</code>，它们是内置的C函数。在堆上<code>free()</code>分配内存后，一旦不再需要该内存，您将负责重新分配该内存。如果您未能执行此操作，则程序将发生所谓的<strong>内存泄漏</strong>。也就是说，堆上的内存仍将被保留（并且其他进程将无法使用）。</p>
<p>与堆栈不同，堆对可变大小没有大小限制（除了计算机明显的物理限制之外）。堆内存的读取和写入速度稍慢，因为必须使用<strong>指针</strong>来访问堆上的内存。</p>
<p>与堆栈不同，可以在程序中的任何位置通过任何函数访问在堆上创建的变量。堆变量的作用域本质上是全局的。</p>
<h3 data-id="heading-9">Stack vs Heap</h3>
<p>因此栈的特点：</p>
<ul>
<li>
<p>快速访问（后进先出<strong>LIFO</strong>）</p>
</li>
<li>
<p>存储在栈中的任何数据都必须是<strong>有限且静态的</strong>（数据大小在编译时是已知的）</p>
</li>
<li>
<p><strong>多线程应用程序</strong>每个线程<strong>可以有一个</strong>栈。</p>
</li>
<li>
<p>栈的内存管理非常**简单明了，**并且由操作系统完成，内存不会碎片化</p>
</li>
<li>
<p>存储的数据是局部变量：基本类型值，引用类型变量的堆地址，<strong>指针</strong>，函数帧（帧包含提供给函数的参数，函数的局部变量以及函数执行的地址）</p>
<p>--每一个被调用的函数都有一个自己的栈帧结构，并且栈帧结构是由函数自己形成的。栈帧的最顶端以两个指针界定——帧指针(寄存器ebp)和栈指针(esp)---具体了解可以参看《深入理解计算机系统》）</p>
</li>
<li>
<p>栈大小限制（取决于OS及架构：i386，x86_64 , PowerPC。多数架构上默认栈大小都在 2 ~ 4 MB 左右)</p>
</li>
<li>
<p>变量无法调整大小</p>
</li>
</ul>
<p>因此堆的特点：</p>
<ul>
<li>
<p>（相对栈）访问速度较慢</p>
</li>
<li>
<p>存储具有<strong>动态大小的</strong>数据</p>
</li>
<li>
<p>堆在应用程序的线程之间<strong>共享</strong>。</p>
</li>
<li>
<p>您必须管理内存（您负责分配和释放变量）</p>
</li>
<li>
<p>存储在堆中的典型数据是<strong>全局变量</strong>，<strong>引用类型</strong></p>
</li>
<li>
<p>内存大小无限制（一般来讲在32位系统下，堆内存可以达到4G的空间从这个角度来看堆内存几乎是没有什么限制的）</p>
</li>
<li>
<p>无法保证有效利用空间，随着时间的推移，内存块可能会随着内存块的分配而碎片化，然后释放</p>
<p>JavaScript中使用的堆栈，对象存储在Heap中，并在需要时引用</p>
<p><img src="https://i.imgur.com/7KpvEn1.gif" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h2 data-id="heading-10">动态分配（基于堆的内存分配）</h2>
<p>在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E8%25AE%25A1%25E7%25AE%2597%25E6%259C%25BA%25E7%25A7%2591%25E5%25AD%25A6" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6" ref="nofollow noopener noreferrer">计算机科学</a>中, <strong>动态内存分配</strong>（Dynamic memory allocation）又称为<strong>堆内存分配</strong>，是指<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E8%25AE%25A1%25E7%25AE%2597%25E6%259C%25BA%25E7%25A8%258B%25E5%25BA%258F" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F" ref="nofollow noopener noreferrer">计算机程序</a>在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E8%25BF%2590%25E8%25A1%258C%25E6%259C%259F" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E8%BF%90%E8%A1%8C%E6%9C%9F" ref="nofollow noopener noreferrer">运行期</a>中分配使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%2586%2585%25E5%25AD%2598" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E5%86%85%E5%AD%98" ref="nofollow noopener noreferrer">内存</a>。它可以当成是一种分配有限内存资源所有权的方法。</p>
<p>动态分配的内存在被程序员明确释放或被<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%259E%2583%25E5%259C%25BE%25E5%259B%259E%25E6%2594%25B6_(%25E8%25A8%2588%25E7%25AE%2597%25E6%25A9%259F%25E7%25A7%2591%25E5%25AD%25B8)" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E5%9E%83%E5%9C%BE%E5%9B%9E%E6%94%B6_(%E8%A8%88%E7%AE%97%E6%A9%9F%E7%A7%91%E5%AD%B8)" ref="nofollow noopener noreferrer">垃圾回收</a>之前一直有效。与<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E9%259D%2599%25E6%2580%2581%25E5%2586%2585%25E5%25AD%2598%25E5%2588%2586%25E9%2585%258D" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E9%9D%99%E6%80%81%E5%86%85%E5%AD%98%E5%88%86%E9%85%8D" ref="nofollow noopener noreferrer">静态内存分配</a>的区别在于没有一个固定的生存期。这样被分配的对象称之为有一个“动态生存期”</p>
<p>不幸的是，当编译时不知道一个变量需要多少内存时，事情就有点复杂了。假设我们想做如下的操作:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">int n = readInput（）; <span class="hljs-comment">//读取用户的输入</span>
...
<span class="hljs-comment">//用“ n”个元素创建一个数组</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在编译时,编译器不知道数组需要使用多少内存,因为这是由用户提供的值决定的。</p>
<p>因此，它不能为堆栈上的变量分配空间。相反，我们的程序需要在运行时显式地向操作系统请求适当的空间,这个内存是从<strong>堆空间</strong>分配的。静态内存分配和动态内存分配的区别总结如下表所示:</p>

























<table><thead><tr><th align="center">静态内存分配</th><th>动态内存分配</th></tr></thead><tbody><tr><td align="center">大小必须在编译时知道</td><td>大小不需要在编译时知道</td></tr><tr><td align="center">在编译时执行</td><td>在运行时执行</td></tr><tr><td align="center">分配给堆栈</td><td>分配给堆</td></tr><tr><td align="center">FILO (先进后出)</td><td>没有特定的分配顺序</td></tr></tbody></table>
<p><strong>动态分配内存的原因和优势：</strong></p>
<ol>
<li>当我们不知道该程序需要多少内存时。</li>
<li>当我们想要没有任何存储空间上限的数据结构时。</li>
<li>当您想更有效地使用您的内存空间时。*示例：*如果您为一维数组分配了存储空间作为array [20]，而最终只使用了10个存储空间，则剩余的10个存储空间将被浪费，而其他程序变量甚至无法利用此浪费的内存。</li>
<li>仅通过操纵地址就可以非常轻松地完成动态创建的列表插入和删除操作，而在静态分配的内存中，插入和删除操作会导致更多的移动和内存浪费。</li>
<li>如果要在编程中使用结构和链表的概念，则必须分配动态内存。</li>
</ol>
<p>要完全理解<em><strong>动态内存分配</strong></em>是如何工作的，需要在c语言以及指针上花费更多的时间，这可能与本文的主题有太多的偏离，这里就不太详细介绍指针的相关的知识了。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FC_dynamic_memory_allocation" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/C_dynamic_memory_allocation" ref="nofollow noopener noreferrer">en.wikipedia.org/wiki/C_dyna…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%258A%25A8%25E6%2580%2581%25E5%2586%2585%25E5%25AD%2598%25E5%2588%2586%25E9%2585%258D" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E5%8A%A8%E6%80%81%E5%86%85%E5%AD%98%E5%88%86%E9%85%8D" ref="nofollow noopener noreferrer">zh.wikipedia.org/wiki/%E5%8A…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmoduscreate.com%2Fblog%2Fdynamic-memory-and-v8-with-javascript%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://moduscreate.com/blog/dynamic-memory-and-v8-with-javascript/" ref="nofollow noopener noreferrer">moduscreate.com/blog/dynami…</a></p>
<h2 data-id="heading-11">在JavaScript中分配内存</h2>
<p>现在将解释第一步:如何在JavaScript中分配内存。参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FMemory_Management" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management" ref="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></p>
<p>与C/C++不同，JavaScript中并没有严格意义上区分栈内存与堆内存。因此我们可以简单粗暴的理解为JavaScript的所有数据都保存在堆内存中。但是在某些场景，我们仍然需要基于堆栈数据结构的思维来实现一些功能，比如JavaScript的执行上下文。执行上下文的执行顺序借用了栈数据结构的存取方式。因此理解栈数据结构的原理与特点十分重要。</p>
<h3 data-id="heading-12">JS数据类型和内存的关系</h3>
<p>ECMAScript中 变量可能包含两种不同数据类型的值:基本类型值和引用类型值。</p>
<p>对于基本类型，数据本身是存在栈内，对于引用类型，在栈中存的只是一个堆内地址的引用。</p>
<p>为了更好的搞懂栈内存与堆内存，我们可以结合以下例子与图解进行理解。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a1 = <span class="hljs-number">0</span>;   <span class="hljs-comment">// 变量对象</span>
<span class="hljs-keyword">var</span> a2 = <span class="hljs-string">'this is string'</span>; <span class="hljs-comment">// 变量对象</span>
<span class="hljs-keyword">var</span> a3 = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 变量对象</span>

<span class="hljs-keyword">var</span> b = &#123; <span class="hljs-attr">m</span>: <span class="hljs-number">20</span> &#125;; <span class="hljs-comment">// 变量b存在于变量对象中，&#123;m: 20&#125; 作为对象存在于堆内存中</span>
<span class="hljs-keyword">var</span> c = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]; <span class="hljs-comment">// 变量c存在于变量对象中，[1, 2, 3] 作为对象存在于堆内存中</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bdbebbaf32040d4b1f1c3884db5dfa7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">值的初始化</h3>
<p>为了不让程序员费心分配内存，JavaScript 在定义变量时就完成了内存分配。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> n = <span class="hljs-number">123</span>; <span class="hljs-comment">// 给数值变量分配内存</span>
<span class="hljs-keyword">var</span> s = <span class="hljs-string">"azerty"</span>; <span class="hljs-comment">// 给字符串分配内存</span>

<span class="hljs-keyword">var</span> o = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">b</span>: <span class="hljs-literal">null</span>
&#125;; <span class="hljs-comment">// 给对象及其包含的值分配内存</span>

<span class="hljs-comment">// 给数组及其包含的值分配内存（就像对象一样）</span>
<span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">"abra"</span>]; 

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">a</span>)</span>&#123;
  <span class="hljs-keyword">return</span> a + <span class="hljs-number">2</span>;
&#125; <span class="hljs-comment">// 给函数（可调用的对象）分配内存</span>

<span class="hljs-comment">// 函数表达式也能分配一个对象</span>
someElement.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  someElement.style.backgroundColor = <span class="hljs-string">'blue'</span>;
&#125;, <span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">通过函数调用分配内存</h3>
<p>某些函数调用也会导致对象的内存分配:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> d = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(); <span class="hljs-comment">// 分配一个 Date 对象</span>

<span class="hljs-keyword">var</span> e = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>); <span class="hljs-comment">// 分配一个 DOM 元素</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有些方法分配新变量或者新对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> s = <span class="hljs-string">"azerty"</span>;
<span class="hljs-keyword">var</span> s2 = s.substr(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>); <span class="hljs-comment">// s2 是一个新的字符串</span>
<span class="hljs-comment">// 因为字符串是不变量，</span>
<span class="hljs-comment">// JavaScript 可能决定不分配内存，</span>
<span class="hljs-comment">// 只是存储了 [0-3] 的范围。</span>

<span class="hljs-keyword">var</span> a = [<span class="hljs-string">"ouais ouais"</span>, <span class="hljs-string">"nan nan"</span>];
<span class="hljs-keyword">var</span> a2 = [<span class="hljs-string">"generation"</span>, <span class="hljs-string">"nan nan"</span>];
<span class="hljs-keyword">var</span> a3 = a.concat(a2); 
<span class="hljs-comment">// 新数组有四个元素，是 a 连接 a2 的结果</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">在JavaScript中使用内存</h2>
<p>基本上，在JavaScript中使用分配的内存意味着对其进行读写。这可以通过读取或写入变量或对象属性的值，或者将参数传递给函数来实现。</p>
<h2 data-id="heading-16">当内存不再需要时进行释放</h2>
<p>大多数内存管理的问题都在这个阶段。</p>
<p>这里最困难的地方是确定何时不再需要分配的内存，它通常要求开发人员确定程序中哪些地方不再需要内存的并释放它。</p>
<p>高级语言嵌入了一种称为垃圾收集器的机制，它的工作是跟踪内存分配和使用，以便发现任何时候一块不再需要已分配的内在。在这种情况下，它将自动释放这块内存。</p>
<p>不幸的是,这个过程只是进行粗略估计,因为知道是否需要一些一块内存的一般问题是<a href="https://link.juejin.cn/?target=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FDecidability_(logic)" target="_blank" rel="nofollow noopener noreferrer" title="http://en.wikipedia.org/wiki/Decidability_(logic)" ref="nofollow noopener noreferrer">不可判定</a> (不能通过算法来解决)。</p>
<p>大多数垃圾收集器通过收集不再被访问的内存来工作，例如，指向它的所有变量都超出了作用域。但是，这是可以收集的内存空间集合的一个不足估计值，因为在内存位置的任何一点上，仍然可能有一个变量在作用域中指向它，但是它将永远不会被再次访问。</p>
<h2 data-id="heading-17">垃圾回收</h2>
<p>由于无法确定某些内存是否真的有用，因此,垃圾收集器想了一个办法来解决这个问题。</p>
<p>堆内存是**垃圾回收（GC）**发生的地方</p>
<h3 data-id="heading-18">什么是垃圾回收</h3>
<p>我们首先先迅速而简单地介绍一下，到底什么是垃圾回收？其实顾名思义，主要是两点：垃圾、回收。</p>
<p>然后基于这两点有个 What/How/When，基本就把事儿讲明白了。翻译成官方术语就是：</p>
<ul>
<li>什么是垃圾？如何找到垃圾？何时找垃圾？</li>
<li>什么是回收？怎么回收？何时回收？</li>
</ul>
<p>对于所有的垃圾回收而言，垃圾其实都是指已经没用的内存区域，回收就是指让这些区域可以被新的有用数据覆盖。</p>
<h3 data-id="heading-19">内存引用</h3>
<p>垃圾收集算法主要依赖的是引用。</p>
<p>在内存管理上下文中，如果对象具有对另一个对象的访问权(可以是隐式的，也可以是显式的)，则称对象引用另一个对象。例如，一个Javascript对象具有对它<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen%2FJavaScript%2FGuide%2FInheritance_and_the_prototype_chain" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en/JavaScript/Guide/Inheritance_and_the_prototype_chain" ref="nofollow noopener noreferrer">原型</a>的引用（隐式引用）和对它属性的引用（显式引用）。</p>
<p>在这种情况下，“对象”的概念不仅特指 JavaScript 对象，还包括函数作用域（或者全局词法作用域）。</p>
<blockquote>
<p>词法作用域定义了如何在嵌套函数中解析变量名:即使父函数已经返回，内部函数也包含父函数的作用</p>
</blockquote>
<p>词法作用域 VS 动态作用域 介绍</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F70b38c7ab69c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/70b38c7ab69c" ref="nofollow noopener noreferrer">www.jianshu.com/p/70b38c7ab…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Flienhua34%2Farchive%2F2012%2F03%2F10%2F2388872.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/lienhua34/archive/2012/03/10/2388872.html" ref="nofollow noopener noreferrer">www.cnblogs.com/lienhua34/a…</a></p>
<h3 data-id="heading-20">垃圾回收算算法</h3>
<p>主流的两类垃圾回收算法有两种，分别是追踪式垃圾回收算法和引用计数法（ Reference counting ）。</p>
<h3 data-id="heading-21">引用计数 (Reference-counting) 垃圾收集算法</h3>
<p>这是最初级的垃圾收集算法。此算法把“对象是否不再需要”简化定义为“对象有没有其他对象引用到它”。如果没有引用指向该对象（零引用），对象将被垃圾回收机制回收。如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> o = &#123; 
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>:<span class="hljs-number">2</span>
  &#125;
&#125;; 
<span class="hljs-comment">// 两个对象被创建，一个作为另一个的属性被引用，另一个被分配给变量o</span>
<span class="hljs-comment">// 很显然，没有一个可以被垃圾收集</span>


<span class="hljs-keyword">var</span> o2 = o; <span class="hljs-comment">// o2变量是第二个对“这个对象”的引用</span>

o = <span class="hljs-number">1</span>;      <span class="hljs-comment">// 现在，“这个对象”只有一个o2变量的引用了，“这个对象”的原始引用o已经没有</span>

<span class="hljs-keyword">var</span> oa = o2.a; <span class="hljs-comment">// 引用“这个对象”的a属性</span>
               <span class="hljs-comment">// 现在，“这个对象”有两个引用了，一个是o2，一个是oa</span>

o2 = <span class="hljs-string">"yo"</span>; <span class="hljs-comment">// 虽然最初的对象现在已经是零引用了，可以被垃圾回收了</span>
           <span class="hljs-comment">// 但是它的属性a的对象还在被oa引用，所以还不能回收</span>

oa = <span class="hljs-literal">null</span>; <span class="hljs-comment">// a属性的那个对象现在也是零引用了</span>
           <span class="hljs-comment">// 它可以被垃圾回收了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e287636f802c4d07829c2f700033c314~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-22">循环会产生问题</h3>
<p>当涉及到循环时,会有一个限制。在下面的示例中,创建了两个对象,两个对象互相引用,从而创建了一个循环。在函数调用之后将超出作用域,因此它们实际上是无用的,应该回收分配的内存。然而,引用计数算法认为,由于每个对象至少被引用一次,导致它们都没有被标记为垃圾回收掉。循环引用是内存泄漏的常见原因。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">var</span> o1 = &#123;&#125;;
  <span class="hljs-keyword">var</span> o2 = &#123;&#125;;
  o1.a = o2; <span class="hljs-comment">// o1 引用 o2</span>
  o2.a = o1; <span class="hljs-comment">// o2 引用 o1  形成了一个循环</span>

  <span class="hljs-keyword">return</span> <span class="hljs-string">"azerty"</span>;
&#125;

f();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8985f070268043688392184721a801b8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">标记-清除(Mark-and-sweep)算法</h3>
<p>该算法把“一个对象不再需要”简化定义为“对象不可访问”。</p>
<p>该算法由以下步骤组成:</p>
<ol>
<li>垃圾收集器构建一个“根”列表,用于保存引用的全局变量。在JavaScript中,“window”对象是一个可作为根节点的全局变量。在Node.js中为“global”对象。</li>
<li>然后，算法检查所有根及其子节点，并将它们标记为活动的(这意味着它们不是垃圾)。任何根不能到达的地方都将被标记为垃圾。</li>
<li>最后，垃圾收集器释放所有未标记为活动的内存块，并将该内存返回给操作系统。</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3cc62cf31374fe1822d6a1533524aa1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​                                                               运行中标记和清除算法的可视化动图</p>
<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Animation_of_the_Naive_Mark_and_Sweep_Garbage_Collector_Algorithm.gif/330px-Animation_of_the_Naive_Mark_and_Sweep_Garbage_Collector_Algorithm.gif" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>该算法是对先前算法的一种改进,因为“有零引用的对象”总是不可访问的，但是相反却不一定，正如我们在循环中看到的那样。</p>
<p>缺点：这种方法有几个缺点，最明显的是在收集过程中必须暂停整个系统。不允许更改工作集。这可能会导致程序定期（通常是不可预测的）“冻结”，从而使某些实时和时间紧迫的应用程序变得不可能。此外，必须检查整个工作内存，其中大部分都要检查两次，从而可能导致<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPaged_memory" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Paged_memory" ref="nofollow noopener noreferrer">分页内存</a>系统出现问题。</p>
<p>（在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FComputer" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Computer" ref="nofollow noopener noreferrer">计算机</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOperating_system" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Operating_system" ref="nofollow noopener noreferrer">操作系统中</a>，<strong>页面调度</strong>是一种<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMemory_management" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Memory_management" ref="nofollow noopener noreferrer">内存管理</a>方案，计算机通过该方案来存储和从<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FComputer_data_storage%23Secondary_storage" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Computer_data_storage#Secondary_storage" ref="nofollow noopener noreferrer">二级存储</a>中检索数据，以供在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FComputer_data_storage%23Primary_storage" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Computer_data_storage#Primary_storage" ref="nofollow noopener noreferrer">主存储器中</a>使用。在此方案中，操作系统从二级存储中以相同大小的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBlock_(data_storage)" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Block_(data_storage)" ref="nofollow noopener noreferrer">块（</a>称为*<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPage_(computer_memory)" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Page_(computer_memory)" ref="nofollow noopener noreferrer">page）</a>*检索数据。分页是现代操作系统中<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FVirtual_memory" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Virtual_memory" ref="nofollow noopener noreferrer">虚拟内存</a>实现的重要组成部分，它使用二级存储来使程序超出可用物理内存的大小。</p>
<p>为简单起见，主存储器称为“ RAM”（“ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FRandom-access_memory" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Random-access_memory" ref="nofollow noopener noreferrer">随机存取存储器</a> ” 的缩写），二级存储称为“磁盘”（“ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FHard_disk_drive" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Hard_disk_drive" ref="nofollow noopener noreferrer">硬盘驱动器</a>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FDrum_memory" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Drum_memory" ref="nofollow noopener noreferrer">磁鼓存储器</a>或<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FSolid-state_drive" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Solid-state_drive" ref="nofollow noopener noreferrer">固态驱动器</a> ” 的简写），但是概念并不取决于这些术语是否从字面上适用于特定的计算机系统。）</p>
<p>截至2012年，所有现代浏览器都有标记-清除垃圾收集器。并且过去几年在JavaScript垃圾收集(分代/增量/并发/并行垃圾收集)领域所做的所有改进都是对标记-清除算法的改进，而不是对垃圾收集算法本身的改进，<strong>也没有简化“一个对象不再需要”的定义。</strong></p>
<p>你以为到这就完了么？NO！以上都是比较简单的是符合逻辑容易理解的。</p>
<h3 data-id="heading-24">如何解决系统相当长的时间内停止的问题？</h3>
<p>mark 阶段会导致应用程序挂起也就是：『<strong>全暂停</strong>式』（Stop-The-World，后面简称 STW）的，当突变（专业术语称 mutator，指能改变这个内存区域是否被程序引用的东西，比如程序本身。简单说就是可以修改 heap）执行，GC 等着；特定时机时（比如内存满了）GC 执行，mutator 等着。因此它的如何找和何时找都比较简单：内存满，STW 开始；而找垃圾就是一种图的遍历，从 Root 出发，对所有能访问的节点进行标记，访问不到的就是垃圾。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9685b496f3224ca3aace8bae58504e04~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>采取 STW 这样凶残的策略，主要还是防止 mutator 在 GC 的时候捣乱——这跟你用扫地机器人的时候把狗关屋子的道理是一样的；而增量标记，就等于赶着狗扫地，是一个跟 mutator 斗智斗勇的过程。</p>
<p>如果我们要解决系统长时间停止的问题需要引入增量式 GC 的概念。</p>
<p>增量式（incremental）GC 顾名思义，允许 collector 分多个小批次执行，每次造成的 mutator 停顿都很小，达到近似实时的效果。</p>
<p>​               <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1a5eb71314d49d8aaee62e3463a1205~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60ac959d237e445b97e0314e2a0845fb~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​                                                                           STW vs 增量式 图1</p>
<p>引用计数类 GC 本身就具有增量式特性，但由于其算法自身的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fliujiacai.net%2Fblog%2F2018%2F06%2F15%2Fgarbage-collection-intro%2F%23%25E5%25BC%2595%25E7%2594%25A8%25E8%25AE%25A1%25E6%2595%25B0%25EF%25BC%2588Reference-counting%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://liujiacai.net/blog/2018/06/15/garbage-collection-intro/#%E5%BC%95%E7%94%A8%E8%AE%A1%E6%95%B0%EF%BC%88Reference-counting%EF%BC%89" ref="nofollow noopener noreferrer">缺陷与效率问题</a>，一般不会采用。而追踪类 GC 实现增量式的难点在于：在 collector 遍历引用关系图，mutator 可能会改变对象间的引用关系</p>
<p>为解决这个问题实现增量式 GC我们需要引入一种新的算法三色标记（Tri-color marking）算法</p>
<h3 data-id="heading-25">三色标记（Tri-color marking）算法</h3>
<p>V8 官博在2018年新发了一篇<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Ftrash-talk%23incremental" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/trash-talk#incremental" ref="nofollow noopener noreferrer">博文</a>介绍 V8 GC 新进展，讲到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.js.cn%2Fblog%2Fconcurrent-marking%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.js.cn/blog/concurrent-marking/" ref="nofollow noopener noreferrer">增量回收</a>的话题。增量 GC 实际上早在 1975 年的一篇<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cs.utexas.edu%2Fusers%2FEWD%2Ftranscriptions%2FEWD05xx%2FEWD520.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cs.utexas.edu/users/EWD/transcriptions/EWD05xx/EWD520.html" ref="nofollow noopener noreferrer">论文</a>中，大宗师 Dijkstra 就已经提出了这个问题的解决方案——<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FTracing_garbage_collection%23Tri-color_marking" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Tracing_garbage_collection#Tri-color_marking" ref="nofollow noopener noreferrer">三色标记算法</a>。（mutator这个词儿也是 Dijkstra 琢磨出来的）</p>
<p>因为增量回收是<strong>并发</strong>的（concurrent），因此它的过程像上面图1一样（可以想象一下 CPU 的时间片轮转），这就意味着 GC 可能被随时暂停、重启，因此暂停时需要保存当时的扫描结果，等下一波 GC 来之后还能继续启动。而双色标记实际上<strong>仅仅是对扫描结果的描述</strong>：非黑即白，但忽略了对<strong>扫描进行状态的描述</strong>：这个点的子节点扫完了没有？假如我上次停在这样一个图上，重新启动的时候我就不仅要问：到底 A、B 点要不要扫子节点？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f9cb4691ad448de9d823636999bc29e~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了处理这种情况，Dijkstra 引入了另外一种颜色：<strong>灰色</strong>，它表示<strong>这个节点被 Root 引用到，但子节点我还没处理</strong>；而<strong>黑色</strong>的意思就变为：这个节点<strong>被 Root 引用</strong>到，而且<strong>子节点都已经标记完成</strong>。这样在恢复扫码时，只需要处理灰色节点即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed36ab59f9aa4e198e61252b1b2e80dd~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>引入灰色标记还有一个好处，就是当图中没有灰色节点时，便是整个图标记完成之时，就可以进行清理工作了。</p>
<p>对象只能从白色移动到灰色，从灰色移动到黑色，因此该算法保留了一个重要的不变性-没有黑色对象引用白色对象。这确保了一旦灰色组为空，则可以释放白色对象。这称为<em><strong>三色不变式</strong></em></p>
<h4 data-id="heading-26">违反三色不变式的情况</h4>
<p>解决了三色的问题，就可以增量回收了么？其实没有这么简单。什么是失败的垃圾回收？无非就是两点：</p>
<ol>
<li>把有用的东西扔了；</li>
<li>把没用的东西留着；</li>
</ol>
<p>其实只要有手段，没用的垃圾还是可以忍它留几轮；但是有用的被干掉是无法忍受的：我刚声明了一个变量你就告诉我 Reference Error，WTF！</p>
<p>对于传统的 STW 而言，通过根节点标记引用，能力立刻区分当前状态下的有用和没用，再做操作的时候便游刃有余；但是对于增量回收而言就不同了，Dijkstra 在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cs.utexas.edu%2Fusers%2FEWD%2Ftranscriptions%2FEWD05xx%2FEWD520.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cs.utexas.edu/users/EWD/transcriptions/EWD05xx/EWD520.html" ref="nofollow noopener noreferrer">论文</a>里举了一个很顽皮的 mutator：</p>
<ol>
<li>三个节点 ABC，C 在 AB 之间反复横跳，一会儿只有 A 指向 C，一会儿只有 B 指向 C；</li>
<li>开始扫 A 时，C 的爸爸是 B，扫完了 A 节点是黑的， C 是白的；</li>
<li>开始扫 B 时，C 的爸爸是 A，扫完了 B 没有子节点，B 节点是黑的，C 还是白的；</li>
<li>由于 A 节点已经标黑，无法扫描其子节点，只好继续向后扫描；</li>
<li>一顿蛇皮操作之后，C 被当成孤儿干掉了，C 的爸爸们留下了无奈的泪水。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5a599dea0b149f5a2ca1dae0fc1fa57~tplv-k3u1fbpfcp-watermark.image" alt="标记遗漏" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-27">如何解决违反三色不变性的问题</h4>
<p>为了解决上面的问题，一般有两类方式来协调 mutator 与 collector 的行为：</p>
<ol>
<li>读屏障（read barrier），它会禁止 mutator 访问白色对象，当检测到 mutator 即将要访问白色对象时，collector 会立刻访问该对象并将之标为灰色。由于 mutator 不能访问指向白色对象的指针，也就无法使黑色对象指向它们了</li>
<li>写屏障（write barrier），它会记录下 mutator 新增的由黑色–>白色对象的指针，并把该对象标为灰色，这样 collector 就又能访问有问题的对象了</li>
</ol>
<p>读/写屏障本质是一些同步操作——在 mutator 进行某些操作前，它必须激活 collector 进行一些操作。</p>
<h5 data-id="heading-28">写屏障</h5>
<p>刚才的案例其实就是说了一个问题：在 mutator 瞎操作的情况下，很有可能将已经标记为扫描完事儿的节点（黑色节点）续上一个当时还未被扫描的白色节点。而一旦这个白色节点后续又被其他已经扫描过的节点引用到，也没有什么机制能够再收集它了。</p>
<p>在思考完这个案例之后，Dijkstra 提出了一个要求：不能让黑色节点指向白色节点！每当发生引用变化时，需要立刻对被引用节点进行着色：即白的立刻染灰，灰的和黑的不变。</p>
<p>比如上面 C 的例子，当 C 的父节点发送变化时，一定会出现类似这样的代码：<code>A.C = C</code>，发生之后，立刻给 C 节点着色并推入灰色栈，这样就解决了不小心清理掉有用节点的问题。</p>
<p><img src="https://malcolmyu.github.io/2019/07/07/Tri-Color-Marking/write-barrier.jpg" alt="写屏障" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-29">读屏障</h5>
<p>不介绍了 参看下面文章</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fliujiacai.net%2Fblog%2F2018%2F08%2F04%2Fincremental-gc%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://liujiacai.net/blog/2018/08/04/incremental-gc/" ref="nofollow noopener noreferrer">liujiacai.net/blog/2018/0…</a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.cs.colorado.edu%2Fdepartment%2Fpublications%2Freports%2Fdocs%2FCU-CS-494-90.pdf" target="_blank" rel="nofollow noopener noreferrer" title="http://www.cs.colorado.edu/department/publications/reports/docs/CU-CS-494-90.pdf" ref="nofollow noopener noreferrer">《Barrier Methods for Garbage Collection》 Benjamin Zorn 1990</a></p>
<h5 data-id="heading-30">总结</h5>
<p>总而言之，三色标记主要是为了解决增量标记中传统双色标记过程无法分片的问题，有了三色标记，传统的双色标记便可以暂停重启，因此就可以划分成小段，变成跟 mutator 并发的方式来运行；写屏障则是用来解决并发中 mutator 变化，导致有用内存被清理的问题。三色标记只是垃圾回收众多技术方案之中的一个，其他如分代假设、清道夫算法等都有其精妙之处，可以深入研究。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/260fa28ffa094a479e179de473e706b3~tplv-k3u1fbpfcp-watermark.image" alt="GC 衍化图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​                                                                                           GC 衍化图</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FTracing_garbage_collection" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Tracing_garbage_collection" ref="nofollow noopener noreferrer">在这篇文章中</a>,你可以更详细地阅读到有关跟踪垃圾收集的详细信息。</p>
<p>也可阅读《垃圾回收的算法与实现》这本书。</p>
<p>资料：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cs.cmu.edu%2F~fp%2Fcourses%2F15411-f08%2Fmisc%2Fwilson94-gc.pdf" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cs.cmu.edu/~fp/courses/15411-f08/misc/wilson94-gc.pdf" ref="nofollow noopener noreferrer">www.cs.cmu.edu/~fp/courses…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fliujiacai.net%2Fblog%2F2018%2F08%2F04%2Fincremental-gc%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://liujiacai.net/blog/2018/08/04/incremental-gc/" ref="nofollow noopener noreferrer">liujiacai.net/blog/2018/0…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fliujiacai.net%2Fblog%2F2018%2F07%2F08%2Fmark-sweep%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://liujiacai.net/blog/2018/07/08/mark-sweep/" ref="nofollow noopener noreferrer">liujiacai.net/blog/2018/0…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fliujiacai.net%2Fblog%2F2018%2F06%2F15%2Fgarbage-collection-intro%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://liujiacai.net/blog/2018/06/15/garbage-collection-intro/" ref="nofollow noopener noreferrer">liujiacai.net/blog/2018/0…</a></p>
<p>目前没有一种垃圾自动回收算法适用于所有场景。v8的内部采用的其实是多种垃圾回收算法。他们回收的对象分别是生存周期较短和生存周期较长的两种对象。
上文说的是基本垃圾回收的方法和原理。</p>
<h3 data-id="heading-31">循环不再是问题</h3>
<p>在上面循环会产生问题的第例子中，在函数调用返回后，这两个对象不再被从全局对象中可访问的对象引用。因此，垃圾收集器将发现它们不可访问。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/253ce4496d8849a5b0690df044de9668~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>即使在对象之间存在引用，也已经无法从根目录访问它们。</p>
<h3 data-id="heading-32">反直觉行为的垃圾回收器</h3>
<p>尽管垃圾收集器很方便,但它们有一套自己的折衷方案,其中之一就是非决定论,换句话说,GC是不可预测的,你无法真正判断何时进行垃圾收集。这意味着在某些情况下,程序会使用更多的内存,这实际上是必需的。在对速度特别敏感的应用程序中,可能会很明显的感受到短时间的停顿。如果没有分配内存,则大多数GC将处于空闲状态。看看以下场景:</p>
<ol>
<li>执行大量分配。</li>
<li>这些元素中的大多数(或全部)被标记为不可访问(假设引用指向一个不再需要的缓存)（假设我们空引用指向我们不再需要的缓存）（假设我们空一个指向我们不再需要的缓存的引用）。</li>
<li>不再执行任何分配。</li>
</ol>
<p>在这些场景中，大多数GCs 将不再继续收集。换句话说，即使有不可访问的引用可供收集，收集器也不会声明这些引用。这些并不是严格意义上的泄漏，但仍然会导致比通常更高的内存使用。</p>
<p>想了解V8垃圾回收器相关： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Ftrash-talk" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/trash-talk" ref="nofollow noopener noreferrer">v8.dev/blog/trash-…</a></p>
<h3 data-id="heading-33">Node.js</h3>
<p>Node.js提供了用于配置和调试内存问题的其他选项和工具，这些问题和工具可能不适用于在浏览器环境中执行的JavaScript。</p>
<h4 data-id="heading-34">V8引擎标志</h4>
<p>可用标志可以增加可用堆内存的最大数量：</p>
<pre><code class="copyable">node --*max-old-space-size=6000* index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还可以使用标志和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fen%2Fdocs%2Fguides%2Fdebugging-getting-started%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/en/docs/guides/debugging-getting-started/" ref="nofollow noopener noreferrer">Chrome Debugger</a>公开垃圾收集器以调试内存问题：</p>
<pre><code class="hljs language-bash copyable" lang="bash">node --expose-gc --inspect index.js
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            