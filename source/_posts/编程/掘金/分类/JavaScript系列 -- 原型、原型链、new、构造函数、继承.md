
---
title: 'JavaScript系列 -- 原型、原型链、new、构造函数、继承'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff89abb801574b0183f8b2f8dcd41728~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 20:01:36 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff89abb801574b0183f8b2f8dcd41728~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff89abb801574b0183f8b2f8dcd41728~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae7ffece953a48bd8ce4bf49ff3cf1a4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从这张图我们可以看出：Array、Object、Map、Set等等这些本质上是一个<strong>构造函数</strong>，其原型<code>prototype</code>（本质上其实是一个<strong>对象</strong>，详见下方）有很多的属性/方法，这些属性/方法都是我们平常会用到的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]
arr.concat([<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]) <span class="hljs-comment">// [1,2,3,4,5,6]</span>
arr.length <span class="hljs-comment">// 6</span>
<span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
map.set(<span class="hljs-string">"name"</span>,<span class="hljs-string">"John"</span>) <span class="hljs-comment">// Map(1) &#123;"name" => "John"&#125;</span>
map.set(<span class="hljs-string">"age"</span>,<span class="hljs-number">18</span>) <span class="hljs-comment">// Map(2) &#123;"name" => "John", "age" => 18&#125;</span>
map.has(<span class="hljs-string">"name"</span>) <span class="hljs-comment">// true</span>
map.has(<span class="hljs-string">"gender"</span>) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显我们看到使用这些方法的时候我们是通过"."来连接arr/map和其对应的属性/方法的，这有点像是对象访问属性/方法。记得之前看过一句话：<strong>万物皆对象</strong>，这就对上了。其实我们创建的arr/map都是一个对象，它们的属性/方法就好比是对象的属性/方法，所以用"."来连接。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0e8809eff4d4802a815417898d435dc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ba198062ffd47f3bb3fab7642d1851a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>诶奇怪，这里我们看到新创建的实例对象 arr/map 并没有那些属性/方法，那为什么可以用呢？而且为什么都能看到有<code>__proto__</code>这个东西呢？</p>
<p>原因有两点：</p>
<ul>
<li>创建的实例对象都有一个<code>__proto__</code>属性，这个属性指向其对应构造函数的<code>ptototype</code>属性（prototype属性见下方）</li>
<li>当我们想使用实例对象的属性或方法时我们先从这个实例对象本身找，如果这个实例对象没有想要的属性或方法，就会去<code>__proto__</code>对象里面找，再找不到就会沿着<code>原型链</code>去找，一直到【找到想要的属性/方法】或【<code>__proto__</code>属性的值为<code>null</code>】（<code>__proto__</code>属性和原型链见下方）</li>
</ul>
<p>那为什么要这样呢？很显然arr、obj、map、set有千千万万个，我们不可能每次创建一个新的arr/obj/map/set都要给它们添加属性/方法，<strong>这样不仅会效率低下，还会造成空间上的浪费</strong>。所以我们利用这个机制（原理），这样就可以直接使用JavaScript中自带的<code>数组/对象/Set/Map</code>的属性/方法，也不会造成空间上的浪费。</p>
<p>为了解释这一点，我们需要清楚：构造函数、new、原型、继承、原型链，我们一步一步来解读：</p>
<h2 data-id="heading-1">函数对象的属性 prototype 对象 —— 被称为 “函数的原型”</h2>
<h3 data-id="heading-2">我们先理解一下函数本质上是个对象</h3>
<h4 data-id="heading-3">1. 创建函数F</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2. 函数也是一个对象，它有一些属性和方法</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce62cf47d65c4ec7b4c80544a1028f4e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 形象地理解就是这样：</span>
F = &#123;
    F.length <span class="hljs-comment">// 形参个数</span>
    F.arguments <span class="hljs-comment">// 存放实参的类数组对象</span>
    F.name <span class="hljs-comment">// 函数名称</span>
    F.prototype <span class="hljs-comment">// 函数的原型</span>
    F.constructor 
    F.hasOwnProperty() <span class="hljs-comment">// 判断属性是否为本身的方法</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>既然如此的话那我们就可以在函数里面添加属性和方法啦：</p>
