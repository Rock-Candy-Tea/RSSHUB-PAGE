
---
title: 'Node V8 作用域相关'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2b3cf91386446619491ce280c014f25~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 01:43:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2b3cf91386446619491ce280c014f25~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一. 前言</h1>
<p>对于一门编程语言来说，变量的存储和访问，是最基本的功能之一。今天，将向大家深入介绍一下，JS 程序在运行的时候，如何找到变量，这需要一套良好的规范来规范，这套规则，就成为了作用域</p>
<h1 data-id="heading-1">二. V8 JS 代码运行的步骤</h1>
<p>在介绍作用域的知识点之前，还需要先介绍一下，V8 JS 代码的运行流程。网上有较多的 V8 工作运行流程图，举例如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2b3cf91386446619491ce280c014f25~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中后面的几步骤，像 Ignition 的字节码、TurboFan 优化编译器，主要是 V8 为了优化性能而做的，在本文不做过多展开。本文主要专注于前面几步骤，可以看到，V8 在拿到 JS 的 source code 后，会首先解析生成 AST 抽象语法树，然后后面再经过若干编译步骤，生成机器码并被运行。其中的作用域规则确定，是在解析成 AST 这一步骤的时候，就已经被确定了</p>
<p>下面以 V8 源码内的 hello-world 程序为例，对流程进行讲解：</p>
<blockquote>
<p>github.com/v8/v8/samples/hello-world.cc</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a1b4c07d2a24179b55abc5bd87532af~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在介绍上图的代码流程之前，先介绍一些概念：</p>
<h4 data-id="heading-2">isolate：</h4>
<ul>
<li>一个 Isolate 是一个独立的虚拟机。对应一个或多个线程。但同一时刻 只能被一个线程进入。</li>
<li>所有的 Isolate 彼此之间是完全隔离的, 它们不能够有任何共享的资源。</li>
<li>如果不显式创建 Isolate, 会自动创建一个默认的 Isolate</li>
</ul>
<h4 data-id="heading-3">handleScope：</h4>
<ul>
<li>表示JS对象的生命周期的范围。</li>
<li>在 V8 中，内存分配都是在 V8 的 Heap 中进行分配的，JavaScript 的值和对象也都存放在 V8 的 Heap 中。而 Handle 即是对 Heap 中对象的引用。V8 为了对内存分配进行管理，GC 需要对 V8 中的所有对象进行跟踪。HandleScope 就是用来管理 Handle 的</li>
<li>Handle 分为 Local 和 Persistent 两种。Local 是局部的，创建一个指向 JS 对象的本地引用，它同时被 HandleScope 进行管理。 persistent，创建一个指向 JS 变量的持久引用，类似与全局的，不受 HandleScope 的影响，其作用域可以延伸到不同的函数。</li>
</ul>
<h4 data-id="heading-4">context：</h4>
<ul>
<li>可以理解为「执行上下文」或者「 执行环境」</li>
<li>每当程序的执行流进入到一个可执行的代码时，就进入到了一个执行环境中</li>
</ul>
<p>三者关系的示意图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f26f9fba21e24e9dabdf68bd7289ec5f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>回到上述一开始的源码截图里，大概做了以下几步工作：</p>
<ol>
<li>定义了一个 isolate</li>
<li>在 isolate 下，定义了一个handle_scope。handle_sope 的生命周期，决定了下面所有 v8::Local 的声明周期的有效性</li>
<li>定义了一个 context，并切换进入</li>
<li>编译 JS 源码成字节码</li>
<li>在当前 context 中，运行上一步编译出的字节码</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25cf197cf42b40c8b9f47aa7b334a3e5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">三. 作用域与执行上下文相关</h1>
<p>在上面第二节中，简单介绍了 V8 执行 JS 代码的流程。再简单概括一下，JavaScript属于解释型语言，JavaScript 的执行分为 「解释 」和 「执行 」两个阶段，如下：</p>
<h4 data-id="heading-6">解释阶段：</h4>
<ul>
<li>词法分析</li>
<li>语法分析</li>
<li><strong>作用域规则确定</strong></li>
</ul>
<h4 data-id="heading-7">执行阶段：</h4>
<ul>
<li>创建执行上下文 context</li>
<li>执行函数代码</li>
<li>垃圾回收</li>
</ul>
<ol>
<li>
<h2 data-id="heading-8">两者区别</h2>
</li>
</ol>
<p>很多同学容易混淆，「作用域 」和 「执行上下文」 这两个概念，的确他们两有一定的相关性，但又有区别：</p>
<ul>
<li>
<p>可以把作用域抽象理解成，是根据名称查找变量的一套规则，这套规则用来管理 js 引擎根据标识符名称如何查找变量。而一系列的嵌套作用域就形成了作用域链（你不知道的 JavaScript 中定义）</p>
</li>
<li>
<p>而执行上下文，如上一节中描述，是在函数运行之前，V8 创建的函数运行环境</p>
</li>
<li>
<p>作用域在 AST 解析阶段就确定，不会改变；而执行上下文，是在执行阶段才确定，可能发生改变。举个例子：</p>
<p>var a = 10;
function fn() &#123;
var b = 20;
function bar() &#123;
console.log(this.b); // 200
console.log(a + b); // 30
&#125;
return bar;
&#125;
var x = fn(),
b = 200;
x();</p>
</li>
</ul>
<p>上面的打印的结果为 200、30，是因为对于 this.b 来说，this 的指向，就是执行上下文中确定的；而 bar 函数中的 b 值，是在 AST 解析 bar 函数定义时，就已经明确 bar 函数的作用域链，为 bar -> fn -> 全局，所以 b 变量会沿着作用域链寻找，找到 fn 中的定义，值为 20</p>
<ul>
<li>一个作用域下，可能包含若干个上下文环境。因为在一个函数作用域里，每次在调用别的函数前，都要先创建调用函数所需的执行上下文。但是调用函数的次数是不定的，需要在运行时才能确定</li>
</ul>
<ol>
<li>
<h2 data-id="heading-9">函数执行流程介绍</h2>
</li>
</ol>
<p>为了更深入的介绍作用域与执行上下文的原理，我们以一个函数的执行为例子，进行详细描述，并对其中一些概念再进行介绍：</p>
<pre><code class="copyable">var scope = "global scope";
function checkscope() &#123;
    var scope = "local scope";
    function f() &#123;
        return scope;
    &#125;
    return f();
