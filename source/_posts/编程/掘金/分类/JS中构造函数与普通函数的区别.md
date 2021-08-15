
---
title: 'JS中构造函数与普通函数的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7318'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 01:21:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=7318'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、两者区别在于：</h3>
<h5 data-id="heading-1">1、调用方式不一样</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//构造函数也是一个普通函数，创建方式和普通函数一样。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
Foo();<span class="hljs-comment">//普通函数调用方式</span>
<span class="hljs-keyword">var</span> f = <span class="hljs-keyword">new</span> Foo();<span class="hljs-comment">//构造函数调用方式</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>普通函数调用方式：直接调用person();</li>
<li>构造函数调用方式：需要使用new关键字来调用 new person();</li>
</ul>
<h5 data-id="heading-2">2、作用也不一样（构造函数用来新建实例对象）</h5>
<h5 data-id="heading-3">3、首字母大小写习惯</h5>
<ul>
<li>一般构造函数的函数名称会用大写</li>
<li>普通函数用小写</li>
</ul>
<h5 data-id="heading-4">4、函数中this的指向不同</h5>
<ul>
<li>普通函数中的this，在严格模式下指向undefined，非严格模式下指向window对象。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>===<span class="hljs-built_in">window</span>);
&#125;
foo();
<span class="hljs-comment">//代码运行结果：true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>构造函数的this则是指向它创建的对象实例。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">this</span>.name = <span class="hljs-string">"令狐冲"</span>;
&#125;
<span class="hljs-keyword">var</span> f = <span class="hljs-keyword">new</span> Foo();
<span class="hljs-built_in">console</span>.log(f.name);
<span class="hljs-comment">//代码运行结果：令狐冲</span>
<span class="hljs-comment">//补充：构造函数的函数名和类名相同：Foo()这个构造函数，Foo是函数名，也是这个对象的类名。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">5、写法的不同</h5>
<p><strong>构造函数：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>)</span>&#123;
<span class="hljs-built_in">this</span>.name = name;
&#125;
<span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'John'</span>);<span class="hljs-comment">//使用new关键字，不使用return</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>普通函数：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">person</span>(<span class="hljs-params">name</span>)</span>&#123;
<span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
obj.name = name;
<span class="hljs-keyword">return</span> obj;<span class="hljs-comment">//使用return</span>
&#125;
<span class="hljs-keyword">var</span> p = person(<span class="hljs-string">'john'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">person</span>(<span class="hljs-params">name</span>)</span>&#123;
<span class="hljs-built_in">this</span>.name = name;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;<span class="hljs-comment">//使用return</span>
&#125;
<span class="hljs-keyword">var</span> p = person(<span class="hljs-string">'john'</span>),
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            