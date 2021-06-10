
---
title: '全面搞定 JavaScript 的继承 & 提升代码复用性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26396db914be4503a10a55645c01dee8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 19:40:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26396db914be4503a10a55645c01dee8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>继承是面向对象编程的一个重要部分。使用<strong>继承可以更好的复用以前开发的代码，缩短开发周期，提升开发效率</strong>。</p>
<h2 data-id="heading-0">继承的概念</h2>
<p>说一个经典的继承例子。</p>
<p>假设定义一个汽车的类，这个汽车颜色，品牌，样式，轮胎等，这些静态样式被称为这个汽车类的属性，汽车可以跑，跑这个动作被称为这个汽车类的方法，根据这个车的类又可以派生出 “轿车” 和 “货车”，给轿车添加一个后备箱的属性，再给货车添加一个大货箱，这样两个车是属于不同的两个类，但是他们都继承自汽车这个类。</p>
<p>从上面这个例子可以看出，轿车和货车这两个类都是继承自汽车这个类。</p>
<h2 data-id="heading-1">继承带来哪些便利呢？</h2>
<p>子类通过继承父类的属性和方法，子类获得了与父类同样的属性和方法，因此，子类不在需要重复定义与父类中公有的属性和方法。在子类继承父类的同时，也可以将父类的属性和方法进行重新定义，这样子类重写的方法就会覆盖父类中的方法，这被称为方法的重写。这样就使得子类拥有了和父类不同的属性或者方法。</p>
<p>接下来，我们送 ES5 和 ES6 实现继承的方式去讲解继承。</p>
<h2 data-id="heading-2">JavaScript 实现继承的几种方式</h2>
<h3 data-id="heading-3">1. 原型链继承</h3>
<h4 data-id="heading-4">原理</h4>
<p>实现原理：每一个构造函数都有一个原型对象，原型对象又包含一个指向构造函数的指针，而实例化对象又包含一个原型对象的指针。让子类构造函数原型对象的指针，指向父类构造函数实例对象的原型对象的指针，实现继承。</p>
<p><strong>简单来说就是，父类实例对象中有proto,是对象,叫原型，子类构造函数中有prototype属性,也是对象,也叫原型，由于原型中的方法是可以互相访问的。因此就是让子类构造函数的原型，指向父类实例对象的原型，就实现了原型链继承。</strong></p>
<h4 data-id="heading-5">实现代码：</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'Tom'</span>;
  <span class="hljs-built_in">this</span>.data = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.age = <span class="hljs-number">18</span>;
&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parent();
<span class="hljs-keyword">let</span> child = <span class="hljs-keyword">new</span> Child();
<span class="hljs-built_in">console</span>.log(child);   

