
---
title: 'Javascript原型，原型链，继承'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4149126ccfe45878de0123b5e7567d4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 17:46:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4149126ccfe45878de0123b5e7567d4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Javascript原型，原型链，继承</h1>
<p>原型和原型链是JavaScript中非常重要的知识点，理解原型首先要从JavaScript的对象入手，本文将逐步深入的讲解原型和原型链。</p>
<h2 data-id="heading-1">创建对象</h2>
<h3 data-id="heading-2">工厂模式</h3>
<p>工厂模式是软件工程中一种一种广泛的设计模式，这种模式抽象了创建具体对象的过程，开发人员就发明了一种函数，用函数来封装创建对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createPerson</span>(<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-keyword">var</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
  o.name = name;
  o.age = age;
  o.job = job;
  o.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name)
  &#125;
  <span class="hljs-keyword">return</span> o
&#125;
<span class="hljs-keyword">var</span> person1 = createPerson(<span class="hljs-string">"Nicholas"</span>, <span class="hljs-number">20</span>, <span class="hljs-string">"software engineer"</span>)
<span class="hljs-keyword">var</span> person2 = createPerson(<span class="hljs-string">"Greg"</span>, <span class="hljs-number">21</span>, <span class="hljs-string">"Doctor"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>工厂模式虽然解决了创建多个相似对象的问题，但却没有解决对象识别的问题（即怎么知道一个对象的类型），随着JavaScript的发展，又一个新的模式出现</p>
<h3 data-id="heading-3">构造函数模式</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.job = job
  <span class="hljs-built_in">this</span>.age = age
  <span class="hljs-built_in">this</span>.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name)
  &#125;
&#125;

<span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"Nicholas"</span>, <span class="hljs-number">20</span>, <span class="hljs-string">"software engineer"</span>)
<span class="hljs-keyword">var</span> person2 = <span class="hljs-keyword">new</span> Person(Greg<span class="hljs-string">", 21, "</span>Doctor)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子中除了用Person()函数取代了createPerson()函数，我们还注意到Person()中的代码除了与createPerson()相同的部分外，还存在如下不同之处：</p>
<ul>
<li>没有显式的创建对象</li>
<li>直接将属性和方法赋给了this</li>
<li>没有return语句</li>
</ul>
<p>创建自定义的构造函数意味着将来可以将它的实例标识为一种特定的类型，这也正是构造函数模式胜过工程模式的地方。</p>
<p>构造函数虽然好用，但也并非没有缺点，使用构造函数的主要问题就是，每个方法都要在实例上重新创建一遍，不同实例上的同名函数是不相等的，下面的代码可以证明这一点。</p>
<pre><code class="hljs language-js copyable" lang="js">alert(person1.sayName == person2.sayName); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">原型模式</h3>
<p>我们创建的每个函数都有一个prototype（原型）属性，这个属性是一个指针，指向一个对象，而这个对象的用途是包含可以由特定类型的所有实例共享的属性和方法，
如果按照字面意思来理解，那么prototype就是通过调用构造函数而创建的那个对象实例的原型对象，使用原型对象的好处是可以让所有对象实例共享它所包含的属性和方法，
换句话说，不必在构造函数中定义对象实例的信息，而是可以将这些信息直接添加到原型对象中，如下面例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;

&#125;

Person.prototype.name = <span class="hljs-string">"Nicholas"</span>;
Person.prototype.age = <span class="hljs-number">20</span>;
person.prototype.job = <span class="hljs-string">"software engineer"</span>;
Person.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  alert(<span class="hljs-built_in">this</span>.name)
&#125;

<span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person()
<span class="hljs-keyword">var</span> person2 = <span class="hljs-keyword">new</span> Person()
alert(person1.name == person2.name) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过调用构造函数来创建新对象，而且新对象还会具有相同的属性和方法，但于构造函数模式不同的是，新对象的这些属性和方法是由所有实例共享的，换句话说，
person1，person2访问的都是同一组属性和同一个sayName函数，要理解原型模式的工作原理必须先理解ECMAScript中原型对象的性质。</p>
<p><strong>下面重点来了</strong></p>
<p>理解原型对象</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4149126ccfe45878de0123b5e7567d4~tplv-k3u1fbpfcp-zoom-1.image" alt="alt 属性文本" loading="lazy" referrerpolicy="no-referrer"></p>
<p>无论什么时候，只要创建一个新函数，就会根据一组特定规则为该函数创建一个Prototype属性，这个属性指向函数的原型对象，在默认情况下，所有原型对象都会自动获得一个constructor属性，指向构造函数</p>
<p><strong>原型对象的问题</strong></p>
<p><strong>原型模式也不是没有缺点，首先，它省略了为构造函数传递初始化参数这一环节，结果所有实例在默认情况下都将取得相同的属性值，虽然这会在某种程度上带来一些不方便，但还不是原型最大的问题，原型模式最大的问题所在是由其共享的本质所导致的。</strong></p>
<p>原型中所有属性是被很多实例共享的，这种共享对函数来说非常合适，对于哪些包含基本值的属性倒也说得过去，通过在实例上添加一个同名属性，可以隐藏原型中的对应属性。然而，对于包含引用类型值的属性来说，问题就比较突出了，来看下面的例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;

&#125;

Person.prototype = &#123;
  <span class="hljs-attr">constructor</span>: Person,
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Nicholas"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>,
  <span class="hljs-attr">job</span>: <span class="hljs-string">"software engineer"</span>,
  <span class="hljs-attr">friends</span>: [<span class="hljs-string">"Shelby"</span>, <span class="hljs-string">"Court"</span>],
  <span class="hljs-attr">sayName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; alert(<span class="hljs-built_in">this</span>.name) &#125;
