
---
title: 'let 、var、const'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/129e2b637d5a4560a4fa8423a3ad4c07~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 02:18:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/129e2b637d5a4560a4fa8423a3ad4c07~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.var</h2>
<p>在 ES6 之前我们都是通过 var 关键字定义 JavaScript 变量。ES6 才新增了 let 和 const 关键字</p>
<p><code>var num = 1</code></p>
<p>在全局作用域下使用 var 声明一个变量，默认它是挂载在顶层对象 window 对象下（Node 是 global）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> num = <span class="hljs-number">1</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.num) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用 var 声明的变量的作用域是它当前的执行上下文，可以是函数也可以是全局</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x = <span class="hljs-number">1</span> <span class="hljs-comment">// 声明在全局作用域下</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> x = <span class="hljs-number">2</span> <span class="hljs-comment">// 声明在 foo 函数作用域下</span>
    <span class="hljs-built_in">console</span>.log(x) <span class="hljs-comment">// 2</span>
&#125;
foo()
<span class="hljs-built_in">console</span>.log(x) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在 foo 没有声明 x ，而是赋值，则赋值的是 foo 外层作用域下的 x </p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x = <span class="hljs-number">1</span> <span class="hljs-comment">// 声明在全局作用域下</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;

    x = <span class="hljs-number">2</span> <span class="hljs-comment">// 赋值</span>

    <span class="hljs-built_in">console</span>.log(x) <span class="hljs-comment">// 2</span>

&#125;

foo()

<span class="hljs-built_in">console</span>.log(x) <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果赋值给未声明的变量，该变量会被隐式地创建为全局变量（它将成为顶层对象的属性）</p>
<pre><code class="hljs language-js copyable" lang="js">a = <span class="hljs-number">2</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.a) <span class="hljs-comment">// 2</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    b = <span class="hljs-number">3</span>
&#125;
foo()
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.b) <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>var 缺陷一：所有未声明直接赋值的变量都会自动挂在顶层对象下，造成全局环境变量不可控、混乱</strong></p>
<h3 data-id="heading-1">变量提升（hoisted）</h3>
<p>使用var声明的变量存在变量提升的情况</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(b) <span class="hljs-comment">// undefined</span>
<span class="hljs-keyword">var</span> b = <span class="hljs-number">3</span>
注意，提升仅仅是变量声明，不会影响其值的初始化，可以与隐式的理解为：
<span class="hljs-keyword">var</span> b
<span class="hljs-built_in">console</span>.log(b) <span class="hljs-comment">// undefined</span>
b = <span class="hljs-number">3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">作用域规则</h3>
<p>var 声明可以在包含它的函数，模块，命名空间或全局作用域内部任何位置被访问，包含它的代码块对此没有什么影响，所以多次声明同一个变量并不会报错：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x = <span class="hljs-number">1</span>
<span class="hljs-keyword">var</span> x = <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种作用域规则可能会引发一些错误</p>
<pre><code class="copyable">function sumArr(arrList) &#123;
    var sum = 0;
    for (var i = 0; i < arrList.length; i++) &#123;
        var arr = arrList[i];
        for (var i = 0; i < arr.length; i++) &#123;
            sum += arr[i];
        &#125;
    &#125;
    return sum;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里很容易看出一些问题，里层的 for 循环会覆盖变量 i，因为所有 i 都引用相同的函数作用域内的变量。 有经验的开发者们很清楚，这些问题可能在代码审查时漏掉，引发无穷的麻烦。</p>
<p><strong>var 缺陷二：允许多次声明同一变量而不报错，造成代码不容易维护</strong></p>
<h3 data-id="heading-3">捕获变量怪异之处</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
  a[i] = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(i);
  &#125;;
&#125;
a[<span class="hljs-number">6</span>](); <span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>i 是全局变量，全局只有一个变量i ，所有i都用同一个引用，前一个i会被后面的i覆盖掉， for 循环结束时， i=10 ，所以 a 【6】( ) 也为 10 ，并且 a 的所有元素里面的 i 都为 10</p>
<h2 data-id="heading-4">2.let</h2>
<p>let 与 var 的写法一致，不同的是它使用的是块作用域</p>
<p><code>let a = 1 </code></p>
<p>块作用域变量在包含它们的块或 for 循环之外是不能访问的</p>
<pre><code class="copyable">&#123;
    let x = 1
&#125;
console.log(x) // Uncaught ReferenceError: x is not defined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以：</p>
<pre><code class="copyable">var a = [];
for (let i = 0; i < 10; i++) &#123; // let有自己的块作用域，每一次循环的 i 其实都是一个新的变量
  a[i] = function () &#123;
    console.log(i);
  &#125;;
