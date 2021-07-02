
---
title: 'TypeScript，从0到入门带你进入类型的世界'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a045cdc9c6a432db0fcf18ab3abf772~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 00:51:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a045cdc9c6a432db0fcf18ab3abf772~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">从0到入门进入TS的世界</h1>
<p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<p>众所周知， <code>js</code> 是一门<strong>弱类型语言</strong>，并且规范较少。这就很容易导致在项目上线之前我们很难发现到它的错误，等到项目一上线，浑然不觉地， <code>bug</code> 就<strong>UpUp</strong>了。于是，在过去的这两年， <code>ts</code> 悄悄的崛起了。</p>
<p>周一随着一波热潮，也开始进入了 <code>ts</code> 的世界，不得不感叹 <code>ts</code> 的静态美。</p>
<p>下面的文章中将讲解我对 <code>TS</code> 入门的一些归纳总结。一起来了解一下吧！</p>
<h1 data-id="heading-1">一、什么是TypeScript？</h1>
<h2 data-id="heading-2">1、编程语言的类型</h2>













<table><thead><tr><th align="center">动态类型语言（Dynamic Typed Language）</th><th align="center">静态类型语言（Statically Typed Langeage）</th></tr></thead><tbody><tr><td align="center">JavaScript</td><td align="center">C,C++,C#,JAVA</td></tr></tbody></table>
<h2 data-id="heading-3">2、TypeScript究竟是什么？</h2>
<ul>
<li>
<p>Typescript，即 <code>Javascript that scales</code> ；</p>
</li>
<li>
<p><code>ts</code> 把不看重类型的动态语言 <code>JS</code> 转变成<strong>关注类型的静态语言</strong>；</p>
</li>
<li>
<p>可以说ts是<strong>静态类型风格的类型系统</strong>；</p>
</li>
<li>
<p>从 <code>es6</code> 到 <code>es10</code> 甚至是 <code>esnext</code> 的语法支持；</p>
</li>
<li>
<p>兼容各种浏览器，各种系统，各种服务器，完全开源。</p>
</li>
</ul>
<h1 data-id="heading-4">二、为什么要学习TypeScript？</h1>
<h2 data-id="heading-5">1、程序更容易理解</h2>
<p>动态语言存在<strong>函数或者方法中其输入输出的参数类型</strong>等问题，同时，动态语言还受到各种各样的约束，比如需要<strong>手动调试</strong>等等。那么有了 <code>ts</code> ，代码本身就可以解决上述问题了， <code>ts</code> 让程序更容易理解，程序理解我们，我们就可以少干很很多事情。</p>
<p>就像我们在与别人交谈时，假如我们逻辑很清晰的表达给对方，对方马上听懂了，并且理解了我们，我们也很省力，不用长篇大论的介绍。</p>
<h2 data-id="heading-6">2、效率更高</h2>
<p><code>ts</code> 可以在在<strong>不同的代码块和定义</strong>中进行跳转，并且<strong>代码有补全功能</strong>。</p>
<p>同时， <code>ts</code> 还有丰富的接口提示，可以通过使用 <code>.</code> 来提示所有的接口内容。</p>
<h2 data-id="heading-7">3、更少的错误</h2>
<p><code>ts</code> 在<strong>编程期间</strong>，就可以<strong>发现大部分的错误</strong>。这样就可以杜绝掉一些比较常见的错误，也使得后面程序运行更加通畅。</p>
<h2 data-id="heading-8">4、非常好的包容性</h2>
<p><code>ts</code> 可以完全地减容 <code>Javascript</code> ，同时，如果要引入像 <code>JQuery</code> 之类的<strong>第三方库</strong>时，可以单独<strong>编写类型文件</strong>来引入这些库。</p>
<h2 data-id="heading-9">5、一点小缺点</h2>
<p>相比于 <code>js</code> 来讲， <code>ts</code> 在学习之初，需要去习惯一些规范，短期内会增加一点学习成本。但短期的学习成本增加将会使得在后期的开发当中减少很多不必要的错误和麻烦，间接的也为自己的开发带来很大的益处。</p>
<p>闲谈到此结束，让我们一起来进入 <code>ts</code> 的世界吧！</p>
<h1 data-id="heading-10">三、typescript入门</h1>
<h2 data-id="heading-11">1、如何安装TypeScript</h2>
<pre><code class="hljs language-bash copyable" lang="bash">npm install -g typescript 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">2、查看版本号</h2>
<pre><code class="hljs language-bash copyable" lang="bash">tsc -v
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">四、Typescript数据类型</h1>
<h2 data-id="heading-14">1、原始数据类型和Any类型</h2>
<h3 data-id="heading-15">（1）原始数据类型</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//定义一个布尔值数据</span>
<span class="hljs-keyword">let</span> isDone: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>

<span class="hljs-comment">//定义一个数字类型</span>
<span class="hljs-keyword">let</span> age: <span class="hljs-built_in">number</span> = <span class="hljs-number">20</span>

<span class="hljs-comment">//定义字符串类型</span>
<span class="hljs-keyword">let</span> firstName: <span class="hljs-built_in">string</span> = <span class="hljs-string">'monday'</span>
<span class="hljs-keyword">let</span> message: <span class="hljs-built_in">string</span> = <span class="hljs-string">`Hello, <span class="hljs-subst">$&#123;firstName&#125;</span>`</span>

