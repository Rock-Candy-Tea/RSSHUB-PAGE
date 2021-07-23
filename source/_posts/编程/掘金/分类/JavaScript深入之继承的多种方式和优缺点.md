
---
title: 'JavaScript深入之继承的多种方式和优缺点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5854'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 04:35:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=5854'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">1. 原型链继承</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'Kevin'</span>
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    consolo.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>)</span>&#123;

&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parent()
<span class="hljs-keyword">var</span> child1 = <span class="hljs-keyword">new</span> Child()
<span class="hljs-built_in">console</span>.log(child1.getName())    <span class="hljs-comment">//  Kevin</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题：</p>
<ol>
<li>引用类型的属性被所有实例共享，举个例子：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = [<span class="hljs-string">'Kevin'</span>,<span class="hljs-string">'daisy'</span>]
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>)</span>&#123;

&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parent();
<span class="hljs-keyword">var</span> chlid1 = <span class="hljs-keyword">new</span> Child()
child1.names.push(<span class="hljs-string">'Lucy'</span>)
<span class="hljs-built_in">console</span>.log(child1.names)   <span class="hljs-comment">//  ['Kevin','daisy','Lucy']</span>
<span class="hljs-keyword">var</span> child2 = <span class="hljs-keyword">new</span> Child()
<span class="hljs-built_in">console</span>.log(child2.names)     <span class="hljs-comment">//  ['Kevin','daisy','Lucy']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在创建Child实例时，不能向Parent传参</li>
</ol>
<p>重点：让新实例的原型等于父类的实例。</p>
<pre><code class="copyable">   特点：1、实例可继承的属性有：实例的构造函数的属性，父类构造函数属性，父类原型的属性。（新实例不会继承父类实例的属性！）
   缺点：1、新实例无法向父类构造函数传参。
       2、继承单一。
       3、所有新实例都会共享父类实例的属性。（原型上的属性是共享的，一个实例修改了原型属性，另一个实例的原型属性也会被修改！）
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-1">2. 构造函数继承（经典继承）</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.names = [<span class="hljs-string">'Kevin'</span>,<span class="hljs-string">'daisy'</span>]
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">name</span>)</span>&#123;
    Parent.call(<span class="hljs-built_in">this</span>,name)
&#125;
<span class="hljs-keyword">var</span> child1 = <span class="hljs-keyword">new</span> Child()
child1.names.push(<span class="hljs-string">'Lucy'</span>)
<span class="hljs-built_in">console</span>.log(child1.names)     <span class="hljs-comment">//  ['Kevin','daisy','Lucy']</span>
<span class="hljs-keyword">var</span> child2 = <span class="hljs-keyword">new</span> Child()
<span class="hljs-built_in">console</span>.log(child2.names)     <span class="hljs-comment">//  ['Kevin','daisy']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优点：</p>
<ol>
<li>避免了引用类型的属性被所有实例共享</li>
<li>可以在 Child 向 Parent 传参</li>
</ol>
<p>举个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">name</span>)</span>&#123;
    Parent.call(<span class="hljs-built_in">this</span>,name)
&#125;
<span class="hljs-keyword">var</span> child1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'Kevin'</span>)
<span class="hljs-built_in">console</span>.log(child1.name)       <span class="hljs-comment">//  Kevin</span>
<span class="hljs-keyword">var</span> child2 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'Lucy'</span>)
<span class="hljs-built_in">console</span>.log(child2.name)       <span class="hljs-comment">//   Lucy</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：</p>
<ol>
<li>方法都在构造函数中定义，每次创建实例都会创建一遍方法。</li>
<li>无法继承到超类原型上的属性（即_proto_和prototype）</li>
</ol>
<h5 data-id="heading-2">3. 组合继承</h5>
<p>原型链继承+构造函数继承</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name
    <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">'pink'</span>,<span class="hljs-string">'blue'</span>,<span class="hljs-string">'green'</span>]
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">name,age</span>)</span>&#123;
    Parent.call(<span class="hljs-built_in">this</span>,name)
    <span class="hljs-built_in">this</span>.age = age
&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parnet()
Child.prorototype.constructor = Child

