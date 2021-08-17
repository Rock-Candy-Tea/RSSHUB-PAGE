
---
title: '一文带你走进 Rust 和 WebAssembly 的世界'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b9542f971924c8385faf070e36345e3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 04:23:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b9542f971924c8385faf070e36345e3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Why Rust</h1>
<p>在进行正式的分享之前，先来说一说为什么，要学习 Rust 这一门在广义上归属于后端的语言，以及它能带给我们什么，未来有什么前景</p>
<ol>
<li>与JavaScript部分相似的语法，就入门来说，应该不难（大概）</li>
<li>安全高效的新兴语言，通过Rust你可以对计算机的底层是如何操作的有一个基本的认识</li>
<li>依托于WebAssembly，Rust可以运行在浏览器上，在某些场景（如视频直播或需要大量运算）具有卓越的性能，例如我们经常用的figma就有使用到WebAssembly</li>
<li>掌握至少一门后端语言有助于后续的提升，Node.js也很对，但是对于计算机底层相对于cpp和rust较黑盒</li>
<li>Rust的设计哲学值得一看</li>
</ol>
<h1 data-id="heading-1">Rust</h1>
<p>Rust 语言是一种高效、可靠的通用高级语言。其高效不仅限于开发效率，它的执行效率也是令人称赞的，是一种少有的兼顾开发效率和执行效率的语言。
Rust 是一种 <strong>预编译静态类型</strong>（<em>ahead-of-time compiled</em>）语言，这意味着你可以编译程序，并将可执行文件送给其他人，他们甚至不需要安装 Rust 就可以运行。如果你给他人一个 <em>.rb</em>、<em>.py</em> 或 <em>.js</em> 文件，他们需要先分别安装 Ruby，Python，JavaScript 实现（运行时环境，VM）
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fkaisery.github.io%2Ftrpl-zh-cn%2Fch01-01-installation.html" target="_blank" rel="nofollow noopener noreferrer" title="https://kaisery.github.io/trpl-zh-cn/ch01-01-installation.html" ref="nofollow noopener noreferrer">中文学习资源</a></p>
<hr>
<p>以上摘抄自官方文档等学习资源
下面不逐个介绍Rust的语法与编译方式，主要介绍一些我认为的Rust语言的一些有意思的特点与设计思想</p>
<ol>
<li>Rust中变量默认是不可变的（immutable）变量不可变可以说是一种规范，可以帮助我们更加直观的追寻数据的变化状态。例如使用react的PureComponent 或者 memo只会对行新旧数据的浅层比对，由于 JS 引用赋值的原因，这种方式仅仅适用于无状态组件或者状态数据非常简单的组件，对于大量的应用型组件，它是无能为力的，所以在编写的时候会考虑使用immutable +memo 浅层比对。</li>
</ol>
<p>举个最简单的例子</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 可变，arr新增 </span>
arr.push(item)  
<span class="hljs-comment">// 不可变 </span>
arr = [...arr,item] 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>完善的类型系统（和Typescript极其相似），但是在某些方面比Typescript更加的细，例如整形可以分为无符号，有符号的8-bit，16-bit，32-bit，64-bit，128-bit。</li>
</ol>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-comment">// 无符号的32位整形 </span>
<span class="hljs-keyword">let</span> guess: <span class="hljs-built_in">u32</span> = <span class="hljs-string">"42"</span>.parse().expect(<span class="hljs-string">"Not a number!"</span>); 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>语言的集大成者，既有Javascript的灵活，又有C/C++的编译加持</li>
</ol>
<p>举一个体现其灵活的例子</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">let</span> x = <span class="hljs-number">5</span>; 
<span class="hljs-keyword">let</span> y = &#123;    
    <span class="hljs-keyword">let</span> x = <span class="hljs-number">3</span>;    
    x + <span class="hljs-number">1</span> 
&#125;; 
<span class="hljs-built_in">println!</span>(<span class="hljs-string">"The value of y is: &#123;&#125;"</span>, y); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的例子中Rust使用**；**来判断该句子是表达式，还是一个语句</p>
<ol start="4">
<li>严谨的，灵活的控制流</li>
</ol>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-comment">// 会报错 </span>
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">main</span></span>() &#123;     
    <span class="hljs-keyword">let</span> number = <span class="hljs-number">3</span>;  
    
    <span class="hljs-keyword">if</span> number &#123;         
        <span class="hljs-built_in">println!</span>(<span class="hljs-string">"number was three"</span>);     
    &#125; 
&#125;  

<span class="hljs-comment">// 形如以下的赋值语句是完全有效的 </span>
<span class="hljs-keyword">let</span> condition = <span class="hljs-literal">true</span>;     
<span class="hljs-keyword">let</span> number = <span class="hljs-keyword">if</span> condition &#123;         
    <span class="hljs-number">5</span>     