<span class="hljs-comment">//定义undefind和null类型</span>
<span class="hljs-keyword">let</span> u: <span class="hljs-literal">undefined</span> = <span class="hljs-literal">undefined</span>
<span class="hljs-keyword">let</span> n: <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>

<span class="hljs-comment">//给数字赋值undefid</span>
<span class="hljs-keyword">let</span> num: <span class="hljs-built_in">number</span> = <span class="hljs-literal">undefined</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">（2）Any 类型</h3>
<p>如果我们有时候不能确定一个数据是什么类型的话，那么我们可以用any类型来定义。比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//定义一个any类型数据</span>
<span class="hljs-keyword">let</span> notSure: <span class="hljs-built_in">any</span> = <span class="hljs-number">4</span>
notSure = <span class="hljs-string">'maybe a string'</span>
notSure = <span class="hljs-literal">true</span>

notSure.myName
notSure.getName()

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">2、数组和元组</h2>
<h3 data-id="heading-18">（1）数组</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//声明一个数字类型的数组</span>
<span class="hljs-comment">//注意：后面的数组只能传递数字，传递其他类型的数据都会报错</span>
<span class="hljs-keyword">let</span> arrOfNumbers: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
arrOfNumbers.push(<span class="hljs-number">3</span>)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">//arguments 为类数组</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">（2）元组</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//确定一个元组里面的内容和数量，下面表示确定user这个元组必须且只能接收两个参数</span>
<span class="hljs-comment">//同时第一个属性必须是String类型，第二个属性是Number类型</span>
<span class="hljs-keyword">let</span> user: [<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Number</span>] = [<span class="hljs-string">'abc'</span>, <span class="hljs-number">13</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">3、interface 接口</h2>
<p><strong>interface的定义：</strong></p>
<ul>
<li>对 <code>对象Object</code> 的形状 <code>(shape)</code> 进行描述；</li>
<li>Duck Typing（鸭子类型）。</li>
</ul>
<p><strong>我们来看一段代码：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Person&#123;
    <span class="hljs-comment">// readonly表示只读状态</span>
    <span class="hljs-keyword">readonly</span> id: <span class="hljs-built_in">number</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-comment">//加一个问号表示该参数可选可不选</span>
    age?: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-keyword">let</span> monday: Person = &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'monday'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
&#125;

monday.id = <span class="hljs-number">12323</span>; <span class="hljs-comment">//因为加了readonly，所以此时访问不了，会报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">4、function函数</h2>
<p><strong>function函数是什么：</strong></p>
<ul>
<li>在 <code>JS</code> 中，函数是一等公民。</li>
<li>函数和其他类型的对象都一样，可以作为<strong>参数</strong>，可以<strong>存入数组</strong>，也可以<strong>被另外一个函数返回</strong>，可以被<strong>赋值给另外一个变量</strong>。</li>
<li>函数主要由两个部分组成：<strong>输入（传参）<strong>和</strong>输出（返回结果）</strong>。</li>
</ul>
<p><strong>我们来看个例子：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span>, z?: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span></span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> z === <span class="hljs-string">'number'</span>)&#123;
        <span class="hljs-keyword">return</span> x + y + z;
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">return</span> x + y;
    &#125;
&#125;

