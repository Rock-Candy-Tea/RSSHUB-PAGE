
---
title: '1155. Number of Dice Rolls With Target Sum'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Documents/1155/1155.svg'
author: LeetCode
comments: false
date: Sun, 17 Jul 2022 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Documents/1155/1155.svg'
---

<div>   
<p>You have <code>n</code> dice and each die has <code>k</code> faces numbered from <code>1</code> to <code>k</code>.</p>

<p>Given three integers <code>n</code>, <code>k</code>, and <code>target</code>, return <em>the number of possible ways (out of the </em><code>k<sup>n</sup></code><em> total ways) </em><em>to roll the dice so the sum of the face-up numbers equals </em><code>target</code>. Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 1, k = 6, target = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> You throw one die with 6 faces.
There is only one way to get a sum of 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 2, k = 6, target = 7
<strong>Output:</strong> 6
<strong>Explanation:</strong> You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> n = 30, k = 30, target = 500
<strong>Output:</strong> 222616187
<strong>Explanation:</strong> The answer must be returned modulo 10<sup>9</sup> + 7.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= n, k <= 30</code></li>
<li><code>1 <= target <= 1000</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>We have <code>n</code> dice, each having <code>k</code> faces with a number from <code>1</code> to <code>k</code>. We need to find the number of ways to roll these $$n$$ dice such that the sum of numbers on them is equal to <code>target</code>.</p>
<p>There are two characteristics of this problem that we should take note of at this time. First, as we iterate over the dice, we need to decide the number for each dice. The feasible options for number at the current dice depend upon the current sum, which is in turn dependent on the number we chose for the previous dice. It implies each decision we make is affected by the previous decisions we have made. Second, the problem is asking to count all the ways to roll <code>n</code> dice. These two characteristics suggest that we may be able to solve this problem using dynamic programming. We will be covering two dynamic programming approaches namely, Top-Down and Bottom-Up.
<br></p>
<hr>
<h4 id="approach1topdowndynamicprogramming">Approach 1: Top-Down Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>A common way to come up with a DP solution is to start with brute force. Let's start with a brute-force solution and then optimize it. In a brute-force solution, we can go through each possible outcome and count those with the result equal to <code>target</code>. To do this, we can iterate over the numbers <code>1</code> to <code>k</code> for each dice and add it to a variable to keep the current sum value and recursively move to the next dice. In the end, after iterating over all the dice, we can check if the current sum is equal to the <code>target</code>. If they are equal, we will increment the variable representing the number of possible ways.</p>
<p>For this recursive approach, what are the parameters that we need to track? The first parameter is the index of the die that we are currently considering as we traverse the dice. Secondly, we need to keep track of the sum of values that we chose for the previous dice.</p>
<p>In this approach, we will have to iterate over all the $$k^n$$ possibilities, and hence is not efficient. If we observe the below figure, there are repeated subproblems. Notice the green nodes are repeated subproblems signifying that we have already solved these subproblems before. To avoid recalculating results for previously seen subproblems, we will memoize the result for each subproblem. So the next time we need to calculate the result for the same set of parameters <code>&#123;index, sum&#125;</code>, we can simply look up the result in constant time instead of recalculating the result.</p>
<p><img src="https://leetcode.com/articles/Documents/1155/1155.svg" alt="fig" referrerpolicy="no-referrer"></p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Start with:</li>
</ol>
<ul>
<li>The dice index <code>diceIndex</code> is <code>0</code>; this is the index of the die we are currently considering.</li>
<li>The sum of numbers on the previous dice <code>currSum</code> as <code>0</code>.</li>
</ul>
<ol>
<li>Initialize the variable <code>ways</code> to <code>0</code>. Iterate over the values from <code>1</code> to <code>k</code>, for each value <code>i</code>:<ul>
<li>If the current die can have value <code>i</code>, i.e., <code>currSum</code> after adding <code>i</code> will not exceed the <code>target</code> value. Then update the value of <code>currSum</code> and recursively move to the next die. Add the value returned by this recursive call to <code>ways</code></li>
<li>Else, if this value is not possible, then break from the loop as the greater values will not satisfy the above condition as well.</li></ul></li>
<li>Base cases:<ul>
<li>If we have iterated over all the dice, i.e., <code>diceIndex = n</code>, then check if the <code>currSum</code> is equal to target or not.</li></ul></li>
<li>Return the value <code>ways</code> and also store it in the memoization table <code>memo</code> corresponding to the current state, which is defined by <code>diceIndex</code> and <code>currSum</code>.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/7bAyR3RJ/shared" frameborder="0" width="100%" height="500" name="7bAyR3RJ"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here, $$N$$ is the number of dice, $$K$$ is the number of faces each dice have, and $$T$$ is the <code>target</code> value.</p>
<ul>
<li><p>Time complexity: $$O(N * T * K)$$</p>
<p>Each state is defined by the <code>diceIndex</code> and the <code>currSum</code>. Hence, there will be $$N * T$$ states, and in the worst, we must visit most of the states to solve the original problem. Each recursive call will require $$O(K)$$ time as we iterate over the possible values from $$1$$ to $$K$$. Therefore, the total time required will be equal to $$O(N * T * K)$$.</p></li>
<li><p>Space complexity: $$O(N * T)$$ </p>
<p>The memoization results are stored in the table memo with size $$N * T$$. Also, stack space in the recursion is equal to the maximum number of active functions. The maximum number of active functions will be at most $$N$$, i.e., one function call for every die. Hence, the space complexity is $$O(N * T)$$.
<br></p></li>
</ul>
<hr>
<h4 id="approach2bottomupdynamicprogramming">Approach 2: Bottom-Up Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>In the previous approach, the recursive calls incurred stack space. We can avoid this by applying the same approach iteratively, which is often faster than the top-down approach. We will follow a similar approach to the previous one. However, this time we will iterate over the states by starting from the base case and ending at the initial query.</p>
<p>As per the previous approach, the recursive equation will be: <code>memo[diceIndex][currSum] = memo[diceIndex + 1][currSum + i]</code> for each <code>i</code> in the range <code>[1, K]</code>. This is because for the current dice we add the value <code>i</code> to <code>currentSum</code> and move on to the next dice. Starting from the base case we will initialize <code>memo[n][target]</code> to <code>1</code>, this is because there is only one way if no dice left and the sum is equal to target. Then we can find values for <code>diceIndex = n - 1</code> and <code>currSum</code> values in the range <code>[0, target]</code> by iterating over the values <code>[0, K]</code> for <code>i</code> using the above recursive equation.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize <code>memo[n][target]</code> to <code>1</code> and all other values to <code>0</code>.</p></li>
<li><p>Iterate over the <code>diceIndex</code> from <code>n - 1</code> to <code>0</code>; for each dice value, iterate over the <code>currSum</code> from <code>0</code> to <code>target</code>. For each such state corresponding to <code>diceIndex</code> and <code>currSum</code>:</p>
<ul>
<li>Initialize <code>ways</code> to <code>0</code>.</li>
<li>Iterate over values from <code>1</code> to <code>K</code> as <code>i</code> and for each valid value of <code>i</code> (adding <code>i</code> to <code>currSum</code> doesn't exceed <code>target</code>) add the value <code>memo[diceIndex + 1][currSum + i]</code> to <code>ways</code>.</li>
<li>Assign the <code>ways</code> to <code>memo[diceIndex][currSum]</code>.</li></ul></li>
<li><p>Return the value <code>memo[0][0]</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/TtpLddj8/shared" frameborder="0" width="100%" height="480" name="TtpLddj8"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here, $$N$$ is the number of dice, $$K$$ is the number of faces each dice have, and $$T$$ is the <code>target</code> value.</p>
<ul>
<li><p>Time complexity: $$O(N * T * K)$$</p>
<p>We have three nested loops, the first one iterate over dices from $$N - 1$$ to $$0$$, the second one iterate over sum value from $$0$$ to $$T$$, and the third value iterate over the possible values of dice face from $$1$$ to $$K$$. Hence, the total time complexity would be equal to $$O(N * T * K)$$.</p></li>
<li><p>Space complexity: $$O(N * T)$$ </p>
<p>The results are stored in the array <code>memo</code>, with the size of $$N * T$$. Hence, the space complexity is equal to $$O(N * T)$$.
<br></p></li>
</ul>
<hr>  
</div>
            