&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-number">6</span>     
&#125;; 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>独特的内存管理方式，区别于垃圾回收机制（javascript）和亲自分配和释放内存（C/C++),Rust采用了另外一种管理操作系统内存的方式：通过所有权系统管理内存，编译器在编译时会根据一系列的规则进行检查。在运行时，所有权系统的任何功能都不会减慢程序。</li>
</ol>
<p>如果内存的操作分为以下两部分</p>
<ul>
<li>必须在运行时向操作系统请求内存。</li>
<li>需要一个当我们处理完 String 时将内存返回给操作系统的方法。</li>
</ul>
<p>第一步大同小异，而对于第二步的处理就是百花齐放了，对于Rust而言</p>
<blockquote>
<ol>
<li>Rust 中的每一个值都有一个被称为其 <strong>所有者</strong>（<em>owner</em>）的变量。</li>
<li>值在任一时刻有且只有一个所有者。</li>
<li>当所有者（变量）离开作用域，这个值将被丢弃。</li>
</ol>
</blockquote>
<p>为了保持运行时的高效，Rust 永远也不会自动创建数据的 “深拷贝”。因此，任何 <strong>自动</strong> 的复制可以被认为对运行时性能影响较小。
对于此，Rust采用了一个规则，禁止把引用堆空间的栈空间变量改变（栈空间上的值类型可以直接引用），因为Rust 不需要在被首次分配空间的变量离开作用域后清理任何东西</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">let</span> s1 = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>); 
<span class="hljs-keyword">let</span> s2 = s1; 
<span class="hljs-built_in">println!</span>(<span class="hljs-string">"&#123;&#125;, world!"</span>, s1); 
<span class="hljs-comment">// 会报错 </span>
<span class="hljs-keyword">let</span> s1 = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>); 
<span class="hljs-keyword">let</span> s2 = s1.clone(); 
<span class="hljs-built_in">println!</span>(<span class="hljs-string">"s1 = &#123;&#125;, s2 = &#123;&#125;"</span>, s1, s2); 
<span class="hljs-comment">// 需要手动克隆 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么当所有者（变量）离开作用域，这个值将被丢弃这句话怎么理解呢？看下面的图，这种操作既不像<strong>浅拷贝</strong>（<em>shallow copy</em>）和 <strong>深拷贝</strong>（<em>deep copy</em>），那么拷贝指针、长度和容量而不拷贝数据可能听起来像浅拷贝。不过因为 Rust 同时使第一个变量无效了，这个操作被称为 <strong>移动</strong>（<em>move</em>），但是注意一点对于值类型，Rust会直接拷贝，而不是进行移动，所以对于值类型(整形等)，有函数调用它之后，仍然可以使用
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b9542f971924c8385faf070e36345e3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">main</span></span>() &#123;
    <span class="hljs-keyword">let</span> s = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>);  <span class="hljs-comment">// s 进入作用域</span>
    takes_ownership(s);             <span class="hljs-comment">// s 的值移动到函数里 ...</span>
                                    <span class="hljs-comment">// ... 所以到这里不再有效</span>
    <span class="hljs-keyword">let</span> x = <span class="hljs-number">5</span>;                      <span class="hljs-comment">// x 进入作用域</span>
    makes_copy(x);                  <span class="hljs-comment">// x 应该移动函数里，</span>
                                    <span class="hljs-comment">// 但 i32 是 Copy 的，所以在后面可继续使用 x</span>
&#125; <span class="hljs-comment">// 这里, x 先移出了作用域，然后是 s。但因为 s 的值已被移走，</span>
  <span class="hljs-comment">// 所以不会有特殊操作</span>
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">takes_ownership</span></span>(some_string: <span class="hljs-built_in">String</span>) &#123; <span class="hljs-comment">// some_string 进入作用域</span>
    <span class="hljs-built_in">println!</span>(<span class="hljs-string">"&#123;&#125;"</span>, some_string);
&#125; <span class="hljs-comment">// 这里，some_string 移出作用域并调用 `drop` 方法。占用的内存被释放</span>
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">makes_copy</span></span>(some_integer: <span class="hljs-built_in">i32</span>) &#123; <span class="hljs-comment">// some_integer 进入作用域</span>
    <span class="hljs-built_in">println!</span>(<span class="hljs-string">"&#123;&#125;"</span>, some_integer);
&#125; <span class="hljs-comment">// 这里，some_integer 移出作用域。不会有特殊操作</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>变量的所有权总是遵循相同的模式：将值赋给另一个变量时移动它。当持有堆中数据值的变量离开作用域时，其值将通过 drop 被清理掉，除非数据被移动为另一个变量所有</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">main</span></span>() &#123;
    <span class="hljs-keyword">let</span> s1 = gives_ownership();         <span class="hljs-comment">// gives_ownership 将返回值</span>
                                        <span class="hljs-comment">// 移给 s1</span>
    <span class="hljs-keyword">let</span> s2 = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>);     <span class="hljs-comment">// s2 进入作用域</span>
    <span class="hljs-keyword">let</span> s3 = takes_and_gives_back(s2);  <span class="hljs-comment">// s2 被移动到</span>
                                        <span class="hljs-comment">// takes_and_gives_back 中,</span>
                                        <span class="hljs-comment">// 它也将返回值移给 s3</span>
&#125; <span class="hljs-comment">// 这里, s3 移出作用域并被丢弃。s2 也移出作用域，但已被移走，</span>
  <span class="hljs-comment">// 所以什么也不会发生。s1 移出作用域并被丢弃</span>
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">gives_ownership</span></span>() -> <span class="hljs-built_in">String</span> &#123;             <span class="hljs-comment">// gives_ownership 将返回值移动给</span>
                                             <span class="hljs-comment">// 调用它的函数</span>
    <span class="hljs-keyword">let</span> some_string = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>); <span class="hljs-comment">// some_string 进入作用域.</span>
    some_string                              <span class="hljs-comment">// 返回 some_string 并移出给调用的函数</span>
&#125;
<span class="hljs-comment">// takes_and_gives_back 将传入字符串并返回该值</span>
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">takes_and_gives_back</span></span>(a_string: <span class="hljs-built_in">String</span>) -> <span class="hljs-built_in">String</span> &#123; <span class="hljs-comment">// a_string 进入作用域</span>
    a_string  <span class="hljs-comment">// 返回 a_string 并移出给调用的函数</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在每一个函数中都获取所有权并接着返回所有权有些啰嗦。如果我们想要函数使用一个值但不获取所有权该怎么办呢？
这里就需要引用和借用（可以理解为c里面的指针）
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4423534030ee4a2394f46bec02e2bafe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">main</span></span>() &#123;
    <span class="hljs-keyword">let</span> s1 = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>);

    <span class="hljs-keyword">let</span> len = calculate_length(&s1);

    <span class="hljs-built_in">println!</span>(<span class="hljs-string">"The length of '&#123;&#125;' is &#123;&#125;."</span>, s1, len);
&#125;
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">calculate_length</span></span>(s: &<span class="hljs-built_in">String</span>) -> <span class="hljs-built_in">usize</span> &#123;
    s.len()
