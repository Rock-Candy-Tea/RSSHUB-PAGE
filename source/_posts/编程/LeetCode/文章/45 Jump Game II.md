
---
title: '45. Jump Game II'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/45/45-Page-1.png'
author: LeetCode
comments: false
date: Thu, 01 Apr 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/45/45-Page-1.png'
---

<div>   
<p>Given an array of non-negative integers <code>nums</code>, you are initially positioned at the first index of the array.</p>

<p>Each element in the array represents your maximum jump length at that position.</p>

<p>Your goal is to reach the last index in the minimum number of jumps.</p>

<p>You can assume that you can always reach the last index.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [2,3,0,1,4]
<strong>Output:</strong> 2
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= nums.length <= 1000</code></li>
<li><code>0 <= nums[i] <= 10<sup>5</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>To find the minimum number of jumps, the brute force solution would be to exhaustively test all possible routes connecting the start and the end of <code>nums</code>. This can be achieved by backtracking. If you are not so sure about how backtracking works or how to implement backtracking, <a href="https://leetcode.com/problems/jump-game/solution/#approach-1-backtracking">55. Jump Game - Approach 1 Backtracking</a> has a very clear explanation. Also, feel free to check out our <a href="https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/">Backtracking Explore Card</a>. This problem is very similar to <a href="https://leetcode.com/problems/jump-game/solution/#approach-1-backtracking">Jump Game</a> so we only need to make one change to the solution. While exploring every jump pattern that takes us from the first position to the last position, we must also keep track of the number of jumps.</p>
<p>However, an exhaustive search would lead to <code>Time Limited Exceeded</code>, because we are literally finding every possible route and its time complexity is $$O(2^N)$$ in the worst case. A key observation is that we don't have to explore every route. Instead, we can find the shortest jumps by making locally optimal choices at each index which leads to a globally optimal solution. Henceforth, this article will focus on introducing an optimized solution: Greedy algorithm.</p>
<p><br></p>
<hr>
<h4 id="approachgreedy">Approach: Greedy</h4>
<p><strong>Intuition</strong></p>
<p>Imagine that you are at index <code>i</code> in the array, the element in your current position defines the maximum distance that you can jump. Therefore, your next step will fall somewhere in the range <code>[start, end]</code>, where <code>start</code> is the place right next to you and <code>end</code> is <code>i + nums[i]</code>. Then the question is, where to jump?</p>
<p><img src="https://leetcode.com/articles/Figures/45/45-Page-1.png" alt="How to choose where to jump." referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1. How to choose where to jump.</em>
&#123;:align="center"&#125;</p>
<p>To answer this question, let's think about it in the following way. Our next move will fall somewhere between <code>[start : end]</code> and to find the minimum number of jumps to reach the end of the array, we must determine which place will take us the farthest in the next jump.</p>
<p><img src="https://leetcode.com/articles/Figures/45/45-Page-2.png" alt="Choose the one that leads us farther." referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 2. Choose the one that leads us farther.</em>
&#123;:align="center"&#125;</p>
<blockquote>
  <p>As you may notice, we are using a greedy approach: always jump to the place that will take us the farthest. Greedy algorithms always make locally optimal decisions, which may or may not lead to the globally optimal solution. Therefore, we must test our greedy algorithm to see if we can prove that it leads to the globally optimal solution.</p>
</blockquote>
<p>We will use proof by contradiction to verify that the greedy algorithm is correct. Our statement is <em>if at any step, we make a different choice than what our greedy algorithm would make, we can find a better solution to the problem</em>.</p>
<p><img src="https://leetcode.com/articles/Figures/45/45-Page-3.png" alt="Proof of correctness of our greedy approach." referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 3. Proof of correctness for our greedy approach.</em>
&#123;:align="center"&#125;</p>
<p>As shown in Figure 3, consider two people A and B, where A follows our greedy strategy and B follows the optimal solution. The number at each index defines the maximum jump distance. Let's assume that until this point, their decisions have been identical, and this is when the disagreement happens.</p>
<p>Note that the choice they make for this jump will define the subarray for the next jump. The greedy solution always picks the largest subarray. Thus A will always have a larger subarray than B. Henceforth, it's not possible to beat the greedy algorithm at any step and reach the end of the array in fewer jumps; this contradicts our statement.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Initialize three integer variables: <code>jumps</code> to count the number of jumps, <code>currentJumpEnd</code> to mark the end of the range that we can jump to, and <code>farthest</code> to mark the farthest place that we can reach. Set each variable to zero.</li>
<li>Iterate over <code>nums</code>. Note that we exclude the last element from our iteration because as soon as we reach the last element, we do not need to jump anymore.</li>
<li>Update <code>farthest</code> to <code>i + nums[i]</code> if the latter is larger.</li>
<li>If we reach <code>currentJumpEnd</code>, it means we finished the current jump, and can begin checking the next jump by setting <code>currentJumpEnd = farthest</code>.</li>
<li>Return <code>jumps</code>.</li>
</ul>
<iframe src="https://leetcode.com/playground/nouVn7Se/shared" frameborder="0" width="100%" height="327" name="nouVn7Se"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity: $$O(N)$$ because there are $$N$$ elements in the array and we visit each element in the array only once.</p></li>
<li><p>Space Complexity: $$O(1)$$ because we don't use any additional data structures.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            