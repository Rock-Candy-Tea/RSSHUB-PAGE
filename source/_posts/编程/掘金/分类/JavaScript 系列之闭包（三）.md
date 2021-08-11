
---
title: 'JavaScript 系列之闭包（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6289'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 17:15:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=6289'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">五、柯里化</h2>
<blockquote>
<p>柯里化（Currying）是把接受多个参数的函数转变为单一参数的函数，并且返回接受余下的参数且返回结果的新函数的技术。</p>
</blockquote>
<p>简单来说：</p>
<ol>
<li>通过闭包管理</li>
<li>支持链式调用</li>
<li>每次运行返回一个 function</li>
</ol>
<p>即：通过将多个参数换成一个参数，每次运行返回新函数的技术</p>
<h3 data-id="heading-1">5.1 柯里化举例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 普通的 add 函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span> (<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 柯里化函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curryingAdd</span> (<span class="hljs-params">x</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">y</span>) </span>&#123;
    <span class="hljs-keyword">return</span> x + y;
  &#125;
&#125;
curryingAdd(x)(y);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">5.2 柯里化好处</h3>
<ol>
<li>参数复用</li>
<li>提前确认</li>
<li>延迟运行</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 校验数字</span>
<span class="hljs-keyword">let</span> numberReg = <span class="hljs-regexp">/[0-9]+/g</span>;

<span class="hljs-comment">// 校验小写字母</span>
<span class="hljs-keyword">let</span> stringReg = <span class="hljs-regexp">/[a-z]+/g</span>;

<span class="hljs-comment">// currying 后</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curryingCheck</span>(<span class="hljs-params">reg</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">txt</span>) </span>&#123;
    <span class="hljs-keyword">return</span> reg.test(txt);
  &#125;
&#125;


<span class="hljs-keyword">let</span> checkNumber = curryingCheck(numberReg);
<span class="hljs-keyword">let</span> checkString = curryingCheck(stringReg);


<span class="hljs-built_in">console</span>.log(checkNumber(<span class="hljs-string">'13888888888'</span>)); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(checkString(<span class="hljs-string">'jsliang'</span>)); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">5.3 柯里化实现 <code>add(1)(2)(3)</code></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 实现一个 add 方法，使计算结果能够满足以下预期</span>
add(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>) = <span class="hljs-number">6</span>;
add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>)(<span class="hljs-number">4</span>) = <span class="hljs-number">10</span>;
add(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>)(<span class="hljs-number">4</span>)(<span class="hljs-number">5</span>) = <span class="hljs-number">15</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> numberList = <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">arguments</span>);

  <span class="hljs-comment">// 进一步收集剩余参数</span>
  <span class="hljs-keyword">const</span> calculate = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    numberList.push(...arguments);
    <span class="hljs-keyword">return</span> calculate;
  &#125;

  <span class="hljs-comment">// 利用 toString 隐式转换，最后执行时进行转换</span>
  calculate.toString = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> numberList.reduce(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a + b, <span class="hljs-number">0</span>);
  &#125;

  <span class="hljs-keyword">return</span> calculate;
&#125;

<span class="hljs-comment">// 实现一个 add 方法，使计算结果能够满足以下预期</span>
<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>)); <span class="hljs-comment">// 6</span>
<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>)(<span class="hljs-number">4</span>)); <span class="hljs-comment">// 10;</span>
<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>)(<span class="hljs-number">4</span>)(<span class="hljs-number">5</span>)); <span class="hljs-comment">// 15;</span>
<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>)(<span class="hljs-number">4</span>)(<span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>)); <span class="hljs-comment">// 28</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5.4 柯里化实现 compose(foo, bar, baz)('start')</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">...args</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(args[<span class="hljs-number">0</span>]);
  <span class="hljs-keyword">return</span> <span class="hljs-string">'foo'</span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params">...args</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(args[<span class="hljs-number">0</span>]);
  <span class="hljs-keyword">return</span> <span class="hljs-string">'bar'</span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baz</span>(<span class="hljs-params">...args</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(args[<span class="hljs-number">0</span>]);
  <span class="hljs-keyword">return</span> <span class="hljs-string">'baz'</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compose</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 闭包元素 - 函数列表</span>
  <span class="hljs-keyword">const</span> list = <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">arguments</span>);

  <span class="hljs-comment">// 闭包元素 - 函数列表执行位置</span>
  <span class="hljs-keyword">let</span> index = -<span class="hljs-number">1</span>;

  <span class="hljs-comment">// 闭包元素 - 上一个函数的返回</span>
  <span class="hljs-keyword">let</span> prev = <span class="hljs-string">''</span>;

  <span class="hljs-comment">// 返回闭包函数</span>
  <span class="hljs-keyword">const</span> doNext = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    index++; <span class="hljs-comment">// 索引值累加</span>
    <span class="hljs-comment">// 一开始没有上一个元素时，获取第二个括号的值</span>
    <span class="hljs-keyword">if</span> (!prev) &#123;
      prev = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>];
    &#125;
    <span class="hljs-comment">// 设置前一个结果为当前函数返回</span>
    prev = list[index](prev);
    <span class="hljs-comment">// 递归调用</span>
    <span class="hljs-keyword">if</span> (index < list.length - <span class="hljs-number">1</span>) &#123;
      doNext(index + <span class="hljs-number">1</span>);
    &#125;
  &#125;;

  <span class="hljs-comment">// 第一次返回闭包函数</span>
  <span class="hljs-keyword">return</span> doNext;
&#125;

compose(foo, bar, baz)(<span class="hljs-string">'start'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">相关好文</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F2975c25e4d71" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/2975c25e4d71" ref="nofollow noopener noreferrer">详解JS函数柯里化</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbeta.segmentfault.com%2Fq%2F1010000004342477%2Fa-1020000004344356" target="_blank" rel="nofollow noopener noreferrer" title="https://beta.segmentfault.com/q/1010000004342477/a-1020000004344356" ref="nofollow noopener noreferrer">编写add函数 然后 add(1)(2)(3)(4) 输出10 再考虑拓展性</a></li>
<li><a href="https://juejin.im/post/6844903769646317576" target="_blank" title="https://juejin.im/post/6844903769646317576">发现 JavaScript 中闭包的强大威力</a></li>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fblog.leapoahead.com%2F2015%2F09%2F15%2Fjs-closure%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://blog.leapoahead.com/2015/09/15/js-closure/" ref="nofollow noopener noreferrer">JavaScript闭包的底层运行机制</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F56490498" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/56490498" ref="nofollow noopener noreferrer">我从来不理解JavaScript闭包，直到有人这样向我解释它</a></li>
<li><a href="https://juejin.im/post/5c4e6a90e51d4552266576d2" target="_blank" title="https://juejin.im/post/5c4e6a90e51d4552266576d2">发现 JavaScript 中闭包的强大威力</a></li>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fblog.leapoahead.com%2F2015%2F09%2F15%2Fjs-closure%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://blog.leapoahead.com/2015/09/15/js-closure/" ref="nofollow noopener noreferrer">JavaScript闭包的底层运行机制</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F56490498" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/56490498" ref="nofollow noopener noreferrer">我从来不理解JavaScript闭包，直到有人这样向我解释它...</a></li>
<li><a href="https://juejin.im/post/6844903474212143117" target="_blank" title="https://juejin.im/post/6844903474212143117">破解前端面试（80% 应聘者不及格系列）：从闭包说起</a></li>
</ul></div>  
</div>
            