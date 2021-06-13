
---
title: '重学 JS _ 箭头函数为什么不能用做构造函数？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3100'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 23:47:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=3100'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>[重学JavaScript系列文章连载中...]</p>
<p>标题是某大佬入职鹅厂的面试题，这里借题聊聊箭头函数。</p>
<p>前几天学习的时候，我写过关于this指向的问题，得出的结论是：this永远指向函数的调用者。但是在箭头函数中，this指向的是定义时所在的对象，而不是使用时所在的对象。换句话说，箭头函数没有自己的this，而是继承父作用域中的this。</p>
<p>附上文章：<a href="https://juejin.cn/post/6971069912928223245" target="_blank">this的指向问题</a></p>
<p>看个例子:</p>
<pre><code class="copyable">var person = &#123;
  name:'张三',
  age:18,
  getName:function()&#123;
  console.log('我的名字是：'+this.name)
  &#125;,
  getAge:()=>&#123;
  console.log('我的年龄是：'+this.age)
  &#125;
&#125;

person.getName() // 我的名字是张三
person.getAge()  // 我的年龄是undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>person.getName()</code>中<code>this</code>指向函数的调用者，也就是<code>person</code>实例，因此<code>this.name = "张三"</code>。</p>
<p><code>getAge()</code>通过箭头函数定义，而箭头函数是没有自己的<code>this</code>，会继承父作用域的<code>this</code>，因此<code>person.getAge()</code>执行时，此时的作用域指向<code>window</code>，而<code>window</code>没有定义<code>age</code>属性，所有报<code>undefined</code>。</p>
<p>从例子可以得出：<strong>对象中定义的函数使用箭头函数是不合适的</strong>。</p>
<p><strong>先解答下标题问题，为啥箭头函数不能作为构造函数？</strong></p>
<pre><code class="copyable">// 构造函数生成实例的过程
function Person(name,age)&#123;
  this.name = name
  this.age = age
&#125;
var p = new Person('张三',18)

//new关键字生成实例过程如下
// 1. 创建空对象p
var p = &#123;&#125; 
// 2. 将空对象p的原型链指向构造器Person的原型
p.__proto__ = Person.prototype
// 3. 将Person()函数中的this指向p
// 若此处Person为箭头函数，而没有自己的this，call()函数无法改变箭头函数的指向，也就无法指向p。
Person.call(p) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构造函数是通过new关键字来生成对象实例，生成对象实例的过程也是通过构造函数给实例绑定this的过程，而箭头函数没有自己的this。创建对象过程，<code>new</code> 首先会创建一个空对象，并将这个空对象的<code>__proto__</code>指向构造函数的<code>prototype</code>，从而继承原型上的方法，但是箭头函数没有<code>prototype</code>。因此不能使用箭头作为构造函数，也就不能通过new操作符来调用箭头函数。</p>
<p>下面看看箭头函数其他需要注意的点：</p>
<ol>
<li>不支持call()/apply()函数的特性</li>
</ol>
<p>call()/bind()函数的作用是改变被调用函数中this的指向。但是箭头函数没有自己的this，而是继承父作用域中的this，所以这两函数没法改变箭头函数的指向。</p>
<pre><code class="copyable">var Person = &#123;
  name:'张三',
  getName:function(arg)&#123;
    let fun = v=>v+this.name
    let boy  = &#123;
      name:'李四'
    &#125;
    // call函数绑定boy实例
    return fun.call(b,arg)
  &#125;
&#125;

Person.getName('我是') // 我是张三
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子中，倘若箭头函数执行fun.call(b,arg)成功改变this的指向，此时应当输出的是：“我是李四”，但实际上输出的是：“我是张三”，由此可以call函数并没有成功改变箭头函数fun内部this的指向。</p>
<ol start="2">
<li>不绑定arguments</li>
</ol>
<pre><code class="copyable">var fun = ()=>&#123;
   console.log(arguments)
&#125;

fun(1) // 报错：ReferenceError: arguments is not defined

// 解决办法
var fun = (...args)=>&#123;
  console.log(args)
&#125;
fun(1)  // 输出：[1]
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>没有prototype属性</li>
</ol>
<pre><code class="copyable">var fun = ()=>&#123;&#125;
fun.prototype // undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>原型函数不能定义成箭头函数</li>
</ol>
<pre><code class="copyable">function Person(name)&#123;
  this.name = name
&#125;

// 原型函数使用箭头函数，其中的this指向全局对象，而不会指向构造函数
// 因此访问不到构造函数本身，也就访问不到实例属性
Person.prototype.say = ()=>&#123;console.log(this.name)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自此我们学习了箭头函数的一些疑难点。</p></div>  
</div>
            