
---
title: '探究Swift Type Inference源码 - 闭包中的"_ in"竟这么神奇？'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12d5c780fadc4b309d733f12ab3e3ef0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 22:42:29 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12d5c780fadc4b309d733f12ab3e3ef0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">从一次RxSwift调用说起</h1>
<h2 data-id="heading-1">问题发现</h2>
<p>在一次编写业务界面场景中，有一个界面需要展示加载页面，等待数据加载完成后，再渲染实际界面。数据可多次加载，每次加载数据视图都要显示Loading页。所以为此在ViewModel中构建了一个发送可选值的信号：</p>
<pre><code class="copyable">let data: BehaviorRelay<DataType?> = BehaviorRelay(value: nil）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个信号的值如果发送nil，则代表数据在加载中，视图需要显示Loading态；如果是非nil，则是代表新数据加载完成，视图层接收此时机，做页面展示工作。为了让视图层更纯粹的响应信号，这两种操作在viewModel中被分开来，如下图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12d5c780fadc4b309d733f12ab3e3ef0~tplv-k3u1fbpfcp-watermark.image" alt="1617609323018_50c71ae2c37c59d6fc6c01914698e057.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>仅考虑上面交互的链路，要想过滤nil，自然用到了compactMap操作符，同时为了不让视图层直接接触数据Data，后面加了一个map操作符，把数据本身map成一个常量。所以视图层订阅的信号实际上变成了如下写法：</p>
<pre><code class="copyable">let dataReady = data.compactMap &#123; $0 &#125;.map &#123; true &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们聚焦的逻辑可以概括为：</p>
<p><strong>视图层在ViewModel接收到非空数据时机，去做视图构建动作</strong></p>
<p>视图层监听信号的操作是这样的：</p>
<pre><code class="copyable">viewModel.dataReady.subscribe(onNext: &#123;

    // do something with build Content
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一段构建绑定的代码，我们都知道，当信号被subscribe订阅时，即触发订阅本身的逻辑闭包。但是由于原信号是个有初始值nil的BehaviorRelay，经过compactMap操作符过滤掉nil之后，理论上首次订阅不会触发监听闭包，预期数据流如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e16044da34b842b7ab6bfb5a0bc49a59~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然而事实是符合预期么？</p>
<p><strong>Of course not</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/614fe0d742994b27b46bd8ec4e66404f~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行起来后，可以从调用栈上看到订阅立即触发了监听闭包（也就是83行和84行是同步串行执行的）。嗯？nil值不是应该被compactMap过滤掉了么？信号应该根本发不出来才对。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c262df1831e44342862ba71da98737f2~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">问题初判断</h2>
<p>遇到这个现象，第一反应是RxSwift的使用姿势不对，因为毕竟它有如此多的操作符和概念，让人没有那么大的信心确定使用方式是正确的。所以直接去翻了下CompactMap操作符的源码：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4cb010a74b2460d9232369789842f6f~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到当源信号发送next值时，CompactMapSink里的处理逻辑（红框部分），做了一个可选值绑定，如果不为nil，才继续发送给下游信号。而_transform闭包就是上文中的 &#123; $0 &#125; 部分，所以self._transform(element)就是element本身。也就是说，理论上这个if是走不进来的。</p>
<p>我们尝试打个断点：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98bfd2d8493d43e880a995d799d692b1~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到确实是走到了if里面，mappedElement是个 <code>(())</code></p>
<p>嗯？这个<code>(())</code>是什么，可以清楚的看到element是nil，然后经过 &#123; $0 &#125; 闭包计算之后，变成了<code>(())</code>这个东西，故而被绑定到了mappedElement上，发送给了下游信号。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f0ef671c8524fcb949a7c5b669d73f2~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>意识到<code>(())</code>这个其实是个空元组，也就是Tuple。我们知道Swift对于Void的类型就是空元组，但它并不等于nil，所以造成了这个问题。那么为什么<code>&#123; $0 &#125;</code>(nil)的结果是个<code>()</code>呢？难道Rxswift背后有什么黑科技对于nil做了特殊处理？</p>
<h2 data-id="heading-3">思路扩散</h2>
<p>当查找问题陷入停滞的时候，可以从多角度尝试观察，比如换一个写法。所以经过几次写法的尝试后，不出所料，这次成功遇到了更诡异的问题。我发现如果把信号转换写成这样：</p>
<pre><code class="copyable">data.compactMap &#123; $0 &#125;.map &#123; _ in true &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题就解决了.....</p>
<p>（为了方便调试mappedElement的值，稍微更改了写法）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/264c6ea99d2a42f78edbed8031a7005a~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer">
对比一下原写法：</p>
<pre><code class="copyable">// 有问题的写法
data.compactMap &#123; $0 &#125;.map &#123; true &#125; 

// 没问题的写法
data.compactMap &#123; $0 &#125;.map &#123; _ in true &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f01eaceb5b9d4348a750210aabd1988c~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这抛出了两个新的疑问：</p>
<ul>
<li>最直接的疑问：难道 「_ in」增加与否会对代码逻辑产生影响？</li>
<li>最诡异的疑问：为什么更改 map 闭包的写法会反过来对compactMap的逻辑有影响？</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea1f08ee3d4d4e4a82b4df91c0e28c58~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">问题根源定位</h1>
<h2 data-id="heading-5">问题简化</h2>
<p>到这里我逐渐意识到应该不是RxSwift的问题，可能是语言层面上的原因。为此我构造了一个简化版的Demo：</p>
<pre><code class="copyable">struct Transform<E> &#123;
 let element: E

 func foo<T>(transform: (E) -> T) -> TransformB<T> &#123;
         let mappedElement = transform(element)
         return TransformB<T>(element: mappedElement)
     &#125;
 &#125;



struct TransformB<E> &#123;
 let element: E

 func foo<T>(transform: (E) -> T) -> T &#123;
         return transform(element)
     &#125;
 &#125;


let instance = Transform(element: "1")

// 模仿写法
let result = instance.foo&#123;$0&#125;.foo&#123;true&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中Transform的结构体有一个foo方法，接收一个闭包，并把闭包的结果包装转换为TransformB的类型；而TransformB同样接收一个闭包，直接输出转换后的值。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87ac6f41b1cf4a828df37a88d21536a7~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行起来，发现仍然和前文的问题一样：第一次的mappedElement输出并不是 "1"，而是()</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3348fea9d80540ea8e72293911e342ae~tplv-k3u1fbpfcp-watermark.image" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以从图中看到mappedElement确实是个Tuple，而且是个空Tuple。</p>
<p>这时意识到Swift对于无返回值函数的类型都是看做返回Void，也就是空Tuple。难道&#123; $0 &#125;的写法有些问题？</p>
<p>带着这个疑问，我尝试着把这两个调用拆开，是想看看第一个闭包调用后的类型是什么。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e0a82d30fa64853b0461a869a296c87~tplv-k3u1fbpfcp-watermark.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第一个调用结果是TransformB，看着没什么问题。</p>
<p>当我想查看第二个类型的时候，编译器报错了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af76527340ec435f8525ae2804168618~tplv-k3u1fbpfcp-watermark.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer">
意思是在这个闭包语境中需要显式列出参数列表，而闭包参数我没有使用到，所以建议我插入<code>_ in</code>。</p>
<p>哈？为啥连在一起调用没有编译错误，拆开就编不过了？一时间感觉被编译器针对了。</p>
<p>于是我又放到了一起调用，还是能编译成功。但是这时报了一个之前没有注意的警告：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a47cacfce8284230b3890b7caef83a13~tplv-k3u1fbpfcp-watermark.image" alt="15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编译器说<code>$0</code>这个变量我没有用到。 （嗯？明明用到了呀，把它当做返回值用到了）</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbcb847ffa294f8da779cc3902d3451d~tplv-k3u1fbpfcp-watermark.image" alt="16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时突然意识到可能是编译器本身的问题，<strong>猜测它把 <code>&#123; $0 &#125;</code>的闭包错误地编译成了返回 Void的闭包</strong>，绕过了$0而没有使用到这个变量，同时又返回了空Tuple值。 这样现象就解释的通了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8d51c16e1054be7b006b624a6e9ee6e~tplv-k3u1fbpfcp-watermark.image" alt="17.png" loading="lazy" referrerpolicy="no-referrer">
经过不断的尝试各种写法，总结出了相似的问题和现象：</p>
<pre><code class="copyable">//编译通过，但现象诡异（第一个闭包返回())
instance.foo &#123; $0 &#125;.foo &#123; true &#125; 
instance.foo &#123; e in e &#125;.foo &#123; return true &#125; 
instance.foo &#123; $0 &#125;.foo &#123; return true &#125; 


//编译不过
instance.foo &#123; e in return e &#125;.foo &#123; true &#125;
instance.foo &#123; e in return e &#125;.foo &#123; return true &#125;
instance.foo &#123; return $0 &#125;.foo &#123; true &#125;


//编译通过，现象符合预期
instance.foo &#123; $0 &#125;.foo &#123; _ in true &#125;
instance.foo &#123; return $0 &#125;.foo &#123; _ in true &#125;
instance.foo &#123; e in return e &#125;.foo &#123; _ in true &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里可能有小伙伴对于要解决的问题比较混乱，这里做个小结：
对于<code>let result = instance.foo &#123; $0 &#125;.foo &#123; true &#125;</code>这个表达式：</p>
<ol>
<li>第一个闭包在某些情景下被编译器错误的编译成返回Void的值，也就是&#123;$0&#125;不论入参是什么，闭包的结果都是()</li>
<li>两个闭包对于各类闭不影响逻辑的包语法糖的改动（比如省略return关键字、省略闭包参数列表。）都会影响整个表达式的编译结果。</li>
</ol>
<h2 data-id="heading-6">寻找定位</h2>
<p>既然程序在运行时在源代码层面展示信息有限，我们从汇编代码里挖掘现象。打开Xcode的<strong>Debug -> Debug WorkFlow -> Always show Disassembly</strong>。</p>
<p>程序运行时，走到第一个transform闭包调用点：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c244bc90e3c5452b9ce5e984fb2653c9~tplv-k3u1fbpfcp-watermark.image" alt="18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时transform闭包的地址已经在rdx寄存器里，执行LLDB的<strong>register read</strong>命令，可以看到控制台输出的注释：</p>
<blockquote>
<p>TestOnMac partial apply forwarder for reabstraction thunk helper from @callee_guaranteed (@guaranteed Swift.String) -> () to @escaping @callee_guaranteed (@in_guaranteed Swift.String) -> (@out ()) at </p>
</blockquote>
<p>这个<code>&#123;$0&#125;</code>transform闭包的类型是<code>(String) -> ()</code>，而不是<code>(String) -> (String)</code>。验证了我们的猜想，确实是编译器产生的可执行代码不符合预期。</p>
<p>那么在整个编译链条中，何处出了问题呢？我决定不放过问题，一探究竟。</p>
<p>我们都知道swift编译链和其它Objective-C、C、C++等语言的区别是，在IR阶段之前，swift有一套功能强大的编译前端系统，它包括类型检查、SIL语言等大力度的优化。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eff291afb9394e098d4c8433dc716068~tplv-k3u1fbpfcp-watermark.image" alt="19.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在，我们去查看SIL的生成结果。</p>
<p>swift编译前端命令是<code>swiftc</code>（实际上和swift命令是同一个），输出sil的命令是</p>
<p><strong>swiftc -emit-sil xxx.swift</strong></p>
<p>执行后得到很多SIL语言的输出，经过简化后，第一个transform被编译成SIL后的结果：</p>
<pre><code class="copyable">// closure #1 in
sil private @$s4mainySSXEfU_ : $@convention(thin) (@guaranteed String) -> () &#123;

// %0 "$0"                                        // user: %1
bb0(%0 : $String):
  debug_value %0 : $String, let, name "$0", argno 1 // id: %1
  %2 = tuple ()                                   // user: %3
  return %2 : $()                                 // id: %3
&#125; // end sil function '$s4mainySSXEfU_'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>closure#1 即为<code>&#123;$0&#125;</code>这个闭包，可以看到在SIL中，它的类型已经是<code>(String) -> ()</code>了，而且看bb0（base block）的代码，可以看出%0是闭包的参数，就是传入的string，%2是空tuple，之后就直接返回了这个空tuple。由此我们可以发现在SIL阶段已经出了问题。</p>
<p>继续沿着编译链条向前，既然是类型判断出了问题，那么去类型决议之后的AST阶段看看：输入命令</p>
<p><strong>swiftc -dump-ast main.swift</strong></p>
<p>我们可以看到输出了色（kan）彩（zhe）缤（tou）纷（teng）的AST结构：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78854425828b416e9492ec598cbff4eb~tplv-k3u1fbpfcp-watermark.image" alt="20.png" loading="lazy" referrerpolicy="no-referrer">
这些是经过类型决议之后的AST结构树，继续在大量结果输出中寻找我们关键的transform闭包类型：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5238ca0134a402689bf3138b7294a7d~tplv-k3u1fbpfcp-watermark.image" alt="21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到经过类型决议后的AST结构也已经把transform判断成(String) -> ()类型的闭包。我们再次执行没有经过类型决议的AST看看：</p>
<p><strong>swiftc -dump-parse main.swift</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a67e10b797d04e14a89c678bbc1c023b~tplv-k3u1fbpfcp-watermark.image" alt="22.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此阶段还没有经过类型决议，仅仅是分析swift源码文本的AST树。</p>
<p>此时我们可以发现在swift编译器构建原始AST结构之后，还没有经过类型决议，经过对AST的语义分析，才得出了错误的类型结果，我们终于定位到了问题所在。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae71116cdbc84f51ae48f0e94897a44d~tplv-k3u1fbpfcp-watermark.image" alt="23.png" loading="lazy" referrerpolicy="no-referrer">
到这里，我们怎样继续深入语义分析的阶段呢？在Swift官方文档有说明：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9609a349965346b18c94f7d0fa1d2ebc~tplv-k3u1fbpfcp-watermark.image" alt="24.png" loading="lazy" referrerpolicy="no-referrer">
执行如下命令：</p>
<p><strong>swiftc -dump-ast main.swift -Xfrontend -debug-constraints</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/341d0adea94d437391dfa1d367af2624~tplv-k3u1fbpfcp-watermark.image" alt="25.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述Log输出了语义分析阶段，类型推断的过程Log，但这次我们略有些看不懂了，所以在继续深入之前，我们先了解一下文章的主角 —— <strong>Swift Type Inference</strong>.</p>
<h1 data-id="heading-7">探究Swift Type Inference</h1>
<h2 data-id="heading-8">简述</h2>
<p>Swift语言的一大特性就是具有强大的类型推断。它很大程度上简化了开发人员的工作量，我们不仅可以省略很多变量类型的显式指定，而且类型推断也同样支撑着代码自动补全的功能。Swift类型推断非常强大，不仅包括变量、表达式的类型推断，而且支持各类泛型结构、泛型函数、协议的关联类型等等。</p>
<p>Swift类型推断系统有三个重要特征：</p>
<ol>
<li><strong>类型推断是双向进行的</strong></li>
<li><strong>类型推断是以单个表达式或陈述语句为范围限制进行处理</strong></li>
<li><strong>类型推断过程基于约束系统实现</strong></li>
</ol>
<p><strong>一、类型推断是双向进行的</strong></p>
<blockquote>
<p>Swift's type inference allows type information to flow in two directions.</p>
</blockquote>
<p>我们直接举个例子，下面定义了一个add函数，并且调用此函数：</p>
<pre><code class="copyable">func add(_ lhs: Int, _ rhs: Int) -> Int &#123;
    lhs + rhs
&#125;

let result = add(4, 5) //result: Int
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们都知道一个表达式(expression)或者陈述语句（statement）被构建成AST结构时，通常表达式的结果是根节点，组成该值的各部分为叶子节点。下图为 let result = add(4, 5) 的AST结构树：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/174ef5b1f3974db6ac9fb4b05c271616~tplv-k3u1fbpfcp-watermark.image" alt="26.png" loading="lazy" referrerpolicy="no-referrer">
在此例中，result类型就可以通过<code>add</code>函数、<code>4</code>、<code>5</code>（字面量）的类型，最后被决议成了Int类型。这样的类型判断流向 "看起来" 是 叶子 -> 根(Leaf To Root)，决议的过程如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b37704bf6d1d4191b3b4cafb11e9810a~tplv-k3u1fbpfcp-watermark.image" alt="27.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上文提到，Swift类型判断是双向的，让我们继续看下面的例子：</p>
<pre><code class="copyable">func add(_ lhs: Int, _ rhs: Int) -> Int &#123;
    lhs + rhs
&#125;


func add(_ lhs: Double, _ rhs: Double) -> Double &#123;
    lhs + rhs
&#125;

let result: Double = add(4, 5) //4: Double, 5: Double
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 let result = add(4,5)，其AST的结构和上一个例子一样，但是这次result被显式指定了Double类型，那么swift类型判断就会反过来决议<code>4</code>，<code>5</code>这两个字面量的类型，在这个case中，通过对add函数的返回值和参数类型、result的类型，最后把<code>4</code>，<code>5</code>两个字面量判断为Double类型。也因此调用到了第二个add函数。这个例子中，类型判断流向 "看起来" 是根->叶子。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6a49fa549904f6eb5298fc5c76e5bb9~tplv-k3u1fbpfcp-watermark.image" alt="28.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注释：</p>
<ul>
<li>上述两个例子中的<code>4</code>，<code>5</code>是字面量，属于<code>integer_literal</code>，不可以直接等价于<code>Int</code>，所以其类型也是需要判断的。</li>
<li>类型推断方向加了引号，是“看起来”。是因为swift类型决议实际上并没有方向的概念，下文会详细说明</li>
</ul>
</blockquote>
<p>双向类型推断（Bi-directional Type Inference）在类ML语言中常见，而主流的C++, Java, C#, Objective-C等语言中不具备此功能。</p>
<p><strong>二、类型推断是以单个表达式或陈述语句为范围限制进行推断</strong></p>
<blockquote>
<p>Swift limits the scope of type inference to a single expression or statement.</p>
</blockquote>
<p>Swift是强类型语言，而且具有复杂的类型系统，除了普通的表达式类型推断，还需要处理泛型、函数重载、协议约束等复杂的情形，所以出于执行性能和给出更准确诊断的考虑，Swift类型推断把范围限制在单个表达式或者陈述语句。</p>
<p><strong>三、类型推断是基于约束系统实现</strong></p>
<p>像布局约束一样，类型推断过程中也是基于类型约束来计算类型的，比如有相等性约束；转换型约束；成员约束；子类约束等等。Swift这样设计是可以把约束系统本身和求解过程解耦。约束本身的定义和描述基本不会变化，而求解过程可以持续优化。</p>
<h2 data-id="heading-9">工作流</h2>
<p>上文提到，Swift类型推断的过程是基于单个表达式或陈述语句，在求解过程中，这个过程可以在被称作一个Scope的概念中进行，对于一个求解Scope，类型推断的过程如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22ef597eeb4e46bb96cc9436963cd197~tplv-k3u1fbpfcp-watermark.image" alt="29.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Constraint Generation</strong></p>
<p>第一个步骤是生成此次求解Scope的所有类型约束，这个过程可能会根据一些已有的上下文（比如上一个Scope的求解结果）去生成。</p>
<p>Type Checker会遍历AST结构树，生成一系列约束，这些约束会描述表达式以及子表达式所有的类型之间关系，比如有成员类型约束、父子类型约束、转换类型约束等等。有些未被决议的类型被标记为变量，用Tx（T0,T1,....)表示，之后这些类型变量会在Solving阶段被决议。</p>
<p><strong>Constraint Solving</strong></p>
<p>当Scope中的所有类型约束生成后，Swift类型推断会进行到这一步骤，这里也是类型推断中最重要的过程，它通过第一阶段生成的类型约束，利用各种不同类型对应的求解策略，计算出所有还未被决议的类型变量。</p>
<p>求解的过程包含大量的策略，有可能进行函数的类型转换、也有可能求出多个类似解，Solving过程有一套Solution的对比策略，来对比出最佳的求解结果。</p>
<p>当然，这一求解过程中有可能因为代码类型的不匹配而出错，这时Swift类型推断会把错误记录下来、会尝试进行修复，以此用于生成编译器的诊断，最后通过编译器的warning或error报出。</p>
<p><strong>Solution Application</strong></p>
<p>当Solving步骤求解成功，决议了所有类型变量之后，Swift类型推断会把之前的求解结果通过Rewrite AST的过程把所有类型变量的结果赋值给对应的类型上去，在这一步骤中，所有类型都必须显式的被决议成具体类型（Concrete types）。</p>
<h2 data-id="heading-10">Solving过程解析</h2>
<p><strong>Step</strong></p>
<p>Solving作为类型推断的核心流程，其整个过程是可以理解为一步步SolverStep对每个类型约束的的求解过程，若干个不同种类的Step逐步解析、最后得到一个完整的求解方案。 在源码中，表示求解步骤的基类是SolverStep，其简化的源码头文件定义如下所示：</p>
<pre><code class="copyable">class SolverStep &#123;

protected:

 ConstraintSystem &CS;  // 表示整个求解Scope的约束系统

 StepState State; // Step的状态 （Setup, Ready, Running, Suspended, Done)

 SmallVectorImpl<Solution> &Solutions; // 求解结果

public:

// 初始化方法， 持有传入的约束系统（获得约束），和Solution数组 （待填充）

 explicit SolverStep(ConstraintSystem &cs,
           SmallVectorImpl<Solution> &solutions)
   : CS(cs), Solutions(solutions) &#123;&#125;

 virtual ~SolverStep() &#123;&#125; // 析构方法

 virtual void setup() &#123;&#125;  // setup方法

 virtual StepResult take(bool prevFailed) = 0;  // take方法，主要求解实现。返回StepResult

 virtual StepResult resume(bool prevFailed) = 0; // resume，在suspended状态被唤起时调用。返回StepResult

 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SolverStep抽象了求解步骤的功能，其内部状态流转图如下所示</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6aaaff2b0f3c4b8f91973ab2e1611e82~tplv-k3u1fbpfcp-watermark.image" alt="30.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>SolverStep的流转主要是通过5个状态 + 2个函数支撑的。五个状态的意义分别代表</p>



































<table><thead><tr><th>Step状态</th><th>作用</th><th>可以产生的StepResult</th></tr></thead><tbody><tr><td><strong>Setup</strong></td><td>Step处于初始状态</td><td>不产生Result</td></tr><tr><td><strong>Ready</strong></td><td>Step处于可执行状态</td><td>不产生Result</td></tr><tr><td><strong>Running</strong></td><td>Step正在执行</td><td>不产生Result</td></tr><tr><td><strong>Suspended</strong></td><td>Step被挂起，仍未求解完成，等待被恢复</td><td>Unsolved</td></tr><tr><td><strong>Done</strong></td><td>Step已结束。求解成功 / 失败</td><td>Solved / Error</td></tr></tbody></table>
<p>这五个状态的流转对该Step的求解过程十分重要，它的状态流转可由内部驱动，也可由外部操作。</p>
<p>而关于<code>take()</code>函数和<code>resume()</code>的函数，它们驱动着实际求解的逻辑。</p>
<ul>
<li><code>take()</code>函数一般是作为求解过程的核心逻辑，不同的Step类型有着不同的目标逻辑。</li>
<li><code>resume()</code>函数是作为suspended状态唤醒之后的入口，通常会根据之前保存的数据结合此次唤醒的操作判断是否可继续执行，如果可继续执行，则会继续调用<code>take()</code>函数。</li>
</ul>
<p>SolverStep是基类，用来抽象Step状态流转。实际的求解过程在子类中实现，它有四种子类，其中BindingStep子类又被细分成两个子类。它们的作用及特点如下表所示：</p>

























<table><thead><tr><th>子类名称</th><th>主要作用</th></tr></thead><tbody><tr><td><strong>SplitterStep</strong></td><td>运用算法，将整个约束图（Constraint Graph）拆解成独立可求解的子系统（component），之后再进行合并</td></tr><tr><td><strong>DependentComponentSplitterStep</strong></td><td>依赖其它component的求解，负责合并依赖的部分求解结果</td></tr><tr><td><strong>ComponentStep</strong></td><td>可独立求解的部分，可以产生BindingStep</td></tr><tr><td><strong>BindingStep</strong></td><td>主要用来做类型绑定，可以认为是类型求解系统的基本执行单元。它有两个细分子类TypeVariableStep 和 DisjunctionStep</td></tr></tbody></table>
<p><strong>Solver</strong></p>
<p>SolverStep是用来求解的步骤，那么整体必然有一只“手”，用来调度各类的步骤。这个过程在CSSolver.cpp文件里的solveImpl函数中体现，核心源码如下：</p>
<pre><code class="copyable">void ConstraintSystem::solveImpl(SmallVectorImpl<Solution> &solutions) &#123;

 // 给整个ConstraintSystem设置Solving阶段
 setPhase(ConstraintSystemPhase::Solving);

 // 确保函数退出时，整个ConstraintSystem设置Finalization阶段
 SWIFT_DEFER &#123; setPhase(ConstraintSystemPhase::Finalization); &#125;;

 // 创建新的求解Scope
 SolverScope scope(*this);

 // 创建workList
 SmallVector<std::unique_ptr<SolverStep>, 16> workList;

 // workList推入第一个Step
 workList.push_back(std::make_unique<SplitterStep>(*this, solutions));

// 对「上一步骤失败」初始化为false
 bool prevFailed = false;

 // advance驱动函数， 用来驱动下一个Step的执行
 auto advance = [](SolverStep *step, bool prevFailed) -> StepResult &#123;

  // 获取当前步骤的执行状态
  auto currentState = step->getState();

  // 如果是setup状态，执行setup操作，并置位ready状态
  if (currentState == StepState::Setup) &#123;

   step->setup();

   step->transitionTo(StepState::Ready);

  &#125;

  // 获取当前状态（在更新running state之前保存）
  currentState = step->getState();

  // step置为running态
  step->transitionTo(StepState::Running);

  // 判断running态之前的状态， 如果是ready，则调用take函数；如果是suspended，则调用resume唤起
  return currentState == StepState::Ready ? step->take(prevFailed)
                      : step->resume(prevFailed);

 &#125;;


 // 对workList的step任务进行LIFO顺序的执行
 while (!workList.empty()) &#123;

 // 取最后一个（最新）的step
  auto &step = workList.back();

  &#123;
   // 执行step，得到StepResult
   auto result = advance(step.get(), prevFailed);

   switch (result.getKind()) &#123;

   // 错误也可以被认为完成状态，表示此步骤没有找到结果。需要退出step。
   case SolutionKind::Error:
    fallthrough;

   // 求解完成，弹出workList
   case SolutionKind::Solved: &#123;
    workList.pop_back();
    break;
   &#125;

   // 尚未求解完成，处于suspended状态，需要求解后续step来回溯等待唤起
   case SolutionKind::Unsolved:
    break;
   &#125;

   // 标识上一步是否error
   prevFailed = result.getKind() == SolutionKind::Error;

   
   // 根据result的结果更新worklist，尾部添加新的step，或者什么也不做（添加0个）
   result.transfer(workList);
  &#125;
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整个操作流程的函数步骤还是比较清晰的，其实不难发现整个workList更像是一个栈，可以不断的在栈顶添加新产生的step，当栈顶的step被完成（Solved或者Error），step就会出栈，从而继续求解下一个step，直到栈为空，整个scope就求解完成了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2806895522e4478caf21bd14a5692d83~tplv-k3u1fbpfcp-watermark.image" alt="31.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">问题带入</h1>
<p><strong>从Log中观察</strong></p>
<p>对类型推断的过程有了了解后，我们把目光回到问题中来，此时我们观察Log输出大概就有了基本的概念认知。对于我们的表达式，整个求解过程的Log的结构大致是这样的：</p>
<pre><code class="copyable">// 求解 let result = instance.foo&#123;$0&#125;.foo&#123;true&#125; 中所有类型的过程


---Constraint solving at [/Users/Rico/Rico/Program/TestOnMac/TestOnMac/main.swift:62:15 - line:62:42]---
---Initial constraints for the given expression---

Score: 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Type Variables:
$T0 : ......
$T1 : ......
.
.
.
$T13: .....


Active Constraints:
  $T4 arg conv (String) -> $T3 
  $T11 arg conv ($T3) -> $T10 


Inactive Constraints:
  $T4 closure can default to ($T5) -> $T6 
  $T11 closure can default to () -> $T12


Opened Types:
....



---Solver statistics---
Maximum depth reached while exploring solutions: 9
Time: 7.490000e+00ms

---Solution---
Fixed score: 0 0 0 0 0 0 0 2 0 0 0 0 0 0
Type Variables:
$T0 as Transform<String>
$T1 as ((String) -> ()) -> TransformB<()>
.
.
.
$T13 as Bool
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到，Log输出基本体现了上述描述的求解过程。整个Log有点长，让我们逐步分析。</p>
<p><strong>类型变量</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95e5cad029f84396826aeeeb6f40624d~tplv-k3u1fbpfcp-watermark.image" alt="32.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先，Type-Checker拿到表达式对应的原始的AST结构，遍历后生成了14个类型变量。这里为了能更清晰地看懂后续的求解过程，这里详细拆解这14个类型变量都代表着什么。</p>
<p>再次回顾一下源码</p>
<pre><code class="copyable">struct Transform<E> &#123;
 let element: E

 func foo<T>(transform: (E) -> T) -> TransformB<T> &#123;
         let mappedElement = transform(element)
         return TransformB<T>(element: mappedElement)
     &#125;
 &#125;

struct TransformB<E> &#123;
 let element: E

 func foo<T>(transform: (E) -> T) -> T &#123;
     return transform(element)
     &#125;
 &#125;

//instance已经被决议成TransformB<String>
let instance = Transform(element: "1") 

// 模仿写法
let result = instance.foo&#123;$0&#125;.foo&#123;true&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这14个类型变量分别代表以下的类型：</p>
















































































<table><thead><tr><th><strong>类型变量</strong></th><th><strong>说明</strong></th><th><strong>可等价于</strong></th></tr></thead><tbody><tr><td>T0</td><td>Instance的类型</td><td>Transform<String></td></tr><tr><td>T1</td><td>第一个foo函数的类型</td><td>((String) -> $T3) -> TransformB<$T3></td></tr><tr><td>T2</td><td>第一个foo函数transform的入参（E）</td><td>String</td></tr><tr><td>T3</td><td>第一个foo函数transform的出参（T)</td><td></td></tr><tr><td>T4</td><td>第一个foo函数transform的类型</td><td>($T2) -> $T3</td></tr><tr><td>T5</td><td>第一个闭包&#123;$0&#125;Tuple element $0的类型</td><td></td></tr><tr><td>T6</td><td>第一个闭包的结果</td><td></td></tr><tr><td>T7</td><td>第一个foo函数的结果</td><td>TransformB<$T3></td></tr><tr><td>T8</td><td>第二个foo函数的类型</td><td>(($T3) -> $T10) -> $T10</td></tr><tr><td>T9</td><td>第二个foo函数transform的入参（E）</td><td>$T3</td></tr><tr><td>T10</td><td>第二个foo函数transform的出参（T)</td><td></td></tr><tr><td>T11</td><td>第二个foo函数transform的类型</td><td>($T3) -> $T10</td></tr><tr><td>T12</td><td>第二个闭包的结果</td><td></td></tr><tr><td>T13</td><td>第二个foo的结果</td><td>$T10</td></tr></tbody></table>
<p>可以看出，仅一个表达式中所产生的类型变量就有14个，主要是因为一个闭包所产生的的类型变量就很多。这里可能有人会疑问，闭包的类型难道不直接是transform参数类型么？其实不然，闭包本身的类型本质上是由闭包语法中的类型指定的（比如 &#123; (str: String) -> Bool in ..... &#125;) ，但是在此例中，因为表达式足够简单，我们省略了闭包类型的显式指定，所以这里会产生相对应的类型变量，因为它是未被决议的。</p>
<p><strong>类型决议结果</strong></p>
<p>因为求解过程比较复杂，让我们先直接跳到结果部分，对生成的结果有个预期，之后带着结果去看过程，会比较清晰。求解结果如下：</p>
















































