&#125; // JavaScript 引擎内部会记住上一轮循环的值，初始化本轮的变量i时，就在上一轮循环的基础上进行计算
a[6](); // 6
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时， let 解决了 var 的两个缺陷：</p>
<h3 data-id="heading-5"><strong>使用 let 在全局作用域下声明的变量也不是顶层对象的属性</strong>*</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>
<span class="hljs-built_in">window</span>.b <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6"><strong>不允许同一块中重复声明</strong></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> x = <span class="hljs-number">1</span>
<span class="hljs-keyword">let</span> x = <span class="hljs-number">2</span>
<span class="hljs-comment">// Uncaught SyntaxError: Identifier 'x' has already been declared</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在不同块中是可以声明的</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-keyword">let</span> x = <span class="hljs-number">1</span>
    &#123;
        <span class="hljs-keyword">let</span> x = <span class="hljs-number">2</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种在一个嵌套作用域中声明同一个变量名称的行为称做 <strong>屏蔽</strong> ，它可以完美解决上面的 sumArr 问题：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sumArr</span>(<span class="hljs-params">arrList</span>) </span>&#123;
    <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arrList.length; i++) &#123;
        <span class="hljs-keyword">var</span> arr = arrList[i];
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
            sum += arr[i];
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> sum;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时将得到正确的结果，因为内层循环的 i 可以屏蔽掉外层循环的 i </p>
<p>通常来讲应该避免使用屏蔽，因为我们需要写出清晰的代码。 同时也有些场景适合利用它，你需要好好打算一下</p>
<h2 data-id="heading-7">3.var 与 let 的区别</h2>
<p>（1）作用域</p>
<p>用 var 声明的变量的作用域是它当前的执行上下文，即如果是在任何函数外面，则是全局执行上下文，如果在函数里面，则是当前函数执行上下文。换句话说，var 声明的变量的作用域只能是全局或者整个函数块的。</p>
<p>而 let 声明的变量的作用域则是它当前所处代码块，即它的作用域既可以是全局或者整个函数块，也可以是 if、while、switch等用&#123;&#125;限定的代码块。</p>
<p>另外，var 和 let 的作用域规则都是一样的，其声明的变量只在其声明的块或子块中可用。</p>
<p>示例代码：</p>
<pre><code class="copyable">function varTest() &#123;
  var a = 1;

  &#123;
    var a = 2; // 函数块中，同一个变量
    console.log(a); // 2
  &#125;

  console.log(a); // 2
&#125;

function letTest() &#123;
  let a = 1;

  &#123;
    let a = 2; // 代码块中，新的变量
    console.log(a); // 2
  &#125;

  console.log(a); // 1
&#125;

varTest();
letTest();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述示例中可以看出，let 声明的变量的作用域可以比 var 声明的变量的作用域有更小的限定范围，更具灵活。</p>
<p>（2）重复声明</p>
<p>var 允许在同一作用域中重复声明，而 let 不允许在同一作用域中重复声明，否则将抛出异常。</p>
<p>var 相关示例代码：</p>
<pre><code class="copyable">var a = 1;
var a = 2;

console.log(a) // 2

function test() &#123;
  var a = 3;
  var a = 4;
  console.log(a) // 4
&#125;

test()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>let 相关示例代码：</p>
<pre><code class="copyable">if(false) &#123;
  let a = 1;
  let a = 2; // SyntaxError: Identifier 'a' has already been declared
&#125;
switch(index) &#123;
  case 0:
    let a = 1;
  break;

  default:
    let a = 2; // SyntaxError: Identifier 'a' has already been declared
    break;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述示例中可以看出，let 声明的重复性检查是发生在词法分析阶段，也就是在代码正式开始执行之前就会进行检查。</p>
<p>（4）变量提升与暂存死区</p>
<p>var 声明变量存在变量提升，如何理解变量提升呢？</p>
<p>要解释清楚这个，就要涉及到执行上下文和变量对象。</p>
<p>在 JavaScript 代码运行时，解释执行全局代码、调用函数或使用 eval 函数执行一个字符串表达式都会创建并进入一个新的执行环境，而这个执行环境被称之为执行上下文。因此执行上下文有三类：全局执行上下文、函数执行上下文、eval 函数执行上下文。</p>
<p>执行上下文可以理解为一个抽象的对象。</p>
<p>Variable object：变量对象，用于存储被定义在执行上下文中的变量 (variables) 和函数声明 (function declarations) 。</p>
<p>Scope chain：作用域链，是一个对象列表 (list of objects) ，用以检索上下文代码中出现的标识符 (identifiers)</p>
<p>thisValue：this 指针，是一个与执行上下文相关的特殊对象，也被称之为上下文对象。
一个执行上下文的生命周期可以分为三个阶段：创建、执行、释放。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/129e2b637d5a4560a4fa8423a3ad4c07~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而所有使用 var 声明的变量都会在执行上下文的创建阶段时作为变量对象的属性被创建并初始化，这样才能保证在执行阶段能通过标识符在变量对象里找到对应变量进行赋值操作等。</p>
<p>而用 var 声明的变量构建变量对象时进行的操作如下：</p>
<ul>
<li>由名称和对应值（undefined）组成一个变量对象的属性被创建（创建并初始化）</li>
<li>如果变量名称跟已经声明的形式参数或函数相同，则变量声明不会干扰已经存在的这类属性。
上述过程就是我们所谓的“变量提升”，这也就能解释为什么变量可以在声明之前使用，因为使用是在执行阶段，而在此之前的创建阶段就已经将声明的变量添加到了变量对象中，所以执行阶段通过标识符可以在变量对象中查找到，也就不会报错。</li>
</ul>
<p>示例代码：</p>
<pre><code class="copyable">console.log(a) // undefined

