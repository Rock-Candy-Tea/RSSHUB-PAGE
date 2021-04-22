
---
title: '1423. Maximum Points You Can Obtain from Cards'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/1423/1423_Maximum_Points_You_Can_Obtain_from_Cards_Overview_Image.png'
author: LeetCode
comments: false
date: Wed, 21 Apr 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/1423/1423_Maximum_Points_You_Can_Obtain_from_Cards_Overview_Image.png'
---

<div>   
<p>There are several cards <strong>arranged in a row</strong>, and each card has an associated number of points The points are given in the integer array <code>cardPoints</code>.</p>

<p>In one step, you can take one card from the beginning or from the end of the row. You have to take exactly <code>k</code> cards.</p>

<p>Your score is the sum of the points of the cards you have taken.</p>

<p>Given the integer array <code>cardPoints</code> and the integer <code>k</code>, return the <em>maximum score</em> you can obtain.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> cardPoints = [1,2,3,4,5,6,1], k = 3
<strong>Output:</strong> 12
<strong>Explanation:</strong> After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> cardPoints = [2,2,2], k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> Regardless of which two cards you take, your score will always be 4.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> cardPoints = [9,7,7,9,7,7,9], k = 7
<strong>Output:</strong> 55
<strong>Explanation:</strong> You have to take all the cards. Your score is the sum of points of all cards.
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> cardPoints = [1,1000,1], k = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> You cannot take the card in the middle. Your best score is 1. 
</pre>

<p><strong>Example 5:</strong></p>

