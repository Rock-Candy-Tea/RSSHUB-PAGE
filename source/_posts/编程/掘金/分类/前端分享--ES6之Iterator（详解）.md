
---
title: '前端分享--ES6之Iterator（详解）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=503'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 08:03:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=503'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">简介</h2>
<p><code>Iterator</code> 是 ES6 引入的一种新的遍历机制，迭代器有两个核心概念：</p>
<ul>
<li>迭代器是一个统一的接口，它的作用是使各种数据结构可被便捷的访问，它是通过一个键为Symbol.iterator 的方法来实现。</li>
<li>迭代器是用于遍历数据结构元素的指针（如数据库中的游标）。</li>
</ul>
<h2 data-id="heading-1">迭代过程</h2>
<p>迭代的过程如下：</p>
<ul>
<li>通过 <code>Symbol.iterator</code> 创建一个迭代器，指向当前数据结构的起始位置</li>
<li>随后通过 next 方法进行向下迭代指向下一个位置， next 方法会返回当前位置的对象，对象包含了 value 和 done 两个属性， value 是当前属性的值， done 用于判断是否遍历结束</li>
<li>当 done 为 true 时则遍历结束</li>
</ul>
<p>下面通过一个简单的例子进行说明：</p>
<pre><code class="copyable">const items = ["zero", "one", "two"]; 
const it = items[Symbol.iterator](); 
it.next(); 
>&#123;value: "zero", done: false&#125; 
it.next();
>&#123;value: "one", done: false&#125; 
it.next(); 
>&#123;value: "two", done: false&#125; 
it.next(); 
>&#123;value: undefined, done: true&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可迭代的数据结构</p>
<p>以下是可迭代的值:</p>
<ul>
<li>Array</li>
<li>String</li>
<li>Map</li>
<li>Set</li>
<li>NodeList（document.getElementsByName("xxx")的返回值）</li>
</ul>
<ol>
<li>NodeList是一中类数组对象，用于保存一组有序的节点</li>
<li>可以通过方括号来访问NodeList的值，他有item()方法与length属性。</li>
<li>他并不是Array的实列，没有数组对象的方法。</li>
</ol>
<h2 data-id="heading-2">什么是 for…of 循环</h2>
<p>for...of 语句创建一个循环来迭代可迭代的对象。在 ES6 中引入的 for...of 循环，以替代 for...in 和 forEach() ，并支持新的迭代协议。for...of 允许你遍历 <code>Arrays（数组）</code>, <code>Strings（字符串）</code>, <code>Maps（映射）</code>, <code>Sets（集合）</code>等可迭代的数据结构等。</p>
<p>语法:
for (variable of iterable) &#123; statement &#125;</p>
<h3 data-id="heading-3">eg:几个不常见的循环</h3>
<h4 data-id="heading-4">1：Maps(映射)</h4>
<p>Map 对象就是保存 key-value(键值) 对。对象和原始值可以用作 key(键)或 value(值)。Map 对象根据其插入方式迭代元素。换句话说， for...of 循环将为每次迭代返回一个 key-value(键值) 数组。</p>
<pre><code class="copyable">//map-example.js 
const iterable = new Map([['one', 1], ['two', 2]]);   
for (const [key, value] of iterable) &#123; 
    console.log(`Key: $&#123;key&#125; and Value: $&#123;value&#125;`); 
&#125;   
// Output: 
// Key: one and Value: 1 
// Key: two and Value: 2
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">2：Set(集合)</h4>
<p>Set(集合) 对象允许你存储任何类型的唯一值，这些值可以是原始值或对象。 Set(集合) 对象只是值的集合。 Set(集合) 元素的迭代基于其插入顺序。 Set(集合) 中的值只能发生一次。如果您创建一个具有多个相同元素的 Set(集合) ，那么它仍然被认为是单个元素。</p>
<pre><code class="copyable">// set-example.js 
const iterable = new Set([1, 1, 2, 2, 1]);   
for (const value of iterable) &#123; 
    console.log(value); 
&#125; 
// Output: 
// 1 
// 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尽管我们的 Set(集合) 有多个 1 和 2 ，但输出的只有 1 和 2 。</p>
<h4 data-id="heading-6">3：Arguments Object(参数对象)</h4>
<p>把一个参数对象看作是一个类数组(array-like)对象，并且对应于传递给函数的参数。这是一个用例：</p>
<pre><code class="copyable">// arguments-example.js 
function args() &#123; 
    for (const arg of arguments) &#123; 
        console.log(arg); 
    &#125; 
&#125;   

