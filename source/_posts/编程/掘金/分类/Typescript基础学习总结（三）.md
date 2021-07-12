
---
title: 'Typescript基础学习总结（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2799'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 05:24:24 GMT
thumbnail: 'https://picsum.photos/400/300?random=2799'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">6类类型-高效使用类型化的面向对象编程利器</h2>
<p>集面向对象抽象、封装、多态三要素为一体的编程利器，类类型。</p>
<p>在JavaScript（ES5）中仅支持通过函数和原型链继承模拟类的实现（用于抽象业务模型、组织数据结构并创建可重用组件），自 ES6 引入 class 关键字后，它才开始支持使用与Java类似的语法定义声明类。</p>
<h3 data-id="heading-1">6.1类</h3>
<p>任何实体都可以被抽象为一个使用类表达的类似对象的数据结构，且这个数据结构既包含属性，又包含方法。</p>
<p>如果使用传统的 JavaScript 代码定义类，我们需要使用函数+原型链的形式进行模拟，如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Dog</span>(<span class="hljs-params">name: string</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name; <span class="hljs-comment">// ts(2683) 'this' implicitly has type 'any' because it does not have a type annotation.</span>
&#125;
Dog.prototype.bark = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Woof! Woof!'</span>);
&#125;;
​
<span class="hljs-keyword">const</span> dog = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">'Q'</span>); <span class="hljs-comment">// ts(7009) 'new' expression, whose target lacks a construct signature, implicitly has an 'any' type.</span>
dog.bark(); <span class="hljs-comment">// => 'Woof! Woof!'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和通过 class 方式定义类相比，这种方式明显麻烦不少，而且还缺少静态类型检测。</p>
<h3 data-id="heading-2">6.2继承</h3>
<p>使用 extends 关键字就能很方便地定义类继承的抽象模式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  type = <span class="hljs-string">'Animal'</span>;
  <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params">name: string</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`I'm <span class="hljs-subst">$&#123;name&#125;</span>!`</span>);
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">bark</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Woof! Woof!'</span>);
  &#125;
&#125;

<span class="hljs-keyword">const</span> dog = <span class="hljs-keyword">new</span> Dog();
dog.bark(); <span class="hljs-comment">// => 'Woof! Woof!'</span>
dog.say(<span class="hljs-string">'Q'</span>); <span class="hljs-comment">// => I'm Q!</span>
dog.type; <span class="hljs-comment">// => Animal</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明：派生类通常被称作子类，基类也被称作超类（或者父类）。</p>
<p><code>派生类如果包含一个构造函数，则必须在构造函数中调用 super() 方法</code>，这是 TypeScript 强制执行的一条重要规则。如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-attr">name</span>: string;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: string</span>)</span> &#123; <span class="hljs-comment">// ts(2377) Constructors for derived classes must contain a 'super' call.</span>
    <span class="hljs-built_in">this</span>.name = name;
  &#125;

  <span class="hljs-function"><span class="hljs-title">bark</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Woof! Woof!'</span>);
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-attr">name</span>: string;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: string</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(); <span class="hljs-comment">// 添加 super 方法</span>
    <span class="hljs-built_in">this</span>.name = name;
  &#125;

  <span class="hljs-function"><span class="hljs-title">bark</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Woof! Woof!'</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 super 函数会调用基类的构造函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-attr">weight</span>: number;
  type = <span class="hljs-string">'Animal'</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">weight: number</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.weight = weight;
  &#125;
  <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params">name: string</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`I'm <span class="hljs-subst">$&#123;name&#125;</span>!`</span>);
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-attr">name</span>: string;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: string</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(); <span class="hljs-comment">// ts(2554) Expected 1 arguments, but got 0.</span>
    <span class="hljs-built_in">this</span>.name = name;
  &#125;

  <span class="hljs-function"><span class="hljs-title">bark</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Woof! Woof!'</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将鼠标放到第 15 行 Dog 类构造函数调用的 super 函数上，我们可以看到一个提示，<code>它的类型是基类 Animal 的构造函数</code>：constructor Animal(weight: number): Animal 。并且因为 Animal 类的构造函数要求必须传入一个数字类型的 weight 参数，而第 15 行实际入参为空，所以提示了一个 ts(2554) 的错误；如果我们显式地给 super 函数传入一个 number 类型的值，比如说 super(20)，则不会再提示错误了。</p>
<h3 data-id="heading-3">6.3公共、私有与受保护的修饰符</h3>
<p>类属性和方法除了可以通过 extends 被继承之外，还可以<code>通过修饰符控制可访问性</code>。</p>
<p>在 TypeScript 中就支持 3 种访问修饰符，分别是 <code>public、private、protected</code>。</p>
<ul>
<li>
<p>public 修饰的是在任何地方可见、公有的属性或方法；</p>
</li>
<li>
<p>private 修饰的是仅在同一类中可见、私有的属性或方法；</p>
</li>
<li>
<p>protected 修饰的是仅在类自身及子类中可见、受保护的属性或方法。</p>
</li>
</ul>
<p>在之前的代码中，示例类并没有用到可见性修饰符，在缺省情况下，类的属性或方法默认都是 public。如果想让有些属性对外不可见，那么我们可以使用private进行设置，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son</span> </span>&#123;
  public firstName: string;
  private lastName: string = <span class="hljs-string">'Stark'</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">firstName: string</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.firstName = firstName;
    <span class="hljs-built_in">this</span>.lastName; <span class="hljs-comment">// ok</span>
  &#125;
&#125;

<span class="hljs-keyword">const</span> son = <span class="hljs-keyword">new</span> Son(<span class="hljs-string">'Tony'</span>);
<span class="hljs-built_in">console</span>.log(son.firstName); <span class="hljs-comment">//  => "Tony"</span>
son.firstName = <span class="hljs-string">'Jack'</span>;
<span class="hljs-built_in">console</span>.log(son.firstName); <span class="hljs-comment">//  => "Jack"</span>
<span class="hljs-built_in">console</span>.log(son.lastName); <span class="hljs-comment">// ts(2341) Property 'lastName' is private and only accessible within class 'Son'.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：TypeScript 中定义类的私有属性仅仅代表静态类型检测层面的私有。如果我们强制忽略 TypeScript 类型的检查错误，转译且运行 JavaScript 时依旧可以获取到 lastName 属性，这是因为 <code>JavaScript 并不支持真正意义上的私有属性</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son</span> </span>&#123;
  public firstName: string;
  protected lastName: string = <span class="hljs-string">'Stark'</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">firstName: string</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.firstName = firstName;
    <span class="hljs-built_in">this</span>.lastName; <span class="hljs-comment">// ok</span>
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GrandSon</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Son</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">firstName: string</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(firstName);
  &#125;

  public <span class="hljs-function"><span class="hljs-title">getMyLastName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.lastName;
  &#125;
&#125;

<span class="hljs-keyword">const</span> grandSon = <span class="hljs-keyword">new</span> GrandSon(<span class="hljs-string">'Tony'</span>);
<span class="hljs-built_in">console</span>.log(grandSon.getMyLastName()); <span class="hljs-comment">// => "Stark"</span>
grandSon.lastName; <span class="hljs-comment">// ts(2445) Property 'lastName' is protected and only accessible within class 'Son' and its subclasses.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在第 3 行，修改 Son 类的 lastName 属性可见修饰符为 protected，表明此属性在 Son 类及其子类中可见。如示例第 6 行和第 16 行所示，我们既可以在父类 Son 的构造器中获取 lastName 属性值，又可以在继承自 Son 的子类 GrandSon 的 getMyLastName 方法获取 lastName 属性的值。</p>
<p>需要注意：<code>虽然我们不能通过派生类的实例访问protected修饰的属性和方法，但是可以通过派生类的实例方法进行访问。</code>比如示例中的第 21 行，通过实例的 getMyLastName 方法获取受保护的属性 lastName 是 ok 的，而第 22 行通过实例直接获取受保护的属性 lastName 则提示了一个 ts(2445) 的错误。</p>
<h3 data-id="heading-4">6.4只读修饰符</h3>
<p>如果我们不希望类的属性被更改，则可以使用 readonly 只读修饰符声明类的属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son</span> </span>&#123;
  public readonly firstName: string;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">firstName: string</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.firstName = firstName;
  &#125;
&#125;
<span class="hljs-keyword">const</span> son = <span class="hljs-keyword">new</span> Son(<span class="hljs-string">'Tony'</span>);
son.firstName = <span class="hljs-string">'Jack'</span>; <span class="hljs-comment">// ts(2540) Cannot assign to 'firstName' because it is a read-only property.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注意：如果只读修饰符和可见性修饰符同时出现，我们需要将只读修饰符写在可见修饰符后面。</code></p>
<h3 data-id="heading-5">6.5存取器</h3>
<p>在 TypeScript 中还可以通过<code>getter、setter</code>截取对类成员的<code>读写访问</code>。</p>
<p>通过对类属性访问的截取，我们可以实现一些特定的访问控制逻辑。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son</span> </span>&#123;
  public firstName: string;
  protected lastName: string = <span class="hljs-string">'Stark'</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">firstName: string</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.firstName = firstName;
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GrandSon</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Son</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">firstName: string</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(firstName);
  &#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">myLastName</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.lastName;
  &#125;
  <span class="hljs-keyword">set</span> <span class="hljs-title">myLastName</span>(<span class="hljs-params">name: string</span>) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.firstName === <span class="hljs-string">'Tony'</span>) &#123;
      <span class="hljs-built_in">this</span>.lastName = name;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'Unable to change myLastName'</span>);
    &#125;
  &#125;
