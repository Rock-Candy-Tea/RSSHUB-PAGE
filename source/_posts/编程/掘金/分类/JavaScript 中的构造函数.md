
---
title: 'JavaScript 中的构造函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5e110915e7d4fb295aaaccdc336d662~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 22:27:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5e110915e7d4fb295aaaccdc336d662~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>面向对象设计的编程语言都会有三个基本特征：封装<sup id="user-content-fnref-1"><a href="https://juejin.cn/post/6963142029693943838#fn-1" class="footnote-ref">1</a></sup>、继承<sup id="user-content-fnref-2"><a href="https://juejin.cn/post/6963142029693943838#fn-2" class="footnote-ref">2</a></sup>和多态<sup id="user-content-fnref-3"><a href="https://juejin.cn/post/6963142029693943838#fn-3" class="footnote-ref">3</a></sup>，有了这三种特征的配合，才能将面向对象思想的优势尽可能的展现出来。 JavaScript 虽然是 OOP（Object-oriented programming）语言，但是由于它的动态语言特征，对「类」支持的不是很完善。</p>
<h2 data-id="heading-1">JavaScript 中的类 — 构造函数</h2>
<p>单从面向对象来说，JavaScript 做的的确不错，因为它可以不通过类直接创建对象。这样带来的最大优点就是能让初入门的开发者无需理解面向对象思想涉及到的概念就能直接上手开发，所谓依葫芦画瓢，别人咋写我咋写，就能运行了；缺点也是对应的，因为无法理解面向对象的核心思想，所以写出来的代码可能无法兼顾效率和性能。</p>
<p>JavaScript 为了照顾到更多的开发者，依然拿出了自己的"类"，它就是构造函数，例子如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Article</span>(<span class="hljs-params">title, content</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.title = title
   <span class="hljs-built_in">this</span>.content = content
&#125;

Article.prototype.Author = <span class="hljs-string">"wolfberry"</span>
Article.prototype.getAuthor = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.Author
&#125;

<span class="hljs-comment">// 实例化</span>
<span class="hljs-keyword">const</span> article = <span class="hljs-keyword">new</span> Article(<span class="hljs-string">"构造函数"</span>, <span class="hljs-string">"AAAA"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，JavaScript 编译器并不会区分函数是构造函数还是普通函数<sup id="user-content-fnref-4"><a href="https://juejin.cn/post/6963142029693943838#fn-4" class="footnote-ref">4</a></sup>，这就意味这任何一个 JavaScript 函数既是普通函数又是构造函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(Article(<span class="hljs-string">"构造函数"</span>, <span class="hljs-string">"AAAA"</span>), <span class="hljs-built_in">window</span>.title, <span class="hljs-built_in">window</span>.content)  <span class="hljs-comment">// undefined "构造函数" "AAAA"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为构造函数的词法作用域，直接调用的时候自身的 <code>this</code> 指向全局对象 <code>window</code> ，所以入参全部赋值到全局对象的属性上了。那么区别构造函数和普通函数的方式只能是 <code>new</code> 构造化调用了。</p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/new" target="_blank" rel="nofollow noopener noreferrer">MDN</a> 对 <code>new</code> 运算符的作用如此解释：</p>
<blockquote>
<p><strong><code>new</code> 运算符</strong>创建一个用户定义的对象类型的实例或具有构造函数的内置对象的实例。</p>
</blockquote>
<h3 data-id="heading-2">不完善之一 — 封装</h3>
<p>如何在 JavaScript 中有效的封装是许多 JavaScript 工具库开发者遇到的第一个难题。因为 JavaScript 的构造函数太过简陋，不支持静态、私有属性或者方法，而这些在工具库里面恰恰是不可或缺的。举个例子来说，我想在 <code>Article</code> 里面新增一个 <code>createTime</code> 属性，但是该属性不能是自己设定的，而是实例化的时候自动生成的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Article</span>(<span class="hljs-params">title, content</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.title = title
   <span class="hljs-built_in">this</span>.content = content
    <span class="hljs-built_in">this</span>.createTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
&#125;

<span class="hljs-keyword">const</span> article = <span class="hljs-keyword">new</span> Article(<span class="hljs-string">"构造函数"</span>, <span class="hljs-string">"AAAA"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的数据格式截图如下：</p>
<p><a href="https://imgtu.com/i/gcR6xI" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5e110915e7d4fb295aaaccdc336d662~tplv-k3u1fbpfcp-zoom-1.image" alt="gcR6xI.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>熟悉 JavaScript 的开发者都知道，一般情况下，对象是可以随意更改的，这就意味着 <code>creatTime</code> 属性是不安全的。为此社区提出的规范是这样的：私有属性通过前缀下划线以示区分：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-built_in">this</span>._createTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但这样也仅仅属于“掩耳盗铃”，因为规范不是语法，从代码层面依然可以通过实例化出来的对象随意修改该属性。那么，有没有更好的方式呢？有的，但是稍微麻烦点，而且也增加了理解难度：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Article</span>(<span class="hljs-params">title, content</span>) </span>&#123;
    <span class="hljs-comment">// 私有变量</span>
    <span class="hljs-keyword">const</span> createTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
    
    <span class="hljs-built_in">this</span>.title = title
   <span class="hljs-built_in">this</span>.content = content
    <span class="hljs-comment">// 特权函数</span>
    <span class="hljs-built_in">this</span>.getCreateTime = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> createTime
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将私有属性直接声明为变量，然后在构造函数里面创建特权函数获取该变量并返回。一定程度上隐藏了该属性，但是带来的问题就是该变量和特权函数存在于每个实例上，增加了资源的占用，显然不是一个很好的解决方案。</p>
<h3 data-id="heading-3">不完善之二 — 继承</h3>
<p>JavaScript 的继承会让子类和父类产生紧密的联系，父类的任何改动都有可能影响到子类，这与别的 OOP 语言大有不同。原因在于 JavaScript 的对象和构造函数都有“原型”这一概念，子类和父类通过原型产生继承关系，而原型又有行为委托的特性，父类的任何改动都有可能影响到子类。</p>
<blockquote>
<p>行为委托通俗点来说，就是在对象获取自身不存在的属性或者方法时，会去原型上继续寻找该属性和方法。</p>
</blockquote>
<p>可以从原型继承上可以了解到这一点：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
A.prototype.print = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.constructor.name)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">B</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
B.prototype = <span class="hljs-keyword">new</span> A

<span class="hljs-keyword">const</span> b = <span class="hljs-keyword">new</span> B
b.print()  <span class="hljs-comment">// A</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 <code>B.prototype</code> 链接到实例化后的 <code>A</code>，最终对象 <code>b</code> 的原型链如图所示：</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph LR
A[对象b] -- __proto__ --> B[实例化后的 A] -- __proto__ --> C[A.prototype] -- __proto__ --> D[Object.prototype] -- __proto__ --> F[null]
</code></pre>
<p>对于 <code>b.print()</code> 会沿着原型链直到在 <code>A.prototype</code> 找到才停止，然后运行该方法。此时将代码改成这样：</p>
<pre><code class="copyable">A.prototype.printIn = function() &#123;
    console.log(this.constructor.name)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接导致子类 <code>B</code> 的实例运行出错。原型继承是最简单也是最好理解的一种继承方式，可以<a href="https://zhuanlan.zhihu.com/p/110175302" target="_blank" rel="nofollow noopener noreferrer">点击此处</a>查看前人总结别的继承方式以及优缺点。虽然继承方案五花八门，但是终究离不开原型链的范畴，只要涉及到原型链就会有乱改父类的担忧。</p>
<h3 data-id="heading-4">不完善之三 — 多态</h3>
<p>基于前面的原型继承事实，我们知道当寻找自身不存在的属性时，引擎会沿着原型链继续查找。那如果查找的属性既出现在自身，原型链上又存在，就会出现原型屏蔽这样的结果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.age = <span class="hljs-number">20</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">PersonA</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.age = <span class="hljs-number">21</span>
&#125;
PersonA.prototype = <span class="hljs-keyword">new</span> Person

<span class="hljs-keyword">const</span> persona = <span class="hljs-keyword">new</span> PersonA
persona.age <span class="hljs-comment">// 21</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象 <code>persona</code> 中的属性 <code>age</code> 会屏蔽掉原型链上的所有 <code>age</code> 属性，因为 <code>persona.age</code> 总是会选择原型链中最底层的 <code>age</code> 属性，而这恰恰是实现多态的一种方式：覆盖。</p>
<p>除了覆盖，还有另一种 JavaScript 目前还不支持的可以实现多态的方式：重载，对象自身的方法与继承而来的方法重名时，可以通过入参个数的不同以示区分。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">B</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
B.prototype = <span class="hljs-keyword">new</span> A
B.prototype.print = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">param</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(param)
&#125;

<span class="hljs-keyword">const</span> b = <span class="hljs-keyword">new</span> B
b.print()  <span class="hljs-comment">// A</span>
b.print(<span class="hljs-string">'b'</span>)  <span class="hljs-comment">// b</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重载技术可用的情况下，上面的代码就是可行的。但同一属性名或者方法名都会产生原型遮蔽的效果，所以重载只能通过别的手段实现，比如通过判断入参数调用不同的方法。</p>
<h2 data-id="heading-5">最新技术 class</h2>
<p>ES6 的到来给 JavaScript 泵入了新的血液，大量的新特性让开发者欢呼雀跃，同时也给不少的开发者增加了理解成本。与此同时，构造函数也迎来了属于自己的春天——有了一个名正言顺的关键字 <code>class</code>，以及一些相关的特性。</p>
<h3 data-id="heading-6">更明确的「类」</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span></span>&#123;&#125;

<span class="hljs-keyword">const</span> a = <span class="hljs-keyword">new</span> A
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与构造函数相比，新的声明方式从语义上更为直白易懂，虽然本质上只是构造函数的语法糖。需要注意的是，通过 <code>class</code> 声明的「类」就不能直接以函数的方式调用了，这与之前稍有不同：</p>
<pre><code class="copyable">A()  // Uncaught TypeError: Class constructor A cannot be invoked without 'new'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台显示的错误提示我们必须使用 <code>new</code> 关键字实例化「类」，这在之前是没有的，但是可以模拟实现，需要用到 <code>new</code> 相关的特性：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">new</span>.target !== A) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">`Class constructor A cannot be invoked without 'new'`</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>new.target</code> 指向当前的构造函数本身，可以通过该特性模拟无法函数调用 <code>class</code> 行为。顺带一提，使用 <code>class</code> 关键字会默认启用严格模式，严格模式下声明不会提前，类内部的写法也需要额外注意。</p>
<h3 data-id="heading-7">更完备的封装</h3>
<p>除了类声明，类的属性和方法权限也有了更新，新增的静态、私有属性和方法大大方便了构建一个合理的工具类。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-keyword">static</span> value = <span class="hljs-number">1</span>
  #private_value = <span class="hljs-number">2</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>静态标识以 <code>static</code> 关键字开头，私有标识以 <code>#</code> 开头，这两种关键字都可以在属性和方法上使用。</p>
<h2 data-id="heading-8">总结</h2>
<p>ES6 虽然为构造函数注入了新的活力，依然改变不了语法糖的事实。在封装方面一定程度上提高了很多，但要是想对标 Java 这一类编程语言还有很多路要走；但是反过来想，为什么一定要对标？JavaScript 就走自己的路才能发挥动态语言的优势。</p>
<h2 data-id="heading-9">随写</h2>
<p>总算是憋出第二篇了，破玩意不写感觉不对劲，动手写发现就跟自己过不去，为何不把时间用在打两把游戏上？</p>
<p>还是那句话，如果我还能写，那就会出第三篇了！</p>
<p>各位安好！</p>
<div class="footnotes">
<hr>
<ol>
<li id="user-content-fn-1">将数据和操作数据的行为打包在一个单元内。<a href="https://juejin.cn/post/6963142029693943838#fnref-1" class="footnote-backref">↩</a></li>
<li id="user-content-fn-2">单元 A 获取到单元 B 的数据和行为。<a href="https://juejin.cn/post/6963142029693943838#fnref-2" class="footnote-backref">↩</a></li>
<li id="user-content-fn-3">基于继承特征，针对同样的行为有不同的结果。<a href="https://juejin.cn/post/6963142029693943838#fnref-3" class="footnote-backref">↩</a></li>
<li id="user-content-fn-4">构造函数的首字母大写只是社区规范，既然是规范就可以选择遵守或者不遵守，编译器不会以这样的规范调整自己的编译。<a href="https://juejin.cn/post/6963142029693943838#fnref-4" class="footnote-backref">↩</a></li>
</ol>
</div></div>  
</div>
            