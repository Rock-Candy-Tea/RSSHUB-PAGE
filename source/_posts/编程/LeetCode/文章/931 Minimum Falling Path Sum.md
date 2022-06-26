
---
title: '931. Minimum Falling Path Sum'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg'
author: LeetCode
comments: false
date: Fri, 03 Jun 2022 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg'
---

<div>   
<p>Given an <code>n x n</code> array of integers <code>matrix</code>, return <em>the <strong>minimum sum</strong> of any <strong>falling path</strong> through</em> <code>matrix</code>.</p>

<p>A <strong>falling path</strong> starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position <code>(row, col)</code> will be <code>(row + 1, col - 1)</code>, <code>(row + 1, col)</code>, or <code>(row + 1, col + 1)</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg" style="width: 499px; height: 500px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> matrix = [[2,1,3],[6,5,4],[7,8,9]]
<strong>Output:</strong> 13
<strong>Explanation:</strong> There are two falling paths with a minimum sum as shown.
</pre>

<p><strong>Example 2:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg" style="width: 164px; height: 365px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> matrix = [[-19,57],[-40,-5]]
<strong>Output:</strong> -59
<strong>Explanation:</strong> The falling path with a minimum sum is shown.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>n == matrix.length == matrix[i].length</code></li>
<li><code>1 <= n <= 100</code></li>
<li><code>-100 <= matrix[i][j] <= 100</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>Given a 2D <code>matrix(row, col)</code>, we have to find the sum of the minimum falling path in a matrix.
To begin with, let's try to understand, what is a falling path?
To put it in simple words, it is a path that satisfies the following criteria,</p>
<ol>
<li>A falling path is a path that begins at <strong>any</strong> cell in the first row of the matrix and ends at <strong>any</strong> cell in the last row of the matrix.</li>
<li>From a certain cell <code>(row, col)</code> in the falling path, we can only move to 3 possible cells, <code>(row + 1, col)</code> , <code>(row + 1, col + 1)</code>, <code>(row + 1, col - 1)</code>.</li>
</ol>
<p></p><center>
<img src="https://leetcode.com/articles/Figures/931/931_overview.png" referrerpolicy="no-referrer">
</center><p></p>
<p>As the name suggests, the falling path sum is the sum of values of all the cells in the chosen path. Our goal is to find the minimum sum from all possible paths. Let's consider different approaches that can be used to solve this problem. We will begin with the brute force approach and optimize it using dynamic programming.</p>
<h2 id="br"><br></h2>
<h4 id="approach1bruteforceusingdepthfirstsearch">Approach 1: Brute Force Using Depth First Search</h4>
<p><strong>Intuition</strong></p>
<p>Brute Force is generally the straightforward approach to solving the problem. You can think of the brute force approach as</p>
<p>"Given pen and paper in your hand, how will you try to solve the problem"?</p>
<p>Though the brute force approach is considered to be the most exhaustive and unoptimized approach, implementing this approach first gives a deeper understanding of the basis of the problem, which can further help to shape a better-optimized solution.</p>
<p>Let's understand the brute force approach with the following example,</p>
<p><img src="https://leetcode.com/articles/Figures/931/931_example_problem.png" alt="Example Problem" referrerpolicy="no-referrer"></p>
<blockquote>
  <p>Before reading the following section, try to find the minimum falling path for the above matrix on your own.</p>
