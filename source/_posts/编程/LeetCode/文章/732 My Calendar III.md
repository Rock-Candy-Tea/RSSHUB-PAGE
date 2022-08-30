
---
title: '732. My Calendar III'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Documents/732/732_odt.drawio.svg'
author: LeetCode
comments: false
date: Wed, 24 Aug 2022 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Documents/732/732_odt.drawio.svg'
---

<div>   
<p>A <code>k</code>-booking happens when <code>k</code> events have some non-empty intersection (i.e., there is some time that is common to all <code>k</code> events.)</p>

<p>You are given some events <code>[start, end)</code>, after each given event, return an integer <code>k</code> representing the maximum <code>k</code>-booking between all the previous events.</p>

<p>Implement the <code>MyCalendarThree</code> class:</p>

<ul>
<li><code>MyCalendarThree()</code> Initializes the object.</li>
<li><code>int book(int start, int end)</code> Returns an integer <code>k</code> representing the largest integer such that there exists a <code>k</code>-booking in the calendar.</li>
</ul>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
<strong>Output</strong>
[null, 1, 1, 2, 3, 3, 3]

<strong>Explanation</strong>
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(50, 60); // return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
myCalendarThree.book(5, 15); // return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>0 <= start < end <= 10<sup>9</sup></code></li>
<li>At most <code>400</code> calls will be made to <code>book</code>.</li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h3 id="overview">Overview</h3>
<p>The problem asked for the maximum value of overlapped intervals at some points each time after adding a new interval. The main challenge here is to find an efficient way to maintain those added intervals and query how many intervals cover a single point quickly and dynamically.</p>
<p>This solution article provides three approaches with different performances. We will start from the most intuitive way, which is also mentioned in the solution to <a href="https://leetcode.com/problems/my-calendar-ii/solution/">731. My Calendar II</a>, and then generalize such kind of interval problems step by step to give two additional approaches.</p>
<hr>
<h3 id="approach1sweeplinealgorithm">Approach 1: Sweep-line Algorithm</h3>
<h4 id="intuition">Intuition</h4>
<p>If we look at each time point separately, our task is to find out how many events are going on at this time point and find the time point of the max number of events. Every time we book a new event <code>[start, end)</code>, what we actually do is add 1 to the event counts to all time points in the range <code>[start, end)</code>. The final result of each <code>book</code> call is exactly the max count of a single time in the whole range of <code>[1, 1e9)</code>.</p>
<p>For such kind of problem that increases all counts in some ranges by some constant values several times and asks to obtain all counts for those time points,  we have a very classic solution called <a href="https://en.wikipedia.org/wiki/Sweep_line_algorithm"><strong>sweep-line algorithm</strong></a>: instead of keeping all values of counts in a traditional way, we use a <em>differential array</em> to represent the change that occurs at each time point. In this problem, we will increase the count by 1 at point <code>start</code> and decrease the count by 1 at point <code>end</code>. After enumerating all booked events and updating the differential array, we can simulate scanning the <em>differential array</em> with a vertical sweep-line from the origin time point <code>0</code> to the maximum <code>1e9</code> and obtain the <em>prefix sum</em> at each time point <code>t</code>, which is also the event count of time <code>t</code>. All we need to do now is find the maximum value of such counts when we scan the array.</p>
<h4 id="algorithm">Algorithm</h4>
<ol>
<li>Initialize a HashMap <code>diff</code> as empty. We use a HashMap here instead of an array because the times given by the inputs are sparse as there are at most 400 calls of <code>book()</code> function, we don't have to create records for all numbers in <code>[1, 1e9)</code>. </li>
<li>Each time we book a new event <code>[start, end)</code></li>
</ol>
<ul>
<li>Update the <code>diff[start]</code> by adding 1 while <code>diff[end]</code> by subtracting 1.</li>
<li>Initialize an integer <code>cur = 0</code> to represent the number of intervals at the current time</li>
<li>Enumerate all times that have records in <code>diff</code> in order, accumulate the corresponding value to <code>cur</code>, and record the max value of <code>cur</code> during our enumeration, which is the result of <code>book()</code> call.</li>
</ul>
<iframe src="https://leetcode.com/playground/YW5ownfr/shared" frameborder="0" width="100%" height="361" name="YW5ownfr"></iframe>
<h4 id="complexityanalysis">Complexity Analysis</h4>
<p>Let $N$ be the number of events booked.</p>
<ul>
<li><p>Time Complexity: $O(N^2)$. For each new event, we update the changes at two points in $O(\log&#123;N&#125;)$ because we keep the HashMap in sorted order. Then we traverse <code>diff</code> in $O(N)$ time.</p></li>
<li><p>Space Complexity: $O(N)$, the size of <code>diff</code>.</p></li>
</ul>
<hr>
<h3 id="approach2segmenttree">Approach 2: Segment Tree</h3>
<h4 id="intuition-1">Intuition</h4>
<p>If we use an array <code>vals</code> with length <code>1e9</code> to represent how many events (intervals) covering a time <code>t</code>, each time a new event <code>[start, end)</code> is added, we just need to increase all values in the subarray of <code>vals</code> from index <code>start</code> to <code>end-1</code> by 1, and then return the max value in <code>val</code>.</p>
<p>A segment tree with <em>lazy tags</em> is often used in this scenario to update scalar data (e.g., max, min, sum, etc.) of a subarray quickly. In this problem, we can use a <code>TreeNode</code> to store the max numbers of intervals in a time range <code>[L, R]</code>. A <code>TreeNode</code> has the following fields:</p>
<ul>
<li><code>L</code> and <code>R</code>: the end points of the interval represented by this <code>TreeNode</code>.</li>
<li><code>val</code>: the max number of events at a time included in this range <code>[L, R]</code></li>
<li><code>lazy</code>: the number of events covering all times in the range. As all numbers that belong to this range will be added by some increment, we don't have to propagate the base increment to every time in the interval, all we need to do is putting the number in this <code>lazy</code> field. We only update <code>val</code> by adding <code>lazy</code> when requested to query the max numbers of intervals in <code>[L, R]</code>.</li>
<li><code>left</code> and <code>right</code>: The left and right child nodes of this node, should represent the range <code>[L, M]</code> and <code>[M + 1, R]</code> respectively unless <code>left = right</code>, <code>M = (L + R) / 2</code> here.</li>
</ul>
<h4 id="algorithm-1">Algorithm</h4>
<p>Each time adding a new event <code>[start, end)</code>, we start from the root node, which represents the time interval <code>[0, C]</code>, where <code>C</code> is the largest possible time and equals to <code>1e9</code> in this problem, check if <code>[start, end - 1]</code> has any intersection with current range <code>[L, R]</code> (<code>[0, C]</code> for the root node), and update those nodes recursively:</p>
<ol>
<li>If <code>L > end - 1</code> or <code>R < start</code>, no elements in <code>[start, end - 1]</code> are included in current node, just return.</li>
<li>If <code>start <= L</code> and <code>R >= end - 1</code>, the range represented by this node is completely contained in <code>[start, end - 1]</code>. All elements in the range will be added by 1, so we just need to increase its <code>lazy</code> and <code>val</code> by 1 and stop.</li>
<li>Otherwise, only partial numbers in this range are coverd by <code>[start, end)</code>. We just go to the two child nodes and repeat the checking steps above to update them. After updating data in child nodes, don't forget to update <code>val</code> of our current node by <code>lazy + max(left.val, right.val)</code>, because the max numbers must come from either left or right half of the range, plus the number shared by all elements in the interval, which is stored in <code>lazy</code>.</li>
<li>The <code>val</code> of the root node is exactly the answer we want.</li>
</ol>
<h4 id="implementation">Implementation</h4>
<p>As we discussed before, the input endpoints are sparse. We don't have to create TreeNode for all intervals in the beginning. We can create a node dynamically when needed. Besides, we don't need to define a <code>TreeNode</code> class, instead, we can represent them by hashmap with unique <code>idx</code>s as keys and specify values at key <code>2 * idx</code> and <code>2 * idx + 1</code> as its left and right child nodes for any <code>idx > 0</code>.</p>
<iframe src="https://leetcode.com/playground/T3LjRRty/shared" frameborder="0" width="100%" height="500" name="T3LjRRty"></iframe>
<h4 id="complexityanalysis-1">Complexity Analysis</h4>
<p>Let $N$ be the number of events booked and $C$ be the largest time (i.e., $10^9$ in this problem)</p>
<ul>
<li>Time Complexity: $O(N \log&#123;C&#125;)$. The max possible depth of the segment tree is $\log&#123;C&#125;$. At most $O(\log&#123;C&#125;)$ nodes will be visited in each <code>update</code> operation. Thus, the time complexity of booking $N$ new events is $O(N \log&#123;C&#125;)$.</li>
<li>Space Complexity: $O(N \log&#123;C&#125;)$. Instead of creating a segment tree of $4C$ at first, we create tree nodes dynamically when needed. Every time <code>update</code> is called, we create at most $O(\log&#123;C&#125;)$ nodes because the max depth of the segment tree is $\log&#123;C&#125;$.</li>
</ul>
<hr>
<h3 id="approach3balancedtree">Approach 3: Balanced Tree</h3>
<h4 id="intuition-2">Intuition</h4>
<p>Inspired by Approach 2, what if we keep all consecutive and disjoint intervals in a sorted container? We mark those intervals with the number of events occurring during it. When we are asked to book a new event <code>[start, end)</code>, find which intervals the two endpoints <code>start</code> and <code>end</code> are located in, and split the intervals by <code>start</code> and <code>end</code> to create new smaller intervals. After that, we can increase the number of events for those intervals within <code>start</code> and <code>end</code> by 1.</p>
<p>For example, assume we have a time interval <code>[0, 21)</code> in the beginning without any booked event. We mark the interval as 0. Then,</p>
<ol>
<li>Add a new event <code>[0, 11)</code>, then we split the interval into <code>[0,11)</code> and <code>[11,21)</code>, and mark <code>[0, 11)</code> as 1.</li>
<li>Add another new event <code>[5, 6)</code>, then we split the interval <code>[0,11)</code> into <code>[0, 5)</code> and <code>[5, 11)</code>,  <code>[11, 21)</code> into <code>[11, 16)</code> and <code>[16, 21)</code>, then we increase the events in  <code>[5, 11)</code> and <code>[11, 21)</code> by 1. </li>
</ol>
<p>The process is shown in the following picture:</p>
<p><img src="https://leetcode.com/articles/Documents/732/732_odt.drawio.svg" alt referrerpolicy="no-referrer"></p>
<p>With the help of those sorted intervals, we can precisely locate those intervals contained in a given <code>[start, end)</code> and increase the events in them by 1. Now, it is much easier to know the events in different time slots and find the max one.</p>
<h4 id="algorithm-2">Algorithm</h4>
<p>To keep all intervals mentioned above sorted, we first use a <strong>balanced tree</strong> as a container initialized with the largest time range <code>[1, 1e9)</code>, which has no events, that is, we have <code>intervals = [[1, 1e9)]</code> at first. All intervals are stored in the array <code>intervals</code> in the form of <code>[left, right)</code>.</p>
<p>When we need to book a new event <code>[start, end)</code>:</p>
<ol>
<li>Binary search all starting points in <code>intervals</code> to find the first interval <code>[L1, R1)</code> that has <code>L1 >= start</code>, then we split the interval into <code>[L1, start)</code> and <code>[start, R1)</code>, keep the events in them the same as the origin interval <code>[L1, R1)</code>, and put them back in <code>intervals</code> container.</li>
<li>Similarly, perform a binary search to get the first <code>[L2, R2)</code> that satisfies <code>L2 <= end</code>, split it into<code>[L2, start)</code> and <code>[start, R2)</code> and inserting them into <code>intervals</code>.</li>
<li>For all non-empty intervals between <code>[start, R1)</code> and <code>[start, R1)</code> inclusively in <code>intervals</code>, increase the events of them by 1 as we added a new event in time <code>[start, end)</code> just now. Because only the number of events in those intervals are updated, to get the max number of events now, we just need to compare the last max number of events with them.</li>
</ol>
<h4 id="implementation-1">Implementation</h4>
<p>The balanced tree container has different implementations in different languages. We use <code>map</code> in C++, <code>TreeMap</code> in java and <code>SortedList</code> in Python to mimic how a balanced tree behaves.</p>
<p>And also, we can maintain only starting points of intervals without their end points, because all intervals are consecutive, the end point of an interval is also the starting point of the next one.</p>
<iframe src="https://leetcode.com/playground/iTAt92jt/shared" frameborder="0" width="100%" height="500" name="iTAt92jt"></iframe>
<h4 id="complexityanalysis-2">Complexity Analysis</h4>
<p>Let $N$ be the number of events booked.</p>
<ul>
<li>Time Complexity: $O(N^2)$  in the worst case. For each new <code>[start, end)</code>, we find the intervals that contains point <code>start</code> and <code>end</code> in $O(\log&#123;N&#125;)$ time, split and add new intervals in $O(\log&#123;N&#125;)$ time. We increase at most 2 new intervals each time, so the size of <code>intervals</code>(or <code>starts</code>) is at most $2N+1$. Finally, we enumerate all intervals contained in <code>[start, end)</code> to get the max number of events, which takes $O(N)$ time. Therefore, the overall time complexity of booking $N$ events is $O(N^2)$.</li>
</ul>
<p>Though the time complexity looks not ideal in the worst case, if the given <code>[start, end)</code> is distributed uniformly, the time complexity is $O(N\log\log N)$ (See also: <a href="https://docs.rs/chtholly_tree/latest/chtholly_tree/">Crate <code>chtholly_tree</code></a>). The proof is not easy so we ignore it here.</p>
<ul>
<li>Space Complexity: $O(N)$, the size of <code>intervals</code>(or <code>starts</code>) is at most $2N+1$ as we analyzed before.</li>
</ul>  
</div>
            