
---
title: '《javascript高级程序设计》学习笔记 _ 10.14-10.16.闭包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9238'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 23:30:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=9238'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>关注<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsimon9124%2Fmy_demos" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/simon9124/my_demos" ref="nofollow noopener noreferrer">前端小讴</a>，阅读更多原创技术文章</strong></p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsimon9124%2Fmy_demos%2Fblob%2Fmaster%2Fjavascript%25E9%25AB%2598%25E7%25BA%25A7%25E7%25A8%258B%25E5%25BA%258F%25E8%25AE%25BE%25E8%25AE%25A1%25EF%25BC%2588%25E7%25AC%25AC%25E5%259B%259B%25E7%2589%2588%25EF%25BC%2589%2F%25E7%25AC%25AC10%25E7%25AB%25A0%2520%25E5%2587%25BD%25E6%2595%25B0%2F10.14-10.16.%25E9%2597%25AD%25E5%258C%2585.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/simon9124/my_demos/blob/master/javascript%E9%AB%98%E7%BA%A7%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%EF%BC%88%E7%AC%AC%E5%9B%9B%E7%89%88%EF%BC%89/%E7%AC%AC10%E7%AB%A0%20%E5%87%BD%E6%95%B0/10.14-10.16.%E9%97%AD%E5%8C%85.js" ref="nofollow noopener noreferrer">相关代码 →</a></p>
<h1 data-id="heading-0">10.14 闭包</h1>
<ul>
<li><strong>闭包</strong>是指<strong>引用了另一个函数作用域中变量</strong>的函数，通常在嵌套函数中实现（<strong>如果一个函数访问了它的外部变量，那么它就是一个闭包</strong>）
<ul>
<li>闭包中函数的作用域链中，有对外部函数变量的引用</li>
<li>为了<strong>在全局作用域可以访问到闭包函数</strong>，通常在外部函数内<strong>返回</strong>内部闭包函数</li>
<li>因此外部函数<strong>被闭包引用的活动对象</strong>，并<strong>不能</strong>在外部函数执行后被销毁，仍保留在内存中</li>
<li>若要<strong>释放内存</strong>，需<strong>解除闭包函数对外部函数活动对象的引用</strong></li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">arraySort</span>(<span class="hljs-params">key, sort</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-comment">// 内部匿名函数，引用外部函数变量key和sort，形成闭包</span>
    <span class="hljs-keyword">let</span> va = a[key]
    <span class="hljs-keyword">let</span> vb = b[key]
    <span class="hljs-keyword">if</span> (sort === <span class="hljs-string">'asc'</span> || sort === <span class="hljs-literal">undefined</span> || sort === <span class="hljs-string">''</span>) &#123;
      <span class="hljs-comment">// 正序：va > vb</span>
      <span class="hljs-keyword">if</span> (va > vb) <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
      <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (va < vb) <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
      <span class="hljs-keyword">else</span> <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sort === <span class="hljs-string">'desc'</span>) &#123;
      <span class="hljs-comment">// 倒序：va < vb</span>
      <span class="hljs-keyword">if</span> (va < vb) <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
      <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (va > vb) <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
      <span class="hljs-keyword">else</span> <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
    &#125;
  &#125;
