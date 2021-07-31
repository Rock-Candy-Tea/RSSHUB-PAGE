
---
title: 'TypeScript——装饰器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3598'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 02:16:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=3598'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote>
<h2 data-id="heading-0">介绍</h2>
<p>随着TypeScript和ES6里引入了类，在一些场景下我们需要额外的特性来支持标注或修改类及其成员。 装饰器（Decorators）为我们在类的声明及成员上通过元编程语法添加标注提供了一种方式。 Javascript里的装饰器目前处在 建议征集的第二阶段，但在TypeScript里已做为一项实验性特性予以支持。</p>
<blockquote>
<p>注意  装饰器是一项实验性特性，在未来的版本中可能会发生改变。</p>
</blockquote>
<p>若要启用实验性的装饰器特性，你必须在命令行或tsconfig.json里启用experimentalDecorators编译器选项：</p>
<p>命令行:</p>
<pre><code class="copyable">tsc --target ES5 --experimentalDecorators
<span class="copy-code-btn">复制代码</span></code></pre>
<p>tsconfig.json:</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"compilerOptions"</span>: &#123;
        <span class="hljs-attr">"target"</span>: <span class="hljs-string">"ES5"</span>,
        <span class="hljs-attr">"experimentalDecorators"</span>: <span class="hljs-literal">true</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">装饰器</h2>
<p>装饰器是一种特殊类型的声明，它能够被附加到类声明，方法， 访问符，属性或参数上。 装饰器使用 @expression这种形式，expression求值后必须为一个函数，它会在运行时被调用，被装饰的声明信息做为参数传入。</p>
<p>例如，有一个@sealed装饰器，我们会这样定义sealed函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sealed</span>(<span class="hljs-params">target</span>) </span>&#123;
    <span class="hljs-comment">// do something with "target" ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意  后面类装饰器小节里有一个更加详细的例子。</p>
<h2 data-id="heading-2">装饰器工厂</h2>
<p>如果我们要定制一个修饰器如何应用到一个声明上，我们得写一个装饰器工厂函数。 装饰器工厂就是一个简单的函数，它返回一个表达式，以供装饰器在运行时调用。</p>
<p>我们可以通过下面的方式来写一个装饰器工厂函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">color</span>(<span class="hljs-params">value: <span class="hljs-built_in">string</span></span>) </span>&#123; <span class="hljs-comment">// 这是一个装饰器工厂</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target</span>) </span>&#123; <span class="hljs-comment">//  这是装饰器</span>
        <span class="hljs-comment">// do something with "target" and "value"...</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意  下面方法装饰器小节里有一个更加详细的例子。</p>
</blockquote>
<h2 data-id="heading-3">装饰器组合</h2>
<p>多个装饰器可以同时应用到一个声明上，就像下面的示例：</p>
<p>书写在同一行上：</p>
<pre><code class="copyable">@f @g x
<span class="copy-code-btn">复制代码</span></code></pre>
<p>书写在多行上：</p>
<pre><code class="copyable">@f
@g
x
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当多个装饰器应用于一个声明上，它们求值方式与复合函数相似。在这个模型下，当复合f和g时，复合的结果(f ∘ g)(x)等同于f(g(x))。</p>
<p>同样的，在TypeScript里，当多个装饰器应用在一个声明上时会进行如下步骤的操作：</p>
<ol>
<li>由上至下依次对装饰器表达式求值。</li>
<li>求值的结果会被当作函数，由下至上依次调用。</li>
</ol>
<p>如果我们使用装饰器工厂的话，可以通过下面的例子来观察它们求值的顺序：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"f(): evaluated"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target, propertyKey: <span class="hljs-built_in">string</span>, descriptor: PropertyDescriptor</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"f(): called"</span>);
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">g</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"g(): evaluated"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target, propertyKey: <span class="hljs-built_in">string</span>, descriptor: PropertyDescriptor</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"g(): called"</span>);
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> </span>&#123;
    <span class="hljs-meta">@f</span>()
    <span class="hljs-meta">@g</span>()
    <span class="hljs-function"><span class="hljs-title">method</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控制台里会打印出如下结果：</p>
