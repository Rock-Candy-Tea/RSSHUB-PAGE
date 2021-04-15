
---
title: '使用JavaScript学习设计模式（1）_ 小册免费学'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7669'
author: 掘金
comments: false
date: Wed, 14 Apr 2021 18:51:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=7669'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">系列文章</h2>
<ul>
<li>使用JavaScript学习设计模式（1）| 小册免费学</li>
<li><a href="https://juejin.cn/post/6951211551340625957" target="_blank">使用JavaScript学习设计模式（2）| 小册免费学</a></li>
<li><a href="https://juejin.cn/post/6951211911748780062" target="_blank">使用JavaScript学习设计模式（3）| 小册免费学</a></li>
<li><a href="https://juejin.cn/post/6951212035145203725" target="_blank">使用JavaScript学习设计模式（4）| 小册免费学</a></li>
</ul>
<h2 data-id="heading-1">前言</h2>
<p>去年的时候先是看了<a href="https://juejin.cn/user/2400989094885495" target="_blank">修言</a>大佬的性能优化掘金小册子，收获良多。</p>
<p>之后紧接着买了这本<a href="https://juejin.cn/book/6844733790204461070/section/6844733790246404109" target="_blank">JavaScript 设计模式核⼼原理与应⽤实践</a>，刚好最近有<a href="https://juejin.cn/post/6943533938090442765" target="_blank">小册免费学</a>的活动，就赶紧把这篇笔记整理出来了，并且补充了小册子中的没有写到的其余设计模式，学习过程中结合 JavaScript 编写的例子，以便于理解和加深印象。</p>
<p>与其说是一篇文章，其实更像是一篇总结性质的学习笔记。</p>
<h2 data-id="heading-2">为什么要学习设计模式？</h2>
<p>学习之前，先了解什么是设计模式？</p>
<blockquote>
<p>设计模式（Design Pattern）是前辈们对代码开发经验的总结，是解决特定问题的一系列套路。它不是语法规定，而是一套用来提高代码可复用性、可维护性、可读性、稳健性以及安全性的解决方案。</p>
</blockquote>
<p>简答理解 <strong>它是一套被反复使用、多人知晓的、经过分类的、代码设计经验总结。</strong></p>
<p>烹饪有菜谱，游戏有攻略，每个领域都存在一些能够让我们又好又快地达成目标的“套路”。在程序世界，编程的“套路”就是设计模式。</p>
<p>学习它也就是学习这个编程世界的套路，对以后升级打怪打装备有很大的帮助。在瞬息万变的前端领域，设计模式也是一种“一次学习，终生受用”知识。</p>
<h3 data-id="heading-3">设计模式的原则</h3>
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
<h3 data-id="heading-4">高内聚和低耦合</h3>
<p>通过设计模式可以帮助我们增强代码的可重用性、可扩充性、 可维护性、灵活性好。我们使用设计模式最终的目的是实现代码的 高内聚 和 低耦合。</p>
<p>举例一个现实生活中的例子，例如一个公司，一般都是各个部门各司其职，互不干涉。各个部门需要沟通时通过专门的负责人进行对接。</p>
<p>在软件里面也是一样的 一个功能模块只是关注一个功能，一个模块最好只实现一个功能，这个是所谓的<strong>内聚</strong>。</p>
<p>模块与模块之间、系统与系统之间的交互，是不可避免的， 但是我们要尽量减少由于交互引起的单个模块无法独立使用或者无法移植的情况发生， 尽可能多的单独提供接口用于对外操作， 这个就是所谓的<strong>低耦合</strong></p>
<h3 data-id="heading-5">封装变化</h3>
<p>在实际开发过程中，不发生变化的代码基本是不存在的，所以我要将代码的变化最小化。</p>
<p><strong>设计模式的核心就是去观察你整个逻辑里的变与不变，然后将不变分离，达到使变化的部分灵活、不变的地方稳定的目的。</strong></p>
<h2 data-id="heading-6">设计模式的种类</h2>
<p>常用的可以分为创建型、结构型、行为型三类，一共 23 种模式。</p>
<p><strong>创建型：</strong></p>
<ul>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F">工厂模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F">单例模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E5%8E%9F%E5%9E%8B%E6%A8%A1%E5%BC%8F">原型模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E6%9E%84%E9%80%A0%E5%99%A8%E6%A8%A1%E5%BC%8F">构造器模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E6%8A%BD%E8%B1%A1%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F">抽象工厂模式</a></li>
</ul>
<p><strong>结构型：</strong></p>
<ul>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E8%A3%85%E9%A5%B0%E5%99%A8%E6%A8%A1%E5%BC%8F">装饰器模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E9%80%82%E9%85%8D%E5%99%A8%E6%A8%A1%E5%BC%8F">适配器模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E4%BB%A3%E7%90%86%E6%A8%A1%E5%BC%8F">代理模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E6%A1%A5%E6%8E%A5%E6%A8%A1%E5%BC%8F">桥接模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E5%A4%96%E8%A7%82%E6%A8%A1%E5%BC%8F">外观模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E7%BB%84%E5%90%88%E6%A8%A1%E5%BC%8F">组合模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E4%BA%AB%E5%85%83%E6%A8%A1%E5%BC%8F">享元模式</a></li>
</ul>
<p><strong>行为型：</strong></p>
<ul>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E8%BF%AD%E4%BB%A3%E5%99%A8%E6%A8%A1%E5%BC%8F">迭代器模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E5%8F%91%E5%B8%83/%E8%AE%A2%E9%98%85%E6%A8%A1%E5%BC%8F%EF%BC%88%E8%A7%82%E5%AF%9F%E8%80%85%EF%BC%89">发布/订阅模式（观察者）</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E7%AD%96%E7%95%A5%E6%A8%A1%E5%BC%8F">策略模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E7%8A%B6%E6%80%81%E6%A8%A1%E5%BC%8F">状态模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E8%A7%A3%E9%87%8A%E5%99%A8%E6%A8%A1%E5%BC%8F">解释器模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E4%B8%AD%E4%BB%8B%E8%80%85%E6%A8%A1%E5%BC%8F">中介者模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E8%AE%BF%E9%97%AE%E8%80%85%E6%A8%A1%E5%BC%8F">访问者模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E5%A4%87%E5%BF%98%E5%BD%95%E6%A8%A1%E5%BC%8F">备忘录模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E6%A8%A1%E6%9D%BF%E6%96%B9%E6%B3%95%E6%A8%A1%E5%BC%8F">模板方法模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E8%81%8C%E8%B4%A3%E9%93%BE%E6%A8%A1%E5%BC%8F">职责链模式</a></li>
<li>[x]<a href="https://juejin.cn/post/6951211356641034247#%E5%91%BD%E4%BB%A4%E6%A8%A1%E5%BC%8F">命令模式</a></li>
</ul>
<h2 data-id="heading-7">创建型</h2>
<h3 data-id="heading-8">工厂模式</h3>
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
<h3 data-id="heading-9">单例模式</h3>
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
<h3 data-id="heading-10">原型模式</h3>
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
<h3 data-id="heading-11">构造器模式</h3>
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
<h3 data-id="heading-12">抽象工厂模式</h3>
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
<blockquote>
<p>来自九旬的原创：<a href="https://www.zhangningle.top/computer-base/%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F.html#%E5%89%8D%E8%A8%80" target="_blank" rel="nofollow noopener noreferrer">博客原文链接</a></p>
</blockquote>
<p>本文正在参与「掘金小册免费学啦！」活动, 点击查看<a href="https://juejin.cn/post/6943533938090442765" target="_blank">活动详情</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            