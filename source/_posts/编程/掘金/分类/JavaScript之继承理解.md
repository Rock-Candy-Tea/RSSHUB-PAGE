
---
title: 'JavaScript之继承理解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e1a6a1e11934e9f86a0b576a21946e8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 02:02:11 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e1a6a1e11934e9f86a0b576a21946e8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第20天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>”</p>
<h4 data-id="heading-0">继承概念的探究</h4>
<ul>
<li>
<p>说到继承的概念，首先要说一个经典的例子。</p>
</li>
<li>
<p>先定义一个类（Class）叫汽车，汽车的属性包括颜色、轮胎、品牌、速度、排气量等，由汽车这个类可以派生出“轿车”和“货车”两个类，那么可以在汽车的基础属性上，为轿车添加一个后备厢、给货车添加一个大货箱。这样轿车和货车就是不一样的，但是二者都属于汽车这个类，这样从这个例子中就能详细说明汽车、轿车以及卡车之间的继承关系。</p>
</li>
<li>
<p>继承可以使得子类别具有父类的各种方法和属性，比如上面的例子中“轿车” 和 “货车” 分别继承了汽车的属性，而不需要再次在“轿车”中定义汽车已经有的属性。在“轿车”继承“汽车”的同时，也可以重新定义汽车的某些属性，并重写或覆盖某些属性和方法，使其获得与“汽车”这个父类不同的属性和方法。</p>
</li>
</ul>
<p>继承的基本概念就初步介绍这些，下面我们就来看看 JavaScript 中都有哪些实现继承的方法。</p>
<h4 data-id="heading-1">JS 实现继承的几种方式</h4>
<h5 data-id="heading-2">第一种：原型链继承</h5>
<ul>
<li>原型链继承是比较常见的继承方式之一，其中涉及的构造函数、原型和实例，三者之间存在着一定的关系，即每一个构造函数都有一个原型对象，原型对象又包含一个指向构造函数的指针，而实例则包含一个原型对象的指针。</li>
</ul>
<p>下面我们结合代码来了解一下。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'parent1'</span>;
    <span class="hljs-built_in">this</span>.play = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.type = <span class="hljs-string">'child2'</span>;
  &#125;
  Child1.prototype = <span class="hljs-keyword">new</span> Parent1();
  <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> Child1());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码看似没有问题，虽然父类的方法和属性都能够访问，但其实有一个潜在的问题，我再举个例子来说明这个问题。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">var</span> s1 = <span class="hljs-keyword">new</span> Child1();
  <span class="hljs-keyword">var</span> s2 = <span class="hljs-keyword">new</span> Child2();
  s1.play.push(<span class="hljs-number">4</span>);
  <span class="hljs-built_in">console</span>.log(s1.play, s2.play);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码在控制台执行之后，可以看到结果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e1a6a1e11934e9f86a0b576a21946e8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>明明我只改变了 s1 的 play 属性，为什么 s2 也跟着变了呢？原因很简单，因为两个实例使用的是同一个原型对象。它们的内存空间是共享的，当一个发生变化的时候，另外一个也随之进行了变化，这就是使用原型链继承方式的一个缺点。</p>
<p>那么要解决这个问题的话，我们就得再看看其他的继承方式，下面我们看看能解决原型属性共享问题的第二种方法。</p>
<h5 data-id="heading-3">第二种：构造函数继承（借助 call）</h5>
<p>直接通过代码来了解，如下所示。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent1</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'parent1'</span>;
  &#125;

  Parent1.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child1</span>(<span class="hljs-params"></span>)</span>&#123;
    Parent1.call(<span class="hljs-built_in">this</span>);
    <span class="hljs-built_in">this</span>.type = <span class="hljs-string">'child1'</span>
  &#125;

  <span class="hljs-keyword">let</span> child = <span class="hljs-keyword">new</span> Child1();
  <span class="hljs-built_in">console</span>.log(child);  <span class="hljs-comment">// 没问题</span>
  <span class="hljs-built_in">console</span>.log(child.getName());  <span class="hljs-comment">// 会报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行上面的这段代码，可以得到这样的结果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fb33f6fdbd24d98a6f991dec090d2a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>可以看到最后打印的 child 在控制台显示，除了 Child1 的属性 type 之外，也继承了 Parent1 的属性 name。这样写的时候子类虽然能够拿到父类的属性值，解决了第一种继承方式的弊端，但问题是，父类原型对象中一旦存在父类之前自己定义的方法，那么子类将无法继承这些方法。这种情况的控制台执行结果如下图所示。</li>