args('a', 'b', 'c'); 
// Output: 
// a 
// b 
// c
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可能会想，发生了什么事?! 如前所述，当调用函数时，arguments 会接收传入 args() 函数的任何参数。所以，如果我们传递 20 个参数给 args() 函数，我们将打印出 20 个参数</p>
<h4 data-id="heading-7">4：Generators(生成器)</h4>
<p>生成器是一个函数，它可以退出函数，稍后重新进入函数。</p>
<pre><code class="copyable">// generator-example.js 
function* generator()&#123; 
    yield 1; yield 2; yield 3; 
&#125;;   
for (const g of generator()) &#123; 
    console.log(g); 
&#125;   

// Output: 
// 1 
// 2 
// 3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>function* 定义了一个生成器函数，该函数返回生成器对象(Generator object)。</p>
<h2 data-id="heading-8">For…of vs For…in</h2>
<p>for...of 循环仅适用于迭代。 而普通对象不可迭代。</p>
<p>for...in 循环将遍历对象的所有可枚举属性。</p>
<pre><code class="copyable">//for-in-example.js 
Array.prototype.newArr = () => &#123;&#125;; 
Array.prototype.anotherNewArr = () => &#123;&#125;; 
const array = ['foo', 'bar', 'baz'];   
for (const value in array) &#123; 
    console.log(value); 
&#125; 
// Outcome: 
// 0 
// 1 
// 2 
// newArr 
// anotherNewArr
<span class="copy-code-btn">复制代码</span></code></pre>
<p>for...in 不仅枚举上面的数组声明，它还从构造函数的原型中查找继承的非枚举属性，在这个例子中，newArr 和 anotherNewArr 也会打印出来。</p>
<h2 data-id="heading-9">什么是 Generator函数</h2>
<p>Generator函数是Iterator接口的具体实现方式。Generator 最大的特点就是可以控制函数的执行。</p>
<pre><code class="copyable">function *foo(x) &#123; 
    let y = 2 * (yield (x + 1)) 
    let z = yield (y / 3) 
    return (x + y + z) 
&#125; 
let it = foo(5) 
console.log(it.next()) // => &#123;value: 6, done: false&#125; 
console.log(it.next(12)) // => &#123;value: 8, done: false&#125; 
console.log(it.next(13)) // => &#123;value: 42, done: true&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这个示例就是一个Generator函数，我们来分析其执行过程：</p>
<ul>
<li>首先 Generator 函数调用时它会返回一个迭代器</li>
<li>当执行第一次 next 时，传参会被忽略，并且函数暂停在 yield (x + 1) 处，所以返回 5 + 1 = 6</li>
<li>当执行第二次 next 时，传入的参数等于上一个 yield 的返回值，如果你不传参，yield 永远返回 undefined。此时 let y = 2 * 12，所以第二个 yield 等于 2 * 12 / 3 = 8</li>
<li>当执行第三次 next 时，传入的参数会传递给 z，所以 z = 13, x = 5, y = 24，相加等于 42</li>
</ul>
<h3 data-id="heading-10">Generator vs async</h3>
<p>1、Generator 出现在ES2015中，async 出现在ES2017中，<code>async 是 Generator 的语法糖</code>；</p>
<p>2、执行方式不同，Generator 执行需要使用执行器（next()等方法）；async 函数自带执行器，与普通函数的执行一样；</p>
<p>3、async 的语法语义更加清楚，async 表示异步，await 表示等待；而 Generator 函数的(*)号和 yield 的语义就没那么直接了；</p>
<p>4、Generator 中 yield 后面只能跟 Thunk 函数或 Promise 对象；而 async 函数中 await 后面可以是 promise 对象或者原始类型的值（会自动转为立即resovle的promise对象）；</p>
<p>5、返回值不同，Generator 返回遍历器，相比于 async 返回 promise 对象操作更加麻烦。</p>
<p>PS：</p>
<p>break 是退出当前循环（如果有多重for循环的情况）</p>
<p>return 是退出整个循环， 使用return会直接跳出函数（如果有多重for循环的情况）</p>
<p>在for中不能使用 return，不然会报错（除非循环是在函数里）</p>
<p>在Javascript中，一个函数一旦开始执行，就会运行到最后或遇到return时结束，运行期间不会有其它代码能够打断它，也不能从外部再传入值到函数体内</p>
<p>而Generator函数（生成器）的出现使得打破函数的完整运行成为了可能，其语法行为与传统函数完全不同</p>
<p>Generator函数是ES6提供的一种异步编程解决方案，形式上也是一个普通函数，但有几个显著的特征：</p>
<p> <code>function关键字与函数名之间有一个星号 "*" （推荐紧挨着function关键字） </code></p>
<p> <code>函数体内使用 yield 表达式，定义不同的内部状态 （可以有多个yield） </code></p>
<p> <code>直接调用 Generator函数并不会执行，也不会返回运行结果，而是返回一个遍历器对象（Iterator Object） </code></p>
<p> <code>依次调用遍历器对象的next方法，遍历 Generator函数内部的每一个状态</code></p></div>  
</div>
            