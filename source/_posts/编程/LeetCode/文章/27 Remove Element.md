
---
title: '27. Remove Element'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=4242'
author: LeetCode
comments: false
date: Wed, 24 Aug 2022 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4242'
---

<div>   
<p>Given an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences of <code>val</code> in <code>nums</code> <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a>. The relative order of the elements may be changed.</p>

<p>Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the <strong>first part</strong> of the array <code>nums</code>. More formally, if there are <code>k</code> elements after removing the duplicates, then the first <code>k</code> elements of <code>nums</code> should hold the final result. It does not matter what you leave beyond the first <code>k</code> elements.</p>

<p>Return <code>k</code><em> after placing the final result in the first </em><code>k</code><em> slots of </em><code>nums</code>.</p>

<p>Do <strong>not</strong> allocate extra space for another array. You must do this by <strong>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> with O(1) extra memory.</p>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) &#123;
    assert nums[i] == expectedNums[i];
&#125;
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,2,3], val = 3
<strong>Output:</strong> 2, nums = [2,2,_,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,2,2,3,0,4,2], val = 2
<strong>Output:</strong> 5, nums = [0,1,4,0,3,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>0 <= nums.length <= 100</code></li>
<li><code>0 <= nums[i] <= 50</code></li>
<li><code>0 <= val <= 100</code></li>
</ul><p>[TOC]</p>
<h2 id="summary">Summary</h2>
<p>This is a pretty easy problem, but one may get confused by the term "in-place" and think it is impossible to remove an element from the array without making a copy of the array.</p>
<h2 id="hints">Hints</h2>
<ol>
<li>Try two pointers.</li>
<li>Did you use the fact that the order of elements can be changed?</li>
<li>What happens when the elements to remove are rare?</li>
</ol>
<h2 id="videosolution">Video Solution</h2>
<hr>
<div class="video-preview"></div>
<h2 id="solutionarticle">## Solution Article</h2>
<h4 id="approach1twopointers">Approach 1: Two Pointers</h4>
<p><strong>Intuition</strong></p>
<p>Since this question is asking us to remove all elements of the given value in-place, we have to handle it with $$O(1)$$ extra space. How to solve it? We can keep two pointers $$i$$ and $$j$$, where $$i$$ is the slow-runner while $$j$$ is the fast-runner.</p>
<p><strong>Algorithm</strong></p>
<p>When $$nums[j]$$ equals to the given value, skip this element by incrementing $$j$$. As long as $$nums[j] \neq val$$, we copy $$nums[j]$$ to $$nums[i]$$ and increment both indexes at the same time. Repeat the process until $$j$$ reaches the end of the array and the new length is $$i$$.</p>
<p>This solution is very similar to the solution to <a href="https://leetcode.com/articles/remove-duplicates-from-sorted-array/">Remove Duplicates from Sorted Array</a>.</p>
<iframe src="https://leetcode.com/playground/SRsw79ix/shared" frameborder="0" width="100%" height="225" name="SRsw79ix"></iframe>
<p><strong>Complexity analysis</strong></p>
<ul>
<li><p>Time complexity : $$O(n)$$.
Assume the array has a total of $$n$$ elements, both $$i$$ and $$j$$ traverse at most $$2n$$ steps.</p></li>
<li><p>Space complexity : $$O(1)$$.
<br></p></li>
</ul>
<h2 id="br"><br></h2>
<h4 id="approach2twopointerswhenelementstoremovearerare">Approach 2: Two Pointers - when elements to remove are rare</h4>
<p><strong>Intuition</strong></p>
<p>Now consider cases where the array contains few elements to remove. For example, $$nums = [1,2,3,5,4], val = 4$$. The previous algorithm will do unnecessary copy operation of the first four elements. Another example is $$nums = [4,1,2,3,5], val = 4$$. It seems unnecessary to move elements $$[1,2,3,5]$$ one step left as the problem description mentions that the order of elements could be changed.</p>
<p><strong>Algorithm</strong></p>
<p>When we encounter $$nums[i] = val$$, we can swap the current element out with the last element and dispose the last one. This essentially reduces the array's size by 1.</p>
<p>Note that the last element that was swapped in could be the value you want to remove itself. But don't worry, in the next iteration we will still check this element.</p>
<iframe src="https://leetcode.com/playground/5syAKQ2f/shared" frameborder="0" width="100%" height="293" name="5syAKQ2f"></iframe>
<p><strong>Complexity analysis</strong></p>
<ul>
<li><p>Time complexity : $$O(n)$$.
Both $$i$$ and $$n$$ traverse at most $$n$$ steps. In this approach, the number of assignment operations is equal to the number of elements to remove. So it is more efficient if elements to remove are rare.</p></li>
<li><p>Space complexity : $$O(1)$$.</p></li>
</ul>  
</div>
            