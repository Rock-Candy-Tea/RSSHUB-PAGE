
---
title: '《javascript高级程序设计》学习笔记 _ 9.1.代理基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8828'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 22:27:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=8828'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>关注<a href="https://github.com/simon9124/my_demos" target="_blank" rel="nofollow noopener noreferrer">前端小讴</a>，阅读更多原创技术文章</strong></p>
</blockquote>
<h1 data-id="heading-0">代理基础</h1>
<ul>
<li>ES6 为的代理和反射为开发者提供<strong>拦截</strong>并向基本操作<strong>嵌入额外行为</strong>的能力</li>
<li>代理是目标对象的<strong>抽象</strong>，其可以用作目标对象的<strong>替身</strong>，但<strong>完全独立</strong>于目标对象</li>
<li><strong>目标对象</strong>既可<strong>直接被操作</strong>，也可<strong>通过代理来操作</strong>，直接操作会绕过代理施予的行为</li>
</ul>
<p><a href="https://github.com/simon9124/my_demos/blob/master/javascript%E9%AB%98%E7%BA%A7%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%EF%BC%88%E7%AC%AC%E5%9B%9B%E7%89%88%EF%BC%89/%E7%AC%AC9%E7%AB%A0%20%E4%BB%A3%E7%90%86%E4%B8%8E%E5%8F%8D%E5%B0%84/9.1.%E4%BB%A3%E7%90%86%E5%9F%BA%E7%A1%80.js" target="_blank" rel="nofollow noopener noreferrer">相关代码 →</a></p>
<h2 data-id="heading-1">创建空代理</h2>
<ul>
<li>使用<code>Proxy</code>构造函数创建代理，接收<strong>目标对象</strong>和<strong>处理程序对象</strong>两个参数（缺一不可）</li>
<li>空代理是<strong>最简单</strong>的代理，可用空对象作为<strong>处理程序对象</strong>，空代理对象仅作为一个抽象的目标对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target = &#123;
  <span class="hljs-comment">// 目标对象</span>
  <span class="hljs-attr">id</span>: <span class="hljs-string">'target'</span>,
&#125;
<span class="hljs-keyword">const</span> handler = &#123;&#125; <span class="hljs-comment">// 处理程序对象（空对象）</span>
<span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler) <span class="hljs-comment">// 创建空代理</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>（默认情况下）<strong>空代理对象</strong>上执行的<strong>所有操作</strong>都会<strong>应用到目标对象</strong>，反之亦然</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(target.id) <span class="hljs-comment">// 'target'</span>
<span class="hljs-built_in">console</span>.log(proxy.id) <span class="hljs-comment">// 'target'</span>

target.id = <span class="hljs-string">'foo'</span> <span class="hljs-comment">// 目标对象属性重新赋值</span>
<span class="hljs-built_in">console</span>.log(target.id) <span class="hljs-comment">// 'foo'</span>
<span class="hljs-built_in">console</span>.log(proxy.id) <span class="hljs-comment">// 'foo'，会反映到代理上</span>

proxy.id = <span class="hljs-string">'bar'</span> <span class="hljs-comment">// 代理属性重新赋值</span>
<span class="hljs-built_in">console</span>.log(target.id) <span class="hljs-comment">// 'bar'，会反映到目标对象上</span>
<span class="hljs-built_in">console</span>.log(proxy.id) <span class="hljs-comment">// 'bar'</span>

<span class="hljs-built_in">console</span>.log(target.hasOwnProperty(<span class="hljs-string">'id'</span>)) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(proxy.hasOwnProperty(<span class="hljs-string">'id'</span>)) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>Proxy</code>构造函数没有<code>prototype</code>属性，也不能使用<code>instanceof</code>操作符检测</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Proxy</span>) <span class="hljs-comment">// [Function: Proxy]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Proxy</span>.prototype) <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(proxy <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Proxy</span>) <span class="hljs-comment">// TypeError: Function has non-object prototype 'undefined' in instanceof check</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用严格相等<code>===</code>用以<strong>区分代理和目标</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(target === proxy) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">定义捕获器</h2>
<ul>
<li>使用代理的主要目的是可以<strong>定义捕获器</strong>，即基本操作的<strong>拦截器</strong></li>
<li>每个捕获器<strong>对应一种</strong>基本操作，可以直接或间接在代理上调用，调用操作时会<strong>先调用捕获器函数，再将操作传播到目标对象</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target2 = &#123;
  <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>,
