
---
title: '使用JavaScript学习设计模式｜小册免费学'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08385cf5952c42959949a3bef0ac2565~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 18:14:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08385cf5952c42959949a3bef0ac2565~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>去年的时候先是看了<a href="https://juejin.cn/user/2400989094885495" target="_blank">修言</a>大佬的性能优化掘金小册子，收获良多。</p>
<p>之后紧接着买了这本<a href="https://juejin.cn/book/6844733790204461070/section/6844733790246404109" target="_blank">JavaScript 设计模式核⼼原理与应⽤实践</a>，刚好最近有<a href="https://juejin.cn/post/6943533938090442765" target="_blank">小册免费学</a>的活动，就赶紧把这篇笔记整理出来了，并且补充了小册子中的没有写到的其余设计模式，学习过程中结合 JavaScript 编写的例子，以便于理解和加深印象。</p>
<p>与其说是一篇文章，其实更像是一篇总结性质的学习笔记。</p>
<h2 data-id="heading-1">为什么要学习设计模式？</h2>
<p>学习之前，先了解什么是设计模式？</p>
<blockquote>
<p>设计模式（Design Pattern）是前辈们对代码开发经验的总结，是解决特定问题的一系列套路。它不是语法规定，而是一套用来提高代码可复用性、可维护性、可读性、稳健性以及安全性的解决方案。</p>
</blockquote>
<p>简答理解 <strong>它是一套被反复使用、多人知晓的、经过分类的、代码设计经验总结。</strong></p>
<p>烹饪有菜谱，游戏有攻略，每个领域都存在一些能够让我们又好又快地达成目标的“套路”。在程序世界，编程的“套路”就是设计模式。</p>
<p>学习它也就是学习这个编程世界的套路，对以后升级打怪打装备有很大的帮助。在瞬息万变的前端领域，设计模式也是一种“一次学习，终生受用”知识。</p>
<h3 data-id="heading-2">设计模式的原则</h3>
<blockquote>
<p>描述一个不断发生的重复的问题，以及该问题的解决方案的核心。
这样，你就能一次又一次的使用该方案而不必做重复劳动。</p>
</blockquote>
<p><strong>一大法则：</strong></p>
<ul>
<li>迪米特法则：又叫最少知识法则，一个软件实体应该尽可能少的语其他实体发生相互作用，每一个软件单位对其他的单位都只有最少的知识，而且局限于那些与本单位密切相关的软件单位。</li>
</ul>
<p><strong>五大原则：</strong></p>
<ul>
<li>单一职责原则：一个类，应该仅有一个引起它变化的原因，简而言之，就是功能要单一。</li>
<li>开放封闭原则：对扩展开放，对修改关闭。</li>
<li>里氏替换原则：基类出现的地方，子类一定出现。</li>
<li>接口隔离原则：一个借口应该是一种角色，不该干的事情不敢，该干的都要干。简而言之就是降低耦合、减低依赖。</li>
<li>依赖翻转原则：针对接口编程，依赖抽象而不依赖具体。</li>
</ul>
<p>JavaScript 中常用的是单一功能和开放封闭原则。</p>
<h3 data-id="heading-3">高内聚和低耦合</h3>
<p>通过设计模式可以帮助我们增强代码的可重用性、可扩充性、 可维护性、灵活性好。我们使用设计模式最终的目的是实现代码的 高内聚 和 低耦合。</p>
<p>举例一个现实生活中的例子，例如一个公司，一般都是各个部门各司其职，互不干涉。各个部门需要沟通时通过专门的负责人进行对接。</p>
<p>在软件里面也是一样的 一个功能模块只是关注一个功能，一个模块最好只实现一个功能，这个是所谓的<strong>内聚</strong>。</p>
<p>模块与模块之间、系统与系统之间的交互，是不可避免的， 但是我们要尽量减少由于交互引起的单个模块无法独立使用或者无法移植的情况发生， 尽可能多的单独提供接口用于对外操作， 这个就是所谓的<strong>低耦合</strong></p>
<h3 data-id="heading-4">封装变化</h3>
<p>在实际开发过程中，不发生变化的代码基本是不存在的，所以我要将代码的变化最小化。</p>
<p><strong>设计模式的核心就是去观察你整个逻辑里的变与不变，然后将不变分离，达到使变化的部分灵活、不变的地方稳定的目的。</strong></p>
<h2 data-id="heading-5">设计模式的种类</h2>
<p>常用的可以分为创建型、结构型、行为型三类，一共 23 种模式。</p>
<p><strong>创建型：</strong></p>
<ul>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F">工厂模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F">单例模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E5%8E%9F%E5%9E%8B%E6%A8%A1%E5%BC%8F">原型模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E6%9E%84%E9%80%A0%E5%99%A8%E6%A8%A1%E5%BC%8F">构造器模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E6%8A%BD%E8%B1%A1%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F">抽象工厂模式</a></li>
</ul>
<p><strong>结构型：</strong></p>
<ul>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E8%A3%85%E9%A5%B0%E5%99%A8%E6%A8%A1%E5%BC%8F">装饰器模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E9%80%82%E9%85%8D%E5%99%A8%E6%A8%A1%E5%BC%8F">适配器模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E4%BB%A3%E7%90%86%E6%A8%A1%E5%BC%8F">代理模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E6%A1%A5%E6%8E%A5%E6%A8%A1%E5%BC%8F">桥接模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E5%A4%96%E8%A7%82%E6%A8%A1%E5%BC%8F">外观模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E7%BB%84%E5%90%88%E6%A8%A1%E5%BC%8F">组合模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E4%BA%AB%E5%85%83%E6%A8%A1%E5%BC%8F">享元模式</a></li>
</ul>
<p><strong>行为型：</strong></p>
<ul>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E8%BF%AD%E4%BB%A3%E5%99%A8%E6%A8%A1%E5%BC%8F">迭代器模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E5%8F%91%E5%B8%83/%E8%AE%A2%E9%98%85%E6%A8%A1%E5%BC%8F%EF%BC%88%E8%A7%82%E5%AF%9F%E8%80%85%EF%BC%89">发布/订阅模式（观察者）</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E7%AD%96%E7%95%A5%E6%A8%A1%E5%BC%8F">策略模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E7%8A%B6%E6%80%81%E6%A8%A1%E5%BC%8F">状态模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E8%A7%A3%E9%87%8A%E5%99%A8%E6%A8%A1%E5%BC%8F">解释器模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E4%B8%AD%E4%BB%8B%E8%80%85%E6%A8%A1%E5%BC%8F">中介者模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E8%AE%BF%E9%97%AE%E8%80%85%E6%A8%A1%E5%BC%8F">访问者模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E5%A4%87%E5%BF%98%E5%BD%95%E6%A8%A1%E5%BC%8F">备忘录模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E6%A8%A1%E6%9D%BF%E6%96%B9%E6%B3%95%E6%A8%A1%E5%BC%8F">模板方法模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E8%81%8C%E8%B4%A3%E9%93%BE%E6%A8%A1%E5%BC%8F">职责链模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6950088586590961700#%E5%91%BD%E4%BB%A4%E6%A8%A1%E5%BC%8F">命令模式</a></li>
</ul>
<h2 data-id="heading-6">创建型</h2>
<h3 data-id="heading-7">工厂模式</h3>
<blockquote>
<p>这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。</p>
</blockquote>
<p>在工厂模式中，我们在创建对象时不会对客户端暴露创建逻辑，并且是通过使用一个共同的接口来指向新创建的对象。
在 JS 中其实就是借助构造函数实现。</p>
<p><strong>例子</strong></p>
<p>某个班级要做一个录入系统，录入一个人，就要写一次。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> liMing = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"李明"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>,
  <span class="hljs-attr">sex</span>: <span class="hljs-string">"男"</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果多个录入，则可以创建一个类。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age, sex</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.age = age;
    <span class="hljs-built_in">this</span>.sex = sex;
  &#125;