&#125;
<span class="hljs-comment">// 尝试修改，那指定是不行的</span>
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">main</span></span>() &#123;
    <span class="hljs-keyword">let</span> s = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>);

    change(&s);
&#125;
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">change</span></span>(some_string: &<span class="hljs-built_in">String</span>) &#123;
    some_string.push_str(<span class="hljs-string">", world"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数调用了引用类型的引用，在函数体中使用该变量被称之为借用，那么又有一个问题了，你不让我改，我就是想改，诶，就是玩！那么这时候需要引入一个新的概念：可变引用</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">main</span></span>() &#123;
    <span class="hljs-keyword">let</span> <span class="hljs-keyword">mut</span> s = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>);

    change(&<span class="hljs-keyword">mut</span> s);
&#125;
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">change</span></span>(some_string: &<span class="hljs-keyword">mut</span> <span class="hljs-built_in">String</span>) &#123;
    some_string.push_str(<span class="hljs-string">", world"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过可变引用有一个很大的限制：在特定作用域中的特定数据只能有一个可变引用，并且可变引用和不可变引用不应该同时存在（这两是互斥的关系）</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-comment">// 会报错</span>
<span class="hljs-keyword">let</span> <span class="hljs-keyword">mut</span> s = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>);
<span class="hljs-keyword">let</span> r1 = &<span class="hljs-keyword">mut</span> s;
<span class="hljs-keyword">let</span> r2 = &<span class="hljs-keyword">mut</span> s;
<span class="hljs-built_in">println!</span>(<span class="hljs-string">"&#123;&#125;, &#123;&#125;"</span>, r1, r2);
<span class="hljs-comment">// 会报错 too</span>
<span class="hljs-keyword">let</span> <span class="hljs-keyword">mut</span> s = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>);
<span class="hljs-keyword">let</span> r1 = &s; <span class="hljs-comment">// 没问题</span>
<span class="hljs-keyword">let</span> r2 = &s; <span class="hljs-comment">// 没问题</span>
<span class="hljs-keyword">let</span> r3 = &<span class="hljs-keyword">mut</span> s; <span class="hljs-comment">// 大问题</span>
<span class="hljs-built_in">println!</span>(<span class="hljs-string">"&#123;&#125;, &#123;&#125;, and &#123;&#125;"</span>, r1, r2, r3);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个限制的好处是 Rust 可以在编译时就避免数据竞争，可以理解为类似于分布式锁的玩意儿~
数据竞争会导致未定义行为，难以在运行时追踪，并且难以诊断和修复；Rust 避免了这种情况的发生，因为它甚至不会编译存在数据竞争的代码
注意一个引用的作用域从声明的地方开始一直持续到最后一次使用为止。例如，因为最后一次使用不可变引用在声明可变引用之前，所以如下代码是可以编译的：</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">let</span> <span class="hljs-keyword">mut</span> s = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>);
<span class="hljs-keyword">let</span> r1 = &s; <span class="hljs-comment">// 没问题</span>
<span class="hljs-keyword">let</span> r2 = &s; <span class="hljs-comment">// 没问题</span>
<span class="hljs-built_in">println!</span>(<span class="hljs-string">"&#123;&#125; and &#123;&#125;"</span>, r1, r2);<span class="hljs-comment">// 此位置之后 r1 和 r2 不再使用</span>
<span class="hljs-keyword">let</span> r3 = &<span class="hljs-keyword">mut</span> s; <span class="hljs-comment">// 没问题</span>
<span class="hljs-built_in">println!</span>(<span class="hljs-string">"&#123;&#125;"</span>, r3);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是虽然可以编译，这样书写是绕不过静态类型检查的！！！！！！
​</p>
<p>相信大家发现了上面的string类型有些特殊，不是说string是"值类型"吗？为什么他又可以用引用类型来表示呢？
string使用了没有所有权的特殊的引用类型slice，slice 允许你引用集合中一段连续的元素序列，而不用引用整个集合。</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">let</span> s = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>);
<span class="hljs-keyword">let</span> slice = &s[<span class="hljs-number">0</span>..<span class="hljs-number">2</span>];
<span class="hljs-keyword">let</span> slice = &s[..<span class="hljs-number">2</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于"值类型"的string</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">let</span> s = <span class="hljs-string">"Hello, world!"</span>; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​</p>
<p>这里 s 的类型是 &str：它是一个指向二进制程序特定位置的 slice。这也就是为什么字符串字面值是不可变的；&str 是一个不可变引用。
​</p>
<p>悬垂引用
悬垂指针是其指向的内存可能已经被分配给其它持有者。相比之下，在 Rust 中编译器确保引用永远也不会变成悬垂状态
例如以下代码
​</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">main</span></span>() &#123;
    <span class="hljs-keyword">let</span> reference_to_nothing = dangle();
&#125;
<span class="hljs-comment">// wrong</span>
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">dangle</span></span>() -> &<span class="hljs-built_in">String</span> &#123;
    <span class="hljs-keyword">let</span> s = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>);
    &s
