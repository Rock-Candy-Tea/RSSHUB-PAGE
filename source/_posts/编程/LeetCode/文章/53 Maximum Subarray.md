
---
title: '53. Maximum Subarray'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://picsum.photos/400/300?random=2931'
author: LeetCode
comments: false
date: Wed, 24 Mar 2021 00:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2931'
---

<div>   
<p>Given an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.</p>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [4,-1,2,1] has the largest sum = 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= nums.length <= 3 * 10<sup>4</sup></code></li>
<li><code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code></li>
</ul>

<p> </p>
<strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.<p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach1optimizedbruteforce">Approach 1: Optimized Brute Force</h4>
<p><strong>Intuition</strong></p>
<p>This algorithm doesn't reliably run under the time limit here on LeetCode. We'll still look briefly at it though, as in an interview scenario it would be a great start if you're struggling to come up with a better approach.</p>
<p>Calculate the sum of all subarrays, and keep track of the best one. To actually generate all subarrays would take $$O(N^3)$$ time, but with a little optimization, we can achieve brute force in $$O(N^2)$$ time. The trick is to recognize that all of the subarrays starting at a particular value will share a common prefix.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize a variable <code>maxSubarray = -infinity</code> to keep track of the best subarray. We need to use negative infinity, not 0, because it is possible that there are only negative numbers in the array.</p></li>
<li><p>Use a <code>for</code> loop that considers each index of the array as a starting point.</p></li>
<li><p>For each starting point, create a variable <code>currentSubarray = 0</code>. Then, loop through the array from the starting index, adding each element to <code>currentSubarray</code>. Every time we add an element it represents a possible subarray - so continuously update <code>maxSubarray</code> to contain the maximum out of the <code>currentSubarray</code> and itself.</p></li>
<li><p>Return <code>maxSubarray</code>. </p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/YZ2Sq9un/shared" frameborder="0" width="100%" height="293" name="YZ2Sq9un"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(N^2)$$, where $$N$$ is the length of <code>nums</code>.</p>
<p>We use 2 nested <code>for</code> loops, with each loop iterating through <code>nums</code>.</p></li>
<li><p>Space complexity: $$O(1)$$</p>
<p>No matter how big the input is, we are only ever using 2 variables: <code>ans</code> and <code>currentSubarray</code>. </p></li>
</ul>
<p><br></p>
<h4 id="approach2dynamicprogrammingkadanesalgorithm">Approach 2: Dynamic Programming, Kadane's Algorithm</h4>
<p><strong>Intuition</strong></p>
<p>Whenever you see a question that asks for the maximum or minimum of something, consider Dynamic Programming as a possibility. The difficult part of this problem is figuring out when a negative number is "worth" keeping in a subarray. This question in particular is a popular problem that can be solved using an algorithm called <a href="https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm">Kadane's Algorithm</a>. If you're good at problem solving though, it's quite likely you'll be able to come up with the algorithm on your own. This algorithm also has a very greedy-like intuition behind it.</p>
<p>Let's focus on one important part: where the optimal subarray <strong>begins</strong>. We'll use the following example.</p>
<p><code>nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]</code></p>
<p>We can see that the optimal subarray couldn't possibly involve the first 3 values - the overall sum of those numbers would always <em>subtract</em> from the total. Therefore, the subarray either starts at the first <code>4</code>, or somewhere further to the right.</p>
<p>What if we had this example though?</p>
<p><code>nums = [-2,1000000000,-3,4,-1,2,1,-5,4]</code></p>
<p>We need a general way to figure out when a part of the array is <strong>worth</strong> keeping.</p>
<p>As expected, any subarray whose sum is <em>positive</em> is worth keeping. Let's start with an empty array, and iterate through the input, adding numbers to our array as we go along. Whenever the sum of the array is negative, we know the entire array is not worth keeping, so we'll reset it back to an empty array.</p>
<p>However, we don't actually need to build the subarray, we can just keep an integer variable <code>current_subarray</code> and add the values of each element there. When it becomes negative, we reset it to 0 (an empty array).</p>
<p>!?!../Documents/53<em>Maximum</em>Subarray.json:960,540!?!</p>
<p><strong>Algorithm</strong></p>
<ol>
<li><p>Initialize 2 integer variables. Set both of them equal to the first value in the array.</p>
<ul>
<li><code>currentSubarray</code> will keep the running count of the current subarray we are focusing on.</li>
<li><code>maxSubarray</code> will be our final return value. Continuously update it whenever we find a bigger subarray.</li></ul></li>
<li><p>Iterate through the array, starting with the 2nd element (as we used the first element to initialize our variables). For each number, add it to the <code>currentSubarray</code> we are building. If <code>currentSubarray</code> becomes negative, we know it isn't worth keeping, so throw it away. Remember to update <code>maxSubarray</code> every time we find a new maximum.</p></li>
<li><p>Return <code>maxSubarray</code>.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<p>A clever way to update <code>currentSubarray</code> is using <code>currentSubarray = max(num, currentSubarray + num)</code>. If <code>currentSubarray</code> is negative, then <code>num > currentSubarray + num</code>.</p>
<iframe src="https://leetcode.com/playground/DTqpuZzF/shared" frameborder="0" width="100%" height="344" name="DTqpuZzF"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(N)$$, where $$N$$ is the length of <code>nums</code>.</p>
<p>We iterate through every element of <code>nums</code> exactly once.</p></li>
<li><p>Space complexity: $$O(1)$$</p>
<p>No matter how long the input is, we are only ever using 2 variables: <code>currentSubarray</code> and <code>maxSubarray</code>. </p></li>
</ul>
<p><br></p>
<hr>
<h4 id="approach3divideandconqueradvanced">Approach 3: Divide and Conquer (Advanced)</h4>
<p><strong>Intuition</strong></p>
<p>This approach is slower than the second approach and uses more space, but it's still a nice and different way to approach the problem. In an interview, sometimes you may be asked for alternative ways to solve a problem - and divide and conquer is an extremely common type of algorithm. This solution will make use of recursion - if you aren't familiar with recursion, check out the <a href="https://leetcode.com/explore/featured/card/recursion-i/">recursion explore card</a>.</p>
<p>Divide and conquer algorithms involve splitting up the input into smaller chunks until they're small enough to be easily solved, and then combining the solutions to get the final overall solution. If you're unfamiliar with them, check out <a href="https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2897/">this explore card</a>. </p>
<p>If we were to split our input in half, then logically the optimal subarray either:</p>
<ul>
<li>Uses elements only from the left side</li>
<li>Uses elements only from the right side</li>
<li>Uses a combination of elements from both the left and right side</li>
</ul>
<p>Thus, the answer is simply the largest of:</p>
<ul>
<li>The maximum subarray contained only in the left side</li>
<li>The maximum subarray contained only in the right side</li>
<li>The maximum subarray that can use elements from both sides</li>
</ul>
<p>Finding the maximum subarray from the left and right half is straightforward - just recurse using the respective half of the array. So, the hard part is figuring out how to find the best subarray that uses elements from both sides. Lets use a smaller example, <code>nums = [5, -2, 1, -3, 4, -2, 1]</code>. Since we want to use elements from both sides, we also must use the middle element, <code>-3</code>. Now, we can also take from the left and the right, but every element must be connected to the middle (since we're still forming a subarray). </p>
<p>The fact that every element must be connected to the middle actually makes our lives a lot easier - every subarray we consider <strong>must</strong> contain the element immediately beside the center, which means there are only as many subarrays as there are elements. In our example, the right side is <code>[4, -2, 1]</code>. There are only 3 subarrays to consider - <code>[4]</code>, <code>[4, -2]</code>, and <code>[4, -2, 1]</code>. To find the best chain of elements we can take from a half, iterate from the middle to the end (start of the array for the left half) and continuously update some counter <code>curr</code>.</p>
<p>!?!../Documents/53<em>Maximum</em>Subarray_2.json:960,540!?!</p>
<p><strong>Algorithm</strong></p>
<p>Now that we know how to find the best subarray containing elements from both sides of any given array, the algorithm is as follows:</p>
<ol>
<li><p>Define a helper function that we will use for recursion.</p>
<ul>
<li>This function will take an input <code>left</code> and <code>right</code>, which defines the bounds of the array. The return value of this function will be the best possible subarray for the array that fits between <code>left</code> and <code>right</code>.</li>
<li>If <code>left > right</code>, we have an empty array. Return negative infinity.</li>
<li>Find the midpoint of our array. This is <code>(left + right) / 2</code>, rounded down. Using this midpoint, find the best possible subarray that uses elements from both sides of the array with the algorithm detailed in the animation above.</li>
<li>The best subarray using elements from both sides is only 1 of 3 possibilities. We still need to find the best subarray using only the left or right halves. So, call this function again, once with the left half, and once with the right half.</li>
<li>Return the largest of the 3 values - the best left half sum, the best right half sum, and the best combined sum.</li></ul></li>
<li><p>Call our helper function with the entire input array (<code>left = 0</code>, <code>right = length - 1</code>). This is our final answer, so return it.</p></li>
</ol>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/RoGrNEAu/shared" frameborder="0" width="100%" height="500" name="RoGrNEAu"></iframe>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time complexity: $$O(N \cdot \log N)$$, where $$N$$ is the length of <code>nums</code>.</p>
<p>On our first call to <code>findBestSubarray</code>, we use for loops to visit every element of <code>nums</code>. Then, we split the array in half and call <code>findBestSubarray</code> with each half. Both those calls will then iterate through every element in that half, which combined is every element of <code>nums</code> again. Then, both those halves will be split in half, and 4 more calls to <code>findBestSubarray</code> will happen, each with a quarter of <code>nums</code>. As you can see, every time the array is split, we still need to handle every element of the original input <code>nums</code>. We have to do this $$\log N$$ times since that's how many times an array can be split in half.</p></li>
<li><p>Space complexity: $$O(\log N)$$, where $$N$$ is the length of <code>nums</code>.</p>
<p>The extra space we use relative to input size is solely occupied by the recursion stack. Each time the array gets split in half, another call of <code>findBestSubarray</code> will be added to the recursion stack, until calls start to get resolved by the base case - remember, the base case happens at an empty array, which occurs after $$\log N$$ calls.</p></li>
</ul>
<p><br></p>
<hr>  
</div>
            