<span class="hljs-keyword">let</span> result = add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>);
<span class="hljs-built_in">console</span>.log(result); <span class="hljs-comment">//6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上函数，我们实现了两个树或者三个树的相加操作。此时，需要我们注意的是，<strong>可选参数</strong>后面不能再添加<strong>不确定参数</strong>，否则程序就会发生混乱。<strong>比如：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span>, z?: <span class="hljs-built_in">number</span>, t: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span></span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> z === <span class="hljs-string">'number'</span>)&#123;
        <span class="hljs-keyword">return</span> x + y + z;
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">return</span> x + y;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码中的 <code>t</code> 是肯定不被允许添加的，因为前面已经有了可选参数 <code>z</code> ，而后面又突然健冒出来个 <code>t</code> ，想想都不太合理。</p>
<hr>
<p>到这里，假设我们有一个新的变量名，名字叫 <code>add2</code> 。这个时候我们想要给它一个像 <code>add</code> 函数一样的类型。<strong>那么该怎么处理呢？</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> add2: <span class="hljs-function">(<span class="hljs-params">x:<span class="hljs-built_in">number</span>, y:<span class="hljs-built_in">number</span>, z?: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">number</span> = add
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意上面这个箭头 <code>=></code> 不是 <code>ES6</code> 中的箭头函数，而是 <code>ts</code> 中声明<strong>函数类型返回值</strong>的方法。</p>
<p>上面这个语句中就说明了， <code>add2</code> 返回的值是一个 <code>number</code> 类型数值，并且让它等于 <code>add</code> 函数。同时，要记得的是，在 <code>ts</code> 当中，凡是在 <code>:</code> 后面都是声明在声明类型。</p>
<hr>
<p>上面这样写好像有点冗余，我们来用 <code>interface</code> 来实现同样的效果。</p>
<p>在第3点的 <code>interface</code> 中我们了解到， <code>interface</code> 是对对象的形状进行描述，但值得注意的是， <code>interface</code> 也可以是<strong>对函数的形状进行描述</strong>。我们用代码来实现一下。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> ISum &#123;
    (x: <span class="hljs-built_in">number</span>, <span class="hljs-attr">y</span>: <span class="hljs-built_in">number</span>, z?: <span class="hljs-built_in">number</span>) : <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-keyword">let</span> add2: ISum = add
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上代码，我们看到，用 <code>interface</code> 来封装一个函数的返回值来行，看起来优雅了不少。这里先体会一下， <code>interface</code> 的强大之处，在后面还会继续讲解。</p>
<h2 data-id="heading-22">5、类型推论、联合类型和类型断言</h2>
<h3 data-id="heading-23">（1）类型推论</h3>
<p>有时候我们还没有给一个数据定义类型，就直接给它赋值了。这个时候我们要怎么来判断呢。这个数据的类型呢？</p>
<p><strong>比如：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> str = <span class="hljs-number">123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当出现这样的情况时，编译器会直接给 <code>str</code> 赋上 <code>number</code> 类型。那么此时如果我们想这么干：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> str = <span class="hljs-number">123</span>
str = <span class="hljs-string">'asd'</span> <span class="hljs-comment">//会报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果当然时不行的。当第一次赋值的时候，编译器就已经给 <code>str</code> 一个 <code>number</code> 类型，认定 <code>str</code> 就是 <code>number</code> 类型。而后我们还想要给 <code>str</code> 赋值上一个 <code>string</code> 类型的数据，肯定是会报错的。</p>
<h3 data-id="heading-24">（2）联合类型</h3>
<p>有时候我们对一个数据的类型不够确定，比如说不知道某一个数据它是 <code>number</code> 类型还是 <code>string</code> 类型。这个时候我们就可以用<strong>联合类型</strong>来进行一波操作。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> numberOrString: <span class="hljs-built_in">number</span> | <span class="hljs-built_in">string</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这种方式，我们对我们所定义的属性 <code>numberOrString</code> 进行联合类型操作。</p>
<p>一般情况下，联合类型会结合类型断言来进行使用。接下来我们来讲类型断言。</p>
<h3 data-id="heading-25">（3）类型断言</h3>
<p><strong>1）</strong> 当 <code>TypeScript</code> 不确定一个联合类型的变量到底是哪个类型的时候，我们只能访问此联合类型的所有类型中共有的属性或方法，而有时候呢，我们确实需要<strong>在还不确定类型的时候</strong>就访问其中一个类型特有的属性或方法。因此我们采用<strong>类型断言</strong>的方式将其指定为一个类型。（这么做只是先欺骗了 <code>ts</code> ，让其信任我们所指定的类型）</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> str = <span class="hljs-number">123</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getLength</span>(<span class="hljs-params">input: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span></span>) : <span class="hljs-title">number</span></span>&#123;
    <span class="hljs-comment">// 用as对input进行类型断言,先给input指定一个类型，后面判断不是再进行转换</span>
    <span class="hljs-comment">//注意:类型断言只做类型选择,而不做类型转换</span>
    <span class="hljs-keyword">const</span> str = input <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> str)
    <span class="hljs-keyword">if</span>(str.length)&#123;
        <span class="hljs-keyword">return</span> str.length
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">const</span> <span class="hljs-built_in">number</span> = input <span class="hljs-keyword">as</span> <span class="hljs-built_in">number</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">number</span>.toString().length
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2）</strong> 看到这里，已经开始感觉到类型断言的神奇之处。但用上面这种方法感觉好像还有一点点冗余，于是我们引入一个 <code>type guard</code> ，即<strong>类型守护</strong>。我们来看下实现方式。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> str = <span class="hljs-number">123</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getLength2</span>(<span class="hljs-params">input: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span></span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> input === <span class="hljs-string">'string'</span>)&#123;
        <span class="hljs-keyword">return</span> input.length
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">return</span> input.toString().length
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-26">五、Typescript中的类：class</h1>
<p>在 <code>js</code> 中我们用了构造函数和原型链的方式来实现继承，同时在 <code>ES6</code> 中出现了 <code>class</code> 类继承的方法。那在 <code>typescript</code> 中呢，继承的方法又更加丰富了。让我们一起来一探究竟吧！</p>
<h2 data-id="heading-27">1、类的定义</h2>
<p>我们先来看下类的定义。</p>
<h3 data-id="heading-28">（1）类（Class）</h3>
<p>类定义了<strong>一切事物</strong>的抽象特点，包含它的属性和方法。<strong>比如：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-comment">// 构造函数是实例化执行时候的逻辑</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name
    &#125;
    <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> is running`</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>阅读以上代码我们可以知道，通过 <code>class</code> 可以定义一个<strong>类</strong>。</p>
<h3 data-id="heading-29">（2）对象（Object）</h3>
<p>对象 <code>Object</code> ，就是<strong>类的实例</strong>。<strong>举个例子：</strong> 🙆‍♂️</p>
<p>我们可以把类 <code>class</code> 比喻成一张<strong>蓝图</strong>，比如说汽车是一个 <code>class</code> ，那么它就像是一张造汽车的图纸。第二个是 <code>Object </code>， <code>Object</code> 通过 <code>new</code> 生成，那么前面有了汽车的蓝图，我们现在就可以创造实实在在的汽车了。我们可以说一辆特斯拉是汽车的实例，也可以说宝马是汽车的另外一个实例。</p>
<p>同样我们用上面的例子来做衍生。<strong>具体如下：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-comment">// 构造函数是实例化执行时候的逻辑</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name
    &#125;
    <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> is running`</span>
    &#125;
