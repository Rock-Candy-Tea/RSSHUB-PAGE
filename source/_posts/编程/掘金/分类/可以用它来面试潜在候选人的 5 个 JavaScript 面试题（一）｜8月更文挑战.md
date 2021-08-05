
---
title: '可以用它来面试潜在候选人的 5 个 JavaScript 面试题（一）｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6819'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 19:05:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=6819'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;position:relative;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;padding-left:8px;padding-bottom:0;margin-top:35px;margin-bottom:10px;font-weight:900;font-family:serif;letter-spacing:1px;color:#000&#125;.markdown-body h1:hover,.markdown-body h2:hover,.markdown-body h3:hover,.markdown-body h4:hover,.markdown-body h5:hover,.markdown-body h6:hover&#123;background-color:#fff&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;font-size:24px;position:relative&#125;.markdown-body h2:after&#123;content:"";left:0;bottom:0;width:100%;height:1px;position:absolute&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-size:4px 1px;background-image:linear-gradient(270deg,#37b2ff 0,#37b2ff 25%,transparent 50%)&#125;.markdown-body code&#123;margin:0 4px;word-break:break-word;overflow-x:auto;background-color:#fff7f7;color:#f06;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:-apple-system,system-ui,Menlo,Monaco,Consolas,Courier New;position:relative&#125;.markdown-body pre&#123;margin:15px 8px;border:1px solid #f5f5f7;line-height:1.75&#125;.markdown-body pre:before&#123;top:-4px;left:-4px;border-top:8px solid #feea1e;border-left:8px solid #feea1e&#125;.markdown-body pre:after,.markdown-body pre:before&#123;width:20px;height:20px;content:"";z-index:10;position:absolute&#125;.markdown-body pre:after&#123;right:-4px;bottom:-4px;border-right:8px solid #37b2ff;border-bottom:8px solid #37b2ff&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;overflow-x:auto;margin:0;word-break:normal;display:block;color:#333;background-color:#fff;background-image:linear-gradient(135deg,hsla(0,0%,87.8%,.1),hsla(0,0%,87.8%,.1) 25%,transparent 0,transparent 50%,hsla(0,0%,87.8%,.1) 0,hsla(0,0%,87.8%,.1) 75%,transparent 0,transparent)!important;background-size:10px 10px!important;position:unset!important&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#37b2ff;transition:.3s;border-bottom:1px dashed #37b2ff;position:relative;display:inline-block;vertical-align:bottom&#125;.markdown-body a:before&#123;bottom:90%;width:120px;max-width:0;content:"READ MORE +";color:#fff;background-color:#1fb3ff;position:absolute;white-space:nowrap;transition:.3s;box-sizing:border-box;pointer-events:none;overflow:hidden&#125;.markdown-body a:active:before,.markdown-body a:hover:before&#123;max-width:120px;padding-left:14px&#125;.markdown-body table&#123;width:100%;max-width:100%;font-size:12px;background-color:#fff;overflow:auto;border-collapse:collapse&#125;.markdown-body table tr:hover td,.markdown-body table tr:hover th&#123;border-bottom:1px solid #feea1e&#125;.markdown-body thead&#123;text-align:left&#125;.markdown-body th&#123;font-size:1.2em;border-bottom:1px dashed #eee&#125;.markdown-body tr:nth-child(2n)&#123;background-color:hsla(0,0%,87.8%,.1);border-bottom:1px solid #fff&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px;border-bottom:1px dashed #fff&#125;.markdown-body blockquote&#123;color:#666;padding:12px 23px 2px;border:1px solid #37b2ff;background-color:#fff;margin:22px 0;position:relative&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body blockquote:after&#123;content:"FROM";left:0;width:40px;color:#fff;background-color:#37b2ff;text-align:center&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;top:0;line-height:1;padding:2px 0;font-size:12px;font-weight:lighter;position:absolute;pointer-events:none&#125;.markdown-body blockquote:before&#123;content:"CITATION";left:44px;color:#37b2ff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;line-height:2em;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol ol li,.markdown-body ol ul li,.markdown-body ul ol li,.markdown-body ul ul li&#123;border-bottom:none&#125;.markdown-body ol li&#123;padding-left:6px;list-style:decimal-leading-zero&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;.markdown-body input[type=checkbox i]:disabled&#123;background-color:#6cf&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. ES6 的类和 ES5 的构造函数有什么区别？</h2>
<p>让我们来看一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ES5 构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
&#125;

