
---
title: '1383. Maximum Performance of a Team'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/1383/1383_example_1.png'
author: LeetCode
comments: false
date: Fri, 30 Apr 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/1383/1383_example_1.png'
---

<div>   
<p>You are given two integers <code>n</code> and <code>k</code> and two integer arrays <code>speed</code> and <code>efficiency</code> both of length <code>n</code>. There are <code>n</code> engineers numbered from <code>1</code> to <code>n</code>. <code>speed[i]</code> and <code>efficiency[i]</code> represent the speed and efficiency of the <code>i<sup>th</sup></code> engineer respectively.</p>

<p>Choose <strong>at most</strong> <code>k</code> different engineers out of the <code>n</code> engineers to form a team with the maximum <strong>performance</strong>.</p>

<p>The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.</p>

<p>Return <em>the maximum performance of this team</em>. Since the answer can be a huge number, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
<strong>Output:</strong> 60
<strong>Explanation:</strong> 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
<strong>Output:</strong> 68
<strong>Explanation:
</strong>This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
<strong>Output:</strong> 72
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= <= k <= n <= 10<sup>5</sup></code></li>
<li><code>speed.length == n</code></li>
<li><code>efficiency.length == n</code></li>
<li><code>1 <= speed[i] <= 10<sup>5</sup></code></li>
<li><code>1 <= efficiency[i] <= 10<sup>8</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>At first glance, the problem might seem to be a combination problem (<em>e.g.</em> <a href="https://leetcode.com/problems/combination-sum-iii/">Combination Sum III</a>), meaning one could enumerate all possible compositions and return the team with the maximum performance based on the given benchmark.</p>
<p>However, while this <strong>brute force</strong> idea is intuitive, it is also inefficient, because the number of combinations grows exponentially with the number of engineers.
In fact, there are some insights that can be derived from the problem, which we can leverage to greatly speed up the algorithm.</p>
<p>In this article, we will introduce a greedy algorithm together with the application of priority queue to solve the problem.</p>
<h2 id="br"><br></h2>
<h4 id="approachgreedywithpriorityqueue">Approach: Greedy with Priority Queue</h4>
<p><strong>Intuition</strong></p>
<blockquote>
  <p>As a reminder, the <strong><em>performance</em></strong> of a team is defined as the <strong>sum</strong> of all members' <strong>speeds</strong> multiplied by the <strong><em>minimum efficiency</em></strong> among the members.</p>
</blockquote>
<p>As one can see, the performance of a team depends on <em><strong>two variables</strong></em>.</p>
<p>To facilitate the enumeration process, let us first <strong>fix</strong> the value of one of the variables, namely the <em>minimum efficiency</em> of the team.</p>
<p>The key idea behind the enumeration process is as follows:</p>
<blockquote>
  <p>For each candidate, we treat him/her as the one who has the <em>minimum efficiency</em> in a team. Then, we select the rest of the team members based on this condition.</p>
