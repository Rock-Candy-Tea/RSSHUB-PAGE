
---
title: '面试：new的原理与实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8908'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 02:16:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=8908'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">定义</h2>
<blockquote>
<p><code>new</code> 运算符创建一个用户定义的对象类型的实例或具有构造函数的内置对象的实例。</p>
</blockquote>
<p>使用<code>new [constructor]</code>的方式来创建一个对象实例，但构造函数的差异会导致创建的实例不同。</p>
<h2 data-id="heading-1">构造函数体不同</h2>
<p>构造函数也是函数，其唯一的区别就是调用方式不同，任何函数只要使用 <code>new</code> 操作符调用就是构造函数，而不使用 <code>new</code> 操作符调用的函数就是普通函数。</p>
<p>因此构造函数也可以带有返回值，但是这会导致<code>new</code>的结果不同。</p>
<h3 data-id="heading-2">无返回值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
&#125;

<span class="hljs-keyword">let</span> obj = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"Jalenl"</span>);
<span class="hljs-built_in">console</span>.log(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然，打印的是<code>&#123;name:'Jalenl'&#125;</code></p>
<h3 data-id="heading-3">返回对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">age</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.age = age;
  <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"Jalenl"</span> &#125;;
&#125;

<span class="hljs-keyword">let</span> obj = <span class="hljs-keyword">new</span> Person(<span class="hljs-number">18</span>);
<span class="hljs-built_in">console</span>.log(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印的是<code>&#123;name:'Jalenl'&#125;</code>，也就是说<code>return</code>之前的定义都被覆盖了。这里<code>return</code>的是一个对象，那返回的是个基本类型呢？</p>
<h3 data-id="heading-4">返回非对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">age</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.age = age;
  <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
&#125;

<span class="hljs-keyword">let</span> obj = <span class="hljs-keyword">new</span> Person(<span class="hljs-number">18</span>);
<span class="hljs-built_in">console</span>.log(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回<code>&#123;age:21&#125;</code>,这么说<code>return</code>失效了，跟没有<code>return</code>一样的结果，那如果没有<code>this</code>绑定内部属性，再返回基本数据类型呢？</p>
<h3 data-id="heading-5">没有属性绑定+返回非对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
&#125;
<span class="hljs-keyword">new</span> Person()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回的是一个空对象<code>&#123;&#125;</code>，意料之中。</p>
<p><strong>综上，只有构造函数<code>return</code>返回的是一个对象类型时，才能改变初始结果。</strong></p>
<h2 data-id="heading-6">构造函数类型不同</h2>
<h3 data-id="heading-7">构造函数为普通函数</h3>
<p><code>ECMA-262 3rd. Edition Specification</code>中的说明了对象实例的创建过程：</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.interglacial.com%2Fjavascript_spec%2Fa-13.html%23a-13.2" target="_blank" rel="nofollow noopener noreferrer" title="http://www.interglacial.com/javascript_spec/a-13.html#a-13.2" ref="nofollow noopener noreferrer">13.2.2</a> <code>[[Construct]]</code></p>
<p>When the <code>[[Construct]]</code> property for a <code>Function</code> object <code>F</code> is called, the following steps are taken:</p>
<ol>
<li>Create a new native ECMAScript object.</li>
<li>Set the <a href="https://link.juejin.cn/?target=http%3A%2F%2Fbclary.com%2F2004%2F11%2F07%2F%23_Class_" target="_blank" rel="nofollow noopener noreferrer" title="http://bclary.com/2004/11/07/#_Class_" ref="nofollow noopener noreferrer"><code>[[Class]]</code></a> property of <code>Result(1)</code> to <code>"Object"</code>.</li>
<li>Get the value of the prototype property of <code>F</code>.</li>
<li>If <code>Result(3)</code> is an object, set the <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.interglacial.com%2Fjavascript_spec%2Fa-4.html%23a-4.3.5" target="_blank" rel="nofollow noopener noreferrer" title="http://www.interglacial.com/javascript_spec/a-4.html#a-4.3.5" ref="nofollow noopener noreferrer"><code>[[Prototype]]</code></a> property of <code>Result(1)</code> to <code>Result(3)</code>.</li>
<li>If <code>Result(3)</code> is not an object, set the <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.interglacial.com%2Fjavascript_spec%2Fa-4.html%23a-4.3.5" target="_blank" rel="nofollow noopener noreferrer" title="http://www.interglacial.com/javascript_spec/a-4.html#a-4.3.5" ref="nofollow noopener noreferrer"><code>[[Prototype]]</code></a> property of <code>Result(1)</code> to the original <code>Object</code> prototype object as described in <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.interglacial.com%2Fjavascript_spec%2Fa-15.html%23a-15.2.3.1" target="_blank" rel="nofollow noopener noreferrer" title="http://www.interglacial.com/javascript_spec/a-15.html#a-15.2.3.1" ref="nofollow noopener noreferrer">15.2.3.1</a>.</li>
<li>Invoke the <a href="https://link.juejin.cn/?target=http%3A%2F%2Fbclary.com%2F2004%2F11%2F07%2F%23a-13.2.1" target="_blank" rel="nofollow noopener noreferrer" title="http://bclary.com/2004/11/07/#a-13.2.1" ref="nofollow noopener noreferrer"><code>[[Call]]</code></a> property of <code>F</code>, providing <code>Result(1)</code> as the <code>this</code> value and providing the argument list passed into <code>[[Construct]]</code> as the argument values.</li>
<li>If <code>Type(Result(6))</code> is <code>Object</code> then return <code>Result(6)</code>.</li>
<li>Return <code>Result(1)</code>.</li>
</ol>
</blockquote>
<p>总结下来就是：</p>
<ol>
<li>在内存中创建一个新对象。</li>
<li>这个新对象内部的<code>[[Prototype]]</code>特性被赋值为构造函数的 <code>prototype</code> 属性。</li>
<li>构造函数内部的 <code>this</code> 被赋值为这个新对象（即 <code>this</code> 指向新对象）。</li>
<li>执行构造函数内部的代码（给新对象添加属性）。</li>
<li>如果构造函数返回对象，则返回该对象；否则，返回刚创建的新对象(空对象)。</li>
</ol>
<p>第五步就已经说明了构造函数不同导致<code>new</code>结果不同的原因。</p>
<p>以下摘自<code>MDN</code>的解释：</p>
<blockquote>
<p>当代码 new Foo(…) 执行时，会发生以下事情：</p>
<ol>
<li>一个继承自 Foo.prototype 的新对象被创建。</li>
<li>使用指定的参数调用构造函数 Foo，并将 this 绑定到新创建的对象。new Foo 等同于 new Foo()，也就是没有指定参数列表，Foo 不带任何参数调用的情况。</li>
<li>由构造函数返回的对象就是 new 表达式的结果。如果构造函数没有显式返回一个对象，则使用步骤1创建的对象。（<strong>一般情况下，构造函数不返回值，但是用户可以选择主动返回对象，来覆盖正常的对象创建步骤</strong>）</li>
</ol>
</blockquote>
<h3 data-id="heading-8">构造函数为箭头函数</h3>
<p>普通函数创建时，引擎会按照特定的规则为这个函数创建一个<code>prototype</code>属性（指向原型对象）。默认情况下，所有原型对象自动获得一个名为 <code>constructor</code> 的属性，指回与之关联的构造函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.age = <span class="hljs-number">18</span>;
&#125;
Person.prototype
<span class="hljs-comment">/**
&#123;
    constructor: ƒ Foo()
    __proto__: Object
&#125;
**/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建箭头函数时，引擎不会为其创建<code>prototype</code>属性，箭头函数没有<code>constructor</code>供<code>new</code>调用，因此使用<code>new</code>调用箭头函数会报错！</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Person = <span class="hljs-function">()=></span>&#123;&#125;
<span class="hljs-keyword">new</span> Person()<span class="hljs-comment">//TypeError: Foo is not a constructor</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">手写new</h2>
<p>综上，熟悉了<code>new</code>的工作原理后，我们可以自己实现一个低配版的<code>new</code>，实现的关键是：</p>
<ol>
<li>让实例可以访问到私有属性；</li>
<li>让实例可以访问构造函数原型（<code>constructor.prototype</code>）所在原型链上的属性；</li>
<li>构造函数返回的最后结果是引用数据类型。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_new</span>(<span class="hljs-params">constructor, ...args</span>) </span>&#123;
    <span class="hljs-comment">// 构造函数类型合法判断</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-title">constructor</span> !== '<span class="hljs-title">function</span>') &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'constructor must be a function'</span>);
    &#125;
    <span class="hljs-comment">// 新建空对象实例</span>
    <span class="hljs-keyword">let</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
    <span class="hljs-comment">// 将构造函数的原型绑定到新创的对象实例上</span>
    obj.__proto__ = <span class="hljs-built_in">Object</span>.create(<span class="hljs-title">constructor</span>.<span class="hljs-title">prototype</span>);
    <span class="hljs-comment">// 调用构造函数并判断返回值</span>
    <span class="hljs-keyword">let</span> res = <span class="hljs-title">constructor</span>.<span class="hljs-title">apply</span>(<span class="hljs-params">obj,  args</span>);
    <span class="hljs-keyword">let</span> isObject = <span class="hljs-keyword">typeof</span> res === <span class="hljs-string">'object'</span> && res !== <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">let</span> isFunction = <span class="hljs-keyword">typeof</span> res === <span class="hljs-string">'function'</span>;
    <span class="hljs-comment">// 如果有返回值且返回值是对象类型，那么就将它作为返回值，否则就返回之前新建的对象</span>
    <span class="hljs-keyword">return</span> isObject || isFunction ? res : obj;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个低配版<code>new</code>实现可以用来创建自定义类的实例，但不支持内置对象，毕竟<code>new</code>属于操作符，底层实现更加复杂。</p></div>  
</div>
            