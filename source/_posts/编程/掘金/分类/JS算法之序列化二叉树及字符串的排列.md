
---
title: 'JS算法之序列化二叉树及字符串的排列'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4072fb2982a47b09652efee078a9db2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 18:06:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4072fb2982a47b09652efee078a9db2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第30天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">序列化二叉树</h2>
<blockquote>
<p>剑指Offer 37.序列化二叉树</p>
<p>难度：困难</p>
<p>leetcode地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fxu-lie-hua-er-cha-shu-lcof%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/" ref="nofollow noopener noreferrer">leetcode-cn.com/problems/xu…</a></p>
</blockquote>
<p>请实现两个函数，分别用来序列化和反序列化二叉树。</p>
<p>你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列/反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。</p>
<p>示例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4072fb2982a47b09652efee078a9db2~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">题解</h2>
<h3 data-id="heading-2">法一 BFS</h3>
<p>序列化步骤：</p>
<ul>
<li>创建一个结果数组res，然后用一个队列，初始让根节点入列，对出列的节点进行考察：
<ul>
<li>出列节点为null，将"$"推入res。</li>
<li>出列节点为数值，将值推入res，并将它的左右节点入列。</li>
</ul>
</li>
<li>入列、出列...直到队列为空，就遍历完所有节点，res构建完毕，将res转为字符串。</li>
</ul>
<p>反序列化步骤：</p>
<p>由上诉序列化能得到的序列是<code>1 2 3 $ $ 4 5 $ $ $ $</code>，可以看出第一个是根节点，其他节点都是对应左右子节点。</p>
<ul>
<li>字符串先转成数组list，用指针cursor从第二项开始扫描。</li>
<li>list[0]构建根节点，将根节点入列。</li>
<li>节点出列，此时cursor指向左子节点，cursor指向右子节点。如果子节点为"$"，跳过；否则（如果子节点为数值），创建节点，并让父节点对应子节点，还要将该节点入列。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>