&#125;
<span class="hljs-keyword">const</span> snake = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'lily'</span>)
<span class="hljs-built_in">console</span>.log(snake.run())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>阅读以上代码我们可以知道，我们定义了一个 <code>snake</code> ，这个 <code>snake</code> 继承了 <code>Animal</code> 类，因此它就可以用 <code>Animal</code> 类的<strong>属性</strong>和<strong>方法</strong>。</p>
<p><strong>此时打印结果如下：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a045cdc9c6a432db0fcf18ab3abf772~tplv-k3u1fbpfcp-zoom-1.image" alt="实例" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-30">（3）面向对象（OOP）的三大特性</h3>
<p>面向对象的三大特性分别为：<strong>封装</strong>、<strong>继承</strong>、<strong>多态</strong> 。</p>
<ul>
<li><strong>封装：</strong> 指将数据的<strong>操作细节</strong>隐藏起来，只暴露对外的接口。那这样子的话，对于外界的调用端来说，他们不需要也不可能知道细节，只能通过<strong>对外的接口</strong>来访问该对象。</li>
<li><strong>继承：</strong> 子类可以继承父类，子类除了拥有父类的所有特征外，还会拥有一些<strong>更具体的特性</strong>。</li>
<li><strong>多态：</strong> 由继承产生的相关不同的类，<strong>对同一个方法可以有不同的响应</strong>。比如，猫和狗，他们都可以继承 <code>Animal</code> 类，但是他们分别实现 <code>run()</code> 方法，此时呢，针对某一个实例，我们无需了解它是猫还是狗，这个时候可以直接调用 <code>run()</code> ，程序会自动判断出来，应该如何去执行这个方法。</li>
</ul>
<p>同样，我们用上面的代码做衍生，来看<strong>继承</strong>和<strong>多态</strong>是怎么样的。</p>
<hr>
<p><strong>继承：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-comment">// 构造函数是实例化执行时候的逻辑</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name
    &#125;
    <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> is running`</span>
    &#125;
&#125;
<span class="hljs-keyword">const</span> snake = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'lily'</span>)
<span class="hljs-comment">// console.log(snake.run())</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">bark</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> is barking`</span>
    &#125;
&#125;

<span class="hljs-keyword">const</span> xiaoqi = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">'xiaoqi'</span>)
<span class="hljs-built_in">console</span>.log(xiaoqi.run())
<span class="hljs-built_in">console</span>.log(xiaoqi.bark())

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>此时打印结果如下：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d12e1dcabcf4b2ba585cc10929cf254~tplv-k3u1fbpfcp-zoom-1.image" alt="继承" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面可以看到， <code>Dog</code> 继承了 <code>Animal</code> 类，此时 <code>Dog</code> 就拥有了 <code>Animal</code> 类的属性和方法。而 <code>xiaoqi</code> 实例化了 <code>Dog</code> ，因此它也拥有 <code>Dog</code> 的属性和方法。</p>
<hr>
<p><strong>多态：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-comment">// 构造函数是实例化执行时候的逻辑</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name
    &#125;
    <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> is running`</span>
    &#125;
&#125;
<span class="hljs-keyword">const</span> snake = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'lily'</span>)
<span class="hljs-comment">// console.log(snake.run())</span>
<span class="hljs-comment">//-----------------------------------</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">bark</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> is barking`</span>
    &#125;
&#125;

<span class="hljs-keyword">const</span> xiaoqi = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">'xiaoqi'</span>)
<span class="hljs-built_in">console</span>.log(xiaoqi.run())
<span class="hljs-built_in">console</span>.log(xiaoqi.bark())
<span class="hljs-comment">//-----------------------------------</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-comment">// 静态方法不需要进行实例化，直接在类上调用即可</span>
    <span class="hljs-keyword">static</span> categories = [<span class="hljs-string">'mammal'</span>]
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-built_in">super</span>(name)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
    &#125;
    <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`Meow, `</span> + <span class="hljs-built_in">super</span>.run() 
    &#125;