<span class="hljs-keyword">var</span> child1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'Kevin'</span>,<span class="hljs-number">18</span>)
child1.colors.push(<span class="hljs-string">'orange'</span>)

<span class="hljs-built_in">console</span>.log(child1.name);       <span class="hljs-comment">// kevin</span>
<span class="hljs-built_in">console</span>.log(child1.age);        <span class="hljs-comment">// 18</span>
<span class="hljs-built_in">console</span>.log(child1.colors);        <span class="hljs-comment">// ["pink", "blue", "green", "orange"]</span>

<span class="hljs-keyword">var</span> child2 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'Lucy'</span>,<span class="hljs-number">18</span>)
<span class="hljs-built_in">console</span>.log(child2.name)       <span class="hljs-comment">//  Lucy</span>
<span class="hljs-built_in">console</span>.log(child2.age)       <span class="hljs-comment">//  18</span>
<span class="hljs-built_in">console</span>.log(child2.colors)      <span class="hljs-comment">//  ["pink","blue","green"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优点：融合原型链继继承和构造函数继承的优点，是 JavaScript 中最常用的继承模式</p>
<pre><code class="copyable">重点：用一个函数包装一个对象，然后返回这个函数的调用，这个函数就变成了个可以随意增添属性的实例或对象。object.create()就是这个原理。
    特点：类似于复制一个对象，用函数来包装。
    缺点：1、所有实例都会继承原型上的属性。
       2、无法实现复用。（新实例属性都是后面添加的）
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">4. 原型式继承</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createObj</span>(<span class="hljs-params">o</span>)</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
    F.prototype = o
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> F()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是 ES5 Object.create 的模拟实现，将传入的对象作为创建的对象的原型。
缺点：包含应用类型的属性值始终都会共享相应的值，这点跟原型链继承有点相似</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Person = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'kevin'</span>,
    <span class="hljs-attr">friends</span>:[<span class="hljs-string">'Lucy'</span>,<span class="hljs-string">'Jack'</span>]
&#125;

<span class="hljs-keyword">var</span> person1 = createObj(Person)
<span class="hljs-keyword">var</span> person2 = createObj(Person)

person1.name = <span class="hljs-string">'person1'</span>
<span class="hljs-built_in">console</span>.log(person1.name)   <span class="hljs-comment">//  Kevin</span>

person1.friends.push(<span class="hljs-string">'Kelly'</span>)
<span class="hljs-built_in">console</span>.log(person2.friends)   <span class="hljs-comment">//  ['Lucy','Jack','Kelly']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：修改 <code>person1.name</code> 的值，<code>person2.name</code> 的值并未发生改变，并不是因为 <code>person1</code> 和 <code>person2</code> 有独立的 <code>name</code> 值，而是因为 <code>person1.name = 'person1' </code> ，给 <code>person1</code> 增加了 <code>name</code> 值，并非修改了原型上的 <code>name</code> 值。</p>
<pre><code class="copyable">重点：用一个函数包装一个对象，然后返回这个函数的调用，这个函数就变成了个可以随意增添属性的实例或对象。object.create()就是这个原理。
    特点：类似于复制一个对象，用函数来包装。
      缺点：1、所有实例都会继承原型上的属性。
           2、无法实现复用。（新实例属性都是后面添加的
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">5. 寄生式继承</h5>
<p>创建一个仅用于封装继承过程的函数，该函数在内部以某种形式来做增强对象，最后返回对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createObj</span>(<span class="hljs-params">o</span>)</span>&#123;
    <span class="hljs-keyword">var</span> clone = <span class="hljs-built_in">Object</span>.create(o)
    clone.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hi'</span>)
    &#125;
    <span class="hljs-keyword">return</span> clone
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：跟借用构造函数模式一样，每次创建对象都会创建一遍方法。</p>
<pre><code class="copyable">重点：就是给原型式继承外面套了个壳子。
    优点：没有创建自定义类型，因为只是套了个壳子返回对象（这个），这个函数顺理成章就成了创建的新对象。
    缺点：没用到原型，无法复用。
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">6. 寄生组合式继承</h5>
<p>为了方便大家阅读，在这里重复一下组合继承的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name
    <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">'pink'</span>,<span class="hljs-string">'blue'</span>,<span class="hljs-string">'green'</span>]
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">name,age</span>)</span>&#123;
    Parent.call(<span class="hljs-built_in">this</span>,name)
    <span class="hljs-built_in">this</span>.age = age