<pre><strong>Input:</strong> cardPoints = [1,79,80,1,1,1,200,1], k = 3
<strong>Output:</strong> 202
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= cardPoints.length <= 10^5</code></li>
<li><code>1 <= cardPoints[i] <= 10^4</code></li>
<li><code>1 <= k <= cardPoints.length</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>The brute force solution is to find all valid combinations of cards and then select the combination that gives us the maximum sum. To accomplish this, we can use a recursive approach. At each point, we choose a card either from the beginning or from the end of the array. Our base condition is when <code>k</code> cards are selected or when no cards are left to be selected.
This solution results in TLE because it checks an exponential number of combinations (many of the same combinations would be checked more than once). 
We can optimize this solution by using a <strong>dynamic programming</strong> approach.</p>
<p>A key observation in this problem is that <em>we need to select k cards from the beginning or end of the array</em>. Thus no matter how many cards we choose from the beginning, in the end, we need to select two subarrays: one from the beginning, and one from the end, and their total lengths must be <code>k</code> (the only exception is when <code>k = cardPoints.length</code>, in that case, we'll select all cards). Thus after selecting the two arrays we will be left with a single subarray of length <code>cardPoints.length - k</code>. There are three ways we can select the cards:</p>
<ol>
<li>Select all cards from the beginning.</li>
<li>Select all cards from the end.</li>
<li>Select some cards from the beginning and the rest from the end.</li>
</ol>
<p>In all the above three cases we will be left with a subarray (in the end, in the beginning, or somewhere in the middle) after our selection. This can be better understood in the following illustration where we are selecting 3 cards from an array of 8 cards.</p>
<p><img src="https://leetcode.com/articles/Figures/1423/1423_Maximum_Points_You_Can_Obtain_from_Cards_Overview_Image.png" alt="fig" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1. An example demonstrating some of the positions of the subarrays possible from selecting <code>k = 3</code> cards from the array.</em>
&#123;:align="center"&#125;</p>
<p>In addition to the dynamic programming approach, we can also take a <strong>sliding window</strong> approach. A sliding window is a standard programming pattern used in many problems, including those related to finding the sum or the product of a subarray. In case you are not familiar with sliding windows, you can go through this article written by one of our LeetCode users: <a href="https://leetcode.com/discuss/study-guide/657507/Sliding-Window-for-Beginners-Problems-or-Template-or-Sample-Solutions">Sliding Window Problems for Beginners</a>.
In this article, we'll start by looking at the dynamic programming approach and discuss how to optimize its space complexity. After that, we will finish with the sliding window approach.</p>
<p><br></p>
<hr>
<h4 id="approach1dynamicprogramming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>As we determined above, the <code>k</code> cards that we choose will form two contiguous subarrays: one at the start, and one at the end of the input array. If we choose <code>i</code> cards from the start (where <code>i <= k</code>) then we must choose <code>k - i</code> cards from the end. There are <code>k</code> <em>different</em> lengths the first array could be. </p>
<p>Since these <code>k</code> arrays are <em>overlapping</em>, we can calculate the <strong>prefix sum</strong> for each of the first <code>k</code> values, and then for each of the last <code>k</code> values (working from the end of the array, and going inwards). We will store these values in two arrays of size <code>k</code>.</p>
<p>We can then use these to efficiently check each possible way of selecting <code>i</code> cards from the start and <code>k - i</code> cards from the end.</p>
<p>!?!../Documents/1423<em>Maximum</em>Points<em>You</em>Can<em>Obtain</em>from_Cards.json:960,540!?!</p>
<p><br></p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize two arrays of size <code>k + 1</code>, namely <code>frontSetOfCards</code> and <code>rearSetOfCards</code> to store the score (prefix sums) obtained by selecting the first <code>i</code> cards and the last <code>i</code> cards in the array.</p></li>
<li><p>We calculate the prefix sum (sum of <code>0 <= i <= k</code> cards) for the first <code>k</code> cards <code>frontSetOfCards[i + 1] = frontSetOfCards[i] + cardPoints[i]</code> and the last <code>k</code> cards <code>rearSetOfCards[i + 1] = cardPoints[n - i - 1] + rearSetOfCards[i]</code>.</p></li>
<li><p>Initialize <code>maxScore</code> to 0.</p></li>
<li><p>Iterate from <code>i = 0 -> k</code>. At each iteration, we determine the possible score by selecting <code>i</code> cards from the beginning of the array and <code>k - i</code> cards from the end (<code>currentScore</code>). If this score is greater than the <code>maxScore</code> then we update it.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/AZ37sVqF/shared" frameborder="0" width="100%" height="500" name="AZ37sVqF"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$k$$ be the number of cards we need to select.</p>
<ul>
<li><p>Time complexity: $$O(k)$$. Here we are using two <code>for</code> loops of length <code>k</code> to calculate the maximum possible score. This gives us $$O(2 \cdot k)$$, which in Big O notation is equal to $$O(k)$$.</p></li>
<li><p>Space complexity: $$O(k)$$. Here we are using two arrays to store the total score obtained by selecting $$i(0 <= i < k)$$ cards from the beginning and $$i$$ cards from the end. This gives us $$O(2 \cdot k)$$, which is equal to $$O(k)$$.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2dynamicprogrammingspaceoptimized">Approach 2: Dynamic Programming - Space Optimized</h4>
<p><strong>Intuition</strong></p>
<p>In approach 1 we used two extra storage spaces (two arrays of size <code>k</code>) to store the total score that can be obtained by taking <code>i</code> cards from the respective end of the array. </p>
<p>Instead of pre-computing the arrays, we can calculate the total score while iterating over the array and store the total score in two variables (in place of the two arrays).</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize two variables, namely <code>frontScore</code> and <code>rearScore</code> to store the score obtained by selecting the first <code>i</code> cards and the last <code>k - i</code> cards in the array.</p></li>
<li><p><code>frontScore</code> is initialized to the sum of the first <code>k</code> cards in the array, and <code>rearScore</code> is initialized to <code>0</code>.</p></li>
<li><p>Initialize <code>maxScore</code> to  <code>frontScore</code>.</p></li>
<li><p>Iterate backwards from <code>i = k - 1 -> 0</code>. At each iteration, we calculate the score by selecting <code>i</code> cards from the beginning of the array and <code>k - i</code> cards from the end (<code>currentScore</code>). If this score is greater than <code>maxScore</code>, we update it.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/ifWWPQjZ/shared" frameborder="0" width="100%" height="497" name="ifWWPQjZ"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$k$$ be the number of cards we need to select.</p>
<ul>
<li><p>Time complexity: $$O(k)$$. We are using two <code>for</code> loops of length <code>k</code> for calculation purposes. This gives us $$O(2 \cdot k)$$, which in Big O notation is equal to $$O(k)$$.</p></li>
<li><p>Space complexity: $$O(1)$$. No extra space is used since all the calculations are done impromptu.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3slidingwindow">Approach 3: Sliding Window</h4>
<p><strong>Intuition</strong></p>
<p>In this problem, we must draw exactly <code>k</code> cards from the array in such a way that the score (sum of the cards) is maximized. After drawing <code>k</code> cards from the array <code>cardPoints.length - k</code> cards will remain in the array.</p>
<p>Another way that we could view the problem is that our objective is to choose cards from the beginning or end of the array in such a way that the sum of the <em>remaining</em> cards is <em>minimized</em>. </p>
<p>We can use a sliding window to find the subarray of size <code>cardPoints.length - k</code> that has the minimal sum. Subtracting this value from the total sum of all the cards will give us our answer. This is because no matter where the minimum subarray is located (in the beginning, the middle, or the end) the remaining cards must be selected under the given rule: <em>in one step, you can take one card from the beginning or the end of the array</em>.  </p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Find the sum of all cards in the array and store it in a variable <code>totalScore</code>.</p></li>
<li><p>If <code>k</code> is equal to <code>cardPoints.length</code>, then <code>return totalScore</code>.</p></li>
<li><p>Initialize <code>requiredSubarrayLength</code> to <code>cardPoints.length - k</code>.</p></li>
<li><p>Initialize two variables: <code>presentSubarrayScore</code> and <code>startingIndex</code> to <code>0</code>. This <code>startingIndex</code> marks the starting point of the subarray presently under consideration. Thus it keeps track of the length of the present subarray. </p></li>
<li><p>Initialize a variable <code>minSubarrayScore</code> to <code>totalScore</code>. When the algorithm completes, this variable will hold the smallest possible subarray score in the input array.</p></li>
<li><p>Iterate over the array.</p>
<ul>
<li>At each iteration add the current card to <code>presentSubarrayScore</code>.</li></ul></li>
<li><p>If the size of the subarray under consideration <code>presentSubarrayLength</code> is equal to the <code>requiredSubarrayLength</code>:</p>
<ul>
<li>Compare the score of the subarray <code>presentSubarrayScore</code> with the <code>minSubarrayScore</code> and modify the <code>minSubarrayScore</code> so that it stores the minimum possible subarray sum. </li>
<li>Subtract the current card from the <code>presentSubarrayScore</code>.</li>
<li>Increment the <code>startingIndex</code>.</li></ul></li>
<li><p>Subtract the <code>minSubarrayScore</code> from the <code>totalScore</code> to get the maximum total score that can be obtained by picking <code>k</code> cards from the beginning or the end of the array. Return this value.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/VyiiNqzW/shared" frameborder="0" width="100%" height="500" name="VyiiNqzW"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the number of cards we need to select.</p>
<ul>
<li><p>Time complexity: $$O(n)$$. In the problem, we are iterating over the array of cards twice. So the time complexity will be $$O(2 \cdot n)$$ = $$O(n)$$.</p></li>
<li><p>Space complexity: $$O(1)$$ since no extra space is required.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            