
---
title: 'js基础之继承'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/535f4edd161d4a2584eef445bbc439cb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 18:54:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/535f4edd161d4a2584eef445bbc439cb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<blockquote>
<p>很多面向对象语言都支持两种继承：接口继承和实现继承。
前者只继承方法签名，后者继承实际的方法。
接口继承在 ECMAScript 中是不可能的，因为函数没有签名。
实现继承是 ECMAScript 唯一支持的继承方式，而这主要是通过原型链实现的。               <em>----js高级程序设计</em></p>
</blockquote>
<h2 data-id="heading-1">实现方式</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/535f4edd161d4a2584eef445bbc439cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">原型链</h3>
<p>每个构造函数都有一个原型对象，原型有一个属性指回构造函数，而实例有一个内部指针指向原型。如果原型是另一个类型的实例呢？那就意味着这个原型本身有一个内部指针指向另一个原型，相应地另一个原型也有一个指针指向另一个构造函数。这样就在实例和原型之间构造了一条原型链。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SuperType</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.property = <span class="hljs-literal">true</span>
  &#125;
  SuperType.prototype.getSuperValue = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.property
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SubType</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.subproperty = <span class="hljs-literal">false</span>
  &#125;
  <span class="hljs-comment">// 继承 SuperType</span>
  SubType.prototype = <span class="hljs-keyword">new</span> SuperType()
  SubType.prototype.getSubValue = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.subproperty
  &#125;
  <span class="hljs-keyword">let</span> instance = <span class="hljs-keyword">new</span> SubType()
  <span class="hljs-built_in">console</span>.log(instance.getSuperValue()) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SubType把原型赋值给了SuperType的实例， 而SuperType的实例能访问构造函数的所有属性和方法，意味着SubType也能访问，这就实现了SubType对SuperType的继承。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c89d55a91a3c4d81a55eabd875c963b4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>原型搜索机制</strong>：在读取实例上的属性时，首先会在实例上搜索这个属性。如果没找到，则会继承搜索实例的原型。在通过原型链实现继承之后，搜索就可以继承向上，搜索原型的原型，一直持续到原型链的末端。</p>
</blockquote>
<p><strong>缺点：</strong></p>
<ul>
<li>在原型中包含引用值的时候，引用值会在所有实例间共享。</li>
<li>子类型在实例化时不能给父类型的构造函数传参</li>
</ul>
<h3 data-id="heading-3">盗用构造函数</h3>
<p>为了解决原型包含引用值导致的继承问题，出现了一种叫作“盗用构造函数”的技术。
基本思路是在子类构造函数中调用父类构造函数。
解决了原型链的引用值共享和不能传参问题。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SuperType</span>(<span class="hljs-params">name</span>) </span>&#123;
 <span class="hljs-built_in">this</span>.name = name
 <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">"red"</span>, <span class="hljs-string">"blue"</span>, <span class="hljs-string">"green"</span>];
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SubType</span>(<span class="hljs-params"></span>) </span>&#123;
 <span class="hljs-comment">// 继承 SuperType</span>
 SuperType.call(<span class="hljs-built_in">this</span>, <span class="hljs-string">'shetia'</span>);
&#125;
<span class="hljs-keyword">let</span> instance1 = <span class="hljs-keyword">new</span> SubType();
<span class="hljs-built_in">console</span>.log(instance1.name)    <span class="hljs-comment">// "shetia"</span>
instance1.colors.push(<span class="hljs-string">"black"</span>);
<span class="hljs-built_in">console</span>.log(instance1.colors); <span class="hljs-comment">// "red,blue,green,black"</span>
<span class="hljs-keyword">let</span> instance2 = <span class="hljs-keyword">new</span> SubType();
<span class="hljs-built_in">console</span>.log(instance2.colors); <span class="hljs-comment">// "red,blue,green" </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>缺点</strong></p>
<ul>
<li>必须在构造函数中定义方法，因此函数不能重用。</li>
<li>子类也不能访问父类原型上定义的方法，因此所有类型只能使用构造函数模式。</li>
</ul>
<h3 data-id="heading-4">组合继承</h3>
<p>综合了原型链和盗用构造函数，将两者的优点集中了起来。</p>
<p>基本的思路是使用原型链继承原型上的属性和方法，而通过盗用构造函数继承实例属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SuperType</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">"red"</span>, <span class="hljs-string">"blue"</span>, <span class="hljs-string">"green"</span>];
&#125;
SuperType.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SubType</span>(<span class="hljs-params">name, age</span>)</span>&#123;
    <span class="hljs-comment">// 继承属性</span>
    SuperType.call(<span class="hljs-built_in">this</span>, name);
    <span class="hljs-built_in">this</span>.age = age;