<table><thead><tr><th><strong>类型变量</strong></th><th><strong>说明</strong></th><th><strong>决议结果</strong></th></tr></thead><tbody><tr><td>T0</td><td>Instance的类型</td><td>Transform<String></td></tr><tr><td>T1</td><td>第一个foo函数的类型</td><td>((String) -> ()) -> TransformB<()></td></tr><tr><td>T2</td><td>第一个transform的入参（E）</td><td>String</td></tr><tr><td>T3</td><td>第一个transform的出参（T)</td><td>()</td></tr><tr><td>T4</td><td>第一个transform的类型</td><td>(String) -> ()</td></tr><tr><td>T5</td><td>Tuple element $0的类型</td><td>String</td></tr><tr><td>T6</td><td>第一个闭包的结果</td><td>()</td></tr><tr><td>T7</td><td>第一个foo函数的结果</td><td>TransformB<()></td></tr><tr><td>T8</td><td>第二个foo函数的类型</td><td>(() -> Bool) -> Bool</td></tr><tr><td>T9</td><td>第二个transform的入参（E）</td><td>()</td></tr><tr><td>T10</td><td>第二个transform的出参（T)</td><td>Bool</td></tr><tr><td>T11</td><td>第二个transform的类型</td><td>() -> Bool</td></tr><tr><td>T12</td><td>第二个闭包的结果</td><td>Bool</td></tr><tr><td>T13</td><td>第二个foo的结果</td><td>Bool</td></tr></tbody></table>
<p>可以看到，有大量类型都被决议成了（），这里一定存在着某些问题，现在，让我们对log中求解过程做分析。</p>
<p><strong>求解过程Log解析</strong></p>
<p>以下是Log中求解的过程（已简化）</p>
<pre><code class="copyable">($T4 involves_type_vars bindings=&#123;(subtypes of) (String) -> $T3&#125;)
  (attempting type variable $T4 := (String) -> $T3
    ($T5 involves_type_vars bindings=&#123;(supertypes of) String&#125;)
    ($T11 involves_type_vars bindings=&#123;(subtypes of) ($T3) -> $T10&#125;)
    (attempting type variable $T5 := String
      ($T6 involves_type_vars bindings=&#123;(supertypes of) String; (supertypes of) ()&#125;)
      ($T11 involves_type_vars bindings=&#123;(subtypes of) ($T3) -> $T10&#125;)
      Initial bindings: $T6 := String, $T6 := ()
      (attempting type variable $T6 := String
        ($T3 potentially_incomplete fully_bound involves_type_vars bindings=&#123;(supertypes of) String&#125;)
        ($T11 involves_type_vars bindings=&#123;(subtypes of) ($T3) -> $T10&#125;)
        (attempting type variable $T11 := ($T3) -> $T10
          (increasing score due to function conversion)
          ($T3 potentially_incomplete bindings=&#123;(supertypes of) String; (subtypes of) ()&#125;)
          Initial bindings: $T3 := String, $T3 := ()
          (attempting type variable $T3 := String
            (failed constraint $T3 subtype () 
          )
          (attempting type variable $T3 := ()
            (failed constraint $T6 subtype $T3 
          )
        )
      )
      (attempting type variable $T6 := ()
        (increasing score due to function conversion)
        ($T3 potentially_incomplete fully_bound involves_type_vars bindings=&#123;(supertypes of) ()&#125;)
        ($T11 involves_type_vars bindings=&#123;(subtypes of) ($T3) -> $T10&#125;)
        Initial bindings: $T11 := ($T3) -> $T10
        (attempting type variable $T11 := ($T3) -> $T10
          (increasing score due to function conversion)
          ($T3 potentially_incomplete bindings=&#123;(supertypes of) ()&#125;)
          ($T17 literal=3 involves_type_vars bindings=&#123;(subtypes of) (default from ExpressibleByBooleanLiteral) Bool&#125;)
          Initial bindings: $T3 := ()
          (attempting type variable $T3 := ()
            ($T17 literal=3 involves_type_vars bindings=&#123;(subtypes of) (default from ExpressibleByBooleanLiteral) Bool&#125;)
            Initial bindings: $T17 := Bool
            (attempting type variable $T17 := Bool
              ($T12 involves_type_vars bindings=&#123;(supertypes of) Bool; (supertypes of) ()&#125;)
              Initial bindings: $T12 := Bool, $T12 := ()
              (attempting type variable $T12 := Bool
                ($T10 potentially_incomplete bindings=&#123;(supertypes of) Bool&#125;)
                Initial bindings: $T10 := Bool
                (attempting type variable $T10 := Bool
                  (found solution 0 0 0 0 0 0 0 2 0 0 0 0 0 0)
                )
              )
              (attempting type variable $T12 := ()
                (increasing score due to function conversion)
                (solution is worse than the best solution)
              )
            )
          )
        )
      )
    )
  )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Log的表达信息有限，但可以看到求解过程就是类似Solving过程的工作机制。 在这段Log中我们可得到如下的关键信息：</p>
<p>整体求解的过程是有一次失败的，具体是决议$T3的类型，也就是transform函数的T类型。从而回溯导致$T6为String时失败。</p>
<p>这一点也是直接导致整个问题的关键，第一个闭包结果，以及transform函数的出参T都被决议成了<code>()</code>类型。那么，就让我们先来看看为何导致T3类型决议的失败。</p>
<pre><code class="copyable">(attempting type variable $T3 := String
     (failed constraint $T3 subtype () 
)

(attempting type variable $T3 := ()
     (failed constraint $T6 subtype $T3 
  )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，尝试T3作为String类型，发现不满足 <strong>T3 subtype ()</strong>，这里A subtype B的意思是 A等于B或者A是B的子类型。 那么<code>()</code>类型，也就是Void类型不能作为String的父类型。那么到底在哪里要求" T3 subtype <code>()</code>"呢？ 这里确实也迷惑了很久，后来经过猜测，发现这条约束已经在Log中有体现。但是不是在求解过程中，是在生成约束的阶段：</p>
<pre><code class="copyable">Active Constraints:
  $T4 arg conv (String) -> $T3 
  $T11 arg conv ($T3) -> $T10 

Inactive Constraints:
  $T4 closure can default to ($T5) -> $T6 
  $T11 closure can default to () -> $T12
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>$T11 arg conv ($T3) -> $T10</strong></li>
<li><strong>$T11 closure can default to () -> $T12</strong></li>
</ul>
<p>在这里我们发现 $T11 can default to () -> $T12， 并且$T11 等价于（$T3) -> $T10，综合这两个约束，可以得出 <strong>T3 subtype ()</strong> 的要求。</p>
<p>第一条约束失败后，继续尝试T3为Void类型，发现不满足"T6 subtype T3"，这里很好理解，T6的类型是闭包的返回结果，T3代表参数签名中的E->T中的T类型，所以T6需要满足是T3或者T3的子类。此时T6在前面已经尝试作为String类型，而String不是Void的子类型，此次求解失败。</p>
<p>回溯到T6，在T6尝试决议String失败后，T6尝试决议成 <code>()</code> 类型，我们发现之后的过程没有遇到失败的情况，最后决议完成。最后得出Log中体现的结果。</p>
<blockquote>
<p>可能有人在Log中发现，<strong>Solution: 0 0 0 0 0 0 0 0 0 0 0 0 0 0</strong> 是什么？
<br>这个Solution的分数可以简单理解成在求解过程中的“妥协”值，这14个0分别代表14种情况，每当对应的情况发生时，该标志位就+1分。最后Type-Checker会进行对比，最好的求解分数就是14个0。可以看到这个case中最终分数其实是 「 0 0 0 0 0 0 0 2 0 0 0 0 0 0」，是因为进行了两次函数类型的转换。</p>
</blockquote>
<p>到这里，从Log中来看，我们可以大致猜测出几个结论：</p>
<ol>
<li>问题的重点就是在T3和T6的判断上，和我们在表象上看到的现象一致，也就是问题的关键在<code>&#123;$0&#125;</code>返回值的类型。我们可以看出求解过程已经将T3和T6尝试过判断为String类型，可是由于<code>()</code>类型的约束干扰，最后没有成功。</li>
<li>最终的决议结果并不是最完美的，期间经历了两次函数类型转换，而且闭包的实际结果是可以被隐式转换成<code>()</code>类型的。</li>
</ol>
<p>种种线索都指向了一个问题，那就是：</p>
<p><strong><code>()</code>类型是产生的根源在哪里？</strong></p>
<h2 data-id="heading-12">源码寻找答案</h2>
<p>既然在Log中的信息已经挖掘完毕，那么我们就去源代码中寻找答案。我们发现，求解过程中的很多约束限制导致了类型被判断为Void，那么我们去生成约束的地方寻找线索。Swift类型推断的源码在语义分析阶段，文件夹位置在<a href="https://github.com/apple/swift/tree/main/lib/Sema" target="_blank" rel="nofollow noopener noreferrer">lib/Sema</a>中。（<del>经过了头秃式的挖掘</del>）果然，在生成closure闭包约束的地方找到了关键信息。</p>
<p>在遍历AST结构时，我们看到<code>visitClosureExpr</code>的实现中，调用了一个叫<a href="https://github.com/apple/swift/blob/main/lib/Sema/CSGen.cpp#L1997" target="_blank" rel="nofollow noopener noreferrer"><code>inferClosureType</code></a>的函数。这个函数的作用就是生成这个闭包的类型。函数的简化版源码如下：</p>
<pre><code class="copyable">FunctionType *inferClosureType(ClosureExpr *closure) &#123;

   SmallVector<AnyFunctionType::Param, 4> closureParams;

   // 添加参数列表
   if (auto *paramList = closure->getParameters()) &#123;
    for (unsigned i = 0, n = paramList->size(); i != n; ++i) &#123;

     // ..... 省略
     closureParams.push_back(param->toFunctionParam(externalType));
    &#125;
   &#125;

   auto extInfo = CS.closureEffects(closure);

   // Closure expressions always have function type. In cases where a
   // parameter or return type is omitted, a fresh type variable is used to
   // stand in for that parameter or return type, allowing it to be inferred
   // from context.
   
   // 闭包表达式总是有一个对应的函数类型，在参数或者返回类型被省略的时候，会创建一个新的类型变量
   Type resultTy = [&] &#123;

   // 如果有显式的return类型
    if (closure->hasExplicitResultType()) &#123;
     const auto resolvedTy = ......
     if (resolvedTy)
      return resolvedTy;
    &#125;

    // If no return type was specified, create a fresh type
    // variable for it and mark it as possible hole.

    // 如果没有明确指定return类型，创建新的typeVariable
    return Type(CS.createTypeVariable(
      CS.getConstraintLocator(closure, ConstraintLocator::ClosureResult),
      shouldTypeCheckInEnclosingExpression(closure) ? 0
                             : TVO_CanBindToHole));

   &#125;();

    // 调用AST模块的函数类型判断
    FunctionType* f = FunctionType::get(closureParams, resultTy, extInfo);
    return f;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从这段源码中我们了解，如果没有显式指定闭包的参数类型以及返回类型，约束系统会生成类型变量代替还未被确定的变量。而闭包的参数变量，是由AST模块的功能函数判断的。</p>
<p>换句话说，如果没有标明参数列表，则闭包等价于没有参数的函数，也就是说参数类型是<code>()</code> ! 而如果闭包中如果写了<code>_ in</code>，即使忽略了参数的具体值，也是会被当做有参数的，会生成一个类型变量，同样地，如果使用了<code>$0</code>，也会被当做有参数。</p>
<p>而闭包的结果参数则不同，可以看到结果参数是由resultTy代码块去决定的，其中注释也明确说明了会给省略return的闭包新建一个TypeVariable。</p>
<p>下面的图示表明了不同闭包的省略写法，对类型推断产生变量造成的影响：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd392f13e078457f9f20db1f5a50e5be~tplv-k3u1fbpfcp-watermark.image" alt="33.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>回到case中上，这次我们知道第一个源码说明了为何第二个闭包会被推断成() -> T12类型，也就是生成了 <strong>$T11 closure can default to () -> $T12</strong> 这个约束，进而引入了<code>()</code>类型。我们似乎发现了问题的直接原因所在。</p>
<p>这里其实还有一个问题，如果根据这个结论，<code>&#123; $0 &#125;</code> 和 <code>&#123; return $0 &#125;</code>生成的类型变量数是一样的，但是根据前文的尝试，我们发现,</p>
<p><strong><code>instance.foo&#123;return $0&#125;.foo&#123; true &#125;</code></strong></p>
<p>这样的写法会编译不过，这是为什么呢？</p>
<p>原因在第二个关键代码：</p>
<pre><code class="copyable">ConstraintSystem::TypeMatchResult

ConstraintSystem::matchTypes(Type type1, Type type2, ConstraintKind kind,
               TypeMatchOptions flags,
               ConstraintLocatorBuilder locator) &#123;
  //.........

 if (auto elt = locator.last()) &#123;
  if (kind >= ConstraintKind::Subtype &&
    (type1->isUninhabited() || type2->isVoid())) &#123;

   // A conversion from closure body type to its signature result type.
   if (auto resultElt = elt->getAs<LocatorPathElt::ClosureBody>()) &#123;

    // If a single statement closure has explicit `return` let's
    // forbid conversion to `Void` and report an error instead to
    // honor user's intent.

    if (type1->isUninhabited() || !resultElt->hasExplicitReturn() ) &#123;
     increaseScore(SK_FunctionConversion);
     return getTypeMatchSuccess();
    &#125;
   &#125;
  &#125;
 &#125;

 // .......
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码是在solving求解过程中进行类型匹配的地方，可以看到，如果闭包是单语句表达式，<strong>且</strong>省略了<code>return</code>关键字，那么type2（目标类型） 就可以被转换为<code>()</code>类型。并且increase了分数，原因是FunctionConversion函数类型转换。这个现象在Log中也有体现。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce84a592625a4aa286fa3b6b7816829f~tplv-k3u1fbpfcp-watermark.image" alt="34.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至此，整个问题大概有了结论。我们可以做一个总结，问题产生的原因如下：</p>
<p>对于 <code>let result = instance.foo&#123;$0&#125;.foo&#123;true&#125;</code></p>
<ol>
<li>因为第二个闭包既没有写出参数列表，又没有使用匿名变量，所以闭包被判断成了<code>() -> T0</code>类型。</li>
<li>在判断第一个闭包的返回值类型时，String类型不满足 <code>()</code> 类型的相关约束，所以类型决议失败。</li>
<li>因为第一个闭包省略了<code>return</code>关键字，所以闭包返回值类型可以被决议成<code>()</code> 类型，但此时编译器做了妥协，并不是最佳解法。</li>
</ol>
<p>现在再来回顾之前几种闭包写法，似乎思路清晰了很多：</p>
<pre><code class="copyable">//编译通过， 但现象不符合预期
instance.foo&#123;$0&#125;.foo&#123; true &#125; 
instance.foo&#123;e in e&#125;.foo&#123;return true &#125; 
instance.foo&#123;$0&#125;.foo&#123; return true &#125; 

//编译不过
instance.foo&#123;e in return e&#125;.foo&#123; true &#125;
instance.foo&#123;e in return e&#125;.foo&#123; return true &#125;
instance.foo&#123;return $0&#125;.foo&#123; true &#125;

//编译通过，现象符合预期
instance.foo&#123;$0&#125;.foo&#123; _ in true &#125;
instance.foo&#123;return $0&#125;.foo&#123; _ in true &#125;
instance.foo&#123;e in return e&#125;.foo&#123; _ in true &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以对以上三种现象做原因归类，在两个闭包都是单个语句表达式的情况下：</p>
<ul>
<li>
<p>如果第二个闭包标明参数，那么整个表达式逻辑符合预期</p>
</li>
<li>
<p>如果第二个闭包不写参数：</p>
<ul>
<li>第一个闭包有return语句，那么编译不过</li>
<li>第一个闭包没有return语句，那么可以编译通过，但是实际运行逻辑会不符合预期。</li>
</ul>
</li>
</ul>
<p>让我们从Log中验证上述逻辑：</p>
<p>首先是逻辑正确的 <code>let result = instance.foo &#123; $0 &#125;.foo &#123; _ in true &#125;</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db7a9c8b11a34af5acbb525a0e461a7f~tplv-k3u1fbpfcp-watermark.image" alt="35.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，在生成类型变量阶段会多了一个T12变量，这个变量指的就是 <code>_ in</code> 中的 <code>_</code> ，也就是被省略的参数。从而没有产生<code>()</code>类型。而后在解决约束的过程中，没有了<code>()</code>类型的限制，自然而然就被决议成了String类型。</p>
<p>第二个是有return语句的编译失败的闭包：<code>let result = instance.foo &#123; return $0 &#125;.foo &#123; true &#125;</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/268786cd99df4cb6aaffc4116791ee2e~tplv-k3u1fbpfcp-watermark.image" alt="36.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到生成的变量情况，和源表达式是一致的。但是在过程中稍有不同：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7d9e3653dd64c3ebe05f7874279e5a4~tplv-k3u1fbpfcp-watermark.image" alt="37.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在尝试把T6当做<code>()</code>的时候，因为第一个闭包显式的写了return关键字，所以根据第二段源码逻辑，不能把闭包结果转换为<code>()</code>类型，T6决议失败，随之整个决议过程失败。</p>
<h2 data-id="heading-13">问题总结</h2>
<p>到这里，我们可以总结下所遇到的所有问题和疑惑：</p>
<p>问：<strong>为什么第二个闭包的写法会对第一个闭包的逻辑有影响？</strong></p>
<p>答：因为Swift类型推断是以整个表达式Scope为求解范围的，所以是整体决议，本质上没有前后的区别。</p>
<p><br>问： <strong>为什么<code>&#123;$0&#125;</code>闭包的出参会被推断成<code>()</code>类型？</strong></p>
<p>答：在Swift类型推断过程中，因为后一个闭包省略了参数，入参被直接判断为<code>()</code>类型，从而在求解过程中对前一个闭包的出参类型产生了影响。</p>
<p><br>问：<strong>为什么后一个闭包加了<code>_ in</code>结果就符合预期了？</strong></p>
<p>答：<code>_ in</code> 的作用代表了后一个闭包是有参数的，在类型判断的过程中会结合此参数进行整体判断，从而求解出符合预期的结果。</p>
<p><br>问：<strong>为什么把两个调用语句拆开后，第二个语句会编不过？</strong></p>
<p>答：Swift类型推断是以单个表达式语句作为求解范围，和第一个问题不同，第一个foo调用已经得到了TransformB的类型，但因为第二个闭包省略了参数，所以第二个闭包的入参<code>()</code>和已经决议完成的第一个闭包的出参String有冲突，所以编译器报错 "ambiguous"</p>
<h1 data-id="heading-14">总结及后续</h1>
<h2 data-id="heading-15">总结</h2>
<p>Swift的类型推断是个非常复杂的过程，相信各位在编码过程中也遇到过各种各样的编译报错，而在编码时，尤其是像RxSwift这样连续闭包调用的情况，一般我们都是在编译不过时，直接通过编译器的诊断去自动修正，就比如提示插入<code>_ in</code>这样的情况，而没有探究背后的过程。如果遇到像本文的场景，可能会遇到意想不到的逻辑错误。可能有人说本文的Rxswift的case不常见，其实有个更容易理解的case，小伙伴们可以动手试试：</p>
<pre><code class="copyable">struct Data &#123;&#125;

let arr = [1, 2, nil, 3]

let mappedArr = arr.compactMap &#123; $0 &#125;.map &#123; Data() &#125; // result: &#123; Data, Data, Data, Data &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然编译器会报警告，但是在实际大型项目中，这类警告很容易被忽略掉，而且产生的现象也十分让人疑惑。</p>
<p>那可能有的小伙伴们会问，怎样避免这类隐藏的坑呢？对此，貌似没有什么好的方法，总不能把所有的闭包参数及结果类型全部写出来，只能说注意编译器的所有可疑警告。而且，我始终认为这似乎是编译器为了满足闭包的各类语法糖，在类型求解策略过程中的一个边缘的bad case，所以我给Swift<a href="https://bugs.swift.org/browse/SR-14401" target="_blank" rel="nofollow noopener noreferrer">提了个bug</a>，想看看编译器开发者的回答。目前还未得到很多合理的解释。</p>
<h2 data-id="heading-16">探究心得</h2>
<p>此次对部分源码的研究只是针对遇到的问题找到一些源码关键点，对自己的疑惑得到求证。其相对于整个Swift Type Inference可以说冰山一角，比如类型约束具体都有什么类型？Constraint Graph是什么？具体的求解Step逻辑是什么？泛型类型是怎么推断的？它们同样有很大的价值去深究。</p>
<p>此篇文章很长，感谢阅读。整篇文章的顺序是本人真实的探究过程，从业务场景编码中发现问题，直到探究从未了解过的Swift类型推断的实现，不断调试运行，找到关键线索，到后来给Swift项目提问题，寻求官方帮助，整个过程还是有些收获。在日常开发遇到问题时，如果有精力的话，建议保持刨根问底的态度，不仅问题本身，其中寻找问题、思考的过程也会带来很大收获，尤其是针对开源项目，比如Swift标准库、编译器以及相关工程，非常值得研究。</p>
<h2 data-id="heading-17">加入我们</h2>
<p>飞书-字节跳动旗下企业协作平台，集视频会议、在线文档、移动办公、协同软件的一站式企业沟通协作平台。目前飞书业务正在飞速发展中，<strong>在北京、深圳等城市都有研发中心，前端、移动端、Rust、服务端、测试、产品等职位都有足够的 HC</strong>，期待你的加入，和我们一起做有挑战的事情（请戳链接：<a href="https://future.feishu.cn/recruit" target="_blank" rel="nofollow noopener noreferrer">future.feishu.cn/recruit</a>）。</p>
<p>我们也欢迎和飞书的同学一起进行技术问题的交流，有兴趣的同学请点击<a href="https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=850v2629-a47c-4f2c-ae70-04de11f260e2" target="_blank" rel="nofollow noopener noreferrer">飞书技术交流群</a>入群交流。</p></div>  
</div>
            