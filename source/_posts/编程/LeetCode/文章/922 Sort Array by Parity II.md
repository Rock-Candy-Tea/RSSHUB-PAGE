
---
title: '922. Sort Array by Parity II'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=5002'
author: LeetCode
comments: false
date: Tue, 01 Jun 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5002'
---

<div>   
<p>Given an array of integers <code>nums</code>, half of the integers in <code>nums</code> are <strong>odd</strong>, and the other half are <strong>even</strong>.</p>

<p>Sort the array so that whenever <code>nums[i]</code> is odd, <code>i</code> is <strong>odd</strong>, and whenever <code>nums[i]</code> is even, <code>i</code> is <strong>even</strong>.</p>

<p>Return <em>any answer array that satisfies this condition</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [4,2,5,7]
<strong>Output:</strong> [4,5,2,7]
<strong>Explanation:</strong> [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [2,3]
<strong>Output:</strong> [2,3]
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>2 <= nums.length <= 2 * 10<sup>4</sup></code></li>
<li><code>nums.length</code> is even.</li>
<li>Half of the integers in <code>nums</code> are even.</li>
<li><code>0 <= nums[i] <= 1000</code></li>
</ul>

<p> </p>
<p><strong>Follow Up:</strong> Could you solve it in-place?</p><p>[TOC]</p>
<h2 id="videosolution">Video Solution</h2>
<hr>
<div class="video-preview"></div>
<div> 
</div>
<h2 id="solutionarticle">## Solution Article</h2>
<h4 id="approach1twopass">Approach 1: Two Pass</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Read all the even integers and put them into places <code>ans[0]</code>, <code>ans[2]</code>, <code>ans[4]</code>, and so on.</p>
<p>Then, read all the odd integers and put them into places <code>ans[1]</code>, <code>ans[3]</code>, <code>ans[5]</code>, etc.</p>
<iframe src="https://leetcode.com/playground/9NCzH2qV/shared" frameborder="0" width="100%" height="429" name="9NCzH2qV"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity:  $$O(N)$$, where $$N$$ is the length of <code>A</code>.</p></li>
<li><p>Space Complexity:  $$O(N)$$.
<br>
<br></p></li>
</ul>
<hr>
<h4 id="approach2readwriteheads">Approach 2: Read / Write Heads</h4>
<p><strong>Intuition</strong></p>
<p>We are motivated (perhaps by the interviewer) to pursue a solution where we modify the original array <code>A</code> in place.</p>
<p>First, it is enough to put all even elements in the correct place, since all odd elements will be in the correct place too.  So let's only focus on <code>A[0], A[2], A[4], ...</code></p>
<p>Ideally, we would like to have some partition where everything to the left is already correct, and everything to the right is undecided.</p>
<p>Indeed, this idea works if we separate it into two slices <code>even = A[0], A[2], A[4], ...</code> and <code>odd = A[1], A[3], A[5], ...</code>.  Our invariant will be that everything less than <code>i</code> in the even slice is correct, and everything less than <code>j</code> in the odd slice is correct.</p>
<p><strong>Algorithm</strong></p>
<p>For each even <code>i</code>, let's make <code>A[i]</code> even.  To do it, we will draft an element from the odd slice.  We pass <code>j</code> through the odd slice until we find an even element, then swap.  Our invariant is maintained, so the algorithm is correct.</p>
<iframe src="https://leetcode.com/playground/aFdAKSoG/shared" frameborder="0" width="100%" height="344" name="aFdAKSoG"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity:  $$O(N)$$, where $$N$$ is the length of <code>A</code>.</p></li>
<li><p>Space Complexity:  $$O(1)$$.
<br>
<br></p></li>
</ul>  
</div>
            