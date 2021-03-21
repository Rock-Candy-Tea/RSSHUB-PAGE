
---
title: 198. House Robber
categories: 
    - 编程
    - LeetCode - 文章
author: LeetCode - 文章
comments: false
date: Wed, 17 Mar 2021 00:00:00 GMT
thumbnail: https://leetcode.com/articles/Figures/198/img1.png
---

<div>   
<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and <b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <b>without alerting the police</b></em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [2,7,9,3,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= nums.length <= 100</code></li>
<li><code>0 <= nums[i] <= 400</code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>Our professional robber is in for a treat! They have a buffet of houses available for them to rob. Technically, they can rob any of the houses on the street. However, the alarm companies are smart enough to catch any robber red-handed under certain conditions. If there were no alarms in the houses, obviously the robber would rob every house and make the most money. </p>
<p>However, now they have a lot of choices to make. Let's look at a few houses on the street, the different choices our robber can make, and how those choices will affect the heist.</p>
<p><img src="https://leetcode.com/articles/Figures/198/img1.png" alt="robber example optimal" referrerpolicy="no-referrer">
{:align="center"}</p>
<p><em>Figure 1. An example showing the robber making the optimal choices to obtain the most money.</em>
{:align="center"}</p>
<p>In this example, the robber ended up making 600 which is the maximum they can make for this series of houses. Let's take another set of choices that the robber can make where they will not make the maximum amount.</p>
<p><img src="https://leetcode.com/articles/Figures/198/img2.png" alt="robber example not so optimal" referrerpolicy="no-referrer">
{:align="center"}</p>
<p><em>Figure 2. The same example showing the robber making sub-optimal choices.</em>
{:align="center"}</p>
<p>In this case, the series of choices that the robber made turned out to be less than optimal and they ended up making a paltry 250.</p>
<blockquote>
  <p>A series of choices essentially gives us a subset of houses from the original list. We need to make these choices in such a way that the overall profit is maximized.</p>
</blockquote>
<p>There is no <em>greedy</em> way of deciding if the robber should rob a house or not. The best greedy strategy may be to check the neighboring houses and only rob a house if it gives them more money than the neighbors combined. That might be a sound greedy strategy. However, by doing so, the robber may miss out on making the maximum profit. Let's look at an example for that.</p>
<p><img src="https://leetcode.com/articles/Figures/198/img3.png" alt="robber greedy choice doesn't work" referrerpolicy="no-referrer">
{:align="center"}</p>
<p><em>Figure 3. Depicting the failure of a greedy strategy on the same example.</em>
{:align="center"}</p>
<p>In this example, you could argue that after the robber decided to rob the 3rd house, they could go back and rob the first one as well. In this case, that will give us the optimal answer. However, that decision is still <strong>local</strong> in that we just consider 3 houses at a time.  </p>
<blockquote>
  <p>What we need is to try all the possibilities and see which one gives us (the robber) the optimal loot.</p>
</blockquote>
<p><br></p>
<hr>
<h4 id="approach1recursionwithmemoization">Approach 1: Recursion with Memoization</h4>
<p><strong>Intuition</strong></p>
<p>As we mentioned above, the easiest approach here is to try <em>all</em> possible combinations of house choices and then use the combination that gives the maximum amount of money to the robber. We do this because there is no plausible greedy strategy that we can use to decide if the robber should rob a particular house or not.</p>
<p>We rely on our good friend recursion whenever we have <em>choices</em> involved in solving a problem. Technically, a robber can come back and rob a house that they previously rejected. However, since we are trying <em>all</em> options, we will not go back and rob an unrobbed house since that scenario will be covered in a different recursive path.</p>
<blockquote>
  <p>The basic choice that we make is whether to rob the current house or not. If the robber decides to rob the current house, they have to skip the next house. Otherwise, they can evaluate the same choice on the next house i.e. to rob or not to rob.</p>
</blockquote>
<p><strong>Subproblems</strong></p>
<p>To approach a problem recursively, we need to make sure that it can be broken down into sub-problems. Additionally, we need to ensure that the optimal solution to these sub-problems can be used to form the solution to the main problem. Let's see how we can divide this problem into smaller recursive problems.</p>
<p>Let's say that we have a function called <code>robFrom</code> which we will use to solve this problem. The only input this function takes is an index, <code>position</code>. This <code>position</code> essentially represents a <em>suffix in the array which we, the robber, have yet to scan</em>. Essentially, the <code>position</code> indicates that the robber has yet to scan houses $$[\text{position}, \cdots, N]$$ where $$N$$ represents the total number of houses.</p>
<p>Naturally, the answer to our problem would be the function call <code>robFrom(0)</code> which means scan all the houses and return the maximum profit. Now let's think about <code>robFrom(i)</code> for a moment. This simply represents a sub-array or a suffix from the main array. We can think about this as a smaller max-profit problem in itself, can't we?</p>
<blockquote>
  <p>A suffix of the initial set of houses simply means a smaller set of houses that the robber has to consider. We will be working with the assumption that in the function call <strong>robFrom(i)</strong>, the robber has to maximize their profit from i..N houses.</p>
</blockquote>
<p>At each step, the robber has two options. If he chooses to rob the current house, he will have to skip the next house on the list by moving two steps forward. If he chooses not to rob the current house, he can simply move on to the next house in the list. Let's see this mathematically. </p>
<p>$$
\text{robFrom}(i) = \text{max}(\text{robFrom}(i + 1), \text{robFrom}(i + 2) + \text{nums}(i))
$$</p>
<p><strong>Recursion tree and memoization</strong></p>
<p>Now that we have an idea about the recursive structure of our problem, let's look at the recursion tree which will be formed. This is important so that we can determine if we have repeating sub-problems, in which case we can use memoization or caching to reduce the overall solution complexity.</p>
<p><img src="https://leetcode.com/articles/Figures/198/img4.png" alt="overlapping subproblems in the recursion tree" referrerpolicy="no-referrer">
{:align="center"}</p>
<p><em>Figure 4. Overlapping sub-problems in the recursion tree.</em>
{:align="center"}</p>
<p>As we can see in the recursion tree above, we have the repeating sub-problems (nodes) marked in the same color. A repeating node in the tree represents an entire subtree calculation that has to be repeated which is computationally expensive. Hence, we cache the already computed results so that we don't need to re-calculate the maximum profit for previously seen sub-problems.</p>
<p>Let's formalize this idea concretely in the algorithm section below.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>We define a function called <code>robFrom()</code> which takes the index of the house that the robber currently has to examine. Also, this function takes the <code>nums</code> array which is required during the calculations.</li>
<li>At each step of our recursive call, the robber has two options. He can either rob the current house or not.</li>
<li>If the robber chooses to rob the current house, then he have to skip the next house i.e <code>robFrom(i + 2, nums)</code>. The answer here would be whatever is returned by <code>robFrom(i + 2, nums)</code> in addition to the amount that the robber will get by robbing the current house i.e. <code>nums[i]</code>.</li>
<li>Otherwise, he can simply move on to the house next door and return whatever profit he will make in the sub-problem i.e. <code>robFrom(i + 1, nums)</code>.</li>
<li>We need to find, cache, and return the maximum of these two options at each step.</li>
<li><code>robFrom(0, nums)</code> will give us the answer to the entire problem.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/UQRs4fvP/shared" frameborder="0" width="100%" height="500" name="UQRs4fvP"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity: $$O(N)$$ since we process at most $$N$$ recursive calls, thanks to caching, and during each of these calls, we make an $$O(1)$$ computation which is simply making two other recursive calls, finding their maximum, and populating the cache based on that.</p></li>
<li><p>Space Complexity: $$O(N)$$ which is occupied by the cache and also by the recursion stack.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2dynamicprogramming">Approach 2: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>The idea here is the same as before except that instead of following a recursive approach, we will be sticking with a tabular approach. The recursive approach may run into trouble when the recursion stack grows too large.  It may also run into trouble because, for each recursive call, the compiler must do additional work to maintain the call stack (function variables, etc.) which results in unwanted overhead. The dynamic programming approach is simply a tabular formulation of the ideas presented above.</p>
<p>The cache we had before will still exist in this approach but instead of calling it a cache, we will refer to it as our dynamic programming table. Every DP solution has a table that we populate starting with the base case or the simplest of cases for which we already know the answer. E.g. for our problem, we know that in the absence of houses, the robber will make <code>0</code> profit. Similarly, if there is just one house left to rob, the robber will rob that house, and that will be the maximum profit. </p>
<p>We start by populating the dynamic programming table with these initial values and then build the table in a <em>bottom-up fashion</em> which is the essence of this solution. Let's look at the algorithm to formalize this idea.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>We define a table which we will use to store the results of our sub-problems. Let's call this table <code>maxRobbedAmount</code> where <code>maxRobbedAmount[i]</code> is the same value that would be returned by <code>recurse(i)</code> in the previous solution.</li>
<li>We set <code>maxRobbedAmount[N]</code> to <code>0</code> since this means the robber doesn't have any houses left to rob, thus zero profit. Additionally, we set <code>maxRobbedAmount[N - 1]</code> to <code>nums[N - 1]</code> because in this case, there is only one house to rob which is the last house. Robbing it will yield the maximum profit.</li>
<li>We iterate from <code>N - 2</code> down to <code>0</code> and we set <code>maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])</code>. Note that this is the same as the recursive formulation in the previous solution. The only difference is that we have <em>already calculated the solutions to the sub-problems and we simply reuse the solutions in O(1) time when calculating the solution to the main problem</em>.</li>
<li>We return the value in <code>maxRobbedAmount[0]</code>.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/Pbi5J5cH/shared" frameborder="0" width="100%" height="500" name="Pbi5J5cH"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity: $$O(N)$$ since we have a loop from $$N - 2 \cdots 0$$ and we simply use the pre-calculated values of our dynamic programming table for calculating the current value in the table which is a constant time operation.</p></li>
<li><p>Space Complexity: $$O(N)$$ which is used by the table. So what is the real advantage of this solution over the previous solution? In this case, we don't have a recursion stack.  When the number of houses is large, a recursion stack can become a serious limitation, because the recursion stack size will be huge and the compiler will eventually run into <code>stack-overflow problems</code> (no pun intended!).</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3optimizeddynamicprogramming">Approach 3: Optimized Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>This is the exact same solution as the previous one with the exception that we will be optimizing the space complexity here. Let's look at the recursive relation again to see where we can reduce the amount of space used.</p>
<p>$$
\text{robFrom}(i) = \text{max}(\text{robFrom}(i + 1), \text{robFrom}(i + 2) + \text{nums}(i))
$$</p>
<blockquote>
  <p>To calculate the current value, we just need to rely on the next two consecutive values/recursive calls.</p>
