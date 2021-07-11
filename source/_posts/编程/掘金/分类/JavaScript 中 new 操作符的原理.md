
---
title: 'JavaScript 中 new 操作符的原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=45'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 05:14:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=45'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">🎯总结</h1>
<ol>
<li>创建一个<strong>空对象</strong></li>
<li>空对象的内部属性 <code>__proto__</code> 赋值为构造函数的 <code>prototype</code> 属性</li>
<li>将构造函数的 <code>this</code> 指向空对象</li>
<li>执行构造函数内部代码</li>
<li>返回该新对象</li>
</ol>
<h1 data-id="heading-1">详细说明</h1>
<p>执行 new 操作时会依次经过以下步骤：</p>
<ol>
<li>
<p>创建一个<strong>空对象</strong></p>
<ul>
<li>空对象是 Object 的实例，即 <code>&#123;&#125;</code> 。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>空对象的内部属性 <code>__proto__</code> 赋值为构造函数的 <code>prototype</code> 属性</p>
<ul>
<li>该操作是为了将空对象链接到正确的原型上去</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.number = num
&#125;

obj.__proto__ = Foo.prototype
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>将构造函数的 <code>this</code> 指向空对象</p>
<ul>
<li>即构造函数内部的 this 被赋值为空对象，以便后面正确执行构造函数。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">Foo.call(obj, <span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>执行构造函数内部代码</p>
<ul>
<li>即给空对象添加属性、方法。</li>
</ul>
</li>
<li>
<p>返回该新对象</p>
<ul>
<li>如果构造函数内部通过 return 语句返回了一个引用类型值，则 new 操作最终返回这个引用类型值；否则返回刚创建的新对象。</li>
<li>引用类型值：除基本类型值（数值、字符串、布尔值、null、undefined、Symbol 值）以外的所有值。</li>
</ul>
</li>
</ol>
<h1 data-id="heading-2">模拟 new 操作符</h1>
<p>下面的 <code>myNew</code> 函数模拟了 new 操作符的行为</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myNew</span>(<span class="hljs-params">func, ...args</span>) </span>&#123;
  <span class="hljs-keyword">let</span> obj = &#123;&#125;
  obj.__proto__ = func.prototype
  <span class="hljs-keyword">let</span> res = func.apply(obj, args)
  <span class="hljs-keyword">return</span> res <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span> ? res : obj
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.number = num
&#125;

<span class="hljs-keyword">let</span> foo1 = myNew(Foo, <span class="hljs-number">1</span>)
<span class="hljs-built_in">console</span>.log(foo1 <span class="hljs-keyword">instanceof</span> Foo)  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(foo1.number)  <span class="hljs-comment">// 1</span>

<span class="hljs-keyword">let</span> foo2 = <span class="hljs-keyword">new</span> Foo(<span class="hljs-number">2</span>)
<span class="hljs-built_in">console</span>.log(foo2 <span class="hljs-keyword">instanceof</span> Foo)  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(foo2.number)  <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面通过 <code>instanceof</code> 操作符来判断构造函数的返回值是否为 <code>Object</code> 的实例，即是否为引用类型值；这是因为所有引用类型值都是 Object 的实例，Object 是所有引用类型值的基类型。</p></div>  
</div>
            