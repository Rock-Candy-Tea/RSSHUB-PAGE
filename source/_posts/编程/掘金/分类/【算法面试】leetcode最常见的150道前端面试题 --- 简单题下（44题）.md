
---
title: '【算法面试】leetcode最常见的150道前端面试题 --- 简单题下（44题）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f23accef4a5402da0c898920e64a8f4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 16:51:58 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f23accef4a5402da0c898920e64a8f4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文题目选自 <a href="https://link.juejin.cn/?target=leetcode-cn.com%2Fproblem-list%2F2ckc81c%2F" title="https://link.juejin.cn/?target=leetcode-cn.com%2Fproblem-list%2F2ckc81c%2F" target="_blank">LeetCode 精选 TOP 面试题</a>，这些题在自己和同事亲身经历中，确实遇到的几率在<code>百分之80%</code>以上（成都和北京的前端岗位）。</p>
<p>本篇是简单题（下）20题左右，上半部分详见<a href="https://juejin.cn/post/6987320619394138148" target="_blank" title="https://juejin.cn/post/6987320619394138148"># 简单题上（22题左右）</a></p>
<h2 data-id="heading-0">二叉树（DFS）</h2>
<h2 data-id="heading-1">二叉树前中后遍历套路详解</h2>
<p>前序遍历题目如下：</p>
<p>root节点是A节点（下图的A节点），然后让你按照下图数字的顺序依次打印出节点。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f23accef4a5402da0c898920e64a8f4~tplv-k3u1fbpfcp-watermark.image" alt="d7948dc5e50e70cc84cfbd0e0cf989da40eb96167f03b710392be45b8c415662.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到这其中的规律，就是<code>深度优先遍历，先遍历左子树，再遍历右子树</code>，这里我们不用递归，因为一些大厂严格要求二叉树遍历不用递归，递归太简单了。</p>
<p>重点思路就是：<code>深度优先遍历，先遍历左子树，再遍历右子树</code>，</p>
<p>所以，我们需要一套如何遍历一颗二叉树，并且是先左子树，再右子树的通用模板，如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> Traversal = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-keyword">const</span> stack = [];
    <span class="hljs-keyword">while</span> (root || stack.length)&#123;
      <span class="hljs-keyword">while</span>(root)&#123;
        stack.push(root);
        root = root.left;
      &#125;
      root = stack.pop();
      root = root.right;
    &#125;
    <span class="hljs-keyword">return</span> res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们结合图片发现这个遍历产生的整体压栈的顺序是</p>
<ul>
<li>A、B、D入栈，</li>
<li>D出栈</li>
<li>B出栈</li>
<li>E入栈</li>
<li>E出栈</li>
<li>A出栈</li>
<li>C入栈</li>
<li>C出栈</li>
<li>F入栈</li>
<li>F出栈</li>
</ul>
<p>我们把上面入栈的元素按顺序排列一下就是，A、B、D、E、C、F，而这就是前序遍历的顺序！解答完毕！</p>
<p>是不是很有意思，下面的中序遍历，我们看看出栈顺序是不是中序遍历的要求：D、B、E、A、C、F（这就是中序遍历的要求，好了，两个题解决）</p>
<p>放具体前序遍历代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> preorderTraversal = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-comment">// 初始化数据</span>
    <span class="hljs-keyword">const</span> res =[];
    <span class="hljs-keyword">const</span> stack = [];
    <span class="hljs-keyword">while</span> (root || stack.length)&#123;
      <span class="hljs-keyword">while</span>(root)&#123;
        res.push(root.val);
        stack.push(root);
        root = root.left;
      &#125;
      root = stack.pop();
      root = root.right;
    &#125;
    <span class="hljs-keyword">return</span> res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>中序遍历是一个意思，在前序遍历的基础上改造一下
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2de9035c3cc1425bbb64ef5b5d821181~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> preorderTraversal = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-comment">// 初始化数据</span>
    <span class="hljs-keyword">const</span> res =[];
    <span class="hljs-keyword">const</span> stack = [];
    <span class="hljs-keyword">while</span> (root || stack.length)&#123;
      <span class="hljs-keyword">while</span>(root)&#123;
        stack.push(root);
        root = root.left;
      &#125;
      root = stack.pop();
      res.push(root.val);
      root = root.right;
    &#125;
    <span class="hljs-keyword">return</span> res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后序遍历有点不太一样，但是套路是一样的，我们需要先遍历右子树，再遍历左子树，反着来，就可以了，代码如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e45cdd1671ed4128ad67b99631146410~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> postorderTraversal = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
  <span class="hljs-comment">// 初始化数据</span>
    <span class="hljs-keyword">const</span> res =[];
    <span class="hljs-keyword">const</span> stack = [];
    <span class="hljs-keyword">while</span> (root || stack.length)&#123;
      <span class="hljs-keyword">while</span>(root)&#123;
        stack.push(root);
        res.unshift(root.val);
        root = root.right;
      &#125;
      root = stack.pop();
      root = root.left;
    &#125;
    <span class="hljs-keyword">return</span> res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">对称二叉树</h2>