&#125;
<span class="hljs-comment">//safe</span>
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">safe</span></span>() -> <span class="hljs-built_in">String</span> &#123;
    <span class="hljs-keyword">let</span> s = <span class="hljs-built_in">String</span>::from(<span class="hljs-string">"hello"</span>);
    s
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 s 是在 dangle 函数内创建的，当 dangle 的代码执行完毕后，s 将被释放。不过我们尝试返回它的引用。这意味着这个引用会指向一个无效的 String，这可不对！Rust 不会允许我们这么做
总结两条规则</p>
<ul>
<li>在任意给定时间，<strong>要么</strong> 只能有一个可变引用，<strong>要么</strong> 只能有多个不可变引用。</li>
<li>引用必须总是有效的。</li>
</ul>
<p>到这里和JavaScript有联系的，并且基础的就分享的差不多了，隐约记得某人说过，如果你对一门语言，了解了其基本的语法，能够编写对应的简单的代码来实现简单的功能，那么你就入门了。
后续的包括以下部分，就先按下不表</p>
<ul>
<li>Cargo : Cargo 是 Rust 的构建系统和包管理器。大多数 Rustacean 们使用 Cargo 来管理他们的 Rust 项目，因为它可以为你处理很多任务，比如构建代码、下载依赖库并编译这些库。类似于JS使用的npm/pnpm/yarn</li>
<li>常见集合：Hashmap（类似于js中的map），Vector（类似于js中的数组），String</li>
<li>错误处理：panic(Throw Error 完全阻塞了程序执行) Result(类似于warning 可以报错但是不影响程序的执行)</li>
<li>.......</li>
</ul>
<p>最后总结一下rust我认为最令人称道的两点</p>
<ol>
<li>丰富而强大的类型系统</li>
<li>可信赖的所有权模型</li>
</ol>
<h1 data-id="heading-2">Rust and WebAssembly</h1>
<p>上面讲了半天rust，他只是我们今天的猪脚之一，那么今天的猪脚还有哪位呢？没错，就是 WebAssembly。
那么WebAssembly到底是什么呢？在说这个之前先康康JavaScript的是怎么进行编译的
这就不得不说到两种编译方式了</p>
<ul>
<li>AOT: Ahead-of-Time compilation</li>
</ul>
<p>必须是强类型语言，编译在执行之前，编译直接生成CPU能够执行的二进制文件，执行时CPU不需要做任何编译操作，直接执行，性能最佳，比如C/C++,Rust</p>
<ul>
<li>JIT: Just-in-Time compilation</li>
</ul>
<p>没有编译环节。执行时根据上下文生成二进制汇编代码，灌入CPU执行。JIT执行时，可以根据代码编译进行优化，代码运行时，不需要每次都翻译成二进制汇编代码，V8就是这样优化JavaScript性能的。</p>
<blockquote>
<p>举个例子，如果使用var来声明一个变量，不使用Typescript等类型系统来限定，一个变量，在多次编译的时候得到的变量的类型可能会不一样，这就导致了每一次JavaScript在执行的时候可能都会被重新编译，这就是类型系统的重要性，不仅能减少bug的发生也可以让我们的代码跑得更快</p>
</blockquote>
<p>详细的说一下这个过程也就是</p>
<ol>
<li>代码文件会被下载下来。</li>
<li>然后进入Parser，Parser会把代码转化成AST（抽象语法树）.</li>
<li>然后根据抽象语法树，Bytecode Compiler字节码编译器会生成引擎能够直接阅读、执行的字节码。</li>
<li>字节码进入翻译器，将字节码一行一行的翻译成效率十分高的Machine Code.</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abf173dfba54437ab976b1edf6843368~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
有同学可能会问：JavaScript不是可以使用Typescript进行静态类型检查吗？为什么不能在编译时编译成可执行的二进制文件呢？盲生，你发现了华点！Typescript说白了也只是给JavaScript打上了补丁，但是JavaScript还是那个JavaScript，说不定在有生之年可以看见JavaScript的整个内核被重写呢？Wasm：那我走？
​</p>
<p>​</p>
<p>回到正题，既然JavaScript的内核变化的几率不大，那我们该如何进行优化呢？
一个思路就是可以直接把 C、C++、Rust等语言编译成 WebAssembly 并能在浏览器中运行，但是有一点需要注意，使用wasm并不是完全舍弃掉了JavaScript，这两者实际上是相辅相成的关系，在实际的应用场景中Rust和JavaScript往往是互相调用包来开发一个web应用。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3986914605146d2ad000ee4e6bf6038~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
WebAssembly是一份字节码标准，以字节码的形式依赖虚拟机在浏览器中运行。
万维网联盟（W3C）2019年12月5日宣布，<a href="https://link.juejin.cn/?target=https://www.w3.org/TR/wasm-core-1/" target="_blank" title="https://link.juejin.cn/?target=https://www.w3.org/TR/wasm-core-1/">WebAssembly 核心规范</a> 现在是一种正式的 Web 标准，它为 Web 发布了一种功能强大的新语言。 WebAssembly 是一种安全、可移植的低级格式，能够在现代处理器（包括 Web 浏览器）中高效执行并紧凑地表示代码。它也被设计为可以与JavaScript共存，允许两者一起工作。
这样说大家可能云里雾里的，那么换个方法
我们每天都在接触各种业务，那大家有没有想过从我们写下JavaScript代码开始，到底发生了什么？
就只看JavaScript大致是这样一个过程</p>
<blockquote>
<p>业务代码 -> v8 解析 -> 得到编译结果（字节码） -> 线程通信 -> 通知GPU绘制 -> 渲染</p>
</blockquote>
<p>​</p>
<p>那如果我们使用了WebAssembly，那又是一个什么过程呢</p>
<blockquote>
<p>业务代码 -> 编译 -> 字节码 -> 线程通信 -> 通知GPU绘制 -> 渲染</p>
</blockquote>
<p>​</p>
<p>可以看出，这两个链路最大的区别就是，在第二种链路中，浏览器(V8)所得到的东西，已经是一份可以执行的字节码了，他只需要执行就完事了，而不需要使用大量的CPU来对可能很复杂的源代码来进行编译。（当然也可以使用worker 这里就不做讨论了）
但是纯纯的字节码指定是不行的，C/C++，Rust可能都有自己的一套规范，所以这就需要一套规范来整合一下，让大家都可以愉快的在浏览器中玩耍，这可以说就是WebAssembly，由他的标准可以生成后缀名为.wasm的文件，可以直接交给浏览器执行
目前主流的浏览器都已经支持了WebAssembly。除此之外 ，依照wasm的特性，个人认为或者wasm未来在多端也能有一定的用处</p>
<h2 data-id="heading-3">实战</h2>
<p>俗话说的好，纸上得来终觉浅，绝知此事要躬行，上面简单学习了rust+wasm，那如果不实践一下那不是浪费了吗，那到底怎么实践rust+wasm呢？自己看着wasm的文档写？那指定是不行的。
那怎么办呢？不要慌，今天的第三位猪脚出现了:Yew
文档在此
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fyew.rs%2Fzh-CN" target="_blank" rel="nofollow noopener noreferrer" title="https://yew.rs/zh-CN" ref="nofollow noopener noreferrer">yew中文文档</a>
简介如下
<strong>Yew</strong> 是一个设计先进的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.rust-lang.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.rust-lang.org/" ref="nofollow noopener noreferrer">Rust</a> 框架，目的是使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebassembly.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webassembly.org/" ref="nofollow noopener noreferrer">WebAssembly</a> 来创建多线程的前端 web 应用。</p>
<ul>
<li><strong>基于组件的框架</strong>，可以轻松的创建交互式 UI。拥有 <a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/" ref="nofollow noopener noreferrer">React</a> 或 <a href="https://link.juejin.cn/?target=https%3A%2F%2Felm-lang.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://elm-lang.org/" ref="nofollow noopener noreferrer">Elm</a> 等框架经验的开发人员在使用 Yew 时会感到得心应手。</li>
<li><strong>高性能</strong> ，前端开发者可以轻易的将工作分流至后端来减少 DOM API 的调用，从而达到异常出色的性能。</li>
<li><strong>支持与 JavaScript 交互</strong> ，允许开发者使用 NPM 包，并与现有的 JavaScript 应用程序结合。</li>
</ul>
<p>让一个yew应用跑起来分三步（确信）</p>
<ol>
<li>创建一个二进制项目</li>
</ol>
<pre><code class="copyable">cargo new --bin yew-app && cd yew-app
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>编写代码，注意要编写index.html</li>
<li>启动</li>
</ol>
<pre><code class="hljs language-sql copyable" lang="sql">cargo install trunk wasm<span class="hljs-operator">-</span>bindgen<span class="hljs-operator">-</span>cli
rustup target <span class="hljs-keyword">add</span> wasm32<span class="hljs-operator">-</span><span class="hljs-literal">unknown</span><span class="hljs-operator">-</span><span class="hljs-literal">unknown</span>
trunk serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一张图简述一下wasm-bindgen的作用
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce10545aa7094d2abcc700db1a4c34ce~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">组件化</h3>
<p>页面展示的代码</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">use</span> yew::prelude::*;

