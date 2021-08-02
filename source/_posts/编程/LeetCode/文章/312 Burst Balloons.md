
---
title: '312. Burst Balloons'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Documents/312/312_overview.drawio.svg'
author: LeetCode
comments: false
date: Mon, 26 Jul 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Documents/312/312_overview.drawio.svg'
---

<div>   
<p>You are given <code>n</code> balloons, indexed from <code>0</code> to <code>n - 1</code>. Each balloon is painted with a number on it represented by an array <code>nums</code>. You are asked to burst all the balloons.</p>

<p>If you burst the <code>i<sup>th</sup></code> balloon, you will get <code>nums[i - 1] * nums[i] * nums[i + 1]</code> coins. If <code>i - 1</code> or <code>i + 1</code> goes out of bounds of the array, then treat it as if there is a balloon with a <code>1</code> painted on it.</p>

<p>Return <em>the maximum coins you can collect by bursting the balloons wisely</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,1,5,8]
<strong>Output:</strong> 167
<strong>Explanation:</strong>
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,5]
<strong>Output:</strong> 10
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>n == nums.length</code></li>
<li><code>1 <= n <= 500</code></li>
<li><code>0 <= nums[i] <= 100</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>This is an interesting problem. Whenever we burst a balloon, we gain a certain number of coins equal to the product of the points of the burst balloon and its neighbors. Our goal is to maximize the total coins gained. A visual example of the balloon bursting process is given below.</p>
<p><img src="https://leetcode.com/articles/Documents/312/312_overview.drawio.svg" alt="Overview" referrerpolicy="no-referrer"></p>
<p>Two hints can be observed from the diagram above and the problem description. First, the problem asks us to <strong>maximize</strong> some value (the number of coins we can collect).  Second, each decision that we make at depends on previously made decisions, in this case the balloons that we have to choose from depends on which ballons we already popped.  Both of these attributes are characteristic of dynamic programming (DP) problems.  As such, we will approach this problem using dynamic programming. We will start with a naive DP approach that is intuitive but suboptimal.  The approach is good starting point that needs some optimizations, which may require you to think outside the box.</p>
<p>Below, we will discuss three approaches: <em>Dynamic Programming (Naive)</em>, <em>Dynamic Programming (Top-Down)</em>, and <em>Dynamic Programming (Bottom-Up)</em>.</p>
<p>The first approach (naive DP) receives <em>Time Limit Exceed</em> and will be optimized in approaches 2 and 3. The purpose of including this approach is to show the thought process from scratch to the optimized solutions. Approaches 2 and 3 have the same ideas but differ in implementation details. We will explain the intuition behind them heavily in Approach 2.</p>
<p>Therefore, the recommended reading order is <strong>Approach 1 then Approach 2 then Approach 3</strong>.</p>
<p><br></p>
<hr>
<h4 id="approach1dynamicprogrammingnaive">Approach 1: Dynamic Programming (Naive)</h4>
<blockquote>
  <p>This approach is <em>Time Limit Exceed</em> and will be optimized in approaches 2 and 3.
  It is still recommended to read since the ideas of approaches 2 and 3 are evolved from here.</p>
</blockquote>
<p><strong>Intuition</strong></p>
<blockquote>
  <p>In this part, we will explain how to think of this approach step by step.</p>
  <p>If you are purely interested in the algorithm, you can jump to the algorithm part in Approach 2.</p>
</blockquote>
<p>Whenever the problem involves different intermediate states and only one final state, it may hint that <strong><em>Dynamic Programming</em></strong> is a viable approach.</p>
<p>Also, DP is our old friend in hard-level problems. If you do not have any idea, you can always give DP a try.</p>
<p>Often, the Top-Down DP approach is more intuitive to implement than the Bottom-Up DP approach. Let's try Top-Down DP first.</p>
<blockquote>
  <p><strong>Tip: Top-Down DP vs. Bottom-Up DP</strong></p>
  <p>Top-Down DP, also known as Memoization DP, uses recursive function and memoization.</p>
  <p>Bottom-Up DP, also known as Tabulation DP, uses iteration and DP array.</p>
  <p>For details, check out <a href="https://stackoverflow.com/questions/6164629/what-is-the-difference-between-bottom-up-and-top-down">Stack Overflow: What is the difference between bottom-up and top-down?</a>.</p>
