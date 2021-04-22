
---
title: '120. Triangle'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/120/triangle_coordinates.png'
author: LeetCode
comments: false
date: Tue, 20 Apr 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/120/triangle_coordinates.png'
---

<div>   
<p>Given a <code>triangle</code> array, return <em>the minimum path sum from top to bottom</em>.</p>

<p>For each step, you may move to an adjacent number of the row below. More formally, if you are on index <code>i</code> on the current row, you may move to either index <code>i</code> or index <code>i + 1</code> on the next row.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The triangle looks like:
   <u>2</u>
  <u>3</u> 4
 6 <u>5</u> 7
4 <u>1</u> 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> triangle = [[-10]]
<strong>Output:</strong> -10
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= triangle.length <= 200</code></li>
<li><code>triangle[0].length == 1</code></li>
<li><code>triangle[i].length == triangle[i - 1].length + 1</code></li>
<li><code>-10<sup>4</sup> <= triangle[i][j] <= 10<sup>4</sup></code></li>
</ul>

<p> </p>
<strong>Follow up:</strong> Could you do this using only <code>O(n)</code> extra space, where <code>n</code> is the total number of rows in the triangle?<p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>As it's always better to try and solve problems on your own before you read the official solution, here are a couple of related, but easier, problems you might like to try first if you're stuck on this problem.</p>
<ol>
<li><p><code>Triangle</code> is a variant of the falling path sum problem - a classic dynamic programming problem. If you're not at all familiar with dynamic programming, then we recommend starting with <a href="https://leetcode.com/problems/minimum-falling-path-sum/">931. Minimum Falling Path Sum</a>, as the idea is the same, but the solution is a bit simpler due to all rows being the same length.</p></li>
<li><p>A simpler triangle-related dynamic programming problem is <a href="https://leetcode.com/problems/pascals-triangle/">118. Pascal's Triangle</a>. If you haven't already solved it, then you should do that now.</p></li>
</ol>
<p><br></p>
<hr>
<h4 id="approach1dynamicprogrammingbottomupinplace">Approach 1: Dynamic Programming (Bottom-up: In-place)</h4>
<p><strong>Intuition</strong></p>
<p>A good way to get started on a problem like this is to make a very small example, and then figure out how to solve it. After that, make the example a bit bigger, and see if you can still solve it. Try and come up with a general way of solving the problem, regardless of the size.</p>
<p>!?!../Documents/120<em>animation</em>1.json:960,540!?!</p>
<p><br></p>
<p>As you hopefully realized from the animation, we can solve the problem by iterating through each row of the triangle, from top to bottom, updating each number to be the sum of itself + the minimum out of the two numbers above it.</p>
<p>!?!../Documents/120<em>animation</em>2.json:960,540!?!</p>
<p><br></p>
<p><strong>Algorithm</strong></p>
<p>The simplest way of implementing this is to overwrite the input. In other words, as an in-place algorithm. In Approach 2, we'll look at how to modify the algorithm so that it doesn't overwrite the input, but doesn't require more than $$O(n)$$ extra space.</p>
<p>When this algorithm has finished running, each cell, <code>(row, col)</code> of the input triangle will be overwritten with the minimal path sum from <code>(0, 0)</code> (the triangle tip), down to and including <code>(row, col)</code>.</p>
<blockquote>
  <p><strong>Interview Tip: In-place Algorithms</strong></p>
  <p>In-place algorithms overwrite the input to save space, but sometimes this can cause problems. Here are a couple of situations where an in-place algorithm might not be suitable.</p>
  <ol>
  <li>The algorithm needs to run in a <em>multi-threaded</em> environment, without exclusive access to the array. Other threads might need to read the array too, and might not expect it to be modified.</li>
  <li>Even if there is only a single thread, or the algorithm has exclusive access to the array while running, the array might need to be reused later or by another thread once the lock has been released.</li>
  </ol>
  <p>In an interview, you should always check whether or not the interviewer minds you overwriting the input. Be ready to explain the pros and cons of doing so if asked!</p>
