
---
title: 'JavaScript 系列之字符串（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bd02e2b1577429cbb9f21adc1c77d13~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 18:06:30 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bd02e2b1577429cbb9f21adc1c77d13~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第23天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bd02e2b1577429cbb9f21adc1c77d13~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、查找判断</h2>
<h3 data-id="heading-1">1.1 charAt</h3>
<blockquote>
<p><code>charAt()</code> 方法从一个字符串中返回指定的字符。</p>
<p><code>str.charAt(index)</code></p>
</blockquote>
<ul>
<li><code>@params</code>：一个介于 0 和字符串长度减1之间的整数。 (0~length-1)，默认 0。</li>
<li><code>@return</code>：字符</li>
<li><code>是否改变原字符串</code>：不改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> str = <span class="hljs-string">'hello'</span>;
<span class="hljs-built_in">console</span>.log(str.charAt(<span class="hljs-number">2</span>));  <span class="hljs-comment">// 'e'</span>
<span class="hljs-built_in">console</span>.log(str.charAt(<span class="hljs-number">5</span>));  <span class="hljs-comment">// ''</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.2 charCodeAt</h3>
<blockquote>
<p><code>charCodeAt()</code> 方法返回 0 到 65535 之间的整数，表示给定索引处的 <code>UTF-16</code> 代码单元。</p>
<p><code>str.charCodeAt(index)</code></p>
</blockquote>
<ul>
<li><code>@params</code>：一个大于等于 0，小于字符串长度的整数。如果不是一个数值，则默认为 0。</li>
<li><code>@return</code>：指定 index 处字符的 UTF-16 代码单元值的一个数字；如果 index 超出范围，charCodeAt() 返回 NaN。</li>
<li><code>是否改变原字符串</code>：不改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> str = <span class="hljs-string">'hello'</span>;
<span class="hljs-built_in">console</span>.log(str.charCodeAt(<span class="hljs-number">2</span>));  <span class="hljs-comment">// 108</span>
<span class="hljs-built_in">console</span>.log(str.charCodeAt(<span class="hljs-number">5</span>));  <span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.3 indexOf</h3>
<blockquote>
<p><code>indexOf()</code> 方法返回调用它的 String 对象中第一次出现的指定值的索引，从 fromIndex 处进行搜索。如果未找到该值，则返回 -1。</p>
<p><code>str.indexOf(searchValue [, fromIndex])</code></p>
</blockquote>
<ul>
<li><code>@params</code>：
<ul>
<li>searchValue：是要被查找的字符串值；</li>
<li>fromIndex：表示开始查找的位置。可以是任意整数，默认值为 0。</li>
</ul>
</li>
<li><code>@return</code>：查找的字符串 searchValue 的第一次出现的索引，如果没有找到，则返回 -1。</li>
<li><code>是否改变原字符串</code>：不改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Blue Whale'</span>.indexOf(<span class="hljs-string">'Blue'</span>))   <span class="hljs-comment">// 返回 0</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Blue Whale'</span>.indexOf(<span class="hljs-string">'Blute'</span>))   <span class="hljs-comment">// 返回 -1</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Blue Whale'</span>.indexOf(<span class="hljs-string">'Whale'</span>, <span class="hljs-number">0</span>))   <span class="hljs-comment">// 返回 5</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Blue Whale'</span>.indexOf(<span class="hljs-string">'Whale'</span>, <span class="hljs-number">5</span>))   <span class="hljs-comment">// 返回 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.4 lastIndexOf</h3>
<blockquote>
<p><code>lastIndexOf()</code> 方法返回调用 String 对象的指定值最后一次出现的索引，在一个字符串中的指定位置 fromIndex处从后向前搜索。如果没找到这个特定值则返回-1 。</p>
<p><code>str.lastIndexOf(searchValue[, fromIndex])</code></p>
</blockquote>
<ul>
<li><code>@params</code>：
<ul>
<li>searchValue：是一个字符串，表示被查找的值。如果 searchValue 是空字符串，则返回 fromIndex。；</li>
<li>fromIndex：可选，待匹配字符串 searchValue 的开头一位字符从 str 的第 fromIndex 位开始向左回向查找。</li>
</ul>
</li>
<li><code>@return</code>：返回指定值最后一次出现的索引(该索引仍是以从左至右0开始记数的)，如果没找到则返回 -1。</li>
<li><code>是否改变原字符串</code>：不改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> str = <span class="hljs-string">'Brave new world'</span>;
<span class="hljs-built_in">console</span>.log(str.lastIndexOf(<span class="hljs-string">'w'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.5 startsWith</h3>
<blockquote>
<p><code>startsWith()</code> 方法用来判断当前字符串是否以另外一个给定的子字符串开头，并根据判断结果返回 true 或 false。</p>
<p><code>str.startsWith(searchString[, position])</code></p>
</blockquote>
<ul>
<li><code>@params</code>：
<ul>
<li>searchString：表示要搜索的子字符串；</li>
<li>position：可选，表示在 str 中搜索 searchString 的开始位置，默认值为 0。</li>
</ul>
</li>
<li><code>@return</code>：如果在字符串的开头找到了给定的字符则返回 true；否则返回 false。</li>
<li><code>是否改变原字符串</code>：不改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> str = <span class="hljs-string">'Saturday night plans'</span>;
<span class="hljs-built_in">console</span>.log(str.startsWith(<span class="hljs-string">'Sat'</span>));  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(str.startsWith(<span class="hljs-string">'Sat'</span>, <span class="hljs-number">3</span>));  <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">1.6 endsWith</h3>
<blockquote>
<p><code>endsWith()</code> 方法用来判断当前字符串是否是以另外一个给定的子字符串“结尾”的，根据判断结果返回 true 或 false。</p>
<p><code>str.endsWith(searchString[, length])</code></p>
</blockquote>
<ul>
<li><code>@params</code>：
<ul>
<li>searchString：表示要搜索的子字符串；</li>
<li>length：可选，是 str 的长度。默认值为 str.length。</li>
</ul>
</li>
<li><code>@return</code>：如果传入的子字符串在搜索字符串的末尾则返回 true，否则将返回 false。</li>
<li><code>是否改变原字符串</code>：不改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> str = <span class="hljs-string">'To be, or not to be, that is the question.'</span>;

<span class="hljs-built_in">console</span>.log(str.endsWith(<span class="hljs-string">'question.'</span>));  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(str.endsWith(<span class="hljs-string">'to be'</span>));      <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(str.endsWith(<span class="hljs-string">'to be'</span>, <span class="hljs-number">19</span>));  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">1.7 includes</h3>
<blockquote>
<p><code>includes()</code> 方法用于判断一个字符串是否包含在另一个字符串中，根据情况返回 true 或 false。</p>
<p><code>str.includes(searchString[, position])</code></p>
</blockquote>
<ul>
<li><code>@params</code>：
<ul>
<li>searchString：表示要在此字符串中搜索的字符串</li>
<li>position：可选，表示从当前字符串的哪个索引位置开始搜寻子字符串，默认值为 0。</li>
</ul>
</li>
<li><code>@return</code>：如果当前字符串包含被搜寻的字符串，就返回 true；否则返回 false。</li>
<li><code>是否改变原字符串</code>：不改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> str = <span class="hljs-string">'To be, or not to be, that is the question.'</span>;

<span class="hljs-built_in">console</span>.log(str.includes(<span class="hljs-string">'To be'</span>));       <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(str.includes(<span class="hljs-string">'question'</span>));    <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(str.includes(<span class="hljs-string">'nonexistent'</span>)); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(str.includes(<span class="hljs-string">'To be'</span>, <span class="hljs-number">1</span>));    <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(str.includes(<span class="hljs-string">'TO BE'</span>));       <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">1.8 localeCompare</h3>
<blockquote>
<p><code>localeCompare()</code> 方法返回一个数字来指示一个参考字符串是否在排序顺序前面或之后或与给定字符串相同。</p>
<p><code>referenceStr.localeCompare(compareString[, locales[, options]])</code></p>
</blockquote>
<ul>
<li><code>@params</code>：
<ul>
<li>compareString：表示用来比较的字符串；</li>
<li>locales：可选，用来表示一种或多种语言或区域的一个符合 BCP 47 标准的字符串或一个字符串数组。</li>
<li>options：可选。</li>
</ul>
</li>
<li><code>@return</code>：如果引用字符存在于比较字符之前则为负数; 如果引用字符存在于比较字符之后则为正数; 相等的时候返回 0。</li>
<li><code>是否改变原字符串</code>：不改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>.localeCompare(<span class="hljs-string">'c'</span>));  <span class="hljs-comment">// -1 </span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'check'</span>.localeCompare(<span class="hljs-string">'against'</span>));  <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>.localeCompare(<span class="hljs-string">'a'</span>));  <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            