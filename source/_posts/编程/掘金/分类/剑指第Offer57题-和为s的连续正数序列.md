
---
title: '剑指第Offer57题-和为s的连续正数序列'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4683'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 22:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4683'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第11天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">题干</h2>
<p>输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。</p>
<p>序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。</p>
<p><strong>示例</strong> 1：</p>
<pre><code class="copyable"> 输入：target = 9
 输出：[[2,3,4],[4,5]]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<pre><code class="copyable"> 输入：target = 15
 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来源：力扣（LeetCode） 链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fhe-wei-sde-lian-xu-zheng-shu-xu-lie-lcof" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof" ref="nofollow noopener noreferrer">leetcode-cn.com/problems/he…</a> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。</p>
<h2 data-id="heading-1">解法：</h2>
<p>作为剑指Offer的简单题，我们使用简单题的思路来进行思考，关于这道题我们双指针的做法，但是和我们常规的双指针做法不同，我们采用<strong>滑动窗口</strong>的方式的来解决，何为滑动窗口，看看题解你就可以感受到了：</p>
<p>题中要求我们至少要有两个数，所以我们设置相邻的两个指针left和right，初始化时使乐left为1，right为2，接着我们定义一个初始化的和right+left</p>
<p>接着开始循环：</p>
<ol>
<li>如果窗口内的add值大于target，我们使当前add减去当前的left，并且left右移</li>
<li>如果窗口的add小于target，我们先是right右移，再使add加上右移后的right</li>
<li>如果当前的add等于tartget，我们将当前的left到right的值一一加入数组中，在重复1，2操作</li>
</ol>
<blockquote>
<p>注意我们的left和right进行操作时需要注意后移和add数据变化的顺序，因为当我们left的值后移时我们要减去之前的left的值，当我们right的值后移时，需要加上我们后移的right值，因为不能加原先的right，这样就是重复计算了。</p>
</blockquote>
<p>代码实现：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">/**
  * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">target</span></span>
  * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number[][]&#125;</span></span>
  */</span>
 <span class="hljs-keyword">var</span> findContinuousSequence = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target</span>) </span>&#123;
     <span class="hljs-keyword">let</span> left = <span class="hljs-number">1</span>;
     <span class="hljs-keyword">let</span> right = <span class="hljs-number">2</span>;
     <span class="hljs-keyword">let</span> add = left + right;
     <span class="hljs-keyword">let</span> arr = []
     <span class="hljs-comment">//结束条件</span>
     <span class="hljs-keyword">while</span> (left <right) &#123;
         <span class="hljs-keyword">if</span> (add > target) &#123;
             add = add - left
             left = left + <span class="hljs-number">1</span>
         &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (add < target) &#123;
             right = right + <span class="hljs-number">1</span>
             add = add + right
         &#125; <span class="hljs-keyword">else</span> &#123;
             <span class="hljs-keyword">let</span> temparr = [];
             <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = left; i <= right; i++) &#123;
                 temparr.push(i)
             &#125;
             arr.push(temparr)
             add = add - left
             left = left + <span class="hljs-number">1</span>
             right = right + <span class="hljs-number">1</span>
             add = add + right
         &#125;
     &#125;
     <span class="hljs-keyword">return</span> arr
 &#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            