&#125;
<span class="hljs-keyword">const</span> maomao = <span class="hljs-keyword">new</span> Cat(<span class="hljs-string">'maomao'</span>)
<span class="hljs-built_in">console</span>.log(maomao.run())
<span class="hljs-comment">// 直接访问静态属性</span>
<span class="hljs-comment">// 为什么要有静态属性？当定义和实例没有太大关系时，可以考虑使用静态方法实现</span>
<span class="hljs-built_in">console</span>.log(Cat.categories)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>此时打印结果如下：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/430d2f29203f425bb890682ea072a5be~tplv-k3u1fbpfcp-zoom-1.image" alt="多态" loading="lazy" referrerpolicy="no-referrer"></p>
<p>阅读代码我们可以发现， <code>xiaoqi</code> 继承了 <code>dog </code> 的 <code>run()</code> 方法，而 <code>Cat</code> 继承了 <code>Animal</code> 类，但是它对 <code>run()</code> 方法进行了改写，因此最终的 <code>run()</code> 方法为改写后的效果。</p>
<p>所以， <code>maomao</code> 继承了 <code>Cat</code> 类，最后 <code>maomao</code> 调用 <code>run()</code> 方法时，就会调用 <code>Cat</code> 里面改写的 <code>run()</code> 方法，而不是 <code>Animal</code> 类的 <code>run()</code> 方法。</p>
<p>这样， <code>xiaoqi</code> 和 <code>maomao</code> 虽然同样继承自 <code>Animal</code> 类，但他们调用 <code>run()</code> 方法的结果各自相互独立，如此，就实现了多态。</p>
<p>同时，我们还要注意一个点，就是静态属性。大家可以看到上面定义的 <code>categories</code> ，用了 <code>static</code> 来定义它为静态属性。当把变量定义为静态属性时，则当外部需要该静态方法时，不需要进行实例化，之类在类上调用即可。</p>
<p>那么问题来了，我们什么时候才需要有静态属性呢？</p>
<p>其实，当定义的内容和实例没有太大关系时，就可以考虑使用<strong>静态方法</strong>。比如<strong>常量的使用</strong>，常量基本是固定的，不会变的，所以我们可以考虑直接使用<strong>静态方法</strong>来获取它。</p>
<h2 data-id="heading-31">2、Typescript中的类</h2>
<p>Typescript是通过什么方式来增强类的呢，typescript一般通过以下<strong>四种修饰符</strong>来增强类：</p>

























<table><thead><tr><th align="center">修饰符</th><th align="center">含义</th></tr></thead><tbody><tr><td align="center">public</td><td align="center">修饰的属性或方法是公有的</td></tr><tr><td align="center">private</td><td align="center">修饰的属性或方法是私有的</td></tr><tr><td align="center">protected</td><td align="center">修饰的属性或方法是受保护的</td></tr><tr><td align="center">readonly</td><td align="center">只能读不能写</td></tr></tbody></table>
<p>有了以上这四种修饰符呢，我们就可以给类的方法和属性进行<strong>权限管理</strong>。为什么要做权限管理呢？因为总有些内容，我们是不愿意暴露给外部使用的，所以需要进行权限管理。</p>
<p>值得注意的是，对于 <code>protected</code> 这个修饰符来说，<strong>只有子类可以访问父类的属性和方法</strong>，<strong>其他实例都不能访问</strong>。这其实可以把 <code>protected</code> 这个变量理解为<strong>遗产</strong>，父类的东西直接给子女继承，其余外部人员一概不能访问。</p>
<h2 data-id="heading-32">3、类和接口</h2>
<h3 data-id="heading-33">（1）解决什么问题</h3>
<p>继承存在着这样一个困境，在面向对象的世界中，一个类只能继承另外一个类，有时候同类之间有一些共同的特性，但是使用子类来继承父类又很难完成。于是接口就出现了。</p>
<h3 data-id="heading-34">（2）如何解决</h3>
<p>类可以使用 <code>implements</code> 来实现接口，怎么做呢？我们可以<strong>把这些相同的特性提取成接口</strong>，然后用 <code>implements</code> 这个<strong>关键字</strong>来实现，这样就大大提高了面向对象的灵活性。</p>
<h3 data-id="heading-35">（3）举个例子</h3>
<p>假如我们现在要让一辆汽车和<strong>一部手机</strong>来实现<strong>打开播放器的功能</strong>，<strong>那么我们会这么实现：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">switchRadio</span>(<span class="hljs-params">trigger: <span class="hljs-built_in">boolean</span></span>)</span>&#123;

    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CellPhone</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">switchRadio</span>(<span class="hljs-params">trigger: <span class="hljs-built_in">boolean</span></span>)</span>&#123;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这样子看起来好像就没有特别雅观。于是我们可以写一个<strong>打开播放器</strong>的接口,然后用 <code>implements</code> 来实现这个功能。<strong>代码如下：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Radio&#123;
switchRadio(trigger: <span class="hljs-built_in">boolean</span>): <span class="hljs-built_in">void</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span> <span class="hljs-title">implements</span> <span class="hljs-title">Radio</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">switchRadio</span>(<span class="hljs-params">trigger: <span class="hljs-built_in">boolean</span></span>)</span>&#123;

    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CellPhone</span> <span class="hljs-title">implements</span> <span class="hljs-title">Radio</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">switchRadio</span>(<span class="hljs-params">trigger: <span class="hljs-built_in">boolean</span></span>)</span>&#123;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，就让Car和CellPhone实现了打开播放器的功能。</p>
<p>接下来，我们继续写一个接口，可以实现检查电池电量的功能。并且让手机不仅可以打开播放器，还可以检查电池电量。<strong>代码如下：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Radio&#123;
    switchRadio(trigger: <span class="hljs-built_in">boolean</span>): <span class="hljs-built_in">void</span>
&#125;

<span class="hljs-keyword">interface</span> Battery&#123;
    checkBatteryStatus(): <span class="hljs-built_in">void</span>
