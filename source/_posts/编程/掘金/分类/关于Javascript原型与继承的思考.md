
---
title: '关于Javascript原型与继承的思考'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d44f5454622456f8e9bdbcee30d0b47~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 11:53:12 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d44f5454622456f8e9bdbcee30d0b47~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">从一个对象开始</h1>
<p>不知你有没有想过，什么是对象？在Javascript中，对象是这样的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> animal = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'a'</span>,
    <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果你还不清楚this的指向问题，看这里 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/this" target="_blank" rel="nofollow noopener noreferrer">this</a></p>
</blockquote>
<p>因此，我们可以这么简单的描述，对象，是属性的集合，是一种数据结构，是一种代码的组织形式，是一种对现实世界物体的表示方法。<br>
关于面向对象的不再多说，总之，我们就从这个对象为起点，开始讨论。</p>
<h1 data-id="heading-1">对象的模板</h1>
<p>现在，假设我们需要3个对象，表示3只动物，如果直接把上面的代码复制3遍，那可是一个不好的习惯，要改掉哦，谨记DRY原则，Don't Repeat Yourself。<br>
最好呢，有一个模板，比如用函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">newAnimal</span>(<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        name,
        <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">const</span> animal1 = newAnimal(<span class="hljs-string">'a'</span>)
<span class="hljs-keyword">const</span> animal2 = newAnimal(<span class="hljs-string">'b'</span>)
<span class="hljs-keyword">const</span> animal3 = newAnimal(<span class="hljs-string">'c'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按下F12，讲这些代码复制进去运行看看，这样生成的对象没问题。<br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d44f5454622456f8e9bdbcee30d0b47~tplv-k3u1fbpfcp-watermark.image" width="50%" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样的写法，至少看着就不优雅了，而且继承也不好搞，关于继承先别急，后面会说。<br>
这里介绍下Javascript的关键字：<em><strong>new</strong></em>，上面的代码可以这么写</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span>(<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name,
    <span class="hljs-built_in">this</span>.getName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
    &#125;
&#125;

<span class="hljs-keyword">const</span> animal1 = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'a'</span>)
<span class="hljs-keyword">const</span> animal2 = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'b'</span>)
<span class="hljs-keyword">const</span> animal3 = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'c'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看着是不是就优雅了一些呢。<br>
那么，这个new关键字干了啥呢？我们自己实现一个简单的函数来模拟new：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// new关键字当然不止干了这点事，其他的先不管</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">newFunc</span>(<span class="hljs-params">func, name</span>) </span>&#123;
    <span class="hljs-keyword">var</span> obj = &#123;&#125; <span class="hljs-comment">// 创建一个新的空对象</span>
    func.call(obj, name) <span class="hljs-comment">// 调用函数，并将函数里面的this指向到obj</span>
    <span class="hljs-keyword">return</span> obj <span class="hljs-comment">// 返回这个对象</span>