<span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">Msg</span></span> &#123;
    AddOne,
&#125;

<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Model</span></span> &#123;
    link: ComponentLink<<span class="hljs-keyword">Self</span>>,
    value: <span class="hljs-built_in">i64</span>,
&#125;

<span class="hljs-keyword">impl</span> Component <span class="hljs-keyword">for</span> Model &#123;
    <span class="hljs-class"><span class="hljs-keyword">type</span> <span class="hljs-title">Message</span></span> = Msg;
    <span class="hljs-class"><span class="hljs-keyword">type</span> <span class="hljs-title">Properties</span></span> = ();

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">create</span></span>(_props: Self::Properties, link: ComponentLink<<span class="hljs-keyword">Self</span>>) -> <span class="hljs-keyword">Self</span> &#123;
        <span class="hljs-keyword">Self</span> &#123;
            link,
            value: <span class="hljs-number">0</span>,
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">update</span></span>(&<span class="hljs-keyword">mut</span> <span class="hljs-keyword">self</span>, msg: Self::Message) -> ShouldRender &#123;
        <span class="hljs-keyword">match</span> msg &#123;
            Msg::AddOne => &#123;
                <span class="hljs-keyword">self</span>.value += <span class="hljs-number">1</span>;
                <span class="hljs-literal">true</span>
            &#125;
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">change</span></span>(&<span class="hljs-keyword">mut</span> <span class="hljs-keyword">self</span>, _props: Self::Properties) -> ShouldRender &#123;
        <span class="hljs-literal">false</span>
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">view</span></span>(&<span class="hljs-keyword">self</span>) -> Html &#123;
        html! &#123;
            <div>
                <p>&#123; <span class="hljs-string">"tandake is a Vegetable Chicken"</span>  &#125;</p>
                <button onclick=<span class="hljs-keyword">self</span>.link.callback(|_| Msg::AddOne)>&#123; <span class="hljs-string">"+1"</span> &#125;</button>
                <p>&#123; <span class="hljs-keyword">self</span>.value  &#125;</p>
            </div>
        &#125;
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">main</span></span>() &#123;
    yew::start_app::<Model>();
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果演示
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/865269e93ae245d09b49e677e3e99024~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看出，这里的渲染的文件来源已经是wasm了
眼尖的同学可能已经发现了上面的create，update ，change几个函数，那么他们是用来干嘛的呢？
简单说一下yew中组件的生命周期：
Component 特质定义了六个生命周期函数。</p>
<ul>
<li>create 是一个构造函数，接收道具和ComponentLink</li>
<li>view 渲染该组件</li>
<li>update 当一个Message 被发送到该组件时被调用，实现消息传递的逻辑</li>
<li>change 重新渲染变化，优化渲染速度</li>
<li>rendered 在view 之后但在浏览器更新之前被调用一次，以区分第一次渲染和连续渲染。</li>
<li>destroy ，当一个组件被卸载并需要进行清理操作时被调用。</li>
</ul>
<p>如果把他类比成react的类组件，那么create就是constructor构造函数，update就是相当于注册在组件内部的一些静态方法，change相当于shouldcomponentupdate，其他的生命周期也可同比</p>
<h3 data-id="heading-5">父子组件中通信</h3>
<p>前文说到yew是基于组件的，那么父子组件该怎么进行最简单的数据通信呢？
声明父组件</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-meta">#[derive(Clone, PartialEq, Properties, Default)]</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Properties</span></span> &#123;
    name: <span class="hljs-built_in">String</span>,
&#125;

<span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">Message</span></span> &#123;
    ChangeName(<span class="hljs-built_in">String</span>),
&#125;

<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Model</span></span> &#123;
    link: ComponentLink<<span class="hljs-keyword">Self</span>>,
    props: Properties,
&#125;