&#125;
    
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span> <span class="hljs-title">implements</span> <span class="hljs-title">Radio</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">switchRadio</span>(<span class="hljs-params">trigger: <span class="hljs-built_in">boolean</span></span>)</span>&#123;

    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CellPhone</span> <span class="hljs-title">implements</span> <span class="hljs-title">Radio</span>,<span class="hljs-title">Battery</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">switchRadio</span>(<span class="hljs-params">trigger: <span class="hljs-built_in">boolean</span></span>)</span>&#123;

    &#125;
    <span class="hljs-function"><span class="hljs-title">checkBatteryStatus</span>(<span class="hljs-params"></span>)</span>&#123;
        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>阅读代码我们可以发现，我们要给继承两个接口 <code>Radio,Battery</code> ，这样看似乎还有点冗余。于是我们可以这样实现：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Radio&#123;
    switchRadio(trigger: <span class="hljs-built_in">boolean</span>): <span class="hljs-built_in">void</span>
&#125;

<span class="hljs-keyword">interface</span> RadioWithBattery <span class="hljs-keyword">extends</span> Radio&#123;
    checkBatteryStatus(): <span class="hljs-built_in">void</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span> <span class="hljs-title">implements</span> <span class="hljs-title">Radio</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">switchRadio</span>(<span class="hljs-params">trigger: <span class="hljs-built_in">boolean</span></span>)</span>&#123;

    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CellPhone</span> <span class="hljs-title">implements</span> <span class="hljs-title">RadioWithBattery</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">switchRadio</span>(<span class="hljs-params">trigger: <span class="hljs-built_in">boolean</span></span>)</span>&#123;

    &#125;
    <span class="hljs-function"><span class="hljs-title">checkBatteryStatus</span>(<span class="hljs-params"></span>)</span>&#123;
        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <code>interface</code> 继承 <code>interface</code> ，最终用 <code>implement</code> 去抽象和验证<strong>类的属性和方法</strong>，达到抽离功能的目的。</p>
<p>相信通过以上的简单了解，大家能感受到一点 <code>interface</code> 的奇妙之处。</p>
<h1 data-id="heading-36">六、枚举</h1>
<h2 data-id="heading-37">1、普通枚举</h2>
<p>枚举常使用于我们在程序中需要做权限管理或者做判断时等各种场景。枚举比较简单，<strong>下面直接用代码演示：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Direction&#123;
    Up,
    Down,
    Left,
    Right
&#125;

<span class="hljs-built_in">console</span>.log(Direction.Up) <span class="hljs-comment">//0</span>
<span class="hljs-built_in">console</span>.log(Direction.Down) <span class="hljs-comment">//1</span>
<span class="hljs-built_in">console</span>.log(Direction.Left) <span class="hljs-comment">//2</span>
<span class="hljs-built_in">console</span>.log(Direction.Right) <span class="hljs-comment">//3</span>
<span class="hljs-built_in">console</span>.log(Direction[<span class="hljs-number">0</span>]) <span class="hljs-comment">//Up</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了以上基本用法外，我们还可以<strong>给枚举赋值：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Direction&#123;
    Up = <span class="hljs-number">10</span>,
    Down,
    Left,
    Right
&#125;

<span class="hljs-built_in">console</span>.log(Direction.Up) <span class="hljs-comment">//10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-38">2、常量枚举</h2>
<p>我们来定义一个常量，与 <code>enum</code> 做判断。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Direction&#123;
    Up = <span class="hljs-string">'Up'</span>,
    Down = <span class="hljs-string">'Down'</span>,
    Left = <span class="hljs-string">'Left'</span>,
    Right = <span class="hljs-string">'Right'</span>
&#125;

<span class="hljs-comment">//定义一个常量，直接与enum做判断</span>
<span class="hljs-keyword">const</span> value = <span class="hljs-string">'Up'</span>;
<span class="hljs-keyword">if</span>(value === Direction.Up)&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'go Up!'</span>) <span class="hljs-comment">// go Up!</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用常量枚举可以有效地提升性能，<strong>常量</strong>会内联枚举的任何用法，而不会把枚举变成任意的 <code>Javascript</code> 代码。</p>
<p>这样一说，那是不是所有的 <code>enum</code> 都可以使用常量枚举呢？答案自然是否定的。</p>
<p><strong>枚举的值有两种类型</strong>，一种是<strong>常量值枚举</strong>(constant)，一种是<strong>计算值枚举</strong>(computed)。只有<strong>常量值枚举</strong>可以进行<strong>常量枚举</strong>，而<strong>计算值枚举</strong>不能进行<strong>常量枚举</strong>。</p>
<h1 data-id="heading-39">七、泛型</h1>
<p>接下来我们来讲 <code>TypeScript</code> 中最难的一部分，泛型。</p>
<h2 data-id="heading-40">1、普通泛型</h2>
<p><strong>泛型</strong>，即 <code>generics</code> 。指在定义函数、接口或类的时候，我们不预先指定类型，而是在使用的时候再指定类型和其特征。</p>
<p>可以理解为，泛型就相当于一个<strong>占位符</strong>或者是一个<strong>变量</strong>，在使用时再动态的填入进去，填进去以后既可以来确定我们的类型值。</p>
<p><strong>接下来我们用代码来演示一下：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">echo</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span></span>&#123;
    <span class="hljs-keyword">return</span> arg
&#125;

