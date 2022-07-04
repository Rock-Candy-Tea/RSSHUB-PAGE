
---
title: '347. Top k Frequent Elements'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/347_rewrite/summary.png'
author: LeetCode
comments: false
date: Sun, 01 May 2022 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/347_rewrite/summary.png'
---

<div>   
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
<li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
<li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>

<p> </p>
<p><strong>Follow up:</strong> Your algorithm's time complexity must be better than <code>O(n log n)</code>, where n is the array's size.</p><p>[TOC]</p>
<h2 id="videosolution">Video Solution</h2>
<hr>
<div class="video-preview"></div>
<div> 
</div>
<h2 id="solutionarticle">Solution Article</h2>
<hr>
<h4 id="approach1heap">Approach 1: Heap</h4>
<p>Let's start from the simple <a href="https://en.wikipedia.org/wiki/Heap_(data_structure)">heap</a> 
approach with $$\mathcal&#123;O&#125;(N \log k)$$
time complexity. To ensure that $$\mathcal&#123;O&#125;(N \log k)$$ is always 
less than $$\mathcal&#123;O&#125;(N \log N)$$, the particular case $$k = N$$ could be 
considered separately and solved in $$\mathcal&#123;O&#125;(N)$$ time. </p>
<p><strong>Algorithm</strong></p>
<ul>
<li><p>The first step is to build a hash map <code>element -> its frequency</code>.
In Java, we use the data structure <code>HashMap</code>.
Python provides dictionary subclass <code>Counter</code> to initialize the hash map we need
directly from the input array.<br>
This step takes $$\mathcal&#123;O&#125;(N)$$ time where <code>N</code> is a number of elements in the list.</p></li>
<li><p>The second step is to build a heap of <em>size k using N elements</em>. 
To add the first <code>k</code> elements takes 
a linear time $$\mathcal&#123;O&#125;(k)$$ in the average case, and
$$\mathcal&#123;O&#125;(\log 1 + \log 2 + … + \log k) = 
\mathcal&#123;O&#125;(log k!) = \mathcal&#123;O&#125;(k \log k)$$ in the worst case.
It's equivalent to
<a href="https://hg.python.org/cpython/file/2.7/Lib/heapq.py#l16">heapify implementation in Python</a>.
After the first <code>k</code> elements we start to push and pop at each step,
<code>N - k</code> steps in total.
The time complexity of heap push/pop 
is $$\mathcal&#123;O&#125;(\log k)$$ and we do it <code>N - k</code> times that means
$$\mathcal&#123;O&#125;((N - k)\log k)$$ time complexity.
Adding both parts up, we get $$\mathcal&#123;O&#125;(N \log k)$$ time 
complexity for the second step.</p></li>
<li><p>The third and the last step is to convert the heap into an output array. 
That could be done in $$\mathcal&#123;O&#125;(k \log k)$$ time.</p></li>
</ul>
<p>In Python, library <code>heapq</code> provides a method <code>nlargest</code>,
which <a href="https://hg.python.org/cpython/file/2.7/Lib/heapq.py#l203">combines the last two steps under the hood</a> 
and has the same $$\mathcal&#123;O&#125;(N \log k)$$ time complexity.</p>
<p><img src="https://leetcode.com/articles/Figures/347_rewrite/summary.png" alt="diff" referrerpolicy="no-referrer"></p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/Bqpwvxv5/shared" frameborder="0" width="100%" height="500" name="Bqpwvxv5"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity : $$\mathcal&#123;O&#125;(N \log k)$$ if $$k < N$$ and $$\mathcal&#123;O&#125;(N)$$
in the particular case of $$N = k$$. That ensures time complexity to be better
than $$\mathcal&#123;O&#125;(N \log N)$$.</p></li>
<li><p>Space complexity : $$\mathcal&#123;O&#125;(N + k)$$ to store the hash map with not more 
$$N$$ elements and a heap with $$k$$ elements.
<br>
<br></p></li>
</ul>
<hr>
<h4 id="approach2quickselecthoaresselectionalgorithm">Approach 2: Quickselect (Hoare's selection algorithm)</h4>
<p>Quickselect is a <a href="https://en.wikipedia.org/wiki/Quickselect">textbook algorthm</a> 
typically used to solve the problems "find <code>k</code><em>th</em> something":
<code>k</code><em>th</em> smallest, <code>k</code><em>th</em> largest, <code>k</code><em>th</em> most frequent, 
<code>k</code><em>th</em> less frequent, etc. Like quicksort, quickselect was developed 
by <a href="https://en.wikipedia.org/wiki/Tony_Hoare">Tony Hoare</a>, 
and also known as <em>Hoare's selection algorithm</em>.</p>
<p>It has $$\mathcal&#123;O&#125;(N)$$ <em>average</em> time complexity and is widely used 
in practice. It worth noting that its worst-case time complexity 
is $$\mathcal&#123;O&#125;(N^2)$$, although the probability of this worst-case 
is negligible.</p>
<p>The approach is the same as for quicksort.</p>
<blockquote>
  <p>One chooses a pivot and defines its position in a sorted array in a 
  linear time using so-called <em>partition algorithm</em>. </p>
</blockquote>
<p>As an output, we have an array where the pivot is on its perfect position
in the ascending sorted array, sorted by the frequency. 
All elements on the left of the pivot are less frequent than the pivot,
and all elements on the right are more frequent or have the
same frequency.</p>
<p>Hence the array is now split into two parts.
If by chance our pivot element took <code>N - k</code><em>th</em> final position, 
then $$k$$ elements on the right are these top $$k$$ 
frequent we're looking for. If not, we can choose one more pivot and 
place it in its perfect position.</p>
<p><img src="https://leetcode.com/articles/Figures/347_rewrite/hoare.png" alt="diff" referrerpolicy="no-referrer"></p>
<p>If that were a quicksort algorithm, one would have to process
both parts of the array. That would result in $$\mathcal&#123;O&#125;(N \log N)$$ time complexity.
In this case, there is no need to deal with both parts since one knows 
in which part to search for <code>N - k</code><em>th</em> less frequent element, and that
reduces the average time complexity to $$\mathcal&#123;O&#125;(N)$$.</p>
<p><strong>Algorithm</strong></p>
<p>The algorithm is quite straightforward :</p>
<ul>
<li><p>Build a hash map <code>element -> its frequency</code> and convert its keys into
the array <code>unique</code> of unique elements. Note that elements are unique, but
their frequencies are <em>not</em>. That means we need a partition algorithm 
that works fine with <em>duplicates</em>. </p></li>
<li><p>Work with <code>unique</code> array. 
Use a partition scheme (please check the next section) to place the pivot 
into its perfect position <code>pivot_index</code> in the sorted array,
move less frequent elements to the left of pivot, 
and more frequent or of the same frequency - to the right.</p></li>
<li><p>Compare <code>pivot_index</code> and <code>N - k</code>.</p>
<ul>
<li><p>If <code>pivot_index == N - k</code>, the pivot is 
<code>N - k</code><em>th</em> most frequent element, and all elements on the right
are more frequent or of the same frequency. 
Return these top $$k$$ frequent elements.</p></li>
<li><p>Otherwise, choose the side of the array to proceed recursively.</p></li></ul></li>
</ul>
<p><img src="https://leetcode.com/articles/Figures/347_rewrite/details.png" alt="diff" referrerpolicy="no-referrer"></p>
<p><strong>Lomuto's Partition Scheme</strong></p>
<p>There is a zoo of partition algorithms. The most simple 
one is <a href="https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme">Lomuto's Partition Scheme</a>, 
and so is what we will use in this article.</p>
<p>Here is how it works:</p>
<ul>
<li><p>Move pivot at the end of the array using swap. </p></li>
<li><p>Set the pointer at the beginning of the array <code>store_index = left</code>.</p></li>
<li><p>Iterate over the array and move all less frequent elements 
to the left
<code>swap(store_index, i)</code>. Move <code>store_index</code> one step to the 
right after each swap.</p></li>
<li><p>Move the pivot to its final place, and return this index.</p></li>
</ul>
<p>!?!../Documents/347_RES.json:1000,556!?!</p>
<iframe src="https://leetcode.com/playground/chUJ7XE5/shared" frameborder="0" width="100%" height="378" name="chUJ7XE5"></iframe>
<p><strong>Implementation</strong></p>
<p>Here is a total algorithm implementation. </p>
<iframe src="https://leetcode.com/playground/36EZRE5t/shared" frameborder="0" width="100%" height="500" name="36EZRE5t"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$\mathcal&#123;O&#125;(N)$$ in the average case, 
$$\mathcal&#123;O&#125;(N^2)$$ in the worst case. 
<a href="https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2871/">Please refer to this card for the good detailed explanation of Master Theorem</a>.
Master Theorem helps to get an average complexity by writing the algorithm cost
as $$T(N) = a T(N / b) + f(N)$$. 
Here we have an example of Master Theorem case III: 
$$T(N) = T \left(\frac&#123;N&#125;&#123;2&#125;\right) + N$$, 
that results in $$\mathcal&#123;O&#125;(N)$$ time complexity.
That's the case of random pivots.</p>
<p>In the worst-case of constantly bad chosen pivots, the problem is 
not divided by half at each step, it becomes just one element less,
that leads to $$\mathcal&#123;O&#125;(N^2)$$ time complexity. 
It happens, for example, if at each step you choose the pivot not 
randomly, but take the rightmost element. 
For the random pivot choice the probability of having such a 
worst-case is negligibly small. </p></li>
<li><p>Space complexity: up to $$\mathcal&#123;O&#125;(N)$$ to store hash map
and array of unique elements.
<br>
<br></p></li>
</ul>
<hr>
<h4 id="furtherdiscussioncouldwedoworstcaselineartime">Further Discussion: Could We Do Worst-Case Linear Time?</h4>
<p>In theory, we could, the algorithm is called 
<a href="https://en.wikipedia.org/wiki/Median_of_medians">Median of Medians</a>.</p>
<p>This method is never used in practice because of two drawbacks:</p>
<ul>
<li><p>It's <em>outperformer</em>. Yes, it works in a linear time $$\alpha N$$, but
the constant $$\alpha$$ is so large that in practice it often works even 
slower than $$N^2$$.  </p></li>
<li><p>It doesn't work with duplicates.
<br>
<br></p></li>
</ul>
<hr>  
</div>
            