<pre><code class="copyable">f(): evaluated
g(): evaluated
g(): called
f(): called
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">装饰器求值</h2>
<p>类中不同声明上的装饰器将按以下规定的顺序应用：</p>
<ol>
<li>参数装饰器，然后依次是方法装饰器，访问符装饰器，或属性装饰器应用到每个实例成员。</li>
<li>参数装饰器，然后依次是方法装饰器，访问符装饰器，或属性装饰器应用到每个静态成员。</li>
<li>参数装饰器应用到构造函数。</li>
<li>类装饰器应用到类。</li>
</ol>
<h2 data-id="heading-5">类装饰器</h2>
<p>类装饰器在类声明之前被声明（紧靠着类声明）。 类装饰器应用于类构造函数，可以用来监视，修改或替换类定义。 类装饰器不能用在声明文件中( .d.ts)，也不能用在任何外部上下文中（比如declare的类）。</p>
<p>类装饰器表达式会在运行时当作函数被调用，类的构造函数作为其唯一的参数。</p>
<p>如果类装饰器返回一个值，它会使用提供的构造函数来替换类的声明。</p>
<blockquote>
<p>注意  如果你要返回一个新的构造函数，你必须注意处理好原来的原型链。 在运行时的装饰器调用逻辑中 不会为你做这些。</p>
</blockquote>
<p>下面是使用类装饰器(@sealed)的例子，应用在Greeter类：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-meta">@sealed</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Greeter</span> </span>&#123;
    <span class="hljs-attr">greeting</span>: <span class="hljs-built_in">string</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">message: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.greeting = message;
    &#125;
    <span class="hljs-function"><span class="hljs-title">greet</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + <span class="hljs-built_in">this</span>.greeting;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以这样定义@sealed装饰器：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sealed</span>(<span class="hljs-params">constructor: <span class="hljs-built_in">Function</span></span>) </span>&#123;
    <span class="hljs-built_in">Object</span>.seal(<span class="hljs-title">constructor</span>);
    <span class="hljs-built_in">Object</span>.seal(<span class="hljs-title">constructor</span>.<span class="hljs-title">prototype</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当@sealed被执行的时候，它将密封此类的构造函数和原型。(注：参见Object.seal)</p>
<p>下面是一个重载构造函数的例子。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">classDecorator</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> </span>&#123;<span class="hljs-keyword">new</span>(...args:<span class="hljs-built_in">any</span>[]):&#123;&#125;&#125;>(<span class="hljs-title">constructor</span>:<span class="hljs-title">T</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">constructor</span> </span>&#123;
        newProperty = <span class="hljs-string">"new property"</span>;
        hello = <span class="hljs-string">"override"</span>;
    &#125;
&#125;

<span class="hljs-meta">@classDecorator</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Greeter</span> </span>&#123;
    property = <span class="hljs-string">"property"</span>;
    hello: <span class="hljs-built_in">string</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">m: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.hello = m;
    &#125;
&#125;

<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> Greeter(<span class="hljs-string">"world"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">方法装饰器</h2>
<p>方法装饰器声明在一个方法的声明之前（紧靠着方法声明）。 它会被应用到方法的 属性描述符上，可以用来监视，修改或者替换方法定义。 方法装饰器不能用在声明文件( .d.ts)，重载或者任何外部上下文（比如declare的类）中。</p>
<p>方法装饰器表达式会在运行时当作函数被调用，传入下列3个参数：</p>
<ol>
<li>对于静态成员来说是类的构造函数，对于实例成员是类的原型对象。</li>
<li>成员的名字。</li>
<li>成员的属性描述符。</li>
</ol>
<blockquote>
<p>注意  如果代码输出目标版本小于ES5，属性描述符将会是undefined。</p>
</blockquote>
<p>如果方法装饰器返回一个值，它会被用作方法的属性描述符。</p>
<blockquote>
<p>注意  如果代码输出目标版本小于ES5返回值会被忽略。</p>
</blockquote>
<p>下面是一个方法装饰器（@enumerable）的例子，应用于Greeter类的方法上：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Greeter</span> </span>&#123;
    <span class="hljs-attr">greeting</span>: <span class="hljs-built_in">string</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">message: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.greeting = message;
    &#125;

    <span class="hljs-meta">@enumerable</span>(<span class="hljs-literal">false</span>)
    <span class="hljs-function"><span class="hljs-title">greet</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + <span class="hljs-built_in">this</span>.greeting;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以用下面的函数声明来定义@enumerable装饰器：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">enumerable</span>(<span class="hljs-params">value: <span class="hljs-built_in">boolean</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target: <span class="hljs-built_in">any</span>, propertyKey: <span class="hljs-built_in">string</span>, descriptor: PropertyDescriptor</span>) </span>&#123;
        descriptor.enumerable = value;
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的@enumerable(false)是一个装饰器工厂。 当装饰器 @enumerable(false)被调用时，它会修改属性描述符的enumerable属性。</p>
<h2 data-id="heading-7">访问器装饰器</h2>
<p>访问器装饰器声明在一个访问器的声明之前（紧靠着访问器声明）。 访问器装饰器应用于访问器的 属性描述符并且可以用来监视，修改或替换一个访问器的定义。 访问器装饰器不能用在声明文件中（.d.ts），或者任何外部上下文（比如 declare的类）里。</p>
<blockquote>
<p>注意  TypeScript不允许同时装饰一个成员的get和set访问器。取而代之的是，一个成员的所有装饰的必须应用在文档顺序的第一个访问器上。这是因为，在装饰器应用于一个属性描述符时，它联合了get和set访问器，而不是分开声明的。</p>
</blockquote>
<p>访问器装饰器表达式会在运行时当作函数被调用，传入下列3个参数：</p>
<ol>
<li>对于静态成员来说是类的构造函数，对于实例成员是类的原型对象。</li>
<li>成员的名字。</li>
<li>成员的属性描述符</li>
</ol>
<p>注意  如果代码输出目标版本小于ES5，Property Descriptor将会是undefined。</p>
<p>如果访问器装饰器返回一个值，它会被用作方法的属性描述符。</p>
<blockquote>
<p>注意  如果代码输出目标版本小于ES5返回值会被忽略。</p>
</blockquote>
<p>下面是使用了访问器装饰器（@configurable）的例子，应用于Point类的成员上：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
    <span class="hljs-keyword">private</span> _x: <span class="hljs-built_in">number</span>;
    <span class="hljs-keyword">private</span> _y: <span class="hljs-built_in">number</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>._x = x;
        <span class="hljs-built_in">this</span>._y = y;
    &#125;

    <span class="hljs-meta">@configurable</span>(<span class="hljs-literal">false</span>)
    <span class="hljs-keyword">get</span> <span class="hljs-title">x</span>() &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._x; &#125;

    <span class="hljs-meta">@configurable</span>(<span class="hljs-literal">false</span>)
    <span class="hljs-keyword">get</span> <span class="hljs-title">y</span>() &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._y; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以通过如下函数声明来定义@configurable装饰器：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configurable</span>(<span class="hljs-params">value: <span class="hljs-built_in">boolean</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target: <span class="hljs-built_in">any</span>, propertyKey: <span class="hljs-built_in">string</span>, descriptor: PropertyDescriptor</span>) </span>&#123;
        descriptor.configurable = value;
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">属性装饰器</h2>
<p>属性装饰器声明在一个属性声明之前（紧靠着属性声明）。 属性装饰器不能用在声明文件中（.d.ts），或者任何外部上下文（比如 declare的类）里。</p>
<p>属性装饰器表达式会在运行时当作函数被调用，传入下列2个参数：</p>
<ol>
<li>对于静态成员来说是类的构造函数，对于实例成员是类的原型对象。</li>
<li>成员的名字。</li>
</ol>
<blockquote>
<p>注意  属性描述符不会做为参数传入属性装饰器，这与TypeScript是如何初始化属性装饰器的有关。 因为目前没有办法在定义一个原型对象的成员时描述一个实例属性，并且没办法监视或修改一个属性的初始化方法。返回值也会被忽略。因此，属性描述符只能用来监视类中是否声明了某个名字的属性。</p>
</blockquote>
<p>我们可以用它来记录这个属性的元数据，如下例所示：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Greeter</span> </span>&#123;
    <span class="hljs-meta">@format</span>(<span class="hljs-string">"Hello, %s"</span>)
    <span class="hljs-attr">greeting</span>: <span class="hljs-built_in">string</span>;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">message: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.greeting = message;
    &#125;
    <span class="hljs-function"><span class="hljs-title">greet</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> formatString = getFormat(<span class="hljs-built_in">this</span>, <span class="hljs-string">"greeting"</span>);
        <span class="hljs-keyword">return</span> formatString.replace(<span class="hljs-string">"%s"</span>, <span class="hljs-built_in">this</span>.greeting);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后定义@format装饰器和getFormat函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> <span class="hljs-string">"reflect-metadata"</span>;

<span class="hljs-keyword">const</span> formatMetadataKey = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"format"</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">format</span>(<span class="hljs-params">formatString: <span class="hljs-built_in">string</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.metadata(formatMetadataKey, formatString);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getFormat</span>(<span class="hljs-params">target: <span class="hljs-built_in">any</span>, propertyKey: <span class="hljs-built_in">string</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.getMetadata(formatMetadataKey, target, propertyKey);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个@format("Hello, %s")装饰器是个 装饰器工厂。 当 @format("Hello, %s")被调用时，它添加一条这个属性的元数据，通过reflect-metadata库里的Reflect.metadata函数。 当 getFormat被调用时，它读取格式的元数据。</p>
<blockquote>
<p>注意  这个例子需要使用reflect-metadata库。 查看 元数据了解reflect-metadata库更详细的信息。</p>
</blockquote>
<h2 data-id="heading-9">参数装饰器</h2>
<p>参数装饰器声明在一个参数声明之前（紧靠着参数声明）。 参数装饰器应用于类构造函数或方法声明。 参数装饰器不能用在声明文件（.d.ts），重载或其它外部上下文（比如 declare的类）里。</p>
<p>参数装饰器表达式会在运行时当作函数被调用，传入下列3个参数：</p>
<ol>
<li>对于静态成员来说是类的构造函数，对于实例成员是类的原型对象。</li>
<li>成员的名字。</li>
<li>参数在函数参数列表中的索引。</li>
</ol>
<blockquote>
<p>注意  参数装饰器只能用来监视一个方法的参数是否被传入。</p>
</blockquote>
<p>参数装饰器的返回值会被忽略。</p>
<p>下例定义了参数装饰器（@required）并应用于Greeter类方法的一个参数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Greeter</span> </span>&#123;
    <span class="hljs-attr">greeting</span>: <span class="hljs-built_in">string</span>;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">message: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.greeting = message;
    &#125;

    <span class="hljs-meta">@validate</span>
    <span class="hljs-function"><span class="hljs-title">greet</span>(<span class="hljs-params"><span class="hljs-meta">@required</span> name: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello "</span> + name + <span class="hljs-string">", "</span> + <span class="hljs-built_in">this</span>.greeting;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们使用下面的函数定义 @required 和 @validate 装饰器：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> <span class="hljs-string">"reflect-metadata"</span>;

<span class="hljs-keyword">const</span> requiredMetadataKey = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"required"</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">required</span>(<span class="hljs-params">target: <span class="hljs-built_in">Object</span>, propertyKey: <span class="hljs-built_in">string</span> | symbol, parameterIndex: <span class="hljs-built_in">number</span></span>) </span>&#123;
    <span class="hljs-keyword">let</span> existingRequiredParameters: <span class="hljs-built_in">number</span>[] = <span class="hljs-built_in">Reflect</span>.getOwnMetadata(requiredMetadataKey, target, propertyKey) || [];
    existingRequiredParameters.push(parameterIndex);
    <span class="hljs-built_in">Reflect</span>.defineMetadata(requiredMetadataKey, existingRequiredParameters, target, propertyKey);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">validate</span>(<span class="hljs-params">target: <span class="hljs-built_in">any</span>, propertyName: <span class="hljs-built_in">string</span>, descriptor: TypedPropertyDescriptor<<span class="hljs-built_in">Function</span>></span>) </span>&#123;
    <span class="hljs-keyword">let</span> method = descriptor.value;
    descriptor.value = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> requiredParameters: <span class="hljs-built_in">number</span>[] = <span class="hljs-built_in">Reflect</span>.getOwnMetadata(requiredMetadataKey, target, propertyName);
        <span class="hljs-keyword">if</span> (requiredParameters) &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> parameterIndex <span class="hljs-keyword">of</span> requiredParameters) &#123;
                <span class="hljs-keyword">if</span> (parameterIndex >= <span class="hljs-built_in">arguments</span>.length || <span class="hljs-built_in">arguments</span>[parameterIndex] === <span class="hljs-literal">undefined</span>) &#123;
                    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Missing required argument."</span>);
                &#125;
            &#125;
        &#125;

        <span class="hljs-keyword">return</span> method.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>@required装饰器添加了元数据实体把参数标记为必需的。 @validate装饰器把greet方法包裹在一个函数里在调用原先的函数前验证函数参数。</p>
<blockquote>
<p>注意  这个例子使用了reflect-metadata库。 查看 元数据了解reflect-metadata库的更多信息。</p>
</blockquote>
<h2 data-id="heading-10">元数据</h2>
<p>一些例子使用了reflect-metadata库来支持实验性的metadata API。 这个库还不是ECMAScript (JavaScript)标准的一部分。 然而，当装饰器被ECMAScript官方标准采纳后，这些扩展也将被推荐给ECMAScript以采纳。</p>
<p>你可以通过npm安装这个库：</p>
<pre><code class="copyable">npm i reflect-metadata --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>TypeScript支持为带有装饰器的声明生成元数据。 你需要在命令行或 tsconfig.json里启用emitDecoratorMetadata编译器选项。</p>
<p>Command Line:</p>
<pre><code class="copyable">tsc --target ES5 --experimentalDecorators --emitDecoratorMetadata
<span class="copy-code-btn">复制代码</span></code></pre>
<p>tsconfig.json:</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"compilerOptions"</span>: &#123;
        <span class="hljs-attr">"target"</span>: <span class="hljs-string">"ES5"</span>,
        <span class="hljs-attr">"experimentalDecorators"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">"emitDecoratorMetadata"</span>: <span class="hljs-literal">true</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当启用后，只要reflect-metadata库被引入了，设计阶段添加的类型信息可以在运行时使用。</p>
<p>如下例所示：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> <span class="hljs-string">"reflect-metadata"</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    y: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Line</span> </span>&#123;
    <span class="hljs-keyword">private</span> _p0: Point;
    <span class="hljs-keyword">private</span> _p1: Point;

    <span class="hljs-meta">@validate</span>
    <span class="hljs-keyword">set</span> <span class="hljs-title">p0</span>(<span class="hljs-params">value: Point</span>) &#123; <span class="hljs-built_in">this</span>._p0 = value; &#125;
    <span class="hljs-keyword">get</span> <span class="hljs-title">p0</span>() &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._p0; &#125;

    <span class="hljs-meta">@validate</span>
    <span class="hljs-keyword">set</span> <span class="hljs-title">p1</span>(<span class="hljs-params">value: Point</span>) &#123; <span class="hljs-built_in">this</span>._p1 = value; &#125;
    <span class="hljs-keyword">get</span> <span class="hljs-title">p1</span>() &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._p1; &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">validate</span><<span class="hljs-title">T</span>>(<span class="hljs-params">target: <span class="hljs-built_in">any</span>, propertyKey: <span class="hljs-built_in">string</span>, descriptor: TypedPropertyDescriptor<T></span>) </span>&#123;
    <span class="hljs-keyword">let</span> set = descriptor.set;
    descriptor.set = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value: T</span>) </span>&#123;
        <span class="hljs-keyword">let</span> <span class="hljs-keyword">type</span> = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-string">"design:type"</span>, target, propertyKey);
        <span class="hljs-keyword">if</span> (!(value <span class="hljs-keyword">instanceof</span> <span class="hljs-keyword">type</span>)) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Invalid type."</span>);
        &#125;
        set(value);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>TypeScript编译器可以通过@Reflect.metadata装饰器注入设计阶段的类型信息。 你可以认为它相当于下面的TypeScript：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Line</span> </span>&#123;
    <span class="hljs-keyword">private</span> _p0: Point;
    <span class="hljs-keyword">private</span> _p1: Point;

    <span class="hljs-meta">@validate</span>
    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-string">"design:type"</span>, Point)
    <span class="hljs-keyword">set</span> <span class="hljs-title">p0</span>(<span class="hljs-params">value: Point</span>) &#123; <span class="hljs-built_in">this</span>._p0 = value; &#125;
    <span class="hljs-keyword">get</span> <span class="hljs-title">p0</span>() &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._p0; &#125;

    <span class="hljs-meta">@validate</span>
    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-string">"design:type"</span>, Point)
    <span class="hljs-keyword">set</span> <span class="hljs-title">p1</span>(<span class="hljs-params">value: Point</span>) &#123; <span class="hljs-built_in">this</span>._p1 = value; &#125;
    <span class="hljs-keyword">get</span> <span class="hljs-title">p1</span>() &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._p1; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意  装饰器元数据是个实验性的特性并且可能在以后的版本中发生破坏性的改变（breaking changes）。</p>
<blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote></div>  
</div>
            