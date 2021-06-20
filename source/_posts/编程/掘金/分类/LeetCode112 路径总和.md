
---
title: 'LeetCode112. 路径总和'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b843aa76c643738f76672b5798d22b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 20:52:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b843aa76c643738f76672b5798d22b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">题目描述</h4>
<h5 data-id="heading-1">公众号：手摸手前端进阶</h5>
<p>给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。</p>
<p>叶子节点 是指没有子节点的节点。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b843aa76c643738f76672b5798d22b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">输入：root = [<span class="hljs-number">5</span>,<span class="hljs-number">4</span>,<span class="hljs-number">8</span>,<span class="hljs-number">11</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">13</span>,<span class="hljs-number">4</span>,<span class="hljs-number">7</span>,<span class="hljs-number">2</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">1</span>], targetSum = <span class="hljs-number">22</span>
输出：<span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28e89f5a976f4fbeabc115d824f7dd7a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) &#123;
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">targetSum</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;boolean&#125;</span></span>
 */</span>
<span class="hljs-comment">/**
 解题步骤：
 1，深度优先遍历二叉树，在叶子节点处，判断当前路径的节点值是否等于目标值，是就返回true
 2，遍历结束，如果没有匹配，就返回false
*/</span>
<span class="hljs-keyword">var</span> hasPathSum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, targetSum</span>) </span>&#123;
  <span class="hljs-keyword">if</span>(!root) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  <span class="hljs-keyword">let</span> res = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">const</span> dfs = <span class="hljs-function">(<span class="hljs-params">n, sum</span>) =></span> &#123;
    <span class="hljs-keyword">if</span>(!n.left && !n.right && sum === targetSum) &#123;
      res = <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-keyword">if</span>(n.left) dfs(n.left, sum + n.left.val)
    <span class="hljs-keyword">if</span>(n.right) dfs(n.right, sum + n.right.val)
  &#125;
  dfs(root, root.val)
  <span class="hljs-keyword">return</span> res
&#125;;

<span class="hljs-comment">// 题目转载自力扣官网：</span>
<span class="hljs-comment">// https://leetcode-cn.com/problems/path-sum/</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            