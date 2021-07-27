
---
title: '带你死磕面向对象，不懂那就再看一遍(或许你没有对象，但看完你可以自信的new一个)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3c0a836fa194375b824a66a2253b9a8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 23:05:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3c0a836fa194375b824a66a2253b9a8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" title="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<h3 data-id="heading-0">对象</h3>
<ul>
<li>对象是单个实物的<strong>抽象</strong></li>
<li>对象是一个容器，封装了<strong>属性</strong>和<strong>方法</strong></li>
<li>对象可以<strong>复用</strong>，通过<strong>继承机制</strong>还可以定制</li>
</ul>
<h3 data-id="heading-1">面向对象（OOP）</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3c0a836fa194375b824a66a2253b9a8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">面向对象做了什么？</h4>
<ul>
<li>将真实的世界中的各种复杂关系，抽象为一个个对象</li>
<li>由对象之间的分工与合作，完成对真实世界的抽象</li>
</ul>
<h4 data-id="heading-3">面向对象解决了什么问题？</h4>
<ul>
<li>具有<strong>灵活、代码可复用、高度模块化</strong>等特点，容易维护和开发</li>
<li>比起由一系列函数或指令组成的传统的过程式编程，更适合多人合作的大型软件项目</li>
</ul>
<h3 data-id="heading-4">构造函数</h3>
<h4 data-id="heading-5">什么是类？</h4>
<ul>
<li>典型的面向对象的语言（eg.c++和Java）中，都有类这个概念</li>
<li>类就是对象的模版，对象就是类的实例</li>
<li>类可以创建任意多个具有相同属性和方法的对象</li>
</ul>
<h4 data-id="heading-6">JS怎么实现"类"?</h4>
<ul>
<li>通过<strong>构造函数</strong>和<strong>原型链</strong></li>
</ul>
<h4 data-id="heading-7">什么是构造函数？</h4>
<ul>
<li>专门用来生成实例对象的函数</li>
<li>是对象的模版，描述实例对象的基本结构</li>
<li>一个构造函数，可以生成多个实例，而且这些实例对象都有相同的结构</li>
</ul>
<h4 data-id="heading-8">构造函数有何特点？</h4>
<pre><code class="copyable">var Vehicle = function (p) &#123;
  this.price = p;
&#125;;

var v = new Vehicle(500);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数体内部使用了this关键字，代表了所要生成的对象实例。</li>
<li>生成对象的时候，必须使用<span><code>new</code></span>命令。</li>
</ul>
<h4 data-id="heading-9">new命令做了什么？</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cd9e2ace10142a7aee1e722754df272~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>创建一个空对象，作为将要返回的对象实例</li>
</ol>
<blockquote>
<p>构造函数内部，this指的是一个新生成的空对象，所有针对this的操作，都会发生在这个空对象上。</p>
</blockquote>
<ol start="2">
<li>将这个空对象的原型，指向构造函数的prototype属性</li>
<li>将这个空对象赋值给函数内部的this关键字</li>
<li>开始执行构造函数内部的代码</li>
</ol>
<blockquote>
<p>如果构造函数内部有return语句，而且return后面跟着一个对象，new命令会返回return语句指定的对象；否则，就会不管return语句，返回this对象。</p>
</blockquote>
<pre><code class="copyable">// new的实现原理
function _new(/* 构造函数 */ constructor, /* 构造函数参数 */ params) &#123;
  // 将 arguments 对象转为数组
  var args = [].slice.call(arguments);
  // 取出构造函数
  var constructor = args.shift();
  // 创建一个空对象，继承构造函数的 prototype 属性
  var context = Object.create(constructor.prototype);
  // 执行构造函数
  var result = constructor.apply(context, args);
  // 如果返回结果是对象，就直接返回，否则返回 context 对象
  return (typeof result === 'object' && result != null) ? result : context;
&#125;

