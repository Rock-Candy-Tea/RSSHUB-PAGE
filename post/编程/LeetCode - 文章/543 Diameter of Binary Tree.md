
---
title: '543. Diameter of Binary Tree'
categories: 
    - 编程
    - LeetCode - 文章
author: LeetCode - 文章
comments: false
date: Tue, 09 Mar 2021 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg'
---

<div>   
<p>Given the <code>root</code> of a binary tree, return <em>the length of the <strong>diameter</strong> of the tree</em>.</p>

<p>The <strong>diameter</strong> of a binary tree is the <strong>length</strong> of the longest path between any two nodes in a tree. This path may or may not pass through the <code>root</code>.</p>

<p>The <strong>length</strong> of a path between two nodes is represented by the number of edges between them.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg" style="width: 292px; height: 302px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3is the length of the path [4,2,1,3] or [5,2,1,3].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 1
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
<li><code>-100 <= Node.val <= 100</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach1depthfirstsearch">Approach 1: Depth-first Search</h4>
<p><strong>Intuition</strong></p>
<p>The key observation to make is: <em>the longest path has to be between two leaf nodes</em>. We can prove this with contradiction. Imagine that we have found the longest path, and it is <strong>not</strong> between two leaf nodes. We can extend that path by 1, by adding the child node of one of the end nodes (as at least one must have a child, given that they aren't both leaves). This contradicts the fact that our path is the longest path. Therefore, the longest path must be between two leaf nodes.</p>
<p>Moreover, we know that in a tree, nodes are only connected with their parent node and 2 children. Therefore we know that the longest path in the tree would consist of a node, its longest left branch, and its longest right branch. So, our algorithm to solve this problem will find the node where the sum of its longest left and right branches is maximized. This would hint at us to apply Depth-first search (DFS) to count each node's branch lengths, because it would allow us to dive deep into the leaves first, and then start counting the edges upwards.</p>
<blockquote>
  <p>DFS is a widely-used graph traversal algorithm. If you are not familiar with it, feel free to visit our <a href="https://leetcode.com/explore/learn/card/data-structure-tree/">Explore Cards</a> where you will see different ways to traverse a binary tree with DFS including preorder, inorder, postorder :)</p>
</blockquote>
<p>Let's try to be more specific about how to apply DFS to this question. To count the lengths of each node's left and right branches, we can implement a recursion function <code>longestPath</code> which takes a <code>TreeNode</code> as input and returns the longest path from it to the leaf node. It will recursively visit children nodes and retrieve the longest paths from them to the leaf first, and then add <code>1</code> to the longer one before returning it as the longest path.</p>
<p>In the midst of DFS, we also need to take the following two cases into account:</p>
<ol>
<li>the current node's both left and right branches might be a part of the longest path;</li>
<li>one of the current node's left/right branches might be a part of the longest path.</li>
</ol>
<p><img src="https://leetcode.com/articles/Figures/543/543.png" alt="Two cases of the longest path." referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1. Two cases of the longest path.</em>
&#123;:align="center"&#125;</p>
<p>You will see we are going to address them by 1) applying DFS to recursively find the longest branches starting with the node's left and right children; 2) initializing a global variable <code>diameter</code> to keep track of the longest path and updating it at each node with the sum of the node's left and right branches; 3) returning the length of the longest branch between a node's left and right branches.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Initalize an integer variable <code>diameter</code> to keep track of the longest path we find from the DFS.</li>
<li>Implement a recursive function <code>longestPath</code> which takes a <code>TreeNode</code> as input. It should recursively explore the entire tree rooted at the given node. Once it's finished, it should return the longest path out of its left and right branches:</li>
<li>if <code>node</code> is <code>None</code>, we have reached the end of the tree, hence we should return <code>0</code>;</li>
<li>we want to recursively explore <code>node</code>'s children, so we call <code>longestPath</code> again with <code>node</code>'s left and right children. In return, we get the longest path of its left and right children <code>leftPath</code> and <code>rightPath</code>;</li>
<li>if <code>leftPath</code> plus <code>rightPath</code> is longer than the current longest diameter found, then we need to update <code>diameter</code>;</li>
<li>finally, we return the longer one of <code>leftPath</code> and <code>rightPath</code>. Remember to add $$1$$ as the edge connecting it with its parent.</li>
<li>Call <code>longestPath</code> with <code>root</code>.</li>
</ul>
<iframe src="https://leetcode.com/playground/btjsoAGc/shared" frameborder="0" width="100%" height="429" name="btjsoAGc"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the number of nodes in the tree.</p>
<ul>
<li><p>Time complexity: $$O(N)$$. This is because in our recursion function <code>longestPath</code>, we only enter and exit from each node once. We know this because each node is entered from its parent, and in a tree, nodes only have one parent.</p></li>
<li><p>Space complexity: $$O(N)$$. The space complexity depends on the size of our implicit call stack during our DFS, which relates to the height of the tree. In the worst case, the tree is skewed so the height of the tree is $$O(N)$$. If the tree is balanced, it'd be $$O(\log N)$$.
<br></p></li>
</ul>
<hr>  
</div>
            