</blockquote>
<p>Porting this idea over to our dynamic programming solution we see that in order to calculate the value at a current index in the dynamic programming table, we simply need to know the next two values i.e. <code>maxRobbedAmount[i + 1]</code> and <code>maxRobbedAmount[i + 2]</code>. In the end we will return the value of <code>maxRobbedAmount[0]</code>. </p>
<blockquote>
  <p>Instead of keeping an entire table for storing these cached values, we can get by with simply keeping track of the "next" two values.</p>
</blockquote>
<p>Let's see this more concretely in the algorithm section.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>We will make use of two variables here called <code>robNext</code> and <code>robNextPlusOne</code> which at any point will represent the optimal solution for <code>maxRobbedAmount[i + 1]</code> and <code>maxRobbedAmount[i + 2]</code>.  These are the two values that we need to calculate the current value.</p></li>
<li><p>We set <code>robNextPlusOne</code> to <code>0</code> since this means the robber doesn't have any houses left to rob, thus zero profit. Additionally, we set <code>robNext</code> to <code>nums[N - 1]</code> because in this case there is only one house to rob which is the last house. Robbing it will yield the maximum profit. </p>
<p><strong>Note</strong> We are assuming that <code>robNextPlusOne</code> is the value of <code>maxRobbedAmount[N]</code> and <code>robNext</code> is <code>maxRobbedAmount[N-1]</code> initially.</p></li>
<li><p>We iterate from <code>N - 2</code> down to <code>0</code> and set <code>current = max(robNext, robNextPlusOne + nums[i])</code>. Note that this is the same as the dynamic programming solution except that we are making use of our variables and not entries from the table.</p></li>
<li><p>Set <code>robNextPlusOne = robNext</code>.</p></li>
<li><p>Set <code>robNext = current</code>. Updating the two variables is important as we iterate down to <code>0</code>.</p></li>
<li><p>We return the value in <code>robNext</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/2DwYPSTt/shared" frameborder="0" width="100%" height="500" name="2DwYPSTt"></iframe>
<p><strong>Time Complexity</strong></p>
<ul>
<li><p>Time Complexity: $$O(N)$$ since we have a loop from $$N - 2 \cdots 0$$ and we use the precalculated values of our dynamic programming table to calculate the current value in the table which is a constant time operation.</p></li>
<li><p>Space Complexity: $$O(1)$$ since we are not using a table to store our values. Simply using two variables will suffice for our calculations.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            