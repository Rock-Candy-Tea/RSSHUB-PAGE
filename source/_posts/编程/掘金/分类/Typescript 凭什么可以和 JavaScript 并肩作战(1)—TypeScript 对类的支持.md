
---
title: 'Typescript 凭什么可以和 JavaScript 并肩作战(1)—TypeScript 对类的支持'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/487fca0f0aed4a4d8121b0165ac4f922~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 23:25:54 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/487fca0f0aed4a4d8121b0165ac4f922~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<blockquote>
<p>为了分享此篇文章，个人做了大量的工作，所以未经本人同意，请勿转载，在此表示感谢！</p>
</blockquote>
<blockquote>
<p>阅读提示:对 Typescript 中类继承(extends)和实现(implement)的区分给出解释和说明。</p>
</blockquote>
<p>大家可能都是认为 Typescript 是 JavaScript 的超集(superset)，可以编译为 Javascript。 Typescript 和 JavaScript 具有相同的能力，大家可能认为 Typescript 最终编译为 JavaScript，Typescript 作为 JavaScript 的超集，地位不断提升，算是比较很成功的 JavaScript 的超级，能够和其修饰的 JavaScript 位于同一排行榜，可见 TypeScript 有其独到之处。</p>
<p>在面向对象编程中，最核心的就是 class 概念，在 ES2015 中，javascript 已经引入的 class 关键词。不过今天我们来看一看 typescript 中如何对 JavaScript 的类的补充。</p>
<p>TypeScript 提供了对 ES2015 中引入的 class 关键词的完全支持。与其他 JavaScript 语言功能一样，TypeScript 增加了类型注释和其他语法，允许你表达类和其他类型之间的关系。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/487fca0f0aed4a4d8121b0165ac4f922~tplv-k3u1fbpfcp-watermark.image" alt="007.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">定义类</h3>
<p>类是将数据结构和一些可以操作和访问数据的行为组织在一起，具有一定封闭性。并且提供方法供用户访问和操作数据。</p>
<h4 data-id="heading-1">定义一个类</h4>
<p>下面我们定义一个类 <code>class</code> 并不含任何内容。。虽然会涉及到用 TypeScript 创建类的一些基本方面，但其语法大多与用 JavaScript 创建类时相同。所以本将重点放在介绍 TypeScript 中的一些与 JavaScript 不同之处。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Tut</span></span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">类的属性</h4>
<p>在类里面可以声明属性并指定类型，默认属性为 <code>public</code> 也就是可读写的属性，没有给出任何修饰符情况下，默认属性修饰符为 <code>public</code>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// class Tut&#123;&#125;</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Tut</span></span>&#123;
    <span class="hljs-attr">title</span>:<span class="hljs-built_in">string</span>;
    lesson:<span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">const</span> machine_learning_tut = <span class="hljs-keyword">new</span> Tut();
machine_learning_tut.title = <span class="hljs-string">"machine leaerning tut"</span>;
machine_learning_tut.lesson = <span class="hljs-number">12</span>;

<span class="hljs-built_in">console</span>.log(machine_learning_tut) <span class="hljs-comment">//Tut &#123; title: 'machine leaerning tut', lesson: 12 &#125;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>属性声明时为属性指定类型是可选的，如果没有指定类型属性类型为 <code>any</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Tut</span></span>&#123;
    title = <span class="hljs-string">""</span>;
    lesson = <span class="hljs-number">0</span>;
&#125;

<span class="hljs-keyword">const</span> machine_learning_tut = <span class="hljs-keyword">new</span> Tut();
machine_learning_tut.title = <span class="hljs-string">"machine leaerning tut"</span>;
<span class="hljs-comment">//error TS2322: Type 'string' is not assignable to type 'number'.</span>
machine_learning_tut.lesson = <span class="hljs-string">"12"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里给属性进行进行了初始化，编译器会根据属性的初始值推断该属性类型，如果随后对该属性赋值不同于初始化值类型的值就会包编译错误，无法通过编译。</p>
<blockquote>
<p>如果在编译时指定 <code>strictPropertyInitialization</code> 为 <code>true</code> 这需要在构造函数初始化变量时给出初值。</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"compilerOptions"</span>: &#123;
      ...
      <span class="hljs-attr">"strictNullChecks"</span>:<span class="hljs-literal">true</span>,
      <span class="hljs-attr">"strictPropertyInitialization"</span>:<span class="hljs-literal">true</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Greeter</span></span>&#123;
    <span class="hljs-attr">name</span>:<span class="hljs-built_in">string</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 <code>"strictPropertyInitialization":true</code> 而没有定义 <code>Greeter</code> 对于 <code>name</code> 属性给出初值编译时则会抛出下面错误信息。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx">
