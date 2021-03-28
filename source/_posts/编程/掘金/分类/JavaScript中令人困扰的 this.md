
---
title: 'JavaScript中令人困扰的 this'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5b7b7d48e24446ba292bd470b5809a9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 22:29:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5b7b7d48e24446ba292bd470b5809a9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>JavaScript this 属于 作用域下的一部分，指的是当前调用的上下文，其他繁杂的概念就不赘述了。</p>
<p>this 是 JavaScript 老掉牙的问题了，同时也是 面试官比较爱考的，但是自己是否真的掌握了呢？</p>
<p>温馨提示：下面的示例，可以作为题型，可先不看答案，尝试 答出，如果全能答出 说明 这块基础 夯实了，最下面有 <strong>总结的 万能大法，建议收藏食用</strong>。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5b7b7d48e24446ba292bd470b5809a9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、普通作用域下的 this</h2>
<h3 data-id="heading-1">1.函数内this</h3>
<p><strong>this 指向 上层 对象。</strong></p>
<h5 data-id="heading-2">1.1 函数在 最外层</h5>
<ul>
<li>web 浏览器下 指向的是 window</li>
<li>node 环境下 指向的是 global</li>
</ul>
<p>例如：</p>
<pre><code class="copyable">function foo()&#123;
console.log(this)
&#125;
foo() // window 或 global
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">1.2 函数在 内层</h5>
<p>示例1：</p>
<pre><code class="copyable">const obj = &#123;
a: 12,
  foo: function()&#123;
    console.log(this.a)
    &#125;
&#125;
obj.foo() // 12
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例2：</p>
<pre><code class="copyable">function foo()&#123;
this.a = 12
  function fn ()&#123;
    console.log(this.a)
    &#125;
    return fn
&#125;
foo()() // 12
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.字面变量声明的对象下的 this</h3>
<p>**指向 全局 **</p>
<ul>
<li>web 浏览器下 指向的是 window</li>
<li>node 环境下 指向的是 global</li>
</ul>
<p>例如：</p>
<pre><code class="copyable">const obj = &#123;
a: 12,
  b: this.a + 1
&#125;
console.log(obj.b) // NaN 因为 this.a 是 undefined，this 指向的是 全局
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">3.构造函数内this</h3>
<p><strong>指向实例，注意只有 new 的 function 才叫做 构造函数，只有new 之后的对象才是 实例。</strong></p>
<p>例如：</p>
<pre><code class="copyable">function Person() &#123;
this.name = "张三"
&#125;
const p = new Person()
console.log(p.name)  // 张三
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">4.原型链上内的this</h3>
<p><strong>指向实例，等同于构造函数内this</strong></p>
<p>例如：</p>
<pre><code class="copyable">function Person()&#123;
this.name = "张三"
&#125;
Person.prototype.say = function ()&#123;
console.log(this.name)
&#125;

const p = new Person()
p.say() // 张三
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">二、改变 this 指向</h2>
<p>**call、apply、bind **  是函数对象的 方法，  <strong>call、apply、bind 绑定的 this，均指向 第一个参数</strong></p>
<h3 data-id="heading-8">1.call</h3>
<p><em><strong>function.call(thisArg, arg1, arg2, ...)</strong></em>  ，第一个参数是 this，后面是 函数对象 本身的参数。
作用有两个：① 执行当前函数  ② 绑定 一个 对象 作为 当前 this。
<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/call" target="_blank" rel="nofollow noopener noreferrer">更多详情</a></p>
<p>示例1：</p>
<pre><code class="copyable">function foo(age)&#123;
  console.log(this.name, age) // 正常调用， this.name 和 age 肯定是不存在的
&#125;
const p = &#123; name: "张三" &#125;
foo.call(p,12) // "张三" 12
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例2:</p>
<pre><code class="copyable">const p = &#123; 
  name："张三", 
  say: function()&#123;
  console.log(this.name)
  &#125; 
&#125;
p.say() // "张三"
const p1 = &#123; name: "李四" &#125;
p.say.call(p1) // 李四
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.apply</h3>
<p><em><strong>function.apply(thisArg, [argsArray])</strong></em>
call() 方法的作用 和 apply() 方法类似，区别就是call()方法接受的是参数列表，而apply()方法接受的是一个参数数组。
<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/apply" target="_blank" rel="nofollow noopener noreferrer">更多详情</a></p>
<p>示例：</p>
<pre><code class="copyable">function foo(age,hobby)&#123;
  console.log(this.name,age,hobby) // age=12 hobby=象棋
&#125;
const p = &#123; name: "张三" &#125;
const args = [12,"象棋"]
foo.apply(p,args) // "张三" 12 象棋
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">3.bind</h3>
<p><em><strong>function.bind(thisArg[, arg1[, arg2[, ...]]])</strong></em>
<strong>bind() 方法创建并返回一个新的函数，</strong>  ，在 bind() 被调用时，这个新函数的 this 被指定为 bind() 的第一个参数，而其余参数将作为新函数的参数。
<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind" target="_blank" rel="nofollow noopener noreferrer">更多详情</a></p>
<p>示例：</p>
<pre><code class="copyable">function foo(age,hobby)&#123;
  console.log(this.name,age,hobby)
&#125;
const p = &#123; name: "张三" &#125;
const fn = foo.bind(p,12,"象棋") // 返回一个函数
fn() // "张三" 12 象棋
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">三、箭头函数</h2>
<p>箭头函数是 ES6 加入的，作用几乎等同于 普通 函数，其中一点重要不同的是   <strong>箭头函数内没有 this，也可以说指向的是外层的 this。</strong>  箭头函数  <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions/Arrow_functions" target="_blank" rel="nofollow noopener noreferrer"> 更多用法详情</a><br>
<strong>所以在箭头函数内，要小心的使用 this。</strong></p>
<h3 data-id="heading-12">1.箭头函数没有this</h3>
<p>示例2：</p>
<pre><code class="copyable">const person = &#123;
  name: "张三",
say: ()=>&#123;
      console.log(this.name)
    &#125;
&#125;
person.say(); // undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>say 函数的 this 指的是 全局下的 window 或 global</p>
<h3 data-id="heading-13">2.箭头函数不可作为 构造函数，不存在 this 问题</h3>
<p>示例1：</p>
<pre><code class="copyable">const Person = (name)=>&#123;
this.name = name
&#125;
console.log(new Person("张三")) // 报错  TypeError: Person is not a constructor
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">四、总结：万能大法</h2>
<ul>
<li>非箭头函数：谁调用 this 就指向谁，没有对象调用 默认指向 全局 window 或 gobal。</li>
<li>构造函数或原型链的函数： 永远指向 实例。</li>
<li>call、apply、bind 情况下 this 永远指向 第一个 参数。</li>
<li>箭头函数：没有this，或指向 外层作用域下的 this。</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            