</blockquote>
<ul>
<li><p>The above enumeration is <strong>sound</strong>, which means it is guaranteed to find the optimal solution to the problem.
For example, before arriving at a final solution where candidate <em>X</em> has the minimum efficiency on the team, we must have enumerated all potential team compositions that include candidate X.</p></li>
<li><p>Most importantly, the above enumeration helps <strong>prune</strong> some of the unnecessary team compositions. Hence it runs significantly faster.
Starting from a fixed candidate and only accepting new team members that have a higher efficiency than the fixed candidate, allows us to only consider teams of size <code>k</code>, rather than enumerating all teams of size one to <code>k</code>.
This is because once the minimum efficiency of a team is fixed, each new team member is guaranteed to improve the team's performance.
Therefore, we should add as many new members as possible.</p></li>
</ul>
<p>Actually, the above enumeration can be categorized as a <a href="https://en.wikipedia.org/wiki/Greedy_algorithm">Greedy algorithm</a>, where we decompose a problem into a series of stages, and at each stage we make the <strong><em>locally optimal</em></strong> choice.</p>
<p>In our case, we derive the solution through an enumeration process, where at each step we build a <em>locally optimal</em> team by starting from a fixed engineer with the minimum efficiency on the team.
At the end of the enumeration process, we select the maximum among the locally optimal solutions to obtain the <strong>globally optimal</strong> solution.</p>
<p><strong>Algorithm</strong></p>
<p>To see how the above enumeration works, let us walk through some concrete examples.</p>
<p>Suppose that we have a list of 6 engineers with <code>speed = [2,10,3,1,5,8]</code>, <code>efficiency = [5,4,3,9,7,2]</code>, and we are asked to compose a team with at most <code>k=2</code> members.</p>
<p>Here are three steps that demonstrate how we can compose a team with the maximum performance and with <strong><em>at most</em></strong> <code>k</code> members.</p>
<p>1). Let's select the first engineer from the list of candidates as a potential member of the team.
The first engineer has speed of <code>2</code> and an efficiency of <code>5</code>.</p>
<p><em>More importantly, we will impose a condition that all future team members must have an efficiency <strong>greater than or equal to</strong> the first team member.</em></p>
<p><img src="https://leetcode.com/articles/Figures/1383/1383_example_1.png" alt="example step 1" referrerpolicy="no-referrer"></p>
<p>2). Next, we will select the rest of the team members.
We will use the following criteria in order to maximize the performance of the team:</p>
<ul>
<li><p>Each of the selected members should have an efficiency that is at least as high as the engineer that was picked in the first step.</p></li>
<li><p>With the minimum effiency fixed, it will be beneficial to pick as many additional members as possible, up to the maximum quota of <code>k-1</code> members.</p></li>
</ul>
<p>With the first candidate fixed as a member of the team, we need to select at most one more member for the team. We are limited to at most one more member because <code>k-1 = 2-1 = 1</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/1383/1383_example_2.png" alt="example step 2" referrerpolicy="no-referrer"></p>
<p>According to the criteria listed above, in order to <strong><em>maximize</em></strong> the performance of the team, we should invite the fifth candidate to join the team. Here is the rationale.
Both the <em>fourth</em> and <em>fifth</em> candidates have a higher efficiency than the first candidate.
Therefore, both of them are eligible to join the team.
However, since the fifth candidate is faster than the fourth candidate, it is <strong><em>optimal</em></strong> to choose the fifth candidate in order to maximize the total speed of the team, and therefore maximize the performance of the team.</p>
<p>3). We repeat the above two steps for each of the remaining candidates.
At the end of the enumeration process, we will discover that the team composition with the second candidate as the one with the minimum efficiency will emerge as the one with the <em>maximum</em> performance.</p>
<p><img src="https://leetcode.com/articles/Figures/1383/1383_example_3.png" alt="example step 3" referrerpolicy="no-referrer"></p>
<p><strong>Implementation</strong></p>
<p>The most complex step in the algorithm is the second step.  In the second step, we have selected a member who will have the lowest efficiency in the team, and we must determine <strong><em>how</em></strong> to construct the rest of the team.
We can answer this question, by breaking it down into two tasks:</p>
<ul>
<li><p>First of all, given a fixed member, we must <strong>find</strong> all eligible candidates (at most <code>k-1</code> members) whose efficiencies are higher than the fixed member's efficiency.</p>
<ul>
<li><p>To achieve this task, we could <strong><em>sort</em></strong> the candidates, in descending order, based on <em>efficiency</em>.</p></li>
<li><p>We then iterate through the sorted candidates. For each candidate, we only need to consider the earlier candidates. Since the list is sorted, only the earlier candidates will have a higher efficiency than the current candidate.</p></li></ul></li>
<li><p>Given all the eligible candidates, in order to maximize the total speed, we need to <strong>find</strong> the <strong>fastest</strong> <code>k-1</code> eligible candidates.</p>
<ul>
<li><p>To achieve this task, we can <strong><em>sort</em></strong> the candidates again. But this time, we sort only the earlier candidates, and most importantly we sort by <em>speed</em> rather than efficiency.</p></li>
<li><p>The sorting idea is a valid one. However, a more efficient option would be to apply the <a href="https://en.wikipedia.org/wiki/Priority_queue">Priority Queue</a> data structure here.
The priority queue, also known as <strong><em>heap</em></strong>, is a data structure which <em>dynamically</em> maintains the order of elements based on some predefined <em>priority</em>.
The priority queue is well-known for its optimized time complexity when maintaining a list of sorted elements.
As such, we will we opt to use a priority queue in the following implementation.</p></li></ul></li>
</ul>
<p><img src="https://leetcode.com/articles/Figures/1383/1383_algorithm.png" alt="algorithm" referrerpolicy="no-referrer"></p>
<p>To recap, we will build a <strong>greedy</strong> algorithm that utilizes the <strong>priority queue</strong> data structure. Here are the steps in detail.</p>
<ul>
<li><p>First of all, let's sort the candidates by efficiency in descending order.</p></li>
<li><p>Then, we will iterate through the sorted candidates.</p></li>
<li><p>At each iteration, our goal is to construct a team with at most <code>k</code> members, while treating the current candidate as the one with the lowest efficiency on the team.</p></li>
<li><p>We use a priority queue to store the speeds for the rest <code>k-1</code> team members.
The priority queue is maintained as a <strong>sliding window</strong> along with our iteration.  For example, we pop out the member with the lowest speed when we exceed the predefined capacity of the queue, which is <code>k-1</code>.</p></li>
</ul>
<iframe src="https://leetcode.com/playground/EEvxmpYV/shared" frameborder="0" width="100%" height="500" name="EEvxmpYV"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the total number of candidates, and $$K$$ be the size of the team.</p>
<ul>
<li><p>Time Complexity: $$O\big(N \cdot (\log N + \log K)\big)$$</p>
<ul>
<li><p>First of all, we build a list of candidates from the inputs, which takes $$O(N)$$ time.</p></li>
<li><p>We then sort the candidates, which takes $$O(N \log N)$$ time.</p></li>
<li><p>We iterate through the sorted candidates. At each iteration, we will perform at most two operations on the priority queue: one push and one pop.
Each operation takes $$O\big(\log (K-1) \big)$$ time, where $$K-1$$ is the capacity of the queue.
To sum up, the time complexity of this iteration will be $$O\big(N \cdot \log (K-1)\big) = O(N \cdot \log K)$$.</p></li>
<li><p>Thus, the overall time complexity of the algorithm will be $$O\big(N \cdot (\log N + \log K)\big)$$.</p></li></ul></li>
<li><p>Space Complexity: $$O(N + K)$$</p>
<ul>
<li><p>We build a list of candidates from the inputs, which takes $$O(N)$$ space.</p></li>
<li><p>We also use the priority queue data structure whose space capacity is $$O(K-1)$$.</p></li>
<li><p>Note that we use sorting in the algorithm, and the space complexity of the sorting algorithm depends on the implementation of each programming language.
For instance, the <code>sorted()</code> function in Python is implemented with the <a href="https://en.wikipedia.org/wiki/Timsort">Timsort</a> algorithm whose space complexity is $$\mathcal&#123;O&#125;(N)$$.
While in Java, the <a href="https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#sort-byte:A-">Collections.sort()</a> is implemented as a variant of the quicksort algorithm whose space complexity is $$\mathcal&#123;O&#125;(\log&#123;N&#125;)$$.</p></li>
<li><p>To sum up, the overall space complexity of the entire algorithm is $$O(N + K)$$.</p></li></ul></li>
</ul>
<h2 id="br-1"><br></h2>  
</div>
            