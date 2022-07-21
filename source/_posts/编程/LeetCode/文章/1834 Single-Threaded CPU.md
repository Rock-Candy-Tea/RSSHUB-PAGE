
---
title: '1834. Single-Threaded CPU'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/1834/Slide29.PNG'
author: LeetCode
comments: false
date: Wed, 29 Jun 2022 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/1834/Slide29.PNG'
---

<div>   
<p>You are given <code>n</code>​​​​​​ tasks labeled from <code>0</code> to <code>n - 1</code> represented by a 2D integer array <code>tasks</code>, where <code>tasks[i] = [enqueueTime<sub>i</sub>, processingTime<sub>i</sub>]</code> means that the <code>i<sup>​​​​​​th</sup></code>​​​​ task will be available to process at <code>enqueueTime<sub>i</sub></code> and will take <code>processingTime<sub>i</sub></code><sub> </sub>to finish processing.</p>

<p>You have a single-threaded CPU that can process <strong>at most one</strong> task at a time and will act in the following way:</p>

<ul>
<li>If the CPU is idle and there are no available tasks to process, the CPU remains idle.</li>
<li>If the CPU is idle and there are available tasks, the CPU will choose the one with the <strong>shortest processing time</strong>. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.</li>
<li>Once a task is started, the CPU will <strong>process the entire task</strong> without stopping.</li>
<li>The CPU can finish a task then start a new one instantly.</li>
</ul>

