
---
title: '重学JS(2)_继承'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6395'
author: 掘金
comments: false
date: Fri, 30 Apr 2021 03:34:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=6395'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在上一篇文章中重新梳理了原型链，原型链一个重要的应用场景就是继承，继承是面向对象编程中的一个概念，简单来说就是子类继承父类的特征和行为，使得子类具有父类的属性和方法，这种编程思想也使得代码的可复用性、可读性和可维护性大大提升，是目前大型前端项目架构设计中不可或缺的一种编程思想。</p>
<h2 data-id="heading-0">ES5中的继承</h2>
<p>在传统的面向对象编程语言，如Java中，继承分为接口继承和实现继承。但是在JavaScript中没有类似于Java中的方法签名，所以JS中的函数是没有重载的，也没有接口继承，下面介绍的几种JS继承方式都是实现继承。</p>
<ol>
<li>原型链继承</li>
<li>经典继承</li>
<li>组合继承</li>
<li>原型式继承</li>
<li>寄生式继承</li>
<li>寄生组合式继承</li>
</ol>
<h3 data-id="heading-1">原型链继承</h3>
<p>由上一篇专栏可知，在JS的原型链中，构造函数A有<code>prototype</code>属性指向其原型对象，其原型对象有<code>constructor</code>属性指回构造函数，其实例有<code>__proto__</code>属性指向A的原型对象。<strong>当A的原型对象为另外一个构造函数B的实例时，就说明实例可以通过原型链访问到B的原型对象上的方法，这就是原型链继承的思想</strong>，用代码表现如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'parent'</span>
    <span class="hljs-built_in">this</span>.sex = <span class="hljs-string">'male'</span>
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name, <span class="hljs-built_in">this</span>.sex)
&#125; 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'Child'</span> <span class="hljs-comment">// 由于原型层级的原因会覆盖</span>
    <span class="hljs-built_in">this</span>.age = <span class="hljs-number">18</span>
&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parent() <span class="hljs-comment">// 原型链继承关键步骤</span>
Child.prototype.constructor = Child <span class="hljs-comment">// 恢复原型对象的constructor指针</span>
Child.prototype.getAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.age)
&#125;
<span class="hljs-keyword">const</span> instance = <span class="hljs-keyword">new</span> Child();
instance.getName(); <span class="hljs-comment">// Child male</span>
instance.getAge(); <span class="hljs-comment">// 18</span>

<span class="hljs-comment">// 原型链继承会保持实例instanceof和PrototypeOf的特性</span>
<span class="hljs-built_in">console</span>.log(instance <span class="hljs-keyword">instanceof</span> Child) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(instance <span class="hljs-keyword">instanceof</span> Parent) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(instance <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>

<span class="hljs-built_in">console</span>.log(Child.prototype.isPrototypeOf(instance)) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(Parent.prototype.isPrototypeOf(instance)) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.isPrototypeOf(instance)) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>原型链中存在的问题</strong>：子类在实例化时无法向父类的构造函数传参，这样就意味着父类构造函数里添加的属性只能是静态值，无法进行动态设置。另外原型链继承的方式会导致子类共享父类中的引用类型的属性，可以看下面的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.fruits = [<span class="hljs-string">'apple'</span>, <span class="hljs-string">'orange'</span>]
&#125;
Parent.prototype.getFruits = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.fruits)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parent()
<span class="hljs-keyword">const</span> instance1 = <span class="hljs-keyword">new</span> Child();
<span class="hljs-keyword">const</span> instance2 = <span class="hljs-keyword">new</span> Child();

instance1.fruits.push(<span class="hljs-string">'banana'</span>)
instance2.fruits.push(<span class="hljs-string">'cherry'</span>)