&#125;
<span class="hljs-keyword">let</span> compareNames = arraySort(<span class="hljs-string">'name'</span>) <span class="hljs-comment">// 执行函数并返回匿名函数，匿名函数的作用域链仍对arraySort的活动对象key和sort有引用，因此不会被销毁</span>
<span class="hljs-keyword">let</span> result = compareNames(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Nicholas'</span> &#125;, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Matt'</span> &#125;) <span class="hljs-comment">// 执行匿名函数</span>
compareNames = <span class="hljs-literal">null</span> <span class="hljs-comment">// 解除匿名函数对arraySort活动对象的引用，释放内存</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">10.14.1 this 对象</h2>
<ul>
<li>在<strong>闭包内</strong>使用<code>this</code>会让代码更复杂，若内部函数没有使用箭头函数，<code>this</code>绑定给<strong>执行函数的上下文</strong>：
<ul>
<li>全局函数中调用，非严格模式下<code>this</code>指向<code>window</code>，严格模式等于<code>undefined</code></li>
<li>作为某个对象的方法调用，<code>this</code>指向该对象</li>
<li><strong>匿名函数</strong>不会绑定到某个对象，其<code>this</code>指向<strong>调用该匿名函数的对象</strong></li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">global</span>.identity = <span class="hljs-string">'The Window'</span> <span class="hljs-comment">// vscode是node运行环境，无法识别全局对象window，测试时将window改为global</span>
<span class="hljs-keyword">let</span> object = &#123;
  <span class="hljs-attr">identity</span>: <span class="hljs-string">'My Object'</span>,
  <span class="hljs-function"><span class="hljs-title">getIdentityFunc</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.identity
    &#125;
  &#125;,
&#125;
<span class="hljs-built_in">console</span>.log(object.getIdentityFunc()) <span class="hljs-comment">// ƒ () &#123; return this.identity &#125;，返回匿名函数</span>
<span class="hljs-built_in">console</span>.log(object.getIdentityFunc()()) <span class="hljs-comment">// 'The Window'，立即调用匿名函数返回this.identity，this指向全局对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数被调用时自动创建变量<code>this</code>和<code>arguments</code>，<strong>内部函数不能直接访问外部函数的这两个变量</strong>，若想访问需<strong>将其引用先保存到闭包能访问的另一个变量中</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> object2 = &#123;
  <span class="hljs-attr">identity</span>: <span class="hljs-string">'My Object'</span>,
  <span class="hljs-function"><span class="hljs-title">getIdentityFunc</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span> <span class="hljs-comment">// 外部函数的变量this保存在that中</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> that.identity <span class="hljs-comment">// 闭包（匿名函数）中引用that，that指向getIdentityFunc()上下文的this（而非闭包内的this）</span>
    &#125;
  &#125;,
&#125;
<span class="hljs-built_in">console</span>.log(object2.getIdentityFunc()()) <span class="hljs-comment">// 'My Object'，立即调用匿名函数返回that.identity，that指向闭包外部函数getIdentityFunc的this</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>一些特殊情况下的<code>this</code>值</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> object3 = &#123;
  <span class="hljs-attr">identity</span>: <span class="hljs-string">'My Object'</span>,
  <span class="hljs-function"><span class="hljs-title">getIdentity</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.identity
  &#125;,
&#125;
<span class="hljs-built_in">console</span>.log(object3.getIdentity()) <span class="hljs-comment">// 'My Object'</span>
<span class="hljs-built_in">console</span>.log(object3.getIdentity) <span class="hljs-comment">// [Function: getIdentity]，函数getIdentity()</span>
<span class="hljs-built_in">console</span>.log((object3.getIdentity = object3.getIdentity)) <span class="hljs-comment">// [Function: getIdentity]，函数getIdentity()赋值给object3.getIdentity</span>
<span class="hljs-built_in">console</span>.log((object3.getIdentity = object3.getIdentity)()) <span class="hljs-comment">// 'The Window'，赋值后在全局立即调用匿名函数，this指向全局对象</span>
<span class="hljs-built_in">console</span>.log((object3.funcA = object3.getIdentity)()) <span class="hljs-comment">// 'The Window'，函数getIdentity()赋值给对象其他属性，结果相同</span>
object3.funcB = object3.getIdentity
<span class="hljs-built_in">console</span>.log(object3.funcB()) <span class="hljs-comment">// 'My Object'，赋值后在object3调用，this指向object3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">10.14.2 内存泄漏</h2>
<ul>
<li>由于使用了不同的垃圾回收机制，闭包在 IE9 之前的 IE 浏览器会导致问题：一旦 HTML 元素保存在某个闭包的作用域中，其不会被销毁</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">assignHandler</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> element = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'someElement'</span>)
  element.onclick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(element.id) <span class="hljs-comment">// 引用外部函数的活动对象element，匿名函数一直存在因此element不会被销毁</span>
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">assignHandler2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> element = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'someElement'</span>)
  <span class="hljs-keyword">let</span> id = element.id <span class="hljs-comment">// 保存element.id的变量id</span>
  element.onclick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(id) <span class="hljs-comment">// 不直接引用element，改为引用改为引用保存着element.id的变量id</span>
  &#125;
  element = <span class="hljs-literal">null</span> <span class="hljs-comment">// 解除对element对象的引用，释放闭包内存</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">10.15 立即调用的函数表达式</h1>
<ul>
<li><strong>立即调用的匿名函数</strong>又称<strong>立即调用的函数表达式（IIFE）</strong>，其类似于函数声明，被<strong>包含在括号中</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">;(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 块级作用域</span>
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>ES5 尚未支持块级作用域，可以使用 IIFE 模拟</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">;(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3</span>; i++) &#123;
    <span class="hljs-built_in">console</span>.log(i) <span class="hljs-comment">// 0、1、2</span>
  &#125;
&#125;)()
<span class="hljs-built_in">console</span>.log(i) <span class="hljs-comment">// ReferenceError: i is not defined，i在函数体作用域（模拟块级作用域）内</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>ES6 支持块级作用域，无须 IIFE 即可实现同样的功能</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
  <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3</span>; i++) &#123;
    <span class="hljs-built_in">console</span>.log(i) <span class="hljs-comment">// 0、1、2</span>
  &#125;
