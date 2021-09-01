
---
title: '12张图带你看看 V8 是如何执行和回收JavaScript代码的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7680519fd0e43c4bb2ee3ffff19d358~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 17:03:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7680519fd0e43c4bb2ee3ffff19d358~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>又到了新的学期（虽然毕业两个月了哈哈哈），九月冲！</p>
<p>今天就来一起看看 V8 引擎执行JavaScript的过程和垃圾回收的机制。</p>
<h2 data-id="heading-0">一、V8 执行代码过程</h2>
<p>在说V8的执行JavaScript代码的机制之前，我们先来看看编译型和解释型语言的区别。</p>
<h3 data-id="heading-1">1. 编译型语言和解释型语言</h3>
<p>我们知道，机器是不能直接理解代码的。所以，在执行程序之前，需要将代码翻译成机器能读懂的机器语言。按语言的执行流程，可以把计算机语言划分为编译型语言和解释型语言：</p>
<ul>
<li><strong>编译型语言</strong>：在代码运行前编译器直接将对应的代码转换成机器码，运行时不需要再重新翻译，直接可以使用编译后的结果；</li>
<li><strong>解释型语言</strong>：需要将代码转换成机器码，和编译型语言的区别在于运行时需要转换。解释型语言的执行速度要慢于编译型语言，因为解释型语言每次执行都需要把源码转换一次才能执行。</li>
</ul>
<p>Java 和 C++ 等语言都是编译型语言，而 JavaScript 是解释性语言，它整体的执行速度会略慢于编译型的语言。V8 是众多浏览器的 JS 引擎中性能表现最好的一个，并且它是 Chrome 的内核，Node.js 也是基于 V8 引擎研发的。</p>
<p>编译型语言和解释器语言代码执行的具体流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7680519fd0e43c4bb2ee3ffff19d358~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图.png" loading="lazy" referrerpolicy="no-referrer">
两者的执行流程如下：</p>
<ul>
<li>在编译型语言的编译过程中，编译器首先会依次对源代码进行词法分析、语法分析，生成抽象语法树（AST），然后优化代码，最后再生成处理器能够理解的机器码。如果编译成功，将会生成一个可执行的文件。但如果编译过程发生了语法或者其他的错误，那么编译器就会抛出异常，最后的二进制文件也不会生成成功。</li>
<li>在解释型语言的解释过程中，同样解释器也会对源代码进行词法分析、语法分析，并生成抽象语法树（AST），不过它会再基于抽象语法树生成字节码，最后再根据字节码来执行程序、输出结果。</li>
</ul>
<h3 data-id="heading-2">2. V8 执行代码过程</h3>
<p>V8 在执行过程用到了<strong>解释器和编译器。</strong> 其执行过程如下：</p>
<ol>
<li>Parse 阶段：V8 引擎将 JS 代码转换成 AST（抽象语法树）；</li>
<li>Ignition 阶段：解释器将 AST 转换为字节码，解析执行字节码也会为下一个阶段优化编译提供需要的信息；</li>
<li>TurboFan 阶段：编译器利用上个阶段收集的信息，将字节码优化为可以执行的机器码；</li>
<li>Orinoco 阶段：垃圾回收阶段，将程序中不再使用的内存空间进行回收。</li>
</ol>
<p>这里前三个步骤是JavaScript的执行过程，最后一步是垃圾回收的过程。下面就先来看看V8 执行 JavaScript的过程。</p>
<h4 data-id="heading-3">（1）生成抽象语法树</h4>
<p>这个过程就是将源代码转换为<strong>抽象语法树（AST）</strong>，并生成<strong>执行上下文</strong>，执行上下文就是代码在执行过程中的环境信息。</p>
<p>将 JS 代码解析成 AST主要分为两个阶段：</p>
<ol>
<li><strong>词法分析</strong>：这个阶段会将源代码拆成最小的、不可再分的词法单元，称为 token。比如代码 var a = 1；通常会被分解成 var 、a、=、1、; 这五个词法单元。代码中的空格在 JavaScript 中是直接忽略的，简单来说就是<strong>将 JavaScript 代码解析成一个个令牌（Token）</strong>。</li>
<li><strong>语法分析</strong>：这个过程是将上一步生成的 token 数据，根据语法规则转为 AST。如果源码符合语法规则，这一步就会顺利完成。如果源码存在语法错误，这一步就会终止，并抛出一个语法错误，简单来说就是<strong>将令牌组装成一棵抽象的语法树（AST）</strong>。</li>
</ol>
<p>通过词法分析会对代码逐个字符进行解析，生成类似下面结构的令牌（Token），这些令牌类型各不相同，有关键字、标识符、符号、数字等。代码 var a = 1；会转化为下面这样的令牌：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">Keyword(<span class="hljs-keyword">var</span>)
Identifier(name)
Punctuator(=)
<span class="hljs-built_in">Number</span>(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>语法分析阶段会用令牌生成一棵抽象语法树，生成树的过程中会去除不必要的符号令牌，然后按照语法规则来生成。下面来看两段代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 第一段代码</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-comment">// 第二段代码</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span> (<span class="hljs-params">a,b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将这两段代码分别转换成 AST 抽象语法树之后返回的 JSON 如下：</p>
<ul>
<li>第一段代码，编译后的结果：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"type"</span>: <span class="hljs-string">"Program"</span>,
  <span class="hljs-string">"start"</span>: <span class="hljs-number">0</span>,
  <span class="hljs-string">"end"</span>: <span class="hljs-number">10</span>,
  <span class="hljs-string">"body"</span>: [
    &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-string">"VariableDeclaration"</span>,
      <span class="hljs-string">"start"</span>: <span class="hljs-number">0</span>,
      <span class="hljs-string">"end"</span>: <span class="hljs-number">10</span>,
      <span class="hljs-string">"declarations"</span>: [
        &#123;
          <span class="hljs-string">"type"</span>: <span class="hljs-string">"VariableDeclarator"</span>,
          <span class="hljs-string">"start"</span>: <span class="hljs-number">4</span>,
          <span class="hljs-string">"end"</span>: <span class="hljs-number">9</span>,
          <span class="hljs-string">"id"</span>: &#123;
            <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,
            <span class="hljs-string">"start"</span>: <span class="hljs-number">4</span>,
            <span class="hljs-string">"end"</span>: <span class="hljs-number">5</span>,
            <span class="hljs-string">"name"</span>: <span class="hljs-string">"a"</span>
          &#125;,
          <span class="hljs-string">"init"</span>: &#123;
            <span class="hljs-string">"type"</span>: <span class="hljs-string">"Literal"</span>,
            <span class="hljs-string">"start"</span>: <span class="hljs-number">8</span>,
            <span class="hljs-string">"end"</span>: <span class="hljs-number">9</span>,
            <span class="hljs-string">"value"</span>: <span class="hljs-number">1</span>,
            <span class="hljs-string">"raw"</span>: <span class="hljs-string">"1"</span>
          &#125;
        &#125;
      ],
      <span class="hljs-string">"kind"</span>: <span class="hljs-string">"var"</span>
    &#125;
  ],
  <span class="hljs-string">"sourceType"</span>: <span class="hljs-string">"module"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的样子大致如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d54015e4f3e4227893b23f1c0c750cf~tplv-k3u1fbpfcp-watermark.image" alt="V8-第 4 页.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>第二段代码，编译出来的结果：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"type"</span>: <span class="hljs-string">"Program"</span>,
  <span class="hljs-string">"start"</span>: <span class="hljs-number">0</span>,
  <span class="hljs-string">"end"</span>: <span class="hljs-number">38</span>,
  <span class="hljs-string">"body"</span>: [
    &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-string">"FunctionDeclaration"</span>,
      <span class="hljs-string">"start"</span>: <span class="hljs-number">0</span>,
      <span class="hljs-string">"end"</span>: <span class="hljs-number">38</span>,
      <span class="hljs-string">"id"</span>: &#123;
        <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,
        <span class="hljs-string">"start"</span>: <span class="hljs-number">9</span>,
        <span class="hljs-string">"end"</span>: <span class="hljs-number">12</span>,
        <span class="hljs-string">"name"</span>: <span class="hljs-string">"sum"</span>
      &#125;,
      <span class="hljs-string">"expression"</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-string">"generator"</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-string">"async"</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-string">"params"</span>: [
        &#123;
          <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,
          <span class="hljs-string">"start"</span>: <span class="hljs-number">14</span>,
          <span class="hljs-string">"end"</span>: <span class="hljs-number">15</span>,
          <span class="hljs-string">"name"</span>: <span class="hljs-string">"a"</span>
        &#125;,
        &#123;
          <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,
          <span class="hljs-string">"start"</span>: <span class="hljs-number">16</span>,
          <span class="hljs-string">"end"</span>: <span class="hljs-number">17</span>,
          <span class="hljs-string">"name"</span>: <span class="hljs-string">"b"</span>
        &#125;
      ],
      <span class="hljs-string">"body"</span>: &#123;
        <span class="hljs-string">"type"</span>: <span class="hljs-string">"BlockStatement"</span>,
        <span class="hljs-string">"start"</span>: <span class="hljs-number">19</span>,
        <span class="hljs-string">"end"</span>: <span class="hljs-number">38</span>,
        <span class="hljs-string">"body"</span>: [
          &#123;
            <span class="hljs-string">"type"</span>: <span class="hljs-string">"ReturnStatement"</span>,
            <span class="hljs-string">"start"</span>: <span class="hljs-number">23</span>,
            <span class="hljs-string">"end"</span>: <span class="hljs-number">36</span>,
            <span class="hljs-string">"argument"</span>: &#123;
              <span class="hljs-string">"type"</span>: <span class="hljs-string">"BinaryExpression"</span>,
              <span class="hljs-string">"start"</span>: <span class="hljs-number">30</span>,
              <span class="hljs-string">"end"</span>: <span class="hljs-number">35</span>,
              <span class="hljs-string">"left"</span>: &#123;
                <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,
                <span class="hljs-string">"start"</span>: <span class="hljs-number">30</span>,
                <span class="hljs-string">"end"</span>: <span class="hljs-number">31</span>,
                <span class="hljs-string">"name"</span>: <span class="hljs-string">"a"</span>
              &#125;,
              <span class="hljs-string">"operator"</span>: <span class="hljs-string">"+"</span>,
              <span class="hljs-string">"right"</span>: &#123;
                <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,
                <span class="hljs-string">"start"</span>: <span class="hljs-number">34</span>,
                <span class="hljs-string">"end"</span>: <span class="hljs-number">35</span>,
                <span class="hljs-string">"name"</span>: <span class="hljs-string">"b"</span>
              &#125;
            &#125;
          &#125;
        ]
      &#125;
    &#125;
  ],
  <span class="hljs-string">"sourceType"</span>: <span class="hljs-string">"module"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的样子大致如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f00d5ce491434c8f8528ce6c0a3bde46~tplv-k3u1fbpfcp-watermark.image" alt="V8-第 3 页.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，AST 只是源代码语法结构的一种抽象的表示形式，计算机也不会去直接去识别 JS 代码，转换成抽象语法树也只是识别这一过程中的第一步。AST 的结构和代码的结构非常相似，其实也可以把 AST 看成代码的结构化的表示，编译器或者解释器后续的工作都需要依赖于 AST。</p>
