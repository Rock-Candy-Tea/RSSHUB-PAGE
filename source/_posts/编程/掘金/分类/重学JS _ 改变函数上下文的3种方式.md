
---
title: '重学JS _ 改变函数上下文的3种方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4734'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 06:10:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=4734'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>[重学JavaScript系列文章连载中...]</p>
<p>在重学JS系列文章中，上一节学习了JS中的this指向问题。这节学习如何改变函数的上下文，实际上是改变函数体中this的指向。<code>call()</code>函数和<code>apply()</code>函数是为改变函数运行时上下文而存在的，但它们并不是从函数继承而来。<code>bind()</code>函数也能达到这个目的。下面看看三者的用法：</p>
<h3 data-id="heading-0">1. call()函数的用法</h3>
<p>call()函数调用一个函数时，会将该函数的执行上下文改变为另一个对象。语法如下：</p>
<pre><code class="copyable">// Function : 调用的函数
// context : 新的对象上下文，函数中的this指向context，若context为null|undefined，则执行window
// arg1,arg2 : 参数列表  
Function.call(context,arg1,arg2,...)       
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看个简单例子：</p>
<pre><code class="copyable">function add(x,y)&#123;
   return this.x+this.y
&#125;
var obj = &#123;
  x:10,
  y:20
&#125;
add.call(obj) // 30
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子里的add()函数执行时，this指向了obj。可以粗俗的理解为add()函数挂载到obj对象上，执行完函数后，obj对象再删除了add()函数属性。下面通过代码模拟下这个过程：</p>
<pre><code class="copyable">Function.prototype.customeCall = function(cxt)&#123;
  // 不传context,或者null|undefined，默认指向window
  let context = cxt || window  
  // 将调用函数挂载到当前context
  context.fun = this
  // 获取除了context外的参数
  const args = Array.from(arguments).splice(1)
  // 执行调用函数
  const result = context.fun(...args)
  // 执行完后删除属性
  delete context.fun
  return result
&#125;
// 按照例子执行
add.customeCall(obj) // 30
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. apply()函数的用法</h3>
<p>apply()作用与call()函数是一致的，只是在传参形式上不同。</p>
<pre><code class="copyable">// [argArray] 这里传递的是数组
Function.apply(context,[argArray])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单例子：</p>
<pre><code class="copyable">function add(x,y)&#123;
  return x + y
&#125;
function mAdd(x,y)&#123;
  // 注意apply的传参为数组，与call()函数不一致
  return add.apply(this,[x,y]) 
&#125;
mAdd(10,20) // 30
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模拟下实现：</p>
<pre><code class="copyable">Function.prototype.customeApply = function(ctx,argArray)&#123;
  let context = ctx || window
  context.fun = this
  if(!Array.isArray(argArray))&#123;
    throw new Error('参数必须为数组')
  &#125;
  if(!argArray)&#123;
    return context.fun()
  &#125;
  const result = context.fun(...argArray)
  delete context.fun
  return result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. bind()函数的使用</h3>
<p>bind()函数创建一个新函数，在调用时设置this关键字为提供的值，在执行新函数时，将给定的参数列表作为原函数的参数序列，从前往后匹配。语法如下：</p>
<pre><code class="copyable">Function.bind(context,arg1,arg2,...)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单例子：</p>
<pre><code class="copyable">function add(x,y)&#123;
  return this.x+this.y
&#125;
var obj = &#123;
  x:10,
  y:20
`&#125;`
// 函数上下文指向obj返回新函数
var newFun = add.bind(obj) 
newFun() // 30
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模拟下实现：</p>
<pre><code class="copyable">Function.prototype.customeBind = function(context, ...rest) &#123;
  if (typeof this !== 'function') 
    throw new TypeError('invalid invoked!');
  var self = this;
  return function F(...args) &#123;
    if (this instanceof F) &#123;
      return new self(...rest, ...args)
    &#125;
    return self.apply(context, rest.concat(args))
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. 总结</h3>
<p><code>call()</code>函数、<code>apply()</code>函数、<code>bind()</code>函数三者都会改变函数调用时的执行主体，修改this的指向。</p>
<p><code>call()</code>函数、<code>apply()</code>两个函数是立即执行返回，而<code>bind()</code>函数是返回一个新函数，在任何使用可以调用。</p>
<p><code>apply()</code>函数第二个入参为数组，与其他2个函数不一致。</p>
<p>当然箭头函数也可以改变内部上下文的指向，因为它本身就没有自己的上下文，这块后面单独讲。</p></div>  
</div>
            