&#125;
<span class="hljs-built_in">console</span>.log(i) <span class="hljs-comment">// ReferenceError: i is not defined</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3</span>; i++) &#123;
  <span class="hljs-built_in">console</span>.log(i) <span class="hljs-comment">// 0、1、2</span>
&#125;
<span class="hljs-built_in">console</span>.log(i) <span class="hljs-comment">// ReferenceError: i is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>执行<strong>单击处理程序</strong>时，<strong>迭代变量</strong>的值是<strong>循环结束时的最终值</strong>，可以用 IIFE 或块级作用域<strong>锁定每次单击要显示的值</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> divs = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'div'</span>)
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < divs.length; ++i) &#123;
  divs[i].addEventListener(
    <span class="hljs-string">'click'</span>,

    <span class="hljs-comment">// 错误的写法：直接打印（单击处理程序迭代变量的值是循环结束时的最终值）</span>
    <span class="hljs-comment">// function()&#123;</span>
    <span class="hljs-comment">//   console.log(i);</span>
    <span class="hljs-comment">// &#125;</span>

    <span class="hljs-comment">// 正确的写法：立即执行的函数表达式，锁定每次要显示的值</span>
    (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_i</span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(_i)
      &#125;
    &#125;)(i) <span class="hljs-comment">// 参数传入每次要显示的值</span>
  )
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < divs.length; ++i) &#123;
  <span class="hljs-comment">// 用let关键字，在循环内部为每个循环创建独立的变量</span>
  divs[i].addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(i)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>同理，执行<strong>超时逻辑</strong>时，<strong>迭代变量</strong>的值是<strong>导致循环退出的值</strong>，同样可用 IIFE 或块级作用域<strong>锁定每次要迭代的值</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">5</span>; i++) &#123;
  <span class="hljs-comment">// 超时逻辑在退出循环后执行，迭代变量保存的是导致循环退出的值5</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(i) <span class="hljs-comment">// 5、5、5、5、5</span>
  &#125;, <span class="hljs-number">0</span>)
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">5</span>; i++) &#123;
  <span class="hljs-comment">// 用立即调用的函数表达式，传入每次循环的当前索引，锁定每次超时逻辑应该显示的索引值</span>
  ;(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_i</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(_i) <span class="hljs-comment">// 0、1、2、3、4</span>
    &#125;, <span class="hljs-number">0</span>)
  &#125;)(i)
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">5</span>; i++) &#123;
  <span class="hljs-comment">// 使用let声明：为每个迭代循环声明新的迭代变量</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(i) <span class="hljs-comment">// 0、1、2、3、4</span>
  &#125;, <span class="hljs-number">0</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">10.16 私有变量</h1>
<ul>
<li>任何定义在<strong>函数</strong>或<strong>块中</strong>的变量，都可以认为是<strong>私有</strong>的（函数或块的外部无法访问其中的变量）</li>
<li>私有变量包括<strong>函数参数</strong>、<strong>局部变量</strong>和<strong>函数内部定义的其他函数</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">num1, num2</span>) </span>&#123;
  <span class="hljs-comment">// 3个私有变量：参数num1、参数num2、局部变量sum</span>
  <span class="hljs-keyword">let</span> sum = num1 + num2
  <span class="hljs-keyword">return</span> sum
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>特权方法</strong>是能够访问函数的私有变量（及私有函数）的公共方法，可在<strong>构造函数</strong>中实现</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyObject</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> privateVariable = <span class="hljs-number">10</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">privateFunction</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'privateFunction'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  &#125;
  <span class="hljs-comment">// 特权方法（闭包）：访问私有变量privateVariable和私有方法privateFunction()</span>
  <span class="hljs-built_in">this</span>.publicMethod = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'privateVariable'</span>, privateVariable++)
    <span class="hljs-keyword">return</span> privateFunction()
  &#125;
