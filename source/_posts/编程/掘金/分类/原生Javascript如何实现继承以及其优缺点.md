
---
title: '原生Javascript如何实现继承以及其优缺点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7811'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 01:58:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=7811'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近在复习javascript的一些基础知识，为开启新的征程做准备。所以开始记录一些自己学习的内容。
那今天的主题是 <code>js的原生继承方式</code></p>
<h3 data-id="heading-0">废话少说，上代码！</h3>
<blockquote>
<p>首先是我们的父类代码。
在这里我们创建一个<code>Person</code>的类作为父类，它的构造函数需要2个参数<code>name</code>和<code>age</code>。</p>
</blockquote>
<p>然后我们在它的原型上添加一个<code>sayHi</code>的方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//父类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span> (<span class="hljs-params">name, age</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name || <span class="hljs-string">'no name'</span>;
    <span class="hljs-built_in">this</span>.age = age || <span class="hljs-number">0</span>;
&#125;

Person.prototype.sayHi = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hi, I\'m '</span> + <span class="hljs-built_in">this</span>.name + <span class="hljs-string">' and i\'m '</span> + <span class="hljs-built_in">this</span>.age + <span class="hljs-string">' years old!'</span>);
&#125;

<span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'A'</span>,<span class="hljs-number">20</span>);
p.sayHi();<span class="hljs-comment">//Hi, I'm A and i'm 20 years old!</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h3 data-id="heading-1">原型继承</h3>
<br>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//原型继承</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Teacher</span>(<span class="hljs-params"></span>)</span>&#123;
&#125;

Teacher.prototype=<span class="hljs-keyword">new</span> Person(<span class="hljs-string">'B'</span>,<span class="hljs-number">22</span>);
Teacher.prototype.constructor=Teacher;

<span class="hljs-keyword">var</span> t = <span class="hljs-keyword">new</span> Teacher();
t.sayHi();<span class="hljs-comment">//Hi, I'm B and i'm 22 years old!</span>
<span class="hljs-built_in">console</span>.log(t <span class="hljs-keyword">instanceof</span> Person);<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(t <span class="hljs-keyword">instanceof</span> Teacher);<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<blockquote>
<h4 data-id="heading-2">优点</h4>从上面的代码来看，<code>Teacher</code> 的实例拥有了 <code>Person</code> 的属性和方法。并且实例对象既是 <code>Person</code>的实例也是 <code>Teacher</code>的实例。而且这种继承方式特别的简单。
</blockquote>
<blockquote>
<h4 data-id="heading-3">缺点</h4>
我们可以很容易的就发现Teacher类的 <code>name</code>和 <code>age</code>是固定的，都是name=B和age=22，换句话说就是我们无法实现按照我们的意愿给父类的构造函数传参。并且一个我们不能给一个 <code>Teacher</code> 指定多个原型，也就是没法 <code>多继承</code>。然后我们看下下面这段代码：
</blockquote>
<br>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> t1 = <span class="hljs-keyword">new</span> Teacher();
<span class="hljs-keyword">var</span> t2 = <span class="hljs-keyword">new</span> Teacher();
Teacher.prototype.name = <span class="hljs-string">"C"</span>;
t1.sayHi();<span class="hljs-comment">//Hi, I'm C and i'm 22 years old!</span>
t2.sayHi();<span class="hljs-comment">//Hi, I'm C and i'm 22 years old!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<blockquote>
<p>上面这段代码中我们可以看到当原型中的属性或者方法被改变时，所有的子类实例的属性和方法也会跟着被改变，也就是原型继承的另一个缺点：<code>所有子类共享同一个原型对象</code></p>
</blockquote>
<blockquote>
<p>这里说到了<code>原型</code>,我很早之前也写过一个关于原型的随笔，不过可能也是有些模糊，现在的理解和当时有所不同，我会在后面重新写一篇关于原型的随笔。（写好了我会附上连接）</p>
</blockquote>
<h3 data-id="heading-4">构造函数继承</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//构造函数继承</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Teacher</span> (<span class="hljs-params">name, age</span>) </span>&#123;
    Person.call(<span class="hljs-built_in">this</span>, name, age);
&#125;