Property <span class="hljs-string">'name'</span> has no initializer and is not definitely assigned <span class="hljs-keyword">in</span> the <span class="hljs-title">constructor</span>.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请注意， 因为<code>"strictPropertyInitialization":true</code>该字段需要在构造函数本身中初始化。TypeScript 不会分析你从构造函数中调用的方法来检测初始化，因为子类类可能会覆盖这些方法而无法初始化成员。</p>
<p>如果打算在构造函数以外为属性赋值，可以使用确定的赋值断言操作符(definite assignment assertion operator)！。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Greeter</span></span>&#123;
    name!:<span class="hljs-built_in">string</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Employee</span></span>&#123;
    <span class="hljs-attr">name</span>:<span class="hljs-built_in">string</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name:<span class="hljs-built_in">string</span>,<span class="hljs-keyword">public</span> age:<span class="hljs-built_in">number</span></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name;
    &#125;
&#125;

<span class="hljs-keyword">const</span> mike = <span class="hljs-keyword">new</span> Employee(<span class="hljs-string">"mike"</span>,<span class="hljs-number">28</span>)
<span class="hljs-built_in">console</span>.log(mike.age)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">私有属性</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VideoTut</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Tut</span></span>&#123;
    <span class="hljs-keyword">private</span> title:<span class="hljs-built_in">string</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">title:<span class="hljs-built_in">string</span></span>)</span>&#123;
        <span class="hljs-comment">//'super' must be called before accessing 'this' in the constructor of a derived class.ts(17009)</span>
        <span class="hljs-comment">// console.log(this.category)</span>
        <span class="hljs-built_in">super</span>()
        <span class="hljs-built_in">this</span>.title = title
    &#125;
&#125;

<span class="hljs-keyword">const</span> videoTut = <span class="hljs-keyword">new</span> VideoTut(<span class="hljs-string">"machine learning"</span>);
<span class="hljs-comment">// Property 'title' is private and only accessible within class 'VideoTut'</span>
<span class="hljs-built_in">console</span>.log(videoTut.title)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当将 <code>title</code> 用 <code>private</code> 修饰符修饰后该属性就成为了私有属性，外界无法访问。当试图访问时，就会抛出<code>Property 'title' is private and only accessible within class 'VideoTut'</code>错误。</p>
<h4 data-id="heading-4">只读属性(readonly)</h4>
<p>如果类中属性前面有 <code>readonly</code> 修饰符，该属性值就只能在类的构造函数里进行修改。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Employee</span></span>&#123;
    readonly position:string = <span class="hljs-string">"employee"</span>
    name!:string;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name:string,otherPosition?:string</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(otherPosition !== <span class="hljs-literal">undefined</span>)&#123;
            <span class="hljs-built_in">this</span>.position = otherPosition;
            <span class="hljs-built_in">this</span>.name = name;
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">intro</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">//Cannot assign to 'name' because it is a read-only property.ts(2540)</span>
        <span class="hljs-built_in">this</span>.position = <span class="hljs-string">"overide name field value"</span>
    &#125;
&#125;

