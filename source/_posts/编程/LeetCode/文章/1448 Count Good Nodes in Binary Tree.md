
---
title: '1448. Count Good Nodes in Binary Tree'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png'
author: LeetCode
comments: false
date: Tue, 20 Jul 2021 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png'
---

<div>   
<p>Given a binary tree <code>root</code>, a node <em>X</em> in the tree is named <strong>good</strong> if in the path from root to <em>X</em> there are no nodes with a value <em>greater than</em> X.</p>

<p>Return the number of <strong>good</strong> nodes in the binary tree.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<p><strong><img alt src="https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png" style="width: 263px; height: 156px;" referrerpolicy="no-referrer"></strong></p>

<pre><strong>Input:</strong> root = [3,1,4,3,null,1,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Nodes in blue are <strong>good</strong>.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.</pre>

<p><strong>Example 2:</strong></p>

<p><strong><img alt src="https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png" style="width: 157px; height: 161px;" referrerpolicy="no-referrer"></strong></p>

<pre><strong>Input:</strong> root = [3,3,null,4,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Root is considered as <strong>good</strong>.</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li>The number of nodes in the binary tree is in the range <code>[1, 10^5]</code>.</li>
<li>Each node's value is between <code>[-10^4, 10^4]</code>.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach1depthfirstsearchrecursion">Approach 1: Depth First Search, Recursion</h4>
<p><strong>Intuition</strong></p>
<p>Whenever you see a tree or graph problem, your first instinct should be Breadth First Search (BFS) or Depth First Search (DFS). For this approach, we'll start with DFS. If you aren't familiar with trees and traversal algorithms, check out this <a href="https://leetcode.com/explore/learn/card/data-structure-tree/">explore card</a>. With tree traversals, algorithms usually follow the same pattern:</p>
<ol>
<li>Do something with the current node</li>
<li>Add the current node's children to the stack or queue being used for the traversal</li>
<li>Move on to the next node</li>
</ol>
<p>A powerful idea for any tree or graph problem involving BFS/DFS that everybody should learn has to do with the second step - instead of just adding nodes to the stack or queue, we can store extra data to represent state. Depending on the language you're using, this might be something like a tuple or custom object which includes the current node and some information about the current state.</p>
<p>In this first approach, we'll be using recursion. For this problem, we're concerned about the <strong>greatest value seen</strong>, so instead of the recursive function only taking nodes as an input, such as <code>dfs(node)</code>, let's also have each call take an integer as well like <code>dfs(node, integer)</code>. This integer will represent the <strong>greatest value on the path from the root to the associated node</strong>. This means that at each node, we can simply check if it is "good" by comparing this integer to the node's value.</p>
<p>How do we calculate this number? For the root, the path from the root contains no other nodes, so we can initially set this value to a very small value (such as INT_MIN). For every call afterwards, we should compare this number with the current node's value. If the current node's value is greater, then set this value equal to the current node's value before visiting this node's children.</p>
<p><img src="https://leetcode.com/articles/Figures/1448/example.png" width="960" referrerpolicy="no-referrer"><br></p>
<p>Using the above tree as an example, we will start our DFS by calling <code>dfs(root, INT_MIN)</code>. At the root, because the root's value (3) is not less than INT_MIN, the root counts as a good node. Next, we call <code>dfs</code> for each of the root's children, passing <code>max(3, INT_MIN)</code> as the second argument. This is because, for both children, the path from the root to the child contains only the root, which means to be considered a good node, they only need to have a value greater than or equal to the root's value.</p>
<p>As we continue to traverse downwards through the tree, the number that we pass along with each node will increase every time it finds a new max value, which allows us to easily check when a node is "good".</p>
<p>The below animation plays through the entire example:</p>
<p>!?!../Documents/1448<em>Count</em>Good_Nodes.json:960,540!?! <br></p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize a function <code>dfs</code>, as well as a variable <code>numGoodNodes</code> that keeps track of how many good nodes are in the tree. The function should take two arguments: a node <code>node</code>, and an integer representing the greatest value in the path leading from the root to the current node <code>maxSoFar</code>.</p></li>
<li><p>For each call to the function, first check if <code>maxSoFar <= node.val</code>. If so, increment <code>numGoodNodes</code>. Next, call <code>dfs(child, max(node.val, maxSoFar))</code> for all children of the current node.</p></li>
<li><p>Call <code>dfs(root, INT_MIN)</code> and return <code>numGoodNodes</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/HsKHgNbR/shared" frameborder="0" width="100%" height="429" name="HsKHgNbR"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the number of nodes in the tree,</p>
<ul>
<li><p>Time complexity: $$O(N)$$</p>
<p>With DFS we visit every node exactly once and do a constant amount of work each time.</p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>Because DFS prioritizes depth, our call stack can be as large as the height $$H$$ of the tree. In the worst case scenario, $$H = N$$, if the tree only has one path.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2depthfirstsearchiterative">Approach 2: Depth First Search, Iterative</h4>
<p><strong>Intuition</strong></p>
<p>DFS can also be implemented iteratively. You may be thinking at this point: what kind of DFS should we use, preorder, postorder, or inorder? The answer is that, for this problem, it doesn't matter. For each node, there is only one path from the root to that node, so regardless of the order of our traversal, the integer we use to track the greatest value will always be the largest value between the current node and the root.</p>
<p>The algorithm works the same as in the previous approach, but we will be using our own stack instead of recursion. We can implement the tracking integer by pairing the nodes with the integer when we push elements onto the stack. Depending on the language you're using, this might be done with a tuple or a custom object.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize a stack to use for DFS, as well as a variable <code>numGoodNodes</code> that keeps track of how many good nodes are in the tree. The stack should initially contain the root and a very small value (like INT_MIN).</p></li>
<li><p>Execute DFS: while the stack is not empty, pop from the stack.</p></li>
<li><p>At each node, first check if <code>node.val</code> is greater than or equal to the number associated with it <code>maxSoFar</code>. If it is, then increment <code>numGoodNodes</code>. Next, push the children onto the stack, along with the greater value between <code>maxSoFar</code> and <code>node.val</code>.</p></li>
<li><p>Return <code>numGoodNodes</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/EZZfKaFv/shared" frameborder="0" width="100%" height="500" name="EZZfKaFv"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the number of nodes in the tree,</p>
<ul>
<li><p>Time complexity: $$O(N)$$</p>
<p>With DFS we visit every node exactly once and do a constant amount of work each time.</p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>In the worst case scenario, where every right child has 2 children and every left child has no children (or vice-versa), our stack will contain $$N / 2$$ nodes at max depth.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3breadthfirstsearch">Approach 3: Breadth First Search</h4>
<p><strong>Intuition</strong></p>
<p>As stated in the previous approach, the order in which we perform DFS does not matter, because the extra state we pass along on each iteration will be correct regardless of traversal order. For this same reason, BFS and DFS are both valid approaches.</p>
<p><strong>Algorithm</strong></p>
<p>The algorithm is identical to the iterative DFS approach, except we are using a queue instead of a stack.</p>
<ol>
<li><p>Initialize a queue to use for BFS, as well as a variable <code>numGoodNodes</code> that keeps track of how many good nodes are in the tree. The BFS should initially contain the root and the a very small value (like INT_MIN).</p></li>
<li><p>Execute BFS: while the queue is not empty, pop from the front of the queue.</p></li>
<li><p>At each node, first check if <code>node.val</code> is greater than or equal to the value of its largest ancestor <code>maxSoFar</code>. If it is, then increment <code>numGoodNodes</code>. Next, push the children onto the queue, along with the greater value between <code>maxSoFar</code> and <code>node.val</code>.</p></li>
<li><p>Return <code>numGoodNodes</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/npf6iuKW/shared" frameborder="0" width="100%" height="500" name="npf6iuKW"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the number of nodes in the tree,</p>
<ul>
<li><p>Time complexity: $$O(N)$$</p>
<p>With BFS we visit every node exactly once and do a constant amount of work each time.</p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>The worst case scenario for space with BFS is when the tree is full. In this scenario, the final level contains $$N / 2$$ nodes, and our queue will hold all the nodes in the final level at some point.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            