<span class="hljs-keyword">var</span> t1 = <span class="hljs-keyword">new</span> Teacher(<span class="hljs-string">'B'</span>, <span class="hljs-number">22</span>);
<span class="hljs-keyword">var</span> t2 = <span class="hljs-keyword">new</span> Teacher(<span class="hljs-string">'C'</span>, <span class="hljs-number">30</span>);
<span class="hljs-built_in">console</span>.log(t1.name);<span class="hljs-comment">//B</span>
<span class="hljs-built_in">console</span>.log(t2.name);<span class="hljs-comment">//C</span>
<span class="hljs-built_in">console</span>.log(t1 <span class="hljs-keyword">instanceof</span> Person);<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(t1 <span class="hljs-keyword">instanceof</span> Teacher);<span class="hljs-comment">//true</span>
t1.sayHi();<span class="hljs-comment">//TypeError: t1.sayHi is not a function</span>
t2.sayHi();<span class="hljs-comment">//TypeError: t1.sayHi is not a function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<blockquote>
<h4 data-id="heading-5">优点</h4>
相对于 <code>原型继承</code> ， <code>构造函数继承</code>解决了所有的子类实例共享统一原型的问题，也可以给父类的构造函数传参，并且我们可以在子类的构造函数中调用多个父类的构造函数，实现所谓的多继承<span>（这里的多继承是指子类通过call,apply等方法去调用父类的构造函数使其拥有父类的属性和方法，但是js中一个函数对象只存在一个 prototype,所以其实我们没法通过原型链的形式去体现出多继承）</span>
</blockquote>
<br>
<blockquote>
<h4 data-id="heading-6">缺点</h4>
上面的代码中我们可以看出创建的实例只是 <code>子类的实例</code> 并不是 <code>父类的实例</code> ，不能直观的体现出继承，这种继承方式也无法继承父类的原型上的属性和方法。
</blockquote>
<h3 data-id="heading-7">组合式继承</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//组合式继承</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Teacher</span> (<span class="hljs-params">name, age</span>) </span>&#123;
    Person.call(<span class="hljs-built_in">this</span>, name, age);
&#125;

Teacher.prototype = <span class="hljs-keyword">new</span> Person();
Teacher.prototype.constructor = Teacher;


<span class="hljs-keyword">var</span> t1 = <span class="hljs-keyword">new</span> Teacher(<span class="hljs-string">'B'</span>, <span class="hljs-number">22</span>);
<span class="hljs-keyword">var</span> t2 = <span class="hljs-keyword">new</span> Teacher(<span class="hljs-string">'C'</span>, <span class="hljs-number">30</span>);
Teacher.prototype.name = <span class="hljs-string">"D"</span>;
<span class="hljs-built_in">console</span>.log(t1.name);<span class="hljs-comment">//B</span>
<span class="hljs-built_in">console</span>.log(t2.name);<span class="hljs-comment">//C</span>
t1.sayHi();<span class="hljs-comment">//Hi, I'm B and i'm 22 years old!</span>
t2.sayHi();<span class="hljs-comment">//Hi, I'm C and i'm 30 years old!</span>
<span class="hljs-built_in">console</span>.log(t1 <span class="hljs-keyword">instanceof</span> Person);<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(t1 <span class="hljs-keyword">instanceof</span> Teacher);<span class="hljs-comment">//true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<blockquote>
<p>组合式继承就是结合了<code>原型继承</code>和<code>构造函数继承</code>的优点，解决了两种方式存在的一些缺点。但是我们会发现每当我们去创建一个子类实例的时候都会去创建一个父类的实例，尽管父类实例不是同一个实例（内存地址不一样），但是他们其实属性和方法上完全一致，所以我们通过下面这种（寄生式组合继承）方式完善它，以避免不必要的实例构造。</p>
</blockquote>
<br>
<h3 data-id="heading-8">寄生式组合继承</h3>
<br>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//寄生式组合继承</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Teacher</span> (<span class="hljs-params">name, age</span>) </span>&#123;
    Person.call(<span class="hljs-built_in">this</span>, name, age);
&#125;

Teacher.prototype = <span class="hljs-built_in">Object</span>.create(Person.prototype);
Teacher.prototype.constructor = Teacher;


<span class="hljs-keyword">var</span> t1 = <span class="hljs-keyword">new</span> Teacher(<span class="hljs-string">'B'</span>, <span class="hljs-number">22</span>);
<span class="hljs-keyword">var</span> t2 = <span class="hljs-keyword">new</span> Teacher(<span class="hljs-string">'C'</span>, <span class="hljs-number">30</span>);
Teacher.prototype.name = <span class="hljs-string">"D"</span>;
<span class="hljs-built_in">console</span>.log(t1.name);<span class="hljs-comment">//B</span>
<span class="hljs-built_in">console</span>.log(t2.name);<span class="hljs-comment">//C</span>
t1.sayHi();<span class="hljs-comment">//Hi, I'm B and i'm 22 years old!  </span>
t2.sayHi();<span class="hljs-comment">//Hi, I'm C and i'm 30 years old!</span>
<span class="hljs-built_in">console</span>.log(t1 <span class="hljs-keyword">instanceof</span> Person);<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(t1 <span class="hljs-keyword">instanceof</span> Teacher);<span class="hljs-comment">//true </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<blockquote>
<p>上面的方式解决了我们没创建一个子类实例都去创建一个父类实例的问题，这也是最为常用的一种js的继承方式，如果我们通过Babel去把ES6中的class的继承转成ES5的代码，我们会发现就是用的寄生式组合继承。</p>
</blockquote>
<blockquote>
<p>好的，到这里我把我常见的原生js继承方式及其优缺点就写完，如果你们看到了错误的点，欢迎留言指正~</p>
</blockquote></div>  
</div>
            