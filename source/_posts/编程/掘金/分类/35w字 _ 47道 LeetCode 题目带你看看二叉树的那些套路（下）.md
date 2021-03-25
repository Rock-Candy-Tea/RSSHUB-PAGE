
---
title: '3.5w字 _ 47道 LeetCode 题目带你看看二叉树的那些套路（下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92d9ac903155447f906eb35672e1f513~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 21:44:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92d9ac903155447f906eb35672e1f513~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>前言：</strong></p>
<p>周末无聊，整理了一下之前做过的LeetCode上的<strong>二叉树</strong>相关的题目，也方便以后不断回顾，LeetCode的题目总是刷完之后感觉会了，过一段时间又忘了，还是要不断复盘。</p>
<p>全文约3.5w字，共47道题目，建议收藏慢慢看，有不对的地方欢迎大家指正！</p>
<p>掘金发文章有字数限制，所以分成了两篇，<strong>本文为下篇</strong> 欢迎关注之后的更新！</p>
<p><img alt="29f9f18e33714061b3a51333f00e00fe_tplv-k3u1fbpfcp-zoom-1.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92d9ac903155447f906eb35672e1f513~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">5. 经典题目：二叉树的操作</h3>
<h4 data-id="heading-1">（1）翻转二叉树</h4>
<p>翻转一棵二叉树。<strong>示例：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：
     <span class="hljs-number">4</span>
   /   \
  <span class="hljs-number">2</span>     <span class="hljs-number">7</span>
 / \   / \
<span class="hljs-number">1</span>   <span class="hljs-number">3</span> <span class="hljs-number">6</span>   <span class="hljs-number">9</span>

输出：
     <span class="hljs-number">4</span>
   /   \
  <span class="hljs-number">7</span>     <span class="hljs-number">2</span>
 / \   / \
<span class="hljs-number">9</span>   <span class="hljs-number">6</span> <span class="hljs-number">3</span>   <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过翻转之后，二叉树的每一个左右子孩子都发生了交换，所有可以使用递归来实现：遍历每一个结点，并将每一个结点的左右孩子进行交换。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> invertTree = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
   <span class="hljs-keyword">if</span>(!root)&#123;
       <span class="hljs-keyword">return</span> root
   &#125;
   <span class="hljs-comment">// 递归获取左右子结点</span>
   <span class="hljs-keyword">let</span> right = invertTree(root.right)
   <span class="hljs-keyword">let</span> left = invertTree(root.left)
   <span class="hljs-comment">// 交换左右子结点</span>
   root.right = left
   root.left =right
   <span class="hljs-keyword">return</span> root
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(N)，其中 N 为二叉树节点的数目。需要遍历二叉树中的每一个节点，对每个节点而言，在常数时间内交换其两棵子树。</li>
<li>空间复杂度：O(N)。使用的空间由递归栈的深度决定，它等于当前节点在二叉树中的高度。在平均情况下，二叉树的高度与节点个数为对数关系，即 O(logN)。而在最坏情况下，树形成链状，空间复杂度为 O(N)。</li>
</ul>
<h4 data-id="heading-2">（2）合并二叉树</h4>
<p>给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。示例 1:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: 
Tree <span class="hljs-number">1</span>                     Tree <span class="hljs-number">2</span>                  
          <span class="hljs-number">1</span>                         <span class="hljs-number">2</span>                             
         / \                       / \                            
        <span class="hljs-number">3</span>   <span class="hljs-number">2</span>                     <span class="hljs-number">1</span>   <span class="hljs-number">3</span>                        
       /                           \   \                      
      <span class="hljs-number">5</span>                             <span class="hljs-number">4</span>   <span class="hljs-number">7</span>                  
输出: 
合并后的树:
     <span class="hljs-number">3</span>
    / \
   <span class="hljs-number">4</span>   <span class="hljs-number">5</span>
  / \   \ 
 <span class="hljs-number">5</span>   <span class="hljs-number">4</span>   <span class="hljs-number">7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意: 合并必须从两个树的根节点开始。</p>
