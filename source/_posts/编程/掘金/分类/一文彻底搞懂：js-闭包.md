
---
title: '一文彻底搞懂：js-闭包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8347'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 14:40:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=8347'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">什么是闭包</h3>
<p>官方解释：</p>
<blockquote>
<p>一个函数和对其周围状态（<strong>lexical environment，词法环境</strong>）的引用捆绑在一起（或者说函数被引用包围），这样的组合就是<strong>闭包</strong>（<strong>closure</strong>）。也就是说，闭包让你可以在一个内层函数中访问到其外层函数的作用域。在 JavaScript 中，每当创建一个函数，闭包就会在函数创建的同时被创建出来。</p>
</blockquote>
<p>我们通俗的理解一下就是：</p>
<p>函数引用了它的外面的变量，就形成了闭包。</p>
<p>下面代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">block</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> name = <span class="hljs-string">'RiverLi'</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">displayName</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>).innerText = name
  &#125;
  displayName()
&#125;
block()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行之后界面上能正确显示结果。上面的代码并不难理解，因为它和下面的代码很相似，区别只是displayName所在的上下文环境不一样，上面的代码中它在 block 函数的作用域内， 下面的代码它在全局作用域内。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> name = <span class="hljs-string">'RiverLi'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">displayName</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>).innerText = name
&#125;
displayName()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但下面的代码就令人迷惑了，block 方法中没有执行displayName 而是将displayName作为函数的返回值return了。在调用Block之后，接收到返回值之后执行fun。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">block</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> name = <span class="hljs-string">'RiverLi'</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">displayName</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>).innerText = name
  &#125;
  <span class="hljs-keyword">return</span> displayName
&#125;
<span class="hljs-keyword">let</span> fun = block()
fun()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那，它能执行成功吗？按道理来讲，block执行完毕之后 name 就销毁了，因为name的作用域在block方法内，但 答案是肯定的，界面依然正确显示。这里就涉及到了闭包的概念：<strong>闭包是由函数以及声明该函数的词法环境组合而成的。该环境包含了这个闭包创建时作用域内的任何局部变量。</strong> displayName创建的作用域是block函数内部，所以displayName执行的时候能访问到block函数作用域内的任何变量。</p>
<p>下面代码中，dispayName 虽然在同一作用域内声明，但fun1和fun2的上下文环境是不一样的，因为是两个block实例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">block</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispayName</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(name)
  &#125;
  <span class="hljs-keyword">return</span> dispayName
&#125;
<span class="hljs-keyword">let</span> fun1 = block(<span class="hljs-string">'1111'</span>)
fun1()
<span class="hljs-keyword">let</span> fun2 = block(<span class="hljs-string">'2222'</span>)
fun2()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">闭包的用途</h3>
<h4 data-id="heading-2">模拟私有方法</h4>
<p>下面代码中，Counter 内部的 changeValue 方法在外部是无法访问到的，只能通过 increment、decrement 方法进行数据的操作，通过value方法获取值，这就使得 changeValue 是私用的方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> _value = <span class="hljs-number">0</span>;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">changeValue</span>(<span class="hljs-params">num</span>) </span>&#123;
    _value += num
  &#125;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">increment</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      changeValue(<span class="hljs-number">1</span>)
    &#125;,
    <span class="hljs-attr">decrement</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      changeValue(-<span class="hljs-number">1</span>)
    &#125;,
    <span class="hljs-attr">value</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> _value
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">let</span> counter1 = Counter()
counter1.increment()
counter1.increment()
<span class="hljs-built_in">console</span>.log(counter1.value())
counter1.decrement()
<span class="hljs-built_in">console</span>.log(counter1.value())
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">避免闭包陷阱</h3>
<p>下面代码中，我们希望实现点击输入框的时候提示对应的提示文案，但效果是，每次的提示文案都是<code>Your age (you must be over 16</code> 。这是因为闭包的行为发生在for循环内部，也就是说闭包能访问到for循环内部的所有变量，值得我们注意的是 item 是使用var声明的，我们知道这会导致变量提升，每次for循环都更新了item的值，最后访问的是item最后一次被赋值的值。解法方法有：</p>
<ol>
<li>使用let 修饰item变量，避免提升。</li>
<li>使用更多的闭包。</li>
<li>使用匿名闭包。</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>闭包<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"help"</span>></span>Helpful notes will appear here<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>E-mail: <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"email"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"email"</span> /></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Name: <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"name"</span> /></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Age: <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"age"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"age"</span> /></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showHelp</span>(<span class="hljs-params">help</span>) </span>&#123;
        <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>).innerHTML = help;
      &#125;
      
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeHelper</span>(<span class="hljs-params">help</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            showHelp(help)
        &#125;
      &#125;

      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setupHelp</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> helpText = [
          &#123; <span class="hljs-attr">id</span>: <span class="hljs-string">"email"</span>, <span class="hljs-attr">help</span>: <span class="hljs-string">"Your e-mail address"</span> &#125;,
          &#123; <span class="hljs-attr">id</span>: <span class="hljs-string">"name"</span>, <span class="hljs-attr">help</span>: <span class="hljs-string">"Your full name"</span> &#125;,
          &#123; <span class="hljs-attr">id</span>: <span class="hljs-string">"age"</span>, <span class="hljs-attr">help</span>: <span class="hljs-string">"Your age (you must be over 16"</span> &#125;,
        ];

        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < helpText.length; i++) &#123;
          <span class="hljs-keyword">var</span> item = helpText[i];
          <span class="hljs-built_in">document</span>.getElementById(item.id).onfocus = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            showHelp(item.help);
          &#125;;
        &#125;
        <span class="hljs-comment">/*
        //使用更多的闭包
        for (var i = 0; i < helpText.length; i++) &#123;
          var item = helpText[i];
          document.getElementById(item.id).onfocus = makeHelper(item.help)
        &#125;
        */</span>

        <span class="hljs-comment">/*
        //是用let 解决闭包
        for (var i = 0; i < helpText.length; i++) &#123;
          let item = helpText[i];
          document.getElementById(item.id).onfocus = function () &#123;
            showHelp(item.help);
          &#125;;
        &#125;
        */</span>

        <span class="hljs-comment">/*
        //使用匿名函数解决闭包
        for (var i = 0; i < helpText.length; i++) &#123;
          (function () &#123;
            var item = helpText[i];
            document.getElementById(item.id).onfocus = function () &#123;
              showHelp(item.help);
            &#125;;
          &#125;)();
        &#125;
        */</span>
      &#125;
      setupHelp()
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">闭包的性能问题</h3>
<p>如果没有特定需求，建议避免使用闭包，因为在它使得上下文作用域不释放或者延迟是否，会增加内存的销毁，降低执行效率。</p>
<p>更多优质内容，请扫码关注公众号：<a href="https://link.juejin.cn/?target=https%3A%2F%2Friverli.oss-cn-beijing.aliyuncs.com%2Ftuiguang%2FRiverLi.jpg" target="_blank" rel="nofollow noopener noreferrer" title="https://riverli.oss-cn-beijing.aliyuncs.com/tuiguang/RiverLi.jpg" ref="nofollow noopener noreferrer">RiverLi</a>。在公众号回复关键字「大前端进阶」，可领取独家资料。</p></div>  
</div>
            