<p>这个题简而言之就是判断一个二叉树是对称的，比如说：</p>
<p>二叉树 [1,2,2,3,4,4,3] 是对称的。</p>
<pre><code class="copyable">    1
   / \
  2   2
 / \ / \
3  4 4  3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:</p>
<pre><code class="copyable">    1
   / \
  2   2
   \   \
   3    3

<span class="copy-code-btn">复制代码</span></code></pre>
<p>思路：</p>
<p>递归解决：</p>
<ul>
<li>判断两个指针当前节点值是否相等</li>
<li>判断 <code>A</code> 的右子树与 <code>B</code> 的左子树是否对称</li>
<li>判断 <code>A</code> 的左子树与 <code>B</code> 的右子树是否对称</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isSame</span>(<span class="hljs-params">leftNode, rightNode</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(leftNode === <span class="hljs-literal">null</span> && rightNode === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    <span class="hljs-keyword">if</span>(leftNode === <span class="hljs-literal">null</span> || rightNode === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    <span class="hljs-keyword">return</span> leftNode.val === rightNode.val && isSame(leftNode.left, rightNode.right) && isSame(leftNode.right, rightNode.left)
&#125;
<span class="hljs-keyword">var</span> isSymmetric = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!root) <span class="hljs-keyword">return</span> root;
    <span class="hljs-keyword">return</span> isSame(root.left, root.right);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">二叉树的最大深度</h2>
<p>这个题在面试滴滴的时候遇到过，主要是掌握二叉树遍历的套路</p>
<ul>
<li>只要遍历到这个节点既没有左子树，又没有右子树的时候</li>
<li>说明就到底部了，这个时候如果之前记录了深度，就可以比较是否比之前记录的深度大，大就更新深度</li>
<li>然后以此类推，一直比较到深度最大的</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> maxDepth = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!root) <span class="hljs-keyword">return</span> root;
    <span class="hljs-keyword">let</span> ret = <span class="hljs-number">1</span>;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dfs</span>(<span class="hljs-params">root, depth</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(!root.left && !root.right) ret = <span class="hljs-built_in">Math</span>.max(ret, depth);
        <span class="hljs-keyword">if</span>(root.left) dfs(root.left, depth+<span class="hljs-number">1</span>);
        <span class="hljs-keyword">if</span>(root.right) dfs(root.right, depth+<span class="hljs-number">1</span>);
    &#125;
    dfs(root, ret);
    <span class="hljs-keyword">return</span> ret
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">将有序数组转化为二叉搜索树</h2>
<p>我们先看题：</p>
<p>给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。</p>
<p>高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。</p>
<p> </p>
<p>示例 1：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/795298bc725b475ba97541f92e7a357f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT">输入：nums = [-<span class="hljs-number">10</span>,-<span class="hljs-number">3</span>,<span class="hljs-number">0</span>,<span class="hljs-number">5</span>,<span class="hljs-number">9</span>]
输出：[<span class="hljs-number">0</span>,-<span class="hljs-number">3</span>,<span class="hljs-number">9</span>,-<span class="hljs-number">10</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">5</span>]
解释：[<span class="hljs-number">0</span>,-<span class="hljs-number">10</span>,<span class="hljs-number">5</span>,<span class="hljs-literal">null</span>,-<span class="hljs-number">3</span>,<span class="hljs-literal">null</span>,<span class="hljs-number">9</span>] 也将被视为正确答案：
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ca89e21fe494dcd86208468c02f19f7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT">输入：nums = [<span class="hljs-number">1</span>,<span class="hljs-number">3</span>]
输出：[<span class="hljs-number">3</span>,<span class="hljs-number">1</span>]
解释：[<span class="hljs-number">1</span>,<span class="hljs-number">3</span>] 和 [<span class="hljs-number">3</span>,<span class="hljs-number">1</span>] 都是高度平衡二叉搜索树。
 

提示：

<span class="hljs-number">1</span> <= nums.length <= <span class="hljs-number">104</span>
-<span class="hljs-number">104</span> <= nums[i] <= <span class="hljs-number">104</span>
nums 按 严格递增 顺序排列
<span class="copy-code-btn">复制代码</span></code></pre>
<p>思路：</p>
<ul>
<li>构建一颗树包括：构建<code>root、构建 root.left 和 root.right</code></li>
<li>题目要求"高度平衡" — 构建 <code>root</code> 时候，选择数组的中间元素作为 <code>root </code>节点值，即可保持平衡。</li>
<li>递归函数可以传递数组，也可以传递指针，选择传递指针的时候： l r 分别代表参与构建BST的数组的首尾索引。</li>
</ul>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-keyword">var</span> sortedArrayToBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
    <span class="hljs-keyword">return</span> toBST(nums, <span class="hljs-number">0</span>, nums.length - <span class="hljs-number">1</span>)
&#125;;
<span class="hljs-keyword">const</span> toBST = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums, l, r</span>)</span>&#123;
    <span class="hljs-keyword">if</span>( l > r)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    &#125;
    <span class="hljs-keyword">const</span> mid = l + r >> <span class="hljs-number">1</span>;
    <span class="hljs-keyword">const</span> root = <span class="hljs-keyword">new</span> TreeNode(nums[mid]);
    root.left = toBST(nums, l, mid - <span class="hljs-number">1</span>);
    root.right = toBST(nums, mid + <span class="hljs-number">1</span>, r);

    <span class="hljs-keyword">return</span> root;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">栈</h3>
<p>栈是一种先进先出的数据结构，所以涉及到你需要<code>先进先出</code>这个想法后，就可以使用栈。</p>
<p>其次我觉得栈跟递归很相似，递归是不是先压栈，然后先进来的先出去，就跟函数调用栈一样。</p>
<h2 data-id="heading-6">20. 有效的括号</h2>
<p>这是一道很典型的用栈解决的问题，
给定一个只包括 '('，')'，'&#123;'，'&#125;'，'['，']' 的字符串 s ，判断字符串是否有效。</p>
<p>有效字符串需满足：</p>
<p>左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 </p>
<pre><code class="hljs language-javascript copyable" lang="javascript">示例 <span class="hljs-number">1</span>：

输入：s = <span class="hljs-string">"()"</span>
输出：<span class="hljs-literal">true</span>
示例 <span class="hljs-number">2</span>：

输入：s = <span class="hljs-string">"()[]&#123;&#125;"</span>
输出：<span class="hljs-literal">true</span>
示例 <span class="hljs-number">3</span>：

输入：s = <span class="hljs-string">"(]"</span>
输出：<span class="hljs-literal">false</span>
示例 <span class="hljs-number">4</span>：

输入：s = <span class="hljs-string">"([)]"</span>
输出：<span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>思路：
这道题有一规律：</p>
<ol>
<li>右括号前面，必须是相对应的左括号，才能抵消！</li>
<li>右括号前面，不是对应的左括号，那么该字符串，一定不是有效的括号！</li>
</ol>
<p>也就是说左括号我们直接放入栈中即可，发现是右括号就要对比是否跟栈顶元素相匹配，不匹配就返回false</p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-keyword">var</span> isValid = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
    <span class="hljs-keyword">const</span> map = &#123; <span class="hljs-string">'&#123;'</span>: <span class="hljs-string">'&#125;'</span>, <span class="hljs-string">'('</span>: <span class="hljs-string">')'</span>, <span class="hljs-string">'['</span>: <span class="hljs-string">']'</span> &#125;;
    <span class="hljs-keyword">const</span> stack = [];
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> s)&#123;
        <span class="hljs-keyword">if</span>(map[i])&#123;
            stack.push(i);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">if</span>(map[stack[stack.length - <span class="hljs-number">1</span>]] === i)&#123;
                stack.pop()
            &#125;<span class="hljs-keyword">else</span>&#123;
                <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> stack.length === <span class="hljs-number">0</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">155、 最小栈</h2>
<p>先看题目：</p>
<p>设计一个支持 <code>push ，pop ，top</code> 操作，并能在常数时间内检索到最小元素的栈。</p>
<ul>
<li>push(x) —— 将元素 x 推入栈中。</li>
<li>pop() —— 删除栈顶的元素。</li>
<li>top() —— 获取栈顶元素。</li>
<li>getMin() —— 检索栈中的最小元素。</li>
</ul>
<p> </p>
<pre><code class="hljs language-javascript copyable" lang="javascript">示例:

MinStack minStack = <span class="hljs-keyword">new</span> MinStack();
minStack.push(-<span class="hljs-number">2</span>);
minStack.push(<span class="hljs-number">0</span>);
minStack.push(-<span class="hljs-number">3</span>);
minStack.getMin();   --> 返回 -<span class="hljs-number">3.</span>
minStack.pop();
minStack.top();      --> 返回 <span class="hljs-number">0.</span>
minStack.getMin();   --> 返回 -<span class="hljs-number">2.</span>

提示：

pop、top 和 getMin 操作总是在 非空栈 上调用。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先不写getMin方法，满足其他方法实现就非常简单，我们来看一下：</p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-keyword">var</span> MinStack = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.stack = [];
&#125;;

MinStack.prototype.push = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.stack.push(x);
&#125;;

MinStack.prototype.pop = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.stack.pop();
&#125;;

MinStack.prototype.top = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.stack[<span class="hljs-built_in">this</span>.stack.length - <span class="hljs-number">1</span>];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何保证每次取最小呢，我们举一个例子：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9731d0d86dd442eba35ffb3b879d72b4~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-25 下午5.46.53.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图，我们需要一个辅助栈来记录最小值，</p>
<ul>
<li>开始我们向stack push -2</li>
<li>此时辅助栈minStack，因为此时stack最小的是-2，也push -2</li>
<li>stack push 0</li>
<li>此时辅助站minStack 会用 0 跟 -2对比，-2更小，minstack会push -2</li>
<li>stack push -3</li>
<li>此时辅助站minStack 会用 -3 跟 -2对比，-3更小，minstack会push -3</li>
</ul>
<p>所以我们取最小的时候，总能在minStack中取到最小值，所以解法就出来了：</p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-keyword">var</span> MinStack = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.stack = [];
    <span class="hljs-comment">// 辅助栈</span>
    <span class="hljs-built_in">this</span>.minStack = [];
&#125;;

MinStack.prototype.push = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.stack.push(x);
    <span class="hljs-comment">// 如果是第一次或者当前x比最小栈里的最小值还小才push x</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.minStack.length === <span class="hljs-number">0</span> || x < <span class="hljs-built_in">this</span>.minStack[<span class="hljs-built_in">this</span>.minStack.length - <span class="hljs-number">1</span>])&#123;
        <span class="hljs-built_in">this</span>.minStack.push(x)
    &#125; <span class="hljs-keyword">else</span> &#123;
         <span class="hljs-built_in">this</span>.minStack.push( <span class="hljs-built_in">this</span>.minStack[<span class="hljs-built_in">this</span>.minStack.length - <span class="hljs-number">1</span>])
    &#125;
&#125;;

MinStack.prototype.pop = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.stack.pop();
    <span class="hljs-built_in">this</span>.minStack.pop();
&#125;;

MinStack.prototype.top = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.stack[<span class="hljs-built_in">this</span>.stack.length - <span class="hljs-number">1</span>];
&#125;;

MinStack.prototype.getMin = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.minStack[<span class="hljs-built_in">this</span>.stack.length - <span class="hljs-number">1</span>];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">动态规划</h2>
<p>动态规划，一定要知道动态转移方程，有了这个，就相当于解题的钥匙，我们从题目中体会一下</p>
<h2 data-id="heading-9">53. 最大子序和</h2>
<p>题目如下：</p>
<p>给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
 </p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT">示例 <span class="hljs-number">1</span>：

输入：nums = [-<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,-<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,-<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,-<span class="hljs-number">5</span>,<span class="hljs-number">4</span>]
输出：<span class="hljs-number">6</span>
解释：连续子数组 [<span class="hljs-number">4</span>,-<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>] 的和最大，为 <span class="hljs-number">6</span> 。
示例 <span class="hljs-number">2</span>：

输入：nums = [<span class="hljs-number">1</span>]
输出：<span class="hljs-number">1</span>
示例 <span class="hljs-number">3</span>：

输入：nums = [<span class="hljs-number">0</span>]
输出：<span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>思路：</p>
<ul>
<li>这道题可以用动态规划来解决，关键是找动态转移方程</li>
<li>我们动态转移方程中，dp表示每一个nums下标的最大自序和，所以dp[i]的意思为：包括下标i之前的最大连续子序列和为dp[i]。</li>
</ul>
<p>确定转义方程的公示：</p>
<p>dp[i]只有两个方向可以推出来：</p>
<ul>
<li>1、如果dp[i - 1] < 0，也就是当前遍历到nums的i，之前的最大子序和是负数，那么我们就没必要继续加它了，因为dp[i] = dp[i - 1] + nums[i] 会比nums[i]更小，所以此时还不如dp[i] = nums[i]，就是目前遍历到i的最大子序和呢</li>
<li>2、同理dp[i - 1] > 0，说明nums[i]值得去加dp[i - 1]，此时回避nums[i]更大</li>
</ul>
<p>这样代码就出来了，其实更多的就是求dp，遍历nums每一个下标都会产生最大子序和，我们记录下来即可</p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-keyword">var</span> maxSubArray = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
  <span class="hljs-keyword">let</span> res = nums[<span class="hljs-number">0</span>];
  <span class="hljs-keyword">const</span> dp = [nums[<span class="hljs-number">0</span>]];
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">1</span>;i < nums.length;i++)&#123;
      <span class="hljs-keyword">if</span>(dp[i-<span class="hljs-number">1</span>]><span class="hljs-number">0</span>)&#123;
        dp[i]=nums[i]+dp[i-<span class="hljs-number">1</span>]
      &#125;<span class="hljs-keyword">else</span>&#123;
       dp[i]=nums[i]
      &#125;
      
    res=<span class="hljs-built_in">Math</span>.max(dp[i],res)
  &#125;
    <span class="hljs-keyword">return</span> res
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">70. 爬楼梯</h2>
<p>先看题目：</p>
<p>假设你正在爬楼梯。需要 n 阶你才能到达楼顶。</p>
<p>每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>
<p>注意：给定 n 是一个正整数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">示例 <span class="hljs-number">1</span>：

输入： <span class="hljs-number">2</span>
输出： <span class="hljs-number">2</span>
解释： 有两种方法可以爬到楼顶。
<span class="hljs-number">1.</span>  <span class="hljs-number">1</span> 阶 + <span class="hljs-number">1</span> 阶
<span class="hljs-number">2.</span>  <span class="hljs-number">2</span> 阶
示例 <span class="hljs-number">2</span>：

输入： <span class="hljs-number">3</span>
输出： <span class="hljs-number">3</span>
解释： 有三种方法可以爬到楼顶。
<span class="hljs-number">1.</span>  <span class="hljs-number">1</span> 阶 + <span class="hljs-number">1</span> 阶 + <span class="hljs-number">1</span> 阶
<span class="hljs-number">2.</span>  <span class="hljs-number">1</span> 阶 + <span class="hljs-number">2</span> 阶
<span class="hljs-number">3.</span>  <span class="hljs-number">2</span> 阶 + <span class="hljs-number">1</span> 阶
<span class="copy-code-btn">复制代码</span></code></pre>
<p>涉及到动态规划，一定要知道动态转移方程，有了这个，就相当于解题的钥匙，</p>
<p>这道题我们假设<code>dp[10]</code>表示爬到是你爬到<code>10</code>阶就到达楼顶的方法数，</p>
<p>那么，<code>dp[10]</code> 是不是就是你爬到8阶，然后再走<code>2</code>步就到了，还有你走到<code>9</code>阶，再走<code>1</code>步就到了，</p>
<p>所以 <code>dp[10]</code> 是不是等于 <code>dp[9]+dp[8]</code></p>
<p>延伸一下 <code>dp[n]</code> 是不是等于 <code>dp[n - 1] + dp[n - 2]</code></p>
<p>代码如下：</p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-keyword">var</span> climbStairs = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-keyword">const</span> dp = &#123;&#125;;
    dp[<span class="hljs-number">1</span>] = <span class="hljs-number">1</span>;
    dp[<span class="hljs-number">2</span>] = <span class="hljs-number">2</span>;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">3</span>; i <= n; i++)&#123;
        dp[i] = dp[i-<span class="hljs-number">1</span>] + dp[i-<span class="hljs-number">2</span>]
    &#125;
    <span class="hljs-keyword">return</span> dp[n]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">数学问题</h2>
<p>以下更多的是涉及数学问题，这些解法非常重要，因为在中级题里面会经常用到，比如我们马上讲到的<code>加一</code>这个题，
中级的两数相加都是一个模板。</p>
<h2 data-id="heading-12">66. 加一</h2>
<p>题目如下：</p>
<p>给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。</p>
<p>最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。</p>
<p>你可以假设除了整数 0 之外，这个整数不会以零开头。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">示例 <span class="hljs-number">1</span>：

输入：digits = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]
输出：[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>]
解释：输入数组表示数字 <span class="hljs-number">123</span>。
示例 <span class="hljs-number">2</span>：

