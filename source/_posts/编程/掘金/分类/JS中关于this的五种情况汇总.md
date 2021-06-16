
---
title: 'JS中关于this的五种情况汇总'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7809'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 00:39:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=7809'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">JS中 this 的五种情况汇总</h4>
<p>1、事件绑定：
给当前元素的某个事件绑定方法，当事件行为触发，方法被执行，方法中的this一般都是当前操作的元素
排除：IE6~8中，基于attachEvent进行的DOM2事件绑定，方法中的this是window</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// 例如：</span>
 <span class="hljs-built_in">document</span>.body.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// body元素</span>
&#125;
<span class="hljs-built_in">document</span>.body.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);<span class="hljs-comment">// body元素</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、函数执行（包括自执行函数）
函数执行，看函数前面有没有点“.”，有点，则点前面是谁，函数中的this就是谁；没有点，则this是window
+ 在严格模式下，没有点，this是undefined
+ 匿名函数（自执行函数/回调函数）执行，一般this也是window（严格模式下是undefined），除非有特殊处理</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 例如：</span>
<span class="hljs-comment">// "use strict"</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
&#125;
<span class="hljs-keyword">let</span> obj = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'obj'</span>,
  <span class="hljs-attr">fn</span>: fn
&#125;
<span class="hljs-comment">//函数前面没有点</span>
fn(); <span class="hljs-comment">// window/undefined</span>
<span class="hljs-comment">// 函数前面有点</span>
obj.fn(); <span class="hljs-comment">// obj</span>
<span class="hljs-comment">// 自执行函数</span>
(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// window/undefined</span>
&#125;)();
<span class="hljs-comment">// 回调函数</span>
[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>].forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a,b</span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// window/undefined</span>
&#125;); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、new 构造函数
构造函数执行(new xxx)，函数体中的this是当前类的实例</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 例如：</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fn</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'构造函数'</span>;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
&#125;
Fn.prototype.sum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-keyword">let</span> f = <span class="hljs-keyword">new</span> Fn; <span class="hljs-comment">// this -> f</span>
Fn(); <span class="hljs-comment">// this -> window</span>
f.sum(); <span class="hljs-comment">// this ->f</span>
f.__proto__.sum(); <span class="hljs-comment">// this -> f.__proto__ </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、箭头函数
ES6中的箭头函数(或者基于&#123;&#125;形成的块级上下文)，里面没有this，如果代码中遇到this也不是它自己的，而是它所在上下文中的this</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 例如：</span>
 <span class="hljs-keyword">let</span> obj = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'obj'</span>,
  <span class="hljs-attr">fn</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// obj.fn()执行： this ->obj</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// window 因为这是一个回调函数</span>
    &#125;,<span class="hljs-number">500</span>);

    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 这里的this用的是上级上下文中的this</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// obj</span>
    &#125;, <span class="hljs-number">1000</span>)
  &#125;
&#125;
obj.fn(); <span class="hljs-comment">// fn中的this-> obj </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5、call/apply/bind
基于Function.prototype上的call/apply/bind方法强制改变函数中的this执行（注意：该结论对箭头函数没用，因为箭头函数中没有自己的this）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 例如：</span>
<span class="hljs-keyword">let</span> obj = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'obj'</span>,
  <span class="hljs-attr">fn</span>:fn
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
&#125;
fn(); <span class="hljs-comment">// window</span>
obj.fn();  <span class="hljs-comment">// obj</span>
fn.call(obj); <span class="hljs-comment">// obj</span>
<span class="hljs-built_in">console</span>.log(fn.call(obj));  <span class="hljs-comment">// undefined</span>
obj.fn.apply(<span class="hljs-built_in">window</span>); <span class="hljs-comment">// window</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-1">关于call/apply/bind 的使用</h6>
<p>=== call ===<br>
语法：函数.call(context, parm1, parm2, ...)<br>
简单说明：把函数执行，让函数中的this指向context，并且把parm1、parm2...作为实参传递给函数<br>
详细说明：<br>
+ 首先函数基于原型链__proto__找到Function.prototype.call方法，并且把call方法执行<br>
+ call方法中的this就是当前操作的Function的实例---函数，传递给call方法的第一个实参是要函数中this的指向，剩余实参是依次要传递给函数的参数<br>
+ call方法执行的过程中，实现了这样的处理：把 函数[call中的this] 执行，让 函数中的this指向context，并且把剩余实参传递给函数。如果一个参数也不传，或者第一个参数传递的是null/undefined，给严格模式下，最后函数中的this都是window(严格模式下，不传是undefined，传了null/undefined，最后函数中的this也会改为对应的值)</p>
<p>=== apply ===<br>
语法：函数.apply(context, [parm1, parm2,...])<br>
对比call和apply的区别只有一个，执行函数的时候，需要传递给函数的参数信息，在最开始传递给call/apply的时候，形式不一样<br>
1、call 是需要把参数一个一个的传递给call<br>
2、apply 是需要把参数放在一个数组中传递给apply</p>
<p>=== bind ===<br>
语法：函数.bind(context,param1,param2,...)<br>
call/apply在执行的时候，都会立即把要操作的函数执行，并且改变它的this指向。<br>
bind 是预先处理：指向bind只是预先把函数中需要改变的this等信息改变了并存储起来，此时函数并不会被立即执行，执行完bind会返回一个匿名函数，当后期执行匿名函数的时候，再去把之前需要执行的函数执行，并且改变this的指向。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> a = fn.bind(obj); <span class="hljs-comment">// 执行bind的时候，fn是不会执行的</span>
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 执行bind会返回一个函数，后期只有手动调用a()才会把里面的fn执行，并且按照执行bind时传递的this指向改变fn中的this值</span>

<span class="hljs-comment">// 需求：1s后执行fn，并且让fn中的this变为obj，传递10，20</span>
<span class="hljs-built_in">setTimeout</span>(fn.call(obj, <span class="hljs-number">10</span>, <span class="hljs-number">20</span>), <span class="hljs-number">1000</span>); <span class="hljs-comment">// 这样写虽然this和参数都是想要的，但是并没有在1s后才执行，而是立即就执行了，这是因为在设置定时器的时候，已经基于call方法把fn给执行了</span>
<span class="hljs-built_in">setTimeout</span>(fn.bind(obj, <span class="hljs-number">10</span>, <span class="hljs-number">20</span>), <span class="hljs-number">1000</span>); <span class="hljs-comment">// 把bind执行完后的结果(一个匿名函数)绑定给定时器，1s之后执行这个匿名函数</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            