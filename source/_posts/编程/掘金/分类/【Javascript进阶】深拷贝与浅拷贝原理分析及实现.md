
---
title: '【Javascript进阶】深拷贝与浅拷贝原理分析及实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4922f126740846d2a9e072c42e598632~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 23:28:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4922f126740846d2a9e072c42e598632~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">背景</h3>
<p>最近开发的小程序项目中，要使用深拷贝，但是不想用<code>Lodash</code>库（太大，小程序受不了）。所以打算自己写，结果没写出来，于是网上找了现成的先应付着。</p>
<p>项目上线后，觉得是时候做个基础知识的回顾了。这是一篇对深浅拷贝探索的文章，借鉴了很多前辈的总结，在此表示感谢（文末会列出参考的文献）。</p>
<h3 data-id="heading-1">浅拷贝</h3>
<p>浅拷贝指的是：拷贝后的引用类型数据与源对象是同一份数据，修改源对象的值，会把拷贝对象的也一起修改，反之亦然。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4922f126740846d2a9e072c42e598632~tplv-k3u1fbpfcp-watermark.image" alt="图片来自木易杨的博客" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">Object.assign是浅拷贝</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj1 = &#123;
    <span class="hljs-attr">a</span>:<span class="hljs-number">111</span>,
    <span class="hljs-attr">b</span>:&#123;<span class="hljs-attr">c</span>:<span class="hljs-number">222</span>&#125;
&#125;

<span class="hljs-keyword">var</span> obj2 = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;,obj1) <span class="hljs-comment">// 浅拷贝</span>
obj2.b.c = <span class="hljs-number">333</span> <span class="hljs-comment">// 修改引用类型的值</span>

<span class="hljs-built_in">console</span>.log(obj1) <span class="hljs-comment">// obj1.b.c的值被修改未333，是浅拷贝</span>
<span class="hljs-built_in">console</span>.log(obj2)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改obj2的值，obj1的值也被修改，因为obj1和obj2的b属性引用的是同一个对象。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/925757beb8454598bcb616f7c24281fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">ES6对象解构也是浅拷贝</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj1 = &#123;
    <span class="hljs-attr">a</span>:<span class="hljs-number">111</span>,
    <span class="hljs-attr">b</span>:&#123;<span class="hljs-attr">c</span>:<span class="hljs-number">222</span>&#125;
&#125;

<span class="hljs-keyword">var</span> obj2 = &#123;...obj1&#125; <span class="hljs-comment">// 浅拷贝</span>
obj2.b.c = <span class="hljs-number">666</span> <span class="hljs-comment">// 修改引用类型的值</span>

<span class="hljs-built_in">console</span>.log(obj1) <span class="hljs-comment">// obj1.b.c的值被修改未666，是浅拷贝</span>
<span class="hljs-built_in">console</span>.log(obj2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原因和上面说的一致，引用的是同一个对象，浅拷贝仅仅拷贝的是对象的引用地址，并没有拷贝对象的内容。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94ba19410f8248f3b6b6b3b48f3cc2e1~tplv-k3u1fbpfcp-watermark.image" alt="图片来自木易杨的博客" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">手写一个简单的浅拷贝</h4>
<h5 data-id="heading-5">思考题：你可以手写一个浅拷贝吗？下方的浅拷贝实现存在哪些问题？</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 一个简单的浅拷贝
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> </span>sourceObj 要复制的对象
 * <span class="hljs-doctag">@returns </span>返回浅拷贝的对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowCopy</span>(<span class="hljs-params">sourceObj</span>) </span>&#123;
  <span class="hljs-keyword">var</span> obj = &#123;&#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> sourceObj !== <span class="hljs-string">'object'</span>) &#123;
    <span class="hljs-keyword">return</span> sourceObj
  &#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> sourceObj) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.prototype.hasOwnProperty.call(sourceObj, key)) &#123;
      obj[key] = sourceObj[key]
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> obj
&#125;

<span class="hljs-keyword">var</span> obj1 = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'obj1'</span>,
  <span class="hljs-attr">info</span>: &#123;
    <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
  &#125;,
  <span class="hljs-attr">undefined</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">func</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am a simple function'</span>) &#125;,
  <span class="hljs-attr">exp</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'\\w+'</span>),
  <span class="hljs-attr">createTime</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
  [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>)]: <span class="hljs-string">'symbol'</span>
&#125;

