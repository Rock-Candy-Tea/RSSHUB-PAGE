
---
title: '聊聊 Typescript 中如何更好地实现多继承与类型推断'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9995'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 21:34:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=9995'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">前言</h2>
<p>最近由于在设计一个sdk，想用搭积木的方式，把不同功能拆分模块，在使用的时候让一个class 通过混合的方式获得不同的功能，于是就开始了对js 多继承的研究。</p>
<p>在实现了多继承之后，又因为用了 typescript 的代码，发现各种语法错误的提醒，所以，在一步步的实践过程中，发现了很多关于多继承的有意思的知识，因此想在这里聊聊关于自己对于多继承的一些认识。</p>
<hr>
<h2 data-id="heading-1">实现</h2>
<p>在javascript 中，并不存在真正意义上的多继承，本质上是将需要继承的类合并为一个，且无论是es 语法或者typescirpt 都尚未有相关实现。为了实现多继承，我们可以通过链式继承或者Mixin 方式实现。</p>
<p>在开始介绍实现方式之前，为了方便class 的声明，我们首先需要定义一个表示构造器的type 用于后续的使用：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Constructor<T = Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>>> = <span class="hljs-keyword">new</span> (...args: <span class="hljs-built_in">any</span>[]) => T;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h3 data-id="heading-2">链式继承</h3>
</li>
</ul>
<p>链式继承的逻辑是从基类开始，根据顺序一个个去继承，最终组合返回成一个类，这个类由最外层也就是最后调用的继承函数所决定，实现的源码如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Base</span>  </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">...args</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'base'</span>)
    &#125;
    <span class="hljs-function"><span class="hljs-title">baseFn</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'base'</span>)
    &#125;
  &#125;

  <span class="hljs-keyword">const</span> AExtends = (SuperClass: T)<T <span class="hljs-keyword">extends</span> Constructor> =>
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SuperClass</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">...args</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(...args)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a ctor'</span>)
      &#125;
      <span class="hljs-function"><span class="hljs-title">aFn</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>);
      &#125;
    &#125;;

  <span class="hljs-keyword">const</span> BExtends = (SuperClass: T)<T <span class="hljs-keyword">extends</span> Constructor> =>
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SuperClass</span> </span>&#123;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">...args</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(...args)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b ctor'</span>)
      &#125;
      <span class="hljs-function"><span class="hljs-title">bFn</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b'</span>);
      &#125;
    &#125;;

  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">BExtends</span>(<span class="hljs-title">AExtends</span>(<span class="hljs-title">Base</span>)) </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">super</span>();
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'test ctor'</span>);
      <span class="hljs-built_in">this</span>.aFn();
      <span class="hljs-built_in">this</span>.bFn();
      
      <span class="hljs-built_in">this</span>.test(); <span class="hljs-comment">// 方法并不存在，但typescript 却不会报错</span>
    &#125;
  &#125;

  <span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> Test();
  <span class="hljs-comment">// base</span>
  <span class="hljs-comment">// a ctor</span>
  <span class="hljs-comment">// b ctor</span>
  <span class="hljs-comment">// test ctor</span>
  <span class="hljs-comment">// a</span>
  <span class="hljs-comment">// b</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据上面的代码的输出结果可以看出，constructor 的调用顺序会按照嵌套的顺序从里到外的执行，看起来很完美，不是吗？</p>