<pre><code class="hljs language-js copyable" lang="js">【添加属性】
F.age = <span class="hljs-number">18</span>
或
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params">age</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.age = <span class="hljs-number">18</span>
&#125;

【添加方法】
F.say()&#123;
    <span class="hljs-comment">// say()函数代码</span>
&#125;
或
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.say()&#123;
        <span class="hljs-comment">// say()函数代码</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">prototype 对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// F()函数对象里有个prototype属性，它也是一个对象</span>
F = &#123;
    <span class="hljs-attr">prototype</span>: &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">prototype 对象的属性</h3>
<p><code>prototype</code> 既然是一个对象，那么就也会有一些属性，它有一个默认的属性<code>constructor</code>，并且它<strong>默认指向当前函数</strong></p>
<pre><code class="hljs language-js copyable" lang="js">F = &#123;
    <span class="hljs-attr">prototype</span>: &#123;
        <span class="hljs-attr">constructor</span>: F    <span class="hljs-comment">// 指向当前函数</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>既然<code>prototype</code>是个对象，那我们也同样可以给它<strong>添加属性</strong>，例如：</p>
<pre><code class="hljs language-js copyable" lang="js">F.prototype.name = <span class="hljs-string">'BatMan'</span>;

<span class="hljs-comment">// 那F就变成如下：</span>
F = &#123;
    <span class="hljs-attr">prototype</span>: &#123;
        <span class="hljs-attr">constructor</span>: F,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'BatMan'</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">按照这个想法，于是我们就有了【构造函数】这个东西</h2>
