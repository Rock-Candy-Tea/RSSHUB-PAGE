
---
title: '52. N-Queens II'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2020/11/13/queens.jpg'
author: LeetCode
comments: false
date: Wed, 07 Apr 2021 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2020/11/13/queens.jpg'
---

<div>   
<p>The <strong>n-queens</strong> puzzle is the problem of placing <code>n</code> queens on an <code>n x n</code> chessboard such that no two queens attack each other.</p>

<p>Given an integer <code>n</code>, return <em>the number of distinct solutions to the <strong>n-queens puzzle</strong></em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> n = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two distinct solutions to the 4-queens puzzle as shown.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= n <= 9</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>A brute force solution would involve generating all possible board states with N queens. There are $$N^2$$ possible squares to place the first queen, $$N^2 - 1$$ to place the second and so on. This leads to a time complexity of $$O(N^N)$$, which is far too slow. The actual number of solutions is <strong>way</strong> smaller than the number of possible board states, so we should aim to minimize our consideration of invalid board states.</p>
<p>Imagine if we tried to generate all board states by placing queens down one by one. For 8 queens on a normal chessboard, let's say we place the first queen on the top left (index <code>(0, 0)</code>, or, if you are familiar with Chess, <code>a8</code>). Then, we place the second queen to its right (index <code>(0, 1)</code>, or <code>b8</code>). </p>
<p><img src="https://leetcode.com/articles/Figures/52/board_example.png" width="960" referrerpolicy="no-referrer"></p>
<p>There are <strong>44,261,653,680</strong> possible ways to place the remaining 6 queens, but we already know that every single one of them is invalid, because the first 2 queens can attack each other.</p>
<p><br></p>
<hr>
<h4 id="approachbacktracking">Approach: Backtracking</h4>
<p><strong>Intuition</strong></p>
<p>We can still follow the strategy of generating board states, but we should never place a queen on an attacked square. This is a perfect problem for backtracking - place the queens one by one, and when all possibilities are exhausted, backtrack by removing a queen and placing it elsewhere.</p>
<blockquote>
  <p>If you're not familiar with backtracking, check out the backtracking section of our <a href="https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/">Recursion II Explore Card</a>.</p>
</blockquote>
<p>Given a board state, and a possible placement for a queen, we need a smart way to determine whether or not that placement would put the queen under attack. A queen can be attacked if another queen is in any of the 4 following positions: on the same row, on the same column, on the same diagonal, or on the same anti-diagonal.</p>
<p>Recall that to implement backtracking, we implement a <code>backtrack</code> function that makes some changes to the state, calls itself again, and then when that call returns it undoes those changes (this last part is why it's called "backtracking").</p>
<p>Each time our <code>backtrack</code> function is called, we can encode state in the following manner:</p>
<ul>
<li><p>To make sure that we only place 1 queen per <strong>row</strong>, we will pass an integer argument <code>row</code> into <code>backtrack</code>, and will only place one queen during each call. Whenever we place a queen, we'll move onto the next row by calling <code>backtrack</code> again with the parameter value <code>row + 1</code>.</p></li>
<li><p>To make sure we only place 1 queen per <strong>column</strong>, we will use a set. Whenever we place a queen, we can add the column index to this set.</p></li>
</ul>
<p>The diagonals are a little trickier - but they have a property that we can use to our advantage.</p>
<ul>
<li>For each square on a given <strong>diagonal</strong>, the difference between the row and column indexes <code>(row - col)</code> will be constant. Think about the diagonal that starts from <code>(0, 0)</code> - the $$i^&#123;th&#125;$$ square has coordinates <code>(i, i)</code>, so the difference is always 0.</li>
</ul>
<p><img src="https://leetcode.com/articles/Figures/52/diagonals.png" width="960" referrerpolicy="no-referrer"></p>
<ul>
<li>For each square on a given <strong>anti-diagonal</strong>, the sum of the row and column indexes <code>(row + col)</code> will be constant. If you were to start at the highest square in an anti-diagonal and move downwards, the row index increments by 1 <code>(row + 1)</code>, and the column index decrements by 1 <code>(col - 1)</code>. These cancel each other out.</li>
</ul>
<p><img src="https://leetcode.com/articles/Figures/52/antidiagonals.png" width="960" referrerpolicy="no-referrer"></p>
<p>Whenever we place a queen, we should calculate the diagonal and the anti-diagonal value it belongs to. In the same way we had a set for the column, we should also have a set for both the diagonals and anti-diagonals. Then, we can put the values for this queen into the corresponding sets. Then, we can put the values for this queen into the corresponding sets.</p>
<p><strong>Algorithm</strong></p>
<p>We'll create a recursive function <code>backtrack</code> that takes 4 arguments to maintain the board state. The first parameter is the row we're going to place a queen on next, and the other 3 are sets that track which columns, diagonals, and anti-diagonals have already had queens placed on them. The function will work as follows:</p>
<ol>
<li><p>If the current row we are considering is greater than <code>n</code>, then we have a solution. Return <code>1</code>.</p></li>
<li><p>Initiate a local variable <code>solutions = 0</code> that represents all the possible solutions that can be obtained from the current board state.</p></li>
<li><p>Iterate through the columns of the current row. At each column, we will attempt to place a queen at the square <code>(row, col)</code> - remember we are considering the current row through the function arguments.</p>
<ul>
<li>Calculate the diagonal and anti-diagonal that the square belongs to. If there has been no queen placed yet in the column, diagonal, or anti-diagonal, then we can place a queen in this column, in the current row.</li>
<li>If we can't place the queen, skip this column (move on to try with the next column).</li></ul></li>
<li><p>If we were able to place a queen, then update our 3 sets (<code>cols</code>, <code>diagonals</code>, and <code>antiDiagonals</code>), and call the function again, but with <code>row + 1</code>.</p></li>
<li><p>The function call made in step 4 explores all valid board states with the queen we placed in step 3. Since we're done exploring that path, backtrack by removing the queen from the square - this just means removing the values we added to our sets.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/E7QpoB9J/shared" frameborder="0" width="100%" height="500" name="E7QpoB9J"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(N!)$$, where $$N$$ is the number of queens (which is the same as the width and height of the board).</p>
<p>Unlike the brute force approach, we place a queen only on squares that aren't attacked. For the first queen, we have $$N$$ options. For the next queen, we won't attempt to place it in the same column as the first queen, and there must be at least one square attacked diagonally by the first queen as well. Thus, the maximum number of squares we can consider for the second queen is $$N - 2$$. For the third queen, we won't attempt to place it in 2 columns already occupied by the first 2 queens, and there must be at least two squares attacked diagonally from the first 2 queens. Thus, the maximum number of squares we can consider for the third queen is $$N - 4$$. This pattern continues, giving an approximate time complexity of $$N!$$ at the end.</p></li>
<li><p>Space complexity: $$O(N)$$, where $$N$$ is the number of queens (which is the same as the width and height of the board).</p>
<p>Extra memory used includes the 3 sets used to store board state, as well as the recursion call stack. All of this scales linearly with the number of queens.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            