<p>Return <em>the order in which the CPU will process the tasks.</em></p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> tasks = [[1,2],[2,4],[3,2],[4,1]]
<strong>Output:</strong> [0,2,3,1]
<strong>Explanation: </strong>The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = &#123;0&#125;.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = &#123;&#125;.
- At time = 2, task 1 is available to process. Available tasks = &#123;1&#125;.
- At time = 3, task 2 is available to process. Available tasks = &#123;1, 2&#125;.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = &#123;1&#125;.
- At time = 4, task 3 is available to process. Available tasks = &#123;1, 3&#125;.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = &#123;1&#125;.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = &#123;&#125;.
- At time = 10, the CPU finishes task 1 and becomes idle.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
<strong>Output:</strong> [4,3,2,0,1]
<strong>Explanation</strong><strong>: </strong>The events go as follows:
- At time = 7, all the tasks become available. Available tasks = &#123;0,1,2,3,4&#125;.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = &#123;0,1,2,3&#125;.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = &#123;0,1,2&#125;.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = &#123;0,1&#125;.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = &#123;1&#125;.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = &#123;&#125;.
- At time = 40, the CPU finishes task 1 and becomes idle.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>tasks.length == n</code></li>
<li><code>1 <= n <= 10<sup>5</sup></code></li>
<li><code>1 <= enqueueTime<sub>i</sub>, processingTime<sub>i</sub> <= 10<sup>9</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>The problem statement asks us to create a scheduling policy that prioritizes the shortest available task; this is known as <strong>Shortest Job First</strong> (SJF) CPU Scheduling. In SJF CPU Scheduling:</p>
<ul>
<li>If the CPU is idle and there are available tasks, the CPU will choose the one with the <strong>shortest processing time</strong>. If multiple tasks have the <strong>same shortest processing time</strong>, it will choose the task with the <strong>smallest index</strong> (the task which arrived first).</li>
<li>Once the CPU starts to execute a task, it will process the entire task without stopping, i.e. it is <strong>non-preemptive</strong>.</li>
</ul>
<p><img src="https://leetcode.com/articles/Figures/1834/Slide29.PNG" alt="sjf example" referrerpolicy="no-referrer"></p>
<p><br></p>
<hr>
<h4 id="approach1sortingminheap">Approach 1: Sorting + Min-Heap</h4>
<p><strong>Intuition</strong></p>
<p>The CPU can only pick a task for execution after it is enqueued. Thus, we need to keep track of <code>current time</code> to see which tasks are available for the CPU and sort the tasks in increasing order of their enqueue time.</p>
<p>Now, we can create a list of tasks available at the <code>current time</code> (tasks whose enqueue time is less than or equal to the current time). From this list, we will select the task with the shortest processing time, so we can think of sorting all the available tasks in increasing order of their processing time.<br>
Then after selecting a task, the CPU will run that task until it is complete, and the <code>current time</code> will increase by the processing time of the selected task.<br>
After increasing <code>current time</code>, some more tasks might become available for execution. We would then add these tasks to our list and again sort the list in increasing order of processing time. This approach will work, but sorting our available task list every time we update it will be costly in terms of runtime.</p>
<p>Thus, this gives us a hint of using a min-heap data structure. If you are new to the heap data structure, we recommend you visit our <a href="https://leetcode.com/explore/featured/card/heap/">Heap Explore Card</a>.<br>
A min-heap is a tree-like data structure that always stores the minimum valued element at the top using some comparison (processing time here, or task index in case of a tie) and where insertion and removal of elements (tasks) take logarithmic time.<br>
Hence, using min-heap will relieve us from the repeated sorting of our list since we can insert new tasks and retrieve the shortest task from the heap in logarithmic time.</p>
<p>Hence, the flow of our approach is something like:<br>
(a) We will insert all the currently available tasks in the min-heap.<br>
(b) Pick the task with the shortest processing time.<br>
(c) Increase the current time by the processing time of the selected task.   </p>
<p>Now, one point to note here is that let's say <code>current time</code> is <code>0</code>, the heap is empty, and the next available task will enqueue at <code>10</code>. The CPU will sit idle until <code>current time</code> reaches <code>10</code>. Instead of incrementing <code>current time</code> by <code>1</code>, we will update <code>current time</code> directly to <code>10</code>, which will reduce the number of iterations in our approach and improve the run-time.</p>
<p>This approach can be better understood with the following slideshow:</p>
<p>!?!../Documents/1834/slideshow1.json:960,540!?!</p>
<p><br></p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize some data-structures:</p>
<ul>
<li><code>nextTask</code>, min-heap to store task with minimum processing time on the top.</li>
<li><code>sortedTasks</code>, array to store tasks in sorted order on the basis of their enqueue time. </li>
<li><code>tasksProcessingOrder</code>, array to store the order in which the CPU will process the tasks.</li></ul></li>
<li><p>Add all of the tasks (with their index) to <code>sortedTasks</code> and sort the array using the built-in sort function.</p></li>
<li><p>Initialize <code>currTime</code> to <code>0</code>.</p></li>
<li><p>While there are tasks in the <code>sortedTasks</code> array that have not been added to the min-heap, or there are tasks remaining in the min-heap:</p>
<ul>
<li>Check if the min-heap is empty and if the enqueue time of the next task is greater than <code>currTime</code>. If so, then update the <code>currTime</code> to the next task's enqueue time.</li>
<li>Insert all the available tasks (tasks whose enqueue time is less than or equal to <code>currTime</code>), into the min-heap.</li>
<li>Pick the task on the top of the min-heap, increment <code>currTime</code> by its processing time, and add its index to the <code>tasksProcessingOrder</code> array. </li></ul></li>
<li><p>Return the <code>tasksProcessingOrder</code> array.</p></li>
</ol>
<p><br></p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/86GEHGdP/shared" frameborder="0" width="100%" height="500" name="86GEHGdP"></iframe>
<p><br></p>
<p><strong>Complexity Analysis</strong></p>
<p>Let $$N$$ be the number of tasks in the input array.</p>
<ul>
<li><p>Time complexity: $$O(N\log N)$$.</p></li>
<li><p>We create <code>sortedTasks</code>, which is a deep copy of the <code>tasks</code> array. This takes $$O(N)$$ time.</p></li>
<li><p>Sorting the <code>sortedTasks</code> array takes $$O(N \log N)$$ time.</p></li>
<li><p>We push and pop each task once in the min-heap, and both the operations take $$O(\log N)$$ time for each element. Thus, it takes $$O(N \log N)$$ time in total.</p></li>
<li><p>Thus, overall time complexity is, $$O(N + N \log N + N \log N)  \approx O(N \log N)$$.</p></li>
<li><p>Space complexity: $$O(N)$$.</p></li>
<li><p>Our <code>sortedTasks</code> array will store all $$N$$ tasks, and the min-heap will also contain at most $$N$$ tasks. </p></li>
<li><p>Thus, we use $$O(N + N) \approx O(N)$$ extra space.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            