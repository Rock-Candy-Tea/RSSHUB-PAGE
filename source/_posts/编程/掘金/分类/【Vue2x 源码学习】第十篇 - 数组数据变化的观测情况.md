
---
title: '【Vue2.x 源码学习】第十篇 - 数组数据变化的观测情况'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f9511786b574f279be8a7d8cc9953b9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 06:32:14 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f9511786b574f279be8a7d8cc9953b9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与更文挑战的第10天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">一，前言</h2>
<p>上篇，主要介绍了对象数据变化的观测情况，涉及以下几个点：</p>
<p>实现了对象老属性值变更为对象、数组时的深层观测处理；</p>
<p>结合实现原理，说明了对象新增属性不能被观测的原因，及如何实现数据观测；</p>
<p>本篇，数组数据变化的观测情况（数组中，新增对象、数组、普通值的情况；）</p>
<hr>
<h2 data-id="heading-1">二，数组中，新增对象、数组、普通值的观测问题</h2>
<h3 data-id="heading-2">1，问题分析</h3>
<p>向数组 arr 中新增对象、数组、普通值，会触发数据更新吗？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">arr</span>: [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"Brave"</span> &#125;, <span class="hljs-number">100</span>] &#125;
  &#125;
&#125;);

vm.arr.push(&#123;<span class="hljs-attr">a</span>:<span class="hljs-number">100</span>&#125;);
vm.arr[<span class="hljs-number">2</span>].a = <span class="hljs-number">200</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>截止至当前版本，针对数组类型的处理：</p>
<ul>
<li>
<p>重写了数组链上的方法，能够对引起原数组变化的 7 个原型方法进行劫持；</p>
</li>
<li>
<p>对数组中的每一项递归调用 observe 进行处理，使数组类型实现递归观测；</p>
<p>由于 observe 仅处理对象类型，所以数组中的普通值不会被观测；</p>
</li>
</ul>
<p>虽然已经实现了数组的数据劫持，但尚未实现数据劫持后的具体逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/Observer/array.js</span>

<span class="hljs-keyword">let</span> oldArrayPrototype = <span class="hljs-built_in">Array</span>.prototype;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> arrayMethods = <span class="hljs-built_in">Object</span>.create(oldArrayPrototype);

<span class="hljs-keyword">let</span> methods = [
  <span class="hljs-string">'push'</span>,
  <span class="hljs-string">'pop'</span>,
  <span class="hljs-string">'shift'</span>,
  <span class="hljs-string">'unshift'</span>,
  <span class="hljs-string">'reverse'</span>,
  <span class="hljs-string">'sort'</span>,
  <span class="hljs-string">'splice'</span>
]

methods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123;
  arrayMethods[method] = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'数组的方法进行重写操作 method = '</span> + method)
    <span class="hljs-comment">// 劫持到数组变化后，尚未实现处理逻辑</span>
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，向数组中添加内容，是能够触发数据劫持的，但还没有实现劫持后的具体逻辑</p>
<p>在 Vue2.x 中，向数组中新增对象，及修改新增对象的属性，都是可以触发更新的；</p>
<h3 data-id="heading-3">2，思路分析</h3>
<p>重写 push 方法逻辑：</p>
<p>由于 7 个方法的入参数量不一致，例如 push 可以传入多个参数</p>
<h3 data-id="heading-4">3，代码实现</h3>
<p>当 push 的参数为对象类型时，需要再次进行观测</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/observe/array.js</span>

methods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123;
  <span class="hljs-comment">// 当前的外部调用：arr.push</span>
  arrayMethods[method] = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'数组的方法进行重写操作 method = '</span> + method)
    <span class="hljs-comment">// AOP:before 原生方法扩展... </span>
    <span class="hljs-comment">// 调用数组原生方法逻辑（绑定到当前调用上下文）</span>
    oldArrayPrototype[method].call(<span class="hljs-built_in">this</span>, ...args)
    <span class="hljs-comment">// AOP::after 原生方法扩展...</span>

    <span class="hljs-comment">// 数组新增的属性如果是属性，要继续观测</span>
    <span class="hljs-comment">// 哪些方法有增加数组的功能: splice push unshift</span>
    <span class="hljs-keyword">let</span> inserted = [];
    <span class="hljs-keyword">switch</span> (method) &#123;
      <span class="hljs-comment">// arr.splice(0,0,100) 如果splice方法用于增加,一定有第三个参数,从第三个开始都是添加的内容</span>
      <span class="hljs-keyword">case</span> <span class="hljs-string">'splice'</span>:  <span class="hljs-comment">// 修改 删除 添加</span>
        inserted = args.slice(<span class="hljs-number">2</span>); <span class="hljs-comment">// splice方法从第三个参数起是新增数据</span>
      <span class="hljs-keyword">case</span> <span class="hljs-string">'push'</span>:    <span class="hljs-comment">// 向前增加</span>
      <span class="hljs-keyword">case</span> <span class="hljs-string">'unshift'</span>: <span class="hljs-comment">// 向后增加</span>
        inserted = args <span class="hljs-comment">// push、unshift的参数就是新增</span>
        <span class="hljs-keyword">break</span>;
    &#125;
    <span class="hljs-comment">// 遍历inserted数组,看一下它是否需要进行劫持</span>
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 push 的参数为对象类型时，需继续对其进行观测；</p>
<h3 data-id="heading-5">问题 1</h3>
<p>数组深层劫持的 observeArray 方法，在 Observer 类中</p>
<p>由于没有导出，在 src/observe/array.js 的 methods.forEach 中是访问不到的</p>
<p>Observer 类中也拿不到 vm，</p>
<p>所以为当前 this 添加自定义属性进行关联：value.<strong>ob</strong> = this;</p>
<p>value：为数组或对象添加自定义属性__ob__ = this，</p>
<p>this：为当前 Observer 类的实例，实例上就有 observeArray 方法；</p>
<p>如此，便可在src/observe/array.js 的 methods.forEach 中，调用到 observeArray 方法实现数组的深层劫持；</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/observe/index.js</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
  
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-comment">// value：为数组或对象添加自定义属性__ob__ = this，</span>
    <span class="hljs-comment">// this：为当前 Observer 类的实例，实例上就有 observeArray 方法；</span>
    value.__ob__ = <span class="hljs-built_in">this</span>;

    <span class="hljs-keyword">if</span> (isArray(value)) &#123;
      value.__proto__ = arrayMethods;
      <span class="hljs-built_in">this</span>.observeArray(value);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.walk(value);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加了__ob__后的数组，调用了 push 方法，所以能够通过__ob__属性获取到 ob</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/observe/array.js</span>

