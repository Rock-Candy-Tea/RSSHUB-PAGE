
---
title: '363. Max Sum of Rectangle No Larger Than K'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2021/03/18/sum-grid.jpg'
author: LeetCode
comments: false
date: Sat, 22 May 2021 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2021/03/18/sum-grid.jpg'
---

<div>   
<p>Given an <code>m x n</code> matrix <code>matrix</code> and an integer <code>k</code>, return <em>the max sum of a rectangle in the matrix such that its sum is no larger than</em> <code>k</code>.</p>

<p>It is <strong>guaranteed</strong> that there will be a rectangle with a sum no larger than <code>k</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2021/03/18/sum-grid.jpg" style="width: 255px; height: 176px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> matrix = [[1,0,1],[0,-2,3]], k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> matrix = [[2,2,-1]], k = 3
<strong>Output:</strong> 3
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>m == matrix.length</code></li>
<li><code>n == matrix[i].length</code></li>
<li><code>1 <= m, n <= 100</code></li>
<li><code>-100 <= matrix[i][j] <= 100</code></li>
<li><code>-10<sup>5</sup> <= k <= 10<sup>5</sup></code></li>
</ul>

<p> </p>
<p><strong>Follow up:</strong> What if the number of rows is much larger than the number of columns?</p><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>The first thing one might think of is a brute force solution. Since the numbers may be negative, there is no clever way to know if we should add more cells to get the best solution or not, hence we would need to enumerate all possible rectangles and get the best result. One might add a <a href="https://leetcode.com/problems/range-sum-query-2d-immutable/solution/">prefix sum for a 2D array</a> to get the sum of a rectangle in $$O(1)$$, however this still has a time complexity of $$O(m^2n^2)$$ due to enumeration of all rectangles. Thus a brute force solution with prefix sums won't suffice and we need to figure out a more clever way to approach this.</p>
<h4 id="approach1prefixsumon1darrayusingsortedcontainer">Approach 1: Prefix Sum on 1D Array using Sorted Container</h4>
<p><strong>Intuition</strong></p>
<p>To understand this approach let's first try to simplify the question and instead of a matrix let's find the maximum sum of a sub-array for a 1D array with <code>sum <= k</code>.
How can we achieve this? Let's use the concept of prefix sums, at every index <code>i</code> we want to find the maximum possible sum of sub-array which ends at <code>i</code>.</p>
<p>Let's also understand what a sorted container is, which is used below. A sorted container maintains an order specified by the comparison function at all times and all operations on a sorted containers are of $$O(\log n)$$. Some examples are, <a href="http://www.cplusplus.com/reference/set/set/">set</a> in c++, <a href="https://docs.oracle.com/javase/8/docs/api/java/util/SortedSet.html">SortedSet</a> in Java and <a href="http://www.grantjenks.com/docs/sortedcontainers/sortedset.html">SortedSet</a> in python.</p>
<p>At every index <code>i</code> we store the prefix sums in a sorted container, now let's say at index <code>i</code> current sum from <code>0..i-1</code> is <code>S</code>, to find the maximum possible <code>sum <= k</code> we would want to find if there is a possible sub-array with sum <code>k</code> that ends at <code>i</code>, and if not then try to find a sub-array with possible sum <code>k-1</code> and so on.</p>
<p>Now to find a sub-array with sum <code>k</code> we have the equation $$\text&#123;S&#125; - \text&#123;X&#125; = \text&#123;k&#125;$$, where we know <code>S</code> and we know <code>k</code> and <code>X</code> is some sub-array sum that when subtracted from <code>S</code> gives us <code>k</code> which means the sum of sub-array from the occurrence of sum <code>X</code> to the occurrence of sum <code>S</code> is <code>k</code>. Since we know the values of the two variable we can rearrange the equation to find <code>X</code> as $$\text&#123;S&#125; - \text&#123;k&#125; = \text&#123;X&#125;$$. However, this only tells us if the sub-array with the sum exactly equal to <code>k</code> exists. What about the sub-array with sum $$\text&#123;k&#125;-1..\text&#123;k&#125;-2$$ and so on?</p>
<p><img src="https://leetcode.com/articles/Figures/363/QueryOnSorted.png" alt="diff" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1.</em>
&#123;:align="center"&#125;</p>
<p>Remember that we are storing the prefix sums in a sorted manner, which means that instead of searching for <code>X</code> we can search for the closest prefix sum that is <code>>= X</code> in $$\log n$$ using binary search. This will always give us the minimum possible value <code>>= X</code> so that the sub-array sum is as close to <code>k</code>, if $$\text&#123;S&#125; - \text&#123;X&#125; = \text&#123;k&#125;$$ then $$\text&#123;S&#125; - (\text&#123;X&#125;+1) = \text&#123;k&#125;-1$$ and so on.</p>
<p>The following visualization will help you understand how to get the result for a 1D array.</p>
<p>!?!../Documents/363/1D.json:1000,500!?!
&#123;:align="center"&#125;</p>
<p><em>Visualization 1. Finding Max Sub-array <code>sum <= k</code> for 1D Array</em>
&#123;:align="center"&#125;</p>
<p><br></p>
<p>Understanding the previous section is the hard part, now all we need to do is extend the procedure to work for a 2D array. This can be accomplished by converting each 2D matrix to a 1D array and then running the previous algorithm.  Each time the algorithm is run, we update the global maximum result.</p>
<p>How do we do this? Imagine we have a $$3 \text&#123;x&#125; 5$$ matrix. We will start by finding the maximum result for all $$1 \text&#123;x&#125; 5$$ arrays (each row of the matrix).  Next, we want to find the maximum possible result for all rectangles of height 2.   So, we first convert each $$2 \text&#123;x&#125; 5$$ sub-matrix into a $$1 \text&#123;x&#125; 5$$ array by summing each column, then we run the algorithm, and update the global maximum result. Finally, we will repeat this process for the entire $$3 \text&#123;x&#125; 5$$ matrix.</p>
<p>The picture below depicts how a $$2 \text&#123;x&#125; 3$$ matrix can be converted to a $$1 \text&#123;x&#125; 3$$ 1D array.</p>
<p><img src="https://leetcode.com/articles/Figures/363/1DRep.png" alt="diff" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 2. Converting a 2D matrix to 1D Sum Array</em>
&#123;:align="center"&#125;</p>
<p>Now let's combine the two algorithms to get the required result for a matrix.</p>
<p>!?!../Documents/363/2D.json:1000,500!?!
&#123;:align="center"&#125;</p>
<p><em>Visualization 2. Finding Max <code>sum <= K</code> of a rectangle for a Matrix</em>
&#123;:align="center"&#125;</p>
<p><br></p>
<p><strong>Algorithm</strong></p>
<style type="text/css">
    ol ol &#123; list-style-type: lower-alpha; &#125;
