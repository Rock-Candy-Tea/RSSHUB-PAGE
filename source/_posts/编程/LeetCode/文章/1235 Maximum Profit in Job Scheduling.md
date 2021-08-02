
---
title: '1235. Maximum Profit in Job Scheduling'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://assets.leetcode.com/uploads/2019/10/10/sample1_1584.png'
author: LeetCode
comments: false
date: Sat, 24 Jul 2021 00:00:00 GMT
thumbnail: 'https://assets.leetcode.com/uploads/2019/10/10/sample1_1584.png'
---

<div>   
<p>We have <code>n</code> jobs, where every job is scheduled to be done from <code>startTime[i]</code> to <code>endTime[i]</code>, obtaining a profit of <code>profit[i]</code>.</p>

<p>You're given the <code>startTime</code>, <code>endTime</code> and <code>profit</code> arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.</p>

<p>If you choose a job that ends at time <code>X</code> you will be able to start another job that starts at time <code>X</code>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<p><strong><img alt src="https://assets.leetcode.com/uploads/2019/10/10/sample1_1584.png" style="width: 380px; height: 154px;" referrerpolicy="no-referrer"></strong></p>

<pre><strong>Input:</strong> startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
<strong>Output:</strong> 120
<strong>Explanation:</strong> The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
</pre>

<p><strong>Example 2:</strong></p>

<p><strong><img alt src="https://assets.leetcode.com/uploads/2019/10/10/sample22_1584.png" style="width: 600px; height: 112px;" referrerpolicy="no-referrer"> </strong></p>

<pre><strong>Input:</strong> startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
<strong>Output:</strong> 150
<strong>Explanation:</strong> The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
</pre>

<p><strong>Example 3:</strong></p>

<p><strong><img alt src="https://assets.leetcode.com/uploads/2019/10/10/sample3_1584.png" style="width: 400px; height: 112px;" referrerpolicy="no-referrer"></strong></p>