methods.forEach(<span class="hljs-function"><span class="hljs-params">method</span> =></span> &#123;
  arrayMethods[method] = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) </span>&#123;
    oldArrayPrototype[method].call(<span class="hljs-built_in">this</span>, ...args)
    <span class="hljs-keyword">let</span> inserted = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">let</span> ob = <span class="hljs-built_in">this</span>.__ob__;<span class="hljs-comment">// 通过 __ob__ 属性获取到 ob</span>
    <span class="hljs-keyword">switch</span> (method) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'splice'</span>: 
        inserted = args.slice(<span class="hljs-number">2</span>);
      <span class="hljs-keyword">case</span> <span class="hljs-string">'push'</span>:  
      <span class="hljs-keyword">case</span> <span class="hljs-string">'unshift'</span>:
        inserted = args 
        <span class="hljs-keyword">break</span>;
    &#125;
    
    <span class="hljs-comment">// observeArray：内部遍历inserted数组,调用observe方法，是对象就new Observer，继续深层观测</span>
    <span class="hljs-keyword">if</span>(inserted)ob.observeArray(inserted);<span class="hljs-comment">// inserted 有值就是数组</span>
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，当向数组 push 对象或数组时，会继续走 observeArray 方法，使对象或数组成为响应式</p>
<h3 data-id="heading-6">问题 2</h3>
<p>运行会导致死循环</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f9511786b574f279be8a7d8cc9953b9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/observe/index.js</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span> &#123;
    value.__ob__ = <span class="hljs-built_in">this</span>;

    <span class="hljs-keyword">if</span> (isArray(value)) &#123;
      value.__proto__ = arrayMethods;
      <span class="hljs-built_in">this</span>.observeArray(value);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.walk(value);
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
      defineReactive(data, key, data[key]);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Observer 类中，由于 value.<strong>ob</strong> = this; 这段代码</p>
<p>value 如果是对象，会走到 this.walk(value); 方法，继续循环对象的属性，</p>
<p>这时，属性__ob__会被循环出来，而__ob__又是一个对象，且在这个对象上还有__ob__</p>
<p>所以，在 walk 循环中对属性__ob__做 defineProperty 后，它的值还是一个对象，就无限递归造成了死循环</p>
<p>value 是对象就会进入 walk 方法，循环 value 对象中的所有属性，</p>
<p>其中__ob__属性将被循环出来，而 <strong>ob</strong> 就是当前实例，实际也是一个对象，会被继续观测，造成死循环</p>
<p>所以，这段代码不能这么写，即__ob__不能被遍历，否则遍历出来后就会被defineProperty，造成死循环；</p>
<p>冻结：属性冻结后只是不能被修改了，但还是能被遍历出来的</p>
<p>需要使用 defineProperty 定义__ob__ 属性，并将 <strong>ob</strong> 属性配置为不可被枚举</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/observe/index.js</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-comment">// value.__ob__ = this;// 可被遍历枚举，会造成死循环</span>
    <span class="hljs-comment">// 定义__ob__ 属性为不可被枚举，防止对象在进入walk都继续defineProperty，造成死循环</span>
    <span class="hljs-built_in">Object</span>.defineProperty(value, <span class="hljs-string">'__ob__'</span>, &#123;
      <span class="hljs-attr">value</span>:<span class="hljs-built_in">this</span>,
      <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">false</span>  <span class="hljs-comment">// 不可被枚举</span>
    &#125;);
    
    <span class="hljs-keyword">if</span> (isArray(value)) &#123;
      value.__proto__ = arrayMethods;
      <span class="hljs-built_in">this</span>.observeArray(value);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.walk(value); 
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再执行，问题解决：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56b8499d707940bf801d4cb567baf65b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-7">三，结尾</h2>
<p>本篇，主要介绍了数组数据变化的观测情况：</p>
<ul>
<li>实现了数组数据变化被劫持后，已重写原型方法的具体逻辑；</li>
<li>数组各种数据变化时的观测情况分析；</li>
</ul>
<p>至此，数据劫持就全部完成了</p>
<p>下一篇，数据渲染的流程</p></div>  
</div>
            