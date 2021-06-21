
---
title: '658. Find K Closest Elements'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=7091'
author: LeetCode
comments: false
date: Fri, 28 May 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7091'
---

<div>   
<p>Given a <strong>sorted</strong> integer array <code>arr</code>, two integers <code>k</code> and <code>x</code>, return the <code>k</code> closest integers to <code>x</code> in the array. The result should also be sorted in ascending order.</p>

<p>An integer <code>a</code> is closer to <code>x</code> than an integer <code>b</code> if:</p>

<ul>
<li><code>|a - x| < |b - x|</code>, or</li>
<li><code>|a - x| == |b - x|</code> and <code>a < b</code></li>
</ul>

<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [1,2,3,4,5], k = 4, x = 3
<strong>Output:</strong> [1,2,3,4]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [1,2,3,4,5], k = 4, x = -1
<strong>Output:</strong> [1,2,3,4]
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= k <= arr.length</code></li>
<li><code>1 <= arr.length <= 10<sup>4</sup></code></li>
<li><code>arr</code> is sorted in <strong>ascending</strong> order.</li>
<li><code>-10<sup>4</sup> <= arr[i], x <= 10<sup>4</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach1sortwithcustomcomparator">Approach 1: Sort With Custom Comparator</h4>
<p><strong>Intuition</strong></p>
<p>This first approach is the most intuitive one that most people probably think of first - check every number in <code>arr</code> for its distance from <code>x</code> and sort the numbers by this criterion. Then, the answer will be the first <code>k</code> elements of our new sorted array.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Create a new array <code>sortedArr</code>, that is <code>arr</code> sorted with a custom comparator. The comparator should be <code>abs(x - num)</code> for each <code>num</code> in <code>arr</code>. Sorting the array in ascending order means that the first <code>k</code> elements will be the <code>k</code> closest elements to <code>x</code>.</p></li>
<li><p>We also have to sort the "sorted" array, since the problem wants our output in ascending order. Return the first <code>k</code> elements of <code>sortedArr</code>, sorted by value, in ascending order.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/jbK2mJxL/shared" frameborder="0" width="100%" height="378" name="jbK2mJxL"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the length of <code>arr</code>,</p>
<ul>
<li><p>Time complexity: $$O(N \cdot \log(N) + k \cdot \log(k))$$.</p>
<p>To build <code>sortedArr</code>, we need to sort every element in the array by a new criteria: <code>x - num</code>. This costs $$O(N \cdot \log(N))$$. Then, we have to sort <code>sortedArr</code> again to get the output in ascending order. This costs $$O(k \cdot \log(k))$$ time since <code>sortedArr.length</code> is only <code>k</code>.</p></li>
<li><p>Space complexity: $$O(N)$$.</p>
<p>Before we slice <code>sortedArr</code> to contain only <code>k</code> elements, it contains every element from <code>arr</code>, which requires $$O(N)$$ extra space. Note that we can use less space if we sort the input in place.</p></li>
</ul>
<p><br></p>
<h4 id="approach2binarysearchslidingwindow">Approach 2: Binary Search + Sliding Window</h4>
<p><strong>Intuition</strong></p>
<p>Every time you see a problem that involves a sorted array, you should consider binary search. In the previous approach, we considered every single number from <code>arr</code> as a potential candidate for the final output. However, when <code>arr.length</code> is very large, and <code>k</code> is very small, we do not care about a vast majority of the numbers in <code>arr</code>, and we should avoid looking at them.</p>
<p>Let's start by finding the closest number to <code>x</code> in <code>arr</code>. Logically, the second closest number to <code>x</code> must be directly beside the first number, either to the left or right. Then, the third closest number to <code>x</code> must be either to the left of the first number or to the right of the second number. This pattern continues, and is true because the input is sorted.</p>
<p>Using two pointers, we can maintain a sliding window that will expand to contain the <code>k</code> closest elements to <code>x</code>. Let's use binary search to efficiently find the closest number to <code>x</code> in <code>arr</code>, and start our pointers there. Then, we should expand our window by moving the pointers either left or right depending on which number is closer to <code>x</code>.</p>
<p>!?!../Documents/658<em>K</em>Closest_1.json:960,540!?!</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>As a base case, if <code>arr.length == k</code>, return <code>arr</code>.</p></li>
<li><p>Use binary search to find the index of the closest element to <code>x</code> in <code>arr</code>. Initailize two pointers <code>left</code> and <code>right</code>, with <code>left</code> set equal to this index, and <code>right</code> equal to this index plus one.</p></li>
<li><p>While the window's size is less than <code>k</code>, check which number is closer to <code>x</code>: <code>arr[left]</code> or <code>arr[right]</code>. Whichever pointer has the closer number, move that pointer towards the edge to include that element in our output.</p></li>
<li><p>Return the elements inside <code>arr</code> contained within the window defined between <code>left</code> and <code>right</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<p>In Python, the <a href="https://docs.python.org/3/library/bisect.html">bisect</a> module provides super handy functions that does binary search for us.</p>
<iframe src="https://leetcode.com/playground/AJ7X8Gqm/shared" frameborder="0" width="100%" height="500" name="AJ7X8Gqm"></iframe>
<p>Given $$N$$ as the length of <code>arr</code>,</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(\log(N) + k)$$.</p>
<p>The initial binary search to find where we should start our window costs $$O(\log(N))$$. Our sliding window initially starts with size 0 and we expand it one by one until it is of size <code>k</code>, thus it costs $$O(k)$$ to expand the window.</p></li>
<li><p>Space complexity: $$O(1)$$</p>
<p>We only use integer variables <code>left</code> and <code>right</code> that are $$O(1)$$ regardless of input size. Space used for the output is not counted towards the space complexity.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3binarysearchtofindtheleftbound">Approach 3: Binary Search To Find The Left Bound</h4>
<p><strong>Intuition</strong></p>
<p>We can actually find the bounds of our sliding window much faster - and independent of <code>k</code>! First of all, what is the biggest index the left bound could be? If there needs to be <code>k</code> elements, then the left bound's upper limit is <code>arr.length - k</code>, because if it were any further to the right, you would run out of elements to include in the final answer.</p>
<p>As demonstrated in Approach 2, binary search is typically used to find if an element exists or where an element belongs in a sorted array. The beauty of algorithms lies in how abstract they are - with some clever thinking, we can apply binary search in a unique way to move our <code>left</code> and <code>right</code> pointers closer and closer to the left bound of our answer.</p>
<p>Let's consider two indices at each binary search operation, the usual <code>mid</code>, and some index <code>mid + k</code>. The relationship between these indices is significant because <strong>only one of them could possibly be in a final answer</strong>. For example, if <code>mid = 2</code>, and <code>k = 3</code>, then <code>arr[2]</code> and <code>arr[5]</code> could not possibly both be in the answer, since that would require taking 4 elements <code>[arr[2], arr[3], arr[4], arr[5]]</code>.</p>
<p>This leads us to the question: how do we move our pointers <code>left</code> and <code>right</code>? If the element at <code>arr[mid]</code> is closer to <code>x</code> than <code>arr[mid + k]</code>, then that means <code>arr[mid + k]</code>, as well as every element to the right of it can never be in the answer. This means we should move our <code>right</code> pointer to avoid considering them. The logic is the same vice-versa - if <code>arr[mid + k]</code> is closer to <code>x</code>, then move the left pointer.</p>
<p>!?!../Documents/658<em>K</em>Closest_2.json:960,540!?!</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initalize two variables to perform binary search with, <code>left = 0</code> and <code>right = len(arr) - k</code>.</p></li>
<li><p>Perform a binary search. At each operation, calculate <code>mid = (left + right) / 2</code> and compare the two elements located at <code>arr[mid]</code> and <code>arr[mid + k]</code>. If the element at <code>arr[mid]</code> is closer to <code>x</code>, then move the right pointer. If the element at <code>arr[mid + k]</code> is closer to <code>x</code>, then move the left pointer. Remember, the smaller element always wins when there is a tie.</p></li>
<li><p>At the end of the binary search, we have located the leftmost index for the final answer. Return the subarray starting at this index that contains <code>k</code> elements.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/ENNsnY26/shared" frameborder="0" width="100%" height="480" name="ENNsnY26"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Given $$N$$ as the length of <code>arr</code>,</p>
<ul>
<li><p>Time complexity: $$O(\log(N - k) + k)$$.</p>
<p>Although finding the bounds only takes $$O(\log(N - k))$$ time from the binary search, it still costs us $$O(k)$$ to build the final output.</p>
<p>Both the Java and Python implementations require $$O(k)$$ time to build the result.  However, it is worth noting that if the input array were given as a list instead of an array of integers, then the Java implementation could use the <code>ArrayList.subList()</code> method to build the result in $$O(1)$$ time.  If this were the case, the Java solution would have an (extremely fast) overall time complexity of $$O(\log(N - k))$$.</p></li>
<li><p>Space complexity: $$O(1)$$.</p>
<p>Again, we use a constant amount of space for our pointers, and space used for the output does not count towards the space complexity.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            