<span class="hljs-comment">// ES6 类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于简单的构造函数而言，他们看起来很相似。</p>
<p>他们的主要区别体现在类继承上。如果我们想要创建一个继承于 <code>Person</code> 父类的 <code>Student</code> 子类，并且添加一个 <code>studentId</code> 字段，我们需要做的修改如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ES5 构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Student</span>(<span class="hljs-params">name, studentId</span>) </span>&#123;
  <span class="hljs-comment">// 调用父类的构造函数来初始化父类的成员变量</span>
  Person.call(<span class="hljs-built_in">this</span>, name);

  <span class="hljs-comment">// 初始化子类自己的成员变量</span>
  <span class="hljs-built_in">this</span>.studentId = studentId;
&#125;

Student.prototype = <span class="hljs-built_in">Object</span>.create(Person.prototype);
Student.prototype.constructor = Student;

<span class="hljs-comment">// ES6 类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, studentId</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name);
    <span class="hljs-built_in">this</span>.studentId = studentId;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的例子我们可以看出来，使用 ES5 构造函数来实现继承特别麻烦，而使用 ES6 类的方式来实现就特别容易理解和记忆。</p>
<h2 data-id="heading-1">2. 你能给出一个使用箭头函数的例子吗，箭头函数与其他函数有什么不同？</h2>
<p>一个很明显的优点就是箭头函数可以简化创建函数的语法，我们不需要在箭头函数前面加上 <code>function</code> 关键词。并且箭头函数的 <code>this</code> 会自动绑定到当前作用域的上下文中，这和普通的函数不一样。普通函数的 <code>this</code> 是在执行的时候才能确定的。箭头函数的这个特点对于回调函数来说特别有用，特别对于 React 组件而言。</p>
<h2 data-id="heading-2">3. 在构造函数中使用箭头函数有什么好处？</h2>
<p>在构造函数里使用箭头函数的主要优点是它的 <code>this</code> 只与箭头函数创建时的 <code>this</code> 保持一致，并且不会修改。所以，当用构造函数去创建一个新的对象的时候，箭头函数的 <code>this</code> 总是指向新创建的对象。比如，假设我们有一个 <code>Person</code> 构造函数，它接受一个 <code>firstName</code> 参数，并且它有两个方法去调用 <code>console.log</code> 这个 <code>firstName</code>，一个是正常的函数，而另一个则是箭头函数:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Person = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">firstName</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.firstName = firstName;
  <span class="hljs-built_in">this</span>.sayName1 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.firstName);
  &#125;;
  <span class="hljs-built_in">this</span>.sayName2 = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.firstName);
  &#125;;
&#125;;

<span class="hljs-keyword">const</span> john = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"John"</span>);
<span class="hljs-keyword">const</span> dave = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"Dave"</span>);

john.sayName1(); <span class="hljs-comment">// John</span>
john.sayName2(); <span class="hljs-comment">// John</span>

<span class="hljs-comment">// 普通函数的 this 可以被修改，而箭头函数则不会</span>
john.sayName1.call(dave); <span class="hljs-comment">// Dave (因为 "this" 现在指向了 dave 对象)</span>
john.sayName2.call(dave); <span class="hljs-comment">// John</span>

john.sayName1.apply(dave); <span class="hljs-comment">// Dave (因为 "this" 现在指向了 dave 对象)</span>
john.sayName2.apply(dave); <span class="hljs-comment">// John</span>

john.sayName1.bind(dave)(); <span class="hljs-comment">// Dave (因为 "this" 现在指向了 dave 对象)</span>
john.sayName2.bind(dave)(); <span class="hljs-comment">// John</span>

<span class="hljs-keyword">var</span> sayNameFromWindow1 = john.sayName1;
sayNameFromWindow1(); <span class="hljs-comment">// undefined (因为 "this" 现在指向了 Window 对象)</span>