</blockquote>
<p>Generally, a basic template of a Top-Down DP follows the below pseudo-code. Don't worry if you do not get the idea from this template alone, we will dive into details right after this, just follow along for now.</p>
<pre><code class="js language-js">function dp(dp_state, memo_dict) &#123;
    // check if we have seen this dp_state
    if dp_state in memo_dict
        return memo_dict[dp_state]

    // base case (a case that we know the answer for already) such as dp_state is empty
    if dp_state is the base cases
        return things like 0 or null

    calculate dp(dp_state) from dp(other_state)

    save dp_state and the result into memo_dict
&#125;
function answerToProblem(input) &#123;
    return dp(start_state, empty_memo_dict)
&#125;
</code></pre>
<blockquote>
  <p><strong>Tip: Decorators for Memoization</strong></p>
  <p>In some languages such as <code>Python</code>, there are some decorators for memoization, such as <code>lru_cache</code>.</p>
  <p>Such decorators automatically maintain the memo<em>dict for us and check if each dp</em>state has been seen.</p>
</blockquote>
<p>Okay, let's fill in the template. There are four key items that we need to fill in:</p>
<ol>
<li>What is <code>dp_state</code>?</li>
<li>What does <code>dp</code> function return?</li>
<li>What is the base case?</li>
<li>How to calculate <code>dp(dp_state)</code> from <code>dp(other_state)</code>?</li>
</ol>
<p>Back to the problem. Since we are bursting balloons in <code>nums</code> and <code>nums</code> keeps changing, it might be a good idea to use <code>nums</code> to define our <code>dp_state</code>. <code>dp(nums, memo_dict)</code> will return the maximum coins obtainable if we burst all balloons in <code>nums</code>.</p>
<p>The base case should be a subproblem for which we already know the answer.  For example: When <code>nums</code> is empty, we cannot burst any more balloons, so return 0.</p>
<pre><code class="js language-js">// memo_dict is ignored for readability
// return maximum coins obtainable by optimally bursting all balloons in `nums`.
function dp(nums) &#123;
    // base case
    if nums is empty
        return 0
    calculate dp(nums) from dp(other_state)
&#125;
</code></pre>
<p>How do we calculate <code>dp(nums)</code> from <code>dp(other_state)</code>?</p>
<p>When given <code>nums</code>, we can burst any balloon in <code>nums</code>. We can try all possibilities and return the maximum.</p>
<pre><code class="js language-js">// memo_dict is ignored for readability
// return maximum coins obtainable by optimally bursting all balloons in `nums`.
function dp(nums) &#123;
    // base case is ignored
    max_coins = 0
    for i in 1...nums.length-2:
        // burst nums[i]
        gain = nums[i - 1] * nums[i] * nums[i + 1]
        // burst the remaining balloons
        remaining = dp(nums without nums[i])
        max_coins = max(max_coins, gain + remaining)
    return max_coins
&#125;
</code></pre>
<p>The above template will work for the most part of <code>nums</code>. However, <code>nums[i - 1]</code> and <code>nums[i + 1]</code> may be out of bounds for edge cases (leftmost and rightmost).</p>
<p>To handle these edge cases, we have two solutions:</p>
<ol>
<li>Add fake balloons (each with the value of 1) to the beginning and the end of the original <code>nums</code>.</li>
<li>Use a customary <code>getOrDefault(nums, i, default)</code> to replace <code>nums[i]</code>.</li>
</ol>
<p>Both options work, but here we will implement the first one, and just let <code>nums = [1] + nums + [1]</code>.</p>
<p><img src="https://leetcode.com/articles/Documents/312/312_add_one.drawio.svg" alt="Add One" referrerpolicy="no-referrer"></p>
<blockquote>
  <p><strong>Tip: Sentinel Node</strong></p>
  <p>The fake balloons solution is a bit similar to Sentinel Node we use in linked lists. Both are fake and used to handle edge cases.</p>
  <p>To learn more about Sentinel Nodes, check out <a href="https://en.wikipedia.org/wiki/Sentinel_node">Wikipedia: Sentinel node</a>.</p>
