
---
title: '2007. Find Original Array From Doubled Array'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=8564'
author: LeetCode
comments: false
date: Thu, 28 Jul 2022 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8564'
---

<div>   
<p>An integer array <code>original</code> is transformed into a <strong>doubled</strong> array <code>changed</code> by appending <strong>twice the value</strong> of every element in <code>original</code>, and then randomly <strong>shuffling</strong> the resulting array.</p>

<p>Given an array <code>changed</code>, return <code>original</code><em> if </em><code>changed</code><em> is a <strong>doubled</strong> array. If </em><code>changed</code><em> is not a <strong>doubled</strong> array, return an empty array. The elements in</em> <code>original</code> <em>may be returned in <strong>any</strong> order</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> changed = [1,3,4,2,6,8]
<strong>Output:</strong> [1,3,4]
<strong>Explanation:</strong> One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> changed = [6,3,0,1]
<strong>Output:</strong> []
<strong>Explanation:</strong> changed is not a doubled array.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> changed = [1]
<strong>Output:</strong> []
<strong>Explanation:</strong> changed is not a doubled array.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= changed.length <= 10<sup>5</sup></code></li>
<li><code>0 <= changed[i] <= 10<sup>5</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>We need to find if the given array is <code>doubled</code> array or not. In a <code>doubled</code> array, for every element <code>X</code> in the array, we should either have <code>2X</code> or <code>X/2</code> in the array.</p>
<p>This implies that in the <code>doubled</code> array, for every element <code>X</code> we will have to check for two options and if we can pair up all the elements using these options then we can deduce that the array is doubled. This approach is, however not efficient as well as complicated. The complexity of the above approach lies in the two options at each step, can we do something to make it easy to choose the transition from an element? Can we choose such an element say <code>X</code> that makes it trivial to choose one of <code>X/2</code> and <code>2X</code>? </p>
<p>If <code>X</code> is the smallest element in the array then element <code>X/2</code> will not exist in the array, hence we will have to check for element <code>2X</code>. Similarly, if <code>X</code> is the greatest element in the array then element <code>2X</code> will not exist in the array, hence we will have to check for <code>X/2</code> only. Therefore, the trick is to go for the smallest or greatest element always because this way we will have only one option to go for. In the two approaches below we chose the smallest element always.
<br></p>
<hr>
<h4 id="approach1sorthashmap">Approach 1: Sort + HashMap</h4>
<p><strong>Intuition</strong></p>
<p>We need to pair up elements in the array as explained above. Thus, the first validation we should do is, if the array size is even or not. If it's not we cannot have an answer. </p>
<p>Now, as per the above discussion, we need to find the smallest element at each iteration. Hence, we can sort the original array in increasing order, then iterating from left to right will provide us with the smallest element. Once we got the smallest element say <code>X</code> we need to check if the element <code>2X</code> exists in the array or not. To check this, we can store the array elements in a HashMap for an efficient lookup at each iteration. If the element <code>2X</code> is present in the HashMap we will decrement its count else the element <code>X</code> cannot be paired with any other element and hence we return an empty array.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Return empty array <code>&#123;&#125;</code> if the size of the given array <code>changed</code> is odd.</li>
<li>Sort the array <code>changed</code> in increasing order.</li>
<li>Store the element count in the HashMap <code>freq</code>. Iterate over the elements in the array <code>changed</code> and increment the count corresponding to the element in the map.</li>
<li>Iterate over the elements in the array <code>changed</code>, for each element <code>num</code>:<ul>
<li>Check if the count of <code>num</code> in the map <code>freq</code> is more than zero or not.</li>
<li>Decrement the frequency of <code>num</code> in the map.</li>
<li>Check if the count of <code>twiceNum</code> (<code>2 * num</code>)  in the map <code>freq</code> is positive or not. If it is then decrement the count and add the element <code>num</code> to the answer array <code>original</code>.</li></ul></li>
</ol>
<ul>
<li>If it is not, then return an empty <code>&#123;&#125;</code> array.</li>
</ul>
<ol>
<li>Return the array <code>original</code>.</li>
</ol>
<p><strong>Note:</strong> This approach requires modifying the input. In an interview setting, we should first confirm it with the interviewer.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/SZvwKqiG/shared" frameborder="0" width="100%" height="500" name="SZvwKqiG"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here, $$N$$ is the size of the given array.</p>
<ul>
<li><p>Time complexity: $$O(N\log N)$$</p>
<p>Sorting the array <code>changed</code> will take $$O(N\log N)$$ and then we iterate over it which will take $$O(N)$$ time. Hence, the time complexity is equal to $$O(N\log N)$$.</p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>Storing the element frequency in the HashMap <code>freq</code> will require $$O(N)$$ space. Some space will be used for sorting the list. The space complexity of the sorting algorithm depends on the implementation of each programming language. For instance, in Java, the <code>Arrays.sort()</code> for primitives is implemented as a variant of the quicksort algorithm whose space complexity is $$O(\log N)$$. In C++, the common implementation of <code>std::sort()</code> function provided by STL is a hybrid of Quick Sort, Heap Sort, and Insertion Sort and has a worst-case space complexity of $$O(\log N)$$. Thus, the use of the inbuilt <code>std::sort()</code> function might add up to $$O(\log N)$$ to space complexity.
<br></p></li>
</ul>
<hr>
<h4 id="approach2countingsort">Approach 2: Counting Sort</h4>
<p><strong>Intuition</strong></p>
<p>Similar to the previous approach, we will find the smallest element always. The only difference here is that instead of sorting the original array using built-in sorting functions we will use counting sort. We will use an array <code>freq</code> to store the frequency of each element in the given array. Now, we will iterate from <code>0</code> to the maximum value that is present in the array. For each element <code>num</code>  we will follow the exact same process as we did previously, we check for the element <code>2 * num</code> and proceed accordingly.</p>
<p>Note that for every element we will be iterating once however there might be multiple instances of it in the original array. Hence, once we iterate over an element we will decrement the counter to reiterate it, this time if the instances are over the <code>if</code> condition will fail and we move to the next number.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Return empty array <code>&#123;&#125;</code> if the size of the given array <code>changed</code> is odd.</li>
<li>Find the maximum element present in the array <code>changed</code>  and store it in the variable <code>maxNum</code>.</li>
<li>Declare the array <code>freq</code> with size <code>2 * maxNum + 1</code> and initialize the indices to <code>0</code>. This is because we will iterate over numbers upto <code>maxNum</code> and hence we might check for <code>2 * maxNum</code> in the <code>freq</code> array.</li>
<li>Iterate over the numbers from <code>0</code> to <code>maxNum</code>, for each element <code>num</code>:<ul>
<li>Check if the count of <code>num</code> in the map <code>freq</code> is more than zero or not.</li>
<li>Decrement the frequency of <code>num</code> in the map.</li>
<li>Check if the count of <code>twiceNum</code> (<code>2 * num</code>)  in the map <code>freq</code> is positive or not. If it is then decrement the count and add the element <code>num</code> to the answer array <code>original</code>. Also decrement the value of <code>num</code> to reiterate it.</li></ul></li>
</ol>
<ul>
<li>If it is not, then return an empty <code>&#123;&#125;</code> array.</li>
</ul>
<ol>
<li>Return the array <code>original</code>.</li>
</ol>
<p>The following slideshow demonstrates the algorithm:</p>
<p>!?!../Documents/2007<em>Find</em>Original<em>Array</em>From<em>Doubled</em>Array.json:960,720!?! <br></p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/kgMS7VbR/shared" frameborder="0" width="100%" height="500" name="kgMS7VbR"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here, $$N$$ is the size of the given array, and $$K$$ is equal to the maximum number in the array <code>changed</code>.</p>
<ul>
<li><p>Time complexity: $$O(N + K)$$</p>
<p>The time to find the greatest element in the array is $$O(N)$$, similarly storing the element frequency in the array <code>freq</code> is $$O(N)$$. We iterate over the numbers from $$0$$ to $$K$$ to pair up the elements, hence the time required will be $$O(K)$$. Hence, the total time complexity will be equal to $$(N + K)$$.</p></li>
<li><p>Space complexity: $$O(K)$$</p>
<p>The space required for the array <code>freq</code> will be equal to $$O(K)$$. Therefore, the space complexity will be equal to $$O(K)$$.
<br></p></li>
</ul>
<hr>  
</div>
            