</style>
<ol>
<li>Let's define a function that gets us the result of the maximum possible sum of a sub-array with <code>sum <= k</code> for a given 1D array.</li>
<li>Let's initialize a variable for running sum with <code>0</code>. Let's call it <code>sum</code>.</li>
<li>Initialize a sorted container to store prefix sums and add <code>0</code> to it.</li>
<li>Iterate each number in the 1D array.</li>
<li>Add current number to the running sum.</li>
<li>Find the closest value of <code>sum - k</code> greater than or equal to <code>sum - k</code> in the sorted prefix sums using binary search. Let's call it <code>X</code>.</li>
<li>If such a number is found store the maximum value of <code>sum - X</code> until now in a global variable.</li>
<li>Add the current running sum in the container for prefix sums.</li>
<li>Repeat steps d to g for all numbers in the 1D array.</li>
<li>Initialize an array with length equal to the number of columns in the matrix. This will store 1D representation of the matrix, let's call it <code>rowSum</code>.</li>
<li>Run a loop from <code>0</code> to rows in the matrix. This represents the starting row of the matrix that we are aiming to find a result for.</li>
<li>At the beginning of this loop fill <code>rowSum</code> with <code>0</code>.</li>
<li>Run a nested loop that would again run from <code>0</code> to number of rows in the matrix. This represents the ending row of the matrix that we are aiming to find the result for.</li>
<li>Perform a column-wise sum of the ending row with the 1D representation <code>rowSum</code>. This will be the 1D representation of the matrix between <code>i..j</code>.</li>
<li>Run the algorithm to find the maximum possible sum of sub-array with <code>sum <= k</code> for this row.</li>
<li>We repeat the steps 3 to 7 for all combinations of <code>i</code> and <code>j</code> where $$\text&#123;i&#125; \le \text&#123;j&#125;$$.</li>
</ol>
<iframe src="https://leetcode.com/playground/gQb3pDii/shared" frameborder="0" width="100%" height="500" name="gQb3pDii"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$m$$ be the number of rows and $$n$$ be the number of columns.</p>
<ul>
<li><p>Time complexity: $$O(m^2n\log n)$$. We iterate over each <code>i</code> and <code>j</code> where $$0 \le i \le j <m$$, within this we iterate over each <code>i</code> where $$0 \le i<n$$ and perform a binary search on the same number of elements.</p></li>
<li><p>Space complexity: $$O(n)$$. We create a separate array of size <code>n</code> representing the 2D matrix and also store prefix sums for all indices.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2followuplargernumberofrowsthancolumns">Approach 2: Follow-up - Larger Number of Rows than Columns</h4>
<p><strong>Intuition</strong></p>
<p>The follow-up question asks if the number of rows is significantly larger, can we improve upon our solution? The answer is Yes!</p>
<p>You will notice that in the previous approach we take the most time $$O(m^2)$$ to iterate over each consecutive combination of rows and convert them to 1D array. It is obvious that if the number of rows increases the time will significantly increase as well. To get around this one may notice that there is no specific reason in the previous approach to perform a row-wise combination and converting them to a 1D array of size <code>n</code>, we can perform a column-wise combination and convert them to 1D array of size <code>m</code> and it would give us the same result.</p>
<p>Thus we can switch between the two based on the size of rows and columns. Let's try this approach.</p>
<p>We can also simply transpose the matrix when <code>m > n</code> and then solve it using approach 1.</p>
<p><strong>Algorithm</strong></p>
<p>We use the same idea as the previous approach but create the 1D vector column-wise if the number of rows is greater than the number of columns or do it row-wise otherwise, same as the previous approach. We can also reuse the function that gets the result for 1D vector.</p>
<iframe src="https://leetcode.com/playground/hCjxwTCp/shared" frameborder="0" width="100%" height="500" name="hCjxwTCp"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$m$$ be the number of rows and $$n$$ be the number of columns.</p>
<ul>
<li><p>Time complexity: $$O(\min(m,n)^2\max(m,n)\log \max(m,n))$$. Using the same thought process as approach 1.</p></li>
<li><p>Space complexity: $$O(\max(m, n))$$. Using the same thought process as approach 1.</p></li>
</ul>
<hr>
<h4 id="approach3combiningitwithkadanesalgorithm">Approach 3: Combining it with Kadane's Algorithm</h4>
<p><strong>Intuition</strong></p>
<p><a href="https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm">Kadane's algorithm</a> gets the max possible sum of a sub-array in $$O(n)$$ time. <a href="https://leetcode.com/problems/maximum-subarray/solution/">This</a> LeetCode article explains the algorithm beautifully.
Let's understand how this algorithm can be used to our advantage for this problem.</p>
<p>For each 1D array that we try to find the result for, we can first run Kadane's algorithm on it and get the maximum possible sum of any sub-array with it. If this result is <code><= k</code> we can simply skip running our initial $$O(n\log n)$$ algorithm as we already have the maximum possible result the 1D array can give. This will help us in significantly reducing the runtime of the algorithm as 1D arrays with max sub-array <code>sum <= k</code> would take $$O(n)$$ time only.</p>
<p><strong>Algorithm</strong></p>
<p>We use the same idea as the previous approach but add an extra Kadane's algorithm in <code>updateResult</code> function before running the algorithm mentioned in previous approaches, if its result is <code><= k</code> we skip running the previous algorithm and return the same result, else we do the same thing as the previous approach.</p>
<iframe src="https://leetcode.com/playground/YWEev7HZ/shared" frameborder="0" width="100%" height="500" name="YWEev7HZ"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$m$$ be the number of rows and $$n$$ be the number of columns.</p>
<ul>
<li><p>Time complexity: $$O(\min(m,n)^2\max(m,n)\log \max(m,n))$$. Using the same thought process as approach 1 as in the worst case we end up running the algorithm from approach 1 for all 1D arrays.</p></li>
<li><p>Space complexity: $$O(\max(m, n))$$. Using the same thought process as approach 1.</p></li>
</ul>
<p><br></p>  
</div>
            