<p>并不，这种方式实际上会把类的原型链的层级变得复杂，当需要混入的类较多的时候，追溯和更改继承的顺序都将是一场灾难。</p>
<p>同时，在使用typescript 的时候，如果不小心使用了一个不存在的方法，由于类型推导我们返回的是一个匿名类，并不知道存在哪些方法，所以不会触发语法错误提示，也就使得类型不再安全。</p>
<p>解决的方法也是有的，就是需要在每个继承函数上声明类的接口</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> AExtends = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">T</span> <span class="hljs-attr">extends</span> <span class="hljs-attr">Constructor</span>></span>(SuperClass: T): T & Constructor<&#123; aFn: ()=> void&#125;> => // ...
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这样一来我们需要的工作也变得重复和繁琐，因此，我们可以尝试用接下来的方式来实现</p>
<ul>
<li>
<h3 data-id="heading-3">Mixin 混合</h3>
</li>
</ul>
<p>这种方式是参考TypeScript <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fmixins.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/mixins.html" ref="nofollow noopener noreferrer">mixins 的内容</a> 而来的，实现的逻辑是将多个类的原型方法拷贝到一个空类上面然后返回，实现的源码如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Mixin</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">Constructor</span>[]>(<span class="hljs-params">
    ...mixins: T
  </span>) </span>&#123;
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Mix</span> </span>&#123;&#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copyProperties</span>(<span class="hljs-params">target, source</span>) </span>&#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">of</span> <span class="hljs-built_in">Reflect</span>.ownKeys(source)) &#123;
        <span class="hljs-comment">// 这些属性会影响继承的基类，避开不继承</span>
        <span class="hljs-keyword">if</span> (key !== <span class="hljs-string">'constructor'</span> && key !== <span class="hljs-string">'prototype'</span> && key !== <span class="hljs-string">'name'</span>) &#123;
          <span class="hljs-keyword">let</span> desc = <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(source, key);
          <span class="hljs-built_in">Object</span>.defineProperty(target, key, desc);
        &#125;
      &#125;
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> mixin <span class="hljs-keyword">of</span> mixins) &#123;
      copyProperties(Mix, mixin); <span class="hljs-comment">// 拷贝静态属性</span>

      copyProperties(Mix.prototype, mixin.prototype); <span class="hljs-comment">// 拷贝原型属性</span>
    &#125;
    <span class="hljs-keyword">return</span> Mix;
  &#125;

  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Base</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">baseFn</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'base'</span>)
    &#125;
  &#125;

  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">aFn</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>)
    &#125;
  &#125;

  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">bFn</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b'</span>)
    &#125;
  &#125;

  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Mixin</span>(<span class="hljs-title">Base</span>, <span class="hljs-title">A</span>, <span class="hljs-title">B</span>) </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">super</span>();
      <span class="hljs-built_in">this</span>.aFn();
      <span class="hljs-built_in">this</span>.bFn();
      <span class="hljs-built_in">this</span>.baseFn();
    &#125;
  &#125;

  <span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> Test();

  <span class="hljs-comment">// a</span>
  <span class="hljs-comment">// b</span>
  <span class="hljs-comment">// base</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方式最终得到的继承链就会比前一种方式简短得多，因为只会有<code>Mix</code>这一层，但是这种方式会丢弃掉所有继承类的 <code>constructor</code>，同时，由于返回的是<code>Mix</code>这个类，typescript 并不能认出原型链上的属性，所以会在使用继承的方法的时候提示语法错误。为了解决这个问题，我们需要为这个函数声明返回类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-keyword">type</span> UnionToIntersection<U> = (U <span class="hljs-keyword">extends</span> <span class="hljs-built_in">any</span> ? <span class="hljs-function">(<span class="hljs-params">k: U</span>) =></span> <span class="hljs-built_in">void</span> : <span class="hljs-built_in">never</span>) <span class="hljs-keyword">extends</span> (
    k: infer I
  ) => <span class="hljs-built_in">void</span>
    ? I
    : <span class="hljs-built_in">never</span>;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Mixin</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">Constructor</span>[]>(<span class="hljs-params">
  ...mixins: T
  </span>): <span class="hljs-title">Constructor</span><<span class="hljs-title">UnionToIntersection</span><<span class="hljs-title">InstanceType</span><<span class="hljs-title">T</span>[<span class="hljs-title">number</span>]>>></span>;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Mixin</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">Constructor</span>[]>(<span class="hljs-params">
    ...mixins: T
  </span>) </span>&#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-keyword">return</span> Mix;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先我们定义了一个交集类型，把所有需要继承的类通过<code>InstanceType</code> 获取构造函数的实例类型并合并起来。</p>