</blockquote>
<p>In this example, if we start at cell <code>(0, 1)</code>, the next cell in the path could be <code>(1, 0)</code>, <code>(1, 1)</code>, or <code>(1, 2)</code>. From the current position, we cannot determine which path will give us the minimum path sum, so let's try all the possible paths.</p>
<p><img src="https://leetcode.com/articles/Figures/931/931_example_3possibilities.png" alt="Example Problem" referrerpolicy="no-referrer"></p>
<p>The minimum path sum from cell <code>(0, 1)</code> is "5" - going from <code>(0, 1)</code> to <code>(1, 2)</code>. Does that mean that we can greedily choose this path and move ahead, discarding the other paths?
Let's find the minimum falling path if we choose the path with the sum "5" i.e <code>(0, 1)</code> to <code>(1, 2)</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/931/931_Explore_greedy_path.png" alt="Example Problem, Explore One Path" referrerpolicy="no-referrer"></p>
<p>Thus, the minimum falling path sum is "14". Now, let's explore other paths starting from cell <code>(0, 1)</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/931/931_Explore_All_Paths.png" alt="Example Problem, Explore All Path" referrerpolicy="no-referrer"></p>
<p>The minimum falling path sum is now "13" i.e <code>(0, 1)</code> -> <code>(1, 1)</code> -> <code>(2, 0)</code>.</p>
<p>This proves that the greedy approach will not work for this problem. A sub-path with the lowest subset-sum cannot guarantee the lowest sum for the entire path. We must explore all possible paths to find the one with the smallest sum.</p>
<p>Since we have to try all paths from any cell, the solution must generate all the possible falling paths and track the one with a minimum sum. To try all possible combinations, we can perform a depth-first search on the matrix.</p>
<blockquote>
  <p>The Depth First Search is an exhaustive search process wherein we will traverse all the cells in a path. On reaching the end of the path, we must undo our last step in the current path and try a different possible next step to extend the path.</p>
</blockquote>
<p>Note: This approach is a brute force solution, and it is not expected to pass all test cases. This approach is included because, often, an intuitive way to approach problems like this one is to start by building a brute force solution and then modify it to achieve an optimized solution.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Implement a Depth First Search algorithm, by defining a recursive function, <code>findMinFallingPathSum(row, col)</code>, that recursively explores all the paths from the current cell (defined by parameters <code>row</code> and <code>col</code>).</li>
</ol>
<ul>
<li>Define Base Case:
In any recursive function, we must define the terminating condition i.e the base case. When the terminating condition is satisfied, we will exit the recursive search process. The base cases are as follows,<ul>
<li>The <code>row</code> or <code>col</code> values are not within the matrix boundaries.</li>
<li>We have reached the last row. In this case, we will return the value of the current cell and not make any other recursive calls.</li></ul></li>
<li><em>Recursively explore all paths:</em> If the base case is not satisfied, it means that we have not reached the end of our current path, and we must try all options to extend our path and find the one with the minimum sum:</li>
</ul>
<pre><code>minimumPath = Minimum(findMinFallingPathSum(row + 1, col + 1),
                      findMinFallingPathSum(row + 1, col),
                      findMinFallingPathSum(row + 1, col - 1))
