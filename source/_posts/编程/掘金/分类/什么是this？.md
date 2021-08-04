
---
title: '什么是this？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5478'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 06:35:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=5478'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第N天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>在我们平常的学习工作中，经常会遇到<strong>this</strong> ，那么到底什么是this你真的搞懂了吗？在JavaScript中，this是一个很复杂的关键字，也是特别烦人的，很多人都会被this搞的晕头转向。下面这篇文章我们就来介绍一下this到底是什么？</p>
</blockquote>
<h1 data-id="heading-0">什么是this？</h1>
<blockquote>
<p><strong>this</strong> 是JavaScript中的一个关键词，在JavaScript中，this不是固定不变的，它会随着执行环境的改变而改变。实际上this就是一个指针，它最终指向调用函数的那个对象。</p>
</blockquote>
<p>通常this的指向分为很多种情况，下面我们一一 来介绍：</p>
<h2 data-id="heading-1">1. 默认情况（默认绑定）</h2>
<p><strong>默认的this</strong></p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// window，这里不区分严格模式和非严格模式，都是指向window</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在默认情况下，this指向window</p>
<p><strong>函数中的this</strong></p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);<span class="hljs-comment">//非严格模式指向window，严格模式指向undefined</span>
&#125;
fn();

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在严格模式下，函数中的this是undefined，但是在非严格模式下，函数中的this指向window</p>
<h2 data-id="heading-2">2. 隐式绑定</h2>
<p><strong>对象方法中的this</strong></p>
<p>1.如果函数调用是在一个对象上触发的，即存在上下文对象，那么这个函数中的this指向调用函数的对象</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello,'</span>, <span class="hljs-built_in">this</span>.name);
&#125;
<span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'jack'</span>,
    <span class="hljs-attr">sayHi</span>: sayHi
&#125;
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'bob'</span>;
person.sayHi(); <span class="hljs-comment">// Hello,jack</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.需要注意的是，在对象的属性链中，只有最后一个属性会影响函数中的this。（就近原则）</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello,'</span>, <span class="hljs-built_in">this</span>.name);
&#125;
<span class="hljs-keyword">var</span> person2 = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'jack'</span>,
    <span class="hljs-attr">sayHi</span>: sayHi
&#125;
<span class="hljs-keyword">var</span> person1 = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'bob'</span>,
    <span class="hljs-attr">friend</span>: person2