&#125;
<span class="hljs-comment">// 继承方法</span>
SubType.prototype = <span class="hljs-keyword">new</span> SuperType();
SubType.prototype.sayAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.age);
&#125;;
<span class="hljs-keyword">let</span> instance1 = <span class="hljs-keyword">new</span> SubType(<span class="hljs-string">"Nicholas"</span>, <span class="hljs-number">29</span>);
instance1.colors.push(<span class="hljs-string">"black"</span>);
<span class="hljs-built_in">console</span>.log(instance1.colors); <span class="hljs-comment">// "red,blue,green,black"</span>
instance1.sayName(); <span class="hljs-comment">// "Nicholas";</span>
instance1.sayAge(); <span class="hljs-comment">// 29</span>
<span class="hljs-keyword">let</span> instance2 = <span class="hljs-keyword">new</span> SubType(<span class="hljs-string">"Greg"</span>, <span class="hljs-number">27</span>);
<span class="hljs-built_in">console</span>.log(instance2.colors); <span class="hljs-comment">// "red,blue,green"</span>
instance2.sayName(); <span class="hljs-comment">// "Greg";</span>
instance2.sayAge(); <span class="hljs-comment">// 27 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组合继承弥补了原型链和盗用构造函数的不足，是 JavaScript 中使用最多的继承模式。</p>
<h3 data-id="heading-5">原型式继承</h3>
<p>通过创建一个临时构造函数，把该构造函数原型赋值给传入的对象，再返回临时构造函数的一个实例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">object</span>(<span class="hljs-params">o</span>) </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;
    F.prototype = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> F();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Nicholas"</span>,
    <span class="hljs-attr">friends</span>: [<span class="hljs-string">"Shelby"</span>, <span class="hljs-string">"Court"</span>, <span class="hljs-string">"Van"</span>]
&#125;;
<span class="hljs-keyword">let</span> anotherPerson = object(person);
anotherPerson.name = <span class="hljs-string">"Greg"</span>;
anotherPerson.friends.push(<span class="hljs-string">"Rob"</span>);
<span class="hljs-keyword">let</span> yetAnotherPerson = object(person);
yetAnotherPerson.name = <span class="hljs-string">"Linda"</span>;
yetAnotherPerson.friends.push(<span class="hljs-string">"Barbie"</span>);
<span class="hljs-built_in">console</span>.log(person.friends); <span class="hljs-comment">// "Shelby,Court,Van,Rob,Barbie" </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ECMAScript 5 通过增加 Object.create()方法将原型式继承的概念规范化了。这个方法接收两个
参数：作为新对象原型的对象，以及给新对象定义额外属性的对象（第二个可选）。在只有一个参数时，
Object.create()与这里的 object()方法效果相同。</p>
<p>原型式继承非常适合不需要单独创建构造函数，但仍然需要在对象间共享信息的场合。</p>
<p>属性中包含的引用值始终会在相关对象间共享，跟使用原型模式是一样的。</p>
<h3 data-id="heading-6">寄生式继承</h3>
<p>与原型式继承类似：创建一个实现继承的函数，以某种方式增强对象，然后返回这个对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAnother</span>(<span class="hljs-params">original</span>)</span>&#123;
    <span class="hljs-keyword">let</span> clone = object(original); <span class="hljs-comment">// 通过调用函数创建一个新对象</span>
    clone.sayHi = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 以某种方式增强这个对象</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"hi"</span>);
    &#125;;
    <span class="hljs-keyword">return</span> clone; <span class="hljs-comment">// 返回这个对象</span>
&#125;
<span class="hljs-keyword">let</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Nicholas"</span>,
    <span class="hljs-attr">friends</span>: [<span class="hljs-string">"Shelby"</span>, <span class="hljs-string">"Court"</span>, <span class="hljs-string">"Van"</span>]
&#125;;
<span class="hljs-keyword">let</span> anotherPerson = createAnother(person);
anotherPerson.sayHi(); <span class="hljs-comment">// "hi" </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意 通过寄生式继承给对象添加函数会导致函数难以重用，与构造函数模式类似。</p>
</blockquote>
<h3 data-id="heading-7">寄生式组合继承</h3>
<p>为解决组合继承会调用两次是父类构造函数问题。</p>
<p>寄生式组合继承通过盗用构造函数继承属性，但使用混合式原型链继承方法。</p>
<p>基本思路是不通过调用父类构造函数给子类原型赋值，而是取得父类原型的一个副本。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inheritPrototype</span>(<span class="hljs-params">subType, superType</span>) </span>&#123;
    <span class="hljs-keyword">let</span> prototype = object(superType.prototype); <span class="hljs-comment">// 创建对象</span>
    prototype.constructor = subType; <span class="hljs-comment">// 增强对象</span>
    subType.prototype = prototype; <span class="hljs-comment">// 赋值对象</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SuperType</span>(<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">"red"</span>, <span class="hljs-string">"blue"</span>, <span class="hljs-string">"green"</span>];
&#125;
SuperType.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SubType</span>(<span class="hljs-params">name, age</span>) </span>&#123;
    SuperType.call(<span class="hljs-built_in">this</span>, name);
    <span class="hljs-built_in">this</span>.age = age;
&#125;
inheritPrototype(SubType, SuperType);
SubType.prototype.sayAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.age);
&#125;; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">总结</h2>
<p>原型链继承是通过重写构造函数原型为另一个构造函数实例实现继承。</p>
<p>盗用构造函数继承解决了原型链继承的引用值共享和不能传参问题。</p>
<p>组合继承综合了原型链继承和构造函数继承的优点，解决构造函数继承不能访问父类原型上的属性和方法问题。</p>
<p>原型式继承主要通过Object.create()。</p>
<p>寄生式继承增强了原型式继承。</p>
<p>寄生组合式继承解决组合继承调用两次父类构造函数问题。</p></div>  
</div>
            