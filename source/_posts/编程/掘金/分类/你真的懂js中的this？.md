
---
title: '你真的懂js中的this？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4000'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 17:32:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=4000'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 为什么要用this？</h2>
<p><code>this</code>是<code>js</code>中最为复杂的机制之一。大部分开发者写了很久的<code>js</code>代码都可能没有主动使用过<code>this</code>，或者遇到就直接"忽略"，但其实<code>this</code>本质上提供了一种更加优雅的方式来传递对象引用，可以使代码更加简洁和易于复用，所以全面了解this是有必要的。</p>
<h2 data-id="heading-1">2. this的误解</h2>
<p>在学习<code>this</code>之前，先来说说它的两个误区。第一个就是<code>this</code>并不是指代本身，这里是因为用了词法作用域才会出现这样的理解；第二个就是<code>this</code>的绑定和声明没有任何关系，它取决于调用时候的条件。</p>
<h2 data-id="heading-2">3. this的理解</h2>
<p><code>this</code>的绑定是在调用的时候确定下来的，和声明没有任何关系。</p>
<h3 data-id="heading-3">3.1. this绑定规则（4个）</h3>
<p><code>this</code>绑定规则有四个，分别是：默认绑定，隐式绑定，显式绑定，new绑定。</p>
<h4 data-id="heading-4">3.1.1. 默认绑定</h4>
<p>独立函数调用，无法应用其他规则的时候使用的默认规则。这个规则根据会根据<code>严格模式</code>和<code>非严格模式</code>绑定不一样的值，严格模式<code>use strict</code>绑定的是<code>undefined</code>，而非严格模式绑定的是全局对象（浏览器就是<code>window</code>）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 非严格模式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
&#125;
foo(); <span class="hljs-comment">// window</span>


<span class="hljs-comment">// 严格模式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">    'use strict'</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
&#125;
bar(); <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">3.1.2. 隐式绑定</h4>
<p>第二个<code>this</code>绑定的规则就是<code>隐式绑定</code>，其实就是调用的位置是否有上下文对象。来看下面这个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;

<span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">foo</span>: foo
&#125;;

obj.foo(); <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里调用<code>foo</code>函数的方式是通过<code>obj.foo()</code>，使这个函数被调用的时候加上了<code>obj</code>这个上下文对象，<code>隐式绑定</code>这个规则会把函数中的this绑定到obj这个对象上，因此<code>this.a</code>和<code>obj.a</code>是一样的。</p>
<p><strong>多个层级引用</strong></p>
<p>大多数情况下，调用函数的层级都不是简单的一层，如果出现多层的话，函数中的<code>this</code>会绑定在哪一个对象上？例如：<code>obj1.obj2.obj3.foo()</code>，可以看下面的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;

<span class="hljs-keyword">var</span> obj2 = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">foo</span>: foo
&#125;;

<span class="hljs-keyword">var</span> obj1 = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">obj2</span>: obj2
&#125;;

<span class="hljs-comment">// 多个对象引用函数的this会绑定在上一层或者最后一层的属性上</span>
obj1.obj2.foo(); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子中的<code>foo</code>中的<code>this</code>绑定在<code>obj2</code>对象上，也就是说函数中的<code>this</code>绑定在上一层或者最后一层对象属性上。</p>
<p><strong>隐式丢失</strong></p>
<p><code>隐式绑定</code>还有一个比较常见的问题就是<code>this</code>绑定时会丢失绑定对象，这样<code>this</code>会应用<code>默认绑定</code>规则，绑定到全局对象或者<code>undefined</code>上，这取决于是否严格模式（<code>use strict</code>）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;

<span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">foo</span>: foo
&#125;;

<span class="hljs-keyword">var</span> f = obj.foo; <span class="hljs-comment">// 这里f是obj.foo的引用,引用的是foo函数本身</span>
f(); <span class="hljs-comment">// undefined; </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面例子中的<code>f</code>是<code>obj.foo</code>的引用，也就是<code>foo</code>函数本身，当执行<code>f</code>函数时，相当于直接执行<code>f()</code>，<code>foo</code>函数中的<code>this</code>应用默认绑定规则，把当前函数内的<code>this</code>绑定到全局对象上（<code>window</code>）。</p>
<p>这里还有一个关于<code>setTimeout</code>经典的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;

<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-string">'obj的a属性'</span>,
  <span class="hljs-attr">foo</span>: foo
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-string">'全局变量a'</span>;

