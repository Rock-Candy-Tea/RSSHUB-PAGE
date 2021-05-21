
---
title: 'ES6(8)Proxy（拦截器、代理器）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5e0957bb6b344aca06f0828f723d9fb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 21 May 2021 02:16:27 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5e0957bb6b344aca06f0828f723d9fb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概述:改变默认行为，对外界的访问进行过滤和改写</h2>
<blockquote>
<p><code>Proxy</code> 用于<code>修改</code>某些操作的<code>默认行为</code>，等同于在<code>语言层面</code>做出修改，所以属于一种<code>“元编程”</code>，即<code>对编程语言进行编程</code>。</p>
<p><code>Proxy</code>改变默认行为</p>
</blockquote>
<blockquote>
<p><code>Proxy </code>可以理解成，在目标对象之前<code>架设一层“拦截”</code>，外界对该对象的访问，都必须先通过这层拦截，因此提供了一种机制，可以<code>对外界的访问</code>进行<code>过滤和改写</code>。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125;, &#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target, key, receiver</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`getting <span class="hljs-subst">$&#123;key&#125;</span>!`</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(target, key, receiver);
  &#125;,
  <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target, key, value, receiver</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`setting <span class="hljs-subst">$&#123;key&#125;</span>!`</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.set(target, key, value, receiver);
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码<code>对一个空对象架设了一层拦截</code>，<code>重定义</code>了属性的<code>读取</code>（get）和<code>设置</code>（set）行为。对设置了拦截行为的对象<code>obj</code>，去读写它的属性，就会得到下面的结果。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">proxy.count = <span class="hljs-number">1</span>
<span class="hljs-comment">//  setting count!</span>
++proxy.count
<span class="hljs-comment">//  getting count!</span>
<span class="hljs-comment">//  setting count!</span>
<span class="hljs-comment">//  2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码说明，<code>Proxy 实际上重载了点运算符</code>，即用<code>自己的定义</code>覆盖了语言的<code>原始定义</code>。</p>
<h2 data-id="heading-1">语法,var proxy = new Proxy(target, handler);</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">target：参数表示所要拦截的目标对象</h3>
<h3 data-id="heading-3">handler：参数也是一个对象，用来定制拦截行为</h3>
<blockquote>
<p>要使得<code>Proxy</code>起作用，必须<code>针对Proxy实例</code>（上例是proxy对象）进行<code>操作</code>，而<code>不是针对目标对象</code>（上例是空对象）进行操作</p>
<p>如果<code>handler没有设置</code>任何拦截，那就等同于<code>直接通向原对象</code>,没有任何拦截效果，访问<code>proxy</code>就等同于访问<code>target</code>。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> target = &#123;&#125;;
<span class="hljs-keyword">var</span> handler = &#123;&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);
proxy.a = <span class="hljs-string">'b'</span>;
target.a <span class="hljs-comment">// "b"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">Proxy 对象，设置到object.proxy属性，从而可以当做object`对象的属性调用</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> object = &#123; <span class="hljs-attr">proxy</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler) &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Proxy 实例作为其他对象的原型对象</h3>
<blockquote>
<p>必须是<code>new</code>以后生成的实例，才会触发拦截</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125;, &#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">target, property</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">35</span>;
  &#125;
&#125;);

<span class="hljs-keyword">let</span> obj = <span class="hljs-built_in">Object</span>.create(proxy);
obj.time <span class="hljs-comment">// 35</span>

<span class="hljs-comment">//obj对象本身并没有time属性，所以根据原型链，会在proxy对象上读取该属性，导致被拦截。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">同一个拦截器函数，可以设置拦截多个操作</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> handler = &#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">target, name</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (name === <span class="hljs-string">'prototype'</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'Hello, '</span> + name;
  &#125;,

  <span class="hljs-attr">apply</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">target, thisBinding, args</span>) </span>&#123;
    <span class="hljs-keyword">return</span> args[<span class="hljs-number">0</span>];
  &#125;,

  <span class="hljs-attr">construct</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">target, args</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">value</span>: args[<span class="hljs-number">1</span>]&#125;;
  &#125;
&#125;;

<span class="hljs-keyword">var</span> fproxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x, y</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x + y;
&#125;, handler);

