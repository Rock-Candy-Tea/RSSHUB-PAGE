
---
title: 'LeetCode第278题：第一个错误的版本'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2920'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 00:42:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=2920'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">题干</h2>
<p>你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。</p>
<p>假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。</p>
<p>你可以通过调用 <code>bool isBadVersion(version)</code> 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。</p>
<p><strong>示例:</strong></p>
<pre><code class="copyable">给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。 
通过次数96,609提交次数223,000
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">思路：二分</h2>
<p>首先我们知道队列的构成时连续的false和连续的true，我们需要找到第一个true，所以我们在二分循环时判断一下结果为true的上一个是否为false即可。</p>
<p><strong>代码实现：</strong></p>
<blockquote>
<p>执行用时：72 ms, 在所有 JavaScript 提交中击败了72.65%的用户</p>
<p>内存消耗：37.6 MB, 在所有 JavaScript 提交中击败了51.50%的用户</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Definition for isBadVersion()
 * 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;integer&#125;</span> </span>version number
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;boolean&#125;</span> </span>whether the version is bad
 * isBadVersion = function(version) &#123;
 *     ...
 * &#125;;
 */</span>

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;function&#125;</span> </span>isBadVersion()
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;function&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> solution = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">isBadVersion</span>) </span>&#123;
    <span class="hljs-comment">/**
     * <span class="hljs-doctag">@param <span class="hljs-type">&#123;integer&#125;</span> </span>n Total versions
     * <span class="hljs-doctag">@return <span class="hljs-type">&#123;integer&#125;</span> </span>The first bad version
     */</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">n</span>) </span>&#123;
        <span class="hljs-keyword">let</span> max = n;
        <span class="hljs-keyword">let</span> min = <span class="hljs-number">1</span>;
        <span class="hljs-keyword">let</span> mid = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">while</span> (min <= max) &#123;
            mid = <span class="hljs-built_in">Math</span>.floor((max + min) / <span class="hljs-number">2</span>);
            <span class="hljs-keyword">let</span> right = isBadVersion(mid - <span class="hljs-number">1</span>)
            <span class="hljs-keyword">let</span> currentMid = isBadVersion(mid)
            <span class="hljs-keyword">if</span> (currentMid) &#123;
                <span class="hljs-keyword">if</span> (!right) &#123;
                    <span class="hljs-keyword">return</span> mid
                &#125;
                max = mid - <span class="hljs-number">1</span>
            &#125; <span class="hljs-keyword">else</span> &#123;
                min = mid + <span class="hljs-number">1</span>
            &#125;
        &#125;
    &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            