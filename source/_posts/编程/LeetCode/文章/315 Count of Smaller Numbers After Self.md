
---
title: '315. Count of Smaller Numbers After Self'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Documents/315/315_bucket1.drawio.svg'
author: LeetCode
comments: false
date: Thu, 29 Apr 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Documents/315/315_bucket1.drawio.svg'
---

<div>   
<p>You are given an integer array <code>nums</code> and you have to return a new <code>counts</code> array. The <code>counts</code> array has the property where <code>counts[i]</code> is the number of smaller elements to the right of <code>nums[i]</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [5,2,6,1]
<strong>Output:</strong> [2,1,1,0]
<strong>Explanation:</strong>
To the right of 5 there are <b>2</b> smaller elements (2 and 1).
To the right of 2 there is only <b>1</b> smaller element (1).
To the right of 6 there is <b>1</b> smaller element (1).
To the right of 1 there is <b>0</b> smaller element.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [-1]
<strong>Output:</strong> [0]
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [-1,-1]
<strong>Output:</strong> [0,0]
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
<li><code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>The problem is straightforward. For each <code>num</code> in <code>nums</code>, we need to obtain the number of smaller elements after <code>num</code>.</p>
<p>A straightforward approach is to use brute force with two for-loops. The first loop iterates over all <code>num</code> in <code>nums</code>, and the second loop iterates over all elements after <code>num</code>. However, this approach costs $$O(N^2)$$ and yields <em>Time Limit Exceed</em>, given that $$N$$ is the length of <code>nums</code>.</p>
<p>Luckily, there are two helpful data structures: <a href="https://en.wikipedia.org/wiki/Segment_tree">segment tree</a> and <a href="https://en.wikipedia.org/wiki/Fenwick_tree">binary indexed tree</a>, which are able to do the range query in logarithmic time.</p>
<p>Also, a solution based on <a href="https://en.wikipedia.org/wiki/Merge_sort">Merge Sort</a> is available.</p>
<p>Below, we will discuss each of the three approaches: <em>Segment Tree</em>, <em>Binary Indexed Tree</em>, and <em>Merge Sort</em>.</p>
<blockquote>
  <p>After you finish, you can practice by solving some similar questions:</p>
  <ul>
  <li><a href="https://leetcode.com/problems/reverse-pairs/solution/">Reverse Pairs</a></li>
  <li><a href="https://leetcode.com/problems/create-sorted-array-through-instructions/">Create Sorted Array through Instructions</a></li>
  </ul>
</blockquote>
<p><br></p>
<hr>
<h4 id="approach1segmenttree">Approach 1: Segment Tree</h4>
<p><strong>Intuition</strong></p>
<blockquote>
  <p><strong>Prerequisite: segment tree</strong></p>
  <p>If you are not familiar with segment trees, you should check out our <a href="https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/">Recursive Approach to segment trees</a> tutorial before continuing.</p>
  <p>Also, here are some relevant applications for segment trees that you can practice on:</p>
  <ul>
  <li><a href="https://leetcode.com/problems/range-sum-query-mutable/">Range Sum Query - Mutable</a></li>
  <li><a href="https://leetcode.com/problems/count-of-range-sum/">Count of Range Sum</a></li>
  </ul>
  <p>For a full list, check out the <a href="https://leetcode.com/tag/segment-tree/">segment tree Tag</a>.</p>