fproxy(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>) <span class="hljs-comment">// 1</span>
<span class="hljs-keyword">new</span> fproxy(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>) <span class="hljs-comment">// &#123;value: 2&#125;</span>
fproxy.prototype === <span class="hljs-built_in">Object</span>.prototype <span class="hljs-comment">// true</span>
fproxy.foo === <span class="hljs-string">"Hello, foo"</span> <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">Proxy 支持的拦截操作</h2>
<ul>
<li><code>get(target, propKey, receiver)</code>：拦截对象<code>属性的读取</code>，比如<code>proxy.foo</code>和<code>proxy['foo']</code>。</li>
<li><code>set(target, propKey, value, receiver)</code>：拦截对象<code>属性的设置</code>，比如<code>proxy.foo = v</code>或<code>proxy['foo'] = v</code>，返回一个布尔值。</li>
<li><code>has(target, propKey)</code>：拦截<code>propKey in proxy的操作</code>，返回一个布尔值。</li>
<li><code>deleteProperty(target, propKey)</code>：拦截<code>delete proxy[propKey]</code>的操作，返回一个布尔值。</li>
<li><code>ownKeys(target)</code>：拦截<code>Object.getOwnPropertyNames(proxy)、Object.getOwnPropertySymbols(proxy)、Object.keys(proxy)、for...in循环</code>，返回一个数组。该方法返回<code>目标对象</code>所有<code>自身的属性</code>的<code>属性名</code>，而Object.keys()的返回结果仅包括目标对象自身的可遍历属性。</li>
<li><code>getOwnPropertyDescriptor(target, propKey)</code>：拦截<code>Object.getOwnPropertyDescriptor(proxy, propKey)</code>，返回属性的描述对象。</li>
<li><code>defineProperty(target, propKey, propDesc)</code>：拦截<code>Object.defineProperty(proxy, propKey, propDesc）、Object.defineProperties(proxy, propDescs)</code>，返回一个布尔值。</li>
<li><code>preventExtensions(target)</code>：拦截<code>Object.preventExtensions(proxy)</code>，返回一个布尔值。</li>
<li><code>getPrototypeOf(target)</code>：拦截<code>Object.getPrototypeOf(proxy)</code>，返回一个对象。</li>
<li><code>isExtensible(target)</code>：拦截<code>Object.isExtensible(proxy)</code>，返回一个布尔值。</li>
<li><code>setPrototypeOf(target, proto)</code>：拦截<code>Object.setPrototypeOf(proxy, proto)</code>，返回一个布尔值。如果目标对象是函数，那么还有两种额外操作可以拦截。</li>
<li><code>apply(target, object, args)</code>：拦截 <code>Proxy 实例作为函数调用的操作</code>，比如<code>proxy(...args)、proxy.call(object, ...args)、proxy.apply(...)</code>。</li>
<li><code>construct(target, args)</code>：拦截 Proxy 实例<code>作为构造函数调用的操作</code>，比如<code>new proxy(...args)</code>。</li>
</ul>
<table>
<thead>
<tr>
<th>方法</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/apply" target="_blank" rel="nofollow noopener noreferrer">handler.apply()</a></td>
<td>拦截 Proxy 实例作为函数调用的操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/construct" target="_blank" rel="nofollow noopener noreferrer">handler.construct()</a></td>
<td>拦截 Proxy 实例作为构造函数调用的操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/defineProperty" target="_blank" rel="nofollow noopener noreferrer">handler.defineProperty()</a></td>
<td>拦截 Object.defineProperty() 的操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/deleteProperty" target="_blank" rel="nofollow noopener noreferrer">handler.deleteProperty()</a></td>
<td>拦截 Proxy 实例删除属性操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/get" target="_blank" rel="nofollow noopener noreferrer">handler.get()</a></td>
<td>拦截 读取属性的操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/set" target="_blank" rel="nofollow noopener noreferrer">handler.set()</a></td>
<td>拦截 属性赋值的操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/getOwnPropertyDescriptor" target="_blank" rel="nofollow noopener noreferrer">handler.getOwnPropertyDescriptor()</a></td>
<td>拦截 Object.getOwnPropertyDescriptor() 的操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/getPrototypeOf" target="_blank" rel="nofollow noopener noreferrer">handler.getPrototypeOf()</a></td>
<td>拦截 获取原型对象的操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/has" target="_blank" rel="nofollow noopener noreferrer">handler.has()</a></td>
<td>拦截 属性检索操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/isExtensible" target="_blank" rel="nofollow noopener noreferrer">handler.isExtensible()</a></td>
<td>拦截 Object.isExtensible()操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/ownKeys" target="_blank" rel="nofollow noopener noreferrer">handler.ownKeys()</a></td>
<td>拦截 Object.getOwnPropertyDescriptor() 的操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/preventExtensions" target="_blank" rel="nofollow noopener noreferrer">handler.preventExtension()</a></td>
<td>拦截 Object().preventExtension() 操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/setPrototypeOf" target="_blank" rel="nofollow noopener noreferrer">handler.setPrototypeOf()</a></td>
<td>拦截Object.setPrototypeOf()操作</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable" target="_blank" rel="nofollow noopener noreferrer">Proxy.revocable()</a></td>
<td>创建一个可取消的 Proxy 实例</td>
</tr>
</tbody>
</table>
<h3 data-id="heading-8">get(target,key,receiver)</h3>
<blockquote>
<p>拦截某个属性的读取操作</p>
</blockquote>
<h4 data-id="heading-9">依次三个参数：目标对象、被读取的属性名、proxy 实例本身</h4>
<blockquote>
<p><code>target</code>：必选、<code>目标对象</code></p>
<p><code>key</code>：必选、<code>被读取的属性名</code>，在get内部是<code>字符串</code></p>
<p><code>receiver</code>：可选、<code>proxy </code>实例本身（严格地说，是操作行为所针对的对象）</p>
<p><code>需要return</code></p>
<p>如果一个属性<code>不可配置（configurable）且不可写（writable）</code>，则 Proxy <code>不能修改该属性</code>，否则通过 <code>Proxy</code> 对象访问该属性<code>会报错</code>。</p>
</blockquote>
<h4 data-id="heading-10">需要return</h4>
<h4 data-id="heading-11">应用实例</h4>
<h5 data-id="heading-12">1、访问目标对象不存在的属性，抛出一个错误而不是返回undefined</h5>
<blockquote>
<p>如果<code>没有</code>这个拦截函数，访问不存在的属性，只会返回<code>undefined</code>。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"张三"</span>
&#125;;

<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">target, property</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (property <span class="hljs-keyword">in</span> target) &#123;
      <span class="hljs-keyword">return</span> target[property];
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">ReferenceError</span>(<span class="hljs-string">"Property \""</span> + property + <span class="hljs-string">"\" does not exist."</span>);
    &#125;
  &#125;
