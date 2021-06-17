
---
title: 'js内功修炼-基础篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/657aa0321a4a4da8afa47cd0fbb0d8c3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 02:42:26 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/657aa0321a4a4da8afa47cd0fbb0d8c3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近负责前端技术一面，提问他人的时候，会发现js基础知识好多细节自己也不是很扎实，特意找时间统一梳理了一下：</p>
<h3 data-id="heading-0">1. JS数据类型</h3>
<p>js数据类型分为：基础数据类型（7种）和引用数据类型object。
基础数据类型： null、undefined、 number、 string、 boolean 、symbol（es6）、 bigint(可以表示大于2^53 -1的整数)
引用数据类型：object。object包括array、function、Date、RegExp等</p>
<h3 data-id="heading-1">2. 判断数据类型的方式：</h3>
<p>（1） typeof：
用来判断除了null的基本数据类型，typeof null返回object.
引用数据类型除function外，都返回object</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">var</span> b = <span class="hljs-string">'lala'</span>;
<span class="hljs-keyword">var</span> c = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">var</span> d = <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">var</span> e = <span class="hljs-built_in">Symbol</span>();
<span class="hljs-keyword">var</span> f = <span class="hljs-number">1n</span>;

<span class="hljs-keyword">var</span> g = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">var</span> h = &#123;&#125;;
<span class="hljs-keyword">var</span> i = [];
<span class="hljs-keyword">var</span> j = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;

<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> a);  <span class="hljs-comment">// number</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> b);  <span class="hljs-comment">// string</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> c);  <span class="hljs-comment">// boolean</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> d);  <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> e);  <span class="hljs-comment">// symbol</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> f);  <span class="hljs-comment">// bigint</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> g);  <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> h);  <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> i);  <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> j);  <span class="hljs-comment">// function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）instanceof
用来判断引用数据类型，类实例，instanceof会沿着原型链一直往上寻找，返回值为true或false</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> h = &#123;&#125;;
<span class="hljs-keyword">var</span> i = [];
<span class="hljs-keyword">var</span> j = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;
<span class="hljs-keyword">var</span> k = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="hljs-keyword">var</span> l = <span class="hljs-regexp">/[0-9]/g</span>;