&#125;
<span class="hljs-keyword">let</span> zhangSan = <span class="hljs-keyword">new</span> Student(<span class="hljs-string">"张三"</span>, <span class="hljs-number">19</span>, <span class="hljs-string">"男"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>工厂模式是将创建对象的过程单独封装，使用使只需要无脑传参就行了，就像一个工厂一样，只要给够原料，就可以轻易的制造出成品。</p>
<p><strong>小结</strong></p>
<ul>
<li>构造函数和创建者分离，对 new 操作进行封装</li>
<li>符合开放封闭原则</li>
</ul>
<h3 data-id="heading-8">单例模式</h3>
<blockquote>
<p>单例模式的定义：保证一个类仅有一个实例，并且提供一个访问它的全局变量。</p>
<p>实现的方法为前判断实例是否存在，如果存在直接返回，不存在则创建在返回，这就确保了一个类只有一个实例对象。</p>
</blockquote>
<p>比如：Vuex、jQuery</p>
<p><strong>例子</strong></p>
<p>使用场景：一个单一对象，比如：弹窗，无论点击多少次，弹窗只应被创建一次，实现起来也很简单，用一个变量缓存就行了。</p>
<p>【点击查看Demo】：<a href="http://jsrun.net/2SNKp/embedded/all/light" target="_blank" rel="nofollow noopener noreferrer">单例模式-在线例子</a></p>
<p>如上面这个弹框，只有在第一次点击按钮时才会创建弹框，之后都不会在创建，而是使用之前创建的弹框。</p>
<p>如此，便是实现了一个应用于单例模式的弹框。</p>
<p><strong>小结</strong></p>
<ul>
<li>维持一个实例，如果已经创建，就直接返回</li>
<li>符合开放封闭原则</li>
</ul>
<h3 data-id="heading-9">原型模式</h3>
<blockquote>
<p>用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。</p>
</blockquote>
<p><strong>例子</strong></p>
<p>在 JavaScript 中，实现原型模式是在 ECMAscript5 中，提出的 Object.create 方法，使用现有的对象来提供创建的对象<code>__proto__</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> prototype = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Jack"</span>,
  <span class="hljs-attr">getName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;,
&#125;;

<span class="hljs-keyword">var</span> obj = <span class="hljs-built_in">Object</span>.create(prototype, &#123;
  <span class="hljs-attr">job</span>: &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-string">"IT"</span>,
  &#125;,
&#125;);

<span class="hljs-built_in">console</span>.log(obj.getName()); <span class="hljs-comment">// Jack</span>
<span class="hljs-built_in">console</span>.log(obj.job); <span class="hljs-comment">// IT</span>
<span class="hljs-built_in">console</span>.log(obj.__proto__ === prototype); <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有原型就有原理性了</p>
<h3 data-id="heading-10">构造器模式</h3>
<blockquote>
<p>在面向对象的编程语言中，构造器是一个类中用来初始化新对象的特殊方法。并且可以接受参数用来设定实例对象的属性的方法</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Car</span>(<span class="hljs-params">model, year, miles</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.model = model;
  <span class="hljs-built_in">this</span>.year = year;
  <span class="hljs-built_in">this</span>.miles = miles;
  <span class="hljs-comment">// this.info = new CarDetail(model)</span>
  <span class="hljs-comment">// 属性也可以通过 new 的方式产生</span>
&#125;

<span class="hljs-comment">// 覆盖原型对象上的toString</span>
Car.prototype.toString = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.model + <span class="hljs-string">" has done "</span> + <span class="hljs-built_in">this</span>.miles + <span class="hljs-string">" miles"</span>;
&#125;;

<span class="hljs-comment">// 使用:</span>
<span class="hljs-keyword">var</span> civic = <span class="hljs-keyword">new</span> Car(<span class="hljs-string">"Honda Civic"</span>, <span class="hljs-number">2009</span>, <span class="hljs-number">20000</span>);
<span class="hljs-keyword">var</span> mondeo = <span class="hljs-keyword">new</span> Car(<span class="hljs-string">"Ford Mondeo"</span>, <span class="hljs-number">2010</span>, <span class="hljs-number">5000</span>);
<span class="hljs-built_in">console</span>.log(civic.toString()); <span class="hljs-comment">// Honda Civic has done 20000 miles</span>
<span class="hljs-built_in">console</span>.log(mondeo.toString()); <span class="hljs-comment">// Ford Mondeo has done 5000 miles</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实就是利用原型链上被继承的特性，实现了构造器。</p>
<h3 data-id="heading-11">抽象工厂模式</h3>
<blockquote>
<p>抽象工厂模式(Abstract Factory)就是通过类的抽象使得业务适用于一个产品类簇的创建，而不负责某一类产品的实例。</p>
</blockquote>
<p>JS 中是没有直接的抽象类的，abstract 是个保留字，但是还没有实现，因此我们需要在类的方法中抛出错误来模拟抽象类，如果继承的子类中没有覆写该方法而调用，就会抛出错误。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Car = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;
Car.prototype.getPrice = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"抽象方法不能调用"</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>面向对象的语言里有抽象工厂模式，首先声明一个抽象类作为父类，以概括某一类产品所需要的特征，继承该父类的子类需要实现父类中声明的方法而实现父类中所声明的功能：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 实现subType类对工厂类中的superType类型的抽象类的继承
 * <span class="hljs-doctag">@param </span>subType 要继承的类
 * <span class="hljs-doctag">@param </span>superType 工厂类中的抽象类type
 */</span>
<span class="hljs-keyword">const</span> VehicleFactory = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">subType, superType</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> VehicleFactory[superType] === <span class="hljs-string">"function"</span>) &#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">this</span>.type = <span class="hljs-string">"车辆"</span>;
    &#125;
    F.prototype = <span class="hljs-keyword">new</span> VehicleFactory[superType]();
    subType.constructor = subType;
    subType.prototype = <span class="hljs-keyword">new</span> F(); <span class="hljs-comment">// 因为子类subType不仅需要继承superType对应的类的原型方法，还要继承其对象属性</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"不存在该抽象类"</span>);
&#125;;
VehicleFactory.Car = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.type = <span class="hljs-string">"car"</span>;
&#125;;
VehicleFactory.Car.prototype = &#123;
  <span class="hljs-attr">getPrice</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"抽象方法不可使用"</span>);
  &#125;,
  <span class="hljs-attr">getSpeed</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"抽象方法不可使用"</span>);
  &#125;,
&#125;;
<span class="hljs-keyword">const</span> BMW = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">price, speed</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.price = price;
  <span class="hljs-built_in">this</span>.speed = speed;
&#125;;
VehicleFactory(BMW, <span class="hljs-string">"Car"</span>); <span class="hljs-comment">// 继承Car抽象类</span>
BMW.prototype.getPrice = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 覆写getPrice方法</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`BWM price is <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.price&#125;</span>`</span>);
&#125;;
BMW.prototype.getSpeed = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`BWM speed is <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.speed&#125;</span>`</span>);
&#125;;
<span class="hljs-keyword">const</span> baomai5 = <span class="hljs-keyword">new</span> BMW(<span class="hljs-number">30</span>, <span class="hljs-number">99</span>);
baomai5.getPrice(); <span class="hljs-comment">// BWM price is 30</span>
baomai5 <span class="hljs-keyword">instanceof</span> VehicleFactory.Car; <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过抽象工厂，就可以创建某个类簇的产品，并且也可以通过 instanceof 来检查产品的类别，也具备该类簇所必备的方法。</p>
<h2 data-id="heading-12">结构型</h2>
<h3 data-id="heading-13">装饰器模式</h3>
<blockquote>
<p>装饰器模式，又名装饰者模式。它的定义是“ 在不改变原对象的基础上，通过对其进行包装拓展，使原有对象可以满足用户的更复杂需求 ”。</p>
</blockquote>
<p><strong>装饰器案例</strong></p>
<p>有一个弹窗函数，点击按钮后会弹出一个弹框。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">openModal</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> div = <span class="hljs-built_in">document</span>.craeteElement(<span class="hljs-string">"div"</span>);
  div.id = <span class="hljs-string">"modal"</span>;
  div.innerHTML = <span class="hljs-string">"提示"</span>;
  div.style.backgroundColor = <span class="hljs-string">"gray"</span>;
  <span class="hljs-built_in">document</span>.body.appendChlid(div);
