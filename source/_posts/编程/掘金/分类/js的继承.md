
---
title: 'js的继承'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1208'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 01:29:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=1208'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1.原型链继承</h3>
<p>核心：</p>
<blockquote>
<p>将父类的<strong>实例</strong>作为子类的原型。</p>
</blockquote>
<p>优点：</p>
<ul>
<li>实现简单。</li>
</ul>
<p>缺点：</p>
<ul>
<li>包含引用类型值的原型属性会被所有实例共享，这会导致对一个实例的修改会影响另一个实例。</li>
<li>要想为子类新增属性和方法，必须在new Cat()这样的语句后执行，不能放在构造器中 如：在创建 Child 的实例时，不能向Cat传参。如果要加，只能在new Cat()以后加 由于这两个问题的存在，实践中很少单独使用原型链。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 原型链继承</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SuperType</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'zhangsan'</span>;
&#125;
SuperType.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SubType</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-comment">// 父类的实例作为子类的原型</span>
SubType.prototype = <span class="hljs-keyword">new</span> SuperType();

<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">let</span> instance1 = <span class="hljs-keyword">new</span> SubType();
instance1.sayName();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2.借用构造函数继承</h3>
<p>核心：</p>
<blockquote>
<p>用.call()或.apply()将父类构造函数引入子类函数，等于是复制父类的实例属性给子类。</p>
</blockquote>
<p>优点：</p>
<ul>
<li>1.只继承了父类构造函数的属性，没有继承父类原型的属性。</li>
<li>2.解决了原型链继承的两个缺点。</li>
<li>3.可以继承多个构造函数属性(call多个)</li>
<li>4.在子实例中可向父实例传参。</li>
</ul>
<p>缺点：</p>
<ul>
<li>1.只能继承父类构造函数的属性。</li>
<li>2.无法实现构造函数的复用。(每次用都需要重新调用)</li>
<li>3.每个新实例都有父类构造函数的副本，臃肿。所以借用构造函数继承很少单独使用。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 借用构造函数继承</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SuperType</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SubType</span>(<span class="hljs-params">name,age</span>) </span>&#123;
  SuperType.call(<span class="hljs-built_in">this</span>,name);
  <span class="hljs-built_in">this</span>.age = age;
&#125;

<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> SubType(<span class="hljs-string">'zhangsan'</span>,<span class="hljs-number">22</span>);
<span class="hljs-built_in">console</span>.log(person1.name);
<span class="hljs-built_in">console</span>.log(person1.age);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3.组合继承</h3>
<p>核心：</p>
<blockquote>
<p>通过构造函数实现对实例属性的继承，通过原型链实现对方法的继承。</p>
</blockquote>
<p>优点：</p>
<ul>
<li>1.可以继承父类原型上的属性，可以传参，可以复用。</li>
<li>2.每个新实例引入的构造函数属性是私有的。</li>
</ul>
<p>缺点：</p>
<ul>
<li>调用了两次(call一次，new一次)父类构造函数(耗内存)，子类的构造函数会代替原型上的那个父类构造函数。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 组合继承</span>
<span class="hljs-comment">// 父类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SuperType</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">'blue'</span>,<span class="hljs-string">'red'</span>];
&#125;
<span class="hljs-comment">// 父类方法</span>
SuperType.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
&#125;
<span class="hljs-comment">// 子类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SubType</span>(<span class="hljs-params">name,age</span>) </span>&#123;
  <span class="hljs-comment">// 继承属性 构造继承</span>
  SuperType.call(<span class="hljs-built_in">this</span>,name);
  <span class="hljs-built_in">this</span>.age = age;
&#125;
<span class="hljs-comment">// 继承方法 原型继承</span>
SubType.prototype = <span class="hljs-keyword">new</span> SuperType()
<span class="hljs-comment">// 子类方法</span>
SubType.prototype.sayAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.age);
&#125;