</blockquote>
<p>We need to be quite careful designing our algorithm: the rows and columns are all different sizes, greatly increasing the risk of off-by-one errors. The rows are numbered from top to bottom (so the triangle tip is the first row), and the columns are numbered left to right. Here is a diagram showing the <code>(row, col)</code> coordinate for a triangle with <code>4</code> rows.</p>
<p><img src="https://leetcode.com/articles/Figures/120/triangle_coordinates.png" alt="img" referrerpolicy="no-referrer"></p>
<p>Combining this diagram with what we determined before, we can deduce the following rules for obtaining the cells above a cell with coordinate <code>(row, col)</code>.</p>
<ol>
<li>If <code>row == 0</code>: This is the top of the triangle: it stays the same.</li>
<li>If <code>col == 0</code>: There is only one cell above, located at <code>(row - 1, col)</code>.</li>
<li>If <code>col == row</code>: There is only one cell above, located at <code>(row - 1, col - 1)</code>.</li>
<li>In all other cases: There are two cells above, located at <code>(row - 1, col - 1</code>) and <code>(row - 1, col)</code> .</li>
</ol>
<p>We can collapse cases 2, 3, and 4 into two overlapping cases by recognizing that case 4 simply cases 2 and 3 combined.</p>
<p>Putting everything together, we get the following algorithm.</p>
<ul>
<li>Iterate through each <code>row</code> index between <code>1</code> and <code>n - 1</code> inclusive (where <code>n</code> is the number of rows in triangle):</li>
<li>Iterate through each <code>col</code> index between <code>0</code> and <code>row</code> inclusive:<ul>
<li>Initialize a variable <code>smallestAbove</code> to positive infinity:</li>
<li>If <code>col > 0</code>:</li>
<li>Set <code>smallestAbove</code> to <code>triangle[row - 1][col - 1]</code>.</li>
<li>If <code>col < row</code>:</li>
<li>Set <code>smallestAbove</code> to be the <code>min</code> out of itself and <code>triangle[row - 1][col]</code>.</li>
<li>Set <code>triangle[row][col]</code> to be itself plus <code>smallestAbove</code>.
Return the minimum value in <code>triangle[n - 1]</code>.</li></ul></li>
</ul>
<iframe src="https://leetcode.com/playground/HPoGaA3j/shared" frameborder="0" width="100%" height="361" name="HPoGaA3j"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the number of rows in the triangle.</p>
<ul>
<li><p>Time Complexity: $$O(n^2)$$. </p>
<p>A triangle with $$n$$ rows and $$n$$ columns contains $$\dfrac&#123;n (n + 1)&#125;&#123;2&#125; = \dfrac&#123;n^2 + n&#125;&#123;2&#125;$$ cells. Recall that in big O notaton, we ignore the less significant terms. This gives us $$O\bigg(\dfrac&#123;n^2 + n&#125;&#123;2&#125;\bigg) = O(n^2)$$ cells. For each cell, we are performing a constant number of operatons, therefore giving us a total time complexity of $$O(n^2)$$.</p></li>
<li><p>Space Complexity: $$O(1)$$.</p>
<p>As we're overwriting the input, we don't need any collections to store our calculations.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2dynamicprogrammingbottomupauxiliaryspace">Approach 2: Dynamic Programming (Bottom-up: Auxiliary Space)</h4>
<p><strong>Intuition</strong></p>
<p>As mentioned in Approach 1, it isn't always desirable to overwrite the input array. It is quite likely, in fact, that your interviewer will expect you to treat it as read-only.</p>
<p>The most obvious solution here is to create a copy of the input, and then run Approach 1's algorithm over it. The downside of this is that it will require $$O(n^2)$$ space, due to there being $$\dfrac&#123;n^2 + n&#125;&#123;2&#125;$$ cells in the triangle. Seeing as the problem description suggests that we use $$O(n)$$ space, we should be trying to do better.</p>
<p>Observe that as we worked our way down the rows of the triangle, we only ever needed to look at the row immediately above. This means that we only need to maintain the current row and the previous row. Because a row contains at most $$n$$ cells, this will meet the $$O(n)$$ space requirement.</p>
<p><strong>Algorithm</strong></p>
<p>This approach is almost the same as Approach 1. The only difference is that we need to write the new values for the current row into an extra list (or array), and then keep track of the previous one of these lists.</p>
<iframe src="https://leetcode.com/playground/MoMAako8/shared" frameborder="0" width="100%" height="395" name="MoMAako8"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity: $$O(n^&#123;2&#125;)$$.</p>
<p>Same as Approach 1. We are still performing a constant number of operations for each cell in the input triangle.</p></li>
<li><p>Space Complexity: $$O(n)$$. </p>
<p>We're using two arrays of up to size $$n$$ each: <code>prevRow</code> and <code>currRow</code>. While this is a higher space complexity than Approach 1, the advantage of this approach is that the input triangle remains unmodified.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3dynamicprogrammingbottomupfliptriangleupsidedown">Approach 3: Dynamic Programming (Bottom-up: Flip Triangle Upside Down)</h4>
<p><strong>Intuition</strong></p>
<p>The problem description tells us that we need to find the minimum path sum from top to bottom. This immediately suggests that we should be working from top to bottom, like what we did in Approaches 1 and 2.</p>
<p><em>But is this actually necessary? Could we go from bottom to top instead?</em></p>
<p>It turns out, we can! The exact same ideas apply - each cell instead becomes the sum of itself plus the minimum of the two cells below it. The only difference is that we need to do the edge case handling a bit differently. </p>
<p><img src="https://leetcode.com/articles/Figures/120/upside_down_triangle_coordinates.png" alt="img" referrerpolicy="no-referrer"></p>
<p>There is a big advantage though: the code turns out a <strong>lot</strong> simpler. Some of the cells only had one cell above them. But every cell has two cells below it! </p>
<blockquote>
  <p><strong>Interview Tip:</strong> Practice Overriding Your Brains "Assume" Mode!</p>
  <p>We humans have a habit of making a lot of assumptions - neurobiologists reassure us that this is quite normal! If we didn't make lots of assumptions, our brains would slow to a crawl like a poorly maintained computer, thanks to the overload of additional information they'd have to process. </p>
  <p>In an interview situation, where most of us are at least a little nervous, we are even less likely to question our assumptions. The moment most of us realize that we can solve the problem using the top-to-bottom approach, we will be frantically coding it up to show our interviewer that we can solve the problem. </p>
  <p>But this isn't ideal! In an interview, and when solving difficult problems in general, you need to learn to identify the assumptions you're making, and question them in your mind. In some problems, this can be things like assuming that input is sorted, that there will be no invalid cases, that they won't mind you overwriting the input, or even that the environment is single-threaded. In this case, the assumption is assuming that the only way of solving this problem is to work from top to bottom.</p>
  <p>The only way to get good at challenging your assumptions is lots of practice. Working in a group with other people preparing for code interviews can help too - learning how other people see problems will widen your own way of seeing problems.</p>
</blockquote>
<p><strong>Algorithm</strong></p>
<p>Like before, we can do this either in place or by overwriting the input. This algorithm will assume that we're overwriting the input, although I've provided the actual code below for both.</p>
<p>When we worked from top to bottom, the cells had only one cell above them. But when we work from bottom to top, all cells, except for those in the bottom row (which are our base case and so don't need to be modified anyway) have exactly two cells below them. Where <code>(row, col)</code> is the current cell, the cells below are located at <code>(row + 1, col)</code> and <code>(row + 1, col + 1)</code>. At the end, the answer will be in <code>triangle[0][0]</code>.</p>
<p>Putting everything together, we get the following algorithm.</p>
<ul>
<li>Iterate <strong>up</strong> through each <code>row</code> index between <code>n - 2</code> and <code>0</code> inclusive (where <code>n</code> is the number of rows in triangle):</li>
<li>Iterate through each <code>col</code> index between <code>0</code> and <code>row</code> inclusive:<ul>
<li>Set <code>smallestBelow</code> to be the <code>min</code> out of <code>triangle[row + 1][col]</code> and <code>triangle[row + 1][col + 1]</code>.</li>
<li>Set <code>triangle[row][col]</code> to be itself plus <code>smallestBelow</code>.</li></ul></li>
<li>Return <code>triangle[0][0]</code></li>
</ul>
<p>Here is the in-place implementation. When this algorithm has finished running, each cell, <code>(row, col)</code> of the input triangle will be overwritten with the minimal path sum from <code>(row, col)</code> to any cell on the bottom <code>row</code>.</p>
<iframe src="https://leetcode.com/playground/XmRYaUUT/shared" frameborder="0" width="100%" height="276" name="XmRYaUUT"></iframe>
<p>And here is the auxiliary space implementation.</p>
<iframe src="https://leetcode.com/playground/VhKv5w9f/shared" frameborder="0" width="100%" height="293" name="VhKv5w9f"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>The time and space complexity for Approach 3 depends on which implementation you're looking at. The in-place implementation has the same complexity analysis as Approach 1, whereas the auxiliary space implementation has the same complexity analysis as Approach 2.</p>
<p><br></p>
<hr>
<h4 id="approach4memoizationtopdown">Approach 4: Memoization (Top-Down)</h4>
<p><strong>Intuition</strong></p>
<p>Usually, for dynamic programming problems, we start with a recursive <a href="https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/">memoization-based approach</a>, and then figure out how to convert it to an iterative dynamic programming (tabulaton) approach. For this particular problem, most people will more naturally think of the problem in terms of iterative dynamic programming from the start though. But it is still worth having a look at how we could instead use memoization.</p>
<p><strong>Algorithm</strong></p>
<p>We'll define a recursive helper function <code>minPath(row, col)</code> that returns the minimum path sum from the cell at <code>(row, col)</code>, down to the base of the triangle. The minimum path sum for the entire triangle, would, therefore, be <code>minPath(0, 0)</code>.</p>
<p>The recursive case is where there is still at least one row below the current cell. Like before, we simply need to add the current cell to the minimum path sum of the cells below it. That is:</p>
<p><code>return triangle[row][col] + min(minPath(row + 1, col), minPath(row + 1, col + 1))</code></p>
<p>The base case is where there are no more rows below. In this case, we should simply return the current cell's value:</p>
<p><code>return triangle[row][col]</code></p>
<p>To avoid re-calculating the same results over and over again, we can use a <code>memoization</code> table.</p>
<iframe src="https://leetcode.com/playground/hoD5bS2S/shared" frameborder="0" width="100%" height="480" name="hoD5bS2S"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the number of rows in the triangle.</p>
<ul>
<li><p>Time Complexity: $$O(n^2)$$.</p>
<p>There are two steps to analyzing the time complexity of an algorithm that uses recursive memoization.</p>
<p>Firstly, determine what the cost of each call to the recursive function is. That is, how much time is spent actively executing instructions within a single call. It does not include time spent in functions called by that function.</p>
<p>Secondly, determine how many times the recursive function is called.</p>
<p>Each call to <code>minPath</code> is $$O(1)$$, because there are no loops. The memoization table ensures that <code>minPath</code> is only called once for each cell.  As there are $$n^2$$ cells, we get a total time complexity of $$O(n^2)$$.</p></li>
<li><p>Space Complexity: $$O(n^2)$$. </p>
<p>Each time a base case cell is reached, there will be a path of $$n$$ cells on the run-time stack, going from the triangle tip, down to that base case cell. This means that there is $$O(n)$$ space on the run-time stack.</p>
<p>Each time a subproblem is solved (a call to <code>minPath</code>), its result is stored in a memoization table. We determined above that there are $$O(n^2)$$ such subproblems, giving a total space complexity of $$O(n^2)$$ for the memoization table.</p></li>
</ul>  
</div>
            