<p>构造函数是这样创建出来的：（我们也将其称为<strong>类的创建</strong>）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47edc35dbd634eb681743e8e08e58235~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时我们使用 new 关键字来创建构造函数 F() 的一个实例对象 f，并在括号里传输参数<code>"John"</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d63dd66d0514c69ade85083e2aabfd9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里可以看到通过 new 关键字对构造函数 F 生成了实例对象 f，它获得了 name 这个属性</p>
<p>再看一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;<span class="hljs-string">"name"</span>:<span class="hljs-string">"nihao"</span>&#125;;
------------------
其实本质上是： 
<span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
<span class="hljs-built_in">console</span>.log(obj) <span class="hljs-comment">// &#123;&#125;</span>
obj.name = <span class="hljs-string">"nihao"</span>
这个过程
------------------
<span class="hljs-built_in">console</span>.log(obj); <span class="hljs-comment">// &#123; name: 'nihao' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们可以看到<code>Object</code>原本是一个函数，我们创建的<code>obj</code>是由<code>Object()</code>这个构造函数生成的，这也照应了Array、Object、Map、Set等等这些本质上是一个<strong>构造函数</strong></p>
<p>同时（通过这个思想的模仿），从本质上来讲：在JavaScript中，<strong>对象是由构造函数生成的</strong>，所以对象和函数对象没有区别，<strong>对象只是函数对象的其中一个</strong></p>
<h2 data-id="heading-8">给构造函数（类）添加属性/方法</h2>
<ul>
<li>方式一：将 say() 方法<strong>直接添加</strong>到构造函数 F 里面（叫做<strong>实例方法</strong>）</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff0babf423764a3aa824c59d86331cba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实例对象 f 将<strong>无法使用</strong> say()</p>
<ul>
<li>方式二：将say()方法<strong>添加到构造函数 F 的<code>prototype</code>属性对象</strong>里面（叫做<strong>原型方法</strong>）</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1ac96bb0999422fa4dd91cb2cd79fbc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里看到实例对象 f <strong>可以使用</strong>say()方法里</p>
<blockquote>
<p>这里解释一下原因：打个比方——（构造函数F）是“真身”，它通过new的方式进行“分身”得到自己的兄弟（实例对象f、f1、f2、f3...）“影分身”，这个期间真身同时将自己从“师傅”（F.prototype）习得的“技能”（属性/方法）同时复制给了影分身，而影分身应该叫真身的师傅为（f.__ proto__），所以真身和影分身们的师傅是同一个。所以师傅有了新技能（新增属性/方法），真身和影分身们就能同时拥有（对应第2个方法成立）。</p>
</blockquote>
<blockquote>
<p>另外，由于影分身是由真身拷贝出来的，所以真身新增技能，已拷贝出来的影分身并不能也拥有（对应第1个方法失效）。然而此时真身再拷贝出影分身，新的影分身就能拥有新技能了（var f1 = new F()，f1将可以使用say()方法）。</p>
</blockquote>
<p>其实这两种不同方式的给构造函数添加属性/方法分别对应的是<strong>构造函数继承</strong>和<strong>原型链继承</strong>（这后面会详解）</p>
<p>综上所述：我们一个类Sub（分身）要继承另一个类Super（真身），不仅<strong>要执行一下Super类的构造函数</strong>（继承真身的属性），还要<strong>继承Super类的prototype下的属性</strong>（继承真身师傅的属性），这是由于JavaScript中给对象定义属性有两种不同方式所造成的需要。</p>
<h2 data-id="heading-9">继承</h2>
<blockquote>
<p>所谓<strong>继承</strong>，就是把对象的属性/方法（函数）进行扩展后，可以继承给其他函数</p>
</blockquote>
<p>像Array、Object、Map、Set这些函数对象的<code>prototype</code>属性对象里面就有很多的属性和方法，如果想使用<code>数组/对象/Set/Map</code>的自带属性/方法原理上就是在这里“拿”的，更恰当的说法是继承的</p>
<p>由上面的例子可以看到，F.prototype新增了say()方法后，实例对象 f 就可以使用say()方法了</p>
<p>此时如果打印一下实例对象 f：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f357b3de23f64166ad4e1b0463913f87~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>诶，实例对象 f 中明明没有say()方法，为什么可以执行<code>console.log("构造函数的say()方法")</code>呢</p>
<p>关于这个问题的解决，我们需要了解new关键字创建实例对象的过程发生了什么、关于<code>__proto__</code>属性的理解</p>
<h2 data-id="heading-10">使用new关键字创建实例对象的过程</h2>
<p>这里参考文章 <a href="https://www.cnblogs.com/faith3/p/6209741.html" target="_blank" rel="nofollow noopener noreferrer">JS中的new操作符</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Base</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name
&#125;
<span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> Base(<span class="hljs-string">"base"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样代码的结果是什么，我们在Javascript引擎中看到的对象模型是：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a635284611674c41b0a1c99c4c55b36e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>new操作符具体干了什么呢?其实很简单，就干了三件事情</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj  = &#123;&#125;;
obj.__proto__ = Base.prototype;
Base.call(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第一行，我们创建了一个空对象obj</li>
<li>第二行，我们<strong>将这个空对象的__proto__成员指向了Base函数对象prototype成员对象</strong></li>
<li>第三行，我们将Base函数对象的<code>this指针替换成obj</code>，然后再调用Base函数，于是我们就给obj对象赋值了一个id成员变量，这个成员变量的值是”base”，（关于call函数的用法见 <a href="https://juejin.cn/post/6955363671371431973/#heading-9" target="_blank">JavaScript系列 -- this关键字</a>）</li>
</ul>
<h2 data-id="heading-11">对象的 <code>__proto__</code>属性 —— 被称为“对象的原型”</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f357b3de23f64166ad4e1b0463913f87~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还是上面那张图，我们看到实例对象 f 除了有name属性，其实还有一个<code>__proto__</code>属性，它也是一个对象，跟<code>prototype</code>分别称为显式原型和隐式原型。我们点开查看<code>__proto__</code>对象的属性：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/651a145f62e94f4c9fb822815583f3a3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里可以看到在实例对象 f 的<code>__proto__</code>这个属性对象里有say()方法，而这个say()方法哪来的呢？结合new的其中一个步骤：<strong>将实例对象的__proto__成员对象指向了构造函数的prototype成员对象</strong>和我们之前的一个操作：</p>
<pre><code class="hljs language-js copyable" lang="js">F.prototype.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"构造函数的say()方法"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个say()方法就是这么来的。我们大胆猜测实例对象 f 的say()方法就是从其<code>__proto__</code>对象中继承而来的</p>
<p>这里补充一下其实对象的属性有两种：<strong>自身属性</strong>和<strong>原型属性</strong>：我们所创建的实例对象f1，有自身属性name，还有从原型上找到的say()方法，我们可以使用hasOwnProperty方法检测一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(f.hasOwnProperty(<span class="hljs-string">'name'</span>));  <span class="hljs-comment">// true 说明是自身属性（方法）</span>
<span class="hljs-built_in">console</span>.log(f.hasOwnProperty(<span class="hljs-string">'say'</span>)); <span class="hljs-comment">// false 说明不是自身方法（属性）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>所以当我们在寻找/使用实例对象 f 的属性/方法时，它会先从自身属性/方法找有没有，如果没有就去<code>__proto__</code>对象，也就是它的原型里面找属性/方法</strong>。这就可以解释为什么实例对象 f 中明明没有say()方法，却可以执行<code>console.log("构造函数的say()方法")</code></p>
<p>那么问题来了，那如果在原型里面找不到呢？</p>
<p>如果原型里面找不到，就去原型里的原型去找，还找不到就去原型的原型的原型里找...于是就有了“<strong>原型链</strong>”的概念</p>
<h2 data-id="heading-12">原型链</h2>
<ol>
<li>外界访问对象的属性或使用它的方法</li>
<li>对象可以通过“.”操作获取到它自身属性/方法</li>
<li>如果查不到会到原型对象(__ proto __) 中去查找，</li>
<li>如果原型对象中还没有就会把当前得到的<strong>原型对象当作实例对象</strong>，继续通过(__ proto__) 去查找当前原型对象的原型对象中去找，</li>
<li>直到 【找到想要的属性/方法（通过字符串名称去判断的）】或 【__proto __为<code>null</code>】 时停止</li>
<li>__ proto __ 为null<strong>之前</strong>的__ proto __ 是一个<code>Object</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a64564f6c96e4191b5a276cf69b809e8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>还是上面那个例子，假设我们要使用另外的属性/方法<code>toString()</code>，在实例对象f的原型中找不到</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/651a145f62e94f4c9fb822815583f3a3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从这张图可以看出：实例对象 f 的原型的原型也是一个<code>Object</code>，我们查看这个<code>Object</code>（实例对象f的原型的原型）</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33e9e7cc4c98487a9c23040adbcea775~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发现诶有我们想要的<code>toString()</code>方法，于是停止向上查询。如果还找不到发现这个<code>Object</code>的<code>__proto__</code>为null或者说没有这个属性，我们也束手无策，返回报错，表示找不到</p>
<p>细心的小伙伴已经注意到：所有的原型链的<strong>终点</strong>都是<code>Object.prototype</code>，也就是上面那个f的原型的原型</p>
<p>那么问题来了，为什么不直接在 f()里面添加 say()就好，要在 F.prototype 里面添加</p>
<h2 data-id="heading-13">继承的作用在哪</h2>
<p>其实在前言中已经回答了这个问题，arr、obj、map、set有千千万万个，我们不可能每次创建一个新的arr/obj/map/set都要给它们添加属性/方法，<strong>不仅浪费时间，而且还会浪费空间</strong>。</p>
<p>同理，如果直接在 f里面添加 say()，那另外new出来的f1、f2、f3、...等实例对象都不能享有 say() 方法，所以不可取。</p>
<p>其次就算我们不在f里面添加 say() 方法，我们在构造函数F里面添加say()方法，然后再new出来的f1、f2、f3等实例对象虽然都能享有 say() 方法，但还是会<strong>浪费空间</strong>。那应该怎么做呢？</p>
<h2 data-id="heading-14">constructor 属性</h2>
<p>在说继承的方式前我们看一下<code>constructor</code>这个属性，构造函数 F 的原型<code>prototype</code>属性对象里面就有<code>constructor</code>这个属性，它的属性值就是构造函数 F</p>
<pre><code class="hljs language-js copyable" lang="js">F.prototype.constructor === F <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>又因为有</p>
<pre><code class="hljs language-js copyable" lang="js">f.__proto__ === F.prototype <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以</p>
<pre><code class="hljs language-js copyable" lang="js">f.__proto__.constructor === F <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值得注意的是</p>
<pre><code class="hljs language-js copyable" lang="js">f.constructor === F <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原因上面已经解释了：f没有<code>constructor</code>这个属性，所以会去<code>f.__proto__</code>里面找，所以上式才会成立</p>
<h2 data-id="heading-15">继承的方式有哪些</h2>
<p>继承方式有：</p>
<ul>
<li>构造函数继承</li>
<li>原型链继承</li>
<li>组合继承（组合了原型链继承和构造函数继承）</li>
<li>寄生组合继承</li>
<li>原型式继承</li>
</ul>
<p>关于理解以上的继承方式，我觉得最重要的是分清私有属性和公有属性，以及继承最终想要的结果：</p>
<blockquote>
<p>注意凡是this.-的，都是类的私有属性和方法，凡是-prototype.-的都是公有属性和方法</p>
</blockquote>
<blockquote>
<p>继承最终想要的结果就是父类创建的子类实例既能有自己的私有属性，还能有父类原型的公有属性</p>
</blockquote>
<h4 data-id="heading-16">原型链继承</h4>
<blockquote>
<p>分身同真身：分身没有私有技能；分身能从真身的师傅习得技能：分身能够共享师傅的公有技能</p>
</blockquote>
<ul>
<li>核心：子类的原型 = 父类的实例</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span> (<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name || <span class="hljs-string">'Animal'</span>;<span class="hljs-comment">// 属性</span>
    <span class="hljs-built_in">this</span>.sleep = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-comment">// 实例方法</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">'正在睡觉！'</span>);
    &#125;
&#125;
Animal.prototype.eat = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">food</span>) </span>&#123;  <span class="hljs-comment">// 原型方法</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">'正在吃：'</span> + food);
&#125;;
--------------------------------------------------------------
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
Cat.prototype = <span class="hljs-keyword">new</span> Animal(); <span class="hljs-comment">// 原型链继承（会造成 Cat.prototype.constructor === Animal）</span>
Cat.prototype.constructor = Cat; <span class="hljs-comment">// 矫正constructor属性，不破坏原型链</span>
--------------------------------------------------------------
Cat.prototype.name = <span class="hljs-string">"Tom"</span>;
<span class="hljs-comment">//　Test Code</span>
<span class="hljs-keyword">var</span> cat1 = <span class="hljs-keyword">new</span> Cat();
<span class="hljs-keyword">var</span> cat2 = <span class="hljs-keyword">new</span> Cat();
<span class="hljs-built_in">console</span>.log(cat1.sleep===cat2.sleep) <span class="hljs-comment">// true ------------------------- 1</span>
<span class="hljs-built_in">console</span>.log(cat1.eat(<span class="hljs-string">'fish'</span>)); <span class="hljs-comment">// "Tom正在吃fish"  --------------------- 2</span>
<span class="hljs-built_in">console</span>.log(cat1.eat===cat2.eat) <span class="hljs-comment">// true  ---------------------------- 3</span>
<span class="hljs-built_in">console</span>.log(cat1.name); <span class="hljs-comment">// "Tom"</span>
<span class="hljs-built_in">console</span>.log(cat1.sleep()); <span class="hljs-comment">// "Tom正在睡觉"</span>
<span class="hljs-built_in">console</span>.log(cat1 <span class="hljs-keyword">instanceof</span> Animal); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(cat1 <span class="hljs-keyword">instanceof</span> Cat); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>优点：</li>
</ul>
<ol>
<li>既能继承<strong>父类实例</strong>的属性和方法，也能继承<strong>父类原型</strong>的属性/方法。由【1】和【2】和【3】综合分析得出的。</li>
<li><strong>可以复用</strong>。由【1】和【2】和【3】综合分析可看出。基于原型链，构造函数所创建的实例中属性就<strong>不再是私有</strong>属性了，而是<strong>在原型中能共享</strong>的属性。无论是【1】中的sleep()方法还是【2】中的eat()方法都是公有的。</li>
</ol>
<ul>
<li>缺点：</li>
</ul>
<ol>
<li>由【1】可以看出，要是其中一个实例cat1对sleep()方法进行修改，那么所有实例对象的sleep()方法也会跟着改变，这意味着实例对象cat1、cat2、...<strong>没有私有属性</strong></li>
<li>创建子类实例时，无法向父类构造函数传参；</li>
<li>无法实现多继承（构造函数继承可解决）</li>
</ol>
<h4 data-id="heading-17">构造函数继承</h4>
<blockquote>
<p>分身不同真身：有私有技能；但分身无法习得真身师傅的技能</p>
</blockquote>
<ul>
<li>核心：使用父类的构造函数来增强子类实例，等于是复制父类的实例属性给子类（没有用到原型）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span> (<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name || <span class="hljs-string">'Animal'</span>;<span class="hljs-comment">// 属性</span>
    <span class="hljs-built_in">this</span>.sleep = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-comment">// 实例方法</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">'正在睡觉！'</span>);
    &#125;
&#125;
Animal.prototype.eat = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">food</span>) </span>&#123;  <span class="hljs-comment">// 原型方法</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">'正在吃：'</span> + food);
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>)</span>&#123;
-------------------------------
    Animal.call(<span class="hljs-built_in">this</span>);