&#125;
btn.onclick = <span class="hljs-function">() =></span> &#123;
  openModal();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是忽然产品经理要改需求，要把提示文字由“提示”改为“警告”，背景颜色由 gray 改为 red。</p>
<p>听到这个你是不是立马就想直接改动源函数：</p>
<pre><code class="hljs language-js&#123;4,5&#125; copyable" lang="js&#123;4,5&#125;">function openModal() &#123;
  let div = document.craeteElement("div");
  div.id = "modal";
  div.innerHTML = "警告";
  div.style.backgroundColor = "red";
  document.body.appendChlid(div);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是如果是复杂的业务逻辑，或者这个代码时上任代码留下来的产物，在考虑到以后的需求变化，每次都这样修改确实很麻烦。</p>
<p>而且，直接修改已有的函数体，有违背了我们的“开放封闭原则”，往一个函数塞这么多的逻辑，也违背了“单一职责原则”，所以上面的方法并不是最佳的。</p>
<p>最省时省力的方式是不去关心它现有得了逻辑，只在此逻辑之上扩展新的功能即可，因此装饰器模式就此而生。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 新逻辑</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">changeModal</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> div = <span class="hljs-built_in">document</span>.getElemnetById(<span class="hljs-string">"modal"</span>);
  div.innerHTML = <span class="hljs-string">"告警"</span>;
  div.style.backgroundColor = <span class="hljs-string">"red"</span>;
&#125;
btn.onclick = <span class="hljs-function">() =></span> &#123;
  openModal();
  changeModal();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种通过函数添加新的功能、而又不修改旧逻辑，这就是装饰器的魅力。</p>
<p><strong>ES7 中的装饰器</strong></p>
<p>在最新的 ES7 中有装饰器的提案，但是还未定案，所以语法可能不是最终版，但是思想是一样的。</p>
<ol>
<li>装饰类的属性</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">@tableColor
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Table</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tableColor</span>(<span class="hljs-params">target</span>) </span>&#123;
  target.color = <span class="hljs-string">"red"</span>;
&#125;
Table.color; <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为<code>Table</code>这个类，添加一个<code>tableColor</code>的装饰器，即可改变<code>Table</code>的<code>color</code>属性</p>
<ol start="2">
<li>装饰类的方法</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  @readonly
  <span class="hljs-function"><span class="hljs-title">name</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.first&#125;</span> <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.last&#125;</span>`</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为<code>Person</code>类的<code>name</code>方法添加只读的装饰器，使得该方法不可被修改。</p>
<p>其实是借助<code>Object.defineProperty</code>的<code>wirteable</code>特性实现的。</p>
<ol start="3">
<li>
<p>装饰函数</p>
<p>因为 JS 中函数存在函数提升，直接使用装饰器并不可取，但是可以使用高级函数的方式实现。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">doSomething</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Hello, "</span> + name);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loggingDecorator</span>(<span class="hljs-params">wrapped</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"fun-Starting"</span>);
    <span class="hljs-keyword">const</span> result = wrapped.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"fun-Finished"</span>);
    <span class="hljs-keyword">return</span> result;
  &#125;;
&#125;
<span class="hljs-keyword">const</span> wrapped = loggingDecorator(doSomething);
<span class="hljs-keyword">let</span> name = <span class="hljs-string">"World"</span>;

doSomething(name); <span class="hljs-comment">// 装饰前</span>
<span class="hljs-comment">// output:</span>
<span class="hljs-comment">// Hello, World</span>

wrapped(name); <span class="hljs-comment">// 装饰后</span>
<span class="hljs-comment">// output:</span>
<span class="hljs-comment">// fun-Starting</span>
<span class="hljs-comment">// Hello, World</span>
<span class="hljs-comment">// fun-Finished</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的装饰器，是给一个函数在执行开始和执行结束分别打印一个 log。</p>
</li>
</ol>
<p><strong>参考</strong></p>
<ul>
<li><a href="https://es6.ruanyifeng.com/?search=%E8%A3%85%E9%A5%B0%E5%99%A8&x=0&y=0#docs/decorator" target="_blank" rel="nofollow noopener noreferrer">ES6 标准入门-decorators</a></li>
<li><a href="https://github.com/jayphelps/core-decorators" target="_blank" rel="nofollow noopener noreferrer">推荐阅读-core-decorators</a></li>
</ul>
<h3 data-id="heading-14">适配器模式</h3>
<blockquote>
<p>适配器模式的作用是解决两个软件实体间的接口不兼容问题。使用适配器模式之后，原本由于接口不兼容而不能工作的两个软件实体可以一起工作。</p>
<p>简单来说，就是把一个类的接口变成客户端期待的另一种接口，<strong>解决兼容问题</strong>。</p>
</blockquote>
<p>比如：axios</p>
<p>例子：一个渲染地图的方法，默认是调用当前地图对象的 show 方法进行渲染操作，当有多个地图，而每个地图的渲染方法都不一样时，为了方便使用者调用，就需要做适配了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> googleMap = &#123;
  <span class="hljs-attr">show</span>: <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开始渲染谷歌地图"</span>);
  &#125;,
&#125;;
<span class="hljs-keyword">let</span> baiduMap = &#123;
  <span class="hljs-attr">display</span>: <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开始渲染百度地图"</span>);
  &#125;,
&#125;;
<span class="hljs-keyword">let</span> baiduMapAdapter = &#123;
  <span class="hljs-attr">show</span>: <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> baiduMap.display();
  &#125;,
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderMap</span>(<span class="hljs-params">obj</span>) </span>&#123;
  obj.show();
