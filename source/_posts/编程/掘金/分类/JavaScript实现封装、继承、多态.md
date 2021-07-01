
---
title: 'JavaScript实现封装、继承、多态'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9397820088db45c39ad4103a7c29d32c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 20:45:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9397820088db45c39ad4103a7c29d32c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">JavaScript实现封装、继承、多态</h2>
<h2 data-id="heading-1">前景提要：</h2>
<p>因为疫情原因，提前出来找工作实习，到今天差不多一年（Vue7个月、React三个多月），终于由前端实习生转变到一名前端工程师啦！！！哈哈哈</p>
<p>为了奖励自己 分享一篇自己最近对面向对象学习的总结。卷起来！</p>
<p>曾在面试过程中遇到请讲述React的class和hooks的区别。</p>
<p>答： function是面向过程编程，class是面向对象编程（也是基于面向过程的面向对象编程）</p>
<p>举个 🌰 ：</p>
<p>面向过程： 我需要找一个女盆友：我需要做什么事呢？ 之前dy流行的背景音乐---始换发型、改变穿衣风格（ins风、oversize...）、自律（自驱动学习、撸铁）、早睡。整个是一个过程依次执行。</p>
<p>面向对象：比如进入一个交友社区，上面发布了有以下交友单 ⬇</p>
<p>一： 1. 性别♂、 2. 胖胖的、 3.高高的</p>
<p>二： 1. 身材好的、 2. 程序员、 3. 帅帅的</p>
<p>嗯，这个就给予了我自己进行选择：它内部已经给我把清单列出来，我按需执行就完事了。</p>
<p>我选择第二个，那么就根据上面的要求依次执行---> 首先拥有健康的身体、学会敲代码、...</p>
<p>面向对象编程也可以称为基于面向过程的。从 🌰 上看，面向对象也离不开面向过程。</p>
<h2 data-id="heading-2">ES5构造函数 和 ES6类的区别</h2>
<h3 data-id="heading-3">ES5 构造函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, height</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name
        <span class="hljs-built_in">this</span>.age = age
        <span class="hljs-built_in">this</span>.height = height
        <span class="hljs-built_in">this</span>.doing = <span class="hljs-function">() =></span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i am coding!'</span>)
        &#125;
        <span class="hljs-built_in">this</span>.info = <span class="hljs-function">() =></span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`hello, i am <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>, i am <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span> year old .`</span>)
        &#125;
&#125;
<span class="hljs-keyword">var</span> echo = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'echo'</span>, <span class="hljs-number">6</span>, <span class="hljs-number">180</span>)
<span class="hljs-keyword">var</span> xiaoming = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'小明'</span>, <span class="hljs-number">1</span>, <span class="hljs-number">175</span>)
echo.doing() <span class="hljs-comment">//i am coding!</span>
echo.info() <span class="hljs-comment">//hello, i am echo, i am 6 year old .</span>
xiaoming.doing() <span class="hljs-comment">//i am coding!</span>
xiaoming.info() <span class="hljs-comment">//hello, i am 小明, i am 1 year old .</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">ES6 Class</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>&#123;
        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age</span>)</span> &#123;
            <span class="hljs-built_in">this</span>.name = name;
                <span class="hljs-built_in">this</span>.age = age;
        &#125;
        <span class="hljs-function"><span class="hljs-title">info</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`name: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> ; age: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>`</span>)
        &#125;
&#125;
<span class="hljs-keyword">const</span> dog = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'狗'</span>, <span class="hljs-number">2</span>)
<span class="hljs-keyword">const</span> cat = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'猫'</span>, <span class="hljs-number">1</span>)
dog.info() <span class="hljs-comment">//name: 狗 ; age: 2</span>
cat.info() <span class="hljs-comment">//name: 猫 ; age: 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据上面的对比：可以看出用构造函数和class都能实现相同的效果</p>
<blockquote>
<p>小结</p>
</blockquote>
<ol>
<li>类的声明没有提升、和函数是不同的</li>
<li>同一个类不能被重复定义（'Identifier 'XXX' has already been declared'），而函数则是下面的会覆盖上一个函数</li>
<li>类也可以看作构造函数的一个语法糖</li>
</ol>
<h2 data-id="heading-5">面向对象的思想. 封装、继承、多态</h2>
<h3 data-id="heading-6">封装： 通过封装，控制类的属性与方法的可访问信息</h3>
<p>关键字：<code>private</code>、<code>public</code>、<code>protected</code></p>
<p>封装的三个好处： 程序低耦合、能够对类的内部结构进行设置可访问/不可访问、能够对内部成员进行限制&#123;三个关键字&#125;</p>
<blockquote>
<p>ES6 目前没有支持封装特性</p>
</blockquote>
<p>对于typescript一个JavaScript的超集就更接近面向对象编程的思想也拥有<code>private</code>、<code>public</code>、<code>protected</code>等关键字进行对其内部成员进行配置。对于面向对象语言来说得先申明好数据的数据类型。</p>
<p>后期再回顾typescript知识并记录学习的知识要点。</p>
<p>扯远了~ 回归正题： js中如何实现封装---让成员变量私有化： 使用<code>Symbol</code>类型（ES6新数据类型）：独一无二的值。</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Glossary/Symbol" target="_blank" rel="nofollow noopener noreferrer">Symbol()</a> <code>symbol</code>类型的值，该类型具有<code>静态属性</code>和<code>静态方法</code>。它的静态属性会暴露几个内建的成员对象；它的静态方法会暴露全局的symbol注册</p>
<p>下面就写一个Symbol实现类属性私有化的 🌰</p>
<h4 data-id="heading-7">Symbol实现封装</h4>
<p>首先创建一个classes.js文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">const</span> hobby = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'hobby'</span>)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age</span>)</span> &#123;
            <span class="hljs-built_in">this</span>.name = name;
            <span class="hljs-built_in">this</span>.age = age;
            <span class="hljs-built_in">this</span>[hobby] = <span class="hljs-string">'撸铁'</span>
