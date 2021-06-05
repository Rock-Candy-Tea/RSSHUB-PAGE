
---
title: '【青山学js】js基础数据类型之Number（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=792'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 06:34:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=792'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与更文挑战的第5天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">关于Number</h2>
<p>Number类型也是JavaScript的基本数据类型之一，同时也是最有意思的一种数据类型。下面我们就一起来了解一下它吧</p>
<h2 data-id="heading-1">数值字面量</h2>
<h3 data-id="heading-2">整数</h3>
<p>整数字面量写法是区分进制的，整数可以被表示成十进制（基数为10）、八进制（基数为8）以及十六进制（基数为16）</p>
<h4 data-id="heading-3">八进制</h4>
<p>对于八进制字面量，书写时候必须以0开头，然后是相应的八进制数字（数值0-7）。如果字面量中包含的数字超出了应有的范围，就会忽略了前缀的0，后面的数被当成十进制。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num1 = <span class="hljs-number">070</span> <span class="hljs-comment">// 八进制的56</span>
<span class="hljs-keyword">let</span> num2 = <span class="hljs-number">079</span> <span class="hljs-comment">// 9 >= 8 无效的八进制值，忽略0，当成79处理</span>
<span class="hljs-keyword">let</span> num3 = <span class="hljs-number">08</span> <span class="hljs-comment">// 8 >= 8 无效的八进制值，忽略0，当成8处理</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意，ECMAScript 2015或ES6中的八进制值通过前缀0o来表示;严格模式下，前缀0会被视为语法错误，如果要表示八进制值，应该使用前缀0o。</p>
</blockquote>
<h4 data-id="heading-4">十进制</h4>
<p>十进制是最基本的数值字面量格式，也是我们最常见到的实质字面量，可以直接在代码中输入</p>
<h4 data-id="heading-5">十六进制</h4>
<p>对于十六进制字面量，书写时候必须以0x开头，然后是相应的十六进制数字（0-7级A-F）。十六进制中的字母大小写均可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num1 = <span class="hljs-number">0xA</span> <span class="hljs-comment">// 10</span>
<span class="hljs-keyword">let</span> num2 = <span class="hljs-number">0x1f</span> <span class="hljs-comment">// 31</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">浮点数</h3>
<p>浮点数就是数学概念中的小数，有整数、小数点、小数部分组成，其中整数部分如果为0可以省略（但不推荐），小数点和小数部分必须有，因为小数会比整数更占用内存，所以js会在符合条件的情况下尽量将小数转为整数，比如小数点后面无值或者小数点后面的数字都为0，那这个数字将被转换为一个整数（因为小数）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> floatNum1 = <span class="hljs-number">1.1</span> <span class="hljs-comment">// 有效</span>
<span class="hljs-keyword">let</span> floatNum2 = <span class="hljs-number">0.1</span> <span class="hljs-comment">// 有效</span>
<span class="hljs-keyword">let</span> floatNum3 = <span class="hljs-number">.1</span>  <span class="hljs-comment">// 有效但不推荐</span>
<span class="hljs-keyword">let</span> floatNum4 = <span class="hljs-number">2.0</span> <span class="hljs-comment">// 会被转为整数 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于太大或太小的数，浮点值可以用科学计数法表示</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> floatNum1 = <span class="hljs-number">3.125e7</span> <span class="hljs-comment">// 等于31250000</span>
<span class="hljs-keyword">let</span> floatNum2 = <span class="hljs-number">3e-7</span> <span class="hljs-comment">// 等于0.0000003</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下，如果一个小数数的小数点后面有6个以上的0时，这个小数会自动被转换为科学计数法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> floatNum1 = <span class="hljs-number">0.000000003</span> <span class="hljs-comment">// 3e-9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浮点数的精确度最高可达17位小数。还有一个经典的问题，在js中，小数的操作时存在精度问题的，例如</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">0.1</span> + <span class="hljs-number">0.2</span>);<span class="hljs-comment">//0.30000000000000004</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1.0</span> - <span class="hljs-number">0.9</span>);<span class="hljs-comment">//0.09999999999999998</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">19.9</span> * <span class="hljs-number">100</span>);<span class="hljs-comment">//1989.9999999999998</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">6.6</span> / <span class="hljs-number">0.2</span>);<span class="hljs-comment">//32.99999999999999</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>感兴趣的朋友可以自己去搜索一下相关的解决方案</p>
<h3 data-id="heading-7">Infinity 无穷</h3>
<p>由于在js重，每个数值都是占用内存的，而js内存是有限的，所以js并不支持这个世界上所有的数，js中支持的最大数值为1.7976931348623157e+308，可以用<code>Number.MAX_VALUE</code> 获取，如果目标数值比这个数值大，则会被自动转化为 无穷大<code>Infinity</code>，js中支持的最小的数为5e-324，可以用 <code>Number.MIN_VALUE</code>获取，如果目标值比这个值小，则会被转化为 无穷小 <code>-Infinity</code></p></div>  
</div>
            