-------------------------------
    <span class="hljs-built_in">this</span>.name = name || <span class="hljs-string">'Tom'</span>;
&#125;
<span class="hljs-comment">// Test Code</span>
<span class="hljs-keyword">var</span> cat1 = <span class="hljs-keyword">new</span> Cat();
<span class="hljs-keyword">var</span> cat2 = <span class="hljs-keyword">new</span> Cat()
<span class="hljs-built_in">console</span>.log(cat1.sleep===cat2.sleep) <span class="hljs-comment">// false ---------------------------------- 1</span>
<span class="hljs-built_in">console</span>.log(cat1.eat(<span class="hljs-string">'fish'</span>)); <span class="hljs-comment">// Uncaught TypeError: cat1.eat is not a function --------------- 2</span>
<span class="hljs-built_in">console</span>.log(cat1.name); <span class="hljs-comment">// "Tom"</span>
<span class="hljs-built_in">console</span>.log(cat1.sleep()); <span class="hljs-comment">// "Tom正在睡觉"</span>
<span class="hljs-built_in">console</span>.log(cat1 <span class="hljs-keyword">instanceof</span> Animal); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(cat1 <span class="hljs-keyword">instanceof</span> Cat); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>特点：</li>
</ul>
<ol>
<li>由【1】可看出每个子类实例cat1、cat2、...的属性/方法都<strong>是私有的</strong>，非共享的</li>
<li>如果删去<code>this.name = name || 'Tom';</code>则<code>console.log(cat1.name); // "Animal"</code>，说明这里<code>this.name = name || 'Animal';</code>的name原本是"Tom"不是null，这说明了创建子类实例时，<strong>可以向父类传递参数</strong>，而且call多个父类对象可以实现<strong>多继承</strong></li>
</ol>
<ul>
<li>缺点：</li>
</ul>
<ol>
<li>由【2】可看出，<strong>子类的实例</strong>只能继承父类的实例属性和方法，<strong>不能继承父类原型的属性/方法</strong></li>
<li><strong>无法实现函数复用</strong>：也是由【2】可看出的（因为无法继承父类原型所以无法做到复用）。</li>
</ol>
<h4 data-id="heading-18">原型链继承和构造函数继承的本质区别理解在于：</h4>
<p>上面说的：继承最终想要的结果就是父类创建的子类实例既能有自己的<code>私有属性</code>，还能有父类原型的<code>公有属性</code>。原型链继承只能实现<code>后者</code>，而构造函数继承只能实现<code>前者</code>。</p>
<h4 data-id="heading-19">组合继承（原型链继承+构造函数继承）</h4>
<blockquote>
<p>弄两个真身。分身不同一个真身：有私有属性；并且分身能够习得另一个真身师傅的公有技能</p>
</blockquote>
<ul>
<li>核心：相当于构造继承和原型链继承的组合体。
<ul>
<li>通过调用父类构造（对应【4】），<strong>继承父类的属性</strong>并保留<strong>传参</strong>的优点（构造函数继承的优点）</li>
<li>通过将父类实例作为子类原型（对应【5】），实现<strong>函数复用</strong>（原型链继承的优点）</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span> (<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name || <span class="hljs-string">'Animal'</span>;<span class="hljs-comment">// 属性</span>
    <span class="hljs-built_in">this</span>.sleep = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-comment">// 实例方法</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">'正在睡觉！'</span>);
    &#125;