&#125;
<span class="hljs-keyword">const</span> handler2 = &#123;
  <span class="hljs-comment">// 定义get()捕获器函数，以方法名为键</span>
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'handler override'</span>
  &#125;,
&#125;
<span class="hljs-keyword">const</span> proxy2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target2, handler2)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>get()</code>函数可以通过<strong>多种形式触发</strong>并被捕获器拦截到：<code>proxy[property]</code>、<code>proxy.property</code>和<code>Object.create(proxy)[property]</code></li>
<li>只有<strong>代理对象</strong>上执行操作才会<strong>触发捕获器</strong>，目标对象上不会</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(proxy2.foo) <span class="hljs-comment">// 'handler override'，代理对象上操作</span>
<span class="hljs-built_in">console</span>.log(proxy2[<span class="hljs-string">'foo'</span>]) <span class="hljs-comment">// 'handler override'，代理对象上操作</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.create(proxy2).foo) <span class="hljs-comment">// 'handler override'，代理对象上操作</span>

<span class="hljs-built_in">console</span>.log(target2.foo) <span class="hljs-comment">// 'bar'，目标对象上操作</span>
<span class="hljs-built_in">console</span>.log(target2[<span class="hljs-string">'foo'</span>]) <span class="hljs-comment">// 'bar'，目标对象上操作</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.create(target2).foo) <span class="hljs-comment">// 'bar'，目标对象上操作</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">捕获器参数和反射 API</h2>
<p><code>get()</code>捕获器接收 3 个参数：目标对象、要查询的属性、代理对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target3 = &#123;
  <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>,
&#125;
<span class="hljs-keyword">const</span> handler3 = &#123;
  <span class="hljs-comment">// get()捕获器接收3个参数：目标对象、要查询的属性、代理对象</span>
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">tar, pro, rec</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(tar === target3)
    <span class="hljs-built_in">console</span>.log(pro)
    <span class="hljs-built_in">console</span>.log(rec === handler3)
  &#125;,
