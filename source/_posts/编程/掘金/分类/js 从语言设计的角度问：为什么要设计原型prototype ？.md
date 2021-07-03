
---
title: 'js 从语言设计的角度问：为什么要设计原型prototype ？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5675'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 04:39:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=5675'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">js从语言设计的角度问：为什么要设计原型prototype</h3>
<h4 data-id="heading-1">设计原型prototype的初心？</h4>
<p>从一个语言设计者的角度想一下，为什么要有原型? javascript 设计出原型prototype，想要解决什么问题呢？没有无缘无故的爱，也没有没有无缘无故的恨。不会觉得好玩，凭空产生的。对不！</p>
<p>Brendan Eich （JavaScript 之父）花了10天的时间设计出来，然后出于营销推广的目的，当时java 名气比较大，以java为前缀，伟大的javascript 诞生了。从此java 和 javascript 成了一辈子的好兄弟。哈哈。。。任何一门编程语言，都要解决一个问题：<code>共享/复用</code>，重要的事情说3遍，<code>(共享/复用) x 3</code>，同一个业务逻辑，同一个状态、行为javascript 你打算让我copy 3次吗？当然是不要。那么是借鉴其它语言的类，模块，包来解决吗？可能经过作者的权衡，天才的构思，原型prototype，就这样应运而生了</p>
<h4 data-id="heading-2">原型构成的2个关键角色？</h4>
<p>从语言设计的角度看，[[Prototype]]或者 <strong>proto</strong> 用来解决什么呢？prototype 是什么，主要是用来干嘛？这个得打电话给 Brendan Eich （JavaScript 之父），好好聊一下了。啥？，，，不记得号码了。好吧，我们从实现上去理解：</p>
<ul>
<li>[[Prototype]]或者 <strong>proto</strong>：是相对实例而言的，指向实例的原型，负责处理的是<code>指向关系</code>。</li>
<li>prototype：是相对构造函数而言，构造函数上的一个属性，负责处理的是<code>共享/复用</code>。 构造函数的prototype 称作 <code>原型对象</code>。</li>
</ul>
<blockquote>
<p>实例的原型是什么？构造函数的原型对象是什么？以这样去提问，对理解是有帮助的</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// 指定共享的属性/方法</span>
<span class="hljs-keyword">const</span> customPrototype = &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">refer</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">action</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125; &#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ancestor</span>(<span class="hljs-params"></span>)</span>&#123;&#125;

<span class="hljs-comment">// 指定构造函数的原型对象</span>
Ancestor.prototype = customPrototype

<span class="hljs-keyword">const</span> a = <span class="hljs-keyword">new</span> Ancestor()
<span class="hljs-keyword">const</span> b = <span class="hljs-keyword">new</span> Ancestor()

<span class="hljs-comment">// 看一下效果</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(a) === a.__proto__  <span class="hljs-comment">// true</span>

<span class="hljs-built_in">Object</span>.getPrototypeOf(a) === customPrototype <span class="hljs-comment">// true</span>

a.id === <span class="hljs-number">0</span> <span class="hljs-comment">// true</span>

a.id === b.id <span class="hljs-comment">// true</span>

b.action === a.action <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了降低理解的成本，先说明一下: Object.getPrototypeOf() 方法返回指定对象的原型（内部[[Prototype]]属性的值。)像[[Prototype]]这种格式，带2个中括号包围的，说明它是浏览器的内部属性。</p>
<h4 data-id="heading-3">分析一下代码</h4>
<ul>
<li><code>a.id === 0; a.id === b.id</code>：属性为0，共享同一属性</li>
<li><code>b.action === a.action</code>: 指向了同一个函数，共享同一方法</li>
<li><code>Object.getPrototypeOf(a) === customPrototype</code>：实例a的原型 customPrototype，等价于构造函数的原型对象</li>
</ul>
<blockquote>
<p>谈到原型就要有一个相对的概念，要明确[[Prototype]]或者 <strong>proto</strong> 的是处理关系。构造函数的prototype 处理共享/复用</p>
</blockquote>
<h4 data-id="heading-4">指定一个原型哪些方式？</h4>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// 方式一: 设置构造函数的 prototype </span>
<span class="hljs-keyword">const</span> customPrototype = &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">refer</span>: <span class="hljs-literal">true</span> &#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ancestor</span>(<span class="hljs-params"></span>)</span>&#123;&#125;