</code></pre>
<ol start="2">
<li><p>Now that we have defined the recursive function, we must find the minimum falling path for all possible starting cells. A starting cell is any cell in the top row.</p>
<p>For this, we have to iterate using a <em>for</em> loop and find the minimum falling path for cell in $$0^&#123;th&#125;$$ row and columns ranging from $$0$$ to $$\text&#123;matrix.length&#125; - 1$$. Define a variable <code>minFallingSum</code> to track the minimum of all the falling paths found so far and return the result.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/Q6grBxnZ/shared" frameborder="0" width="100%" height="500" name="Q6grBxnZ"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of <code>matrix</code>.</p>
<ul>
<li><p>Time Complexity: $$O(&#123;N&#125; \cdot 3^&#123;N&#125;)$$ The solution takes the form of a 3-ary recursion tree where there are 3 possibilities for every node in the tree. The time complexity can be derived as follows,</p></li>
<li><p>The maximum depth of the recursion tree is equal to the number of rows in the matrix i.e $$N$$.</p></li>
<li><p>Each level (<code>level</code>) of the recursion tree will contain approximately $$3^\text&#123;level&#125;$$ nodes. For example, at level $$0$$ there are $$3^0$$ nodes, for level 1, $$3^&#123;1&#125;$$ nodes, and so on. Thus, the maximum number of nodes at level $$N$$ would be approximately $$3^&#123;N&#125;$$.</p></li>
<li><p>Thus the time complexity is roughly, $$O(&#123;N&#125; \cdot 3^&#123;N&#125;)$$.</p>
<p>The time complexity is exponential, hence this approach is exhaustive and results in <em>Time Limit Exceeded (TLE)</em>.</p></li>
<li><p>Space Complexity: $$O(N)$$ This space will be used to store the recursion stack. As the maximum depth of the tree is $$N$$, we will not have more than $$N$$ recursive calls on the call stack at any time.</p></li>
</ul>
<h2 id="br-1"><br></h2>
<h4 id="approach2topdowndynamicprogramming">Approach 2: Top Down Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>The brute force approach is exhaustive. To come up with the optimized solution for the problem, let's take a deeper look at the  following recursion tree,</p>
<p><img src="https://leetcode.com/articles/Figures/931/931_recursion_tree.png" alt="Example Problem, Recursion Tree" referrerpolicy="no-referrer"></p>
<p>In the above recursion tree, we can identify the repetitive sub-paths (circled in the same color). For example, <code>findMinPathSum(1, 0)</code> is calculated twice, <code>findMinPathSum(1, 1)</code> is calculated three times, and so on.</p>
<p>Repeated calculation of the same subproblems is the root cause of the exponential time complexity in the previous approach.  Although, what if our algorithm could remember the result for a subproblem when it is computed the first time and reuses the stored result every other time?</p>
<blockquote>
  <p>Pretend you are on a treasure hunt. On reaching point A, you travel to the destination and don't find anything there. You go back to some other path which again takes you to point A. You wouldn't explore the same path from point A again. You would say, "I have been here before; I know where this path goes."</p>
  <p>How can we make our algorithm think the same way? We can do so by marking every path we have visited so that if we reach the same path again, we know the result!!</p>
</blockquote>
<p>In <a href="https://leetcode.com/explore/featured/card/dynamic-programming/630/an-introduction-to-dynamic-programming/4034/">Dynamic Programming</a>, when a recursive problem solves the same subproblem multiple times, it has the Overlapping Subproblem property. Such problems can be optimized using a dynamic programming technique called Memoization.</p>
<p>As in the previous approach, each call to <code>findMinFallingPathSum</code> will return the minimum falling path sum between the current cell and the bottom of the <code>matrix</code>. However, in this approach, we will store the result of each call in the new parameter <code>memo</code>, and when we revisit this cell in a subsequent call, we will be able to reuse the stored result.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>In order to record the results of computation for every cell,  maintain a 2-dimensional matrix named <code>memo</code> where the value of <code>memo[row][col]</code> would give the minimum falling path starting from the cell <code>(row, col)</code>.</p></li>
<li><p>Implement a Depth First Search algorithm, by defining a recursive function, <code>findMinFallingPathSum(row, col)</code>, that recursively explores all the paths from the current cell (defined by parameters <code>row</code> and <code>col</code>).</p></li>
</ol>
<ul>
<li>Define Base Case:
In any recursive function, we must define the terminating condition i.e the base case. When the terminating condition is satisfied, we will exit the recursive search process. The base cases are as follows,<ul>
<li>The <code>row</code> or <code>col</code> values are not within the matrix boundaries.</li>
<li>We have reached the last row. In this case, we will return the value of the current cell and not make any other recursive calls.</li></ul></li>
<li><em>Recursively explore all paths:</em> If the base case is not satisfied, it means that we have not reached the end of our current path, and we must try all options to extend our path and find the one with the minimum sum:</li>
</ul>
<pre><code>minimumPath = Minimum(findMinFallingPathSum(row + 1, col + 1),
                      findMinFallingPathSum(row + 1, col),
                      findMinFallingPathSum(row + 1, col - 1))
</code></pre>
<ol start="3">
<li>To avoid repetitive computation of the results as in the brute force approach, we make use of stored results as follows,</li>
</ol>
<ul>
<li><p>Before recursively computing the result for the current cell, check if the <code>memo</code> has the result for the current cell. If so, return the result, otherwise, proceed with the recursive call to compute the result.</p></li>
<li><p>After computing the result, store the result in the <code>memo[row][col]</code>.</p></li>
</ul>
<ol start="3">
<li>Iteratively find the minimum falling path for all possible starting cells i.e cells in $$0^&#123;th&#125;$$ row and columns ranging from $$0$$ to $$\text&#123;matrix.length&#125; - 1$$. Track the minimum value in the variable <code>minFallingSum</code> and return the result.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/HL4Cuj6E/shared" frameborder="0" width="100%" height="500" name="HL4Cuj6E"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of <code>matrix</code>.</p>
<ul>
<li><p>Time Complexity: $$O(N^2)$$</p>
<p>For every cell in the matrix, we will compute the result only once and update the <code>memo</code>. For the subsequent calls, we are using the stored results that take $$O(1)$$ time. There are $$N^2$$ cells in the matrix, and thus $$N^2$$ dp states. So, the time complexity is $$O(N^2)$$.</p></li>
<li><p>Space Complexity: $$O(N^2)$$</p>
<p>The recursive call stack uses $$O(N)$$  space. As the maximum depth of the tree is $$N$$, we can’t have more than $$N$$ recursive calls on the call stack at any time. The 2D matrix <code>memo</code> uses $$O(N^2)$$ space. Thus, the space complexity is $$O(N) + O(N^2) = O(N^2)$$.</p></li>
</ul>
<h2 id="br-2"><br></h2>
<h4 id="approach3bottomupdynamicprogrammingtabulation">Approach 3: Bottom-Up Dynamic Programming (Tabulation)</h4>
<p><strong>Intuition</strong></p>
<p>The memoization technique follows the top-down approach. We start by finding the result for the original matrix and recursively move towards computing the result of smaller subproblems.</p>
<p>There is yet another technique to implement Dynamic Programming problems called bottom-up dynamic programming also known as, Tabulation. In the bottom-up approach, we start by finding the result of the smallest subproblem and iteratively move towards larger sub-problems. Being non-recursive in nature, this approach does not require maintaining a separate internal call stack for storing the intermediate state of recursion.</p>
<p>The results of subproblems are stored in a 2-dimensional table, <code>dp</code>. Here, the smallest sub-problem would be a matrix with only one row. Thus, we will first calculate the result for each cell in the last row (base case), call this the $$n^&#123;th&#125;$$ row, and store the results in <code>dp</code>. Next, when we move to the $$(n-1)^&#123;th&#125;$$ row, the results for the next row (i.e. the $$n^&#123;th&#125;$$ row) are already present. In this way, in every iteration, we are calculating and storing the result for the subsequent problem.</p>
<p>While this approach does not improve the time or space complexity compared to the top-down approach, it does act as a stepping stone towards the next approach where we will improve the space complexity.</p>
<p><strong>Algorithm</strong></p>
<p>Bottom-up Dynamic Programming follows an iterative approach to solving the problem. We have to start by finding the minimum falling path for the smallest possible matrix i.e the matrix having a single cell and one by one move towards the rest of the cells in the matrix.</p>
<ol>
<li><p>To compute the minimum falling path for a certain cell <code>(row, col)</code>, we must have pre-computed values for the minimum falling path for cells <code>(row + 1, col - 1)</code>, <code>(row + 1, col)</code> and <code>(row + 1, col + 1)</code>.  For this, we will iterate from $$(n-1)^&#123;th&#125;$$ row to $$0^&#123;th&#125;$$ row and from $$0^&#123;th&#125;$$ column to $$(n-1)^&#123;th&#125;$$ column.</p>
<blockquote>
  <p>Note: The order of iterating the columns does not matter in this case. Even if we iterate from $$(n-1)^&#123;th&#125;$$ to $$0^&#123;th&#125;$$ column, the results would be the same.</p>
</blockquote></li>
<li><p>Build a 2D matrix <code>dp</code> and compute the minimum falling path of current <code>row</code> and <code>col</code> as,</p>
<pre><code>    dp[row][col] = min(dp[row + 1][col - 1],
                       dp[row + 1][col],
                       dp[row + 1][col + 1]) + value of current (row, col) in matrix
</code></pre>
<p>Note: We must handle the edge cases, for example, if the col value is <code>0</code> or <code>n - 1</code>.</p></li>
<li><p>Once we have the value of the minimum falling path from every cell, we must get the result from the start cell. The start cell can be any cell on the first row. Thus, we will iterate over all the cells in the first row, and return the minimum value.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/6AXTLYiP/shared" frameborder="0" width="100%" height="500" name="6AXTLYiP"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of <code>matrix</code>.</p>
<ul>
<li><p>Time Complexity: $$O(N^&#123;2&#125;)$$</p></li>
<li><p>The nested for loop takes ($$N^&#123;2&#125;$$) times to fill the <code>dp</code> array.</p></li>
<li><p>Then, takes $$N$$ time to find the minimum falling path.</p></li>
<li><p>So, Time Complexity $$T(n) = O(N^&#123;2&#125;) + O(N) = O(N^&#123;2&#125;)$$</p></li>
<li><p>Space Complexity: $$O(N^&#123;2&#125;)$$. The additional space is used for <code>dp</code> array of size $$N^&#123;2&#125;$$.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach4spaceoptimizedbottomupdynamicprogramming">Approach 4: Space Optimized, Bottom-Up Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>The tabulation approach used $$O(N^&#123;2&#125;)$$ space to track the minimum falling path starting from every cell. But, in the end, to calculate the final result, we only need the minimum falling path of all the cells in the first row.</p>
<p>Furthermore, to calculate the values for cells in the row <code>n</code>, we only need the values of the <code>n + 1</code> row. So, after finding the results for row <code>n</code>, we no longer need to store the values for the <code>n + 1</code> row. As such, we can optimize the space complexity of the tabulation approach as follows,</p>
<ul>
<li>Calculate the values for all the cells in the current row <code>n</code> based on results for the cells in the <code>n + 1</code> row. Let's define a 1-dimensional array, <code>dp</code>, to store the results of the <code>n + 1</code> row.</li>
<li>As we move to the <code>n - 1</code> row, the current row becomes the <code>n + 1</code> row. So, we can discard the current values of <code>dp</code>, and begin to store the results for the current row in the <code>dp</code> array.</li>
</ul>
<p>In this way, instead of maintaining a 2-dimensional array the size of a <code>matrix</code>, we can just define two 1-dimensional arrays, one that stores the value of the current row and the other that has the results of the previous row.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Define a 1-dimensional array, <code>dp</code>, initialized with all values set to <code>0</code>,</p></li>
<li><p>For every row, define a 1-dimensional array, <code>currentRow</code>, to store the results of all the columns in the current row.</p></li>
<li><p>Calculate the values for all the columns in the current row, <code>currentRow</code> based on the values of the previous row stored in  array<code>dp</code>,</p>
<pre><code>currentRow[col] = min(dp[col - 1],
                      dp[col],
                      dp[col + 1]) + value of current (row, col) in matrix
</code></pre>
<p>Note: We must handle the edge cases, for example, if the col value is <code>0</code> or <code>n - 1</code>.</p></li>
<li><p>Once all the values of the current row are calculated, assign the values of <code>currentRow</code> to the <code>dp</code> array. So that the values in <code>dp</code> servers as the values of the previous row for the next iteration.</p>
<p>In some programming languages, this can be done by just changing the pointer reference instead of copying the values one by one.</p></li>
<li><p>The process is repeated for all the rows, and at the end, we will have the results for the cells in the first row, in the <code>dp</code> array, and we can find the minimum falling path.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/emds4kgq/shared" frameborder="0" width="100%" height="500" name="emds4kgq"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of <code>matrix</code>.</p>
<ul>
<li><p>Time Complexity: $$O(N^&#123;2&#125;)$$</p></li>
<li><p>The nested for loop takes ($$N^&#123;2&#125;$$) time.</p></li>
<li><p>Then, it takes $$N$$time to find the minimum falling path.</p></li>
<li><p>So, Time Complexity $$T(n) = O(N^&#123;2&#125;) + O(N) = O(N^&#123;2&#125;)$$</p></li>
<li><p>Space Complexity: $$O(N)$$.</p></li>
<li><p>We are using two 1-dimensional arrays <code>dp</code> and <code>currentRow</code> of size $$N$$.</p></li>
</ul>  
</div>
            