<p>这里可以使用递归的方式来计算，保持t1不便，将t2的节点往t1上加就可以了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">t1</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">t2</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> mergeTrees = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">t1, t2</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!t1 && t2)&#123;
        <span class="hljs-keyword">return</span> t2
    &#125;
    <span class="hljs-keyword">if</span>(t1 && !t2 || !t1 && !t2)&#123;
        <span class="hljs-keyword">return</span> t1
    &#125;

    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    <span class="hljs-keyword">return</span> t1
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(min(m,n))，其中 m 和 n 分别是两个二叉树的节点个数。对两个二叉树同时进行深度优先搜索，只有当两个二叉树中的对应节点都不为空时才会对该节点进行显性合并操作，因此被访问到的节点数不会超过较小的二叉树的节点数。</li>
<li>空间复杂度：O(min(m,n))，其中 m 和 n 分别是两个二叉树的节点个数。空间复杂度取决于递归调用的层数，递归调用的层数不会超过较小的二叉树的最大高度，最坏情况下，二叉树的高度等于节点数。</li>
</ul>
<h4 data-id="heading-3">（3）二叉树展开为链表</h4>
<p>给你二叉树的根结点 root ，请你将它展开为一个单链表：</p>
<p>展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。展开后的单链表应该与二叉树 <strong>先序遍历</strong> 顺序相同。</p>
<p>示例 1：
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efdb11b46bff4265b7d00952d5befe50~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：root = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">6</span>]
输出：[<span class="hljs-number">1</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">2</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">3</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">5</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">6</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：root = []
输出：[]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 3：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：root = [<span class="hljs-number">0</span>]
输出：[<span class="hljs-number">0</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<ul>
<li>树中结点数在范围 [0, 2000] 内</li>
<li>-100 <= Node.val <= 100</li>
</ul>
<p>进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？</p>
<p>题目中也说了，展开后的单链表与二叉树 <strong>先序遍历</strong> 顺序相同，所以我们可以先对二叉树进行先序遍历，然后将遍历的结果置位一条链表。这个链表相当于左子节点都是null，右子节点都是二叉树的值的二叉树。**</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) &#123;
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;void&#125;</span> </span>Do not return anything, modify root in-place instead.
 */</span>
<span class="hljs-keyword">var</span> flatten = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-comment">// 前序遍历</span>
    <span class="hljs-keyword">const</span> fn = <span class="hljs-function">(<span class="hljs-params">root</span>) =></span> &#123;
        <span class="hljs-keyword">if</span>(!root)&#123;
            <span class="hljs-keyword">return</span> 
        &#125;
        res.push(root)
        fn(root.left)
        fn(root.right)
    &#125;

    <span class="hljs-keyword">let</span> res = []
    fn(root)
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < res.length - <span class="hljs-number">1</span>; i++)&#123;
        res[i].left = <span class="hljs-literal">null</span>
        res[i].right = res[i + <span class="hljs-number">1</span>]
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中 n 是二叉树的节点数。前序遍历的时间复杂度是 O(n)，前序遍历之后，需要对每个节点更新左右子节点的信息，时间复杂度也是 O(n)。</li>
<li>空间复杂度：O(n)，其中 n 是二叉树的节点数。空间复杂度取决于栈（递归调用栈或者迭代中显性使用的栈）和存储前序遍历结果的列表的大小，栈内的元素个数不会超过 n，前序遍历列表中的元素个数是 n。</li>
</ul>
<h4 data-id="heading-4">（4）从前序与中序遍历序列构造二叉树</h4>
<p>根据一棵树的前序遍历与中序遍历构造二叉树。**注意：**你可以假设树中没有重复的元素。例如，给出</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">前序遍历 preorder = [<span class="hljs-number">3</span>,<span class="hljs-number">9</span>,<span class="hljs-number">20</span>,<span class="hljs-number">15</span>,<span class="hljs-number">7</span>]
中序遍历 inorder = [<span class="hljs-number">9</span>,<span class="hljs-number">3</span>,<span class="hljs-number">15</span>,<span class="hljs-number">20</span>,<span class="hljs-number">7</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回如下的二叉树：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-number">3</span>
   / \
  <span class="hljs-number">9</span>  <span class="hljs-number">20</span>
    /  \
   <span class="hljs-number">15</span>   <span class="hljs-number">7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先看下前序遍历和中序遍历的规律：</p>
<ul>
<li>前序遍历：根节点 + 左子树前序遍历 + 右子树前序遍历</li>
<li>中序遍历：左子树中序遍历 + 根节点 + 右字数中序遍历</li>
</ul>
<p>可以根据上面获得根据点判断，哪些是左子节点，哪些是右子节点，依次这样判断即可。</p>
<p>实现步骤如下：</p>
<ul>
<li>前序遍历找到根结点<code>root</code></li>
<li>找到<code>root</code>在中序遍历的位置 -> 左子树的长度和右子树的长度</li>
<li>截取左子树的中序遍历、右子树的中序遍历</li>
<li>截取左子树的前序遍历、右子树的前序遍历</li>
<li>递归重建二叉树</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">preorder</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">inorder</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> buildTree = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">preorder, inorder</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!inorder.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    <span class="hljs-keyword">let</span> tmp = preorder[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">let</span> mid = inorder.indexOf(tmp)
    
    <span class="hljs-keyword">let</span> root = <span class="hljs-keyword">new</span> TreeNode(tmp)
    root.left = buildTree(preorder.slice(<span class="hljs-number">1</span>,mid+<span class="hljs-number">1</span>),inorder.slice(<span class="hljs-number">0</span>,mid))
    root.right = buildTree(preorder.slice(mid+<span class="hljs-number">1</span>),inorder.slice(mid + <span class="hljs-number">1</span>))
    <span class="hljs-keyword">return</span> root
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>复杂度分析：</p>
<ul>
<li>时间复杂度：O(n)，其中 n 是树中的节点个数。</li>
<li>空间复杂度：O(n)，除去返回的答案需要的 O(n) 空间之外，还需要使用 O(n) 的空间存储哈希映射，以及 O(h)（其中 h 是树的高度）的空间表示递归时栈空间。这里 h<n，所以总空间复杂度为 O(n)。</li>
</ul>
<h4 data-id="heading-5">（5）从中序与后序遍历序列构造二叉树</h4>
<p>根据一棵树的中序遍历与后序遍历构造二叉树。注意：你可以假设树中没有重复的元素。例如，给出</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">中序遍历 inorder = [<span class="hljs-number">9</span>,<span class="hljs-number">3</span>,<span class="hljs-number">15</span>,<span class="hljs-number">20</span>,<span class="hljs-number">7</span>]
后序遍历 postorder = [<span class="hljs-number">9</span>,<span class="hljs-number">15</span>,<span class="hljs-number">7</span>,<span class="hljs-number">20</span>,<span class="hljs-number">3</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回如下的二叉树：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-number">3</span>
   / \
  <span class="hljs-number">9</span>  <span class="hljs-number">20</span>
    /  \
   <span class="hljs-number">15</span>   <span class="hljs-number">7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先看下中序遍历和后序遍历的规律：</p>
<ul>
<li>中序遍历：左子树中序遍历 + 根节点 + 右字数中序遍历</li>
<li>后序遍历：左子树后序遍历 + 右子树后序遍历 + 根节点</li>
</ul>
<p>这个题目的思路也是使用递归：</p>
<ul>
<li>可以看到，后序遍历数组的最后一个值是二叉树的根节点，也就是示例中的7</li>
<li>根据根节点的值，在中序遍历的数组中找到该值的索引，我就可以知道，3左边的是左子树的中序遍历的数组，3后面的是右子树的中序遍历的数组</li>
<li>根据根节点的值，在后续遍历数组中找到的该值得索引，就可以知道，0到该索引的的值都是左子树的后序遍历的数组，后面的数值就是右子树的后序遍历的数组（需要排除根节点）</li>
<li>根据上面得到的左右子树的中序遍历和后续遍历的结果进行递归操作</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">inorder</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">postorder</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> buildTree = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">inorder, postorder</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!inorder.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    <span class="hljs-keyword">let</span> len = postorder.length
    <span class="hljs-keyword">let</span> tmp = postorder[len-<span class="hljs-number">1</span>]
    <span class="hljs-keyword">let</span> mid = inorder.indexOf(tmp)
    
    <span class="hljs-keyword">let</span> root = <span class="hljs-keyword">new</span> TreeNode(tmp)
    root.left = buildTree(inorder.slice(<span class="hljs-number">0</span>,mid), postorder.slice(<span class="hljs-number">0</span>,mid))
    root.right = buildTree(inorder.slice(mid + <span class="hljs-number">1</span>), postorder.slice(mid,len-<span class="hljs-number">1</span>))
    <span class="hljs-keyword">return</span> root
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>复杂度分析：</p>
<ul>
<li>时间复杂度：O(n)，其中 n 是树中的节点个数。</li>
<li>空间复杂度：O(n)，除去返回的答案需要的 O(n) 空间之外，还需要使用 O(n) 的空间存储哈希映射，以及 O(h)（其中 h 是树的高度）的空间表示递归时栈空间。这里 h<n，所以总空间复杂度为 O(n)。</li>
</ul>
<h4 data-id="heading-6">（6）从前序与后序遍历序列构造二叉树</h4>
<p>返回与给定的前序和后序遍历匹配的任何二叉树。其中，pre 和 post 遍历中的值是不同的正整数。示例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：pre = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">3</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>], post = [<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">2</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">3</span>,<span class="hljs-number">1</span>]
输出：[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<ul>
<li>1 <= pre.length == post.length <= 30</li>
<li>pre[] 和 post[] 都是 1, 2, …, pre.length 的排列</li>
<li>每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。</li>
</ul>
<p>先看下前序遍历和后序遍历的规律：</p>
<ul>
<li>前序遍历：根节点 + 左子树前序遍历 + 右子树前序遍历</li>
<li>后序遍历：左子树后序遍历 + 右子树后序遍历 + 根节点</li>
</ul>
<p>这个题目的思路也是使用递归：</p>
<ul>
<li>根据前序遍历的特点，就可以知道1是二叉树的根节点，那么紧跟其后的应该就是左节点，也就是2。</li>
<li>在后序遍历中找到2对应的位置，我们就可以知道2及之前的数都是该二叉树的左节点的后序遍历数组，之后的数都是二叉树的右节点的后序遍历数组（需要除去根节点）</li>
<li>根据左子树的长度在先序遍历中找到左子树和右子树的前序遍历值。</li>
<li>进行递归操作，得出最后的二叉树。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">pre</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">post</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> constructFromPrePost = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">pre, post</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!pre.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    <span class="hljs-keyword">let</span> tmp = pre[<span class="hljs-number">0</span>];
    <span class="hljs-keyword">let</span> index = post.indexOf(pre[<span class="hljs-number">1</span>]);
    <span class="hljs-keyword">let</span> root = <span class="hljs-keyword">new</span> TreeNode(tmp);
    
    root.left = constructFromPrePost(pre.slice(<span class="hljs-number">1</span>,index+<span class="hljs-number">2</span>),post.slice(<span class="hljs-number">0</span>,index+<span class="hljs-number">1</span>));
    root.right = constructFromPrePost(pre.slice(index+<span class="hljs-number">2</span>),post.slice(index+<span class="hljs-number">1</span>,post.length-<span class="hljs-number">1</span>));
    <span class="hljs-keyword">return</span> root;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>复杂度分析：</p>
<ul>
<li>时间复杂度：O(n)，其中 n 是树中的节点个数。</li>
<li>空间复杂度：O(n)，除去返回的答案需要的 O(n) 空间之外，还需要使用 O(n) 的空间存储哈希映射，以及 O(h)（其中 h 是树的高度）的空间表示递归时栈空间。这里 h<n，所以总空间复杂度为 O(n)。</li>
</ul>
<h4 data-id="heading-7">（7）填充每个节点的下一个右侧节点指针</h4>
<p>给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">struct Node &#123;
  int val;
  Node *left;
  Node *right;
  Node *next;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。初始状态下，所有 next 指针都被设置为 NULL。</p>
<p>示例：
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e2a7a3ed35140219e12ce85997fd5b4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"1"</span>,<span class="hljs-string">"left"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"2"</span>,<span class="hljs-string">"left"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"3"</span>,<span class="hljs-string">"left"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"next"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"right"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"val"</span>:<span class="hljs-number">4</span>&#125;,<span class="hljs-string">"next"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"right"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"4"</span>,<span class="hljs-string">"left"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"next"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"right"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"val"</span>:<span class="hljs-number">5</span>&#125;,<span class="hljs-string">"val"</span>:<span class="hljs-number">2</span>&#125;,<span class="hljs-string">"next"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"right"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"5"</span>,<span class="hljs-string">"left"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"6"</span>,<span class="hljs-string">"left"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"next"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"right"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"val"</span>:<span class="hljs-number">6</span>&#125;,<span class="hljs-string">"next"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"right"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"7"</span>,<span class="hljs-string">"left"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"next"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"right"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"val"</span>:<span class="hljs-number">7</span>&#125;,<span class="hljs-string">"val"</span>:<span class="hljs-number">3</span>&#125;,<span class="hljs-string">"val"</span>:<span class="hljs-number">1</span>&#125;

输出：&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"1"</span>,<span class="hljs-string">"left"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"2"</span>,<span class="hljs-string">"left"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"3"</span>,<span class="hljs-string">"left"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"next"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"4"</span>,<span class="hljs-string">"left"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"next"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"5"</span>,<span class="hljs-string">"left"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"next"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"6"</span>,<span class="hljs-string">"left"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"next"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"right"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"val"</span>:<span class="hljs-number">7</span>&#125;,<span class="hljs-string">"right"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"val"</span>:<span class="hljs-number">6</span>&#125;,<span class="hljs-string">"right"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"val"</span>:<span class="hljs-number">5</span>&#125;,<span class="hljs-string">"right"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"val"</span>:<span class="hljs-number">4</span>&#125;,<span class="hljs-string">"next"</span>:&#123;<span class="hljs-string">"$id"</span>:<span class="hljs-string">"7"</span>,<span class="hljs-string">"left"</span>:&#123;<span class="hljs-string">"$ref"</span>:<span class="hljs-string">"5"</span>&#125;,<span class="hljs-string">"next"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"right"</span>:&#123;<span class="hljs-string">"$ref"</span>:<span class="hljs-string">"6"</span>&#125;,<span class="hljs-string">"val"</span>:<span class="hljs-number">3</span>&#125;,<span class="hljs-string">"right"</span>:&#123;<span class="hljs-string">"$ref"</span>:<span class="hljs-string">"4"</span>&#125;,<span class="hljs-string">"val"</span>:<span class="hljs-number">2</span>&#125;,<span class="hljs-string">"next"</span>:<span class="hljs-literal">null</span>,<span class="hljs-string">"right"</span>:&#123;<span class="hljs-string">"$ref"</span>:<span class="hljs-string">"7"</span>&#125;,<span class="hljs-string">"val"</span>:<span class="hljs-number">1</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。</p>
<p>提示：</p>
<ul>
<li>你只能使用常量级额外空间。</li>
<li>使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度</li>
</ul>
<p>这里我们使用递归的方式来解决这个问题。我们对二叉树进行先序遍历。我们要讨论两种情况：<strong>同一父节点的左右节点相连</strong> 和 <strong>非同一父节点的左右节点相连</strong>，下面来看以下：</p>
<ul>
<li>第一步，对于同一父节点的左右节点相连，将左节点的值指向右节点</li>
<li>第二部，对于非同一父节点的左右节点相连，以图中的5和6为例，我们通过5的父节点2，找到他的右节点3，再通过3找到其左节点，并将5和相连3相连。</li>
</ul>
<p>对于上面的步骤，进行递归，直至遍历完所有的节点。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * // Definition for a Node.
 * function Node(val, left, right, next) &#123;
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * &#125;;
 */</span>

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Node&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;Node&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> connect = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!root) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
<span class="hljs-comment">// 同一父节点的左右节点相连</span>
    <span class="hljs-keyword">if</span>(root.left && root.right)&#123;
        root.left.next = root.right
    &#125;
<span class="hljs-comment">// 非同一父节点的左右节点相连</span>
    <span class="hljs-keyword">if</span>(root.right && root.next && root.next.left)&#123;
        root.right.next = root.next.left
    &#125;
<span class="hljs-comment">// 递归遍历</span>
    connect(root.left)
    connect(root.right)
    <span class="hljs-keyword">return</span> root
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>
<p>时间复杂度：O(N)，其中n是二叉树的节点的数量，每个节点只访问一次。</p>
</li>
<li>
<p>空间复杂度：O(1)，不需要存储额外的节点。</p>
</li>
</ul>
<h4 data-id="heading-8">（8）填充每个节点的下一个右侧节点指针 II</h4>
<p>给定一个二叉树：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">struct Node &#123;
  int val;
  Node *left;
  Node *right;
  Node *next;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 <code>NULL</code>。初始状态下，所有 next 指针都被设置为 <code>NULL</code>。</p>
<p><strong>进阶：</strong></p>
<ul>
<li>你只能使用常量级额外空间。</li>
<li>使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。</li>
</ul>
<p><strong>示例：</strong>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6386396747340f09a57fd8ed714affd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>输入</strong>：root = [1,2,3,4,5,null,7]
<strong>输出：</strong>[1,#,2,3,#,4,5,7,#]
<strong>解释：</strong> 给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。</p>
<p><strong>提示：</strong></p>
<ul>
<li>树中的节点数小于 <code>6000</code></li>
<li><code>-100 <= node.val <= 100</code></li>
</ul>
<p>对于这道题目，我们可以对树进行层序遍历，树的层序遍历是基于广度优先遍历的，按照层的顺序进行遍历，我们需要舒适话一个队列queue，这个队列中保存着当前层的节点。</p>
<p>当队列不为空的时候就记录当前队列的的长度len，当遍历这一层的时候，修改这一层节点的 next 指针，这样就可以把每一层都组织成链表。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * // Definition for a Node.
 * function Node(val, left, right, next) &#123;
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * &#125;;
 */</span>

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Node&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;Node&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> connect = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!root) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    &#125;
    <span class="hljs-keyword">const</span> queue = [root];
    <span class="hljs-keyword">while</span> (queue.length) &#123;
        <span class="hljs-keyword">const</span> len = queue.length;
        <span class="hljs-keyword">let</span> last = <span class="hljs-literal">null</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i <= len; ++i) &#123;
            <span class="hljs-keyword">let</span> node = queue.shift();
            <span class="hljs-keyword">if</span> (node.left) &#123;
                queue.push(node.left);
            &#125;
            <span class="hljs-keyword">if</span> (node.right) &#123;
                queue.push(node.right);
            &#125;
            <span class="hljs-keyword">if</span> (i !== <span class="hljs-number">1</span>) &#123;
                last.next = node;
            &#125;
            last = node;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> root;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(N)。其中N是树的节点数，我们需要遍历这棵树上所有的点，时间复杂度为 O(N)。</li>
<li>空间复杂度：O(N)。其中N是树的节点数，我们需要初始化一个队列，它的长度最大不超过树的节点数。</li>
</ul>
<h4 data-id="heading-9">（9）二叉树的序列化与反序列化</h4>
<p>序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。</p>
<p>请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。</p>
<p>示例:你可以将以下二叉树：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-number">1</span>
   / \
  <span class="hljs-number">2</span>   <span class="hljs-number">3</span>
     / \
    <span class="hljs-number">4</span>   <span class="hljs-number">5</span>
    
序列化为 <span class="hljs-string">"[1,2,3,null,null,4,5]"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。</p>
<p>说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。</p>
<p>对于这道二叉树的题目，我们能想到的最直接的方式就是深度优先宾利和广度优先遍历，这里就分别用两种方式来解答。</p>
<p><strong>深度优先遍历：</strong></p>
<ul>
<li>首先是序列化二叉树，可以定义一个遍历方法，先访问根节点，再访问左节点，最后访问右节点，将每个节点的值都存入数组，如果是null也要存入数组。</li>
<li>之后是反序列化二叉树，也就是将数组转化为二叉树，因为数组是二叉树先序遍历的结果，所以我们就可以遍历数组，然后按照根节点、左子树、右子树的顺序复原二叉树</li>
</ul>
<p><strong>广度优先遍历：</strong></p>
<ul>
<li>首先是序列化二叉树，广度优先遍历的遍历顺序是按照层级从上往下遍历（层序遍历），所以我们可以利用队列先进先出的特性，维持一个数组。先将根节点入队，再将左节点和右节点入队，递归即可。</li>
<li>之后是反序列化二叉树，我们可以从数组中取出第一个元素生成根节点，将根节点加入队列，循环队列，将根节点的左右子树分别加入队列，循环此操作，直至队列为空。其中队列中的节点用于后面遍历其左右子节点。</li>
</ul>
<p><strong>1）深度优先遍历：</strong></p>
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
    <span class="hljs-keyword">const</span> result = []
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">traverseNode</span>(<span class="hljs-params">node</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(node === <span class="hljs-literal">null</span>)&#123;
            result.push(<span class="hljs-literal">null</span>)
        &#125;<span class="hljs-keyword">else</span>&#123;
            result.push(node.val)
            traverseNode(node.left)
            traverseNode(node.right)
        &#125;
    &#125;
    traverseNode(root)
    <span class="hljs-keyword">return</span> result
&#125;;

<span class="hljs-comment">/**
 * Decodes your encoded data to tree.
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">data</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> deserialize = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-keyword">const</span> len = data.length
    <span class="hljs-keyword">if</span>(!len)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">structure</span> (<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 递归停止条件</span>
        <span class="hljs-keyword">if</span>(i >= len)&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
        &#125;
        <span class="hljs-keyword">const</span> val = data[i]
        i++
        <span class="hljs-keyword">if</span>(val === <span class="hljs-literal">null</span>)&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
        &#125;
        <span class="hljs-keyword">const</span> node = <span class="hljs-keyword">new</span> TreeNode(val)
        node.left = structure()
        node.right = structure()
        <span class="hljs-keyword">return</span> node
    &#125;
    <span class="hljs-keyword">return</span> structure()
&#125;;

<span class="hljs-comment">/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：在序列化和反序列化函数中，我们只访问每个节点一次，因此时间复杂度为 O(n)，其中 n 是节点数，即树的大小。</li>
<li>空间复杂度：在序列化和反序列化函数中，我们递归会使用栈空间，故渐进空间复杂度为 O(n)。</li>
</ul>
<p><strong>2）广度优先遍历：</strong></p>
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
    <span class="hljs-keyword">if</span>(!root)&#123;
        <span class="hljs-keyword">return</span> []
    &#125;
    <span class="hljs-keyword">const</span> result = []
    <span class="hljs-keyword">const</span> queue = []
    queue.push(root)

    <span class="hljs-keyword">let</span> node ;
    <span class="hljs-keyword">while</span>(queue.length)&#123;
        node = queue.shift()
        result.push(node ? node.val : <span class="hljs-literal">null</span>)
        <span class="hljs-keyword">if</span>(node)&#123;
            queue.push(node.left)
            queue.push(node.right)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> result
&#125;;

<span class="hljs-comment">/**
 * Decodes your encoded data to tree.
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">data</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> deserialize = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-keyword">const</span> len = data.length
    <span class="hljs-keyword">if</span>(!len)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-keyword">const</span> root = <span class="hljs-keyword">new</span> TreeNode(data.shift())
    <span class="hljs-keyword">const</span> queue = [root]
    <span class="hljs-keyword">while</span>(queue.length)&#123;
        <span class="hljs-comment">// 取出将要遍历的节点</span>
        <span class="hljs-keyword">const</span> node = queue.shift()
        <span class="hljs-keyword">if</span>(!data.length)&#123;
            <span class="hljs-keyword">break</span>
        &#125;
        <span class="hljs-comment">// 还原左节点</span>
        <span class="hljs-keyword">const</span> leftVal = data.shift()
        <span class="hljs-keyword">if</span>(leftVal === <span class="hljs-literal">null</span>)&#123;
            node.left = <span class="hljs-literal">null</span>
        &#125;<span class="hljs-keyword">else</span>&#123;
            node.left = <span class="hljs-keyword">new</span> TreeNode(leftVal)
            queue.push(node.left)
        &#125;
        <span class="hljs-keyword">if</span>(!data.length)&#123;
            <span class="hljs-keyword">break</span>
        &#125;

        <span class="hljs-comment">// 还原右节点</span>
        <span class="hljs-keyword">const</span> rightVal = data.shift()
        <span class="hljs-keyword">if</span>(rightVal === <span class="hljs-literal">null</span>)&#123;
            node.right = <span class="hljs-literal">null</span>
        &#125;<span class="hljs-keyword">else</span>&#123;
            node.right = <span class="hljs-keyword">new</span> TreeNode(rightVal)
            queue.push(node.right)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> root
&#125;;

<span class="hljs-comment">/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：在序列化和反序列化函数中，我们只访问每个节点一次，因此时间复杂度为 O(n)，其中 n 是节点数，即树的大小。</li>
<li>空间复杂度：在序列化和反序列化函数中，我们递归会使用栈空间，故渐进空间复杂度为 O(n)。</li>
</ul>
<h3 data-id="heading-10">6. 经典题目：二叉搜索树的属性</h3>
<h4 data-id="heading-11">（1）验证二叉搜索树</h4>
<p>给定一个二叉树，判断其是否是一个有效的二叉搜索树。假设一个二叉搜索树具有如下特征：</p>
<ul>
<li>节点的左子树只包含<strong>小于</strong>当前节点的数。</li>
<li>节点的右子树只包含<strong>大于</strong>当前节点的数。</li>
<li>所有左子树和右子树自身必须也是二叉搜索树。</li>
</ul>
<p><strong>示例 1:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入:
    <span class="hljs-number">2</span>
   / \
  <span class="hljs-number">1</span>   <span class="hljs-number">3</span>
输出: <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入:
    <span class="hljs-number">5</span>
   / \
  <span class="hljs-number">1</span>   <span class="hljs-number">4</span>
     / \
    <span class="hljs-number">3</span>   <span class="hljs-number">6</span>
输出: <span class="hljs-literal">false</span>
解释: 输入为: [<span class="hljs-number">5</span>,<span class="hljs-number">1</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">3</span>,<span class="hljs-number">6</span>]。
     根节点的值为 <span class="hljs-number">5</span> ，但是其右子节点值为 <span class="hljs-number">4</span> 。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先使用DFS（深度优先遍历）递归遍历整棵树，检验每棵子树中是否都满足 <strong>左 < 根 < 右</strong> 这样的关系。</p>
<p>设定两个值：最大值和最小值分别为正无穷和负无穷，然后通过判断左孩子的值是否小于根节点，右孩子的值是否大于根节点来断定该二叉树是否是二叉搜索树。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125; 
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;boolean&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> isValidBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dfs</span>(<span class="hljs-params">root, minValue, maxValue</span>)</span>&#123;
       <span class="hljs-comment">// 判断树为空的情况</span>
       <span class="hljs-keyword">if</span>(!root)&#123;
           <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
       &#125;
       <span class="hljs-comment">// 关键性的判断条件：左 < 根 < 右</span>
       <span class="hljs-keyword">if</span>(root.val <= minValue || root.val >= maxValue)&#123;
           <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
       &#125;
       <span class="hljs-comment">// 遍历左子树和右子树</span>
       <span class="hljs-keyword">return</span> dfs(root.left, minValue, root.val)&&dfs(root.right, root.val, maxValue)
   &#125;
   <span class="hljs-comment">// 对dfs遍历进行初始化</span>
   <span class="hljs-keyword">return</span> dfs(root, -<span class="hljs-literal">Infinity</span>, <span class="hljs-literal">Infinity</span>)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)：在递归调用的时候二叉树的每个节点最多被访问一次，因此时间复杂度为 O(n)。</li>
<li>空间复杂度：O(n)：递归函数在递归过程中需要为每一层递归函数分配栈空间，所以这里需要额外的空间且该空间取决于递归的深度，即二叉树的高度。最坏情况下二叉树为一条链，树的高度为 nn ，递归最深达到 nn 层，故最坏情况下空间复杂度为 O(n)。</li>
</ul>
<p><strong>【方法二】中序遍历</strong>
使用二叉树的中序遍历来判断。我们知道：二叉搜索树的中序遍历是有序的。所以，直接对二叉树进行中序遍历，将得出的数组进行遍历，判断这个数组是否是有序的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;boolean&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> isValidBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
   <span class="hljs-keyword">const</span> queue = []
   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dfs</span>(<span class="hljs-params">root</span>)</span>&#123;
       <span class="hljs-keyword">if</span>(!root)&#123;
           <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
       &#125;
       <span class="hljs-keyword">if</span>(root.left)&#123;
           dfs(root.left)
       &#125;
       <span class="hljs-keyword">if</span>(root)&#123;
           queue.push(root.val)
       &#125;
       <span class="hljs-keyword">if</span>(root.right)&#123;
           dfs(root.right)
       &#125;
   &#125;
   dfs(root)
   <span class="hljs-comment">// 判断遍历的结果是否有序</span>
   <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i<queue.length-<span class="hljs-number">1</span>; i++)&#123;
       <span class="hljs-keyword">if</span>(queue[i] >= queue[i+<span class="hljs-number">1</span>])&#123;
           <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
       &#125;
   &#125;
   <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度 : O(n)，其中 n为二叉树的节点个数。二叉树的每个节点最多被访问一次，因此时间复杂度为 O(n)。</li>
<li>空间复杂度 : O(n)，其中 n为二叉树的节点个数。栈最多存储 n个节点，因此需要额外的 O(n)的空间。</li>
</ul>
<h4 data-id="heading-12">（2）二叉搜索树中第k小的元素</h4>
<p>给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。说明：你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。</p>
<p>示例 1:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: root = [<span class="hljs-number">3</span>,<span class="hljs-number">1</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">2</span>], k = <span class="hljs-number">1</span>
   <span class="hljs-number">3</span>
  / \
 <span class="hljs-number">1</span>   <span class="hljs-number">4</span>
  \
   <span class="hljs-number">2</span>
输出: <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: root = [<span class="hljs-number">5</span>,<span class="hljs-number">3</span>,<span class="hljs-number">6</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">1</span>], k = <span class="hljs-number">3</span>
       <span class="hljs-number">5</span>
      / \
     <span class="hljs-number">3</span>   <span class="hljs-number">6</span>
    / \
   <span class="hljs-number">2</span>   <span class="hljs-number">4</span>
  /
 <span class="hljs-number">1</span>
输出: <span class="hljs-number">3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？</p>
<p>我们知道，二叉搜索树的左节点小于其父节点，右节点小于其右节点。这样二叉搜索树的中序遍历就是一个从小到大的有序序列。我们可以根据这个特性进行解答。</p>
<p><strong>递归：</strong> 对二叉搜索树进行中序遍历，遍历的原则就是先遍历左子树，然后遍历根节点，最后遍历左子树。在遍历过程中，将遍历的结果不断存入数组中，当遍历到第k个元素的时候，就终止遍历。</p>
<p><strong>迭代：</strong> 递归的方法也是利用的二叉搜索树的中序遍历：</p>
<ol>
<li>初始化一个栈暂存树的节点</li>
<li>先遍历根节点，再遍历左子树，并保存在栈中</li>
<li>遍历完左子树之后，将栈中的元素的出栈，这样顺序就反过来了，变成了先成遍历的根节点，再遍历的左子树</li>
<li>在遍历的过程中，每遍历一次k就减一</li>
<li>遍历完左子树之后再遍历右子树</li>
<li>不断循环，直到k为0位置，返回当前的节点值。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) &#123;
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">k</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>

<span class="hljs-comment">// 递归的实现：</span>
<span class="hljs-keyword">var</span> kthSmallest = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, k</span>) </span>&#123;
    <span class="hljs-keyword">const</span> result = []
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">travel</span>(<span class="hljs-params">node</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(result.length >= k) <span class="hljs-keyword">return</span> 
        <span class="hljs-keyword">if</span>(node.left)&#123;
            travel(node.left)
        &#125;
        result.push(node.val)
        <span class="hljs-keyword">if</span>(node.right)&#123;
            travel(node.right)
        &#125;
    &#125;
    travel(root)
    <span class="hljs-keyword">return</span> result[k - <span class="hljs-number">1</span>]
&#125;;

<span class="hljs-comment">// 迭代的实现：</span>
<span class="hljs-keyword">let</span> kthSmallest = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, k</span>) </span>&#123;
    <span class="hljs-keyword">let</span> stack = []
    <span class="hljs-keyword">let</span> node = root
   
    <span class="hljs-keyword">while</span>(node || stack.length) &#123;
        <span class="hljs-comment">// 遍历左子树</span>
        <span class="hljs-keyword">while</span>(node) &#123;
            stack.push(node)
            node = node.left
        &#125;
     
        node = stack.pop()
        <span class="hljs-keyword">if</span>(--k === <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">return</span> node.val
        &#125;
        node = node.right
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>递归的复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中n是二叉树的节点数，需要遍历了整个树。</li>
<li>空间复杂度：O(n)，用了一个数组存储中序序列。</li>
</ul>
<p><strong>迭代的复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(H+k)，其中 H 指的是树的高度，由于开始遍历之前，要先向下达到叶，当树是一个平衡树时：复杂度为 O(logN+k)。当树是一个不平衡树时：复杂度为 O(N+k)，此时所有的节点都在左子树。</li>
<li>空间复杂度：O(H+k)。当树是一个平衡树时：O(logN+k)。当树是一个非平衡树时：O(N+k)。</li>
</ul>
<h4 data-id="heading-13">（3）二叉搜索树的第k大节点</h4>
<p>给定一棵二叉搜索树，请找出其中第k大的节点。</p>
<p><strong>示例 1:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: root = [<span class="hljs-number">3</span>,<span class="hljs-number">1</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">2</span>], k = <span class="hljs-number">1</span>
   <span class="hljs-number">3</span>
  / \
 <span class="hljs-number">1</span>   <span class="hljs-number">4</span>
  \
   <span class="hljs-number">2</span>
输出: <span class="hljs-number">4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: root = [<span class="hljs-number">5</span>,<span class="hljs-number">3</span>,<span class="hljs-number">6</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">1</span>], k = <span class="hljs-number">3</span>
       <span class="hljs-number">5</span>
      / \
     <span class="hljs-number">3</span>   <span class="hljs-number">6</span>
    / \
   <span class="hljs-number">2</span>   <span class="hljs-number">4</span>
  /
 <span class="hljs-number">1</span>
输出: <span class="hljs-number">4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>限制：</strong> 1 ≤ k ≤ 二叉搜索树元素个数</p>
<p>我们知道，二叉搜索树的中序遍历的结果是一个有大到小的数组，所以我们可以倒中序遍历，然后将第结果的第k大节点返回即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">k</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> kthLargest = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, k</span>) </span>&#123;
    <span class="hljs-keyword">let</span> res = []

    <span class="hljs-keyword">const</span> dfs = <span class="hljs-function">(<span class="hljs-params">root</span>) =></span> &#123;
        <span class="hljs-keyword">if</span>(!root)&#123;
            <span class="hljs-keyword">return</span> 
        &#125;

        dfs(root.right)
        res.push(root.val)
        dfs(root.left)
    &#125;
    dfs(root)

    <span class="hljs-keyword">return</span> res[k - <span class="hljs-number">1</span>]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度 O(n)，最差的情况下，也就是当树退化为链表时（全部为右子节点），无论 k 的值大小，递归深度都为 n ，占用 O(n) 时间；</li>
<li>空间复杂度 O(n)，最差的情况下，也就是当树退化为链表时（全部为右子节点），系统使用 O(n) 大小的栈空间。</li>
</ul>
<h4 data-id="heading-14">（4）二叉搜索树的最小绝对差</h4>
<p>给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。示例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：

   <span class="hljs-number">1</span>
    \
     <span class="hljs-number">3</span>
    /
   <span class="hljs-number">2</span>

输出：
<span class="hljs-number">1</span>

解释：
最小绝对差为 <span class="hljs-number">1</span>，其中 <span class="hljs-number">2</span> 和 <span class="hljs-number">1</span> 的差的绝对值为 <span class="hljs-number">1</span>（或者 <span class="hljs-number">2</span> 和 <span class="hljs-number">3</span>）。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：树中至少有 2 个节点。</p>
<p>这道题目比较简单，先回忆一下二叉搜索树的特征：左子树的值始终小于父节点的值，右子树的值始终大于父节点的值。还有很重要的一点：在二叉搜索树的遍历中，中序遍历出来的结果是一个升序的数组。</p>
<p>那我们就可以进行中序遍历，并比较相邻的节点的值，始终保持结果是当前最小的值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> getMinimumDifference = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-keyword">let</span> pre = <span class="hljs-literal">null</span>
    <span class="hljs-keyword">let</span> min = <span class="hljs-literal">Infinity</span>
    
    <span class="hljs-keyword">let</span> inOrderTravel = <span class="hljs-function">(<span class="hljs-params">root</span>) =></span> &#123;
        <span class="hljs-keyword">if</span>(root)&#123;
            inOrderTravel(root.left)
            <span class="hljs-keyword">if</span>(pre)&#123;
                min = <span class="hljs-built_in">Math</span>.abs(root.val - pre.val) < min ? <span class="hljs-built_in">Math</span>.abs(root.val - pre.val) : min
            &#125;
            pre = root
            inOrderTravel(root.right)
        &#125;
    &#125;
    inOrderTravel(root)
    <span class="hljs-keyword">return</span> min
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中 n 为二叉搜索树节点数。每个节点在中序遍历中都会被访问一次且只会被访问一次，因此总时间复杂度为 O(n)。</li>
<li>空间复杂度：O(n)。递归函数的空间复杂度取决于递归的栈深度，而栈深度在二叉搜索树为一条链的情况下会达到 O(n) 级别。</li>
</ul>
<h4 data-id="heading-15">（5）二叉搜索树中的众数</h4>
<p>给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。假定 BST 有如下定义：</p>
<ul>
<li>结点左子树中所含结点的值小于等于当前结点的值</li>
<li>结点右子树中所含结点的值大于等于当前结点的值</li>
<li>左子树和右子树都是二叉搜索树</li>
</ul>
<p>例如：给定 BST <code>[1,null,2,2]</code>,</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-number">1</span>
    \
     <span class="hljs-number">2</span>
    /
   <span class="hljs-number">2</span>
返回[<span class="hljs-number">2</span>].
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示</strong>：如果众数超过1个，不需考虑输出顺序
<strong>进阶：</strong> 你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）</p>
<p>对于这道题目，我们可以对二叉树进行深度优先遍历，在遍历过程中，初始化一个max，用来保存当前元素出现的最大的次数，将二叉树值与对应的次数保存在一个map中，最后我们遍历一遍这个map，将所有次数与max相等的值都保存在res中即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number[]&#125;</span></span>
 */</span>

<span class="hljs-keyword">var</span> findMode = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-keyword">let</span> map = &#123;&#125;, max = <span class="hljs-number">0</span>, res = []

    <span class="hljs-keyword">const</span> dfs = <span class="hljs-function">(<span class="hljs-params">root</span>) =></span> &#123;
        <span class="hljs-keyword">if</span>(!root)&#123;
            <span class="hljs-keyword">return</span> []
        &#125;
        map[root.val] ? map[root.val] += <span class="hljs-number">1</span> : map[root.val] = <span class="hljs-number">1</span>;

        max = <span class="hljs-built_in">Math</span>.max(max, map[root.val])
        dfs(root.left)
        dfs(root.right)
    &#125;
    dfs(root)
    
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> map)&#123;
        <span class="hljs-keyword">if</span>(max === map[key])&#123;
            res.push(key)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> res
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中n是这棵树的节点数量，我们需要遍历整棵树。</li>
<li>空间复杂度：O(n)，其中n是这棵树的节点数量，这里需要的是递归的栈空间的空间代价。</li>
</ul>
<h3 data-id="heading-16">7. 经典题目：二叉搜索树的操作</h3>
<h4 data-id="heading-17">（1）将有序数组转换为二叉搜索树</h4>
<p>将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。本题中，一个高度平衡二叉树是指一个二叉树_每个节点 _的左右两个子树的高度差的绝对值不超过 1。
<strong>示例：</strong> 给定有序数组: [-10,-3,0,5,9]，一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">      <span class="hljs-number">0</span>
     / \
   -<span class="hljs-number">3</span>   <span class="hljs-number">9</span>
   /   /
 -<span class="hljs-number">10</span>  <span class="hljs-number">5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>二分递归实现：</strong>