</blockquote>
<p>To sum up, our pseudo-code right now is:</p>
<pre><code class="js language-js">// return maximum coins obtainable if we burst all balloons in `nums`.
function dp(nums, memo_dict) &#123;
    // check if have we seen this dp_state
    if nums in memo_dict
        return memo_dict[dp_state]

    // base case
    if nums is empty
        return 0

    max_coins = 0
    for i in 1 ... nums.length - 2:
        // burst nums[i]
        gain = nums[i - 1] * nums[i] * nums[i + 1]
        // burst the remaining balloons
        remaining = dp(nums without nums[i])
        max_coins = max(max_coins, gain + remaining)

    save dp_state and the result into memo_dict
    return max_coins
&#125;

function maxCoin(nums) &#123;
    nums = [1] + nums + [1] // add fake balloons
    return dp(nums, empty_memo_dict)
&#125;
</code></pre>
<p>Hopefully, at this point, the above variation of the basic template is not difficult to follow.</p>
<p>Let's take a moment to analyze the complexity of our solution so far.</p>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the number of balloons given.</p>
<ul>
<li><p>Time complexity: $$O(N2^N)$$</p></li>
<li><p>There are $$O(2^N)$$ states. For each state, determining the maximum coins requires iterating over all balloons. Thus the total time complexity is $$O(2^N) \times O(N) = O(N2^N)$$.</p></li>
<li><p>From the problem description, we know that <code>1 <= N <= 500</code>. Therefore, in the worst case, time_complexity $$ = 2^&#123;500&#125; \times 500 \approx 1.6 \times 10^&#123;154&#125;$$, which is unacceptable. Generally, a number around or less then $$10^8$$ is feasible.</p></li>
<li><p>Space complexity: $$O(N2^N)$$</p></li>
<li><p>There are $$O(2^N)$$ states, and we need $$O(N)$$ to store each state. In total, this algorithm requires $$O(2^N) \times O(N) = O(N2^N)$$ space.</p></li>
</ul>
<p>How can we improve our time complexity? Let's go to <strong>Approach 2</strong>.</p>
<blockquote>
  <p>This approach is <em>Time Limit Exceed</em> and will be optimized in Approach 2 and 3.</p>
</blockquote>
<p><br></p>
<hr>
<h4 id="approach2dynamicprogrammingtopdown">Approach 2: Dynamic Programming (Top-Down)</h4>
<p><strong>Intuition</strong></p>
<p>We are going to improve our naive DP approach.</p>
<blockquote>
  <p>If you haven't read the Approach 1 (the naive DP approach), it is recommended to read it first.</p>
  <p>If you are purely interested in the algorithm, you can jump to the algorithm section below.</p>
</blockquote>
<p>Let's dig deeper into the time complexity, which can be divided into two parts: <code>number_of_states</code> and <code>time_spent_on_each_state</code>.</p>
<p>Therefore, generally, there are two approaches to decrease the time complexity.</p>
<ol>
<li>Decrease <code>number_of_states</code>.</li>
<li>Decrease <code>time_spent_on_each_state</code>.</li>
</ol>
<p>Here, our <code>number_of_states</code> is $$O(2^N)$$, which is far larger than <code>time_spent_on_each_state</code>. As such, we may benefit more by considering how to reduce <code>number_of_states</code>. For this problem, a good target to reduce <code>number_of_states</code> to is $$O(N^2)$$.  This would reduce the total operations to $$N^2 \times N = N^3 \approx 1.25 * 10^8$$ which as mentioned before is close to the upper limit of operations that can be executed in a reasonable amount of time.</p>
<p>What can we do to decrease <code>number_of_states</code>?</p>
<p>As you may remember, we can use <code>left</code> and <code>right</code> pointers to represent a subarray in the original array.</p>
<p>If we can use <code>dp(left, right)</code> to replace <code>dp(nums)</code>, then the problem is solved.</p>
<p>But our DP states are not continuous and are not always a subarray of <code>nums</code>. For example, we can burst many balloons in the middle.</p>
<p><img src="https://leetcode.com/articles/Documents/312/312_not_continuous.drawio.svg" alt="Not Continuous" referrerpolicy="no-referrer"></p>
<p>Is that really true? Do we have a workaround?</p>
<p>Take a deeper look at what happens when we burst the first balloon.</p>
<p><img src="https://leetcode.com/articles/Documents/312/312_first_burst.drawio.svg" alt="First Burst" referrerpolicy="no-referrer"></p>
<p>Is there any continuous array? Yes! The burst balloon divides the original array into two <strong>subarrays</strong>.</p>
<p>We can recursively call the left subarray and the right subarray, and add the results together.</p>
<pre><code class="js language-js">// memo_dict is ignored for readability
// return the maximum coins obtainable if we burst all balloons 
// in nums[left] ... nums[right], inclusively.
function dp(left, right) &#123;
    // base case is ignored
    max_coins = 0
    for i in 1 ... nums.length - 2:
        // burst nums[i]
        gain = nums[i - 1] * nums[i] * nums[i + 1]
        // burst remaining
        remaining = dp(left, i - 1) + dp(i + 1, right)
        max_coins = max(result, gain + remaining)
    return max_coins
