
---
title: 'this指向问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6905'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 06:39:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=6905'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">this指向的方式</h2>
<pre><code class="copyable">① 在普通函数中，this指向window
② 在构造函数中，this指向创建的对象
③ 在方法声明中，this指向调用者
④ 在定时器中， this指向window
⑤ 在事件中，this 指向事件源

//this指向window
function foo() &#123;
console.log(this.a)
&#125;
var a = 1foo()   

//this指向obj，调用foo的对象上
const obj = &#123;
a: 2,
foo: foo
&#125;
obj.foo()

//this指向new这个函数上，即c
const c = new foo()

//箭头函数的this指向定义这个函数的位置，bind，apply无效，此时this指向window
function a() &#123;
    return () => &#123;
        return () => &#123;
            console.log(this)
        &#125;
    &#125;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">改变this指向</h2>
<p>1.使用bind</p>
<pre><code class="copyable">var foo = &#123;
x: 3
&#125;
var bar = function()&#123;
console.log(this.x);
&#125;
bar(); // undefined

var boundFunc = bar.bind(foo); //使用bind将this绑定到window上，可以访问到foo
boundFunc(); // 3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.let self = this<br>
3.立即执行函数(function(j) &#123;&#125;)(i)</p>
<h2 data-id="heading-2">bind、apply、call</h2>
<p>在说区别之前还是先总结一下三者的相似之处：<br></p>
<h3 data-id="heading-3">相似之处</h3>
<p>1、都是用来改变函数的this对象的指向的。<br>
2、第一个参数都是this要指向的对象。<br>
3、都可以利用后续参数传参。</p>
<h3 data-id="heading-4">区别</h3>
<p>1.call、apply与bind都用于改变this绑定，但call、apply在改变this指向的同时还会执行函数，而bind在改变this后是返回一个全新的boundFcuntion绑定函数，这也是为什么上方例子中bind后还加了一对括号 ()的原因。</p>
<p>2.bind属于硬绑定，返回的 boundFunction 的 this 指向无法再次通过bind、apply或 call 修改；call与apply的绑定只适用当前调用，调用完就没了，下次要用还得再次绑。</p>
<p>3.call与apply功能完全相同，唯一不同的是call方法传递函数调用形参是以散列形式，而apply方法的形参是一个数组。在传参的情况下，call的性能要高于apply，因为apply在执行时还要多一步解析数组。</p>
<p>wx.say.bind(this)   不能立即执行，无效，必须wx.say.bind(this)("aaa"),参数置后<br>
wx.say.call(this,"aaa","bbb")   立即执行<br>
wx.say.apply(this,["aaa","bbb"])   立即执行,参数为数组</p>
<h2 data-id="heading-5">手写call,apply,bind</h2>
<pre><code class="copyable">Function.prototype.myCall = 
    function (ctx) &#123; 
    ctx = ctx || window; 
    ctx.fn = this; 
    let args = Array.from(arguments).slice(1); 
    let res = ctx.fn(...args); 
    delete ctx.fn; 
    return res;
&#125;; 
Function.prototype.myApply = function (ctx) &#123; 
    ctx = ctx || window; 
    ctx.fn = this; 
    let args = Array.from(arguments[1]); 
    let res = ctx.fn(...args); 
    delete ctx.fn; 
    return res; 
&#125;;
Function.prototype.myBind = function (ctx) &#123; 
    let args = Array.from(arguments).slice(1); 
    let that = this; 
    return function (...oargs) 
        &#123; 
            return that.apply(ctx, [...args, ...oargs]); 
        &#125;;
 &#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            