将数组的值转化为一个高度平衡的二叉搜索树，我们只要找到中间的元素作为根节点，然后将中间元素的左边和右边分别二分，找出中间值作为子树的根节点，重复上述操作，直到遍历完整个数组为止即可。</p>
<ul>
<li>当数组长度为奇数时，以中间值作为根节点，形成的平衡二叉搜索树的两侧差值为0。</li>
<li>当数组长度为偶数时，可以取中间两个元素的任意一个作为根节点的值，这样形成的平衡二叉树的两侧差值的绝对值为1。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> sortedArrayToBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
   <span class="hljs-keyword">if</span>(!nums.length)&#123;
       <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
   &#125;
   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bst</span>(<span class="hljs-params">low, high</span>)</span>&#123;
       <span class="hljs-comment">// 遍历结束条件</span>
       <span class="hljs-keyword">if</span>(low > high)&#123;
           <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
       &#125;
       <span class="hljs-comment">// 取出当前子序列的中间元素的索引值</span>
       <span class="hljs-keyword">const</span> mid = <span class="hljs-built_in">Math</span>.floor(low+(high-low)/<span class="hljs-number">2</span>)
       <span class="hljs-comment">// 将中间元素的值作为当前子树的根节点</span>
       <span class="hljs-keyword">const</span> cur = <span class="hljs-keyword">new</span> TreeNode(nums[mid])
       <span class="hljs-comment">// 递归构建左子树</span>
       cur.left = bst(low, mid-<span class="hljs-number">1</span>)
       <span class="hljs-comment">// 递归构建右子树</span>
       cur.right = bst(mid+<span class="hljs-number">1</span>, high)
       <span class="hljs-keyword">return</span> cur
   &#125;
   <span class="hljs-keyword">return</span> bst(<span class="hljs-number">0</span>, nums.length-<span class="hljs-number">1</span>)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度： O(log n)：通过二分查找的方式递归查询了树的所有子节点。查询花费 O(log n) 的时间。</li>