&#125;
renderMap(googleMap); <span class="hljs-comment">// 开始渲染谷歌地图</span>
renderMap(baiduMapAdapter); <span class="hljs-comment">// 开始渲染百度地图</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这其中对“百度地图”做了适配的处理。</p>
<p><strong>小结</strong></p>
<ul>
<li>适配器模式主要解决两个接口之间不匹配的问题，不会改变原有的接口，而是由一个对象对另一个对象的包装</li>
<li>适配器模式符合开放封闭原则</li>
<li>把变化留给自己，把统一留给用户。</li>
</ul>
<h3 data-id="heading-15">代理模式</h3>
<blockquote>
<p>代理模式——在某些情况下，出于种种考虑/限制，一个对象不能直接访问另一个对象，需要一个第三者（代理）牵桥搭线从而间接达到访问目的，这样的模式就是代理模式。</p>
</blockquote>
<p>提起代理（Proxy），对于前端很熟悉的，我能联想到一系列的东西，比如：</p>
<ul>
<li>ES6 新增的 proxy 属性</li>
<li>为了解决跨域问题而经常使用的 webpack 的 proxy 配置和 Nginx 代理</li>
<li>还有科学上网所使用的的代理。</li>
<li>等等</li>
</ul>
<p><strong>事件代理</strong></p>
<p>常见的列表、表格都需要单独处理事件时，使用父级元素事件代理，可以极大的减少代码量。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"father"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"1"</span>></span>新闻1<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"2"</span>></span>新闻2<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"3"</span>></span>新闻3<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"4"</span>></span>新闻4<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"5"</span>></span>新闻5<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"6"</span>></span>新闻6<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-comment"><!-- 7、8... --></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码，我想点击每个新闻，都可以拿到当前新闻的<code>id</code>，从而进行下一步操作。</p>
<p>如果给每一个<code>span</code>都绑定一个<code>onclick</code>事件，就太耗费性能了，而且写起来也很麻烦。</p>
<p>我们常见的做法是利用事件冒泡的原理，将事件带代理到父元素上，然后统一处理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> father = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"father"</span>);
father.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">(<span class="hljs-params">evnet</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (event.target.nodeName === <span class="hljs-string">"SPAN"</span>) &#123;
    event.preventDefault();
    <span class="hljs-keyword">let</span> id = event.target.id;
    <span class="hljs-built_in">console</span>.log(id); <span class="hljs-comment">// 拿到id，进行下一步操作</span>
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>虚拟代理</strong></p>
<p>例如：某个花销很大的操作，可以通过虚拟代理的方式延迟到这种需要它的时候才去创建（例如：使用虚拟代理实现图片懒加载）</p>
<p>图片预加载：先通过一张 loading 图占位，然后通过异步的方式加载图片，等图片加载完成之后在使用原图替换 loading 图。</p>
<blockquote>
<p>问什么要使用预加载+懒加载？以淘宝举例，商城物品图片多之又多，一次全部请求过来这么多图片无论是对 js 引擎还是浏览器本身都是一个巨大的工作量，会拖慢浏览器响应速度，用户体验极差，而预加载+懒加载的方式会大大节省浏览器请求速度，通过预加载率先加载占位图片（第二次及以后都是缓存中读取），再通过懒加载直到要加载的真实图片加载完成，瞬间替换。这种模式很好的解决了图片一点点展现在页面上用户体验差的弊端。</p>
</blockquote>
<p>须知：图片第一次设置 src，浏览器发送网络请求；如果设置一个请求过的 src 那么浏览器则会从缓存中读取 from disk cache</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PreLoadImage</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">imgNode</span>)</span> &#123;
    <span class="hljs-comment">// 获取真实的DOM节点</span>
    <span class="hljs-built_in">this</span>.imgNode = imgNode;
  &#125;

  <span class="hljs-comment">// 操作img节点的src属性</span>
  <span class="hljs-function"><span class="hljs-title">setSrc</span>(<span class="hljs-params">imgUrl</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.imgNode.src = imgUrl;
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ProxyImage</span> </span>&#123;
  <span class="hljs-comment">// 占位图的url地址</span>
  <span class="hljs-keyword">static</span> LOADING_URL = <span class="hljs-string">"xxxxxx"</span>;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">targetImage</span>)</span> &#123;
    <span class="hljs-comment">// 目标Image，即PreLoadImage实例</span>
    <span class="hljs-built_in">this</span>.targetImage = targetImage;
  &#125;

  <span class="hljs-comment">// 该方法主要操作虚拟Image，完成加载</span>
  <span class="hljs-function"><span class="hljs-title">setSrc</span>(<span class="hljs-params">targetUrl</span>)</span> &#123;
    <span class="hljs-comment">// 真实img节点初始化时展示的是一个占位图</span>
    <span class="hljs-built_in">this</span>.targetImage.setSrc(ProxyImage.LOADING_URL);
    <span class="hljs-comment">// 创建一个帮我们加载图片的虚拟Image实例</span>
    <span class="hljs-keyword">const</span> virtualImage = <span class="hljs-keyword">new</span> Image();
    <span class="hljs-comment">// 监听目标图片加载的情况，完成时再将DOM上的真实img节点的src属性设置为目标图片的url</span>
    virtualImage.onload = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.targetImage.setSrc(targetUrl);
    &#125;;
    <span class="hljs-comment">// 设置src属性，虚拟Image实例开始加载图片</span>
    virtualImage.src = targetUrl;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ProxyImage</code> 帮我们调度了预加载相关的工作，我们可以通过 <code>ProxyImage</code> 这个代理，实现对真实 img 节点的间接访问，并得到我们想要的效果。</p>
<p>在这个实例中，<code>virtualImage</code> 这个对象是一个“幕后英雄”，它始终存在于 JavaScript 世界中、代替真实 DOM 发起了图片加载请求、完成了图片加载工作，却从未在渲染层面抛头露面。因此这种模式被称为“虚拟代理”模式。</p>
<p>【点击查看Demo】：<a href="https://jsrun.net/YSNKp/embedded/all/light">虚拟代理-在线例子</a></p>
<p><strong>缓存代理</strong></p>
<blockquote>
<p>缓存代理比较好理解，它应用于一些计算量较大的场景里。在这种场景下，我们需要“用空间换时间”——当我们需要用到某个已经计算过的值的时候，不想再耗时进行二次计算，而是希望能从内存里去取出现成的计算结果。</p>
</blockquote>
<p>这种场景下，就需要一个代理来帮我们在进行计算的同时，进行计算结果的缓存了。</p>
<p>例子：对参数求和函数进行缓存代理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// addAll方法会对你传入的所有参数做求和操作</span>
<span class="hljs-keyword">const</span> addAll = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"进行了一次新计算"</span>);
  <span class="hljs-keyword">let</span> result = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">const</span> len = <span class="hljs-built_in">arguments</span>.length;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
    result += <span class="hljs-built_in">arguments</span>[i];
  &#125;
  <span class="hljs-keyword">return</span> result;
&#125;;

<span class="hljs-comment">// 为求和方法创建代理</span>
<span class="hljs-keyword">const</span> proxyAddAll = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 求和结果的缓存池</span>
  <span class="hljs-keyword">const</span> resultCache = &#123;&#125;;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 将入参转化为一个唯一的入参字符串</span>
    <span class="hljs-keyword">const</span> args = <span class="hljs-built_in">Array</span>.prototype.join.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-string">","</span>);

    <span class="hljs-comment">// 检查本次入参是否有对应的计算结果</span>
    <span class="hljs-keyword">if</span> (args <span class="hljs-keyword">in</span> resultCache) &#123;
      <span class="hljs-comment">// 如果有，则返回缓存池里现成的结果</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"无计算-使用缓存的数据"</span>);
      <span class="hljs-keyword">return</span> resultCache[args];
    &#125;
    <span class="hljs-keyword">return</span> (resultCache[args] = addAll(...arguments));
  &#125;;
&#125;)();

<span class="hljs-keyword">let</span> sum1 = proxyAddAll(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>); <span class="hljs-comment">// 进行了一次新计算</span>

<span class="hljs-keyword">let</span> sum2 = proxyAddAll(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>); <span class="hljs-comment">// 无计算-使用缓存的数据</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一次进行计算返回结果，并存入缓存。如果再次传入相同的参数，则不计算，直接返回缓存中存在的结果。</p>
<p>在常见在 HTTP 缓存中，浏览器就相当于进行了一层代理缓存，通过 HTTP 的缓存机制控制（强缓存和协商缓存）判断是否启用缓存。</p>
<p>频繁却变化小的的网络请求，比如<code>getUserInfo</code>，可以使用代理请求，设置统一发送和存取。</p>
<p><strong>小结</strong></p>
<ul>
<li>代理模式符合开放封闭原则。</li>
<li>本体对象和代理对象拥有相同的方法，在用户看来并不知道请求的是本体对象还是代理对象。</li>
</ul>
<h3 data-id="heading-16">桥接模式</h3>
<blockquote>
<p>桥接模式：将抽象部分和具体实现部分分离，两者可独立变化，也可以一起工作。</p>
<p>在这种模式的实现上，需要一个对象担任“桥”的角色，起到连接的作用。</p>
</blockquote>
<p>例子：</p>
<p>JavaScript 中桥接模式的典型应用是：<code>Array</code>对象上的<code>forEach</code>函数。</p>
<p>此函数负责循环遍历数组每个元素，是<strong>抽象部分</strong>； 而回调函数<code>callback</code>就是具体<strong>实现部分</strong>。</p>
<p>下方是模拟<code>forEach</code>方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> forEach = <span class="hljs-function">(<span class="hljs-params">arr, callback</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(arr)) <span class="hljs-keyword">return</span>;

  <span class="hljs-keyword">const</span> length = arr.length;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; ++i) &#123;
    callback(arr[i], i);
  &#125;