instance1.getFruits() <span class="hljs-comment">// ["apple", "orange", "banana", "cherry"]</span>
instance2.getFruits() <span class="hljs-comment">// ["apple", "orange", "banana", "cherry"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到<code>instance1</code>和<code>instance2</code>同时修改了父类里的<code>fruits</code>属性，由于原型链继承方式存在这两种问题，导致这种继承方式几乎不会被单独使用</p>
<h3 data-id="heading-2">经典继承(盗用构造函数继承)</h3>
<p>为了避免原型链继承中共用父类属性的问题，<strong>经典继承的思想就是在子类的构造函数中调用父类的构造函数，使父类构造函数在子类的上下文中运行</strong>，可以看下面的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">favorites</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.fruits = [<span class="hljs-string">'apple'</span>, <span class="hljs-string">'orange'</span>]
    <span class="hljs-built_in">this</span>.favorites = favorites
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">favorites</span>)</span>&#123;
    Parent.call(<span class="hljs-built_in">this</span>, favorites)
&#125;
Child.prototype.getFruits = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.fruits, <span class="hljs-built_in">this</span>.favorites)
&#125;
<span class="hljs-keyword">const</span> instance1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'banana'</span>)
<span class="hljs-keyword">const</span> instance2 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'cherry'</span>)

instance1.fruits.push(<span class="hljs-string">'banana'</span>)
instance2.fruits.push(<span class="hljs-string">'cherry'</span>)

instance1.getFruits() <span class="hljs-comment">// ["apple", "orange", "banana"] "banana"</span>
instance2.getFruits() <span class="hljs-comment">// ["apple", "orange", "cherry"] "cherry"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<code>call()</code>或者<code>apply()</code>方法使父类构造函数在子类上下文中执行，使得每个子类都独自拥有<code>fruits</code>属性。并且，通过经典继承的方式，可以在调用构造函数时传入参数执行。</p>
<p><strong>经典继承中存在的问题</strong>：经典继承方式中只能将属性和方法写在构造函数里，因此导致无法重用，并且实例也无法调用父类原型对象中的方法，所以这些问题导致经典继承的方式也不会被单独使用</p>
<h3 data-id="heading-3">组合继承(伪经典继承)</h3>
<p>组合继承结合了原型链继承和经典继承的优点，其<strong>思想是利用原型链继承的方式继承父类原型对象上的方法，用经典继承的方式继承父类中的属性</strong>，可以看下面例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">favorites</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.fruits = [<span class="hljs-string">'apple'</span>, <span class="hljs-string">'orange'</span>]
    <span class="hljs-built_in">this</span>.favorites = favorites
&#125;
Parent.prototype.getFavorites = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.favorites)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">favorites</span>)</span>&#123;
    Parent.call(<span class="hljs-built_in">this</span>, favorites) <span class="hljs-comment">// 使用了经典继承的特性</span>
&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parent(); <span class="hljs-comment">// 使用了原型链继承的特性</span>
Child.prototype.constructor = Child <span class="hljs-comment">// 恢复原型对象的constructor指针</span>
Child.prototype.getFruits = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.fruits)
&#125;

<span class="hljs-keyword">const</span> instance1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'banana'</span>)
<span class="hljs-keyword">const</span> instance2 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'cherry'</span>)

instance1.fruits.push(<span class="hljs-string">'banana'</span>)
instance2.fruits.push(<span class="hljs-string">'cherry'</span>)