Ancestor.prototype = customPrototype

<span class="hljs-keyword">const</span> a = <span class="hljs-keyword">new</span> Ancestor()

<span class="hljs-comment">// 方式二：Object.create</span>
<span class="hljs-keyword">const</span> b = <span class="hljs-built_in">Object</span>.create(customPrototype)

<span class="hljs-comment">// 方式三：setPrototypeOf, 会引发性能问题，有兴趣的可点击文末的引用连接</span>
<span class="hljs-keyword">const</span> c = <span class="hljs-built_in">Object</span>.setPrototypeOf(&#123;&#125;,customPrototype)

<span class="hljs-comment">// 方式四：重新赋值 __prototype</span>
<span class="hljs-keyword">const</span> d = &#123;&#125;
d.__proto__ = customPrototype

<span class="hljs-comment">// 看一下效果</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(a) === <span class="hljs-built_in">Object</span>.getPrototypeOf(b) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(b) === <span class="hljs-built_in">Object</span>.getPrototypeOf(c) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(c) === <span class="hljs-built_in">Object</span>.getPrototypeOf(d) <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>有一点要注意：<strong>proto</strong>  不是EMCA规范，是浏览器作为宿主环境实现的非标准属性，IE 上不一定都提供。[[Prototype]], 在浏览器上不支持访问, 代码只能使用 <strong>proto</strong> 进行赋值操作，为了方便理解 <strong>proto</strong> 和 [[Prototype]], 可以理解成等价，不作过多的区分。</p>
<h4 data-id="heading-5">运行时改变原型会怎么样？</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> customPrototype = &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">refer</span>: <span class="hljs-literal">true</span> &#125;
<span class="hljs-keyword">const</span> anothePrototype = &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">refer</span>: <span class="hljs-literal">false</span> &#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ancestor</span>(<span class="hljs-params"></span>)</span>&#123;&#125;

Ancestor.prototype = customPrototype

<span class="hljs-keyword">const</span> a = <span class="hljs-keyword">new</span> Ancestor()

<span class="hljs-comment">// 运行时改变构造函数原型</span>
Ancestor.prototype = anothePrototype

<span class="hljs-keyword">const</span> b = <span class="hljs-keyword">new</span> Ancestor()

<span class="hljs-built_in">Object</span>.getPrototypeOf(a) === <span class="hljs-built_in">Object</span>.getPrototypeOf(b) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(a) === customPrototype <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(b) === anothePrototype <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 再改变一次</span>
<span class="hljs-built_in">Object</span>.setPrototypeOf(b,customPrototype)
<span class="hljs-built_in">Object</span>.getPrototypeOf(a) === <span class="hljs-built_in">Object</span>.getPrototypeOf(b) <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码可以得出：原型是可以在运行时重新指定的，b 实例也好，构造函数Ancestor也好，都可以动态指定。
只是在 new Ancestor() 调用了，使用 customPrototype 作为 b 实例的原型。</p>
<p>Object.setPrototypeOf 改变的是[[Prototype]]的值，Ancestor.prototype = anothePrototype 改变的是
构造函数的被使用 new 操作调用时，生成的实例链接的对象变成 anothePrototype。</p>
<h3 data-id="heading-6">原型链是怎么产生的？</h3>
<p>实例的原型是通过[[Prototype]]进行链接，可以理解成一个链表，一个节点指向上一个节点，直到尽头。前面我们已经知道实例的原型是可以在运行时改变的，那么原型链也是动态的。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> customPrototype = &#123; <span class="hljs-attr">level</span>: <span class="hljs-number">0</span> &#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ancestor</span>(<span class="hljs-params"></span>)</span>&#123;&#125;

Ancestor.prototype = customPrototype

<span class="hljs-keyword">const</span> a = <span class="hljs-keyword">new</span> Ancestor()

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A1</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

A1.prototype = a

a1 = <span class="hljs-keyword">new</span> A1()

<span class="hljs-comment">// 测试一下指向哪个原型</span>
a1.__proto__ === a <span class="hljs-comment">// true</span>
a1.__proto__.__proto__ === customPrototype <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 改变实例指向的原型</span>
<span class="hljs-built_in">Object</span>.setPrototypeOf(a1,customPrototype)

a1.__proto__ === a <span class="hljs-comment">// false</span>
a1.__proto__ === customPrototype <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 遍历整个原型链</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">prototypeChain</span>(<span class="hljs-params">instance</span>) </span>&#123;
  <span class="hljs-comment">// 没有原型可言</span>
  <span class="hljs-keyword">if</span>(instance === <span class="hljs-keyword">void</span> <span class="hljs-number">0</span> || instance === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> 
  &#125; 

  <span class="hljs-keyword">let</span> prototype = <span class="hljs-built_in">Object</span>.getPrototypeOf(instance)
  <span class="hljs-keyword">do</span> &#123;
    <span class="hljs-built_in">console</span>.log(prototype)
    prototype = <span class="hljs-built_in">Object</span>.getPrototypeOf(prototype)
  &#125; <span class="hljs-keyword">while</span>(prototype)
  <span class="hljs-built_in">console</span>.log(prototype)
&#125;

prototypeChain(a1)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">原型的生产流水线？</h3>
<p>new 调用构造函数发生了什么？constructor 设计的初衷是什么？了解设语言设计api的初衷，可以看buildint，初始化是怎么样的？</p>
<h4 data-id="heading-8">constructor 在哪里，主要处理什么事情？</h4>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ancestor</span>(<span class="hljs-params"></span>)</span>&#123;&#125;

<span class="hljs-keyword">const</span> obj = <span class="hljs-keyword">new</span> Ancestor()

<span class="hljs-comment">// 构造函数对象prototype 的一个属性</span>
Ancestor.prototype.constructor === obj.constructor <span class="hljs-comment">// true</span>
Ancestor.prototype.constructor === Ancestor <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(obj,<span class="hljs-string">'constructor'</span>) === <span class="hljs-literal">undefined</span> <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的3个等式，可以看出</p>
<ul>
<li>constructor：是构造函数原型对象prototype 的一个属性</li>
<li>constructor：指向构造函数自身</li>
<li>实例上的constructor，是通过继承得来的，访问的是构造函数原型对象prototype.constructor</li>
</ul>
<h4 data-id="heading-9">constructor 本质是用来说明实例是调用哪个构造函数生成</h4>
<p>在constructor哪里清楚啦，我们来看一下，它主要处理什么事情？</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ancestor</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Ancestor'</span>)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Descendant</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Descendant'</span>)
&#125;

Ancestor.prototype = &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">0</span> &#125;
Descendant.prototype = &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span> &#125;

Ancestor.prototype.constructor = Descendant

<span class="hljs-keyword">const</span> obj = <span class="hljs-keyword">new</span> Ancestor()

obj.constructor === Descendant <span class="hljs-comment">// true</span>
obj.id === <span class="hljs-number">1</span> <span class="hljs-comment">// false</span>
obj.id === <span class="hljs-number">0</span> <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Descendant 没有调用：说明原型对象 Ancestor.prototype.constructor 只是用来标记</li>
<li>obj.id === 0： 说明实例的原型是 Ancestor.prototype</li>
<li>obj.constructor === Descendant： 综上2点，可以得出 constructor 来自实例原型上的constructor</li>
</ul>
<p>从目前来看 <code>constructor 只实例原型上的为作构造函数标记，用来说明实例的类型</code>,再来验证一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ancestor</span>(<span class="hljs-params"></span>)</span>&#123;&#125;

Ancestor.prototype.constructor = <span class="hljs-string">'mark type'</span>

<span class="hljs-keyword">const</span> obj = <span class="hljs-keyword">new</span> Ancestor()

obj.constructor === <span class="hljs-string">'mark type'</span> <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此，可以明确constructor 可以作为一个字符串，不是一定要作为函数。主要是标记实例的类型，是被哪个构造函数生成的。当然注意的是可以随意改变的，那么用 constructor 并不准确的。</p>
<h4 data-id="heading-10">new 发生了什么？</h4>
<p>new 以这种方式调用构造函数会执行如下操作：</p>
<p>(1)在内存中创建一个新对象。
(2)这个新对象内部的[[Prototype]]特性被赋值为构造函数的prototype属性。
(3)构造函数内部的this被赋值为这个新对象（即this指向新对象）。
(4)执行构造函数内部的代码（给新对象添加属性）。
(5)如果构造函数返回非空对象，则返回该对象；否则，返回刚创建的新对象</p>
<p>这个流程是一定这样的吗？会受到其它其它因素的影响吗？带着这些疑问，我们用代码的求证。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ancestor</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Descendant</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 情况一：返回一个对象</span>
  <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span> &#125;
&#125;

<span class="hljs-comment">// 情况二：原型对象是基本数据类型：string, number, undefined, null</span>
Ancestor.prototype = <span class="hljs-literal">null</span>

Descendant.prototype = &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">0</span> &#125;

<span class="hljs-keyword">const</span> a = <span class="hljs-keyword">new</span> Ancestor()
<span class="hljs-keyword">const</span> b = <span class="hljs-keyword">new</span> Descendant()

<span class="hljs-comment">// 测试等式</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(a) === <span class="hljs-literal">null</span> <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(a) === <span class="hljs-built_in">Object</span>.prototype <span class="hljs-comment">// true</span>
b.id === <span class="hljs-number">0</span> <span class="hljs-comment">// false</span>
b.id === <span class="hljs-number">1</span> <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在用new 操作符调用构造函数的过程中，有2个细节要注意</p>
<ul>
<li>
<p>第（2）步的 [[Prototype]], 会判断原型对象数据类型，如果是基本的数据类型（string,number, null, undefined, 布尔值,Symbol), 那么原型对象不会被链接。 [[Prototype]] 赋值为 Object.prototype</p>
</li>
<li>
<p>构造函数的return 返回值也是要分情况，如果是返回的是引用数据类型，第（3）步的this被丢弃，返回值作为实例值。
没有返回值或者返回的是基本数据类型，则返回的是 this(也就是新对象)</p>
</li>
</ul>
<h3 data-id="heading-11">如何检测原型关系？</h3>
<p>原型链可以理解成一个链表，进行搜索任务时，是一个节点一个节点递归的向上查找：1.找到并返回 2.到达最后一个节点，没有找到退出。</p>
<p>要判断一个实例是不是某一个构造函数生成的，可以使用instanceof,该运算符用于检测构造函数的 prototype 属性是否出现在某个实例对象的原型链上。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Ancestor</span>(<span class="hljs-params"></span>)</span>&#123;&#125;