&#125;;

<span class="hljs-comment">// 以下是测试代码</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-string">"a"</span>, <span class="hljs-string">"b"</span>];
forEach(arr, <span class="hljs-function">(<span class="hljs-params">el, index</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"元素是"</span>, el, <span class="hljs-string">"位于"</span>, index));
<span class="hljs-comment">// 元素是 a 位于 0</span>
<span class="hljs-comment">// 元素是 b 位于 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">外观模式</h3>
<blockquote>
<p>外观模式（Facade Pattern）隐藏系统的复杂性，并向客户端提供了一个客户端可以访问系统的接口。这种类型的设计模式属于结构型模式，它向现有的系统添加一个接口，来隐藏系统的复杂性。</p>
<p>这种模式涉及到一个单一的类，该类提供了客户端请求的简化方法和对现有系统类方法的委托调用。</p>
</blockquote>
<p><strong>例子</strong></p>
<p>外观模式即执行一个方法可以让多个方法一起被调用。</p>
<p>涉及到兼容性，参数支持多个格式、环境等等.. 对外暴露统一的 api</p>
<p>比如自己封装的事件对象包含了阻止冒泡和添加事件监听的兼容方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> myEvent = &#123;
    stop (e)&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> e.preventDefault() == <span class="hljs-string">'function'</span>)&#123;
            e.preventDefault();
        &#125;
        <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> e.stopPropagation() == <span class="hljs-string">'function'</span>)&#123;
            e.stopPropagation()
        &#125;
        <span class="hljs-comment">// IE</span>
        <span class="hljs-keyword">if</span>(typeOd e.retrunValue === <span class="hljs-string">'boolean'</span>)&#123;
            e.returnValue = <span class="hljs-literal">false</span>
        &#125;
        <span class="hljs-keyword">if</span>(typeOd e.cancelBubble === <span class="hljs-string">'boolean'</span>)&#123;
            e.returnValue = <span class="hljs-literal">true</span>
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">addEvnet</span>(<span class="hljs-params">dom, type, fn</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(dom.addEventListener)&#123;
            dom.addEventlistener(type, fn, <span class="hljs-literal">false</span>);
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(dom.attachEvent)&#123;
            dom.attachEvent(<span class="hljs-string">'on'</span>+type, fn)
        &#125;<span class="hljs-keyword">else</span>&#123;
            dom[<span class="hljs-string">'on'</span>+type] = fn
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">组合模式</h3>
<blockquote>
<p>组合模式（Composite Pattern），又叫部分整体模式，是用于把一组相似的对象当作一个单一的对象。</p>
<p>组合模式依据树形结构来组合对象，用来表示部分以及整体层次。这种类型的设计模式属于结构型模式，它创建了对象组的树形结构。</p>
</blockquote>
<p>这种模式创建了一个包含自己对象组的类。该类提供了修改相同对象组的方式。</p>
<p><strong>例子</strong></p>
<p>想象我们现在手上有多个万能遥控器，当我们回到家中，按一下开关，下列事情将被执行</p>
<ul>
<li>开门</li>
<li>开电脑</li>
<li>开音乐</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 先准备一些需要批量执行的功能</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GoHome</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开门"</span>);
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OpenComputer</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开电脑"</span>);
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OpenMusic</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"开音乐"</span>);
  &#125;
&#125;

<span class="hljs-comment">// 组合器，用来组合功能</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Comb</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 准备容器，用来防止将来组合起来的功能</span>
    <span class="hljs-built_in">this</span>.skills = [];
  &#125;
  <span class="hljs-comment">// 用来组合的功能，接收要组合的对象</span>
  <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">task</span>)</span> &#123;
    <span class="hljs-comment">// 向容器中填入，将来准备批量使用的对象</span>
    <span class="hljs-built_in">this</span>.skills.push(task);
  &#125;
  <span class="hljs-comment">// 用来批量执行的功能</span>
  <span class="hljs-function"><span class="hljs-title">action</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 拿到容器中所有的对象，才能批量执行</span>
    <span class="hljs-built_in">this</span>.skills.forEach(<span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
      val.init();
    &#125;);
  &#125;
&#125;

<span class="hljs-comment">// 创建一个组合器</span>
<span class="hljs-keyword">let</span> c = <span class="hljs-keyword">new</span> Comb();

<span class="hljs-comment">// 提前将，将来要批量操作的对象，组合起来</span>
c.add(<span class="hljs-keyword">new</span> GoHome()); <span class="hljs-comment">// 添加'开门'命令</span>
c.add(<span class="hljs-keyword">new</span> OpenComputer()); <span class="hljs-comment">// 添加'开电脑'命令</span>
c.add(<span class="hljs-keyword">new</span> OpenMusic()); <span class="hljs-comment">// 添加'开音乐'命令</span>

c.action(); <span class="hljs-comment">// 执行添加的所有命令</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>小结</strong></p>
<ul>
<li>组合模式在对象间形成<code>树形</code>结构</li>
<li>组合模式中对基本对象和组合对象<code>被一致对待</code></li>
<li>无需关心对象有多少层，调用时只需要在<code>根部进行调用</code></li>
<li>将多个对象的功能，组装起来，实现<code>批量执行</code></li>
</ul>
<h3 data-id="heading-19">享元模式</h3>
<blockquote>
<p>享元模式（Flyweight Pattern）主要用于减少创建对象的数量，以减少内存占用和提高性能。</p>
<p>这种类型的设计模式属于结构型模式，它提供了减少对象数量从而改善应用所需的对象结构的方式。</p>
</blockquote>
<p><strong>特点</strong></p>
<ul>
<li>共享内存（主要是考虑内存，而非效率）</li>
<li>相同的数据（内存），共享使用</li>
</ul>
<p><strong>例子</strong></p>
<p>比如常见的事件代理，通过将若干个子元素的事件代理到一个父元素，子元素共同使用一个方法。如果都绑定到<code><span></code>标签，对内存开销太大 。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 点击span,拿到当前的span中的内容 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>1<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>2<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>3<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>4<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">var</span> box = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"box"</span>);
  box.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-keyword">let</span> target = e.target;
    <span class="hljs-keyword">if</span> (e.nodeName === <span class="hljs-string">"SPAN"</span>) &#123;
      alert(target.innerHTML);
    &#125;
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>小结</strong></p>
<ul>
<li>将相同的部分抽象出来</li>
<li>符合开放封闭的原则</li>
</ul>
<h2 data-id="heading-20">行为型</h2>
<h3 data-id="heading-21">迭代器模式</h3>
<blockquote>
<p>迭代器模式提供一种方法顺序访问一个聚合对象中的各个元素，而又不暴露对象的对象的内部表示。</p>
<p>迭代器模式可以把迭代的过程从业务逻辑中分离出来，在使用迭代器模式之后，及时不关心对象的内部构造，也可以按照顺序访问其中的每个元素。</p>
</blockquote>
<p>简单类说，它的目的就是去遍历一个可遍历的对象。</p>
<p>像 JS 中原生的 forEach、map 等方法都属于是迭代器模式的一种实现，一般来说不用自己去实现迭代器。</p>
<p>在 JS 中有一种<strong>类数组</strong>的存在，他们没有迭代方法，比如 nodeList、arguments 并不能直接使用迭代方法，需要使用 jQuery 的 each 方法或者将类数组装换为真正的数组在进行迭代。</p>
<p>而在最新的 ES6 中，对有只要有 Iterator 接口的数据类型都可以使用 for..of..进行遍历，而他的底层则是对 next 方法的反复调用，具体参考<a href="https://es6.ruanyifeng.com/#docs/iterator" target="_blank" rel="nofollow noopener noreferrer">阮一峰-Iterator 和 for...of 循环</a>。</p>
<p><strong>例子</strong></p>
<p>我们可以借助 Iterator 接口自己实现一个迭代器。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Creater</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">list</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.list = list;
  &#125;
  <span class="hljs-comment">// 创建一个迭代器，也叫遍历器</span>
  <span class="hljs-function"><span class="hljs-title">createIterator</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Iterator(<span class="hljs-built_in">this</span>);
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Iterator</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">creater</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.list = creater.list;
    <span class="hljs-built_in">this</span>.index = <span class="hljs-number">0</span>;
  &#125;
  <span class="hljs-comment">// 判断是否遍历完数据</span>
  <span class="hljs-function"><span class="hljs-title">isDone</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.index >= <span class="hljs-built_in">this</span>.list.length) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.list[<span class="hljs-built_in">this</span>.index++];
  &#125;
