
---
title: 'JavaScript Debugger 原理揭秘'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d192629e37d945fd80d82c703d68fe53~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 07:06:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d192629e37d945fd80d82c703d68fe53~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>代码写完会运行一下看下效果，开发的时候我们更多都是通过 dubugger 来单步或断点运行。我们整天在用 debugger，可是你有想过它的实现原理么。</p>
<p>本文会解答以下问题：</p>
<ul>
<li>代码运行的底层原理是什么</li>
<li>为什么需要 debugger</li>
<li>debugger 实现原理是什么</li>
<li>如何实现 debugger 客户端</li>
</ul>
<h2 data-id="heading-0">代码运行的原理是什么</h2>
<p>代码的运行方式可以分为直接执行和解释执行两类。</p>
<p>不知道平时你有没有注意，可执行文件直接 <code>./xxx</code> 就可以执行，而执行 js 文件需要 <code>node ./xxx</code>，执行 python 文件需要 <code>python ./xxx</code>，这就是编译执行（直接执行）和解释执行的区别。</p>
<h3 data-id="heading-1">直接执行</h3>
<p>cpu 提供了一套指令集，基于这套指令集就可以控制整个计算机的运转，机器语言的代码就是由这些指令和对应的操作数构成的，这些机器码可以直接跑在计算机上，也就是可直接执行。由它们构成的文件叫做可执行文件。</p>
<p>不同操作系统可执行文件的格式不同，在 windows 上是 pe（Portable Executable） 格式，在 linux、unix 系统上是 elf（Executable Linkable Format） 格式，在 mac 上是 mash-o 格式。它们规定了不同的内容（.text 是代码、.data .bass 等是数据）放在文件中的什么位置。但其中真正可执行的部分还是由 cpu 提供的机器指令构成的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d192629e37d945fd80d82c703d68fe53~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>编译型语言会经过编译、汇编、链接的阶段，编译是把源代码转成汇编语言构成的中间代码，汇编是把中间代码变成目标代码，链接会把目标代码组合成可执行文件。这个可执行文件是可以在操作系统上直接执行的。就因为它是由 cpu 的机器指令构成的，可以直接控制 cpu。所以可以直接 <code>./xxx</code> 就可以执行。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2683062728c74a82bfddc2d769e5eedd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">解释执行</h3>
<p>编译型语言都是生成可执行文件直接在操作系统上来执行的，不需要安装解释器，而 js、python 等解释型语言的代码需要用解释器来跑。</p>
<p>为什么有了解释器就不需要生成机器码了，cpu 仍然不认识这些代码啊？</p>
<p>那是因为解释器是需要编译成机器码的，cpu 知道怎么执行解释器，而解释器知道怎么执行更上层的脚本代码，就这样，<strong>由机器码解释执行解释器，再由解释器解释执行上层代码，这就是脚本语言的原理。</strong> 包括 js、python 等都是这样。</p>
<p>但是解释器毕竟多了一层，所以有的时候会把它编译成机器码来直接执行，这就是 JIT 编译器。比如 js 引擎一般就是由 parser、解释器、JIT 编译器、GC 构成，大部分代码是由解释器解释执行的，而热点代码会经过 JIT 编译器编译成由机器码，直接在操作系统上执行以提高性能。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b57e2a355da4e8b96492697eb05ccd1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>编译成机器码直接执行，或者是从源码解释执行，代码就这两种执行方式。两者各有各的好处，编译型速度快，解释型跨平台。这就是代码运行的原理。</strong></p>
<p>王垠说过，<strong>计算机的本质就是解释器</strong>。就是说 cpu 用电路解释机器码，解释器用机器码解释更上层的脚本代码，所以计算机的本质是解释器。</p>
<h2 data-id="heading-3">为什么需要 debugger</h2>
<p>我们知道，图灵完备的语言可以解释任何可计算问题，所以不管是编译型还是解释型都能够描述所有可计算的业务逻辑。</p>
<p>我们利用不同的语言描述业务逻辑，然后运行它看效果，当代码的逻辑比较复杂的时候，难免会出错，我们希望能够一步步运行或是运行到某个点停下来，然后看一下当时的环境中的变量，执行某个脚本。完成这个功能的就是 debugger。</p>
<p>也许还有很多初级程序员只会用 console.log 打日志，但是日志不能完全展现当时的环境，最好的方式还是 debugger。</p>
<p>狼叔说过，<strong>是否会用 debugger 是 nodejs 水平的一个明显的区分</strong>。</p>
<h2 data-id="heading-4">debugger 的原理</h2>
<p>我们知道了 debugger 是调试程序必不可少的，那么它是怎么实现的呢？</p>
<h3 data-id="heading-5">可执行文件的 debugger</h3>
<p>其实 cpu、操作系统在设计的时候就支持了 debugger 的能力（可见 debugger 的重要性），cpu 里面有 4 个寄存器可以做硬中断，操作系统提供了系统调用来做软中断。这是编译型语言的 debugger 实现的基础。</p>
<h4 data-id="heading-6">中断</h4>
<p>cpu 只会不断的执行下一条指令，但程序运行过程中难免要处理一些外部的消息，比如 io、网络、异常等等，所以设计了中断的机制，cpu 每执行完一条指令，就会去看下中断标记，是否需要中断了。就像 event loop 每次 loop 完都要检查下是否需要渲染一样。</p>
<h4 data-id="heading-7">INT 指令</h4>
<p>cpu 支持 INT 指令来触发中断，中断有编号，不同的编号有不同的处理程序，记录编号和中断处理程序的表叫做中断向量表。其中 INT 3 （3 号中断）可以触发 debugger，这是一种约定。</p>
<p>那么可执行文件是怎么利用这个 3 号中断来 debugger 的呢？其实就是运行时替换执行的内容，debugger 程序会在需要设置断点的位置把指令内容换成 INT 3，也就是 0xCC，这就断住了。就可以获取这时候的环境数据来做调试。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c8ae3dc5706430ca1e262a7ffce661e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过机器码替换成 0xcc （INT 3）是把程序断住了，可是怎么恢复执行呢？其实也比较简单，把当时替换的机器码记录下来，需要释放断点的时候再换回去就行了。</p>
<p>这就是可执行文件的 debugger 的原理了，最终还是靠 cpu 支持的中断机制来实现的。</p>
<h4 data-id="heading-8">中断寄存器</h4>
<p>上面说的 debugger 实现方式是修改内存中的机器码的方式，但有的时候修改不了代码，比如 ROM，这种情况就要通过 cpu 提供的 4 个中断寄存器（DR0 - DR3）来做了。这种叫做硬中断。</p>
<p>总之，<strong>INT 3 的软中断，还有中断寄存器的硬中断，是可执行文件实现 debugger 的两种方式。</strong></p>
<h3 data-id="heading-9">解释型语言的 debugger</h3>
<p>编译型语言因为直接在操作系统之上执行，所以要利用 cpu 和操作系统的中断机制和系统调用来实现 debugger。但是解释型语言是自己实现代码的解释执行的，所以不需要那一套，但是实现思路还是一样的，就是插入一段代码来断住，支持环境数据的查看和代码的执行，当释放断点的时候就继续往下执行。</p>
<p>比如 javascript 中支持 debugger 语句，当解释器执行到这一条语句的时候就会断住。</p>
<p>解释型语言的 debugger 相对简单一些，不需要了解 cpu 的 INT 3 中断。</p>
<h2 data-id="heading-10">debugger 客户端</h2>
<p>上面我们了解了直接执行和解释执行的代码的 debugger 分别是怎么实现的。我们知道了代码是怎么断住的，那么断住之后呢？怎么把环境数据暴露出去，怎么执行外部代码？</p>
<p>这就需要 debugger 客户端了。</p>
<p>比如 v8 引擎会把设置断点、获取环境信息、执行脚本的能力通过 socket 暴露出去，socket 传递的信息格式就是 <a href="https://github.com/buggerjs/bugger-v8-client/blob/master/PROTOCOL.md" target="_blank" rel="nofollow noopener noreferrer">v8 debug protocol</a> 。</p>
<p>比如：</p>
<p>设置断点：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"seq"</span>:<span class="hljs-number">117</span>,
    <span class="hljs-string">"type"</span>:<span class="hljs-string">"request"</span>,
    <span class="hljs-string">"command"</span>:<span class="hljs-string">"setbreakpoint"</span>,
    <span class="hljs-string">"arguments"</span>:&#123;
        <span class="hljs-string">"type"</span>:<span class="hljs-string">"function"</span>,
        <span class="hljs-string">"target"</span>:<span class="hljs-string">"f"</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>去掉断点：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"seq"</span>:<span class="hljs-number">117</span>,
    <span class="hljs-string">"type"</span>:<span class="hljs-string">"request"</span>,
    <span class="hljs-string">"command"</span>:<span class="hljs-string">"clearbreakpoint"</span>,
    <span class="hljs-string">"arguments"</span>: &#123;
        <span class="hljs-string">"type"</span>:<span class="hljs-string">"function"</span>,
        <span class="hljs-string">"breakpoint"</span>:<span class="hljs-number">1</span>
     &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>继续：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"seq"</span>:<span class="hljs-number">117</span>,
    <span class="hljs-string">"type"</span>:<span class="hljs-string">"request"</span>,
    <span class="hljs-string">"command"</span>:<span class="hljs-string">"continue"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"seq"</span>:<span class="hljs-number">117</span>,
    <span class="hljs-string">"type"</span>:<span class="hljs-string">"request"</span>,
    <span class="hljs-string">"command"</span>:<span class="hljs-string">"evaluate"</span>,
    <span class="hljs-string">"arguments"</span>:&#123;
        <span class="hljs-string">"expression"</span>:<span class="hljs-string">"1+2"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>感兴趣的同学可以去 <a href="https://github.com/buggerjs/bugger-v8-client/blob/master/PROTOCOL.md" target="_blank" rel="nofollow noopener noreferrer">v8 debug protocol 的文档</a>中去查看全部的协议。</p>