&#125;
</code></pre>
<blockquote>
  <p><strong>Tip: Divide and Conquer</strong></p>
  <p>Here we divide the original array into two subarrays and then conquer them respectively. It is a perfect example of the Divide and Conquer algorithm.</p>
  <p>For details, check out <a href="https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm">Wikipedia: Divide and Conquer</a></p>
  <p><strong>Tip: Inclusive or Not</strong></p>
  <p>Should <code>dp(left, right)</code> represent the maximum coins obtainable after bursting <code>[left, right]</code>, <code>[left, right)</code>, …, or <code>(left, right)</code>?</p>
  <p>In other words, should we include the edge case?</p>
  <p>The answer is that all of them work. However, <code>[left, right]</code> may be easier to visualize, and <code>[left, right)</code> maybe easier to implement. Here, we choose <code>[left, right]</code>.</p>
</blockquote>
<p>Wait! You may say, this code yields the wrong answer!</p>
<p>Oh. What happened?</p>
<p>Note in this line</p>
<pre><code class="js language-js">remaining = dp(left, i - 1) + dp(i + 1, right)
</code></pre>
<p>Inside the left part <code>dp(left, i - 1)</code>, when we burst the rightmost balloon (i.e., <code>i - 1</code>th), what will we gain?</p>
<p><code>nums[i - 2] * nums[i - 1] * nums[i]</code>? No, <code>nums[i]</code> has been burst, so <code>nums[i]</code> should be replaced by <strong>some balloon</strong> in the right part.</p>
<p>But exactly which one? Well…it seems it depends on the <strong>order</strong> of bursting balloons in the left part and in the right part.</p>
<p><img src="https://leetcode.com/articles/Documents/312/312_not_independent.drawio.svg" alt="Not Independent" referrerpolicy="no-referrer"></p>
<p>In other words, <code>dp(left, i - 1)</code> and <code>dp(i + 1, right)</code> are not independent, and cannot be calculated separately.</p>
<p>Bad news. Our divide and conquer plan fails. Is there any way to fix this?</p>
<p>What if…<code>nums[i]</code> has not burst? If we keep <code>nums[i]</code> alive <strong>all the time</strong>, then <code>nums[i - 2] * nums[i - 1] * nums[i]</code> always refers to the correct balloons, and the left part and right part are independent.</p>
<p>How to keep <code>nums[i]</code> alive <strong>all the time</strong>? Easy, just mark <code>nums[i]</code> as the <strong>last</strong> burst balloon among <code>[left, right]</code>.</p>
<p><img src="https://leetcode.com/articles/Documents/312/312_keep_i.drawio.svg" alt="Keep i" referrerpolicy="no-referrer"></p>
<blockquote>
  <p><strong>Tip: Thinking Backwards</strong></p>
  <p>Instead of thinking of which one to burst <strong>first</strong>, we think of which one to burst <strong>last</strong>.</p>
  <p>Alternatively, you can reverse the whole process: instead of bursting the balloon, we add balloons to the empty array. This approach will result in the same code.</p>
