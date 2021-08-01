
---
title: 'JavaScript 系列之类型（一）｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3515'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 00:09:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=3515'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">一、内置类型</h2>
<h2 data-id="heading-1">1.1 基本类型</h2>
<ul>
<li>Boolean</li>
<li>String</li>
<li>Number</li>
<li>Null</li>
<li>Undefined</li>
<li>Symbol（ES6 新定义）</li>
</ul>
<h2 data-id="heading-2">1.2 引用类型</h2>
<ul>
<li>Object
<ul>
<li>Function</li>
<li>Date</li>
<li>Array</li>
<li>等等</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">b</span>: [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>],
&#125;;
<span class="hljs-keyword">let</span> aa = obj.a;
<span class="hljs-keyword">let</span> bb = obj.b;
aa = <span class="hljs-number">2</span>;
bb.push(<span class="hljs-number">4</span>);
<span class="hljs-built_in">console</span>.log(obj);
<span class="hljs-built_in">console</span>.log(aa);
<span class="hljs-built_in">console</span>.log(bb);

<span class="hljs-comment">// &#123;a: 1, b: [1, 2, 3, 4]&#125;</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// [1, 2, 3, 4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然 obj 本身是个引用类型的变量（对象），但是内部的 a 和 b 一个是<strong>值类型</strong>一个是<strong>引用类型</strong>，aa 的赋值不会改变 obj.a，但是 bb 的操作却会反映到 obj 对象上。</p>
<p>JS 中这种设计的原因是：按值传递的类型，复制一份存入栈内存，这类类型一般不占用太多内存，而且按值传递保证了其访问速度。按共享传递的类型，是复制其引用，而不是整个复制其值（C 语言中的指针），保证过大的对象等不会因为不停复制内容而造成内存的浪费。</p>
<h2 data-id="heading-3">二、类型转换</h2>
<h3 data-id="heading-4">2.1 转 Boolean</h3>
<p>在条件判断时，除了 <code>undefined</code>， <code>null</code>， <code>false</code>， <code>NaN</code>， <code>''</code>， <code>0</code>， <code>-0</code> 会转为  <code>false</code>，其他所有值都转为 <code>true</code>，包括所有对象。</p>
<h3 data-id="heading-5">2.2 对象转基本类型</h3>
<p>对象在转换基本类型时，首先会检查有无设置  <code>Symbol.toPrimitive</code>（该方法优先级最高），然后调用 <code>valueOf</code>，然后调用 <code>toString</code>。三个方法都可以重写。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = &#123;
  <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'1'</span>;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">valueOf</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
  &#125;,
  [<span class="hljs-built_in">Symbol</span>.toPrimitive]() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>;
  &#125;
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> + a) <span class="hljs-comment">// => 3</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span> + a) <span class="hljs-comment">// => '12'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.3 四则运算</h3>
<ul>
<li><code>-、*、/、%</code> ：一律转换成数值后计算</li>
<li><code>+</code>：
<ul>
<li><code>数字 + 字符串 = 字符串</code>， 运算顺序是从左到右</li>
<li><code>数字 + 对象</code>， 优先调用对象的 <code>valueOf -> toString</code></li>
<li><code>数字 + boolean/null -> 数字</code></li>
<li><code>数字 + undefined -> NaN</code></li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span> + <span class="hljs-string">'1'</span> <span class="hljs-comment">// '11'</span>
<span class="hljs-number">2</span> * <span class="hljs-string">'2'</span> <span class="hljs-comment">// 4</span>

[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>] + [<span class="hljs-number">2</span>, <span class="hljs-number">1</span>] <span class="hljs-comment">// '1,22,1'</span>
<span class="hljs-comment">// [1, 2].toString() -> '1,2'</span>
<span class="hljs-comment">// [2, 1].toString() -> '2,1'</span>
<span class="hljs-comment">// '1,2' + '2,1' = '1,22,1'</span>

