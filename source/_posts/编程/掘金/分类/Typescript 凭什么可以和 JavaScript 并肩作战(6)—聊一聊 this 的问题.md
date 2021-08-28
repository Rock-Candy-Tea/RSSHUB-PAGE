
---
title: 'Typescript 凭什么可以和 JavaScript 并肩作战(6)—聊一聊 this 的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1592'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 02:01:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=1592'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第28天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<blockquote>
<p>在 JavaScript 有关 this 问题，一直以来也是面试官喜欢问的一个问题，特别是 this 的指向问题，所以今天我们就聊一聊在 TypeScript 中类和方法中 this 指向问题。</p>
</blockquote>
<p>重要的是要记住，TypeScript 并没有改变 JavaScript 的运行时行为，而 JavaScript 因为有一些独特的运行时行为。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;
    name = <span class="hljs-string">"MyClass"</span>;
    <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> c = <span class="hljs-keyword">new</span> MyClass();
  <span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"obj"</span>,
    <span class="hljs-attr">getName</span>: c.getName,
  &#125;;
   
  <span class="hljs-comment">// Prints "obj", not "MyClass"</span>
  <span class="hljs-built_in">console</span>.log(obj.getName());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>长话短说，默认情况下，函数内<code>this</code> 具体表示什么值是取决于函数的调用方式。在这个例子中，因为函数是通过<code>obj</code> 引用调用的，所以 <code>this</code>值是<code>obj</code>而不是类实例。这很少是你希望发生的事情! TypeScript提供了一些方法来减轻或防止这种错误。</p>
<h3 data-id="heading-0">箭头函数</h3>
<p>如何经常会遇到这种情况，调用函数时丢失了函数的 ·<code>this</code> 这个上下文对象，为了 <code>this</code> 丢失可以通过箭头函数来代替普通函数来解决这个问题。</p>
<p><code>call</code>、<code>apply</code>和 <code>bind</code>方法不适合箭头函数，因为它们被设计为允许方法在不同的作用域内执行。因为箭头函数根据箭头函数定义的作用域来定义 <code>this</code>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;
    name = <span class="hljs-string">"MyClass"</span>;
    getName = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
    &#125;
&#125;
<span class="hljs-keyword">const</span> c = <span class="hljs-keyword">new</span> MyClass();
<span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"obj"</span>,
    <span class="hljs-attr">getName</span>: c.getName,
&#125;;

<span class="hljs-comment">// Prints "obj", not "MyClass"</span>
<span class="hljs-built_in">console</span>.log(obj.getName());
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">需要做一些权衡</h4>
<ul>
<li>即使在没有 <code>TpyeScript</code> 对代码进行检测情况下，在运行时也需要保证<code>this</code>值保证正确地使用</li>
<li>这将占用更多的内存，因为类每一个实例都会拥有这种方式定义的方法的副本</li>
<li>无法在子类中使用<code>super.getName</code>，因为在原型链中没有条目可以获取基类方法</li>
</ul>
<p>在类中，一个叫做<code>this</code>的特殊类型动态地指向当前类的类型。接下来，下面的例子中可以看到<code>modelType</code> 类型为 <code>Model3</code>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span></span>&#123;
    <span class="hljs-attr">model</span>:<span class="hljs-built_in">string</span> = <span class="hljs-string">""</span>
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">model:<span class="hljs-built_in">string</span></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.model = model
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Model3</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Car</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.model = <span class="hljs-string">""</span>
    &#125;
&#125;

<span class="hljs-keyword">const</span> model_3 = <span class="hljs-keyword">new</span> Model3()
<span class="hljs-keyword">const</span> modelType = model_3.set(<span class="hljs-string">"model 3"</span>) <span class="hljs-comment">// Model3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>this</code> 也可以作为类方法的参数的类型使用</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Rect</span></span>&#123;
    <span class="hljs-attr">width</span>:<span class="hljs-built_in">number</span>;
    height:<span class="hljs-built_in">number</span>;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">w:<span class="hljs-built_in">number</span>,h:<span class="hljs-built_in">number</span></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.width = w;
        <span class="hljs-built_in">this</span>.height = h;
    &#125;

    <span class="hljs-function"><span class="hljs-title">compareWith</span>(<span class="hljs-params">other:<span class="hljs-built_in">this</span></span>)</span>&#123;
        
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这与写其他不同。Rect 的子类 Square 的 compareWith 方法现只接受的子类只是继承没否实现自己方法或定义自己的属性，例如<code>length:number = 0</code> 这是实例上调用 <code>compareWith</code> 方法就无法接受 <code>Rect</code> 的实例来作为参数</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Square</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Rect</span></span>&#123;
    <span class="hljs-attr">length</span>:<span class="hljs-built_in">number</span> = <span class="hljs-number">0</span>
&#125;

<span class="hljs-keyword">const</span> rect = <span class="hljs-keyword">new</span> Rect(<span class="hljs-number">12</span>,<span class="hljs-number">15</span>)

<span class="hljs-keyword">const</span> square = <span class="hljs-keyword">new</span> Square(<span class="hljs-number">12</span>,<span class="hljs-number">12</span>)

<span class="hljs-built_in">console</span>.log(square.compareWith(rect))
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            