</blockquote>
<h5 id="specialcases">Special Cases</h5>
<p>Now our time complexity is $$O(N^3)$$. Are there any other rooms to optimize? Note that if the array has some special properties, we may be able to calculate the result very fast.</p>
<p>For example, if all the numbers are the same, the answer is straight forward.</p>
<p>Let <code>N</code> be the length of <code>nums</code>, and <code>a</code> be the element in <code>nums</code>. The coins we gain, no matter which one is burst, are always <code>a * a * a</code>, since all balloons are the same, except the last two balloons. For the last two balloons, one yields <code>a * a * 1</code>, and the other yields <code>1 * a * 1</code>.</p>
<p>Therefore, we have <code>N-2</code> <code>a * a * a</code>, one <code>a * a * 1</code>, and one <code>1 * a * 1</code>. Adding together, we have <code>(N - 2) * a * a * a + a * a + a</code>.</p>
<p>We can improve the performance sightly by handling those special cases one by one. However, please notice that this optimization does not improve the time complexity and can not speed up too much if the input is highly randomized.</p>
<blockquote>
  <p><strong>Tip: Matrix-Chain Multiplication</strong></p>
  <p>In fact, this problem is a variant of a classical DP problem, Matrix-Chain Multiplication, where we need to find the most efficient way to multiply a given sequence of matrices. The main idea is the same as above: DP, Divide and Conquer, and Thinking Backwards.</p>
  <p>For details of Matrix-Chain Multiplication, check out <a href="https://en.wikipedia.org/wiki/Matrix_chain_multiplication">Wikipedia: Matrix Chain Multiplication</a>.</p>
