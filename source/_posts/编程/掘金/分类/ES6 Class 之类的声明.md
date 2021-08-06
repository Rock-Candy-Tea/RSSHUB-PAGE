
---
title: 'ES6 Class 之类的声明'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/792ac71ad85749f287f16c35ddeb3635~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 15:41:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/792ac71ad85749f287f16c35ddeb3635~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">1. <code>ES5</code> 中定义类</h2>
<p><code>ES5</code> 中没有专门的类的语法，它是用函数（对于一个类来说，肯定要有构造函数，构造函数解决两个问题：第一个是传参数；第二个是实例化，也就是初始化）去模拟的。举个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 定义一个 Animal 类</span>
 <span class="hljs-keyword">let</span> Animal = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type</span>) </span>&#123;
   <span class="hljs-built_in">this</span>.type = type <span class="hljs-comment">// 定义一个属性并初始化</span>
   <span class="hljs-built_in">this</span>.eat = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// 定义一个 eat() 方法</span>
 &#125;
 
 <span class="hljs-comment">// 生成一个 dog 实例对象</span>
 <span class="hljs-keyword">let</span> dog = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'dog'</span>)
 <span class="hljs-comment">// 生成一个 monkey 实例对象</span>
 <span class="hljs-keyword">let</span> monkey = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'monkey'</span>)
 
 <span class="hljs-comment">// 打印这个 dog 实例对象</span>
 <span class="hljs-built_in">console</span>.log(dog)
 <span class="hljs-comment">// 打印这个 monkey 实例对象</span>
 <span class="hljs-built_in">console</span>.log(monkey)
 
 <span class="hljs-comment">/* 运行结果：
 Animal &#123;type: "dog", eat: ƒ&#125;
 Animal &#123;type: "monkey", eat: ƒ&#125;
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果看起来好像没什么问题，那我们修改一下类中的 <code>eat</code> 方法，在上面的 <code>eat</code> 方法中再添加一条语句，同时修改 <code>monkey</code> 对象的 <code>eat</code> 方法，然后分别调用 <code>dog</code> 和 <code>monkey</code> 的 <code>eat</code> 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> Animal = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type</span>) </span>&#123;
   <span class="hljs-built_in">this</span>.type = type
   <span class="hljs-built_in">this</span>.eat = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
     <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am eating food.'</span>) <span class="hljs-comment">// 在 eat 方法中添加一条语句</span>
   &#125;
 &#125;
 
 <span class="hljs-keyword">let</span> dog = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'dog'</span>)
 <span class="hljs-keyword">let</span> monkey = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'monkey'</span>)
 
 <span class="hljs-built_in">console</span>.log(dog)
 <span class="hljs-built_in">console</span>.log(monkey)
 
 <span class="hljs-comment">// 修改 monkey 对象的 eat 方法</span>
 monkey.eat = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error'</span>)
 &#125;
 
 <span class="hljs-comment">// 分别调用 dog 和 monkey 的 eat 方法</span>
 dog.eat()
 monkey.eat()
 
 <span class="hljs-comment">/* 运行结果：
 Animal &#123;type: "dog", eat: ƒ&#125;
 Animal &#123;type: "monkey", eat: ƒ&#125;
 I am eating food.
 error
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，修改了 <code>monkey</code> 对象的 <code>eat</code> 方法后，并没有影响到 <code>dog</code> 对象的 <code>eat</code> 方法。<code>dog</code> 成功执行了继承自 <code>Animal</code> 的 <code>eat</code> 方法，而 <code>monkey</code> 继承自 <code>Animal</code> 的 <code>eat</code> 方法被修改后，执行的就不再是 <code>Animal</code> 的 <code>eat</code> 方法，而是自己的 <code>eat</code> 方法了，这就<strong>违背了继承的原则</strong>，什么是继承？继承就是实例对象都继承了父类的某个方法，如果父类修改了这个方法，那么所有实例对象都会跟着改变。</p>
<p>此外，这样定义一个类还有一个问题，就是生成的每个实例对象都很大，因为每个对象都会有一个 <code>eat</code> 方法。那么该怎么写呢？</p>
<p>其实，非常简单，只要把共有的方法（像这里的 <code>eat</code> 方法）写在这个 <code>function</code> 的原型链（函数都有的一个对象，叫做 <code>prototype</code>，类继承的工作原理就是会沿着原型链往上找）上即可：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> Animal = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type</span>) </span>&#123;
   <span class="hljs-built_in">this</span>.type = type
 &#125;
 
 <span class="hljs-comment">// 使用原型链的方式定义 eat() 方法</span>
 Animal.prototype.eat = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am eating food.'</span>)
 &#125;
 
 <span class="hljs-keyword">let</span> dog = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'dog'</span>)
 <span class="hljs-keyword">let</span> monkey = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'monkey'</span>)
 
 <span class="hljs-built_in">console</span>.log(dog)
 <span class="hljs-built_in">console</span>.log(monkey)
 
 dog.eat()
 monkey.eat()
 
 <span class="hljs-comment">/* 运行结果：
 Animal &#123;type: "dog"&#125;
 Animal &#123;type: "monkey"&#125;
 I am eating food.
 I am eating food.
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果截图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/792ac71ad85749f287f16c35ddeb3635~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="ES5 中定义类" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中，<code>&#123;type: "dog"&#125;</code> 和 <code>&#123;type: "monkey"&#125;</code> 分别代表两个实例的本身，然后这两个实例都指向了作用域的上一层，也就是原型链上，上面挂载了 <code>eat</code> 方法，这就是用的原型链的方式做了继承（可以理解成一个树根和两个树杈，所有公共方法都放在了树根上，而不是树杈上）。结果就是都输出了相同的内容。</p>
<p>这时，如果我们修改其中一个实例对象原型链上的 <code>eat</code> 方法，另一个实例对象的原型链上的 <code>eat</code> 方法也会跟着改变：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> Animal = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type</span>) </span>&#123;
   <span class="hljs-built_in">this</span>.type = type 
 &#125;
 
 Animal.prototype.eat = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am eating food.'</span>)
 &#125;
 
 <span class="hljs-keyword">let</span> dog = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'dog'</span>)
 <span class="hljs-keyword">let</span> monkey = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'monkey'</span>)
 
 <span class="hljs-built_in">console</span>.log(dog)
 <span class="hljs-built_in">console</span>.log(monkey)
 
 <span class="hljs-comment">// 修改 monkey 对象原型链上的 eat 方法</span>
 monkey.constructor.prototype.eat = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// monkey.constructor 指的就是定义 Animal 的 function</span>
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error'</span>)
 &#125;
 
 dog.eat()
 monkey.eat()
 
 <span class="hljs-comment">/* 运行结果：
 Animal &#123;type: "dog"&#125;
 Animal &#123;type: "monkey"&#125;
 error
 error
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，最后都打印出了“<code>error</code>”。</p>
<blockquote>
<p>总结：<code>ES5</code> 中，把定义类的 <code>function</code> 当成构造函数去用，<code>function</code> 内只写实例对象独有的东西，而公有的东西都放到原型链上去。</p>
</blockquote>
<h2 data-id="heading-1">2. <code>ES6</code> 中定义类</h2>
<p><code>ES6</code> 使用 <code>class</code> 声明类，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
   <span class="hljs-comment">// 构造函数，传参，初始化</span>
   <span class="hljs-title">constructor</span> (<span class="hljs-params">type</span>) &#123;
     <span class="hljs-built_in">this</span>.type = type
   &#125;
   <span class="hljs-comment">// 定义一个 eat() 方法</span>
   eat () &#123;
     <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am eating food.'</span>)
   &#125;
 &#125;
 <span class="hljs-comment">// 生成一个 dog 实例对象</span>
 <span class="hljs-keyword">let</span> dog = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'dog'</span>)
 <span class="hljs-comment">// 生成一个 monkey 实例对象</span>
 <span class="hljs-keyword">let</span> monkey = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'monkey'</span>)
 
 <span class="hljs-built_in">console</span>.log(dog)
 <span class="hljs-built_in">console</span>.log(monkey)
 
 dog.eat()
 monkey.eat()
 <span class="hljs-comment">// 打印 Animal 的类型</span>
 <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> Animal)
 
 <span class="hljs-comment">/* 运行结果：
 Animal &#123;type: "dog"&#125;
 Animal &#123;type: "monkey"&#125;
 I am eating food.
 I am eating food.
 function
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果截图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db3a2caf496a443e9ac064281c867bcb~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="ES6 中定义类" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，上面通过 <code>typeof</code> 判断出 <code>class</code> 声明的 <code>Animal</code> 的类型也是 <code>function</code>（<code>ES5</code> 中就是用的 <code>function</code> 声明的类），<code>eat</code> 方法位于两个实例对象的原型链上，也就是说和 <code>ES5</code> 中直接写在 <code>function</code> 的原型链上的效果是一样的。换句话说，<strong><code>ES6</code> 中的 <code>class</code> 只是 <code>ES5</code> 中用原型链声明类的语法糖</strong><sup id="user-content-fnref-1"><a href="https://juejin.cn/post/6993094414792917029#fn-1" class="footnote-ref" target="_blank" title="#fn-1">1</a></sup>（语法不一样，但本质是一样的）。</p>
<blockquote>
<p>总结：<code>ES6</code> 中的 <code>class</code> 实际上是 <code>ES5</code> 中用原型链声明类的语法糖。</p>
</blockquote>
<div class="footnotes">
<hr>
<ol>
<li id="user-content-fn-1">指计算机语言中添加的某种语法，这种语法对语言的功能并没有影响，但是更方便程序员使用。通常来说使用语法糖能够增加程序的可读性，从而减少程序代码出错的机会。<a href="https://juejin.cn/post/6993094414792917029#fnref-1" class="footnote-backref" target="_blank" title="#fnref-1">↩</a></li>
</ol>
</div></div>  
</div>
            