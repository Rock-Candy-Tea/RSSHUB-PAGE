
---
title: 'JavaScript 系列之类（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1413'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 17:29:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=1413'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第17天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">二、ES6 上的类经过 Babel 编译</h2>
<h3 data-id="heading-1">2.1 编译一</h3>
<p>ES6 代码为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Babel 编译为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">"use strict"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classCallCheck</span>(<span class="hljs-params">instance, Constructor</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!(instance <span class="hljs-keyword">instanceof</span> Constructor)) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Cannot call a class as a function"</span>);
  &#125;
&#125;

<span class="hljs-keyword">var</span> Person = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
  _classCallCheck(<span class="hljs-built_in">this</span>, Person);

  <span class="hljs-built_in">this</span>.name = name;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_classCallCheck</code> 的作用是检查 Person 是否是通过 new 的方式调用，在上面，我们也说过，类必须使用 new 调用，否则会报错。</p>
<p>使用 new 来调用 Person 时，我们会构造一个新对象并把它绑定到 <code>Person()</code> 调用中的 this 上。</p>
<p>当我们使用 <code>var person = Person()</code> 的形式调用的时候，this 指向 window，所以 <code>instance instanceof Constructor</code> 就会为 false，与 ES6 的要求一致。</p>
<h3 data-id="heading-2">2.2 编译二</h3>
<p>ES6 代码为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-comment">// 实例属性</span>
  foo = <span class="hljs-string">'foo'</span>;
  
  <span class="hljs-comment">// 静态属性</span>
  <span class="hljs-keyword">static</span> bar = <span class="hljs-string">'bar'</span>;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Babel 编译为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classCallCheck</span>(<span class="hljs-params">instance, Constructor</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!(instance <span class="hljs-keyword">instanceof</span> Constructor)) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Cannot call a class as a function"</span>);
  &#125;
&#125;

<span class="hljs-keyword">var</span> Person = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
  _classCallCheck(<span class="hljs-built_in">this</span>, Person);

  <span class="hljs-built_in">this</span>.foo = <span class="hljs-string">'foo'</span>;

  <span class="hljs-built_in">this</span>.name = name;
&#125;;

Person.bar = <span class="hljs-string">'bar'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.3 编译三</h3>
<p>ES6 代码为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;

  <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'hello, I am '</span> + <span class="hljs-built_in">this</span>.name;
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">onlySayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'hello'</span>
  &#125;

  <span class="hljs-keyword">get</span> <span class="hljs-title">name</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'kevin'</span>;
  &#125;

  <span class="hljs-keyword">set</span> <span class="hljs-title">name</span>(<span class="hljs-params">newName</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'new name 为：'</span> + newName)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应到 ES5 的代码应该是：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
&#125;

Person.prototype =  &#123;
  <span class="hljs-attr">sayHello</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'hello, I am '</span> + <span class="hljs-built_in">this</span>.name;
  &#125;,
  <span class="hljs-keyword">get</span> <span class="hljs-title">name</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'kevin'</span>;
  &#125;,
  <span class="hljs-keyword">set</span> <span class="hljs-title">name</span>(<span class="hljs-params">newName</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'new name 为：'</span> + newName)
  &#125;
&#125;

Person.onlySayHello = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'hello'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Babel 编译后为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>;

<span class="hljs-keyword">var</span> _createClass = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineProperties</span>(<span class="hljs-params">target, props</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < props.length; i++) &#123;
      <span class="hljs-keyword">var</span> descriptor = props[i];
      descriptor.enumerable = descriptor.enumerable || <span class="hljs-literal">false</span>;
      descriptor.configurable = <span class="hljs-literal">true</span>;
      <span class="hljs-keyword">if</span> (<span class="hljs-string">"value"</span> <span class="hljs-keyword">in</span> descriptor) descriptor.writable = <span class="hljs-literal">true</span>;
      <span class="hljs-built_in">Object</span>.defineProperty(target, descriptor.key, descriptor);
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">Constructor, protoProps, staticProps</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (protoProps) defineProperties(Constructor.prototype, protoProps);
    <span class="hljs-keyword">if</span> (staticProps) defineProperties(Constructor, staticProps);
    <span class="hljs-keyword">return</span> Constructor;
  &#125;;
&#125;();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classCallCheck</span>(<span class="hljs-params">instance, Constructor</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!(instance <span class="hljs-keyword">instanceof</span> Constructor)) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Cannot call a class as a function"</span>);
  &#125;
&#125;

<span class="hljs-keyword">var</span> Person = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
    _classCallCheck(<span class="hljs-built_in">this</span>, Person);

    <span class="hljs-built_in">this</span>.name = name;
  &#125;

  _createClass(Person, [&#123;
    <span class="hljs-attr">key</span>: <span class="hljs-string">'sayHello'</span>,
    <span class="hljs-attr">value</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'hello, I am '</span> + <span class="hljs-built_in">this</span>.name;
    &#125;
  &#125;, &#123;
    <span class="hljs-attr">key</span>: <span class="hljs-string">'name'</span>,
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'kevin'</span>;
    &#125;,
    <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">set</span>(<span class="hljs-params">newName</span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'new name 为：'</span> + newName);
    &#125;
  &#125;], [&#123;
    <span class="hljs-attr">key</span>: <span class="hljs-string">'onlySayHello'</span>,
    <span class="hljs-attr">value</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onlySayHello</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'hello'</span>;
    &#125;
  &#125;]);

  <span class="hljs-keyword">return</span> Person;
&#125;();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到 Babel 生成了一个 <code>_createClass</code> 辅助函数，该函数传入三个参数：</p>
<ul>
<li>第一个是构造函数，在这个例子中也就是 Person</li>
<li>第二个是要添加到<strong>原型</strong>上的函数数组</li>
<li>第三个是要添加到<strong>构造函数</strong>本身的函数数组，也就是所有添加 static 关键字的函数。</li>
</ul>
<p>该函数的作用就是将函数数组中的方法添加到构造函数或者构造函数的原型中，最后返回这个构造函数。</p>
<p>在其中，又生成了一个 <code>defineProperties</code> 辅助函数，使用 <code>Object.defineProperty</code> 方法添加属性。</p>
<p>默认 <code>enumerable</code> 为 false，<code>configurable</code> 为 true，这个在上面也有强调过，是为了防止 <code>Object.keys()</code> 之类的方法遍历到。然后通过判断 value 是否存在，来判断是否是 getter 和 setter。如果存在 value，就为 descriptor 添加 value 和 writable 属性，如果不存在，就直接使用 get 和 set 属性。</p></div>  
</div>
            