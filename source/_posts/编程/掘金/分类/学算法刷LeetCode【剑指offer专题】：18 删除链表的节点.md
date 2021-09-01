
---
title: '学算法刷LeetCode【剑指offer专题】：18. 删除链表的节点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf81078d17dd467a930744ca165bd7f5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 18:46:18 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf81078d17dd467a930744ca165bd7f5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">题目描述</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf81078d17dd467a930744ca165bd7f5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fshan-chu-lian-biao-de-jie-dian-lcof%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/" ref="nofollow noopener noreferrer">剑指 Offer 18. 删除链表的节点</a></p>
<h1 data-id="heading-1">解题思路</h1>
<p>题目中提示这是个单链表，单链表的特征就是节点中有一个指向下一个节点的指针，如果要删除一个节点，直接这个节点的前一个节点指向它的下一个节点即可。跳过要删除的节点，这个节点就被删除了。JavaScript 中， 我们不用关心这个节点最后是否需要释放内存。</p>
<p>考虑三种情况：</p>
<ul>
<li>
<p>如果头节点不存在，直接返回</p>
</li>
<li>
<p>如果头节点就是要删除的节点，直接将它的下一个节点返回。</p>
</li>
<li>
<p>遍历单链表，变量 <code>cur</code> 为头节点</p>
<ul>
<li>如果 <code>cur</code> 的下一个节点的 <code>val</code>和 给定要删除的 <code>val</code> 值相等，则跳过该节点，将 <code>cur</code> 的 <code>next</code> 指针指向  <code>cur.next.next</code>： <strong><code>cur.next = cur.next.next</code></strong>;</li>
<li>否则，说明没有遇到要删除的节点，则直接将下一个节点复值给 cur 节点： <strong><code>cur = cur.next</code></strong> 完成遍历即可。当节点为 <code>null</code> 时即遍历结束。</li>
</ul>
<p><strong>注意：当找到要删除的值的时候，改变的是 <code>cur</code> 的指针 <code>next, cur.next = cur.next.next</code>， 而正常遍历的时候， <code>cur</code> 是下一个节点 <code>cur = cur.next</code></strong></p>
</li>
</ul>
<h1 data-id="heading-2">代码</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Definition for singly-linked list.
 * function ListNode(val) &#123;
 *     this.val = val;
 *     this.next = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;ListNode&#125;</span> <span class="hljs-variable">head</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">val</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;ListNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> deleteNode = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">head, val</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!head) <span class="hljs-keyword">return</span> head;
    <span class="hljs-keyword">if</span>(head.val === val) <span class="hljs-keyword">return</span> head.next;
    <span class="hljs-keyword">let</span> cur = head;
    <span class="hljs-keyword">while</span>(cur.next)&#123;
        <span class="hljs-keyword">if</span>(cur.next.val === val)&#123;
            cur.next = cur.next.next;
        &#125;<span class="hljs-keyword">else</span>&#123;
            cur = cur.next
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> head;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">总结</h1>
<p>总的思路就是遍历，找到要删除的节点之后改变它的前一个元素的指针，让其指向它的后一个节点，然后需要考虑一下特殊情况，头节点不存在或者头节点的值就是要删除掉的节点的情况。</p>
<p>时间复杂度：O(n) 链表有 n 个， 进行了 n 次操作</p>
<p>空间复杂度：O(1)</p></div>  
</div>
            