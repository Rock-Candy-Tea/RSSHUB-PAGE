
---
title: 'JavaScript 系列之类型（二）｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5633d14322934986a31b19e58cb27735~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 16:31:19 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5633d14322934986a31b19e58cb27735~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">三、类型判断</h2>
<p>JavaScript 判断变量的方式有：</p>
<ul>
<li><code>typeof(variable)</code></li>
<li><code>variable instanceof Array</code></li>
<li><code>variable.constructor = Array</code></li>
<li><code>Object.prototype.toString.call(variable)</code></li>
</ul>
<h3 data-id="heading-1">3.1 typeof</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> num = <span class="hljs-number">123</span>;
<span class="hljs-keyword">var</span> str = <span class="hljs-string">'abcdef'</span>;
<span class="hljs-keyword">var</span> bool = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">var</span> json = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'jsliang'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">25</span> &#125;;
<span class="hljs-keyword">var</span> func = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'this is function'</span>); &#125;
<span class="hljs-keyword">var</span> und = <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">var</span> nul = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="hljs-keyword">var</span> reg = <span class="hljs-regexp">/^[a-zA-Z]&#123;5,20&#125;$/</span>;
<span class="hljs-keyword">var</span> error = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>();
<span class="hljs-keyword">var</span> nan = <span class="hljs-literal">NaN</span>;

<span class="hljs-built_in">console</span>.log(
  <span class="hljs-keyword">typeof</span> num, <span class="hljs-comment">// number</span>
  <span class="hljs-keyword">typeof</span> str, <span class="hljs-comment">// string</span>
  <span class="hljs-keyword">typeof</span> bool, <span class="hljs-comment">// boolean</span>
  <span class="hljs-keyword">typeof</span> arr, <span class="hljs-comment">// object</span>
  <span class="hljs-keyword">typeof</span> json, <span class="hljs-comment">// object</span>
  <span class="hljs-keyword">typeof</span> func, <span class="hljs-comment">// function</span>
  <span class="hljs-keyword">typeof</span> und, <span class="hljs-comment">// undefined</span>
  <span class="hljs-keyword">typeof</span> nul, <span class="hljs-comment">// object</span>
  <span class="hljs-keyword">typeof</span> date, <span class="hljs-comment">// object</span>
  <span class="hljs-keyword">typeof</span> reg, <span class="hljs-comment">// object</span>
  <span class="hljs-keyword">typeof</span> error, <span class="hljs-comment">// object</span>
  <span class="hljs-keyword">typeof</span> nan, <span class="hljs-comment">// number</span>
  
  <span class="hljs-keyword">typeof</span> <span class="hljs-number">10n</span>; <span class="hljs-comment">// bigint</span>
  <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">BigInt</span>(<span class="hljs-number">10</span>); <span class="hljs-comment">// bigint</span>
  <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span>(); <span class="hljs-comment">// symbol</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>typeof</code> 能区分的：</p>
<ul>
<li><code>number</code></li>
<li><code>string</code></li>
<li><code>boolean</code></li>
<li><code>undefined</code></li>
<li><code>symbol</code></li>
</ul>
<hr>
<ul>
<li><code>function</code></li>
<li>检测其他类型的时候，都返回 <code>object</code>。</li>
</ul>
<blockquote>
<p>PS：为什么会出现 <code>type null // object</code> 这种情况呢？因为在 JS 的最初版本中，使用的是 32 位系统，为了性能考虑使用低位存储了变量的类型信息，000 开头代表是对象，然而 null 表示为全零，所以将它错误的判断为 object 。虽然现在的内部类型判断代码已经改变了，但是对于这个 Bug 却是一直流传下来。</p>
</blockquote>
<h3 data-id="heading-2">3.2 instanceof</h3>
<p>用于实例和构造函数的对应。例如判断一个变量是否是数组，使用 <code>typeof</code> 无法判断，但可以使用 <code>[1, 2] instanceof Array</code> 来判断。因为，<code>[1, 2]</code> 是数组，它的构造函数就是 <code>Array</code>。</p>
<p><code>instanceof</code> 判断原型链指向，我们可以看一下它的实现原理：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5633d14322934986a31b19e58cb27735~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myInstanceof</span>(<span class="hljs-params">left, right</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> left !== <span class="hljs-string">'object'</span> || right === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
  
  <span class="hljs-comment">// 获得类型的原型</span>
  <span class="hljs-keyword">let</span> prototype = right.prototype
  <span class="hljs-comment">// 获得对象的原型</span>
  left = left.__proto__
  <span class="hljs-comment">// 判断对象的类型是否等于类型的原型</span>
  <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
    <span class="hljs-keyword">if</span> (left === <span class="hljs-literal">null</span>)
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    <span class="hljs-keyword">if</span> (prototype === left)
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    left = left.__proto__
  &#125;
&#125;

<span class="hljs-built_in">console</span>.log(myInstanceof([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>], <span class="hljs-built_in">Array</span>)) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> num = <span class="hljs-number">123</span>;
<span class="hljs-keyword">var</span> str = <span class="hljs-string">'abcdef'</span>;
<span class="hljs-keyword">var</span> bool = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">var</span> json = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'jsliang'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">25</span> &#125;;
<span class="hljs-keyword">var</span> func = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'this is function'</span>); &#125;
<span class="hljs-keyword">var</span> und = <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">var</span> nul = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="hljs-keyword">var</span> reg = <span class="hljs-regexp">/^[a-zA-Z]&#123;5,20&#125;$/</span>;
<span class="hljs-keyword">var</span> error = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>();

<span class="hljs-built_in">console</span>.log(
  num <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Number</span>, <span class="hljs-comment">// false</span>
  str <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">String</span>, <span class="hljs-comment">// false</span>
  bool <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Boolean</span>, <span class="hljs-comment">// false</span>
  und <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>, <span class="hljs-comment">// false</span>
  nul <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>, <span class="hljs-comment">// false</span>
  arr <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>, <span class="hljs-comment">// true</span>
  json <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>, <span class="hljs-comment">// true</span>
  func <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Function</span>, <span class="hljs-comment">// true</span>
  date <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Date</span>, <span class="hljs-comment">// true</span>
  reg <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">RegExp</span>, <span class="hljs-comment">// true</span>
  error <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Error</span>, <span class="hljs-comment">// true</span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>instanceof</code> 能判断的有：</p>
<ul>
<li><code>Array</code></li>
<li><code>Function</code></li>
<li><code>Date</code></li>
<li><code>RegExp</code></li>
<li><code>Error</code></li>
</ul>
<h3 data-id="heading-3">3.3 constructor</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> num = <span class="hljs-number">123</span>;
<span class="hljs-keyword">var</span> str = <span class="hljs-string">'abcdef'</span>;
<span class="hljs-keyword">var</span> bool = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">var</span> json = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'jsliang'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">25</span> &#125;;
<span class="hljs-keyword">var</span> func = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'this is function'</span>); &#125;
<span class="hljs-keyword">var</span> und = <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">var</span> nul = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="hljs-keyword">var</span> reg = <span class="hljs-regexp">/^[a-zA-Z]&#123;5,20&#125;$/</span>;
<span class="hljs-keyword">var</span> error = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>)</span>&#123;

