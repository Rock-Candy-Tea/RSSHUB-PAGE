
---
title: '学算法刷LeetCode【剑指offer专题】：06. 从尾到头打印链表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/507a24de432a45aaa68844b974be478b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 01:38:56 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/507a24de432a45aaa68844b974be478b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">题目描述</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/507a24de432a45aaa68844b974be478b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">思路</h1>
<h2 data-id="heading-2">思路一</h2>
<h3 data-id="heading-3">遍历</h3>
<p>遍历节点，将链表的值存到数组里面，这里有两种方法:</p>
<ul>
<li>
<p>存的时候就从数组的头部插入（<code>unshift()</code>），这样直接返回该数组即可。（见解法1）</p>
</li>
<li>
<p>增加一个新的数组2，遍历链表的时候按原顺序存入数组1中，然后再反向遍历一次数组1，将结果存入数组2中，返回数组2的结果。（见解法2）</p>
</li>
</ul>
<h4 data-id="heading-4">解法1</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Definition for singly-linked list.
 * function ListNode(val) &#123;
 *     this.val = val;
 *     this.next = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;ListNode&#125;</span> <span class="hljs-variable">head</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number[]&#125;</span></span>
 */</span>
 <span class="hljs-keyword">var</span> reversePrint = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">head</span>) </span>&#123;
    <span class="hljs-keyword">let</span> res = [];
    <span class="hljs-keyword">while</span>(head)&#123;
        res.unshift(head.val);
        head = head.next;
    &#125;
    <span class="hljs-keyword">return</span> res;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">解法2</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> reversePrint = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">head</span>) </span>&#123;
    <span class="hljs-keyword">let</span> arr1 = [];
    <span class="hljs-keyword">let</span> arr2 = [];
    <span class="hljs-keyword">while</span>(head)&#123;
        arr1.push(head.val);
        head = head.next;
    &#125;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = arr1.length - <span class="hljs-number">1</span>; i <= <span class="hljs-number">0</span>; i--)&#123;
        arr2.push(arr1[i]);
    &#125;
    <span class="hljs-keyword">return</span> arr2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上两种解法：</p>
<p>时间复杂度为 O(n)</p>
<p>空间复杂度为： O(n)</p>
<h2 data-id="heading-6">思路二</h2>
<h3 data-id="heading-7">递归</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> reversePrint = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">head</span>) </span>&#123;
    <span class="hljs-keyword">let</span> res = [];
    <span class="hljs-keyword">var</span> reverse = <span class="hljs-function">(<span class="hljs-params">head</span>) =></span> &#123;
        <span class="hljs-keyword">if</span>(!head) <span class="hljs-keyword">return</span>;
        reverse(head.next);
        res.push(head.val);
    &#125;
    reverse(head);
    <span class="hljs-keyword">return</span> res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>递归的时间复杂度为：递归的次数*每次递归中的操作次数，这里递归次数为 n， 操作数为 1，所以:</p>
<p>时间复杂度为 O(n)</p>
<p>空间复杂度为： O(n)</p>
<h1 data-id="heading-8">总结</h1>
<p>思路就是遍历加反转，至于是用多余的数组还是用递归，看个人喜好吧。</p></div>  
</div>
            