
---
title: '105. Construct Binary Tree From Preorder and Inorder Traversal'
categories: 
    - 编程
    - LeetCode
    - 文章

author: LeetCode
comments: false
date: Tue, 09 Mar 2021 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2021/02/19/tree.jpg'
---

<div>   
<p>Given two integer arrays <code>preorder</code> and <code>inorder</code> where <code>preorder</code> is the preorder traversal of a binary tree and <code>inorder</code> is the inorder traversal of the same tree, construct and return <em>the binary tree</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> preorder = [-1], inorder = [-1]
<strong>Output:</strong> [-1]
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= preorder.length <= 3000</code></li>
<li><code>inorder.length == preorder.length</code></li>
<li><code>-3000 <= preorder[i], inorder[i] <= 3000</code></li>
<li><code>preorder</code> and <code>inorder</code> consist of <strong>unique</strong> values.</li>
<li>Each value of <code>inorder</code> also appears in <code>preorder</code>.</li>
<li><code>preorder</code> is <strong>guaranteed</strong> to be the preorder traversal of the tree.</li>
<li><code>inorder</code> is <strong>guaranteed</strong> to be the inorder traversal of the tree.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<blockquote>
  <p>This problem examines your understanding of preorder and inorder binary tree traversals. If you are not familiar with them, feel free to visit our <a href="https://leetcode.com/explore/learn/card/data-structure-tree/">Explore Cards</a> where you will see all the ways to traverse a binary tree including preorder, inorder, postorder, and level-order traversals :)</p>
</blockquote>
<p>A tree has a recursive structure because it has subtrees which are trees themselves. Let's take a look at the inorder traversal of a binary tree, and you will see the built-in recursive structure.</p>
<p><img src="https://leetcode.com/articles/Figures/105/105-Page-1.png" alt="The recursive structure in a Tree." referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1. The recursive structure in a Tree.</em>
&#123;:align="center"&#125;</p>
<p>Henceforth, we will leverage this property and find a way to recursively construct the tree.</p>
<p><br></p>
<hr>
<h4 id="approach1recursion">Approach 1: Recursion</h4>
<p><strong>Intuition</strong></p>
<p>The two key observations are:</p>
<ol>
<li><p>Preorder traversal follows <code>Root -> Left -> Right</code>, therefore, given the preorder array <code>preorder</code>, we have easy access to the root which is <code>preorder[0]</code>.</p></li>
<li><p>Inorder traversal follows <code>Left -> Root -> Right</code>, therefore if we know the position of <code>Root</code>, we can recursively split the entire array into two subtrees.</p></li>
</ol>
<p>Now the idea should be clear enough. We will design a recursion function: it will set the first element of <code>preorder</code> as the root, and then construct the entire tree. To find the left and right subtrees, it will look for the root in <code>inorder</code>, so that everything on the left should be the left subtree, and everything on the right should be the right subtree. Both subtrees can be constructed by making another recursion call.</p>
<p>It is worth noting that, while we recursively construct the subtrees, we should choose the next element in <code>preorder</code> to initialize as the new roots. This is because the current one has already been initialized to a parent node for the subtrees.</p>
<p><img src="https://leetcode.com/articles/Figures/105/105-Page-2.png" alt="Always use the next element in <code>preorder</code> to initialize a root." referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 2. Always use the next element in <code>preorder</code> to initialize a root.</em>
&#123;:align="center"&#125;</p>
<p>!?!../Documents/105_LIS.json:1008,542!?!</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Build a hashmap to record the relation of <code>value -> index</code> for <code>inorder</code>, so that we can find the position of root in constant time.</li>
<li>Initialize an integer variable <code>preorderIndex</code> to keep track of the element that will be used to construct the root.</li>
<li>Implement the recursion function <code>arrayToTree</code> which takes a range of <code>inorder</code> and returns the constructed binary tree:</li>
<li>if the range is empty, return <code>null</code>;</li>
<li>initialize the root with <code>preorder[preorderIndex]</code> and then increment <code>preorderIndex</code>;</li>
<li>recursively use the left and right portions of <code>inorder</code> to construct the left and right subtrees.</li>
<li>Simply call the recursion function with the entire range of <code>inorder</code>.</li>
</ul>
<iframe src="https://leetcode.com/playground/cVfShiVy/shared" frameborder="0" width="100%" height="500" name="cVfShiVy"></iframe>
<p><strong>Complexity analysis</strong></p>
<p>Let $$N$$ be the length of the input arrays.</p>
<ul>
<li><p>Time complexity : $$O(N)$$.</p>
<p>Building the hashmap takes $$O(N)$$ time, as there are $$N$$ nodes to add, and adding items to a hashmap has a cost of $$O(1)$$, so we get $$N \cdot O(1) = O(N)$$.</p>
<p>Building the tree also takes $$O(N)$$ time. The recursive helper method has a cost of $$O(1)$$ for each call (it has no loops), and it is called <em>once</em> for each of the $$N$$ nodes, giving a total of $$O(N)$$.</p>
<p>Taking both into consideration, the time complexity is $$O(N)$$.</p></li>
<li><p>Space complexity : $$O(N)$$.</p>
<p>Building the hashmap and storing the entire tree each requires $$O(N)$$ memory. The size of the implicit system stack used by recursion calls depends on the height of the tree, which is $$O(N)$$ in the worst case and $$O(\log N)$$ on average. Taking both into consideration, the space complexity is $$O(N)$$.</p></li>
</ul>
<hr>  
</div>
            