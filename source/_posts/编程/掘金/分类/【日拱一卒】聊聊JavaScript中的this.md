
---
title: '【日拱一卒】聊聊JavaScript中的this'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/684e3bad1ae44b689a092365cc175276~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 23:30:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/684e3bad1ae44b689a092365cc175276~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第4天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>”</p>
<h2 data-id="heading-0">前言</h2>
<p>聊聊执行上下文中的this</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/684e3bad1ae44b689a092365cc175276~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>JavaScript的执行上下文中，有：</p>
<p><strong>变量环境</strong>(保存当前执行上下文中var声明的变量)，</p>
<p><strong>词法环境</strong>(保存当前执行上下文语句块中let、const声明的变量)，</p>
<p><strong>outer</strong>（指向上一级执行上下文，由静态代码中的嵌套关系决定，全局上下文的值为NULL），</p>
<p>还有一个<strong>this</strong>？</p>
<p>似乎这个this在JavaScript整个执行过程中，没有起到作用。那this到底是用来干什么的呢？</p>
<p>先给出结论：使用this机制实现，<strong>在对象内部的方法中使用对象内部的属性</strong>。</p>
<p>this主要是一种规范标准，浏览器依照规范标准而实现，所以了解this，还是得从一些经典案例之中去分析，弄懂的案例越多，你肚子里的存货就越多。你才能更懂得别人那些从ECMA规范总结出的1，2，3。</p>
<p>this值的定义（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fthis" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/this" ref="nofollow noopener noreferrer">MDN</a>）：</p>
<p>当前执行上下文（global、function 或 eval）的一个属性，在非严格模式下，总是指向一个<strong>对象</strong>，在严格模式下可以是任意值。</p>
<h2 data-id="heading-1">经典案例</h2>
<h2 data-id="heading-2">案例1（入门级别）</h2>
<pre><code class="copyable">// 全局环境中的this指向了全局对象 
console.log(this)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b9dd1aa81034f728403fd1d4325e80e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>定义如此，不赘述</p>
<h2 data-id="heading-3">案例2（小白级别）</h2>
<pre><code class="copyable">var obj = &#123;
  foo: function () &#123;console.log(this.bar)&#125;,
  bar: 1
&#125;;

var foo = obj.foo;
var bar = 2;

// 写法一
obj.foo() // 1 foo函数中的this指向了obj

// 写法二
foo() // 2 foo函数中的this指向了全局对象
<span class="copy-code-btn">复制代码</span></code></pre>
<p>var obj = &#123;……&#125;</p>
<p>本质上是把一个堆内存的地址的值赋给了obj，这个值指向的内存空间是一个对象。</p>
<p>obj.foo() 是对象调用方法</p>
<p>this指向了obj</p>
<p>var foo = obj.foo</p>
<p>本质上也是把一个堆内存的地址的值赋给了obj，这个值指向的内存空间是一个函数。</p>
<p>foo()是等同于全局环境中的函数执行</p>
<p>this指向了全局对象</p>
<p>参考：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2018%2F06%2Fjavascript-this.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.ruanyifeng.com/blog/2018/06/javascript-this.html" ref="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2018/0…</a></p>
<h2 data-id="heading-4">案例3（菜鸟级别）</h2>
<pre><code class="copyable">var myObj = &#123;
  name : "极客时间", 
  showThis: function()&#123;
    console.log(this)
    function bar()&#123;console.log(this)&#125;
    bar()
  &#125;
&#125;
myObj.showThis()
// bar()中的this指向了全局对象 这个有大佬觉得是设计失误 
// 这个案例经典的原因就是  大部分bug都是源自这里

// 分析（可能过度分析了）：函数中执行其他函数,与全局环境执行函数，没有区别。
// 大部分人也在这里总结出谁调用，this就指向谁，没有谁调用默认指向全局对象
// 这里可以通过箭头函数 和 闭包去 在bar函数中使用showThis 中的this
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9f30aa7429148a880db5bbb0970a9b0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">案例4（应试级别）</h2>
<pre><code class="copyable">// JS中函数调用的三种形式

// 初学者语法糖1
func(p1, p2)

// 初学者语法糖2 
obj.child.method(p1, p2)

// 函数调用的终极必杀
func.call(context, p1, p2) // 先不讲 apply
<span class="copy-code-btn">复制代码</span></code></pre>
<p>语法糖1等价于func.call(undefined, p1, p2)</p>
<pre><code class="copyable">function func()&#123;
  console.log(this)
&#125;

// 函数调用
func()

//等价于
func.call(undefined)

// 简写为
func.call()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>语法糖2等价于obj.foo.call(obj,p1,p2)</p>
<pre><code class="copyable">var obj = &#123;
  foo: function()&#123;
    console.log(this)
  &#125;
&#125;

