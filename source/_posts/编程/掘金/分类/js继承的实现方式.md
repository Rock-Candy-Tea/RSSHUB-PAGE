
---
title: 'js继承的实现方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/398300eb490b40f19653a55df022924b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 06:41:53 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/398300eb490b40f19653a55df022924b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>要实现继承，必须要有一个父类</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">//定义一个动物类</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span>(<span class="hljs-params">name</span>)</span>&#123;
     <span class="hljs-comment">//属性</span>
      <span class="hljs-built_in">this</span>.name = name;
      <span class="hljs-comment">//实例方法</span>
      <span class="hljs-built_in">this</span>.sleep = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">'正在睡觉'</span>);
      &#125;
    &#125;
    <span class="hljs-comment">//原型方法</span>
    Animal.prototype.eat = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">food</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">'正在吃'</span> + food);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-0">1.原型链继承</h3>
<p><strong>核心</strong> 将父类的实例作为子类的原型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params"></span>)</span>&#123;

&#125;
Cat.prototype = <span class="hljs-keyword">new</span> Animal();
Cat.prototype.name = <span class="hljs-string">'cat'</span>;

<span class="hljs-keyword">var</span> cat = <span class="hljs-keyword">new</span> Cat();
<span class="hljs-built_in">console</span>.log(cat.name);   <span class="hljs-comment">//cat</span>
<span class="hljs-built_in">console</span>.log(cat.eat(<span class="hljs-string">'fish'</span>)); <span class="hljs-comment">//cat正在吃fish</span>
<span class="hljs-built_in">console</span>.log(cat.sleep());  <span class="hljs-comment">//cat正在睡觉</span>
<span class="hljs-built_in">console</span>.log(cat <span class="hljs-keyword">instanceof</span> Animal); <span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(cat <span class="hljs-keyword">instanceof</span> Cat);  <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>特点：简单易于实现，父类的新增的实例与属性子类都能访问</p>
</blockquote>
<blockquote>
<p>缺点：可以在子类中增加实例属性，如果要新增加原型属性和方法需要在new父类构造函数的后面 ,无法实现多继承 , 创建子类实例的时候，不能向父类构造函数中传参</p>
</blockquote>
<h2 data-id="heading-1"><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/398300eb490b40f19653a55df022924b~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></h2>
<h3 data-id="heading-2">2.构造继承</h3>
<p><strong>核心</strong> 使用父类的构造函数来增强子类实例，等于是复制父类的实例属性给子类</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>)</span>&#123;
    Animal.call(<span class="hljs-built_in">this</span>,<span class="hljs-string">'cat'</span>);
  &#125;
  <span class="hljs-keyword">let</span> cat = <span class="hljs-keyword">new</span> Cat();
  <span class="hljs-built_in">console</span>.log(cat.name);  <span class="hljs-comment">//cat</span>
  <span class="hljs-built_in">console</span>.log(cat.sleep());   <span class="hljs-comment">//cat正在睡觉</span>
  <span class="hljs-built_in">console</span>.log(cat <span class="hljs-keyword">instanceof</span> Animal);  <span class="hljs-comment">//false</span>
  <span class="hljs-built_in">console</span>.log(cat <span class="hljs-keyword">instanceof</span> Cat);  <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/601a07b93b86490ba4905baf8bb16064~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>特点：解决了子类构造函数向父类构造函数中传递参数，可以实现多继承（call或者apply多个父类）</p>
</blockquote>
<blockquote>
<p>缺点：方法都在构造函数中定义，无法复用。不能继承原型属性、方法，只能继承父类的实例属性和方法</p>
</blockquote>
<hr>
<h3 data-id="heading-3">3.实例继承</h3>
<p><strong>核心</strong>：为父类实例添加新特性，作为子实例返回</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>)</span>&#123;
  <span class="hljs-keyword">var</span> instance = <span class="hljs-keyword">new</span> Animal(name);
  <span class="hljs-keyword">return</span> instance;
