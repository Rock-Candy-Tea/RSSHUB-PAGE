
---
title: '学算法刷LeetCode【剑指offer专题】：59-II.队列的最大值'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b12d8483a736415a8cee1a2250db9bb2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 04:14:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b12d8483a736415a8cee1a2250db9bb2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">题目描述</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b12d8483a736415a8cee1a2250db9bb2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fdui-lie-de-zui-da-zhi-lcof%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/" ref="nofollow noopener noreferrer">59-II.队列的最大值</a></p>
<h1 data-id="heading-1">解题思路</h1>
<h2 data-id="heading-2">思路1(暴力解法)</h2>
<p>使用队列的特性尾部插入，头部删除实现 push_back 和 pop_front， 至于寻找最大值，则遍历队列元素，找到最大值就返回，否则返回 -1。</p>
<p>时间复杂度：max_value 为O(n), 其余为 O(1)
空间复杂度： O(n)</p>
<p><strong>代码略</strong></p>
<h2 data-id="heading-3">思路2（维护一个单调的双端队列）</h2>
<p>我们从上面分析得知，实际上最耗时的是找到最大值，那么我们可以针对这个寻找过程做一些优化，增加一个队列，这个队列里面存放最大值。</p>
<ul>
<li>push_back 元素时， 普通的队列（队列1）直接在队尾添加元素，而单调队列则需要判断一下，如果队列的头部元素比当前元素都要小，将整个队列的元素出队，再将当前元素（最大值）添加到队尾</li>
<li>max_value 时，如果队列2不为空，则它的队首元素为最大值，否则，没有最大值，返回 -1.</li>
</ul>
<h1 data-id="heading-4">代码</h1>
<h2 data-id="heading-5">JS</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> MaxQueue = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.queue1 = [];
    <span class="hljs-built_in">this</span>.queue2 = [];
&#125;

MaxQueue.prototype.push_back = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>)</span>&#123;
    <span class="hljs-comment">// 单调队列里的最大值比当前值小，则清空整个队列。</span>
    <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.queue2.length && <span class="hljs-built_in">this</span>.queue2[<span class="hljs-built_in">this</span>.queue2.length - <span class="hljs-number">1</span>] < value)&#123;
        <span class="hljs-built_in">this</span>.queue2.pop();
    &#125;
    <span class="hljs-built_in">this</span>.queue1.push(value);
    <span class="hljs-built_in">this</span>.queue2.push(value);
&#125;

MaxQueue.prototype.pop_front = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// 队列为空，返回 -1</span>
    <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">this</span>.queue1.length) <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
    
    <span class="hljs-comment">// 元素存在，返回队头删除的元素</span>
    <span class="hljs-keyword">const</span> val = <span class="hljs-built_in">this</span>.queue1.shift();
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.queue2.length && <span class="hljs-built_in">this</span>.queue2[<span class="hljs-number">0</span>] === val)&#123;
        <span class="hljs-built_in">this</span>.queue2.shift();
    &#125;
    <span class="hljs-keyword">return</span> val;
&#125;

MaxQueue.prototype.max_value = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.queue2.length ? <span class="hljs-built_in">this</span>.queue2[<span class="hljs-number">0</span>] : -<span class="hljs-number">1</span>

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">总结</h1>
<p>关键思路在于如何优化的取得最大值的时间复杂度（max_value）， 利用单调队列，维护最大值即可，同时记得删除队首元素的时候，判断一下该元素是否正好也在单调队列中即可。</p>
<p>时间复杂度： O(1)</p>
<p>空间复杂度： O(n)</p></div>  
</div>
            