&#125;
<span class="hljs-keyword">var</span> Tom = <span class="hljs-keyword">new</span> Person();

<span class="hljs-built_in">console</span>.log(
  Tom.constructor === Person, <span class="hljs-comment">// true</span>
  num.constructor === <span class="hljs-built_in">Number</span>, <span class="hljs-comment">// true</span>
  str.constructor === <span class="hljs-built_in">String</span>, <span class="hljs-comment">// true</span>
  bool.constructor === <span class="hljs-built_in">Boolean</span>, <span class="hljs-comment">// true</span>
  arr.constructor === <span class="hljs-built_in">Array</span>, <span class="hljs-comment">// true</span>
  json.constructor === <span class="hljs-built_in">Object</span>, <span class="hljs-comment">// true</span>
  func.constructor === <span class="hljs-built_in">Function</span>, <span class="hljs-comment">// true</span>
  date.constructor === <span class="hljs-built_in">Date</span>, <span class="hljs-comment">// true</span>
  reg.constructor === <span class="hljs-built_in">RegExp</span>, <span class="hljs-comment">// true</span>
  error.constructor === <span class="hljs-built_in">Error</span> <span class="hljs-comment">// true</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>得到的所有结果都是 <code>true</code>，除了 <code>undefined</code> 和 <code>null</code>，其他类型基本可以通过 <code>constructor</code> 判断。</p>
<p>不过因为 <code>constructor</code> 的属性是可以被修改的，可能导致检测出的结果不正确。</p>
<h3 data-id="heading-4">3.4 Object.prototype.toString.call</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> num = <span class="hljs-number">123</span>;
<span class="hljs-keyword">var</span> str = <span class="hljs-string">'abcdef'</span>;
<span class="hljs-keyword">var</span> bool = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">var</span> json = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'jsliang'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">25</span> &#125;;
<span class="hljs-keyword">var</span> func = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'this is function'</span>); &#125;
<span class="hljs-keyword">var</span> und = <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">var</span> nul = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="hljs-keyword">var</span> reg = <span class="hljs-regexp">/^[a-zA-Z]&#123;5,20&#125;$/</span>;
<span class="hljs-keyword">var</span> error = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>();

<span class="hljs-built_in">console</span>.log(
  <span class="hljs-built_in">Object</span>.prototype.toString.call(num), <span class="hljs-comment">// [object Number]</span>
  <span class="hljs-built_in">Object</span>.prototype.toString.call(str), <span class="hljs-comment">// [object String]</span>
  <span class="hljs-built_in">Object</span>.prototype.toString.call(bool), <span class="hljs-comment">// [object Boolean]</span>
  <span class="hljs-built_in">Object</span>.prototype.toString.call(arr), <span class="hljs-comment">// [object Array]</span>
  <span class="hljs-built_in">Object</span>.prototype.toString.call(json), <span class="hljs-comment">// [object Object]</span>
  <span class="hljs-built_in">Object</span>.prototype.toString.call(func), <span class="hljs-comment">// [object Function]</span>
  <span class="hljs-built_in">Object</span>.prototype.toString.call(und), <span class="hljs-comment">// [object Undefined]</span>
  <span class="hljs-built_in">Object</span>.prototype.toString.call(nul), <span class="hljs-comment">// [object Null]</span>
  <span class="hljs-built_in">Object</span>.prototype.toString.call(date), <span class="hljs-comment">// [object Date]</span>
  <span class="hljs-built_in">Object</span>.prototype.toString.call(reg), <span class="hljs-comment">// [object RegExp]</span>
  <span class="hljs-built_in">Object</span>.prototype.toString.call(error), <span class="hljs-comment">// [object Error]</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个完美的判断方法，可以检测上面提到的所有类型，只需要将它的结果 <code>result.slice(8, -1)</code> 就能得到具体的类型。</p></div>  
</div>
            