&#125;
<span class="hljs-keyword">const</span> proxy3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target3, handler3)
proxy3.foo
<span class="hljs-comment">/* 
  true
  'foo'
  false
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>捕获器利用这些参数<strong>重建</strong>被捕获方法的<strong>原始行为</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> handler4 = &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">tar, pro, rec</span>)</span> &#123;
    <span class="hljs-keyword">return</span> tar[pro] <span class="hljs-comment">// target3['foo']</span>
  &#125;,
&#125;
<span class="hljs-keyword">const</span> proxy4 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target3, handler4)
<span class="hljs-built_in">console</span>.log(proxy4.foo) <span class="hljs-comment">// 'bar'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>处理对象的<strong>所有捕获器方法</strong>都有对应的<strong>反射 API 方法</strong>（<strong>同名</strong>且<strong>行为相同</strong>），方法存在于全局对象<code>Reflect</code>上</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> handler5 = &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(...arguments) <span class="hljs-comment">// 用arguments解耦</span>
  &#125;,
  <span class="hljs-comment">// get: Reflect.get, // 更简洁的写法</span>
&#125;
<span class="hljs-keyword">const</span> proxy5 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target3, handler5)
<span class="hljs-built_in">console</span>.log(proxy5.foo) <span class="hljs-comment">// 'bar'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建一个可以<strong>捕获所有方法</strong>，并将<strong>每个方法</strong>都转发给反射 API 的<strong>空代理</strong>，可不定义处理程序对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> proxy6 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target3, <span class="hljs-built_in">Reflect</span>)
<span class="hljs-built_in">console</span>.log(proxy6.foo) <span class="hljs-comment">// 'bar'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>利用反射 API，可用<strong>最少的代码</strong>修改捕获的方法</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target4 = &#123;
  <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>,
  <span class="hljs-attr">baz</span>: <span class="hljs-string">'qux'</span>,
&#125;
<span class="hljs-keyword">const</span> handler6 = &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">tar, pro, rec</span>)</span> &#123;
    <span class="hljs-keyword">let</span> dec = <span class="hljs-string">''</span>
    pro === <span class="hljs-string">'foo'</span> && (dec = <span class="hljs-string">'!!!'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(...arguments) + dec
  &#125;,
&#125;
<span class="hljs-keyword">const</span> proxy7 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target4, handler6)
<span class="hljs-built_in">console</span>.log(proxy7.foo) <span class="hljs-comment">// 'bar!!!'</span>
<span class="hljs-built_in">console</span>.log(proxy7.baz) <span class="hljs-comment">// 'qux'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">捕获器不变式</h2>
<ul>
<li>捕获处理程序的行为必须遵循<strong>捕获器不变式</strong></li>
<li>如：目标对象有一个<strong>不可配置</strong>且<strong>不可重写</strong>的属性，捕获器修改返回值会报错</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target5 = &#123;&#125;
<span class="hljs-built_in">Object</span>.defineProperty(target5, <span class="hljs-string">'foo'</span>, &#123;
  <span class="hljs-attr">configurable</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 不可配置</span>
  <span class="hljs-attr">writable</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 不可重写</span>
  <span class="hljs-attr">value</span>: <span class="hljs-string">'bar'</span>,
&#125;)
<span class="hljs-keyword">const</span> handler7 = &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'qux'</span>
  &#125;,
&#125;
<span class="hljs-keyword">const</span> proxy8 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target5, handler7)
<span class="hljs-built_in">console</span>.log(proxy8.foo) <span class="hljs-comment">// TypeError: 'get' on proxy: property 'foo' is a read-only and non-configurable data property on the proxy target but the proxy did not return its actual value (expected 'bar' but got 'qux')</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">可撤销代理</h2>
<ul>
<li><code>new Proxy()</code>创建的代理<strong>不可撤销</strong>，会在代理对象生命周期内一直存在</li>
<li><code>Proxy.revocable()</code>方法可以用来创建一个<strong>可撤销</strong>的代理对象
<ul>
<li>接收<strong>目标对象</strong>和<strong>处理对象</strong>2 个参数</li>
<li>返回结构为<code>&#123;"proxy":proxyObj,"revoke":revokeFun&#125;</code>的对象</li>
<li><code>proxy</code>为代理对象；<code>revoke</code>为撤销方法，调用时不需参数</li>
<li>撤销函数<code>revoke()</code>幂等，调用多次结果相同</li>
<li>撤销操作<strong>不可逆</strong>，撤销后再次调用代理会报错</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target6 = &#123;
  <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>,
&#125;
<span class="hljs-keyword">const</span> handler8 = &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'intercepted'</span>
  &#125;,
&#125;
<span class="hljs-keyword">const</span> revocable = <span class="hljs-built_in">Proxy</span>.revocable(target6, handler8)
<span class="hljs-keyword">const</span> proxy9 = revocable.proxy <span class="hljs-comment">// 创建可撤销代理</span>
<span class="hljs-built_in">console</span>.log(proxy9.foo) <span class="hljs-comment">// 'intercepted'</span>

revocable.revoke() <span class="hljs-comment">// 撤销代理</span>
revocable.revoke() <span class="hljs-comment">// 撤销代理，调用多次结果相同</span>
revocable.revoke() <span class="hljs-comment">// 撤销代理，调用多次结果相同</span>
<span class="hljs-comment">// console.log(proxy9.foo) // TypeError: Cannot perform 'get' on a proxy that has been revoked</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">实用反射 API</h2>
<h3 data-id="heading-7">反射 API 与对象 API</h3>
<ul>
<li>反射 API 不限于捕获处理程序</li>
<li>大多数反射 API 在 <code>Object</code> 类型上有对应的方法：
<ul>
<li><code>Object</code>上的方法适用于<strong>通用程序</strong>，反射方法适用于<strong>细粒度的对象控制与操作</strong></li>
</ul>
</li>
</ul>
<h3 data-id="heading-8">状态标记</h3>
<ul>
<li>以下反射方法提供<strong>状态标记</strong>，返回<strong>布尔值</strong>表示操作是否成功
<ul>
<li><code>Reflect.defineProperty()</code>、<code>Reflect.preventExtensions()</code>、<code>Reflect.setPrototypeOf()</code>、<code>Reflect.set()</code>、<code>Reflect.deleteProperty()</code></li>
<li>（参数格式正确）<strong>操作失败</strong>时，不会抛出错误，而是返回<code>false</code></li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> o = &#123;&#125;
<span class="hljs-built_in">Object</span>.defineProperty(o, <span class="hljs-string">'foo'</span>, &#123;
  <span class="hljs-attr">writable</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 不可重写</span>
&#125;)

<span class="hljs-built_in">Object</span>.defineProperty(o, <span class="hljs-string">'foo'</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'bar'</span> &#125;) <span class="hljs-comment">// TypeError: Cannot redefine property: foo，Object.defineProperty()定义不成功会抛出错误</span>
<span class="hljs-built_in">Reflect</span>.defineProperty(o, <span class="hljs-string">'foo'</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'bar'</span> &#125;) <span class="hljs-comment">// Reflect.defineProperty()定义不成功不会抛出错误</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Reflect</span>.defineProperty(o, <span class="hljs-string">'foo'</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'bar'</span> &#125;)) <span class="hljs-comment">// false，Reflect.defineProperty()返回“状态标记”的布尔值</span>

<span class="hljs-comment">// 重构后的代码</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">Reflect</span>.defineProperty(o, <span class="hljs-string">'foo'</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'bar'</span> &#125;)) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'success'</span>)
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'failure'</span>) <span class="hljs-comment">// 'failure'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">用一等函数替代操作符</h3>
<ul>
<li>以下反射方法提供<strong>只有通过操作符才能完成的操作</strong>
<ul>
<li><code>Reflect.get()</code>：可以替代<strong>对象属性访问</strong>操作符</li>
<li><code>Reflect.set()</code>：可以替代赋值操作符<code>=</code></li>
<li><code>Reflect.has()</code>：可以替代<code>in</code>操作符或<code>with()</code></li>
<li><code>Reflect.deleteProperty()</code>：可以替代<code>delete</code>操作符</li>
<li><code>Reflect.construct()</code>：可以替代<code>new</code>操作符</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> o2 = &#123;
  <span class="hljs-attr">foo</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">bar</span>: <span class="hljs-number">2</span>,
  <span class="hljs-keyword">get</span> <span class="hljs-title">baz</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.foo + <span class="hljs-built_in">this</span>.bar
  &#125;,
&#125;
<span class="hljs-built_in">Reflect</span>.get(o2, <span class="hljs-string">'foo'</span>) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">Reflect</span>.set(o2, <span class="hljs-string">'foo'</span>, <span class="hljs-number">3</span>)
<span class="hljs-built_in">console</span>.log(o2.foo) <span class="hljs-comment">// 3</span>
<span class="hljs-built_in">Reflect</span>.has(o2, <span class="hljs-string">'foo'</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Reflect</span>.deleteProperty(o2, <span class="hljs-string">'bar'</span>)
<span class="hljs-built_in">console</span>.log(o2.bar) <span class="hljs-comment">// undefined</span>
<span class="hljs-keyword">const</span> arr = <span class="hljs-built_in">Reflect</span>.construct(<span class="hljs-built_in">Array</span>, [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>])
<span class="hljs-built_in">console</span>.log(arr) <span class="hljs-comment">// [ 1, 2, 3 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">安全地应用函数</h3>
<ul>
<li>对函数原型对象<code>Function.prototype</code>的<code>apply</code>方法利用<code>call</code>进行绑定时，<code>Reflect.apply()</code>可以使代码更加简洁易懂</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> f1 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>] + <span class="hljs-built_in">this</span>.mark)
&#125;
<span class="hljs-keyword">const</span> o3 = &#123;
  <span class="hljs-attr">mark</span>: <span class="hljs-number">95</span>,
&#125;
f1.apply(o3, [<span class="hljs-number">15</span>]) <span class="hljs-comment">// 110，将f1的this绑定到o3</span>
<span class="hljs-built_in">Function</span>.prototype.apply.call(f1, o3, [<span class="hljs-number">15</span>]) <span class="hljs-comment">// 110，函数的原型对象的apply方法，利用call进行绑定</span>
<span class="hljs-built_in">Reflect</span>.apply(f1, o3, [<span class="hljs-number">15</span>]) <span class="hljs-comment">// 110，通过指定的参数列表发起对目标函数的调用，三个参数（目标函数、绑定的this对象、实参列表）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://cloud.tencent.com/developer/chapter/13618" target="_blank" rel="nofollow noopener noreferrer">有关 Reflect 对象的详细文档 →</a></p>
<h2 data-id="heading-11">代理另一个代理</h2>
<ul>
<li>创建一个代理，通过它<strong>代理另一个代理</strong>，从而在一个目标对象上<strong>构建多层拦截网</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target7 = &#123;
  <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>,
&#125;
<span class="hljs-keyword">const</span> firstProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target7, &#123;
  <span class="hljs-comment">// 第一层代理</span>
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'first proxy'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(...arguments)
  &#125;,
&#125;)
<span class="hljs-keyword">const</span> secondProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(firstProxy, &#123;
  <span class="hljs-comment">// 第二层代理</span>
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'second proxy'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(...arguments)
  &#125;,
&#125;)
<span class="hljs-built_in">console</span>.log(secondProxy.foo)
<span class="hljs-comment">/* 
  'second proxy'
  'first proxy'
  'bar'
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">代理的问题与不足</h2>
<h3 data-id="heading-13">代理中的 this</h3>
<ul>
<li>代理中的<code>this</code>值是潜在的问题来源，例如方法中的<code>this</code>通常指向调用该方法的对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target8 = &#123;
  <span class="hljs-function"><span class="hljs-title">thisValEqualProxy</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span> === proxy10
    <span class="hljs-comment">/* 
      this指向：
      在实例中，指向实例本身
      在代理中，指向代理对象
    */</span>
  &#125;,