obj.foo() 
// 等价于
obj.foo.call(obj)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>PS：箭头函数中没有this这个概念，箭头函数中的this直接当作他外面函数中的this即可</p>
<p>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F23804247" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/23804247" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/23804247</a></p>
<p>至此，this核心案例大概就这些了。关于new，箭头函数，乃至严格模式，感觉这些与this机制的主脉络无关，此处不做深入探讨之后梳理到这些内容的时候，再进行梳理。</p>
<h2 data-id="heading-6">梳理ECMAScript中的this</h2>
<p>ECMAScript 的类型分为<strong>语言类型</strong>和<strong>规范类型</strong>。</p>
<p>ECMAScript 语言类型是开发者直接使用 ECMAScript 可以操作的。其实就是我们常说的Undefined, Null, Boolean, String, Number, 和 Object。</p>
<p>而<strong>规范类型</strong>相当于 meta-values，是用来用算法描述 ECMAScript 语言结构和 ECMAScript 语言类型的。规范类型包括：<strong>Reference</strong>, List, Completion, Property Descriptor, Property Identifier, Lexical Environment, 和 Environment Record。</p>
<p>PS：其中Reference与 this 的指向有着密切的关联</p>
<blockquote>
<p>The Reference type is used to explain the behaviour of such operators as delete, typeof, and the assignment operators.</p>
</blockquote>
<p>所以 Reference 类型就是用来解释诸如 delete、typeof 以及赋值等操作行为的。</p>
<blockquote>
<p>A Reference is a resolved name binding.</p>
</blockquote>
<blockquote>
<p>A Reference consists of three components, the base value, the referenced name and the Boolean valued strict reference flag.</p>
</blockquote>
<blockquote>
<p>The base value is either undefined, an Object, a Boolean, a String, a Number, or an environment record (10.2.1).</p>
</blockquote>
<blockquote>
<p>A base value of undefined indicates that the reference could not be resolved to a binding. The referenced name is a String.</p>
</blockquote>
<p><strong>Reference</strong> 由 base value 和 referenced name 以及 strict reference组成</p>
<p><strong>base value</strong> 属性所在的对象</p>
<p><strong>referenced name</strong> 属性的名称 </p>
<p><strong>strict reference</strong></p>
<pre><code class="copyable">var foo = 1;

// 对应的Reference是：
var fooReference = &#123;
    base: EnvironmentRecord,
    name: 'foo',
    strict: false
&#125;;


var foo = &#123;
    bar: function () &#123;
        return this;
    &#125;
&#125;;
 
foo.bar(); // foo

// bar对应的Reference是：
var BarReference = &#123;
    base: foo,
    propertyName: 'bar',
    strict: false
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>GetBase</strong> Reference的方法，返回reference的base value</p>
<p><strong>IsPropertyReference</strong> Reference的方法，如果base value 是一个对象 返回true</p>
<p><strong>GetValue</strong> 返回对象属性真正的值</p>
<p>函数调用中如何确定this，（规范 11.2.3 Function Calls）</p>
<p>1.计算 MemberExpression 的结果赋值给 ref</p>
<p>2.判断 ref 是不是一个 Reference 类型 </p>
<ul>
<li>
<p>2.1 如果 ref 是 Reference，并且 IsPropertyReference(ref) 是 true, 那么 this 的值为 GetBase(ref) </p>
</li>
<li>
<p>2.2 如果 ref 是 Reference，并且 base value 值是 Environment Record, 那么this的值为 ImplicitThisValue(ref) </p>
</li>
<li>
<p>2.3 如果 ref 不是 Reference，那么 this 的值为 undefined</p>
<p>var value = 1;</p>
<p>var foo = &#123;
value: 2,
bar: function () &#123;
return this.value;
&#125;
&#125;</p>
<p>//示例1
console.log(foo.bar());
//示例2
console.log((foo.bar)());
//示例3
console.log((foo.bar = foo.bar)());
//示例4
console.log((false || foo.bar)());
//示例5
console.log((foo.bar, foo.bar)());</p>
</li>
</ul>
<h2 data-id="heading-7">MemberExpression</h2>
<pre><code class="copyable">foo.bar()
// 此处的MemberExpression是 foo.bar
// 根据规范11.2.1 PropertyAccessors,foo.bar会返回一个Reference类型 
// 进入2.1 this的值为GetBase(ref) 即foo

(foo.bar)()
// 此处的MemberExpression是 (foo.bar)
// 根据规范11.1.6 The Grouping Operator 不会对MemberExpression进行计算
// 与foo.bar()相同返回一个Reference类型

(foo.bar = foo.bar)()
// 此处的MemberExpression是(foo.bar = foo.bar)
// 根据规范11.13.1 Simple Assignment(=) MemberExpression为GetValue(rref)
// 返回一个非Reference类型
// (false || foo.bar) 、(foo.bar, foo.bar)与本情况类似 返回结果都是一个非Reference类型
// 进入2.3 this的值为undefined  非严格模式下 被隐式转换为全局对象

// 补充
foo(); 
// base为EnvironmentRecord 进入2.2
// this的值为ImplicitThisValue(ref)  函数返回undefined
// this的值为undefined  非严格模式下 被隐式转换为全局对象
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考 </p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmqyqingfeng%2FBlog%2Fissues%2F7" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mqyqingfeng/Blog/issues/7" ref="nofollow noopener noreferrer">github.com/mqyqingfeng…</a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fyanhaijing.com%2Fes5%2F%23null" target="_blank" rel="nofollow noopener noreferrer" title="http://yanhaijing.com/es5/#null" ref="nofollow noopener noreferrer">yanhaijing.com/es5/#null</a></p>
<p>PS: 关于this，浅尝则止。继续深入的时候，感受到一种被深渊凝视的刺痛感。此时深入研究ECMAScript相关规范还是太蠢了一点。留给未来的自己吧。</p></div>  
</div>
            