// 实例
var actor = _new(Person, '张三', 28);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">如果忘了使用new命令，直接调用构造函数会发生什么事？</h4>
<ul>
<li>this会指向全局</li>
</ul>
<h4 data-id="heading-11">new.target的作用是什么？</h4>
<ul>
<li>函数内部可以使用new.target属性</li>
<li>如果当前函数是new命令调用，new.target指向当前函数，否则为undefined</li>
<li>可以用来判断函数调用时是否使用了new命令</li>
</ul>
<pre><code class="copyable">function f() &#123;
  if (!new.target) &#123;
    throw new Error('请使用 new 命令调用！');
  &#125;
  // ...
&#125;

f() // Uncaught Error: 请使用 new 命令调用！
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">构造函数的缺点是什么？</h4>
<ul>
<li>同一个构造函数的多个实例之间，无法共享属性，从而造成对系统资源的浪费</li>
<li>解决方法==><strong>原型对象</strong></li>
</ul>
<h3 data-id="heading-13">原型对象&原型链</h3>
<h4 data-id="heading-14">什么是原型对象？</h4>
<ul>
<li>每个函数都有一个prototype属性，指向一个对象</li>
</ul>
<blockquote>
<p>对于普通函数来说，该属性基本无用。但是，对于构造函数来说，生成实例的时候，该属性会自动成为实例对象的原型</p>
</blockquote>
<ul>
<li>原型对象的属性不是实例对象自身的属性。只要修改原型对象，变动就立刻会体现在所有实例对象上</li>
</ul>
<blockquote>
<p>原型对象的作用，就是定义所有实例对象共享的属性和方法</p>
</blockquote>
<h4 data-id="heading-15">什么是原型链</h4>
<blockquote>
<p>所有对象都有自己的原型对象（prototype）。一方面，任何一个对象，都可以充当其他对象的原型；另一方面，由于原型对象也是对象，所以它也有自己的原型。因此，就会形成一个“原型链”（prototype chain）：对象到原型，再到原型的原型……</p>
</blockquote>
<ul>
<li>读取对象的某个属性时，JavaScript 引擎先寻找对象本身的属性，如果找不到，就到它的原型去找，如果还是找不到，就到原型的原型去找。如果直到最顶层的Object.prototype还是找不到，则返回undefined</li>
<li>原型链的尽头就是null</li>
</ul>
<h4 data-id="heading-16">constructor 属性到底是个啥？</h4>
<ul>
<li>prototype对象有一个constructor属性，默认指向<strong>prototype对象所在的构造函数</strong>，可以被所有实例对象继承</li>
</ul>
<pre><code class="copyable">function P() &#123;&#125;
P.prototype.constructor === P // true
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>constructor属性的作用是，可以得知某个实例对象，到底是哪一个构造函数产生的</li>
<li>有了constructor属性，就可以从一个实例对象新建另一个实例（间接调用</li>
</ul>
<pre><code class="copyable">function Constr() &#123;&#125;
var x = new Constr();
var y = new x.constructor();
y instanceof Constr // true

//在实例方法中，调用自身的构造函数成为可能
Constr.prototype.createCopy = function () &#123;
  return new this.constructor();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">instanceof 运算符有何作用？</h4>
<ul>
<li>instanceof运算符返回一个布尔值，表示对象是否为某个构造函数的实例</li>
</ul>
<h4 data-id="heading-18">构造函数如何实现继承？</h4>
<ol>
<li>第一步是在子类的构造函数中，调用父类的构造函数</li>
</ol>
<pre><code class="copyable">function Sub(value) &#123;
//Sub是子类的构造函数，this是子类的实例
//在实例上调用父类的构造函数Super，就会让子类实例具有父类实例的属性
  Super.call(this);
  this.prop = value;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>是让子类的原型指向父类的原型，这样子类就可以继承父类原型</li>
</ol>
<pre><code class="copyable">Sub.prototype = Object.create(Super.prototype);
Sub.prototype.constructor = Sub;
Sub.prototype.method = '...';
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>未完待续</p>
</blockquote>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwangdoc.com%2Fjavascript%2Foop%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://wangdoc.com/javascript/oop/index.html" ref="nofollow noopener noreferrer">了解面向对象编程</a></p>
</blockquote>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Fclass" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/#docs/class" ref="nofollow noopener noreferrer">es6 class您再瞅瞅</a></p>
</blockquote></div>  
</div>
            