&#125;);

proxy.name <span class="hljs-comment">// "张三"</span>
proxy.age <span class="hljs-comment">// 抛出一个错误</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">2、get方法可以继承（定义在Prototype对象上，拦截实例通过原型链获取继承的方法的操作）</h5>
<blockquote>
<p>当拦截操作定义在<code>Prototype</code>对象上面时，读取<code>obj对象继承的属性(自身没有的属性)</code>时，拦截会生效。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> proto = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125;, &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, propertyKey, receiver</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'GET '</span> + propertyKey);
    <span class="hljs-keyword">return</span> target[propertyKey];
  &#125;
&#125;);

<span class="hljs-keyword">let</span> obj = <span class="hljs-built_in">Object</span>.create(proto);  
obj.foo <span class="hljs-comment">// "GET foo"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>拦截</code>操作定义<code>在Prototype对象上面</code>，所以如果读取obj对象继承的属性时(<code>本身没有，通过原型链查找的属性</code>)，拦截会生效。</p>
<h5 data-id="heading-14">3、使用get拦截，实现数组读取负数的索引</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createArray</span>(<span class="hljs-params">...elements</span>) </span>&#123;
  <span class="hljs-keyword">let</span> handler = &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, propKey, receiver</span>)</span> &#123;
      <span class="hljs-keyword">let</span> index = <span class="hljs-built_in">Number</span>(propKey);
      <span class="hljs-keyword">if</span> (index < <span class="hljs-number">0</span>) &#123;
        propKey = <span class="hljs-built_in">String</span>(target.length + index);
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(target, propKey, receiver);
    &#125;
  &#125;;

  <span class="hljs-keyword">let</span> target = [];
  target.push(...elements);
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);
&#125;