<pre><strong>Input:</strong> startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
<strong>Output:</strong> 6
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= startTime.length == endTime.length == profit.length <= 5 * 10<sup>4</sup></code></li>
<li><code>1 <= startTime[i] < endTime[i] <= 10<sup>9</sup></code></li>
<li><code>1 <= profit[i] <= 10<sup>4</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>We have N jobs each having some profit associated with it, and we want to gain maximum profit by selecting some non-conflicting jobs. Two jobs A and B represented as <code>(startTime, endTime)</code> by <code>(startA, endA)</code> and <code>(startB, endB)</code> are <strong><em>non-conflicting</em></strong> if either job A starts after job B ends which can be represented by condition <code>startA >= endB</code>, or if job B starts after job A ends which can be represented by <code>startB >= endA</code>.</p>
<p>We can observe that for each job, there are two options, either to schedule it or not. The total number of possible combinations with N jobs is $$2^N$$. The brute force approach is to enumerate every possible combination. However, we want a better-optimized approach. We can achieve this by applying our definition for <strong><em>non-conflicting</em></strong> jobs. If we schedule the job at index <code>i</code> that ends at <code>endTime[i]</code>, then all the jobs which have a <code>startTime</code> before <code>endTime[i]</code> can be discarded. The next job to schedule at index <code>j</code> should have a start time, <code>startTime[j]</code>, such that <code>startTime[j] >= endTime[i]</code>.</p>
<p>There are two key characteristics of this problem that we should take note of at this time.  First, a job cannot be scheduled if a conflicting job has already been scheduled. In other words, each decision we make is affected by the previous decisions we have made.  Second, the problem asks us to <strong>maximize</strong> the profit by scheduling non-conflicting jobs.  These are two common characteristics of dynamic programming problems, and as such we will approach this problem using dynamic programming.</p>
<p><br></p>
<hr>
<h4 id="approach1topdowndynamicprogrammingbinarysearch">Approach 1: Top-Down Dynamic Programming + Binary Search</h4>
<p><strong>Intuition</strong></p>
<p>Let's start at time zero, before the <code>startTime</code> of any job, at this point we can choose any job to schedule first. Once the first job has ended, we can iterate over all of the jobs and only consider scheduling those that start after the current time.  The process of repeatedly iterating over the jobs array is very time-consuming and we can do better: if we sort our jobs according to start time, then we can apply binary search to find the next job. After sorting jobs according to <code>startTime</code>, to find the index of the first non-conflicting job, binary search for the <code>endTime</code> of the current job in the list of start times for all jobs.</p>
<p>For each job, we will try two options:</p>
<ul>
<li>Schedule this job and move on to the next non-conflicting job using binary search.</li>
<li>Skip this job and move on to the next available job. </li>
</ul>
<p>Then we can make an informed decision about whether we should schedule the job based on which of the above two options results in the greater profit.</p>
<p>This recursive approach will have repeated subproblems; this can be observed in the figure below. Notice, the subtree with root $$2$$ is repeated signifying that we must solve this subproblem more than once. 
<img src="https://leetcode.com/articles/Figures/1235/1235A.png" alt="fig" referrerpolicy="no-referrer"></p>
<p>To address this issue, the first time we calculate <code>maxProfit</code> for a certain <code>position</code>, we will store the value in an array; this value represents the maximum profit we can get from the jobs at indices from <code>position</code> to the end of the array.  The next time we need to calculate <code>maxProfit</code> for this <code>position</code>, we can look up the result in constant time. This technique is known as memoization and it helps us avoid recalculating repeated subproblems.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Store the <code>startTime</code>, <code>endTime</code> and <code>profit</code> of each job in <code>jobs</code>.</li>
<li>Sort the <code>jobs</code> according to their starting time.</li>
<li>Iterate over jobs from left to right, where <code>position</code> is the index of the current job.  For each job, we must compare two options:</li>
</ol>
<ul>
<li>i. Skip the current job (earn 0 profit) and move on to consider the job at the index <code>position + 1</code>.<ul>
<li>ii. Schedule the current job (earn profit for the current job) and move on to the next non-conflicting job whose index is <code>nextIndex</code>. <code>nextIndex</code> is determined by using binary search in the <code>startTime</code> array.</li></ul></li>
</ul>
<ol>
<li>Return the maximum profit of the two choices and record this profit in the array <code>memo</code> (memoization).</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/iqfHEL2f/shared" frameborder="0" width="100%" height="500" name="iqfHEL2f"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of the <code>jobs</code> array.</p>
<ul>
<li><p>Time complexity: $$O(N\log N)$$</p>
<p>Sorting jobs according to their starting time will take $$O(N\log N)$$.</p>
<p>The time complexity for the recursion (with memoization) is equal to the number of times <code>findMaxProfit</code> is called times the average time of <code>findMaxProfit</code>. The number of calls to <code>findMaxProfit</code> is $$2*N$$ because each non-memoized call will call <code>findMaxProfit</code> twice. 
Each memoized call will take $$O(1)$$ time while for the non-memoized call, we will perform a binary search that takes $$O(log N)$$ time, hence the time complexity will be $$O(N\log N + N)$$.</p>
<p>The total time complexity is therefore equal to $$O(N\log N)$$.</p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>Storing the starting time, ending time, and profit of each job will take $$3\cdot N$$ space. 
Hence the complexity is $$O(N)$$.</p>
<p>The space complexity of the sorting algorithm depends on the implementation of each programming language. For instance, in Java, the Arrays.sort() for primitives is implemented as a variant of quicksort algorithm whose space complexity is $$O(\log 
N)$$. In C++ sort() function provided by STL is a hybrid of Quick Sort, Heap Sort and 
Insertion Sort with the worst-case space complexity of $$O(\log N)$$. Thus the use of 
inbuilt sort() function adds $$O(\log N)$$ to space complexity.</p>
<p>The result for each <code>position</code> will be stored in <code>memo</code> and <code>position</code> can have the values from $0$ to $N$, thus the space required is $$O(N)$$. Also, stack space in recursion is equal to the maximum number of active functions.  In the scenario where every job is not scheduled, the function call stack will be of size $$N$$.</p>
<p>The total space complexity is therefore equal to $$O(N)$$.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2bottomupdynamicprogrammingbinarysearch">Approach 2: Bottom-Up Dynamic Programming + Binary Search</h4>
<p><strong>Intuition</strong></p>
<p>In the previous approach, the recursive calls incurred stack space. This can be avoided by applying the same approach in an iterative manner which is generally faster than the top-down approach. In this approach, we start from <code>position = n</code> which is our base case because when there are no more jobs to schedule the maximum profit must be 0.  We will traverse the <code>jobs</code> array from right to left and build up <code>memo</code> with the previously calculated maximum profits. In order to build up <code>memo</code>, for each index, we will check the profit that can be obtained by scheduling and not scheduling the job at that index. </p>
<ol>
<li>If we schedule the job at index <code>i</code>, we will apply binary search to find the index (<code>nextIndex</code>) of the first non-conflicting job. The total profit by scheduling the job at index <code>i</code> is the sum of the profit of the current job and the value of <code>memo[nextIndex]</code>.</li>
<li>If we skip the job at index <code>i</code>, the maximum profit will be the same as <code>memo[i+1]</code> which is the maximum profit that can be obtained by starting at the next job. </li>
</ol>
<p>The maximum profit obtained from the above two options will be stored at <code>memo[i]</code> which represents the maximum profit we can achieve by scheduling non-conflicting jobs between index <code>i</code> and the end of the array.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Store the <code>startTime</code>, <code>endTime</code> and <code>profit</code> of each job in <code>jobs</code>.</li>
<li>Sort the jobs according to their starting time.</li>
<li>Iterate over the jobs from right to left find the <code>currProfit</code> for each job. <code>currProfit</code> is the sum of the current job's profit and the maximum profit obtained by scheduling jobs between <code>nextIndex</code> and the end of the jobs array(<code>memo[nextIndex]</code>).</li>
<li>For each index <code>i</code>, set <code>memo[i]</code> equal to the maximum between <code>currProfit</code> and <code>memo[i+1]</code>. If <code>currProfit</code> is greater, then it's more profitable to schedule the job at index <code>i</code>, otherwise, it's better not to schedule this job.</li>
<li>Return the value <code>memo[0]</code>.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/27ZXUaaT/shared" frameborder="0" width="100%" height="500" name="27ZXUaaT"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of the <code>jobs</code> array.</p>
<ul>
<li><p>Time complexity: $$O(N\log N)$$</p>
<p>Sorting jobs according to their starting time will take $$O(N\log N)$$ time.</p>
<p>We iterate over all $$N$$ jobs from right to left and for each job we perform a 
binary search which takes $$O(\log N)$$, so this step also requires $$O(N\log N)$$ time.</p>
<p>The total time complexity is therefore equal to $$O(N\log N)$$.</p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>Storing the start time, end time, and profit of each job takes $$3\cdot N$$ space. 
Hence the complexity is $$O(N)$$.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3sortingpriorityqueue">Approach 3: Sorting + Priority Queue</h4>
<p><strong>Intuition</strong></p>
<p>This problem can be correlated to <a href="https://leetcode.com/problems/maximum-length-of-pair-chain/">Maximum Length of Pair Chain</a> where each job can be thought of as a pair of startTime and endTime (a link in the chain). Now consider that each link in the chain has a profit associated with it, and rather than making the longest chain, our goal is to make the most profitable chain. </p>
<p>Considering the problem this way, it becomes similar to <a href="https://leetcode.com/problems/longest-increasing-subsequence/">Longest Increasing Subsequence</a> with the goal of maximizing the profit instead of length. As such, we can approach this problem in a similar way, by first sorting the jobs according to their start time and then for each job, choose the most profitable chain of jobs to add the current job to. </p>
<p>Let's walk through an example to see how this will work:</p>
<p>!?!../Documents/1235<em>maximum</em>profit<em>in</em>job_scheduling.json:960,720!?! <br></p>
<p>Notice that for every new job, we iterate over all of the previous job chains to find the most profitable chain that ends at or before the current job starts.  This results in $$O(N^2)$$ time complexity. Can we do better?</p>
<p>Let's take a moment and think about how we can optimize this approach.</p>
<p>There are two key observations to make: </p>
<ol>
<li>For each job we want to find all chains that end before the current job's start time.  </li>
<li>Since the jobs are sorted according to start time if a chain does not conflict with the current job, then it will also not conflict with any future job. </li>
</ol>
<p>The first observation tells us that we want to store the existing chains so that those with the earliest end time can be accessed efficiently.  The second observation tells us that we do not need to remember chains that have ended, we only need to remember the maximum profit from any chain that has ended.  These observations (accessing chains that have earlier end times and removing them from the data structure) hint that a heap is an efficient data structure to store the chains.  </p>
<p><strong>Algorithm</strong></p>
<p>We will iterate over the jobs from left to right and for each job, we will check if this job can be appended to any previous chain of jobs by popping out the chains from the heap. Among all chains that do not conflict with the current job, we will append the current job to the chain with the highest profit. When we append the current job to the highest profit chain, we form a new chain. This job chain will then be pushed into the heap as a pair of the end time and the total profit (the current job's profit plus maximum profit from non-conflicting chains).</p>
<p>However, there is a tricky part here. When we pop a job chain from the heap we don't push it back into the heap, although this job chain can still be combined with other jobs in the future. To handle this case we introduce a variable <code>maxProfit</code> whenever we pop a job chain from heap we compare its profit with the <code>maxProfit</code> and update it accordingly. The reason is that the jobs are sorted and hence if we pop out a chain from the heap for the <code>ith</code> job then it implies that this chain can be combined with any other job that comes after index <code>i</code>. Therefore we only need to store the chain's profit. Furthermore, since it is always optimal to use the most profitable chain, we only need to keep track of the maximum profit seen so far. Formally at the time of <code>ith</code> iteration, the value of <code>maxProfit</code> will be the maximum profit of a set of job chains to which the <code>ith</code> job can be appended.</p>
<ol>
<li>Store the <code>startTime</code>, <code>endTime</code>, and <code>profit</code> of each job in <code>jobs</code>.</li>
<li>Sort the <code>jobs</code> according to their starting time.</li>
<li>Iterate over jobs from left to right, where <code>i</code> is the index of the current job. For each job<ul>
<li>While the job chain at the top of the priority queue does not conflict with the current job, pop from the priority queue.</li>
<li>For each popped job chain compare its total profit with the <code>maxProfit</code> and update <code>maxProfit</code> accordingly.</li></ul></li>
<li>Push the pair of ending time and the combined profit (<code>maxProfit</code> + profit of this job) into the heap. This item represents the chain created by adding the current job to the most profitable job chain.</li>
<li>After iterating over all the jobs, compare the profit of the remaining chains in the priority queue with the <code>maxProfit</code>. Return the value of <code>maxProfit</code>.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/M9FFgqo4/shared" frameborder="0" width="100%" height="500" name="M9FFgqo4"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the length of the <code>jobs</code> array.</p>
<ul>
<li><p>Time complexity: $$O(N\log N)$$</p>
<p>Sorting jobs according to their starting time will take $$O(N\log N)$$ time.</p>
<p>We iterate over all $$N$$ jobs. For each job, we push the maximum profit job chain into the heap once which takes $$O(\log N)$$ time.</p>
<p>The total time complexity is therefore equal to $$O(N\log N)$$.</p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>Storing the start time, end time, and profit of each job takes $$3\cdot N$$ space. 
Hence the complexity is $$O(N)$$.</p>
<p>The space complexity of the sorting algorithm depends on the implementation of each programming language. For instance, in Java, the Arrays.sort() for primitives is implemented as a variant of quicksort algorithm whose space complexity is $$O(\log 
N)$$. In C++ sort() function provided by STL is a hybrid of Quick Sort, Heap Sort and 
Insertion Sort with the worst-case space complexity of $$O(\log N)$$. Thus the use of 
inbuilt sort() function adds $$O(\log N)$$ to space complexity.</p>
<p>Each of the $$N$$ jobs will be pushed into the heap.  In the worst-case scenario, when all $$N$$ jobs end later than the last job starts, the heap will reach size $$N$$.</p>
<p>The total space complexity is therefore equal to $$O(N)$$.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            