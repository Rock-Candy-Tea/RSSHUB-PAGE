
---
title: 'JavaScript之执行上下文栈'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9117'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 05:24:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=9117'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">顺序执行？</h4>
<p>我们先来看下面这两段代码</p>
<pre><code class="copyable">var foo = function () &#123;

    console.log('foo1');

&#125;

foo();  // foo1

var foo = function () &#123;

    console.log('foo2');

&#125;

foo(); // foo2
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">function foo() &#123;

    console.log('foo1');

&#125;

foo();  // foo2

function foo() &#123;

    console.log('foo2');

&#125;


foo(); // foo2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面这两段代码，我们可以看出很明显的区别，打印出来的结果也不一样。刷过面试题的人都知道这是因为 JavaScript 引擎并非一行一行地分析执行。当执行一行代码的时候，会进行一个“准备工作”，比如第一个例子中的变量提升，和第二个例子中的函数提升。</p>
<p>但是本文真正想让大家思考的是：这个“一段一段”的“段”究竟是怎么划分的呢？</p>
<p>到底 JavaScript 引擎遇到一段怎么样的代码才会做“准备工作”呢？</p>
<h4 data-id="heading-1">可执行代码</h4>
<p>这就要说到 JavaScript 的可执行（executable code）的类型有哪些了？</p>
<p>其实很简单，就三种：全局代码、函数代码、eval代码</p>
<p>举个例子，当执行到一个函数的时候，就会进行准备工作，这里的“准备工作”，让我们用个更专业一点的说法，就叫做"执行上下文（execution context）"。</p>
<p>执行上下文的类型也分三种：</p>
<p>全局执行上下文：它做了两件事，1.创建一个全局对象，在浏览器中这个全局对象就是 window 对象。
2.将 this 指针指向这个全局对象。
一个程序只能存在一个全局执行上下文</p>
<p>函数执行上下文：每次调用函数时，都会为该函数创建一个新的执行上下文。每个函数都拥有自己的执行上下文，但是只有在函数被调用的时候才会被创建。一个程序中可以存在任意数量的函数执行上下文。每当一个新的执行上下文被创建，它都会按照特定的顺序执行一系列步骤，具体过程将在本文后面讨论。</p>
<p>Eval 执行上下文：运行在 eval 函数中的代码也获得了自己的执行上下文但由于 JavaScript 开发人员不常用 eval 函数，所以这里不讨论。</p>
<h4 data-id="heading-2">执行上下文的生命周期</h4>
<p>执行上下文的生命周期包括三个阶段：创建阶段 -> 执行阶段 -> 回收阶段</p>
<ol>
<li>创建阶段</li>
</ol>
<p>当函数被调用，但为执行任何其内部代码之前，会做以下三件事：</p>
<ul>
<li>创建变量对象：首先初始化函数的参数 arguments ，提升函数声明和变量声明。</li>
<li>创建作用域链（Scope Chain）：在执行上下文的创建阶段，作用域链是在变量对象之后创建的。作用域链本身包含对象。作用域链用于解析变量。当被要求解析变量时， JavaScript 始终从代码嵌套的最内层开始，如果内层没有找到变量，就会跳转到上一层父作用域中查找，直到找到该变量。</li>
<li>确定 this 指向：包括多种情况。</li>
</ul>
<p>在一段 JS 脚本执行之前，要先解析代码（所以说 JS 是解释执行的脚本语言），解析的时候会先创建一个全局执行上下文环境，先把代码中即将执行的变量、函数声明都拿出来。变量先暂时赋值为 undefined，函数则先声明好可使用。这一步做完了，然后再开始正式执行程序。</p>
<p>另外，一个函数在执行之前，也会创建一个函数执行上下文环境，跟全局上下文差不多，不过 函数执行上下文中会多出 this arguments 和函数的参数。
2. 执行阶段
执行变量赋值，代码执行
3. 回收阶段
执行上下文出栈等待虚拟机回收执行上下文</p>
<h4 data-id="heading-3">执行上下文栈</h4>
<p>我们写的函数多了，要如何管理那么多的执行上下文呢？</p>
<p>所以 JavaScript 引擎创建了执行上下文栈 （Execution context stack，ECS）来管理执行上下文</p>
<p>为了模拟执行上下文的行为，让我们定义执行上下文栈是一个数组：</p>
<pre><code class="copyable">ECStack = [];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>试想当 JavaScript 开始要解释执行代码的时候，最先遇到的就是全局代码，所以初始化的时候首先就会向执行上下文栈压入一个全局执行上下文，我们用 globalContext 表示它，并且只有当整个应用程序结束的时候，ECStack 才会被清空，所以程序结束之前， ECStack 最底部永远有个 globalContext：</p>
<pre><code class="copyable">ECStack = [
    globalContext
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当执行一个函数的时候，就会创建一个执行上下文，并且压入执行上下文栈，当函数执行完毕的时候，就会将函数的执行上下文从栈中弹出。知道了这样的工作原理，让我们来看看如何处理上面这段代码：</p>
<pre><code class="copyable">// 伪代码

// fun1()
ECStack.push(<fun1> functionContext);

// fun1中竟然调用了fun2，还要创建fun2的执行上下文
ECStack.push(<fun2> functionContext);

// 擦，fun2还调用了fun3！
ECStack.push(<fun3> functionContext);

// fun3执行完毕
ECStack.pop();

// fun2执行完毕
ECStack.pop();

// fun1执行完毕
ECStack.pop();

// javascript接着执行下面的代码，但是ECStack底层永远有个globalContext
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例：</p>
<pre><code class="copyable">var scope = "global scope";
function checkscope()&#123;
   var scope = "local scope";
   function f()&#123;
       return scope;
   &#125;
   return f();
&#125;
checkscope();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">var scope = "global scope";
function checkscope()&#123;
    var scope = "local scope";
    function f()&#123;
        return scope;
    &#125;
    return f;
&#125;
checkscope()();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两段代码的执行上下文栈的变化不一样：
第一段代码：</p>
<pre><code class="copyable">ECStack.push(<checkscope> functionContext);
ECStack.push(<f> functionContext);
ECStack.pop();
ECStack.pop();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二段代码：</p>
<pre><code class="copyable">ECStack.push(<checkscope> functionContext);
ECStack.pop();
ECStack.push(<f> functionContext);
ECStack.pop();
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            