&#125;
<span class="hljs-keyword">const</span> grandSon = <span class="hljs-keyword">new</span> GrandSon(<span class="hljs-string">'Tony'</span>);
<span class="hljs-built_in">console</span>.log(grandSon.myLastName); <span class="hljs-comment">// => "Stark"</span>
grandSon.myLastName = <span class="hljs-string">'Rogers'</span>;
<span class="hljs-built_in">console</span>.log(grandSon.myLastName); <span class="hljs-comment">// => "Rogers"</span>
<span class="hljs-keyword">const</span> grandSon1 = <span class="hljs-keyword">new</span> GrandSon(<span class="hljs-string">'Tony1'</span>);
grandSon1.myLastName = <span class="hljs-string">'Rogers'</span>; <span class="hljs-comment">// => "Unable to change myLastName"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">6.6静态属性</h3>
<p>以上介绍的关于类的所有属性和方法，<code>只有类在实例化时才会被初始化</code>。实际上，我们也可以给类定义静态属性和方法。</p>
<p>因为<code>这些属性存在于类这个特殊的对象上，而不是类的实例上</code>，所以我们可以直接通过类访问静态属性，如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyArray</span> </span>&#123;
  <span class="hljs-keyword">static</span> displayName = <span class="hljs-string">'MyArray'</span>;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">isArray</span>(<span class="hljs-params">obj: unknown</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(obj).slice(<span class="hljs-number">8</span>, -<span class="hljs-number">1</span>) === <span class="hljs-string">'Array'</span>;
  &#125;