</ul>
<p>因此，从上面的结果就可以看到构造函数实现继承的优缺点，它使父类的引用属性不会被共享，优化了第一种继承方式的弊端；但是随之而来的缺点也比较明显——只能继承父类的实例属性和方法，不能继承原型属性或者方法。</p>
<p>上面的两种继承方式各有优缺点，那么结合二者的优点，于是就产生了下面这种组合的继承方式。</p>
<h5 data-id="heading-4">第三种：组合继承（前两种组合）</h5>
<p>这种方式结合了前两种继承方式的优缺点，结合起来的继承，代码如下。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent3</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'parent3'</span>;
    <span class="hljs-built_in">this</span>.play = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
  &#125;

  Parent3.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child3</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 第二次调用 Parent3()</span>
    Parent3.call(<span class="hljs-built_in">this</span>);
    <span class="hljs-built_in">this</span>.type = <span class="hljs-string">'child3'</span>;
  &#125;

  <span class="hljs-comment">// 第一次调用 Parent3()</span>
  Child3.prototype = <span class="hljs-keyword">new</span> Parent3();
  <span class="hljs-comment">// 手动挂上构造器，指向自己的构造函数</span>
  Child3.prototype.constructor = Child3;
  <span class="hljs-keyword">var</span> s3 = <span class="hljs-keyword">new</span> Child3();
  <span class="hljs-keyword">var</span> s4 = <span class="hljs-keyword">new</span> Child3();
  s3.play.push(<span class="hljs-number">4</span>);
  <span class="hljs-built_in">console</span>.log(s3.play, s4.play);  <span class="hljs-comment">// 不互相影响</span>
  <span class="hljs-built_in">console</span>.log(s3.getName()); <span class="hljs-comment">// 正常输出'parent3'</span>
  <span class="hljs-built_in">console</span>.log(s4.getName()); <span class="hljs-comment">// 正常输出'parent3'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行上面的代码，可以看到控制台的输出结果，之前方法一和方法二的问题都得以解决。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/036e26bb27a642a5b42de283be6b3711~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是这里又增加了一个新问题：通过注释我们可以看到 Parent3 执行了两次，第一次是改变Child3 的 prototype 的时候，第二次是通过 call 方法调用 Parent3 的时候，那么 Parent3 多构造一次就多进行了一次性能开销，这是我们不愿看到的。</p>
<p>那么是否有更好的办法解决这个问题呢？请你再往下学习，下面的第六种继承方式可以更好地解决这里的问题。</p>
<p>上面介绍的更多是围绕着构造函数的方式，那么对于 JavaScript 的普通对象，怎么实现继承呢？</p>
<p>第四种：原型式继承
这里不得不提到的就是 ES5 里面的 Object.create 方法，这个方法接收两个参数：一是用作新对象原型的对象、二是为新对象定义额外属性的对象（可选参数）。</p>
<p>我们通过一段代码，看看普通对象是怎么实现的继承。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> parent4 = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"parent4"</span>,
    <span class="hljs-attr">friends</span>: [<span class="hljs-string">"p1"</span>, <span class="hljs-string">"p2"</span>, <span class="hljs-string">"p3"</span>],
    <span class="hljs-attr">getName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
    &#125;
  &#125;;

  <span class="hljs-keyword">let</span> person4 = <span class="hljs-built_in">Object</span>.create(parent4);
  person4.name = <span class="hljs-string">"tom"</span>;
  person4.friends.push(<span class="hljs-string">"jerry"</span>);

  <span class="hljs-keyword">let</span> person5 = <span class="hljs-built_in">Object</span>.create(parent4);
  person5.friends.push(<span class="hljs-string">"lucy"</span>);

  <span class="hljs-built_in">console</span>.log(person4.name);
  <span class="hljs-built_in">console</span>.log(person4.name === person4.getName());
  <span class="hljs-built_in">console</span>.log(person5.name);
  <span class="hljs-built_in">console</span>.log(person4.friends);
  <span class="hljs-built_in">console</span>.log(person5.friends);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码中可以看到，通过 Object.create 这个方法可以实现普通对象的继承，不仅仅能继承属性，同样也可以继承 getName 的方法，请看这段代码的执行结果。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/748e0907319744e18c9c76631064a11b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>第一个结果“tom”，比较容易理解，person4 继承了 parent4 的 name 属性，但是在这个基础上又进行了自定义。</p>