<li>空间复杂度： O(n)：每次递归都需要创建新的临时空间，空间复杂度 O(n)。</li>
</ul>
<h4 data-id="heading-18">（2）二叉树搜索树中的搜索</h4>
<p>给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。例如，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">给定二叉搜索树:
    <span class="hljs-number">4</span>
   / \
  <span class="hljs-number">2</span>   <span class="hljs-number">7</span>
 / \
<span class="hljs-number">1</span>   <span class="hljs-number">3</span>
和值: <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你应该返回如下子树:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-number">2</span>     
 / \   
<span class="hljs-number">1</span>   <span class="hljs-number">3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">val</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>

<span class="hljs-comment">// 迭代的实现：</span>
<span class="hljs-keyword">var</span> searchBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, val</span>) </span>&#123;
   <span class="hljs-keyword">while</span>(root)&#123;
       <span class="hljs-keyword">if</span>(root.val === val)&#123;
           <span class="hljs-keyword">return</span> root
       &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(root.val <val)&#123;
           root = root.right
       &#125;<span class="hljs-keyword">else</span>&#123;
           root = root.left
       &#125;
   &#125;
   <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
&#125;;

<span class="hljs-comment">// 递归的实现：</span>
<span class="hljs-keyword">var</span> searchBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, val</span>) </span>&#123;
   <span class="hljs-keyword">if</span>(!root)&#123;
       <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
   &#125;
   <span class="hljs-keyword">if</span>(root.val === val)&#123;
       <span class="hljs-keyword">return</span> root
   &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(root.val < val)&#123;
       <span class="hljs-keyword">return</span> searchBST(root.right, val)
   &#125;<span class="hljs-keyword">else</span>&#123;
       <span class="hljs-keyword">return</span> searchBST(root.left, val)
   &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>迭代的复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(H)，其中 H 是树高。平均时间复杂度为 O(logN)，最坏时间复杂度为 O(N)。</li>