&#125;
Animal.prototype.eat = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">food</span>) </span>&#123;  <span class="hljs-comment">// 原型方法</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">'正在吃：'</span> + food);
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>)</span>&#123;
-------------------------------
    Animal.call(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// --------------------------------- 4</span>
-------------------------------
    <span class="hljs-built_in">this</span>.name = name || <span class="hljs-string">'Tom'</span>;
&#125;
-------------------------------
Cat.prototype = <span class="hljs-keyword">new</span> Animal();  <span class="hljs-comment">// --------------------------------- 5</span>
Cat.prototype.constructor = Cat; <span class="hljs-comment">// ---------------------------- 5 // 矫正constructor属性，不破坏原型链</span>
-------------------------------
<span class="hljs-comment">// Test Code</span>
<span class="hljs-keyword">var</span> cat1 = <span class="hljs-keyword">new</span> Cat();
<span class="hljs-keyword">var</span> cat2 = <span class="hljs-keyword">new</span> Cat()
<span class="hljs-built_in">console</span>.log(cat1.sleep===cat2.sleep) <span class="hljs-comment">// false --------------------------- 1</span>
<span class="hljs-built_in">console</span>.log(cat1.eat(<span class="hljs-string">'fish'</span>)); <span class="hljs-comment">// "Tom正在吃：fish" -------------------------- 2</span>
<span class="hljs-built_in">console</span>.log(cat1.eat===cat2.eat) <span class="hljs-comment">// true --------------------------------- 3</span>
<span class="hljs-built_in">console</span>.log(cat1.name); <span class="hljs-comment">// "Tom"</span>
<span class="hljs-built_in">console</span>.log(cat1.sleep()); <span class="hljs-comment">// "Tom正在睡觉"</span>
<span class="hljs-built_in">console</span>.log(cat1 <span class="hljs-keyword">instanceof</span> Animal); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(cat1 <span class="hljs-keyword">instanceof</span> Cat); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>优点：</li>
</ul>
<ol>
<li>由【1】和【2】和【3】可看出：可以继承实例属性/方法，也可以继承原型属性/方法</li>
<li>由【1】可看出：可以拥有私有属性</li>
<li>由【2】和【3】可看出：可以实现函数复用</li>
<li>由【2】和【4】可看出：可以传参</li>
</ol>
<ul>
<li>缺点：调用了两次父类构造函数，生成了<strong>两份实例</strong>（不过也只是多耗了一点内存空间）</li>
</ul>
<h4 data-id="heading-20">寄生组合继承</h4>
<blockquote>
<p>效果跟组合继承一样，但实现方式完全不同，寄生组合式继承是借助中间方来继承</p>
</blockquote>
<ul>
<li>核心：通过寄生方式（利用中间函数），拷贝一份父类原型，这样，在调用两次父类的构造的时候，就不会初始化两次实例方法/属性</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span> (<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name || <span class="hljs-string">'Animal'</span>;<span class="hljs-comment">// 属性</span>
    <span class="hljs-built_in">this</span>.sleep = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-comment">// 实例方法</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">'正在睡觉！'</span>);
    &#125;
&#125;
Animal.prototype.eat = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">food</span>) </span>&#123;  <span class="hljs-comment">// 原型方法</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">'正在吃：'</span> + food);
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cat</span>(<span class="hljs-params">name</span>)</span>&#123;
-------------------------------
    Animal.call(<span class="hljs-built_in">this</span>);