&#125;
<span class="hljs-function"><span class="hljs-title">info</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`name: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> ; age: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>`</span>)
&#125;
        <span class="hljs-function"><span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`我是classes.js文件，我现在访问自己的私有属性hobby：<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>[hobby]&#125;</span>`</span>)
        &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再创建一个subClass.js文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> Animal <span class="hljs-keyword">from</span> <span class="hljs-string">'./classes.js'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>  () => &#123;
    <span class="hljs-keyword">const</span> dog = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'狗'</span>, <span class="hljs-number">2</span>)
    dog.info()
    dog.foo()
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`我是subClass.js文件，我正在访问Classes.js的私有属性hobby：<span class="hljs-subst">$&#123;dog[<span class="hljs-string">'hobby'</span>]&#125;</span>`</span> )
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            哈哈哈
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9397820088db45c39ad4103a7c29d32c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">继承</h3>
<p>在es5中，用构造函数call、apply改变this指向或者使用原型链继承js实现继承的方式多种，就举栗这两种吧。</p>
<h4 data-id="heading-9">1. 原型链继承</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, height</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name
        <span class="hljs-built_in">this</span>.age = age
        <span class="hljs-built_in">this</span>.height = height
        <span class="hljs-built_in">this</span>.doing = <span class="hljs-function">() =></span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i am coding!'</span>)
        &#125;
        <span class="hljs-built_in">this</span>.info = <span class="hljs-function">() =></span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`hello, i am <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>, i am <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span> year old .`</span>)
        &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MoreInformation</span>(<span class="hljs-params"></span>)</span>&#123;
&#125;
MoreInformation.prototype.bobby = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i like Swimming'</span>)
&#125;
Person.prototype = MoreInformation.prototype
Person.prototype.sleeping = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i am sleeping'</span>)
&#125;
<span class="hljs-keyword">var</span> echo = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'echo'</span>, <span class="hljs-number">6</span>, <span class="hljs-number">180</span>)
echo.sleeping() <span class="hljs-comment">//i am sleeping</span>
echo.bobby() <span class="hljs-comment">//i like Swimming</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">2. call、apply 借用方法、属性</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, height</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name
    <span class="hljs-built_in">this</span>.age = age
    <span class="hljs-built_in">this</span>.height = height
    <span class="hljs-built_in">this</span>.doing = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i am coding!'</span>)
    &#125;
    <span class="hljs-built_in">this</span>.info = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`hello, i am <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>, i am <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span> year old .`</span>)
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>)</span>&#123;
    Person.call(<span class="hljs-built_in">this</span>, <span class="hljs-string">'echoBoy'</span>, <span class="hljs-number">2</span>, <span class="hljs-number">155</span>)
    <span class="hljs-comment">// Person.apply(this, ['echoBoy', 2, 155])</span>
    <span class="hljs-built_in">this</span>.info()
&#125;
<span class="hljs-keyword">var</span> echo = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'echo'</span>, <span class="hljs-number">6</span>, <span class="hljs-number">180</span>)
<span class="hljs-keyword">var</span> echoBoy = <span class="hljs-keyword">new</span> Child() <span class="hljs-comment">// hello, i am echoBoy, i am 2 year old .</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">3. ES6类继承</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>&#123;
        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age</span>)</span> &#123;
            <span class="hljs-built_in">this</span>.name = name;
            <span class="hljs-built_in">this</span>.age = age;
        &#125;
        <span class="hljs-function"><span class="hljs-title">info</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`name: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> ; age: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>`</span>)
        &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ChildAnimal</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span></span>&#123;
        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age, color</span>)</span> &#123;
            <span class="hljs-built_in">super</span>(name, age)
            <span class="hljs-built_in">this</span>.color = color
        &#125;
        <span class="hljs-function"><span class="hljs-title">infomation</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`name: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> ; age: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span> ; color: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.color&#125;</span>`</span>)
        &#125;
&#125;
<span class="hljs-keyword">const</span> dog = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'狗'</span>, <span class="hljs-number">2</span>)
<span class="hljs-keyword">const</span> cat = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'猫'</span>, <span class="hljs-number">1</span>)
dog.info() <span class="hljs-comment">//name: 狗 ; age: 2</span>
cat.info() <span class="hljs-comment">//name: 猫 ; age: 1</span>
<span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">new</span> ChildAnimal(<span class="hljs-string">'哈哈'</span>, <span class="hljs-number">6</span>, <span class="hljs-string">'yellow'</span>)
foo.info() <span class="hljs-comment">//name: 哈哈 ; age: 6</span>
foo.infomation() <span class="hljs-comment">//name: 哈哈 ; age: 6 ; color: yellow</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从代码运行结果看出 ChildAnimal类继承了父类Animal。可以调用父类的方法和使用其父类的属性。
<code>super</code>关键字：<code>super</code>关键字用于访问和调用一个对象的父对象上的函数。</p>
<h3 data-id="heading-12">多态</h3>
<p>多态： 成员方法的重载和重写</p>
<hr>
<p>tips: 希望自己的总结对屏幕前的您有帮助，若有不对的地方，积极指出。thanks</p>
<p>一起进步！！!</p></div>  
</div>
            