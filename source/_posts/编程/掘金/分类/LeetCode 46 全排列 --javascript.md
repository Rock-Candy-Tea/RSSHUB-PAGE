
---
title: 'LeetCode 46. 全排列 --javascript'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5461'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 08:54:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=5461'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">46. 全排列</h1>
<h2 data-id="heading-1">描述</h2>
<p>给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。</p>
<p>示例 1：</p>
<pre><code class="copyable">输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<pre><code class="copyable">输入：nums = [0,1]
输出：[[0,1],[1,0]]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 3：</p>
<pre><code class="copyable">输入：nums = [1]
输出：[[1]]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<pre><code class="copyable">1 <= nums.length <= 6
-10 <= nums[i] <= 10
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">题解</h2>
<h3 data-id="heading-3">回溯法</h3>
<p>回溯法（backtracking）是优先搜索的一种特殊情况，又称为试探法，常用于需要记录节点状态的深度优先搜索。通常来说，排列、组合、选择类问题使用回溯法比较方便。
顾名思义，回溯法的核心是回溯。在搜索到某一节点的时候，如果我们发现目前的节点（及其子节点）并不是需求目标时，我们回退到原来的节点继续搜索，并且把在目前节点修改的状态 还原。</p>
<p>这样的好处是我们可以始终只对图的总状态进行修改，而非每次遍历时新建一个图来储存
状态。
在具体的写法上，它与普通的深度优先搜索一样，都有 [修改当前节点状态]→[递归子节
点] 的步骤，只是多了回溯的步骤，变成了 [修改当前节点状态]→[递归子节点]→[回改当前节点
状态]。
回溯法。有两个小诀窍，一是按引用传状态，二是所有的状态修 改在递归完成后回改。
回溯法修改一般有两种情况，一种是修改最后一位输出，比如排列组合；一种是修改访问标
记，比如矩阵里搜字符串。</p>
<h3 data-id="heading-4">分析</h3>
<p>怎样输出所有的排列方式呢？对于每一个当前位置 i，我们可以将其于之后的任意位置交换，
然后继续处理位置 i+1，直到处理到最后一位。为了防止我们每此遍历时都要新建一个子数组储
存位置 i 之前已经交换好的数字，我们可以利用回溯法，只对原数组进行修改，在递归完成后再
修改回来。
我们以样例[1,2,3]为例，按照这种方法，我们输出的数组顺序为[[1,2,3], [1,3,2], [2,1,3], [2,3,1],
[3,1,2], [3,2,1]]，可以看到所有的排列在这个算法中都被考虑到了。</p>
<h3 data-id="heading-5">coding</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number[][]&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> permute = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
   <span class="hljs-keyword">let</span> ans = [];
   <span class="hljs-keyword">let</span> start = <span class="hljs-number">0</span>, len = nums.length, _start = <span class="hljs-number">0</span>;
   backtracking(nums, start, ans);
   <span class="hljs-keyword">return</span> ans;
&#125;;

<span class="hljs-keyword">const</span> backtracking = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">_nums, level, ans</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(level === _nums.length - <span class="hljs-number">1</span>) &#123;
        ans.push([..._nums]);
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = level; i < _nums.length; i++) &#123;
        [_nums[i], _nums[level]] = [_nums[level], _nums[i]] <span class="hljs-comment">//  修改当前节点状态</span>
        backtracking(_nums, level + <span class="hljs-number">1</span>, ans); <span class="hljs-comment">// 递归子节点</span>
        [_nums[i], _nums[level]] = [_nums[level], _nums[i]] <span class="hljs-comment">//  恢复当前节点状态</span>
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            