<span class="hljs-comment">// 浅拷贝，修改原对象的引用类型的值，拷贝出来的对象也一同被修改</span>
<span class="hljs-keyword">var</span> shObj = shallowCopy(obj1)
obj1.info.age = <span class="hljs-number">16</span> <span class="hljs-comment">// 修改源对象</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'shObj'</span>, shObj) <span class="hljs-comment">// 浅拷贝出来的对象也被修改了</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台的输出如下，修改obj1的age为16，shObj对象的age也被修改了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f879316a78904cd4a143718f19107aee~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述浅拷贝方法存在的问题有很多，包括判断对象不够严谨，没有考虑循环引用等。我们的重点不是浅拷贝，为什么还要讲浅拷贝？</p>
<p>因为了解浅拷贝，才知道为什么要做深拷贝，浅拷贝是基础，深拷贝是进阶！</p>
<h3 data-id="heading-6">深拷贝</h3>
<p>深拷贝指的是：拷贝后的对象是独立的（包括引用类型），修改源对象的值，不会对拷贝对象产生影响，反之亦然。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0d60871822c48fbbc1e886fab521500~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">JSON.stringify()的弊端</h4>
<p>说到深拷贝，很多人喜欢一把梭（即使用<code>JSON.stringify()</code>方法和<code>JSON.parse()</code>方法）。你知道使用这个两个方法做深拷贝会有哪些问题和隐患吗？</p>
<p>据我所知，使用JSON.stringify()做深拷贝，至少存在以下问题：</p>
<p>1、会忽略 undefined；</p>
<p>2、会忽略 symbol；</p>
<p>3、会忽略函数；</p>
<p>4、不能正确处理new Date()；</p>
<p>5、不能处理正则（变成空对象）；</p>
<p>6、不能解决循环引用的对象（直接报错）。</p>
<p>举个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 深拷贝0（JSON.stringify()一把梭）
 * <span class="hljs-doctag">@param</span>0 sourceObj 要复制的对象
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Object&#125;</span> </span>返回深拷贝的对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCopy0</span>(<span class="hljs-params">sourceObj</span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(sourceObj))
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'JSON.stringify报错：'</span>, error)
  &#125;
&#125;

<span class="hljs-keyword">var</span> obj0 = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'obj0'</span>,
  <span class="hljs-attr">info</span>: &#123;
    <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">22</span>
  &#125;,
  <span class="hljs-attr">undefined</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">func</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am a simple function'</span>) &#125;,
  <span class="hljs-attr">exp</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'\\w+'</span>),
  <span class="hljs-attr">createTime</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
  [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>)]: <span class="hljs-string">'symbol'</span>,
&#125;

<span class="hljs-comment">// 循环引用（已注释，打开后会报错，不信你拷贝到控制台试一下）</span>
<span class="hljs-comment">// obj0.circularReference = obj0</span>

<span class="hljs-comment">// 深拷贝，完全独立的两份数据，修改原对象引用类型的值，对拷贝出来的对象没影响</span>
<span class="hljs-keyword">var</span> copyObj0 = deepCopy0(obj0)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj0--origin'</span>, obj0)
obj0.info.age = <span class="hljs-number">100</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj0--copy'</span>, copyObj0)

<span class="hljs-keyword">try</span> &#123;
  copyObj0.func()
&#125; <span class="hljs-keyword">catch</span> (error) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这里会报错：'</span>, error)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从结果可以看出，以上问题确实存在！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c801e6e338c14bcf845782b4481e44ba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">手写一个简单的深拷贝</h4>
<h5 data-id="heading-9">思考题：除了<code>JSON.stringify()</code>方法，你还能想到其他办法实现深拷贝吗？</h5>
<p>回顾上文中手写的浅拷贝，之所以是浅拷贝，是因为仅拷贝了引用类型的地址（保存在栈中的指针），没有拷贝引用类型的值（保存在堆中数据）。</p>
<p>我们稍微修改一下，如果是引用类型，就使用递归的方式拷贝属性的值，一个简单的深拷贝就出来了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 深拷贝1
 * <span class="hljs-doctag">@param</span>0 sourceObj 要复制的对象
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Object&#125;</span> </span>返回深拷贝的对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCopy1</span>(<span class="hljs-params">sourceObj</span>) </span>&#123;
  <span class="hljs-keyword">var</span> obj = &#123;&#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> sourceObj !== <span class="hljs-string">'object'</span>) &#123;
    <span class="hljs-keyword">return</span> sourceObj
  &#125;

  <span class="hljs-built_in">Object</span>.keys(sourceObj).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
    <span class="hljs-comment">// 新增代码，遇到引用类型的属性，递归拷贝后再赋值</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> sourceObj[key] === <span class="hljs-string">'object'</span>) &#123;
      obj[key] = deepCopy1(sourceObj[key])
    &#125; <span class="hljs-keyword">else</span> &#123;
      obj[key] = sourceObj[key]
    &#125;
  &#125;)
  <span class="hljs-keyword">return</span> obj
