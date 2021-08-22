
---
title: 'js的五种绑定'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=112'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 06:42:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=112'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">五种绑定</h2>
<p>方式:默认绑定、隐式绑定、显示绑定、new绑定、箭头函数绑定</p>
<p>优先级：显式绑定 > 隐式绑定 > 默认绑定     new绑定 > 隐式绑定 > 默认绑定</p>
<h3 data-id="heading-1">默认绑定</h3>
<blockquote>
<p>当函数调用没有任何前缀的情况下，this在非严格模式下指向window，在严格模式下指向undefined，在严格模式下调用不在严格模式下的函数，并不影响this的返回</p>
</blockquote>
<pre><code class="copyable">function fn1() &#123;
    console.log(this); //window
&#125;;
function fn2() &#123;
    "use strict";
    console.log(this); //undefined
&#125;;
var name = '听风是风';
function fn3() &#123;
    console.log(this); //window
&#125;;
(function () &#123;
    "use strict";
    fn3();
&#125;());
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">隐式绑定</h3>
<h4 data-id="heading-3">1. 如果函数调用时，前面存在调用它的对象，那么this就会隐式绑定到这个对象上</h4>
<pre><code class="copyable">function fn() &#123;
    console.log(this.name);
&#125;;
let obj = &#123;
    name: '听风是风',
    func: fn
&#125;;
obj.func() //听风是风
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2. 如果函数调用前存在多个对象，this指向距离调用自己最近的对象</h4>
<pre><code class="copyable">function fn() &#123;
    console.log(this.name);
&#125;;
let obj = &#123;
    name: '行星飞行',
    func: fn,
&#125;;
let obj1 = &#123;
    name: '听风是风',
    o: obj
&#125;;
obj1.o.func() //行星飞行
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">隐式丢失</h4>
<ol>
<li>作为参数传递以及变量赋值</li>
</ol>
<pre><code class="copyable">var name = '行星飞行';
let obj = &#123;
    name: '听风是风',
    fn: function () &#123;
        console.log(this.name);
    &#125;
&#125;;
function fn1(param) &#123;
    param();
&#125;;
fn1(obj.fn);//行星飞行
例子中我们将 obj.fn 也就是一个函数传递进 fn1 中执行，这里只是单纯传递了一个函数而已，this并没有跟函数绑在一起，所以this丢失这里指向了window。
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>变量赋值，其实本质上与传参相同</li>
</ol>
<pre><code class="copyable">var name = '行星飞行';
let obj = &#123;
    name: '听风是风',
    fn: function () &#123;
        console.log(this.name);
    &#125;
&#125;;
let fn1 = obj.fn;
fn1(); //行星飞行
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.隐式绑定丢失并不是都会指向全局对象</p>
<pre><code class="copyable">var name = '行星飞行';
let obj = &#123;
    name: '听风是风',
    fn: function () &#123;
        console.log(this.name);
    &#125;
&#125;;
let obj1 = &#123;
    name: '时间跳跃'
&#125;
obj1.fn = obj.fn;
obj1.fn(); //时间跳跃
虽然丢失了 obj 的隐式绑定，但是在赋值的过程中，又建立了新的隐式绑定，这里this就指向了对象 obj1。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">显示绑定</h3>
<blockquote>
<p>通过call、apply以及bind方法改变this的行为</p>
</blockquote>
<pre><code class="copyable">let obj1 = &#123;
    name: '听风是风'
&#125;;
let obj2 = &#123;
    name: '时间跳跃'
&#125;;
let obj3 = &#123;
    name: 'echo'
&#125;
var name = '行星飞行';

function fn() &#123;
    console.log(this.name);
&#125;;
fn(); //行星飞行
fn.call(obj1); //听风是风
fn.apply(obj2); //时间跳跃
fn.bind(obj3)(); //echo ，因为bind非立即执行，详情参考笔记的this指向call，apply，bind
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意，如果在使用call之类的方法改变this指向时，指向参数提供的是null或者undefined，那么 this 将指向全局对象。</p>
</blockquote>
<pre><code class="copyable">let obj1 = &#123;
    name: '听风是风'
&#125;;
let obj2 = &#123;
    name: '时间跳跃'
&#125;;
var name = '行星飞行';
function fn() &#123;
    console.log(this.name);
&#125;;
fn.call(undefined); //行星飞行
fn.apply(null); //行星飞行
fn.bind(undefined)(); //行星飞行
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">new绑定</h3>
<p>new执行了什么<br>
(1) 创建一个新对象<br>
(2) 将构造函数的作用域赋给新对象（因此 this 就指向了这个新对象） <br>
(3) 执行构造函数中的代码（为这个新对象添加属性） <br>
(4) 返回新对象<br></p>
<pre><code class="copyable">function Fn()&#123;
    this.name = '听风是风';
&#125;;
let echo = new Fn(); //this将指向新对象echo上
echo.name//听风是风
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">箭头函数</h3>
<p>准确来说，箭头函数中没有this，箭头函数的this指向取决于外层作用域中的this，外层作用域或函数的this指向谁，箭头函数中的this便指向谁。</p></div>  
</div>
            