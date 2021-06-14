
---
title: '有趣的JavaScript：隐式类型转换规则整理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a5880680f0548c0b2cfdd9eec0d78f8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 07:39:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a5880680f0548c0b2cfdd9eec0d78f8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">JavaScript中的类型转换规则</h1>
<blockquote>
<p>这是我参与更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a5880680f0548c0b2cfdd9eec0d78f8~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出，JavaScript的隐式类型转换是很有意思的（让人摸不着头脑）</p>
<p>同时面试中页通常会遇到类型转换的考（ba）题（gu），比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 哪些为真?</span>
<span class="hljs-keyword">if</span>([])
<span class="hljs-keyword">if</span>(&#123;&#125;)
<span class="hljs-keyword">if</span>([]==<span class="hljs-literal">false</span>)
<span class="hljs-keyword">if</span>(&#123;&#125;==<span class="hljs-literal">false</span>)
<span class="hljs-keyword">if</span>([] == ![])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果看着这题摸不着头脑，大伙儿可以接着往下看</p>
<p>本文<strong>较完整</strong>的梳理一下常见的类型<code>转换规则</code>与<code>转换场景</code></p>
<p><strong>一点说明：</strong> 文中的值类型等价于所说的基础类型，其范围是（boolean,string,number）</p>
<h2 data-id="heading-1">向基础类型转换</h2>
<h3 data-id="heading-2">布尔Boolean</h3>
<h4 data-id="heading-3">转换为<code>boolean</code>的方式</h4>
<p>常用的两种</p>
<ul>
<li><code>!!value</code>：取反两次</li>
<li><code>Boolean(value)</code>：用Boolean包裹</li>
</ul>
<h4 data-id="heading-4">转换为假（false）</h4>
<ul>
<li><code>undefined</code>， <code>null</code>，<code>NaN</code>，<code>''</code>， <code>0</code> --> false</li>
</ul>
<details>
<summary>
点击查看示例代码
</summary>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(!!<span class="hljs-literal">undefined</span>);
<span class="hljs-built_in">console</span>.log(!!<span class="hljs-literal">null</span>);
<span class="hljs-built_in">console</span>.log(!!<span class="hljs-literal">NaN</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Boolean</span>(<span class="hljs-string">''</span>));
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Boolean</span>(<span class="hljs-number">0</span>)); 
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h4 data-id="heading-5">转换为真（true）</h4>
<ul>
<li>除上述值外的<code>其它值类型</code>与<code>对象</code>都转为 --> true</li>
</ul>
<details>
<summary>
点击查看示例代码
</summary>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(!!&#123;&#125;);
<span class="hljs-built_in">console</span>.log(!![]);
<span class="hljs-built_in">console</span>.log(!!<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>());
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Boolean</span>(<span class="hljs-number">1</span>));
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Boolean</span>(<span class="hljs-string">'123'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h3 data-id="heading-6">数字Number</h3>
<h4 data-id="heading-7">转换为<code>number</code>的方式</h4>
<p>常用的两种</p>
<ul>
<li><code>+value</code>：以<code>+</code>开头</li>
<li><code>Number(value)</code>：用Number包裹</li>
</ul>
<h4 data-id="heading-8">数组转数字</h4>
<p>Array => Number</p>
<ul>
<li>空数组转为0: <code>[]</code> --> 0</li>
<li>含有一个元素且为<code>数字</code>或<code>数字字符串</code>则转换为数字：<code>[1]</code>或<code>['1']</code> --> 1</li>
<li>其余情况转为<code>NaN</code></li>
</ul>
<details>
<summary>
点击查看示例代码
</summary>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(+[]); <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(+[<span class="hljs-number">1</span>]); <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>([<span class="hljs-string">'1.23'</span>])); <span class="hljs-comment">// 1.23</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>])); <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>([<span class="hljs-string">'1'</span>,<span class="hljs-number">2</span>])); <span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h4 data-id="heading-9">值类型转数字</h4>
<ul>
<li><code>null</code> --> 0</li>
<li><code>'123'</code> --> 123: 纯数字构成的字符串直接转换为应的数字</li>
<li><code>true</code> --> 1</li>
<li><code>false</code> --> 0</li>
<li><code>'124a'</code> --> NaN</li>
<li><code>undefined</code> --> NaN</li>
<li><code>Symbol</code> --> <strong>抛出错误</strong></li>
</ul>
<details>
<summary>
点击查看示例代码
</summary>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(+<span class="hljs-literal">null</span>); <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(+<span class="hljs-literal">undefined</span>); <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">console</span>.log(+<span class="hljs-string">'123'</span>); <span class="hljs-comment">// 123</span>
<span class="hljs-built_in">console</span>.log(+<span class="hljs-string">'true'</span>); <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">console</span>.log(+<span class="hljs-literal">true</span>); <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(+<span class="hljs-literal">false</span>);<span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h4 data-id="heading-10">引用类型转数字</h4>
<p>除了上述的<code>数组</code>,<code>日期(Date)</code>之外的引用类型(<code>Object</code>)都转为<code>NaN</code></p>
<details>
<summary>
点击查看示例代码
</summary>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(+ <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()); <span class="hljs-comment">// 1623597270652</span>
<span class="hljs-built_in">console</span>.log(+ [<span class="hljs-number">1</span>]); <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(+ &#123;&#125;); <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">console</span>.log(+ <span class="hljs-regexp">/\d/</span>); <span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h3 data-id="heading-11">字符串String</h3>
<h4 data-id="heading-12">转字符串的方式</h4>
<ul>
<li>加空字符串:<code>’’ + value</code></li>
<li>String(value)：用<code>String</code>包裹</li>
</ul>
<h4 data-id="heading-13">值类型转字符串</h4>
<ul>
<li>数字直接转
<ul>
<li><code>666</code> --> '666':</li>
</ul>
</li>
<li>布尔值直接转换
<ul>
<li><code>true</code> --> 'true'</li>
<li><code>false</code> --> 'false'</li>
</ul>
</li>
</ul>
<details>
<summary>
点击查看示例代码
</summary>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">''</span>+<span class="hljs-literal">true</span>); <span class="hljs-comment">// 'true'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">''</span>+<span class="hljs-literal">false</span>); <span class="hljs-comment">// 'false'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">String</span>(<span class="hljs-number">666</span>)); <span class="hljs-comment">// '666'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h4 data-id="heading-14">引用类型转数字</h4>
<ul>
<li>数组
<ul>
<li><code>[]</code> --> '' ：空数组转为空串</li>
<li><code>[2,'3']</code> --> '2,3' ：非空数组的每一项转为字符串再用<code>,</code>分割</li>
</ul>
</li>
<li>对象:
<ul>
<li>&#123;&#125; --> [object Object]</li>
<li>&#123;a:1&#125; --> [object Object]</li>
</ul>
</li>
</ul>
<details>
<summary>
点击查看示例代码
</summary>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">String</span>([])); <span class="hljs-comment">// ''</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">String</span>([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-string">'3'</span>])); <span class="hljs-comment">// '1,2,3'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">String</span>(&#123;&#125;)); <span class="hljs-comment">// '[object Object]'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">String</span>(&#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>&#125;)); <span class="hljs-comment">// '[object Object]'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h2 data-id="heading-15">对象转基础类型规则</h2>
<p>对象在转换类型的时候，会调用内置的 <code>[[ToPrimitive]]</code> 函数，对于该函数来说，逻辑一般来说如下：</p>
<ol>
<li>如果已经是基础类型了，那就不需要转换了</li>
<li>目标类型为<strong>字符串</strong>就先调用 toString
<ul>
<li>转换为基础类型的话就返回转换的值</li>
</ul>
</li>
<li>目标类型不为<strong>字符串</strong>就先调用 valueOf
<ul>
<li>结果为基础类型，就返回转换的值</li>
<li>结果不是基础类型的话再调用 toString</li>
</ul>
</li>
<li>如果都没有返回基础类型，就会报错</li>
</ol>
<p>各种情况示例如下：</p>
<details>
<summary>
点击查看示例代码
</summary>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> demo1 = &#123;
    [<span class="hljs-built_in">Symbol</span>.toPrimitive]: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>
    &#125;
&#125;
<span class="hljs-comment">// 情况1</span>
<span class="hljs-built_in">console</span>.log(demo1 + <span class="hljs-number">1</span>); <span class="hljs-comment">// 3</span>

<span class="hljs-keyword">const</span> demo2 = &#123;
    <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'demo2'</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">valueOf</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">20</span>
    &#125;
&#125;
<span class="hljs-comment">// 情况2</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">String</span>(demo2)) <span class="hljs-comment">// demo2</span>

<span class="hljs-comment">// 情况3-1</span>
<span class="hljs-built_in">console</span>.log(demo2 - <span class="hljs-number">3</span>); <span class="hljs-comment">// 17</span>

<span class="hljs-keyword">const</span> demo3 = &#123;
    <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">30</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">valueOf</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;&#125;
    &#125;
&#125;
<span class="hljs-comment">// 情况3-2</span>
<span class="hljs-built_in">console</span>.log(demo3 - <span class="hljs-number">4</span>); <span class="hljs-comment">// 26</span>

<span class="hljs-keyword">const</span> demo4 = &#123;
    <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;&#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">valueOf</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;&#125;
    &#125;
&#125;
<span class="hljs-comment">// 情况4</span>
<span class="hljs-built_in">console</span>.log(demo4 + <span class="hljs-number">1</span>); <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h2 data-id="heading-16">四则运算规则中的类型转换</h2>
<h3 data-id="heading-17">加法</h3>
<ul>
<li>有一方为<code>String</code>，那么另一方也会被转为<code>String</code></li>
<li>一方为<code>Number</code>,另一方为原始值类型，则将原始值类型转换为<code>Number</code></li>
<li>一方为<code>Number</code>,另一方为引用类型，双方都转为<code>String</code></li>
</ul>
<details>
<summary>
点击查看示例代码
</summary>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">'123'</span> + <span class="hljs-number">4</span> <span class="hljs-comment">// '1234'</span>

<span class="hljs-number">123</span> + <span class="hljs-literal">true</span> <span class="hljs-comment">// 124</span>
<span class="hljs-number">123</span> + <span class="hljs-literal">undefined</span> <span class="hljs-comment">// NaN</span>
<span class="hljs-number">123</span> + <span class="hljs-literal">null</span> <span class="hljs-comment">// 123</span>

<span class="hljs-number">123</span> + [] <span class="hljs-comment">//  '123'</span>
<span class="hljs-number">123</span> + &#123;&#125; <span class="hljs-comment">// '123[object Object]'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h3 data-id="heading-18">其它</h3>
<p>除了加法的运算符来说（-，*，/），会将非<code>Number</code>类型转换为<code>Number</code>类型</p>
<h2 data-id="heading-19">== 中的类型转换</h2>
<ol>
<li><code>NaN</code>不等于任何其它类型</li>
<li><code>Boolean</code> 与其它类型进行比较,<code>Boolean</code>转换为<code>Number</code></li>
<li><code>String</code> 与 <code>Number</code>进行比较,<code>String</code> 转化为<code>Number</code></li>
<li><code>null</code> 与 <code>undefined</code>进行比较结果为true</li>
<li><code>null</code>,<code>undefined</code>与其它任何类型进行比较结果都为false</li>
<li><code>引用类型</code>与<code>值类型</code>进行比较,引用类型先转换为<code>值类型</code>(调用[ToPrimitive])</li>
<li><code>引用类型</code>与<code>引用类型</code>，直接判断是否指向同一对象</li>
</ol>
<blockquote>
<p>来源于参考资料中的网图</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f78979cc54834a67b788929389116835~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<details>
<summary>
点击查看示例代码
</summary>
<pre><code class="hljs language-js copyable" lang="js">[]==![] <span class="hljs-comment">// true</span>
<span class="hljs-comment">// [] == false  1. 根据运算符优先级 ![] --> false</span>
<span class="hljs-comment">// [] == 0      2. 上面规则2</span>
<span class="hljs-comment">// '' == 0      3. 上面规则6</span>
<span class="hljs-comment">//  0 == 0      4. 上面规则3</span>
<span class="hljs-comment">// 所以结果为true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h2 data-id="heading-20">自测</h2>
<details>
<summary>
点击查看自测代码
</summary>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> ([]) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);             
<span class="hljs-keyword">if</span> (&#123;&#125;) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);             
<span class="hljs-keyword">if</span> ([] == <span class="hljs-literal">false</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);    
<span class="hljs-keyword">if</span> (&#123;&#125; == <span class="hljs-literal">false</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">4</span>);    
<span class="hljs-keyword">if</span> ([] == ![]) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>);      
<span class="hljs-keyword">if</span> (&#123;&#125; == !&#123;&#125;) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">6</span>);      
<span class="hljs-keyword">if</span> (<span class="hljs-string">''</span> == <span class="hljs-literal">false</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">7</span>);    
<span class="hljs-keyword">if</span> (<span class="hljs-literal">false</span> == <span class="hljs-number">0</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">8</span>);     
<span class="hljs-keyword">if</span> (<span class="hljs-number">1</span> == <span class="hljs-literal">true</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">9</span>);      
<span class="hljs-keyword">if</span> (<span class="hljs-string">''</span> == <span class="hljs-number">0</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>);       
<span class="hljs-keyword">if</span> (<span class="hljs-literal">NaN</span> == <span class="hljs-literal">NaN</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">11</span>);    
<span class="hljs-keyword">if</span> ([] == !<span class="hljs-literal">true</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">12</span>);   
<span class="hljs-keyword">if</span> ([] == <span class="hljs-literal">false</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">13</span>);   
<span class="hljs-keyword">if</span> ([] == <span class="hljs-number">0</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">14</span>);       
<span class="hljs-keyword">if</span> (+<span class="hljs-number">0</span> == -<span class="hljs-number">0</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">15</span>);      
<span class="hljs-keyword">if</span> (<span class="hljs-literal">NaN</span> == <span class="hljs-literal">false</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-number">16</span>);  
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">&#123; &#125; +<span class="hljs-number">1</span>              
<span class="hljs-number">1</span> + &#123;&#125;              
[] + <span class="hljs-number">1</span>              
<span class="hljs-number">1</span> + []              
[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>] + <span class="hljs-number">0</span>       
[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>] + <span class="hljs-string">'0'</span>     
<span class="hljs-number">1</span> + <span class="hljs-string">'0'</span>             
<span class="hljs-number">1</span> + <span class="hljs-number">0</span>               
<span class="hljs-number">1</span> + <span class="hljs-literal">true</span>            
<span class="hljs-number">1</span> + <span class="hljs-literal">false</span>           
<span class="hljs-string">'1'</span> + <span class="hljs-literal">true</span>          
<span class="hljs-string">'1'</span> + <span class="hljs-literal">false</span>         
![] + []            
<span class="hljs-number">1</span> - <span class="hljs-literal">true</span>            
<span class="hljs-string">'0'</span> - <span class="hljs-number">0</span>             
<span class="hljs-number">0</span> - <span class="hljs-string">'1'</span>             
<span class="hljs-literal">false</span> - <span class="hljs-literal">true</span>        
&#123; &#125; -[]             
[] - &#123;&#125;             
<span class="hljs-literal">false</span> - []          
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h2 data-id="heading-21">TODO</h2>
<ul>
<li>补图：用图概括文章内容</li>
</ul>
<h2 data-id="heading-22">参考</h2>
<ul>
<li><a href="https://segmentfault.com/a/1190000008594792" target="_blank" rel="nofollow noopener noreferrer">思否-前端碎碎念 之 为什么[] == ![] ?</a></li>
<li><a href="https://juejin.cn/post/6973302910172004366">freeCodeCamp-Javascript 隐式类型转换，一篇就够了</a></li>
</ul></div>  
</div>
            