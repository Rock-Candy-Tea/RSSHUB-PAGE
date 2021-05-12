
---
title: '746. Min Cost Climbing Stairs'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/746/746_1.png'
author: LeetCode
comments: false
date: Wed, 28 Apr 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/746/746_1.png'
---

<div>   
<p>You are given an integer array <code>cost</code> where <code>cost[i]</code> is the cost of <code>i<sup>th</sup></code> step on a staircase. Once you pay the cost, you can either climb one or two steps.</p>

<p>You can either start from the step with index <code>0</code>, or the step with index <code>1</code>.</p>

<p>Return <em>the minimum cost to reach the top of the floor</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> cost = [10,15,20]
<strong>Output:</strong> 15
<strong>Explanation:</strong> Cheapest is: start on cost[1], pay that cost, and go to the top.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> cost = [1,100,1,1,1,100,1,1,100,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>2 <= cost.length <= 1000</code></li>
<li><code>0 <= cost[i] <= 999</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>We can make two important observations about this problem. First, we need to find the maximum or minimum of something. Second, we have to make decisions that might look different depending on decisions we made previously. These characteristics are typical of a dynamic programming problem. In this case, we need to make decisions about either taking 1 step or 2 steps at a time, and our goal is to minimize the overall cost. </p>
<p>If you're new to dynamic programming, this question may seem more like a medium. Don't worry though, this is a great problem for getting started with dynamic programming. Generally, there are two main ways to implement a dynamic programming algorithm - top-down and bottom-up. In this article, we will take a look at both.</p>
<p>Before we begin, let's clear up some of the confusion surrounding the problem statement. <br></p>
<p><img src="https://leetcode.com/articles/Figures/746/746_1.png" width="960" referrerpolicy="no-referrer"> <br></p>
<p>The "top of the floor" does not refer to the final index of <code>costs</code>. We actually need to "arrive" beyond the array's bounds.</p>
<p><br></p>
<hr>
<h4 id="approach1bottomupdynamicprogrammingtabulation">Approach 1: Bottom-Up Dynamic Programming (Tabulation)</h4>
<p><strong>Intuition</strong></p>
<p>Bottom-up dynamic programming is also known as <strong>tabulation</strong> and is done iteratively. Dynamic programming is based on the concept of <strong>overlapping subproblems</strong> and <strong>optimal substructure</strong>. This is when the solution to a problem can be constructed from solutions to similar and smaller subproblems. Solving a smaller version of the problem can be easier and faster, thus if we break up the problem into smaller subproblems, solving them can lead us to the final solution easier and faster.</p>
<p>Let's look at an example <code>costs = [0,1,2,3,4,5]</code>. Since we can take 1 or 2 steps at a time, we need to reach either step 4 or step 5 (0-indexed), and then pay the respective cost to reach the top. For this example, to reach step 4 optimally would cost <strong>2</strong> by taking path <code>0 --> 2 --> 4</code> (we're not counting the cost of step 4 yet since we are only talking about <em>reaching</em> the step right now). To reach step 5 optimally would cost <strong>4</strong> by taking path <code>1 --> 3 --> 5</code>.</p>
<p>Now, imagine that before we started the problem, somebody came up to us and said "to optimally reach step 4 costs <strong>2</strong> and to optimally reach step 5 costs <strong>4</strong>." Well, then the problem is trivial - the answer is the minimum of <code>2 + cost[4] = 6</code> and <code>4 + cost[5] = 9</code>. The only reason this was so easy was because we already knew the cost to reach steps 4 and 5.</p>
<p>So how do we find the minimum cost to reach step 4 or step 5? Well, you might notice that it's the exact same problem, just with a smaller input. For example, finding the minimum cost to reach step 4 is like solving the original problem with input <code>[0,1,2,3]</code> (step 4 is the "top of the floor" now). To solve this subproblem, we need to find the minimum cost to reach steps 2 and 3, which requires us to answer the original problem for inputs <code>[0,1]</code> and <code>[0,1,2]</code>.</p>
<p>This pattern is known as a <strong>recurrence relation</strong>, and in this case, the minimum cost to reach the $$i^&#123;th&#125;$$ step is equal to <code>minimumCost[i] = min(minimumCost[i - 1] + cost[i - 1], minimumCost[i - 2] + cost[i - 2])</code>. As you can see, we get the solution for the $$i^&#123;th&#125;$$ step by using solutions from earlier steps. So, when does the sequence terminate? For this question, the base cases are given in the problem description - we are allowed to start at either step 0 or step 1, so <code>minimumCost[0]</code> and <code>minimumCost[1]</code> are both <code>0</code>.</p>
<p><strong>Algorithm</strong></p>
<p>With our base cases and recurrence relation, we can now easily solve this problem.</p>
<ol>
<li><p>Define an array <code>minimumCost</code>, where <code>minimumCost[i]</code> represents the minimum cost of reaching the $$i^&#123;th&#125;$$ step. The array should be one element longer than <code>costs</code> and start with all elements set to <code>0</code>.</p>
<ul>
<li>The reason the array should contain one additional element is because we will treat the <em>top floor</em> as the <em>step</em> to reach.</li></ul></li>
<li><p>Iterate over the array starting at the 2nd index. The problem statement says we are allowed to start at the $$0^&#123;th&#125;$$ or $$1^&#123;st&#125;$$ step, so we know the minimum cost to reach those steps is <code>0</code>.</p></li>
<li><p>For each step, apply the recurrence relation - <code>minimumCost[i] = min(minimumCost[i - 1] + cost[i - 1], minimumCost[i - 2] + cost[i - 2])</code>. As you can see, as we populate <code>minimumCost</code>, it becomes possible to solve future subproblems. For example, before solving the 5th and 6th steps we are required to solve the 4th step.</p></li>
<li><p>At the end, return the final element of <code>minimumCost</code>. Remember, we are treating this "step" as the top floor that we need to reach.</p></li>
</ol>
<p>Here's an animation that shows how and why this algorithm works:</p>
<p>!?!../Documents/746<em>Min</em>Cost_Stairs.json:960,540!?!</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/Fpv7YmHx/shared" frameborder="0" width="100%" height="361" name="Fpv7YmHx"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the length of <code>cost</code>,</p>
<ul>
<li><p>Time complexity: $$O(N)$$.</p>
<p>We iterate <code>N - 1</code> times, and at each iteration we apply an equation that requires $$O(1)$$ time.</p></li>
<li><p>Space complexity: $$O(N)$$.</p>
<p>The array <code>minimumCost</code> is always 1 element longer than the array <code>cost</code>.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2topdowndynamicprogrammingrecursionmemoization">Approach 2: Top-Down Dynamic Programming (Recursion + Memoization)</h4>
<p><strong>Intuition</strong></p>
<p>Bottom-up dynamic programming is named as such because we start from the bottom (in this case, the bottom of the staircase) and iteratively work our way to the top. Top-down dynamic programming starts at the top and works its way down to the base cases. Typically, this is implemented through recursion, and then made efficient using <em>memoization</em>. Memoization refers to storing the results of expensive function calls in order to avoid duplicate computations - we'll soon see why this is important for this problem. If you're new to recursion, check out the <a href="https://leetcode.com/explore/featured/card/recursion-i/">recursion explore card</a>.</p>
<p>Similar to the first approach, we will make use of the recurrence relation we found. This time, we will implement <code>minimumCost</code> as a function instead of an array. Again, <code>minimumCost(i)</code> will represent the minimum cost to reach the $$i^&#123;th&#125;$$ step. The base cases for this function will be <code>minimumCost(0) = minimumCost(1) = 0</code>, since we are allowed to start on either step 0 or step 1. For any other step <code>i</code>, we can refer to our recurrence relation - we know <code>minimumCost(i) = min(cost[i - 1] + minimumCost(i - 1), cost[i - 2] + minimumCost(i - 2))</code>.</p>
<p>We can implement this function easily enough, but there's a major problem - repeated computations. If we want to find <code>minimumCost(5)</code>, then we call <code>minimumCost(3)</code> and <code>minimumCost(4)</code>. However, <code>minimumCost(4)</code> will then call <code>minimumCost(3)</code>, and both <code>minimumCost(3)</code> calls will call <code>minimumCost(2)</code>, on top of another <code>minimumCost(2)</code> call from <code>minimumCost(4)</code>. <br></p>
<p><img src="https://leetcode.com/articles/Figures/746/746_1b.png" width="960" referrerpolicy="no-referrer"> <br></p>
<p>As you can see, there are a ton of repeat computations. When there are only 5 stairs, it might not seem that bad. However, imagine if there were 6 stairs instead. This entire image would be one child of the root. As <code>n</code> increases, the amount of computations required grows exponentially. So, how do we resolve this issue? If we calculate, say, <code>minimumCost(3)</code>, then why should we calculate it again? Instead of going through the entire subtree every time we want to calculate <code>minimumCost(3)</code>, let's just store the value of <code>minimumCost(3)</code> after calculating it the first time, and refer to that instead.</p>
<p>This is what memoization is - caching "expensive" function calls to avoid duplicate computations. Imagine what the recursion tree would look like for a call to <code>minimumCost(10000)</code>, and how expensive calls like <code>minimumCost(9998)</code> would be to compute multiple times. We can use a hash map for the memoization, where each key will have the value <code>minimumCost(key)</code>.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Define a hash map <code>memo</code>, where <code>memo[i]</code> represents the minimum cost of reaching the $$i^&#123;th&#125;$$ step.</p></li>
<li><p>Define a function <code>minimumCost</code>, where <code>minimumCost(i)</code> will determine the minimum cost to reach the $$i^&#123;th&#125;$$ step. </p></li>
<li><p>In our function <code>minimumCost</code>, first check the base cases: <code>return 0</code> when <code>i == 0</code> or <code>i == 1</code>. Next, check if the argument <code>i</code> has already been calculated and stored in our hash map <code>memo</code>. If so, <code>return memo[i]</code>. Otherwise, use the recurrence relation to calculate <code>memo[i]</code>, and then return <code>memo[i]</code>.</p></li>
<li><p>Simply call and return <code>minimumCost(cost.length)</code>. Once again, we can make use of the trick from approach 1 where we treat the top floor as an extra "step". Since <code>cost</code> is 0-indexed, <code>cost.length</code> will be an index 1 step above the last element of <code>cost</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/9jYfvFfe/shared" frameborder="0" width="100%" height="480" name="9jYfvFfe"></iframe>
<p><strong>Extra Notes</strong></p>
<p>For this approach, we are using hash maps as our data structure to memoize function calls. We could also use an array since the calls to <code>minimumCost</code> are very well defined (between 0 and <code>cost.length + 1</code>). However, a hash map is used for most top-down dynamic programming solutions, as there will often be multiple function arguments, the arguments will not be integers, or a variety of other reasons that require a hash map instead of an array. Although using an array is slightly more efficient, using a hash map here is good practice that can be applied to other problems.</p>
<p>In Python, the <a href="https://docs.python.org/3/library/functools.html">functools</a> module contains functions that can be used to automatically memoize a function. In LeetCode, modules are automatically imported, so you can just add the <code>@cache</code> wrapper to any function definition to have it automatically memoize.</p>
<iframe src="https://leetcode.com/playground/j2J8QMdT/shared" frameborder="0" width="100%" height="259" name="j2J8QMdT"></iframe>
<p>You can observe that by removing the @cache wrapper, on attempted submission, the code will exceed the time limit.</p>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the length of <code>cost</code>,</p>
<ul>
<li><p>Time complexity: $$O(N)$$</p>
<p><code>minimumCost</code> gets called with each index from <code>0</code> to <code>N</code>. Because of our memoization, each call will only take $$O(1)$$ time.</p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>The extra space used by this algorithm is the recursion call stack. For example, <code>minimumCost(1000)</code> will call <code>minimumCost(9999)</code>, which calls <code>minimumCost(9998)</code> etc., all the way down until the base cases at <code>minimumCost(0)</code> and <code>minimumCost(1)</code>. In addition, our hash map <code>memo</code> will be of size <code>N</code> at the end, since we populate it with every index from <code>0</code> to <code>N</code>.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3bottomupconstantspace">Approach 3: Bottom-Up, Constant Space</h4>
<p><strong>Intuition</strong></p>
<p>You may have noticed that our recurrence relation from the previous two approaches only cares about 2 steps below the current step. For example, if we are calculating the minimum cost to reach step 12, we only care about data from step 10 and step 11. While we would have needed to calculate the minimum cost for steps 2-9 as well, at the time of the actual calculation for step 12, we no longer care about any of those steps.</p>
<p>Therefore, instead of using $$O(n)$$ space to keep an array, we can improve to $$O(1)$$ space using only two variables.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize two variables, <code>downOne</code> and <code>downTwo</code>, that represent the minimum cost to reach one step and two steps below the current step, respectively. We will start iteration from step 2, which means these variables will initially represent the minimum cost to reach steps 0 and 1, so we will initialize each of them to 0.</p></li>
<li><p>Iterate over the array, again with 1 extra iteration at the end to treat the top floor as the final "step". At each iteration, simulate moving 1 step up. This means <code>downOne</code> will now refer to the current step, so apply our recurrence relation to update <code>downOne</code>. <code>downTwo</code> will be whatever <code>downOne</code> was prior to the update, so let's use a temporary variable to help with the update.</p></li>
<li><p>In the end, since we treated the top floor as a <em>step</em>, <code>downOne</code> will refer to the minimum cost to reach the top floor. Return <code>downOne</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/VsgXp8xP/shared" frameborder="0" width="100%" height="276" name="VsgXp8xP"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the length of <code>cost</code>,</p>
<ul>
<li><p>Time complexity: $$O(N)$$.</p>
<p>We only iterate <code>N - 1</code> times, and at each iteration we apply an equation that uses $$O(1)$$ time.</p></li>
<li><p>Space complexity: $$O(1)$$</p>
<p>The only extra space we use is 2 variables, which are independent of input size.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="closingnotes">Closing Notes</h4>
<p>If you're new to dynamic programming, hopefully you learned something from this article. Please post any questions you may have in the comment section below. For additional practice, here's a list of similar dynamic programming questions that are good for beginners.</p>
<p><a href="https://leetcode.com/problems/climbing-stairs/">70. Climbing Stairs (Easy)</a></p>
<p><a href="https://leetcode.com/problems/house-robber/">198. House Robber (Medium)</a></p>
<p><a href="https://leetcode.com/problems/paint-house/">256. Paint House (Medium)</a></p>
<p><a href="https://leetcode.com/problems/fibonacci-number/">509. Fibonacci Number (Easy)</a></p>
<p><a href="https://leetcode.com/problems/minimum-falling-path-sum/">931. Minimum Falling Path Sum (Medium)</a></p>
<hr>  
</div>
            