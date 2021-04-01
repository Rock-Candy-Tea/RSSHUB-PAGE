
---
title: '34. Find First and Last Position of Element in Sorted Array'
categories: 
 - 编程
 - LeetCode
 - 文章
headimg: 'https://leetcode.com/articles/Figures/34/img1.png'
author: LeetCode
comments: false
date: Wed, 31 Mar 2021 00:00:00 GMT
thumbnail: 'https://leetcode.com/articles/Figures/34/img1.png'
---

<div>   
<p>Given an array of integers <code>nums</code> sorted in ascending order, find the starting and ending position of a given <code>target</code> value.</p>

<p>If <code>target</code> is not found in the array, return <code>[-1, -1]</code>.</p>

<p><strong>Follow up:</strong> Could you write an algorithm with <code>O(log n)</code> runtime complexity?</p>

<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong>Output:</strong> [3,4]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong>Output:</strong> [-1,-1]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> [-1,-1]
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
<li><code>0 <= nums.length <= 10<sup>5</sup></code></li>
<li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
<li><code>nums</code> is a non-decreasing array.</li>
<li><code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code></li>
</ul><p>[TOC]</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="overview">Overview</h4>
<p>Let's briefly look at a brute-force way of solving this problem. Given a target element, we can simply do a linear scan over the entire array to find the first and the last position. The first occurrence will be the first time when we encounter this target. Thereafter, we continue to scan elements until we find one that is greater than the target or until we reach the end of the array. This will help us determine the last position of the target. </p>
<p>The downside of this approach is that it doesn't take advantage of the <em>sorted</em> nature of the array. This linear scan approach has a time complexity of $$O(N)$$ because there are $$N$$ elements in the array. That doesn't sound too bad, right? Well, it does if we compare it to an approach with logarithmic time complexity. We'll look at a <em>binary search-based approach</em> to solve this problem which will take advantage of the sorted nature of the array.</p>
<p><br></p>
<hr>
<h4 id="approachbinarysearch">Approach: Binary Search</h4>
<p><strong>Intuition</strong></p>
<p>Let's review binary search a bit. Given a sorted array, binary search works by looking at the middle element of the given array, and based on the value of the middle element, it decides to discard one half of the array. At each step, we reduce the length of the array to search by half and that is what leads to the logarithmic time complexity of the algorithm. Usually, we employ the binary search algorithm to determine if an element is in a sorted array. Here, we can tweak the binary search algorithm to find the first and the last position of a given element. </p>
<p>Let's look at the basic binary search algorithm one step at a time:</p>
<ul>
<li>We use 2 variables to keep track of the subarray that we are scanning. Let's call them <code>begin</code> and <code>end</code>. Initially, <code>begin</code> is set to <code>0</code> and <code>end</code> is set to the last index of the array.</li>
<li>We iterate until <code>begin</code> is greater than or equal to <code>end</code>.</li>
<li>At each step, we calculate the middle element <code>mid = (begin + end) / 2</code>. We use the value of the middle element to decide which half of the array we need to search. <ul>
<li>If the target that we're searching for has a value lower than the <code>mid</code> element, we discard the right half of the array i.e. <code>end = mid - 1</code>. </li>
<li>If the target that we're searching for has a value higher than the <code>mid</code> element, we discard the left half of the array i.e. <code>begin = mid + 1</code>. </li>
<li>If <code>nums[mid] == element</code>, then we found our target and we return from there.</li></ul></li>
</ul>
<p><strong>Binary Search and Bidirectional Scan</strong></p>
<p>A naive way to use binary search to find the first and the last position of a target is to first determine the index of <strong>any</strong> occurrence of the given target. Suppose we know that the target is at the index <code>i</code> in the array. From there on, we do a linear scan to the left and keep going until we find the first occurrence of this target. Similarly, we do a linear scan to the right to find the last position. This works just fine. However, in the worst case when our entire array (or say 90% or more of it) is filled with the target, then this is a linear-time algorithm. In that case, the linear scan will end up taking more time than the binary-search itself.</p>
<p><strong>Two Binary Searches</strong></p>
<p>Instead of using a linear-scan approach to find the boundaries once the target has been found, let's use two binary searches to find the first and last position of the target. We can make a small tweak to the checks we perform on the middle element.  This tweak will help us determine the first and the last position of an element</p>
<p>Normally, we compare <code>nums[mid] == target</code> because we simply need to check if we found our target or not. But now, apart from checking for equality, we also need to check if <code>mid</code> is the first or the last index where the target occurs. Let's see how we can do that. </p>
<p><strong>First position in the array</strong></p>
<p>There are two situations where an index will be the first occurrence of the target in the array.</p>
<ol>
<li>If <code>mid</code> is the same as <code>begin</code> which implies our <code>mid</code> element is the <em>first</em> element in the remaining subarray.</li>
<li>The element to the left of this index is not equal to the target that we are searching for. I.e. <code>nums[mid - 1] != target</code>. If this condition is not met, we should keep searching on the left side of the array for the first occurrence of the target. </li>
</ol>
<p>Let's take a look at an example depicting this idea. In the example below, we are searching for the first occurrence of the number <code>7</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/34/img1.png" alt="Example for finding the first position of a target" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 1. Find the first position of "7" in the array.</em>
&#123;:align="center"&#125;</p>
<p>Initially, the variables <code>begin</code> and <code>end</code> are <code>0</code> and <code>5</code> respectively. So, our <code>mid</code> element is <code>(0 + 5) / 2 = 2</code>. </p>
<p><img src="https://leetcode.com/articles/Figures/34/img2.png" alt="Middle element not the first occurrence" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 2. The middle element is a match but it is not the first occurrence.</em>
&#123;:align="center"&#125;</p>
<p>Now, <code>begin</code> is still <code>0</code> but <code>end</code> has moved to <code>mid - 1 = 1</code>. Now we have narrowed our search down to the first two elements of the array. Our updated <code>mid</code> is <code>(0 + 1) / 2 = 0</code>. This element is lower than the target we are looking for <code>2 < 7</code>. So, we discard the "left" side of this subarray and update <code>begin = mid + 1</code>.  This leaves us with a single index, which is in fact the first occurrence of the element "7".</p>
<p><strong>Last position in the array</strong></p>
<p>There are two situations where an index will be the last occurrence of the target in the array.</p>
<ol>
<li>If <code>mid</code> is the same as <code>end</code> which implies our <code>mid</code> element is the <em>last</em> element of the remaining subarray.</li>
<li>If the element to the right of <code>mid</code> is not equal to the target we are searching for. I.e. <code>nums[mid + 1] != target</code>. If this condition is not met, we should keep searching on the right side of the array for the last occurrence of the target. </li>
</ol>
<p>Let's take a look at an example depicting this idea. In the example below, we are searching for the last occurrence of the number <code>7</code>.</p>
<p><img src="https://leetcode.com/articles/Figures/34/img3.png" alt="Example for finding the last position of an element" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 3. Find the last position of "7" in the array.</em>
&#123;:align="center"&#125;</p>
<p>Initially, the variables <code>begin</code> and <code>end</code> are <code>0</code> and <code>5</code> respectively. So, our <code>mid</code> element is <code>(0 + 5) / 2 = 2</code>. </p>
<p><img src="https://leetcode.com/articles/Figures/34/img4.png" alt="Middle element not the last occurrence" referrerpolicy="no-referrer">
&#123;:align="center"&#125;</p>
<p><em>Figure 4. The middle element is not a match.</em>
&#123;:align="center"&#125;</p>
<p>The updated <code>mid</code> is greater than "7". So, we discard the right side of the array.  This leaves us with just a single element in the array which is "7" and it is also the last occurrence.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Define a function called <code>findBound</code> which takes three arguments: the <code>array</code>, the <code>target</code> to search for, and a boolean value <code>isFirst</code> which indicates if we are trying to find the first or the last occurrence of <code>target</code>.</li>
<li>We use 2 variables to keep track of the subarray that we are scanning. Let's call them <code>begin</code> and <code>end</code>. Initially, <code>begin</code> is set to <code>0</code> and <code>end</code> is set to the last index of the array.</li>
<li>We iterate until <code>begin</code> is greater than or equal to <code>end</code>.</li>
<li>At each step, we calculate the middle element <code>mid = (begin + end) / 2</code>. We use the value of the middle element to decide which half of the array we need to search. <ul>
<li><em>nums[mid] == target</em><ul>
<li><em>isFirst is true</em> ~ This implies that we are trying to find the first occurrence of the element. If <code>mid == begin</code> or <code>nums[mid - 1] != target</code>, then we return <code>mid</code> as the first occurrence of the <code>target</code>. Otherwise, we update <code>end = mid - 1</code></li>
<li><em>isFirst is false</em> ~ This implies we are trying to find the last occurrence of the element. If <code>mid == end</code> or <code>nums[mid + 1] != target</code>, then we return <code>mid</code> as the last occurrence of the <code>target</code>. Otherwise, we update <code>begin = mid + 1</code></li></ul></li>
<li><em>nums[mid] > target</em> ~ We update <code>end = mid - 1</code> since we must discard the right side of the array as the middle element is greater than <code>target</code>.</li>
<li><em>nums[mid] < target</em> ~ We update <code>begin = mid + 1</code> since we must discard the left side of the array as the middle element is less than <code>target</code>.</li></ul></li>
<li>We return a value of <code>-1</code> at the end of our function which indicates that <code>target</code> was not found in the array.</li>
<li>In the main <code>searchRange</code> function, we first call <code>findBound</code> with <code>isFirst</code> set to <code>true</code>. If this value is <code>-1</code>, we can simply return <code>[-1, -1]</code>. Otherwise, we call <code>findBound</code> with <code>isFirst</code> set to false to get the last occurrence and then return the result.</li>
</ol>
<p><strong>Implementation</strong></p>
<pre><code class="java language-java">class Solution &#123;
    public int[] searchRange(int[] nums, int target) &#123;

        int firstOccurrence = this.findBound(nums, target, true);

        if (firstOccurrence == -1) &#123;
            return new int[]&#123;-1, -1&#125;;
        &#125;

        int lastOccurrence = this.findBound(nums, target, false);

        return new int[]&#123;firstOccurrence, lastOccurrence&#125;;
    &#125;

    private int findBound(int[] nums, int target, boolean isFirst) &#123;
        int N = nums.length;
        int begin = 0, end = N - 1;

        while (begin <= end) &#123;

            int mid = (begin + end) / 2;

            if (nums[mid] == target) &#123;

                if (isFirst) &#123;

                    // This means we found our lower bound.
                    if (mid == begin || nums[mid - 1] != target) &#123;
                        return mid;
                    &#125;

                    // Search on the left side for the bound.
                    end = mid - 1;

                &#125; else &#123;

                    // This means we found our upper bound.
                    if (mid == end || nums[mid + 1] != target) &#123;
                        return mid;
                    &#125;

                    // Search on the right side for the bound.
                    begin = mid + 1;
                &#125;

            &#125; else if (nums[mid] > target) &#123;
                end = mid - 1;
            &#125; else &#123;
                begin = mid + 1;
            &#125;
        &#125;

        return -1;
    &#125;
&#125;
</code></pre>
<pre><code class="python3 language-python3">class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]

        upper_bound = self.findBound(nums, target, False)

        return [lower_bound, upper_bound]

    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:

        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)    

            if nums[mid] == target:

                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:

                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid

                    # Search on the right side for the bound.
                    begin = mid + 1

            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1

        return -1
</code></pre>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li><p>Time Complexity: $$O(\text&#123;log&#125; N)$$ considering there are $$N$$ elements in the array. This is because binary search takes logarithmic time to scan an array of $$N$$ elements. Why? Because at each step we discard half of the array we are scanning and hence, we're done after a logarithmic number of steps. We simply perform binary search twice in this case.</p></li>
<li><p>Space Complexity: $$O(1)$$ since we only use space for a few variables and our result array, all of which require constant space.</p></li>
</ul>  
</div>
            