&#125;
checkscope();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<h4 data-id="heading-10">执行全局代码，创建全局执行上下文，全局上下文被压入执行上下文栈</h4>
<p>ECStack = [
globalContext
];</p>
</li>
</ol>
<blockquote>
<p><strong>执行上下文栈</strong>：如上述介绍，V8 的执行流，在进入可执行代码之前，会为其创建一个执行上下文。执行流依次进入的执行环境，在逻辑上形成了一个栈，则成为执行上下文栈。栈的底部永远是全局环境，栈的顶部则是处于活动状态的当前执行环境（浏览器总是执行，处于栈顶的上下文）</p>
</blockquote>
<ol>
<li>
<h4 data-id="heading-11">全局上下文初始化（初始化全局环境的变量对象 VO，确定全局环境的 Scope，绑定全局环境的 this）</h4>
<p>globalContext = &#123;
VO: &#123;
global: window,
scope: undefined,
checkscope: reference to function checkscope
&#125;,
Scope: [globalContext.VO],
this: globalContext.VO
&#125;</p>
</li>
</ol>
<blockquote>
<p><strong>变量对象 VO</strong>：</p>
</blockquote>
<ul>
<li>
<blockquote>
<p>存储了在上下文中定义的变量和函数声明；除了我们无法访问它外，和普通对象没什么区别</p>
</blockquote>
</li>
<li>
<blockquote>
<p>对于函数，执行前的初始化阶段叫变量对象，执行中就变成了活动对象</p>
</blockquote>
</li>
<li>
<blockquote>
<p>每一个执行环境都有一个与之相关的变量对象，其中存储着上下文中声明的：变量、函数、形式参数</p>
</blockquote>
</li>
</ul>
<ol>
<li>
<h4 data-id="heading-12">checkScope 函数执行前阶段。初始化的同时，checkscope 函数被创建，保存全局环境的作用域链，到函数 checkscope 的内部属性 [[scope]] 中</h4>
<p>checkscope.[[scope]] = [
globalContext.VO
];</p>
<p>globalContext = &#123;
VO: &#123;
global: window,
scope: "global scope",
checkscope: reference to function checkscope
&#125;,
Scope: [globalContext.VO],
this: globalContext.VO
&#125;</p>
</li>
<li>
<h4 data-id="heading-13">执行 checkscope 函数，创建 checkscope 函数执行上下文，checkscope 函数的执行上下文，被压入执行上下文栈</h4>
<p>ECStack = [
checkscopeContext,
globalContext
];</p>
</li>
<li>
<h4 data-id="heading-14">初始化 checkscope 函数执行上下文。会有以下几步：</h4>
<ol>
<li>用 arguments 创建活动对象 checkscopeContext.AO</li>
<li>利用 checkscopeContext.AO 与 checkscope.[[scope]]，形成checkscope 函数执行环境的作用域链 checkscopeContext.Scope</li>
<li>绑定 this 到 undefined（非严格模式下会绑定到全局对象）</li>
</ol>
<p>checkscopeContext = &#123;
AO: &#123;
arguments: &#123;
length: 0
&#125;,
scope: undefined,
f: reference to function f()&#123;&#125;
&#125;,
Scope: [AO, globalContext.VO],
this: undefined
&#125;</p>
</li>
</ol>
<blockquote>
<p><strong>活动对象 AO</strong>：</p>
</blockquote>
<ul>
<li>
<blockquote>
<p>在没有执行当前环境之前，变量对象中的属性都不能访问。但是进入执行阶段之后，变量对象转变为了活动对象，所以活动对象和变量对象其实是一个东西，只是处于执行环境的不同生命周期</p>
</blockquote>
</li>
<li>
<blockquote>
<p>AO 实际上是包含了 VO 的。因为除了 VO 之外，AO 还包含函数的参数 parameters，以及 arguments 这个特殊对象</p>
</blockquote>
</li>
</ul>
<ol>
<li>
<h4 data-id="heading-15">f 函数执行前阶段。更新 f.[[scope]]， checkscopeContext.AO.scope 等赋值</h4>
<p>f.[[scope]] = [
checkscopeContext.AO,
globalContext.VO
];</p>
<p>checkscopeContext = &#123;
AO: &#123;
arguments: &#123;
length: 0
&#125;,
scope: "local scope",
f: reference to function f()&#123;&#125;
&#125;,
Scope: [AO, globalContext.VO],
this: undefined
&#125;</p>
</li>
<li>
<h4 data-id="heading-16">执行 f 函数，创建 f 函数执行上下文，f 函数执行上下文被压入执行上下文栈</h4>
<p>ECStack = [
fContext,
checkscopeContext,
globalContext
];</p>
</li>
<li>
<h4 data-id="heading-17">f 函数执行环境初始化（参考第 e 步）</h4>
<p>fContext = &#123;
AO: &#123;
arguments: &#123;
length: 0
&#125;
&#125;,
Scope: [AO, checkscopeContext.AO, globalContext.VO],
this: undefined
&#125;</p>
</li>
<li>
<h4 data-id="heading-18">f 函数中代码执行。需要对 scope 进行 RHS 查找。查找从作用域链中当前活动对象，开始沿着作用域链向上查找</h4>
</li>
</ol>
<blockquote>
<pre><code class="copyable">// 查找过程：
1. fContext.AO.scope 没有该变量声明，继续
2. checkscopeContext.AO.scope 有该变量声明，获取其值为"local scope"
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<blockquote>
<p><strong>LHS、RHS</strong>：为 V8 引擎的两种查询方式</p>
</blockquote>
<ul>
<li>
<blockquote>
<p>LHS：代码中出现变量时，目的是要进行存储，也就是我们关心的是要找到变量的容器本身，来进行不同数据的存储赋值操作，而不关心现在这个容器里面存的是什么</p>
</blockquote>
</li>
<li>
<blockquote>
<p>RHS：目的只是拿这个变量来用，也就是只关心这个变量存储的内容是什么，而不需要关心这个变量存在哪个容器</p>
</blockquote>
</li>
</ul>
<ol>
<li>
<h4 data-id="heading-19">f 函数执行完毕，返回"local scope"。f 函数上下文从执行上下文栈中弹出</h4>
<p>ECStack = [
checkscopeContext,
globalContext
];</p>
</li>
<li>
<h4 data-id="heading-20">checkscope 函数在执行完 f 处，获取 f 执行的返回值 "local scope"，函数继续向下执行</h4>
</li>
<li>
<h4 data-id="heading-21">checkScope 执行完毕，返回获取到的返回值 "local scope"。checkScope 函数上下文，从执行上下文栈中弹出</h4>
<p>ECStack = [
globalContext
];</p>
</li>
<li>
<h4 data-id="heading-22">代码执行流回到全局执行环境中调用 checoscope 处，拿到 checkScope 返回值并继续向下执行</h4>
</li>
<li>
<h4 data-id="heading-23">直到程序终止，或者页面关闭。全局上下文出栈并销毁</h4>
</li>
</ol>
<p>作者：陆瀚陶</p></div>  
</div>
            