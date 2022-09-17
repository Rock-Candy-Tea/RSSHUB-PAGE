
---
title: 'Javascript装饰器的妙用'
categories: 
 - 编程
 - 掘金
 - 收藏集
headimg: 'https://picsum.photos/400/300?random=5906'
author: 掘金
comments: false
date: Sun, 08 Jul 2018 17:28:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=5906'
---

<div>   
<div class="markdown-body cache html"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近新开了一个Node项目，采用TypeScript来开发，在数据库及路由管理方面用了不少的装饰器，发觉这的确是一个好东西。<br>
装饰器是一个还处于草案中的特性，目前木有直接支持该语法的环境，但是可以通过 babel 之类的进行转换为旧语法来实现效果，所以在TypeScript中，可以放心的使用<code>@Decorator</code>。</p>

<h2 data-id="heading-0">什么是装饰器</h2>
<p>装饰器是对类、函数、属性之类的一种装饰，可以针对其添加一些额外的行为。<br>
通俗的理解可以认为就是在原有代码外层包装了一层处理逻辑。<br>
个人认为装饰器是一种解决方案，而并非是狭义的<code>@Decorator</code>，后者仅仅是一个语法糖罢了。</p>
<p>装饰器在身边的例子随处可见，一个简单的例子，水龙头上边的起泡器就是一个装饰器，在装上以后就会把空气混入水流中，掺杂很多泡泡在水里。<br>
但是起泡器安装与否对水龙头本身并没有什么影响，即使拆掉起泡器，也会照样工作，水龙头的作用在于阀门的控制，至于水中掺不掺杂气泡则不是水龙头需要关心的。</p>
<p>所以，对于装饰器，可以简单地理解为是非侵入式的行为修改。</p>
<h2 data-id="heading-1">为什么要用装饰器</h2>
<p>可能有些时候，我们会对传入参数的类型判断、对返回值的排序、过滤，对函数添加节流、防抖或其他的功能性代码，基于多个类的继承，各种各样的与函数逻辑本身无关的、重复性的代码。</p>
<h3 data-id="heading-2">函数中的作用</h3>
<p>可以想像一下，我们有一个工具类，提供了一个获取数据的函数：</p>
<pre><code lang="python" class="hljs language-python copyable"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Model1</span> &#123;
  getData() &#123;
    // 此处省略获取数据的逻辑
    <span class="hljs-keyword">return</span> [&#123;
      <span class="hljs-built_in">id</span>: <span class="hljs-number">1</span>,
      name: <span class="hljs-string">'Niko'</span>
    &#125;, &#123;
      <span class="hljs-built_in">id</span>: <span class="hljs-number">2</span>,
      name: <span class="hljs-string">'Bellic'</span>
    &#125;]
  &#125;
&#125;

console.log(new Model1().getData())     // [ &#123; <span class="hljs-built_in">id</span>: <span class="hljs-number">1</span>, name: <span class="hljs-string">'Niko'</span>&#125;, &#123; <span class="hljs-built_in">id</span>: <span class="hljs-number">2</span>, name: <span class="hljs-string">'Bellic'</span> &#125; ]
console.log(Model1.prototype.getData()) // [ &#123; <span class="hljs-built_in">id</span>: <span class="hljs-number">1</span>, name: <span class="hljs-string">'Niko'</span>&#125;, &#123; <span class="hljs-built_in">id</span>: <span class="hljs-number">2</span>, name: <span class="hljs-string">'Bellic'</span> &#125; ]
<span class="copy-code-btn">复制代码</span></code></pre><p>现在我们想要添加一个功能，记录该函数执行的耗时。<br>
因为这个函数被很多人使用，在调用方添加耗时统计逻辑是不可取的，所以我们要在<code>Model1</code>中进行修改：</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Model1</span> &#123;
  <span class="hljs-title function_">getData</span>(<span class="hljs-params"></span>) &#123;
+   <span class="hljs-keyword">let</span> start = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">valueOf</span>()
+   <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// 此处省略获取数据的逻辑</span>
      <span class="hljs-keyword">return</span> [&#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Niko'</span>
      &#125;, &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Bellic'</span>
      &#125;]
+   &#125; <span class="hljs-keyword">finally</span> &#123;
+     <span class="hljs-keyword">let</span> end = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">valueOf</span>()
+     <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`start: <span class="hljs-subst">$&#123;start&#125;</span> end: <span class="hljs-subst">$&#123;end&#125;</span> consume: <span class="hljs-subst">$&#123;end - start&#125;</span>`</span>)
+   &#125;
  &#125;
&#125;

<span class="hljs-comment">// start: XXX end: XXX consume: XXX</span>
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-keyword">new</span> <span class="hljs-title class_">Model1</span>().<span class="hljs-title function_">getData</span>())     <span class="hljs-comment">// [ &#123; id: 1, name: 'Niko'&#125;, &#123; id: 2, name: 'Bellic' &#125; ]</span>
<span class="hljs-comment">// start: XXX end: XXX consume: XXX</span>
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-title class_">Model1</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-title function_">getData</span>()) <span class="hljs-comment">// [ &#123; id: 1, name: 'Niko'&#125;, &#123; id: 2, name: 'Bellic' &#125; ]</span>
<span class="copy-code-btn">复制代码</span></code></pre><p>这样在调用方法后我们就可以在控制台看到耗时的输出了。<br>
但是这样直接修改原函数代码有以下几个问题：</p>
<ol>
<li>统计耗时的相关代码与函数本身逻辑并无一点关系，影响到了对原函数本身的理解，对函数结构造成了破坏性的修改</li>
<li>如果后期还有更多类似的函数需要添加统计耗时的代码，在每个函数中都添加这样的代码显然是低效的，维护成本太高</li>
</ol>
<p>所以，为了让统计耗时的逻辑变得更加灵活，我们将创建一个新的工具函数，用来包装需要设置统计耗时的函数。<br>
通过将<code>Class</code>与目标函数的<code>name</code>传递到函数中，实现了通用的耗时统计：</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-keyword">function</span> <span class="hljs-title function_">wrap</span>(<span class="hljs-params">Model, key</span>) &#123;
  <span class="hljs-comment">// 获取Class对应的原型</span>
  <span class="hljs-keyword">let</span> target = <span class="hljs-title class_">Model</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>

  <span class="hljs-comment">// 获取函数对应的描述符</span>
  <span class="hljs-keyword">let</span> descriptor = <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">getOwnPropertyDescriptor</span>(target, key)

  <span class="hljs-comment">// 生成新的函数，添加耗时统计逻辑</span>
  <span class="hljs-keyword">let</span> log = <span class="hljs-keyword">function</span> (<span class="hljs-params">...arg</span>) &#123;
    <span class="hljs-keyword">let</span> start = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">valueOf</span>()
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">return</span> descriptor.<span class="hljs-property">value</span>.<span class="hljs-title function_">apply</span>(<span class="hljs-variable language_">this</span>, arg) <span class="hljs-comment">// 调用之前的函数</span>
    &#125; <span class="hljs-keyword">finally</span> &#123;
      <span class="hljs-keyword">let</span> end = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">valueOf</span>()
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`start: <span class="hljs-subst">$&#123;start&#125;</span> end: <span class="hljs-subst">$&#123;end&#125;</span> consume: <span class="hljs-subst">$&#123;end - start&#125;</span>`</span>)
    &#125;
  &#125;

  <span class="hljs-comment">// 将修改后的函数重新定义到原型链上</span>
  <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(target, key, &#123;
    ...descriptor,
    <span class="hljs-attr">value</span>: log      <span class="hljs-comment">// 覆盖描述符重的value</span>
  &#125;)
&#125;

<span class="hljs-title function_">wrap</span>(<span class="hljs-title class_">Model1</span>, <span class="hljs-string">'getData'</span>)
<span class="hljs-title function_">wrap</span>(<span class="hljs-title class_">Model2</span>, <span class="hljs-string">'getData'</span>)

<span class="hljs-comment">// start: XXX end: XXX consume: XXX</span>
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-keyword">new</span> <span class="hljs-title class_">Model1</span>().<span class="hljs-title function_">getData</span>())     <span class="hljs-comment">// [ &#123; id: 1, name: 'Niko'&#125;, &#123; id: 2, name: 'Bellic' &#125; ]</span>
<span class="hljs-comment">// start: XXX end: XXX consume: XXX</span>
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-title class_">Model2</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-title function_">getData</span>()) <span class="hljs-comment">// [ &#123; id: 1, name: 'Niko'&#125;, &#123; id: 2, name: 'Bellic' &#125; ]</span>
<span class="copy-code-btn">复制代码</span></code></pre><p>接下来，我们想控制其中一个<code>Model</code>的函数不可被其他人修改覆盖，所以要添加一些新的逻辑：</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-keyword">function</span> <span class="hljs-title function_">wrap</span>(<span class="hljs-params">Model, key</span>) &#123;
  <span class="hljs-comment">// 获取Class对应的原型</span>
  <span class="hljs-keyword">let</span> target = <span class="hljs-title class_">Model</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>

  <span class="hljs-comment">// 获取函数对应的描述符</span>
  <span class="hljs-keyword">let</span> descriptor = <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">getOwnPropertyDescriptor</span>(target, key)

  <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(target, key, &#123;
    ...descriptor,
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">false</span>      <span class="hljs-comment">// 设置属性不可被修改</span>
  &#125;)
&#125;

<span class="hljs-title function_">wrap</span>(<span class="hljs-title class_">Model1</span>, <span class="hljs-string">'getData'</span>)

<span class="hljs-title class_">Model1</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">getData</span> = <span class="hljs-number">1</span> <span class="hljs-comment">// 无效</span>
<span class="copy-code-btn">复制代码</span></code></pre><p>可以看出，两个<code>wrap</code>函数中有不少重复的地方，而修改程序行为的逻辑，实际上依赖的是<code>Object.defineProperty</code>中传递的三个参数。<br>
所以，我们针对<code>wrap</code>在进行一次修改，将其变为一个通用类的转换：</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-keyword">function</span> <span class="hljs-title function_">wrap</span>(<span class="hljs-params">decorator</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">function</span> (<span class="hljs-params">Model, key</span>) &#123;
    <span class="hljs-keyword">let</span> target = <span class="hljs-title class_">Model</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>
    <span class="hljs-keyword">let</span> dscriptor = <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">getOwnPropertyDescriptor</span>(target, key)

    <span class="hljs-title function_">decorator</span>(target, key, descriptor)
  &#125;
&#125;

<span class="hljs-keyword">let</span> log = <span class="hljs-keyword">function</span> (<span class="hljs-params">target, key, descriptor</span>) &#123;
  <span class="hljs-comment">// 将修改后的函数重新定义到原型链上</span>
  <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(target, key, &#123;
    ...descriptor,
    <span class="hljs-attr">value</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">...arg</span>) &#123;
      <span class="hljs-keyword">let</span> start = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">valueOf</span>()
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">return</span> descriptor.<span class="hljs-property">value</span>.<span class="hljs-title function_">apply</span>(<span class="hljs-variable language_">this</span>, arg) <span class="hljs-comment">// 调用之前的函数</span>
      &#125; <span class="hljs-keyword">finally</span> &#123;
        <span class="hljs-keyword">let</span> end = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">valueOf</span>()
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`start: <span class="hljs-subst">$&#123;start&#125;</span> end: <span class="hljs-subst">$&#123;end&#125;</span> consume: <span class="hljs-subst">$&#123;end - start&#125;</span>`</span>)
      &#125;
    &#125;
  &#125;)
&#125;

<span class="hljs-keyword">let</span> seal = <span class="hljs-keyword">function</span> (<span class="hljs-params">target, key, descriptor</span>) &#123;
  <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(target, key, &#123;
    ...descriptor,
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">false</span>
  &#125;)
&#125;

<span class="hljs-comment">// 参数的转换处理</span>
log = <span class="hljs-title function_">wrap</span>(log)
seal = <span class="hljs-title function_">warp</span>(seal)

<span class="hljs-comment">// 添加耗时统计</span>
<span class="hljs-title function_">log</span>(<span class="hljs-title class_">Model1</span>, <span class="hljs-string">'getData'</span>)
<span class="hljs-title function_">log</span>(<span class="hljs-title class_">Model2</span>, <span class="hljs-string">'getData'</span>)

<span class="hljs-comment">// 设置属性不可被修改</span>
<span class="hljs-title function_">seal</span>(<span class="hljs-title class_">Model1</span>, <span class="hljs-string">'getData'</span>)
<span class="copy-code-btn">复制代码</span></code></pre><p>到了这一步以后，我们就可以称<code>log</code>和<code>seal</code>为装饰器了，可以很方便的让我们对一些函数添加行为。<br>
而拆分出来的这些功能可以用于未来可能会有需要的地方，而不用重新开发一遍相同的逻辑。</p>
<h3 data-id="heading-3">Class 中的作用</h3>
<p>就像上边提到了，现阶段在JS中继承多个<code>Class</code>是一件头疼的事情，没有直接的语法能够继承多个 Class。</p>
<pre><code lang="scala" class="hljs language-scala copyable"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123; say () &#123; <span class="hljs-keyword">return</span> <span class="hljs-number">1</span> &#125; &#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> </span>&#123; hi () &#123; <span class="hljs-keyword">return</span> <span class="hljs-number">2</span> &#125; &#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">A</span>, <span class="hljs-title">B</span> </span>&#123;&#125;        <span class="hljs-comment">// Error</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">B</span> </span>&#123;&#125; <span class="hljs-comment">// Error</span>

<span class="hljs-comment">// 这样才是可以的</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> </span>&#123;&#125;
<span class="hljs-keyword">for</span> (let key of <span class="hljs-type">Object</span>.getOwnPropertyNames(<span class="hljs-type">A</span>.prototype)) &#123;
  <span class="hljs-keyword">if</span> (key === 'constructor') <span class="hljs-keyword">continue</span>
  <span class="hljs-type">Object</span>.defineProperty(<span class="hljs-type">C</span>.prototype, key, <span class="hljs-type">Object</span>.getOwnPropertyDescriptor(<span class="hljs-type">A</span>.prototype, key))
&#125;
<span class="hljs-keyword">for</span> (let key of <span class="hljs-type">Object</span>.getOwnPropertyNames(<span class="hljs-type">B</span>.prototype)) &#123;
  <span class="hljs-keyword">if</span> (key === 'constructor') <span class="hljs-keyword">continue</span>
  <span class="hljs-type">Object</span>.defineProperty(<span class="hljs-type">C</span>.prototype, key, <span class="hljs-type">Object</span>.getOwnPropertyDescriptor(<span class="hljs-type">B</span>.prototype, key))
&#125;

let c = <span class="hljs-keyword">new</span> <span class="hljs-type">C</span>()
console.log(c.say(), c.hi()) <span class="hljs-comment">// 1, 2</span>
<span class="copy-code-btn">复制代码</span></code></pre><p>所以，在<code>React</code>中就有了一个<code>mixin</code>的概念，用来将多个<code>Class</code>的功能复制到一个新的<code>Class</code>上。<br>
大致思路就是上边列出来的，但是这个<code>mixin</code>是<code>React</code>中内置的一个操作，我们可以将其转换为更接近装饰器的实现。<br>
在不修改原<code>Class</code>的情况下，将其他<code>Class</code>的属性复制过来：</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-keyword">function</span> <span class="hljs-title function_">mixin</span>(<span class="hljs-params">constructor</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> arg <span class="hljs-keyword">of</span> args) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">of</span> <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">getOwnPropertyNames</span>(arg.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>)) &#123;
        <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'constructor'</span>) <span class="hljs-keyword">continue</span> <span class="hljs-comment">// 跳过构造函数</span>
        <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(constructor.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>, key, <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">getOwnPropertyDescriptor</span>(arg.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>, key))
      &#125;
    &#125;
  &#125;
&#125;

<span class="hljs-title function_">mixin</span>(C)(A, B)

<span class="hljs-keyword">let</span> c = <span class="hljs-keyword">new</span> <span class="hljs-title function_">C</span>()
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(c.<span class="hljs-title function_">say</span>(), c.<span class="hljs-title function_">hi</span>()) <span class="hljs-comment">// 1, 2</span>
<span class="copy-code-btn">复制代码</span></code></pre><p>以上，就是装饰器在函数、<code>Class</code>上的实现方法（至少目前是的），但是草案中还有一颗特别甜的语法糖，也就是<code>@Decorator</code>了。<br>
能够帮你省去很多繁琐的步骤来用上装饰器。</p>
<h2 data-id="heading-4">@Decorator的使用方法</h2>
<p>草案中的装饰器、或者可以说是TS实现的装饰器，将上边的两种进一步地封装，将其拆分成为更细的装饰器应用，目前支持以下几处使用：</p>
<ol>
<li>Class</li>
<li>函数</li>
<li>get set访问器</li>
<li>实例属性、静态函数及属性</li>
<li>函数参数</li>
</ol>
<p>@Decorator的语法规定比较简单，就是通过<code>@</code>符号后边跟一个装饰器函数的引用：</p>
<pre><code lang="scss" class="hljs language-scss copyable"><span class="hljs-keyword">@tag</span>
class A &#123; 
  <span class="hljs-keyword">@method</span>
  hi () &#123;&#125;
&#125;

function <span class="hljs-built_in">tag</span>(constructor) &#123;
  console<span class="hljs-selector-class">.log</span>(constructor === A) <span class="hljs-comment">// true</span>
&#125;

function <span class="hljs-built_in">method</span>(target) &#123;
  console<span class="hljs-selector-class">.log</span>(target.constructor === A, target === A.prototype) <span class="hljs-comment">// true, true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>函数<code>tag</code>与<code>method</code>会在<code>class A</code>定义的时候执行。</p>
<h3 data-id="heading-5">@Decorator 在 Class 中的使用</h3>
<p>该装饰器会在class定义前调用，如果函数有返回值，则会认为是一个新的构造函数来替代之前的构造函数。</p>
<p>函数接收一个参数：</p>
<ol>
<li>constructor 之前的构造函数</li>
</ol>
<p>我们可以针对原有的构造函数进行一些改造:</p>
<h4 data-id="heading-6">新增一些属性</h4>
<p>如果想要新增一些属性之类的，有两种方案可以选择：</p>
<ol>
<li>创建一个新的<code>class</code>继承自原有<code>class</code>，并添加属性</li>
<li>针对当前<code>class</code>进行修改</li>
</ol>
<p>后者的适用范围更窄一些，更接近mixin的处理方式。</p>
<pre><code lang="scala" class="hljs language-scala copyable"><span class="hljs-meta">@name</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  sayHi() &#123;
    console.log(`<span class="hljs-type">My</span> name is: $&#123;<span class="hljs-keyword">this</span>.name&#125;`)
  &#125;
&#125;

<span class="hljs-comment">// 创建一个继承自Person的匿名类</span>
<span class="hljs-comment">// 直接返回并替换原有的构造函数</span>
function name(constructor) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">constructor</span> </span>&#123;
    name = '<span class="hljs-type">Niko</span>'
  &#125;
&#125;

<span class="hljs-keyword">new</span> <span class="hljs-type">Person</span>().sayHi()
<span class="copy-code-btn">复制代码</span></code></pre><h4 data-id="heading-7">修改原有属性的描述符</h4>
<pre><code lang="javascript" class="hljs language-javascript copyable">@seal
<span class="hljs-keyword">class</span> <span class="hljs-title class_">Person</span> &#123;
  <span class="hljs-title function_">sayHi</span>(<span class="hljs-params"></span>) &#123;&#125;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">seal</span>(<span class="hljs-params">constructor</span>) &#123;
  <span class="hljs-keyword">let</span> descriptor = <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">getOwnPropertyDescriptor</span>(constructor.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>, <span class="hljs-string">'sayHi'</span>)
  <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(constructor.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>, <span class="hljs-string">'sayHi'</span>, &#123;
    ...descriptor,
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">false</span>
  &#125;)
&#125;

<span class="hljs-title class_">Person</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">sayHi</span> = <span class="hljs-number">1</span> <span class="hljs-comment">// 无效</span>
<span class="copy-code-btn">复制代码</span></code></pre><h4 data-id="heading-8">使用闭包来增强装饰器的功能</h4>
<blockquote>
<p>在TS文档中被称为装饰器工厂</p>
</blockquote>
<p>因为<code>@</code>符号后边跟的是一个函数的引用，所以对于mixin的实现，我们可以很轻易的使用闭包来实现：</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-keyword">class</span> <span class="hljs-title class_">A</span> &#123; <span class="hljs-title function_">say</span>(<span class="hljs-params"></span>) &#123; <span class="hljs-keyword">return</span> <span class="hljs-number">1</span> &#125; &#125;
<span class="hljs-keyword">class</span> <span class="hljs-title class_">B</span> &#123; <span class="hljs-title function_">hi</span>(<span class="hljs-params"></span>) &#123; <span class="hljs-keyword">return</span> <span class="hljs-number">2</span> &#125; &#125;

@<span class="hljs-title function_">mixin</span>(A, B)
<span class="hljs-keyword">class</span> <span class="hljs-title class_">C</span> &#123; &#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">mixin</span>(<span class="hljs-params">...args</span>) &#123;
  <span class="hljs-comment">// 调用函数返回装饰器实际应用的函数</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">function</span>(<span class="hljs-params">constructor</span>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> arg <span class="hljs-keyword">of</span> args) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">of</span> <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">getOwnPropertyNames</span>(arg.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>)) &#123;
        <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'constructor'</span>) <span class="hljs-keyword">continue</span> <span class="hljs-comment">// 跳过构造函数</span>
        <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(constructor.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>, key, <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">getOwnPropertyDescriptor</span>(arg.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>, key))
      &#125;
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">let</span> c = <span class="hljs-keyword">new</span> <span class="hljs-title function_">C</span>()
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(c.<span class="hljs-title function_">say</span>(), c.<span class="hljs-title function_">hi</span>()) <span class="hljs-comment">// 1, 2</span>
<span class="copy-code-btn">复制代码</span></code></pre><h4 data-id="heading-9">多个装饰器的应用</h4>
<p>装饰器是可以同时应用多个的（不然也就失去了最初的意义）。<br>
用法如下：</p>
<pre><code lang="less" class="hljs language-less copyable"><span class="hljs-variable">@decorator1</span>
<span class="hljs-variable">@decorator2</span>
class &#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>执行的顺序为<code>decorator2</code> -> <code>decorator1</code>，离<code>class</code>定义最近的先执行。<br>
可以想像成函数嵌套的形式：</p>
<pre><code lang="scss" class="hljs language-scss copyable"><span class="hljs-built_in">decorator1</span>(decorator2(class &#123;&#125;))
<span class="copy-code-btn">复制代码</span></code></pre><h3 data-id="heading-10">@Decorator 在 Class 成员中的使用</h3>
<p>类成员上的 @Decorator 应该是应用最为广泛的一处了，函数，属性，<code>get</code>、<code>set</code>访问器，这几处都可以认为是类成员。<br>
在TS文档中被分为了<code>Method Decorator</code>、<code>Accessor Decorator</code>和<code>Property Decorator</code>，实际上如出一辙。</p>
<p>关于这类装饰器，会接收如下三个参数：</p>
<ol>
<li>如果装饰器挂载于静态成员上，则会返回构造函数，如果挂载于实例成员上则会返回类的原型</li>
<li>装饰器挂载的成员名称</li>
<li>成员的描述符，也就是<code>Object.getOwnPropertyDescriptor</code>的返回值</li>
</ol>
<blockquote>
<p><code>Property Decorator</code>不会返回第三个参数，但是可以自己手动获取<br>
前提是静态成员，而非实例成员，因为装饰器都是运行在类创建时，而实例成员是在实例化一个类的时候才会执行的，所以没有办法获取对应的descriptor</p>
</blockquote>
<h4 data-id="heading-11">静态成员与实例成员在返回值上的区别</h4>
<p>可以稍微明确一下，静态成员与实例成员的区别：</p>
<pre><code lang="scss" class="hljs language-scss copyable">class Model &#123;
  <span class="hljs-comment">// 实例成员</span>
  method1 () &#123;&#125;
  method2 = () => &#123;&#125;

  <span class="hljs-comment">// 静态成员</span>
  static method3 () &#123;&#125;
  static method4 = () => &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p><code>method1</code>和<code>method2</code>是实例成员，<code>method1</code>存在于<code>prototype</code>之上，而<code>method2</code>只在实例化对象以后才有。<br>
作为静态成员的<code>method3</code>和<code>method4</code>，两者的区别在于是否可枚举描述符的设置，所以可以简单地认为，上述代码转换为ES5版本后是这样子的：</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-keyword">function</span> <span class="hljs-title function_">Model</span> () &#123;
  <span class="hljs-comment">// 成员仅在实例化时赋值</span>
  <span class="hljs-variable language_">this</span>.<span class="hljs-property">method2</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;&#125;
&#125;

<span class="hljs-comment">// 成员被定义在原型链上</span>
<span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(<span class="hljs-title class_">Model</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>, <span class="hljs-string">'method1'</span>, &#123;
  <span class="hljs-attr">value</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;&#125;, 
  <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>, 
  <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,  <span class="hljs-comment">// 设置不可被枚举</span>
  <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>
&#125;)

<span class="hljs-comment">// 成员被定义在构造函数上，且是默认的可被枚举</span>
<span class="hljs-title class_">Model</span>.<span class="hljs-property">method4</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;&#125;

<span class="hljs-comment">// 成员被定义在构造函数上</span>
<span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(<span class="hljs-title class_">Model</span>, <span class="hljs-string">'method3'</span>, &#123;
  <span class="hljs-attr">value</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;&#125;, 
  <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>, 
  <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,  <span class="hljs-comment">// 设置不可被枚举</span>
  <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre><p>可以看出，只有<code>method2</code>是在实例化时才赋值的，一个不存在的属性是不会有<code>descriptor</code>的，所以这就是为什么TS在针对<code>Property Decorator</code>不传递第三个参数的原因，至于为什么静态成员也没有传递<code>descriptor</code>，目前没有找到合理的解释，但是如果明确的要使用，是可以手动获取的。</p>
<p>就像上述的示例，我们针对四个成员都添加了装饰器以后，<code>method1</code>和<code>method2</code>第一个参数就是<code>Model.prototype</code>，而<code>method3</code>和<code>method4</code>的第一个参数就是<code>Model</code>。</p>
<pre><code lang="less" class="hljs language-less copyable"><span class="hljs-selector-tag">class</span> <span class="hljs-selector-tag">Model</span> &#123;
  <span class="hljs-comment">// 实例成员</span>
  <span class="hljs-variable">@instance</span>
  method1 () &#123;&#125;
  <span class="hljs-variable">@instance</span>
  method2 = () => &#123;&#125;

  <span class="hljs-comment">// 静态成员</span>
  <span class="hljs-variable">@static</span>
  static method3 () &#123;&#125;
  <span class="hljs-variable">@static</span>
  static method4 = () => &#123;&#125;
&#125;

<span class="hljs-selector-tag">function</span> <span class="hljs-selector-tag">instance</span>(target) &#123;
  <span class="hljs-selector-tag">console</span><span class="hljs-selector-class">.log</span>(target.constructor === Model)
&#125;

<span class="hljs-selector-tag">function</span> <span class="hljs-selector-tag">static</span>(target) &#123;
  <span class="hljs-selector-tag">console</span><span class="hljs-selector-class">.log</span>(target === Model)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><h3 data-id="heading-12">函数，访问器，和属性装饰器三者之间的区别</h3>
<h4 data-id="heading-13">函数</h4>
<p>首先是函数，函数装饰器的返回值会默认作为属性的<code>value</code>描述符存在，如果返回值为<code>undefined</code>则会忽略，使用之前的<code>descriptor</code>引用作为函数的描述符。<br>
所以针对我们最开始的统计耗时的逻辑可以这么来做：</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Model</span> &#123;
  @log1
  <span class="hljs-title function_">getData1</span>(<span class="hljs-params"></span>) &#123;&#125;
  @log2
  <span class="hljs-title function_">getData2</span>(<span class="hljs-params"></span>) &#123;&#125;
&#125;

<span class="hljs-comment">// 方案一，返回新的value描述符</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">log1</span>(<span class="hljs-params">tag, name, descriptor</span>) &#123;
  <span class="hljs-keyword">return</span> &#123;
    ...descriptor,
    <span class="hljs-title function_">value</span>(<span class="hljs-params">...args</span>) &#123;
      <span class="hljs-keyword">let</span> start = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">valueOf</span>()
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">return</span> descriptor.<span class="hljs-property">value</span>.<span class="hljs-title function_">apply</span>(<span class="hljs-variable language_">this</span>, args)
      &#125; <span class="hljs-keyword">finally</span> &#123;
        <span class="hljs-keyword">let</span> end = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">valueOf</span>()
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`start: <span class="hljs-subst">$&#123;start&#125;</span> end: <span class="hljs-subst">$&#123;end&#125;</span> consume: <span class="hljs-subst">$&#123;end - start&#125;</span>`</span>)
      &#125;
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// 方案二、修改现有描述符</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">log2</span>(<span class="hljs-params">tag, name, descriptor</span>) &#123;
  <span class="hljs-keyword">let</span> func = descriptor.<span class="hljs-property">value</span> <span class="hljs-comment">// 先获取之前的函数</span>

  <span class="hljs-comment">// 修改对应的value</span>
  descriptor.<span class="hljs-property">value</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) &#123;
    <span class="hljs-keyword">let</span> start = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">valueOf</span>()
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">return</span> func.<span class="hljs-title function_">apply</span>(<span class="hljs-variable language_">this</span>, args)
    &#125; <span class="hljs-keyword">finally</span> &#123;
      <span class="hljs-keyword">let</span> end = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">valueOf</span>()
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`start: <span class="hljs-subst">$&#123;start&#125;</span> end: <span class="hljs-subst">$&#123;end&#125;</span> consume: <span class="hljs-subst">$&#123;end - start&#125;</span>`</span>)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><h4 data-id="heading-14">访问器</h4>
<p>访问器就是添加有<code>get</code>、<code>set</code>前缀的函数，用于控制属性的赋值及取值操作，在使用上与函数没有什么区别，甚至在返回值的处理上也没有什么区别。<br>
只不过我们需要按照规定设置对应的<code>get</code>或者<code>set</code>描述符罢了：</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Modal</span> &#123;
  _name = <span class="hljs-string">'Niko'</span>

  @prefix
  <span class="hljs-keyword">get</span> <span class="hljs-title function_">name</span>() &#123; <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">_name</span> &#125;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">prefix</span>(<span class="hljs-params">target, name, descriptor</span>) &#123;
  <span class="hljs-keyword">return</span> &#123;
    ...descriptor,
    get () &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">`wrap_<span class="hljs-subst">$&#123;<span class="hljs-variable language_">this</span>._name&#125;</span>`</span>
    &#125;
  &#125;
&#125;

<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-keyword">new</span> <span class="hljs-title class_">Modal</span>().<span class="hljs-property">name</span>) <span class="hljs-comment">// wrap_Niko</span>
<span class="copy-code-btn">复制代码</span></code></pre><h4 data-id="heading-15">属性</h4>
<p>对于属性的装饰器，是没有返回<code>descriptor</code>的，并且装饰器函数的返回值也会被忽略掉，如果我们想要修改某一个静态属性，则需要自己获取<code>descriptor</code>：</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Modal</span> &#123;
  @prefix
  <span class="hljs-keyword">static</span> name1 = <span class="hljs-string">'Niko'</span>
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">prefix</span>(<span class="hljs-params">target, name</span>) &#123;
  <span class="hljs-keyword">let</span> descriptor = <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">getOwnPropertyDescriptor</span>(target, name)

  <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(target, name, &#123;
    ...descriptor,
    <span class="hljs-attr">value</span>: <span class="hljs-string">`wrap_<span class="hljs-subst">$&#123;descriptor.value&#125;</span>`</span>
  &#125;)
  
  <span class="hljs-keyword">return</span> target
&#125;

<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-title class_">Modal</span>.<span class="hljs-property">name1</span>) <span class="hljs-comment">// wrap_Niko</span>
<span class="copy-code-btn">复制代码</span></code></pre><p>对于一个实例的属性，则没有直接修改的方案，不过我们可以结合着一些其他装饰器来曲线救国。</p>
<p>比如，我们有一个类，会传入姓名和年龄作为初始化的参数，然后我们要针对这两个参数设置对应的格式校验：</p>
<pre><code lang="typescript" class="hljs language-typescript copyable"><span class="hljs-keyword">const</span> validateConf = &#123;&#125; <span class="hljs-comment">// 存储校验信息</span>

<span class="hljs-meta">@validator</span>
<span class="hljs-keyword">class</span> <span class="hljs-title class_">Person</span> &#123;
  <span class="hljs-meta">@validate</span>(<span class="hljs-string">'string'</span>)
  name
  <span class="hljs-meta">@validate</span>(<span class="hljs-string">'number'</span>)
  age

  <span class="hljs-title function_">constructor</span>(<span class="hljs-params">name, age</span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">name</span> = name
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">age</span> = age
  &#125;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">validator</span>(<span class="hljs-params">constructor</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">extends</span> constructor &#123;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">...args</span>) &#123;
      <span class="hljs-variable language_">super</span>(...args)

      <span class="hljs-comment">// 遍历所有的校验信息进行验证</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key, <span class="hljs-keyword">type</span>] <span class="hljs-keyword">of</span> <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">entries</span>(validateConf)) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-variable language_">this</span>[key] !== <span class="hljs-keyword">type</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Error</span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span> must be <span class="hljs-subst">$&#123;<span class="hljs-keyword">type</span>&#125;</span>`</span>)
      &#125;
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">validate</span>(<span class="hljs-params"><span class="hljs-keyword">type</span></span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">function</span> (<span class="hljs-params">target, name, descriptor</span>) &#123;
    <span class="hljs-comment">// 向全局对象中传入要校验的属性名及类型</span>
    validateConf[name] = <span class="hljs-keyword">type</span>
  &#125;
&#125;

<span class="hljs-keyword">new</span> <span class="hljs-title class_">Person</span>(<span class="hljs-string">'Niko'</span>, <span class="hljs-string">'18'</span>)  <span class="hljs-comment">// throw new error: [age must be number]</span>
<span class="copy-code-btn">复制代码</span></code></pre><p>首先，在类上边添加装饰器<code>@validator</code>，然后在需要校验的两个参数上添加<code>@validate</code>装饰器，两个装饰器用来向一个全局对象传入信息，来记录哪些属性是需要进行校验的。<br>
然后在<code>validator</code>中继承原有的类对象，并在实例化之后遍历刚才设置的所有校验信息进行验证，如果发现有类型错误的，直接抛出异常。<br>
这个类型验证的操作对于原<code>Class</code>来说几乎是无感知的。</p>
<h3 data-id="heading-16">函数参数装饰器</h3>
<p>最后，还有一个用于函数参数的装饰器，这个装饰器也是像实例属性一样的，没有办法单独使用，毕竟函数是在运行时调用的，而无论是何种装饰器，都是在声明类时（可以认为是伪编译期）调用的。</p>
<p>函数参数装饰器会接收三个参数：</p>
<ol>
<li>类似上述的操作，类的原型或者类的构造函数</li>
<li>参数所处的函数名称</li>
<li>参数在函数中形参中的位置（函数签名中的第几个参数）</li>
</ol>
<p>一个简单的示例，我们可以结合着函数装饰器来完成对函数参数的类型转换：</p>
<pre><code lang="typescript" class="hljs language-typescript copyable"><span class="hljs-keyword">const</span> parseConf = &#123;&#125;
<span class="hljs-keyword">class</span> <span class="hljs-title class_">Modal</span> &#123;
  <span class="hljs-meta">@parseFunc</span>
  <span class="hljs-title function_">addOne</span>(<span class="hljs-params"><span class="hljs-meta">@parse</span>(<span class="hljs-string">'number'</span>) num</span>) &#123;
    <span class="hljs-keyword">return</span> num + <span class="hljs-number">1</span>
  &#125;
&#125;

<span class="hljs-comment">// 在函数调用前执行格式化操作</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">parseFunc</span> (target, name, descriptor) &#123;
  <span class="hljs-keyword">return</span> &#123;
    ...descriptor,
    value (...arg) &#123;
      <span class="hljs-comment">// 获取格式化配置</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [index, <span class="hljs-keyword">type</span>] <span class="hljs-keyword">of</span> parseConf) &#123;
        <span class="hljs-keyword">switch</span> (<span class="hljs-keyword">type</span>) &#123;
          <span class="hljs-keyword">case</span> <span class="hljs-string">'number'</span>:  arg[index] = <span class="hljs-title class_">Number</span>(arg[index])             <span class="hljs-keyword">break</span>
          <span class="hljs-keyword">case</span> <span class="hljs-string">'string'</span>:  arg[index] = <span class="hljs-title class_">String</span>(arg[index])             <span class="hljs-keyword">break</span>
          <span class="hljs-keyword">case</span> <span class="hljs-string">'boolean'</span>: arg[index] = <span class="hljs-title class_">String</span>(arg[index]) === <span class="hljs-string">'true'</span>  <span class="hljs-keyword">break</span>
        &#125;
      &#125;

      <span class="hljs-keyword">return</span> descriptor.<span class="hljs-property">value</span>.<span class="hljs-title function_">apply</span>(<span class="hljs-variable language_">this</span>, arg)
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// 向全局对象中添加对应的格式化信息</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">parse</span>(<span class="hljs-params"><span class="hljs-keyword">type</span></span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">function</span> (<span class="hljs-params">target, name, index</span>) &#123;
    parseConf[index] = <span class="hljs-keyword">type</span>
  &#125;
&#125;

<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-keyword">new</span> <span class="hljs-title class_">Modal</span>().<span class="hljs-title function_">addOne</span>(<span class="hljs-string">'10'</span>)) <span class="hljs-comment">// 11</span>
<span class="copy-code-btn">复制代码</span></code></pre><h2 data-id="heading-17">使用装饰器实现一个有趣的Koa封装</h2>
<p>比如在写Node接口时，可能是用的<code>koa</code>或者<code>express</code>，一般来说可能要处理很多的请求参数，有来自<code>headers</code>的，有来自<code>body</code>的，甚至有来自<code>query</code>、<code>cookie</code>的。<br>
所以很有可能在<code>router</code>的开头数行都是这样的操作：</p>
<pre><code lang="csharp" class="hljs language-csharp copyable">router.<span class="hljs-keyword">get</span>(<span class="hljs-string">'/'</span>, <span class="hljs-keyword">async</span> (ctx, next) => &#123;
  <span class="hljs-keyword">let</span> id = ctx.query.id
  <span class="hljs-keyword">let</span> uid = ctx.cookies.<span class="hljs-keyword">get</span>(<span class="hljs-string">'uid'</span>)
  <span class="hljs-keyword">let</span> device = ctx.header[<span class="hljs-string">'device'</span>]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre><p>以及如果我们有大量的接口，可能就会有大量的<code>router.get</code>、<code>router.post</code>。<br>
以及如果要针对模块进行分类，可能还会有大量的<code>new Router</code>的操作。</p>
<p>这些代码都是与业务逻辑本身无关的，所以我们应该尽可能的简化这些代码的占比，而使用装饰器就能够帮助我们达到这个目的。</p>
<h3 data-id="heading-18">装饰器的准备</h3>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-comment">// 首先，我们要创建几个用来存储信息的全局List</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> routerList      = []
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> controllerList  = []
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> parseList       = []
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> paramList       = []

<span class="hljs-comment">// 虽说我们要有一个能够创建Router实例的装饰器</span>
<span class="hljs-comment">// 但是并不会直接去创建，而是在装饰器执行的时候进行一次注册</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">Router</span>(<span class="hljs-params">basename = <span class="hljs-string">''</span></span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">constrcutor</span>) =></span> &#123;
    routerList.<span class="hljs-title function_">push</span>(&#123;
      constrcutor,
      basename
    &#125;)
  &#125;
&#125;

<span class="hljs-comment">// 然后我们在创建对应的Get Post请求监听的装饰器</span>
<span class="hljs-comment">// 同样的，我们并不打算去修改他的任何属性，只是为了获取函数的引用</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">Method</span>(<span class="hljs-params">type</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">path</span>) =></span> <span class="hljs-function">(<span class="hljs-params">target, name, descriptor</span>) =></span> &#123;
    controllerList.<span class="hljs-title function_">push</span>(&#123;
      target,
      type,
      path,
      <span class="hljs-attr">method</span>: name,
      <span class="hljs-attr">controller</span>: descriptor.<span class="hljs-property">value</span>
    &#125;)
  &#125;
&#125;

<span class="hljs-comment">// 接下来我们还需要用来格式化参数的装饰器</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">Parse</span>(<span class="hljs-params">type</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">target, name, index</span>) =></span> &#123;
    parseList.<span class="hljs-title function_">push</span>(&#123;
      target,
      type,
      <span class="hljs-attr">method</span>: name,
      index
    &#125;)
  &#125;
&#125;

<span class="hljs-comment">// 以及最后我们要处理的各种参数的获取</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">Param</span>(<span class="hljs-params">position</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">key</span>) =></span> <span class="hljs-function">(<span class="hljs-params">target, name, index</span>) =></span> &#123;
    paramList.<span class="hljs-title function_">push</span>(&#123;
      target,
      key,
      position,
      <span class="hljs-attr">method</span>: name,
      index
    &#125;)
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title class_">Body</span>   = <span class="hljs-title class_">Param</span>(<span class="hljs-string">'body'</span>)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title class_">Header</span> = <span class="hljs-title class_">Param</span>(<span class="hljs-string">'header'</span>)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title class_">Cookie</span> = <span class="hljs-title class_">Param</span>(<span class="hljs-string">'cookie'</span>)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title class_">Query</span>  = <span class="hljs-title class_">Param</span>(<span class="hljs-string">'query'</span>)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title class_">Get</span>    = <span class="hljs-title class_">Method</span>(<span class="hljs-string">'get'</span>)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title class_">Post</span>   = <span class="hljs-title class_">Method</span>(<span class="hljs-string">'post'</span>)
<span class="copy-code-btn">复制代码</span></code></pre><h3 data-id="heading-19">Koa服务的处理</h3>
<p>上边是创建了所有需要用到的装饰器，但是也仅仅是把我们所需要的各种信息存了起来，而怎么利用这些装饰器则是下一步需要做的事情了：</p>
<pre><code lang="javascript" class="hljs language-javascript copyable"><span class="hljs-keyword">const</span> routers = []

<span class="hljs-comment">// 遍历所有添加了装饰器的Class，并创建对应的Router对象</span>
routerList.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
  <span class="hljs-keyword">let</span> &#123; basename, constrcutor &#125; = item
  <span class="hljs-keyword">let</span> router = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Router</span>(&#123;
    <span class="hljs-attr">prefix</span>: basename
  &#125;)

  controllerList
    .<span class="hljs-title function_">filter</span>(<span class="hljs-function"><span class="hljs-params">i</span> =></span> i.<span class="hljs-property">target</span> === constrcutor.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>)
    .<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">controller</span> =></span> &#123;
      router[controller.<span class="hljs-property">type</span>](controller.<span class="hljs-property">path</span>, <span class="hljs-keyword">async</span> (ctx, next) => &#123;
        <span class="hljs-keyword">let</span> args = []
        <span class="hljs-comment">// 获取当前函数对应的参数获取</span>
        paramList
          .<span class="hljs-title function_">filter</span>( <span class="hljs-function"><span class="hljs-params">param</span> =></span> param.<span class="hljs-property">target</span> === constrcutor.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span> && param.<span class="hljs-property">method</span> === controller.<span class="hljs-property">method</span> )
          .<span class="hljs-title function_">map</span>(<span class="hljs-function"><span class="hljs-params">param</span> =></span> &#123;
            <span class="hljs-keyword">let</span> &#123; index, key &#125; = param
            <span class="hljs-keyword">switch</span> (param.<span class="hljs-property">position</span>) &#123;
              <span class="hljs-keyword">case</span> <span class="hljs-string">'body'</span>:    args[index] = ctx.<span class="hljs-property">request</span>.<span class="hljs-property">body</span>[key] <span class="hljs-keyword">break</span>
              <span class="hljs-keyword">case</span> <span class="hljs-string">'header'</span>:  args[index] = ctx.<span class="hljs-property">headers</span>[key]      <span class="hljs-keyword">break</span>
              <span class="hljs-keyword">case</span> <span class="hljs-string">'cookie'</span>:  args[index] = ctx.<span class="hljs-property">cookies</span>.<span class="hljs-title function_">get</span>(key)  <span class="hljs-keyword">break</span>
              <span class="hljs-keyword">case</span> <span class="hljs-string">'query'</span>:   args[index] = ctx.<span class="hljs-property">query</span>[key]        <span class="hljs-keyword">break</span>
            &#125;
          &#125;)

        <span class="hljs-comment">// 获取当前函数对应的参数格式化</span>
        parseList
          .<span class="hljs-title function_">filter</span>( <span class="hljs-function"><span class="hljs-params">parse</span> =></span> parse.<span class="hljs-property">target</span> === constrcutor.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span> && parse.<span class="hljs-property">method</span> === controller.<span class="hljs-property">method</span> )
          .<span class="hljs-title function_">map</span>(<span class="hljs-function"><span class="hljs-params">parse</span> =></span> &#123;
            <span class="hljs-keyword">let</span> &#123; index &#125; = parse
            <span class="hljs-keyword">switch</span> (parse.<span class="hljs-property">type</span>) &#123;
              <span class="hljs-keyword">case</span> <span class="hljs-string">'number'</span>:  args[index] = <span class="hljs-title class_">Number</span>(args[index])             <span class="hljs-keyword">break</span>
              <span class="hljs-keyword">case</span> <span class="hljs-string">'string'</span>:  args[index] = <span class="hljs-title class_">String</span>(args[index])             <span class="hljs-keyword">break</span>
              <span class="hljs-keyword">case</span> <span class="hljs-string">'boolean'</span>: args[index] = <span class="hljs-title class_">String</span>(args[index]) === <span class="hljs-string">'true'</span>  <span class="hljs-keyword">break</span>
            &#125;
          &#125;)

        <span class="hljs-comment">// 调用实际的函数，处理业务逻辑</span>
        <span class="hljs-keyword">let</span> results = controller.<span class="hljs-title function_">controller</span>(...args)

        ctx.<span class="hljs-property">body</span> = results
      &#125;)
    &#125;)

  routers.<span class="hljs-title function_">push</span>(router.<span class="hljs-title function_">routes</span>())
&#125;)

<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Koa</span>()

app.<span class="hljs-title function_">use</span>(<span class="hljs-title function_">bodyParse</span>())
app.<span class="hljs-title function_">use</span>(<span class="hljs-title function_">compose</span>(routers))

app.<span class="hljs-title function_">listen</span>(<span class="hljs-number">12306</span>, <span class="hljs-function">() =></span> <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'server run as http://127.0.0.1:12306'</span>))
<span class="copy-code-btn">复制代码</span></code></pre><p>上边的代码就已经搭建出来了一个Koa的封装，以及包含了对各种装饰器的处理，接下来就是这些装饰器的实际应用了：</p>
<pre><code lang="less" class="hljs language-less copyable"><span class="hljs-selector-tag">import</span> &#123; <span class="hljs-selector-tag">Router</span>, <span class="hljs-selector-tag">Get</span>, <span class="hljs-selector-tag">Query</span>, <span class="hljs-selector-tag">Parse</span> &#125; <span class="hljs-selector-tag">from</span> "../<span class="hljs-selector-tag">decorators</span>"

@<span class="hljs-selector-tag">Router</span>(<span class="hljs-string">''</span>)
<span class="hljs-selector-tag">export</span> <span class="hljs-selector-tag">default</span> <span class="hljs-selector-tag">class</span> &#123;
  <span class="hljs-variable">@Get</span>(<span class="hljs-string">'/'</span>)
  index (<span class="hljs-variable">@Parse</span>(<span class="hljs-string">'number'</span>) <span class="hljs-variable">@Query</span>(<span class="hljs-string">'id'</span>) <span class="hljs-attribute">id</span>: number) &#123;
    <span class="hljs-selector-tag">return</span> &#123;
      code: 200,
      id,
      type: typeof id
    &#125;
  &#125;

  <span class="hljs-variable">@Post</span>(<span class="hljs-string">'/detail'</span>)
  detail (
    <span class="hljs-variable">@Parse</span>(<span class="hljs-string">'number'</span>) <span class="hljs-variable">@Query</span>(<span class="hljs-string">'id'</span>) <span class="hljs-attribute">id</span>: number, 
    <span class="hljs-variable">@Parse</span>(<span class="hljs-string">'number'</span>) <span class="hljs-variable">@Body</span>(<span class="hljs-string">'age'</span>) <span class="hljs-attribute">age</span>: number
  ) &#123;
    <span class="hljs-selector-tag">return</span> &#123;
      code: 200,
      age: age + 1
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>很轻易的就实现了一个<code>router</code>的创建，路径、method的处理，包括各种参数的获取，类型转换。<br>
将各种非业务逻辑相关的代码统统交由装饰器来做，而函数本身只负责处理自身逻辑即可。<br>
这里有完整的代码：<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FJiasm%2Fnotebook%2Ftree%2Fmaster%2Flabs%2Fdemo%2Ftypescript%2Fkoa-decorators" title="https://github.com/Jiasm/notebook/tree/master/labs/demo/typescript/koa-decorators" ref="nofollow noopener noreferrer">GitHub</a>。安装依赖后<code>npm start</code>即可看到效果。</p>
<p>这样开发带来的好处就是，让代码可读性变得更高，在函数中更专注的做自己应该做的事情。<br>
而且装饰器本身如果名字起的足够好的好，也是在一定程度上可以当作文档注释来看待了（Java中有个类似的玩意儿叫做注解）。</p>
<h2 data-id="heading-20">总结</h2>
<p>合理利用装饰器可以极大的提高开发效率，对一些非逻辑相关的代码进行封装提炼能够帮助我们快速完成重复性的工作，节省时间。<br>
但是糖再好吃，也不要吃太多，容易坏牙齿的，同样的滥用装饰器也会使代码本身逻辑变得扑朔迷离，如果确定一段代码不会在其他地方用到，或者一个函数的核心逻辑就是这些代码，那么就没有必要将它取出来作为一个装饰器来存在。</p>
<h3 data-id="heading-21">参考资料</h3>
<ol>
<li><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fdecorators.html" title="https://www.typescriptlang.org/docs/handbook/decorators.html" ref="nofollow noopener noreferrer">typescript | decorators</a></li>
<li><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftypestack%2Frouting-controllers" title="https://github.com/typestack/routing-controllers" ref="nofollow noopener noreferrer">koa示例的原版，简化代码便于举例</a></li>
</ol>
<h3 data-id="heading-22">One more thing</h3>
<p>我司现在大量招人咯，前端、Node方向都有HC<br>
公司名：<strong>Blued</strong>，坐标帝都朝阳双井<br>
主要技术栈是React，也会有机会玩ReactNative和Electron<br>
Node方向8.x版本+koa 新项目会以TS为主<br>
有兴趣的小伙伴可以联系我详谈：<br>
email: jiashunming@blued.com<br>
wechat: github_jiasm</p>
</div>  
</div>
            