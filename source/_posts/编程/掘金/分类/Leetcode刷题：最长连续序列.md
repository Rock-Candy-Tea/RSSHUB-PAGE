
---
title: 'Leetcode刷题：最长连续序列'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2800'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 07:19:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=2800'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与新手入门的第3篇文章。</p>
<h1 data-id="heading-0">题目描述</h1>
<p>给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。</p>
<p><strong>进阶：</strong> 你可以设计并实现时间复杂度为 O(n) 的解决方案吗？</p>
<p>示例1:</p>
<pre><code class="copyable">输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例2:</p>
<pre><code class="copyable">输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">思路分析</h1>
<p>分析题目可知，数字 x 的最长连续序列其实是 x，x+1，x+2，……，x+n，其长度为 n+1，这样我们就可以便利数组，对每一个数字找出 x+n 不在数组中时 n 的值，此值就是 x 的连续序列长度。比较每次得到的长度取最大值，这就是我们要找的连续的最长序列的长度。</p>
<p>根据以上分析，我们可以发现：</p>
<ul>
<li>重复的数字 x 对我们找出连续的最长序列是没有意义的，故我们可以使用 ES6 中新的数据类型 Set 为数组去重。</li>
<li>对于任意数字 x 的为起始的最长连续序列，不应该存在 x-1 在数组 nums 中，所以对于 x-1 在数组 nums 中的情况我们无需探索它的连续序列长度</li>
</ul>
<p>还有下面我们来实现代码</p>
<h1 data-id="heading-2">代码实现</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">const</span> longestConsecutive = <span class="hljs-function"><span class="hljs-params">nums</span> =></span> &#123;
  <span class="hljs-keyword">const</span> numSet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(nums);

  <span class="hljs-keyword">let</span> longest = <span class="hljs-number">0</span>;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> num <span class="hljs-keyword">of</span> numSet) &#123;
    <span class="hljs-keyword">if</span> (!numSet.has(num - <span class="hljs-number">1</span>)) &#123;
      <span class="hljs-keyword">let</span> n = <span class="hljs-number">1</span>;
      <span class="hljs-keyword">while</span> (numSet.has(num + n)) &#123;
        n++;
      &#125;

      longest = <span class="hljs-built_in">Math</span>.max(n, longest);
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> longest;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先我们使用 Set 对数组去重，接着我们定义了一个变量用来储存最长的连续序列长度，开始时我们将它置为 0；然后我们迭代 numSet，对每次迭代时的数字 num 判断是否在 numSet中存在 num-1，因为每个连续序列的起点都不应该存在 num-1 在 numSet 中；之后我们又定义了变量 n，用它表示数字 num 的连续序列长度，接下来我们开始探索数字 num 的连续序列的最大长度，将得出的 n 与已经记录的最大的长度比较，取较大的值；最后返回迭代数组完毕后的最大值。</p>
<h1 data-id="heading-3">总结</h1>
<p>现在来总结一下，我们具体做了哪些：</p>
<ol>
<li>我们分析了什么是最长连续序列，即 x，x+1，x+2，……，x+n，长度为 n+1</li>
<li>我们发现重复的数字对找出连续的最长序列是没有意义</li>
<li>对于任意数字 x 的为起始的最长连续序列，不应该存在 x-1 在数组 nums 中</li>
<li>我们编码代码实现了算法</li>
</ol></div>  
</div>
            