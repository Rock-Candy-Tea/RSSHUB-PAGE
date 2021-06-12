
---
title: 'LeetCode第540题：有序数组中的单一元素'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef4bc607178e4e6d860022f27dc866ec~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 00:44:03 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef4bc607178e4e6d860022f27dc866ec~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">题干</h2>
<p>给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。</p>
<p><strong>示例 1:</strong></p>
<pre><code class="copyable">输入: [1,1,2,3,3,4,4,8,8]
输出: 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2:</strong></p>
<pre><code class="copyable">输入: [3,3,7,7,10,11,11]
输出: 10
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">思路1：一次循环</h2>
<p>这种解法思路比较简单，每一次循环时将当前元素与下一个元素进行比较，如果相同，则继续，直至循环结束，返回最后一个元素；不同则返回当前值。</p>
<blockquote>
<p>执行用时：80 ms, 在所有 JavaScript 提交中击败了83.39%的用户</p>
<p>内存消耗：38.6 MB, 在所有 JavaScript 提交中击败了100.00%的用户</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">var</span> singleNonDuplicate = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">nums</span>) </span>&#123;
    <span class="hljs-keyword">let</span> length = nums.length;
    <span class="hljs-keyword">if</span> (length == <span class="hljs-number">1</span>) &#123;
      <span class="hljs-keyword">return</span> nums[<span class="hljs-number">0</span>]
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length - <span class="hljs-number">1</span>;) &#123;
      <span class="hljs-keyword">if</span> (nums[i] == nums[i + <span class="hljs-number">1</span>]) &#123;
        i = i + <span class="hljs-number">2</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> nums[i]
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> nums[length - <span class="hljs-number">1</span>]
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">思路2：二分法</h2>
<p>这道题依然可以使用二分法来解决，就是按照我们的位置进行判断，如果我们当前的位置时偶位置，那么根据与左右元素的对比情况来判断二分的边界，奇位置与偶位置判定相反。</p>
<p>画图分析一下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef4bc607178e4e6d860022f27dc866ec~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210612163538.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码实现：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> singleNonDuplicate2 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">nums</span>) </span>&#123;
    <span class="hljs-comment">// 二分思想</span>
    <span class="hljs-keyword">let</span> mid = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> min = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> max = nums.length - <span class="hljs-number">1</span>;
    <span class="hljs-keyword">while</span> (min <= max) &#123;
        mid = <span class="hljs-built_in">Math</span>.floor((min + max) / <span class="hljs-number">2</span>);
        <span class="hljs-keyword">let</span> right = nums[mid + <span class="hljs-number">1</span>];
        <span class="hljs-keyword">let</span> left = nums[mid - <span class="hljs-number">1</span>];
        <span class="hljs-keyword">if</span> (right != nums[mid] && left != nums[mid]) &#123; <span class="hljs-keyword">return</span> nums[mid] &#125;
        <span class="hljs-keyword">if</span> (mid % <span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">if</span>(nums[mid]==right)&#123;
                min=mid+<span class="hljs-number">1</span>
            &#125;<span class="hljs-keyword">else</span>&#123;
                max=mid-<span class="hljs-number">1</span>
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">if</span>(nums[mid]==left)&#123;
                min=mid+<span class="hljs-number">1</span>
            &#125;<span class="hljs-keyword">else</span>&#123;
                max=mid-<span class="hljs-number">1</span>
            &#125;
        &#125;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            