<span class="hljs-string">'a'</span> + + <span class="hljs-string">'b'</span> <span class="hljs-comment">// -> "aNaN"</span>
<span class="hljs-comment">// 因为 + 'b' -> NaN</span>
<span class="hljs-comment">// 你也许在一些代码中看到过 + '1' -> 1</span>

+<span class="hljs-literal">undefined</span> <span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2.4 相等（==）</h3>
<blockquote>
<p>相等和不相等 —— <strong>先转换再比较</strong></p>
</blockquote>
<p>规则：</p>
<ol>
<li>一个是布尔，比较之前<strong>先转换成数值</strong> —— <code>false</code>转 <code>0</code>，<code>true</code> 转 <code>1</code>。</li>
<li>一个是字符串，一个是数值 ，比较之前<strong>先将字符串转成数值</strong>。</li>
<li>一个是对象，另一个不是，则调用对象的 <code>valueof</code> 方法，用得到的基本类型值按照前面的规则进行比较。</li>
</ol>
<p>比较时遵循：</p>
<ol>
<li><code>null</code> 和 <code>undefined</code> 相等。</li>
<li>一个是 <code>NaN</code>，另一个无论是什么，相等操作符都返回 <code>false</code>；繁殖不相等操作符则返回 <code>true</code>。</li>
<li>两个都是对象，则比较是否是同一个对象。如果两个操作数<strong>指向同一个对象，即指向同一个引用</strong>，则相等操作符返回 <code>true</code>。否则返回 <code>false</code>。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-literal">null</span>==<span class="hljs-literal">undefined</span> <span class="hljs-comment">//true</span>
<span class="hljs-string">"NaN"</span>==<span class="hljs-literal">NaN</span> <span class="hljs-comment">//false</span>
<span class="hljs-number">5</span>==<span class="hljs-literal">NaN</span> <span class="hljs-comment">//false</span>
<span class="hljs-literal">NaN</span>==<span class="hljs-literal">NaN</span> <span class="hljs-comment">//false</span>
<span class="hljs-literal">NaN</span>!=<span class="hljs-literal">NaN</span> <span class="hljs-comment">//true</span>
<span class="hljs-literal">false</span>==<span class="hljs-number">0</span> <span class="hljs-comment">//true</span>
<span class="hljs-literal">true</span>==<span class="hljs-number">1</span> <span class="hljs-comment">//true</span>
<span class="hljs-literal">true</span>==<span class="hljs-number">2</span> <span class="hljs-comment">//false</span>
<span class="hljs-literal">undefined</span>==<span class="hljs-number">0</span> <span class="hljs-comment">//false</span>
<span class="hljs-literal">null</span>==<span class="hljs-number">0</span> <span class="hljs-comment">//false</span>
<span class="hljs-string">"5"</span>==<span class="hljs-number">5</span> <span class="hljs-comment">//true</span>

<span class="hljs-keyword">let</span> a = &#123; <span class="hljs-attr">c</span>: <span class="hljs-number">1</span> &#125;
<span class="hljs-keyword">let</span> b = &#123; <span class="hljs-attr">c</span>: <span class="hljs-number">1</span> &#125;
<span class="hljs-built_in">console</span>.log(a == b) <span class="hljs-comment">// false</span>

<span class="hljs-keyword">let</span> d = b
<span class="hljs-built_in">console</span>.log(d == b) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2.5 全等（===）</h3>
<blockquote>
<p>全等和不全等——<strong>仅比较而不转换</strong>（除了在比较之前不转换操作数外，全等和不全等与相等和不相等没有什么区别）</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"55"</span>===<span class="hljs-number">55</span> <span class="hljs-comment">//false</span>
<span class="hljs-literal">null</span>===<span class="hljs-literal">undefined</span> <span class="hljs-comment">//false</span>
<span class="hljs-literal">NaN</span>===<span class="hljs-literal">NaN</span> <span class="hljs-comment">//false</span>
<span class="hljs-literal">undefined</span>===<span class="hljs-literal">undefined</span> <span class="hljs-comment">//true</span>
<span class="hljs-literal">null</span>===<span class="hljs-literal">null</span> <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            