<p><strong>AST的应用场景：</strong></p>
<p>AST 是一种很重要的数据结构，很多地方用到了AST。比如在 Babel 中，Babel 是一个代码转码器，可以将 ES6 代码转为 ES5 代码。Babel 的工作原理就是先将 ES6 源码转换为 AST，然后再将 ES6 语法的 AST 转换为 ES5 语法的 AST，最后利用 ES5 的 AST 生成 JavaScript 源代码。</p>
<p>除了 Babel 之外，ESLint 也使用到了 AST。ESLint 是一个用来检查 JavaScript 编写规范的插件，其检测流程也是需要将源码转换为 AST，然后再利用 AST 来检查代码规范化的问题。</p>
<p>除了上述应用场景，AST 的应用场景还有很多：</p>
<ul>
<li>JS 反编译，语法解析；</li>
<li>代码高亮；</li>
<li>关键字匹配；</li>
<li>代码压缩。</li>
</ul>
<h4 data-id="heading-4">（2）生成字节码</h4>
<p>有了 抽象语法树 AST 和执行上下文后，就轮到解释器就登场了，它会根据 AST 生成字节码，并解释执行字节码。</p>
<p>在 V8 的早期版本中，是通过 AST 直接转换成机器码的。将 AST 直接转换为机器码会存在一些问题：</p>
<ul>
<li>直接转换会带来内存占用过大的问题，因为将抽象语法树全部生成了机器码，而机器码相比字节码占用的内存多了很多；</li>
<li>某些 JavaScript 使用场景使用解释器更为合适，解析成字节码，有些代码没必要生成机器码，进而尽可能减少了占用内存过大的问题。</li>
</ul>
<p>为了解决内存占用问题，就在 V8 引擎中引入了字节码。那什么是字节码呢？为什么引入字节码就能解决内存占用问题呢？</p>
<p><strong>字节码就是介于 AST 和机器码之间的一种代码。</strong> 需要将其转换成机器码后才能执行，字节码是对机器码的一个抽象描述，相对于机器码而言，它的代码量更小，从而可以减少内存消耗。解释器除了可以快速生成没有优化的字节码外，还可以执行部分字节码。</p>
<h4 data-id="heading-5">（3）生成机器码</h4>
<p>生成字节码之后，就进入执行阶段了，实际上，这一步就是<strong>将字节码生成机器码</strong>。
​</p>
<p>一般情况下，如果字节码是第一次执行，那么解释器就会逐条解释执行。在执行字节码过程中，如果发现有<strong>热代码</strong>（重复执行的代码，运行次数超过某个阈值就被标记为热代码），那么后台的编译器就会把该段热点的字节码编译为高效的机器码，然后当再次执行这段被优化的代码时，只需要执行编译后的机器码即可，这样提升了代码的执行效率。</p>
<p>字节码配合解释器和编译器的技术就是 <strong>即时编译（JIT）</strong>。在 V8 中就是指解释器在解释执行字节码的同时，收集代码信息，当它发现某一部分代码变热了之后，编译器便闪亮登场，把热点的字节码转换为机器码，并把转换后的机器码保存起来，以备下次使用。</p>
<p>因为 V8 引擎是多线程的，编译器的编译线程和生成字节码不会在同一个线程上，这样可以和解释器相互配合着使用，不受另一方的影响。下面是JIT技术的工作机制：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df45f4316a2f440c90b532719d1ca5a6~tplv-k3u1fbpfcp-watermark.image" alt="V8-机器码.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解释器在得到 AST 之后，会按需进行解释和执行。也就是说如果某个函数没有被调用，则不会去解释执行它。在这个过程中解释器会将一些重复可优化的操作收集起来生成分析数据，然后将生成的字节码和分析数据传给编译器，编译器会依据分析数据来生成高度优化的机器码。
​</p>
<p>优化后的机器码的作用和缓存很类似，当解释器再次遇到相同的内容时，就可以直接执行优化后的机器码。当然优化后的代码有时可能会无法运行（比如函数参数类型改变），那么会再次反优化为字节码交给解释器。
​</p>
<p>整个过程如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6df0e400bc574cd9a072af7386d4c39c~tplv-k3u1fbpfcp-watermark.image" alt="V8-全流程.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">3. 执行过程优化</h3>
<p>如果JavaScript代码在执行前都要完全经过解析才能执行，那可能会面临以下问题：</p>
<ul>
<li>代码执行时间变长：一次性解析所有代码会增加代码的运行时间。</li>
<li>消耗更多内存：解析完的 AST 以及根据 AST 编译后的字节码都会存放在内存中，会占用更多内存空间。</li>
<li>占用磁盘空间：编译后的代码会缓存在磁盘上，占用磁盘空间。</li>
</ul>
<p>​</p>
<p>所以，V8 引擎使用了<strong>延迟解析</strong>：在解析过程中，对于不是立即执行的函数，只进行预解析；只有当函数调用时，才对函数进行全量解析。
​</p>
<p>进行预解析时，只验证函数语法是否有效、解析函数声明、确定函数作用域，不生成 AST，而实现预解析的，就是 Pre-Parser 解析器。
​</p>
<p>以下面代码为例：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="hljs-keyword">const</span> a = <span class="hljs-number">666</span>;
<span class="hljs-keyword">const</span> c = <span class="hljs-number">996</span>;
foo(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>V8 解析器是从上往下解析代码的，当解析器遇到函数声明 foo 时，发现它不是立即执行，所以会用 Pre-Parser 解析器对其预解析，过程中只会解析函数声明，不会解析函数内部代码，不会为函数内部代码生成 AST。
​</p>
<p>之后解释器会把 AST 编译为字节码并执行，解释器会按照自上而下的顺序执行代码，先执行 const a = 666;  和 const c = 996; ，然后执行函数调用 sum(1, 1) ，这时 Parser 解析器才会继续解析函数内的代码、生成 AST，再交给解释器编译执行。</p>
<h2 data-id="heading-7">二、V8 垃圾回收机制</h2>
<h3 data-id="heading-8">1. JavaScript 内存管理机制</h3>
<p>计算机程序语言都运行在对应的代码引擎上，使用内存过程可以分为以下三个步骤：</p>
<ol>
<li>分配所需要的系统内存空间；</li>
<li>使用分配到的内存进行读或写等操作；</li>
<li>不需要使用内存时，将其空间释放或者归还。</li>
</ol>
<p>在 JavaScript 中，当创建变量时，系统会自动给对象分配对应的内存，来看下面的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a = <span class="hljs-number">123</span>; <span class="hljs-comment">// 给数值变量分配栈内存</span>
<span class="hljs-keyword">var</span> etf = <span class="hljs-string">"ARK"</span>; <span class="hljs-comment">// 给字符串分配栈内存</span>
<span class="hljs-comment">// 给对象及其包含的值分配堆内存</span>
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'tom'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">13</span>
&#125;; 
<span class="hljs-comment">// 给数组及其包含的值分配内存</span>
<span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">"str"</span>]; 
<span class="hljs-comment">// 给函数分配内存</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">a, b</span>)</span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JavaScript 中的数据分为两类：</p>
<ul>
<li><strong>基本类型</strong>：这些类型在内存中会占据固定的内存空间，它们的值都保存在栈空间中，直接可以通过值来访问这些；</li>
<li><strong>引用类型</strong>：由于引用类型值大小不固定，栈内存中存放地址指向堆内存中的对象，是通过引用来访问的。</li>
</ul>
<p>栈内存中的基本类型，可以通过操作系统直接处理；而堆内存中的引用类型，正是由于可以经常变化，大小不固定，因此需要 JavaScript 的引擎通过垃圾回收机制来处理。所谓的垃圾回收是指：<strong>JavaScript代码运行时，需要分配内存空间来储存变量和值。当变量不在参与运行时，就需要系统收回被占用的内存空间。</strong> Javascript 具有自动垃圾回收机制，会定期对那些不再使用的变量、对象所占用的内存进行释放，原理就是找到不再使用的变量，然后释放掉其占用的内存。</p>
<p>JavaScript中存在两种变量：局部变量和全局变量。全局变量的生命周期会持续要页面卸载；而局部变量声明在函数中，它的生命周期从函数执行开始，直到函数执行结束，在这个过程中，局部变量会在堆或栈中存储它们的值，当函数执行结束后，这些局部变量不再被使用，它们所占有的空间就会被释放。不过，当局部变量被外部函数使用时，其中一种情况就是闭包，在函数执行结束后，函数外部的变量依然指向函数内部的局部变量，此时局部变量依然在被使用，所以不会回收。</p>
<h3 data-id="heading-9">2. V8 垃圾回收过程</h3>
<p>先来看看 Chrome浏览器的垃圾回收过程：</p>
<p><strong>（1）通过 GC Root 标记空间中活动对象和⾮活动对象。</strong></p>
<p>⽬前 V8 采⽤的<strong>可访问性</strong>算法来判断堆中的对象是否是活动对象。这个算法是将⼀些 GC Root 作为初始存活的对象的集合，从 GC Roots 对象出发，遍历 GC Root 中所有对象：</p>
<ul>
<li>通过 GC Root 遍历到的对象是<strong>可访问的</strong>​，必须保证这些对象应该在内存中保留，可访问的对象称为<strong>活动对象</strong>；</li>
<li>通过 GC Roots 没有遍历到的对象是<strong>不可访问的</strong>，这些不可访问的对象就可能被回收，不可访问的对象称为<strong>⾮活动对象</strong>。</li>
</ul>
<p><strong>（2）回收⾮活动对象所占据的内存。</strong></p>
<p>其实就是在所有的标记完成之后，统⼀清理内存中所有被标记为可回收的对象。</p>
<p><strong>（3）内存整理。</strong></p>
<p>⼀般来说，频繁回收对象后，内存中就会存在⼤量不连续空间，这些不连续的内存空间称为内存碎⽚。当内存中出现了⼤量的内存碎⽚之后，如果需要分配较⼤的连续内存时，就有可能出现内存不⾜的情况，所以最后⼀步需要整理这些内存碎⽚。这步其实是可选的，因为有的垃圾回收器不会产⽣内存碎⽚。</p>
<p>以上就是⼤致的垃圾回收流程。⽬前 V8 使用了两个垃圾回收器：<strong>主垃圾回收器</strong>和<strong>副垃圾回收器</strong>。下面就来看看 V8 是如何实现垃圾回收的。</p>
<p>在 V8 中，<strong>会把堆分为新生代和老生代两个区域</strong>，<strong>新生代中存放的是生存时间短的对象，老生代中存放生存时间久的对象：</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eb239e1efb348f0b32b6d884bdf991e~tplv-k3u1fbpfcp-watermark.image" alt="V8-新老生代.png" loading="lazy" referrerpolicy="no-referrer">
新⽣代通常只⽀持 1～8M 的容量，⽽⽼⽣代⽀持的容量就⼤很多。对于这两块区域，V8分别使⽤两个不同的垃圾回收器，以便更⾼效地实施垃圾回收：</p>
<ul>
<li>副垃圾回收器：负责新⽣代的垃圾回收。</li>
<li>主垃圾回收器：负责⽼⽣代的垃圾回收。</li>
</ul>
<h4 data-id="heading-10">（1）副垃圾回收器（新生代）</h4>
<p>副垃圾回收器主要负责新⽣代的垃圾回收。大多数的对象最开始都会被分配在新生代，该存储空间相对较小，分为两个空间：from 空间（对象区）和 to 空间（空闲区）。</p>
<p>新加⼊的对象都会存放到对象区域，当对象区域快被写满时，就需要执⾏⼀次垃圾清理操作：首先要对对象区域中的垃圾做标记，标记完成之后，就进入垃圾清理阶段。副垃圾回收器会把这些存活的对象复制到空闲区域中，同时它还会把这些对象有序地排列起来。这个复制过程就相当于完成了内存整理操作，复制后空闲区域就没有内存碎片了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c11326543b554917aa40f3e537991ef6~tplv-k3u1fbpfcp-watermark.image" alt="V8-第 7 页.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完成复制后，对象区域与空闲区域进行角色翻转，也就是原来的对象区域变成空闲区域，原来的空闲区域变成了对象区域，这种算法称之为 Scavenge 算法，这样就完成了垃圾对象的回收操作。同时，这种角色翻转的操作还能让新生代中的这两块区域无限重复使用下去：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b64901b23283407faa3fbc743edb3b66~tplv-k3u1fbpfcp-watermark.image" alt="V8-第 7 页.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过，副垃圾回收器每次执⾏清理操作时，都需要将存活的对象从对象区域复制到空闲区域，复制操作需要时间成本，如果新⽣区空间设置得太⼤了，那么每次清理的时间就会过久，所以<strong>为了执⾏效率，⼀般新⽣区的空间会被设置得⽐较⼩。</strong> 也正是因为新⽣区的空间不⼤，所以很容易被存活的对象装满整个区域，副垃圾回收器⼀旦监控对象装满了，便执⾏垃圾回收。同时，副垃圾回收器还会采⽤对象晋升策略，也就是移动那些经过两次垃圾回收依然还存活的对象到⽼⽣代中。</p>
<h4 data-id="heading-11">（2）主垃圾回收器（老生代）</h4>
<p>主垃圾回收器主要负责⽼⽣代中的垃圾回收。除了新⽣代中晋升的对象，⼀些⼤的对象会直接被分配到⽼⽣代⾥。因此，⽼⽣代中的对象有两个特点：</p>
<ul>
<li>对象占⽤空间⼤；</li>
<li>对象存活时间⻓。</li>
</ul>
<p>由于⽼⽣代的对象⽐较⼤，若要在⽼⽣代中使⽤ Scavenge 算法进⾏垃圾回收，复制这些⼤的对象将会花费较多时间，从⽽导致回收执⾏效率不⾼，同时还会浪费空间。所以，主垃圾回收器采⽤<strong>标记清除</strong>的算法进⾏垃圾回收。</p>
<p>这种方式分为<strong>标记</strong>和<strong>清除</strong>两个阶段：</p>
<ol>
<li><strong>标记阶段：</strong> 从一组根元素开始，递归遍历这组根元素，在这个遍历过程中，能到达的元素称为活动对象，没有到达的元素就可以判断为垃圾数据。</li>
<li><strong>清除阶段：</strong> 主垃圾回收器会直接将标记为垃圾的数据清理掉。</li>
</ol>
<p>这两个阶段如图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ef5e9bbcc094de1be9e4d932a742549~tplv-k3u1fbpfcp-watermark.image" alt="V8-第 7 页.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对垃圾数据进⾏标记，然后清除，这就是标记清除算法，不过对⼀块内存多次执⾏标记清除算法后，会产⽣⼤量不连续的内存碎⽚。⽽碎⽚过多会导致⼤对象⽆法分配到⾜够的连续内存，于是⼜引⼊了另外⼀种算法——标记整理。</p>
<p>这个算法的标记过程仍然与标记清除算法⾥的是⼀样的，先标记可回收对象，但后续步骤不是直接对可回收对象进⾏清理，⽽是让所有存活的对象都向⼀端移动，然后直接清理掉这⼀端之外的内存：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01abc7919b78482089055ba3dfef38ef~tplv-k3u1fbpfcp-watermark.image" alt="V8-第 8 页.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">（3）全停顿</h4>
<p>我们知道，JavaScript 是单行线语言，运行在主线程上。一旦执行垃圾回收算法，都需要将正在执行的 JavaScript 脚本暂停下来，待垃圾回收完毕后再恢复脚本执行。这种行为叫做<strong>全停顿。</strong></p>
<p>主垃圾回收器执行一次完整的垃圾回收流程如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/829ce8749c654daa935a037f3fb704c7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 V8 新生代的垃圾回收中，因其空间较小，且存活对象较少，所以全停顿的影响不大。但老生代中，如果在执行垃圾回收的过程中，占用主线程时间过久，主线程是不能做其他事情的，需要等待执行完垃圾回收操作才能做其他事情，这将就可能会造成页面的卡顿现象。</p>
<p>为了降低老生代的垃圾回收而造成的卡顿，V8 将标记过程分为一个个的子标记过程，同时让垃圾回收标记和 JavaScript 应用逻辑交替进行，直到标记阶段完成，这个算法称为<strong>增量标记</strong>算法。如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e6906238d314d5eb0f8be2b45558cf1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用增量标记算法可以把一个完整的垃圾回收任务拆分为很多小的任务，这些小的任务执行时间比较短，可以穿插在其他的 JavaScript 任务中间执行，这样当执行代码时，就不会让用户因为垃圾回收任务而感受到页面的卡顿了。</p>
<h3 data-id="heading-13">3. 减少垃圾回收</h3>
<p>虽然浏览器可以进行垃圾自动回收，但是当代码比较复杂时，垃圾回收所带来的代价较大，所以应该尽量减少垃圾回收：</p>
<ul>
<li><strong>对数组进行优化：</strong> 在清空一个数组时，最简单的方法就是给其赋值为[ ]，但是与此同时会创建一个新的空对象，可以将数组的长度设置为0，以此来达到清空数组的目的。</li>
<li><strong>对object进行优化：</strong> 对象尽量复用，对于不再使用的对象，就将其设置为null，尽快被回收。</li>
<li><strong>对函数进行优化：</strong> 在循环中的函数表达式，如果可以复用，尽量放在函数的外面。</li>
</ul></div>  
</div>
            