
---
title: '876. Middle of the Linked List'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg'
author: LeetCode
comments: false
date: Thu, 18 Aug 2022 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg'
---

<div>   
<p>Given the <code>head</code> of a singly linked list, return <em>the middle node of the linked list</em>.</p>

<p>If there are two middle nodes, return <strong>the second middle</strong> node.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg" style="width: 544px; height: 65px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [3,4,5]
<strong>Explanation:</strong> The middle node of the list is node 3.
</pre>

<p><strong>Example 2:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg" style="width: 664px; height: 65px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> head = [1,2,3,4,5,6]
<strong>Output:</strong> [4,5,6]
<strong>Explanation:</strong> Since the list has two middle nodes with values 3 and 4, we return the second one.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li>The number of nodes in the list is in the range <code>[1, 100]</code>.</li>
<li><code>1 <= Node.val <= 100</code></li>
</ul><p>[TOC]</p>
<h2 id="videosolution">Video Solution</h2>
<hr>
<div class="video-preview"></div>
<h2 id="solutionarticle">Solution Article</h2>
<hr>
<h4 id="approach1outputtoarray">Approach 1: Output to Array</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Put every node into an array <code>A</code> in order.  Then the middle node is just <code>A[A.length // 2]</code>, since we can retrieve each node by index.</p>
<p>We can initialize the array to be of length <code>100</code>, as we're told in the problem description that the input contains between <code>1</code> and <code>100</code> nodes.</p>
<iframe src="https://leetcode.com/playground/FxMEQfWD/shared" frameborder="0" width="100%" height="242" name="FxMEQfWD"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given list.</p></li>
<li><p>Space Complexity:  $$O(N)$$, the space used by <code>A</code>.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2fastandslowpointer">Approach 2: Fast and Slow Pointer</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>When traversing the list with a pointer <code>slow</code>, make another pointer <code>fast</code> that traverses twice as fast.  When <code>fast</code> reaches the end of the list, <code>slow</code> must be in the middle.</p>
<iframe src="https://leetcode.com/playground/5RXifTh4/shared" frameborder="0" width="100%" height="259" name="5RXifTh4"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given list.</p></li>
<li><p>Space Complexity:  $$O(1)$$, the space used by <code>slow</code> and <code>fast</code>.
<br>
<br></p></li>
</ul>  
</div>
            