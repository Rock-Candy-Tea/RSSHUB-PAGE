
---
title: '1335. Minimum Difficulty of a Job Schedule'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2020/01/16/untitled.png'
author: LeetCode
comments: false
date: Tue, 02 Aug 2022 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2020/01/16/untitled.png'
---

<div>   
<p>You want to schedule a list of jobs in <code>d</code> days. Jobs are dependent (i.e To work on the <code>i<sup>th</sup></code> job, you have to finish all the jobs <code>j</code> where <code>0 <= j < i</code>).</p>

<p>You have to finish <strong>at least</strong> one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the <code>d</code> days. The difficulty of a day is the maximum difficulty of a job done on that day.</p>

<p>You are given an integer array <code>jobDifficulty</code> and an integer <code>d</code>. The difficulty of the <code>i<sup>th</sup></code> job is <code>jobDifficulty[i]</code>.</p>

<p>Return <em>the minimum difficulty of a job schedule</em>. If you cannot find a schedule for the jobs return <code>-1</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<img alt src="https://assets.leetcode.com/uploads/2020/01/16/untitled.png" style="width: 365px; height: 370px;" referrerpolicy="no-referrer">
<pre><strong>Input:</strong> jobDifficulty = [6,5,4,3,2,1], d = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> jobDifficulty = [9,9,9], d = 4
<strong>Output:</strong> -1
<strong>Explanation:</strong> If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> jobDifficulty = [1,1,1], d = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The schedule is one job per day. total difficulty will be 3.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= jobDifficulty.length <= 300</code></li>
<li><code>0 <= jobDifficulty[i] <= 1000</code></li>
<li><code>1 <= d <= 10</code></li>
</ul><p>[TOC]</p>
<h4 id="overview">Overview</h4>
<p>In this question, we want to distribute <code>n</code> jobs across <code>d</code> days in a way that minimizes the difficulty of the job schedule. The difficulty of a job schedule is the sum of the maximum difficulty job for each day and every day must have at least one job. Whenever you need to search for the most efficient way to distribute <code>n</code> items, brute force is always an option. Typically, brute force solutions are very slow, but they serve as a good starting point that can be optimized later. The brute force solution to this problem is to generate all valid ways to distribute the <code>n</code> jobs across <code>d</code> days, and then calculate the minimum job difficulty of each way.</p>
<p>How many possible valid ways are there to distribute the jobs? Without thinking about the implementation details, we can abstract the question into inserting <code>d - 1</code> boards to divide <code>n</code> balls into <code>d</code> piles, which is a classic problem in permutations and combinations.</p>
<p>Let's illustrate the scenario using Example 4 (<code>jobDifficulty = [7,1,7,1,7,1], d = 3</code>).
<img src="https://leetcode.com/articles/Figures/1335/1335_1BruteForce.JPG" alt="separate n job into d days" referrerpolicy="no-referrer"></p>
<p>How do we code the brute force solution? Depth-first search (DFS) is a reasonable option because it is guaranteed to explore every possible sequence of states that results in scheduling all jobs in <code>d</code> days. Each state is a different combination of the starting index in the <code>jobDifficulty</code> array, and the number of days remaining. Thus, a job schedule is a valid sequence of <code>d</code> states that schedules all jobs and at least one job per day.  The output will be the minimum difficulty among all valid job schedules.</p>
<p>In this example, we want to get the result for <code>min_diff(0, 3)</code>, which represents the minimum job difficulty when starting from the $$0^&#123;th&#125;$$ index with 3 days remaining. Refer to the top panel of the image below to see the backtracking process.
Each edge signifies how the state from a top row can be derived from the state in a bottom row. For instance, the edge connecting <code>dp(0,3)</code> and <code>dp(1,2)</code> means the state <code>min_diff(0, 3)</code> (starting from the $$0^&#123;th&#125;$$ index with 3 days remaining) can be derived from <code>min_diff(1, 2)</code> (starting from the $$1^&#123;st&#125;$$ index with 2 days remaining, if only the $$0^&#123;th&#125;$$ job is performed on that day). Notice that some states, <code>min_diff(5, 1)</code> for instance, were calculated many times. Therefore, to improve the time complexity, we can use memoization to avoid such repeated calculations. Adding memoization to DFS is an example of dynamic programming and is illustrated in the bottom panel of the image below.</p>
<p><img src="https://leetcode.com/articles/Figures/1335/1335_2DFS_to_dp.JPG" alt="dfs to dp" referrerpolicy="no-referrer"></p>
<p>We will go over progressively more efficient approaches to solve the problem using dynamic programming. We will start with the most intuitive approach, top-down DP (Approach 1), followed by bottom-up DP (Approach 2), and then bottom-up DP with optimized space complexity (Approach 3). Lastly, we will explore an advanced stack solution that is the optimal approach (Approach 4).</p>
<p><br></p>
<hr>
<h4 id="approach1topdowndp">Approach 1: Top-down DP</h4>
<p><strong>Intuition</strong></p>
<p>Thinking back, how did we figure out this question can be solved using dynamic programming? We were given a few clues.  First, the problem asks us to <strong>minimize</strong> something, in this case, the difficulty of the job schedule.  Second, our current decisions (what jobs to schedule today) depend on our previous decisions (what jobs have already been scheduled).  Lastly, as shown in the diagram above, the original problem can be broken into smaller subproblems, and we can reuse the results of those subproblems to solve the original problem. These three traits are characteristic of problems that can be solved with dynamic programming. In most cases, this problem included, it is more intuitive to solve DP problems using a top-down approach as opposed to a bottom-up approach. So, for our first approach, we will use top-down dynamic programming.
Now, let's take a closer look at how we can break the original problem into smaller subproblems and reuse the results of those subproblems to solve the original problem.</p>
<p>In this case, we need to find all possible ways to schedule the job today and define the subproblem as starting from a larger index <code>j</code> with one day less.
That is, to solve for <code>min_diff(i, d)</code>, we must first calculate <code>min_diff(j, d - 1)</code> for all <code>j > i</code>, and then take the minimum job difficulty of all these possibilities as the output.</p>
<p>Finally, when there is only 1 day left, we must complete all of the remaining jobs on that final day; this is the base case.</p>
<p><strong>Algorithm</strong></p>
<p>The dynamic programming solution to this problem consists of three components:</p>
<ol>
<li><p>State definition:</p>
<p>Index <code>i</code> (the index of the <strong>first</strong> task for <strong>today</strong> in the <code>jobDifficulty</code> array) and day <code>d</code> (number of remaining days) will define the DP state. <code>min_diff(i, d)</code> refers to the minimum difficulty when starting at the $$i^&#123;th&#125;$$ job with <code>d</code> days left.</p>
<p><code>min_diff(0, d)</code> will be the final answer since it represents starting at the beginning of the job array and finishing all jobs in exactly <code>d</code> days.</p></li>
<li><p>State transition function:</p>
<p>The job at index <code>j</code> will be the <strong>first</strong> task for the <strong>upcoming</strong> day, therefore, the jobs to be finished today are all jobs with indices between <code>i</code> and <code>j</code>,  which is <code>jobDifficulty[i:j]</code>.  Since the difficulty of a day is the maximum difficulty of a job done in that day, the maximum of <code>jobDifficulty[i:j]</code> will be added to the sum of job difficulties.</p>
<p>With this in mind, let's formulate the state transition function as follows:</p>
<p><code>min_diff(i, d) = min_diff(j, d - 1) + max(jobDifficulty[i:j]) for all j > i</code></p></li>
<li><p>Base case:</p>
<p>When there is only 1 day remaining, we need to finish all unfinished jobs on that day and increase the difficulty of the job schedule by the maximum difficulty of these jobs.</p></li>
</ol>
<p>Before we dive into the code, let's take a moment to consider edge cases and optimizations.</p>
<p>One edge case that we must consider is if the number of days is more than the number of tasks, then we won't be able to arrange at least one job per day; in this case, we should return <code>-1</code>.</p>
<p>Finally, one optimization that we can implement is to use a variable, <code>daily_max_job_diff</code>, to keep track of the most difficult job scheduled on the current day. As we scan through the jobs for the current day, we do not need to revisit the full subarray of <code>jobDifficulty[i:j]</code> every time we want to calculate the maximum difficulty. Instead, each day, we can update the maximum job difficulty seen so far if the current job difficulty is greater than <code>daily_max_job_diff</code>.</p>
<iframe src="https://leetcode.com/playground/9b4Werv2/shared" frameborder="0" width="100%" height="500" name="9b4Werv2"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the length of the <code>jobDifficulty</code> array, and $$d$$ be the total number of days.</p>
<ul>
<li><p>Time complexity: $$O(n^2 \cdot d)$$ since there are $$n \cdot d$$ possible states, and we need $$O(n)$$ time to calculate the result for each state.</p></li>
<li><p>Space complexity: $$O(n \cdot d)$$ space is required to memoize all $$n \cdot d$$ states.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2bottomup2ddp">Approach 2: Bottom-up 2D DP</h4>
<p><strong>Intuition</strong></p>
<p>The previous solution used a function call stack to manage recursive calls; this requires additional space and time to maintain. We can circumvent the need for a function call stack by implementing the same approach using bottom-up DP.  Bottom-up DP is not as flexible as top-down DP because it must solve the subproblems in a specific order and usually needs to solve every subproblem (which sometimes may be more subproblems than that of top-down DP).  Although the overall time complexity remains the same for the bottom-up DP, it is often slightly faster than top-down DP because it is an iterative approach and does not need to maintain a function call stack.  Readers may check out <a href="https://awjin.me/algos-js/dp/tab-memo.html">Comparison of top-down and bottom-up DP</a> for more detailed comparisons between the two approaches.  So let's reimplement the solution from Approach 1 using bottom-up DP.</p>
<p>The key to writing bottom-up DP is to determine the dimensions of the DP matrix first and then understand how states transfer from one row to another.  Remember each state is a combination of the starting index, <code>i</code>, and the number of days remaining, <code>d</code>.</p>
<p>When transferring states, we need to ensure there are enough tasks remaining to arrange at least one job per day.  See below for an example to schedule 7 jobs in 3 days. The line from (2 days remaining, index 2) to (1 day remaining, index 5) can be interpreted as:
(1) jobs 5 and 6 are scheduled with 1 day remaining because our base case is to finish all jobs on the last day.<br>
(2) jobs 2, 3 and 4 are scheduled with 2 days remaining since <code>i</code> is the index of the first job done on the current day.
(3) jobs 0, 1 and 2 are scheduled with 3 days remaining.</p>
<p><img src="https://leetcode.com/articles/Figures/1335/1335_3Bottom-up_dp.JPG" alt="Bottom-up dp illustration" referrerpolicy="no-referrer"></p>
<p>There is no dependency between <code>min_diff[d][i]</code> and <code>min_diff[d][j]</code> if <code>i != j</code>, because the value of <code>min_diff[d][i]</code> only depends on the results of <code>min_diff[d - 1][j]</code> when <code>j > i</code>. By identifying such relationships, we can draw viable edges for state transfer between different cells in the DP matrix.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>State definition:</p>
<p>Index <code>i</code> (starting index in the <code>jobDifficulty</code> array) and day <code>d</code> (number of remaining days) will define the DP state. <code>min_diff[d][i]</code> refers to the minimum difficulty when starting at the $$i^&#123;th&#125;$$ job with <code>d</code> days left.</p>
<p><code>min_diff[d][0]</code> will be the final answer since it represents starting at the beginning of the job array and finishing all jobs in <code>d</code> days.</p></li>
<li><p>State transfer function:</p>
<p>The number of rows in the DP matrix is the total number of remaining days plus one (<code>d + 1</code>), and the number of columns in the DP matrix is the length of the <code>jobDifficulty</code> array plus one (<code>n + 1</code>). Note, for <code>n</code> jobs to be completed, there are <code>n + 1</code> possible states, ranging from 0 jobs being done, to all <code>n</code> jobs being completed.</p>
<p>The value of <code>min_diff[d][i]</code> only depends on the results of <code>min_diff[d - 1][j]</code> when <code>j > i</code>. The statements can be expressed as:</p>
<p><code>min_diff[d][i] = min(daily_max_job_diff + min_diff[d - 1][j])</code> for all <code>j > i</code>,</p>
<p>where <code>daily_max_job_diff</code> is the maximum difficulty of jobs between index <code>i</code> and index <code>j</code> not including <code>j</code>, and <code>i</code> is the index of the first job that is done on the current day and <code>j</code> is the index of the first job that is done on the next day.</p></li>
<li><p>Base case:</p>
<p>We will prefill the last column of the matrix with zeros, to indicate that when there are no remaining jobs, the maximum job difficulty to be added is 0.</p></li>
</ol>
<iframe src="https://leetcode.com/playground/XJuGdxD9/shared" frameborder="0" width="100%" height="500" name="XJuGdxD9"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the length of the <code>jobDifficulty</code> array, and $$d$$ be the total number of days.</p>
<ul>
<li><p>Time complexity: $$O(n^2 \cdot d)$$ since there are $$n \cdot d$$ possible states, and we need $$O(n)$$ time to calculate the result for each state.</p></li>
<li><p>Space complexity: $$O(n \cdot d)$$ is required for the $$(n + 1) \times (d + 1)$$ DP array.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3bottomup1ddp">Approach 3: Bottom-up 1D DP</h4>
<p><strong>Intuition</strong></p>
<p>As mentioned in the previous approach, bottom-up DP requires subproblems to be solved in a specific order.  While this makes bottom-up DP less flexible than top-down DP, with some clever planning, this constraint allows us to reduce the amount of space used.  Because the subproblems are solved in a specific order, sometimes the results of subproblems will be referenced early in the iterative process and then never referenced again.  Therefore, once we are certain we do not need to reference the results of these subproblems, the results can be removed from memory. Let's see if we can improve the previous approach by implementing this optimization.</p>
<p>Notice that in Approach 2, any state with <code>d</code> days remaining only depends on the results for states with <code>d - 1</code> days remaining.  Therefore, we do not need to store the states with less than <code>d - 1</code> days remaining.
Therefore, the space complexity can be further improved.</p>
<p><strong>Algorithm</strong></p>
<p>Since the result in <code>min_diff[d][i]</code> only depends on <code>min_diff[d - 1][j]</code>, we only need to store the states of the current day and the next day as two DP arrays of size <code>n</code>, where <code>n</code> is the number of jobs.</p>
<p>This approach is very similar to Approach 2, the few changes made include:  <code>min_diff[d][i]</code> has been replaced by with <code>min_diff_curr_day[i]</code>, and <code>min_diff[d - 1][j]</code> has been replaced with <code>min_diff_next_day[j]</code>.
<code>min_diff_curr_day[i]</code> records all the results for the current day, while <code>min_diff_next_day[j]</code> records all the results for the next day (with one less remaining day).</p>
<iframe src="https://leetcode.com/playground/GRCkwowR/shared" frameborder="0" width="100%" height="500" name="GRCkwowR"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the length of the <code>jobDifficulty</code> array, and $$d$$ be the total number of days.</p>
<ul>
<li><p>Time complexity: $$O(n^2 \cdot d)$$ since there are $$n \cdot d$$ possible states, and we need $$O(n)$$ time to calculate the result for each state.</p></li>
<li><p>Space complexity: $$O(n)$$ as we only use two arrays of length $$n + 1$$ to store all relevant states at any given time.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach4monotonicstackbettertimecomplexity">Approach 4: Monotonic Stack - Better Time Complexity</h4>
<p><strong>Intuition</strong></p>
<p>We have walked through the intuition and implementation of the top-down and bottom-up DP approaches. Being able to clearly articulate the logic and time/space complexity for these approaches will be more than sufficient for most interviews.</p>
<p>But is there an even better solution? Can we improve even more?</p>
<p>The answer is yes! This approach falls outside the scope of a typical interview.  However, it will be fun to explore the solution, and to think about where else this methodology could be applied!</p>
<p>First, let's consider what inefficiency exists in the previous approach that we can improve on.</p>
<p>Remember our conclusion in the previous approaches that the value of <code>min_diff[d][i]</code> only depends on the results of <code>min_diff[d - 1][j]</code> when <code>j > i</code>. From the state transfer function <code>min_diff_curr_day[i] = min(min_diff_curr_day[i], dailyMaxJobDiff + min_diff_next_day[j])</code>, it is evident that the job difficulty of the current day is solely determined by the maximum job difficulty seen so far, on the current day (between index <code>i</code> and <code>j</code>). Therefore, when <code>jobDifficulty[i]</code> and <code>jobDifficulty[j]</code> are the two jobs with the highest job difficulty between <code>i</code> and <code>j</code>, then the values of other job difficulties between <code>i</code> and <code>j</code> do not affect the difficulty of the current day as shown in the figure below.</p>
<p><img src="https://leetcode.com/articles/Figures/1335/1335_lower_job_difficulties.JPG" alt="Ignore jobs with lower job difficulties" referrerpolicy="no-referrer"></p>
<p>With this in mind, we do not actually need to check every combination of <code>i</code> and <code>j</code> and update their values in the DP matrix. Instead, we can use a monotonic stack to reduce the total amount of calculations.</p>
<p>To better understand how we can use a monotonic stack to exploit this observation, let's start by focusing on two indices, <code>j</code> and <code>i</code> (where out of all the jobs between <code>j</code> and <code>i</code> inclusive, jobs at <code>j</code> and <code>i</code> will have the two greatest difficulties). Notice that the order of <code>i</code> and <code>j</code> is a different this time.  Instead of <code>i</code> being the index of the first job done today and <code>j</code> being the index of the first job done tomorrow, in this approach, <code>i</code> is the index of the <strong>last</strong> job that we try to schedule for today, and <code>j</code> is the index of a job in the job schedule that is scheduled for today <strong>before</strong> index <code>i</code> (i.e., <code>j</code> < <code>i</code>).</p>
<p>Given that the $$j^&#123;th&#125;$$ job is scheduled on the current day, let's find out how to update the value of minimum job schedule difficulty when we include the $$i^&#123;th&#125;$$ job on the current day. There are two possible scenarios:</p>
<ul>
<li>Scenario 1: <code>jobDifficulty[j] <= jobDifficulty[i]</code>. After we include the $$i^&#123;th&#125;$$ job on the current day, the minimum job schedule difficulty on the current day will increase by at most <code>jobDifficulty[i] - jobDifficulty[j]</code> compared with when the $$j^&#123;th&#125;$$ job is the <strong>last</strong> job scheduled for the current day. Since job <code>i</code> has higher job difficulty than job <code>j</code>, the value for <code>jobDifficulty[j]</code> becomes irrelevant when scheduling any future jobs on the current day, so index <code>j</code> can be popped from the stack.</li>
</ul>
<p><img src="https://leetcode.com/articles/Figures/1335/1335_Scenario_1.JPG" alt="Scenario 1" referrerpolicy="no-referrer"></p>
<ul>
<li>Scenario 2: <code>jobDifficulty[j] > jobDifficulty[i]</code>. The minimum job schedule difficulty on the current day only depends on the most difficult job scheduled on that day, which is <code>jobDifficulty[j]</code>. So after we include the $$i^&#123;th&#125;$$ job on the current day, the minimum job schedule difficulty will be no higher than that of when the $$j^&#123;th&#125;$$ job is the <strong>last</strong> job scheduled for the current day. We still need to keep job <code>j</code> in the stack for scheduling future jobs on the current day.</li>
</ul>
<p><img src="https://leetcode.com/articles/Figures/1335/1335_Scenario_2.JPG" alt="Scenario 2" referrerpolicy="no-referrer"></p>
<p>To recap, in the above scenarios, every time a new job (<code>i</code>) is added to the current day's schedule, if any prior job (<code>j</code>) has a lower or equal job difficulty, then we can discard the job <code>j</code> as it becomes irrelevant for the job schedule difficulty of the current day (as in scenario 1). Otherwise, we will need to keep the value the job <code>j</code> when <code>jobDifficulty[j] > jobDifficulty[i]</code> (as in scenario 2).  As a result, at any given moment, the difficulty of the jobs we keep in the stack will be monotonically decreasing. The monotonically decreasing relationship is a hint that we may be able to solve this problem more efficiently by using a monotonic stack. Notice that when the $$i^&#123;th&#125;$$ job is added to the current day's schedule, we focus on whether previous jobs should be popped out from the stack and how to update the current state of job difficulty using the popped out job.</p>
<p>Now, with a monotonic stack in mind, let's approach the problem from a different angle (credit to @Lee215), as demonstrated in the slides below.</p>
<blockquote>
  <p>Note, for the monotonic stack used here, instead of recording the values, we will keep track of the corresponding indices since we can always look up values in the <code>jobDifficulty</code> array and <code>min_diff_curr_day</code> array.  So, the values that correspond to the indices contained in the stack are monotonically decreasing.</p>
</blockquote>
<p>Contrary to the previous approach, where we iterated over the <code>days_remaining</code> from <code>1</code> to <code>d</code>. Here, we will iterate over the current day from <code>day</code> equals 0, which is the start of the job schedule, to <code>day</code> equals <code>d - 1</code>, which is the last day of the job schedule.</p>
<p>Each day, we will iterate over the indices <code>i</code> of all jobs that could be scheduled on the current day. We start at <code>i</code> equals <code>day</code> because at least one job per day must have been scheduled on previous days. For each index <code>i</code>, we will say this will be the index of the <strong>last</strong> job scheduled today. Thus, the current day's job minimum schedule difficulty will start as <code>jobDifficulty[i]</code> for <code>i = day</code> because, so far, the job at <code>i</code> is the only job scheduled today, and the job schedule difficulty (<code>min_diff_curr_day[i]</code>) is the difficulty of the job at index <code>i</code> plus the minimum difficulty of the job schedule that ended yesterday at index <code>i - 1</code>, which is <code>min_diff_prev_day[i - 1]</code>.</p>
<p>Now, let's try to schedule more jobs for today by increasing <code>i</code> and see how previous jobs at index <code>j</code> where <code>day <= j < i</code> will impact the minimum job difficulty of the current day. Here's the trick, as long as the difficulty of the job at index <code>i</code> is greater than the difficulty of all jobs between <code>j</code> and <code>i</code>, then extending a job schedule to include all jobs up to and including <code>i</code> will change the schedule difficulty by <code>jobDifficulty[i] - jobDifficulty[j]</code>. This is because <code>jobDifficulty[j]</code> is the most difficult job scheduled today so far, and by extending the schedule to include the job at <code>i</code>, the schedule difficulty for today will increase to <code>jobDifficulty[i]</code> from <code>jobDifficulty[j]</code>.</p>
<p>A naive way is to repeat this process by including each potential index <code>i</code>, and compare it with all previous job <code>j</code>, we will update the minimum job difficulty schedule that ends at job <code>i</code>. However, doing this for each <code>i</code> will result in $$O(n^2 \cdot d)$$ total time required for this approach… which is no better than the previous approach.</p>
<p>So what makes this approach more efficient? The key insight is that after extending the job schedule that ends at index <code>i</code> once, we never need to consider extending it again. Here's why. Consider the case where we update the job schedule difficulty at <code>i</code> (<code>min_diff_curr_day[i]</code>) by extending the job schedule that ends at index <code>j</code> like so: <code>min_diff_curr_day[i] <= min_diff_curr_day[j] + (jobDifficulty[i]- jobDifficulty[j])</code>. Then at a later index (say <code>i + 1</code>), we update the job schedule difficulty at <code>i + 1</code> by extending the job schedule that ends at index <code>i</code> following the same equation. Let's take a close look at <code>min_diff_curr_day[i + 1]</code> when we extend the job schedule ending at <code>i</code> and <code>jobDifficulty[j] < jobDifficulty[i]</code>.</p>
<pre><code>min_diff_curr_day[i + 1] <= min_diff_curr_day[i] + jobDifficulty[i + 1] - jobDifficulty[i]
# Substitute in the above equation for min_diff_curr_day[i]
                         <= min_diff_curr_day[j] + jobDifficulty[i] - jobDifficulty[j]
                                                 + jobDifficulty[i + 1] - jobDifficulty[i]
                         = min_diff_curr_day[j] + jobDifficulty[i + 1] - jobDifficulty[j]
</code></pre>
<p>Notice that extending the job schedule ending at <code>i</code> to include all jobs up to <code>i + 1</code> has a equal or tighter bound than extending the job schedule ending at <code>j</code> to include all jobs up to <code>i + 1</code> given <code>jobDifficulty[j] < jobDifficulty[i]</code>. For this reason, we only need to consider extending the job schedule that ends at <code>j</code> once, then the difficulty of the job schedule that ends at <code>j</code> can be forgotten.</p>
<p>The key insight is: once we have considered extending a schedule once, we never need to consider extending it again. Only considering the most recent schedules where today's difficulty is less than job <code>i</code> and safely ignoring schedules that have already been extended suggest that a stack will be a good data structure. For each <code>i</code>, we will pop the job schedules from the top of the stack where the difficulty of job <code>j</code> (the top of the stack) is less than <code>i</code>, and consider extending the popped job schedule to include <code>i</code>.</p>
<blockquote>
  <p>"Consider extending the schedule" means updating <code>min_diff_curr_day[i]</code> to <code>min_diff_curr_day[j] + jobDifficulty[i] - jobDifficulty[j]</code> if it is less than the value of <code>min_diff_curr_day[i]</code>.</p>
</blockquote>
<p>After popping all <code>j</code> from the stack where <code>jobDifficulty[j] <= jobDifficulty[i]</code> (scenario 1), if the stack is not empty, we will check scenario 2 once. Finally, we can push <code>i</code> onto the stack since we may consider extending the job schedule that ends at <code>i</code> later.</p>
<p>Now, let's take a look at how to maintain the monotonic stack and summarize the steps of the algorithm.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>We will need two arrays, <code>min_diff_curr_day</code> and <code>min_diff_prev_day</code> to record the minimum total job difficulty of the current day and the previous day (one more day remaining).</li>
</ol>
<p>For instance, <code>min_diff_curr_day[i]</code> records the minimum total job difficulty after completing the $$i^&#123;th&#125;$$ job on the current day.  Since we need to complete at lease one job on each day, when we are at day 0 (with <code>d</code> remaining days), we can only perform the $$0^&#123;th&#125;$$ job, so <code>min_diff_curr_day[i]</code> is <code>jobDifficulty[0]</code>. When we are not at the very first day, then we must have previously completed at least $$day-1^&#123;th&#125;$$ jobs. On the current day, by completing the $$i = day^&#123;th&#125;$$ job, <code>min_diff_curr_day[i]</code> will be <code>min_diff_prev_day[i-1] + jobDifficulty[i]</code>.</p>
<p>Refer to the slides below for two examples of initialization at <code>day = 0</code> and <code>day = 1</code>, respectively.
!?!../Documents/1335/1335_initialization.json:1119,636!?! <br></p>
<ol start="2">
<li>We will then iterate through each day and update the <code>min_diff_curr_day</code> along the way for each possible last job scheduled on that day.</li>
</ol>
<p>Specifically, we iterate through jobs with indices ranging from <code>i</code> equals <code>day</code> to <code>n</code>. To maintain a monotonically decreasing stack, if the job difficulty of the last element in the stack (<code>j</code>) is smaller than or equal to the current job (<code>i</code>), we will pop the last element (<code>j</code>) from the stack.</p>
<p>Since <code>jobDifficulty[j] <= jobDifficulty[i]</code>, by additionally completing jobs from index <code>j + 1</code> to index <code>i</code>, the total job difficulty <code>min_diff_curr_day[i]</code> will be no more than <code>min_diff_curr_day[j] + jobDifficulty[i] - jobDifficulty[j]</code>. So, we can update <code>min_diff_curr_day[i]</code> as <code>min(min_diff_curr_day[i], min_diff_curr_day[j] + jobDifficulty[i] - jobDifficulty[j])</code></p>
<ol start="3">
<li><p>On each day, after we iterate through each indices <code>i</code>, popping all indices <code>j</code> off the stack where <code>jobDifficulty[j] <= jobDifficulty[i]</code>, and updating <code>min_diff_curr_day[i]</code>, there may be some remaining indices in the monotonically decreasing stack. Since we are using a monotonically decreasing stack, we know that <code>jobDifficulty[j] > jobDifficulty[i]</code> for all of the remaining indices in the stack. Until now, while updating <code>min_diff_curr_day[i]</code>, we only considered scenario 1 (when <code>jobDifficulty[j] <= jobDifficulty[i]</code>). Before we move to the next day, we must consider scenario 2 as well. Thus, if the stack is not empty, we compare the minimum difficulty job schedule ending at job <code>j</code> where <code>j</code> is on the top of the stack, and the total job difficulty in the current day <code>min_diff_curr_day[i]</code> will be no more than <code>min_diff_curr_day[j]</code>. So, we can update <code>min_diff_curr_day[i]</code> as <code>min(min_diff_curr_day[i], min_diff_curr_day[j])</code>.</p></li>
<li><p>At the end, we will return the total minimum job difficulty on the $$d^&#123;th&#125;$$ day after completing the $$n-1^&#123;th&#125;$$ job, which is <code>min_diff_prev_day[n - 1]</code>.</p></li>
</ol>
<p>Refer to the slides below for how to update the DP states with the monotonically decreasing stack step by step. The height of each circle corresponds to the job difficulty.</p>
<p>!?!../Documents/1335/1335<em>stack</em>solution.json:1119,636!?! <br></p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/mSyPpDLG/shared" frameborder="0" width="100%" height="500" name="mSyPpDLG"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$n$$ be the length of the <code>jobDifficulty</code> array, and $$d$$ be the total number of days.</p>
<ul>
<li><p>Time complexity: $$O(n \cdot d)$$ as there are $$n \cdot d$$ possible states. Using the stack solution, we need $$O(n)$$ time to calculate all $$n$$ states for each day.</p></li>
<li><p>Space complexity: $$O(n)$$ as we only use one array of length <code>n</code> to store all DP states for the prior day and the current day, and the stack that will contain at most <code>n</code> elements.</p></li>
</ul>
<p>If you are interested in practicing the skill to optimize the DP solution using a monotonic stack, you may want to try the following two LeetCode problems.</p>
<p><a href="https://leetcode.com/problems/longest-valid-parentheses/">LeetCode 32. Longest Valid Parenthesis</a>. Check out Approach 3 in the official solution.</p>
<p><a href="https://leetcode.com/problems/maximal-rectangle/">LeetCode 85. Maximal Rectangle</a>. Check out Approach 3 in the official solution.</p>  
</div>
            