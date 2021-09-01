
---
title: '热爱函数式的你，句句纯正的 Haskell【函数篇】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3328'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 23:19:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=3328'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">函数本质</h2>
<blockquote>
<p><strong>Haskell 里变量的值在绑定后不会改变，所有变量一定意义上可以理解为定值。</strong></p>
<p>无论如何，定义过的值是没法再改变的。</p>
</blockquote>
<p>Haskell 值与函数是统一的，函数只是需要其他参数输入的值。如果定义的是函数，那么这个函数的行为在运行过程中也是不会改变的，<strong>对于某一个特定的输入返回的结果总是确定的，这样的函数为纯函数。</strong></p>
<p>有人觉得不改内存状态的想法听上去很荒诞，甚至觉得这样是没有办法做计算的。其实，这两种想法都是错误的。不改变内存状态自有道理，而其它编程语言可以完成的工作，Haskell 一样可以完成。</p>
<p>再三强调，在 Haskell 中，<strong>函数与值没有本质的区别</strong>，它可以是单一的定值，也可以是任意两个函数间的映射；</p>
<p>实际上，在 Haskell 世界里，所有的运算符号都可以被看做是函数，如加号 + 是一个需要两个参数的函数。</p>
<pre><code class="copyable">Prelude> (+)5 7
12
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">函数定义</h2>
<p>直接上干货~</p>
<p>实现：f(x) = 4x+ 1</p>
<pre><code class="copyable">Prelude> f1(x)=4*x + 1
Prelude> f1 4
17
Prelude> :t f1
f1 :: Num a => a -> a
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再比如实现：f(x,y) = 4x+ 5y+ 1，</p>
<p>我们可以设想到这个函数的类型是：</p>
<pre><code class="copyable">f2 :: Num a => (a, a) -> a
<span class="copy-code-btn">复制代码</span></code></pre>
<p>验证一下：</p>
<pre><code class="copyable">Prelude> f2(x,y)=4*x+5*y+1
Prelude> f2(4,3)
32
Prelude> :t f2
f2 :: Num a => (a, a) -> a
<span class="copy-code-btn">复制代码</span></code></pre>
<p>确实如此；b(￣▽￣)d</p>
<p>Haskell 中定义的函数的大致格式是这样的：</p>
<pre><code class="copyable">// 定义方式 1

函数名 (参数1,参数2,...) = 函数体

// 定义方式 2

函数名 参数1 参数2.. =函数体

// 类型

函数名 :: 参数1的类型->参数2的类型->...->结果类型
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说这么多，不如在编译器中感受感受：</p>
<pre><code class="copyable">Prelude> f3 x y z=3*x+2*y-z
Prelude> f3 1 2 3
4
Prelude> :t f3
f3 :: Num a => a -> a -> a -> a
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>我们惊人的发现，从定义方式 1 到 定义方式 2 的过程，就是柯里化的过程！</strong></p>
<h2 data-id="heading-2">λ表达式</h2>
<p>Haskell 还有另外一种书写函数的格式，即 λ 表达式；</p>
<pre><code class="copyable">// 定义方式 3

函数名= (\参数1 -> \参数2 -> ... ->函数体)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="copyable">Prelude> f4= (\x -> \y -> x*y)
Prelude> f4 2 3
6

Prelude> f5 =(\x -> \y->4*x+5*y+1)
Prelude> f5 2 3
24
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用一些高阶函数时，如果不想定义新函数，可以使用 λ 表达式来定义这个函数：</p>
<pre><code class="copyable">Prelude> map(\x->2*x+7)[1..10]
[9,11,13,15,17,19,21,23,25,27]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>\x -> 2*x+7 是一个没有名字的匿名函数，在 Haskell 中，通常用 λ 表达式来构造匿名函数；</p>
<h2 data-id="heading-3">阶段小结</h2>
<p>小结中，我们再来回归三种定义函数的方式：</p>
<pre><code class="copyable">// 方式 1：

f2(x,y)=4*x+5*y+1

// 方式 2：

f3 x y z=3*x+2*y-z

// 方式 3：

f4= (\x -> \y -> x*y)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数作为 Haskell 基础之基础，牢记 3 种函数定义的方式则是基础之基础之基础。</p>
<p>第 1 种方式到 第 2 种方式是柯里化思想的体现。柯里化如此自然，就像呼吸一般~还有 λ 表达式，是实现匿名函数的有效方式！！</p>
<p>以上，真的要在编译器中敲一敲才会有更多体验。看看不同语言对于函数申明及调用的不同实现，体会函数式编程参数在函数中的输入、传递 ......</p>
<blockquote>
<p>我是掘金安东尼，输出暴露输入，技术洞见生活，再会~</p>
</blockquote></div>  
</div>
            