&#125;
<span class="hljs-keyword">let</span> obj = <span class="hljs-keyword">new</span> MyObject()
obj.publicMethod()
<span class="hljs-comment">/* 
  privateVariable 10
  privateFunction
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>同<strong>构造函数的缺点</strong>，在构造函数中实现私有变量的问题是：<strong>每个实例都重新创建方法（私有方法&特权方法），机制相同的 Function 对象被多次实例化</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-comment">/* 私有变量name无法被直接访问到，只能通过getName()和setName()特权方法读写 */</span>
  <span class="hljs-built_in">this</span>.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> name
  &#125;
  <span class="hljs-built_in">this</span>.setName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_name</span>) </span>&#123;
    name = _name
  &#125;
&#125;
<span class="hljs-keyword">let</span> person = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'Nicholas'</span>) <span class="hljs-comment">// 每创建一个实例都创建一遍方法（私有方法&特权方法）</span>
<span class="hljs-built_in">console</span>.log(person.getName()) <span class="hljs-comment">// 'Nicholas'</span>
person.setName(<span class="hljs-string">'Greg'</span>)
<span class="hljs-built_in">console</span>.log(person.getName()) <span class="hljs-comment">// 'Greg'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">10.16.1 静态私有变量</h2>
<ul>
<li>使用<strong>匿名函数表达式</strong>创建<strong>私有作用域</strong>，实现特权方法：
<ul>
<li>定义<strong>私有变量</strong>和<strong>私有方法</strong>
<ul>
<li>私有变量作为<strong>静态私有变量</strong>，被<strong>共享</strong>，但<strong>不存在</strong>于每个实例中</li>
</ul>
</li>
<li>定义<strong>构造函数</strong>
<ul>
<li>使用<strong>函数表达式</strong>定义构造函数（函数声明会创建内部函数）</li>
<li><strong>不使用关键字</strong>定义构造函数，使其创建在<strong>全局作用域</strong>中</li>
</ul>
</li>
<li>定义<strong>公有方法（特权方法）</strong>
<ul>
<li>定义在构造函数的<strong>原型</strong>上</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">;(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">/* 匿名函数表达式，创建私有作用域 */</span>

  <span class="hljs-comment">// 私有变量和私有方法，被隐藏</span>
  <span class="hljs-keyword">let</span> privateVariable = <span class="hljs-number">10</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">privateFunction</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  &#125;

  <span class="hljs-comment">// 构造函数：使用函数表达式 & 不使用关键字（创建在全局作用域）</span>
  MyObject = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;

  <span class="hljs-comment">// 公有方法/特权方法（闭包）：定义在构造函数的原型上</span>
  MyObject.prototype.publicMethod = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'privateVariable'</span>, privateVariable++)
    <span class="hljs-keyword">return</span> privateFunction()
  &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>该方式下，私有变量和私有方法由实例<strong>共享</strong>，<strong>特权方法</strong>定义在原型上，也由实例<strong>共享</strong></li>
<li>创建实例<strong>不会重新创建方法</strong>，但<strong>调用特权方法并修改静态私有变量</strong>会<strong>影响所有实例</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">;(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 私有变量name，被隐藏</span>
  <span class="hljs-keyword">let</span> name = <span class="hljs-string">''</span>

  <span class="hljs-comment">// 构造函数，创建在全局作用域中</span>
  Person = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_name</span>) </span>&#123;
    name = _name
  &#125;

  <span class="hljs-comment">// 特权方法，定义在构造函数原型上</span>
  Person.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> name
  &#125;
  Person.prototype.setName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_name</span>) </span>&#123;
    name = _name
  &#125;
&#125;)()

<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'Nicholas'</span>)
<span class="hljs-built_in">console</span>.log(person1.getName()) <span class="hljs-comment">// 'Nicholas'</span>
person1.setName(<span class="hljs-string">'Matt'</span>)
<span class="hljs-built_in">console</span>.log(person1.getName()) <span class="hljs-comment">// 'Matt'</span>