&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parnet()
Child.prorototype.constructor = Child

<span class="hljs-keyword">var</span> child1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'Kevin'</span>,<span class="hljs-number">18</span>)
child1.colors.push(<span class="hljs-string">'orange'</span>)

<span class="hljs-built_in">console</span>.log(child1.name);       <span class="hljs-comment">// kevin</span>
<span class="hljs-built_in">console</span>.log(child1.age);   组合继承最大的缺点是会调用两次父构造函数。
一次是设置子类型实例原型的时候。
<span class="hljs-comment">// 18</span>
<span class="hljs-built_in">console</span>.log(child1.colors);        <span class="hljs-comment">// ["pink", "blue", "green", "orange"]</span>

<span class="hljs-keyword">var</span> child2 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'Lucy'</span>,<span class="hljs-number">18</span>)
<span class="hljs-built_in">console</span>.log(child2.name)       <span class="hljs-comment">//  Lucy</span>
<span class="hljs-built_in">console</span>.log(child2.age)       <span class="hljs-comment">//  18</span>
<span class="hljs-built_in">console</span>.log(child2.colors)      <span class="hljs-comment">//  ["pink","blue","green"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组合继承最大的缺点是会调用两次父构造函数。</p>
<p>一次是设置子类型实例的原型的时候。</p>
<pre><code class="copyable">Child.prototype = new Parent();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一次是在创建子类实例的时候</p>
<pre><code class="copyable">var child1 = new Child('Kevin','18')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回想下 new 的模拟实现，其实在这句中，我们回执行：</p>
<pre><code class="copyable">Parent.call(this,name)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里，我们又调用了一次 <code>Parent</code> 构造函数。
所以，在这个例子中，如果我们打印 child1 对象，我们会发现 <code>Child.prototype</code> 和 <code>child1</code> 都有一个属性为 <code>colors</code> ，属性值为 <code>['red', 'blue', 'green']</code> 。</p>
<p>那么我们该如何精益求精，避免这一次重复调用呢？</p>
<p>如果我们不使用 <code>Child.prototype = new Parent()</code> ，而是间接的让 <code>Child.prototype</code> 访问到 <code>Parent.prototype</code> 呢？
看看如何实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">'red'</span>, <span class="hljs-string">'blue'</span>, <span class="hljs-string">'green'</span>];
&#125;

Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params">name, age</span>) </span>&#123;
    Parent.call(<span class="hljs-built_in">this</span>, name);
    <span class="hljs-built_in">this</span>.age = age;
&#125;

<span class="hljs-comment">// 关键的三步</span>
<span class="hljs-keyword">var</span> F = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;;

F.prototype = Parent.prototype;

Child.prototype = <span class="hljs-keyword">new</span> F();


<span class="hljs-keyword">var</span> child1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'kevin'</span>, <span class="hljs-string">'18'</span>);

<span class="hljs-built_in">console</span>.log(child1);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们封装一下这个继承方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">object</span>(<span class="hljs-params">o</span>) </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
    F.prototype = o;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> F();
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">prototype</span>(<span class="hljs-params">child, parent</span>) </span>&#123;
    <span class="hljs-keyword">var</span> prototype = object(parent.prototype);
    prototype.constructor = child;
    child.prototype = prototype;
&#125;

<span class="hljs-comment">// 当我们使用的时候：</span>
prototype(Child, Parent);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方式的高效率体现它只调用了一次 Parent 构造函数，并且因此避免了在 Parent.prototype 上面创建不必要的、多余的属性。与此同时，原型链还能保持不变；因此，还能够正常使用 instanceof 和 isPrototypeOf。开发人员普遍认为寄生组合式继承是引用类型最理想的继承范式。</p>
<pre><code class="copyable">   重点：修复了组合继承的问题。
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            