<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> SubType(<span class="hljs-string">'zhangsan'</span>,<span class="hljs-number">22</span>);
person1.sayName();
person1.sayAge();
person1.colors.push(<span class="hljs-string">'black'</span>);
<span class="hljs-built_in">console</span>.log(person1.colors);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4.原型式继承</h3>
<p>核心：</p>
<blockquote>
<p>ES5 Object.create的模拟实现，将传入的对象作为创建的对象的原型。</p>
</blockquote>
<p>优点：</p>
<ul>
<li>参考原型链继承</li>
</ul>
<p>缺点：</p>
<ul>
<li>参考原型链继承</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 原型式继承</span>
<span class="hljs-comment">// 先封装一个函数容器，用来输出对象和承载继承的原型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createObj</span>(<span class="hljs-params">o</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
  F.prototype = o; <span class="hljs-comment">// 继承了传入的参数</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> F(); <span class="hljs-comment">// 返回函数对象</span>
&#125;

<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">let</span> person = &#123;
  name： <span class="hljs-string">'zhangsan'</span>,
  <span class="hljs-attr">friends</span>: [<span class="hljs-string">'lisi'</span>,<span class="hljs-string">'wangwu'</span>]
&#125;
<span class="hljs-keyword">let</span> person1 = createObj(person);
<span class="hljs-keyword">let</span> person2 = createObj(person);
person1.name = <span class="hljs-string">'person1'</span>;
<span class="hljs-built_in">console</span>.log(person2.name);
person1.friends.push(<span class="hljs-string">'zhou'</span>);
<span class="hljs-built_in">console</span>.log(person2.friends);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5.寄生式继承</h3>
<p>核心：</p>
<blockquote>
<p>就是给原型式继承外面套了个壳子。</p>
</blockquote>
<p>优点：</p>
<ul>
<li>没有创建自定义类型，因为只是套了个壳返回对象，这个函数顺理成章就成了创建的新对象。</li>
</ul>
<p>缺点：</p>
<ul>
<li>跟借用构造函数模型一样，每次创建对象都会创建一遍方法。</li>
<li>没用到原型，无法复用。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 寄生式继承</span>
<span class="hljs-comment">// 在原型式的外面套了个函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createObj</span>(<span class="hljs-params">o</span>) </span>&#123;
  <span class="hljs-comment">// 这一步可以看做是原型式继承的简写</span>
  <span class="hljs-keyword">let</span> clone = <span class="hljs-built_in">Object</span>.create(o);
  <span class="hljs-comment">// 新增属性</span>
  clone.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hi'</span>);
  &#125;
  <span class="hljs-keyword">return</span> clone; <span class="hljs-comment">// 返回这个对象</span>
&#125;

<span class="hljs-comment">// 测试</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">child</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-keyword">let</span> child1 = createObj(child)
child1.sayName()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6.寄生组合式继承</h3>
<p>核心：</p>
<blockquote>
<p>使用寄生式继承来继承父类原型，然后将返回的新对象赋值给子类原型，寄生式组合继承可以算是引用类型继承的最佳模式。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 寄生组合式继承</span>
<span class="hljs-comment">// 父类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SuperType</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">'blue'</span>,<span class="hljs-string">'red'</span>];
&#125;
SuperType.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
&#125;
<span class="hljs-comment">// 子类</span>
<span class="hljs-keyword">function</span>.SubType(name,age) &#123;
  SuperType.call(<span class="hljs-built_in">this</span>,name);
  <span class="hljs-built_in">this</span>.age = age;
&#125;
<span class="hljs-comment">// 封装一个继承函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">extend</span>(<span class="hljs-params">subtype,supertype</span>) </span>&#123;
  <span class="hljs-keyword">let</span> prototype = <span class="hljs-built_in">Object</span>(supertype.prototype);
  prototype.constructor = subtype;
  subtype.prototype = prototype;
&#125;
<span class="hljs-comment">// 调用</span>
extend(SubType,SuperType)

<span class="hljs-comment">// 测试</span>
SubType.prototype.sayAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.age);
&#125;
<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> SubType(<span class="hljs-string">'zhangsan'</span>,<span class="hljs-number">22</span>);
person1.sayName();
person1.sayAge();
person1.colors.push(<span class="hljs-string">'black'</span>);
<span class="hljs-built_in">console</span>.log(person1.colors);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            