&#125;

<span class="hljs-keyword">var</span> obj1 = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'obj1'</span>,
  <span class="hljs-attr">info</span>: &#123;
    <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
  &#125;,
  <span class="hljs-attr">undefined</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">func</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am a simple function'</span>) &#125;,
  <span class="hljs-attr">exp</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'\\w+'</span>),
  <span class="hljs-attr">createTime</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
  [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>)]: <span class="hljs-string">'symbol'</span>
&#125;
<span class="hljs-comment">// 循环引用</span>
<span class="hljs-comment">// obj1.circularReference = obj1</span>

<span class="hljs-comment">// 深拷贝，完全独立的两份数据，修改原对象引用类型的值，对拷贝出来的对象没影响</span>
<span class="hljs-keyword">var</span> copyObj1 = deepCopy1(obj1)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj1-origin'</span>, obj1)
obj1.info.age = <span class="hljs-number">16</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj1-copy'</span>, copyObj1)
copyObj1.func()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拷贝效果比一把梭好一些，起码保留了undefined属性值。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/299c12fd88244f02b2b016feb547fb9c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是问题还很多，需要继续完善。</p>
<p><strong>deepCopy1方法存在的问题有:</strong></p>
<p>1、会忽略 symbol</p>
<p>2、不能正确处理new Date()（变成空对象）</p>
<p>3、不能处理正则（变成空对象）</p>
<p>4、不能解决循环引用的对象（会导致堆栈溢出）</p>
<h4 data-id="heading-10">解决时间对象、正则表拷贝</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 深拷贝2（解决时间对象、正则表达式拷贝问题）
 * <span class="hljs-doctag">@param</span>0 sourceObj 要复制的对象
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Object&#125;</span> </span>返回深拷贝的对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCopy2</span>(<span class="hljs-params">sourceObj</span>) </span>&#123;
  <span class="hljs-keyword">var</span> obj = &#123;&#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> sourceObj !== <span class="hljs-string">'object'</span>) &#123;
    <span class="hljs-keyword">return</span> sourceObj
  &#125;

  <span class="hljs-built_in">Object</span>.keys(sourceObj).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
    <span class="hljs-comment">// 引用类型，递归</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> sourceObj[key] === <span class="hljs-string">'object'</span>) &#123;
      <span class="hljs-keyword">if</span> (sourceObj[key].constructor.name === <span class="hljs-string">'Date'</span>) &#123;
        obj[key] = sourceObj[key]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sourceObj[key].constructor.name === <span class="hljs-string">'RegExp'</span>) &#123;
        <span class="hljs-keyword">var</span> regexp = sourceObj[key]
        <span class="hljs-keyword">var</span> reFlags = <span class="hljs-regexp">/\w*$/</span> <span class="hljs-comment">// 提取正则的标识位</span>
        <span class="hljs-comment">// var result = new regexp.constructor(regexp.source, reFlags.exec(regexp)) // lodash的做法（保留原型链上的内容？）</span>
        <span class="hljs-keyword">var</span> result = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(regexp.source, reFlags.exec(regexp)) <span class="hljs-comment">// 我的做法</span>
        result.lastIndex = regexp.lastIndex <span class="hljs-comment">// 上一次匹配执行到的位置，默认为0</span>
        obj[key] = result
      &#125; <span class="hljs-keyword">else</span> &#123;
        obj[key] = deepCopy2(sourceObj[key])
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      obj[key] = sourceObj[key]
    &#125;
  &#125;)
  <span class="hljs-keyword">return</span> obj
&#125;

<span class="hljs-keyword">var</span> obj2 = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'obj2'</span>,
  <span class="hljs-attr">info</span>: &#123;
    <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
  &#125;,
  <span class="hljs-attr">undefined</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">func</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am a simple function'</span>) &#125;,
  <span class="hljs-attr">exp</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'\[0-9\]'</span>),
  <span class="hljs-attr">createTime</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
  [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>)]: <span class="hljs-string">'symbol'</span>
