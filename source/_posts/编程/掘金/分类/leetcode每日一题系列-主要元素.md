
---
title: 'leetcode每日一题系列-主要元素'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3524'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 17:57:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=3524'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">leetcode-面试17.10-主要元素</h1>
<h2 data-id="heading-1">[博客链接]</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.saberlgy.top" target="_blank" rel="nofollow noopener noreferrer" title="https://www.saberlgy.top" ref="nofollow noopener noreferrer">菜🐔的学习之路</a></p>
<p><a href="https://juejin.cn/user/1882827881711389" target="_blank" title="https://juejin.cn/user/1882827881711389">掘金首页</a></p>
<h2 data-id="heading-2">[题目描述</h2>
<pre><code class="copyable">数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1
) 的解决方案。 



 示例 1： 


输入：[1,2,5,9,5,9,5,5,5]
输出：5 

 示例 2： 


输入：[3,2]
输出：-1 

 示例 3： 


输入：[2,2,1,1,1,2,2]
输出：2 
 Related Topics 数组 计数 
 👍 100 👎 0

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">[题目链接]</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Ffind-majority-element-lcci%2F" title="https://leetcode-cn.com/problems/find-majority-element-lcci/" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">leetcode题目链接</a></p>
<h2 data-id="heading-4">[github地址]</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsaberlgy1%2Fleetcode%2Fblob%2Fmaster%2Fsrc%2Fcom%2Fcute%2Fleetcode%2Feditor%2Fcn%2FFindMajorityElementLcci.java" title="https://github.com/saberlgy1/leetcode/blob/master/src/com/cute/leetcode/editor/cn/FindMajorityElementLcci.java" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">代码链接</a></p>
<h2 data-id="heading-5">[思路介绍]</h2>
<p><strong>思路一：Boyer-Moore投票算法</strong></p>
<ul>
<li><strong>暴力法</strong></li>
<li>通过map存储每个元素的信息，然后通过<strong>value</strong> 判断数组中占比超过一半的元素元素即可</li>
<li>时间复杂度O(n) 空间复杂度O(n)</li>
<li>这种方法就不写了，太简单了</li>
<li><strong>Boyer-Moore投票算法</strong>这也是我第一次听说这个算法</li>
<li>整体思路类似于随机确立一个候选元素</li>
<li>每当遍历一个元素与当前元素相同则计数器<strong>count+1</strong>，不同则<strong>count-1</strong></li>
<li>当count=0的时候遍历下一个元素，将候选元素变为下一个元素</li>
<li>重复上述过程</li>
<li>证明原理，因为只要元素的定义是超过数组一半数量元素</li>
<li>所以这种做法一定会抵消其余元素</li>
<li>剩余的元素可能是主要元素</li>
<li>需要再次扫描数组，确认主要元素的数量是否超过数组的一半</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">majorityElement</span><span class="hljs-params">(<span class="hljs-keyword">int</span>[] nums)</span> </span>&#123;
            <span class="hljs-keyword">int</span> count = <span class="hljs-number">1</span>, master = nums[<span class="hljs-number">0</span>], n = nums.length;
            <span class="hljs-keyword">if</span> (n == <span class="hljs-number">1</span>) &#123;
                <span class="hljs-keyword">return</span> master;
            &#125;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">1</span>; i < n; i++) &#123;
                <span class="hljs-keyword">if</span> (count == <span class="hljs-number">0</span>) &#123;
                    master = nums[i];
                &#125;
                <span class="hljs-keyword">if</span> (nums[i] == master) &#123;
                    count++;
                &#125; <span class="hljs-keyword">else</span> &#123;
                    count--;
                &#125;
            &#125;
            count = <span class="hljs-number">0</span>;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> num : nums
            ) &#123;
                <span class="hljs-keyword">if</span> (num == master) &#123;
                    count++;
                &#125;
            &#125;
    <span class="hljs-comment">//确保奇数个元素的一半长度</span>
            <span class="hljs-keyword">return</span> count >= (n + <span class="hljs-number">1</span>) / <span class="hljs-number">2</span> ? master : -<span class="hljs-number">1</span>;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>时间复杂度</mtext><mi>O</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo><mtext>空间复杂度</mtext><mi>O</mi><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">时间复杂度O(n) 空间复杂度O(1)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord cjk_fallback">时</span><span class="mord cjk_fallback">间</span><span class="mord cjk_fallback">复</span><span class="mord cjk_fallback">杂</span><span class="mord cjk_fallback">度</span><span class="mord mathnormal" style="margin-right:0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mclose">)</span><span class="mord cjk_fallback">空</span><span class="mord cjk_fallback">间</span><span class="mord cjk_fallback">复</span><span class="mord cjk_fallback">杂</span><span class="mord cjk_fallback">度</span><span class="mord mathnormal" style="margin-right:0.02778em;">O</span><span class="mopen">(</span><span class="mord">1</span><span class="mclose">)</span></span></span></span></span></p></div>  
</div>
            