&#125;

<span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person()
<span class="hljs-keyword">var</span> person2 = <span class="hljs-keyword">new</span> Person()

person1.friends.push(<span class="hljs-string">"Van"</span>);

alert(person1.friends) <span class="hljs-comment">// "Shelby, Court Van"</span>
alert(person2.friends) <span class="hljs-comment">// "Shelby, Court Van"</span>
alert(person1.friends === preson2.friends) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Person.prototype对象有一个名为frends的属性，该属性是一个数组，然后创建了两个实例，接着，修改了person1.friends引用的数组，向数组中添加了一个字符串，由于friends存在于Person.prototype而非person1中，所以刚刚的修改也会通过person2.friends反映出来，假如我门的初衷就是所有实例共享一个数组，那么对这个结果没什么可说的。可是实例一般都是要有自己的全部属性，这也正是很少单独使用原型模式的原因所在。</p>
<p>组合使用构造函数模式和原型模式</p>
<p>创建自定义类型的最常用方式，就是组合使用构造函数模式于原型模式，构造函数模式用于定义实例属性，而原型模式用于定义方法和共享的属性，结果，每个实例都会有自己的一份实例属性的副本，但同时又共享着对方法的引用，最大限度地节省了内存，另外，这种混成模式还支持向构造函数传递参数，可谓是集两种模式之长。下面从写前面的例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
  <span class="hljs-built_in">this</span>.job = job
  <span class="hljs-built_in">this</span>.friends = [<span class="hljs-string">"Shelby"</span>, <span class="hljs-string">"Court"</span>]
&#125;

Person.prototype = &#123;
  <span class="hljs-attr">constructor</span>: Person,
  <span class="hljs-attr">sayName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name)
  &#125;
&#125;

<span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"Nicholas"</span>, <span class="hljs-number">20</span>, <span class="hljs-string">"software engineer"</span>)
<span class="hljs-keyword">var</span> person2 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"Greg"</span>, <span class="hljs-number">21</span>, <span class="hljs-string">"Doctor"</span>);
person1.friends.push(<span class="hljs-string">"Van"</span>)

alert(person1.friends) <span class="hljs-comment">// "Shelby, Court, Van"</span>
alert(person2.friends) <span class="hljs-comment">// "Shelby, Court"</span>
alert(person1.friends === person2.friends) <span class="hljs-comment">// false</span>
alert(person1.sayName === person2.sayName) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，实例属性都是在构造函数中定义的，而所有实例共享的属性constructor和方法sayName则是在原型中定义的，而修改person1.friends并不会影响到person2.friends，因为他们分别引用了不同的数组。</p>
<p>上半部分通过创建对象一步步的分析问题，解决问题，引出了原型的概念，下半部分将通过继承，引出原型链</p>
<h3 data-id="heading-5">继承</h3>
<p>ECMAScript中主要是靠原型链实现继承的</p>
<p>原型链</p>
<p>原型链的概念：每个构造函数都有一个原型对象，原型对象都包含一个指向构造函数的指针，而实例都包含一个指向原型对象的内部指针，那么，假如我们让原型对象等于另一个类型的实例，结果会怎样呢？显然，此时的原型对象将包含一个指向另一个原型的指针，响应地，另一个原型中也包含着一个指向另一个构造函数的指针，假如另一个原型又是另一个类型的实例，那么上述关系依然成立，如此层层递进，就构成了实例和原型的链条，这就是所谓的原型链的基本概念。</p>
<p>组合继承</p>
<p>组合继承也叫经典继承，指的是将原型链和借用构造函数的技术组合到一块，从而发挥二者之长的一种继承模式，其背后的思路是使用原型链实现对原型属性和方法的继承，而通过借用构造函数来实现对实例属性的继承，这样，既通过在原型上定义方法实现了函数的复用，又能保证每个实例都有它自己的属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SuperType</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">"red"</span>, <span class="hljs-string">"blue"</span>, <span class="hljs-string">"green"</span>]
&#125;

SuperType.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  alert(<span class="hljs-built_in">this</span>.name)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SubType</span>(<span class="hljs-params">name, age</span>) </span>&#123;
  SuperType.call(<span class="hljs-built_in">this</span>, name)
  <span class="hljs-built_in">this</span>.age = age
&#125;
SubType.prototype = <span class="hljs-keyword">new</span> SuperType()
SubType.prototype.constructor = SubType
SubType.prototype.sayAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  alert(<span class="hljs-built_in">this</span>.age)
&#125;

<span class="hljs-keyword">var</span> instance1 = <span class="hljs-keyword">new</span> SuperType(<span class="hljs-string">"Nicholas"</span>, <span class="hljs-number">20</span>)
instance1.colors.push(<span class="hljs-string">"black"</span>)
alert(instance1.colors) <span class="hljs-comment">// "red", "blue", "green", "black"</span>
instance1.sayName() <span class="hljs-comment">// "Nicholas"</span>
instance1.sayAge() <span class="hljs-comment">// 20</span>

<span class="hljs-keyword">var</span> instance2 = <span class="hljs-keyword">new</span> SuperType(<span class="hljs-string">"Greg"</span>, <span class="hljs-number">21</span>)
alert(instance2.colors) <span class="hljs-comment">// "red", "blue", "green"</span>
instance2.sayName() <span class="hljs-comment">// "Greg"</span>
instance2.sayAge() <span class="hljs-comment">// 21</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            