<span class="hljs-keyword">const</span> result = echo(<span class="hljs-literal">true</span>)
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过 <code><></code> 来定义一个未知的泛型，之后当我们给它赋值时，就可以对应值的数据类型。</p>
<hr>
<p>现在我们再用泛型来定义一个 <code>number</code> 类型的数组。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 早期定义一个number类型的数组</span>
<span class="hljs-keyword">let</span> arr: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
<span class="hljs-comment">// 用泛型定义一个number类型的数组</span>
<span class="hljs-keyword">let</span> arrTwo: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>假如我们现在要调换两个元素的位置，那么用泛型我们可以这么实现。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">swap</span><<span class="hljs-title">T</span>, <span class="hljs-title">U</span>>(<span class="hljs-params">tuple: [T, U]</span>): [<span class="hljs-title">U</span>, <span class="hljs-title">T</span>]</span>&#123;
    <span class="hljs-keyword">return</span> [tuple[<span class="hljs-number">1</span>], tuple[<span class="hljs-number">0</span>]]
&#125;

<span class="hljs-keyword">const</span> result2 = swap([<span class="hljs-string">'abc'</span>, <span class="hljs-number">123</span>])
<span class="hljs-built_in">console</span>.log(result2[<span class="hljs-number">0</span>]) <span class="hljs-comment">//123</span>
<span class="hljs-built_in">console</span>.log(result2[<span class="hljs-number">1</span>]) <span class="hljs-comment">//abc</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<strong>泛型</strong>，我们就顺利调换了两个元素的位置。</p>
<h2 data-id="heading-41">2、约束泛型</h2>
<p>在泛型中使用 <code>extends</code> 关键字，就可以让传入值满足我们<strong>特定的约束条件</strong>，而不是毫无理由的随意传入。</p>
<p>比如，我们想要让我们定义的内容是一个<strong>数组</strong>，我们可以这么处理。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">echoWithArr</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T[]</span>): <span class="hljs-title">T</span>[]</span>&#123;
    <span class="hljs-built_in">console</span>.log(arg.length)
    <span class="hljs-keyword">return</span> arg
