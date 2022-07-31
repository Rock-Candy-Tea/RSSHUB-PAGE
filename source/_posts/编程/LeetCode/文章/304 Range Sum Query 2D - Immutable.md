
---
title: '304. Range Sum Query 2D - Immutable'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg'
author: LeetCode
comments: false
date: Mon, 18 Jul 2022 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg'
---

<div>   
<p>Given a 2D matrix <code>matrix</code>, handle multiple queries of the following type:</p>

<ul>
<li>Calculate the <strong>sum</strong> of the elements of <code>matrix</code> inside the rectangle defined by its <strong>upper left corner</strong> <code>(row1, col1)</code> and <strong>lower right corner</strong> <code>(row2, col2)</code>.</li>
</ul>

<p>Implement the <code>NumMatrix</code> class:</p>

<ul>
<li><code>NumMatrix(int[][] matrix)</code> Initializes the object with the integer matrix <code>matrix</code>.</li>
<li><code>int sumRegion(int row1, int col1, int row2, int col2)</code> Returns the <strong>sum</strong> of the elements of <code>matrix</code> inside the rectangle defined by its <strong>upper left corner</strong> <code>(row1, col1)</code> and <strong>lower right corner</strong> <code>(row2, col2)</code>.</li>
</ul>

<p> </p>
<p><strong>Example 1:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg" style="width: 415px; height: 415px;" referrerpolicy="no-referrer">
<pre><strong>Input</strong>
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
<strong>Output</strong>
[null, 8, 11, 12]

<strong>Explanation</strong>
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>m == matrix.length</code></li>
<li><code>n == matrix[i].length</code></li>
<li><code>1 <= m, n <= 200</code></li>
<li><code>-10<sup>4</sup> <= matrix[i][j] <= 10<sup>4</sup></code></li>
<li><code>0 <= row1 <= row2 < m</code></li>
<li><code>0 <= col1 <= col2 < n</code></li>
<li>At most <code>10<sup>4</sup></code> calls will be made to <code>sumRegion</code>.</li>
</ul><p>[TOC]</p>
<h2 id="videosolution">Video Solution</h2>
<hr>
<div class="video-preview"></div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach1bruteforce">Approach 1: Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>Each time <em>sumRegion</em> is called, we use a double for loop to sum all elements from $$(row1, col1) \rightarrow (row2, col2)$$.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/iFLWkJ2C/shared" frameborder="0" width="100%" height="344" name="iFLWkJ2C"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(mn)$$ time per query.
Assume that $$m$$ and $$n$$ represents the number of rows and columns respectively, each <em>sumRegion</em> query can go through at most $$m \times n$$ elements.</p></li>
<li><p>Space complexity: $$O(1)$$. Note that <code>data</code> is a <em>reference</em> to <code>matrix</code> and is not a copy of it.</p></li>
</ul>
<hr>
<h4 id="approach2cachingmemorylimitexceeded">Approach 2: Caching [Memory Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>Since <em>sumRegion</em> could be called many times, we definitely need to do some pre-processing.</p>
<p><strong>Algorithm</strong></p>
<p>We could trade in extra space for speed by pre-calculating all possible rectangular region sum and store them in a hash table. Each <em>sumRegion</em> query now takes only constant time complexity.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(1)$$ time per query, $$O(m^2n^2)$$ time pre-computation.
Each <em>sumRegion</em> query takes $$O(1)$$ time as the hash table lookup's time complexity is constant. The pre-computation will take $$O(m^2n^2)$$ time as there are a total of $$m^2 \times n^2$$ possibilities need to be cached.</p></li>
<li><p>Space complexity: $$O(m^2n^2)$$.
Since there are $$mn$$ different possibilities for both top left and bottom right points of the rectangular region, the extra space required is $$O(m^2n^2)$$.</p></li>
</ul>
<hr>
<h4 id="approach3cachingrows">Approach 3: Caching Rows</h4>
<p><strong>Intuition</strong></p>
<p>Remember from the <a href="https://leetcode.com/problems/range-sum-query-immutable/">1D version</a> where we used a cumulative sum array? Could we apply that directly to solve this 2D version?</p>
<p><strong>Algorithm</strong></p>
<p>Try to see the 2D matrix as $$m$$ rows of 1D arrays. To find the region sum, we just accumulate the sum in the region row by row.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/kA7KjX4A/shared" frameborder="0" width="100%" height="412" name="kA7KjX4A"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(m)$$ time per query, $$O(mn)$$ time pre-computation.
The pre-computation in the constructor takes $$O(mn)$$ time. The <em>sumRegion</em> query takes $$O(m)$$ time.</p></li>
<li><p>Space complexity: $$O(mn)$$.
The algorithm uses $$O(mn)$$ space to store the cumulative sum of all rows.</p></li>
</ul>
<hr>
<h4 id="approach4cachingsmarter">Approach 4: Caching Smarter</h4>
<p><strong>Algorithm</strong></p>
<p>We used a cumulative sum array in the <a href="https://leetcode.com/problems/range-sum-query-immutable/">1D version</a>. We notice that the cumulative sum is computed with respect to the origin at index 0. Extending this analogy to the 2D case, we could pre-compute a cumulative region sum with respect to the origin at $$(0, 0)$$.</p>
<p><img src="https://leetcode.com/static/images/courses/sum_od.png" alt="Sum OD" referrerpolicy="no-referrer"><br>
<small>Sum(OD) is the cumulative region sum with respect to the origin at (0, 0).</small></p>
<p>How do we derive $$Sum(ABCD)$$ using the pre-computed cumulative region sum?</p>
<p><img src="https://leetcode.com/static/images/courses/sum_ob.png" alt="Sum OB" referrerpolicy="no-referrer"><br>
<small>Sum(OB) is the cumulative region sum on top of the rectangle.</small></p>
<p><img src="https://leetcode.com/static/images/courses/sum_oc.png" alt="Sum OC" referrerpolicy="no-referrer"><br>
<small>Sum(OC) is the cumulative region sum to the left of the rectangle.</small></p>
<p><img src="https://leetcode.com/static/images/courses/sum_oa.png" alt="Sum OA" referrerpolicy="no-referrer"><br>
<small>Sum(OA) is the cumulative region sum to the top left corner of the rectangle.</small></p>
<p>Note that the region $$Sum(OA)$$ is covered twice by both $$Sum(OB)$$ and $$Sum(OC)$$. We could use the principle of inclusion-exclusion to calculate $$Sum(ABCD)$$ as following:</p>
<p>$$
Sum(ABCD) = Sum(OD) - Sum(OB) - Sum(OC) + Sum(OA)
$$</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/CqzhufQe/shared" frameborder="0" width="100%" height="344" name="CqzhufQe"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(1)$$ time per query, $$O(mn)$$ time pre-computation.
The pre-computation in the constructor takes $$O(mn)$$ time. Each <em>sumRegion</em> query takes $$O(1)$$ time.</p></li>
<li><p>Space complexity: $$O(mn)$$.
The algorithm uses $$O(mn)$$ space to store the cumulative region sum.</p></li>
</ul>  
</div>
            