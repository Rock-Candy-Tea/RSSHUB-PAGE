
---
title: 'JavaScript中 prototype 原型继承'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f718cbe37c0a4707b60e0267c628c86c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 00:48:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f718cbe37c0a4707b60e0267c628c86c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">原型继承</h1>
<p>说到原型继承，那就是要从原型入手，就让我们来简单回顾一下什么是原型吧</p>
<blockquote>
<p>原型概述：每个函数身上都有一个原型，我们称之为原型对象</p>
</blockquote>
<p>函数的 prototype 属性指向原型对象，原型对象上的 constructor 指回构造函数</p>
<p>那么顾名思义，原型对象那就要从原型下手啦 ! !</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.uname = <span class="hljs-string">'张三'</span>, 
  <span class="hljs-built_in">this</span>.age = <span class="hljs-number">22</span>
&#125;
<span class="hljs-comment">// 原型对象</span>
Person.prototype.sex = <span class="hljs-string">'男'</span>
Person.prototype.head = <span class="hljs-number">1</span>
Person.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello javascript'</span>)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Son</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.eye = <span class="hljs-number">2</span>
&#125;

<span class="hljs-comment">// 把构造函数 Person 的实例化对象赋值给构造函数 Son 的原型对象，那么在构造函数 Person 原型上添加的属性或者方法， Son的实例对象也是可以访问到的，这正是原型链起到的作用</span>
Son.prototype = <span class="hljs-keyword">new</span> Person()

<span class="hljs-comment">// 实例化对象</span>
<span class="hljs-keyword">let</span> per = <span class="hljs-keyword">new</span> Son()
<span class="hljs-built_in">console</span>.log(per)

<span class="hljs-comment">// 可以访问原型对象上添加的属性</span>
per.sayName()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>sayName 方法定义在了构造函数 Person 的原型上，而通过构造函数 Son 的实例对象却能够访问得到，那么 sayName 方法相当于定义在了 Son 原型对象的原型对象上，之所以 Son 的实例化对象能够访问得到，那正是原型链的功劳</p>
<p>通过 <code>per.sayName()</code> 可以早控制台看到打印结果 <code>'hello javascript'</code></p>
<p>上面代码运行，打印Son 的实例化对象 per ，可以看到如下图， 正是 (<code>Son.prototype = new Person()</code>) 让Son的原型对象变成了 <code>new Person()</code>,  而且 Person 的原型对象上也有我们自己定义的属性方法， 并且它的 <strong>constructor</strong> 指回 <strong>构造函数 Person</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f718cbe37c0a4707b60e0267c628c86c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
喜欢的小伙伴，点个赞再走呗 ！！</div>  
</div>
            