&#125;
<span class="hljs-comment">// 循环引用</span>
<span class="hljs-comment">// obj2.circularReference = obj2</span>

<span class="hljs-keyword">var</span> copyObj2 = deepCopy2(obj2)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj2-origin'</span>, obj2)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj2-copy'</span>, copyObj2)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台输出如下（成功拷贝时间和正则表达式）：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01471288ca3e4a1bb3b25919dc6a4d68~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>deepCopy2方法存在的问题有:</strong></p>
<p>1、会忽略 symbol</p>
<p>2、不能解决循环引用的对象（会导致堆栈溢出）</p>
<h4 data-id="heading-11">解决循环引用问题</h4>
<p><code>deepCopy0</code>、<code>deepCopy1</code>、<code>deepCopy2</code>方法，遇到循环引用会直接爆栈。解决循环引用的办法是，利用<code>WeakMap</code>来缓存遍历过的对象，如果存在就直接使用存在的对象，防止进入死循环。当然也可以用数组或者Map缓存。</p>
<h5 data-id="heading-12">思考题：为什么是<code>WeakMap</code>？ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FWeakMap" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/WeakMap" ref="nofollow noopener noreferrer">答案在这里</a></h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 深拷贝3（解决循环引用问题）
 * <span class="hljs-doctag">@param</span>0 sourceObj 要复制的对象
 * <span class="hljs-doctag">@param</span>1 hash 哈希表（非必填）
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Object&#125;</span> </span>返回深拷贝的对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCopy3</span>(<span class="hljs-params">sourceObj, hash</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> sourceObj !== <span class="hljs-string">'object'</span>) &#123;
    <span class="hljs-keyword">return</span> sourceObj
  &#125;

  <span class="hljs-keyword">var</span> obj = &#123;&#125;
  <span class="hljs-keyword">var</span> hash = hash || <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>() <span class="hljs-comment">// 使用哈希表存储遍历过的对象</span>

  <span class="hljs-comment">// 查找hash表中是否存在相同的值</span>
  <span class="hljs-keyword">if</span> (hash.has(sourceObj)) &#123;
    <span class="hljs-keyword">return</span> hash.get(sourceObj)
  &#125;

  <span class="hljs-comment">// 缓存当前的数据对象</span>
  hash.set(sourceObj, obj)

  <span class="hljs-built_in">Object</span>.keys(sourceObj).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
    <span class="hljs-comment">// 引用类型，递归</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> sourceObj[key] === <span class="hljs-string">'object'</span>) &#123;
      <span class="hljs-keyword">if</span> (sourceObj[key].constructor.name === <span class="hljs-string">'Date'</span>) &#123;
        obj[key] = sourceObj[key]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sourceObj[key].constructor.name === <span class="hljs-string">'RegExp'</span>) &#123;
        <span class="hljs-keyword">var</span> regexp = sourceObj[key]
        <span class="hljs-keyword">var</span> reFlags = <span class="hljs-regexp">/\w*$/</span> <span class="hljs-comment">// 提取正则的标识位</span>
        <span class="hljs-keyword">var</span> result = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(regexp.source, reFlags.exec(regexp)) <span class="hljs-comment">// 我的做法</span>
        <span class="hljs-comment">// var result = new regexp.constructor(regexp.source, reFlags.exec(regexp)) // lodash的做法</span>

        result.lastIndex = regexp.lastIndex <span class="hljs-comment">// 上一次匹配执行到的位置，默认为0</span>
        obj[key] = result
      &#125; <span class="hljs-keyword">else</span> &#123;
        obj[key] = deepCopy3(sourceObj[key], hash) <span class="hljs-comment">// 新增代码，传入hash表</span>
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      obj[key] = sourceObj[key]
    &#125;
  &#125;)
  <span class="hljs-keyword">return</span> obj
&#125;

<span class="hljs-keyword">var</span> obj3 = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'obj3'</span>,
  <span class="hljs-attr">info</span>: &#123;
    <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
  &#125;,
  <span class="hljs-attr">undefined</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">func</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am a simple function'</span>) &#125;,
  <span class="hljs-attr">exp</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'\[0-9\]'</span>),
  <span class="hljs-attr">createTime</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
  [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>)]: <span class="hljs-string">'symbol'</span>
&#125;
<span class="hljs-comment">// 循环引用</span>
obj3.circularReference = obj3

