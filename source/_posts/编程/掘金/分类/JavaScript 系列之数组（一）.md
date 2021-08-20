
---
title: 'JavaScript 系列之数组（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6189b377c2594a50be213b70340ce83c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 17:05:07 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6189b377c2594a50be213b70340ce83c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6189b377c2594a50be213b70340ce83c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、增删查改</h2>
<h3 data-id="heading-1">1.1 push</h3>
<blockquote>
<p><code>push()</code> 方法将一个或多个元素添加到数组的末尾，并返回新数组的长度。</p>
<p><code>arr.push(element1, ..., elementN)</code></p>
</blockquote>
<ul>
<li><code>@params</code>：数组要新增的元素（任意数据类型，一次可添加多个，用逗号隔开）</li>
<li><code>@return</code>：返回数组新增元素后的长度</li>
<li><code>是否改变原数组</code>：改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> res = arr.push(<span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>);    
<span class="hljs-built_in">console</span>.log(res);   <span class="hljs-comment">// res = 6</span>
<span class="hljs-built_in">console</span>.log(arr);   <span class="hljs-comment">// [1,2,3,6,7,8]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.2 unshift</h3>
<blockquote>
<p><code>unshift()</code> 方法将一个或多个元素添加到数组的开头，并返回该数组的新长度。此方法更改数组的长度。</p>
<p><code>arr.unshift(element1, ..., elementN)</code></p>
</blockquote>
<ul>
<li><code>@params</code>：数组要新增的元素（任意数据类型，一次可添加多个，用逗号隔开）</li>
<li><code>@return</code>：返回数组新增元素后的长度</li>
<li><code>是否改变原数组</code>：改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> res = arr.unshift(<span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>);    

<span class="hljs-built_in">console</span>.log(res);  <span class="hljs-comment">// res = 6</span>
<span class="hljs-built_in">console</span>.log(arr);  <span class="hljs-comment">// [6,7,8,1,2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.3 pop</h3>
<blockquote>
<p><code>pop()</code> 方法从数组中删除最后一个元素，并返回该元素的值。此方法更改数组的长度。</p>
<p><code>arr.pop()</code></p>
</blockquote>
<ul>
<li><code>@params</code>：无</li>
<li><code>@return</code>：返回数组被删除的元素</li>
<li><code>是否改变原数组</code>：改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> res = arr.pop();    

<span class="hljs-built_in">console</span>.log(res);  <span class="hljs-comment">// res = 3</span>
<span class="hljs-built_in">console</span>.log(arr);  <span class="hljs-comment">// [1,2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.4 shift</h3>
<blockquote>
<p><code>shift()</code> 方法从数组中删除第一个元素，并返回该元素的值。此方法更改数组的长度。</p>
<p><code>arr.shift()</code></p>
</blockquote>
<ul>
<li><code>@params</code>：</li>
<li><code>@return</code>：</li>
<li><code>是否改变原数组</code>：改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> res = arr.shift();    

<span class="hljs-built_in">console</span>.log(res);  <span class="hljs-comment">// res = 1</span>
<span class="hljs-built_in">console</span>.log(arr);  <span class="hljs-comment">// [2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.5 splice</h3>
<blockquote>
<p><code>splice()</code> 方法通过删除或替换现有元素或者原地添加新的元素来修改数组,并以数组形式返回被修改的内容。此方法会改变原数组。</p>
<p><code>array.splice(start[, deleteCount[, item1[, item2[, ...]]]])</code></p>
</blockquote>
<ul>
<li><code>@params</code>：不限参数， n,m,x,...第一个参数n是必传（数组的下标，代表从第n个元素起），第二个参数（可选）代表要删除（或被替代，取决于第三个参数是否有值）的元素个数，第三个参数（可选）起，代表要添加（或替代）的元素</li>
<li><code>@return</code>：返回值是一个数组，里面是删除项</li>
<li><code>是否改变原数组</code>：改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 删除</span>
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> res = arr.splice(<span class="hljs-number">1</span>);  <span class="hljs-comment">// 只传第一个参数，表示删除从下标为 1 的元素起，到最后一个元素</span>
<span class="hljs-built_in">console</span>.log(res);  <span class="hljs-comment">// [2, 3]</span>
<span class="hljs-built_in">console</span>.log(arr);  <span class="hljs-comment">// [1]</span>
<span class="hljs-comment">// arr.splice(0)：可以清空数组，把原始数组中的内容基于新数组储存起来（有点类似于数组克隆）</span>
<span class="hljs-comment">// arr.splice(arr.length-1)：删除最后一项</span>
<span class="hljs-comment">// arr.splice(0, 1)：删除第一项</span>

<span class="hljs-comment">// 增加</span>
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> res = arr.splice(<span class="hljs-number">1</span>, <span class="hljs-number">0</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>);  <span class="hljs-comment">// 第二个参数为0，表示不删除，之后的参数表示插进数组，下标从1开始，之前的元素往后挪</span>
<span class="hljs-built_in">console</span>.log(res);  <span class="hljs-comment">// []</span>
<span class="hljs-built_in">console</span>.log(arr);  <span class="hljs-comment">// [1, 8, 9, 2, 3]</span>

<span class="hljs-comment">// 改（替代）    </span>
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> res = arr.splice(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>);  <span class="hljs-comment">// 第二个参数为1，表示替代掉下标为1的元素</span>
<span class="hljs-built_in">console</span>.log(res);  <span class="hljs-comment">// [2]</span>
<span class="hljs-built_in">console</span>.log(arr);  <span class="hljs-comment">// [1, 8, 9, 3]</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            