</blockquote>
<p>For a particular element in <code>nums</code>, located at index <code>i</code>, we want to count how many of the numbers on the right side of index <code>i</code> are smaller than <code>nums[i]</code>. Notice that the value of the smaller numbers must be in the range $$(-\infty, \text&#123;nums[i]&#125;-1]$$.</p>
<p>Hence, if we can find the count of <strong>each number</strong> in the range $$(-\infty, \text&#123;nums[i]&#125;-1]$$ on the right side of index <code>i</code>, then the answer will be the sum of those counts.</p>
<p>Therefore, for each index <code>i</code>, we need a query to find the sum of those counts. Recall that the segment tree and the binary indexed tree are two data structures that are generally helpful when solving range query problems.</p>
<p>Since we need counts of values, we can use an approach similar to <a href="https://en.wikipedia.org/wiki/Bucket_sort">bucket sort</a>, where we have buckets of values and <code>buckets[value]</code> stores the count of <code>value</code>. For each value, we increment <code>buckets[value]</code> by 1. With this approach, the number of elements smaller than <code>nums[i]</code> is the range sum of $$(-\infty, \text&#123;num&#125;-1]$$ in buckets.</p>
<p>With the help of a segment tree or binary indexed tree, we can perform the range sum query in logarithmic time.</p>
<p><img src="https://leetcode.com/articles/Documents/315/315_bucket1.drawio.svg" alt="Figure 1" referrerpolicy="no-referrer"></p>
<p><img src="https://leetcode.com/articles/Documents/315/315_bucket2.drawio.svg" alt="Figure 2" referrerpolicy="no-referrer"></p>
<p>With the given constraint <code>-10^4 <= nums[i] <= 10^4</code>, we can initialize buckets from <code>-10^4</code> to <code>10^4</code>.</p>
<p>Wait, there is a problem: Usually, we store buckets in an array, so the indices of buckets are non-negative. However, here we need to store some <strong>negative</strong> values. How can we resolve this problem?</p>
<p>There are two solutions:</p>
<ol>
<li>Use a map rather than an array.</li>
<li>Shift all numbers to non-negative.</li>
</ol>
<p>Both solutions work, and here we have chosen the second one since it is easier to implement. Interested readers are welcome to try the first one on their own.</p>
<p>To shift all numbers to non-negative, we simply add a constant. Here we chose the constant <code>offset = 10^4</code> and increase each number by <code>offset</code>:</p>
<pre><code class="python language-python">nums[i] = nums[i] + offset
</code></pre>
<p>The smallest number <code>-10^4</code> becomes <code>0</code> under this shift.</p>
<p><img src="https://leetcode.com/articles/Documents/315/315_shift.drawio.svg" alt="Figure 3" referrerpolicy="no-referrer"></p>
<p>Note that while querying a particular index, we only need to consider elements that are on the right side of the index. Therefore we need to make sure that when we query an index, say <code>i</code>, only elements from index <code>i+1</code> to the end of the array are present in the buckets.</p>
<p>To achieve this, we need to traverse <code>nums</code> from <strong>right to left</strong>, while performing range sum queries and updating the counts.</p>
<p>Similarly, with the help of a segment tree or binary indexed tree, we can perform the updates in logarithmic time.</p>
<p><img src="https://leetcode.com/articles/Documents/315/315_right_to_left.drawio.svg" alt="Figure 4" referrerpolicy="no-referrer"></p>
<p>(For convenience, the offset is not included in the above picture.)</p>
<p><strong>Algorithm</strong></p>
<ul>
<li><p>Implement the segment tree. Since the tree is initialized with all zeros, only <code>update</code> and <code>query</code> need to be implemented. Set <code>offset = 10^4</code>.</p></li>
<li><p>Iterate over each <code>num</code> in <code>nums</code> in reverse. For each <code>num</code>:</p></li>
<li><p>Shift <code>num</code> to <code>num + offset</code>.</p></li>
<li><p>Query the number of elements in the segment tree smaller than <code>num</code>.</p></li>
<li><p>Update the count of <code>num</code> in the segment tree.</p></li>
<li><p>Return the result.</p></li>
</ul>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/JkZ5ysmJ/shared" frameborder="0" width="100%" height="500" name="JkZ5ysmJ"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of <code>nums</code> and $$M$$ be the difference between the maximum and minimum values in <code>nums</code>.</p>
<p>Note that for convenience, we fix $$M=2*10^4$$ in the above implementations.</p>
<ul>
<li><p>Time Complexity: $$O(N\log(M))$$.<br>
We need to iterate over <code>nums</code>. For each element, we spend $$O(\log(M))$$ to find the number of smaller elements after it, and spend $$O(\log(M))$$ time to update the counts. In total, we need $$O(N \cdot \log(M)) = O(N\log(M))$$ time.</p></li>
<li><p>Space Complexity: $$O(M)$$, since we need, at most, an array of size $$2M+2$$ to store the segment tree.<br>
We need at most $$M+1$$ buckets, where the extra $$1$$ is for the value $$0$$. For the segment tree, we need twice the number of buckets, which is $$(M+1)\times 2 = 2M+2$$.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2binaryindexedtreefenwicktree">Approach 2: Binary Indexed Tree (Fenwick Tree)</h4>
<p><strong>Intuition</strong></p>
<blockquote>
  <p><strong>Prerequisite: binary indexed tree</strong></p>
  <p>If you are not familiar with binary indexed tree (BIT), you should check relevant tutorials, such as <a href="https://leetcode.com/problems/range-sum-query-2d-mutable/solution/">Range Sum Query 2D - Mutable</a> before continuing.</p>
  <p>Also, here are some relevant applications for binary indexed trees that you can practice on:</p>
  <ul>
  <li><a href="https://leetcode.com/problems/range-sum-query-mutable/">Range Sum Query - Mutable</a></li>
  <li><a href="https://leetcode.com/problems/count-of-range-sum/">Count of Range Sum</a></li>
  </ul>
  <p>(Yes, many problems which can be solved by segment tree can also be solved by binary indexed tree.)</p>
  <p>For a full list, you can check the <a href="https://leetcode.com/tag/binary-indexed-tree/">binary indexed tree Tag</a>.</p>
</blockquote>
<p>Binary indexed tree is similar to segment tree. It allows us to perform a prefix query, such as prefix sum, in $$\log$$ time. Can we transform this problem into a <strong>prefix sum</strong> problem?</p>
<p>Yes, using the same tricks that we used in approach 1, buckets and shift, we can transform the number of smaller elements into a prefix sum for the range $$[0, \text&#123;num&#125;+\text&#123;offset&#125;-1]$$, where $$\text&#123;offset&#125;=10^4$$.</p>
<p><img src="https://leetcode.com/articles/Documents/315/315_bit.drawio.svg" alt="Figure 5" referrerpolicy="no-referrer"></p>
<p>Similarly, when querying, we need to traverse <code>nums</code> from right to left in order to ensure that only the elements to the right are in the buckets.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li><p>Implement the binary indexed tree. Since the tree is initialized with all zeros, only <code>update</code> and <code>query</code> need to be implemented. Set <code>offset = 10^4</code>.</p></li>
<li><p>Iterate over each <code>num</code> in <code>nums</code> in reverse. For each <code>num</code>:</p></li>
<li><p>Shift <code>num</code> to <code>num + offset</code>.</p></li>
<li><p>Query the number of elements in the BIT that are smaller than <code>num</code>.</p></li>
<li><p>Update the count of <code>num</code> in the BIT.</p></li>
<li><p>Return the result.</p></li>
</ul>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/NSkvX6EL/shared" frameborder="0" width="100%" height="500" name="NSkvX6EL"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of <code>nums</code> and $$M$$ be the difference between the maximum and minimum values in <code>nums</code>.</p>
<p>Note that for convenience, we fix $$M=2*10^4$$ in the above implementations.</p>
<ul>
<li><p>Time Complexity: $$O(N\log(M))$$.<br>
We need to iterate over <code>nums</code>. For each element, we spend $$O(\log(M))$$ to find the number of smaller elements after it, and spend $$O(\log(M))$$ time to update the counts. In total, we need $$O(N \cdot \log(M)) = O(N\log(M))$$ time.</p></li>
<li><p>Space Complexity: $$O(M)$$, since we need, at most, an array of size $$M+2$$ to store the BIT.<br>
We need at most $$M+1$$ buckets, where the extra $$1$$ is for the value $$0$$. The BIT requires an extra dummy node, so the size is $$(M+1)+1 = M+2$$.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3mergesort">Approach 3: Merge Sort</h4>
<p><strong>Intuition</strong></p>
<blockquote>
  <p><strong>Prerequisite: Merge Sort</strong></p>
  <p>If you are not familiar with Merge Sort, you should check relevant tutorials before continuing.</p>
  <p>Also, here is a basic application of Merge Sort that you can practice on:</p>
  <ul>
  <li><a href="https://leetcode.com/problems/sort-an-array/">Sort an Array</a></li>
  </ul>
</blockquote>
<p>To apply merge sort, one key observation is that:</p>
<blockquote>
  <p>The smaller elements on the right of a number will <strong>jump from its right to its left</strong> during the sorting process.</p>
</blockquote>
<p><img src="https://leetcode.com/articles/Documents/315/315_jumping.drawio.svg" alt="Figure 6" referrerpolicy="no-referrer"></p>
<p>If we can record the numbers of those elements during sorting, then the problem is solved.</p>
<p>Can we modify the merge sort a little to meet our needs?</p>
<p>Consider when merging two sorted list</p>
<p><img src="https://leetcode.com/articles/Documents/315/315_merging.drawio.svg" alt="Figure 7" referrerpolicy="no-referrer"></p>
<p>Yes! When we select an element <code>i</code> on the left array, we know that elements selected previously from the right array <strong>jump</strong> from <code>i</code>'s right to <code>i</code>'s left.</p>
<p>By adding the counts of those elements in every merge step, we get the total number of elements that jumped from <code>i</code>'s right to <code>i</code>'s left.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li><p>Implement a merge sort function.</p></li>
<li><p>For each element <code>i</code>, the function records the number of elements jumping from <code>i</code>'s right to <code>i</code>'s left during the merge sort.</p></li>
<li><p>Merge sort <code>nums</code>, store the number of elements jumping from right to left in <code>result</code>.</p></li>
<li><p>Alternatively, one can sort the <em>indices</em> with corresponding values in <code>nums</code>. That is to say, we are going to sort list <code>[0, 1, ..., n-1]</code> according to the comparator <code>nums[i]</code>. This helps to track the indices and update <code>result</code>. You can find additional details in the implementations below.</p></li>
<li><p>Return <code>result</code>.</p></li>
</ul>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/deoB8KuH/shared" frameborder="0" width="100%" height="500" name="deoB8KuH"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of <code>nums</code>.</p>
<ul>
<li><p>Time Complexity: $$O(N\log(N))$$. We need to perform a merge sort which takes $$O(N\log(N))$$ time. All other operations take at most $$O(N)$$ time.</p></li>
<li><p>Space Complexity: $$O(N)$$, since we need a constant number of arrays of size $$O(N)$$.</p></li>
</ul>
<p><br></p>  
</div>
            