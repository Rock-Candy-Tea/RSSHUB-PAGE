
---
title: 'LeetCode3. 无重复字符的最长子串'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3792'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 06:14:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=3792'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">题目描述</h4>
<p>给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。</p>
<h5 data-id="heading-1">示例 1:</h5>
<pre><code class="hljs language-js copyable" lang="js">输入: s = <span class="hljs-string">"abcabcbb"</span>
输出: <span class="hljs-number">3</span> 
解释: 因为无重复字符的最长子串是 <span class="hljs-string">"abc"</span>，所以其长度为 <span class="hljs-number">3</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">示例 2:</h5>
<pre><code class="hljs language-js copyable" lang="js">输入: s = <span class="hljs-string">"bbbbb"</span>
输出: <span class="hljs-number">1</span>
解释: 因为无重复字符的最长子串是 <span class="hljs-string">"b"</span>，所以其长度为 <span class="hljs-number">1</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">示例 3:</h5>
<pre><code class="hljs language-js copyable" lang="js">输入: s = <span class="hljs-string">"pwwkew"</span>
输出: <span class="hljs-number">3</span>
解释: 因为无重复字符的最长子串是 <span class="hljs-string">"wke"</span>，所以其长度为 <span class="hljs-number">3</span>。
     请注意，你的答案必须是 子串 的长度，<span class="hljs-string">"pwke"</span> 是一个子序列，不是子串。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 解题思路</span>
<span class="hljs-comment">// 1，先找出所有的不包含重复字符的子串</span>
<span class="hljs-comment">// 2，找出长度最大那个子串，返回其长度即可</span>

<span class="hljs-comment">// 解题步骤</span>
<span class="hljs-comment">// 1，用双指针维护一个滑动窗口，用来剪切子串</span>
<span class="hljs-comment">// 2，不断移动右指针，遇到重复字符，就把左指针移动到重复字符的下一位</span>
<span class="hljs-comment">// 3，过程中，记录所有窗口的长度，并返回最大值</span>
<span class="hljs-comment">// 4，赶紧关注我的微信公众号获取更多内容吧：手摸手前端进阶  </span>

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">s</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> lengthOfLongestSubstring = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">s</span>) </span>&#123;
  <span class="hljs-keyword">let</span> l = <span class="hljs-number">0</span> <span class="hljs-comment">// 左指针</span>
  <span class="hljs-keyword">let</span> res = <span class="hljs-number">0</span> <span class="hljs-comment">// 声明res 记录最大值</span>
  <span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> r = <span class="hljs-number">0</span>; r < s.length; r++) &#123;  <span class="hljs-comment">// 右指针滑动遍历</span>
    <span class="hljs-keyword">if</span> (map.has(s[r]) && map.get(s[r]) >= l) &#123; 
        <span class="hljs-comment">// map.get(s[r]) >= l 尾元素与首元素相同的情况</span>
      l = map.get(s[r]) + <span class="hljs-number">1</span>
    &#125;
    res = <span class="hljs-built_in">Math</span>.max(res, r - l + <span class="hljs-number">1</span>)
    map.set(s[r], r)
  &#125;
  <span class="hljs-keyword">return</span> res
&#125;;

<span class="hljs-comment">// 时间复杂度：O(n)</span>
<span class="hljs-comment">// 空间复杂度：O(m),m是字符串中不重复字符的个数</span>

<span class="hljs-comment">// 题目转载自力扣官网：</span>
<span class="hljs-comment">// https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            