&#125;
<span class="hljs-keyword">const</span> proxy10 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target8, &#123;&#125;)
<span class="hljs-built_in">console</span>.log(target8.thisValEqualProxy()) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(proxy10.thisValEqualProxy()) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当<strong>目标对象依赖于对象标识</strong>时，<code>this</code>的指向会产生问题</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> wm = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">User</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">userId</span>)</span> &#123;
    wm.set(<span class="hljs-built_in">this</span>, userId) <span class="hljs-comment">// 使用目标对象作为WeakMap的键</span>
    <span class="hljs-comment">/* 
      this的指向：目标对象
    */</span>
  &#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">id</span>() &#123;
    <span class="hljs-keyword">return</span> wm.get(<span class="hljs-built_in">this</span>)
    <span class="hljs-comment">/* 
      this的指向：
      在实例中，指向实例本身 User &#123;&#125;
      在代理中，指向代理对象
    */</span>
  &#125;
&#125;

<span class="hljs-keyword">const</span> user = <span class="hljs-keyword">new</span> User(<span class="hljs-number">123</span>)
<span class="hljs-built_in">console</span>.log(wm) <span class="hljs-comment">// WeakMap &#123;User => 123&#125;</span>
<span class="hljs-built_in">console</span>.log(user.id) <span class="hljs-comment">// 123</span>