<p>这里有个需要注意的地方是，入参的类型是 <code>T</code> 而不是 <code>T[]</code> ，且<code>T</code> 是继承自<code>Contructor[]</code>的，这样一来，我们才能通过 <code>T[number]</code> 的方式获取每个参数来进行推导。</p>
<p>到此，我们已经可以得到一个基础版本的混入了，但是，如果我们需要继承的类也是继承了其他父类的情况下，像下面这种情况，就会出现找不到祖父类上的方法的问题</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">pFn</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'parent'</span>)
    &#125;
  &#125;

  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parent</span> </span>&#123;
    <span class="hljs-comment">//...</span>
  &#125;

  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parent</span> </span>&#123;
    <span class="hljs-comment">//...</span>
  &#125;
  <span class="hljs-comment">//...</span>
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Mixin</span>(<span class="hljs-title">Base</span>, <span class="hljs-title">A</span>, <span class="hljs-title">B</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">super</span>();
      <span class="hljs-built_in">this</span>.aFn();
      <span class="hljs-built_in">this</span>.bFn();
      <span class="hljs-built_in">this</span>.baseFn();

      <span class="hljs-built_in">this</span>.pFn(); <span class="hljs-comment">// this.pFn is not a function</span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了解决这个问题，我们还需要在拷贝属性时，多加一步对继承类的拷贝，</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Mixin</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">Constructor</span>[]>(<span class="hljs-params">...mixins: T</span>) </span>&#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> mixin <span class="hljs-keyword">of</span> mixins) &#123;

      <span class="hljs-comment">//...</span>

      copyProperties(Mix.prototype, mixin.prototype.__proto__); <span class="hljs-comment">// 拷贝继承的原型属性</span>
    &#125;
    <span class="hljs-comment">//...</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次运行，我们就能得到 <code>a b base parent</code> 这个正确的结果了。</p>
<p>到这里我们看起来得到了一个比第一种方法看起来更完美的多继承解决方案了，不是吗？</p>
<p>但是……</p>
<p>这种方案其实存在两个说大不大说小不小的缺点：</p>
<h3 data-id="heading-4">1. <strong>实例属性缺失</strong></h3>
<p>通过以下的代码我们可以看到，我们无法直接获取到以等式形式写入到类上的实例属性</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  aProps = <span class="hljs-number">123</span>;
  <span class="hljs-function"><span class="hljs-title">aFn</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="hljs-built_in">Reflect</span>.ownKeys(A) <span class="hljs-comment">// [ 'constructor', 'aFn' ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了遍历到实例属性，我们只能把属性定义到class的<code>prototype</code> 上，才能拷贝到继承的子类上，而且子类获取时只会拿到<code>prototype</code> 上定义的值，本身的值会被忽略。</p>
<p>问题是解决了，但是意味着我们的属性都需要定义在外部，不够优雅和直觉。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> </span>&#123;
  bProps;
  <span class="hljs-function"><span class="hljs-title">bFn</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
B.prototype.bProps = <span class="hljs-number">123</span>;
<span class="hljs-built_in">Reflect</span>.ownKeys(B) <span class="hljs-comment">// [ 'constructor', 'bFn', 'bProps' ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2. <strong>重名方法覆盖</strong></h3>
<p>试想一下，下面的代码会输出什么？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Base</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">same</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'base same'</span>)
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">same</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a same'</span>)
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">same</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b same'</span>)
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Mixin</span>(<span class="hljs-title">Base</span>, <span class="hljs-title">A</span>, <span class="hljs-title">B</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
    <span class="hljs-built_in">this</span>.same();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>答案是<code>b same</code>，也就是最后一个拷贝的class 上的<code>same</code> 方法，覆盖了前面的<code>same</code> 方法。</p>
<p>为了解决这个问题，我们可以通过将同名的方法按组合顺序合并为一个方法，然后在调用这个组合方法的时候依次执行这些同名方法。另外，执行的上下文也是需要注意改写的</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Mixin</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">Constructor</span>[]>(<span class="hljs-params">
  ...mixins: T
</span>) </span>&#123;
  <span class="hljs-comment">//...</span>
  <span class="hljs-keyword">const</span> mergeDesc = &#123;&#125;;
  <span class="hljs-keyword">const</span> allowMergeKeys = [<span class="hljs-string">'init'</span>, <span class="hljs-string">'same'</span>];
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copyProperties</span>(<span class="hljs-params">target, source</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">of</span> <span class="hljs-built_in">Reflect</span>.ownKeys(source)) &#123;
      <span class="hljs-keyword">if</span> (key !== <span class="hljs-string">'constructor'</span> && key !== <span class="hljs-string">'prototype'</span> && key !== <span class="hljs-string">'name'</span>) &#123;
        <span class="hljs-keyword">let</span> desc = <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(source, key);
        <span class="hljs-keyword">if</span> (allowMergeKeys.includes(key <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>)) &#123;
          mergeDesc[key] = mergeDesc[key] || [];
          mergeDesc[key].push(desc.value);
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">Object</span>.defineProperty(target, key, desc);
        &#125;
      &#125;
    &#125;
  &#125;
  <span class="hljs-comment">//...</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> mergeDesc) &#123;
    <span class="hljs-keyword">const</span> fns = mergeDesc[key];
    <span class="hljs-built_in">Object</span>.defineProperty(Mix.prototype, key, &#123;
      <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-function"><span class="hljs-title">value</span>(<span class="hljs-params">...args</span>)</span> &#123;
        <span class="hljs-keyword">const</span> context = <span class="hljs-built_in">this</span>;
        fns.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn</span>) </span>&#123;
          fn.call(context, ...args);
        &#125;);
      &#125;,
    &#125;);
  &#125;
  <span class="hljs-comment">//...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-6">总结</h2>
<p>虽然我们已经可以实现了多继承，并完成了类型推断，但其实上述的两种方法都各有缺点：第一种方法可以解决构造器和重复调用的问题，但是对typescript 的类型推断不友好；第二种方式对typescript 更友好，但是却不方便多层继承和重名属性拓展；因此，希望未来的ES 中有更好的对多继承的实现支持。</p>
<p>同时，如果各位大大有更好的实现方式或者对上面代码存在的问题有疑问或者建议，欢迎指教，感谢</p></div>  
</div>
            