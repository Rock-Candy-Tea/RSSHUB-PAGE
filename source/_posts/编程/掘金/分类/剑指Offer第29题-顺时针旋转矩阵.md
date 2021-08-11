
---
title: '剑指Offer第29题-顺时针旋转矩阵'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dda189fa62e741f4824c116b9c62d2a9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 22:28:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dda189fa62e741f4824c116b9c62d2a9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第10天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">题干</h2>
<p>输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。</p>
<p><strong>示例 1：</strong></p>
<pre><code class="copyable"> 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
 输出：[1,2,3,6,9,8,7,4,5]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong></p>
<pre><code class="copyable"> 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">解法：</h2>
<p>看到这道题时直呼好家伙，这题也配归为简单题？力扣分类简直骚的不要。</p>
<p>顺时针打印二维数组，首先我们画出一个数组：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dda189fa62e741f4824c116b9c62d2a9~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们首先需要定义四个指针变量分别来表示我们横行位置Top、横行位置Bottom、竖行位置Left、竖行位置Right。</p>
<ul>
<li>当我们遍历完第一行时，Top下移</li>
<li>接着来遍历右边竖行，遍历结束后Right左移</li>
<li>接着遍历最后一行，遍历结束后Bottom上移</li>
<li>接着遍历左边竖行，遍历结束后Left右移</li>
</ul>
<p>我们循环结束的条件分别是，当我们Top>Bottom或Right<Left或Bottom>Top或Left>Right时都可以证明我们的循环结束了</p>
<p>代码实现：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">/**
  * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[][]&#125;</span> <span class="hljs-variable">matrix</span></span>
  * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number[]&#125;</span></span>
  */</span>
 <span class="hljs-keyword">var</span> spiralOrder = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">matrix</span>) </span>&#123;
     <span class="hljs-keyword">if</span> (matrix.length == <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> []
     <span class="hljs-keyword">let</span> left = <span class="hljs-number">0</span>;
     <span class="hljs-keyword">let</span> top = <span class="hljs-number">0</span>;
     <span class="hljs-keyword">let</span> right = matrix[<span class="hljs-number">0</span>].length - <span class="hljs-number">1</span>;
     <span class="hljs-keyword">let</span> bottom = matrix.length - <span class="hljs-number">1</span>
     <span class="hljs-keyword">let</span> res = [];
     <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
         <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = left; i <=right; i++) &#123;
             res.push(matrix[top][i]);
         &#125;
         top += <span class="hljs-number">1</span>;
         <span class="hljs-keyword">if</span> (top > bottom) <span class="hljs-keyword">break</span>
 ​
         <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = top; i <= bottom; i++) &#123;
             res.push(matrix[i][right]);
         &#125;
         right -= <span class="hljs-number">1</span>;
         
         <span class="hljs-keyword">if</span> (right < left) <span class="hljs-keyword">break</span>
 ​
         <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = right; i >= left; i--) &#123;
             res.push(matrix[bottom][i]);
         &#125;
         bottom -= <span class="hljs-number">1</span>;
         <span class="hljs-keyword">if</span> (bottom < top) <span class="hljs-keyword">break</span>
 ​
         <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = bottom; i >=top; i--) &#123;
             res.push(matrix[i][left]);
         &#125;
         left += <span class="hljs-number">1</span>;
         <span class="hljs-keyword">if</span> (left > right) <span class="hljs-keyword">break</span>
     &#125;
     <span class="hljs-keyword">return</span> res
 &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单的分析以下代码：</p>
<p>在循环中我们按照我们分析的顺序来一次遍历每一行或者每一列的数据，将得到的数据push到新的数组中，并且每一次遍历结束时将我们本位置的指针做出相应的移动，一旦遇到我们的结束条件就直接跳出循环，这说明我们此可已经遍历完了整个二维矩阵</p></div>  
</div>
            