&#125;
<span class="hljs-keyword">const</span> animal4 = newFunc(Animal, <span class="hljs-string">'d'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行起来，对比下animal3跟animal4。<br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ed83d0e3c0f48cabdc83c0971587883~tplv-k3u1fbpfcp-watermark.image" width="50%" loading="lazy" referrerpolicy="no-referrer"><br>
animal3左边有个Animal，是函数Animal的名字，也既Animal.name，说明这个对象是Animal创建的。</p>
<blockquote>
<p>关于new的更多资料，参考<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/new" target="_blank" rel="nofollow noopener noreferrer">new运算符的介绍</a><br>
如果call函数看不懂，参考<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/call" target="_blank" rel="nofollow noopener noreferrer">call函数介绍</a></p>
</blockquote>
<h1 data-id="heading-2">对象的原型(prototype)</h1>
<p>使用new来执行一个函数，是解决了模板的问题，但是还存在一个不可忽视的问题：每次创建一个对象的时候，对象里面的所有属性都要创建一次。</p>
<p>对于有些属性，比如函数<strong>getName</strong>，只需要一个，所有对象都使用这个函数就行了，多个相同的函数会浪费内存，显然可以优化。</p>
<p>而且，记住，Javascript是动态语言，运行过程中的属性是可以随意修改的，为了避免在运行中，修改函数的实现的需要找到所有对象一个个的改，也不能让每个对象都自带一个函数。</p>
<p>Javascript对此的解决方案，叫做原型(prototype)，这么写：</p>
<pre><code class="copyable">function Animal(name) &#123;
    this.name = name
&#125;
// 把getName放到了原型上
Animal.prototype.getName = function() &#123;
    return this.name
&#125;
var animal = new Animal('a')
console.log(animal.getName())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行起来，getName能调用到。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22663cc0d2444c0eb49c06f6325853f7~tplv-k3u1fbpfcp-watermark.image" width="60%" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">prototype哪里来的</h2>
<p>Javascript对每一个函数，自动给它加上prototype属性，它就是个对象。</p>
<blockquote>
<p>实际上不是所有函数都有prototype的，下面会说到。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 默认的原型对象</span>
Animal.prototype = &#123;
    <span class="hljs-attr">constructor</span>: Animal <span class="hljs-comment">// constructor是啥？先无视它</span>
&#125;

<span class="hljs-comment">// 这只是个默认操作，如果我们用这样的写法</span>
<span class="hljs-comment">// 默认的对象就会被覆盖掉，constructor就没了</span>
Animal.prototype = &#123;
    <span class="hljs-attr">getName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行代码，将两种写法运行下进行验证。<br>
这样写有constructor<br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb4b4aca17944523b521de4e715df968~tplv-k3u1fbpfcp-watermark.image" width="50%" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样写没有<br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b03c44d9df54786bf29fda52fc0ee0f~tplv-k3u1fbpfcp-watermark.image" width="40%" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">对象为什么可以直接调用prototype上的属性</h2>
<p>new的时候，Javascript会给新建的对象设置一个__proto__属性，指向prototype。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">animal.__proto__ = Animal.prototype
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，当在animal本身找不到属性时，会往__proto__里面找。<br>
也既，<strong>animal.__proto__.getName</strong> 可以直接写成<strong>animal.getName</strong></p>
<blockquote>
<p>__proto__属性已被删除，你不可以在代码中使用它。<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/proto" target="_blank" rel="nofollow noopener noreferrer">MDN这里说了</a></p>
</blockquote>
<h1 data-id="heading-5">基于原型的继承</h1>
<p>想必继承的概念不必解释吧。假设我们现在需要写一个对象来表示狗，代码是这样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Dog</span>(<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name
&#125;
Dog.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
&#125;
Dog.prototype.bark = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'wang'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来分析下这段代码，先跟Animal对比下，问题就很明显，大部分代码跟Animal重复了。<br>
所以，最好让Dog继承Animal。<br>
首先，分析Animal，可以看到，Animal实例化后的对象属性分两种：</p>
<ul>
<li>一种是对象本身的，写在类函数里面</li>
<li>一种是原型上的，写在prototype上面</li>
</ul>
<p>对于第一种，可以像模拟new的实现一样，使用call函数把属性复制过来。<br>
对于第二种，因为对象可以访问原型上的属性，让Dog的原型指向Animal的原型可以吗？<br>
答案是，<strong>不可以</strong>。</p>
<blockquote>
<p>如果Dog原型直接指向Animal原型，Dog跟Animal就共用一个原型对象了，在Dog里面加个属性，Animal里面就有了，假如我们再写个对象Cat继承Animal，那Cat里面岂不是也有了个bark属性？</p>
</blockquote>
<h2 data-id="heading-6">第一次继承尝试</h2>
<p>既然不能直接指向，我们先尝试复制一个Animal的原型对象，指向这个复制后的，代码如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Dog</span>(<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-comment">// 运行Animal函数，将函数里面的this指向Dog的this，相当于给Dog添加属性</span>
    Animal.call(<span class="hljs-built_in">this</span>, name)
&#125;
<span class="hljs-comment">// 复制Animal的原型对象，老规矩，当constructor不存在</span>
Dog.prototype = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, Animal.prototype)
Dog.prototype.bark = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'wang'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Object.assign的介绍 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/assign" target="_blank" rel="nofollow noopener noreferrer">看这里</a></p>
</blockquote>
<p>运行代码，跟预期的结果相符<br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ec61ba6dd504efaa4fc3dcb0bb31015~tplv-k3u1fbpfcp-watermark.image" width="50%" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样的方式，虽说可用，但也有限制。记住，Javascript是动态语言，如果在复制完Dog的属性之后，Animal的原型上增加了一个属性，Dog是没有的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 比如给Animal加个walk属性</span>
Animal.prototype.walk = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'walking'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再运行代码，可以看到，walk属性dog里面并没有。<br>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a56f31f67ea4c999ad62c04806d2186~tplv-k3u1fbpfcp-watermark.image" width="45%" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">第二次继承尝试</h2>
<p>我们再回顾下原型，JS在查找属性的时候，如果本身没找到，会去__proto__里面找。如果__proto__里面也没找到呢？<br>
这里就要说下<strong>原型链</strong>了，简单的说，__proto__里面也可以继续嵌套__proto__的，属性查找就可以这样继续下去。<br>
一个Dog的创建出来的对象如果能长这样子，不就能解决Animal原型上增加了属性Dog里面没有的问题了吗？</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> dog = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">'dog'</span>)
<span class="hljs-comment">// 这里只是示例，实际上并不相等</span>
dog == &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'dog'</span>,
    <span class="hljs-attr">__proto__</span>: &#123;
        <span class="hljs-attr">bark</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">'wang'</span>
        &#125;,
        <span class="hljs-attr">__proto__</span>: &#123;
            <span class="hljs-attr">getName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再回想之前讲到的：</p>
<ul>
<li>第一，使用<strong>new</strong>创建对象时干了这么一件事</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">dog.__proto__ === Dog.prototype
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第二，原型的默认值是这样的，并且可以更改</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">Dog.prototype = &#123;
    <span class="hljs-attr">constructor</span>: Dog
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第三，这个上面没说过。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 我们平时创建对象都习惯使用声明式语法</span>
<span class="hljs-keyword">const</span> prototype = &#123;
    <span class="hljs-attr">constructor</span>: Dog
&#125;
<span class="hljs-comment">// 其实还有个构造式语法</span>
<span class="hljs-keyword">const</span> prototype = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
prototype.constructor = Dog
<span class="hljs-comment">// 两者创建的对象时一样的。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在构造式语法中，我们就可以轻易看出来，原型对象，它也是有__proto__的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Dog.prototype.__proto__ === <span class="hljs-built_in">Object</span>.prototype
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，只要Dog的原型不用默认的，用Animal的实例，像这样子</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Dog.prototype = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'ani'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是呢，这么写的话，Dog.prototype上就存在name属性了。</p>
<blockquote>
<p>当然，这样问题也不大，根据属性查找规则，实例本身的name属性优先级是要高于原型上的，所以正常访问也不会访问出错。但是，如果把实例上的name属性删除了，dog.name还是会存在，也就是说这个属性怎么删也删不掉。<br>
聪明的你，可能会想，那我把原型上的name删除不就完了吗？这。。。也行吧。</p>
</blockquote>
<p>我们有更好的解决办法，既然我们想要的只是Animal的原型，那就可以这样</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">T</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
T.prototype = Animal.prototype
Dog.prototype = <span class="hljs-keyword">new</span> T()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，我们就实现一个理想的继承了。<br>
来看下JS的继承完整代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span>(<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name
&#125;

Animal.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Dog</span>(<span class="hljs-params">name</span>) </span>&#123;
    Animal.call(<span class="hljs-built_in">this</span>, name)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">T</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
T.prototype = Animal.prototype
Dog.prototype = <span class="hljs-keyword">new</span> T()

Dog.prototype.bark = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'wang'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看下运行效果<br>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b88e015ed5db4a8c9f4d393f60f1dcbc~tplv-k3u1fbpfcp-watermark.image" width="45%" loading="lazy" referrerpolicy="no-referrer"><br>
再看下这代码，别说优雅了，看都很难看懂好吧。<br>
连封装成一个函数都不好封装，因为Dog里面为了得到Animal的属性，是必须要调用Animal的。</p>
<h1 data-id="heading-8">ES6的新写法</h1>
<p>所幸，现在是2021年了，javascript的划时代版本，ES6，已经推出6年了。来看下ES6版本的代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.name = name
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(name)
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">bark</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'wang'</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是看着都舒服，但是这些<strong>class</strong> <strong>extends</strong> <strong>super</strong>都是啥啊？</p>
<h1 data-id="heading-9">类理论</h1>
<p>说到这些关键字，就不得不提下类。如果你学过Java，就很熟悉类是什么，简单说一句，类就是一种设计模式，对继承思想的一种实现。<br>
你可能从来没把类当成一种设计模式来看，但看看我们用Javascript实现继承，从头到尾都没提到类，不也照样实现了，只是代码好丑，所以Javascript在ES6版本就借用了类的语法。<br>
<strong>要记住，继承，是一种编程思想；类，是一种实现方案。</strong><br>
Javascript另辟跷径的用原型也做到了，思路都是相通的。</p>
<blockquote>
<p>关于类与继承的更多资料，推荐一本书，<a href="https://blog.csdn.net/qq_38021852/article/details/82756068" target="_blank" rel="nofollow noopener noreferrer">你不知道的Javascript</a>，上卷第二部分第四章，深度好书，每一章都值得看。</p>
</blockquote>
<p>再顺便看下Java的继承代码实现</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-keyword">private</span> String name = <span class="hljs-string">""</span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Animal</span><span class="hljs-params">(String name)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.name = name;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getName</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.name;
    &#125;
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Dog</span><span class="hljs-params">(String name)</span> </span>&#123;
        <span class="hljs-keyword">super</span>(name);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">bark</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"wang"</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是看起来就挺像的。但是，Javascript中的类，就是语法糖，那些类语法的关键字class extends super啊，都是虚的，记住能这么写就行，实际运行时还是原型那一套。</p>
<h2 data-id="heading-10">对比Java的类以及Javascript的原型对继承的实现</h2>
<p>Javascript的原型实现继承我们已经基本清楚了，那它跟基于类的继承有什么区别呢？</p>
<blockquote>
<p>这里只是为了跟Javascript做个对比，会说的尽量简单，大概思路清楚就行。<br>
如果想知道Java继承的详细实现，可以去<a href="https://www.cnblogs.com/swiftma/p/5537665.html" target="_blank" rel="nofollow noopener noreferrer">这里看看</a></p>
</blockquote>
<h3 data-id="heading-11">概念对应</h3>
<p>首先理清两个概念跟Javascript的对应关系。</p>
<ul>
<li>变量：指的是除了函数之外的数据类型</li>
<li>方法：就是函数</li>
</ul>
<p>先来看下Java的class是干嘛用的。不去管public private这些权限修饰符。class里面有</p>
<ul>
<li>静态方法</li>
<li>静态变量</li>
<li>实例方法</li>
<li>实例变量</li>
<li>构造函数</li>
</ul>
<p>以Animal为例，静态属性跟静态方法的调用是这样的</p>
<pre><code class="hljs language-java copyable" lang="java">Animal.a
Animal.b()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在Javascript中，Animal首先是个对象，然后才是个函数，这也意味着，我们可以给Animal本身添加属性，这就模拟了Java中的静态变量、方法了。</p>
<blockquote>
<p>函数跟对象的区别，<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions" target="_blank" rel="nofollow noopener noreferrer">看这里</a></p>
</blockquote>
<p>再看下实例方法跟实例变量<br>
Javascript写在函数里面的this.xxx就是实例属性，而且，比Java更强大的是，Javascript中函数是一等公民。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Javascript可以把函数也当成变量</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.go = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">'gogogo'</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// Java中只能把函数当成方法</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">go</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'gogogo'</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过在Java8之后引入了lambda表达式，这里就不管它了。
至于构造函数，Javascript中就是Animal本身了。</p>
<h3 data-id="heading-12">具体实现</h3>
<h4 data-id="heading-13">先加载类</h4>
<p>你可以这么理解，Java在加载类的时候，先把类变成一个对象，里面放着静态属性、静态方法、实例方法、构造函数，以及对父类的引用。<br>
而在Javascript中，静态属性静态方法都是函数的属性，实例方法在原型上，构造函数就是函数本身，对父类的引用也在原型上。</p>
<h4 data-id="heading-14">再实例化对象</h4>
<p>当Java执行new Animal的时候，就会调用类的构造函数，并逐级往上，调用所有父类的构造函数，将所有实例变量放到new出来的对象，并存放Animal类的引用。
以animal跟dog为例，大概长这样子</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">dog = &#123;
    <span class="hljs-string">'类Dog的引用'</span>: &#123;
        <span class="hljs-string">'父类Animal的引用'</span>: &#123;
            <span class="hljs-string">'实例方法getName'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name &#125;
        &#125;
        <span class="hljs-string">'实例方法bark'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-string">'wang'</span> &#125;
    &#125;
    <span class="hljs-string">'父类Animal的实例变量'</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'parent'</span>
    &#125;,
    <span class="hljs-string">'类Dog的实例变量'</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'parent'</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大概就是这样，所以，可以把类看成Javascript的原型，都是引用，不会把这些函数放在自己身上。<br>
这里可以看出一个区别，Javascript继承时如果遇到子类的属性跟父类一样，子类会直接覆盖，而Java会两者都保留，而且通过多态可以切换访问父类与子类的实例变量。<br>
对于方法的查找也跟Javascript差不多，都是逐级向上。<br>
<strong>总的来说，基于原型跟基于类的实现，其实大同小异。</strong></p>
<h1 data-id="heading-15">尴尬的constructor</h1>
<p>constructor，就是构造函数。干嘛用的呢？先别急，看下Java，没办法，构造函数就是类理论的东西，Javascript老想着模拟类咱也没办法。</p>
<h2 data-id="heading-16">Java为什么需要构造函数</h2>
<p>因为Java实例化一个对象的模板是类，而Javascript的模板是函数，函数可以直接执行，类怎么直接执行呢？</p>
<blockquote>
<p>如果你非要问函数为什么可以直接执行，那就没完没了，不是一篇文章讲得完的。</p>
</blockquote>
<p>因此，同样是 <strong>new Animal()</strong> 这么一句代码。</p>
<ul>
<li>Java的Animal是一个类，需要借助构造函数执行初始化操作</li>
<li>Javascript的Animal是一个函数，直接就执行初始化操作了</li>
</ul>
<h2 data-id="heading-17">constructor有啥用</h2>
<p>我们再想想，Javascript，它需要再来个构造函数吗？明显不需要嘛。<br>
那Javascript搞了这个constructor有啥用呢？<br>
也不能说没用吧，至少面试的时候面试官会问下。开玩笑的。<br>
不过，在ES6之前，constructor还真的没啥用，就规范里说了原型上要有个构造函数，指向函数本身，然后就没了，Javascript中没有任何地方使用到原型上的构造函数。<br>
到了ES6，constructor终于被用上了，除此之外，有些第三方库的代码也会使用这个属性。</p>
<blockquote>
<p>关于构造函数干嘛用，请看<a href="https://stackoverflow.com/questions/8453887/why-is-it-necessary-to-set-the-prototype-constructor" target="_blank" rel="nofollow noopener noreferrer">这里</a></p>
</blockquote>
<p>只要记住原型上有个构造函数，指向函数本身，不能弄没了，有人会用。</p>
<h1 data-id="heading-18">prototype constructor __proto__的三角关系</h1>
<p>大部分都理不清这些关系，我感觉是因为对原型不够了解造成的，特别是原型跟类混在一起就更乱了。<br>
我们以ES6版本的Animal跟Dog为例，一步步来。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// new一条狗</span>
<span class="hljs-keyword">const</span> dog = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">'dog'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把这条狗展开<br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38e1700357c64373a70f99053a66d2d9~tplv-k3u1fbpfcp-watermark.image" width="50%" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再把Dog这个函数展开<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/400ddc0eb20a4587a8f7bf5fa7e68e9e~tplv-k3u1fbpfcp-watermark.image" width="30%" loading="lazy" referrerpolicy="no-referrer"><br>
有点尴尬，这个展不开，不管了。</p>
<h2 data-id="heading-19">dog.__proto__ === Dog.prototype</h2>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3894be209e4c42f2a4afd36bb15fe431~tplv-k3u1fbpfcp-watermark.image" width="50%" loading="lazy" referrerpolicy="no-referrer"> 
<p>对比dog的展开，是不是明摆着一样的。再用全等号验证下<br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c4fe5f1359a411492e353d825796456~tplv-k3u1fbpfcp-watermark.image" width="40%" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 那么</span>
dog.__proto__.__proto__  === Dog.prototype.__proto__
<span class="hljs-comment">// 并且</span>
Dog.prototype === <span class="hljs-keyword">new</span> Animal()<span class="hljs-comment">// 可以当作是Animal的实例。假设叫它animal</span>
<span class="hljs-comment">// 又因为</span>
animal.__proto__ === Animal.prototype
<span class="hljs-comment">// 综上所述</span>
dog.__proto__.__proto__ === Animal.prototype
<span class="hljs-comment">// 同理可得</span>
dog.__proto__.__proto__.__proto__ === <span class="hljs-built_in">Object</span>.prototype
<span class="hljs-comment">// 不管继承了多少次，这么推导下去一定能一级一级的推导出来</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">dog.constructor === Dog</h2>
<p>记住，constructor只在原型中存在。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 因为</span>
<span class="hljs-built_in">Object</span>.hasOwnProperty.call(dog, <span class="hljs-string">'constructor'</span>) === <span class="hljs-literal">false</span>
<span class="hljs-comment">// 所以</span>
dog.constructor === dog.__proto__.constructor
<span class="hljs-comment">// 又因为</span>
dog.__proto__ === Dog.prototype
<span class="hljs-comment">// 所以</span>
dog.__proto__.constructor === Dog.prototype.constructor
<span class="hljs-comment">// 所以</span>
dog.constructor === Dog
<span class="hljs-comment">// 再来个乱七八糟的</span>
Dog.prototype.__proto__.constructor == Animal
<span class="hljs-comment">// 自己推导试试</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">Dog.constructor === Function</h2>
<p>同对象一样，函数也有构造式写法</p>
<pre><code class="copyable">const Dog = new Function(name, 'Animal.call(this, name)')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以看出来，Dog，是Function的一个实例。</p>
<h1 data-id="heading-22">来一些探索</h1>
<p><strong>请注意，下面涉及到Javascript本质的讨论，比较有难度，我也还没吃透，难免有些错误</strong></p>
<h2 data-id="heading-23">Object哪来的</h2>
<p>可能你会说，Object是Javascript内置的，是这么说没错，但我们来更进一步试试看。<br>
先打印下Object<br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1915017e6009435c97459defb862941a~tplv-k3u1fbpfcp-watermark.image" width="40%" loading="lazy" referrerpolicy="no-referrer"><br>
看不到Object的源代码代码。</p>
<blockquote>
<p>[native code]是什么意思呢，可以看下别人怎么说 <a href="https://www.zhihu.com/question/22331234" target="_blank" rel="nofollow noopener noreferrer">别人的回答</a></p>
</blockquote>
<p>那么我们再试试这个。<br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/140f79e7670b4f24ab09d92b3b80570c~tplv-k3u1fbpfcp-watermark.image" width="20%" loading="lazy" referrerpolicy="no-referrer"><br>
哦，Object居然是一个函数。倒也是，<strong>new Object()</strong> 也很好的证明的这一点，因为new后面只能是函数。</p>
<blockquote>
<p>如果new一个对象的时候，函数没有参数，不带括号也可以的哦，new Object也是正确语法</p>
</blockquote>
<p>那么，我们就可以说，下面的等式也是成立的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 自己推导，不解释</span>
<span class="hljs-built_in">Object</span>.__proto__ === <span class="hljs-built_in">Function</span>.prototype
<span class="hljs-built_in">Object</span>.constructor === <span class="hljs-built_in">Function</span>
<span class="hljs-built_in">Object</span>.prototype === ? <span class="hljs-comment">// prototype是创建函数默认加上的，下面继续讨论</span>
<span class="hljs-built_in">Object</span>.prototype.__proto__ === <span class="hljs-literal">null</span> <span class="hljs-comment">// 没了，原型链到此结束</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有个地方打破了我的认知，默认对象都是Object的实例。<br>
那么Object.prototype是对象吗？当然是。<br>
那么它是Object的实例吗？居然不是。
如果是，那么，Object.prototype.__proto__就应该等于Object.prototype。但是它等于null啊。<br>
不过这也好理解，如果这样设计，原型链就没有终点了，这会导致属性的查询陷入死循环。</p>
<h2 data-id="heading-24">再看看Function</h2>
<p>跟Object一样，打印出来也是[native code]，也是一个函数。</p>
<p>那么问题来了，Function的<strong>constructor</strong> <strong>__proto__</strong> <strong>prototype</strong>会是什么呢？<br>
我看来看下浏览器的打印<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd4ad91d266049769d8fef3760fa93e8~tplv-k3u1fbpfcp-watermark.image" width="40%" loading="lazy" referrerpolicy="no-referrer"><br>
说实话，看到这些玩意我人都傻了。</p>
<p>我一直以为prototype默认就是个new Object，可这是啥？函数？不过函数也是一个可执行的对象，这总没错吧，来试试看。<br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b173412dccbd46a5a968b52f5f72d7bb~tplv-k3u1fbpfcp-watermark.image" width="50%" loading="lazy" referrerpolicy="no-referrer"><br>
还好，这个是对的。</p>
<p>那么，所有函数都有prototype这个结论靠谱吗？经过一番查证，还真找到了答案，<strong>不靠谱</strong>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68cb39bcd5b7471f80dd322d990f1fe1~tplv-k3u1fbpfcp-watermark.image" width="40%" loading="lazy" referrerpolicy="no-referrer"><br>
意不意外，函数不一定有prototype哦。</p>
<p>从上面的运行结果我们可以得出以下结论</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Function</span>.constructor === <span class="hljs-built_in">Function</span>
<span class="hljs-built_in">Function</span>.__proto__ === <span class="hljs-built_in">Function</span>.prototype
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这说明了什么？Function自己创建了自己？对于这个答案，我是不满意的。<br>
继续找答案，这种问题应该要找RFC规范吧，然而，我死活没找到，RFC就说了要这么干，没说为什么。<br>
所幸，不止我一个人有疑问，答案在这，这就是个先有鸡还是先有蛋的问题。不想写了，有兴趣的自己去看吧。</p>
<blockquote>
<p><a href="https://github.com/jawil/blog/issues/13" target="_blank" rel="nofollow noopener noreferrer">github上的关于这些头疼问题的讨论</a></p>
</blockquote></div>  
</div>
            