<span class="hljs-keyword">let</span> arr = createArray(<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>);
arr[-<span class="hljs-number">1</span>] <span class="hljs-comment">// c</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//简略版</span>
<span class="hljs-keyword">var</span> arr=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>([<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>],&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, p, receiver</span>)</span> &#123;
        <span class="hljs-keyword">if</span>(p<<span class="hljs-number">0</span>)&#123;
            <span class="hljs-keyword">var</span> n=<span class="hljs-built_in">eval</span>(target.length-<span class="hljs-number">1</span>+p);
            <span class="hljs-keyword">return</span> target[n];
        &#125;
        <span class="hljs-keyword">return</span> target[p];
    &#125;
&#125;)

<span class="hljs-built_in">console</span>.log(arr[-<span class="hljs-number">1</span>]);   <span class="hljs-comment">//3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">4、将读取属性的操作（get），转变为执行某个函数【vue3.0】有点像发布订阅</h5>
<blockquote>
<p>利用<code>Proxy get</code>拦截以后仍然返回<code>Proxy</code>实例的特性，达到了将函数名链式使用的效果</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> pipe = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-keyword">var</span> funcStack = [];
    <span class="hljs-keyword">var</span> oproxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125; , &#123;
      <span class="hljs-attr">get</span> : <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">pipeObject, fnName</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (fnName === <span class="hljs-string">'get'</span>) &#123;
        <span class="hljs-comment">//如果获取的是get 对数组funcStack中的函数一次调用</span>
          <span class="hljs-keyword">return</span> funcStack.reduce(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">val, fn</span>) </span>&#123;
            <span class="hljs-keyword">return</span> fn(val);
          &#125;,value);
        &#125;
        <span class="hljs-comment">//如果不是get  向数组funcStack中添加函数</span>
        funcStack.push(<span class="hljs-built_in">window</span>[fnName]);
        <span class="hljs-keyword">return</span> oproxy;
      &#125;
    &#125;);
    <span class="hljs-keyword">return</span> oproxy;
  &#125;
&#125;());

<span class="hljs-keyword">var</span> double = <span class="hljs-function"><span class="hljs-params">n</span> =></span> n * <span class="hljs-number">2</span>;
<span class="hljs-keyword">var</span> pow    = <span class="hljs-function"><span class="hljs-params">n</span> =></span> n * n;
<span class="hljs-keyword">var</span> reverseInt = <span class="hljs-function"><span class="hljs-params">n</span> =></span> n.toString().split(<span class="hljs-string">""</span>).reverse().join(<span class="hljs-string">""</span>) | <span class="hljs-number">0</span>;

pipe(<span class="hljs-number">3</span>).double.pow.reverseInt.get; <span class="hljs-comment">// 63</span>

<span class="hljs-comment">//有点像发布订阅</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">5、利用get拦截，实现一个生成各种 DOM 节点的通用函数dom【vue3.0】</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> dom=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125;,&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, p, receiver</span>)</span> &#123;
        <span class="hljs-comment">//(attrs=&#123;&#125;,...children)   第一个参数为attrs 剩余的都是children</span>
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">attrs=&#123;&#125;,...children</span>) </span>&#123;
            <span class="hljs-comment">//get属性名  就是要创建的 元素名称</span>
            <span class="hljs-keyword">const</span> el=<span class="hljs-built_in">document</span>.createElement(p);
            <span class="hljs-comment">//循环 attrs设置元素属性</span>
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> prop <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.keys(attrs))&#123;
                el.setAttribute(prop,attrs[prop]);
            &#125;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> child <span class="hljs-keyword">of</span> children)&#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> child === <span class="hljs-string">'string'</span>)&#123;
                    child = <span class="hljs-built_in">document</span>.createTextNode(child);
                &#125;
                el.append(child)
            &#125;
            <span class="hljs-keyword">return</span> el;
        &#125;
    &#125;
&#125;)