&#125;
person1.friend.sayHi();<span class="hljs-comment">// Hello,jack</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>回调函数中的this</strong></p>
<p>1.普通回调函数中</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">f</span>)</span>&#123;
    f();
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
&#125;
fn(fn1);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，fn1被作为回调函数调用，回调函数中的this指向和默认绑定的一样，在非严格模式下指向window，在严格模式下指向undefined。</p>
<p>promise中的.then回调也属于普通回调，同样遵循此规则。</p>
<p>2.特殊回调函数（定时器回调函数）</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
&#125;);
<span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); 
&#125;,<span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于定时器中的回调，不管是在严格模式还是非严格模式下，this稳定指向window。</p>
<p>3.数组遍历方法中的this</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>];
arr.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在数组的遍历方法中，传入的方法其实也是回调函数，如果在这个方法中不指定替代this对象时，同样非严格模式指向window，严格模式指向undefined。</p>
<p>4.事件回调函数</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">"click"</span>,clickhandler);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clickhandler</span>(<span class="hljs-params">e</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);<span class="hljs-comment">//侦听事件的对象</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在绑定事件的回调函数中，回调函数中的this指向被侦听事件的对象。上面的例子中，this就是document对象。</p>
<p>5.使用<em>arguments</em>关键字调用回调函数</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>]()
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);<span class="hljs-comment">//this指向fn中arguments</span>
&#125;
fn(fn1);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当在函数中通过arguments调用回调函数时，回调函数中的this指向Arguments对象。</p>
<h2 data-id="heading-3">3.call、apply、bind（显式绑定）</h2>
<p>call、apply、bind都可以通过传递参数来改变this的指向。</p>
<p>相同点：</p>
<ol>
<li>
<p>都可以通过传参改变this的指向，传递的第一个参数就是this</p>
</li>
<li>
<p>如果第一个参数传null或undefined，那么这些值都会被忽略，this的指向就会走默认绑定规则，非严格模式下指向window</p>
</li>
</ol>
<p>不同点：</p>
<ol>
<li>
<p>传参不同：<code>call( this，pra1,pra2,pra3 )</code>，call传递参数是一个一个传递，而apply第二个参数是一个数组 <code>apply( this，[pra1,pra2,pra3] )</code></p>
</li>
<li>
<p>call和apply在执行时会直接调用函数，而bind不会调用函数。</p>
</li>
</ol>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-built_in">document</span>.onclick = fn.call(obj); <span class="hljs-comment">// this改变为obj了，但是绑定的时候立即执行，当触发点击事件的时候执行的是fn的返回值undefined</span>
<span class="hljs-built_in">document</span>.onclick = fn.bind(obj); <span class="hljs-comment">// bind会把fn中的this预处理为obj，此时fn没有执行，当点击的时候才会把fn执行</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">4. new 绑定</h2>
<p>在JavaScript中，构造函数只是使用new操作符时被调用的普通函数，不属于某个类，也不会实例化一个类。所有的函数都可以通过new来调用，称为构造函数调用。</p>
<p>当使用new来调用函数的时候会自动执行以下操作：</p>
<p>    1. 创建一个空对象，构造函数中的this指向这个空对象</p>
<p>    2. 执行原型连接 <code>target.__proto__ = constructor.prototype</code></p>
<p>    3. 执行构造函数方法，属性和方法都被添加到this指向的对象上</p>
<p>    4. 如果构造函数中没有返回其他的对象，那么就返回this（即创建的这个新对象）；否则，返回构造函数中返回的对象。</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'jack'</span>;
&#125;;
<span class="hljs-keyword">let</span> person = <span class="hljs-keyword">new</span> Fn();
person.name<span class="hljs-comment">//jack</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这个例子中，这个过程就称为构造调用，this将指向新创建的对象person；</p>
<h2 data-id="heading-5">5.箭头函数绑定</h2>
<p>箭头函数是ES6新增的，它和普通函数有一些区别，箭头函数没有自己的this，它的this继承于当前函数执行上下文中的this。</p>
<p>在使用箭头函数时，有几点需要注意：</p>
<p>    1. 函数中的this，继承的是外层代码块中的this。</p>
<p>    2. 箭头函数不能作为构造函数使用new调用，否则会抛出错误。<code>TypeError: fn is not a constructor</code></p>
<p>    3. 不可以使用arguments对象，该对象在函数体内不存在。如果要用可以使用rest参数代替。</p>
<blockquote>
<p>Q：什么是rest参数？ rest 顾名思义，就是剩余的。下面看两个例子就懂了。</p>
</blockquote>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// 例1</span>
<span class="hljs-keyword">let</span> fn = <span class="hljs-function">(<span class="hljs-params">...vals</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(vals); <span class="hljs-comment">// [1, 2, 3]</span>
&#125;
fn(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>);
<span class="hljs-comment">// 例2</span>
<span class="hljs-keyword">let</span> fn = <span class="hljs-function">(<span class="hljs-params">name, ...vals</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(name); <span class="hljs-comment">// jack</span>
    <span class="hljs-built_in">console</span>.log(vals); <span class="hljs-comment">// [1, 2, 3]</span>
&#125;
fn(<span class="hljs-string">'jack'</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>    4. 不可以使用yield命令，所有箭头函数不能用作Generator函数。</p>
<p>    5. 箭头函数没有自己的this，所以不能用call、apply、bind这些方法去改变this的指向。</p>
<h2 data-id="heading-6">总结</h2>
<blockquote>
<p>this绑定无非就是分为几种场景：默认绑定、隐式绑定、显示绑定、new绑定、箭头函数绑定</p>
</blockquote>
<ol>
<li>默认绑定</li>
</ol>
<p>    默认绑定可以理解为<strong>函数调用时无任何调用前缀的场景</strong> ，默认绑定的情况下，this指向全局对象window（非严格模式），this指向undefined（严格模式）。</p>
<ol start="2">
<li>隐式绑定</li>
</ol>
<p>    如果函数调用时，前面存在调用它的对象，那么this就会隐式的绑定到这个对象上。如果函数调用前存在多个对象，this指向距离调用自己最近的对象</p>
<ol start="3">
<li>显示绑定</li>
</ol>
<p>    显示绑定就是通过call、apply、bind方法改变this指向。这三个方法传递的第一个参数就是最终的this指向。如果第一个参数是null或undefined，那么this将采用默认绑定的规则，指向全局对象。</p>
<ol start="4">
<li>new绑定</li>
</ol>
<p>    使用new绑定时，this指向新创建的那个对象。</p>
<ol start="5">
<li>箭头函数</li>
</ol>
<p>    箭头函数中没有this，箭头函数的this指向取决于外层作用域中的this，外层作用域或函数的this指向谁，箭头函数中的this便指向谁。</p>
<blockquote>
<p>看到最后，是不是感觉对this有了一定了解了，下面就在例题中检测一下吧。</p>
</blockquote>
<h2 data-id="heading-7">例题</h2>
<ol>
<li>例1</li>
</ol>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">10</span>,
  <span class="hljs-attr">c</span>: <span class="hljs-number">50</span>,
  <span class="hljs-attr">b</span>: &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">c</span>: <span class="hljs-built_in">this</span>.a,
    <span class="hljs-attr">run</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.c);
    &#125;
  &#125;
&#125;
obj.b.run();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>例2</li>
</ol>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> length = <span class="hljs-number">10</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.length);
&#125;
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">length</span>: <span class="hljs-number">5</span>,
  <span class="hljs-attr">method</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn</span>) </span>&#123;
    fn();
    <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>]();
  &#125;
&#125;
obj.method(fn, <span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>例3</li>
</ol>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> name = <span class="hljs-string">'222'</span>;
<span class="hljs-keyword">var</span> a = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'111'</span>,
    <span class="hljs-attr">say</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
    &#125;
&#125;
<span class="hljs-keyword">var</span> b = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'333'</span>,
    <span class="hljs-attr">say</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn</span>) </span>&#123;
        fn()
    &#125;
&#125;
a.say()
b.say(a.say)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>例4</li>
</ol>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-built_in">window</span>.number = <span class="hljs-number">2</span>;
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-string">'number'</span>: <span class="hljs-number">3</span>,
  <span class="hljs-string">'db1'</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
      <span class="hljs-built_in">this</span>.number *= <span class="hljs-number">4</span>;
      <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
          <span class="hljs-built_in">this</span>.number *= <span class="hljs-number">5</span>;
      &#125;
  &#125;)()
&#125;
<span class="hljs-keyword">var</span> db1 = obj.db1;
db1();
obj.db1();
<span class="hljs-built_in">console</span>.log(obj.number);
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>本文参考：
作者：刘小夕
链接：<a href="https://juejin.cn/post/6844903805587619854" target="_blank" title="https://juejin.cn/post/6844903805587619854">juejin.cn/post/684490…</a>来源：掘金</p></div>  
</div>
            