<span class="hljs-keyword">impl</span> Model &#123;
    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">change_name</span></span>(&<span class="hljs-keyword">mut</span> <span class="hljs-keyword">self</span>, name: <span class="hljs-built_in">String</span>) &#123;
        <span class="hljs-keyword">self</span>.props.name = name;
    &#125;
&#125;
<span class="hljs-keyword">impl</span> Component <span class="hljs-keyword">for</span> Model &#123;
    <span class="hljs-class"><span class="hljs-keyword">type</span> <span class="hljs-title">Message</span></span> = Message;
    <span class="hljs-class"><span class="hljs-keyword">type</span> <span class="hljs-title">Properties</span></span> = Properties;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">create</span></span>(_props: Self::Properties, link: ComponentLink<<span class="hljs-keyword">Self</span>>) -> <span class="hljs-keyword">Self</span> &#123;
        <span class="hljs-keyword">Self</span> &#123;
            link,
            props: Properties &#123;
                name: <span class="hljs-string">"tandake"</span>.to_string(),
            &#125;,
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">update</span></span>(&<span class="hljs-keyword">mut</span> <span class="hljs-keyword">self</span>, msg: Self::Message) -> ShouldRender &#123;
        <span class="hljs-keyword">match</span> msg &#123;
            Message::ChangeName(name) => &#123;
                <span class="hljs-keyword">self</span>.change_name(name);
            &#125;
        &#125;;
        <span class="hljs-literal">true</span>
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">change</span></span>(&<span class="hljs-keyword">mut</span> <span class="hljs-keyword">self</span>, _props: Self::Properties) -> ShouldRender &#123;
        <span class="hljs-literal">false</span>
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">view</span></span>(&<span class="hljs-keyword">self</span>) -> Html &#123;
        html! &#123;
            <div>
                <p>&#123; <span class="hljs-string">"大家好，我是练习时长两天半的rust实习生，谭达科"</span>  &#125;</p>
                <p>&#123;<span class="hljs-string">"hello "</span>&#125;&#123;<span class="hljs-keyword">self</span>.props.name.clone()&#125;</p>
            <Button onclick=&#123;<span class="hljs-keyword">self</span>.link.callback(|name: <span class="hljs-built_in">String</span>| Message::ChangeName(name))&#125; />
            </div>
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>声明子组件</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-meta">#[derive(Clone, PartialEq, Properties, Default)]</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">ButtonProperties</span></span> &#123;
    onclick: Callback<<span class="hljs-built_in">String</span>>,
&#125;

<span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">ButtonMessage</span></span> &#123;
    ChangName,
&#125;

<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Button</span></span> &#123;
    props: ButtonProperties,
    link: ComponentLink<<span class="hljs-keyword">Self</span>>,
&#125;

<span class="hljs-keyword">impl</span> Button &#123;
    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">change_name</span></span>(&<span class="hljs-keyword">mut</span> <span class="hljs-keyword">self</span>) &#123;
        <span class="hljs-keyword">self</span>.props.onclick.emit(<span class="hljs-string">"is a vegetableChicken"</span>.to_string());
    &#125;
&#125;

<span class="hljs-keyword">impl</span> Component <span class="hljs-keyword">for</span> Button &#123;
    <span class="hljs-class"><span class="hljs-keyword">type</span> <span class="hljs-title">Message</span></span> = ButtonMessage;
    <span class="hljs-class"><span class="hljs-keyword">type</span> <span class="hljs-title">Properties</span></span> = ButtonProperties;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">create</span></span>(props: Self::Properties, link: ComponentLink<<span class="hljs-keyword">Self</span>>) -> <span class="hljs-keyword">Self</span> &#123;
        <span class="hljs-keyword">Self</span> &#123; props, link &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">update</span></span>(&<span class="hljs-keyword">mut</span> <span class="hljs-keyword">self</span>, msg: Self::Message) -> <span class="hljs-built_in">bool</span> &#123;
        <span class="hljs-keyword">match</span> msg &#123;
            ButtonMessage::ChangName => &#123;
                <span class="hljs-keyword">self</span>.change_name();
            &#125;
        &#125;;
        <span class="hljs-literal">true</span>
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">change</span></span>(&<span class="hljs-keyword">mut</span> <span class="hljs-keyword">self</span>, props: Self::Properties) -> <span class="hljs-built_in">bool</span> &#123;
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">self</span>.props != props &#123;
            <span class="hljs-keyword">self</span>.props = props;
            <span class="hljs-literal">true</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-literal">false</span>
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">view</span></span>(&<span class="hljs-keyword">self</span>) -> Html &#123;
        html! &#123;
        <button onclick=&#123;<span class="hljs-keyword">self</span>.link.callback(|_| ButtonMessage::ChangName)&#125;>&#123;<span class="hljs-string">"click me"</span>&#125;</button>
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>演示效果
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/238d2237516c44dcaa02491e38289137~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
声明一个组件需要一些什么东西呢？
从上面这个简单的demo可以看出一个大概</p>
<ol>
<li>定义属性结构</li>
</ol>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-meta">#[derive(Clone, PartialEq, Properties, Default)]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>把属性附加到状态</li>
</ol>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Button</span></span> &#123;
    props: ButtonProperties,
    link: ComponentLink<<span class="hljs-keyword">Self</span>>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>初始化组件的状态</li>
</ol>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">create</span></span>(props: Self::Properties, link: ComponentLink<<span class="hljs-keyword">Self</span>>) -> <span class="hljs-keyword">Self</span> &#123;
        <span class="hljs-keyword">Self</span> &#123; props, link &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>初始化生命周期，在update中接受事件，在change中重新渲染</li>