<li>空间复杂度：O(1)，恒定的额外空间。</li>
</ul>
<p><strong>递归的复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(H)，其中 H 是树高。平均时间复杂度为 O(logN)，最坏时间复杂度为 O(N)。</li>
<li>空间复杂度：O(H)，递归栈的深度为 H。平均情况下深度为 O(logN)，最坏情况下深度为 O(N)。</li>
</ul>
<h4 data-id="heading-19">（3）二叉搜索树中的插入操作</h4>
<p>给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。</p>
<p>例如，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">给定二叉搜索树:
    <span class="hljs-number">4</span>
   / \
  <span class="hljs-number">2</span>   <span class="hljs-number">7</span>
 / \
<span class="hljs-number">1</span>   <span class="hljs-number">3</span>
和 插入的值: <span class="hljs-number">5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以返回这个二叉搜索树:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">     <span class="hljs-number">4</span>
   /   \
  <span class="hljs-number">2</span>     <span class="hljs-number">7</span>
 / \   /
<span class="hljs-number">1</span>   <span class="hljs-number">3</span> <span class="hljs-number">5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者这个树也是有效的:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">     <span class="hljs-number">5</span>
   /   \
  <span class="hljs-number">2</span>     <span class="hljs-number">7</span>
 / \   
<span class="hljs-number">1</span>   <span class="hljs-number">3</span>
     \
      <span class="hljs-number">4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>二叉搜索树的性质：对于任意节点 root 而言，左子树（如果存在）上所有节点的值均小于 root.val，右子树（如果存在）上所有节点的值均大于 root.val，且它们都是二叉搜索树。</p>
