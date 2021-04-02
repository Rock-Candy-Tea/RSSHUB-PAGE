
---
title: '665. Non-Decreasing array'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/665/img1.png'
author: LeetCode
comments: false
date: Thu, 01 Apr 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/665/img1.png'
---

<div>   
<p>Given an array <code>nums</code> with <code>n</code> integers, your task is to check if it could become non-decreasing by modifying <strong>at most one element</strong>.</p>

<p>We define an array is non-decreasing if <code>nums[i] <= nums[i + 1]</code> holds for every <code>i</code> (<strong>0-based</strong>) such that (<code>0 <= i <= n - 2</code>).</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [4,2,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> You could modify the first <code>4</code> to <code>1</code> to get a non-decreasing array.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [4,2,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> You can't get a non-decreasing array by modify at most one element.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>n == nums.length</code></li>
<li><code>1 <= n <= 10<sup>4</sup></code></li>
<li><code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approachgreedy">Approach: Greedy</h4>
<p><strong>Intuition</strong></p>
<p>The one thing that we should focus on here is the fact that the problem description says non-decreasing, which is just another way of saying increasing. In this case, it means the next element must always be greater than or equal to the current element. Thus, in an array, the item on the left must be less than or equal to the item on the right. Since we can only rectify a single violation of this rule, if more than one violation exists, it is impossible to make the array non-decreasing. </p>
<p>The first time we encounter such a violation i.e. <code>nums[i - 1] > nums[i]</code>, we make a change.  You don't actually have to make a change because the question doesn't ask us to give the final array in order, it just asks if it could become non-decreasing. Then, we move on with the rest of the array, and continue to check for other violations. If it ever so happens that the rule gets violated again, we return <code>false</code> since this would be the second violation of the rule. If we don't find a second violation, we can return <code>true</code> since rectifying the first violation made our array non-decreasing.</p>
<p>Whenever we encounter a violation at a particular index <code>i</code>, we need to check what modification we can make to make the array sorted. Let's see this scenario using an example.</p>
<p><img src="https://leetcode.com/articles/Figures/665/img1.png" alt="Single violation" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1. A violation in the sorted array.</em>
&#123;:align="center"&#125;</p>
<p>In the example above, we consider the numbers <code>4, 5, 3</code> for deciding on how to fix the violation or. In this case, the correct modification is to change the number <code>3</code> to <code>5</code>. If we change <code>5</code> to <code>3</code>, then we won't be fixing the violation because the resulting array would be <code>3, 4, 3, 3, 6, 8</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/665/img2.png" alt="Single violation modification" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 2. Rectifying a single violation leading to sorted array.</em>
&#123;:align="center"&#125;</p>
<p>The basic decision making process for fixing a violation is listed below. Without considering the number at the index <code>i - 2</code>, we won't be able to choose between updating <code>nums[i]</code> or <code>nums[i - 1]</code>. The modification has to fit in with the sorted nature of the array.</p>
<pre>if nums[i - 2] > nums[i] then
    nums[i] = nums[i - 1]
else
    nums[i - 1] = nums[i]
</pre>
<p>Once we make the modification, we expect that the rest of the array will be sorted. If that is not the case, then we return <code>false</code> from our function. Some arrays will have violations in different places e.g. a <code>10</code> element array where <code>nums[4] > nums[5]</code> and also <code>nums[8] > nums[9]</code>. This array cannot be sorted by only fixing the violation at <code>nums[5]</code>.</p>
<p>Additionally, it is possible that a modification in the array leads to another violation that did not exist before. Let's consider an example where this can happen.</p>
<p><img src="https://leetcode.com/articles/Figures/665/img3.png" alt="Additional violation introduced" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 3. Rectifying a single violation introduces a new violation.</em>
&#123;:align="center"&#125;</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>We iterate over the array until we reach the end of the array or find a violation.</li>
<li>If we reach the end of the array, we know it is sorted and we return <code>true</code>.</li>
<li>Otherwise, we found a violation. We consider the <code>nums[i - 2]</code> to fix the violation. <ul>
<li>If the violation is at the index <code>1</code>, we won't have a <code>nums[i - 2]</code> available. In that case we simply set <code>nums[i - 1]</code> equal to <code>nums[i]</code>.  </li>
<li>Otherwise, we check if <code>nums[i - 2] <= nums[i]</code> in which case we set <code>nums[i - 1]</code> equal to <code>nums[i]</code>. </li>
<li>Finaly, if <code>nums[i - 2] > nums[i]</code>, then we set <code>nums[i]</code> equal to <code>nums[i - 1]</code>.</li></ul></li>
<li>Once we make the modification, we simply iterate over the remaining array. If we find another violation, we return <code>false</code>. Otherwise, we return <code>true</code> once the iteration is complete.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/VvXCTRCw/shared" frameborder="0" width="100%" height="480" name="VvXCTRCw"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity: $$O(n)$$ considering there are $$n$$ elements in the array and we process each element at most once.</p></li>
<li><p>Space Complexity: $$O(1)$$ since we don't use any additional space apart from a couple of variables for executing this algorithm.</p></li>
</ul>  
</div>
            