</li>
<li>
<p>第二个是继承过来的 getName 方法检查自己的 name 是否和属性里面的值一样，答案是 true。</p>
</li>
<li>
<p>第三个结果“parent4”也比较容易理解，person5 继承了 parent4 的 name 属性，没有进行覆盖，因此输出父对象的属性。</p>
</li>
<li>
<p>最后两个输出结果是一样的，讲到这里你应该可以联想到 02 讲中浅拷贝的知识点，关于引用数据类型“共享”的问题，其实 Object.create 方法是可以为一些对象实现浅拷贝的。</p>
</li>
</ul>
<p>那么关于这种继承方式的缺点也很明显，多个实例的引用类型属性指向相同的内存，存在篡改的可能，接下来我们看一下在这个继承基础上进行优化之后的另一种继承方式——寄生式继承。</p>
<h5 data-id="heading-5">第五种：寄生式继承</h5>
<p>使用原型式继承可以获得一份目标对象的浅拷贝，然后利用这个浅拷贝的能力再进行增强，添加一些方法，这样的继承方式就叫作寄生式继承。</p>
<p>虽然其优缺点和原型式继承一样，但是对于普通对象的继承方式来说，寄生式继承相比于原型式继承，还是在父类基础上添加了更多的方法。那么我们看一下代码是怎么实现。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">let</span> parent5 = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"parent5"</span>,
    <span class="hljs-attr">friends</span>: [<span class="hljs-string">"p1"</span>, <span class="hljs-string">"p2"</span>, <span class="hljs-string">"p3"</span>],
    <span class="hljs-attr">getName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
    &#125;
  &#125;;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clone</span>(<span class="hljs-params">original</span>) </span>&#123;
    <span class="hljs-keyword">let</span> clone = <span class="hljs-built_in">Object</span>.create(original);
    clone.getFriends = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.friends;
    &#125;;
    <span class="hljs-keyword">return</span> clone;
  &#125;

  <span class="hljs-keyword">let</span> person5 = clone(parent5);

  <span class="hljs-built_in">console</span>.log(person5.getName());
  <span class="hljs-built_in">console</span>.log(person5.getFriends());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面这段代码，我们可以看到 person5 是通过寄生式继承生成的实例，它不仅仅有 getName 的方法，而且可以看到它最后也拥有了 getFriends 的方法，结果如下图所示。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4e35acc020f48ffb86cf3e83ecbb5fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从最后的输出结果中可以看到，person5 通过 clone 的方法，增加了 getFriends 的方法，从而使 person5 这个普通对象在继承过程中又增加了一个方法，这样的继承方式就是寄生式继承。</p>
<p>我在上面第三种组合继承方式中提到了一些弊端，即两次调用父类的构造函数造成浪费，下面要介绍的寄生组合继承就可以解决这个问题。</p>
<h5 data-id="heading-6">第六种：寄生组合式继承</h5>
<p>结合第四种中提及的继承方式，解决普通对象的继承问题的 Object.create 方法，我们在前面这几种继承方式的优缺点基础上进行改造，得出了寄生组合式的继承方式，这也是所有继承方式里面相对最优的继承方式，代码如下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clone</span> (<span class="hljs-params">parent, child</span>) </span>&#123;
    <span class="hljs-comment">// 这里改用 Object.create 就可以减少组合继承中多进行一次构造的过程</span>
    child.prototype = <span class="hljs-built_in">Object</span>.create(parent.prototype);
    child.prototype.constructor = child;
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent6</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'parent6'</span>;
    <span class="hljs-built_in">this</span>.play = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
  &#125;
   Parent6.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child6</span>(<span class="hljs-params"></span>) </span>&#123;
    Parent6.call(<span class="hljs-built_in">this</span>);
    <span class="hljs-built_in">this</span>.friends = <span class="hljs-string">'child5'</span>;
  &#125;

  clone(Parent6, Child6);

  Child6.prototype.getFriends = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.friends;
  &#125;

  <span class="hljs-keyword">let</span> person6 = <span class="hljs-keyword">new</span> Child6();
  <span class="hljs-built_in">console</span>.log(person6);
  <span class="hljs-built_in">console</span>.log(person6.getName());
  <span class="hljs-built_in">console</span>.log(person6.getFriends());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这段代码可以看出来，这种寄生组合式继承方式，基本可以解决前几种继承方式的缺点，较好地实现了继承想要的结果，同时也减少了构造次数，减少了性能的开销，我们来看一下上面这一段代码的执行结果。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7045ca4213594e2aa96b3a41486ab627~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到 person6 打印出来的结果，属性都得到了继承，方法也没问题，可以输出预期的结果。</p>