<p>因此，当将val 插入到以root 为根的子树上时，根据 val 与 root.val 的大小关系，就可以确定要将val 插入到哪个子树中。</p>
<ul>
<li>如果该子树不为空，则问题转化成了将 val 插入到对应子树上。</li>
<li>否则，在此处新建一个以 val 为值的节点，并链接到其父节点 root 上。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) &#123;
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">val</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>

<span class="hljs-comment">// 递归的实现：</span>
<span class="hljs-keyword">var</span> insertIntoBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, val</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!root)&#123;
        <span class="hljs-keyword">return</span>  <span class="hljs-keyword">new</span> TreeNode(val)
    &#125;
    <span class="hljs-keyword">if</span>(val < root.val)&#123;
        root.left = insertIntoBST(root.left,val)
    &#125;<span class="hljs-keyword">else</span>&#123;
        root.right = insertIntoBST(root.right,val)
    &#125;
    <span class="hljs-keyword">return</span> root
&#125;;

<span class="hljs-comment">// 迭代的实现：</span>
<span class="hljs-keyword">var</span> insertIntoBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, val</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!root)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> TreeNode(val)
    &#125;
    <span class="hljs-keyword">let</span> cur = root
    <span class="hljs-keyword">while</span>(cur)&#123;
        <span class="hljs-keyword">if</span>(val > cur.val)&#123;
           <span class="hljs-keyword">if</span>(!cur.right)&#123;
                cur.right = <span class="hljs-keyword">new</span> TreeNode(val)
                <span class="hljs-keyword">return</span> root
           &#125;<span class="hljs-keyword">else</span>&#123;
               cur = cur.right
           &#125;
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-keyword">if</span>(!cur.left)&#123;
                cur.left = <span class="hljs-keyword">new</span> TreeNode(val)
                <span class="hljs-keyword">return</span> root
            &#125;<span class="hljs-keyword">else</span>&#123;
                cur = cur.left
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> root
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>迭代的复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(N)，其中 N 为树中节点数。最坏情况下，需要将值插入到树的最深的叶子结点上，而叶子节点最深为 O(N)。</li>
<li>空间复杂度：O(1)。我们只使用了常数大小的空间。</li>
</ul>
<p><strong>递归的复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(N)，其中 N 为树中节点数。最坏情况下，需要将值插入到树的最深的叶子结点上，而叶子节点最深为 O(N)。</li>
<li>空间复杂度：O(1)。我们只使用了常数大小的空间。</li>
</ul>
<h4 data-id="heading-20">（4）将二叉搜索树变平衡</h4>
<p>给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。如果有多种构造方法，请你返回任意一种。</p>
<p>示例：
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/581d7e9d8a1a4821b5b315fd8cf73f33~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05dd86f4fdda4d20b4d2f95ef12532c3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：root = [<span class="hljs-number">1</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">2</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">3</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>]
输出：[<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">4</span>]
解释：这不是唯一的正确答案，[<span class="hljs-number">3</span>,<span class="hljs-number">1</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">2</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>] 也是一个可行的构造方案。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<ul>
<li>树节点的数目在 1 到 10 之间。</li>
<li>树节点的值互不相同，且在 1 到 10 之间。</li>
</ul>
<p>解题思路和上面的将一个有序数组转化为高度平衡的二叉搜索树问题类似。</p>
<p>我们知道，二叉搜索树的中序遍历是一个有序数组，那么就可以将题目给出的二叉搜索树进行中序遍历，将遍历得到的有序数组转化为平衡的二叉搜索树。其中后半部分和之前的解题思路完全一致。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> balanceBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
   <span class="hljs-comment">// 初始化一个数组用来储存中序遍历的结果</span>
   <span class="hljs-keyword">const</span> nums = []
   <span class="hljs-comment">// 对二叉搜索树进行中序遍历</span>
   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inorder</span>(<span class="hljs-params">root</span>)</span>&#123;
       <span class="hljs-keyword">if</span>(!root)&#123;
           <span class="hljs-keyword">return</span> 
       &#125;
       inorder(root.left)
       nums.push(root.val)
       inorder(root.right)
   &#125;
   <span class="hljs-comment">// 将有序数组转化为高度平衡的二叉搜索树</span>
   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildAvl</span>(<span class="hljs-params">low, high</span>)</span>&#123;
       <span class="hljs-keyword">if</span>(low > high)&#123;
           <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
       &#125;
       <span class="hljs-keyword">const</span> mid = <span class="hljs-built_in">Math</span>.floor(low+(high-low)/<span class="hljs-number">2</span>)
       <span class="hljs-keyword">const</span> cur = <span class="hljs-keyword">new</span> TreeNode(nums[mid])
       cur.left = buildAvl(low, mid-<span class="hljs-number">1</span>)
       cur.right = buildAvl(mid+<span class="hljs-number">1</span>, high)
       <span class="hljs-keyword">return</span> cur
   &#125;
   inorder(root)
   <span class="hljs-keyword">return</span> buildAvl(<span class="hljs-number">0</span>, nums.length-<span class="hljs-number">1</span>)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：由于每个节点最多被访问一次，因此总的时间复杂度为 O(N)，其中 N 为链表长度。</li>
<li>空间复杂度：虽然使用了递归，但是瓶颈不在栈空间，而是开辟的长度为 N 的 nums 数组，因此空间复杂度为 O(N)，其中 N 为树的节点总数。</li>
</ul>
<h4 data-id="heading-21">（5）将有序链表转换为二叉搜索树</h4>
<p>给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。示例:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">给定的有序链表： [-<span class="hljs-number">10</span>, -<span class="hljs-number">3</span>, <span class="hljs-number">0</span>, <span class="hljs-number">5</span>, <span class="hljs-number">9</span>],

一个可能的答案是：[<span class="hljs-number">0</span>, -<span class="hljs-number">3</span>, <span class="hljs-number">9</span>, -<span class="hljs-number">10</span>, <span class="hljs-literal">null</span>, <span class="hljs-number">5</span>], 它可以表示下面这个高度平衡二叉搜索树：

      <span class="hljs-number">0</span>
     / \
   -<span class="hljs-number">3</span>   <span class="hljs-number">9</span>
   /   /
 -<span class="hljs-number">10</span>  <span class="hljs-number">5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于数组是有序递增排列的，所以我们可以从数组的中间开始查找。利用递归+二分法来解决这个问题。具体实现思路如下：</p>
<ul>
<li>找出数组的中间元素，作为二叉树的根节点的值</li>
<li>二叉树的左节点是<code>0—mid-1</code>的中间坐标对应的元素</li>
<li>二叉树的右节点是<code>mid+1—arr.length-1</code>的中间坐标对应元素</li>
<li>按照上面的规律进行地递归，直到数组元素遍历完</li>
</ul>
<p>需要注意的是，最后的结果可能不唯一。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for singly-linked list.
 * function ListNode(val, next) &#123;
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) &#123;
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;ListNode&#125;</span> <span class="hljs-variable">head</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> sortedListToBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">head</span>) </span>&#123;
    <span class="hljs-keyword">const</span> arr=[];
    <span class="hljs-keyword">while</span>(head)&#123;
        arr.push(head.val)
        head = head.next
    &#125;
    <span class="hljs-keyword">const</span> resTree=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">left, right</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(left > right) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
        <span class="hljs-keyword">const</span> mid = <span class="hljs-built_in">Math</span>.floor(left + (right - left)/<span class="hljs-number">2</span>); 
        <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">new</span> TreeNode(arr[mid]);
        res.left = resTree(left, mid-<span class="hljs-number">1</span>);
        res.right = resTree(mid+<span class="hljs-number">1</span>, right);
        <span class="hljs-keyword">return</span> res
    &#125;
    <span class="hljs-keyword">return</span> resTree(<span class="hljs-number">0</span>, arr.length-<span class="hljs-number">1</span>) 
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中 n 是数组的长度。每个数字只访问一次。</li>
<li>空间复杂度：O(logn)，其中 n 是数组的长度。空间复杂度不考虑返回值，因此空间复杂度主要取决于递归栈的深度，递归栈的深度是 O(logn)。</li>
</ul>
<h4 data-id="heading-22">（6）把二叉搜索树转换为累加树</h4>
<p>给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: 原始二叉搜索树:
              <span class="hljs-number">5</span>
            /   \
           <span class="hljs-number">2</span>     <span class="hljs-number">13</span>

输出: 转换为累加树:
             <span class="hljs-number">18</span>
            /   \
          <span class="hljs-number">20</span>     <span class="hljs-number">13</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这也是一个简单题目，我们都知道二叉树的中序遍历结果是一个递增的数组。这里我们可以进行倒序进行中序遍历，这样遍历的出的数组就是递减的。</p>
<p>中序遍历的顺序是 **左子树→根节点→右子树。**所以可以先遍历右子树，再遍历根节点，最后遍历左子树。</p>
<p>这样的话，设置一个节点不断累加之前的值，那么在当前节点的值就会赋值成比他大的数的和。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> convertBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>

    <span class="hljs-keyword">const</span> inOrder = <span class="hljs-function">(<span class="hljs-params">root</span>) =></span> &#123;
        <span class="hljs-keyword">if</span>(!root)&#123;
            <span class="hljs-keyword">return</span> 
        &#125;
        <span class="hljs-keyword">if</span>(root.right)&#123;
            inOrder(root.right)
        &#125;
        sum += root.val
        root.val = sum
        <span class="hljs-keyword">if</span>(root.left)&#123;
            inOrder(root.left)
        &#125;
    &#125;
    inOrder(root)
    <span class="hljs-keyword">return</span> root
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中 n 是二叉搜索树的节点数。每一个节点恰好被遍历一次。</li>
<li>空间复杂度：O(n)，为递归过程中栈的开销，平均情况下为 O(logn)，最坏情况下树呈现链状，为 O(n)。</li>
</ul>
<h4 data-id="heading-23">（7）修剪二叉搜索树</h4>
<p>给你二叉搜索树的根节点 <code>root</code> ，同时给定最小边界<code>low</code> 和最大边界 <code>high</code>。通过修剪二叉搜索树，使得所有节点的值在<code>[low, high]</code>中。修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。</p>
<p>所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。</p>
<p><strong>示例 1：</strong>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d45b7b3d8e98433fbb82f7dd2bf3d892~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：root = [<span class="hljs-number">1</span>,<span class="hljs-number">0</span>,<span class="hljs-number">2</span>], low = <span class="hljs-number">1</span>, high = <span class="hljs-number">2</span>
输出：[<span class="hljs-number">1</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">2</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cfd8555c59b4d2689b51944684716d9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：root = [<span class="hljs-number">3</span>,<span class="hljs-number">0</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">2</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">1</span>], low = <span class="hljs-number">1</span>, high = <span class="hljs-number">3</span>
输出：[<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">1</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 3：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：root = [<span class="hljs-number">1</span>], low = <span class="hljs-number">1</span>, high = <span class="hljs-number">2</span>
输出：[<span class="hljs-number">1</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 4：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：root = [<span class="hljs-number">1</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">2</span>], low = <span class="hljs-number">1</span>, high = <span class="hljs-number">3</span>
输出：[<span class="hljs-number">1</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">2</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 5：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：root = [<span class="hljs-number">1</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">2</span>], low = <span class="hljs-number">2</span>, high = <span class="hljs-number">4</span>
输出：[<span class="hljs-number">2</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提示：</strong></p>
<ul>
<li>树中节点数在范围 <code>[1, 10]</code> 内</li>
<li><code>0 <= Node.val <= 10</code></li>
<li>树中每个节点的值都是唯一的</li>
<li>题目数据保证输入是一棵有效的二叉搜索树</li>
<li><code>0 <= low <= high <= 10</code></li>
</ul>
<p>对于这道题目，我们可以使用递归来实现。</p>
<ul>
<li>如果当前结点小于下界，直接将修剪后的右子树替换当前节点并返回；</li>
<li>如果当前结点大于上界，直接将修剪后的左子树替换当前节点并返回；</li>
<li>如果当前节点在范围之内，就继续递归左右子树查找越界的节点。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) &#123;
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">low</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">high</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> trimBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, low, high</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!root)&#123;
        <span class="hljs-keyword">return</span> root
    &#125;
    <span class="hljs-comment">// 如果当前结点小于下界，直接将修剪后的右子树替换当前节点并返回</span>
    <span class="hljs-keyword">if</span>(root.val < low)&#123;
        <span class="hljs-keyword">return</span> trimBST(root.right, low, high)
    &#125;
    <span class="hljs-comment">// 如果当前结点大于上界，直接将修剪后的左子树替换当前节点并返回</span>
    <span class="hljs-keyword">if</span>(root.val > high)&#123;
        <span class="hljs-keyword">return</span> trimBST(root.left, low, high)
    &#125;

    <span class="hljs-comment">// 如果当前结点不越界，继续往左右子树进行递归</span>
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)
    <span class="hljs-keyword">return</span> root
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中 n 是给定的树节点数。我们最多访问每个节点一次。</li>
<li>空间复杂度：O(n)，这里虽然没有使用任何额外的内存，但是在最差情况下，递归调用的栈可能与节点数一样大。</li>
</ul>
<h4 data-id="heading-24">（8）删除二叉搜索树中的节点</h4>
<p>给定一个二叉搜索树的根节点 <strong>root</strong> 和一个值 <strong>key</strong>，删除二叉搜索树中的 <strong>key</strong> 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。一般来说，删除节点可分为两个步骤：</p>
<ol>
<li>首先找到需要删除的节点；</li>
<li>如果找到了，删除它。</li>
</ol>
<p><strong>说明：</strong> 要求算法时间复杂度为 O(h)，h 为树的高度。
<strong>示例:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">root = [<span class="hljs-number">5</span>,<span class="hljs-number">3</span>,<span class="hljs-number">6</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">7</span>]
key = <span class="hljs-number">3</span>
    <span class="hljs-number">5</span>
   / \
  <span class="hljs-number">3</span>   <span class="hljs-number">6</span>
 / \   \
<span class="hljs-number">2</span>   <span class="hljs-number">4</span>   <span class="hljs-number">7</span>
给定需要删除的节点值是 <span class="hljs-number">3</span>，所以我们首先找到 <span class="hljs-number">3</span> 这个节点，然后删除它。
一个正确的答案是 [<span class="hljs-number">5</span>,<span class="hljs-number">4</span>,<span class="hljs-number">6</span>,<span class="hljs-number">2</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">7</span>], 如下图所示。
    <span class="hljs-number">5</span>
   / \
  <span class="hljs-number">4</span>   <span class="hljs-number">6</span>
 /     \
<span class="hljs-number">2</span>       <span class="hljs-number">7</span>
另一个正确答案是 [<span class="hljs-number">5</span>,<span class="hljs-number">2</span>,<span class="hljs-number">6</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">4</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">7</span>]。
    <span class="hljs-number">5</span>
   / \
  <span class="hljs-number">2</span>   <span class="hljs-number">6</span>
   \   \
    <span class="hljs-number">4</span>   <span class="hljs-number">7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们知道，二叉搜索树的左子树总是比根节点小，右子树总是比根节点大，所以可以将根节点的值与要删除的 key 值对比，就知道要删除的值在哪个位置：</p>
<ul>
<li>如果key 和根节点相等，那么就删除当前的根节点，退出递归；</li>
<li>如果key 比根节点值大，那么就要递归右子树去查找；</li>
<li>如果key 比根节点值小，那么就要递归左子树去查找；</li>
</ul>
<p>当我们找到需要删除的节点时，会有以下四种情况：</p>
<ul>
<li>待删除的节点的左右子节点均为空，那么就直接删除当前节点即可；</li>
<li>待删除的节点存在左子节点，而右子节点为空，那么就当前节点设置为左子节点的值；</li>
<li>待删除的节点存在右子节点，而左子节点为空，那么就当前节点设置为右子节点的值；</li>
<li>带删除的节点同时存在左子子节点，那么就要找到<strong>比当前节点小的最大节点</strong>（<strong>或者比当前节点大的最小节点</strong>）来替换掉当前的节点（下面代码中，我们是找的是比当前节点大的最小节点）；**</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) &#123;
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">key</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> deleteNode = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, key</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!root)&#123;
        <span class="hljs-keyword">return</span> root
    &#125;

    <span class="hljs-keyword">if</span>(root.val > key)&#123;
        root.left = deleteNode(root.left, key)
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(root.val < key)&#123;
        root.right = deleteNode(root.right, key)
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">if</span>(!root.left && !root.right)&#123;
            root = <span class="hljs-literal">null</span>
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(root.left && !root.right)&#123;
            root = root.left
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(!root.left && root.right)&#123;
            root = root.right
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(root.left && root.right)&#123;
            <span class="hljs-keyword">let</span> last = root.right
            <span class="hljs-keyword">while</span> (last.left) &#123;
                last = last.left
            &#125;
            root.val = last.val
            root.right = deleteNode(root.right, last.val)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> root

&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(logN)。在算法的执行过程中，我们一直在树上向左或向右移动。首先先用 O(H) 的时间找到要删除的节点，H指得是从根节点到要删除节点的高度。然后删除节点需要 O(H) 的时间，H指的是从要删除节点到替换节点的高度。由于 O(H+  H)=O(H)，H 指得是树的高度，若树是一个平衡树，则 H = logN。</li>
<li>空间复杂度：O(H)，递归时堆栈使用的空间，其中 H 是树的高度。</li>
</ul>
<h3 data-id="heading-25">8. 经典题目：二叉树的公共祖先</h3>
<h4 data-id="heading-26">（1）二叉树的最近公共祖先</h4>
<p>给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”</p>
<p>例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f800d62a987c4cd0a5023d1849caacdc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>示例 1:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: root = [<span class="hljs-number">3</span>,<span class="hljs-number">5</span>,<span class="hljs-number">1</span>,<span class="hljs-number">6</span>,<span class="hljs-number">2</span>,<span class="hljs-number">0</span>,<span class="hljs-number">8</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">7</span>,<span class="hljs-number">4</span>], p = <span class="hljs-number">5</span>, q = <span class="hljs-number">1</span>
输出: <span class="hljs-number">3</span>
解释: 节点 <span class="hljs-number">5</span> 和节点 <span class="hljs-number">1</span> 的最近公共祖先是节点 <span class="hljs-number">3</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: root = [<span class="hljs-number">3</span>,<span class="hljs-number">5</span>,<span class="hljs-number">1</span>,<span class="hljs-number">6</span>,<span class="hljs-number">2</span>,<span class="hljs-number">0</span>,<span class="hljs-number">8</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">7</span>,<span class="hljs-number">4</span>], p = <span class="hljs-number">5</span>, q = <span class="hljs-number">4</span>
输出: <span class="hljs-number">5</span>
解释: 节点 <span class="hljs-number">5</span> 和节点 <span class="hljs-number">4</span> 的最近公共祖先是节点 <span class="hljs-number">5</span>。因为根据定义最近公共祖先节点可以为节点本身。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明:</p>
<ul>
<li>所有节点的值都是唯一的。</li>
<li>p、q 为不同节点且均存在于给定的二叉树中。</li>
</ul>
<p>对于二叉树的题目，经常用的就是递归遍历，这里我们也使用到了<strong>递归：</strong></p>
<p>首先判断，如果树为空树或p、q中任意一节和根节点相等，那么p和q 的最近公共祖先节点就是根节点root。</p>
<p>如果树不为空树，并且p和q和根节点不相等，那么就递归遍历左右子树：</p>
<ul>
<li>如果p和q节点在左右子树的最近公共祖先节点都存在，说明p和q分布在左右子树上，则它们的最近公共祖先节点就是根节点root。</li>
<li>如果只有一个子树递归有结果，说明p和q都在这个子树中，那么就返回该树的递归的结果。</li>
<li>如果两个子树递归结果都为null，说明p和q都不在这俩子树中，那么就返回根节点root。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">p</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">q</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> lowestCommonAncestor = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, p, q</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!root || root === p || root === q)&#123;
        <span class="hljs-keyword">return</span> root
    &#125;

    <span class="hljs-keyword">const</span> left = lowestCommonAncestor(root.left, p, q)
    <span class="hljs-keyword">const</span> right = lowestCommonAncestor(root.right, p, q)
    
    <span class="hljs-keyword">if</span>(!left) <span class="hljs-keyword">return</span> right
    <span class="hljs-keyword">if</span>(!right) <span class="hljs-keyword">return</span> left

    <span class="hljs-keyword">return</span> root
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>复杂度分析：</strong></p>
<ul>
<li>时间复杂度: O(n)，其中 n 是二叉树节点的个数。这里遍历了二叉树的每个节点，所以时间复杂度为O(n)。</li>
<li>空间复杂度: O(n)，其中 n 是二叉树节点的个数。递归调用的栈深度取决于二叉树的高度，二叉树最坏情况下为一条链，此时高度为 n，所以空间复杂度为 O(n)。</li>
</ul>
<h4 data-id="heading-27">（2）二叉搜索树的最近公共祖先</h4>
<p>给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。</p>
<p><a href="https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin" target="_blank" rel="nofollow noopener noreferrer">百度百科</a>中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（<strong>一个节点也可以是它自己的祖先</strong>）。”</p>
<p>例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ac2f584ad414e74b0030d05d4d20ca3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>示例 1:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: root = [<span class="hljs-number">6</span>,<span class="hljs-number">2</span>,<span class="hljs-number">8</span>,<span class="hljs-number">0</span>,<span class="hljs-number">4</span>,<span class="hljs-number">7</span>,<span class="hljs-number">9</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">3</span>,<span class="hljs-number">5</span>], p = <span class="hljs-number">2</span>, q = <span class="hljs-number">8</span>
输出: <span class="hljs-number">6</span> 
解释: 节点 <span class="hljs-number">2</span> 和节点 <span class="hljs-number">8</span> 的最近公共祖先是 <span class="hljs-number">6</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: root = [<span class="hljs-number">6</span>,<span class="hljs-number">2</span>,<span class="hljs-number">8</span>,<span class="hljs-number">0</span>,<span class="hljs-number">4</span>,<span class="hljs-number">7</span>,<span class="hljs-number">9</span>,<span class="hljs-literal">null</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">3</span>,<span class="hljs-number">5</span>], p = <span class="hljs-number">2</span>, q = <span class="hljs-number">4</span>
输出: <span class="hljs-number">2</span>
解释: 节点 <span class="hljs-number">2</span> 和节点 <span class="hljs-number">4</span> 的最近公共祖先是 <span class="hljs-number">2</span>, 因为根据定义最近公共祖先节点可以为节点本身。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>说明:</strong></p>
<ul>
<li>所有节点的值都是唯一的。</li>
<li>p、q 为不同节点且均存在于给定的二叉搜索树中。</li>
</ul>
<p>对于这道题目，我们可以使用递归或者迭代来实现。</p>
<p><strong>1）递归实现：</strong> 对于二叉树搜索树：</p>
<ul>
<li>如果 p.val 和 q.val 都比 root.val 小，则 p、q 肯定在 root 的左子树；</li>
<li>如果 p.val 和 q.val 都比 root.val 大，则 p、q 肯定在 root 的右子树；</li>
<li>如果 p.val 和 q.val 一个比 root.val 大，一个比 root.val 小，那说明这两个节点的最进公共祖先就是root；**</li>
</ul>
<p><strong>2）迭代实现：</strong> 我们可以使用一个 while 循环，当 root 为 null 时就结束循环：</p>
<ul>
<li>如果 p.val 和 q.val 都比 root.val 小，则 p、q 肯定在 root 的左子树，root=root.left，遍历到 root 的左子节点。</li>
<li>如果 p.val 和 q.val 都比 root.val 大，则 p、q 肯定在 root 的右子树，root=root.right，遍历到 root 的右子节点。</li>
<li>其他情况，当前的 root 就是最近公共祖先，结束遍历，直接结束循环。</li>
</ul>
<p><strong>递归实现：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">p</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">q</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> lowestCommonAncestor = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, p, q</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(p.val < root.val && q.val < root.val)&#123;
        <span class="hljs-keyword">return</span> lowestCommonAncestor(root.left, p, q)
    &#125;
    <span class="hljs-keyword">if</span>(p.val > root.val && q.val > root.val)&#123;
        <span class="hljs-keyword">return</span> lowestCommonAncestor(root.right, p, q)
    &#125;
    <span class="hljs-keyword">return</span> root
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>迭代实现：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * Definition for a binary tree node.
 * function TreeNode(val) &#123;
 *     this.val = val;
 *     this.left = this.right = null;
 * &#125;
 */</span>

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">p</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">q</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> lowestCommonAncestor = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, p, q</span>) </span>&#123;
    <span class="hljs-keyword">while</span>(root)&#123;
        <span class="hljs-keyword">if</span>(p.val < root.val && q.val < root.val)&#123;
            root = root.left
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(p.val > root.val && q.val > root.val)&#123;
            root = root.right
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-keyword">break</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> root
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>迭代复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中 n 是二叉搜索树的节点数。最坏的情况下，我们需要深度优先遍历整棵二叉树；</li>
<li>空间复杂度：O(1)，我们只需要常量空间来操作。</li>
</ul>
<p><strong>递归复杂度分析：</strong></p>
<ul>
<li>时间复杂度：O(n)，其中 n 是二叉搜索树的节点数。最坏的情况选，我们需要深度优先遍历整棵二叉树；</li>
<li>空间复杂度：O(n)，我们需要递归遍历这棵树，所以空间复杂度为O(n)；</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            