<span class="hljs-keyword">const</span> mike = <span class="hljs-keyword">new</span> Employee(<span class="hljs-string">"mike"</span>);
<span class="hljs-comment">//Cannot assign to 'position' because it is a read-only property.ts(2540)</span>
mike.position = <span class="hljs-string">"overide name field valu"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">构造函数(Constructors)</h4>
<p>类构造函数与函数非常相似。可以添加带有类型注释的参数、默认值和重载。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Tut</span></span>&#123;
    <span class="hljs-attr">title</span>:<span class="hljs-built_in">string</span>;
    subTitle:<span class="hljs-built_in">string</span>;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">title:<span class="hljs-built_in">string</span>,subTitle:<span class="hljs-built_in">string</span></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.title = title;
        <span class="hljs-built_in">this</span>.subTitle = subTitle
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构造函数重载，虽然构造函数也是函数，所以构造函数的重载也就是复合函数的重载。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Tut</span></span>&#123;
    <span class="hljs-keyword">public</span> title:<span class="hljs-built_in">string</span>;
    <span class="hljs-keyword">public</span> subTitle:<span class="hljs-built_in">string</span>;

    <span class="hljs-title">constructor</span>(<span class="hljs-params"></span>);
    <span class="hljs-title">constructor</span>(<span class="hljs-params">title:<span class="hljs-built_in">string</span></span>);
    <span class="hljs-title">constructor</span>(<span class="hljs-params">title:<span class="hljs-built_in">any</span>,subTitle?:<span class="hljs-built_in">any</span></span>);
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">title?:<span class="hljs-built_in">string</span>,subTitle?:<span class="hljs-built_in">string</span></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.title = title;
        <span class="hljs-built_in">this</span>.subTitle = subTitle;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae8d86ff13014c86971f1355afad2657~tplv-k3u1fbpfcp-watermark.image" alt="010.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>类的构造函数签名和函数签名之间只有一些区别。</p>
<ul>
<li>构造函数不能有类型参数--这属于外层类的声明，有关这部分内容将在后面介绍。</li>
<li>构造函数不能有返回类型注释，构造函数将返回类的实例类型。</li>
</ul>
<h4 data-id="heading-6">Super 调用</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Tut</span> </span>&#123;
    <span class="hljs-attr">category</span>:<span class="hljs-built_in">string</span> =<span class="hljs-string">"programming"</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VideoTut</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Tut</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">//'super' must be called before accessing 'this' in the constructor of a derived class.ts(17009)</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.category)
        <span class="hljs-built_in">super</span>()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里<code>VideoTut</code> 继承了</p>
<h4 data-id="heading-7">类的方法</h4>
<p>在类内部定义函数被称为方法，方法可以使用与函数相同，并无明显区别。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VideoTut</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Tut</span></span>&#123;
    <span class="hljs-keyword">private</span> title:<span class="hljs-built_in">string</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">title:<span class="hljs-built_in">string</span></span>)</span>&#123;
        <span class="hljs-comment">//'super' must be called before accessing 'this' in the constructor of a derived class.ts(17009)</span>
        <span class="hljs-comment">// console.log(this.category)</span>
        <span class="hljs-built_in">super</span>();
        <span class="hljs-built_in">this</span>.title = title;
    &#125;

    description():<span class="hljs-built_in">string</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`title: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.title&#125;</span>`</span>
    &#125;
&#125;


<span class="hljs-keyword">const</span> videoTut = <span class="hljs-keyword">new</span> VideoTut(<span class="hljs-string">"machine learning"</span>);
videoTut.description()<span class="hljs-comment">//title: machine learning</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/485c17ce7b0c48299cb1b49f2f4c6f39~tplv-k3u1fbpfcp-watermark.image" alt="008.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">getters/setters</h4>
<p>通过定义 set/get 方法我们可以设置一个属性访问设置，通过 set/get 外界可以访问或者修改一些类私有属性，但是无法修改修饰为 <code>readonly</code> 的属性。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Employee</span></span>&#123;
    <span class="hljs-keyword">private</span> _name:<span class="hljs-built_in">string</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name:<span class="hljs-built_in">string</span>,<span class="hljs-keyword">public</span> age:<span class="hljs-built_in">number</span></span>)</span>&#123;
        <span class="hljs-built_in">this</span>._name = name;
    &#125;
    <span class="hljs-keyword">get</span> <span class="hljs-title">name</span>()&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._name;
    &#125;
    <span class="hljs-keyword">set</span> <span class="hljs-title">name</span>(<span class="hljs-params">newName:<span class="hljs-built_in">string</span></span>)&#123;
        <span class="hljs-built_in">this</span>._name = newName;
    &#125;