<span class="hljs-comment">/**
 * Encodes a tree to a single string.
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;string&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> serialize = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
  <span class="hljs-keyword">const</span> queue = [root];
  <span class="hljs-keyword">let</span> res = [];
  <span class="hljs-keyword">while</span>(queue.length)&#123;
    <span class="hljs-keyword">const</span> node = queue.shift(); <span class="hljs-comment">// 考察出列节点</span>
    <span class="hljs-keyword">if</span>(node)&#123;<span class="hljs-comment">// 节点不为null，则节点入列，否则将$入列。</span>
      res.push(node.val);
      queue.push(node.left);
      queue.push(node.right);
    &#125;<span class="hljs-keyword">else</span>&#123;
      res.push(<span class="hljs-string">'$'</span>);
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> res.join(<span class="hljs-string">','</span>);<span class="hljs-comment">// 数组转字符串</span>
&#125;;

<span class="hljs-comment">/**
 * Decodes your encoded data to tree.
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">data</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> deserialize = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
<span class="hljs-keyword">if</span>(data === <span class="hljs-string">'$'</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  
  <span class="hljs-keyword">const</span> list = data.split(<span class="hljs-string">','</span>);<span class="hljs-comment">// 序列化字符串split成数组</span>
  
  <span class="hljs-keyword">const</span> root = <span class="hljs-keyword">new</span> TreeNode(list[<span class="hljs-number">0</span>]);<span class="hljs-comment">// 构建根节点</span>
  <span class="hljs-keyword">const</span> queue = [root];<span class="hljs-comment">// 根节点入列</span>
  <span class="hljs-keyword">let</span> cursor = <span class="hljs-number">1</span>;<span class="hljs-comment">// 初始指向list第二项</span>
  
  <span class="hljs-keyword">while</span>(cursor < list.length)&#123;<span class="hljs-comment">// 指针越界，即扫完了序列化字符串</span>
    <span class="hljs-keyword">const</span> node = queue.shift();<span class="hljs-comment">// 考察出列节点</span>
    
    <span class="hljs-keyword">const</span> leftVal = list[cursor];<span class="hljs-comment">// 左节点值</span>
    <span class="hljs-keyword">const</span> rightVal = list[cursor+<span class="hljs-number">1</span>];<span class="hljs-comment">// 右节点值</span>
    
    <span class="hljs-keyword">if</span>(leftVal !== <span class="hljs-string">'$'</span>)&#123;<span class="hljs-comment">// 节点不为null，则：</span>
      <span class="hljs-keyword">const</span> leftNode = <span class="hljs-keyword">new</span> TreeNode(leftVal);<span class="hljs-comment">// 创建左子节点</span>
      node.left = leftNode;<span class="hljs-comment">// 父节点左子树指向左子节点</span>
      queue.push(leftNode);<span class="hljs-comment">// 自己是父节点，入列</span>
    &#125;
    <span class="hljs-keyword">if</span>(rightVal !== <span class="hljs-string">'$'</span>)&#123;
      <span class="hljs-keyword">const</span> rightNode = <span class="hljs-keyword">new</span> TreeNode(rightVal);
      node.right = rightNode;
      queue.push(rightNode);
    &#125;
    cursor += <span class="hljs-number">2</span>;
  &#125;
  <span class="hljs-keyword">return</span> root;
&#125;;

<span class="hljs-comment">/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">法二 DFS</h3>
<p>序列化步骤：</p>
<ul>
<li>递归遍历一棵树，再将返回结果拼接。</li>
<li>选择采用前序遍历（根｜左｜右）的方式，在遇到null节点时，用"$"来代替。</li>
</ul>
<p>反序列化步骤：</p>
<ul>
<li>上述序列化的结果为<code>1 2 $ $ 3 4 $ $ 5 $ $</code></li>
<li>定义函数buildTree用于还原二叉树，传入序列化字符串转成的list数组。</li>
<li>逐个shift出list首项，构建当前子树的根节点，顺着list，构建顺序是根->左->右
<ul>
<li>如果弹出字符为$，则返回null</li>
<li>如果弹出字符为数值，则创建root节点，并递归构建root的左右子树，最后返回root。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> serialize = <span class="hljs-function">(<span class="hljs-params">root</span>) =></span> &#123;
  <span class="hljs-keyword">if</span>(root === <span class="hljs-literal">null</span>)&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'$'</span>;
  &#125;
  <span class="hljs-keyword">const</span> left = serialize(root.left);
  <span class="hljs-keyword">const</span> right = serialize(root.right);
  <span class="hljs-keyword">return</span> root.val + <span class="hljs-string">','</span> + left + <span class="hljs-string">','</span> + right;
&#125;;

<span class="hljs-keyword">const</span> deserialize = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> list = data.split(<span class="hljs-string">','</span>);
  
  <span class="hljs-keyword">const</span> buildTree = <span class="hljs-function">(<span class="hljs-params">list</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> rootVal = list.shift();
    <span class="hljs-keyword">if</span>(rootVal === <span class="hljs-string">'$'</span>)&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    &#125;
    <span class="hljs-keyword">const</span> root = <span class="hljs-keyword">new</span> TreeNode(rootVal);
    root.left = buildTree(list);
    root.right = buildTree(list);
    <span class="hljs-keyword">return</span> root;
  &#125;;
  <span class="hljs-keyword">return</span> buildTree(list);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-4">字符串的排列</h2>
<blockquote>
<p>剑指Offer 38.字符串的排列</p>
<p>难度：中等</p>
<p>leetcode地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fzi-fu-chuan-de-pai-lie-lcof%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/" ref="nofollow noopener noreferrer">leetcode-cn.com/problems/zi…</a></p>
</blockquote>
<p>输入一个字符串，打印出该字符串中字符的所有排列。</p>
<p>你可以任意顺序返回这个字符串数组，但里面不能有重复元素。</p>
<p>示例：</p>
<pre><code class="copyable">输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>限制：1 <= s的长度 <= 8</p>
<h2 data-id="heading-5">题解</h2>
<p>经典的回溯算法，本题求的是全排列+去重，排序使用回溯算法，去重这里直接采用Set，方便省事。经典的回溯算法，本题求的是全排列+去重，排序使用回溯算法，去重这里直接采用Set，方便省事。关于回溯算法理论这里推荐看Carl哥B站教学视频的<strong>带你学透回溯算法！（理论篇）</strong>，能够快速帮我们理解回溯算法的使用场景。</p>
<p>回溯算法（纯暴力的搜索）使用场景：组合、排列、切割、子集、棋盘</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">s</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;string[]&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> permutation = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
  <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();<span class="hljs-comment">// 用于去重</span>
  <span class="hljs-keyword">const</span> visit = &#123;&#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dfs</span>(<span class="hljs-params">path</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(path.length === s.length) <span class="hljs-keyword">return</span> res.add(path);<span class="hljs-comment">// 终止条件</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < s.length; i++) &#123;
      <span class="hljs-keyword">if</span> (!visit[i])&#123;
        visit[i] = <span class="hljs-literal">true</span>;<span class="hljs-comment">// 标记访问</span>
        dfs(path + s[i]);<span class="hljs-comment">// 递归</span>
        visit[i] = <span class="hljs-literal">false</span>;<span class="hljs-comment">// 回溯，将标记解除</span>
      &#125;
    &#125;
  &#125;
  dfs(<span class="hljs-string">''</span>);
  <span class="hljs-keyword">return</span> [...res];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>坚持每日一练！前端小萌新一枚，希望能点个<code>赞</code>哇～</p></div>  
</div>
            