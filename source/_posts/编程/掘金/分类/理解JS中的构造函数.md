
---
title: '理解JS中的构造函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3686'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 20:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3686'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">JavaScript中的构造函数</h1>
<h2 data-id="heading-1">理解构造函数模式</h2>
<h3 data-id="heading-2">为什么要使用构造函数模式</h3>
<ul>
<li>首先我们看看使用工厂模式创建对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createPerson</span>(<span class="hljs-params">name,age</span>)</span>&#123;
    <span class="hljs-keyword">let</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
    o.name = name;
    o.age = age;
    o.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
      &#125;
    <span class="hljs-keyword">return</span> o;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在这个例子中，使用工厂模式创建对象，每次可以用不同的参数调用此函数，每次都会返回两个属性和一个方法的对象</li>
<li>但是通过工厂模式无法解决对象标识问题(即新创建的对象是什么类型)，但<strong>构造函数模式</strong>可以解决这个问题</li>
</ul>
<h3 data-id="heading-3">通过构造函数模式创建对象</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name,age</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.age = age;
    <span class="hljs-built_in">this</span>.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
    &#125;
  &#125;

  <span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'simple'</span>,<span class="hljs-number">20</span>);
  <span class="hljs-keyword">let</span> person2 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'zywoo'</span>,<span class="hljs-number">19</span>);

  person1.sayName(); <span class="hljs-comment">//simple</span>
  person2.sayName(); <span class="hljs-comment">//zywoo</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">构造函数模式与工厂模式的区别</h3>
<ul>
<li>构造函数没有显示地创建对象</li>
<li>属性和方法直接赋值给this</li>
<li>没有return</li>
<li>注意：函数名Person的<strong>首字母为大写</strong>，按照惯例，构造函数名称的首字母都是要大写的，非构造函数则以小写字母开头</li>
<li>创建构造函数的实例前，需要使用new操作符</li>
</ul>
<h3 data-id="heading-5">new一个对象的过程</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">let</span> player = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"curry"</span>,<span class="hljs-number">33</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码的过程如下：</p>
<ol>
<li>在内存中创建一个新对象</li>
<li>这个新对象的内部 [[Prototype]] 特性被赋值为构造函数的prototype属性：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">  player.__proto__ = Person.prototype
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>构造函数内部的this被赋值给新的对象 也就是新对象和函数调用的this会绑定起来</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">  Person.call(player,<span class="hljs-string">"curry"</span>,<span class="hljs-number">30</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>执行构造函数内部的代码 即给新对象添加属性和方法</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">  player.name;
  player.age;
  player.sayName();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>如果构造函数返回非空对象，则返回该对象；否则，返回刚创建的新对象</li>
</ol>
<h2 data-id="heading-6">构造函数与普通函数</h2>
<ul>
<li>构造函数与普通函数唯一的区别就是<strong>调用方式不同</strong>。除此之外，<strong>构造函数也是函数</strong>。并没有把某个函数定义为构造函数的特殊语法。任何函数只要使用 new 操作符调用就是构造函数，而不使用 new 操作符调用的函数就是普通函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 作为构造函数</span>
  <span class="hljs-keyword">let</span> person = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'simple'</span>,<span class="hljs-number">20</span>);
  person.sayName(); <span class="hljs-comment">// simple</span>

  <span class="hljs-comment">// 作为普通函数调用</span>
  Person(<span class="hljs-string">'zywoo'</span>,<span class="hljs-number">19</span>); <span class="hljs-comment">// 添加到window对象</span>
  <span class="hljs-built_in">window</span>.sayName(); <span class="hljs-comment">// zywoo</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在上述例子中，作为普通函数调用时，结果会将属性和方法添加到window对象</li>
<li>在调用一个函数而没有明确设置 this 值的情况下（即没有作为对象的方法调用，或者没有使用 call() / apply() 调用），this 始终指向 Global 对象（在浏览器中就是 window 对象）</li>
</ul>
<h2 data-id="heading-7">构造函数的问题</h2>
<ul>
<li>通过构造函数定义的方法会在每个实例上都创建一遍，但它们做的都是同一件事情</li>
<li>可以通过把函数定义转移到构造函数外部</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name,age</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.age = age;
    <span class="hljs-built_in">this</span>.sayName = sayName;
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayName</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在上面这个例子中，sayName() 被定义在了构造函数外部。在构造函数内部， sayName 属性等于全局 sayName()函数。因为这一次 sayName 属性中包含的只是一个指向外部函数的指针</li>
<li>这样虽然解决了相同逻辑的函数重复定义的问题，但全局作用域也因此被搞乱了，因为那个函数实际上只能在一个对象上调用</li>
<li>要想解决这个问题，可以使用<strong>原型模式</strong>来解决</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            