<span class="hljs-keyword">let</span> a = <span class="hljs-keyword">new</span> Ancestor()


<span class="hljs-comment">// 等式一</span>
a <span class="hljs-keyword">instanceof</span> Ancestor === <span class="hljs-literal">true</span> <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 等式二为真：因为实例a原型链找到了构造函数Ancestor的原型对象</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(a) === Ancestor.prototype <span class="hljs-comment">// true</span>

Ancestor.prototype = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>()

a = <span class="hljs-keyword">new</span> Ancestor()

a <span class="hljs-keyword">instanceof</span> Ancestor <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 等式二</span>
a <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span> <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 等式二为真：因为实例a原型链找到了构造函数Array的原型对象</span>
a.__proto__.__proto__ === <span class="hljs-built_in">Array</span>.prototype <span class="hljs-comment">// true</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Descendant</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span> &#125;
&#125;

<span class="hljs-keyword">const</span> b = <span class="hljs-keyword">new</span> Descendant()

<span class="hljs-comment">// 等式不成立</span>
<span class="hljs-comment">// 构造函数 Descendant 返回 &#123; id: 1 &#125;， 这样 Descendant.prototype原型对象，没有进行链接</span>
b <span class="hljs-keyword">instanceof</span> Descendant <span class="hljs-comment">// false</span>