</blockquote>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Handle the special cases (all numbers are the same) if you want.</p></li>
<li><p>Add one balloon at the start of <code>nums</code> and one at the end to handle edge cases.</p></li>
<li><p>Define a function <code>dp</code> to return the maximum coins obtainable, if we burst all balloons on the interval <code>[left, right]</code>, inclusively.</p>
<p>The base case is that the interval is empty, which yields 0 coin.</p>
<p>For general cases, we iterate over every index <code>i</code> in <code>[left, right]</code>, and mark the balloon at that index as the <strong>last</strong> one burst.</p>
<p>First, We burst all balloons expect the <code>i</code>th one. What we gain is:</p>
<pre><code class="python language-python"> dp(left, i - 1) + dp(i + 1, right)
</code></pre>
<p>Then, we burst the <code>i</code>th one:</p>
<pre><code class="python language-python"> nums[left - 1] * nums[i] * nums[right + 1]
</code></pre>
<p>Just return the maximum sum of those two among all possible <code>i</code>s.</p></li>
<li><p>Finally, return <code>dp(1, len(dp) - 2)</code>.</p>
<p>Do not return <code>dp(0, len(dp) - 1)</code> since the first and the last balloons were added by us and we cannot burst them.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/Y2kysycN/shared" frameborder="0" width="100%" height="500" name="Y2kysycN"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the number of balloons given.</p>
<ul>
<li><p>Time complexity: $$O(N^3)$$. There are $$O(N^2)$$ states. For each state, determining the maximum coins requires iterating over all balloons in the range <code>[left, right]</code>.  Thus the total time complexity is $$O(N^2) \times O(N) = O(N^3)$$.</p></li>
<li><p>Space complexity: $$O(N^2)$$. We need $$O(N^2)$$ to store all states, $$O(N)$$ for stacks to perform recursion, and $$O(N)$$ to store <code>[1] + nums + [1]</code>. In total, this algorithm requires $$O(N^2) + O(N) + O(N) = O(N^2)$$ space.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3dynamicprogrammingbottomup">Approach 3: Dynamic Programming (Bottom-Up)</h4>
<p><strong>Intuition</strong></p>
<p>The intuition is the same as Approach 1. Here, we use DP array and iteration to re-implement Approach 1.</p>
<p>When iterating, we need to carefully arrange the order of iteration, such that <code>dp[left][i - 1]</code> and <code>dp[i + 1][right]</code> are iterated <strong>before</strong> <code>dp[left][right]</code>, where <code>left <= i <= right</code>.</p>
<p>This is important because in order to calculate <code>dp[left][right]</code>, we will use the results of <code>dp[left][i - 1]</code> and <code>dp[i + 1][right]</code>, where <code>left <= i <= right</code>.</p>
<p>But how arrange the order of iteration? Let's take a look at the DP table.</p>
<p>Suppose we have added fake balloons to the beginning and the end of <code>nums</code>, and <code>n</code> is the length of the <strong>new</strong> <code>nums</code> array.</p>
<p>We only need the top-right triangle since we only need <code>dp[left][right]</code> where <code>left</code> will always be less than or equal to <code>right</code>.</p>
<p><img src="https://leetcode.com/articles/Documents/312/312_dp_table.drawio.svg" alt="DP Table" referrerpolicy="no-referrer"></p>
<p>(Here <code>left</code> is for rows and <code>right</code> is for columns, or you can use a transposed one. Either way works.)</p>
<p>Also, we cannot have <code>dp[0][j]</code> and <code>dp[i][n-1]</code>, where <code>0 <= i < n</code> and <code>0 <= j < n</code>, since we cannot burst the fake balloons that we added.</p>
<p><img src="https://leetcode.com/articles/Documents/312/312_dp_table_inner.drawio.svg" alt="DP Table Inner" referrerpolicy="no-referrer"></p>
<p>Okay, now let's consider <code>dp[left][right]</code>. <code>dp[left][i - 1]</code> and <code>dp[i + 1][right]</code> should be iterated before <code>dp[left][right]</code>, where <code>left <= i <= right</code>. Where are they?</p>
<p><img src="https://leetcode.com/articles/Documents/312/312_dp_table_cell.drawio.svg" alt="DP Table Cell" referrerpolicy="no-referrer"></p>
<p>Notice that <code>dp[left][right]</code> depends on the cells directly below it and the cells to its left. If we always iterate from the lowest or the leftmost cell, then we can ensure that <code>dp[left][i - 1]</code> and <code>dp[i + 1][right]</code> are calculated before <code>dp[left][right]</code>.</p>
<p>There are many ways to do that. One possible iteration path is given below.</p>
<p><img src="https://leetcode.com/articles/Documents/312/312_dp_table_iterate.drawio.svg" alt="DP Table Iterate" referrerpolicy="no-referrer"></p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Handle the special cases (all numbers are the same) if you want.</p></li>
<li><p>Add one balloon at the start of <code>nums</code> and one at the end to handle edge cases.</p></li>
<li><p>Define an array <code>dp</code>, where <code>dp[left][right]</code> represents the maximum coins obtainable, if we burst all balloons on the interval <code>[left, right]</code>, inclusively.</p></li>
<li><p>Iterate over the <code>dp</code> array such that <code>dp[left][i - 1]</code> and <code>dp[i + 1][right]</code> are visited before <code>dp[left][right]</code> is visited.
For <code>dp[left][right]</code>:</p>
<p>We iterate over every index <code>i</code> in the range <code>[left, right]</code>, and mark it as the <strong>last</strong> burst balloon.</p>
<p>First, we burst all balloons except the <code>i</code>th balloon. What we gain is:</p>
<pre><code class="python language-python">dp[left][i - 1] + dp[i + 1][right]
</code></pre>
<p>Then, we burst the <code>i</code>th balloon and gain:</p>
<pre><code class="python language-python">nums[left - 1] * nums[i] * nums[right + 1]
</code></pre>
<p>Let <code>dp[left][right]</code> be the maximum sum of these two values among all possible <code>i</code>s.</p></li>
<li><p>Finally, return <code>dp[1][len(nums) - 2]</code>.</p>
<p>Note: Do not return <code>dp[0][len(nums) - 1]</code> because the first and the last balloons were added by us and we cannot be popped.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/JNP6zpza/shared" frameborder="0" width="100%" height="500" name="JNP6zpza"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the number of balloons given.</p>
<ul>
<li><p>Time complexity: $$O(N^3)$$. There are $$O(N^2)$$ states. For each state, determining the maximum coins requires iterating over all balloons in the range <code>[left, right]</code>, giving $$O(N^2) \times O(N) = O(N^3)$$.</p></li>
<li><p>Space complexity: $$O(N^2)$$. We need $$O(N^2)$$ to store <code>dp</code>, and $$O(N)$$ to store <code>[1] + nums + [1]</code> (if fake balloons are added). In total, we need $$O(N^2) + O(N) + O(N) = O(N^2)$$ space.</p></li>
</ul>  
</div>
            