<span class="hljs-keyword">let</span> person2 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'Michael'</span>)
<span class="hljs-built_in">console</span>.log(person2.getName()) <span class="hljs-comment">// 'Michael'，调用特权方法并修改静态私有变量</span>
<span class="hljs-built_in">console</span>.log(person1.getName()) <span class="hljs-comment">// 'Michael'，影响所有实例</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">10.16.2 模块模式</h2>
<ul>
<li>在<strong>单例对象</strong>基础上加以扩展，通过<strong>作用域链</strong>关联私有变量和特权方法:
<ul>
<li>将单例对象的<strong>对象字面量</strong>扩展为<strong>立即调用的函数表达式</strong></li>
<li>在匿名函数内部，定义私有变量和私有方法</li>
<li>在匿名函数内部，<strong>返回</strong>只包含可以公开访问属性和方法的<strong>对象字面量</strong></li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> singleton = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">/* 立即调用的函数表达式，创建私有作用域 */</span>

  <span class="hljs-comment">// 私有变量和私有方法，被隐藏</span>
  <span class="hljs-keyword">let</span> privateVariable = <span class="hljs-number">10</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">privateFunction</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  &#125;

  <span class="hljs-comment">// 返回只包含可以公开访问属性和方法的对象字面量</span>
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">publicProperty</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-function"><span class="hljs-title">publicMethod</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(++privateVariable)
      <span class="hljs-keyword">return</span> privateFunction
    &#125;,
  &#125;
&#125;)()
<span class="hljs-built_in">console</span>.log(singleton) <span class="hljs-comment">// &#123; publicProperty: true, publicMethod: [Function: publicMethod] &#125;</span>
singleton.publicMethod() <span class="hljs-comment">// 11</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>本质</strong>上，该模式用对象字面量定义了<strong>单例对象的公共接口</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">BaseComponent</span>(<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// BaseComponent组件</span>

<span class="hljs-keyword">let</span> application = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> components = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>() <span class="hljs-comment">// 创建私有数组components</span>
  components.push(<span class="hljs-keyword">new</span> BaseComponent()) <span class="hljs-comment">// 初始化，将BaseComponent组件的新实例添加到数组中</span>

  <span class="hljs-comment">/* 公共接口 */</span>
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-comment">// getComponentCount()特权方法：返回注册组件数量</span>
    <span class="hljs-function"><span class="hljs-title">getComponentCount</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> components.length
    &#125;,
    <span class="hljs-comment">// registerComponent()特权方法：注册组件</span>
    <span class="hljs-function"><span class="hljs-title">registerComponent</span>(<span class="hljs-params">component</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> component === <span class="hljs-string">'object'</span>) &#123;
        components.push(component)
      &#125;
    &#125;,
    <span class="hljs-comment">// getRegistedComponents()特权方法：查看已注册的组件</span>
    <span class="hljs-function"><span class="hljs-title">getRegistedComponents</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> components
    &#125;,
  &#125;
&#125;)()