<span class="hljs-built_in">setTimeout</span>(obj.foo, <span class="hljs-number">0</span>); <span class="hljs-comment">// '全局变量a'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里传入<code>setTimeout</code>的其实是<code>obj.foo</code>引用的函数本身，也就是<code>f</code>函数，那么这个时候也是应用<code>默认绑定</code>规则，函数里的<code>this</code>会绑定到全局对象上。其实回调函数丢失<code>this</code>绑定是非常常见的，所以在处理回调函数的<code>this</code>绑定时候要注意。</p>
<h4 data-id="heading-6">3.1.3. 显式绑定</h4>
<p>显式绑定一般使用的就是<code>apply</code>、<code>call</code>、<code>bind</code>这几个方法，其中<code>apply</code>和<code>call</code>都是调用函数并且把它的<code>this</code>绑定在方法的第一个参数上，这两个方法的区别在于其他参数上。而<code>bind</code>也会绑定<code>this</code>到第一个参数对象上，但并不执行该函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;

<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-string">'obj的a属性'</span>
&#125;;

foo.apply(obj); <span class="hljs-comment">// 'obj的a属性'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里使用<code>foo.apply(obj)</code>显式地绑定<code>foo</code>函数里面的<code>this</code>到<code>obj</code>对象上，<code>foo</code>函数里的<code>this.a</code>也就是<code>obj.a</code>。</p>
<p><strong>apply和call</strong></p>
<p><code>apply</code>和<code>call</code>通过第一个参数影响函数里面的<code>this</code>绑定，但有时候第一个参数并不是普通的对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.toFixed(<span class="hljs-number">2</span>));
&#125;

foo.apply(<span class="hljs-number">3</span>); <span class="hljs-comment">// 3.00</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>apply</code>方法里面的<code>3</code>明显不是对象，那在<code>apply</code>执行后，函数里面的<code>this</code>会被转换成<code>new Number(3)</code>，所以最终执行的就是<code>new Number(3).toFixed(2)</code>输出结果是<code>3.00</code>。<code>apply</code>和<code>call</code>如果第一个参数传入原始值（数字，字符串，布尔值）来绑定<code>this</code>对象，那么<code>this</code>绑定的当前值是（<code>new Number()</code>、<code>new Boolean()</code>、<code>new String()</code>） 。</p>
<p>还有一种特殊情况就是，<code>apply</code>和<code>call</code>第一个参数传入<code>null</code>和<code>undefined</code>，那么函数中的<code>this</code>绑定被忽略，使用<code>默认绑定</code>规则，<code>this</code>绑定在全局对象或者<code>undefined</code>（这个取决于是否严格模式）。</p>
<p><strong>bind</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">param</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a, param);
&#125;

<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-string">'obj的a属性'</span>
&#125;;

<span class="hljs-keyword">var</span> f = foo.bind(obj);
f(<span class="hljs-string">'f的参数'</span>); <span class="hljs-comment">// obj的a属性 f的参数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>bind()会返回一个新的函数，并且会为函数的this绑定到第一个参数上。</p>
<h4 data-id="heading-7">3.1.4. new绑定</h4>
<p>在<code>js</code>中，构造函数其实是使用<code>new</code>操作符时调用的函数，构造函数并不属于某个类，实际上也不会实例化一个类，构造函数就是一个使用<code>new</code>操作符调用的普通函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.a = a;
&#125;

<span class="hljs-keyword">var</span> f = <span class="hljs-keyword">new</span> Foo(<span class="hljs-number">1</span>);
<span class="hljs-built_in">console</span>.log(f.a); <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的<code>new</code>操作符调用<code>Foo()</code>函数时，内部会创建一个新的对象并把它绑定到<code>Foo()</code>调用的<code>this</code>上，如果这个函数没有其他返回值对象，那么函数就会自动返回这个新对象。</p>
<h3 data-id="heading-8">3.2. 箭头函数的this</h3>
<p>上面介绍的<code>this</code>绑定的四个规则已经可以包含所有“正常“的函数。但是ES6中的<code>箭头函数</code>却无法使用这些规则。箭头函数的<code>this</code>是根据外层作用域来决定的。来看看箭头函数的词法作用域：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
  &#125;
&#125;

<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-string">'obj的a属性'</span>
&#125;;

<span class="hljs-keyword">var</span> f = foo.call(obj);
f(); <span class="hljs-comment">// &#123;a: 'obj的a属性'&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的<code>f()</code>输出的并不是<code>window</code>全局对象，而是<code>obj</code>对象，因为在调用<code>foo</code>函数的时候使用了<code>call</code>方法显式绑定到<code>obj</code>属性上，而<code>foo</code>函数的返回值是箭头函数，那么这个返回的箭头函数里面的<code>this</code>绑定就是外层<code>foo</code>函数执行时绑定的<code>obj</code>对象上，所以这里的箭头函数的<code>this</code>最终绑定在obj对象上。</p></div>  
</div>
            