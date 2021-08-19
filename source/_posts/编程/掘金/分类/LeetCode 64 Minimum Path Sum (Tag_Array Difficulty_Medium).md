
---
title: 'LeetCode 64 Minimum Path Sum (Tag_Array Difficulty_Medium)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91ece0abbea0422389313f3be459955d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 05:37:47 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91ece0abbea0422389313f3be459955d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><p>这是我参与8月更文挑战的第18天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>关于 LeetCode 数组类型题目的相关解法，可见<a href="https://juejin.cn/post/6978419497153593352" target="_blank" title="https://juejin.cn/post/6978419497153593352">LeetCode 数组类型题目做前必看</a>，分类别解法总结了题目，可以用来单项提高。觉得有帮助的话，记得多多点赞关注哦，感谢！</p>
<h2 data-id="heading-1">题目描述</h2>
<p>给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。</p>
<p>说明：每次只能向下或者向右移动一步。</p>
<p>示例 1：<br>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91ece0abbea0422389313f3be459955d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]<br>
输出：7<br>
解释：因为路径 1→3→1→1→1 的总和最小。</p>
<p>示例 2：<br>
输入：grid = [[1,2,3],[4,5,6]]<br>
输出：12</p>
<p>链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fminimum-path-sum" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/minimum-path-sum" ref="nofollow noopener noreferrer">leetcode-cn.com/problems/mi…</a></p>
<h2 data-id="heading-2">题解</h2>
<ol>
<li>
<p>记忆化递归. 同上一道题<a href="https://juejin.cn/post/6997426896086499358" target="_blank" title="https://juejin.cn/post/6997426896086499358">Unique Paths II</a> 一样, 可以利用递归的方法求解, path[i][j] = min(path[i-1][j], path[i][j-1]) + grid[i][j], 因为在求解过程中, 存在同一个值会被多次计算的情况, 比如 path[i][j-1] 除了在计算 path[i][j] 中被用到, 也会在计算 path[i+1][j-1] (path[i+1][j-1] = path[i][j-1] + path[i][j-2]) 中用到, 因此, 为了避免多次计算同一个值, 我们可以利用一个记忆数组来保存已经计算过的值, 这样, 在下一次用到该值时, 就可以直接取出来, 而不是重复计算.</p>
<p>具体解法见如下代码, 其中 path 数组就代表记忆数组, 当对应的元素为 -1 时, 就表示还未计算过, 当不为 -1 时, 表示已经计算过, 可以直接返回.</p>
<p>时间复杂度 O(mn), 空间复杂度 O(mn)</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[][]&#125;</span> <span class="hljs-variable">grid</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> minPathSum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">grid</span>) </span>&#123;
  <span class="hljs-keyword">const</span> m = grid.length
  <span class="hljs-keyword">const</span> n = grid[<span class="hljs-number">0</span>].length
  <span class="hljs-comment">// 记忆数组</span>
  <span class="hljs-keyword">const</span> path = <span class="hljs-built_in">Array</span>.from(&#123; <span class="hljs-attr">length</span>: m &#125;, <span class="hljs-function">() =></span> (<span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(n).fill(-<span class="hljs-number">1</span>)))
  
  <span class="hljs-keyword">const</span> minPath = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-comment">// 到了起点</span>
    <span class="hljs-keyword">if</span> (x === <span class="hljs-number">0</span> && y === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> grid[<span class="hljs-number">0</span>][<span class="hljs-number">0</span>]
    <span class="hljs-comment">// 出了边界</span>
    <span class="hljs-keyword">if</span> (x < <span class="hljs-number">0</span> || y < <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Number</span>.MAX_VALUE
    <span class="hljs-comment">// 记忆数组中对应位置已经计算过值了</span>
    <span class="hljs-keyword">if</span> (path[x][y] !== -<span class="hljs-number">1</span>) &#123;
      <span class="hljs-keyword">return</span> path[x][y]
    &#125; 
    <span class="hljs-comment">// 递归</span>
    path[x][y] = grid[x][y] + <span class="hljs-built_in">Math</span>.min(minPath(x-<span class="hljs-number">1</span>, y), minPath(x, y-<span class="hljs-number">1</span>))
    <span class="hljs-keyword">return</span> path[x][y]
  &#125;
  
  <span class="hljs-keyword">return</span> minPath(m-<span class="hljs-number">1</span>, n-<span class="hljs-number">1</span>)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>动态规划. 一般来讲, 如果一个问题能用记忆化递归的方法来解决, 那么该问题也能用动态规划的问题来解决. 记忆化递归是从尾到头的方式, 而动态规划是从头到尾的方式. 什么意思呢? 就是我们从起点开始计算, path[0][0] = grid[0][0], 边界上的点有 path[i][0] = path[i-1][0] + grid[i][0], path[0, j] = path[0, j-1] + grid[0, j], 那么内部的点有 path[i][j] = min(path[i-1][j] + path[i][j-1]) + grid[i][j], 这样就实现了从头到尾的方式.</li>
</ol>
<p>具体代码见下方, 需要注意的一个点是, 我们用原 grid 数组来当作了 path 数组, 这样可以减少空间复杂度.</p>
<p>时间复杂度 O(mn), 空间复杂度 O(1)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[][]&#125;</span> <span class="hljs-variable">grid</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> minPathSum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">grid</span>) </span>&#123;
    <span class="hljs-keyword">let</span> m = grid.length;
    <span class="hljs-keyword">if</span> (m == <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> n = grid[<span class="hljs-number">0</span>].length;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < m; ++i) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < n; ++j) &#123;
            <span class="hljs-keyword">if</span> (i === <span class="hljs-number">0</span> && j === <span class="hljs-number">0</span>) <span class="hljs-keyword">continue</span>;
            <span class="hljs-keyword">if</span> (i === <span class="hljs-number">0</span>)
                grid[i][j] += grid[i][j-<span class="hljs-number">1</span>]
            <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (j === <span class="hljs-number">0</span>) 
                grid[i][j] += grid[i-<span class="hljs-number">1</span>][j]
            <span class="hljs-keyword">else</span> 
                grid[i][j] += <span class="hljs-built_in">Math</span>.min(grid[i][j-<span class="hljs-number">1</span>], grid[i-<span class="hljs-number">1</span>][j])
        &#125;
    &#125;   
    <span class="hljs-keyword">return</span> grid[m - <span class="hljs-number">1</span>][n - <span class="hljs-number">1</span>];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            