var a = 1;

console.log(a) // 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>let 声明变量存在暂存死区，如何理解暂存死区呢？</p>
<p><strong>其实 let 也存在与 var 类似的“变量提升”过程，但与 var 不同的是其在执行上下文的创建阶段，只会创建变量而不会被初始化（undefined），并且 ES6 规定了其初始化过程是在执行上下文的执行阶段（即直到它们的定义被执行时才初始化），使用未被初始化的变量将会报错。</strong></p>
<p>在变量初始化前访问该变量会导致 ReferenceError，因此从进入作用域创建变量，到变量开始可被访问的一段时间（过程），就称为暂存死区(Temporal Dead Zone)。</p>
<p>示例代码 1：</p>
<pre><code class="copyable">console.log(bar); // undefined
console.log(foo); // ReferenceError: foo is not defined

var bar = 1;
let foo = 2;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例代码 2：</p>
<pre><code class="copyable">var foo = 33;
&#123;
  let foo = (foo + 55); // ReferenceError: foo is not defined
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：首先，需要分清变量的创建、初始化、赋值是三个不同的过程。另外，从 ES5 开始用词法环境（Lexical Environment）替代了 ES3 中的变量对象（Variable object）来管理静态作用域，但作用是相同的。为了方便理解，上述讲解中仍保留使用变量对象来进行描述。</p>
<p>小结</p>
<ul>
<li>var 声明的变量在执行上下文创建阶段就会被「创建」和「初始化」，因此对于执行阶段来说，可以在声明之前使用。</li>
<li>let 声明的变量在执行上下文创建阶段只会被「创建」而不会被「初始化」，因此对于执行阶段来说，如果在其定义执行前使用，相当于使用了未被初始化的变量，会报错。</li>
</ul>
<h2 data-id="heading-8">4.let 与 const 异同</h2>
<p>const 与 let 很类似，都具有上面提到的 let 的特性，唯一区别就在于 const 声明的是一个只读变量，声明之后不允许改变其值。因此，const 一旦声明必须初始化，否则会报错。</p>
<p>示例代码：</p>
<pre><code class="copyable">let a;
const b = "constant"

a = "variable"
b = 'change' // TypeError: Assignment to constant variable
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何理解声明之后不允许改变其值？</p>
<p>其实 const 其实保证的不是变量的值不变，而是保证变量指向的内存地址所保存的数据不允许改动（即栈内存在的值和地址）。</p>
<p>JavaScript 的数据类型分为两类：原始值类型和对象（Object类型）。</p>
<p>对于原始值类型（undefined、null、true/false、number、string），值就保存在变量指向的那个内存地址（在栈中），因此 const 声明的原始值类型变量等同于常量。</p>
<p>对于对象类型（object，array，function等），变量指向的内存地址其实是保存了一个指向实际数据的指针，所以 const 只能保证指针是不可修改的，至于指针指向的数据结构是无法保证其不能被修改的（在堆中）。</p>
<p>示例代码：</p>
<pre><code class="copyable">const obj = &#123;
  value: 1
&#125;

obj.value = 2

console.log(obj) // &#123; value: 2 &#125;

obj = &#123;&#125; // TypeError: Assignment to constant variable
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> user = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"sisterAn"</span>,
    <span class="hljs-attr">age</span>: num,
&#125;
user = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"pingzi"</span>,
    <span class="hljs-attr">age</span>: num
&#125; <span class="hljs-comment">// Uncaught TypeError: Assignment to constant variable.</span>

<span class="hljs-comment">// 下面这些都是运行成功的</span>
user.name = <span class="hljs-string">"Hello"</span>
user.name = <span class="hljs-string">"Kitty"</span>
user.name = <span class="hljs-string">"Cat"</span>
user.age--
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其它 const 与 let 相同，例如：</p>
<p>· 作用域相同，只在声明所在的块级作用域内有效</p>
<p>· 常量也是不提升，同样存在暂时性死区</p></div>  
</div>
            