&#125;
<span class="hljs-keyword">const</span> arrs = echoWithArr([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，就把 <code>arrs</code> 定义为一个数组。</p>
<hr>
<p>假设我们现在想要让我们<strong>定义的内容</strong>可以访问到 <code>length</code> 方法，那么我们需要加一点佐料。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> IWithLength&#123;
    <span class="hljs-attr">length</span>: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">echoWithLength</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">IWithLength</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span></span>&#123;
    <span class="hljs-built_in">console</span>.log(arg.length)
    <span class="hljs-keyword">return</span> arg
&#125;

<span class="hljs-keyword">const</span> str = echoWithLength(<span class="hljs-string">'str'</span>)
<span class="hljs-keyword">const</span> obj = echoWithLength(&#123; <span class="hljs-attr">length</span>: <span class="hljs-number">10</span>, <span class="hljs-attr">width</span>: <span class="hljs-number">20</span> &#125;)
<span class="hljs-keyword">const</span> arr2 = echoWithLength([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <code>extends</code> 关键字来继承特定的 <code>interface</code> ，使得我们定义的内容 <code>str</code> ， <code>obj</code> ，<code>arr2</code> 达到可以访问length方法的目的。</p>
<p>通过以上举例，我们可以知道，泛型可以用来灵活的<strong>约束参数的类型</strong>，参数不需要是个特别死板的类型，而可以通过我们的约束来达到我们想要的目的。</p>
<h2 data-id="heading-42">3、泛型在类和接口中的使用</h2>
<h3 data-id="heading-43">（1）泛型在类中的使用</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Queue</span><<span class="hljs-title">T</span>></span>&#123;
    <span class="hljs-keyword">private</span> data = []
    <span class="hljs-function"><span class="hljs-title">push</span>(<span class="hljs-params">item: T</span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.data.push(item)
    &#125;
    pop(): T&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.data.shift()
    &#125;
&#125;
<span class="hljs-comment">// 确定这是一个number类型的队列</span>
<span class="hljs-keyword">const</span> queue = <span class="hljs-keyword">new</span> Queue<<span class="hljs-built_in">number</span>>()
queue.push(<span class="hljs-number">1</span>)
<span class="hljs-built_in">console</span>.log(queue.pop().toFixed())
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">（2）泛型在接口中的使用</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> KeyPair<T, U>&#123;
    <span class="hljs-attr">key</span>: T
    <span class="hljs-attr">value</span>: U
&#125;
<span class="hljs-keyword">let</span> kp1: KeyPair<<span class="hljs-built_in">number</span>, <span class="hljs-built_in">string</span>> = &#123;<span class="hljs-attr">key</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'str'</span>&#125;
<span class="hljs-keyword">let</span> kp2: KeyPair<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">number</span>> = &#123;<span class="hljs-attr">key</span>: <span class="hljs-string">'str'</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">2</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上代码演示可以发现，泛型就像是创建了一个<strong>拥有特定类型的容器</strong>，就仿佛给一个<strong>容器</strong>贴上标签一样。</p>
<h1 data-id="heading-45">八、类型别名</h1>
<h2 data-id="heading-46">1、类型别名</h2>
<p><strong>类型别名</strong>，即 <code>type aliase</code> 。类型别名可以看作是一个<strong>快捷方式</strong>，可以把一个写起来很繁琐的类型创建一个简单的写法。<strong>比如：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//用以下这种写法，每次都要写一长串的(x: number, y: number) => number</span>
<span class="hljs-keyword">let</span> sum: <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">number</span>
<span class="hljs-keyword">const</span> result = sum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>)

<span class="hljs-comment">//用type给类型进行别名</span>
<span class="hljs-keyword">type</span> PlusType = <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">number</span>
<span class="hljs-keyword">let</span> sum2: PlusType
<span class="hljs-keyword">const</span> result2 = sum2(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>)

<span class="hljs-comment">//一个类型可以是字符串也可以是数字</span>
<span class="hljs-keyword">type</span> StrOrNumber = <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>
<span class="hljs-keyword">let</span> result3: StrOrNumber = <span class="hljs-string">'123'</span>
result3 = <span class="hljs-number">123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-47">2、字符串字面量</h2>
<p><strong>字符串字面量</strong>，指可以提供一系列非常方便使用的<strong>常量写法</strong>。<strong>比如：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> str: <span class="hljs-string">'name'</span> = <span class="hljs-string">'name'</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">number</span>: <span class="hljs-number">1</span> = <span class="hljs-number">1</span>
<span class="hljs-keyword">type</span> Direction = <span class="hljs-string">'Up'</span> | <span class="hljs-string">'Down'</span> | <span class="hljs-string">'Left'</span> | <span class="hljs-string">'Right'</span>
<span class="hljs-keyword">let</span> toWhere: Direction = <span class="hljs-string">'Left'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-48">3、交叉类型</h2>
<p><strong>交叉类型</strong>，使用 <code>type</code> 这个<strong>扩展对象</strong>的一种方式。<strong>比如：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> IName&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
&#125;
<span class="hljs-keyword">type</span> IPerson = IName & &#123;<span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>&#125;
<span class="hljs-keyword">let</span> person: IPerson = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'monday'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-49">九、声明文件</h1>
<p>我们在写ts时，难免会有遇到要引入第三方库的时候。这个时候就需要ts来做特殊处理。<strong>主要有以下两种做法：</strong></p>
<h2 data-id="heading-50">1、 .d.ts 文件引入</h2>
<p>假设我们要引入JQuery库来使用，那么我们可以在外部新增一个 <code>JQuery.d.ts</code> 文件，<strong>文件内代码如下：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-keyword">var</span> JQuery: <span class="hljs-function">(<span class="hljs-params">selector: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">any</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后便可以在我们定义的 <code>ts</code> 文件下引用 <code>JQuery</code> 相关库的内容。<strong>比如：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts">jQuery(<span class="hljs-string">'#foo'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-51">2、npm安装</h2>
<p>我们也可以安装对应的第三方库的 <code>npm</code> 包。假如我们现在要引入一个 <code>JQuery</code> 库，那么我们可以这么处理。</p>
<pre><code class="hljs language-ts copyable" lang="ts">npm install --save <span class="hljs-meta">@type</span>/jquery
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-52">十、内置类型</h1>
<p>我们在写 <code>ts</code> 代码时，其实不知不觉已经使用了很多的<strong>内置对象</strong>。对象呢，是指根据标准（标准指 <code>ECMA</code> 、 <code>DOM</code> 等标准），在全局作用域 <code>global</code> 上面存在的对象。那我们在运行 <code>tsc</code> 时，这些内置的对象就会被当作附加的礼物给程序加载进行。接下来我们来体会一下几种常见的内置对象。</p>
<p><strong>全局对象：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// global object 全局对象</span>
<span class="hljs-keyword">const</span> a: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
<span class="hljs-keyword">const</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
date.getTime()
<span class="hljs-keyword">const</span> reg = <span class="hljs-regexp">/abc/</span>
reg.test(<span class="hljs-string">'abc'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>内置对象：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// build-in object 内置对象</span>
<span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">2</span>, <span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>DOM和BOM对象：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// DOM 和 BOM</span>
<span class="hljs-keyword">let</span> body = <span class="hljs-built_in">document</span>.body
<span class="hljs-keyword">let</span> allLis = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'li'</span>)
allLis.keys()

<span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
    e.preventDefault()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>功能性类型：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Utility Types 功能性类型</span>
<span class="hljs-keyword">interface</span> IPerson&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-keyword">let</span> monday: IPerson = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'monday'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>&#125;

<span class="hljs-comment">//可选属性</span>
<span class="hljs-keyword">type</span> IPartial = Partial<IPerson>
<span class="hljs-keyword">let</span> monday2: Ipartial = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'monday'</span>&#125;

<span class="hljs-comment">//移除某一个属性</span>
<span class="hljs-keyword">type</span> Omit = Omit<IPerson, <span class="hljs-string">'name'</span>>
<span class="hljs-keyword">let</span> monday3: Omit = &#123;<span class="hljs-attr">age</span>: <span class="hljs-number">20</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-53">十一、结束语</h1>
<p>关于 <code>ts</code> 的入门讲到这里就结束啦！希望大家能对 <code>ts</code> 有一个简单的认识！</p>
<p>如本文有不理解或有误的地方欢迎评论区留言或公众号后台加我微信交流~</p>
<blockquote>
<ul>
<li>关注公众号 <strong>星期一研究室</strong> ，第一时间关注学习干货，更多精选专栏待你解锁~</li>
<li>如果这篇文章对你有用，记得<strong>点个赞加个关注</strong>再走哦~</li>
<li>我们下期见！🥂🥂🥂</li>
</ul>
</blockquote></div>  
</div>
            