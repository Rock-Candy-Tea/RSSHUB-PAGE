
---
title: '300. Longest Increasing Subsequence'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=7212'
author: LeetCode
comments: false
date: Fri, 18 Jun 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7212'
---

<div>   
<p>Given an integer array <code>nums</code>, return the length of the longest strictly increasing subsequence.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, <code>[3,6,2,7]</code> is a subsequence of the array <code>[0,3,1,6,2,2,7]</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [10,9,2,5,3,7,101,18]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,0,3,2,3]
<strong>Output:</strong> 4
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [7,7,7,7,7,7,7]
<strong>Output:</strong> 1
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= nums.length <= 2500</code></li>
<li><code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code></li>
</ul>

<p> </p>
<p><b>Follow up:</b> Can you come up with an algorithm that runs in <code>O(n log(n))</code> time complexity?</p><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach1dynamicprogramming">Approach 1: Dynamic Programming</h4>
<p><strong>Realizing a Dynamic Programming Problem</strong></p>
<p>This problem has two important attributes that let us know it should be solved by dynamic programming. First, the question is asking for the maximum or minimum of something. Second, we have to make decisions that may depend on previously made decisions, which is very typical of a problem involving subsequences.</p>
<p>As we go through the input, each "decision" we must make is simple: is it worth it to consider this number? If we use a number, it may contribute towards an increasing subsequence, but it may also eliminate larger elements that came before it. For example, let's say we have <code>nums = [5, 6, 7, 8, 1, 2, 3]</code>. It isn't worth using the 1, 2, or 3, since using any of them would eliminate 5, 6, 7, and 8, which form the longest increasing subsequence. We can use dynamic programming to determine whether an element is worth using or not.</p>
<p><strong>A Framework to Solve Dynamic Programming Problems</strong></p>
<p>Typically, dynamic programming problems can be solved with three main components. If you're new to dynamic programming, this might be hard to understand but is extremely valuable to learn since <strong>most dynamic programming problems can be solved this way</strong>. </p>
<p>First, we need some function or array that represents the answer to the problem from a given state. For many solutions on LeetCode, you will see this function/array named "dp". For this problem, let's say that we have an array <code>dp</code>. As just stated, this array needs to represent <strong>the answer to the problem for a given state</strong>, so let's say that <code>dp[i]</code> represents the length of the <strong>longest increasing subsequence</strong> that <strong>ends with the $$i^&#123;th&#125;$$ element</strong>. The "state" is one-dimensional since it can be represented with only one variable - the index <code>i</code>.</p>
<p>Second, we need a way to transition between states, such as <code>dp[5]</code> and <code>dp[7]</code>. This is called a <strong>recurrence relation</strong> and can sometimes be tricky to figure out. Let's say we know <code>dp[0]</code>, <code>dp[1]</code>, and <code>dp[2]</code>. How can we find <code>dp[3]</code> given this information? Well, since <code>dp[2]</code> represents the length of the longest increasing subsequence that ends with <code>nums[2]</code>, if <code>nums[3] > nums[2]</code>, then we can simply take the subsequence ending at <code>i = 2</code> and append <code>nums[3]</code> to it, increasing the length by 1. The same can be said for <code>nums[0]</code> and <code>nums[1]</code> if <code>nums[3]</code> is larger. Of course, we should try to maximize <code>dp[3]</code>, so we need to check all 3. Formally, the recurrence relation is: <code>dp[i] = max(dp[j] + 1) for all j where nums[j] < nums[i] and j < i</code>.</p>
<p>The third component is the simplest: we need a base case. For this problem, we can initialize every element of <code>dp</code> to <code>1</code>, since every element on its own is technically an increasing subsequence.</p>
<p>!?!../Documents/300_LIS.json:960,540!?!</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize an array <code>dp</code> with length <code>nums.length</code> and all elements equal to 1. <code>dp[i]</code> represents the length of the longest increasing subsequence that ends with the element at index <code>i</code>.</p></li>
<li><p>Iterate from <code>i = 1</code> to <code>i = nums.length - 1</code>. At each iteration, use a second for loop to iterate from <code>j = 0</code> to <code>j = i - 1</code> (all the elements before i). For each element before <code>i</code>, check if that element is smaller than <code>nums[i]</code>. If so, set <code>dp[i] = max(dp[i], dp[j] + 1)</code>.</p></li>
<li><p>Return the max value from <code>dp</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/EGqZzdye/shared" frameborder="0" width="100%" height="412" name="EGqZzdye"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the length of <code>nums</code>,</p>
<ul>
<li><p>Time complexity: $$O(N^2)$$</p>
<p>We use two nested for loops resulting in $$1 + 2 + 3 + 4 + … + N = \dfrac &#123;N * (N + 1)&#125;&#123;2&#125;$$ operations, resulting in a time complexity of $$O(N^2)$$. </p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>The only extra space we use relative to input size is the <code>dp</code> array, which is the same length as <code>nums</code>.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2intelligentlybuildasubsequence">Approach 2: Intelligently Build a Subsequence</h4>
<p><strong>Intuition</strong></p>
<p>As stated in the previous approach, the difficult part of this problem is deciding if an element is worth using or not. Consider the example <code>nums = [8, 1, 6, 2, 3, 10]</code>. Let's try to build an increasing subsequence starting with an empty one: <code>sub = []</code>. </p>
<ul>
<li><p>At the first element <code>8</code>, we might as well take it since it's better than nothing, so <code>sub = [8]</code>. </p></li>
<li><p>At the second element <code>1</code>, we can't increase the length of the subsequence since <code>8 >= 1</code>, so we have to choose only one element to keep. Well, this is an easy decision, let's take the <code>1</code> since there may be elements later on that are greater than <code>1</code> but less than <code>8</code>, now we have <code>sub = [1]</code>. </p></li>
<li><p>At the third element <code>6</code>, we can build on our subsequence since <code>6 > 1</code>, now <code>sub = [1, 6]</code>.</p></li>
<li><p>At the fourth element <code>2</code>, we can't build on our subsequence since <code>6 >= 2</code>, but can we improve on it for the future? Well, similar to the decision we made at the second element, if we replace the <code>6</code> with <code>2</code>, we will open the door to using elements that are greater than <code>2</code> but less than <code>6</code> in the future, so <code>sub = [1, 2]</code>.</p></li>
<li><p>At the fifth element <code>3</code>, we can build on our subsequence since <code>3 > 2</code>. Notice that this was only possible because of the swap we made in the previous step, so <code>sub = [1, 2, 3]</code>.</p></li>
<li><p>At the last element <code>10</code>, we can build on our subsequence since <code>10 > 3</code>, giving a final subsequence <code>sub = [1, 2, 3, 10]</code>. The length of <code>sub</code> is our answer.</p></li>
</ul>
<p>It appears the best way to build an increasing subsequence is: for each element <code>num</code>, if <code>num</code> is greater than the largest element in our subsequence, then add it to the subsequence. Otherwise, perform a linear scan through the subsequence starting from the smallest element and replace the first element that is greater than <code>num</code> with <code>num</code>.  This opens the door for elements that are greater than <code>num</code> but less than the element replaced to be included in the sequence. </p>
<p>One thing to add: this algorithm does not always generate a valid subsequence of the input, but the length of the subsequence will always equal the length of the longest increasing subsequence. For example, with the input <code>[3, 4, 5, 1]</code>, at the end we will have <code>sub = [1, 4, 5]</code>, which isn't a subsequence, but the length is still correct. The length remains correct because the length only changes when a new element is larger than any element in the subsequence. In that case, the element is appended to the subsequence instead of replacing an existing element.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize an array <code>sub</code> which contains the first element of <code>nums</code>.</p></li>
<li><p>Iterate through the input, starting from the second element. For each element <code>num</code>:</p>
<ul>
<li>If <code>num</code> is greater than any element in <code>sub</code>, then add <code>num</code> to <code>sub</code>.</li>
<li>Otherwise, iterate through <code>sub</code> and find the first element that is greater than <code>num</code>. Replace that element with <code>num</code>.</li></ul></li>
<li><p>Return the length of <code>sub</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/kpYbANnB/shared" frameborder="0" width="100%" height="446" name="kpYbANnB"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the length of <code>nums</code>,</p>
<ul>
<li><p>Time complexity: $$O(N^2)$$</p>
<p>The worst case is when the input is strictly increasing. In this case, the algorithm will have the same number of operations as the first approach. However, in the average and best case, the number of operations will be significantly less. </p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>When the input is strictly increasing, the <code>sub</code> array will be the same size as the input.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3improvewithbinarysearch">Approach 3: Improve With Binary Search</h4>
<p><strong>Intuition</strong></p>
<p>In the previous approach, when we have an element <code>num</code> that is not greater than all the elements in <code>sub</code>, we perform a linear scan to find the first element in <code>sub</code> that is greater than <code>num</code>. Since <code>sub</code> is in sorted order, we can use binary search instead to greatly improve the efficiency of our algorithm.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize an array <code>sub</code> which contains the first element of <code>nums</code>.</p></li>
<li><p>Iterate through the input, starting from the second element. For each element <code>num</code>:</p>
<ul>
<li>If <code>num</code> is greater than any element in <code>sub</code>, then add <code>num</code> to <code>sub</code>.</li>
<li>Otherwise, perform a binary search in <code>sub</code> to find the smallest element that is greater than <code>num</code>. Replace that element with <code>num</code>.</li></ul></li>
<li><p>Return the length of <code>sub</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<p>In Python, the <a href="https://docs.python.org/3/library/bisect.html">bisect</a> module provides super handy functions that does binary search for us.</p>
<iframe src="https://leetcode.com/playground/kDf5xMVL/shared" frameborder="0" width="100%" height="500" name="kDf5xMVL"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the length of <code>nums</code>,</p>
<ul>
<li><p>Time complexity: $$O(N \cdot \log(N))$$</p>
<p>Binary search uses $$\log(N)$$ time as opposed to the $$O(N)$$ time of a linear scan, which improves our time complexity from $$O(N^2)$$ to $$O(N \cdot \log(N))$$.</p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>When the input is strictly increasing, the <code>sub</code> array will be the same size as the input.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            