<span class="hljs-comment">// instanceof 操作符限制</span>

<span class="hljs-comment">// 情况一：包装对象</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(<span class="hljs-number">3</span>) === <span class="hljs-built_in">Number</span>.prototype <span class="hljs-comment">// true</span>
<span class="hljs-number">3</span> <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Number</span> <span class="hljs-comment">// false</span>

<span class="hljs-comment">// 情况二：instanceof 和多全局对象(例如：多个 frame 或多个 window 之间的交互)</span>

<span class="hljs-comment">// 情况三：当然还会有一些情况，可以从instanceof 判断的依据去想想</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">内置对象原型关系图?</h3>
<p>浏览器会内置哪些对象？Object 是比较高频出现的，Array，Date 也可能经常用到。Function 可能并没有经常出现，但是在框架可以经常看到他的踪迹。Function 才是内置对象的<code>核心枢纽</code>，那我们一起看看Function 有什么特别?</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// 特别之处一：Function 的原型对象是一个 ƒ () &#123; [native code] &#125;</span>
<span class="hljs-comment">// 对的，它是一个函数, 就这么特别</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Function</span>.prototype === <span class="hljs-string">'function'</span> <span class="hljs-comment">// true</span>
<span class="hljs-comment">// Object的原型对象是一个 对象</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Object</span>.prototype === <span class="hljs-string">'object'</span> <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 特别之处二：Function 作为一个实例来看，那的原型是什么？</span>
<span class="hljs-comment">// 对的，Function 的原型是它自身的原型对象, 也就是 Function.prototype</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(<span class="hljs-built_in">Function</span>) === <span class="hljs-built_in">Function</span>.prototype <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>看起来很特别了，那么我们再看看Function.prototype 到底是什么？</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// Function.prototype 的 [[Prototype]] 是 Object.prototype</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(<span class="hljs-built_in">Function</span>.prototype) === <span class="hljs-built_in">Object</span>.prototype <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 和其它构造函数一样，指向自身</span>
<span class="hljs-built_in">Function</span>.prototype.constructor === <span class="hljs-built_in">Function</span> <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的可以知道 Function.prototype 的原型是 Object.prototype，但是，还是没有找到更加明确的信息。这个时候可以查看规范，<a href="https://262.ecma-international.org/5.1/#sec-15.3.4" target="_blank" rel="nofollow noopener noreferrer">官方链接</a></p>
<p>The Function prototype object is itself a Function object (its [[Class]] is "Function") that, when invoked, accepts any arguments and returns undefined.</p>
<p>The value of the [[Prototype]] internal property of the Function prototype object is the standard built-in Object prototype object (15.2.4). The initial value of the [[Extensible]] internal property of the Function prototype object is true.</p>
<p>The Function prototype object does not have a valueOf property of its own; however, it inherits the valueOf property from the Object prototype Object.</p>
<p>The length property of the Function prototype object is 0.</p>
<p>翻译一下：Function 原型对象本身就是一个 函数对象（它的 [[Class]] 是“Function”，是可调用的），当被调用时，它接受任意参数并返回 undefined。</p>
<p>Function 原型对象的 [[Prototype]] 内部属性的值是标准的内置 Object.prototype， Function 原型对象的 [[Extensible]] 内部属性的初始值为 true。</p>
<p>Function 原型对象没有自己的valueOf 属性；然而它从 Object.prototype 继承了 valueOf属性。需要注意的是valueOf 是一个函数，翻译为 valueOf 方法更贴切。</p>
<p>Function 原型对象的长度属性为 0，也就说 Function.prototype 作为函数调用，他们参数个数是0;</p>
<p>综合上面的我们做一个总结：</p>
<ul>
<li>Function.prototype： Function 的原型对象是一个函数；作为函数调用，接受任意参数，并返回 undefined</li>
<li>Function 的原型：是指向 Function.prototype，这也是原型链 关系出现<code>环</code>的关键，就是常说的 <code>绕</code></li>
<li>Function 的原型对象的原型： Function.<strong>proto</strong>.<strong>proto</strong> === Object.prototype 就这样，Function 和 Object 产生了关系</li>
</ul>
<h4 data-id="heading-13">Function 和 Object 的环形关系</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Function 的原型是 Function 的原型对象这个是环产生的原因</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(<span class="hljs-built_in">Function</span>) === <span class="hljs-built_in">Function</span>.prototype <span class="hljs-comment">// true</span>
<span class="hljs-comment">// Object 的原型是Function 原型对象</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(<span class="hljs-built_in">Object</span>) === <span class="hljs-built_in">Function</span>.prototype <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(<span class="hljs-built_in">Function</span>.prototype) === <span class="hljs-built_in">Object</span>.prototype <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(<span class="hljs-built_in">Object</span>.prototype) === <span class="hljs-literal">null</span> <span class="hljs-comment">// true</span>