<p>整体看下来，这六种继承方式中，寄生组合式继承是这六种里面最优的继承方式。另外，ES6 还提供了继承的关键字 extends，我们再看下 extends 的底层实现继承的逻辑。</p>
<p>ES6 的 extends 关键字实现逻辑
我们可以利用 ES6 里的 extends 的语法糖，使用关键词很容易直接实现 JavaScript 的继承，但是如果想深入了解 extends 语法糖是怎么实现的，就得深入研究 extends 的底层逻辑。</p>
<p>我们先看下用利用 extends 如何直接实现继承，代码如下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name
  &#125;
  <span class="hljs-comment">// 原型方法</span>
  <span class="hljs-comment">// 即 Person.prototype.getName = function() &#123; &#125;</span>
  <span class="hljs-comment">// 下面可以简写为 getName() &#123;...&#125;</span>
  getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Person:'</span>, <span class="hljs-built_in">this</span>.name)
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Gamer</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age</span>)</span> &#123;
    <span class="hljs-comment">// 子类中存在构造函数，则需要在使用“this”之前首先调用 super()。</span>
    <span class="hljs-built_in">super</span>(name)
    <span class="hljs-built_in">this</span>.age = age
  &#125;
&#125;
<span class="hljs-keyword">const</span> asuna = <span class="hljs-keyword">new</span> Gamer(<span class="hljs-string">'Asuna'</span>, <span class="hljs-number">20</span>)
asuna.getName() <span class="hljs-comment">// 成功访问到父类的方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为浏览器的兼容性问题，如果遇到不支持 ES6 的浏览器，那么就得利用 babel 这个编译工具，将 ES6 的代码编译成 ES5，让一些不支持新语法的浏览器也能运行。</p>
<p>那么最后 extends 编译成了什么样子呢？我们看一下转译之后的代码片段。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_possibleConstructorReturn</span> (<span class="hljs-params">self, call</span>) </span>&#123; 
<span class="hljs-comment">// ...</span>
<span class="hljs-keyword">return</span> call && (<span class="hljs-keyword">typeof</span> call === <span class="hljs-string">'object'</span> || <span class="hljs-keyword">typeof</span> call === <span class="hljs-string">'function'</span>) ? call : self; 
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_inherits</span> (<span class="hljs-params">subClass, superClass</span>) </span>&#123; 
    <span class="hljs-comment">// 这里可以看到</span>
subClass.prototype = <span class="hljs-built_in">Object</span>.create(superClass && superClass.prototype, &#123; 
<span class="hljs-attr">constructor</span>: &#123; 
<span class="hljs-attr">value</span>: subClass, 
<span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>, 
<span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>, 
<span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span> 
&#125; 
&#125;); 
<span class="hljs-keyword">if</span> (superClass) <span class="hljs-built_in">Object</span>.setPrototypeOf ? <span class="hljs-built_in">Object</span>.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; 
&#125;

<span class="hljs-keyword">var</span> Parent = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-comment">// 验证是否是 Parent 构造出来的 this</span>
_classCallCheck(<span class="hljs-built_in">this</span>, Parent);
&#125;;
<span class="hljs-keyword">var</span> Child = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_Parent</span>) </span>&#123;
_inherits(Child, _Parent);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params"></span>) </span>&#123;
_classCallCheck(<span class="hljs-built_in">this</span>, Child);
<span class="hljs-keyword">return</span> _possibleConstructorReturn(<span class="hljs-built_in">this</span>, (Child.__proto__ || <span class="hljs-built_in">Object</span>.getPrototypeOf(Child)).apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>));
&#125;
<span class="hljs-keyword">return</span> Child;
&#125;(Parent));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面编译完成的源码中可以看到，它采用的也是寄生组合继承方式，因此也证明了这种方式是较优的解决继承的方式。</p>
<p>通过 Object.create 来划分不同的继承方式，最后的寄生式组合继承方式是通过组合继承改造之后的最优继承方式，而 extends 的语法糖和寄生组合继承的方式基本类似。</p>
<p>综上，我们可以看到不同的继承方式有不同的优缺点，我们需要深入了解各种方式的优缺点，这样才能在日常开发中，选择最适合当前场景的继承方式。</p>
<p>在日常的前端开发工作中，开发者往往会忽视对继承相关的系统性学习，但因为继承的方法比较多，每个实现的方法细节也比较零散，很多开发者很难有一个系统的、整体的认识，造成效率低下，以及代码能力难以进一步提升等问题。</p></div>  
</div>
            