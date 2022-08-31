
---
title: '237. Delete Node in a Linked List'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2020/09/01/node1.jpg'
author: LeetCode
comments: false
date: Tue, 30 Aug 2022 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2020/09/01/node1.jpg'
---

<div>   
<p>There is a singly-linked list <code>head</code> and we want to delete a node <code>node</code> in it.</p>

<p>You are given the node to be deleted <code>node</code>. You will <strong>not be given access</strong> to the first node of <code>head</code>.</p>

<p>All the values of the linked list are <strong>unique</strong>, and it is guaranteed that the given node <code>node</code> is not the last node in the linked list.</p>

<p>Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:</p>

<ul>
<li>The value of the given node should not exist in the linked list.</li>
<li>The number of nodes in the linked list should decrease by one.</li>
<li>All the values before <code>node</code> should be in the same order.</li>
<li>All the values after <code>node</code> should be in the same order.</li>
</ul>

<p><strong>Custom testing:</strong></p>

<ul>
<li>For the input, you should provide the entire linked list <code>head</code> and the node to be given <code>node</code>. <code>node</code> should not be the last node of the list and should be an actual node in the list.</li>
<li>We will build the linked list and pass the node to your function.</li>
<li>The output will be the entire list after calling your function.</li>
</ul>

<p> </p>
<p><strong>Example 1:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2020/09/01/node1.jpg" style="width: 400px; height: 286px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> head = [4,5,1,9], node = 5
<strong>Output:</strong> [4,1,9]
<strong>Explanation: </strong>You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
</pre>

<p><strong>Example 2:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2020/09/01/node2.jpg" style="width: 400px; height: 315px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> head = [4,5,1,9], node = 1
<strong>Output:</strong> [4,5,9]
<strong>Explanation: </strong>You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li>The number of the nodes in the given list is in the range <code>[2, 1000]</code>.</li>
<li><code>-1000 <= Node.val <= 1000</code></li>
<li>The value of each node in the list is <strong>unique</strong>.</li>
<li>The <code>node</code> to be deleted is <strong>in the list</strong> and is <strong>not a tail</strong> node.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h3 id="overview">Overview</h3>
<p>The problem is an extension of <a href="https://leetcode.com/problems/remove-linked-list-elements/">LeetCode 203. Remove Linked List Elements</a>.</p>
<p>In the original <a href="https://leetcode.com/problems/remove-linked-list-elements/">LeetCode 203. Remove Linked List Elements</a>, we were given the head of the linked list, so we can go to the desired node and connect the previous nodes to the next node.</p>
<p>However, here we are not given access to the head of the linked list, and it makes the problem a bit tricky.</p>
<hr>
<h3 id="approach1deletenextnodeinsteadofcurrentone">Approach 1: Delete next node instead of current one</h3>
<h4 id="intuition">Intuition</h4>
<p>To solve the problem, let's look at the condition carefully,</p>
<blockquote>
  <p>It is <strong>guaranteed</strong> that the node to be deleted is <strong>not a tail node</strong> in the list.</p>
</blockquote>
<p>There are a few observations here,</p>
<ul>
<li><p>The conventional deletion approach will fail here since we are not able to get the previous node by iterating from the <code>head</code> of the linked list. In fact, we do not have any method to fetch the previous node.</p>
<p>Without the knowledge of the previous node, it's not possible to delete the current node.</p></li>
<li><p>Notice that we are told the given node is not a tail node. Therefore, we can delete the next node instead of the current node given, and "pretend" that the node we are given is the next node.</p></li>
</ul>
<p>Using this intuition, let's understand how to implement this problem.</p>
<h4 id="algorithm">Algorithm</h4>
<p>By analyzing the above two key observations, we can derive the following algorithm,</p>
<ul>
<li>Store the next node in a temporary variable.</li>
<li>Copy data of the next node to the current node.</li>
<li>Change the next pointer of the current node to the next pointer of the next node.</li>
</ul>
<blockquote>
  <p>Note: Above 3 steps makes sure that your current node becomes same as next node and then you can safely delete next node from the Linked List</p>
</blockquote>
<p><em>Steps</em></p>
<ol>
<li><p>Initial Linked List</p>
<ul>
<li><img src="https://leetcode.com/articles/Figures/237/Initially.png" alt="Initially" referrerpolicy="no-referrer"></li></ul></li>
<li><p>Update current node with next node details</p></li>
</ol>
<ul>
<li><img src="https://leetcode.com/articles/Figures/237/updateValue.png" alt="Updating Node" referrerpolicy="no-referrer"></li>
</ul>
<ol>
<li>Update current node next pointer with next node next pointer</li>
</ol>
<ul>
<li><img src="https://leetcode.com/articles/Figures/237/updatePointer.png" alt="Updating Pointer" referrerpolicy="no-referrer"></li>
</ul>
<h4 id="implementation">Implementation</h4>
<iframe src="https://leetcode.com/playground/9pF6WBfP/shared" frameborder="0" width="100%" height="276" name="9pF6WBfP"></iframe>
<h4 id="complexityanalysis">Complexity Analysis</h4>
<p>Time Complexity: $O(1)$ since only 1 node needs to be updated and we only traverse one node behind.</p>
<p>Space Complexity: $O(1)$, since we use constant extra space to track the next node.</p>  
</div>
            