</ol>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">update</span></span>(&<span class="hljs-keyword">mut</span> <span class="hljs-keyword">self</span>, msg: Self::Message) -> <span class="hljs-built_in">bool</span> &#123;
        <span class="hljs-keyword">match</span> msg &#123;
            ButtonMessage::ChangName => &#123;
                <span class="hljs-keyword">self</span>.change_name();
            &#125;
        &#125;;
        <span class="hljs-literal">true</span>
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">change</span></span>(&<span class="hljs-keyword">mut</span> <span class="hljs-keyword">self</span>, props: Self::Properties) -> <span class="hljs-built_in">bool</span> &#123;
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">self</span>.props != props &#123;
            <span class="hljs-keyword">self</span>.props = props;
            <span class="hljs-literal">true</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-literal">false</span>
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">view</span></span>(&<span class="hljs-keyword">self</span>) -> Html &#123;
        html! &#123;
        <button onclick=&#123;<span class="hljs-keyword">self</span>.link.callback(|_| ButtonMessage::ChangName)&#125;>&#123;<span class="hljs-string">"click me"</span>&#125;</button>
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>需要交互注册自定义事件</li>
</ol>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">impl</span> Button &#123;
    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">change_name</span></span>(&<span class="hljs-keyword">mut</span> <span class="hljs-keyword">self</span>) &#123;
        <span class="hljs-keyword">self</span>.props.onclick.emit(<span class="hljs-string">"is a vegetableChicken"</span>.to_string());
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种写法与现在我们使用的react的写法是比较类似的（当然也可以使用vue的emit的方式）</p>
<h3 data-id="heading-6">函数式组件</h3>
<p>上诉yew的组件多多少少和类组件比较像，那么yew可不可以使用一种类似函数式组件的方法？甚至使用hooks呢？
当然可以
下面我们来实现一个简单的点击计数器（效果和第一个类似，就不再赘述了）</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-meta">#[derive(Properties, Clone, PartialEq)]</span>
<span class="hljs-keyword">pub</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">RenderedAtProps</span></span> &#123;
    <span class="hljs-keyword">pub</span> time: <span class="hljs-built_in">String</span>,
&#125;
<span class="hljs-meta">#[function_component(App)]</span>
<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">app</span></span>() -> Html &#123;
    <span class="hljs-keyword">let</span> (counter, set_counter) = use_state(|| <span class="hljs-number">0</span>);

    <span class="hljs-keyword">let</span> onclick = &#123;
        <span class="hljs-keyword">let</span> counter = Rc::clone(&counter);
        Callback::from(<span class="hljs-keyword">move</span> |_| set_counter(*counter + <span class="hljs-number">1</span>))
    &#125;;

    html! &#123;
        <div>
            <button onclick=onclick>&#123; <span class="hljs-string">"Increment value"</span> &#125;</button>
            <p>
                <b>&#123; <span class="hljs-string">"Current value: "</span> &#125;</b>
                &#123; counter &#125;
            </p>
        </div>
    &#125;
&#125;

<span class="hljs-meta">#[function_component(RenderedAt)]</span>
<span class="hljs-keyword">pub</span> <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">rendered_at</span></span>(props: &RenderedAtProps) -> Html &#123;
    html! &#123;
        <p>
            <b>&#123; <span class="hljs-string">"Rendered at: "</span> &#125;</b>
            &#123; props.time.clone() &#125;
        </p>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样看起来是不是有react的函数式组件那味了，在使用函数组件的时候，我们也可以使用yew中自带的各种hooks，包括了但不限于以下hook钩子</p>
<ul>
<li>use_state</li>
<li>use_ref</li>
<li>use_reducer</li>
<li>use_reducer_with_init</li>
<li>use_effect</li>
<li>use_effect_with_deps</li>
</ul>
<p>​</p>
<p>Yew虽然说是一款Rust框架，但是在实际使用上与Rust相关，而与我们现在学习的知识无关的地方很少，大多的时候我们都在这里面看到vue和react中的影子，使用的成本其实并不高，就像我们使用JavaScript来开发一样，大家都知道JavaScript是基于V8的，但是我们在编程的时候不是只是关注V8来进行开发吧？这个框架也是一样，虽然基于WebAssembly和Rust，但是使用起来，会比我们想象的顺滑很多
​</p>
<h1 data-id="heading-7">WebAssembly 和 Javascript</h1>
<p>上面讲了yew这个新框架，但是问题又来了，这不是还是要学习Rust吗？我不会Rust，但是我就是想用WebAssembly！我就是想用JavaScript！那怎么办呢？没事，你能想到的，大家都想到了，那下面又来了一位猪脚
​</p>
<h2 data-id="heading-8">AssemblyScript：用Javascript的方式来编写WebAssembly</h2>
<p>还记得上面在介绍rust的时候，提到过的的Rust比Typescript更加丰富的系统吗？
是不是看的心痒痒？没事，Rust的类型系统的确很好，但是下一秒就是我的了，那下面再请出一位猪脚
AssemblyScript
看一句官网的描述</p>
<blockquote>
<p>AssemblyScript compiles a <strong>variant</strong> of <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/" ref="nofollow noopener noreferrer">TypeScript</a>(a typed superset of JavaScript) to <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebassembly.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webassembly.org/" ref="nofollow noopener noreferrer">WebAssembly</a> using <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FWebAssembly%2Fbinaryen" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/WebAssembly/binaryen" ref="nofollow noopener noreferrer">Binaryen</a>，It generates lean and mean WebAssembly modules while being just an npm install away</p>
</blockquote>
<p>它其实就是Typescript的变种，在Typescript的基础上进一步丰富了类型系统，并且可以编译成wasm文件执行，Typescript你不要再给我打电话啦，我怕AssemblyScript 误会
可以将其视为 TypeScript 的高级语法和 C 的低级功能的混合（没错，你可以使用AssemblyScript 来操作内存！！），上文已经说过了jit是个什么玩意儿，一个完整且严格的类型系统可以让JIT更加的迅速，既然要保证对于Jit编译时的优化，也为了WebAssembly来提供静态保证，所以有意<strong>避免JavaScript</strong>无法提前_有效_编译的动态_性_。也就是说，无类型状态，是不存在的！
​</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-comment">// 😢</span>
var a = &#123;&#125;
a.prop = <span class="hljs-string">"hello world"</span>
<span class="hljs-comment">// 😊</span>
var a = new Map<string,string>()
a.set(<span class="hljs-string">"prop"</span>, <span class="hljs-string">"hello world"</span>)
<span class="hljs-comment">// 😢</span>
function foo(a?) &#123;
  var b = a + <span class="hljs-number">1</span>
  <span class="hljs-keyword">return</span> b