<span class="hljs-keyword">var</span> copyObj3 = deepCopy3(obj3)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj3-origin'</span>, obj3)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj3-copy'</span>, copyObj3)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下，circularReference是循环引用字段，没有进入死循环，且完成了拷贝工作。</p>
<h5 data-id="heading-13">思考题：对属性circularReference的拷贝是深拷贝还是浅拷贝？为什么？</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcdb74b7c7a84aed9ee8cb98c7aff852~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>deepCopy3方法存在的问题有:</strong></p>
<p>1、会忽略 symbol</p>
<p>2、不能拷贝数组</p>
<h4 data-id="heading-14">解决Symbol和数组拷贝问题</h4>
<p><code>Symbol</code>是ES6新的基本数据类型，任意两个Symbol值都不相等。Symbol的出现是为了解决对象属性覆盖问题（对象合并时，同名属性会被后来者覆盖）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 深拷贝4（Symbol拷贝、数组拷贝）
 * <span class="hljs-doctag">@param</span>0 sourceObj 要复制的对象
 * <span class="hljs-doctag">@param</span>1 hash 哈希表（非必填）
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Object&#125;</span> </span>返回深拷贝的对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCopy4</span>(<span class="hljs-params">sourceObj, hash</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> sourceObj !== <span class="hljs-string">'object'</span>) &#123;
    <span class="hljs-keyword">return</span> sourceObj
  &#125;

  <span class="hljs-keyword">var</span> obj = <span class="hljs-built_in">Array</span>.isArray(sourceObj) ? [] : &#123;&#125;
  <span class="hljs-keyword">var</span> hash = hash || <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>() <span class="hljs-comment">// 使用哈希表存储遍历过的对象</span>

  <span class="hljs-comment">// 查找hash表中是否存在相同的值</span>
  <span class="hljs-keyword">if</span> (hash.has(sourceObj)) &#123;
    <span class="hljs-keyword">return</span> hash.get(sourceObj)
  &#125;

  <span class="hljs-comment">// 缓存当前的数据对象</span>
  hash.set(sourceObj, obj)

  <span class="hljs-comment">// 新增代码，遍历symbols</span>
  <span class="hljs-keyword">var</span> objSymbols = <span class="hljs-built_in">Object</span>.getOwnPropertySymbols(sourceObj)<span class="hljs-comment">// 获取所有Symbol的key</span>
  <span class="hljs-keyword">if</span> (objSymbols.length) &#123;
    objSymbols.forEach(<span class="hljs-function"><span class="hljs-params">symKey</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> objSymbols[symKey] === <span class="hljs-string">'object'</span>) &#123;
        obj[symKey] = deepCopy4(sourceObj[symKey], hash)
      &#125; <span class="hljs-keyword">else</span> &#123;
        obj[symKey] = sourceObj[symKey]
      &#125;
    &#125;)
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> sourceObj) &#123;
    <span class="hljs-keyword">if</span> (sourceObj.hasOwnProperty(key)) &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> sourceObj[key] === <span class="hljs-string">'object'</span>) &#123;
        <span class="hljs-keyword">if</span> (sourceObj[key].constructor.name === <span class="hljs-string">'Date'</span>) &#123;
          obj[key] = sourceObj[key]
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sourceObj[key].constructor.name === <span class="hljs-string">'RegExp'</span>) &#123;
          <span class="hljs-keyword">var</span> regexp = sourceObj[key]
          <span class="hljs-keyword">var</span> reFlags = <span class="hljs-regexp">/\w*$/</span> <span class="hljs-comment">// 提取正则的标识位</span>
          <span class="hljs-keyword">var</span> result = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(regexp.source, reFlags.exec(regexp)) <span class="hljs-comment">// 我的做法</span>
          <span class="hljs-comment">// var result = new regexp.constructor(regexp.source, reFlags.exec(regexp)) // lodash的做法</span>

          result.lastIndex = regexp.lastIndex <span class="hljs-comment">// 上一次匹配执行到的位置，默认为0</span>
          obj[key] = result
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// 引用类型，递归</span>
          obj[key] = deepCopy4(sourceObj[key], hash) <span class="hljs-comment">// 新增代码，传入hash表</span>
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        obj[key] = sourceObj[key]
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> obj
&#125;

