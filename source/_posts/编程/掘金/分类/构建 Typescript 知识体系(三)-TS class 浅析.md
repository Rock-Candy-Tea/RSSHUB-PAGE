
---
title: '构建 Typescript 知识体系(三)-TS class 浅析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2871'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 02:08:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=2871'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与更文挑战的第九天，活动详情查看:<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><strong>无论 ES 还是 TS 中， 类成员都是实例属性，类成员方法都是实例方法</strong></p>
<h2 data-id="heading-0">一. TS 中 class 的特点</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;

  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-built_in">console</span>.log(Dog.prototype);
<span class="hljs-comment">// &#123;run: ƒ, constructor: ƒ&#125;</span>

<span class="hljs-comment">/*
打印出类的原型，
结果是不包含类的成员的， 只有  run(), constructor()
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">1.1 成员属性只在实例上， 而不在原型上</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> dog = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">"大黄"</span>);
<span class="hljs-built_in">console</span>.log(dog);
<span class="hljs-comment">// Dog &#123;name: "大黄"&#125;</span>

<span class="hljs-comment">/*
可以看出name属性只在实例上， 而不在原型上
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2.1 实例的属性必须具有初始值，或者在构造函数中被初始化</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog1</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-comment">// this.name = name;</span>
  &#125;
  <span class="hljs-comment">// 错误提示: 属性“name”没有初始化表达式，且未在构造函数中明确赋值。ts(2564)</span>
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;

  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog1</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-comment">// this.name = name;</span>
  &#125;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span> = <span class="hljs-string">"dog"</span>;

  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-comment">// 或者</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog2</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;

  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">二. 类的继承</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat0</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-comment">//错误提示: 派生类的构造函数必须包含 "super" 调用。ts(2377)</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决 <code>super</code> 代表父类的实例</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, color: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name);
    <span class="hljs-built_in">this</span>.color = color;
  &#125;
  <span class="hljs-attr">color</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">三. 类的成员修饰符</h2>
<h3 data-id="heading-5">1. 共有成员-public</h3>
<p><strong>类的所有属性默认都是 public，当然也可以直接申明出来</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog1</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-comment">// this.name = name;</span>
  &#125;
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span> = <span class="hljs-string">"dog"</span>;

  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2. 私有成员-private</h3>
<p><strong>私有成员只能被类本身调用，而不能被类的实例调用，有不能被子类调用</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>;

  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;&#125;

  <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-keyword">let</span> dog = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">"大黄"</span>);

<span class="hljs-comment">// 错误提示:  属性“walk”为私有属性，只能在类“Dog”中访问。ts(2341)</span>
dog.walk();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, color: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name);
    <span class="hljs-built_in">this</span>.color = color;
    <span class="hljs-comment">// 错误提示:  属性“walk”为私有属性，只能在类“Dog”中访问。ts(2341)</span>
    <span class="hljs-built_in">this</span>.walk = <span class="hljs-function">() =></span> &#123;&#125;;
  &#125;
  <span class="hljs-attr">color</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>可以给构造函数添加私有成员属性，表示该类既不能被实例化，也不能被继承</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>;

  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;&#125;

  <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="hljs-comment">// 错误提示:  类“Dog”的构造函数是私有的，仅可在类声明中访问。ts(2673)</span>
<span class="hljs-keyword">let</span> dog = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">"大黄"</span>);

<span class="hljs-comment">// 错误提示:  无法扩展类“Dog”。类构造函数标记为私有。ts(2675)</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, color: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name);
    <span class="hljs-built_in">this</span>.color = color;
  &#125;
  <span class="hljs-attr">color</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">3. 受保护成员-protect</h3>
<p><strong>受保护成员只能在类及其子类中访问， 而不能再类的实例中访问</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>;

  <span class="hljs-keyword">protected</span> <span class="hljs-function"><span class="hljs-title">shout</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-keyword">let</span> dog = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">"大黄"</span>);
<span class="hljs-comment">// 错误提示: 属性“shout”受保护，只能在类“Dog”及其子类中访问。ts(2445)</span>
dog.shout();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, color: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name);
    <span class="hljs-built_in">this</span>.color = color;
    <span class="hljs-comment">// 可以正常访问和执行</span>
    <span class="hljs-built_in">this</span>.shout();
  &#125;
  <span class="hljs-attr">color</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>可以给构造函数添加受保护成员属性，表示该类不能被实例化，只能被继承，相当于申明一个基类</strong></p>
<h3 data-id="heading-8">4. 只读属性</h3>
<p><strong>只读属性表示不能被更改，并且一定要被初始化</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>;

  <span class="hljs-keyword">readonly</span> foots: <span class="hljs-built_in">number</span> = <span class="hljs-number">4</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">5. 静态成员-static</h3>
<p><strong>类的静态成员只能通过类名来调用，二不能通过子类调用</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>;

  <span class="hljs-keyword">static</span> food = <span class="hljs-string">"bones"</span>;
&#125;

<span class="hljs-keyword">let</span> dog = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">"大黄"</span>);
<span class="hljs-comment">// bones</span>
<span class="hljs-built_in">console</span>.log(Dog.food);
<span class="hljs-comment">// 错误提示: 属性 "food" 不是类型为 "Dog" 的静态成员ts(2576)</span>
<span class="hljs-built_in">console</span>.log(dog.food);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>类的静态成员也可以被继承</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>;

  <span class="hljs-keyword">static</span> food = <span class="hljs-string">"bones"</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, color: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name);
    <span class="hljs-built_in">this</span>.color = color;
  &#125;
  <span class="hljs-attr">color</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-comment">// bones</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Cat.food :"</span>, Cat.food);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES 中并没有抽象类的概念，TS 对此进行了扩展</p>
<h2 data-id="heading-10">抽象类</h2>
<p><strong>抽象类: 只能被继承，不能被实例化的类</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="hljs-comment">// 无法创建抽象类的实例。ts(2511)</span>
<span class="hljs-keyword">let</span> animal = <span class="hljs-keyword">new</span> Animal();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>可以在抽象类中定义一个具体的方法并有相关实现</strong>
<strong>这样子类就可以直接使用，而不用重复实现---实现了方法的复用</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"eat"</span>);
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Pig</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>;

  <span class="hljs-keyword">static</span> food = <span class="hljs-string">"bones"</span>;
&#125;

<span class="hljs-keyword">let</span> pig = <span class="hljs-keyword">new</span> Pig(<span class="hljs-string">"佩奇"</span>);

pig.eat();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">多态</h2>
<p><strong>可以在抽象类中定义一个方法但不具体实现，形成一个抽象方法</strong>
**抽象方法的好处是可以在子类中有多种方式实现， **</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;

  <span class="hljs-keyword">abstract</span> sleep(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Pig</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>;

  <span class="hljs-function"><span class="hljs-title">sleep</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"站着睡"</span>);
  &#125;
&#125;

<span class="hljs-keyword">let</span> pig = <span class="hljs-keyword">new</span> Pig(<span class="hljs-string">"佩奇"</span>);

pig.sleep();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">sleep</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"趴着睡"</span>);
  &#125;
&#125;
<span class="hljs-keyword">let</span> cat = <span class="hljs-keyword">new</span> Cat();
cat.sleep();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">特殊的 TS 类型: this 类型</h2>
<p><strong>类的成员方法可以直接返回一个 this, 这样就可以很方便的实现链式调用</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WorkFlow</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">step1</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">step2</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;
&#125;

<span class="hljs-keyword">let</span> workFlow = <span class="hljs-keyword">new</span> WorkFlow();

workFlow.step1().step2();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在继承的时候，<code>this</code> 也可以表现出多态(this 既可以是父类型，也可以是子类型)</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WorkFlow</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">step1</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">step2</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;
&#125;

<span class="hljs-keyword">let</span> workFlow = <span class="hljs-keyword">new</span> WorkFlow();

workFlow.step1().step2();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyFlow</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">WorkFlow</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;
&#125;

<span class="hljs-keyword">let</span> myflow = <span class="hljs-keyword">new</span> MyFlow();

<span class="hljs-comment">// myflow.next():  MyFlow &#123;&#125;</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"myflow.next(): "</span>, myflow.next());

<span class="hljs-comment">// myflow.next().step1():  MyFlow &#123;&#125;</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"myflow.next().step1(): "</span>, myflow.next().step1().next().step2());
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            