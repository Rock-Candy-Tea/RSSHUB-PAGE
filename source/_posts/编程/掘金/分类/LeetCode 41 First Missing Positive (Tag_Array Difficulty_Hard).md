
---
title: 'LeetCode 41 First Missing Positive (Tag_Array Difficulty_Hard)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9587'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 06:49:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=9587'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><p>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>关于 LeetCode 数组类型题目的相关解法，可见<a href="https://juejin.cn/post/6978419497153593352" target="_blank" title="https://juejin.cn/post/6978419497153593352">LeetCode 数组类型题目做前必看</a>，分类别解法总结了题目，可以用来单项提高。觉得有帮助的话，记得多多点赞关注哦，感谢！</p>
<h2 data-id="heading-1">题目描述</h2>
<p>给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。</p>
<p>请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 </p>
<p>示例 1：<br>
输入：nums = [1,2,0]<br>
输出：3</p>
<p>示例 2：<br>
输入：nums = [3,4,-1,1]<br>
输出：2</p>
<p>示例 3：<br>
输入：nums = [7,8,9,11,12]<br>
输出：1</p>
<p>链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Ffirst-missing-positive" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/first-missing-positive" ref="nofollow noopener noreferrer">leetcode-cn.com/problems/fi…</a></p>
<h2 data-id="heading-2">题解</h2>
<ol>
<li>可以先从简单的方案说起. 可以想到的是利用 hash 的方法, 将 nums 中的元素作为 hash 的下标, 出现在 nums 中的元素, 在 hash 对应下标均为 1. 这样, 将所以的出现过的元素都用 hash 数组标识了, 我们可以从位置 1 开始检查对应位置上的 hash 是否为 1, 一旦发现未出现或者遍历到 hash 数组的尾部了, 那么就可以找出对应的值了. 具体代码见下方, 虽然本方法的时间复杂度为 <strong>O(n)</strong>, 但是空间复杂度为 <strong>O(max(nums))</strong>, 因此并不满足题目的要求.</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> firstMissingPositive = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">nums</span>) </span>&#123;
  <span class="hljs-keyword">let</span> hash = [];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> n <span class="hljs-keyword">of</span> nums) &#123;
    <span class="hljs-keyword">if</span> (n >= <span class="hljs-number">0</span>) &#123;
      hash[n] = <span class="hljs-number">1</span>;
    &#125;
  &#125;
  <span class="hljs-keyword">let</span> res = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">while</span> (i < hash.length) &#123;
    <span class="hljs-keyword">if</span> (!hash[i]) &#123;
      res = i;
      <span class="hljs-keyword">break</span>;
    &#125;
    i++;
  &#125;
  <span class="hljs-keyword">if</span> (i === hash.length) &#123;
    res = hash.length;
  &#125;
  <span class="hljs-keyword">return</span> res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>方法1中, 我们利用 hash 的方法来达到时间复杂度为 O(n) 的目的, 但是空间复杂度不是常数, 有没有更好的方法来减少空间复杂度呢? 聪明的你可能已经想到了, 我们可以复用 nums 这个数组而不必开辟新的 hash 数组, 怎么做呢.<br>
首先我们要确定的是, 最终要返回的正整数一定是在 <strong>[1, n+1]</strong> 的区间内, n 为 nums 的长度, 这是要明确的. 在确定好这一点之后就好办了, 其实只要我们把每个元素放在跟他对应的位置上, 然后从头检查每个位置上的元素和下标是不是对应的就好. 具体来说就是, 比如有元素 1, 就把 1 放在 0 位置上, 元素 5 就把 5 放在 4 位置上, 即数组中元素是下标加一, 这样调整过后, 当位置 i 上的元素不是 i + 1 时, i + 1 就是最后的答案, 如果所有的元素都是对应的, 那就返回 n + 1. 在调整过程中我们可能会遇到小于 1 或者大于 n 的数, 这时候跳过这个位置就好. 具体方法可以见下面的代码. 我们可以称本方法为原地hash, 时间复杂度为 O(n), 空间复杂度为 O(1).</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> firstMissingPositive = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
    <span class="hljs-keyword">const</span> len = nums.length
    
    <span class="hljs-keyword">const</span> swap = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp
    &#125;
    
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; ++i) &#123;
        <span class="hljs-comment">// 调整 i 位置的元素, 直到符合要求或者超出范围</span>
        <span class="hljs-keyword">while</span> (nums[i] > <span class="hljs-number">0</span> && nums[i] < len + <span class="hljs-number">1</span> && nums[nums[i] - <span class="hljs-number">1</span>] !== nums[i]) &#123;
            swap(i, nums[i] - <span class="hljs-number">1</span>)
        &#125;
    &#125;
    
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; ++i) &#123;
        <span class="hljs-keyword">if</span> (nums[i] !== i + <span class="hljs-number">1</span>) &#123;
            <span class="hljs-keyword">return</span> i + <span class="hljs-number">1</span>
        &#125;
    &#125;
    
    <span class="hljs-keyword">return</span> len + <span class="hljs-number">1</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            