
---
title: 'javaScript实现二叉搜索数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9722'
author: 掘金
comments: false
date: Sat, 10 Apr 2021 22:33:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=9722'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">javaScript实现二叉搜索数</h2>
<blockquote>
<p>二叉搜索数是二叉树的一种，只允许左子节点比父节点小，右侧子节点比父节点大或者相等</p>
</blockquote>
<ol>
<li>创建一个节点构造函数Node，用于新建节点</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Node</span>(<span class="hljs-params">val</span>) </span>&#123;
<span class="hljs-built_in">this</span>.val = val;<span class="hljs-comment">//该节点的值</span>
<span class="hljs-built_in">this</span>.left = <span class="hljs-literal">null</span>;<span class="hljs-comment">//该节点的左侧子节点</span>
<span class="hljs-built_in">this</span>.right = <span class="hljs-literal">null</span>;<span class="hljs-comment">//该节点的右侧子节点</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>创建一个搜索树构造函数</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SearchTree</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">this</span>.root = <span class="hljs-literal">null</span>;<span class="hljs-comment">//根节点</span>
<span class="hljs-built_in">this</span>.length = <span class="hljs-number">0</span>;<span class="hljs-comment">//该树中所有节点的个数，包括根节点</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>给SearchTreet添加insertTree方法,用于向树中插入新的节点。首先我们需要判断根节点是否为空，然后从根节点进行迭代，如果待插入节点的值比父节点小，则作为父节点的左侧子节点，反之 作为右侧子节点。最后插入完毕之后返回该节点，并且将length加一</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">SearchTree.prototype.insertTree = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>) </span>&#123;
<span class="hljs-comment">//新建一个节点</span>
<span class="hljs-keyword">let</span> node = <span class="hljs-keyword">new</span> Node(val);
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.root === <span class="hljs-literal">null</span>) &#123;
<span class="hljs-comment">//如果我们的根节点为null，则需要初始搜索树</span>
<span class="hljs-built_in">this</span>.root = node;
<span class="hljs-built_in">this</span>.length++;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.root;
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">let</span> curr = <span class="hljs-built_in">this</span>.root;
<span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
<span class="hljs-comment">//迭代二叉树，将比根节点小的放在节点的左边，反之放在右边</span>
<span class="hljs-keyword">if</span> (val < curr.val) &#123;
<span class="hljs-keyword">if</span> (curr.left !== <span class="hljs-literal">null</span>) &#123;
<span class="hljs-comment">//如果left不为空则继续迭代</span>
curr = curr.left;
&#125; <span class="hljs-keyword">else</span> &#123;
curr.left = node;
<span class="hljs-comment">//退出while循环</span>
<span class="hljs-keyword">break</span>;
&#125;
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">if</span> (curr.right !== <span class="hljs-literal">null</span>) &#123;
curr = curr.right;
&#125; <span class="hljs-keyword">else</span> &#123;
curr.right = node;
<span class="hljs-keyword">break</span>;
&#125;
&#125;
&#125;
&#125;
<span class="hljs-built_in">this</span>.length++;
<span class="hljs-keyword">return</span> node;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>前序遍历</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">SearchTree.prototype.prevErgodic  = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">node, arr = []</span>) </span>&#123;
<span class="hljs-keyword">if</span> (node !== <span class="hljs-literal">null</span>) &#123;
arr.push(node.val)
<span class="hljs-built_in">this</span>.prevErgodic  (node.left, arr);
<span class="hljs-built_in">this</span>.prevErgodic  (node.right, arr)
&#125;
<span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>中序遍历</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">SearchTree.prototype.centerErgodic = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">node, arr = []</span>) </span>&#123; 
<span class="hljs-keyword">if</span> (node !== <span class="hljs-literal">null</span>) &#123;
<span class="hljs-comment">//升序排序</span>
<span class="hljs-built_in">this</span>.centerErgodic (node.left, arr);
arr.push(node.val);
<span class="hljs-built_in">this</span>.centerErgodic (node.right, arr);
<span class="hljs-comment">//降序排序</span>
<span class="hljs-comment">//this.centerErgodic (node.right, arr);</span>
<span class="hljs-comment">//arr.push(node.val);</span>
<span class="hljs-comment">//this.centerErgodic (node.left, arr);</span>
&#125;
<span class="hljs-keyword">return</span> arr;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>后序遍历</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">SearchTree.prototype.nextErgodic.function(node, arr = []) &#123; 
<span class="hljs-keyword">if</span> (node !== <span class="hljs-literal">null</span>) &#123;
<span class="hljs-built_in">this</span>.nextErgodic(node.left, arr);
<span class="hljs-built_in">this</span>.nextErgodic(node.right, arr);
arr.push(node.val);
&#125;
<span class="hljs-keyword">return</span> arr;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>获得最小值，从根节点一直遍历左节点到叶子节点，该叶子节点即为最小值</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">SearchTree.prototype.getMin = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">node</span>) </span>&#123;
<span class="hljs-keyword">let</span> curr = node || <span class="hljs-built_in">this</span>.root;
<span class="hljs-keyword">if</span> (curr === <span class="hljs-literal">null</span>) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">while</span> (curr.left !== <span class="hljs-literal">null</span>) &#123;
curr = curr.left
&#125;
<span class="hljs-keyword">return</span> curr.val
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>获得最大值，从根节点一直遍历右节点到叶子节点，该叶子节点即为最大值</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">SearchTree.prototype.getMax = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">node</span>) </span>&#123;
<span class="hljs-keyword">let</span> curr = node || <span class="hljs-built_in">this</span>.root;
<span class="hljs-keyword">if</span> (curr === <span class="hljs-literal">null</span>) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">while</span> (curr.right!== <span class="hljs-literal">null</span>) &#123;
curr = curr.right
&#125;
<span class="hljs-keyword">return</span> curr.val
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="9">
<li>判断值是否存在，如果存在返回该节点，否则返回false</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">SearchTree.prototype.getItem = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">node, item</span>) </span>&#123;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.root === <span class="hljs-literal">null</span>) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">let</span> curr = node;
<span class="hljs-keyword">if</span> (curr === <span class="hljs-literal">null</span>) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">if</span> (item < curr.val) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getItem(curr.left, item);
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (item === curr.val) &#123;
<span class="hljs-keyword">return</span> curr;
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (item > curr.val) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getItem(curr.right, item);
&#125;
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">测试代码</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//创建实例</span>
<span class="hljs-keyword">const</span> searchTree = <span class="hljs-keyword">new</span> SearchTree();
<span class="hljs-comment">//创建数组，循环给searchTree 插入节点</span>
<span class="hljs-keyword">let</span> max = <span class="hljs-number">100</span>;
<span class="hljs-keyword">let</span> arr = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; index < max; index++) &#123;
<span class="hljs-keyword">let</span> item = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * max);
arr.push(item);
searchTree.insertTree(item)
&#125;
<span class="hljs-built_in">console</span>.log(searchTree)
<span class="hljs-comment">//打印原数组</span>
<span class="hljs-built_in">console</span>.log(arr)
<span class="hljs-comment">//打印前序遍历的数组</span>
<span class="hljs-built_in">console</span>.log(searchTree.prevErgodic(searchTree.root))
<span class="hljs-comment">//打印中序遍历的数组</span>
<span class="hljs-built_in">console</span>.log(searchTree.centerErgodic(searchTree.root))
<span class="hljs-comment">//打印升序排列后的数组，与中序遍历的数组比较</span>
<span class="hljs-built_in">console</span>.log(arr.sort(<span class="hljs-function">(<span class="hljs-params">a,b</span>)=></span>a - b))
<span class="hljs-comment">//打印后序遍历的数组</span>
<span class="hljs-built_in">console</span>.log(searchTree.nextErgodic(searchTree.root))
<span class="hljs-comment">//获取最小值</span>
<span class="hljs-built_in">console</span>.log(searchTree.getMin())
<span class="hljs-comment">//获取最大值</span>
<span class="hljs-built_in">console</span>.log(searchTree.getMax())
<span class="hljs-comment">//获取指定值节点</span>
<span class="hljs-built_in">console</span>.log(searchTree.getItem(searchTree.root, searchTree.getMax()))
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            