<span class="hljs-comment">// 可以看到实例都独自继承拥有了fruits属性</span>
instance1.getFruits() <span class="hljs-comment">// ["apple", "orange", "banana"] </span>
instance2.getFruits() <span class="hljs-comment">// ["apple", "orange", "cherry"] </span>
<span class="hljs-comment">// 实例能够使用父类原型对象上的方法</span>
instance1.getFavorites() <span class="hljs-comment">// banana</span>
instance2.getFavorites() <span class="hljs-comment">// cherry</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组合继承的方式弥补了原型链继承和经典继承方式的不足，并且通过组合继承方式创建的实例，能够保留<code>instanceof</code>和<code>isPrototypeOf()</code>判断之间关系的能力，组合继承也是JS中广发使用的一种继承方式。</p>
<h4 data-id="heading-4">原型式继承</h4>
<p>Douglas Crockford在文章《Prototypal Inheritance in JavaScript》中介绍了原型式继承的思想，在文章中给出了一个函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">object</span>(<span class="hljs-params">o</span>)</span>&#123;
    <span class="hljs-comment">// 首先创建一个临时构造函数</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
    <span class="hljs-comment">// 临时构造函数的原型对象赋值为传进来的对象</span>
    F.prototype = o
    <span class="hljs-comment">// 用临时构造函数创建一个实例并返回</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> F()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看下面使用时的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> superMarket = &#123;
     <span class="hljs-attr">owner</span>: <span class="hljs-string">'ashun'</span>,
     <span class="hljs-attr">fruits</span>: [<span class="hljs-string">'apple'</span>, <span class="hljs-string">'orange'</span>],
     <span class="hljs-function"><span class="hljs-title">getInfo</span>(<span class="hljs-params"></span>)</span>&#123;
         <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.owner, <span class="hljs-built_in">this</span>.fruits)
     &#125;
 &#125;
 
 <span class="hljs-keyword">const</span> familyMart = object(superMarket)
 <span class="hljs-comment">// 由于原型层级，会遮盖原型对象上的简单属性</span>
 familyMart.owner = <span class="hljs-string">'tom'</span>
 <span class="hljs-comment">// 引用类型的属性会被共享</span>
 familyMart.fruits.push(<span class="hljs-string">'banana'</span>)
 <span class="hljs-comment">// 可以使用原型对象上的方法</span>
 familyMart.getInfo()
 
 <span class="hljs-keyword">const</span> walMart = object(superMarket)
 walMart.owner = <span class="hljs-string">'Jack'</span>
 walMart.fruits.push(<span class="hljs-string">'cherry'</span>)
 walMart.getInfo()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原型式继承适用于这种情况，你已经有一个对象，但你想在这个对象的基础上增强这个对象的能力或者修改这个对象的属性，此时可以使用原型式继承，把已有对象传给<code>obejct()</code>，然后在返回的新对象中修改共享属性和调用共享方法。原型模式非常适合不想单独定义一个构造函数，但仍然需要共享数据的情况。但是需要注意的时，如果共享的是引用类型的数据，在修改时修改的会是同一份数据。
在ES5中提出了<code>Object.create()</code>方法，把原型式继承规范化了，在上面的例子中将object替换成为<code>Object.create</code>即可。</p>
<h4 data-id="heading-5">寄生式继承</h4>
<p>寄生式继承结合了原型式继承和工厂模式的思想，创建一个实现继承的工厂方法函数，在函数中增强原始对象并返回，可以看下面这个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 实现一个寄生式继承的工厂函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createSuperMarket</span>(<span class="hljs-params">originMarket</span>)</span>&#123;
    <span class="hljs-keyword">let</span> inner = <span class="hljs-built_in">Object</span>.create(originMarket)
    originMarket.getOwner = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.owner)
    &#125;
    <span class="hljs-keyword">return</span> inner
&#125;
<span class="hljs-comment">// 原始对象</span>
<span class="hljs-keyword">const</span> superMarket = &#123;
    <span class="hljs-attr">owner</span>: <span class="hljs-string">'ashun'</span>,
    <span class="hljs-attr">fruits</span>: [<span class="hljs-string">'apple'</span>, <span class="hljs-string">'orange'</span>],
    <span class="hljs-function"><span class="hljs-title">getInfo</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.owner, <span class="hljs-built_in">this</span>.fruits)
    &#125;
&#125;
<span class="hljs-keyword">const</span> familyMart = createSuperMarket(superMarket)
<span class="hljs-comment">// 增强了getOwner()方法</span>
familyMart.getOwner() <span class="hljs-comment">// ashun</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与原型式继承一样，寄生式继承适合不想单独创建构造函数，但仍然想共享方法和属性的场景，但是通过寄生式继承给原始对象添加函数会导致函数难以复用，使用场景比较窄</p>
<h4 data-id="heading-6">寄生组合式继承</h4>
<p>在解释这个继承方式之前，我们再来回顾一下组合继承的实现代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">favorites</span>)</span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>)</span>&#123;
    Parent.call(<span class="hljs-built_in">this</span>) <span class="hljs-comment">// 第二次调用Parent()</span>
