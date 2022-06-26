
---
title: '561. Array Partition I'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=8906'
author: LeetCode
comments: false
date: Mon, 06 Jun 2022 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8906'
---

<div>   
<p>Given an integer array <code>nums</code> of <code>2n</code> integers, group these integers into <code>n</code> pairs <code>(a<sub>1</sub>, b<sub>1</sub>), (a<sub>2</sub>, b<sub>2</sub>), ..., (a<sub>n</sub>, b<sub>n</sub>)</code> such that the sum of <code>min(a<sub>i</sub>, b<sub>i</sub>)</code> for all <code>i</code> is <strong>maximized</strong>. Return<em> the maximized sum</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,4,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [6,2,6,5,1,2]
<strong>Output:</strong> 9
<strong>Explanation:</strong> The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= n <= 10<sup>4</sup></code></li>
<li><code>nums.length == 2 * n</code></li>
<li><code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>We are given a list of $$2N$$ integers. We need to group these integers into $$N$$ pairs such that the sum of minimum elements in all pairs is the maximum possible.</p>
<p>The key observation here is that if we have a pair like $$(a, b)$$ such that $$a \leq b$$, then we will add $$a$$ to the answer and $$b$$ cannot be used anymore. Therefore, in each such pair, we will add the value of the smaller element but the greater element will not contribute to the answer.</p>
<p>Suppose $$x$$ is the smallest possible element in the given list. This means that the contribution to the answer for any pair that includes $$x$$ must be $$x$$, irrespective of the paired element. The other element will essentially be wasted. Hence to minimize our losses, we would like to pair $$x$$ with the smallest element other than $$x$$.</p>
<p>The number paired with $$x$$ will be the second smallest element in the given list. Hence, we will pair each element with the closest unpaired number in ascending sorted order. After sorting the given list, the first element can be paired with the second element, the third element can be paired with the fourth, and so on.
<br></p>
<hr>
<h4 id="approach1sorting">Approach 1: Sorting</h4>
<p><strong>Intuition</strong></p>
<p>We will sort the given list using the built-in sorting function. In the sorted list we will pair the first two elements then the next two elements and so on. Therefore, the first element (at index <code>0</code>) will be added to the answer <code>maxSum</code> as it is the minimum of the first two elements. Similarly, the third element in the list (at index <code>2</code>) will be added, and so on. Hence, we will only sum the elements located at the even indices.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Sort the list <code>nums</code>.</li>
<li>Initialize the answer variable <code>maxSum</code> as <code>0</code>.</li>
<li>Iterate over the list <code>nums</code> and add the elements at even indices to <code>maxSum</code>.</li>
<li>Return <code>maxSum</code>.</li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/GUUKkKUM/shared" frameborder="0" width="100%" height="293" name="GUUKkKUM"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here, $$N$$ is the number of pairs that will be produced (i.e., the size of list <code>nums</code> is $$2 \cdot N$$).</p>
<ul>
<li><p>Time complexity: $$O(N \log N)$$</p>
<p>Sorting the list <code>nums</code> of size $$2 \cdot N$$ will take $$O(2 \cdot N \log(2 \cdot N))$$ time which is equivalent to $$O(N \log N)$$, and iterating over the list will take an additional $$O(N)$$ time. Hence, the time complexity is $$O(N \log N)$$.</p></li>
<li><p>Space complexity: $$O(N)$$</p>
<p>The only variable we need is <code>maxSum</code>, which takes $$O(1)$$ space. However, some space will be used for sorting the list  <code>nums</code>. The space complexity of the sorting algorithm depends on the implementation of each programming language. For instance, in Java, the Arrays.sort() for primitives is implemented as a variant of the QuickSort algorithm whose space complexity is $$O(\log N)$$. In C++, sort() function provided by STL is a hybrid of QuickSort, Heap Sort, and Insertion Sort and has a worst-case space complexity of $$O(\log N)$$. Python, on the other hand, uses Timsort, which has a space complexity of $$O(N)$$. Thus, the use of the built-in sort() function could add up to $$O(N)$$ to the space complexity.</p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach2countingsort">Approach 2: Counting Sort</h4>
<p><strong>Intuition</strong></p>
<p>In this approach, we will be sorting the list <code>nums</code> using counting sort. We will store the frequency count for each element in the array <code>elementToCount</code>.</p>
<p>After sorting, we will iterate over all of the elements in sorted order, and add even indexed elements to <code>maxSum</code>. After that, we will iterate over the frequency array and use a boolean variable that flips at each element and is only true when we are on an even indexed element.</p>
<p>Since we are using an array where the element values will be used as indices, we need to ensure that we don't have any negative elements. The elements in the list <code>nums</code> can be negative with a value down to $$-10^4$$. Hence, we will add $$10^4$$ to each element so that all the elements convert to a non-negative value. Therefore, our <code>elementToCount</code> array will need to be of size $$2 * 10^4 + 1$$ to account for the full range of possible values in <code>nums</code>.</p>
<p><strong>Note:</strong></p>
<ul>
<li>We could limit the size of the <code>elementToCount</code> array to the range of numbers in the nums array by performing a single pass to find the minimum and maximum values in nums, but to make the solution easier to follow, we chose to use a fixed value for $$K$$ based on the given problem constraints.</li>
<li>Instead of iterating over every instance of an element in <code>elementToCount</code>. We can find the number of times that an element will be added to the final answer. Since this method doesn't improve the time/space complexity we avoided it to improve the code readability.</li>
</ul>
<p><strong>Algorithm</strong></p>
<ol>
<li>Iterate over each element in the list <code>nums</code> and for each <code>element</code> we will:<ul>
<li>Add the value $$K = 10^4$$ </li>
<li>Increment the frequency corresponding to the above element in the array <code>elementToCount</code>.</li></ul></li>
<li>Initialize the answer variable <code>maxSum</code> as $$0$$. Initialize the variable <code>isEvenIndex</code> as true. This variable will be true when we are at an even position and will be false for odd positions. Since we start with index $$0$$ we have initialized it as true.</li>
<li>Iterate through <code>elementToCount</code>, and for each element:<ul>
<li>Iterate over the instances of <code>element</code> and for each instance:<ul>
<li>If the current element is at an even index, then we will add the value of that element to the <code>maxSum</code>. Since we shifted each element by $$K$$ when creating the frequency array, the element's value is <code>element - K</code>.</li></ul></li>
<li>Decrement the frequency of <code>element</code> in <code>elementToCount</code> by $$1$$.</li>
<li>Flip the value of <code>isEvenIndex</code>. This is because if the current position is even the next will be odd and the variable <code>isEvenIndex</code> should be false in that case and vice versa.</li></ul></li>
<li>Return <code>maxSum</code>.</li>
</ol>
<p>The following slideshow demonstrates this algorithm. For simplicity, the example contains only positive values; hence it does not shift each value by $$10^4$$:</p>
<p>!?!../Documents/561<em>Array</em>Partition_I.json:960,720!?! <br></p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/G6QhieGq/shared" frameborder="0" width="100%" height="500" name="G6QhieGq"></iframe>
<p><strong>Complexity Analysis</strong></p>
<p>Here, $$N$$ is the number of pairs that will be produced i.e., the size of list <code>nums</code> is $$2N$$, and $$K$$ is the range of possible values in nums, which in this problem equals $$2·10^4$$.</p>
<ul>
<li><p>Time complexity: $$O(N + K)$$</p>
<p>First, we iterate over each of the $$2N$$ elements in <code>nums</code> in $$O(2N)$$ time. Then we iterate through the $$2K$$ elements in <code>elementToCount</code> during which we'll have another $$2N$$ frequency count operations for a total of $$O(2K + 2N)$$ time. Hence the total time complexity reduces to $$O(N + K)$$.</p></li>
<li><p>Space complexity: $$O(K)$$</p>
<p>The size of <code>elementToCount</code> needs to be able to accommodate the full range of values in <code>nums</code>, which can be up to $$2K$$. Hence the total space complexity reduces to $$O(K)$$.
<br></p></li>
</ul>
<hr>  
</div>
            