&#125; 
<span class="hljs-keyword">var</span> cat = <span class="hljs-keyword">new</span> Cat(<span class="hljs-string">'cat'</span>);
<span class="hljs-built_in">console</span>.log(cat.name);  <span class="hljs-comment">//Tom</span>
<span class="hljs-built_in">console</span>.log(cat.sleep());  <span class="hljs-comment">//Tom正在睡觉</span>
<span class="hljs-built_in">console</span>.log(cat <span class="hljs-keyword">instanceof</span> Animal);  <span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(cat <span class="hljs-keyword">instanceof</span> Cat);   <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc43bd90ec54499c8f2ece5ecca04bdd~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>特点：不限制调用方式，简单易实现</p>
</blockquote>
<blockquote>
<p>缺点：不能多次继承</p>
</blockquote>
<h3 data-id="heading-4">4.拷贝继承</h3>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>)</span>&#123;
  <span class="hljs-keyword">var</span> animal = <span class="hljs-keyword">new</span> Animal();
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> animal)&#123;
    Cat.prototype[key] = animal[key];
  &#125;
  <span class="hljs-comment">//如果使用prototye.name = name；会出现所有实例的name都是相同的，不能设置到原型上</span>
  <span class="hljs-built_in">this</span>.name = name;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab58c51703e246a68ccbaca2d6e69e9e~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>优点：支持多继承</p>
</blockquote>
<blockquote>
<p>缺点：效率低，内存占用高  ， 无法获取父类不可枚举的方法</p>
</blockquote>
<h3 data-id="heading-5">5.组合继承</h3>
<p>核心：通过调用父类构造，继承父类的属性并保留传参的优点，然后通过将父类实例作为子类原型，实现函数复用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>)</span>&#123;
  Animal.call(<span class="hljs-built_in">this</span>,name);
&#125;
Cat.prototype = <span class="hljs-keyword">new</span> Animal();
<span class="hljs-comment">//组合继承需要修复构造函数的指向</span>
Cat.prototype.constructor = <span class="hljs-string">'Cat'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dabe146037241c8beed2984973aa281~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>优点：既可以继承属性，也可以继承方法。既是子类的实例，也是父类的实例。不存在引用属性共享的问题。可传参。函数可复用</p>
</blockquote>
<h3 data-id="heading-6">6.寄生组合继承</h3>
<p>核心：通过寄生的形式，砍掉父元素的实例属性，这样在调用两次父类的构造的时候，就不会初始化两次实例方法和属性，避免了组合继承的缺点</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>)</span>&#123;
   Animal.call(<span class="hljs-built_in">this</span>,name);
 &#125;
 (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
 <span class="hljs-comment">//创建一个没有实例方法的类</span>
 <span class="hljs-keyword">var</span> Super = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
 Super.prototype = Animal.prototype;
 Cat.prototype = <span class="hljs-keyword">new</span> Super();
 &#125;)()
 <span class="hljs-comment">//寄生组合继承需要修复构造函数的指向</span>
 Cat.prototype.constructor = <span class="hljs-string">'Cat'</span>;
 <span class="hljs-keyword">var</span> cat = <span class="hljs-keyword">new</span> Cat(<span class="hljs-string">'cat'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccadcae56a474a598edd9d7af8680d35~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>优点：堪称完美</p>
</blockquote>
<blockquote>
<p>缺点：实现较为复杂</p>
</blockquote>
<h3 data-id="heading-7">es6继承</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//class  相当于es5中的构造函数</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">People</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name=<span class="hljs-string">'wang'</span>,age=<span class="hljs-string">'27'</span></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.age = age;
  &#125;
  <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> eat food`</span>);
  &#125;
&#125;
<span class="hljs-comment">//继承父类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Woman</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">People</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name=<span class="hljs-string">'ren'</span>,age=<span class="hljs-string">'27'</span></span>)</span>&#123;
     <span class="hljs-built_in">super</span>(name,age);
  &#125;
  <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-built_in">super</span>.eat()
  &#125;
&#125;
<span class="hljs-keyword">let</span> womanObj = <span class="hljs-keyword">new</span> Woman(<span class="hljs-string">'xiaoxiami'</span>);
womanObj.eat();
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            