<span class="hljs-keyword">const</span> userInstanceProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(user, &#123;&#125;) <span class="hljs-comment">// 代理user实例，User类constructor中的this指向User类实例</span>
<span class="hljs-built_in">console</span>.log(wm) <span class="hljs-comment">// WeakMap &#123;User => 123&#125;，弱键未发生变化</span>
<span class="hljs-built_in">console</span>.log(userInstanceProxy.id) <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>将<strong>代理实例</strong>改为<strong>代理类本身</strong>，再创建代理实例，解决问题</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> userClassProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(User, &#123;&#125;) <span class="hljs-comment">// 代理User类本身</span>
<span class="hljs-keyword">const</span> proxyUser = <span class="hljs-keyword">new</span> userClassProxy(<span class="hljs-number">456</span>) <span class="hljs-comment">// 创建代理实例，User类constructor中的this指向代理实例</span>
<span class="hljs-built_in">console</span>.log(wm) <span class="hljs-comment">// WeakMap &#123;User => 123, User => 456&#125;，弱键发生变化，追加了以代理作为键</span>
<span class="hljs-built_in">console</span>.log(proxyUser.id) <span class="hljs-comment">// 456</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">代理与内部槽位</h3>
<ul>
<li>有些内置类型可能会依赖代理无法控制的机制：如<code>Date</code>类型方法的执行依赖<code>this</code>值上的内部槽位<code>[[NumberDate]]</code>，而该槽位<strong>不存在</strong>于代理对象，且无法被<code>get()</code>或<code>set()</code>操作访问到</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target9 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
<span class="hljs-keyword">const</span> proxy11 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target9, &#123;&#125;)
<span class="hljs-built_in">console</span>.log(target9.getDate()) <span class="hljs-comment">// 24，当天日期</span>
<span class="hljs-built_in">console</span>.log(proxy11.getDate()) <span class="hljs-comment">// TypeError: this is not a Date object.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">总结 & 问点</h2>
<ul>
<li>代理的用处是什么？其和目标对象有怎样的关系？</li>
<li>如何创建空代理？如何区分空代理对象和目标对象？</li>
<li>什么是捕获器？其是如何被调用和触发的？get()函数可以通过哪些形式被捕获器拦截？</li>
<li>get()捕获器接收哪些参数？写一段代码，利用这些参数重写捕获方法的原始行为</li>
<li>如何创建可撤销代理？撤销后再次撤销会怎样？撤销后调用代理会怎样？</li>
<li>如何理解 Reflect 对象？其反射 API 与对象 API 有怎样的关联和异同？如何理解 Reflect.apply()方法？</li>
<li>如何通过代理，在一个目标对象上构建多层拦截网？</li>
<li>代理有哪些潜在的问题？如何解决呢？</li>
</ul></div>  
</div>
            