<span class="hljs-keyword">const</span> el = dom.div(
    &#123;&#125;,
    <span class="hljs-string">'Hello, my name is '</span>,
    dom.a(&#123;<span class="hljs-attr">href</span>: <span class="hljs-string">'//example.com'</span>&#125;, <span class="hljs-string">'Mark'</span>),
    <span class="hljs-string">'. I like:'</span>,
    dom.ul(&#123;&#125;,
        dom.li(&#123;&#125;, <span class="hljs-string">'The web'</span>),
        dom.li(&#123;&#125;, <span class="hljs-string">'Food'</span>),
        dom.li(&#123;&#125;, <span class="hljs-string">'…actually that\'s it'</span>)
    )
);

<span class="hljs-comment">//相对与div ：&#123;&#125;为 attrs ，剩余的都是子级</span>
<span class="hljs-built_in">console</span>.log(el);
<span class="hljs-built_in">document</span>.body.appendChild(el);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5e0957bb6b344aca06f0828f723d9fb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-17">第三个参数的例子，一般情况下就是 Proxy 实例</h5>
<blockquote>
<p>总是指向原始的读操作所在的那个对象，一般情况下就是 Proxy 实例。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125;, &#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">target, property, receiver</span>) </span>&#123;
    <span class="hljs-keyword">return</span> receiver;
  &#125;
&#125;);
proxy.getReceiver === proxy <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125;, &#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">target, property, receiver</span>) </span>&#123;
    <span class="hljs-keyword">return</span> receiver;
  &#125;
&#125;);

<span class="hljs-keyword">const</span> d = <span class="hljs-built_in">Object</span>.create(proxy);
d.a === d <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>d</code>对象本身<code>没有a属性</code>，所以读取<code>d.a</code>的时候，会去<code>d的原型proxy对象找</code>。这时，<code>receiver就指向d</code>，代表原始的读操作所在的那个对象。</p>
<h3 data-id="heading-18">set（obj, prop, value,receiver）</h3>
<blockquote>
<p><code>拦截</code>某个属性的<code>赋值操作</code></p>
</blockquote>
<h4 data-id="heading-19">依次四个参数：目标对象，属性名，属性值，Proxy 实例本身</h4>
<blockquote>
<p><code>target</code>：目标对象</p>
<p><code>prop</code>：属性名，在get内部是<code>字符串</code></p>
<p><code>value</code>：属性值</p>
<p><code>receiver</code>：可选，Proxy 实例本身</p>
<p>如果目标对象自身的某个属性，不可写且不可配置，那么set方法将不起作用。</p>
</blockquote>
<h4 data-id="heading-20">在赋值操作发生时进行自己想要的操作，还可以进行数据绑定，即每当对象发生变化时，会自动更新 DOM（vue3.0）</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> validator = &#123;
  <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">obj, prop, value</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (prop === <span class="hljs-string">'age'</span>) &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Number</span>.isInteger(value)) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'The age is not an integer'</span>);
      &#125;
      <span class="hljs-keyword">if</span> (value > <span class="hljs-number">200</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">RangeError</span>(<span class="hljs-string">'The age seems invalid'</span>);
      &#125;
    &#125;

    <span class="hljs-comment">// 对于满足条件的 age 属性以及其他属性，直接保存</span>
    obj[prop] = value;
  &#125;
&#125;;

<span class="hljs-keyword">let</span> person = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125;, validator);

person.age = <span class="hljs-number">100</span>;

person.age <span class="hljs-comment">// 100</span>
person.age = <span class="hljs-string">'young'</span> <span class="hljs-comment">// 报错</span>
person.age = <span class="hljs-number">300</span> <span class="hljs-comment">// 报错</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">设置一些内部属性不被外部读写（假定开头是_的为内部属性）</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> handler = &#123;
  get (target, key) &#123;
    invariant(key, <span class="hljs-string">'get'</span>);
    <span class="hljs-keyword">return</span> target[key];
  &#125;,
  set (target, key, value) &#123;
    invariant(key, <span class="hljs-string">'set'</span>);
    target[key] = value;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invariant</span> (<span class="hljs-params">key, action</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (key[<span class="hljs-number">0</span>] === <span class="hljs-string">'_'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Invalid attempt to <span class="hljs-subst">$&#123;action&#125;</span> private "<span class="hljs-subst">$&#123;key&#125;</span>" property`</span>);
  &#125;
&#125;
<span class="hljs-keyword">const</span> target = &#123;&#125;;
<span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);
proxy._prop
<span class="hljs-comment">// Error: Invalid attempt to get private "_prop" property</span>
proxy._prop = <span class="hljs-string">'c'</span>
<span class="hljs-comment">// Error: Invalid attempt to set private "_prop" property</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">第四个参数的例子</h4>
<p>set方法的第四个参数receiver，指的是原始的操作行为所在的那个对象，一般情况下是proxy实例本身，<code>跟get的第三个参数的运用相同</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> handler = &#123;
  <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">obj, prop, value, receiver</span>) </span>&#123;
    obj[prop] = receiver;
  &#125;
&#125;;
<span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125;, handler);
proxy.foo = <span class="hljs-string">'bar'</span>;
proxy.foo === proxy <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">apply(target, context, args),拦截函数的调用、call和apply操作</h3>
<h4 data-id="heading-24">依次三个形参：目标对象，上下文对象（this），参数数组</h4>
<blockquote>
<p>target：<code>目标对象</code></p>
<p>context：目标对象的<code>上下文对象</code>（<code>this</code>）</p>
<p>args：目标对象的<code>参数数组</code></p>
</blockquote>
<h4 data-id="heading-25">设置apply拦截后  函数自身内部的代码不再执行</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> handler = &#123;
  apply (target, ctx, args) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.apply(...arguments);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> fn=<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">//不执行</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>,<span class="hljs-string">'fn'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">'I am fn'</span>
&#125;

<span class="hljs-keyword">var</span> p=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(fn,&#123;
    <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">target, thisArg, argArray</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(thisArg,<span class="hljs-string">'p'</span>)   <span class="hljs-comment">//undefined 'p'</span>
        <span class="hljs-keyword">return</span> <span class="hljs-string">'I am p'</span>
    &#125;
&#125;)

<span class="hljs-built_in">console</span>.log(p());   <span class="hljs-comment">//I am p</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> twice = &#123;
  apply (target, ctx, args) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.apply(...arguments) * <span class="hljs-number">2</span>;
  &#125;
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span> (<span class="hljs-params">left, right</span>) </span>&#123;
  <span class="hljs-keyword">return</span> left + right;
&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(sum, twice);
proxy(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>) <span class="hljs-comment">// 6</span>
proxy.call(<span class="hljs-literal">null</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>) <span class="hljs-comment">// 22</span>
proxy.apply(<span class="hljs-literal">null</span>, [<span class="hljs-number">7</span>, <span class="hljs-number">8</span>]) <span class="hljs-comment">// 30</span>

<span class="hljs-comment">//直接调用Reflect.apply方法，也会被拦截。</span>

<span class="hljs-built_in">Reflect</span>.apply(proxy, <span class="hljs-literal">null</span>, [<span class="hljs-number">9</span>, <span class="hljs-number">10</span>]) <span class="hljs-comment">// 38</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">construct(target, args, newTarget)</h3>
<blockquote>
<p>用于<code>拦截new命令</code></p>
</blockquote>
<h4 data-id="heading-28">依次三个形参：目标对象，参数对象，new 后面的函数</h4>
<blockquote>
<p>target：<code>目标对象</code></p>
<p>args：构造函数的<code>参数对象</code></p>
<p>newTarget：<code>可选</code>，创造实例对象时，new命令作用的<code>构造函数</code>（new 后面的函数）</p>
</blockquote>
<h4 data-id="heading-29">construct方法返回的必须是一个对象</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> handler = &#123;
  construct (target, args, newTarget) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> target(...args);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;, &#123;
  <span class="hljs-attr">construct</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">target, args</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'called: '</span> + args.join(<span class="hljs-string">', '</span>));
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">value</span>: args[<span class="hljs-number">0</span>] * <span class="hljs-number">10</span> &#125;;
  &#125;
&#125;);

(<span class="hljs-keyword">new</span> p(<span class="hljs-number">1</span>)).value
<span class="hljs-comment">// "called: 1"</span>
<span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">has(target, key)，拦截HasProperty操作，即判断对象是否具有某个属性（in运算符）</h3>
<blockquote>
<p><code>拦截HasProperty操作</code>，即<code>判断对象是否具有某个属性时</code>，这个方法会生效。典型的操作就是<code>in运算符</code>。</p>
</blockquote>
<p>依次两个形参</p>
<blockquote>
<p>target：目标对象</p>
<p>key：需查询的属性名</p>
</blockquote>
<p>下面的例子使用has方法隐藏某些属性，不被in运算符发现。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> handler = &#123;
  has (target, key) &#123;
    <span class="hljs-keyword">if</span> (key[<span class="hljs-number">0</span>] === <span class="hljs-string">'_'</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;
    <span class="hljs-keyword">return</span> key <span class="hljs-keyword">in</span> target;
  &#125;
&#125;;
<span class="hljs-keyword">var</span> target = &#123; <span class="hljs-attr">_prop</span>: <span class="hljs-string">'foo'</span>, <span class="hljs-attr">prop</span>: <span class="hljs-string">'foo'</span> &#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);
<span class="hljs-string">'_prop'</span> <span class="hljs-keyword">in</span> proxy <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">deleteProperty(target, key)，用于拦截delete操作</h3>
<blockquote>
<p>用于拦截delete操作</p>
<p>通过<code>抛出错误</code>或者<code>返回false</code>，阻止delete命令删除。</p>
</blockquote>
<p>依次两个形参：目标对象、需查删除的属性名</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> handler = &#123;
  deleteProperty (target, key) &#123;
    invariant(key, <span class="hljs-string">'delete'</span>);
    <span class="hljs-keyword">delete</span> target[key];
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invariant</span> (<span class="hljs-params">key, action</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (key[<span class="hljs-number">0</span>] === <span class="hljs-string">'_'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Invalid attempt to <span class="hljs-subst">$&#123;action&#125;</span> private "<span class="hljs-subst">$&#123;key&#125;</span>" property`</span>);
  &#125;
&#125;

<span class="hljs-keyword">var</span> target = &#123; <span class="hljs-attr">_prop</span>: <span class="hljs-string">'foo'</span> &#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);
<span class="hljs-keyword">delete</span> proxy._prop
<span class="hljs-comment">// Error: Invalid attempt to delete private "_prop" property</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">Proxy.revocable() ，返回一个可取消的 Proxy 实例</h3>
<blockquote>
<p><code>Proxy.revocable</code>方法返回一个对象，该对象的<code>proxy</code>属性是<code>Proxy</code>实例，<code>revoke</code>属性是一个函数，可以取消<code>Proxy</code>实例。</p>
<p>当执行<code>revoke</code>函数之后，再访问<code>Proxy</code>实例，就会<code>抛出一个错误</code>。</p>
<p><code>使用场景是</code>，目标对象不允许直接访问，必须通过代理访问，一旦访问结束，就收回代理权，不允许再次访问。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> target = &#123;&#125;;
<span class="hljs-keyword">let</span> handler = &#123;&#125;;

<span class="hljs-keyword">let</span> &#123;proxy, revoke&#125; = <span class="hljs-built_in">Proxy</span>.revocable(target, handler);

proxy.foo = <span class="hljs-number">123</span>;
proxy.foo <span class="hljs-comment">// 123</span>

revoke();
proxy.foo <span class="hljs-comment">// TypeError: Revoked</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">this 问题</h2>
<h3 data-id="heading-34">Proxy不做任何拦截的情况下，也无法保证与目标对象的行为一致</h3>
<h3 data-id="heading-35">在Proxy代理的情况下，目标对象内部的this关键字会指向 Proxy 代理</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> target = &#123;
  <span class="hljs-attr">m</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span> === proxy);
  &#125;
&#125;;
<span class="hljs-keyword">const</span> handler = &#123;&#125;;

<span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);

target.m() <span class="hljs-comment">// false</span>
proxy.m()  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> _name = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    _name.set(<span class="hljs-built_in">this</span>, name);
  &#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">name</span>() &#123;
    <span class="hljs-keyword">return</span> _name.get(<span class="hljs-built_in">this</span>);
  &#125;
&#125;

<span class="hljs-keyword">const</span> jane = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'Jane'</span>);
jane.name <span class="hljs-comment">// 'Jane'</span>

<span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(jane, &#123;&#125;);
proxy.name <span class="hljs-comment">// undefined</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，目标对象<code>jane</code>的<code>name</code>属性，实际保存在外部<code>WeakMap</code>对象<code>_name</code>上面，通过<code>this</code>键区分。由于通过<code>proxy.name</code>访问时，<code>this</code>指向<code>proxy</code>，导致无法取到值，所以返回<code>undefined</code>。</p>
<h3 data-id="heading-36">原生对象的内部属性，只有通过正确的this才能拿到</h3>
<blockquote>
<p>也就是说<code>this</code>必须是对应类的实例才能拿到的内部属性</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> target = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="hljs-keyword">const</span> handler = &#123;&#125;;
<span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);

proxy.getDate();
<span class="hljs-comment">// TypeError: this is not a Date object.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-37">用bind将this绑定到原始处理对象，就可以解决这个问题</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> target = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-string">'2015-01-01'</span>);
<span class="hljs-keyword">const</span> handler = &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, prop</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (prop === <span class="hljs-string">'getDate'</span>) &#123;
      <span class="hljs-keyword">return</span> target.getDate.bind(target);
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(target, prop);
  &#125;
&#125;;
<span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);
proxy.getDate() <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            