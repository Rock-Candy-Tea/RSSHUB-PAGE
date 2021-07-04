
---
title: 'Leetcode 79. 单词搜索 --javascript'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae080754f46844a89cbd9dcda72efe3b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 00:58:03 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae080754f46844a89cbd9dcda72efe3b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">79. 单词搜索</h1>
<h2 data-id="heading-1">描述</h2>
<p>给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。</p>
<p>单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae080754f46844a89cbd9dcda72efe3b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0673f724c970462eb13eb82a77cfc7ec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7868d3a887b9496b817082ec598c6ff1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
提示：</p>
<pre><code class="copyable">m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">题解</h2>
<p>不同于排列组合修改输出方式，而是修改访问标记。</p>
<p>在我们对任意位置进行深度优先搜索时，我们先标记当前位置为已访问，以避免重复遍历（如防止向右搜索后
又向左返回);</p>
<p>在所有的可能都搜索完成后，再回改当前位置为未访问，防止干扰其它位置搜索
到当前位置。</p>
<p>使用回溯法，我们可以只对一个二维的访问矩阵进行修改，而不用把每次的搜索状
态作为一个新对象传入递归函数中。</p>
<h3 data-id="heading-3">coding</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;character[][]&#125;</span> <span class="hljs-variable">board</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">word</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;boolean&#125;</span></span>
 */</span>
<span class="hljs-keyword">const</span> direction = [-<span class="hljs-number">1</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0</span>, -<span class="hljs-number">1</span>];
<span class="hljs-keyword">const</span> exist = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">board, word</span>) </span>&#123;
   <span class="hljs-keyword">if</span>(!board.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
   <span class="hljs-keyword">let</span> m = board.length, n = board[<span class="hljs-number">0</span>].length;
   <span class="hljs-keyword">let</span> visited = <span class="hljs-built_in">Array</span>.from(&#123;<span class="hljs-attr">length</span>: m&#125;, <span class="hljs-function">()=></span> <span class="hljs-built_in">Array</span>(n).fill(<span class="hljs-literal">false</span>));
   <span class="hljs-keyword">const</span> find = &#123;<span class="hljs-attr">flag</span>:<span class="hljs-literal">false</span>&#125;;
   <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < m; i++) &#123;
       <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < n; j++) &#123;
            backtracking(i, j, board, word, find, visited, <span class="hljs-number">0</span>);
       &#125;
   &#125;
   <span class="hljs-keyword">return</span> find.flag;
&#125;;
<span class="hljs-keyword">const</span> backtracking = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">i, j, board, word, find,visited, pos</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(i < <span class="hljs-number">0</span> || i >= board.length || j < <span class="hljs-number">0</span> || j >= board[<span class="hljs-number">0</span>].length) &#123;
        <span class="hljs-keyword">return</span>;
    &#125; 
    <span class="hljs-keyword">if</span>(visited[i][j] || (board[i][j] !== word[pos]) || find.flag) &#123;
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">if</span>(pos === word.length - <span class="hljs-number">1</span>) &#123;
      find.flag = <span class="hljs-literal">true</span>
      <span class="hljs-keyword">return</span>;
    &#125;
    visited[i][j] = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 修改当前节点状态。</span>
     <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> k = <span class="hljs-number">0</span>; k < <span class="hljs-number">4</span>; k++)&#123;
         <span class="hljs-keyword">const</span> dx = i + direction[k];
         <span class="hljs-keyword">const</span> dy = j + direction[k+<span class="hljs-number">1</span>];
         backtracking(dx, dy, board, word,find, visited, pos + <span class="hljs-number">1</span>);
     &#125;
     visited[i][j] = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 恢复节点状态；</span>

&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            