<span class="hljs-built_in">console</span>.log(application.getComponentCount()) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(application.getRegistedComponents()) <span class="hljs-comment">// [ BaseComponent &#123;&#125; ]，已注册组件BaseComponent</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">APPComponent</span>(<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// APPComponent组件</span>
application.registerComponent(<span class="hljs-keyword">new</span> APPComponent()) <span class="hljs-comment">// 注册组件APPComponent</span>
<span class="hljs-built_in">console</span>.log(application.getComponentCount()) <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(application.getRegistedComponents()) <span class="hljs-comment">// [ BaseComponent &#123;&#125;, APPComponent &#123;&#125; ]，已注册组件BaseComponent和APPComponent</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">10.16.3 模块增强模式</h2>
<ul>
<li>利用<strong>模块模式</strong>，在<strong>返回对象前</strong>进行增强，适合<strong>单例对象为某个特定类型的实例，但必须给它添加额外属性或方法</strong>的场景：
<ul>
<li>在匿名函数内部，定义私有变量和私有方法</li>
<li>在匿名函数内部，<strong>创建某（特定）类型的实例</strong></li>
<li>给实例对象添加共有属性和方法（增强）</li>
<li>返回实例对象</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CustomType</span>(<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// 特定类型</span>
<span class="hljs-keyword">let</span> singleton2 = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 私有变量和私有方法，被隐藏</span>
  <span class="hljs-keyword">let</span> privateVariable = <span class="hljs-number">10</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">privateFunction</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  &#125;

  <span class="hljs-comment">// 创建特定类型的实例</span>
  <span class="hljs-keyword">let</span> object = <span class="hljs-keyword">new</span> CustomType()

  <span class="hljs-comment">// 添加公有属性和方法</span>
  object.publicProperty = <span class="hljs-literal">true</span>
  object.publicMethod = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(++privateVariable)
    <span class="hljs-keyword">return</span> privateFunction
  &#125;

  <span class="hljs-comment">// 返回实例</span>
  <span class="hljs-keyword">return</span> object
&#125;)()
<span class="hljs-built_in">console</span>.log(singleton2) <span class="hljs-comment">// CustomType &#123; publicProperty: true, publicMethod: [Function: publicMethod] &#125;</span>
singleton2.publicMethod() <span class="hljs-comment">// 11</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>以<strong>模块模式</strong>的<strong>单例对象公共接口</strong>为例，若<code>application</code>必须是<code>BaseComponent</code>组件的实例，可以使用模块增强模式来创建：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> application2 = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> components = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>() <span class="hljs-comment">// 创建私有数组components</span>
  components.push(<span class="hljs-keyword">new</span> BaseComponent()) <span class="hljs-comment">// 初始化，将BaseComponent组件的新实例添加到数组中</span>
  <span class="hljs-keyword">let</span> app = <span class="hljs-keyword">new</span> BaseComponent() <span class="hljs-comment">// 创建局部变量保存实例</span>

  <span class="hljs-comment">/* 公共接口 */</span>
  <span class="hljs-comment">// getComponentCount()特权方法：返回注册组件数量</span>
  app.getComponentCount = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> components.length
  &#125;
  <span class="hljs-comment">// registerComponent()特权方法：注册组件</span>
  app.registerComponent = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">component</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> component === <span class="hljs-string">'object'</span>) &#123;
      components.push(component)
    &#125;
  &#125;
  <span class="hljs-comment">// getRegistedComponents()特权方法：查看已注册的组件</span>
  app.getRegistedComponents = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> components
  &#125;

  <span class="hljs-keyword">return</span> app <span class="hljs-comment">// 返回实例</span>
&#125;)()

<span class="hljs-built_in">console</span>.log(application2) <span class="hljs-comment">// BaseComponent &#123; getComponentCount: [Function (anonymous)], registerComponent: [Function (anonymous)], getRegistedComponents: [Function (anonymous)] &#125;</span>
<span class="hljs-built_in">console</span>.log(application2.getComponentCount()) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(application2.getRegistedComponents()) <span class="hljs-comment">// [ BaseComponent &#123;&#125; ]，已注册组件BaseComponent</span>

application2.registerComponent(<span class="hljs-keyword">new</span> APPComponent()) <span class="hljs-comment">// 注册组件APPComponent</span>
<span class="hljs-built_in">console</span>.log(application2.getComponentCount()) <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(application2.getRegistedComponents()) <span class="hljs-comment">// [ BaseComponent &#123;&#125;, APPComponent &#123;&#125; ]，已注册组件BaseComponent和APPComponent</span>
<span class="copy-code-btn">复制代码</span></code></pre>



































<table><thead><tr><th></th><th>私有变量 & 私有方法</th><th>特权方法</th><th>缺点</th></tr></thead><tbody><tr><td>构造函数</td><td>实例中，独立</td><td>实例中</td><td>每个实例重新创建方法（私有方法&特权方法）</td></tr><tr><td>私有作用域</td><td>私有作用域中，静态，共享</td><td>构造函数原型上</td><td>调用特权方法修改私有变量，影响其他实例</td></tr><tr><td>模块模式</td><td>私有作用域中，独立</td><td>单例对象上</td><td></td></tr><tr><td>模块增强模式</td><td>私有作用域中，独立</td><td>实例对象上</td><td></td></tr></tbody></table>
<h1 data-id="heading-8">总结 & 问点</h1>
<ul>
<li>什么是闭包？其作用是什么？</li>
<li>在没有使用箭头函数的情况下，this 在全局和局部方法调用时，分别指向哪里？若是匿名函数中的 this 呢？</li>
<li>函数嵌套时，内部函数如何访问外部函数的 this 和 arguments?</li>
<li>什么是立即调用的函数表达式？请用代码用其模拟块级作用域</li>
<li>请用代码实现功能：获取所有的 div 元素，点击不同的 div 显示其相应的索引值。要求分别用 IIFE 和块级作用域实现</li>
<li>请用代码实现功能：1 秒后实现 0~4 的数字迭代。要求分别用 IIFE 和块级作用域实现</li>
<li>什么是私有变量？其可能包括哪些内容？</li>
<li>什么是特权方法？请写一段代码，在构造函数中实现特权方法，并说说这种方式有什么问题</li>
<li>请写一段代码，通过私有变量实现特权方法，说说并证明这种方式有什么局限</li>
<li>请写一段代码，通过模块模式定义单例对象的公共接口，实现 Web 组件注册</li>
<li>模块增强模式适合什么场景？请用代码实现其模式下的 Web 组件注册</li>
</ul></div>  
</div>
            