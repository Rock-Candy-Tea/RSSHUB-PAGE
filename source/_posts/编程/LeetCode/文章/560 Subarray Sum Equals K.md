
---
title: '560. Subarray Sum Equals K'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=6820'
author: LeetCode
comments: false
date: Fri, 08 Apr 2022 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6820'
---

<div>   
<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the total number of subarrays whose sum equals to</em> <code>k</code>.</p>

<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1], k = 2
<strong>Output:</strong> 2
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3], k = 3
<strong>Output:</strong> 2
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= nums.length <= 2 * 10<sup>4</sup></code></li>
<li><code>-1000 <= nums[i] <= 1000</code></li>
<li><code>-10<sup>7</sup> <= k <= 10<sup>7</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="videosolution">Video Solution</h2>
<hr>
<div class="video-preview"></div>
<div> 
</div>
<h2 id="solutionarticle">Solution Article</h2>
<hr>
<h4 id="approach1bruteforce">Approach 1: Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>The simplest method is to consider every possible subarray of the given $$nums$$ array, find the sum of the elements of each of those subarrays and check for the equality of the sum obtained with the given $$k$$. Whenever the sum equals $$k$$, we can increment the $$count$$ used to store the required result.</p>
<iframe src="https://leetcode.com/playground/uzdLhWrz/shared" frameborder="0" name="uzdLhWrz" width="100%" height="309"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity : $$O(n^3)$$. Considering every possible subarray takes $$O(n^2)$$ time. For each of the subarray we calculate the sum taking $$O(n)$$ time in the worst case, taking a total of $$O(n^3)$$ time.</p></li>
<li><p>Space complexity : $$O(1)$$. Constant space is used.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2usingcumulativesum">Approach 2: Using Cumulative Sum</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of determining the sum of elements every time for every new subarray considered, we can make use of a cumulative sum array , $$sum$$. Then, in order to calculate the sum of elements lying between two indices, we can subtract the cumulative sum corresponding to the two indices to obtain the sum directly, instead of iterating over the subarray to obtain the sum.</p>
<p>In this implementation, we make use of a cumulative sum array, $$sum$$, such that $$sum[i]$$ is used to store the cumulative sum of $$nums$$ array up to the element corresponding to the $$(i-1)^&#123;th&#125;$$ index. Thus, to determine the sum of elements for the subarray $$nums[i:j]$$, we can directly use $$sum[j+1] - sum[i]$$.</p>
<iframe src="https://leetcode.com/playground/YnknRnC6/shared" frameborder="0" name="YnknRnC6" width="100%" height="326"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity : $$O(n^2)$$. Considering every possible subarray takes $$O(n^2)$$ time. Finding out the sum of any subarray takes $$O(1)$$ time after the initial processing of $$O(n)$$ for creating the cumulative sum array.</p></li>
<li><p>Space complexity : $$O(n)$$. Cumulative sum array $$sum$$ of size $$n+1$$ is used.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3withoutspace">Approach 3: Without Space</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of considering all the $$start$$ and $$end$$ points and then finding the sum for each subarray corresponding to those points, we can directly find the sum on the go while considering different $$end$$ points. i.e. We can choose a particular $$start$$ point and while iterating over the $$end$$ points, we can add the element corresponding to the $$end$$ point to the sum formed till now. Whenever the $$sum$$ equals the required $$k$$ value, we can update the $$count$$ value. We do so while iterating over all the $$end$$ indices possible for every $$start$$ index. Whenever, we update the $$start$$ index, we need to reset the $$sum$$ value to 0.</p>
<iframe src="https://leetcode.com/playground/MGuUEEUy/shared" frameborder="0" name="MGuUEEUy" width="100%" height="292"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity : $$O(n^2)$$. We need to consider every subarray possible.</p></li>
<li><p>Space complexity : $$O(1)$$. Constant space is used.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach4usinghashmap">Approach 4: Using Hashmap</h4>
<p><strong>Algorithm</strong></p>
<p>The idea behind this approach is as follows: If the cumulative sum(represented by $$sum[i]$$ for sum up to $$i^&#123;th&#125;$$ index) up to two indices is the same, the sum of the elements lying in between those indices is zero. Extending the same thought further, if the cumulative sum up to two indices, say $$i$$ and $$j$$ is at a difference of $$k$$ i.e. if $$sum[i] - sum[j] = k$$, the sum of elements lying between indices $$i$$ and $$j$$ is $$k$$.</p>
<p>Based on these thoughts, we make use of a hashmap $$map$$ which is used to store the cumulative sum up to all the indices possible along with the number of times the same sum occurs. We store the data in the form: $$(sum<em>i, no. of occurrences of sum</em>i)$$. We traverse over the array $$nums$$ and keep on finding the cumulative sum. Every time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum. If the same sum occurs again, we increment the count corresponding to that sum in the hashmap. Further, for every sum encountered, we also determine the number of times the sum $$sum-k$$ has occurred already, since it will determine the number of times a subarray with sum $$k$$ has occurred up to the current index. We increment the $$count$$ by the same amount. </p>
<p>After the complete array has been traversed, the $$count$$ gives the required result.</p>
<p>The animation below depicts the process.</p>
<p>!?!../Documents/560_Subarray.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/S6xciAtN/shared" frameborder="0" name="S6xciAtN" width="100%" height="292"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity : $$O(n)$$. The entire $$nums$$ array is traversed only once.</p></li>
<li><p>Space complexity : $$O(n)$$. Hashmap $$map$$ can contain up to $$n$$ distinct entries in the worst case.</p></li>
</ul>
<p><br></p>  
</div>
            