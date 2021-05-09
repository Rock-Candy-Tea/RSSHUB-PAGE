
---
title: '从 JS 执行机制理解变量提升等特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c05d51be11d4feeaa0781addf049fc8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 08 May 2021 19:27:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c05d51be11d4feeaa0781addf049fc8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>对于 Javascript 的执行机制的认识还比较浅，恰好最近有看到<a href="https://time.geekbang.org/column/article/119046" target="_blank" rel="nofollow noopener noreferrer">李兵老师浏览器的课程(得付费哟)</a>，了解了 JavaScript 的执行机制，对于变量提升，暂时性死区的理解能够加深，也能够初步复刻出代码的执行。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">showName()
<span class="hljs-built_in">console</span>.log(myName)
<span class="hljs-keyword">var</span> myName = <span class="hljs-string">'小林别闹'</span>
<span class="hljs-built_in">console</span>.log(yourName)
<span class="hljs-keyword">let</span> yourName = <span class="hljs-string">'小林加油'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showName</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'函数showName被执行'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c05d51be11d4feeaa0781addf049fc8~tplv-k3u1fbpfcp-watermark.image" alt="image-20210508200203787.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果您也对上边代码的运行结果感到疑惑或者感兴趣，那么请阅读下去吧</p>
<h2 data-id="heading-0">1.编译</h2>
<p>首先可以明确，<strong>代码先编译再执行</strong></p>
<p>编译的过程比较复杂，俺暂时也不是很清楚，感兴趣的朋友可以去学一下，然后告诉我(笑)，引用一段李兵老师的话</p>
<blockquote>
<p>编译先是生成字节码，然后解释器可以直接执行字节码，输出结果。 但是通常 Javascript 还有个编译器，会把那些频繁执行的字节码编译为二进制，这样那些经常被运行的函数就可以快速执行了，通常又把这种解释器和编译器混合使用的技术称为 JIT</p>
</blockquote>
<p>我们可以暂时将这段代码的<strong>编译结果</strong>可以分为两部分：<strong>执行上下文</strong>和<strong>可执行代码</strong></p>
<p>另外 <code>var myName = '小林别闹'</code> 这个语句就可以分为声明和赋值两部分</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> myName    <span class="hljs-comment">//声明部分</span>
myName = <span class="hljs-string">'小林别闹'</span>  <span class="hljs-comment">//赋值部分</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">1.1执行上下文</h3>
<p>执行上下文有三种(开始学习的时候误以为块作用域都有执行上下文)：</p>
<ul>
<li>
<p>全局执行上下文：只有一个，程序首次运行时创建，一直压在调用栈的底部，直到程序运行结束</p>
</li>
<li>
<p>函数执行上下文：函数被调用时创建，每次调用都会为该函数创建一个新的执行上下文，<strong>不管这个函数是不是重复调用</strong></p>
</li>
<li>
<p>Eval 函数执行上下文：运行<code>eval</code>函数中的代码时创建的执行上下文，少用且不建议使用，俺也不太清楚</p>
</li>
</ul>
<p><strong>执行上下文可以暂时理解为包括****变量环境</strong>和<strong>词法环境</strong>两个对象</p>
<p>文章开头的代码编译后的执行上下文大致如图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cde23c3c84b402d85807e58afb5722c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210508201124664.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编译的时候，JavaScript 引擎把由 <code>var</code> 声明的变量和函数的<strong>声明部分</strong>，提到了<strong>变量环境对象中</strong>，给定默认值 <code>undefined</code>。JavaScript 引擎发现了一个通过 function 定义的函数，所以它将函数定义存储到堆 (HEAP）中，并在环境对象中创建一个 showName 的属性</p>
<p>将由 <code>let</code> 和 <code>const</code> 声明的变量的声明部分提到了<strong>词法环境对象</strong>，<strong>词法环境由一个栈结构管理</strong>。同样给定默认值 <code>undefined</code>。当执行上下文没有切换时，当遇到新的<strong>块作用域</strong>，用 <code>let</code> 和 <code>const</code> 声明的变量会创建新的词法环境。新创建的词法环境会压入这个栈中，并伴随相关语句的结束弹出销毁。</p>
<h3 data-id="heading-2">1.2可执行代码</h3>
<p>编译完后就是执行了，是一行一行的执行的哦，执行代码大致长这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">showName()<span class="hljs-comment">//函数声明提升到变量环境中了，所以是可以执行的，输出那句'函数showName被执行'</span>
<span class="hljs-built_in">console</span>.log(myname)<span class="hljs-comment">//var 定义的变量也提升到变量环境中，并默认为undefined,所以输出undefined</span>
myname = <span class="hljs-string">'小林别闹'</span><span class="hljs-comment">//将变量环境中myname的值改成 "小林别闹"</span>
<span class="hljs-built_in">console</span>.log(yourName)<span class="hljs-comment">//let 定义的变量再词法环境中，默认为undefined,但是javascript不允许 let 定义的变量在声明前使用，所以会报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样对于文章开头代码的执行结果是不是清楚了呢</p>
<h2 data-id="heading-3">2.调用栈</h2>
<p><strong>函数只有在调用的时候才会被编译</strong>。调用一个函数就会有一个新的执行上下文，通过一个栈结构来管理这些上下文，进而管理函数之间的调用关系。这个栈就叫调用栈，<strong>文章开头的代码其实就有两个执行上下文</strong>。<code>showName</code> 函数执行完毕，该执行上下文就从调用栈内出来。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e88258beb3a4498c9c4fe1e9cce8e5a1~tplv-k3u1fbpfcp-watermark.image" alt="image-20210508203339901.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">2.1栈溢出</h3>
<p>栈的大小是有限的，超过栈的大小就会造成栈溢出，比如说递归调用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// function foo()&#123;</span>
<span class="hljs-comment">//    return setTimeout(foo, 0);</span>
<span class="hljs-comment">//&#125;</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> foo();
&#125;
foo()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91559845e5bd468cae7631125c3f9a7e~tplv-k3u1fbpfcp-watermark.image" alt="image-20210508212633663.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为啥 <code>setTimeout</code> 能够避免栈溢出呢，这是因为 <code>setTimeout</code> 是异步的，会被交给 Web API，时间触发时，回调函数被送到任务队列，事件循环不断地监视任务队列，并按它们排队的顺序一次处理一个回调。每当调用堆栈为空时，事件循环获取回调并将其放入堆栈中进行处理。请记住，<strong>如果调用堆栈不是空的，则事件循环不会将任何回调推入堆栈</strong>。</p>
<p>还可以，设置一个变量depth用来表示调用的层数，当超过一定层数时，则终止递归</p>
<h2 data-id="heading-5">3.作用域链</h2>
<p>在编写代码的时候，如果你使用了一个在当前作用域中不存在的变量，这时 JavaScript 引擎就需要按照<strong>作用域链</strong>在其他作用域中查找该变量</p>
<p>这是因为 JavaScript 语言的作用域链是由词法作用域决定的，而词法作用域是由代码结构来确定的，也就是代码中函数<strong>声明</strong>的位置来决定的</p>
<p><strong>在执行上下文中寻找变量按照的是先词法环境，再变量环境</strong>，调用栈的顺序就是函数的调用顺序，执行上下文之间，查找变量就沿着作用域链来查找，作用域的顺序和调用顺序无关，仅和<strong>声明</strong>顺序有关</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a = <span class="hljs-string">'A'</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-string">"B"</span>
<span class="hljs-keyword">let</span> c = <span class="hljs-string">"C"</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log( a ); 
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-string">"a"</span>;
    foo();
    <span class="hljs-built_in">console</span>.log(c)
    <span class="hljs-keyword">let</span> c = <span class="hljs-string">"c"</span> 
&#125;
bar();

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ff48c3eb0004262b2b1eeb546a56c84~tplv-k3u1fbpfcp-watermark.image" alt="image-20210508204705599.png" loading="lazy" referrerpolicy="no-referrer">
<code>foo</code> 和 <code>bar</code> 函数都声明在全局作用域，它们沿着作用域链找变量的时候当然就找到了全局执行上下文这里了，但是在<code>bar</code> 函数里面通过 <code>let</code> 声明了 <code>c</code> 所以 <code>bar</code> 找到的是自己的词法环境里面的 <code>c</code> 但是在赋值前调用，Javascript 引擎不允许，所以报错了。下面的图应该画错了(哭)，bar函数执行上下文的词法环境里面，<code>c</code> 应该还是 <code>undefined</code> ,因为报错了，下面的代码应该不会执行下去了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2665330ecb6d446aad14938c665522d7~tplv-k3u1fbpfcp-watermark.image" alt="image-20210508203339901.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>顺带提一下，执行上下文里边东西挺多的，可以参考下图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6a02fdf6690453da14a77e546dd25d2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210508213439494.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>outer就是一个外部引用，用来指向外部的执行上下，这个<strong>外部是沿着作用域链</strong>的，和调用没关系哦</p>
<p>this 应该不陌生了，非严格模式下，普通函数中的this都是window,当然你可以这样记住：this总是指向调用者，咱们的箭头函数都没有this,都是外部的</p>
<p>参考：</p>
<p><a href="https://juejin.cn/post/6844903890270289928#heading-15" target="_blank">8个问题看你是否真的懂 JS</a></p>
<p><a href="https://time.geekbang.org/column/article/119046" target="_blank" rel="nofollow noopener noreferrer">浏览器工作原理与实践</a></p></div>  
</div>
            