&#125;

<span class="hljs-comment">// 😊</span>
function foo(a: <span class="hljs-built_in">i32</span> = <span class="hljs-number">0</span>): <span class="hljs-built_in">i32</span> &#123;
  var b = a + <span class="hljs-number">1</span>
  <span class="hljs-keyword">return</span> b
&#125;
<span class="hljs-comment">// 😢</span>
function foo(a: <span class="hljs-built_in">i32</span> | string): void &#123;
&#125;

<span class="hljs-comment">// 😊</span>
function foo<T>(a: T): void &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，目前这门语言还有许多不完善的地方，对应的生态也不成熟，这门语言的目标是想要成为一个对web开发者上手门槛极低的语言，但是同时他又是一门最终需要编译为WebAssembly的语言，这就需要它在支持目前已有的开发语言的特性的基础上，又不能在依然保有某些语言编译效率底下的特性或者是盲目的迷信二进制的路上越走越远，这可以说是这门语言的哲学，也可以说是这门语言前进的方向
具体的用法就不多说了，大家有兴趣的可以去研究一下（手动狗头）
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.assemblyscript.org%2Fintroduction.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.assemblyscript.org/introduction.html" ref="nofollow noopener noreferrer">AssemblyScript官方英文文档</a>
​</p>
<h2 data-id="heading-9">整合 WebAssembly+Javascript+Vite+Vue/React+Rust</h2>
<p>其实分享到这里，看了wasm这么多骚操作之后，又想起了我们平时的开发框架Vue/React，自然而然，我就会想到：那我能不能直接在Vue/React中使用WebAssembly呢？再过分一点，我甚至把下一代打包构建工具Vite也用上？
答案只有一个：可以
下面我们来实战操作一下，以Vue3为示例
使用到的技术名词</p>
<ul>
<li>Vite: 下一代前端工具</li>
<li>Rust: 一门赋予每个人构建可靠且高效软件能力的语言</li>
<li>WebAssembly: WebAssembly（缩写为Wasm）是基于堆栈的虚拟机的二进制指令格式。 Wasm被设计为编程语言的可移植编译目标，从而可以在Web上为客户端和服务器应用程序进行部署。</li>
<li>wasm-pack: Rust→Wasm 工作流程工具！</li>
<li>vite-plugin-rsw: Vite插件，集成了wasm-pack的CLI，生成wasm的npm包，实现了文件变更，自动构建及热更新。</li>
</ul>
<p>第一步：安装依赖，并且配置vite</p>
<pre><code class="hljs language-rust copyable" lang="rust"># install rsw
npm i -D vite-plugin-rsw
# or
yarn add -D vite-plugin-rsw
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vite.config.ts</span>
<span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>;
<span class="hljs-keyword">import</span> ViteRsw <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-rsw'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [
    ViteRsw(&#123;
      <span class="hljs-attr">crates</span>: [
        <span class="hljs-string">'@rsw/hey'</span>,
        <span class="hljs-string">'rsw-test'</span>,
        <span class="hljs-comment">// https://github.com/lencx/vite-plugin-rsw/issues/8#issuecomment-820281861</span>
        <span class="hljs-comment">// outDir: use `path.resolve` or relative path.</span>
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'@rsw/hello'</span>, <span class="hljs-attr">outDir</span>: <span class="hljs-string">'custom/path'</span> &#125;,
      ],
    &#125;),
  ],
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步</p>
<ol>
<li>配置rust</li>
</ol>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">use</span> wasm_bindgen::prelude::*;

<span class="hljs-comment">// Import the `window.alert` function from the Web.</span>
<span class="hljs-meta">#[wasm_bindgen]</span>
<span class="hljs-keyword">extern</span> <span class="hljs-string">"C"</span> &#123;
    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">alert</span></span>(s: &<span class="hljs-built_in">str</span>);
&#125;

<span class="hljs-comment">// Export a `greet` function from Rust to JavaScript, that alerts a</span>
<span class="hljs-comment">// hello message.</span>
<span class="hljs-meta">#[wasm_bindgen]</span>
<span class="hljs-keyword">pub</span> <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">greet</span></span>(name: &<span class="hljs-built_in">str</span>) &#123;
    alert(&<span class="hljs-built_in">format!</span>(<span class="hljs-string">"Hello, &#123;&#125;!"</span>, name));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>在JavaScript的模块中引用</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"greet('webAssembly')"</span>></span>hello wasm<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"greet2('wasm')"</span>></span>hi wasm<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> init, &#123; greet &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@rsw/hey'</span>;
<span class="hljs-keyword">import</span> init2, &#123; greet <span class="hljs-keyword">as</span> greet2 &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rsw-test'</span>;
<span class="hljs-keyword">import</span> &#123; ref, defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-comment">// init wasm</span>
init();
init2();

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'HelloWasm'</span>,
  <span class="hljs-attr">setup</span>: <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> &#123; greet, greet2 &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，这样本质上还是rust不过是在vite+vue3的环境中来书写rust，利用wasm-bindgen让rust和JavaScript可以互相调用，体验上确实没有JavaScript来得好，不过也算是另一种开发的思路</p>
<h1 data-id="heading-10">总结</h1>
<p>不能说未来全是WebAssembly，但是以后WebAssembly在web上绝对会有一个极其重要的地位，现在的WebAssembly各种思路，百花齐放，但是有一点是不变的，WebAssembly的发展一定是紧跟着未来的趋势的，各种WebAssembly的GitHub仓库，各种构建打包工具，各种WebAssembly的开发框架，都如雨后春笋一般正在涌现。当然Rust也是一样，我相信这俩兄弟，在未来一定大放光彩！</p></div>  
</div>
            