&#125;

<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">var</span> creater = <span class="hljs-keyword">new</span> Creater(arr);
<span class="hljs-keyword">var</span> iterator = creater.createIterator();
<span class="hljs-built_in">console</span>.log(iterator.list); <span class="hljs-comment">// [1, 2, 3, 4]</span>
<span class="hljs-keyword">while</span> (!iterator.isDone()) &#123;
  <span class="hljs-built_in">console</span>.log(iterator.next());
  <span class="hljs-comment">// 1</span>
  <span class="hljs-comment">// 2</span>
  <span class="hljs-comment">// 3</span>
  <span class="hljs-comment">// 4</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>小结</strong></p>
<ol>
<li>JavaScript 中的有序数据集合有 Array，Map，Set，String，typeArray，arguments，NodeList，不包括 Object</li>
<li>任何部署了[Symbol.iterator]接口的数据都可以使用 for...of 循环遍历</li>
<li>迭代器模式使目标对象和迭代器对象分离，符合开放封闭原则</li>
</ol>
<h3 data-id="heading-22">订阅/发布模式（观察者）</h3>
<blockquote>
<p>发布/订阅模式又叫观察者模式，她定义对象间的一种一对多的依赖关系。当一个对象的状态发生改变时，所有依赖他的对象都将得到通知。在 JavaScrtipt 中，我们一般使用时间模型来替代传统的发布/订阅模式。</p>
</blockquote>
<p>比如：Vue 中的双向绑定和事件机制。</p>
<p><strong>发布/订阅模式和观察者模式的区别</strong></p>
<ul>
<li>
<p>发布者可以直接处接到订阅的操作，叫观察者模式</p>
</li>
<li>
<p>发布者不直接触及到订阅者，而是由统一的第三方完成通信操作，叫发布/订阅模式</p>
<p><img alt="发布订阅模式和观察者模式.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08385cf5952c42959949a3bef0ac2565~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p><strong>例子</strong></p>
<p>可以自己实现一个事件总线，模拟<code>$emit</code>和<code>$on</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventBus</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.callbacks = &#123;&#125;;
  &#125;
  $on(name, fn) &#123;
    (<span class="hljs-built_in">this</span>.callbacks[name] || (<span class="hljs-built_in">this</span>.callbacks[name] = [])).push(fn);
  &#125;
  $emit(name, args) &#123;
    <span class="hljs-keyword">let</span> cbs = <span class="hljs-built_in">this</span>.callbacks[name];
    <span class="hljs-keyword">if</span> (cbs) &#123;
      cbs.forEach(<span class="hljs-function">(<span class="hljs-params">c</span>) =></span> &#123;
        c.call(<span class="hljs-built_in">this</span>, args);
      &#125;);
    &#125;
  &#125;
  $off(name) &#123;
    <span class="hljs-built_in">this</span>.callbacks[name] = <span class="hljs-literal">null</span>;
  &#125;
&#125;
<span class="hljs-keyword">let</span> event = <span class="hljs-keyword">new</span> EventBus();
event.$on(<span class="hljs-string">"event1"</span>, <span class="hljs-function">(<span class="hljs-params">arg</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"event1"</span>, arg);
&#125;);

event.$on(<span class="hljs-string">"event2"</span>, <span class="hljs-function">(<span class="hljs-params">arg</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"event2"</span>, arg);
&#125;);

event.$emit(<span class="hljs-string">"event1"</span>, <span class="hljs-number">1</span>); <span class="hljs-comment">// event1 1</span>
event.$emit(<span class="hljs-string">"event2"</span>, <span class="hljs-number">2</span>); <span class="hljs-comment">// event2 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">策略模式</h3>
<blockquote>
<p>定义一系列的算法，把他们一个个封装起来，并使他们可以替换。</p>
</blockquote>
<p>策略模式的目的就是将算法的使用和算法的实现分离开来。</p>
<p>一个策略模式通常由两部分组成：</p>
<ul>
<li>一组可变的策略类：封装了具体的算法，负责具体的计算过程</li>
<li>一组不变的环境类：接收到请求后，随后将请求委托到某个策略类</li>
</ul>
<p>说明环境类要维持对某个策略对象的引用。</p>
<p><strong>例子</strong></p>
<p>通过绩效等级计算奖金，可以轻易的写出如下的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> calculateBonus = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">performanceLevel, salary</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (performanceLevel === <span class="hljs-string">"S"</span>) &#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">4</span>;
  &#125;
  <span class="hljs-keyword">if</span> (performanceLevel === <span class="hljs-string">"A"</span>) &#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">3</span>;
  &#125;
  <span class="hljs-keyword">if</span> (performanceLevel === <span class="hljs-string">"B"</span>) &#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">2</span>;
  &#125;
&#125;;

calculateBonus(<span class="hljs-string">"B"</span>, <span class="hljs-number">20000</span>); <span class="hljs-comment">// 输出：40000</span>
calculateBonus(<span class="hljs-string">"S"</span>, <span class="hljs-number">6000</span>); <span class="hljs-comment">// 输出：24000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用策略模式修改代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> strategies = &#123;
  <span class="hljs-attr">S</span>: <span class="hljs-function">(<span class="hljs-params">salary</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">4</span>;
  &#125;,
  <span class="hljs-attr">A</span>: <span class="hljs-function">(<span class="hljs-params">salary</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">3</span>;
  &#125;,
  <span class="hljs-attr">B</span>: <span class="hljs-function">(<span class="hljs-params">salary</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">2</span>;
  &#125;,
&#125;;
<span class="hljs-keyword">var</span> calculateBonus = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">level, salary</span>) </span>&#123;
  <span class="hljs-keyword">return</span> strategies[level](salary);
&#125;;
<span class="hljs-built_in">console</span>.log(calculateBonus(<span class="hljs-string">"S"</span>, <span class="hljs-number">200</span>)); <span class="hljs-comment">// 输出：800</span>
<span class="hljs-built_in">console</span>.log(calculateBonus(<span class="hljs-string">"A"</span>, <span class="hljs-number">200</span>)); <span class="hljs-comment">// 输出：600</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">状态模式</h3>
<blockquote>
<p>状态模式允许一个对象在其内部状态改变的时候改变</p>
</blockquote>
<p>状态模式主要解决的是当控制一个对象状态的条件表达式过于复杂时的情况。把状态的判断逻辑转移到表示不同状态的一系列类中，可以把复杂的判断逻辑简化。</p>
<p><strong>例子</strong></p>
<p>实现一个交通灯的切换。</p>
<p>点击查看Demo：<a href="https://jsrun.net/x4NKp/embedded/all/light">交通信号灯-在线例子</a></p>
<p>这时候如果在加一个蓝光的话，可以直接添加一个蓝光的类，然后添加 parssBtn 方法，其他状态都不需要变化。</p>
<p><strong>小结</strong></p>
<ul>
<li>通过定义不同的状态类，根据状态的改变而改变状态的行为，不必把大量的逻辑都写在被操作对象的类中，而且容易增加新的状态。</li>
<li>符合开放封闭原则</li>
</ul>
<h3 data-id="heading-25">解释器模式</h3>
<blockquote>
<p>**解释器模式(Interpreter)：**给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子。</p>
</blockquote>
<p>用到的比较少，可以参考两篇文章来理解。</p>
<ul>
<li><a href="https://cloud.tencent.com/developer/article/1617312" target="_blank" rel="nofollow noopener noreferrer">设计模式 - 解释器模式 - JavaScript</a></li>
<li><a href="https://www.jb51.net/article/50680.htm" target="_blank" rel="nofollow noopener noreferrer">javascript 设计模式之解释器模式详解</a></li>
</ul>
<p><strong>小结</strong></p>
<ul>
<li>描述语言语法如何定义，如何解释和编译</li>
<li>用于专业场景</li>
</ul>
<h3 data-id="heading-26">中介者模式</h3>
<blockquote>
<p>中介者模式（Mediator Pattern）是用来降低多个对象和类之间的通信复杂性。</p>
<p>这种模式提供了一个中介类，该类通常处理不同类之间的通信，并支持松耦合，使代码易于维护</p>
</blockquote>
<p>通过一个中介者对象，其他所有相关对象都通过该对象来通信，而不是相互引用，但其中一个对象发生改变时，只需要通知中介者对象即可。</p>
<p>通过中介者模式可以解除对象与对象之前的耦合关系。</p>
<p>例如：Vuex</p>
<p><img alt="middle-parttern.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18a0b60237d64eaf9339df75e32c1d2e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>参考链接：<a href="https://segmentfault.com/a/1190000020075738" target="_blank" rel="nofollow noopener noreferrer">JavaScript 中介者模式</a></p>
<p><strong>小结</strong></p>
<ul>
<li>将各关联对象通过中介者隔离</li>
<li>符合开放封闭原则</li>
<li>减少耦合</li>
</ul>
<h3 data-id="heading-27">访问者模式</h3>
<blockquote>
<p>在访问者模式（Visitor Pattern）中，我们使用了一个访问者类，它改变了元素类的执行算法。</p>
<p>通过这种方式，元素的执行算法可以随着访问者改变而改变。</p>
</blockquote>
<p><strong>例子</strong></p>
<p>通过访问者调用元素类的方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 访问者</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Visitor</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.visit = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">concreteElement</span>) </span>&#123;
    concreteElement.doSomething(); <span class="hljs-comment">// 谁访问，就使用谁的doSomething()</span>
  &#125;;
&#125;
<span class="hljs-comment">// 元素类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ConceteElement</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.doSomething = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"这是一个具体元素"</span>);
  &#125;;
  <span class="hljs-built_in">this</span>.accept = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">visitor</span>) </span>&#123;
    visitor.visit(<span class="hljs-built_in">this</span>);
  &#125;;
&#125;
<span class="hljs-comment">// Client</span>
<span class="hljs-keyword">var</span> ele = <span class="hljs-keyword">new</span> ConceteElement();
<span class="hljs-keyword">var</span> v = <span class="hljs-keyword">new</span> Visitor();
ele.accept(v); <span class="hljs-comment">// 这是一个具体元素</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>小结</strong></p>
<ul>
<li>假如一个对象中存在着一些与本对象不相干（或者关系较弱）的操作，为了避免这些操作污染这个对象，则可以使用访问者模式来把这些操作封装到访问者中去。</li>
<li>假如一组对象中，存在着相似的操作，为了避免出现大量重复的代码，也可以将这些重复的操作封装到访问者中去。</li>
</ul>
<h3 data-id="heading-28">备忘录模式</h3>
<blockquote>
<p>备忘录模式（Memento Pattern）保存一个对象的某个状态，以便在适当的时候恢复对象</p>
</blockquote>
<p><strong>例子</strong></p>
<p>实现一个带有保存记录功能的”编辑器“，功能包括</p>
<ul>
<li>随时记录一个对象的状态变化</li>
<li>随时可以恢复之前的某个状态（如撤销功能）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 状态备忘</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Memento</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">content</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.content = content;
  &#125;
  <span class="hljs-function"><span class="hljs-title">getContent</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.content;
  &#125;
&#125;

<span class="hljs-comment">// 备忘列表</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CareTaker</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.list = [];
  &#125;
  <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">memento</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.list.push(memento);
  &#125;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">index</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.list[index];
  &#125;
&#125;

<span class="hljs-comment">// 编辑器</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Editor</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.content = <span class="hljs-literal">null</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">setContent</span>(<span class="hljs-params">content</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.content = content;
  &#125;
  <span class="hljs-function"><span class="hljs-title">getContent</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.content;
  &#125;
  <span class="hljs-function"><span class="hljs-title">saveContentToMemento</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Memento(<span class="hljs-built_in">this</span>.content);
  &#125;
  <span class="hljs-function"><span class="hljs-title">getContentFromMemento</span>(<span class="hljs-params">memento</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.content = memento.getContent();
  &#125;
&#125;

<span class="hljs-comment">// 测试代码</span>
<span class="hljs-keyword">let</span> editor = <span class="hljs-keyword">new</span> Editor();
<span class="hljs-keyword">let</span> careTaker = <span class="hljs-keyword">new</span> CareTaker();

editor.setContent(<span class="hljs-string">"111"</span>);
editor.setContent(<span class="hljs-string">"222"</span>);
careTaker.add(editor.saveContentToMemento()); <span class="hljs-comment">// 存储备忘录</span>
editor.setContent(<span class="hljs-string">"333"</span>);
careTaker.add(editor.saveContentToMemento()); <span class="hljs-comment">// 存储备忘录</span>
editor.setContent(<span class="hljs-string">"444"</span>);

<span class="hljs-built_in">console</span>.log(editor.getContent()); <span class="hljs-comment">// 444</span>
editor.getContentFromMemento(careTaker.get(<span class="hljs-number">1</span>)); <span class="hljs-comment">// 撤销</span>
<span class="hljs-built_in">console</span>.log(editor.getContent()); <span class="hljs-comment">// 333</span>
editor.getContentFromMemento(careTaker.get(<span class="hljs-number">0</span>)); <span class="hljs-comment">// 撤销</span>
<span class="hljs-built_in">console</span>.log(editor.getContent()); <span class="hljs-comment">// 222</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>小结</strong></p>
<ul>
<li>状态对象与使用者分开（解耦）</li>
<li>符合开放封闭原则</li>
</ul>
<h3 data-id="heading-29">模板方法模式</h3>
<blockquote>
<p>在模板模式（Template Pattern）中，一个抽象类公开定义了执行它的方法的方式/模板。</p>
<p>它的子类可以按需要重写方法实现，但调用将以抽象类中定义的方式进行。</p>
</blockquote>
<p>感觉用到的不是很多，想了解的可以点击下面的参考链接。</p>
<p>参考：<a href="https://zhuanlan.zhihu.com/p/95084871" target="_blank" rel="nofollow noopener noreferrer">JavaScript 设计模式之模板方法模式</a></p>
<h3 data-id="heading-30">职责链模式</h3>
<blockquote>
<p>顾名思义，责任链模式（Chain of Responsibility Pattern）为请求创建了一个接收者对象的链。</p>
<p>这种模式给予请求的类型，对请求的发送者和接收者进行解耦。</p>
</blockquote>
<p>在这种模式中，通常每个接收者都包含对另一个接收者的引用。</p>
<p>如果一个对象不能处理该请求，那么它会把相同的请求传给下一个接收者，依此类推。</p>
<p><strong>例子</strong></p>
<p>公司的报销审批流程：组长=》项目经理=》财务总监</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 请假审批，需要组长审批、经理审批、最后总监审批</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Action</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.nextAction = <span class="hljs-literal">null</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">setNextAction</span>(<span class="hljs-params">action</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.nextAction = action;
  &#125;
  <span class="hljs-function"><span class="hljs-title">handle</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> 审批`</span>);
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.nextAction != <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-built_in">this</span>.nextAction.handle();
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">let</span> a1 = <span class="hljs-keyword">new</span> Action(<span class="hljs-string">"组长"</span>);
<span class="hljs-keyword">let</span> a2 = <span class="hljs-keyword">new</span> Action(<span class="hljs-string">"项目经理"</span>);
<span class="hljs-keyword">let</span> a3 = <span class="hljs-keyword">new</span> Action(<span class="hljs-string">"财务总监"</span>);
a1.setNextAction(a2);
a2.setNextAction(a3);
a1.handle();
<span class="hljs-comment">// 组长 审批</span>
<span class="hljs-comment">// 项目经理 审批</span>
<span class="hljs-comment">// 财务总监 审批</span>

<span class="hljs-comment">// 将一步操作分为多个职责来完成，一个接一个的执行，最终完成操作。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>小结</strong></p>
<ul>
<li>可以联想到 jQuery、Promise 这种链式操作</li>
<li>发起者和处理者进行隔离</li>
<li>符合开发封闭原则</li>
</ul>
<h3 data-id="heading-31">命令模式</h3>
<blockquote>
<p>命令模式（Command Pattern）是一种数据驱动的设计模式，它属于行为型模式。</p>
<p>请求以命令的形式包裹在对象中，并传给调用对象。</p>
</blockquote>
<p>调用对象寻找可以处理该命令的合适的对象，并把该命令传给相应的对象，该对象执行命令。</p>
<p><strong>例子</strong></p>
<p>实现一个编辑器，有很多命令，比如：写入、读取等等。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Editor</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.content = <span class="hljs-string">""</span>;
    <span class="hljs-built_in">this</span>.operator = [];
  &#125;
  <span class="hljs-function"><span class="hljs-title">write</span>(<span class="hljs-params">content</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.content += content;
  &#125;
  <span class="hljs-function"><span class="hljs-title">read</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.content);
  &#125;
  <span class="hljs-function"><span class="hljs-title">space</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.content += <span class="hljs-string">" "</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">readOperator</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.operator);
  &#125;
  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params">...args</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.operator.push(args[<span class="hljs-number">0</span>]);
    <span class="hljs-built_in">this</span>[args[<span class="hljs-number">0</span>]].apply(<span class="hljs-built_in">this</span>, args.slice(<span class="hljs-number">1</span>));
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;
&#125;

<span class="hljs-keyword">const</span> editor = <span class="hljs-keyword">new</span> Editor();

editor
  .run(<span class="hljs-string">"write"</span>, <span class="hljs-string">"hello"</span>)
  .run(<span class="hljs-string">"space"</span>)
  .run(<span class="hljs-string">"write"</span>, <span class="hljs-string">"zkk!"</span>)
  .run(<span class="hljs-string">"read"</span>); <span class="hljs-comment">// => 'hello zkk!'</span>

<span class="hljs-comment">// 输出操作队列</span>
editor.readOperator(); <span class="hljs-comment">// ["write", "space", "write", "read"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>小结</strong></p>
<ul>
<li>降低耦合</li>
<li>新的命令可以很容易的添加到系统中</li>
</ul>
<h2 data-id="heading-32">综述</h2>
<h3 data-id="heading-33">(1)面向对象最终的设计目标：</h3>
<ul>
<li>
<p>A 可扩展性：有了新的需求，新的性能可以容易添加到系统中，不影响现有的性能，也不会带来新的缺陷。</p>
</li>
<li>
<p>B 灵活性：添加新的功能代码修改平稳地发生，而不会影响到其它部分。</p>
</li>
<li>
<p>C 可替换性：可以将系统中的某些代码替换为相同接口的其它类，不会影响到系统。</p>
</li>
</ul>
<h3 data-id="heading-34">(2)设计模式的好处：</h3>
<ul>
<li>A 设计模式使人们可以更加简单方便地复用成功的设计和体系结构。</li>
<li>B 设计模式也会使新系统开发者更加容易理解其设计思路。</li>
</ul>
<h3 data-id="heading-35">(3)学习设计模式有三重境界(网上看到好多次)：</h3>
<ul>
<li>
<p>第一重： 你学习一个设计模式就在思考我刚做的项目中哪里能用到(手中有刀，心中无刀)</p>
</li>
<li>
<p>第二重： 设计模式你都学完了，但是当遇到一个问题的时候，你发现有好几种设计模式供你选择，你无处下(手中有刀，心中也有刀)</p>
</li>
<li>
<p>第三重：也是最后一重，你可能没有设计模式的概念了，心里只有几大设计原则，等用到的时候信手拈来(刀法的最高境界：手中无刀，心中也无刀)</p>
</li>
</ul>
<h2 data-id="heading-36">结语</h2>
<p>以下是摘抄自掘金小册-<a href="https://juejin.cn/book/6844733790204461070" target="_blank">JavaScript 设计模式核⼼原理与应⽤实践</a>的结语。</p>
<p>设计模式的征程，到此就告一段落了。但对各位来说，真正的战斗才刚刚开始。设计模式的魅力，不在纸面上，而在实践中。</p>
<blockquote>
<p>学设计模式：</p>
<p>一在多读——读源码，读资料，读好书；</p>
<p>二在多练——把你学到的东西还原到业务开发里去，看看它是否 OK，有没有问题？如果有问题，如何修复、如何优化？没有一种设计模式是完美的，设计模式和人一样，处在动态发展的过程中，并不是只有 GOF 提出的 23 种设计模式可以称之为设计模式。</p>
</blockquote>
<p><strong>只要一种方案遵循了设计原则、解决了一类问题，那么它都可以被冠以“设计模式”的殊荣。</strong></p>
<p>在各位从设计模式小册毕业之际，希望大家带走的不止是知识，还有好的学习习惯、阅读习惯。最重要的，是深挖理论知识的勇气和技术攻关的决心。这些东西不是所谓“科班”的专利，而是一个优秀工程师的必须。</p>
<h2 data-id="heading-37">参考</h2>
<ul>
<li><a href="https://juejin.cn/book/6844733790204461070" target="_blank">JavaScript 设计模式核⼼原理与应⽤实践</a></li>
<li><a href="https://segmentfault.com/a/1190000017787537" target="_blank" rel="nofollow noopener noreferrer">JavaScript 中常用的设计模式</a></li>
<li><a href="https://blog.csdn.net/erlian1992/article/details/51151928" target="_blank" rel="nofollow noopener noreferrer">大话设计模式</a></li>
<li><a href="https://www.w3cschool.cn/zobyhd/iqdu9ozt.html" target="_blank" rel="nofollow noopener noreferrer">设计模式-W3CSchool</a></li>
<li><a href="https://www.runoob.com/design-pattern/design-pattern-tutorial.html" target="_blank" rel="nofollow noopener noreferrer">设计模式-菜鸟教程</a></li>
</ul>
<blockquote>
<p>来自九旬的原创：<a href="https://www.zhangningle.top/computer-base/%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F.html#%E5%89%8D%E8%A8%80" target="_blank" rel="nofollow noopener noreferrer">博客原文链接</a></p>
</blockquote>
<p>本文正在参与「掘金小册免费学啦！」活动, 点击查看<a href="https://juejin.cn/post/6943533938090442765" target="_blank">活动详情</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            