
---
title: '54. Spiral Matrix'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg'
author: LeetCode
comments: false
date: Mon, 16 Aug 2021 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg'
---

<div>   
<p>Given an <code>m x n</code> <code>matrix</code>, return <em>all elements of the</em> <code>matrix</code> <em>in spiral order</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong>Example 2:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>m == matrix.length</code></li>
<li><code>n == matrix[i].length</code></li>
<li><code>1 <= m, n <= 10</code></li>
<li><code>-100 <= matrix[i][j] <= 100</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>The problem statement asks us to <em>return all elements of the <code>matrix</code> in spiral order</em>, which means we will start from the top left corner and move towards right, then down, then left, and then up. Let's break this into further details:</p>
<ol>
<li>We can achieve moving in different directions by modifying row and column indices. Specifically, we have:</li>
</ol>
<pre><code class="plain language-plain">Given that we are at (row, col), where row is the row index, and col is the column index.

move right: (row, col + 1)
move downwards: (row + 1, col)
move left: (row, col - 1)
move upwards: (row - 1, col)
</code></pre>
<ol start="2">
<li>When shall we change our direction? We need to turn when we either <em>reach the matrix boundaries</em>, or we <em>reach the cells in the array that we have visited before</em>. Matrix boundaries are fixed and provided already, but how could we know if we have visited a particular cell or not?
In fact, we have two different strategies and they will be introduced in the following approaches. Generally speaking, they are as follows:</li>
</ol>
<ul>
<li>Approach 1. We can move the boundaries towards the center of the matrix after we have traversed a row or a column. Then when we meet a boundary, we know it's time to change the direction and update the boundary.</li>
<li>Approach 2. While traversing the matrix, we can record each location that we have visited. Then when we meet a matrix boundary or a previously visited cell, we know it's time to change the direction.</li>
</ul>
<blockquote>
  <p>This is a good time to stop and see if you can come up with the implementations yourselves!</p>
</blockquote>
<p><br></p>
<hr>
<h4 id="approach1setupboundaries">Approach 1: Set Up Boundaries</h4>
<p><strong>Intuition</strong></p>
<p>Our goal is to update boundaries as follows: when we finish traversing a row or column, we want to set up a boundary on it so that next time we get there, we know we need to change the direction. Here is a demo for the first round of updating the top, right, bottom, and left boundaries.</p>
<p>!?!../Documents/54<em>spiral</em>matrix.json:1920,1080!?!</p>
<p><br></p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize the top, right, bottom, and left boundaries as <code>up</code>, <code>right</code>, <code>down</code>, and <code>left</code>.</li>
<li>Initialize the output array <code>result</code>.</li>
<li>Traverse the elements in spiral order and add each element to <code>result</code>:<ul>
<li>Traverse from <code>left</code> boundary to <code>right</code> boundary.</li>
<li>Traverse from <code>up</code> boundary to <code>down</code> boundary.</li>
<li>Before we traverse from right to left, we need to make sure that we are not on a row that has already been traversed. If we are not, then we can traverse from <code>right</code> to <code>left</code>.</li>
<li>Similarly, before we traverse from top to bottom, we need to make sure that we are not on a column that has already been traversed. Then we can traverse from <code>down</code> to <code>up</code>.</li>
<li>Remember to move the boundaries by updating <code>left</code>, <code>right</code>, <code>up</code>, and <code>down</code> accordingly.</li></ul></li>
<li>Return <code>result</code>.</li>
</ol>
<iframe src="https://leetcode.com/playground/Zi2NiW6U/shared" frameborder="0" width="100%" height="500" name="Zi2NiW6U"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$M$$ be the number of rows and $$N$$ be the number of columns.</p>
<ul>
<li><p>Time complexity: $$O(M \cdot N)$$. This is because we visit each element once.</p></li>
<li><p>Space complexity: $$O(1)$$. This is because we don't use other data structures. Remember that we don't include the output array in the space complexity.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2markvisitedelements">Approach 2: Mark Visited Elements</h4>
<p><strong>Intuition</strong></p>
<p>If we mark the cells that we have visited, then when we run into a visited cell, we know we need to turn.</p>
<blockquote>
  <p>How do we know which direction we need to turn to? Well, we are always following this loop: right, down, left, up, right again, and so on. Therefore, when we run into a cell that we have visited, we can simply turn to the next direction in the aforementioned loop.</p>
</blockquote>
<p>Note that elements in the matrix are constrained to <code>-100 <= matrix[row][col] <= 100</code>, therefore we can select a number that is out of this range to mark it. In this article, <code>101</code> is selected for marking purposes.</p>
<blockquote>
  <p>Modifying the original data may not be a good choice sometimes. Therefore, we can also prepare another boolean matrix to store the cells we visited. However, the implementation of this approach is quite similar. You are welcome to explore this implementation as an exercise.</p>
</blockquote>
<p>The last puzzle piece is when shall we stop. An interesting observation is that if we reach the visited cell, we need to turn.  However, when we meet another visited cell immediately after changing the direction, it means we reached the last element in the matrix. You'll see that an integer <code>changeDirection</code> is used to track the number of times we changed the direction consecutively.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Initializations:<ul>
<li>Initialize a 2D array <code>directions</code> to represent the four directions that we will move.</li>
<li>Initialize <code>currentDirection</code> to 0 to signify that we are moving right at the beginning.</li>
<li>Initialize <code>VISITED</code> to 101 to mark visited cells.</li>
<li>Initialize <code>changeDirection</code> to 0.</li>
<li>Initialize <code>row</code> and <code>col</code> to 0 since our initial position is <code>(0, 0)</code>.</li></ul></li>
<li>We follow the current direction until we reach the matrix boundaries or a visited cell.<ul>
<li>While traversing in the current direction, remember to reset <code>changeDirection</code> to 0 at every step.</li>
<li>Move to the next cell by updating the row and column indices.</li>
<li>Append the element to the result and mark the location as visited.</li></ul></li>
<li>Update the direction and <code>changeDirection</code>. If <code>changeDirection</code> is larger than 1, it means we are continuously changing our directions, and therefore we've visited all of the elements.</li>
</ul>
<iframe src="https://leetcode.com/playground/VyCCgRAL/shared" frameborder="0" width="100%" height="500" name="VyCCgRAL"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$M$$ be the number of rows and $$N$$ be the number of columns.</p>
<ul>
<li><p>Time complexity: $$O(M \cdot N)$$. This is because we visit each element once.</p></li>
<li><p>Space complexity: $$O(1)$$. This is because we don't use other data structures. Remember that we don't consider the output array or the input matrix when calculating the space complexity. However, if we were prohibited from mutating the input matrix, then this would be an $$O(M \cdot N)$$ space solution.  This is because we would need to use a boolean matrix to track all of the previously seen cells.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            