<span class="hljs-keyword">var</span> sayNameFromWindow2 = john.sayName2;
sayNameFromWindow2(); <span class="hljs-comment">// John</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里主要的区别是，正常函数的 <code>this</code> 是可以在执行过程中被改变的，而箭头函数的 <code>this</code> 则会一直保持一致。所以在使用箭头函数的时候，你就不需要担心它的上下文被改变了。</p>
<p>这在 React 的类组件里非常有用。如果你使用普通的函数来定义一个类方法，比如一个点击处理函数，然后你将这个点击处理函数通过 prop 的形式传递给子节点，你将必须在父组件的 <code>constroctor</code> 里使用 <code>fn.bind(this)</code> 的形式来确保该函数能正常工作。但是如果你使用箭头函数的话，你就不需要手动去绑定 <code>this</code> 了，因为箭头函数会自动绑定创建时的 <code>this</code>。</p>
<h2 data-id="heading-3">4. 高阶函数（higher-order）的定义是什么？</h2>
<p>高阶函数是将一个或多个函数作为参数的函数，它用于数据处理，也可能将函数作为返回结果。高阶函数是为了抽象一些重复执行的操作。一个典型的例子是<code>map</code>，它将一个数组和一个函数作为参数。<code>map</code>使用这个函数来转换数组中的每个元素，并返回一个包含转换后元素的新数组。JavaScript 中的其他常见示例是<code>forEach</code>、<code>filter</code>和<code>reduce</code>。高阶函数不仅需要操作数组的时候会用到，还有许多函数返回新函数的用例。<code>Function.prototype.bind</code>就是一个例子。</p>
<p><strong>Map 示例：</strong></p>
<p>假设我们有一个由名字组成的数组，我们需要将每个字符转换为大写字母。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> names = [<span class="hljs-string">'irish'</span>, <span class="hljs-string">'daisy'</span>, <span class="hljs-string">'anna'</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不使用高阶函数的方法是这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> transformNamesToUppercase = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">names</span>) </span>&#123;
  <span class="hljs-keyword">const</span> results = [];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < names.length; i++) &#123;
    results.push(names[i].toUpperCase());
  &#125;
  <span class="hljs-keyword">return</span> results;
&#125;;
transformNamesToUppercase(names); <span class="hljs-comment">// ['IRISH', 'DAISY', 'ANNA']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>.map(transformerFn)</code>使代码更简明</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> transformNamesToUppercase = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">names</span>) </span>&#123;
  <span class="hljs-keyword">return</span> names.map(<span class="hljs-function">(<span class="hljs-params">name</span>) =></span> name.toUpperCase());
&#125;;
transformNamesToUppercase(names); <span class="hljs-comment">// ['IRISH', 'DAISY', 'ANNA']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">5. 请给出一个解构（destructuring）对象或数组的例子。</h2>
<p>解构是 ES6 中新功能，它提供了一种简洁方便的方法来提取对象或数组的值，并将它们放入不同的变量中。</p>
<h3 data-id="heading-5">5.1 数组解构</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 变量赋值</span>
<span class="hljs-keyword">const</span> foo = [<span class="hljs-string">'one'</span>, <span class="hljs-string">'two'</span>, <span class="hljs-string">'three'</span>];

<span class="hljs-keyword">const</span> [one, two, three] = foo;
<span class="hljs-built_in">console</span>.log(one); <span class="hljs-comment">// "one"</span>
<span class="hljs-built_in">console</span>.log(two); <span class="hljs-comment">// "two"</span>
<span class="hljs-built_in">console</span>.log(three); <span class="hljs-comment">// "three"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 变量交换</span>
<span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> b = <span class="hljs-number">3</span>;

[a, b] = [b, a];
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 3</span>
<span class="hljs-built_in">console</span>.log(b); <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">5.2 对象解构</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 变量赋值</span>
<span class="hljs-keyword">const</span> o = &#123;<span class="hljs-attr">p</span>: <span class="hljs-number">42</span>, <span class="hljs-attr">q</span>: <span class="hljs-literal">true</span>&#125;;
<span class="hljs-keyword">const</span> &#123;p, q&#125; = o;

<span class="hljs-built_in">console</span>.log(p); <span class="hljs-comment">// 42</span>
<span class="hljs-built_in">console</span>.log(q); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            