<span class="hljs-comment">// 打印台输出</span>
<span class="hljs-comment">/*
Child
        age: 18
        __proto__: Parent
            data: (3) [1, 2, 3]
            name: "Tom"
        __proto__: Object
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26396db914be4503a10a55645c01dee8~tplv-k3u1fbpfcp-watermark.image" alt="原型链继承1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面的代码以及输出，可以看到 Child 构造函数，在原型上继承了 Parent 构造函数，并且拥有了它的属性。</p>
<h4 data-id="heading-6">缺点</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> child1 = <span class="hljs-keyword">new</span> Child();
<span class="hljs-keyword">let</span> child2 = <span class="hljs-keyword">new</span> Child();
child1.data.push(<span class="hljs-number">4</span>);
<span class="hljs-built_in">console</span>.log(child1.data);
<span class="hljs-built_in">console</span>.log(child2.data);

<span class="hljs-comment">// 打印台输出</span>
<span class="hljs-comment">/*
  [1, 2, 3, 4]
  [1, 2, 3, 4]
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，<strong>只改变了 child1 的data 数组的属性，但是child2 实例对象也跟着改变了</strong>。这是由于 两个实例使用的是同一个原型对象。它们的<strong>内存是共享的，因此当一个对象发生变化时，另一个也会随着发生变化，这是原型链继承的一个很大缺点</strong>。</p>
<p>接下来介绍一种能够避免原型属性共享问题的继承方式。</p>
<h3 data-id="heading-7">2. 构造函数继承（call，apply）</h3>
<h4 data-id="heading-8">原理</h4>
<p><strong>通过在子类里调用 call 或者 apply 方法，让子类构造函数直接指向父类构造函数。</strong></p>
<h4 data-id="heading-9">实现代码：</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'Tom'</span>;
  <span class="hljs-built_in">this</span>.data = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
&#125;
Parent.prototype.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">123</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>) </span>&#123;
  Parent.call(<span class="hljs-built_in">this</span>);
  <span class="hljs-built_in">this</span>.age = <span class="hljs-number">18</span>;
&#125;
<span class="hljs-keyword">let</span> child1 = <span class="hljs-keyword">new</span> Child();
<span class="hljs-keyword">let</span> child2 = <span class="hljs-keyword">new</span> Child();
child1.data.push(<span class="hljs-number">4</span>);
<span class="hljs-built_in">console</span>.log(child1);
<span class="hljs-built_in">console</span>.log(child2);

<span class="hljs-comment">// 控制台打印输出</span>
<span class="hljs-comment">/*
child1:
Child &#123;name: "Tom", data: Array(4), age: 18&#125;
        age: 18
        data: (4) [1, 2, 3, 4]
        name: "Tom"
        __proto__: Object
        
child2:
    Child &#123;name: "Tom", data: Array(3), age: 18&#125;
        age: 18
        data: (3) [1, 2, 3]
        name: "Tom"
        __proto__: Object
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e612ad39d84481cb0d0435a4fd3e507~tplv-k3u1fbpfcp-watermark.image" alt="call继承.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>从打印台输出，可以看出 Child 通过 call 方法，直接将 Parent 中的属性拿到自己身上，这样就实现了属性的继承。同时我们改变实例化传 child1 的 data 属性的值，child2 中的属性值并没有随着 child1 变化，也解决了原型链继承内存共享的问题。</strong></p>
<h4 data-id="heading-10">缺点</h4>
<p>Parent 的 <strong>原型上的say方法并没有被继承</strong>，这是因为 Child 实例化对象产生的 child1 原型还是指向自身。没有有继承 Parent 的原型链。</p>
<p>因此，我们将上面两种方式组合在一起使用，实现继承，下面我们来接着说一下！</p>
<h3 data-id="heading-11">3. 组合继承（上面两种继承方式的组合）</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'parent'</span>
  <span class="hljs-built_in">this</span>.num = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
&#125;

Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params"></span>) </span>&#123;
  Parent.call(<span class="hljs-built_in">this</span>)
  <span class="hljs-built_in">this</span>.age = <span class="hljs-number">18</span>
&#125;

Child.prototype = <span class="hljs-keyword">new</span> Parent()
Child.prototype.constructor = Child

<span class="hljs-keyword">const</span> c1 = <span class="hljs-keyword">new</span> Child()
<span class="hljs-keyword">const</span> c2 = <span class="hljs-keyword">new</span> Child()

c1.num.push(<span class="hljs-number">4</span>)

<span class="hljs-built_in">console</span>.log(c1.num);  <span class="hljs-comment">// -> [ 1, 2, 3, 4 ]</span>
<span class="hljs-built_in">console</span>.log(c2.num);  <span class="hljs-comment">// -> [ 1, 2, 3 ]</span>

<span class="hljs-built_in">console</span>.log(c1.getName());  <span class="hljs-comment">// -> parent</span>
<span class="hljs-built_in">console</span>.log(c2.getName());  <span class="hljs-comment">// -> parent</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>由上面的结果可知，通过call，继承没有出现属性的数据共享问题，在原型上继承方法，也可以正常使用。</strong></p>
<h3 data-id="heading-12">4. 原型式继承（Object.create）</h3>
<p><code>Object.create</code>这个方法接收两个参数：一是用作新对象原型的对象、二是为新对象定义额外属性的对象（可选参数）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> parent = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'tom'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
  <span class="hljs-attr">num</span>: [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>],
  <span class="hljs-attr">getName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;
&#125;

<span class="hljs-keyword">const</span> c1 = <span class="hljs-built_in">Object</span>.create(parent)

<span class="hljs-built_in">console</span>.log(c1.name);  <span class="hljs-comment">// tom</span>
c1.num.push(<span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(c1.num);   <span class="hljs-comment">// [ 1, 2, 3, 4 ]</span>

<span class="hljs-keyword">const</span> c2 = <span class="hljs-built_in">Object</span>.create(parent)
<span class="hljs-built_in">console</span>.log(c2.num);   <span class="hljs-comment">// [ 1, 2, 3, 4 ]</span>

<span class="hljs-built_in">console</span>.log(c2.getName()); <span class="hljs-comment">// tom</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由上面的结果可以看出，<code>Object.create</code> 实现对象的继承，与浅拷贝相似，引用类型的数据同样也发生了共享，但是可以实现方法的继承。</p>
<h3 data-id="heading-13">5. 寄生组合式继承</h3>
<p>前面使用原型链继承的方式，存在着调用父类构造函数的浪费。</p>
<p>接下来的方式在使用<code>Object.create</code> 的基础上，减少构造函数的调用，以达到最优继承。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clone</span>(<span class="hljs-params">parent, child</span>) </span>&#123;
  child.prototype = <span class="hljs-built_in">Object</span>.create(parent.prototype)
  child.prototype.constructor = child
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'tom'</span>,
  <span class="hljs-built_in">this</span>.num = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
&#125;

Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>) </span>&#123;
  Parent.call(<span class="hljs-built_in">this</span>)
&#125;

clone(Parent, Child)

<span class="hljs-keyword">const</span> c1 = <span class="hljs-keyword">new</span> Child()
<span class="hljs-keyword">const</span> c2 = <span class="hljs-keyword">new</span> Child()

c1.num.push(<span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(c1.num);  <span class="hljs-comment">// [ 1, 2, 3, 4 ]</span>
<span class="hljs-built_in">console</span>.log(c2.num);  <span class="hljs-comment">// [ 1, 2, 3 ]</span>

<span class="hljs-built_in">console</span>.log(c1.getName());  <span class="hljs-comment">// tom</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>Object.create</code> 实现方法继承，不会共享的原因是因为函数在调用过程中，谁调用函数，函数的<code>this</code>就会指向谁所以不存在通用的结果。</strong></p>
<h3 data-id="heading-14">6. ES6 的 extends 实现继承</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name
  &#125;
  <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name)
    <span class="hljs-built_in">this</span>.age = age
  &#125;
&#125;

<span class="hljs-keyword">const</span> child = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'tom'</span>, <span class="hljs-number">18</span>)

<span class="hljs-built_in">console</span>.log(child);  <span class="hljs-comment">// &#123; name: 'tom', age: 18 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ES6 extends 继承方式也是采用 寄生组合式 的继承方式。</strong></p></div>  
</div>
            