&#125;

<span class="hljs-keyword">const</span> mike = <span class="hljs-keyword">new</span> Employee(<span class="hljs-string">"mike"</span>,<span class="hljs-number">28</span>)
<span class="hljs-built_in">console</span>.log(mike.name)<span class="hljs-comment">//mike</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>TypeScript 对访问器有一些特殊的推理规则。</p>
<ul>
<li>如果存在get，但没有set，则该属性自动是 readonly，如果在定义属性值已经指定了 <code>readonly</code> 则只有 <code>set</code> 方法</li>
<li>如果没有指定<code>setter</code>参数的类型，将从<code>getter</code>的返回类型中推断出来</li>
<li>获取器和设置器必须有相同的成员可见性</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da76673c928a43a3abe33df283b0dc1d~tplv-k3u1fbpfcp-watermark.image" alt="006.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">继承和实现</h3>
<h4 data-id="heading-10">继承(extends)</h4>
<p>在大多数基于类的面向对象语言中，继承是一种机制，其中一个对象获得了父对象的所有属性和行为。继承允许程序员：创建建立在现有类之上的类</p>
<h4 data-id="heading-11">实现(implements)</h4>
<p>可以用 <code>implements</code> 语句去实现一个类，编译过程会检查实现了 <code>CanDoSomethingInterface</code> 接口的类 <code>Developer</code> 是否满足实现接口要求。如果没有实现接口定义的内容，编译过程就会提示错误。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3f6ff8f09a74cd399849868114692a6~tplv-k3u1fbpfcp-watermark.image" alt="005.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> CanDoSomethingInterface&#123;
    canDoSomething():<span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Employee</span></span>&#123;
    <span class="hljs-keyword">private</span> _name:<span class="hljs-built_in">string</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name:<span class="hljs-built_in">string</span>,<span class="hljs-keyword">public</span> age:<span class="hljs-built_in">number</span></span>)</span>&#123;
        <span class="hljs-built_in">this</span>._name = name;
    &#125;
    <span class="hljs-keyword">get</span> <span class="hljs-title">name</span>()&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._name;
    &#125;
    <span class="hljs-keyword">set</span> <span class="hljs-title">name</span>(<span class="hljs-params">newName:<span class="hljs-built_in">string</span></span>)&#123;
        <span class="hljs-built_in">this</span>._name = newName;
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Developer</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Employee</span> <span class="hljs-title">implements</span> <span class="hljs-title">CanDoSomethingInterface</span></span>&#123;

    canDoSomething():<span class="hljs-built_in">void</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> can write some code`</span>)
    &#125;
&#125;

<span class="hljs-keyword">const</span> mike = <span class="hljs-keyword">new</span> Developer(<span class="hljs-string">"mike"</span>,<span class="hljs-number">28</span>)
<span class="hljs-comment">// mike.name = "tony"</span>
<span class="hljs-comment">// console.log(mike.name)</span>
mike.canDoSomething() <span class="hljs-comment">//mike can write some code</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过继承，子类拥有其父类的所有属性和方法，可以覆写(实现)父类方法，也可以在父类基础扩展一些属性和方法。</p>
<h4 data-id="heading-12">可以实现多个接口</h4>
<pre><code class="hljs language-js copyable" lang="js">interface Sendable&#123;
    send():<span class="hljs-keyword">void</span>;
&#125;

interface Receivable&#123;
    receive():<span class="hljs-keyword">void</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EMail</span> <span class="hljs-title">implements</span> <span class="hljs-title">Sendable</span>,<span class="hljs-title">Receivable</span></span>&#123;
    send():<span class="hljs-keyword">void</span>&#123;

    &#125;
    receive():<span class="hljs-keyword">void</span>&#123;
        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于一个类可以实现多个接口，上面 <code>EMail</code> 实现了 <code>Sendable</code>和<code>Receivable</code> 接口。看似接口实现和类继承很相似，但是这是两个不同的东西，首先接口更加抽象，很多语言将接口用 <code>contract</code> ，也是可以理解为类型，是一种基于行为或者数据的类型约束，或者契约，这个契约可以便于不同事物联系起来。</p>
<p>重要的是要明白， <code>implements</code> 子句只是检查类是否可以被当作接口类型，也就是检查该类是否实现了接口的方法。但不会改变类的类型或其方法。一个常见的错误来源是认为 <code>implements</code> 子句会改变类的类型。</p>
<p>在这个例子中，我们也许期望<code>s</code>的类型会受到 <code>check</code>的<code>name: string</code>参数的影响。其实不然--实现子句并没有改变类主体的检查方式或其类型的推断。</p>
<p>同样地，实现一个带有可选属性的接口并不能创建该属性。</p>
<h4 data-id="heading-13">覆写方法</h4>
<p>子类也可以覆写基类的一个字段或属性。可以使用 super.语法来调用基类的方法。<code>TypeScript</code>要求子类始终是其基类的一个子类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Employee</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">intro</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"I am employee"</span>);
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Developer</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Employee</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">intro</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">super</span>.intro();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"I'm a developer"</span>)
  &#125;
&#125;

<span class="hljs-keyword">const</span> mike = <span class="hljs-keyword">new</span> Developer()
mike.intro()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子类需要准寻其基类契约，所以子类可以作为基类类型来使用。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Employee</span></span>&#123;
        <span class="hljs-function"><span class="hljs-title">intro</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"I am employee"</span>);
        &#125;
    &#125;

    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Developer</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Employee</span></span>&#123;
        <span class="hljs-function"><span class="hljs-title">intro</span>(<span class="hljs-params">name?:string</span>)</span>&#123;
            <span class="hljs-keyword">if</span>(name == <span class="hljs-literal">undefined</span>)&#123;
                <span class="hljs-built_in">super</span>.intro();
            &#125;<span class="hljs-keyword">else</span>&#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`I'm a developer and my name is <span class="hljs-subst">$&#123;name&#125;</span>`</span>)
            &#125;
            
            
        &#125;
    &#125;

    <span class="hljs-keyword">const</span> mike:Developer = <span class="hljs-keyword">new</span> Developer()
    mike.intro(<span class="hljs-string">"mike"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在子类实现 <code>intro</code> 方法时没有遵循父类对 <code>intro</code>方法定义就是抛出错误。</p>
<pre><code class="hljs language-ts copyable" lang="ts">intro(name:<span class="hljs-built_in">string</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts">Property <span class="hljs-string">'intro'</span> <span class="hljs-keyword">in</span> <span class="hljs-keyword">type</span> <span class="hljs-string">'Developer'</span> is not assignable to the same property <span class="hljs-keyword">in</span> base <span class="hljs-keyword">type</span> <span class="hljs-string">'Employee'</span>.
  Type <span class="hljs-string">'(name: string) => void'</span> is not assignable to <span class="hljs-keyword">type</span> <span class="hljs-string">'() => void'</span>.ts(<span class="hljs-number">2416</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64a97f1e819f46018bc02bfca57762c1~tplv-k3u1fbpfcp-watermark.image" alt="011.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">初始化顺序</h4>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Tut</span></span>&#123;
        level = <span class="hljs-string">"begin"</span>
        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`level: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.level&#125;</span>`</span>)
        &#125;
    &#125;

    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MachineLearningTut</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Tut</span></span>&#123;
        level = <span class="hljs-string">"advance"</span> 
    &#125;

    <span class="hljs-keyword">const</span> tut = <span class="hljs-keyword">new</span> MachineLearningTut()
    <span class="hljs-comment">// level: begin</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照 JavaScript 的定义，类初始化的顺序是如何进行的。</p>
<ul>
<li>初始化基类的字段被</li>
<li>执行基类构造函数</li>
<li>初始化子类的字段</li>
<li>执行子类构造函数</li>
</ul>
<p>这意味着基类构造函数在自己的构造函数中看到了基类的 name 值而不是子类的 name，因为子类的字段初始化还没有运行。</p></div>  
</div>
            