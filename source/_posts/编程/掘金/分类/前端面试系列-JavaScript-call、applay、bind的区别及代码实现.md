
---
title: '前端面试系列-JavaScript-call、applay、bind的区别及代码实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5757'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 20:49:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=5757'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>call 和 apply 的主要作用，是改变对象的执行上下文，并且是立即执行的。它们在参数上的写法略有区别；bind 也能改变对象的执行上下文，它与 call 和 apply 不同的是，返回值是一个函数，并且需要稍后再调用一下，才会执行。</p>
<h1 data-id="heading-0">一、call</h1>
<p>call 的写法</p>
<pre><code class="copyable">Function.call(obj,[param1[,param2[,…[,paramN]]]])
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">var name = 'name'
var obj = &#123;
 name: 'objName'
&#125;
function getName(p1, p2) &#123;
 console.log(p1, p2,this.name)
&#125;
getName(1, 2) //1 2 "name"
getName.call(obj, 1, 2)//1 2 "objName"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意以下几点：</p>
<ul>
<li>调用 call 的对象，必须是个函数 Function。</li>
<li>call 的第一个参数，是一个对象。 Function 的调用者，将会指向这个对象。如果不传，则默认为全局对象 window。</li>
<li>第二个参数开始，可以接收任意个参数。每个参数会映射到相应位置的 Function 的参数上。但是如果将所有的参数作为数组传入，它们会作为一个整体映射到 Function 对应的第一个参数上，之后参数都为空。</li>
</ul>
<pre><code class="copyable">function func (a,b,c) &#123;&#125;

func.call(obj, 1,2,3)
// func 接收到的参数实际上是 1,2,3

func.call(obj, [1,2,3])
// func 接收到的参数实际上是 [1,2,3],undefined,undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">call模拟实现</h2>
<ol>
<li>明确是谁调用call：函数。</li>
<li>call接收的第一个参数是要改变的this指向(去执行这个函数)。若无指定，默认为window</li>
<li>call接收的后续参数就是作为调用call的那个函数所需的参数。</li>
</ol>
<pre><code class="copyable">function myCall(context) &#123;
  //判断一下
  if (typeof this !== 'function')&#123;
throw new TypeError('error')
  &#125;
  //this指向,谁去执行去这个函数
  context = context || window
  //要执行的函数
  context.fn = this
  //取出参数
  const args = [...arguments].slice(1)
  //执行函数
  const result = context.fn(...args)
  //删除fn
  delete context.fn
  return result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>验证一下</p>
<pre><code class="copyable">Function.prototype.myCall = myCall
getName.myCall(obj， 1, 2)//1 2 "objName"
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">二、applay</h1>
<p>apply使用与call大体一致，只是接受参数的方法不同。call可以接收多个参数。apply接收的第一个参数是this，第二个参数是 所需参数所组成的数组。</p>
<pre><code class="copyable">Function.apply(obj[,argArray])
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">applay模拟实现</h2>
<pre><code class="copyable">function myApply(context) &#123;
  if (typeof this !== 'function') &#123;
    throw new TypeError('Error');
  &#125;
  context = context || window;
  context.fn = this;
  var result;
  if (arguments[1]) &#123;
    result = context.fn(...arguments[1]);
  &#125; else &#123;
    result = context.fn();
  &#125;
  delete context.fn;
  return result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">三、bind</h1>
<pre><code class="copyable">Function.bind(thisArg[, arg1[, arg2[, ...]]])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>bind 方法 与 apply 和 call 比较类似，也能改变函数体内的 this 指向。不同的是，<strong>bind 方法的返回值是函数</strong>，并且需要稍后调用，才会执行。而 apply 和 call 则是立即调用。</p>
<h2 data-id="heading-5">bind模拟实现</h2>
<pre><code class="copyable">function  myBind(context) &#123;
  if (typeof this !== 'function') &#123;
    throw new TypeError('Error')
  &#125;
const _this = this
const args = [...arguments].slice(1)
// 返回函数
return function F() &#123;
  // 1 判断是否用作构造函数
  if (this instanceof F) &#123;
    return new _this(...args, ...arguments)
  &#125;
  // 2 用作普通函数
  return _this.apply(context, args.concat(...arguments))
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>验证一下：
普通函数</p>
<pre><code class="copyable">Function.prototype.myBind = myBind

var name = 'name'
var obj = &#123;
 name: 'objName'
&#125;

function test(p1, p2)&#123;
  this.a = p1
  this.b = p2
  console.log(this.name,p1, p2)
&#125;
var f1 = test.myBind(obj, 1)
f1(2)//objName 1 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构造函数</p>
<pre><code class="copyable">var name = 'name'
var obj = &#123;
 name: 'objName'
&#125;

function test(p1, p2)&#123;
  this.a = p1
  this.b = p2
  console.log(this.name,p1, p2)//undefined 1 2
&#125;
var f1 = test.myBind(obj, 1)
var f= new f1(2)
console.log(f)//test &#123;a: 1, b: 2&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">应用场景</h1>
<h2 data-id="heading-7">1.对象的继承</h2>
<pre><code class="copyable">function superClass () &#123;
    this.value = 123;
    this.print = function () &#123;
        console.log(this.value);
    &#125;
&#125;

function subClass () &#123;
    superClass.call(this);
    this.print();
&#125;

subClass();
//123
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">2.借用方法</h2>
<p>使类数组可以使用Array 原型链上的方法</p>
<pre><code class="copyable">let domNodes = Array.prototype.slice.call(document.getElementsByTagName("*"));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">3.Math.max||Math.min</h2>
<pre><code class="copyable">let arr = [1,2,3,4,5];
console.log(Math.max.apply(this,arr))//5
console.log(Math.min.call(this,...arr))//1
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">4.数组合并</h2>
<pre><code class="copyable">let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];

Array.prototype.push.apply(arr1, arr2);
console.log(arr1); // [1, 2, 3, 4, 5, 6]
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            