<span class="hljs-keyword">var</span> obj4 = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'obj4'</span>,
  <span class="hljs-attr">info</span>: &#123;
    <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
  &#125;,
  <span class="hljs-attr">undefined</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">func</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am a simple function'</span>) &#125;,
  <span class="hljs-attr">exp</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'\[0-9\]'</span>),
  <span class="hljs-attr">createTime</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
  [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>)]: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
  [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'bar'</span>)]: <span class="hljs-string">'symbol bar'</span>,
  [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'bar'</span>)]: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'\[a-z\]'</span>),
  <span class="hljs-attr">arr</span>: [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>],
  <span class="hljs-attr">fetchData</span>: [<span class="hljs-string">"2021-08-12"</span>, <span class="hljs-string">"2021-08-12"</span>]
&#125;
<span class="hljs-keyword">var</span> arr4 = [
  obj4,
  <span class="hljs-number">111</span>,
  [<span class="hljs-number">222</span>, <span class="hljs-number">888</span>],
  [&#123; <span class="hljs-attr">fetchData</span>: [<span class="hljs-string">"2021-08-12"</span>, <span class="hljs-string">"2021-08-12"</span>] &#125;]
]
<span class="hljs-comment">// 循环引用</span>
obj4.circularReference = obj4

<span class="hljs-keyword">var</span> copyObj4 = deepCopy4(obj4)
<span class="hljs-keyword">var</span> copyArr4 = deepCopy4(arr4)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj4-copy'</span>, copyObj4)
obj4.info.age = <span class="hljs-number">100</span>
obj4.arr[<span class="hljs-number">2</span>] = <span class="hljs-number">666</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj4-origin'</span>, obj4)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyArr4-copy'</span>, copyArr4)
arr4[<span class="hljs-number">3</span>][<span class="hljs-number">0</span>].a = <span class="hljs-string">'changed to bbb'</span>
arr4[<span class="hljs-number">2</span>][<span class="hljs-number">1</span>] = <span class="hljs-string">'change to 666'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyArr4-origin'</span>, arr4)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下，Symbol类型的属性可以拷贝了：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bad4028296ea4d9a9a1188cd9ce65acc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>数组也可以拷贝了：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/647154a783e8489f8b8d2f5b7a57cea4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>deepCopy4存在的问题：</strong></p>
<p>1、对引用类型的判断不够严谨；</p>
<p>2、采用递归，没有考虑爆栈问题。</p>
<h4 data-id="heading-15">解决递归爆栈问题（成品）</h4>
<p>大家都知道，浏览器可以使用的内存受到操作系统的限制。如果需要深拷贝的对象层级太深（例如：10000级别的深度），就会导致内存溢出。所以我们要改用循环的方式，循环的好处是，拷贝过程中内存会得到释放，每一次循环结束都会执行出栈操作，这样一来占用的内存就不会一直增加。</p>
<h5 data-id="heading-16">思考题：代码中的<code>continue</code>可否修改为<code>break</code>？为什么？</h5>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">/**
 * 深拷贝5（改用循环，解决爆栈问题，并优化对象的判断方式）
 * <span class="hljs-doctag">@param</span>0 sourceObj 要复制的对象
 * <span class="hljs-doctag">@param</span>1 hash 哈希表（非必填）
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Object&#125;</span> </span>返回深拷贝的对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCopy5</span>(<span class="hljs-params">sourceObj, hash</span>) </span>&#123;
  <span class="hljs-comment">// 优化代码，优化引用类型判断</span>
  <span class="hljs-keyword">if</span> (!isObject(sourceObj)) &#123;
    <span class="hljs-keyword">return</span> sourceObj
  &#125;

  <span class="hljs-comment">// 新增代码，兼容数组类型</span>
  <span class="hljs-keyword">var</span> root = <span class="hljs-built_in">Array</span>.isArray(sourceObj) ? [] : &#123;&#125;
  <span class="hljs-keyword">var</span> uniqueList = [] <span class="hljs-comment">// 使用数组缓存</span>

  <span class="hljs-keyword">var</span> loopList = [&#123;
    <span class="hljs-attr">parent</span>: root,
    <span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>,
    <span class="hljs-attr">data</span>: sourceObj
  &#125;]

  <span class="hljs-keyword">while</span> (loopList.length) &#123;
    <span class="hljs-keyword">var</span> node = loopList.pop() <span class="hljs-comment">// 出栈</span>
    <span class="hljs-keyword">var</span> key = node.key
    <span class="hljs-keyword">var</span> data = node.data
    <span class="hljs-keyword">var</span> parent = node.parent

    <span class="hljs-comment">// 初始化赋值目标，key为undefined则拷贝到父元素，否则拷贝到子元素</span>
    <span class="hljs-keyword">let</span> res = parent
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> key !== <span class="hljs-string">'undefined'</span>) &#123;
      res = parent[key] = <span class="hljs-built_in">Array</span>.isArray(data) ? [] : &#123;&#125;
    &#125;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'uniqueList'</span>, uniqueList)
    <span class="hljs-comment">// debugger</span>
    <span class="hljs-comment">// 数据已经存在</span>
    <span class="hljs-keyword">let</span> uniqueData = find(uniqueList, data);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'uniqueData'</span>,uniqueData)
    <span class="hljs-keyword">if</span> (uniqueData) &#123;
      parent[key] = uniqueData.target;
      <span class="hljs-keyword">continue</span>; <span class="hljs-comment">// 中断本次循环，不能用break，否则会无法拷贝其他的对象（&#123;&#125;）类型呢</span>
    &#125;

    <span class="hljs-comment">// 数据不存在</span>
    <span class="hljs-comment">// 保存源数据，在拷贝数据中对应的引用</span>
    uniqueList.push(&#123;
      <span class="hljs-attr">source</span>: data,
      <span class="hljs-attr">target</span>: res
    &#125;);

    <span class="hljs-comment">// 遍历symbols</span>
    <span class="hljs-keyword">var</span> objSymbols = <span class="hljs-built_in">Object</span>.getOwnPropertySymbols(data)<span class="hljs-comment">// 获取所有Symbol的key</span>

    <span class="hljs-keyword">if</span> (objSymbols.length) &#123;
      objSymbols.forEach(<span class="hljs-function"><span class="hljs-params">symKey</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> objSymbols[symKey] === <span class="hljs-string">'object'</span>) &#123;
          loopList.push(&#123;
            <span class="hljs-attr">parent</span>: res,
            <span class="hljs-attr">key</span>: key,
            <span class="hljs-attr">data</span>: res[symKey]
          &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
          res[symKey] = data[symKey]
        &#125;
      &#125;)
    &#125;

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> data) &#123;
      <span class="hljs-keyword">if</span> (data.hasOwnProperty(key)) &#123;
        <span class="hljs-keyword">let</span> tempObj = data[key]

        <span class="hljs-keyword">if</span> (isObject(tempObj)) &#123;
          <span class="hljs-keyword">if</span> (tempObj.constructor.name === <span class="hljs-string">'Date'</span>) &#123;
            loopList.push(&#123;
              <span class="hljs-attr">parent</span>: res,
              <span class="hljs-attr">key</span>: key,
              <span class="hljs-attr">data</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(tempObj)
            &#125;)
          &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (tempObj.constructor.name === <span class="hljs-string">'RegExp'</span>) &#123;
            loopList.push(&#123;
              <span class="hljs-attr">parent</span>: res,
              <span class="hljs-attr">key</span>: key,
              <span class="hljs-attr">data</span>: copyRegExp(tempObj)
            &#125;)
          &#125; <span class="hljs-keyword">else</span> &#123;
            loopList.push(&#123;
              <span class="hljs-attr">parent</span>: res,
              <span class="hljs-attr">key</span>: key,
              <span class="hljs-attr">data</span>: tempObj
            &#125;)
          &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
          res[key] = tempObj
        &#125;
      &#125;
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> root
&#125;

<span class="hljs-comment">/**
 * 判断输入是否为对象类型（数组也是对象）
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;any&#125;</span> </span>obj 
 * <span class="hljs-doctag">@returns </span>Boolean 返回true或false
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isObject</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(obj) === <span class="hljs-string">'[object Object]'</span> || <span class="hljs-built_in">Object</span>.prototype.toString.call(obj) === <span class="hljs-string">'[object Array]'</span>
&#125;

<span class="hljs-comment">/**
 * 正则拷贝
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;RegExp&#125;</span> </span>regexp 
 * <span class="hljs-doctag">@returns </span>拷贝后的正则
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copyRegExp</span>(<span class="hljs-params">regexp</span>) </span>&#123;
  <span class="hljs-keyword">var</span> reFlags = <span class="hljs-regexp">/\w*$/</span> <span class="hljs-comment">// 提取正则的标识位</span>
  <span class="hljs-keyword">var</span> result = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(regexp.source, reFlags.exec(regexp)) <span class="hljs-comment">// 我的做法</span>
  <span class="hljs-comment">// var result = new regexp.constructor(regexp.source, reFlags.exec(regexp)) // lodash的做法</span>

  result.lastIndex = regexp.lastIndex <span class="hljs-comment">// 上一次匹配执行到的位置，默认为0</span>
  <span class="hljs-keyword">return</span> result
&#125;

<span class="hljs-comment">/**
 * 数组查找
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;原数组&#125;</span> </span>arr 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;要查找的目标&#125;</span> </span>item 
 * <span class="hljs-doctag">@returns </span>返回找到的数据，找不到则null
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">find</span>(<span class="hljs-params">arr, item</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
    <span class="hljs-keyword">if</span> (arr[i].source === item) &#123;
      <span class="hljs-keyword">return</span> arr[i];
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;

<span class="hljs-keyword">var</span> obj5 = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'obj5'</span>,
  <span class="hljs-attr">info</span>: &#123;
    <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
  &#125;,
  <span class="hljs-attr">undefined</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">func</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am a simple function'</span>) &#125;,
  <span class="hljs-attr">exp</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'\[0-9\]'</span>),
  <span class="hljs-attr">createTime</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
  [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>)]: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
  [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'bar'</span>)]: <span class="hljs-string">'symbol bar'</span>,
  [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'bar'</span>)]: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'\[a-z\]'</span>),
&#125;

<span class="hljs-comment">// 循环引用</span>
obj5.circularRef = obj5

<span class="hljs-comment">// 对象拷贝测试</span>
<span class="hljs-keyword">var</span> copyObj5 = deepCopy5(obj5)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj5-copy'</span>, copyObj5)
copyObj5.info.age = <span class="hljs-number">66</span>
copyObj5.createTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-string">'2021-08-10 18:16:40'</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyObj5-origin'</span>, obj5)

<span class="hljs-keyword">var</span> arr5 = [
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'obj5'</span>,
    <span class="hljs-attr">info</span>: &#123;
      <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>,
      <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
    &#125;,
    <span class="hljs-attr">undefined</span>: <span class="hljs-literal">undefined</span>,
    <span class="hljs-attr">func</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am a simple function'</span>) &#125;,
    <span class="hljs-attr">exp</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'\[0-9\]'</span>),
    <span class="hljs-attr">createTime</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
    [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>)]: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
    [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'bar'</span>)]: <span class="hljs-string">'symbol bar'</span>,
    [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'bar'</span>)]: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'\[a-z\]'</span>),
  &#125;,
  <span class="hljs-number">111</span>,
  [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>]
]

<span class="hljs-comment">// 数组拷贝测试</span>
<span class="hljs-keyword">var</span> copyArr5 = deepCopy5(arr5)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyArr5-copy'</span>, copyArr5)
copyArr5[<span class="hljs-number">0</span>].info.age = <span class="hljs-number">100</span>
copyArr5[<span class="hljs-number">2</span>][<span class="hljs-number">0</span>] = <span class="hljs-number">666</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'copyArr5-origin'</span>, arr5)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象深拷贝拷贝测试结果，修改引用类型的值不会互相影响，循环引用也不会有问题：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67d39ab5b1c5418ea7dc4dab34a7059b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>数组深拷贝测试结果，修改引用类型的值不会互相影响：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d730559f766f4b1c8a2c03b4f825c412~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">还存在的问题</h3>
<p>目前没有实现的功能有：Map、Set、Weakmap、Weakset等新增数据类型，还有Function的拷贝，原型链的拷贝等等。</p>
<p>当然如果你能确保项目中没有这些数据类型，那么<code>deepCopy5</code>基本可以满足要求。所谓优化无止境，如果发现错漏或者有优化的建议，欢迎在评论区指出，如果觉得文章对你有帮助，就大方的点个赞吧(<del>^_^</del>)</p>
<p><strong>参考文献：</strong></p>
<p>1、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmuyiy.vip%2Fblog%2F4%2F4.3.html%23%25E5%25BC%2595%25E8%25A8%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://muyiy.vip/blog/4/4.3.html#%E5%BC%95%E8%A8%80" ref="nofollow noopener noreferrer">面试题之如何实现一个深拷贝</a></p>
<p>2、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000016672263" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000016672263" ref="nofollow noopener noreferrer">深拷贝的终极探索（99%的人都不知道）</a></p></div>  
</div>
            