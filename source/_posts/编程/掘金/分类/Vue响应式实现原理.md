
---
title: 'Vue响应式实现原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23515a73d6dc4553a54cacbe533fc5e1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 20:33:50 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23515a73d6dc4553a54cacbe533fc5e1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Vue的一大特性就是响应式。这里的响应式指的是，当状态发生变化时，系统会自动更新关联状态。在Vue中的具体表现有：当数据发生改变时，触发视图重新渲染；computed属性在依赖值发生变化时，自动重新计算新值；提供watch监听器，可以监听到数据的变化。</p>
<p>这些都是怎么实现的呢？Vue2和Vue3中关于响应式实现的原理不太一样，Vue2使用ES5的defineProperty实现，而Vue3使用的是ES6的propxy.(PS:这也就是为什么Vue2不支持IE7/8，而Vue3不支持IE11.)</p>
<h3 data-id="heading-0">defineProperty实现</h3>
<blockquote>
<p>Object.defineProperty() 方法会直接在一个对象上定义一个新属性，或者修改一个对象的现有属性，并返回此对象。</p>
</blockquote>
<p>语法：</p>
<blockquote>
<p>Object.defineProperty(obj, prop, descriptor)</p>
</blockquote>
<ol>
<li>第一个参数obj：要设置属性的对象；</li>
<li>第二个参数prop：要设置的属性名,这个属性可以是已存在也可以是不存在的；</li>
<li>第三个参数descriptor:该参数接收一个对象，用来对属性进行描述。如value(值),writable(是否可重写)，enumerable(是否可枚举)等</li>
</ol>
<p>举个🌰：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> student = &#123;&#125;;

<span class="hljs-built_in">Object</span>.defineProperty(student, <span class="hljs-string">'age'</span>, &#123;
  <span class="hljs-attr">value</span>: <span class="hljs-number">17</span>,
  <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>
&#125;);

student.age = <span class="hljs-number">18</span>;

<span class="hljs-built_in">console</span>.log(student.age);<span class="hljs-comment">//打印出18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子里，定义了一个student对象。然后通过defineProperty给该对象定义了age属性，该属性值是可写的。所以，后面我们可以修改这个student对象age的值。</p>
<p>那之所以能够用来它实现响应式，是因为它的第三个参数，还提供了getter和setter方法。</p>
<blockquote>
<p>get: 属性的 getter 函数，如果没有 getter，则为 undefined。当访问该属性时，会调用此函数。该函数的返回值会被用作属性的值。默认为 undefined。</p>
</blockquote>
<blockquote>
<p>set: 属性的 setter 函数，如果没有 setter，则为 undefined。当属性值被修改时，会调用此函数。默认为 undefined。</p>
</blockquote>
<p>举个🌰：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> student = &#123;&#125;;
<span class="hljs-keyword">let</span> age;

<span class="hljs-built_in">Object</span>.defineProperty(student,<span class="hljs-string">'age'</span>,&#123;
  <span class="hljs-attr">get</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'读取age'</span>);
    <span class="hljs-keyword">return</span> age;
  &#125;,
  <span class="hljs-attr">set</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'设置age'</span>);
    age = val;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当对age进行设置和读值时：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23515a73d6dc4553a54cacbe533fc5e1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>也就是说，有了getter和setter，当某个属性被读取和设置时，我们可以进行拦截并做一些事情（比如重新渲染页面）。</p>
<p>如果我们想让对象的所有属性都具有响应式，就需要对全部属性进行遍历，实现getter和setter:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">convert</span> (<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-built_in">Object</span>.keys(obj).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
    <span class="hljs-keyword">let</span> internalValue = obj[key]
    <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
      get () &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`读取"<span class="hljs-subst">$&#123;key&#125;</span>": <span class="hljs-subst">$&#123;internalValue&#125;</span>`</span>)
        <span class="hljs-keyword">return</span> internalValue
      &#125;,
      set (newValue) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`设置"<span class="hljs-subst">$&#123;key&#125;</span>"为: <span class="hljs-subst">$&#123;newValue&#125;</span>`</span>)
        internalValue = newValue
      &#125;
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再进一步，如果对象的某个属性的值是一个数组或者对象，那么就还需要进行深度的遍历。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">convert</span>(<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-built_in">Object</span>.keys(obj).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> internalValue = obj[key]
      <span class="hljs-comment">//Object.defineProperty()...</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> internalValue === <span class="hljs-string">"object"</span>) &#123;
        convert(internalValue);
      &#125;
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是通过defineProperty实现响应式的主要原理。这种方法存在一个不足之处就是对于对象新增加的属性，仍然不具备响应式的特定。</p>
<h3 data-id="heading-1">Proxy实现</h3>
<p>Vue3使用Proxy来实现响应式。先来看看MDN上的定义：</p>
<blockquote>
<p>Proxy 对象用于创建一个对象的代理，从而实现基本操作的拦截和自定义（如属性查找、赋值、枚举、函数调用等）。</p>
</blockquote>
<p>语法：</p>
<blockquote>
<p>const p = new Proxy(target, handler)</p>
</blockquote>
<p>1.第一个参数target:要包装的目标对象；
2.第二个参数handle:接收一个对象，内部定义了操作目标对象时的方法；</p>
<p>通过给对象设置代理，我们可以拦截对象属性的取值/赋值操作。</p>
<p>举个🌰：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> student = &#123;
    <span class="hljs-attr">age</span>: <span class="hljs-number">23</span>,
  &#125;;
  <span class="hljs-keyword">const</span> handler = &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, prop</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"读值："</span>, prop);
      <span class="hljs-keyword">return</span> target[prop];
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, value</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"设置值"</span>, key, value);
      target[key] = value;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;,
  &#125;;
  <span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(student, handler);
  <span class="hljs-built_in">console</span>.log(proxy.age);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0883845b0154420af15d66525794284~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">总结</h3>
<p>通可见，虽然Vue3使用了ES6的新特性，但是基本思路还是跟Vue2一样的：通过拦截属性的取赋值进行数据的追踪与监听，从而实现数据变化触发页面的重新渲染。</p></div>  
</div>
            