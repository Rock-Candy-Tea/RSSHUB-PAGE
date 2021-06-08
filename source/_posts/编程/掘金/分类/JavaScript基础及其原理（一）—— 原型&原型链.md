
---
title: 'JavaScript基础及其原理（一）—— 原型&原型链'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee7e6444db7044e3b237eddc6048fce5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 20:10:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee7e6444db7044e3b237eddc6048fce5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>本文首发于笔者的<a href="https://github.com/aki-yuan/Blog" target="_blank" rel="nofollow noopener noreferrer">个人博客</a>，欢迎围观。</p>
<p>如果在阅读过程发现文章有表达不当的地方，还希望各位大佬在评论区多多指教。</p>
<h2 data-id="heading-1">为什么存在原型、原型链</h2>
<p>首先，我们先来看一个例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
  <span class="hljs-built_in">this</span>.eat = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;age&#125;</span>岁的<span class="hljs-subst">$&#123;name&#125;</span>正在吃饭`</span>)
  &#125;
&#125;

<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'aki'</span>, <span class="hljs-number">19</span>)
<span class="hljs-keyword">let</span> person2 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'aki'</span>, <span class="hljs-number">19</span>)

<span class="hljs-built_in">console</span>.log(person1 === person2)<span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么打印输出的结果是false呢？</p>
<p>因为对于同一个函数，我们通过 <code>new</code> 生成的实例，都会开辟出一个新的堆区，并且在每个实例上添加属性。所以在上述函数中，两个对象是不同的。</p>
<p>如果每生成一个对象都开辟一个新的堆区，很容易会造成<strong>内存不足</strong>的情况，而原型链&原型链就是来解决这个问题的，因为利用原型模式定义的属性和方法是有所有实例共享的，因此实例访问的都是相同的属性和函数。</p>
<p>我们不再需要在每个<strong>实例对象</strong>上添加属性，而是将属性添加在<strong>构造函数的原型对象</strong>上，这样一来，我们只需要通过<strong>原型链</strong>找到<strong>原型</strong>，实例对象就可以动态地获取构造函数的属性和方法。</p>
<p>如果上面那段话不是很好理解，那么接下来我将会通过例子理清各个概念以及它们之间的关系。</p>
<h2 data-id="heading-2">构造函数创建对象</h2>
<p>先使用构造函数创建一个对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;

&#125;
<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person()
person1.name = <span class="hljs-string">'aki'</span>
<span class="hljs-built_in">console</span>.log(person1)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，<code>Person</code> 作为一个构造函数，创建了一个实例对象 <code>person1</code>，很好理解吧？</p>
<h3 data-id="heading-3">prototype</h3>
<p>首先我们来讲讲<code>prototype</code>。在《JavaScript高级程序》一书中是这么说的：</p>
<blockquote>
<p>无论何时，只要创建一个函数，就会按照特定的规则为这个函数创建一个prototype属性（指向原型对象）。</p>
</blockquote>
<p>所以Person作为构造函数，也会有<code>prototype</code>属性指向实例原型，如下图所示。</p>
<p><a href="https://imgtu.com/i/2Nc1QU" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee7e6444db7044e3b237eddc6048fce5~tplv-k3u1fbpfcp-zoom-1.image" alt="2Nc1QU.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>那什么是原型呢？原型指的就是一个对象，实例“继承”那个对象的属性。在原型上定义的属性，通过“继承”，实例也拥有了这个属性。</p>
<p>“继承”这个行为是在 <code>new</code> 操作符内部实现的。</p>
<h3 data-id="heading-4">_<em>proto</em>_</h3>
<p>每一个JavaScript对象(除了 null )都具有的一个隐式属性<code>__proto__</code>，<code>__proto__</code> 属性会指向该对象的原型 <code>prototype</code> 。</p>
<p>可以用代码来证明这一点：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;
  
&#125;
<span class="hljs-keyword">let</span> person = <span class="hljs-keyword">new</span> Person()
<span class="hljs-built_in">console</span>.log(person.__proto__ === Person.prototype)<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图所示：</p>
<p><a href="https://pic.imgdb.cn/item/60bd72b9844ef46bb2c0e1a1.jpg" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/169b1c5c3fef47fda5e98d51b9ed0dbe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<h3 data-id="heading-5">constructor</h3>
<p>从上图不难发现，构造函数（函数）以及实例对象（对象）分别有一个 <code>prototype</code> 属性和 <code>__proto__</code> 属性指向实例对象的原型。</p>
<p>那么，原型是否存在指向构造函数（函数）或者是实例对象（对象）的属性呢？答案是有的，不过原型只有指向构造函数的属性，毕竟一个构造函数能够生成很多实例对象。这个属性就是 <code>constructor</code> 。</p>
<p>依然用代码来证明这一点：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;
  