-------------------------------
    <span class="hljs-built_in">this</span>.name = name || <span class="hljs-string">'Tom'</span>;
&#125;
--------------------------------------------------------------
(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> Super = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;; <span class="hljs-comment">// 新建一个"空"属性的构造函数Super -------------------------4</span>
    Super.prototype = Animal.prototype;  <span class="hljs-comment">// 将Animal.prototype拷贝一份出来 -------------------4</span>
    Cat.prototype = <span class="hljs-keyword">new</span> Super(); <span class="hljs-comment">// Cat的原型指向Super创建的实例对象（分身拷贝真身） ------------4</span>
    Cat.prototype.constructor = Cat;  <span class="hljs-comment">// 矫正constructor属性，不破坏原型链</span>
&#125;)();
--------------------------------------------------------------
<span class="hljs-comment">// Test Code</span>
<span class="hljs-keyword">var</span> cat1 = <span class="hljs-keyword">new</span> Cat();
<span class="hljs-keyword">var</span> cat2 = <span class="hljs-keyword">new</span> Cat()
<span class="hljs-built_in">console</span>.log(cat1.sleep===cat2.sleep) <span class="hljs-comment">// false --------------------------- 1</span>
<span class="hljs-built_in">console</span>.log(cat1.eat(<span class="hljs-string">'fish'</span>)); <span class="hljs-comment">// "Tom正在吃：fish" -------------------------- 2</span>
<span class="hljs-built_in">console</span>.log(cat1.eat===cat2.eat) <span class="hljs-comment">// true --------------------------------- 3</span>
<span class="hljs-built_in">console</span>.log(cat1.name); <span class="hljs-comment">// "Tom"</span>
<span class="hljs-built_in">console</span>.log(cat1.sleep()); <span class="hljs-comment">// "Tom正在睡觉"</span>
<span class="hljs-built_in">console</span>.log(cat1 <span class="hljs-keyword">instanceof</span> Animal); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(cat1 <span class="hljs-keyword">instanceof</span> Cat); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>较为推荐</p>
<h4 data-id="heading-21">寄生组合式继承和组合继承的区别在于这里：</h4>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> Super = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;;
    Super.prototype = Animal.prototype;
    Cat.prototype = <span class="hljs-keyword">new</span> Super();
    Cat.prototype.constructor = Cat;
&#125;)();

与

Cat.prototype = <span class="hljs-keyword">new</span> Animal();
Cat.prototype.constructor = Cat;

（相比于组合继承少了一份“真身”，可能是因为<span class="hljs-string">`垃圾回收机制`</span>吧）
（这也是为什么寄生组合式继承的核心步骤要放在一个<span class="hljs-function"><span class="hljs-keyword">function</span>里面的原因吧）
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">解释构造函数继承的传参原理</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//父类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Super</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">this</span>.sss=<span class="hljs-number">1</span>
&#125;
<span class="hljs-comment">//子类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Sub</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-comment">//arguments是Sub收到的参数，将这个参数传给Super</span>
Super.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>)
&#125;
<span class="hljs-comment">//实例</span>
sub = <span class="hljs-keyword">new</span> Sub()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Super.apply(this, arguments)这一句，将Super类作为一个普通函数来执行，但是Super类的this被换成了Sub类的this，Sub收到的参数也传给了Super
最后执行结果相当于sub.sss=1（这也就完成了继承）</p>
<h3 data-id="heading-23">class是ES6新增，是构造函数的语法糖</h3>
<p><a href="https://www.cnblogs.com/honkerzh/p/10270624.html" target="_blank" rel="nofollow noopener noreferrer">ES6 中 class 与构造函数的关系</a></p>
<h2 data-id="heading-24">参考文章</h2>
<ul>
<li><a href="https://juejin.cn/post/6844903717414633486" target="_blank">彻底弄懂JS原型与继承</a></li>
<li><a href="https://juejin.cn/post/6844904127344934926" target="_blank">一文读懂JS中类、原型和继承</a></li>
<li><a href="https://www.nowcoder.com/tutorial/96/7a253a443122467b8d022ca88d33ec62" target="_blank" rel="nofollow noopener noreferrer">JavaScript(一)面试宝典</a></li>
<li><a href="https://www.zhihu.com/question/22232912/answer/21392778" target="_blank" rel="nofollow noopener noreferrer">如何理解javascript中寄生组合式继承？</a></li>
</ul></div>  
</div>
            