&#125;
<span class="hljs-built_in">console</span>.log(MyArray.displayName); <span class="hljs-comment">// => "MyArray"</span>
<span class="hljs-built_in">console</span>.log(MyArray.isArray([])); <span class="hljs-comment">// => true</span>
<span class="hljs-built_in">console</span>.log(MyArray.isArray(&#123;&#125;)); <span class="hljs-comment">// => false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 static 修饰符，我们给 MyArray 类分别定义了一个静态属性 displayName 和静态方法 isArray。之后，我们<code>无须实例化 MyArray </code>就可以直接访问类上的静态属性和方法了</p>
<p>基于静态属性的特性，<code>我们往往会把与类相关的常量、不依赖实例 this 上下文的属性和方法定义为静态属性</code>，从而避免数据冗余，进而提升运行性能。</p>
<p><code>注意：</code>上边我们提到了不依赖实例 this 上下文的方法就可以定义成静态方法，这就意味着需要显式注解 this 类型才可以在静态方法中使用 this；非静态方法则不需要显式注解 this 类型，因为 this 的指向默认是类的实例。</p>
<h3 data-id="heading-7">6.7抽象类</h3>
<p>它是一种<code>不能被实例化仅能被子类继承的特殊类</code>。</p>
<p>我们可以<code>使用抽象类定义派生类需要实现的属性和方法，同时也可以定义其他被继承的默认属性和方法</code>，如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js">abstract <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Adder</span> </span>&#123;
  abstract x: number;
  abstract y: number;
  abstract add(): number;
  displayName = <span class="hljs-string">'Adder'</span>;
  addTwice(): number &#123;
    <span class="hljs-keyword">return</span> (<span class="hljs-built_in">this</span>.x + <span class="hljs-built_in">this</span>.y) * <span class="hljs-number">2</span>;
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NumAdder</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Adder</span> </span>&#123;
  <span class="hljs-attr">x</span>: number;
  y: number;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: number, y: number</span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
    <span class="hljs-built_in">this</span>.x = x;
    <span class="hljs-built_in">this</span>.y = y;
  &#125;
  add(): number &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.x + <span class="hljs-built_in">this</span>.y;
  &#125;
&#125;
<span class="hljs-keyword">const</span> numAdder = <span class="hljs-keyword">new</span> NumAdder(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
<span class="hljs-built_in">console</span>.log(numAdder.displayName); <span class="hljs-comment">// => "Adder"</span>
<span class="hljs-built_in">console</span>.log(numAdder.add()); <span class="hljs-comment">// => 3</span>
<span class="hljs-built_in">console</span>.log(numAdder.addTwice()); <span class="hljs-comment">// => 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 abstract 关键字，我们定义了一个抽象类 Adder，并通过abstract关键字定义了抽象属性x、y及方法add，而且<code>任何继承 Adder 的派生类都需要实现这些抽象属性和方法</code>。</p>
<p>如果派生类中缺少对 x、y、add 这三者中任意一个抽象成员的实现，那么第 12 行就会提示一个 ts(2515) 错误，关于这点你可以亲自验证一下。</p>
<p><code>抽象类中的其他非抽象成员则可以直接通过实例获取</code>，比如第 26～28 行中，通过实例 numAdder，我们获取了 displayName 属性和 addTwice 方法。</p>
<p>因为<code>抽象类不能被实例化</code>，并且<code>派生类必须实现继承自抽象类上的抽象属性和方法定义</code>，所以抽象类的作用其实就是对基础逻辑的封装和抽象。</p>
<p>实际上，我们也可以定义一个描述对象结构的接口类型（详见 07 讲）抽象类的结构，并通过 <code>implements 关键字</code>约束类的实现。</p>
<p>使用接口与使用抽象类相比，<code>区别在于接口只能定义类成员的类型</code></p>
<pre><code class="hljs language-js copyable" lang="js">interface IAdder &#123;
  <span class="hljs-attr">x</span>: number;
  y: number;
  add: <span class="hljs-function">() =></span> number;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NumAdder</span> <span class="hljs-title">implements</span> <span class="hljs-title">IAdder</span> </span>&#123;
  <span class="hljs-attr">x</span>: number;
  y: number;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: number, y: number</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.x = x;
    <span class="hljs-built_in">this</span>.y = y;
  &#125;
  <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.x + <span class="hljs-built_in">this</span>.y;
  &#125;
  <span class="hljs-function"><span class="hljs-title">addTwice</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (<span class="hljs-built_in">this</span>.x + <span class="hljs-built_in">this</span>.y) * <span class="hljs-number">2</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">6.8类的类型</h3>
<p>类的最后一个特性——类的类型和函数类似，即在声明类的时候，其实也同时声明了一个特殊的类型（确切地讲是一个接口类型），<code>这个类型的名字就是类名，表示类实例的类型</code>；在定义类的时候，我们声明的除构造函数外所有属性、方法的类型就是这个特殊类型的成员。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-attr">name</span>: string;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: string</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;
<span class="hljs-keyword">const</span> a1: A = &#123;&#125;; <span class="hljs-comment">// ts(2741) Property 'name' is missing in type '&#123;&#125;' but required in type 'A'.</span>
<span class="hljs-keyword">const</span> a2: A = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'a2'</span> &#125;; <span class="hljs-comment">// ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在定义类 A ，也说明我们同时定义了一个包含字符串属性 name 的同名接口类型 A。因此，在第 7 行把一个空对象赋值给类型是 A 的变量 a1 时，TypeScript 会提示一个 ts(2741) 错误，因为缺少 name 属性。在第 8 行把对象&#123; name: 'a2' &#125;赋值给类型同样是 A 的变量 a2 时，TypeScript 就直接通过了类型检查，因为有 name 属性。</p>
<p>在 TypeScript 中，因为我们需要实践 <code>OOP 编程思想</code>，所以离不开类的支撑。在实际工作中，类与函数一样，都是<code>极其有用的抽象、封装利器</code>。</p>
<h2 data-id="heading-9">7接口类型与类型别名</h2>
<p>这一讲我们将学习 TypeScript 与 JavaScript 不一样却堪称精华之一的特性——接口类型与类型别名。这些特性让 TypeScript 具备了 JavaScript 所缺少的、描述较为复杂数据结构的能力。在使用 TypeScript 之前，可能我们只能通过文档或大量的注释来做这件事。</p>
<h3 data-id="heading-10">7.1Interface 接口类型</h3>
<p>TypeScript 不仅能帮助前端改变思维方式，还能强化面向接口编程的思维和能力，而这正是得益于 Interface 接口类型。<code>通过接口类型，我们可以清晰地定义模块内、跨模块、跨项目代码的通信规则。</code></p>
<p>TypeScript 对对象的类型检测遵循一种被称之为“鸭子类型”（duck typing）或者<code>“结构化类型（structural subtyping）”</code>的准则，即只要两个对象的结构一致，属性和方法的类型一致，则它们的类型就是一致的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Study</span>(<span class="hljs-params">language: &#123; name: string; age: () => number &#125;</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`ProgramLanguage <span class="hljs-subst">$&#123;language.name&#125;</span> created <span class="hljs-subst">$&#123;language.age()&#125;</span> years ago.`</span>);
&#125;
Study(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'TypeScript'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getFullYear() - <span class="hljs-number">2012</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在调用函数的过程中，TypeScript 静态类型检测到传递的对象字面量类型为 string 的 name 属性和类型为() => number 的 age 属性与函数参数定义的类型一致，于是不会抛出一个类型错误。</p>
<p>如果我们传入一个 name 属性是 number 类型或者缺少age属性的对象字面量，</p>
<pre><code class="hljs language-js copyable" lang="js">Study(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getFullYear() - <span class="hljs-number">2012</span>
&#125;);
Study(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'TypeScript'</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时，第 2 行会提示错误： ts(2322) number 不能赋值给 string，第 7 行也会提示错误： ts(2345) 实参(Argument)与形参(Parameter)<code>类型不兼容</code>，缺少必需的属性 age。</p>
<p>同样，如果我们传入一个包含了形参类型定义里没有的 id 属性的对象字面量作为实参，也会得到一个类型错误 ts(2345)，实参（Argument）与形参（Parameter）<code>类型不兼</code>容，不存在的属性 id，如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** ts(2345) 实参(Argument)与形参(Parameter)类型不兼容，不存在的属性 id */</span>
Study(&#123;
  <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'TypeScript'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getFullYear() - <span class="hljs-number">2012</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有意思的是，在上边的示例中，<code>如果我们先把这个对象字面量赋值给一个变量，然后再把变量传递给函数进行调用，那么 TypeScript 静态类型检测就会仅仅检测形参类型中定义过的属性类型，而包容地忽略任何多余的属性</code>，此时也不会抛出一个 ts(2345) 类型错误。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> ts = &#123;
  <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'TypeScript'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getFullYear() - <span class="hljs-number">2012</span>
&#125;;
Study(ts); <span class="hljs-comment">// ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这并非一个疏忽或 bug，而是有意为之地将<code>对象字面量和变量进行区别对待</code>，我们把这种情况称之为<code>对象字面量的 freshness</code>（在 12 讲中会再次详细介绍）。</p>
<p>因为这种内联形式的接口类型定义在语法层面与熟知的 JavaScript 解构颇为神似，所以很容易让我们产生混淆。下面我们通过如下示例对比一下<code>解构语法与内联接口类型</code>混用的效果。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** 纯 JavaScript 解构语法 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">StudyJavaScript</span>(<span class="hljs-params">&#123;name, age&#125;</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(name, age);
&#125;
<span class="hljs-comment">/** TypeScript 里解构与内联类型混用 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">StudyTypeScript</span>(<span class="hljs-params">&#123;name, age&#125;: &#123;name: string, age: () => number&#125;</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(name, age);
&#125;
<span class="hljs-comment">/** 纯 JavaScript 解构语法，定义别名 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">StudyJavaScript</span>(<span class="hljs-params">&#123;name: aliasName&#125;</span>) </span>&#123; <span class="hljs-comment">// 定义name的别名</span>
  <span class="hljs-built_in">console</span>.log(aliasName);
&#125;
<span class="hljs-comment">/** TypeScript */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">StudyTypeScript</span>(<span class="hljs-params">language: &#123;name: string&#125;</span>) </span>&#123;
  <span class="hljs-comment">// console.log(name); // 不能直接打印name</span>
  <span class="hljs-built_in">console</span>.log(language.name);  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在函数中，对象解构和定义接口类型的语法很类似（如第 12 行和 17 行所示），注意不要混淆。实际上，定义内联的接口类型是不可复用的，所以我们<code>应该更多地使用interface关键字来抽离可复用的接口类型</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">/ ** 关键字 接口名称 */
interface ProgramLanguage &#123;
  <span class="hljs-comment">/** 语言名称 */</span>
  <span class="hljs-attr">name</span>: string;
  <span class="hljs-comment">/** 使用年限 */</span>
  age: <span class="hljs-function">() =></span> number;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>接口的语法格式</code>是在 <code>interface 关键字的空格后+接口名字，然后属性与属性类型的定义用花括弧包裹</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">NewStudy</span>(<span class="hljs-params">language: ProgramLanguage</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`ProgramLanguage <span class="hljs-subst">$&#123;language.name&#125;</span> created <span class="hljs-subst">$&#123;language.age()&#125;</span> years ago.`</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还可以通过<code>复用接口类型</code>定义来约束其他逻辑。比如，我们通过如下所示代码定义了一个类型为 ProgramLanguage 的变量 TypeScript 。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> TypeScript: ProgramLanguage;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，我们把满足接口类型约定的一个对象字面量赋值给了这个变量,不会报错。</p>
<pre><code class="hljs language-js copyable" lang="js">TypeScript = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'TypeScript'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getFullYear() - <span class="hljs-number">2012</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而任何不符合约定的情况，都会提示类型错误。
如以下示例中额外多出了一个接口并未定义的属性 id，也会提示一个 ts(2322) 错误：对象字面量不能赋值给 ProgramLanguage 类型的变量 TypeScript。</p>
<pre><code class="hljs language-js copyable" lang="js">TypeScript = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'TypeScript'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getFullYear() - <span class="hljs-number">2012</span>,
  <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">7.2可缺省属性</h3>
<p>如果我们希望缺少 age 属性的对象字面量也能符合约定且不抛出类型错误，确切地说在接口类型中 age 属性可缺省，那么我们可以在属性名之后通过添加如下所示的<code>? 语法</code>来标注可缺省的属性或方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** 关键字 接口名称 */</span>
interface OptionalProgramLanguage &#123;
  <span class="hljs-comment">/** 语言名称 */</span>
  <span class="hljs-attr">name</span>: string;
  <span class="hljs-comment">/** 使用年限 */</span>
  age?: <span class="hljs-function">() =></span> number;
&#125;
<span class="hljs-keyword">let</span> OptionalTypeScript: OptionalProgramLanguage = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'TypeScript'</span>
&#125;; <span class="hljs-comment">// ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当属性被标注为可缺省后，它的类型就变成了<code>显式指定的类型与 undefined 类型</code>组成的联合类型. 比如示例中 OptionalTypeScript 的 age 属性类型就变成了如下所示内容：</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">() =></span> number) | <span class="hljs-literal">undefined</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发散思考一下：你觉得如下所示的接口类型 OptionalTypeScript2 和 OptionalTypeScript 等价吗？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** 关键字 接口名称 */</span>
interface OptionalProgramLanguage2 &#123;
  <span class="hljs-comment">/** 语言名称 */</span>
  <span class="hljs-attr">name</span>: string;
  <span class="hljs-comment">/** 使用年限 */</span>
  age: (<span class="hljs-function">() =></span> number) | <span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>答案当然是不等价，这与 05 讲中提到函数可缺省参数和参数类型可以是 undefined 一样，<code>可缺省意味着可以不设置属性键名</code>，<code>类型是 undefined 意味着属性键名不可缺省</code>。</p>
<p>既然值可能是 undefined ，如果我们需要对该对象的属性或方法进行操作，就可以使用类型守卫（详见 11 讲）或 Optional Chain（在第 5 行的属性名后加 ? ），如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> OptionalTypeScript.age === <span class="hljs-string">'function'</span>) &#123;
  OptionalTypeScript.age();
&#125;
OptionalTypeScript.age?.();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">7.3只读属性</h3>
<p>我们可以<code>在属性名前通过添加 readonly 修饰符的语法</code>来标注 name 为只读属性。</p>
<pre><code class="hljs language-js copyable" lang="js">interface ReadOnlyProgramLanguage &#123;
  <span class="hljs-comment">/** 语言名称 */</span>
  readonly name: string;
  <span class="hljs-comment">/** 使用年限 */</span>
  readonly age: (<span class="hljs-function">() =></span> number) | <span class="hljs-literal">undefined</span>;
&#125;
 
<span class="hljs-keyword">let</span> ReadOnlyTypeScript: ReadOnlyProgramLanguage = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'TypeScript'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-literal">undefined</span>
&#125;
<span class="hljs-comment">/** ts(2540)错误，name 只读 */</span>
ReadOnlyTypeScript.name = <span class="hljs-string">'JavaScript'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，这仅仅是静态类型检测层面的只读，实际上并不能阻止对对象的篡改。因为在转译为 JavaScript 之后，readonly 修饰符会被抹除。因此，任何时候<code>与其直接修改一个对象，不如返回一个新的对象</code>👍，这会是一种比较安全的实践。</p>
<h3 data-id="heading-13">7.4定义函数类型</h3>
<p>接口类型不仅能用来定义<code>对象的类型</code>，接口类型还可以用来定义<code>函数的类型</code> （备注：仅仅是定义函数的类型，而不包含函数的实现）</p>
<pre><code class="hljs language-js copyable" lang="js">interface StudyLanguage &#123;
  (language: ProgramLanguage): <span class="hljs-keyword">void</span>
&#125;
<span class="hljs-comment">/** 单独的函数实践 */</span>
<span class="hljs-keyword">let</span> StudyInterface: StudyLanguage 
  = <span class="hljs-function"><span class="hljs-params">language</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;language.name&#125;</span> <span class="hljs-subst">$&#123;language.age()&#125;</span>`</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上，我们很少使用接口类型来定义函数的类型，更多使用<code>内联类型或类型别名（本讲后半部分讲解）配合箭头函数语法</code>来定义函数类型，具体示例如下：</p>
<pre><code class="hljs language-js copyable" lang="js">type StudyLanguageType = <span class="hljs-function">(<span class="hljs-params">language: ProgramLanguage</span>) =></span> <span class="hljs-keyword">void</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们给箭头函数类型指定了一个别名 StudyLanguageType，在其他地方就可以直接复用 StudyLanguageType，而不用重新声明新的箭头函数类型定义。</p>
<h3 data-id="heading-14">7.5索引签名</h3>
<p>在实际工作中，<code>使用接口类型较多的地方是对象</code>，比如 React 组件的 Props & State、HTMLElement 的 Props，这些对象有一个<code>共性，即所有的属性名、方法名都确定</code>。</p>
<p>实际上，我们经常会把对象当 Map 映射使用，比如下边代码示例中定义了索引是任意数字的对象 LanguageRankMap 和索引是任意字符串的对象 LanguageMap。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> LanguageRankMap = &#123;
  <span class="hljs-number">1</span>: <span class="hljs-string">'TypeScript'</span>,
  <span class="hljs-number">2</span>: <span class="hljs-string">'JavaScript'</span>,
  ...
&#125;;
<span class="hljs-keyword">let</span> LanguageMap = &#123;
  <span class="hljs-attr">TypeScript</span>: <span class="hljs-number">2012</span>,
  <span class="hljs-attr">JavaScript</span>: <span class="hljs-number">1995</span>,
  ...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候，我们需要使用索引签名来定义上边提到的对象映射结构，并通过 <code>“[索引名: 类型]”的格式</code>约束索引的类型。</p>
<p><code>索引名称的类型分为 string 和 number 两种</code>，通过如下定义的 LanguageRankInterface 和 LanguageYearInterface 两个接口，我们可以用来描述索引是任意数字或任意字符串的对象。</p>
<pre><code class="hljs language-js copyable" lang="js">interface LanguageRankInterface &#123;
  [rank: number]: string;
&#125;
interface LanguageYearInterface &#123;
  [name: string]: number;
&#125;
&#123;
  <span class="hljs-keyword">let</span> LanguageRankMap: LanguageRankInterface = &#123;
    <span class="hljs-number">1</span>: <span class="hljs-string">'TypeScript'</span>, <span class="hljs-comment">// ok</span>
    <span class="hljs-number">2</span>: <span class="hljs-string">'JavaScript'</span>, <span class="hljs-comment">// ok</span>
    <span class="hljs-string">'WrongINdex'</span>: <span class="hljs-string">'2012'</span> <span class="hljs-comment">// ts(2322) 不存在的属性名</span>
  &#125;;
  
  <span class="hljs-keyword">let</span> LanguageMap: LanguageYearInterface = &#123;
    <span class="hljs-attr">TypeScript</span>: <span class="hljs-number">2012</span>, <span class="hljs-comment">// ok</span>
    <span class="hljs-attr">JavaScript</span>: <span class="hljs-number">1995</span>, <span class="hljs-comment">// ok</span>
    <span class="hljs-number">1</span>: <span class="hljs-number">1970</span> <span class="hljs-comment">// ok</span>
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong>：在上述示例中，<code>数字作为对象索引时，它的类型既可以与数字兼容，也可以与字符串兼容</code>，这与 JavaScript 的行为一致。因此，使用 0 或 '0' 索引对象时，这两者等价。</p>
<p>同样，我们可以使用 readonly 注解索引签名，此时将对应属性设置为只读就行</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  interface LanguageRankInterface &#123;
    readonly [rank: number]: string;
  &#125;
  
  interface LanguageYearInterface &#123;
    readonly [name: string]: number;
  &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：虽然<code>属性可以与索引签名进行混用</code>，但是<code>属性的类型必须是对应的数字索引或字符串索引的类型的子集</code>，否则会出现错误提示。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  interface StringMap &#123;
    [prop: string]: number;
    age: number; <span class="hljs-comment">// ok</span>
    name: string; <span class="hljs-comment">// ts(2411) name 属性的 string 类型不能赋值给字符串索引类型 number</span>
  &#125;
  interface NumberMap &#123;
    [rank: number]: string;
    <span class="hljs-number">1</span>: string; <span class="hljs-comment">// ok</span>
    <span class="hljs-number">0</span>: number; <span class="hljs-comment">// ts(2412) 0 属性的 number 类型不能赋值给数字索引类型 string</span>
  &#125;
  interface LanguageRankInterface &#123;
    <span class="hljs-attr">name</span>: string; <span class="hljs-comment">// ok</span>
    <span class="hljs-number">0</span>: number; <span class="hljs-comment">// ok</span>
    [rank: number]: string;
    [name: string]: number;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为接口 StringMap 属性 name 的类型 string 不是它所对应的字符串索引（第 3 行定义的 prop: string）类型 number 的子集，所以会提示一个错误。同理，因为接口 NumberMap 属性 0 的类型 number 不是它所对应的数字索引（第 8 行定义的 rank: number）类型 string 的子集，所以也会提示一个错误。</p>
<p>另外，由于上边提到了<code>数字类型索引的特殊性</code>，所以<code>我们不能约束数字索引属性与字符串索引属性拥有截然不同的类型</code></p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  interface LanguageRankInterface &#123;
    [rank: number]: string; <span class="hljs-comment">// ts(2413) 数字索引类型 string 类型不能赋值给字符串索引类型 number</span>
    [prop: string]: number;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们定义了 LanguageRankInterface 的数字索引 rank 的类型是 string，与定义的字符串索引 prop 的类型 number 不兼容，所以会提示一个 ts(2413) 错误。</p>
<p>这里埋个伏笔：<code>如果我们确实需要使用 age 是 number 类型、其他属性类型是 string 的对象数据结构，应该如何定义它的类型且不提示错误呢？</code></p>
<p>比如如下示例中定义的 age 属性是数字、其他任意属性是字符串的对象，我们应该怎么定义它的类型呢？</p>
<pre><code class="hljs language-js copyable" lang="js">
&#123;
  <span class="hljs-attr">age</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 数字类型</span>
  <span class="hljs-attr">anyProperty</span>: <span class="hljs-string">'str'</span>, <span class="hljs-comment">// 字符串</span>
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于<code>属性和索引签名的类型限制</code>，使得我们不能通过单一的接口来描述这个对象，这时我们该怎么办呢？08 讲中我们会解决这个问题。</p>
<h3 data-id="heading-15">7.6继承与实现</h3>
<p>在 TypeScript 中，接口类型可以继承和被继承，比如我们可以使用如下所示的 <code>extends 关键字</code>实现接口的继承。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  interface DynamicLanguage <span class="hljs-keyword">extends</span> ProgramLanguage &#123;
    <span class="hljs-attr">rank</span>: number; <span class="hljs-comment">// 定义新属性</span>
  &#125;
  
  interface TypeSafeLanguage <span class="hljs-keyword">extends</span> ProgramLanguage &#123;
    <span class="hljs-attr">typeChecker</span>: string; <span class="hljs-comment">// 定义新的属性</span>
  &#125;
  <span class="hljs-comment">/** 继承多个 */</span>
  interface TypeScriptLanguage <span class="hljs-keyword">extends</span> DynamicLanguage, TypeSafeLanguage &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'TypeScript'</span>; <span class="hljs-comment">// 用原属性类型的兼容的类型(比如子集)重新定义属性</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注意：我们仅能使用兼容的类型覆盖继承的属性</code></p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-comment">/** ts(6196) 错误的继承，name 属性不兼容 */</span>
  interface WrongTypeLanguage <span class="hljs-keyword">extends</span> ProgramLanguage &#123;
    <span class="hljs-attr">name</span>: number;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们既可以使用接口类型来约束类，反过来也可以使用类实现接口，那两者之间的关系到底是什么呢？这里，我们通过使用如下所示的 <code>implements</code>关键字描述一下类和接口之间的关系。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** 类实现接口 */</span>
&#123;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LanguageClass</span> <span class="hljs-title">implements</span> <span class="hljs-title">ProgramLanguage</span> </span>&#123;
    <span class="hljs-attr">name</span>: string = <span class="hljs-string">''</span>;
    age = <span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getFullYear() - <span class="hljs-number">2012</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">7.7Type 类型别名</h3>
<p>接口类型的一个作用是<code>将内联类型抽离出来</code>，从而实现类型可复用。其实，我们也可以使用类型别名接收抽离出来的内联类型实现复用。</p>
<p>此时，我们可以通过如下所示<code>“type 别名名字 = 类型定义”的格式</code>来定义类型别名。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** 类型别名 */</span>
&#123;
  type LanguageType = &#123;
    <span class="hljs-comment">/** 以下是接口属性 */</span>
    <span class="hljs-comment">/** 语言名称 */</span>
    <span class="hljs-attr">name</span>: string;
    <span class="hljs-comment">/** 使用年限 */</span>
    age: <span class="hljs-function">() =></span> number;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，<code>针对接口类型无法覆盖的场景，比如组合类型、交叉类型（详见 08 讲），我们只能使用类型别名来接收</code>，如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-comment">/** 联合 */</span>
  type MixedType = string | number;
  <span class="hljs-comment">/** 交叉 */</span>
  type IntersectionType = &#123; <span class="hljs-attr">id</span>: number; name: string; &#125; 
    & &#123; <span class="hljs-attr">age</span>: number; name: string &#125;;
  <span class="hljs-comment">/** 提取接口属性类型 */</span>
  type AgeType = ProgramLanguage[<span class="hljs-string">'age'</span>];  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们定义了一个 IntersectionType 类型别名，表示两个匿名接口类型交叉出的类型；同时定义了一个 AgeType 类型别名，表示抽取的 ProgramLanguage age 属性的类型。</p>
<h3 data-id="heading-17">7.8Interface 与 Type 的区别</h3>
<p>适用接口类型标注的地方大都可以使用类型别名进行替代，这是否意味着在相应的场景中这两者等价呢？</p>
<p>实际上，在<code>大多数的情况下使用接口类型和类型别名的效果等价</code>，但是在某些特定的场景下这两者还是存在很大区别。比如，<code>重复定义的接口类型，它的属性会叠加，这个特性使得我们可以极其方便地对全局变量、第三方库的类型做扩展</code>，如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  interface Language &#123;
    <span class="hljs-attr">id</span>: number;
  &#125;
  
  interface Language &#123;
    <span class="hljs-attr">name</span>: string;
  &#125;
  <span class="hljs-keyword">let</span> lang: Language = &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// ok</span>
    <span class="hljs-attr">name</span>: <span class="hljs-string">'name'</span> <span class="hljs-comment">// ok</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>先后定义的两个 Language 「接口」属性被叠加在了一起</code>，此时我们可以赋值给 lang 变量一个同时包含 id 和 name 属性的对象。</p>
<p>不过，<code>如果我们重复定义类型别名，如下代码所示，则会提示一个 ts(2300) 错误。</code></p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-comment">/** ts(2300) 重复的标志 */</span>
  type Language = &#123;
    <span class="hljs-attr">id</span>: number;
  &#125;
  
  <span class="hljs-comment">/** ts(2300) 重复的标志 */</span>
  type Language = &#123;
    <span class="hljs-attr">name</span>: string;
  &#125;
  <span class="hljs-keyword">let</span> lang: Language = &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'name'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接口类型是 TypeScript 最核心的知识点之一，掌握好接口类型，养成面向接口编程思维方式和惯性，将让我们的编程之路愈发顺利、高效。</p>
<p>类型别名使得类型可以像值一样能赋予另外一个变量（别名），大大提升了类型复用性，最终也提升了我们的编程效率。</p>
<h2 data-id="heading-18">8高级类型：联合类型和交叉类型</h2>
<h3 data-id="heading-19">8.1联合类型</h3>
<p>联合类型（Unions）用来表示变量、参数的类型不是单一原子类型，而可能是多种不同的类型的组合。</p>
<p>我们主要通过“|”操作符分隔类型的语法来表示联合类型。这里，我们可以把“|”类比为 JavaScript 中的逻辑或 “||”，只不过前者表示可能的类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">formatPX</span>(<span class="hljs-params">size: unknown</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> size === <span class="hljs-string">'number'</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;size&#125;</span>px`</span>;
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> size === <span class="hljs-string">'string'</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">parseInt</span>(size) || <span class="hljs-number">0</span>&#125;</span>px`</span>;
  &#125;
  <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">` 仅支持 number 或者 string`</span>);
&#125;
formatPX(<span class="hljs-number">13</span>);
formatPX(<span class="hljs-string">'13px'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明：在学习联合类型之前，我们可能免不了使用 any 或 unknown 类型来表示参数的类型（为了让大家养成好习惯，推荐使用 unknown）。</p>
<p>通过这样的方式带来的问题是，在调用 formatPX 时，我们可以传递任意的值，并且可以通过静态类型检测（使用 any 亦如是），但是运行时还是会抛出一个错误，例如：</p>
<pre><code class="hljs language-js copyable" lang="js">formatPX(<span class="hljs-literal">true</span>);
formatPX(<span class="hljs-literal">null</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这显然不符合我们的预期，因为 size 应该是更明确的，即可能也只可能是 number 或 string 这两种可选类型的类型。</p>
<p>所幸<code>有联合类型，我们可以使用一个更明确表示可能是 number 或 string 的联合类型来注解 size 参数</code>，如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">formatPX</span>(<span class="hljs-params">size: number | string</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;
formatPX(<span class="hljs-number">13</span>); <span class="hljs-comment">// ok</span>
formatPX(<span class="hljs-string">'13px'</span>); <span class="hljs-comment">// ok</span>
formatPX(<span class="hljs-literal">true</span>); <span class="hljs-comment">// ts(2345) 'true' 类型不能赋予 'number | string' 类型</span>
formatPX(<span class="hljs-literal">null</span>); <span class="hljs-comment">// ts(2345) 'null' 类型不能赋予 'number | string' 类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，我们可以组合任意个、任意类型来构造更满足我们诉求的类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">formatUnit</span>(<span class="hljs-params">size: number | string, unit: <span class="hljs-string">'px'</span> | <span class="hljs-string">'em'</span> | <span class="hljs-string">'rem'</span> | <span class="hljs-string">'%'</span> = <span class="hljs-string">'px'</span></span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;
formatUnit(<span class="hljs-number">1</span>, <span class="hljs-string">'em'</span>); <span class="hljs-comment">// ok</span>
formatUnit(<span class="hljs-string">'1px'</span>, <span class="hljs-string">'rem'</span>); <span class="hljs-comment">// ok</span>
formatUnit(<span class="hljs-string">'1px'</span>, <span class="hljs-string">'bem'</span>); <span class="hljs-comment">// ts(2345)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以<code>使用类型别名抽离上边的联合类型</code>，然后再将其进一步地联合，</p>
<pre><code class="hljs language-js copyable" lang="js">type ModernUnit = <span class="hljs-string">'vh'</span> | <span class="hljs-string">'vw'</span>;
type Unit = <span class="hljs-string">'px'</span> | <span class="hljs-string">'em'</span> | <span class="hljs-string">'rem'</span>;
type MessedUp = ModernUnit | Unit; <span class="hljs-comment">// 类型是 'vh' | 'vw' | 'px' | 'em' | 'rem'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以<code>把接口类型联合起来</code>表示更复杂的结构.</p>
<pre><code class="hljs language-js copyable" lang="js">interface Bird &#123;
  fly(): <span class="hljs-keyword">void</span>;
  layEggs(): <span class="hljs-keyword">void</span>;
&#125;
interface Fish &#123;
  swim(): <span class="hljs-keyword">void</span>;
  layEggs(): <span class="hljs-keyword">void</span>;
&#125;
<span class="hljs-keyword">const</span> getPet: <span class="hljs-function">() =></span> Bird | Fish = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
   <span class="hljs-comment">// ...</span>
  &#125; <span class="hljs-keyword">as</span> Bird | Fish;
&#125;;
<span class="hljs-keyword">const</span> Pet = getPet();
Pet.layEggs(); <span class="hljs-comment">// ok</span>
Pet.fly(); <span class="hljs-comment">// ts(2339) 'Fish' 没有 'fly' 属性; 'Bird | Fish' 没有 'fly' 属性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在联合类型中，我们可以直接访问各个接口成员都拥有的属性、方法，且不会提示类型错误。但是，<code>如果是个别成员特有的属性、方法，我们就需要区分对待了</code>，此时又要引入类型守卫（详见 11 讲）来区分不同的成员类型。</p>
<p>只不过，在这种情况下，我们还需要使用基于 in 操作符判断的类型守卫</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> Pet.fly === <span class="hljs-string">'function'</span>) &#123; <span class="hljs-comment">// ts(2339)</span>
  Pet.fly(); <span class="hljs-comment">// ts(2339)</span>
&#125;
<span class="hljs-keyword">if</span> (<span class="hljs-string">'fly'</span> <span class="hljs-keyword">in</span> Pet) &#123;
  Pet.fly(); <span class="hljs-comment">// ok</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">8.2交叉类型</h3>
<p>在 TypeScript 中，还存在一种类似<code>逻辑与</code>行为的类型——交叉类型（Intersection Type），它可以把多个类型合并成一个类型，合并后的类型将拥有所有成员类型的特性。</p>
<p>在 TypeScript 中，我们可以使用<code>“&”操作符</code>来声明交叉类型，</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  type Useless = string & number;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们仅仅把原始类型、字面量类型、函数类型等原子类型合并成交叉类型，是没有任何用处的，因为任何类型都不能满足同时属于多种原子类型,因此，在上述的代码中，类型别名 Useless 的类型就是个 never。</p>
<h3 data-id="heading-21">8.3合并接口类型</h3>
<p><code>联合类型真正的用武之地就是将多个接口类型合并成一个类型，从而实现等同接口继承的效果</code>，也就是所谓的合并接口类型</p>
<pre><code class="hljs language-js copyable" lang="js">type IntersectionType = &#123; <span class="hljs-attr">id</span>: number; name: string; &#125; 
    & &#123; <span class="hljs-attr">age</span>: number &#125;;
  <span class="hljs-keyword">const</span> mixed: IntersectionType = &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'name'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过交叉类型，使得 IntersectionType 同时拥有了 id、name、age 所有属性，这里我们可以试着<code>将合并接口类型理解为求并集</code>。</p>
<p>这里，我们来发散思考一下：如果合并的多个接口类型存在同名属性会是什么效果呢？</p>
<p>此时，我们可以根据<code>同名属性的类型是否兼容</code>（详见 12 讲）将这个问题分开来看。</p>
<p>如果同名属性的类型不兼容，比如上面示例中两个接口类型同名的 name 属性类型一个是 number，另一个是 string，合并后，name 属性的类型就是 number 和 string 两个原子类型的交叉类型，即 never，如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js">type IntersectionTypeConfict = &#123; <span class="hljs-attr">id</span>: number; name: string; &#125; 
    & &#123; <span class="hljs-attr">age</span>: number; name: number; &#125;;
  <span class="hljs-keyword">const</span> mixedConflict: IntersectionTypeConfict = &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// ts(2322) 错误，'number' 类型不能赋给 'never' 类型</span>
    <span class="hljs-attr">age</span>: <span class="hljs-number">2</span>
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果同名属性的类型兼容，比如一个是 number，另一个是 number 的子类型、数字字面量类型，合并后 name 属性的类型就是<code>两者中的子类型</code>。</p>
<p>如下所示示例中 name 属性的类型就是数字字面量类型 2，因此，我们不能把任何非 2 之外的值赋予 name 属性。</p>
<pre><code class="hljs language-js copyable" lang="js">type IntersectionTypeConfict = &#123; <span class="hljs-attr">id</span>: number; name: <span class="hljs-number">2</span>; &#125; 
  & &#123; <span class="hljs-attr">age</span>: number; name: number; &#125;;
  <span class="hljs-keyword">let</span> mixedConflict: IntersectionTypeConfict = &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// ok</span>
    <span class="hljs-attr">age</span>: <span class="hljs-number">2</span>
  &#125;;
  mixedConflict = &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-number">22</span>, <span class="hljs-comment">// '22' 类型不能赋给 '2' 类型</span>
    <span class="hljs-attr">age</span>: <span class="hljs-number">2</span>
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">8.3合并联合类型</h3>
<p>另外，我们可以合并联合类型为一个交叉类型，这个交叉类型需要同时满足不同的联合类型限制，也就是提取了所有联合类型的相同类型成员。这里，我们也可以将<code>合并联合类型理解为求交集</code>。</p>
<p>在如下示例中，两个联合类型交叉出来的类型 IntersectionUnion 其实等价于 'em' | 'rem'，所以我们只能把 'em' 或者 'rem' 字符串赋值给 IntersectionUnion 类型的变量。</p>
<pre><code class="hljs language-js copyable" lang="js">type UnionA = <span class="hljs-string">'px'</span> | <span class="hljs-string">'em'</span> | <span class="hljs-string">'rem'</span> | <span class="hljs-string">'%'</span>;
  type UnionB = <span class="hljs-string">'vh'</span> | <span class="hljs-string">'em'</span> | <span class="hljs-string">'rem'</span> | <span class="hljs-string">'pt'</span>;
  type IntersectionUnion = UnionA & UnionB;
  <span class="hljs-keyword">const</span> intersectionA: IntersectionUnion = <span class="hljs-string">'em'</span>; <span class="hljs-comment">// ok</span>
  <span class="hljs-keyword">const</span> intersectionB: IntersectionUnion = <span class="hljs-string">'rem'</span>; <span class="hljs-comment">// ok</span>
  <span class="hljs-keyword">const</span> intersectionC: IntersectionUnion = <span class="hljs-string">'px'</span>; <span class="hljs-comment">// ts(2322)</span>
  <span class="hljs-keyword">const</span> intersectionD: IntersectionUnion = <span class="hljs-string">'pt'</span>; <span class="hljs-comment">// ts(2322)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>既然是求交集，如果多个联合类型中没有相同的类型成员，交叉出来的类型自然就是 never 了</p>
<pre><code class="hljs language-js copyable" lang="js">type UnionC = <span class="hljs-string">'em'</span> | <span class="hljs-string">'rem'</span>;
  type UnionD = <span class="hljs-string">'px'</span> | <span class="hljs-string">'pt'</span>;
  type IntersectionUnionE = UnionC & UnionD;
  <span class="hljs-keyword">const</span> intersectionE: IntersectionUnionE = <span class="hljs-string">'any'</span> <span class="hljs-keyword">as</span> any; <span class="hljs-comment">// ts(2322) 不能赋予 'never' 类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">8.4联合、交叉组合</h3>
<p>在前面的示例中，我们把一些联合、交叉类型抽离成了类型别名，再把它作为原子类型进行进一步的联合、交叉。其实，<code>联合、交叉类型本身就可以直接组合使用</code>，这就涉及 |、& 操作符的优先级问题。实际上，联合、交叉运算符不仅在行为上表现一致，还在运算的优先级和 JavaScript 的逻辑或 ||、逻辑与 && 运算符上表现一致 。</p>
<p><code>联合操作符 | 的优先级低于交叉操作符 &</code>，同样，我们可以通过使用小括弧 () 来调整操作符的优先级。</p>
<pre><code class="hljs language-js copyable" lang="js">type UnionIntersectionA = &#123; <span class="hljs-attr">id</span>: number; &#125; & &#123; <span class="hljs-attr">name</span>: string; &#125; | &#123; <span class="hljs-attr">id</span>: string; &#125; & &#123; <span class="hljs-attr">name</span>: number; &#125;; <span class="hljs-comment">// 交叉操作符优先级高于联合操作符</span>
  type UnionIntersectionB = (<span class="hljs-string">'px'</span> | <span class="hljs-string">'em'</span> | <span class="hljs-string">'rem'</span> | <span class="hljs-string">'%'</span>) | (<span class="hljs-string">'vh'</span> | <span class="hljs-string">'em'</span> | <span class="hljs-string">'rem'</span> | <span class="hljs-string">'pt'</span>); <span class="hljs-comment">// 调整优先级</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以把<code>分配率、交换律等基本规则</code>引入类型组合中，然后优化出更简洁、清晰的类型</p>
<pre><code class="hljs language-js copyable" lang="js"> type UnionIntersectionC = (&#123; <span class="hljs-attr">id</span>: number; &#125; & &#123; <span class="hljs-attr">name</span>: string; &#125; | &#123; <span class="hljs-attr">id</span>: string; &#125;) & &#123; <span class="hljs-attr">name</span>: number; &#125;;
  type UnionIntersectionD = &#123; <span class="hljs-attr">id</span>: number; &#125; & &#123; <span class="hljs-attr">name</span>: string; &#125; & &#123; <span class="hljs-attr">name</span>: number; &#125; | &#123; <span class="hljs-attr">id</span>: string; &#125; & &#123; <span class="hljs-attr">name</span>: number; &#125;; <span class="hljs-comment">// 满足分配率</span>
  type UnionIntersectionE = (&#123; <span class="hljs-attr">id</span>: string; &#125; | &#123; <span class="hljs-attr">id</span>: number; &#125; & &#123; <span class="hljs-attr">name</span>: string; &#125;) & &#123; <span class="hljs-attr">name</span>: number; &#125;; <span class="hljs-comment">// 满足交换律</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">8.5类型缩减</h3>
<p><code>如果将 string 原始类型和“string字面量类型”组合成联合类型会是什么效果？效果就是类型缩减成 string 了。</code>
对于 number、boolean（其实还有枚举类型，详见第 9 讲）也是一样的缩减逻辑</p>
<pre><code class="hljs language-js copyable" lang="js">type URStr = <span class="hljs-string">'string'</span> | string; <span class="hljs-comment">// 类型是 string</span>
  type URNum = <span class="hljs-number">2</span> | number; <span class="hljs-comment">// 类型是 number</span>
  type URBoolen = <span class="hljs-literal">true</span> | boolean; <span class="hljs-comment">// 类型是 boolean</span>
  enum EnumUR &#123;
    ONE,
    TWO
  &#125;
  type URE = EnumUR.ONE | EnumUR; <span class="hljs-comment">// 类型是 EnumUR</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>TypeScript 对这样的场景做了缩减，它把字面量类型、枚举成员类型缩减掉，<code>只保留原始类型、枚举类型等父类型</code>，这是合理的“优化”。</p>
<p>可是这个缩减，却极大地削弱了 IDE 自动提示的能力</p>
<pre><code class="hljs language-js copyable" lang="js"> type BorderColor = <span class="hljs-string">'black'</span> | <span class="hljs-string">'red'</span> | <span class="hljs-string">'green'</span> | <span class="hljs-string">'yellow'</span> | <span class="hljs-string">'blue'</span> | string; <span class="hljs-comment">// 类型缩减成 string</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述代码中，我们希望 IDE 能自动提示显示注解的字符串字面量，但是因为类型被缩减成 string，所有的字符串字面量 black、red 等都无法自动提示出来了。
不要慌，TypeScript 官方其实还提供了一个黑魔法，它可以让类型缩减被控制。如下代码所示，我们只需要给父类型添加“& &#123;&#125;”即可。</p>
<pre><code class="hljs language-js copyable" lang="js">  type BorderColor = <span class="hljs-string">'black'</span> | <span class="hljs-string">'red'</span> | <span class="hljs-string">'green'</span> | <span class="hljs-string">'yellow'</span> | <span class="hljs-string">'blue'</span> | string & &#123;&#125;; <span class="hljs-comment">// 字面类型都被保留</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，其他字面量类型就不会被缩减掉了，在 IDE 中字符串字面量 black、red 等也就自然地可以自动提示出来了。</p>
<p>此外，<code>当联合类型的成员是接口类型，如果满足其中一个接口的属性是另外一个接口属性的子集，这个属性也会类型缩减</code>，如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js"> type UnionInterce =
  | &#123;
      <span class="hljs-attr">age</span>: <span class="hljs-string">'1'</span>;
    &#125;
  | (&#123;
      <span class="hljs-attr">age</span>: <span class="hljs-string">'1'</span> | <span class="hljs-string">'2'</span>;
      [key: string]: string;
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里因为 '1' 是 '1' | '2' 的子集，所以 age 的属性变成 '1' | '2'.</p>
<p>利用这个特性，我们来实现 07 讲中埋下的那个伏笔，如何定义如下所示 age 属性是数字类型，而其他不确定的属性是字符串类型的数据结构的对象？</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">age</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 数字类型</span>
  <span class="hljs-attr">anyProperty</span>: <span class="hljs-string">'str'</span>, <span class="hljs-comment">// 其他不确定的属性都是字符串类型</span>
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里提到这个伏笔，想必你应该明白了，我们肯定要用到两个接口的联合类型及类型缩减，<code>这个问题的核心在于找到一个既是 number 的子类型</code>，这样 age 类型缩减之后的类型就是 number；<code>同时也是 string 的子类型</code>，这样才能满足属性和 string 索引类型的约束关系。</p>
<p>哪个类型满足这个条件呢？我们一起回忆一下 02 讲中介绍的特殊类型 never。</p>
<p><code>never 有一个特性是它是所有类型的子类型</code>，自然也是 number 和 string 的子类型，所以答案如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js">type UnionInterce =
  | &#123;
      <span class="hljs-attr">age</span>: number;
    &#125;
  | (&#123;
      <span class="hljs-attr">age</span>: never;
      [key: string]: string;
    &#125;);
  <span class="hljs-keyword">const</span> O: UnionInterce = &#123;
    <span class="hljs-attr">age</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">string</span>: <span class="hljs-string">'string'</span>
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>学习和掌握联合和交叉类型后，可以培养我们抽离、复用公共类型的意识和能力。</p></div>  
</div>
            