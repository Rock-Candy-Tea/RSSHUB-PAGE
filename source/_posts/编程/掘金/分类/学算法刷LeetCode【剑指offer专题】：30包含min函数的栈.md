
---
title: '学算法刷LeetCode【剑指offer专题】：30.包含min函数的栈'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b760b9de60e42ea892f9abef8cc1b8f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 00:32:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b760b9de60e42ea892f9abef8cc1b8f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">题目描述</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b760b9de60e42ea892f9abef8cc1b8f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fbao-han-minhan-shu-de-zhan-lcof%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/" ref="nofollow noopener noreferrer">30.包含min函数的栈</a></p>
<h1 data-id="heading-1">解体思路</h1>
<ol>
<li>这道题只对时间复杂度有要求，那可以在空间复杂度上放宽。因此，我们可以使用两个栈，</li>
<li>栈1正常实现的 push、pop()、top() 等 API</li>
<li>栈2则用于实现 min()。栈2维护一个最小值，这里有两种维护的方法:
<ul>
<li>一种是在 push 新元素的时候，把栈2的栈顶元素和新元素比较，把当前最小的值压入栈，这样栈2和栈1的元素个数始终相等，空间复杂度平均为 O(n);这样 pop 的时候，两个栈同时出栈即可。（见解法1）</li>
<li>一种是在 push 新元素的时候，判断一下，只有栈2栈顶元素比新元素大的时候，再压入栈2，这样的话，栈2的元素和栈1的元素个数可能就不一样了，所以出栈的时候，pop方法也要进行判断，如果栈1出栈的元素和栈2出栈的元素的一样才需要出栈，否则栈2不操作。这个的最坏空间复杂度为 O(n), 我个人觉得除非数据量特别大，这点优化可以不用做。（见解法2）
<ul>
<li>
<p>push 时判断，如果栈2为空或者新元素小于等于栈2顶部元素，则添加到栈2</p>
</li>
<li>
<p>pop 时判断，栈1将要pop的元素与栈2是否相等，相等则需要将该元素也出栈。</p>
</li>
</ul>
</li>
</ul>
</li>
</ol>
<h1 data-id="heading-2">代码</h1>
<h2 data-id="heading-3">JS</h2>
<h3 data-id="heading-4">解法1</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> MinStack = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.stack1 = [];
    <span class="hljs-built_in">this</span>.stack2 = [<span class="hljs-literal">Infinity</span>];
&#125;

MinStack.prototype.push = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.stack1.push(x);
    <span class="hljs-built_in">this</span>.stack2.push(<span class="hljs-built_in">Math</span>.min(<span class="hljs-built_in">this</span>.stack2[<span class="hljs-built_in">this</span>.stack2.length - <span class="hljs-number">1</span>], x));
&#125;

MinStack.prototype.pop = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.stack1.pop();
    <span class="hljs-built_in">this</span>.stack2.pop();
&#125;

MinStack.prototype.min = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.stack2[<span class="hljs-built_in">this</span>.stack2.length - <span class="hljs-number">1</span>];
&#125;

MinStack.prototype.top = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.stack1[<span class="hljs-built_in">this</span>.stack1.length - <span class="hljs-number">1</span>];
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">解法2</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> MinStack = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.stack1 = [];
    <span class="hljs-built_in">this</span>.stack2 = [];
&#125;

MinStack.prototype.push = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.stack1.push(x);
    <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">this</span>.stack2.length || <span class="hljs-built_in">this</span>.stack2[<span class="hljs-built_in">this</span>.stack2.length - <span class="hljs-number">1</span>] >= x)&#123;
        <span class="hljs-built_in">this</span>.stack2.push(x)
    &#125;
&#125;

MinStack.prototype.pop = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> ele = <span class="hljs-built_in">this</span>.stack1[<span class="hljs-built_in">this</span>.stack1.length - <span class="hljs-number">1</span>];

    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.stack2[<span class="hljs-built_in">this</span>.stack2.length - <span class="hljs-number">1</span>] == ele)&#123;
        <span class="hljs-built_in">this</span>.stack2.pop();
    &#125;

    <span class="hljs-built_in">this</span>.stack1.pop();
&#125;

MinStack.prototype.min = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.stack2.length ? <span class="hljs-built_in">this</span>.stack2[<span class="hljs-built_in">this</span>.stack2.length - <span class="hljs-number">1</span>] : <span class="hljs-number">0</span>
&#125;

MinStack.prototype.top = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.stack1[<span class="hljs-built_in">this</span>.stack1.length - <span class="hljs-number">1</span>];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>时间复杂度： O(1)
空间复杂度： O(n)</p></div>  
</div>
            