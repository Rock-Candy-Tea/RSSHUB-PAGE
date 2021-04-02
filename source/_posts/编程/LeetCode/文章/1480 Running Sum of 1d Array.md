
---
title: '1480. Running Sum of 1d Array'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=7094'
author: LeetCode
comments: false
date: Wed, 31 Mar 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7094'
---

<div>   
<p>Given an array <code>nums</code>. We define a running sum of an array as <code>runningSum[i] = sum(nums[0]…nums[i])</code>.</p>

<p>Return the running sum of <code>nums</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [1,3,6,10]
<strong>Explanation:</strong> Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,1,1,1]
<strong>Output:</strong> [1,2,3,4,5]
<strong>Explanation:</strong> Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [3,1,2,10,1]
<strong>Output:</strong> [3,4,6,16,17]
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= nums.length <= 1000</code></li>
<li><code>-10^6 <= nums[i] <= 10^6</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach1usingseparatespace">Approach 1: Using Separate Space</h4>
<p><strong>Intuition</strong></p>
<p>We are required to find the running sum of numbers <code>nums[i]</code> in the input array where <code>i</code> ranges from <code>0</code> to <code>n-1</code> and <code>n</code> is the size of the input array. We can see that the running sum is the sum of all of the elements from index <code>0</code> to index <code>i</code> inclusive. Since we start building our output array at index <code>0</code>, at each index <code>i</code> we have already calculated the sum of all numbers up to and including index <code>i-1</code>. Thus, instead of recalculating the sum, we can get the result for index <code>i</code> by simply adding the element at index <code>i</code> to the previously calculated running sum for index <code>i-1</code>.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Define an array <code>result</code>.</li>
<li>Initialize the first element of <code>result</code> with the first element of the input array.</li>
<li>At index <code>i</code> append the sum of the element <code>nums[i]</code> and previous running sum <code>result[i - 1]</code> to the <code>result</code> array.</li>
<li>We repeat step 3 for all indices from <code>1</code> to <code>n-1</code>.</li>
</ol>
<iframe src="https://leetcode.com/playground/HmpnCZtd/shared" frameborder="0" width="100%" height="276" name="HmpnCZtd"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(n)$$ where $$n$$ is the length of the input array. This is because we use a single loop that iterates over the entire array to calculate the running sum.</p></li>
<li><p>Space complexity: $$O(1)$$ since we don't use any additional space to find the running sum. <em>Note</em> that we do not take into consideration the space occupied by the output array.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2usinginputarrayforoutput">Approach 2: Using Input Array for Output</h4>
<p><strong>Intuition</strong></p>
<p>In the previous approach we created an extra array to store our results. However, we do not actually need to do so. We can obtain the same result without using extra space by performing the same operations on the input array instead.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Increase <code>nums[i]</code> by the previous index's running sum.  The previous index's running sum is stored at index <code>i-1</code> in the input array.</li>
<li>We repeat step 1 for all indices from <code>1</code> to <code>n-1</code>.</li>
</ol>
<iframe src="https://leetcode.com/playground/8p9N4E2a/shared" frameborder="0" width="100%" height="225" name="8p9N4E2a"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(n)$$ where $$n$$ is the length of input array.</p></li>
<li><p>Space complexity: $$O(1)$$ since we don't use any additional space to find the running sum. <em>Note</em> that we do not take into consideration the space occupied by the output array.</p></li>
</ul>
<p><br></p>  
</div>
            