<span class="hljs-built_in">console</span>.log(h <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>);  <span class="hljs-comment">// trye</span>
<span class="hljs-built_in">console</span>.log(i <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>);  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(j <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Function</span>);  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(k <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Date</span>);  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(l <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">RegExp</span>);  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(3) Object.prototype.toString.call()</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">null</span>); <span class="hljs-comment">// "[object Null]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">undefined</span>); <span class="hljs-comment">// "[object Undefined]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-string">'lala'</span>);<span class="hljs-comment">// "[object String]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-number">1</span>);<span class="hljs-comment">// "[object Number]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">true</span>);<span class="hljs-comment">// "[object Boolean]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>());<span class="hljs-comment">// "[object Date]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-regexp">/[0-9]/</span>);<span class="hljs-comment">// "[object RegExp]"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">手写instanceof</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myInstanceof</span>(<span class="hljs-params">left, right</span>) </span>&#123;

  <span class="hljs-comment">// 这里先用typeof来判断基础数据类型，如果是，直接返回false</span>
  <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> left !== <span class="hljs-string">'object'</span> || left === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  
  <span class="hljs-comment">// getProtypeOf是Object对象自带的API，能够拿到参数的原型对象</span>
  <span class="hljs-keyword">let</span> proto = <span class="hljs-built_in">Object</span>.getPrototypeOf(left);
  
  <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>) &#123;                  <span class="hljs-comment">//循环往下寻找，直到找到相同的原型对象</span>
    <span class="hljs-keyword">if</span>(proto === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    <span class="hljs-keyword">if</span>(proto === right.prototype) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;<span class="hljs-comment">//找到相同原型对象，返回true</span>
    proto = <span class="hljs-built_in">Object</span>.getPrototypeof(proto);
  &#125;
&#125;

<span class="hljs-comment">// 验证一下自己实现的myInstanceof是否OK</span>
<span class="hljs-built_in">console</span>.log(myInstanceof(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">123</span>), <span class="hljs-built_in">Number</span>));    <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(myInstanceof(<span class="hljs-number">123</span>, <span class="hljs-built_in">Number</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">3. 深浅拷贝</h3>
<p>这要从数据的在内存中存储的位置说起，基本数据类型存储在栈中，引用数据类型数据存储在堆中，栈中存储了访问对象的地址。</p>
<p>对于基础数据类型来讲，都是对值的拷贝；
但是对引用数据类型来讲，分为深拷贝和浅拷贝。</p>
<p>浅拷贝首先会创建一个对象，对原对象的属性值精准拷贝，如果属性值是基础数据类型，拷贝的就是基础数据类型的值，如果属性值是引用数据类型，拷贝的是内存地址。</p>
<p>深拷贝会拷贝所有的属性，并拷贝属性指向的动态分配的内存。当对象和它所引用的对象一起拷贝时即发生深拷贝。也就是说是在堆内存中重新开辟空间，拷贝后数据存放在新的地址，同时指针指向新的地址，与原数据完全隔离。</p>
<p><strong>常见的浅拷贝的实现方式有：</strong>
object.assign(target, ...sources)
扩展运算符 ...
concat 拷贝数组
slice 拷贝数组 arr.slice(begin, end);</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Object.assign()</span>
<span class="hljs-keyword">let</span> target = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;
<span class="hljs-keyword">let</span> source = &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">c</span>: &#123; <span class="hljs-attr">d</span>: <span class="hljs-number">3</span> &#125; &#125;;

<span class="hljs-built_in">Object</span>.assign(target, source);
<span class="hljs-built_in">console</span>.log(target);  <span class="hljs-comment">// &#123; a: 1, b: 2, c: &#123; d: 3 &#125; &#125;;</span>

target.b = <span class="hljs-number">5</span>; 
target.c.d = <span class="hljs-number">4</span>; 
<span class="hljs-built_in">console</span>.log(source); <span class="hljs-comment">// &#123; b: 2, c: &#123; d: 4 &#125; &#125;;</span>
<span class="hljs-built_in">console</span>.log(target); <span class="hljs-comment">// &#123; a: 1, b: 5, c: &#123; d: 4 &#125; &#125;;</span>

<span class="hljs-comment">// ...</span>
<span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-attr">a</span>:<span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: &#123; <span class="hljs-attr">c</span>:<span class="hljs-number">1</span> &#125; &#125;
<span class="hljs-keyword">let</span> obj2 = &#123; ...obj &#125;
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">let</span> newArr = [...arr];


<span class="hljs-comment">// concat()</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">let</span> newArr = arr.concat();


<span class="hljs-comment">// slice()</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, &#123;<span class="hljs-attr">val</span>: <span class="hljs-number">4</span>&#125;];
<span class="hljs-keyword">let</span> newArr = arr.slice();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是使用 object.assign 方法有几点需要注意：</p>
<ul>
<li>它不会拷贝对象的继承属性；</li>
<li>它不会拷贝对象的不可枚举的属性；</li>
<li>可以拷贝 Symbol 类型的属性。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj1 = &#123; <span class="hljs-attr">a</span>:&#123; <span class="hljs-attr">b</span>:<span class="hljs-number">1</span> &#125;, <span class="hljs-attr">sym</span>:<span class="hljs-built_in">Symbol</span>(<span class="hljs-number">1</span>)&#125;; 
<span class="hljs-built_in">Object</span>.defineProperty(obj1, <span class="hljs-string">'innumerable'</span> ,&#123;
    <span class="hljs-attr">value</span>:<span class="hljs-string">'不可枚举属性'</span>,
    <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">false</span>
&#125;);
<span class="hljs-keyword">let</span> obj2 = &#123;&#125;;
<span class="hljs-built_in">Object</span>.assign(obj2,obj1)
obj1.a.b = <span class="hljs-number">2</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'obj1'</span>,obj1);  <span class="hljs-comment">// &#123; a: &#123; b: 2 &#125;, sym: Symbol(1), innumerable: '不可枚举属性'&#125;</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'obj2'</span>,obj2);  <span class="hljs-comment">// &#123; a: &#123; b: 2 &#125;, sym: Symbol(1)&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>深拷贝的实现方式：JSON.stringify</strong></p>
<p>但是使用 JSON.stringify 实现深拷贝还是有一些地方值得注意，总结下来主要有这几点：</p>
<ol>
<li>拷贝的对象的值中如果有函数、undefined、symbol 这几种类型，经过 JSON.stringify 序列化之后的字符串中这个键值对会消失；</li>
<li>拷贝 Date 引用类型会变成字符串；</li>
<li>无法拷贝不可枚举的属性；</li>
<li>无法拷贝对象的原型链；</li>
<li>拷贝 RegExp 引用类型会变成空对象；</li>
<li>对象中含有 NaN、Infinity 以及 -Infinity，JSON 序列化的结果会变成 null；</li>
<li>无法拷贝对象的循环应用，即对象成环 (obj[key] = obj)。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Obj</span>(<span class="hljs-params"></span>) </span>&#123; 
  <span class="hljs-built_in">this</span>.func = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; alert(<span class="hljs-number">1</span>) &#125;; 
  <span class="hljs-built_in">this</span>.obj = &#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>&#125;;
  <span class="hljs-built_in">this</span>.arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
  <span class="hljs-built_in">this</span>.und = <span class="hljs-literal">undefined</span>; 
  <span class="hljs-built_in">this</span>.reg = <span class="hljs-regexp">/123/</span>; 
  <span class="hljs-built_in">this</span>.date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-number">0</span>); 
  <span class="hljs-built_in">this</span>.NaN = <span class="hljs-literal">NaN</span>;
  <span class="hljs-built_in">this</span>.infinity = <span class="hljs-literal">Infinity</span>;
  <span class="hljs-built_in">this</span>.sym = <span class="hljs-built_in">Symbol</span>(<span class="hljs-number">1</span>);
&#125; 
<span class="hljs-keyword">let</span> obj1 = <span class="hljs-keyword">new</span> Obj();
<span class="hljs-built_in">Object</span>.defineProperty(obj1,<span class="hljs-string">'innumerable'</span>,&#123; 
  <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">false</span>,
  <span class="hljs-attr">value</span>:<span class="hljs-string">'innumerable'</span>
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'obj1'</span>,obj1);
<span class="hljs-keyword">let</span> str = <span class="hljs-built_in">JSON</span>.stringify(obj1);
<span class="hljs-keyword">let</span> obj2 = <span class="hljs-built_in">JSON</span>.parse(str);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'obj2'</span>,obj2);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/657aa0321a4a4da8afa47cd0fbb0d8c3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">手写浅拷贝</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> shallowClone = <span class="hljs-function">(<span class="hljs-params">target</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> target === <span class="hljs-string">'object'</span> && target !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">let</span> cloneTarget = <span class="hljs-built_in">Array</span>.isArray(target) ? [] : &#123;&#125;;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> prop <span class="hljs-keyword">in</span> target) &#123;
      <span class="hljs-keyword">if</span> (target.hasOwnProperty(prop)) &#123;  <span class="hljs-comment">// 遍历对象自身可枚举属性（不考虑继承属性和原型对象</span>
          cloneTarget[prop] = target[prop]
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> cloneTarget
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> target
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">手写深拷贝</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> deepClone = <span class="hljs-function">(<span class="hljs-params">target</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> target === <span class="hljs-string">'object'</span> && target !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">let</span> cloneTarget = <span class="hljs-built_in">Array</span>.isArray(target) ? [] : &#123;&#125;;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> prop <span class="hljs-keyword">in</span> target) &#123;
      <span class="hljs-keyword">if</span> (target.hasOwnProperty(prop)) &#123;  <span class="hljs-comment">// 遍历对象自身可枚举属性（不考虑继承属性和原型对象</span>
          cloneTarget[prop] = deepClone(target[prop]);  <span class="hljs-comment">//递归导致日期、正则变成&#123;&#125;</span>
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> cloneTarget
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> target
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f058a9568d34de3b4286770f3221769~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">改进版深拷贝</h4>
<p>考虑日期、正则、循环引用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> deepClone = <span class="hljs-function">(<span class="hljs-params">target, map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()</span>) =></span> &#123;
<span class="hljs-keyword">if</span> (target === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> target !== <span class="hljs-string">'object'</span> || target.constructor === <span class="hljs-built_in">Date</span> || target.constructor === <span class="hljs-built_in">RegExp</span>) <span class="hljs-keyword">return</span> target
  <span class="hljs-keyword">if</span> (map.has(target)) <span class="hljs-keyword">return</span> target  <span class="hljs-comment">// 解决循环引用</span>
  
  <span class="hljs-keyword">const</span> deepTarget = <span class="hljs-built_in">Array</span>.isArray(target) ? [] : &#123;&#125;;
  map.set(target, <span class="hljs-literal">true</span>)
  
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> prop <span class="hljs-keyword">in</span> target) &#123;
    <span class="hljs-keyword">if</span> (target.hasOwnProperty(prop)) &#123;  <span class="hljs-comment">// 遍历对象自身可枚举属性（不考虑继承属性和原型对象</span>
      deepTarget[prop] = deepClone(target[prop], map)
     &#125;
  &#125;
  <span class="hljs-keyword">return</span> deepTarget
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4. 原型</h3>
<h4 data-id="heading-8">原型对象</h4>
<p>首先思考三个问题：</p>
<ol>
<li>什么是原型对象？</li>
<li>原型对象何时产生？</li>
<li>原型对象如何访问？</li>
</ol>
<h4 data-id="heading-9">什么是原型对象？</h4>
<p>原型对象本质就是一个对象，所有函数都有prototype属性，该属性指向函数的原型对象，原型对象中包括：</p>
<ul>
<li>constructor: 指向构造函数</li>
<li>继承自Object的属性和方法</li>
</ul>
<h4 data-id="heading-10">原型对象何时产生？</h4>
<p>原型对象在函数创建的时候产生，每声明一个函数，都会做以下操作：</p>
<ul>
<li>浏览器会在内存中创建一个对象</li>
<li>对象中添加一个constructor属性</li>
<li>constructor属性指向该函数</li>
<li>将新创建的对象赋值给函数的prototype属性</li>
</ul>
<h4 data-id="heading-11">原型对象如何访问？</h4>
<p>函数名.prototype
通过函数实例的__proto__属性，函数每创建一个实例，该实例内部包含一个指针，指向构造函数的原型对象。</p>
<h3 data-id="heading-12">5. 原型链</h3>
<p>原型链就是访问实例上某个属性或者方法时，先在实例中查找，找到即返回；若没有，则通过__proto__属性到构造函数的原型对象prototype上去找，找到则返回；若没有，则继续到构造函数的原型对象prototype的__proto__属性查找，直到搜索到Object.prototype为止。</p>
<h4 data-id="heading-13">一张图理解原型、原型链</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afdc98204979402597f2a0ed030ca01b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">总结</h4>
<p>所有函数都是Function的实例，Function也是Function的实例
Function继承Object，除Object外，其他一切皆继承自Object</p>
<h3 data-id="heading-15">6. 继承</h3>
<p>有两个函数、函数A、函数B，实现函数A继承函数B的属性和方法：</p>
<h4 data-id="heading-16">原型链继承</h4>
<pre><code class="hljs language-js copyable" lang="js">A.prototype = <span class="hljs-keyword">new</span> B()
A.prototype.constructor = A

<span class="hljs-keyword">var</span> a1 = <span class="hljs-keyword">new</span> A()
<span class="hljs-keyword">var</span> a2 = <span class="hljs-keyword">new</span> A()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73e85f70ab4640c4aa709bdf5e6ce9cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>缺点：</p>
<ol>
<li>父类B函数原型对象的引用类型属性会被实例 a1 a2共享</li>
<li>创建子类A的实例无法向父类B传参数</li>
<li>子类无法实现继承多个函数，这里A只能继承自B</li>
</ol>
<h4 data-id="heading-17">构造函数继承</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params">e</span>) </span>&#123;
  B.call(<span class="hljs-built_in">this</span>, e)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：
子类无法访问父类原型上的属性和方法</p>
<h4 data-id="heading-18">组合继承</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">B</span> (<span class="hljs-params">name, age</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
&#125;
B.prototype.setName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span> (<span class="hljs-params">name, age, price</span>) </span>&#123;
  B.call(<span class="hljs-built_in">this</span>, name, age)
  <span class="hljs-built_in">this</span>.price = price
&#125;

A.prototype = <span class="hljs-keyword">new</span> B ()
A.prototype.constructor = A

A.prototype.setPrice = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">price</span>) </span>&#123;
<span class="hljs-built_in">this</span>.price = price
&#125;

<span class="hljs-keyword">var</span> sub = <span class="hljs-keyword">new</span> A()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：
调用了两次B()：一次是B.call()；一次是new B()</p>
<h4 data-id="heading-19">寄生组合继承</h4>
<p>Object.create 方法，这个方法接收两个参数：一是用作新对象原型的对象、二是为新对象定义额外属性的对象（可选参数）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">B</span> (<span class="hljs-params">name, age</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
&#125;
B.prototype.setName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
&#125;
t
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span> (<span class="hljs-params">name, age, price</span>) </span>&#123;
  B.call(<span class="hljs-built_in">this</span>, name, age)
  <span class="hljs-built_in">this</span>.price = price
&#125;

<span class="hljs-comment">// 第一种写法 </span>
<span class="hljs-comment">// 创建一个对象&#123;&#125;，并且把对象的_proto_赋值为Object.create 的参数 </span>
<span class="hljs-comment">// A.prototype.__proto__ = B.prototype</span>
A.prototype = <span class="hljs-built_in">Object</span>.create(B.prototype, &#123;<span class="hljs-attr">consturctor</span>: A&#125;)

<span class="hljs-comment">// 第二种写法</span>
<span class="hljs-comment">//var F = function () &#123; &#125; //核心代码</span>
<span class="hljs-comment">//F.prototype = B.prototype; //核心代码</span>
<span class="hljs-comment">//A.prototype = new F();</span>
<span class="hljs-comment">//A.prototype.contructor = A</span>

A.prototype.setPrice = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">price</span>) </span>&#123;
<span class="hljs-built_in">this</span>.price = price
&#125;

<span class="hljs-keyword">var</span> sub = <span class="hljs-keyword">new</span> A()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">ES6 Class类</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> </span>&#123;
    <span class="hljs-keyword">static</span> mood = <span class="hljs-string">'good'</span>  <span class="hljs-comment">// 静态属性</span>
    <span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
        <span class="hljs-built_in">this</span>.money = <span class="hljs-number">1000000</span>
    &#125;
    
    buybuybuy () &#123;
        <span class="hljs-built_in">this</span>.money -= <span class="hljs-number">100</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'money'</span>, <span class="hljs-built_in">this</span>.money)
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">B</span> </span>&#123;
<span class="hljs-built_in">super</span>()
&#125;    

<span class="hljs-keyword">var</span> a1 = <span class="hljs-keyword">new</span> A()
a1.buybuybuy()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">7. 执行上下文（Execution Context）</h3>
<p>浏览器获取到源代码后，主要做了几个事情：</p>
<ul>
<li>分词/词法分析（）：将代码进行分割，生成token；</li>
<li>解析/语法分析（）：按照语法将token转换成AST抽象语法树；</li>
<li>可执行代码：解析器生成字节码，逐行解释执行，分析器监控热点代码，编译器将热点代码编译为机器码。</li>
</ul>
<h4 data-id="heading-22">什么是执行上下文？</h4>
<p>执行上下文，又称执行上下文环境。执行上下文分为三种类型：</p>
<ul>
<li>全局执行上下文：程序开始时，会创建全局执行上下文，并压入执行栈中。</li>
<li>函数执行上下文：当函数被调用时创建函数执行上下文，并将函数压入执行栈中。</li>
<li>eval执行上下文：eval函数专有的执行上下文。</li>
</ul>
<p>执行上下文分两个阶段：创建阶段和执行阶段。</p>
<h4 data-id="heading-23">创建阶段</h4>
<p>执行上下文主要由两部分组成：词法环境和变量环境。</p>
<h5 data-id="heading-24">词法环境(LexicalEnvironment)</h5>
<p>词法环境分类：全局、函数、模块</p>
<p>词法环境构成：</p>
<ul>
<li>
<p>环境记录（Environment Record）：存放、初始化变量</p>
<pre><code class="copyable"> 声明式环境记录（Declarative Environment Record）: 存放直接用标识符定义的元素，比如const let声明的变量

 对象式环境记录（Object Environment Record）：主要用于with的语法环境。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>外部环境(Outer)：创建作用域链，访问父词法作用域的引用</p>
</li>
<li>
<p>thisBinding：确定当前环境中this的指向</p>
</li>
</ul>
<h5 data-id="heading-25">变量环境(variableEnvironment)</h5>
<p>也是一个词法环境。主要的区别在于通过var 声明的变量以及函数声明存放在变量环境。</p>
<p>简单来说，执行上下文创建阶段主要做了三件事情：</p>
<ol>
<li>初始化变量、函数、形参</li>
<li>创建作用域链</li>
<li>绑定this</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">executionContext = &#123;
    <span class="hljs-attr">variableObject</span>: &#123;
    <span class="hljs-attr">arguments</span>: &#123;
&#125;,
      <span class="hljs-attr">name</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">getData</span>: <span class="hljs-literal">undefined</span>
    &#125;,  <span class="hljs-comment">// 初始化变量、函数、形参</span>
    <span class="hljs-attr">scopeChain</span>: &#123;&#125;,  <span class="hljs-comment">// 创建作用域链</span>
    <span class="hljs-attr">this</span>: &#123;&#125; <span class="hljs-comment">// 绑定this</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">执行阶段</h4>
<p>执行阶段主要做了两件事：</p>
<ol>
<li>分配变量、函数的引用、赋值</li>
<li>执行代码</li>
</ol>
<p><strong>变量提升 vs 暂时性死区</strong>
var声明的变量以及函数声明，在执行上下文创建阶段，已经初始化完成，并赋值为undefined，代码未执行到var赋值行，也可以访问var定义的变量，值为undefined，这种现象被称作变量提升</p>
<p>相反，由const、let声明的变量，在词法环境中，初始化时会被置为标志位，在代码没执行到let、const赋值行时，提前读取变量会报错，这个特性叫做暂时性死区。</p>
<h4 data-id="heading-27">执行上下文栈</h4>
<p>浏览器的JS解释器是单线程的，相当于浏览器在同一时间只能做一件事。
代码中只有一个全局执行上下文，和无数个函数执行上下文，组成了执行上下文栈。
一个函数的执行上下文，在函数执行完毕后会被移除执行栈。</p>
<h3 data-id="heading-28">8. 作用域</h3>
<p>作用域的主要用途是隔离变量和函数，并控制它们的生命周期。主要分为三种类型：</p>
<ul>
<li>全局作用域</li>
<li>函数作用域</li>
<li>块级作用域</li>
</ul>
<p>作用域是在执行上下文创建时定义的，不是在代码执行时创建的，因此又称为词法作用域。</p>
<h4 data-id="heading-29">词法作用域 vs 动态作用域</h4>
<p>词法作用域语动态作用域的区别是，词法作用域是执行上下文创建阶段阶段就定义的，动态作用域是指代码执行阶段创建的。
为了更好的理解JS采用的是词法作用域，看一下例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> name = <span class="hljs-string">'xuna'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getName</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(name)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getName1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> name = <span class="hljs-string">'na.xu'</span>
    <span class="hljs-keyword">return</span> getName()
&#125;
getName1() <span class="hljs-comment">// xuna</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">作用域链</h4>
<p>当一个函数嵌套另一个函数时，在当前执行上下文环境的词法环境和变量环境的环境记录（Environment Record）中无法找到某个变量，就会通过外部环境(Outer)去访问父词法作用域，如果还没找到，就一层一层向上寻找，直到找到该变量或抵达全局作用域为止，这样的链式关系称为作用域链。</p>
<h3 data-id="heading-31">9. 闭包</h3>
<p>闭包一般发生在函数嵌套时，内部函数访问外部函数的变量。
高级程序设计三中：闭包是指有权访问另一个函数作用域中的变量的函数，可以理解为（能够读取其他函数内部变量的函数）
再理解一下：
一个函数执行完，被弹出执行栈，当前执行上下文中不能直接访问被弹出栈的函数的词法作用域，而另一个函数中还保留了对该函数词法作用域的引用，这个引用就是闭包。</p>
<h4 data-id="heading-32">闭包的应用</h4>
<h5 data-id="heading-33">封装私有变量</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">var</span> money = <span class="hljs-number">10000</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-title">buy</span>(<span class="hljs-params"></span>)</span> &#123;
  money -= <span class="hljs-number">1</span>
  &#125;
&#125;

<span class="hljs-keyword">var</span> person = <span class="hljs-keyword">new</span> Person()
person.buy() <span class="hljs-comment">// money为person的私有变量，只能通过buy（）修改</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-34">缓存数据</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getDataList</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">let</span> data = <span class="hljs-literal">null</span>
  <span class="hljs-keyword">return</span> &#123;
  <span class="hljs-function"><span class="hljs-title">getData</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span>(data) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(data)
      <span class="hljs-keyword">return</span> fetch().then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> data = res.json())
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">const</span> list = getDataList()
list.getData()
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-35">柯里化</h5></div>  
</div>
            