&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parent() <span class="hljs-comment">// 第一次调用Parent()</span>
<span class="hljs-keyword">const</span> instance = <span class="hljs-keyword">new</span> Child()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到在组合继承方式中，父类构造函数Parent()被调用了两次，如果在<code>parent()</code>中定义了属性和方法，结果会导致在<code>instance</code>和<code>Child.prototype</code>上都会被赋予这些属性和方法，但是由于原型层级的原型，始终会使用<code>instance</code>上的属性和方法，造成了<code>Child.prototype</code>上相同的属性和方法的冗余（本来也不希望使用<code>Child.prototype</code>上面的方法）
使用寄生组合式继承可以优化这一问题，其思想是不通过调用父类的构造函数给子类原型对象赋值，而是取得父类原型对象的一个副本，赋予子类原型对象，可以看下面例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inheritPrototype</span>(<span class="hljs-params">parent, child</span>)</span>&#123;
    <span class="hljs-comment">// 复制一份父类原型对象的副本</span>
    <span class="hljs-keyword">const</span> prototype = <span class="hljs-built_in">Object</span>.create(parent.prototype)
    <span class="hljs-comment">// 修复constructor指针</span>
    prototype.constructor = child
    <span class="hljs-comment">// 将父类原型对象的副本赋给子类原型对象</span>
    child.prototype = prototype
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">favorites</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.fruits = [<span class="hljs-string">'apple'</span>, <span class="hljs-string">'orange'</span>]
    <span class="hljs-built_in">this</span>.favorites = favorites
&#125;
Parent.prototype.getFavorites = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.favorites)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">favorites</span>)</span>&#123;
    Parent.call(<span class="hljs-built_in">this</span>, favorites) <span class="hljs-comment">// 使用了经典继承的特性</span>
&#125;
inheritPrototype(Parent, Child) <span class="hljs-comment">// 使用寄生组合式继承代替组合继承</span>
Child.prototype.getFruits = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.fruits)
&#125;
<span class="hljs-keyword">const</span> instance1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'banana'</span>)
<span class="hljs-keyword">const</span> instance2 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'cherry'</span>)

instance1.fruits.push(<span class="hljs-string">'banana'</span>)
instance2.fruits.push(<span class="hljs-string">'cherry'</span>)
<span class="hljs-comment">// 可以看到实例都独自继承拥有了fruits属性</span>
instance1.getFruits() <span class="hljs-comment">// ["apple", "orange", "banana"] </span>
instance2.getFruits() <span class="hljs-comment">// ["apple", "orange", "cherry"] </span>
<span class="hljs-comment">// 实例能够使用父类原型对象上的方法</span>
instance1.getFavorites() <span class="hljs-comment">// banana</span>
instance2.getFavorites() <span class="hljs-comment">// cherry</span>

<span class="hljs-comment">// 可以看到使用寄生组合式继承时子类原型对象上没有多余的属性和方法</span>
<span class="hljs-built_in">console</span>.log(Child.prorotype) <span class="hljs-comment">// Parent &#123;constructor: ƒ, getFruits: ƒ&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用寄生组合式继承相比于组合继承，只调用一次父类构造函数，去掉了子类原型对象上冗余的属性和方法，提升了组合继承的性能和效率，同时，寄生组合式继承仍然可以使用<code>instanceof</code>和<code>isPrototypeOf()</code>方法来获取实例、子类构造函数和父类构造函数之间的关系。</p>
<h2 data-id="heading-7">ES6中的继承</h2>
<p>ES6中新增了class和extends关键字，它们其实是语法糖，ES6原生支持单继承，其实现方式和思想仍然是原型链。</p></div>  
</div>
            