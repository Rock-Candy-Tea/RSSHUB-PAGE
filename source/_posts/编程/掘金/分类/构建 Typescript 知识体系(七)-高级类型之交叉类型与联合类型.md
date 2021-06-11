
---
title: '构建 Typescript 知识体系(七)-高级类型之交叉类型与联合类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2743'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 17:53:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=2743'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与更文挑战的第十三天，活动详情查看:<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>TS 的高级类型是，TS 为了保证语言的灵活性，所引用的一些语言特性。这些特性有利于应对复杂多变的开发场景</p>
<h2 data-id="heading-0">什么是交叉类型</h2>
<p>将多个类型合并为一个类型，新的类型将具有所有类型的特性，所以交叉类型特别适合对象过多的场景。<strong>交叉类型实际上是取所有类型的并集</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> DogInterface &#123;
  run(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">interface</span> CatInterface &#123;
  jump(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-comment">// pet变量将具有两个接口类型的所有方法</span>
<span class="hljs-comment">/*
不能将类型“&#123;&#125;”分配给类型“DogInterface & CatInterface”。
  类型 "&#123;&#125;" 中缺少属性 "run"，但类型 "DogInterface" 中需要该属性。ts(2322)
*/</span>
<span class="hljs-keyword">let</span> pet: DogInterface & CatInterface = &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> DogInterface &#123;
  run(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">interface</span> CatInterface &#123;
  jump(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-comment">// pet变量将具有两个接口类型的所有方法</span>
<span class="hljs-keyword">let</span> pet: DogInterface & CatInterface = &#123;
  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  <span class="hljs-function"><span class="hljs-title">jump</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">什么是联合类型</h2>
<p>声明的类型并不确定，可以为多个类型中的一个</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> a: <span class="hljs-built_in">number</span> | <span class="hljs-built_in">string</span> = <span class="hljs-string">"a"</span>;
<span class="hljs-keyword">let</span> b: <span class="hljs-built_in">number</span> | <span class="hljs-built_in">string</span> = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>有时候不仅要限制变量的类型，还需要限定变量的取值在某个特定的范围内</p>
<h2 data-id="heading-2">字符串的字面量联合类型</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//  testName是一个联合类型，并且取值必须是   'a'|'b'|'c' 中的一个</span>
<span class="hljs-keyword">let</span> testName: <span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">数字的字面量联合类型</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> testName: <span class="hljs-number">1</span> | <span class="hljs-number">2</span> | <span class="hljs-number">3</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">对象的联合类型</h2>
<p>如果对象时联合类型，在对象不确定的情况下，只能访问所有类型的公有有成员( <strong>这种情况下的联合类型只能取所有成员的交集</strong>)</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> DogInterface &#123;
  run(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">interface</span> CatInterface &#123;
  jump(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-comment">// pet变量将具有两个接口类型的所有方法</span>
<span class="hljs-keyword">let</span> pet: DogInterface & CatInterface = &#123;
  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  <span class="hljs-function"><span class="hljs-title">jump</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
&#125;;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-title">implements</span> <span class="hljs-title">DogInterface</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-title">implements</span> <span class="hljs-title">CatInterface</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">jump</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-built_in">enum</span> Master &#123;
  Boy,
  Girl,
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getPet</span>(<span class="hljs-params">master: Master</span>) </span>&#123;
  <span class="hljs-comment">// 类型推断为:  (let pet: Dog | Cat)  联合类型</span>
  <span class="hljs-keyword">let</span> pet = master === Master.Boy ? <span class="hljs-keyword">new</span> Dog() : <span class="hljs-keyword">new</span> Cat();
  <span class="hljs-comment">// 编译器提示只能调用  eat 方法</span>
  pet.eat();
  <span class="hljs-keyword">return</span> pet;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">可区分的联合类型</h2>
<p>本质上是结合联合类型与字面量类型的一种类型保护方法。核心思想:一个类型如果是多个对象的联合类型，并且每个类型之间有一个公共属性，就可以凭借此公共属性，创建类型保护区块</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Square &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"square"</span>;
  size: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> Reactangle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"reactangle"</span>;
  width: <span class="hljs-built_in">number</span>;
  height: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">type</span> Shape = Square | Reactangle;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">s: Shape</span>) </span>&#123;
  <span class="hljs-comment">// 通过两个类型的共有属性 kind,就可以创建类型保护区块</span>
  <span class="hljs-keyword">switch</span> (s.kind) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"reactangle"</span>:
      <span class="hljs-keyword">return</span> s.height * s.width;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>:
      <span class="hljs-keyword">return</span> s.size * s.size;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码如果不升级维护是没有问题的，但是如果添加了一个新的形状后呢？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Square &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"square"</span>;
  size: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> Reactangle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"reactangle"</span>;
  width: <span class="hljs-built_in">number</span>;
  height: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> Circle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>;
  r: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">type</span> Shape = Square | Reactangle | Circle;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">s: Shape</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (s.kind) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"reactangle"</span>:
      <span class="hljs-keyword">return</span> s.height * s.width;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>:
      <span class="hljs-keyword">return</span> s.size * s.size;
  &#125;
&#125;

<span class="hljs-comment">// 打印出undefined</span>
<span class="hljs-built_in">console</span>.log(area(&#123; <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>, <span class="hljs-attr">r</span>: <span class="hljs-number">100</span> &#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决方式一:为函数指定一个明确的返回类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Square &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"square"</span>;
  size: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> Reactangle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"reactangle"</span>;
  width: <span class="hljs-built_in">number</span>;
  height: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> Circle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>;
  r: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">type</span> Shape = Square | Reactangle | Circle;
<span class="hljs-comment">/*
函数缺少结束 return 语句，返回类型不包括 "undefined"。ts(2366)
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">s: Shape</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">switch</span> (s.kind) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"reactangle"</span>:
      <span class="hljs-keyword">return</span> s.height * s.width;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>:
      <span class="hljs-keyword">return</span> s.size * s.size;
  &#125;
&#125;

<span class="hljs-built_in">console</span>.log(area(&#123; <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>, <span class="hljs-attr">r</span>: <span class="hljs-number">100</span> &#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决方式二: 检查是否是 <code>never</code> 类型，如果是 <code>never</code> 类型，说明前面所有的分支都被覆盖了， 如实 <code>s</code> 不是 <code>never</code> 类型，就说明前面的分支有遗漏</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Reactangle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"reactangle"</span>;
  width: <span class="hljs-built_in">number</span>;
  height: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> Circle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>;
  r: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">type</span> Shape = Square | Reactangle | Circle;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">s: Shape</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (s.kind) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"reactangle"</span>:
      <span class="hljs-keyword">return</span> s.height * s.width;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>:
      <span class="hljs-keyword">return</span> s.size * s.size;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-comment">/*
类型“Circle”的参数不能赋给类型“never”的参数。ts(2345)
*/</span>
      <span class="hljs-keyword">return</span> (<span class="hljs-function">(<span class="hljs-params">e: <span class="hljs-built_in">never</span></span>) =></span> &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(e);
      &#125;)(s);
  &#125;
&#125;

<span class="hljs-built_in">console</span>.log(area(&#123; <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>, <span class="hljs-attr">r</span>: <span class="hljs-number">100</span> &#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Square &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"square"</span>;
  size: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> Reactangle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"reactangle"</span>;
  width: <span class="hljs-built_in">number</span>;
  height: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> Circle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>;
  r: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">type</span> Shape = Square | Reactangle | Circle;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">s: Shape</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (s.kind) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"reactangle"</span>:
      <span class="hljs-keyword">return</span> s.height * s.width;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>:
      <span class="hljs-keyword">return</span> s.size * s.size;
    <span class="hljs-comment">// 添加上遗漏的分支即可</span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">"circle"</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * s.r ** <span class="hljs-number">2</span>;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> (<span class="hljs-function">(<span class="hljs-params">e: <span class="hljs-built_in">never</span></span>) =></span> &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(e);
      &#125;)(s);
  &#125;
&#125;

<span class="hljs-comment">// 打印出正确的值</span>
<span class="hljs-built_in">console</span>.log(area(&#123; <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>, <span class="hljs-attr">r</span>: <span class="hljs-number">100</span> &#125;));
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            