<span class="copy-code-btn">复制代码</span></code></pre>
<p>从实例来看，我们讲原型是什么？从构造函数来看，我们讲的是原型对象，这样就不会出现绕的情况。从语言设计的角度，他们出现都是为了解决一些问题，回顾前面讲的。我们再来梳理一下，上面的为什么要这样设计</p>
<ul>
<li>
<p>Function.prototype: 更多的是作为函数可以被调用，作为所有函数的鼻祖，最初始的状态，prototype 本身就有雏形的意思。</p>
</li>
<li>
<p>Object.prototype: 更多的是作为对象的原始公用属性和方法提供者，本身承载就是<code>共享/复用</code>职责</p>
</li>
<li>
<p>null：是一切原型的雏形，最纯粹，没有任何方法，属性。</p>
</li>
<li>
<p>Object 是一个函数，为获得<code>可调用</code>这个特征，把[[Prototype]] 指向 Function.prototype 很好理解</p>
</li>
<li>
<p>Function 是一个可调用的对象，注意是对象，原型链必须有一节点，把[[Prototype]] 指向 Object.prototype</p>
</li>
<li>
<p>如果 Function.<strong>proto</strong> 指向 null 会怎么样？那 Function 就没有办法拥有 对象的表现了，不能称为是一个可调用对象了。因为要是函数，又要是对象，一开始 Object.prototype， Function.prototype 是分开的，要达到这样的一个效果，就要有一个交叉点。这样Function.<strong>proto</strong> 直接指向身原型，这个方案可行，也挺完美的。当然也可以增加一个节点，再指向Object.prototype 也是可以，但这样很啰嗦了。</p>
</li>
</ul>
<p>曾经也想过一个问题：先有Function.prototype 还是先Object.prototype。其实这个问题是不存在的，从上面来看。先有哪个都是可以的，通过[[Prototype]]链接起来就可以。先有什么，后有什么，本身就有时间的这个设定条件，时间24h本身就是人类创造出来的，是一个虚拟的概念。就好比先有鸡，还是先有蛋。鸡和蛋，本质上就是物质，和时间没有关系。试想生物技术足够发达，直接分别生产出鸡和蛋，你还会问先有哪个吗？</p>
<p>结束语</p>
<hr>
<p>以上是个人对原型的一些理解，如有错漏，欢迎指出纠正。从语言的设计的角度去看，更多从api 的设计的初衷，使用的角度去看，希望不要造成误解，仅仅是个人的一些猜测。</p>
<h3 data-id="heading-14">参与资料</h3>
<ul>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf" target="_blank" rel="nofollow noopener noreferrer">Object.setPrototypeOf</a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/GetPrototypeOf" target="_blank" rel="nofollow noopener noreferrer">Object.getPrototypeOf</a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/instanceof" target="_blank" rel="nofollow noopener noreferrer">instanceof</a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/new.target" target="_blank" rel="nofollow noopener noreferrer">new 操作符</a></p>
</li>
</ul></div>  
</div>
            