输入：digits = [<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>]
输出：[<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">2</span>]
解释：输入数组表示数字 <span class="hljs-number">4321</span>。
示例 <span class="hljs-number">3</span>：

输入：digits = [<span class="hljs-number">0</span>]
输出：[<span class="hljs-number">1</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个题的关键有两点：</p>
<ul>
<li>需要有一个进位的变量carry记录到底进位是几</li>
<li>还需要一个每次迭代都重置和的变量sum来帮我们算是否进位，以及进位后的数字</li>
</ul>
<p>记住这个题，这是两数字相加的套路，这次是+1，其实就是两数相加的题（腾讯面试遇到过两数相加）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> plusOne = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">digits</span>) </span>&#123;
  <span class="hljs-keyword">let</span> carry = <span class="hljs-number">1</span>; <span class="hljs-comment">// 进位（因为我们确定+1，初始化进位就是1）</span>
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = digits.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--)&#123;
      <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>; <span class="hljs-comment">// 这个变量是用来每次循环计算进位和digits[i]的值的</span>
      sum = digits[i] + carry; 
      digits[i] = sum % <span class="hljs-number">10</span>; <span class="hljs-comment">// 模运算取个位数</span>
      carry = (sum / <span class="hljs-number">10</span>) | <span class="hljs-number">0</span>; <span class="hljs-comment">//  除以10是取百位数，并且｜0表示舍弃小数位</span>
  &#125;
  <span class="hljs-keyword">if</span>(digits[<span class="hljs-number">0</span>] === <span class="hljs-number">0</span>) digits.unshift(carry);
  <span class="hljs-keyword">return</span> digits
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">69 x的平方根</h2>
<p>题目如下：
实现 int sqrt(int x) 函数。</p>
<p>计算并返回 x 的平方根，其中 x 是非负整数。</p>
<p>由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。</p>
<p>示例 1:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: <span class="hljs-number">4</span>
输出: <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入: <span class="hljs-number">8</span>
输出: <span class="hljs-number">2</span>
说明: <span class="hljs-number">8</span> 的平方根是 <span class="hljs-number">2.82842</span>..., 
     由于返回类型是整数，小数部分将被舍去。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这道题是典型的二分法解题，所以我们需要熟悉二分法的通用模板，我们出一个题：</p>
<p><strong>在 [1, 2, 3, 4, 5, 6, 7, 8, 9] 中找到 4，若存在则返回下标，不存在返回-1</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">funcion <span class="hljs-function"><span class="hljs-title">searchNum</span>(<span class="hljs-params">target, nums</span>)</span>&#123;
     <span class="hljs-keyword">if</span>(!nums.length) <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
     <span class="hljs-keyword">let</span> l = <span class="hljs-number">0</span>;
     <span class="hljs-keyword">let</span> r = nums[nums.length - <span class="hljs-number">1</span>];     
     <span class="hljs-keyword">while</span>(l <= r)&#123;
         <span class="hljs-keyword">let</span> mid = l + r >> <span class="hljs-number">1</span>
         <span class="hljs-keyword">if</span>(nums[mid] === target) <span class="hljs-keyword">return</span> mid;
         <span class="hljs-keyword">if</span>(nums[mid] > target) &#123;
             r--
         &#125; <span class="hljs-keyword">else</span> &#123;
             l++
         &#125;
     &#125;
     <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意到题目中给出的例 2，小数部分将被舍去。我们就知道了，如果一个数 aa 的平方大于 xx ，那么 aa 一定不是 xx 的平方根。我们下一轮需要在 [0..a - 1][0..a−1] 区间里继续查找 xx 的平方根。</p>
<p>所以代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> mySqrt = <span class="hljs-function"><span class="hljs-params">x</span> =></span> &#123;
    <span class="hljs-keyword">let</span> [low, high] = [<span class="hljs-number">0</span>, x];
    <span class="hljs-keyword">while</span> (low <= high) &#123;
        <span class="hljs-keyword">const</span> mid = (low + high) >> <span class="hljs-number">1</span>;
        <span class="hljs-keyword">if</span> (mid * mid > x) &#123;
            high = mid - <span class="hljs-number">1</span>;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (mid * mid < x) &#123;
            low = mid + <span class="hljs-number">1</span>;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> mid;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> high;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">171. Excel表序列号</h2>
<p>这个题比较重要，也比较基础，简而言之就是进制转换</p>
<p>题目如下：</p>
<p>给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。</p>
<p>例如：</p>
<pre><code class="copyable">A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">示例 <span class="hljs-number">1</span>：

输入：columnNumber = <span class="hljs-number">1</span>
输出：<span class="hljs-string">"A"</span>
示例 <span class="hljs-number">2</span>：

输入：columnNumber = <span class="hljs-number">28</span>
输出：<span class="hljs-string">"AB"</span>
示例 <span class="hljs-number">3</span>：

输入：columnNumber = <span class="hljs-number">701</span>
输出：<span class="hljs-string">"ZY"</span>
示例 <span class="hljs-number">4</span>：

输入：columnNumber = <span class="hljs-number">2147483647</span>
输出：<span class="hljs-string">"FXSHRXW"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说白了，这就是一道26进制的问题，以前我们知道10进制转2进制就是不停的除2，把余数加起来，26进制也是一样，不停的除26</p>
<p>思路：</p>
<ul>
<li>从末尾开始取得每一个字符对应的数cur = c.charCodeAt() - 64</li>
<li>数字总和sum += 当前数 * 进制位数</li>
<li>进制位数 *= 26，初始化进制位数carry = 1</li>
</ul>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-keyword">var</span> titleToNumber = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
    <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>, i = s.length - <span class="hljs-number">1</span>, carry = <span class="hljs-number">1</span>;

    <span class="hljs-keyword">while</span> (i >= <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">let</span> cur = s[i].charCodeAt() - <span class="hljs-number">64</span>;

        sum += cur * carry;
        carry *= <span class="hljs-number">26</span>;
        i--;
    &#125;

    <span class="hljs-keyword">return</span> sum;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">172. 阶乘中的零</h2>
<p>题目：
给定一个整数 n，返回 n! 结果尾数中零的数量。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">示例 <span class="hljs-number">1</span>:

输入: <span class="hljs-number">3</span>
输出: <span class="hljs-number">0</span>
解释: <span class="hljs-number">3</span>! = <span class="hljs-number">6</span>, 尾数中没有零。
示例 <span class="hljs-number">2</span>:

输入: <span class="hljs-number">5</span>
输出: <span class="hljs-number">1</span>
解释: <span class="hljs-number">5</span>! = <span class="hljs-number">120</span>, 尾数中有 <span class="hljs-number">1</span> 个零.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这道题很简单，有多少个5就有多少个0</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> trailingZeroes = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">n</span>) </span>&#123;
  <span class="hljs-keyword">let</span> r = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">while</span> (n > <span class="hljs-number">1</span>) &#123;
    n = <span class="hljs-built_in">parseInt</span>(n / <span class="hljs-number">5</span>);
    r += n;
  &#125;
  <span class="hljs-keyword">return</span> r;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>// ## 190.颠倒二进制位</p>
<h2 data-id="heading-16">268. 丢失的数字</h2>
<p>题目如下：</p>
<p>给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。</p>
<p>进阶：</p>
<p>你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
 </p>
<pre><code class="hljs language-javascript copyable" lang="javascript">示例 <span class="hljs-number">1</span>：

输入：nums = [<span class="hljs-number">3</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>]
输出：<span class="hljs-number">2</span>
解释：n = <span class="hljs-number">3</span>，因为有 <span class="hljs-number">3</span> 个数字，所以所有的数字都在范围 [<span class="hljs-number">0</span>,<span class="hljs-number">3</span>] 内。<span class="hljs-number">2</span> 是丢失的数字，因为它没有出现在 nums 中。
示例 <span class="hljs-number">2</span>：

输入：nums = [<span class="hljs-number">0</span>,<span class="hljs-number">1</span>]
输出：<span class="hljs-number">2</span>
解释：n = <span class="hljs-number">2</span>，因为有 <span class="hljs-number">2</span> 个数字，所以所有的数字都在范围 [<span class="hljs-number">0</span>,<span class="hljs-number">2</span>] 内。<span class="hljs-number">2</span> 是丢失的数字，因为它没有出现在 nums 中。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这题很简单，就是用0-n的总和减去数组总和</p>
<ul>
<li>0 - n 的总和用等差数列:<code>（首数+尾数）* 项数 / 2 </code>来求</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">var</span> missingNumber = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
    <span class="hljs-keyword">const</span> len = nums.length
 
   <span class="hljs-keyword">let</span> sum = ((<span class="hljs-number">1</span> + len) * len) / <span class="hljs-number">2</span>
 
   <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
     sum -= nums[i]
   &#125;
 
   <span class="hljs-keyword">return</span> sum
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>// - 3的幂</p>
<h2 data-id="heading-17">412. Fizz Buzz</h2>
<p>这个题没啥好说的，就按照题目说的写代码就行，先看题目：</p>
<p>写一个程序，输出从 1 到 n 数字的字符串表示。</p>
<ol>
<li>
<p>如果 n 是3的倍数，输出“Fizz”；</p>
</li>
<li>
<p>如果 n 是5的倍数，输出“Buzz”；</p>
</li>
<li>
<p>如果 n 同时是3和5的倍数，输出 “FizzBuzz”。</p>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">示例：

n = <span class="hljs-number">15</span>,

返回:
[
    <span class="hljs-string">"1"</span>,
    <span class="hljs-string">"2"</span>,
    <span class="hljs-string">"Fizz"</span>,
    <span class="hljs-string">"4"</span>,
    <span class="hljs-string">"Buzz"</span>,
    <span class="hljs-string">"Fizz"</span>,
    <span class="hljs-string">"7"</span>,
    <span class="hljs-string">"8"</span>,
    <span class="hljs-string">"Fizz"</span>,
    <span class="hljs-string">"Buzz"</span>,
    <span class="hljs-string">"11"</span>,
    <span class="hljs-string">"Fizz"</span>,
    <span class="hljs-string">"13"</span>,
    <span class="hljs-string">"14"</span>,
    <span class="hljs-string">"FizzBuzz"</span>
]
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">var</span> fizzBuzz = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-keyword">const</span> list = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i <= n; i++) &#123;
      <span class="hljs-keyword">const</span> is3Times = i % <span class="hljs-number">3</span> === <span class="hljs-number">0</span>; <span class="hljs-comment">// 是否是3的倍数</span>
      <span class="hljs-keyword">const</span> is5Times = i % <span class="hljs-number">5</span> === <span class="hljs-number">0</span>; <span class="hljs-comment">// 是否是5的倍数</span>
      <span class="hljs-keyword">const</span> is15Times = is3Times && is5Times; <span class="hljs-comment">// 是否是15的倍数</span>
      <span class="hljs-keyword">if</span> (is15Times) &#123;
        list.push(<span class="hljs-string">'FizzBuzz'</span>);
        <span class="hljs-keyword">continue</span>;
      &#125;
      <span class="hljs-keyword">if</span> (is3Times) &#123;
        list.push(<span class="hljs-string">'Fizz'</span>);
        <span class="hljs-keyword">continue</span>;
      &#125;
      <span class="hljs-keyword">if</span> (is5Times) &#123;
        list.push(<span class="hljs-string">'Buzz'</span>);
        <span class="hljs-keyword">continue</span>;
      &#125;
      list.push(<span class="hljs-string">`<span class="hljs-subst">$&#123;i&#125;</span>`</span>);
    &#125;
    <span class="hljs-keyword">return</span> list;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<ol start="7">
<li>整数反转</li>
</ol>
</li>
</ul>
<p>稍后更新本文章</p>
<h2 data-id="heading-18">环问题</h2>
<p>这类问题的特点就是，你要循环寻找，到底怎么循环寻找，看题便知。</p>
<h2 data-id="heading-19">141. 环形链表</h2>
<p>题目如下：</p>
<p>给定一个链表，判断链表中是否有环。</p>
<p>如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。</p>
<p>如果链表中存在环，则返回 true 。 否则，返回 false 。</p>
<p><strong>示例 1：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bccd989c0d3f4203ae318b855a00b8d3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">输入： head = [3,2,0,-4], pos = 1
输出： true
解释： 链表中有一个环，其尾部连接到第二个节点。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例 2：</strong>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e62e60cb229b4316bd4fce76cc713377~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">输入： head = [1,2], pos = 0
输出： true
解释： 链表中有一个环，其尾部连接到第一个节点。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们采用标记法：</p>
<p>给遍历过的节点打记号，如果遍历过程中遇到有记号的说明已环</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> hasCycle = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">head</span>) </span>&#123;
    <span class="hljs-keyword">let</span> traversingNode = head;
    <span class="hljs-keyword">while</span>(traversingNode)&#123;
        <span class="hljs-keyword">if</span>(traversingNode.isVistitd) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        traversingNode.isVistitd = <span class="hljs-literal">true</span>
        traversingNode = traversingNode.next
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">160. 相交链表</h2>
<p>题目如下：</p>
<p>给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。</p>
<p>图示两个链表在节点 c1 开始相交：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7075f5cae16b4c86b74f3e1150438bd3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>题目数据 <strong>保证</strong> 整个链式结构中不存在环。</p>
<p><strong>注意</strong>，函数返回结果后，链表必须 <strong>保持其原始结构</strong> 。</p>
<p>示例 1：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa6843fa5fab49828ff4582bbf854525~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：intersectVal = <span class="hljs-number">8</span>, listA = [<span class="hljs-number">4</span>,<span class="hljs-number">1</span>,<span class="hljs-number">8</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>], listB = [<span class="hljs-number">5</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">8</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>], skipA = <span class="hljs-number">2</span>, skipB = <span class="hljs-number">3</span>
输出：Intersected at <span class="hljs-string">'8'</span>
解释：相交节点的值为 <span class="hljs-number">8</span> （注意，如果两个链表相交则不能为 <span class="hljs-number">0</span>）。
从各自的表头开始算起，链表 A 为 [<span class="hljs-number">4</span>,<span class="hljs-number">1</span>,<span class="hljs-number">8</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]，链表 B 为 [<span class="hljs-number">5</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">8</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]。
在 A 中，相交节点前有 <span class="hljs-number">2</span> 个节点；在 B 中，相交节点前有 <span class="hljs-number">3</span> 个节点。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44151e18902842de89f422802c3e1807~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">输入：intersectVal = <span class="hljs-number">2</span>, listA = [<span class="hljs-number">0</span>,<span class="hljs-number">9</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>], listB = [<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>], skipA = <span class="hljs-number">3</span>, skipB = <span class="hljs-number">1</span>
输出：Intersected at <span class="hljs-string">'2'</span>
解释：相交节点的值为 <span class="hljs-number">2</span> （注意，如果两个链表相交则不能为 <span class="hljs-number">0</span>）。
从各自的表头开始算起，链表 A 为 [<span class="hljs-number">0</span>,<span class="hljs-number">9</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>]，链表 B 为 [<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>]。
在 A 中，相交节点前有 <span class="hljs-number">3</span> 个节点；在 B 中，相交节点前有 <span class="hljs-number">1</span> 个节点。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>稍后更新本文章</p>
<h2 data-id="heading-21">202. 快乐数</h2>
<p>题目如下：
编写一个算法来判断一个数 n 是不是快乐数。</p>
<p>「快乐数」定义为：</p>
<ul>
<li>对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。</li>
<li>然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。</li>
<li>如果 可以变为  1，那么这个数就是快乐数。</li>
<li>如果 n 是快乐数就返回 true ；不是，则返回 false 。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6660588e4364aa9a36d4e41102c8f12~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>快乐数怎么分析呢？</p>
<p>我们来看一个表，就会得出结论，一个数按照快乐数定义的方式分别每个数字平方，会有两种情况</p>
<ul>
<li>
<ol>
<li>得到<code>1</code></li>
</ol>
</li>
<li>
<ol start="2">
<li>无限循环</li>
</ol>
</li>
</ul>
<p>无限循环参照下图</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46818478a7ec474bb81cb2c640b64eb5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有人会说会不会一直变大，答案是不会：
我们看下面列表，</p>
<ul>
<li>可以看到如果你是13位，你的下一次快乐数算法会变为4位1053，</li>
<li>如果你是<code>9999</code>, <code>4</code>位，下一个快乐数是<code>324</code></li>
</ul>



































<table><thead><tr><th>位数</th><th>位数对应最大值</th><th>下一个快乐数</th></tr></thead><tbody><tr><td>1</td><td>9</td><td>81</td></tr><tr><td>2</td><td>99</td><td>162</td></tr><tr><td>3</td><td>999</td><td>243</td></tr><tr><td>4</td><td>9999</td><td>324</td></tr><tr><td>13</td><td>9999999999999</td><td>1053</td></tr></tbody></table>
<p>所以代码只要判断这两种就行了，代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 封装获取快乐数的方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getNext</span>(<span class="hljs-params">n</span>)</span>&#123;
    n = <span class="hljs-built_in">String</span>(n);
    <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> num <span class="hljs-keyword">of</span> n)&#123;
        sum = sum + <span class="hljs-built_in">Math</span>.pow(+num, <span class="hljs-number">2</span>);
    &#125;
    <span class="hljs-keyword">return</span> sum;
&#125;
<span class="hljs-keyword">var</span> isHappy = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-comment">// 哈希表来看是否循环</span>
    <span class="hljs-keyword">const</span> map = &#123;&#125;;
    <span class="hljs-keyword">while</span>( n !== <span class="hljs-number">1</span> )&#123;
        map[n] = <span class="hljs-literal">true</span>;
        n = getNext(n)
        <span class="hljs-keyword">if</span>(map[n]) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后面会写中级算法的题，请大家务必把这些基础算法题掌握好，基础不牢地动山摇，后面中级题很多都是在这些基础题的基础上的。</p></div>  
</div>
            