&#125;
<span class="hljs-keyword">let</span> person = <span class="hljs-keyword">new</span> Person()
<span class="hljs-built_in">console</span>.log(Person.prototype.constructor === Person)<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们对上图进行补充，可以得到：</p>
<p><a href="https://pic.imgdb.cn/item/60bd76dc844ef46bb20a9dcb.jpg" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dabfcd72eb54aff85dc5dfa292dcabb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<blockquote>
<p>注意这里的 constructor 是原型的一个属性，Constructor 指的才是真正的构造函数。两者名字不要弄混了</p>
</blockquote>
<h2 data-id="heading-6">理解原型</h2>
<p>至此，我们已经了解了 <code>构造函数</code> 、 <code>实例对象</code> 、 <code>实例原型</code> 三者之间的关系：</p>
<blockquote>
<p>每个构造函数都有一个原型对象prototype，原型对象都包含一个指向构造函数的指针constructor，而实例（instance）都包含一个指向原型对象的内部指针_<em>proto</em>_</p>
</blockquote>
<p>多说无益，上代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
* 构造函数可以是函数表达式，也可以是函数声明。
* 所以下面两种形式都可以
* function Person() &#123;&#125;
* let Person = function() &#123;&#125;
* */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-comment">/*
* 声明之后，构造函数就有一个与之关联的原型对象
* */</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> Person.prototype)
<span class="hljs-built_in">console</span>.log(Person.prototype)

<span class="hljs-comment">/*
* 原型对象有一个 constructor 属性可以引用构造函数
* */</span>
<span class="hljs-built_in">console</span>.log(Person.prototype.constructor === Person)

<span class="hljs-comment">/*
* 正常的原型链都会终止于 Object 的原型对象
* Object 原型的原型是 null
* */</span>
<span class="hljs-built_in">console</span>.log(Person.prototype.__proto__ === <span class="hljs-built_in">Object</span>.prototype)
<span class="hljs-built_in">console</span>.log(Person.prototype.__proto__.constructor === <span class="hljs-built_in">Object</span>)
<span class="hljs-built_in">console</span>.log(Person.prototype.__proto__.__proto__ === <span class="hljs-literal">null</span>)

<span class="hljs-comment">/*
* 同一个构造函数创建的两个实例
* 共享同一个原型对象
* */</span>
<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person(),
    person2 = <span class="hljs-keyword">new</span> Person()
<span class="hljs-built_in">console</span>.log(person1.__proto__ === person2.__proto__)

<span class="hljs-comment">/* 
 * instanceof可以检查实例的原型链中是否包含指定构造函数的原型
 * */</span>
<span class="hljs-built_in">console</span>.log(person1 <span class="hljs-keyword">instanceof</span> Person)
<span class="hljs-built_in">console</span>.log(person1 <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)
<span class="hljs-built_in">console</span>.log(person1.prototype <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">参考书籍及文章</h2>
<p>《 JavaScript高级程序设计 》</p>
<p><a href="https://github.com/mqyqingfeng/Blog/issues/2" target="_blank" rel="nofollow noopener noreferrer">冴羽 —— JavaScript深入之从原型到原型链</a></p>
<p><a href="https://juejin.cn/post/6844903989088092174" target="_blank">妖精的尾巴 —— 轻松理解JS 原型原型链</a></p>
<h2 data-id="heading-8">占坑</h2>
<p>本系列（ JavaScript基础及其原理 ）预计共十七篇，暂未完结。</p>
<ul>
<li><a href="https://github.com/aki-yuan/Blog/issues/1" target="_blank" rel="nofollow noopener noreferrer">JavaScript基础及其原理（一）—— 原型链</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（二）—— 继承</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（三）—— 作用域</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（四）—— 闭包</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（五）—— 变量提升</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（六）—— this指向</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（七）—— 立即执行函数</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（八）—— instanceof原理</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（九）—— bind实现</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（十）—— apply和call</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（十一）—— 柯里化</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（十二）—— v8垃圾回收机制</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（十三）—— 浮点数精度</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（十四）—— new操作符</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（十五）—— 事件循环机制</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（十六）—— promise原理</a></li>
<li><a href="https://juejin.cn/post/6971268700645097503">JavaScript基础及其原理（十七）—— generator原理</a></li>
</ul></div>  
</div>
            