<p>基于这些协议就可以控制 v8 的 debugger 了，所有的能够实现 debugger 的都是对接了这个协议，比如 chrome devtools、vscode debugger 还有其他各种 ide 的 debugger。</p>
<h3 data-id="heading-11">nodejs 代码的调试</h3>
<p>nodejs 可以通过添加 --inspect 的 option 来做调试（也可以是 --inspect-brk，这个会在首行就断住）。</p>
<p>它会起一个 debugger 的 websocket 服务端，我们可以用 vscode 来调试 nodejs 代码，也可以用 chrome devtools 来调试（见 <a href="https://nodejs.org/en/docs/guides/debugging-getting-started/" target="_blank" rel="nofollow noopener noreferrer">nodejs debugger 文档</a>）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">➜ node --inspect test.js
Debugger listening on ws:<span class="hljs-comment">//127.0.0.1:9229/db309268-623a-4abe-b19a-c4407ed8998d</span>
For help see https:<span class="hljs-comment">//nodejs.org/en/docs/inspector</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理就是实现了 v8 debug protocol。</p>
<p>我们如果自己做调试工具、做 ide，那就要对接这个协议。</p>
<h3 data-id="heading-12">debugger adaptor protocol</h3>
<p>上面介绍的 v8 debug protocol 可以实现 js 代码的调试，那么 python、c# 等肯定也有自己的调试协议，如果要实现 ide，都要对接一遍太过麻烦。所以后来出现了一个中间层协议，DAP（debugger adaptor protocol）。</p>
<p>debugger adaptor protocol， 顾名思义，就是适配的，一端适配各种 debugger 协议，一端提供给客户端统一的协议。这是适配器模式的一个很好的应用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/785f94da9bdb415880f896172d6c8acc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">总结</h2>
<p>本文我们学习了 debugger 的实现原理和暴露出的调试协议。</p>
<p>首先我们了解了代码两种运行方式：直接执行和解释执行，然后分析了下为什么需要 debugger。</p>
<p>之后探索了直接执行的代码通过 INT 3 的中断的方式来实现 debugger 和解释型语言自己实现的 debugger。</p>
<p>然后 debugger 的能力会通过 socket 暴露给客户端，提供调试协议，比如 v8
debug protocol，各种客户端包括 chrome devtools、ide 等都实现了这个协议。</p>
<p>但是每种语言都要实现一次的话太过麻烦，所以后来出现了一个适配层协议，屏蔽了不同协议的区别，提供统一的协议接口给客户端用。</p>
<p>希望这篇文章能够让你理解 debugger 的原理，如果要实现调试工具也知道怎么该怎么去对接协议。能够知道 chrome devtools、vscode 为啥都可以调试 nodejs 代码。</p></div>  
</div>
            